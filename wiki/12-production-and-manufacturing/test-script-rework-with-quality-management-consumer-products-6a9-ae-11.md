---
id: 12-production-and-manufacturing/test-script-rework-with-quality-management-consumer-products-6a9-ae-11
title: "Test Script: Rework with Quality Management – Consumer Products (6A9_AE) (6A9_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 6A9 (AE): rework of production orders with QM, covering in-production and post-goods-receipt rework."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/rework-processing]
aliases: [6A9_S4CLD2608_BPD_EN_AE]
keywords: [Rework Processing, rework production orders, quality inspection, usage decision, inspection lots, partial confirmation, blocked stock, production order confirmation, event-based production costs, batch traceability]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6A9_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1155
topic: 12-production-and-manufacturing/rework-processing
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Rework with Quality Management – Consumer Products (6A9_AE) (6A9_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6A9_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Rework Processing** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Rework with Quality Management – Consumer Products (6A9_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 4](#_Toc232857633)

[2 Prerequisites 5](#_Toc232857634)

[2.1 System Access 5](#_Toc232857635)

[2.2 Roles 5](#_Toc232857636)

[2.3 Master Data, Organizational Data, and Other Data 6](#_Toc232857637)

[2.4 Business Conditions 9](#_Toc232857638)

[2.5 Preliminary Steps 10](#_Toc232857639)

[2.5.1 Assign Reference Operation Set and Order Type to Routing 10](#_Toc232857640)

[2.5.2 Adopt Routing for Packed Roasted Coffee Beans 11](#_Toc232857641)

[2.5.3 Create Inspection Plan for Finished Materials 14](#_Toc232857642)

[2.5.4 Create Initial Material Stock 15](#_Toc232857643)

[3 Overview Table 17](#_Toc232857644)

[4 Test Procedures 22](#_Toc232857645)

[4.1 Rework Production Orders within Production Execution 22](#_Toc232857646)

[4.1.1 Create Planned Independent Requirements 22](#_Toc232857647)

[4.1.2 Material Requirements Planning at Plant Level 24](#_Toc232857648)

[4.1.3 Evaluate Stock/Requirements Situation (Optional) 26](#_Toc232857649)

[4.1.4 Convert Planned Orders to Production Orders 28](#_Toc232857650)

[4.1.5 Production Order Processing 29](#_Toc232857651)

[4.1.5.1 Execute Material Staging 29](#_Toc232857652)

[4.1.5.2 Release Production Order 31](#_Toc232857653)

[4.1.5.3 Goods Issue of Batch-Managed Raw Materials via Pick List 33](#_Toc232857654)

[4.1.6 Quality Management - Overview Inspection Lots 34](#_Toc232857655)

[4.1.6.1 Display Open Inspection Lots 34](#_Toc232857656)

[4.1.7 Quality Inspection - within Production (Roasting) 36](#_Toc232857657)

[4.1.7.1 Display Routing for Inspection Characteristics 36](#_Toc232857658)

[4.1.7.2 Display Quality Technician Overview (Optional) 38](#_Toc232857659)

[4.1.7.3 Display Open Inspection Lots (Optional) 38](#_Toc232857660)

[4.1.7.4 Execute Quality Inspection with Inspection Points for Operation Roasting 40](#_Toc232857661)

[4.1.7.5 Display Inspection Results History (Optional) 42](#_Toc232857662)

[4.1.8 Production Order Confirmation of Roasting and Cooling Process 43](#_Toc232857663)

[4.1.8.1 Confirm Production for Operation Roasting 43](#_Toc232857664)

[4.1.8.2 Confirm Production for Operation Cooling 44](#_Toc232857665)

[4.1.8.3 Monitor Order Progress (Optional) 46](#_Toc232857666)

[4.1.9 Quality Inspection - Early Goods Receipt Inspection/End-Product-Control (Before Goods Receipt) 47](#_Toc232857667)

[4.1.9.1 Display Inspection Plan for Inspection Characteristics 47](#_Toc232857668)

[4.1.9.2 Display Quality Technician Overview (Optional) 48](#_Toc232857669)

[4.1.9.3 Display Open Inspection Lots (Optional) 49](#_Toc232857670)

[4.1.9.4 Record Inspection Results (Before Goods Receipt) 51](#_Toc232857671)

[4.1.9.5 Display Inspection Results History (Optional) 53](#_Toc232857672)

[4.1.10 Quality Inspection - In-Process Control (Operation Packaging) 54](#_Toc232857673)

[4.1.10.1 Record Inspection Results (Hierarchical Worklist) 54](#_Toc232857674)

[4.1.11 Execute Partial Production Order Confirmation for Operation Packaging 56](#_Toc232857675)

[4.1.12 Adopt and Release Rework Order 58](#_Toc232857676)

[4.1.13 Confirm Rework Production Order 60](#_Toc232857677)

[4.1.14 Quality Inspection - In-Process Control (Operation Packaging) and Usage Decision 61](#_Toc232857678)

[4.1.14.1 Record Inspection Results (Hierarchical Worklist) 61](#_Toc232857679)

[4.1.14.2 Display Inspection Results History (Optional) 63](#_Toc232857680)

[4.1.14.3 Display Quality Engineer Overview (Optional) 64](#_Toc232857681)

[4.1.14.4 Make Usage Decision 66](#_Toc232857682)

[4.1.15 Confirm Original Production Order for Operation Packaging 67](#_Toc232857683)

[4.1.16 Post Goods Receipt for Production Order 69](#_Toc232857684)

[4.1.17 Cost Analysis of Original and Rework Production Orders 70](#_Toc232857685)

[4.1.17.1 Analyze Event-Based Production Costs 70](#_Toc232857686)

[4.1.17.2 Analyze Event-Based Production Variances (Optional) 71](#_Toc232857687)

[4.2 Rework Production Order of Stock Manufactured Material with Quality Management 72](#_Toc232857688)

[4.2.1 Create Stock for material FG0502 72](#_Toc232857689)

[4.2.1.1 Option 1: Execute complete Production Process for Material FG0502 72](#_Toc232857690)

[4.2.1.2 Option 2: Create Initial Material Stock 73](#_Toc232857691)

[4.2.2 Create and Release Rework Production Order 74](#_Toc232857692)

[4.2.3 Transfer Rework Material from Blocked to Unrestricted Use Stock 75](#_Toc232857693)

[4.2.4 Goods Issue for Defective Materials 76](#_Toc232857694)

[4.2.5 Confirmation of Rework Production Activities 77](#_Toc232857695)

[4.2.6 Manage Production Operations 79](#_Toc232857696)

[4.2.7 Post Goods Receipt for Rework Production Order 80](#_Toc232857697)

[4.2.8 Event-Based Production Cost Overview 81](#_Toc232857698)

[4.2.9 Quality Inspection of Reworked Material 83](#_Toc232857699)

[4.2.9.1 Display Material Stock Before Quality Inspection (Optional) 83](#_Toc232857700)

[4.2.9.2 Display Inspection Plan for Inspection Characteristics (Optional) 84](#_Toc232857701)

[4.2.9.3 Display Quality Technician Overview (Optional) 85](#_Toc232857702)

[4.2.9.4 Display Open Inspection Lots 86](#_Toc232857703)

[4.2.9.5 Record Inspection Results (Hierarchical Worklist) 87](#_Toc232857704)

[4.2.9.6 Display Quality Engineer Overview (Optional) 89](#_Toc232857705)

[4.2.9.7 Make Usage Decision 90](#_Toc232857706)

[4.2.9.8 Display Material Stock After Usage Decision 92](#_Toc232857707)

[4.3 Evaluations 93](#_Toc232857708)

[4.3.1 Batch Information Cockpit - Top-Down and Bottom-Up Analysis 93](#_Toc232857709)

[5 Appendix 95](#_Toc232857710)

[5.1 Process Integration 95](#_Toc232857711)

[5.2 Preceding Processes 95](#_Toc232857712)

[5.3 Succeeding Processes 95](#_Toc232857713)

## Purpose

Overview

This scope item describes two rework processes:

Rework Process 1: This rework process focuses on rework activities and material postings during production execution for the original material. Quality Management identifies deviation from the specification. The original production order is only partly confirmed, another part is booked to be relevant for rework. The result is the automatic creation of a rework production order via a trigger point.

Rework Process 2: This rework process focuses on rework activities after goods receipt for the product from production order. During goods receipt for the product, quality issues are identified and the usage decision fails. The products are booked into inventory, but the failed part is posted to blocked stock (not to unrestricted use). The products booked to blocked stock are subject to rework activities to overcome the defect. After rework, is finished the material is again subject to quality inspection to check successful rework processing.

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
| Production Engineer - Discrete Manufacturing | SAP_BR_PRODN_ENG_DISC | Production Engineering - Discrete Manufacturing | SAP_BR_PRODN_ENG_DISC |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Production Planner | SAP_BR_PRODN_PLNR | Production Planning | SAP_BR_PRODN_PLNR |  |
| Production Supervisor - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC | Production Management - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC |  |
| Production Operator - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC | Production Execution - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC |  |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |
| Quality Planner | SAP_BR_QUALITY_PLANNER | Quality Planning | SAP_BR_QUALITY_PLANNER |  |
| Quality Engineer | SAP_BR_QUALITY_ENGINEER | Quality Engineering | SAP_BR_QUALITY_ENGINEER |  |
| Quality Technician | SAP_BR_QUALITY_TECHNICIAN | Quality Inspection | SAP_BR_QUALITY_TECHNICIAN |  |
| Cost Accountant - Production | SAP_BR_PRODN_ACCOUNTANT | Product Costing | SAP_BR_PRODN_ACCOUNTANT |  |
| BOM Engineer | SAP_BR_BOM_ENGINEER | Bills Of Material | SAP_BR_BOM_ENGINEER |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

This scope item requires new master data set to be created and the needed master data objects are mentioned below:

Material Master Data

| Data | Sample Value | Description | Other Attributes |
| --- | --- | --- | --- |
| Material | FG0502 | Display Med + Dark 48 * 1kg Arabica | Batch Managed Finished Material, MTS, QM, Manufacturing Date |
| Material | FG0511 | Carton 12 x 1kg Bags Medium Beans Arabica | Batch Managed Finished Material, MTS with Maximum Lot Size, QM |
| Material | PK0501 | Coffee Bag "Medium" 1 kg | Batch Managed Packaging Material, MRP and Costing Relevant |
| Material | PK0504 | Label (Batch) | Batch Managed Packaging Material, MRP and Costing Relevant |
| Material | PK0507 | Carton for 12 x 1kg Bags | Packaging Material, MRP and Costing Relevant |
| Material | PK0508 | Display Carton Coffee Beans 48 x 1 kg | Packaging Material, MRP and Costing Relevant, no Batch |
| Material | RM0501 | Raw Coffee Beans- Arabica | Batch Managed Raw Material |

Organization Data

| Data | Sample Value | Description | Other Attributes |
| --- | --- | --- | --- |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Storage Location | 331B | Std. storage 2 |  |
| Storage Location | 331C | Raw mat. stoloc. |  |
| Controlling Area | A000 | Controlling Area A000 |  |
| Cost center | 33101301 | Manufacturing 1 (AE) |  |

Bill of Material Structure

| Material | Level | Material Type | Unit | Characteristics of Material | Component Quantity | Component UOM |
| --- | --- | --- | --- | --- | --- | --- |
| FG0502 | 0 | FERT | PC | Finished Good for MTS processing with Batch Management | 1 | PC |
| FG0502 | 1 | FERT | PC | Finished Material, Batch Managed, QM, MTS | 1 | PC |

| Material | Level | Material Type | Unit | Characteristics of Material | Component Quantity | Component UOM |
| --- | --- | --- | --- | --- | --- | --- |
| FG0511 | 1 | FERT | PC | Finished Material, Batch Managed, QM, MTS | 120 | PC |
| PK0501 | 2 | VERP | PC | Packaging Material, Batch Managed, External Procurement | 120 | PC |
| PK0504 | 2 | VERP | PC | Label | 10 | PC |
| PK0507 | 2 | VERP | PC | Packaging Material | 10 | PC |
| RM0501 | 2 | RAW | PC | Raw Material, Batch Managed, External Procurement | 138 | KG |

Work Center

| Work Center | Plant | Work Center Category | Work Center Description |
| --- | --- | --- | --- |
| DP050001 | 3310 | 0001 | Display Packaging 1 |
| DR050001 | 3310 | 0001 | Drum Roasting Machine 1 |
| PM050001 | 3310 | 0001 | Packaging Machine 1 |
| CS050001 | 3310 | 0001 | Cooling Sieve 1 |
| RW050001 | 3310 | 0003 | Manual Rework |

Quality Master Inspection Characteristics

| Master data | Value | Plant | Master. data details | Comments |
| --- | --- | --- | --- | --- |
| Master Inspection Characteristic | YQM00001 | 3310 | Roast Color (Medium) |  |
| Master Inspection Characteristic | YQM00002 | 3310 | Roast Color (Dark) |  |
| Master Inspection Characteristic | YQM00003 | 3310 | Temperature |  |
| Master Inspection Characteristic | YQM00004 | 3310 | Weight |  |
| Master Inspection Characteristic | YQM00005 | 3310 | Sensory |  |
| Master Inspection Characteristic | YQM00006 | 3310 | Relative Humidity |  |
| Master Inspection Characteristic | YQM00007 | 3310 | Rebrand |  |

For more information on creating your own master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNR | Create Product Master of type "Raw Material" - MDS |
| 3Y1 | Create Product Master of Type "Packaging" - MDS |
| BNT | Create Product Master of type "Finished Good" - MDS |
| BNJ | Create Production Work Center - MDS |
| BNK | Create Material BOM for Production and Sales - MDS |
| BNL | Create Routing - MDS |
| BLD | Create Production Version - MDS |
| BNQ | Create Quality Inspection Plan - MDS |
| BNY | Create Quality Management Attributes for Material/Product Master - MDS |
| 2ZW | Create Batch Management Master Data - MDS |

### Business Conditions

Before this scope item can be tested, the following business condition must be met.

| Scope Item | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS (BNZ) master data script. Posting Period is up to date. |
| BNY - Create Quality Management Attributes for Material/Product Master - MDS | Inspection type 03 and 04 are already provided for all relevant materials. |
| BNU - Create Costing Run - MDS | Complete all steps in the test script.Note Before executing the costing run, please ensure that the production version 0001 is maintained in the costing view for material FG0502. Therefore, logon as BOM Engineer and choose app Change Material (MM02). Enter material FG0502 and choose Continue. On the Select View(s) pop-up, select Costing 1 and choose Continue (Enter). On the Organization Levels pop-up, enter plant 3310 and choose Continue (Enter). Check if production version 0001 is maintained. If not, make the entry and choose Save. |

### Preliminary Steps

#### Assign Reference Operation Set and Order Type to Routing

Purpose

This process step shows you how to assign the reference operation set to any routing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Engineer - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Routing (CA02). | The Change Routing: Initial Screen displays. |  |
| 3 | Enter Details | Make the following entries and press Enter:Material: FG0511Plant: 3310Group: 43300515Group counter: 01 | The Change Routing: Operation Overview screen displays. |  |
| 4 | Turn to Trigger Point Overview | Select operation number 0030 and choose Menu > GoTo > Trigger point overview . | The Change Routing: Operation Trigger Points screen displays. |  |
| 5 | Enter Trigger Point | Make the following entries and choose Enter.Trigger point usage: 00004Description: Rework due to weight issueIndicator: Functions: Set |  |  |
| 6 | Turn to Trigger Point Details | Select the row of your trigger point and choose Menu > Details > Trigger point . | The Change Routing: Trigger Point Details screen displays. |  |
| 7 | Enter the Trigger Point Details | Make the following entries and choose Enter.Indicator: Create order with reference: Function: SetSyst. Sts.: PCNFChange: + |  |  |
| 8 | Turn to the Parameters | Mark Create order with reference and choose Parameters. | The Parameters for Function dialog box displays. |  |
| 9 | Enter the Parameters | Make the following entries and choose Enter:Group: 43305001Group Counter: 1Order Type: YRW1 |  |  |
| 10 | Save | Select Back and choose Save. | Note If you get the pop up that says Task list data contains errors. Do you still want to save? and has the buttons Yes, No and Cancel, choose Yes and save. |  |

#### Adopt Routing for Packed Roasted Coffee Beans

Purpose

To run through this business scenario, the routing for FG0511 needs to be enhanced with the allocation of components to routing operations other than operation 0010. Moreover relevant QM inspection data must be maintained in the routing headers and operations 0010 and 0030.

Prerequisite

The routings for the semifinished material FG0511 is already available in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Production Engineer - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Routing (CA02). | The Change Routing: Initial Screen is displayed. |  |
| 3 | Enter Allocation Data | On the Change Routing: Initial Screen, make the following entries and choose Continue:Material: FG0511Plant: 3310On the Change Routing: Overview mark the routing with following Group Counter and choose button Allocation:GrC: 1On the Routing Change: Material Component Overview, select the following materials and choose button New Assignment.Material: PK0501, PK0504, PK0507.If the pop up Choose Alternative BOM should appear, select the following BOM and choose OK:Usage: 1Alt BOM: 1On the New Assignment pop up, make the following entries and choose Continue:Activity: 0030Go back to Change Routing: Overview screen. | The allocation of component PK0501, PK0504 and PK0507 to operation 0030 is done.Ignore the warning message. |  |
| 4 | Maintain Header Details | On the Change Routing: Overview view, choose button Header.Define Inspection Points Identifier: Y01 Free Insp.Point (Last Sample is valid) | The Change Routing: Header Details view is displayed. |  |
| 5 | Enter Operation Data (Overview) | Choose Header.On the Change Routing: Header Details view, choose button Operations. | The Change Routing: Operation Overview is displayed. |  |
| 6 | Enter Operation Data (Details) for operation 0010 | On the Change Routing: Operation Overview mark the following Operation and choose button Detail:Operation: 0010 | The Change Routing: Operation Details is displayed. |  |
| 7 | Change Operation Data (Details) | On the Change Routing: Operation Details view, scroll to review the Quality Management: Inspection Points section.Select No ReferenceInsp.point Completion: Automatic valuation based on insp. point definitionChoose Back to return to the Operation Overview view. | Note The Reference influences the inspection point creation in results recording later. |  |
| 8 | Enter Operation Data (Details) for operation 0030 | Repeat steps 5 to 7 for the below operation.Operation: 0030 |  |  |
| 9 | Enter Inspection Characteristics for operation 0010 | Mark the operation line 0010 and choose Inspection Characteristics.Assign Master Inspection Characteristic Roast Color (Medium).Master Inspection Characteristic: YQM00001Sampling Procedure: YFIXFIP1Assign Master Inspection Characteristic Temperature.Master Inspection Characteristic: YQM00003Sampling Procedure: YFIXFIP2Replace Lower and Upper Limit with: 210 - 212 °C.Choose Enter.Choose Back to return to Operations Overview screen. | Master Inspection Characteristics are assigned to the routing. |  |
| 10 | Enter Inspection Characteristics for operation 0030 | Mark the operation line 0030 and choose Inspection Characteristics.Assign Master Inspection Characteristic Weight.Master Inspection Characteristic: YQM00004Sampling Procedure: YFIXFIP3Replace Lower Limit with: 1050 gChoose Enter. | Master Inspection Characteristics are assigned to the routing. |  |
| 11 | Save Your Data | Choose Save. | Your data is saved. |  |

Repeat steps 1 to 11 for following routing: material/plant combination:

| Material | Plant | GrC | Component to be assigned | Assignment to operation (OpAc) |
| --- | --- | --- | --- | --- |
| FG0511 | 3310 | 2 | PK0501PK0504PK0507 | 0030 |

#### Create Inspection Plan for Finished Materials

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Quality Planner. | The Start page appears. |  |
| 2 | Access the SAP Fiori App | Open Create Inspection Plan (QP01) tile. | Create Inspection Plan (Initial view) appears. |  |
| 3 | Enter Data | In the Create Inspection Plan (Initial view), make the following entries:Material: FG0511Plant: 3310Key Date: <today>Choose Continue. | The Create Inspection Plan: Header Details view appears when there is no plan available for the specified material/plant combination.Note If there is a plan available, choose a group from the dialog box and Inspection Plan Create: Task List Overview appears. Choose New Entries to create a new inspection plan. |  |
| 4 | Maintain Header Details | Create Inspection Plan (Header Details) appears. Enter the following data:Usage: Choose from the value help list for usage purpose 5 Goods receiptStatus: Choose from the value help list 4 Released (General)Lot size: Within 1 to 99,999Choose Operations. | Inspection Plan Create: Operation Overview appears. |  |
| 5 | Enter Operation Data (Overview) | On the Inspection Plan Create: Operation Overview view, enter the following:Operation Number: 0010Work Center: QMLABSControl Key: QM01Description: End-Product-ControlMark the operation line item, then choose Operation.Note If the Operation button is not available, choose Menu > Operation . | Create Inspection Plan: Operation Details appears.Note The Control Key influences the planning and processing of inspection operation, for example whether or not inspection characteristics must be maintained for an inspection operation. |  |
| 6 | Operation Data (Details) | On the Create Inspection Plan: Operation Details view, scroll to review the Recording View: single values and summarized result (default view)Choose Back to return to the Operation Overview view. |  |  |
| 7 | Enter Inspection Characteristics | Mark the operation line 0010 and choose Inspection Characteristic.Assign Master Inspection Characteristic Sensory Roasted Beans:Master Inspection Characteristic: YQM00005Sample Procedure: YFIX1Assign Master Inspection Characteristic Relative Humidity and change the tolerances as follows:Master Inspection Characteristic: YQM00006Sample Procedure: YFIX2Replace Upper Limit with: 5%Assign Master Inspection Characteristic RebrandMaster Inspection Characteristic: YQM00007Sample Procedure: YFIX2Replace Lower and Upper Limit with: 14 – 17%Choose Enter. | Master Inspection Characteristics are assigned to inspection plan. |  |
| 8 | Save Your Data | Choose Save. | Your data is saved. |  |

#### Create Initial Material Stock

Purpose

In a real business scenario, initial material stock is usually purchased from external suppliers through standard purchasing or subcontracting processes. For only testing purpose, this process step shows you how to create and post the initial material stock to storage locations directly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Post Goods Movement (MIGO) screen displays. |  |
| 3 | Choose Document Type | Choose Goods Receipt and Other. Select for Init.entry of stBal. 561 without any stock indicator and press Enter. |  |  |
| 4 | Enter Data | In the Detail Data section, make the following entries and press Enter:On the Where tab:Goods Movement Type: 561Plant: 3310Storage Location: 331C for RMXXXX (Raw Materials) materials and PKXXXX (Packaging Materials)On the Quantity tab:Quantity: <Quantity>, for example, <1000> (for RM0501, PK0501, PK0502, PK0507 and PK0504 add for example 40000 PC/kg and for PK0508, for example 5000 PC)On the Material tab:Material: <BOM Material>, refer to section Master Data, Organizational Data, and Other Data for Bill of Material Structure. You must create initial stock for all materials except for FG0511.Ensure that Item OK is selected and choose Next Item to maintain entries for the next material. |  |  |
| 5 | Check | Choose Check. | The document is ready to be posted. |  |
| 6 | Post | Choose Post. | Material document XXX is posted and materials are available in stock. |  |

We recommend that you check stock level for FG0511, FG0512 and FG0502. To do that, log onto the SAP Fiori launchpad as a Production Planner, and open Manage Material Coverage - New Version (F0251A) app. Remove some stock if there is already sufficient amount of stock in store. Otherwise, no planned orders can be generated later. Use Post Goods Movement (MIGO) app with movement type 562 resp. for Init.entry of stBal. 562 without any stock indicator to remove stock and run the test again.

## Overview Table

This scope item consists of several process steps provided in the table below.

If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the home page will only contain the essential apps for performing the typical tasks of a business role.

You can find all other apps not included on the home page using the search bar.

If you want to personalize the home page and include the hidden apps, navigate to your user profile and choose Settings > App Finder.

| Process Step | Business Role | Transaction/App | Expected Output |
| --- | --- | --- | --- |
| Rework Production Orders within Production Execution |  |  |  |
| [Create Planned Independent Requirements](#unique_12) | Production Planner | Maintain PIRs (F3445) | Planned Independent Requirements for Finished Material are created. |
| [Material Requirements Planning at Plant Level](#unique_13) | Production Planner | Schedule MRP Runs (F1339) | Planned Independent Requirements for Finished Materials and also the components are planned. |
| [Evaluate Stock/Requirements Situation (Optional)](#unique_14) | Production Planner | Monitor Material Coverage - Net / Individual Segments (F2101A) | Stock/Requirements situation for the planned materials is analyzed. |
| [Convert Planned Orders to Production Orders](#unique_15) | Production Planner | Manage Material Coverage - New Version (F0251A) | Planned Orders for Finished Materials are converted to Production Orders. |
| Production Order Processing |  |  |  |
| [Execute Material Staging](#unique_16) | Production Operator - Discrete Manufacturing | Stage Materials for Production (MF60) | The components needed for the Finished Material production order are moved from various storage locations to the production storage location. |
| [Release Production Order](#unique_17) | Production Supervisor - Discrete Manufacturing | Manage Production Orders (F2336) | Production order for Finished Material is released. |
| [Goods Issue of Batch-Managed Raw Materials via Pick List](#unique_18) | Production Operator - Discrete Manufacturing | Pick Components for Production Orders (CO27) | Goods movements are posted. |
| Quality Management - Overview Inspection Lots |  |  |  |
| [Display Open Inspection Lots](#unique_19) | Quality Technician | Manage Inspection Lots (F2343) | Inspection lots after release of production order are reviewed. |
| Quality Inspection - within Production (Roasting) |  |  |  |
| [Display Routing for Inspection Characteristics](#unique_20) | Production Engineer - Discrete Manufacturing | Display Routing (CA03) | The routing setup is reviewed. |
| [Display Quality Technician Overview (Optional)](#unique_21) | Quality Technician | Quality Technician Overview (F2361) | An overview of open inspection lots is given. |
| [Display Open Inspection Lots (Optional)](#unique_22) | Quality Technician | Manage Inspection Lots (F2343) | The open inspection lots are checked. |
| [Execute Quality Inspection with Inspection Points for Operation Roasting](#unique_23) | Quality Technician | Record Results for Inspection Points (F2689) | Quality Inspection with Inspection Points is executed. |
| [Display Inspection Results History (Optional)](#unique_24) | Quality Technician | Display Results History (F2428) | Inspection results are reviewed. |
| Production Order Confirmation of Roasting and Cooling Process |  |  |  |
| [Confirm Production for Operation Roasting](#unique_25) | Production Operator - Discrete Manufacturing | Confirm Production Operation (F3069) | Production Order Operation 0010 is confirmed. |
| [Confirm Production for Operation Cooling](#unique_26) | Production Operator - Discrete Manufacturing | Confirm Production Operation (F3069) | Production Order Operation 0020 is confirmed. |
| [Monitor Order Progress (Optional)](#unique_27) | Production Supervisor - Discrete Manufacturing | Manage Production Orders (F2336) | The production order progress is reviewed. |
| Quality Inspection - Early Goods Receipt Inspection/End-Product-Control (Before Goods Receipt) |  |  |  |
| [Display Inspection Plan for Inspection Characteristics](#unique_28) | Quality Technician | Display Inspection Plan (QP03) | The Inspection Plan is reviewed. |
| [Display Quality Technician Overview (Optional)](#unique_29) | Quality Technician | Quality Technician Overview (F2361) | An overview of open Inspection Lots is given. |
| [Display Open Inspection Lots (Optional)](#unique_30) | Quality Technician | Manage Inspection Lots (F2343) | Open Inspection Lots are reviewed. |
| [Record Inspection Results (Before Goods Receipt)](#unique_31) | Quality Technician | Record Inspection Results (F1685A) | Inspection Results are recorded. |
| [Display Inspection Results History (Optional)](#unique_32) | Quality Technician | Display Results History (F2428) | Inspection Results are reviewed. |
| Quality Inspection - In-Process Control (Operation Packaging) |  |  |  |
| [Record Inspection Results (Hierarchical Worklist)](#unique_33) | Quality Technician | Record Inspection Results - Hierarchical Worklist (QE51N) | Inspection Results are recorded. |
| [Execute Partial Production Order Confirmation for Operation Packaging](#unique_34) | Production Operator - Discrete Manufacturing | Confirm Production Operation (F3069) | The operation 0030 of the production order is partly confirmed and rework order is triggered due to partial confirmation status. |
| [Adopt and Release Rework Order](#unique_35) | Production Supervisor - Discrete Manufacturing | Monitor Production / Planned Orders (COOIS) | The rework production order is adopted and the cost assignments for rework order and ooriginal order are reviewed. |
| [Confirm Rework Production Order](#unique_36) | Production Operator - Discrete Manufacturing | Confirm Production Operation (F3069) | The rework production order is confirmed and components and activities are posted. |
| Quality Inspection - In-Process Control (Operation Packaging) and Usage Decision |  |  |  |
| [Record Inspection Results (Hierarchical Worklist)](#unique_37) | Quality Technician | Record Inspection Results - Hierarchical Worklist (QE51N) | Inspection results are recorded. |
| [Display Inspection Results History (Optional)](#unique_38) | Quality Engineer | Display Results History (F2428) | Inspection Results are reviewed. |
| [Display Quality Engineer Overview (Optional)](#unique_39) | Quality Engineer | Quality Engineer Overview (F2360) | The Inspection lots without Usage Decision are displayed. |
| [Make Usage Decision](#unique_40) | Quality Engineer | Manage Usage Decisions (F2345) | Usage Decision is made. |
| [Confirm Original Production Order for Operation Packaging](#unique_41) | Production Operator - Discrete Manufacturing | Confirm Production Operation (F3069) | The original production order is finally confirmed. |
| [Post Goods Receipt for Original Production Order](#unique_42) | Warehouse Clerk | Post Goods Receipt for Production Order (F3110) | The goods receipt for the production order is posted. |
| Cost Analysis of Original and Rework Production Orders |  |  |  |
| [Analyze Event-Based Production Costs](#unique_43) | Cost Accountant - Production | Analyze Production Costs - Event-Based (F4059) | The product costs are analyzed in real time. |
| [Analyze Event-Based Order Costs](#unique_44) | Cost Accountant - Production | Order Cost Details - Event-Based (F4254) | The analysis of event-based orders is executed. |
| Rework Production Order of Stock Manufactured Material with Quality Management |  |  |  |
| Create Stock for Material FG0502 |  |  |  |
| [Option 1: Execute complete Production Process for Material FG0502](#unique_45) | Various | Various | Stock for material FG0502 is available either in unrestriced or blocked stock. |
| [Option 2: Create Initial Material Stock](#unique_46) | Warehouse Clerk | Post Goods Movement (MIGO) | Initial stock is posted. |
| [Create and Release Rework Production Order](#unique_47) | Production Supervisor - Discrete Manufacturing | Create Production Order (CO01) | A rework production order is created. |
| [Transfer Rework Material from Blocked to Unrestricted Use Stock](#unique_48) | Warehouse Clerk | Post Goods Movement (MIGO) | The stock is moved from blocked to unrestricted use stock. |
| [Goods Issue for Defective Materials](#unique_49) | Warehouse Clerk | Post Goods Movement (MIGO) | The goods issue of defective material is posted. |
| [Confirmation of Rework Production Activities](#unique_50) | Production Operator - Discrete Manufacturing | Confirm Production Operation (F3069) | The rework activities are posted. |
| [Manage Production Operations](#unique_51) | Production Supervisor - Discrete Manufacturing | Manage Production Operations (F2335) | Review production order after release / confirmation is performend. |
| [Post Goods Receipt for Rework Production Order](#unique_52) | Warehouse Clerk | Post Goods Movement (MIGO) | The goods receipt for production order is posted. |
| [Event-Based Production Cost Overview](#unique_53) | Cost Accountant - Production | Production Cost Overview - Event-Based (F6248) | The event-based production cost overview is reviewed. |
| Quality Inspection of Reworked Material |  |  |  |
| [Display Material Stock before Quality Inspection (Optional)](#unique_54) | Inventory Manager | Stock - Single Material (F1076) | Stock Situation is reviewed. |
| [Display Inspection Plan for Inspection Characteristics (Optional)](#unique_55) | Quality Technician | Display Inspection Plan (QP03) | The inspection plan setup is reviewed. |
| [Display Quality Technician Overview (Optional)](#unique_56) | Quality Technician | Quality Technician Overview (F2361) | An overview of open inspection lots is given. |
| [Display Open Inspection Lots](#unique_57) | Quality Technician | Manage Inspection Lots (F2343) | Open Inspection Lots are checked. |
| [Record Inspection Results (Hierarchical Worklist)](#unique_58) | Quality Technician | Record Inspection Results - Hierarchical Worklist (QE51N) | Inspection results are recorded. |
| [Display Quality Engineer Overview (Optional)](#unique_59) | Quality Engineer | Quality Engineer Overview (F2360) | Inspection results without Usage Decision are reviewed. |
| [Make Usage Decision](#unique_60) | Quality Engineer | Manage Usage Decisions (F2345) | Usage Decision is executed. |
| [Display Material Stock after Usage Decision](#unique_61) | Warehouse Clerk | Stock - Single Material (F1076) | Stock Situation is reviewed. |
| Evaluations |  |  |  |
| [Batch Information Cockpit - Top Down and Bottom-Up Analysis](#unique_62) | Quality Technician | Batch Information Cockpit (BMBC) | The batch traceability is executed. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Rework Production Orders within Production Execution

This rework process focuses on rework activities and material postings during production execution for the original material before goods receipt for the product. Issues with the produced material are monitored before it is posted to inventory.

#### Create Planned Independent Requirements

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create Planned Independent Requirements (PIRs). PIRs are used to perform demand management functions. A planned independent requirement contains one planned quantity and one date, or a number of planned independent requirements schedule lines, such as one planned quantity split according to dates.

|  |
| --- |
| Note Instead of creating a single requirement, sometimes one or more planned independent requirements can be maintained and included in a requirement plan for mass processing. In this case, the requirements are grouped and maintained under a requirement plan number. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Planner. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Maintain PIRs (F3445). | The Maintain PIRs screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, choose Area of Responsibility.On My Area of Responsibility screen, check if the below entry is assigned:Plant 1 AE (3310)MRP Controller 001 (001)Choose AOR Status if the status for the above entry is not yet assigned.Choose AOR Status to unassign the rest of other entries. |  |  |
| 4 | Select Material Items | On the Maintain PIRs screen, make the following entries and choose Go:Plant: 3310Period Indicator: Weekly(W)Version Active: Select all optionsMaterial: FG0511 | The searched material item displays. If the material filter is not directly available choose Adapt Filters, select the Material Filter, enter the desired material and choose OK.Note If no PIRs for FG0511 have been maintained in the system before, the selection is empty in the app. In that case please leave this app and access the app Create PIRs (MD61), make the following entries on the Create Planned Independent Requirements: Initial Screen and choose Continue:Plant: 3310Period Indicator: Weekly (W)Version: 00Material: FG0511Choose Save and restart with step 1. |  |
| 5 | Edit PIRs | Select the material item and choose Edit in the upper right corner of the screen.On the Edit PIRs screen, enter quantities per week, for example:Week 1 (current week + 1 week): 40 PCWeek 2 (current week + 2 weeks): 80 PCWeek 3 (current week + 3 weeks): 80 PCWeek 4 (current week + 4 weeks): 100 PCWeek 5 (current week + 5 weeks): 80 PCWeek 6 (current week + 6 weeks): 80 PCVersion is Active: YES | Note If already stock for FG0511 is available, increase the quantity for PIR of current week + 1 for the stock already available. As an alternative, remove the stock to get planned orders in next step. |  |
| 6 | Save PIR's Draft | Choose Save in the bottom right corner of the screen. | The PIRs draft is saved. |  |

#### Material Requirements Planning at Plant Level

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to use Material Requirement Planning (MRP) to tailor available capacities and receipts on time to suit requirement quantities. As a result, single-item multi-level requirement planning is performed for plant 3310.

Prerequisite

The Make-to-Stock finished goods are planned at plant level. There is now a requirement for FG0511 in plant 3310.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Planner. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Schedule MRP Runs (F1339). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create.On the New Job screen, make the following entries:For 1. Template Selection section:Job Template: Material Requirements Planning (MRP)Job Name: MRP for FG0511Choose Step 2.For 2. Scheduling Options section:Start Immediately: <select>Choose Define Recurrence Pattern.On the Scheduling Information screen, make the following entries:Start Immediately: XRecurrence Pattern: Single RunChoose OK.Choose Step 3.For 3. Parameters section:Plant: 3310Material: FG0511Changed BOM Components: selectStock Transfer Materials: selectScheduling: 2Planning Mode: 1Choose Check at the bottom right.Choose Schedule. | A message appears: You can go ahead and schedule the job. |  |
| 4 | Refresh Application Jobs List | To check the job’s status, enter MRP for FG0511 in the search box and choose Go at the top right section of the screen. | The new job is created and is displayed in the Application Jobs table when refreshed. |  |

#### Evaluate Stock/Requirements Situation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display the stock/requirements situation for Make-to-Stock finished goods (FG0511) and the components relevant for production (packaging and raw materials) in the stock/requirements list after the requirement planning is performed.

Prerequisite

Requirement planning is carried out.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). | The Monitor Material Coverage - Net / Individual Segments (F2101A) screen displays. |  |
| 3 | Check Area of Responsibility | Choose the user icon and select App Settings. In the MRP Settings dialog box, choose Area of Responsibility.Check if only this entry displays, and choose OK:Plant 1 AE 3310MRP Controller (001)Choose + to select this entry if not displayed; choose the Delete icon to remove any other plant entries and then choose OK. |  |  |
| 4 | Select Material | Search in the Material bar, select the following materials and then choose Go.Material: FG0511Material: PK0501Material: PK0504Material: PK0507Material: RM0501 | The Material and Material Details subscreens display. |  |
| 5 | Review Stock / Requirements List | Select the following materials on the Material screen and choose Manage Materials.Material: FG0511 | The detailed stock / requirements list for each material displays. |  |
| 6 | Display Planned Order | On the Material Details subscreen, choose PldOrd XXX in the MRP Element column.Note The BOM explosion during the MRP run has generated dependent requirements for the demand-driven planned components. If there is not enough inventory to fulfill the requirements, planned orders and purchase requisitions are created for both inhouse-produced and externally-procured materials. | The selected planned order displays.Note The planned order is generated only when there is storage for these materials.If you want to display more information of the planned order, click on Display Planned Order at the bottom right of the dialog box. |  |
| 7 | Rescheduling Check (Optional) | On the Stock/Requirements List tab, the Rescheduling column displays the rescheduling status of the following MRP elements.PurReqPurchase OrdersPlanned OrdersProduction OrdersProcess OrdersIf needed, you can choose the following icons in Rescheduling column for corresponding functions:Reschedule in (bring operation forward if the receipt element lies after the requirement date)Reschedule out (postpone operation, if the receipt element lies before the requirement date)Plan Process according to scheduleCancel ProcessExcess StockExcess in individual segment |  |  |
| 8 | Display Stock situation of Raw and Packaging Materials | Return to the Materials Overview screen, select following materials and choose Manage MaterialsMaterial: PK0501Material: PK0504Material: PK0507Material: RM0501 |  |  |
| 9 | Simulation and solving shortage situations (Optional) | If a shortage situation for components exists, the number in the Available column is marked in red and an arrow is visible next to the amount. Click on that arrow and you will be guided to a simulation section. In this section you get provided different solutions how to overcome the corresponding shortage situation. Choose Simulate in the Actions column to simulate your preferred option. Afterwards, you can either choose Cancel in the Actions column to return to previous planning situation or choose Apply to take over the proposed simulation in the operative Stock/Requirements List. |  |  |

#### Convert Planned Orders to Production Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Daily MRP run creates planned orders for goods to be produced internally. This process step shows you how to convert the planned orders to production orders for finished materials when reached the planned start date.

Prerequisite

The MRP run has generated planned orders for FG0511 (finished material).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Material Coverage - New Version (F0251A). | The Check Material Coverage displays with Find Material dialog box. |  |
| 3 | Select Material | Enter the following data in the Find Material dialog box and choose OK.Material: FG0511Plant: 3310Shortage Definition: MRP Standard | The Manage Material Coverage screen displays. |  |
| 4 | Find Planned Order | Check the generated planned order.If no planned orders are generated, it could be because FG0511 has sufficient amount of stock in store. In this case, remove some stock or enhance the amount for PIRs for FG0511 and run MRP again to generate planned orders. |  |  |
| 5 | Add Planned Order Long Text (Optional) | Click on the planned order number (PldOrd XXX) under column MRP Element. In the quickview screen, choose Open > Planned Order .On the Change Planned Order screen, choose tab Long Text, enter the text and choose Save. | The long text maintained here can be later copied to the the converted production order. |  |
| 6 | Convert Planned Order to Production Order | Select Convert from Edit dropdown list in the Action column for a planned order (PldOrd XXX).In the Convert Planned Order XXX dialog box, choose Convert to Production Order radio button, confirm End Date and Quantity. Choose OK.Choose the Refresh button on the top of the material overview section, scroll to the created production order and note down the production order number for material FG0511. | The production order is created.Production Order Number ___________________. |  |

#### Production Order Processing

##### Execute Material Staging

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to stage materials for finished material production.

|  |
| --- |
| Note If there is sufficient amount of stock available in the production storage location, then no line items are generated. In this case, you can skip this step and proceed onward. |

Prerequisite

Stock must be available.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Stage Materials for Production (MF60). | The Material Staging for Planned Orders screen displays. |  |
| 3 | Enter Details | Make the following entries and choose Execute.In the Staging Types section:SLoc Level: <select>Plant: 3310Selection Horizon for Reqmts: <date must be in the future - after scheduled start date of production order created>On the Production/Process Orders tab:Order: <Production Order Number for Finished Material> | The Pull List: Storage Location Level screen displays. |  |
| 4 | Choose Replenishment Elements | In the Total Reqmts table, select the line items and choose Replenishment Proposal on the top of the screen.Review staged quantities and choose Replenishment Elements. |  |  |
| 5 | Enter Replenishment Storage Location and Stage Material | In the Replen. Element table, in the RepLoc column, enter 331C for staged materials.In the Batch field, select an appropriate batch available in storage location 331C for the corresponding material and press Enter. Select all entries.Choose Stage. |  |  |
| 6 | Save | Save your entries.Missing materials are transferred to the shop floor from the designated storage area.With this step, the shortage of material RM0501, PK0501, PK0504 and PK0507 for the finished production order of FG0511 is supplied. | Materials are staged for production. |  |

##### Release Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to release the order at header level, which releases the entire order and all its operations. The order and the operations receive the REL (released) status.

Prerequisite

The production order created by the MRP controller is assigned a release date in accordance with the scheduling margin key.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Production Orders (F2336). | The Manage Production Order screen displays. |  |
| 3 | Check Default Area of Responsibility (Supervisor) | Choose the user icon and select App Settings. In the Area of Responsibility dialog box, choose Production Supervisor, check if this entry displays and choose OK:Plant 1 AE (3310)MTS DI - Valuated (YB1)Choose + to select this entry if not displayed; choose the Delete icon to remove any other plant entries. Choose OK. |  |  |
| 4 | Select Production Order | On the Manage Production Orders screen, choose Adapt Filters to display more filter options. In the Adapt Filters dialog box, choose More filters. Select Material and Production Plant and choose OK. Choose Go.Enter the following filter criteria, and choose Go:Status: CreatedMaterial: FG0511Production Plant: 3310 | The Material and Production Plant fields are added to filter bar.The searched order displays. |  |
| 5 | Assign Batch Number to Production Order before Order Release | Select the order you want to release and choose Edit.In the Production Order Change header move to the tab Goods Receipt.Either click on the Create button next to the Batch field to create an automatic batch number or enter a batch number in the field Batch manually.Choose Save. Confirm the popup for the creation of a new batch number. | Make a note of the batch number.Batch: __________Note By adopting the customizing settings, an automatic creation of batch number either during production order creation or production order release is possible. |  |
| 6 | Execute Release | Select the searched order once again. Choose Release. |  |  |

Result

The production order is released. With release of the production order, an inspection lot is created for material FG0511 that contains quality inspections for operations 0010 (Roasting) and 0030 (Packaging) which are performed within the production process (In-Process Control).

At the same time, an inspection lot for the goods receipt inspection is created. Thus, the early End Product Control for material FG0511 can be started in parallel to the running production process and before goods receipt for production order is posted.

##### Goods Issue of Batch-Managed Raw Materials via Pick List

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The withdrawal of the raw materials is used for the order. This withdrawal can be done by using the picking list.

|  |
| --- |
| Note If the material is set for backflush (in material master or resource), the withdrawing is done automatically after you confirm the operation or the whole order. Backflushing should not be used for batch-managed components (to ensure that the physically picked and consumed batch is the same as the recorded batch). |

|  |
| --- |
| Note In this scope item the packaging materials PK0501 and PK0504 are (even though it is batch managed) subject to backflush due to process requirements and hence picking will only be executed for RM0501. |

Prerequisites

Ensure that sufficient material is present on stock. If not enough stock is present, execute Create Initial Material Stock in the preliminary steps of this scope item.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori Launchpad displays. |  |
| 2 | Access App | Open Pick Components for Production Orders (CO27). | The Picking List: Initial Screen displays. |  |
| 3 | Enter Restriction and Run | Make the following entries and choose Execute:Profile: 000002Production Order: <Order ID> (from previous steps)Plant: 3310 | The Order Information System: Detail List of Components screen displays. |  |
| 4 | Picking Raw Materials | Select the relevant reservations for RM0501 and choose the upper left Picking. | The Picking list screen displays. On this screen, a list of all the selected reservations is displayed. |  |
| 5 | Batch Determination | RM0501 is managed by batches.You have two options:Manually enter the relevant batch number.Execute a Batch Determination by selecting the line for RM0501 and choose button Batch Determination. The Batch determination result is displayed. You can either do changes in the proposed selection or directly accept the proposal. Choose Copy. The number of line items available now in the Picking list corresponds to the number of selected batches. | Back to Picking list screen.If multiple line items were selected in this step, the Picking list screen is displayed after completion of the last line item. |  |
| 6 | Post | Choose Post to post the goods movements. | The goods movements have been posted. |  |

#### Quality Management - Overview Inspection Lots

In this process step you execute the steps already described in scope item 5HK in order to create a production order with full integrated QM for material FG0511. Some steps are optional ones.

##### Display Open Inspection Lots

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection lots are used to record the results for In-Process Control and the early Goods Receipt Inspection (End-Product Control), In this step, the references to production order are verified as well as the inspection lot quantities, sample sizes and postings can be reviewed.

The early goods receipt inspection can be started after Cooling (operation 0020) and while Packaging (operation 0030). Thus, dependent from capacity in the laboratory, the results recording can be started before goods receipt for production order is done.

Prerequisite

In this scope item, two inspection lots with different inspection lot origins are created automatically upon release of previous production order. Due to material master settings, the goods receipt inspection can be performed early.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Inspection Lots (F2343). | The Manage Inspection Lots (F2343) screen displays. |  |
| 3 | Filter Fields | Make the following entries and choose Go:Plant: 3310Material: FG0511Inspection Lot Status: Outstanding | Alternatively, you can search for the batch <Batch ID> (from previous step). |  |
| 4 | Select the Corresponding Inspection Lot | In the inspection lot list, select the inspection lot with column Production Order equals to the Production Order: <Order ID> (from previous step). | The Production Order number assigned with Inspection lot is displayed.If the Production Order column does not appear, please choose the button Settings. In the View Settings dialog box, select Production Order and choose OK. |  |
| 5 | Check Inspection Lot | Under Inspection Type, check the different inspection types.Under Batch, check the batch from previous step. | Make a note of the inspection lot IDs:Inspection Lot ______________ with inspection type 03 (In-process insp. for production order).Inspection Lot ______________ with inspection type 04 (Goods receipt inspection from production). |  |
| 6 | Check First Inspection Lot by Selecting the Line | In the Origin tab, verify the referenced production order and inspection lot origin. | The production order number from which the inspection lot originates is displayed.Origin: Production |  |
| 7 | Check Inspection Lot Quantities | In the Origin tab, check the Lot Quantities, Sample Size and Postings. | The quantities according to the released production order quantity are displayed. The calculated sample size is displayed. Posting = 0 (not relevant). |  |
| 8 | Check Second Inspection Lot by Selecting the Line | In the Origin tab, verify the referenced production order and inspection lot origin. | The production order number from which the inspection lot originates is displayed.Origin: Goods Receipt from Production |  |
| 9 | Check Inspection Lot Quantities | In the Origin tab, check the Lot Quantities, Sample Size and Postings. | The quantities according to the released production order quantity are displayed. The calculated sample size is displayed. Posting = 0 (not yet started). |  |

#### Quality Inspection - within Production (Roasting)

##### Display Routing for Inspection Characteristics

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

An inspection during production (In-Process Control) is triggered by the release of a production order. When you release the production order, an inspection lot is generated, containing the inspection characteristics for operation 0010 (Roasting) and 0030 (Packaging). This inspection lot offers inspection points for repeating the inspections several times, until the expected results are reached (e.g. roast color of coffee beans). With inspection point Y01 in the routing header, only the last sample is valid for usage decision.

In this step, you display the routing (group counter 1 or 2) that is related to the finished good. The difference between the routings are only different drum roasting lines (Drum Roasting Line 1 and 2) used for production. Regarding quality inspection, it is exactly the same.

The routing defines all inspection characteristics used later in the quality inspection. As well you can review the inspection points definition for operation 0010 and 0030.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Engineer - Discrete Manufacturing. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Display Routing (CA03). | The Display Routing: Initial Screen displays. |  |
| 3a | Enter Selection Fields | Make the following entries and choose Continue.Material: FG0511Plant: 3310 | The Display Routing: Overview displays.There are two routings (Drum Roasting Line 1 and Drum Roasting Line 2) with respective work centers in PP. The QM data remains the same. |  |
| 3b | Select Group Counter | Select Group Counter: e.g. 1 and choose Operations | The Display Routing: Operation Overview displays. |  |
| 4 | Review the Inspection Points Setting (operation 0010) | Double-click Operation 0010.Scroll down to the Quality Management: Inspection Points section.After reviewing, choose Back. | A No Reference inspection point is defined for this operation in the routing.Insp. point Completion is: Automatic valuation based on insp. Point definition |  |
| 5 | Review the Inspection Points Setting (operation 0030) | Repeat step 4.Double-click Operation 0030. |  |  |
| 6 | Review the Inspection Characteristics (operation 0010) | Select Operation 0010 and choose Inspection Characteristics.There are two Master Inspection Characteristics:One is Qualitative - Roast Color (medium) with Inspection MethodColor Check of Roasted Beans.The other is Quantitative - Temperature.For both, sample size 1 is to be inspected. | The Display Routing: Characteristics Overview displays.If Inspection Characteristics is not displayed, choose More. In the dialogue box, find Inspection Characteristics. |  |
| 7 | Review the Inspection Characteristics (operation 0030) | Repeat step 6.Select Operation 0030 and choose Inspection Characteristics.There is one Master Inspection Characteristic, which is Quantitative - Weight with 3 samples to be inspected. | You have now reviewed the inspection characteristics for which results have to be maintained within a later step.The sampling procedure can be displayed in detail with app Display Sampling Procedures (F2255) (optional). |  |

##### Display Quality Technician Overview (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this optional step, you can display an overview of open inspection lots via the overview page for quality technicians.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Quality Technician Overview (F2361). | The Quality Technician Overview (F2361) screen displays.You can get an overview of the inspection lots with open results recording and the inspection lots without an inspection plan.Choose card Inspection Lots with Open Results Recording for Inspection Points if you want to record results for the In-Process Control inspection lot. |  |

##### Display Open Inspection Lots (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The In-Process Control inspection lot is used to record the results during production. In this optional step, the operations and characteristics are reviewed as well as assigned inspection methods with attachments used for quality inspection.

Prerequisite

In this scope item, the inspection lot is created automatically upon release of production order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Inspection Lots (F2343). | The Manage Inspection Lots screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Plant: 3310Material: FG0511Inspection Lot Status: OutstandingInspection Lot Origin: Production | Alternatively, you can search for the batch <Batch ID> (from previous step). |  |
| 4 | Select the corresponding Inspection Lot | In the inspection lot list, select the inspection lot with column Production Order equals to the Production Order: <Order ID> (from previous step) | The Production Order number assigned to Inspection Lot is displayed.If the Production Order column does not appear, please choose the button Settings. In the View Settings dialog box, select Production Order and choose OK.If needed, press button Show Details to make the column visible. |  |
| 5 | Choose Operation (optional) | In Result, choose operation Roasting (Medium). | Inspection Characteristics Roast Color and Temperature can be reviewed with their specifications and calculated sample sizes. |  |
| 6 | Choose Characteristic (optional) | Click Roast Color in the characteristics column. | For checking the attachment in the inspection method:If you have attached a document in the inspection method as described in the Preliminary Steps, the Quality Technician can review the attachment referring to step 6 to 8.A dialog box appears with the Characteristics Details with the link to the Inspection Method. |  |
| 7 | Display the Attachment (optional) | Under Documents, the attachment for an illustration of the Roast Color of coffee beans is displayed. |  |  |
| 8 | Display Text | In General, Long Text is displayed. |  |  |
| 9 | Choose next Operation (optional) | In Result, choose operation Packaging | Inspection Characteristic Weight can be reviewed with its specification and calculated sample size. |  |

##### Execute Quality Inspection with Inspection Points for Operation Roasting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the quality technician performs the quality inspection and records the inspection result(s) for operation 0010 (Roasting) in order to decide whether the next operation of the production order can be executed. The result is recorded in the inspection lot according to the defined inspection parameters in the routing. Here, free inspection points are used for result recording. Leveraging inspection points, you can have several inspections and can record multiple sets of characteristic results for a single operation. Each inspection point is valuated separately with a coded valuation.

Using Inspection point identifier Y01, only the last sample results are valid.

Prerequisite

The inspection is processed based on inspection lot. In this scope item, the inspection lot is automatically created upon release of the production order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access App | Open Record Results for Inspection Points (F2689). | The Record Results for Inspection Points screen displays. |  |
| 3 | Execute Search | If not already shown, expand search header, make the following entries and choose Go:Order: <Order ID>Work Center: DR050001 or DR050002 | Selected Order and Work Centers (Drum Roasting Machine 1 or Drum Roasting Machine 2) are displayed in the result list. |  |
| 4 | Open Inspection Points | Click on the line item of the search result. | A list of inspection points is displayed. If inspection point data have not been captured, continue with step 5. |  |
| 5 | Create New Inspection Point | Click On request to create a new inspection point. | Record Results for Inspection Points screen is displayed. |  |
| 6 | Maintain Inspection Results | Maintain the following inspection results and choose Save.a) Negative ResultRoast Color: 10 – Light brownTemperature:Valuation: Rejected (R) | Inspection point data is saved and the system displays the list of inspection points. |  |
| 7 | Create Next Inspection Point and Maintain Inspection Results (Optional) | Create a new inspection point as described in step 5 and maintain inspection results as follows:a) Negative ResultRoast Color: 20 – Moderate Light brownTemperature:Valuation: Rejected (R) | Further inspection point with inspection results is captured. |  |
| 8 | Create Last Inspection Point and Maintain Inspection Results | Create a new inspection point as described in step 5 and maintain inspection results as follows:a) Positive ResultRoast Color: 30 – Medium shade of brownTemperature:Valuation: Accepted (A) | Last inspection point is recorded. Only last sample is valid.Temperature and Roast Color of coffee beans are reached and roasting process can be finished. |  |

##### Display Inspection Results History (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this optional step, an overview about the history of inspection result is shown. For each quantitative Inspection Characteristic several statistical values and the development for recorded results are illustrated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Display Results History (F2428). | The Results History screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Aggregation Level: Master Inspection Characteristic |  |  |
| 4 | Select Inspection Characteristic | Select an Inspection Characteristic, for example Temperature. | Information is provided about the selected characteristics for process control, for example:A diagram displays the development of the recorded results for this characteristic with lower and upper limit.Statistical Values for Control Chart and Process Capability, for example Mean Value. |  |

#### Production Order Confirmation of Roasting and Cooling Process

##### Confirm Production for Operation Roasting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In the Consumer Products Industry, goods receipt and goods issue postings are usually done immediately during the physical movements of the materials to ensure batch traceability and data consistency. Order confirmations with backflush are done either at shift end or day end. The sum of the GI and GR quantity for the given order is then recorded within the confirmation and scrap quantities (optional). The time ticket confirmation allows recording either the default times for machine and labor usage, or record actual times for major deviations.

Prerequisite

The production order for the finished material FG0511 has been released and material staging has been carried out.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Confirm Production Operation (F3069). | The Enter Order and Operation screen displays. |  |
| 3 | Enter Order Number and Operation | On the Enter Order and Operation screen, make the following entries, and choose Go:Order: <Order ID> (from previous steps)Operation: 0010 | The Confirm Production Operation (F3069) screen displays. |  |
| 4 | Enter Fields in Quantities Section | In the Quantities section, check the following entries and make changes if required:Yield: <enter the amount you want to confirm>Scrap: <enter the amount you want to scrap> |  |  |
| 5 | Check Material Movements | The system shows you an overview table of all materials for which the withdrawal is done automatically with operation 0010 with the confirmation of the operation.Note All materials assigned to operation 0010 are not subject to backflush and the list is empty. |  |  |
| 6 | Enter Fields in Activities Section | In the Activities section, make the following entries:Setup: <setup time>Machine: <machine time>Labor: <labor time> | Confirmation is made. |  |
| 7 | Save your Entries | Choose Post and Complete to make final confirmation for this operation. | Confirmation has been created.Note For partial confirmation choose Post instead of Post and Complete. |  |

##### Confirm Production for Operation Cooling

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In the Consumer Products Industry, goods receipt and goods issue postings are usually done immediately during the physical movements of the materials to ensure batch traceability and data consistency. Order confirmations with backflush are done at shift end or day end. The sum of the GI and GR quantity for the given order is then recorded within the confirmation and scrap quantities (optional). The time ticket confirmation allows recording either the default times for machine and labor usage, or record actual times for major deviations.

Prerequisite

The production order for the seminfinished material FG0511 has been released and material staging has been carried out. The operation 0010 of the production order has already been confirmed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Confirm Production Operation (F3069). | The Enter Order and Operation screen displays. |  |
| 3 | Enter Order Number and Operation | On the Enter Order and Operation screen, make the following entries, and choose Go:Order: <Order ID> (from previous steps)Operation: 0020 | The Confirm Production Operation (F3069) screen displays. |  |
| 4 | Enter Fields in Quantities Section | In the Quantities section, check the following entries and make changes if required:Yield: <enter the amount you want to confirm>Scrap: <enter the amount you want to scrap> |  |  |
| 5 | Check Material Movements | In the Material Movements section, check the material list.Note For operation 0020 no components relevant to backflush are assigned. Hence the list is empty. | The system shows you an overview table of all materials for which the withdrawing is done automatically with the confirmation of the operation. |  |
| 6 | Enter Fields in Activities Section | In the Activities section, make the following entries:Machine: <enter the setup time you want to confirm for this operation> |  |  |
| 7 | Save your Entries | Choose Post and Complete to make final confirmation for this operation. | Confirmation has been created.Note For partial confirmation choose Post instead of Post and Complete. |  |

##### Monitor Order Progress (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the release or (partial) confirmation of finished goods orders is performed, the production supervisor could display and check the order using the app Manage Production Orders for the finished material FG0511.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Production Orders (F2336). | The Manage Production Orders (F2336) screen displays. |  |
| 3 | Select Production Order | On the Manage Production Orders (F2336) screen, make the following entries:To check default Area of Responsibilities (supervisor), select the user (from the top left corner), App Settings > Area of Responsibility Production Supervisor. Check only this entry is displayed.Plant 1 AE (3310)MTS DI - Valuated (YB1)Click Adapt Filters to display more selection filter. Select the checkboxes for Material and Production Plant and click OK.Material: FG0511Production Plant: 3310Click Go to execute. | Selected order displays. |  |
| 4 | Check detailed operations status | Check detailed information for selected production operations.Issues:Empty, if there is no issue for production orderDelay or Missing Components / PRT issue or Quantity Deviation / Quality Issue information shows if relevant issue existsComponents:Material, total quantity and issued / open quantity information for order components is displayedOrder Schedule:Detailed operation information with relevant work center, confirmed quantity, start and end time is displayedWork Center Schedule:The relevant order covering the same work center capacity (operation is partially confirmed) is displayedOperations not Started:The relevant order that would cover the same work center capacity (operation is released) is displayedConfirmation:Detailed confirmation information with Yield, Scrap, Rework quantity displays if confirmation executedInspection:Detailed inspection lots information displays if existed | Detailed operations status displays. |  |

|  |
| --- |
| Note To display the inspection lots, you need further authorizations of SAP_BR_QUALITY_TECHNICIAN (transaction QA03). Ensure that your user has the appropriate authorizations if you want to review the inspection lots. Else this section is empty even though inspection lots are available. |

#### Quality Inspection - Early Goods Receipt Inspection/End-Product-Control (Before Goods Receipt)

##### Display Inspection Plan for Inspection Characteristics

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

By the release of the production order, the early goods receipt inspection is triggered as well. While inspection lot creation the relevant inspection plan is assigned to the inspection lot.

In this step, you display the inspection plan that is related to the finished good. The inspection plan defines all inspection characteristics used later in the quality inspection (End-Product Control).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Display Inspection Plan (QP03). | The Display Inspection Plan: Initial Screen displays. |  |
| 3 | Enter Selection Fields | Make the following entries and choose Continue.Material: FG0511Plant: 3310 |  |  |
| 4 | Go to Inspection Characteristics Overview Screen | Select the entry for Operation 0010 and choose Inspection Characteristics.Note If you could not find Inspection Characteristics in your screen, choose Menu > Inspection Characteristics . | The Display Inspection Plan: Characteristic Overview screen displays. |  |
| 5 | Review the Inspection Characteristics | There are three Master Inspection Characteristics:One is Qualitative – Sensory Roasted Beans with inspection method Sensory of Roasted Coffee Beans.Two others are Quantitative – Relative Humidity and Rebrand.For all, sample size 1 is to be inspected.Auto-defect recording is defined if characteristics are rejected. | You have now reviewed the inspection characteristics for which data has to be maintained later. |  |

##### Display Quality Technician Overview (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this optional step, you can display an overview of open inspection lots via the overview page for quality technicians.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Quality Technician Overview (F2361). | The Quality Technician Overview (F2361) screen displays.You can get an overview of the inspection lots with open results recording and the inspection lots without an inspection plan.Choose card Inspection Lots with Open Results Recording, No Inspection Points if you want to record results for the early goods receipt inspection lot. |  |

##### Display Open Inspection Lots (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The early goods receipt inspection lot is used to start the End-Process Control already before goods receipt. In this optional step, the operations and characteristics are reviewed as well as assigned inspection methods with attachments used for quality inspection.

Prerequisite

In this scope item, the inspection lot is created automatically upon release of production order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Inspection Lots (F2343). | The Manage Inspection Lots screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Plant: 3310Material: FG0511Inspection Lot Status: OutstandingInspection Lot Origin: Goods Receipt from Production | Alternatively, you can search for the batch <Batch ID> (from previous step). |  |
| 4 | Select the corresponding Inspection Lot | In the inspection lot list, select the inspection lot with column Production Order equals to the Production Order: <Order ID> (from previous step) | The Production Order number assigned to Inspection Lot is displayed.If the Production Order column does not appear, please choose the button Settings. In the View Settings dialog box, select Production Order and choose OK.If needed, press button Show Details to make the column visible. |  |
| 5 | Choose Operation (optional) | In Result, choose operation End-Product-Control. | Inspection Characteristics Sensory Roasted Beans, Relative Humidity and Rebrand can be reviewed with their specifications and calculated sample sizes. |  |
| 6 | Choose Characteristic (optional) | Click Sensory Roasted Beans in the characteristics column. | For checking the attachment in the inspection method:If you have attached a document in the inspection method as described in the Preliminary Steps, the Quality Technician can review the attachment referring to step 6 to 8.A dialog box appears with the Characteristics Details with the link to the Inspection Method. |  |
| 7 | Display the Attachment (optional) | Under Documents, the attachment for an illustration of the Roast Color of coffee beans is displayed. |  |  |
| 8 | Display Text | In General, Long Text is displayed. |  |  |

##### Record Inspection Results (Before Goods Receipt)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the quality technician performs the quality inspection and records the inspection results for operation 0010 (End-Product Control).

After Cooling, the Quality Technician takes a sample of unpacked Roasted Beans and starts with quality inspection. This step can be performed alternatively before goods receipt (Option 1) or after goods receipt (Option 2).

It´s also possible to record results for some MICs earlier (e.g. rebrand and relative humidity), for others later (e.g. sensory), dependent from capacity in the laboratory.

Procedure

Record Inspection Results for one Inspection Lot

If inspection results shall be recorded for one or only a few inspection lots, execute the following steps:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Record Inspection Results (F1685A) | The Results Recording screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Plant: 3310Material: FG0511Order: <Order ID> from previous step. | If Order is not displayed in the Filters, please choose Filters. On the popup screen Filters, select Order and choose OK. Choose Go. |  |
| 4 | Select the Corresponding Inspection Lot | In the inspection lot list, select the inspection lot.Choose Record Multiple Results at the bottom right. |  |  |
| 5 | Enter Inspection Result | Depending on the inspection result, select one of the following two options:Positive ResultSensory: OKRelative Humidity: Mean Value (%): 4,0Rebrand: Mean Value (%): 14Negative ResultSensory: NOKRelative Humidity: Mean Value (%): 5,2Rebrand: Mean Value (%): 18 | For the qualitative characteristic (Sensory) the search help is needed to select a value. For the quantity characteristic (Relative Humidity and Rebrand) a number can be entered directly.The valuation and close are performed automatically, and the status is set to Valuated.The default number of inspected objects is calculated based on the sample size reviewed in an earlier step. The number of inspected objects can be manually changed. As well a number of nonconforming objects can be maintained directly in the respective fields for every inspection characteristic. |  |
| 6 | Save Inspection Lot | Choose Save. | The inspection lot is saved. QM Inspection for finished material has been performed and result recorded. |  |

Optional: Process-Optimized Results Recording for Multiple Inspection Lots

If inspection results shall be recorded for several inspection lots at the same time, execute the following steps.

|  |
| --- |
| Caution Note that this app can only be used for quality inspections with master inspection characteristics. It is not possible to capture inspection results for inspections with plan characteristics. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Record Inspection Results in Table Form (F3365) | The Record Inspection Results in Table Form screen displays. |  |
| 3 | Enter Filter Fields | Maintain filter values and choose Go. | A list of inspection lots is displayed. |  |
| 4 | Select Inspection Lots and Inspection Characteristics | Select the inspection lots for which inspection results shall be recorded and choose Record Multiple Results.In the dialogue box Select Characteristics for Result Recording, select the master inspection characteristics for which inspection results shall be recorded and choose button OK. | The Record Inspection Results in Table Form screen displays.Note The system creates one table line item per inspection lot operation. Each master inspection characteristic is displayed in a separate column. The valuation of the inspection characteristic is displayed in a separate adjacent column. If a master inspection characteristic is assigned to another inspection operation, the respective table field is grayed out. |  |
| 5 | Show Inspection Details (Optional) | Click on one inspection characteristic in the table and choose Show Details. | The side panel opens and detailed inspection data are displayed (e.g. inspection specifications, master inspection characteristic, inspection method, test equipment, and inspection remarks). |  |
| 6 | Show Work Center (Optional) | Choose Settings button in the upper right corner of the table. In the Define Colunm Properties dialogue box, select Work Center and choose OK. | An additional Work Center column is displayed. |  |
| 7 | Enter Inspection Results | Enter inspection results. See above for example data. | For qualitative results, a corresponding value help is provided. Quantitative inspection results can be entered directly.Depending on the defined valuation mode (check inspection details), the valuation is either done automatically by the system or must be done manually by the user.If a inspection result requires an inspection remark (check master inspection characteristic settings), it is not possible to navigate to the next inspection result. Open Details side panel and maintain the inspection remark in section Remarks. |  |
| 8 | Save Inspection Data | Choose Save. | Inspection results are saved and a success message is displayed. |  |

##### Display Inspection Results History (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this optional step, an overview about the history of inspection result is shown. For each quantitative Inspection Characteristic several statistical values and the development for recorded results are illustrated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Display Results History (F2428). | The Results History screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Aggregation Level: Master Inspection Characteristic |  |  |
| 4 | Select Inspection Characteristic | Select an Inspection Characteristic, for example, Relative Humidity and Rebrand. | Information is provided about the selected characteristics for process control, for example:A diagram displays the development of the recorded results for this characteristic with lower and upper limit.Statistical Values for Control Chart and Process Capability, for example Mean Value. |  |

#### Quality Inspection - In-Process Control (Operation Packaging)

##### Record Inspection Results (Hierarchical Worklist)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the quality technician performs the quality inspection and records the inspection result(s) for last operation 0030 (Packaging) within the production process.

The result is recorded in the inspection lot according to the defined inspection parameters in the routing. Here, free inspection points are used for result recording. Leveraging inspection points, you can have several inspections and can record multiple sets of characteristic results for a single operation. Each inspection point is valuated separately with a coded valuation.

Using inspection point identifier Y01, only the last sample results are valid.

For the rework process, the quality inspection should result in weight deviations meaning that some of the packages do not fit into the specification.

Prerequisite

The inspection is processed based on inspection lot. In this scope item, the inspection lot is automatically created upon release of the production order.

Production order operations 0010 (Roasting) and 0020 (Cooling) have already been confirmed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Record Inspection Results - Hierarchical Worklist (QE51N). | The Results Recording Worklist screen displays.Note The app Record Results for Inspection Points (F2689) can be used as an alternative to capture inspection results for inspection points. However, recording of different single values currently causes an issue. Therefore, use app Record Inspection Results - Hierarchical Worklist (QE51N). |  |
| 3 | Enter Selection Fields | Make the following entries and choose Execute.Plant: 3310Insp. Lot Origin: 03 (Production)Material: FG0511Batch: <Batch ID> from previous stepLot Created: <choose one week ago until today>Work Center: PM050001 | The Results Recording Worklist screen displays.Caution In Cloud system, Dynamic Selection (e.g. for production order) is not offered.Alternatively you can search for the <Batch ID> or <Inspection Lot ID> from previous step.Selected work centers (Packaging Machine 1 or Packaging Machine 2) are displayed in the result list. |  |
| 4 | Select the Corresponding Inspection Lot | On the left pane, expand the corresponding inspection lot which you want to record a result. | If a dialogue appears asking to save, choose Cancel. |  |
| 5 | Choose the First Inspection Point | Choose the first inspection point Further Inspection which is under the activity 0030 Packaging 1 KG Work Center Packaging Machine with a click. | When the work center is selected, the cursor jumps automatically to the result. |  |
| 6 | Enter Inspection Result for the First Inspection Point | Depending on the inspection result, enter your values: e.g.Negative ResultWeight – Result: 1048, 1049, 1050 | For the quantitative characteristic Weight, three independent values need to be entered and the system will calculate the mean value. |  |
| 7 | Close and Save the First Inspection Point | Choose Enter.Choose Save. | Auto Valuation Rejected is done by the system.The status is set to 5 Processing is completed. |  |

#### Execute Partial Production Order Confirmation for Operation Packaging

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In the Consumer Products Industry, Goods receipt and Goods Issue postings are usually done immediately during the physical movements of the materials to ensure batch traceability and data consistency.

During packaging process, the weight of the 1kg coffee bags is permanently monitored. The coffee bags that differ from specification are phased out from production and will be stored separately. They are subject to rework which is handled by a separate production order that is automatically triggered during partial confirmation of production order (with a rework amount). Rework means in this case that the bags will be ripped off and the lose coffee beans will be pushed back in the packaging process of the original production order.

The costs for rework activities and the additional packaging material shall be monitored on a separate order. So the confirmation of the original production order with status partial confirmation results in the creation of a new rework production order which is linked from costing point of view to the original production order where it is created from. The connection to the original order is set via the corresponding settlement rule.

Prerequisite

The production order for the finished material FG0511 has been released and material staging has been carried out. The operations 0010 and 0020 of the production order have already been confirmed. The QM checks result in a weight deviation for some of the coffee bean bags during weight check for operation 0030.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment. |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Confirm Production Operation (F3069). | The Enter Order and Operation screen displays. |  |
| 3 | Enter Order Number and Operation | On the Enter Order and Operation screen, make the following entries, and choose Go:Order: <Order ID> (from previous steps)Operation: 0030 | The Confirm Production Operation (F3069) screen displays. |  |
| 4 | Enter Fields in Quantities Section | In the Quantities section, make the following entries:Yield: <enter the amount you want to confirm>Rework: <enter the amount you want to rework>Reason for Variance: Weight Deviation | Note You must enter an amount for rework to create a rework order with rework amount. |  |
| 5 | Check Material Movements | In the Material Movements section, check the material list.Materials PK0501, PK0504 and PK0507 are subject to backflush and partly managed by batches (PK0501 and PK0504).Choose the Edit button on the right side of the material.Enter the relevant batch number and choose Save. | The system shows you an overview table of all materials for which the withdrawing is done automatically with the confirmation of the operation.The materials PK0501, PK0504 and PK0507 are set for backflush (in material master) and assigned to operation 0030 in the routing of FG0511 so that the withdrawing is done automatically after you confirm the operation. |  |
| 6 | Enter Fields in Activities Section | In the Activities section, make the following entries:Machine: <enter the setup time you want to confirm for this operation>Labor: <enter the setup time you want to confirm for this operation> |  |  |
| 7 | Save your Entries | Choose Post to make partial confirmation for this operation. | Parital confirmation has been created.Note The operation status partial confirmation PCNF triggers the creation of a rework production order of order type YRW1 and the rework amount maintained earlier.If you execute a final confirmation by selecting Post and Complete instead of Post, no rework order will be created and you cannot continue with this scenario. |  |

#### Adopt and Release Rework Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The rework production order created from an original production order is still linked to that order both from logistic and costing point of view. So the rework order has no material assignment and costs are transferred to related original order.

In this step you check the connection from the origional order to the rework production order and do some adoptions in the rework order.

Prerequisite

A rework production order has been created from the original production order for material FG0511.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment. |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Production / Planned Orders (COOIS). | The Production Order Information screen displays. |  |
| 3 | Enter Order Number and Operation | On the Production Order Information System screen, make the following entries, and choose Execute:Order: <Order ID> (from previous steps, original order for material FG0511)Plant: 3310Display Complete Rework: <set flag> | The Order Info System - Order Headers screen is displayed. |  |
| 4 | Adopt Rework production order | In the Order Info System - Order Headers screen make a note of the rework production order ________________ (rework production order number starting with 5*), mark the order and choose Change Object.On the Production Order Change: Header screen please note that this rework order has no material asssignment. Check the order quantity which should reflect the amount you confirmed as rework in previous step.Select the Assignment tab and make the following entries:MRP Controller: 001Prodn Supervisor: YB1Profit Center: YB110Choose Operations. On the Production Order Change: Operation Overview screen check the creation of operation 0010 according to reference operation set.Choose button Components.On the Production Order Change: Component Overview screen make the following settings:Component: PK0501Reqmt QTY: <quantity> Enter the quantity of additional packaging material you need for rework processingItem Category: LOperation: 0010Batch: <batch number>Choose Enter.Choose Release.Choose Save. |  |  |
| 5 | Analyse Costs for Rework Production Order | In the Order Info System - Order Headers screen choose the rework production order (order number is starting with 5*) and choose Display Object. Choose Menu > Goto > Costs > Analysis . On the Order - Event-Based screen check the Receiver Category which is Order.Close the tab and on the previous tab choose Back to return to the Order Info System - Order Headers screen. | Note To be able to see the cost analysis, in addition to the role Production Supervisor - Discrete Manufacturing, the role Cost Accountant - Production must be assigned to your user. |  |
| 6 | Analyse Costs for Original Production Order | In the Order Info System - Order Headers screen choose the initial production order (order number is starting with 1*) and choose Display Object. Choose Menu > Goto > Costs > Analysis . On the Order - Event-Based screen check the Receiver Category which is Material.Close the tab and on the previous tab choose Back to return to the Order Info System - Order Headers screen. | Note To be able to see the cost analysis, in addition to the role Production Supervisor - Discrete Manufacturing, the role Cost Accountant - Production must be assigned to your user. |  |

#### Confirm Rework Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step you confirm all activities related to rework processing:

- Confirm activities related to rework
- Confirm goods issue of components that are needed for rework processing

Prerequisite

A rework order has been created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment. |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Confirm Production Operation (F3069). | The Enter Order and Operation screen displays. |  |
| 3 | Enter Order Number and Operation | On the Enter Order and Operation screen, make the following entries, and choose Go:Order: <Order ID> (rework order from previous steps)Operation: 0010 | The Confirm Production Operation (F3069) screen displays. |  |
| 4 | Enter Fields in Quantities Section | In the Quantities section, make the following entries:Yield: <enter the amount you want to confirm>Scrap: <enter the amount you want to scrap> |  |  |
| 5 | Check Material Movements | In the Material Movements section, check the material list.Material PK0501 is subject to backflush and managed by batches.Choose the Edit button on the right side of the material.Enter the relevant batch number and choose Save. | The system shows you an overview table of all materials for which the withdrawing is done automatically with the confirmation of the operation.The material PK0501 is set for backflush (in material master) and assigned to operation 0010 in the rework production order so that the withdrawing is done automatically after you confirm the operation. |  |
| 6 | Enter Fields in Activities Section | In the Activities section, make the following entries:Machine: <enter the setup time you want to confirm for this operation>Labor: <enter the setup time you want to confirm for this operation> |  |  |
| 7 | Save your Entries | Choose Post and Complete to make final confirmation for this operation. | Confirmation has been created. |  |

#### Quality Inspection - In-Process Control (Operation Packaging) and Usage Decision

##### Record Inspection Results (Hierarchical Worklist)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the quality technician performs the quality inspection and records the inspection result(s) for last operation 0030 (Packaging) within the production process.

The result is recorded in the inspection lot according to the defined inspection parameters in the routing. Here, free inspection points are used for result recording. Leveraging inspection points, you can have several inspections and can record multiple sets of characteristic results for a single operation. Each inspection point is valuated separately with a coded valuation.

Using Inspection point identifier Y01, only the last sample results are valid.

Prerequisite

The inspection is processed based on inspection lot. In this scope item, the inspection lot is automatically created upon release of the production order.

Production order operations 0010 (Roasting) and 0020 (Cooling) have already been confirmed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Record Inspection Results - Hierarchical Worklist (QE51N). | The Results Recording Worklist screen displays.Note The app Record Results for Inspection Points (F2689) can be used as an alternative to capture inspection results for inspection points. However, recording of different single values currently causes an issue. Therefore, use app Record Inspection Results - Hierarchical Worklist (QE51N). |  |
| 3 | Enter Selection Fields | Make the following entries and choose Execute.Plant: 3310Insp. Lot Origin: 03 (Production)Material: FG0511Batch: <Batch ID>Lot Created: <choose one week ago until today>Work Center: PM050001 | The Results Recording Worklist screen displays.Caution In Cloud system, Dynamic Selection (e.g. for production order) is not offered.Alternatively, you can search for the <Batch ID> or <Inspection Lot ID> from previous step.Selected work centers (Packaging Machine 1 or Packaging Machine 2) are displayed in the result list. |  |
| 4 | Select the Corresponding Inspection Lot | On the left pane, expand the corresponding inspection lot which you want to record a result. | If a dialogue appears asking to save, choose Cancel. |  |
| 5 | Choose the First Inspection Point | Choose the first inspection point Further Inspection which is under the activity 0030 Packaging 1 KG Work Center Packaging Machine with a click. | When the work center is selected, the cursor jumps automatically to the result. |  |
| 6 | Create the Next Inspection Point | Choose Further Inspection which is under the activity 0030 Packaging 1 KG Work Center Packaging Machine with a click. | The next inspection point is created with current Date/Time.A dialogue appears asking to save data for operation 0030, Choose Yes. |  |
| 7 | Enter Inspection Result for the Next Inspection Point | Depending on the inspection result, enter your values: e.g.Positive ResultWeight – Result: 1050, 1051, 1052 | For the quantitative characteristic Weight, three independent values need to be entered and the system will calculate the mean value. |  |
| 8 | Close and Save the Next Inspection Point | Choose Enter.Choose Save. | Auto Valuation Accepted is done by the system.The status is set to 5 Processing is completed. |  |

##### Display Inspection Results History (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this optional step, an overview about the history of inspection result is shown. For each quantitative Inspection Characteristic, several statistical values and the development for recorded results are illustrated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Display Results History (F2428). | The Results History screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Aggregation Level: Master Inspection Characteristic |  |  |
| 4 | Select Inspection Characteristic | Select an Inspection Characteristic, for example, Weight. | Information is provided about the selected characteristics for process control, for example:A diagram displays the development of the recorded results for this characteristic with lower and upper limit.Statistical Values for Control Chart and Process Capability, for example Mean Value and Variance. |  |

##### Display Quality Engineer Overview (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection is done and the inspection result is recorded. You must decide whether or not to accept the inspection lot depending on the inspection result. As an optional entry point for making this usage decision, you can use the app Quality Engineer Overview (F2360). Furthermore, the Quality Engineer Overview (F2360) app displays inspection lots without an inspection plan (e.g. if automatic assignment of an inspection plan is not set up in the material master or if automatic assignment failed), inspection lots without usage decision and inspection lots ready for usage decision.

|  |
| --- |
| Caution For this scope item example, auto-defect recording has not been performed in quality inspection within production (In-Process Control) because deviations are expected during the production process and shall not be tracked as defects later. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Quality Engineer Overview (F2360). | The Quality Engineer Overview (F2360) screen displays. |  |
| 3 | In Card: Inspection Lots without Inspection Plan choose one entry (optional) |  | To assign missing data and ensure automatic inspection plan determination for further usage. |  |
| 4a | In Card: Select Inspection Lots Without Usage Decision (Optional) | Choose card Inspection Lots Without Usage Decision. | You can process further as described in Make Usage Decision Chapter. |  |
| 4b | Select the Corresponding Inspection Lot you have created before (optional) | In the inspection lot list, select the inspection lot. | The Manage Usage Decisions screen displays. Alternative entry to chapter Manage Usage Decision. |  |
| 4c | Select one of the Inspection Lot by Results Recording Status (Optional) | Select one of the Inspection Lot by Results Recording Status (Optional). | Alternative entry to chapter Manage Usage Decision. |  |
| 5 | Select Card Inspection Lots Ready for Usage Decision (optional) |  | All inspection lots with positive results get collectively an accepted usage decision (e.g. defaulted by A1) when pressing button Make Quick Usage Decision will be renamed soon. |  |
| 6 | In Card: Inspection Lots with Defects (optional) | (In case negative inspection results have been recorded and auto-defect recording has been defined) Select one of the inspection lot origins, then you will be directed to app Manage Defects (F2649) automatically. Choose the relevant defect ID to check the details of the defect. | The defect details are displayed. |  |
| 7 | In Card: Top Defective Materials (optional) | (In case failed inspection results have been recorded and auto-defect recording has been defined) Select one of the materials inspected, then you will be directed to app Manage Defects (F2649) automatically. Choose the relevant defect ID to check the details of the defect. | The defect details are displayed. |  |
| 8 | In Card: Top Defective Codes (optional) | (In case negative inspection results have been recorded and auto-defect recording has been defined) Select one of the defect codes recorded, then you will be directed to app Manage Defects (F2649) automatically. Choose the relevant defect ID to check the details of the defect. |  |  |

##### Make Usage Decision

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspections within production (operation Roasting and Packaging) are done and the inspection results are recorded. The Production Operator - Discrete Manufacturing was informed about the inspection results and can confirm last production order operation 0030 Packaging.

After recording of the inspection results by the quality technician, the quality engineer can now make a usage decision.

In order to close the inspection lot, the quality engineer makes a usage decision. As the inspection lot of origin 03 is not stock-relevant, there is no follow-up action assigned to the usage decision code that triggers a goods movement.

|  |
| --- |
| Caution In this example, the In-Process Control is performed as long as the relevant process parameters are reached. Thus, the last sample will always be accepted and because with inspection point Y01 only the last sample is valid, the UD can always be made with UD03 A (Accepted). For performing the UD you can either edit the inspection lot after checking the inspection data or you can perform the Quick Usage decision immediately after inspection lot selection. |

Procedure: Usage Decision after checking inspection data

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Usage Decisions (F2345). | The Manage Usage Decisions (F2345) screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Plant: 3310Material: FG0511Inspection Lot Origin: ProductionUsage Decision Made: No | Alternatively you can search for the <Order ID> or <Batch ID> from previous steps.If Production Order is not displayed in the Filters, choose Adapt Filters. On the popup screen Adapt Filters, find Production and choose More Filters. Select Production Order and choose OK. Choose Go.If Batch is not displayed in the Filters, choose Adapt Filters. On the popup screen Adapt Filters, find Material and choose More Filters. Select Batch and choose OK. Choose Go. |  |
| 4 | Click the Corresponding Inspection Lots | In the inspection lot list, select the inspection lot with column Production Order equals to the Production Order: <Order ID> (from previous step). | The Production Order number is assigned to Inspection Lot.If the Production Order column does not appear, please choose the button Settings. In the View Settings dialog box, select Production Order and choose OK. |  |
| 5 | Review of Inspection Points | Select the tab Inspection Points, and review the detailed inspection results recorded previously (from previous steps - Inspection Operations - Roasting) |  |  |
| 6 | Enter UD code | Choose Edit and select the tab Usage Decision. The UD code you select depends on the Inspection Result. Please select the following option,Positive ResultUD code: A UD03 (Accepted) |  |  |
| 7 | Save Usage Decision | Choose Save. | Usage decision has been made for In-process control inspection lot.Following a negative usage decision, you only partly confirm the operation Packaging of the production order and trigger with this activity the rework of the material. |  |

#### Confirm Original Production Order for Operation Packaging

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After rework of the coffee bags with weight deviation, the coffee beans are handled further within the original production order and final confirmation and goods receipt is done for this order.

Prerequisite

The rework production order has been finally confirmed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment. |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Confirm Production Operation (F3069). | The Enter Order and Operation screen displays. |  |
| 3 | Enter Order Number and Operation | On the Enter Order and Operation screen, make the following entries, and choose Go:Order: <Order ID> (from original production order from previous steps)Operation: 0030 | The Confirm Production Operation (F3069) screen displays. |  |
| 4 | Enter Fields in Quantities Section | In the Quantities section, make the following entries and choose Enter:Yield: <enter the amount you want to confirm> |  |  |
| 5 | Check Material Movements | In the Material Movements section, check the material list.Materials PK0501, PK0504 and PK0507 are subject to backflush and partly managed by batches (PK0501 and PK0504).Choose the Edit button on the right side of the material.Enter the relevant quantity to be posted and if needed the batch number. Choose Save. | The system shows you an overview table of all materials for which the withdrawing is done automatically with the confirmation of the operation.The materials PK0501, PK0504 and PK0507 are set for backflush (in material master) and assigned to operation 0030 in the routing of FG0511 so that the withdrawing is done automatically after you confirm the operation. |  |
| 6 | Enter Fields in Activities Section | In the Activities section, make the following entries:Machine: <enter the setup time you want to confirm for this operation>Labor: <enter the setup time you want to confirm for this operation> |  |  |
| 7 | Save your Entries | Choose Post and Complete to make final confirmation for this operation. | Final confirmation has been created. |  |

#### Post Goods Receipt for Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post the goods receipt for the production order. You may post goods receipt for the total quantity, but if already partial quantities of the products are required for further processing, for example for further production or subsequent deliveries for sales orders, you can also execute partial confirmation during production process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Receipt for Production Order (F3110). | The Post Goods Receipt for Production Order (F3110) screen displays. |  |
| 3 | Enter Details | On the Post Goods Receipt for Production Order (F3110) screen, make the following entries and choose Enter:Order: <Order ID> (from previous steps) |  |  |
| 4 | Select the Item | In the Items section, select the item. | The Goods Receipt Item screen displays. |  |
| 5 | Input Production Date | In the Production and Shelf Life Expiration Date section, make the following entries and choose Apply:Production Date: <Current Date> | The Goods Receipt screen displays. |  |
| 6 | Post | Choose Post. | Goods receipt for production order has been done. |  |

#### Cost Analysis of Original and Rework Production Orders

After rework of the coffee bags with weight deviation and confirmation of original production order, the costs for both production orders are reviewed.

For further detailed event-based insights or error handling and monitoring the scope item 3F0 Event-Based Production Cost Posting can be referred.

Prerequisite

The rework production order and the original order are available, goods movements were executed and activities are confirmed.

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

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Production. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Analyze Production Costs - Event-Based (F4059). | The Event-Based Production Costs screen displays. |  |
| 3 | Enter Data | Make the following entries and choose Go:Fiscal Period From: <enter period>Fiscal Period To: <enter period>Currency: AEDCompany Code: 3310Order number: <Order ID> | The selected Production order - Rework Order or Production Order as Superior Order - will be listed and can be analyzed in detail.Note The Rework Order is not assigned to a material, but the settlement of the Rework Order is assigned to the Header material related Production Order. |  |
| 4 | Select Order Details | Select the order number and choose Details. | The screen provides an overview of the production order related cost details. |  |

##### Analyze Event-Based Production Variances (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you run the report to review event-based production variances, this step is executed for final delivered or technical completed production orders.

Procedure

To execute this activity, execute the Analyze Event-Based Order Costs step from the Event-Based Production Cost Posting (3F0) test script.

### Rework Production Order of Stock Manufactured Material with Quality Management

This rework process focuses on rework activities and material postings after production execution for the original material including goods receipt for the product. During goods receipt for the product quality issues have been identified for a part of the produced products and the usage decision failed. The products are booked into inventory, but the failed part is posted not to unrestricted use but to blocked stock.

The products booked to blocked stock will be subject to rework activities to overcome the defect. The rework process of stock-manufactured materials begins with the creation of a new production order. This is done using the material to be reworked as both input and output. Costs are listed in the new production order and are settled within controlling as production variants. The input component and product have the same material number.

After rework is finished the material is again subject to quality inspection to check successful rework processing. Therefore, an inspection lot of origin 04 (goods receipt from production) is created during goods receipt for rework production order. After inspection execution and, depending on usage decision, the reworked product is posted to corresponding stock (unrestricted stock or not if QM inspection failed again).

#### Create Stock for material FG0502

Before you can start rework, you need to post stock for the finished material that is subject to rework.

You have two options:

Option 1: Execute complete production process for material FG0502

Option 2: Create initial material stock

##### Option 1: Execute complete Production Process for Material FG0502

To run through the complete production process for the finished material FG0502, execute all steps described in scope item 5HK - Quality Management in Discrete Manufacturing – Consumer Products. Please ensure that in step 4.14.7 the usage decision results in blocked stock. Note down the batch number and the amount booked into blocked stock.

|  |
| --- |
| Note If you want to run the rework scenario and you have already stock posted to unrestricted you can also run through the test case and skip step “Transfer Material from Blocked to Unrestricted Use Stock” from this test script. |

##### Option 2: Create Initial Material Stock

Purpose

In a real business scenario, materials are produced as described in option 1. For only testing purpose, this process step shows you how to create and post the initial material stock to storage locations in blocked stock directly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Post Goods Movement (MIGO) screen displays. |  |
| 3 | Choose Document Type | Choose Goods Receipt and Other. Select for Init.entry of stBal. 561 without any stock indicator and press Enter. |  |  |
| 4 | Enter Data | In the Detail Data section, make the following entries and press Enter:On the Where tab:Goods Movement Type: 561Stock Type: BlockedPlant: 3310Storage Location: 331A for FGXXXX (Finished Materials) materialsOn the Quantity tab:Quantity: 30, for exampleOn the Material tab:Material: FG0502.On the Batch tab:Batch: <batch number> exampleDate of Manufacture: <Today's date> exampleEnsure that Item OK is selected. |  |  |
| 5 | Check | Choose Check. | The document is ready to be posted. |  |
| 6 | Post | Choose Post. | Material document XXX is posted and materials are available in stock.Note down the batch number and the amount you have booked into blocked stock. |  |

#### Create and Release Rework Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how the manufacturing staff reworks the manufactured material from stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Production Order (CO01). | The Production Order Create: Initial Screen displays. |  |
| 3 | Enter the Order Information | Make the following entries and press Enter:Materials : FG0502Production Plant : 3310Order Type: YBW1 | The Production Order Create: Header screen displays. |  |
| 4 | Enter the Order Details | Make the following entries and press Enter:Quantity : <Quantity>End Date: <Date>, for example, Today's date +2 Days | The Select Production Version for Material and Plant dialog box displays. |  |
| 5 | Select the Production Version | Select the Production Version 0099 line and select Choose. |  |  |
| 6 | Save | Choose Save and make a note of your production order number. | Note The creation and release of the production order is executed in one step. |  |

#### Transfer Rework Material from Blocked to Unrestricted Use Stock

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After production order release, the goods issue for the material FG0502 that is subject to rework should be booked in next step. This material is currently located in blocked stock due to failed quality check and negative usage decision. Before goods issue for a production order can be executed, the material must be transferred from blocked stock to unrestricted use stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Goods Issue Order - <Your User name> displays. |  |
| 3 | Enter Details | Make the following entries:Transfer PostingOtherMovement Type: 343 (TR blocked to unre.)Choose Enter. |  |  |
| 4 | Enter Transfer Posting Data | Select the Transfer Posting tab and make the following settings:Dest sectionMaterial: FG0502Plant: 3310Location: 331AFrom sectionLocation: 331AQty in UnE: <quantity> (quantity relevant to rework)Choose Enter.Enter the batch number (see previous step) for Dest and From sections. |  |  |
| 5 | Post | Set Item OK indicator and choose Post. |  |  |

#### Goods Issue for Defective Materials

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how the system performs a goods issue for the defective material that must be reworked.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Goods Issue Order - Your User name screen displays. |  |
| 3 | Enter Details | Make the following entries:Goods IssueOrder: <Rework Production Order Number> (From the previous step)Movement Type : 261Press Enter. |  |  |
| 4 | Review the Details | Select the Where tab and check the following settings:Plant: 3310Storage Location: 331A |  |  |
| 5 | Enter Batch | Select Batch tab and choose the appropriate batch number. |  |  |
| 6 | Post | Set Item OK indicator and choose Post. |  |  |

#### Confirmation of Rework Production Activities

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to execute and record confirmations of all rework activities of the rework production order before posting the goods receipt in usual business practice.

Prerequisite

The goods issue for the defective material has been completed in the previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Confirm Production Operation (F3069). | The Perform Work screen displays. |  |
| 3 | Enter Production Order and Operation | On the Perform Work screen, make the following entries and choose Enter:Order: 60000XX (from the previous step)Operation: 0010 |  |  |
| 4 | Enter Fields in Quantities Section | In the Quantities section, make the following entries:Yield: <Quantity - the quantity you want to confirm>Scrap: <Quantity - the quantity that cannot be reworked> |  |  |
| 5 | Post Additional Goods Movements | In the Material Movements section, choose Add Material. | The Add Material screen display.Only when you need additional goods issue posting in your rework process, you need proceed with these next two steps. If you have no additional goods issues posting, continue with step 7. |  |
| 6 | Enter Goods Movement Details | Make the following entries and choose Add:Material: PACKAGING MATERIAL, for example, PK0504 (Label), PK0508 (Display Carton Coffee Beans 48 x 1 kg)Plant: 3310Storage Location: 331CQuantity to be Posted: <Quantity>UoM: PCBatch: Enter a batch number if the material is managed in batches. |  |  |
| 7 | Enter Fields in Activities Section | In the Activities section, make the following entries:Setup: <enter the setup time you want to confirm for this operation>Labor: <enter the labor time you want to confirm for this operation > |  |  |
| 8 | Save Your Entries | Choose Post and Complete to make final confirmation for this operation. | Confirmation has been created. |  |

#### Manage Production Operations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display and check the order using the Manage Production Operations (F2335) app for finished goods Make-To-Stock (FG0502) after the release/confirm of finished goods orders is performed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Production Operations (F2335) | The Manage Production Operations (F2335) screen displays. |  |
| 3 | Select Production Order | On the Manage Production Operations (F2335) screen, enter the following search condition as filter.To review the Default Area of Responsibility (supervisor), select the user from the top left of the App Settings Area of Responsibility Production Supervisor screen and ensure only the following displays:Plant: 3310Supervisors: YB5Select Adapt Filters to display more selection filters. Select the checkbox for Material and Plant, and choose OK.Result: Material and Plant fields are then added to filter bar.Status: ConfirmedMaterial: FG0502Plant: 3310 (Production plant)Choose Go to execute. | Selected order displays. |  |
| 4 | Check Detailed Operations Status | Check detailed information for selected production operations.Operation Issues:Empty if there is no issue for production order.Delay/Missing Components/PRT issue/Quantity Deviation/Quality Issue information displays when relevant issues exist.Components:Material, total quantity and Issued/open quantity information for order components displays.Order Schedule:Detailed operation information with relevant work center, confirmed quantity, start/end time displays.Work Center Schedule:The relevant order covering the same work center capacity (operation is partially confirmed) displays.Confirmation:Detailed confirmation information with Yield, Scrap & Rework quantity displays when confirmation is executed.Inspection:Detailed inspection lots information displays when available. | Detailed operations status displays. |  |

#### Post Goods Receipt for Rework Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post the goods receipt for the rework production order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Goods Receipt Order - Your User name screen displays. |  |
| 3 | Enter Details | Make the following entries:Goods ReceiptOrder : Rework Production Order Number, from previous stepMove Type : 101Choose Enter.Plant : 3310Storage Location : 331AChoose Batch tab. Enter batch details.Choose Enter. |  |  |
| 4 | OK Item and Check | Select the Item OK checkbox and choose Check. |  |  |
| 5 | Post | Choose Post. |  |  |

#### Event-Based Production Cost Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

After the rework process is finished, the related cost information can be monitored based on a central Event-Based Production Cost Overview which provides, among others, access to key information and KPIs within the production accounting area and insight into current trends.

For further detailed event-based insights or error handling and monitoring the scope item, 3F0 Event-Based Production Cost Posting can be referred.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Production. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Production Cost Overview - Event-Based (F6248). | The Event-Based Production Accounting Overview view displays. |  |
| 3 | Enter Selection Parameters | Make the following entries:Fiscal Period From: <Current date>Fiscal Period To: <Current date>Ledger: 0LCurrency Type: <for example, 10>Company Code: 3310Currency: AEDPlant: 3310Order Type: <Enter any order type that is supported, for example YBW1 for Rework orders>Order: <Enter the order number you created in previous step> |  |  |
| 4 | View Event-Based KPIs | Choose the Go button. | Key highlights:• Production volume per product: The card lists products with actual and planned quantities, it is sorted from the highest actual quantity for selected filters. Clicking the header of the card takes you to Event-Based Production Costs app.• Variances overview: The card presents chart with all supported variances that are split by Plant in default view, but you could change it to view by Product, Profit Center, Product Group, Storage Location. Clicking the header of the card takes you to Event-Based Production Costs app.• Total Production Costs: The card shows chart with Total Actual costs compared to Total Plan Costs. Default view is by Plant, but you could change it the same way as before. Clicking the header of the card takes you to Event-Based Production Costs app.• WIP overview: The card shows Total Work in Process as of last date of fiscal period selected in the Fiscal Period To field. In case it is current month, the key date is set to today. You can change the default view by Plant to any other perspective as for the other cards. The card navigates to Event-Based Work in Process app.• Quick Links: The card provides links to other event-based reporting apps. |  |

#### Quality Inspection of Reworked Material

##### Display Material Stock Before Quality Inspection (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this optional step, a review of the finished material stock is done. Due to quality inspection, the material is not available for other processing.

Prerequisite

The goods receipt from production order was posted for the finished material directly to quality inspection stock. This is caused by material master settings for inspection type 04 Goods Receipt Inspection from Production.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as an Inventory Manager. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Stock - Single Material (F1076). | The Stock - Single Material (F1076) screen displays. |  |
| 3 | Enter Material | Make the following entries and press Enter.Material: FG0502 | Stock for the material is displayed. |  |
| 4 | Check Stock Quantity | Check the Quality Inspection Stock under the plant 3310 and batch <Batch ID> from previous step. | Stock for the material, batch and storage location is checked. |  |
| 5 | Check Inspection Lots | Choose Manage Stock on the bottom of the screen. Then choose Manage Inspection Lots on the bottom of the screen.Note Ensure your user has necessary authorization to view Manage Inspection Lots. | The Inspection Lots for the selected material are displayed. |  |

##### Display Inspection Plan for Inspection Characteristics (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you display the inspection plan that is related to the finished goods. The inspection plan defines all inspection characteristics used later in the quality inspection.

|  |
| --- |
| Note If necessary the quality inspection plan determination for the rework process could be modified. With the User-Exit QPAP0002 a special quality inspection plan could be determined, depending of the production order type. So it is possible to distinguish between a good receipt from a normal production against a goods receipt from a rework production.To implement the adaptation use the app Custom Fields (F1481). With this app you can make enhancement implementation if you have the corresponding authorizations. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Display Inspection Plan (QP03). | The Display Inspection Plan: Initial Screen displays. |  |
| 3 | Enter Selection Fields | Make the following entries and choose Continue.Material: FG0502Plant: 3310 |  |  |
| 4 | Go to Inspection Characteristics Overview Screen | Choose Inspection Plan with Group Counter GrC 1 and choose Operations.Select the entry for Operation 0010 and choose Inspection Characteristics.Note If you could not find Inspection Characteristics in your screen, choose Menu > Goto > Inspection Characteristic Overview . | The Display Inspection Plan: Characteristic Overview screen displays. |  |
| 5 | Review the Inspection Characteristics | There is one Master Inspection Characteristics: It is Qualitative – Visual Pack Check.Sample size is 100% to be inspected.Auto-defect recording is defined if charac. is rejected. | You have now reviewed the inspection characteristics for which data has to be maintained later. |  |

##### Display Quality Technician Overview (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this optional step, you can display an overview of open inspection lots via the overview page for quality technicians.

Prerequisite

The goods receipt from production order was posted for the finished material directly to quality inspection stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Quality Technician Overview (F2361). | The Quality Technician Overview (F2361) screen displays.You can get an overview of the inspection lots with open results recording and the inspection lots without an inspection plan.Choose card Inspection Lots with Open Results Recording, No Inspection Points if you want to record results for the goods receipt inspection lot. |  |

##### Display Open Inspection Lots

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
| 1 | Log On | Log onto the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Inspection Lots (F2343). | The Manage Inspection Lots (F2343) screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Plant: 3310Material: FG0502Inspection Lot Status: Outstanding | Alternatively, you can search for the batch <Batch ID> (from previous step). |  |
| 4 | Select the Corresponding Inspection Lot | In the inspection lot list, select the inspection lot with column Production Order equals to the Production Order: <Order ID> (from previous step). | The Production Order number assigned with Inspection lot is displayed.If the Production Order column does not appear, please choose the button Settings. In the View Settings dialog box, select Production Order and choose OK. |  |
| 5 | Check Inspection Lot | In the inspection lot list you can watch the progress of characteristics. | Make a note of the inspection lot:Inspection Lot ______________ with progress 0%. |  |
| 6 | Check Inspection Lot | In the Origin tab, verify the referenced production order and material document. | The production order and material document from which the inspection lot originates are displayed. |  |
| 7 | Check Inspection Lot Quantities | In the Origin tab, check the Lot Quantities, Sample Size and Postings. | The size of the sample for quality inspection is displayed (100% of inspection lot quantity).Actual Lot Quantity and Postings are according to goods receipt quantity from previous step. |  |
| 8 | Check Material Document | In the Stock Postings tab, check details of the assigned material document, which has created the inspection lot. | Movement Type of this material document is 101 GR goods receipt.Quantity is as posted in the previous step. |  |

##### Record Inspection Results (Hierarchical Worklist)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the quality technician performs the quality inspection and records the inspection result(s) for operation 0010 (Display Packaging Check). The result is recorded in the inspection lot according to the defined inspection parameters in the inspection plan.

Prerequisite

The inspection is processed based on inspection lot. In this scope item, the inspection lot is automatically created upon goods receipt for production order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Record Inspection Results - Hierarchical Worklist (QE51N). | The Results Recording Worklist screen displays. |  |
| 3 | Enter Selection Fields | Make the following entries and choose Execute.Plant： 3310Insp. Lot Origin： 04 (Goods Receipt from Production)Material: FG0502Batch: <Batch ID> from previous stepLot Created: <choose one week ago until today>> | The Results Recording Worklist Screen displays.Caution In Cloud system, Dynamic Selection (e.g. for production order) is not offered.Alternatively you can search for the <Batch ID> or <Inspection Lot ID> from previous step. |  |
| 4 | Select the Corresponding Inspection Lot | On the left pane, expand the corresponding inspection lot which you want to record a result. | If a dialogue appears asking to save, choose Cancel. |  |
| 5 | Choose the Characteristic | Select the characteristic which is under the activity 0010 Display Pack-Control Work Center Quality Check Point with a click (or use icon Select a Characteristic). | When the characteristic is selected, Record Results for XXXX: Characteristic Single Screen, opens where the class size can be recorded. |  |
| 6 | Enter Inspection Result for Characteristic | Depending on the inspection result, classify the no. of inspected displays and then confirm with Save.Positive ResultVisual Pack Check: <enter no. of displays in class size> of class OKNegative ResultVisual Pack Check: <enter no. of displays in class size> of class NOK | For the qualitative characteristic Visual Check a 100% check is performed, assigning the no. of displays to the corresponding class OK or NOK.Auto Valuation is done by the system.The status is set to 5 Processing is completed. |  |

##### Display Quality Engineer Overview (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection is done and the inspection result is recorded. You must decide whether or not to accept the inspection lot depending on the inspection result. As an optional entry point for making this usage decision, you can use the app Quality Engineer Overview (F2360). Furthermore, the Quality Engineer Overview (F2360) app displays inspection lots without an inspection plan (e.g. if automatic assignment of an inspection plan is not set up in the material master or if automatic assignment failed), inspection lots without usage decision and inspection lots ready for usage decision. If negative inspection results are recorded, you can check the defect details in app Manage Defects (F2649) directed from the app Quality Engineer Overview (F2360) via the cards Inspection Lots with Defects, Top Defective Materials, or Top Defects.

|  |
| --- |
| Caution For this scope item example, auto-defect recording is performed in quality inspection for goods receipt (End-Product Control) because deviations shall be tracked as defects later. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Quality Engineer Overview (F2360). | The Quality Engineer Overview (F2360) screen displays. |  |
| 3 | In Card: Inspection Lots without Inspection Plan choose one entry (optional) |  | Assign missing data and ensure automatic inspection plan determination for further usage. |  |
| 4a | In Card: Select Inspection Lots Without Usage Decision (Optional) | Choose card Inspection Lots Without Usage Decision. | You can process further as described in Make Usage Decision. |  |
| 4b | Select the Corresponding Inspection Lot you have created before (optional) | In the inspection lot list, select the inspection lot. | The Usage Decisions screen displays. Alternative entry to Make Usage Decision. |  |
| 4c | Select one of the Inspection Lot by Results Recording Status (Optional) | Select one of the Inspection Lot by Results Recording Status (Optional). | Alternative entry to Make Usage Decision. |  |
| 5 | Select Card Inspection Lots Ready for Usage Decision (optional) |  | All inspection lots with positive results get collectively an accepted usage decision (e.g. defaulted by A1) when pressing button Make Quick Usage Decision. |  |
| 6 | In Card: Inspection Lots with Defects (optional) | (In case negative inspection results have been recorded and auto-defect recording has been defined). Select one of the inspection lot origins, then you will be directed to app Manage Defects (F2649) automatically. Choose the relevant defect ID to check the details of the defect. | The defect details are displayed. |  |
| 7 | In Card: Top Defective Materials (optional) | (In case negative inspection results have been recorded and auto-defect recording has been defined). Select one of the materials inspected, then you will be directed to app Manage Defects (F2649) automatically. Choose the relevant defect ID to check the details of the defect. | The defect details are displayed. |  |
| 8 | In Card: Top Defects (optional) | (In case negative inspection results have been recorded and auto-defect recording has been defined). Select one of the defect codes recorded, then you will be directed to app Manage Defects (F2649) automatically. Choose the relevant defect ID to check the details of the defect. |  |  |

##### Make Usage Decision

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection is done and the inspection result is recorded. You must decide whether or not to accept the finished material depending on the inspection result. If you do not want to use the Quality Engineer Overview (F2360), you can open the Manage Usage Decisions (F2345) app directly.

In order to close the inspection lot, the quality engineer makes a usage decision. As the inspection lot of origin 04 is stock-relevant, there is a follow-up action assigned to the usage decision code that triggers a goods movement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Usage Decisions (F2345). | The Manage Usage Decisions (F2345) screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go:Plant: 3310Material: FG0502Usage Decision Made: No | Alternatively you can search for the <Order ID> or <Batch ID> from previous steps.If Production Order is not displayed in the Filters, choose Adapt Filters. On the popup screen Adapt Filters, find Production and choose More Filters. Select Production Order and choose OK. Choose Go.If Batch is not displayed in the Filters, choose Adapt Filters. On the popup screen Adapt Filters, find Material and choose More Filters. Select Batch and choose OK. Choose Go. |  |
| 4 | Select the Corresponding Inspection Lot | In the inspection lot list, select the inspection lot. |  |  |
| 5 | Display Defects | Scroll down to the Defects area. Check the details of Defects. | Only available if you have recorded a Negative result. For a visual check rejection, there will be a packaging defect. |  |
| 6 | Enable Edit | Choose Edit. In the Document section choose Upload, select the path and add the document. | For example, you can upload pictures to visualize the defect. |  |
| 7 | Enter UD code | Depending on the inspection result, select one of the following two options via search help and confirm with Choose.Positive ResultUD code: UD04 A1 (Accepted - unrestricted stock)Negative ResultUD code: UD04 R1 (Rejected-blocked Stock)UD code: UD04 R320 Rejected–scrap (complete quantity) | If the dialogue 'Some required characteristics are still open. Do you want to force inspection completion?' appears, choose Yes.The corresponding stock posting is processed automatically in background for the complete quantity for Usage Decision codes A1, R1, and R320. |  |
| 8 | Modify Stock Posting (Optional) | In the Inspection Lot Stock section, enter the quantities to be posted to different stock types. | Note If you want to scrap a partial quantity with UD code R310, you can split the quantity and post to To Unrestricted Use and To Scrap, respectively. It is also possible to transfer the (partial or full) quantity to a different material if, for example, inspection results show that the product is of higher/lower quality than initially planned in the production order and the higher/lower quality corresponds to different materials. |  |
| 9 | Save Usage Decision | Choose Save. | The usage decision is made with regard to the manufactured goods. The system automatically triggers the material movements if associated with the usage decision code.Positive Result: The usage decision made for the inspection is Quality Inspection Passed. A goods movement is posted automatically from quality inspection stock to unrestricted use stock for the finished material FG0502.Negative Result: The usage decision made for the inspection is Quality Inspection Failed. A goods movement is posted automatically from quality inspection stock to blocked stock for the finished material FG0502. |  |

##### Display Material Stock After Usage Decision

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, we now verify the material movement done based on the usage decision codes by looking again at the material stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Warehouse Clerk. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Stock - Single Material (F1076). | The Stock - Single Material (F1076) screen displays. |  |
| 3 | Enter Selection Fields | Make the following entries and choose Enter.Material: FG0502 |  |  |
| 4 | Check Stock Quantity | Check the changed quantities of the Quality Inspection Stock, Unrestricted Use Stock (in case of positive usage decision) or Blocked Stock (in case of negative usage decision). | The stock quantities for finished material FG0502 and <Batch ID> are updated based on the quality inspection and respective usage decision of the previous steps. |  |

### Evaluations

#### Batch Information Cockpit - Top-Down and Bottom-Up Analysis

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this functionality you can identify which batches are delivered to which customer and which raw material batches are used for the production of which finished product. You can adapt the selection in the Batch Information Cockpit to customer-specific requirements by creating user-specific groups. You can get additional information by using subsequent actions.

Depending on how you ran through the test case the evaluation is limited to the rework processes or also covers production process. As soon as you have purchased the raw materials and/or delivered the finished good FG0502 to a customer the evaluation is automatically enhanced with these information.

|  |
| --- |
| Note Components booked for the rework order are also subject to the original order batch traceability but not displayed in the Batch Cockpit during Top-Down Analysis. Bottom-Up Analysis is working for this process. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad using the Quality Technician role. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Batch Information Cockpit (BMBC). | The Batch Information Cockpit (Original) screen displays. |  |
| 3 | Select batches | On the Batch Information Cockpit (Original) screen, make the following entries.Go to Material (Original) tab.Material (Original) : FG0502 resp. FG0511Plant: 3310Choose Execute Selection. | One or multiple batches are displayed in the left screen area Selection Result for Batches. The standard sorting is done per material number. |  |
| 4 | Expand selection | In the section Selection Result for Batches. Select Checkbox for FG0502 resp. FG0511 and then choose Expand subtree or Expand node. | The selection result is analyzed and a batch for further investigation is identified. |  |
| 5 | Start Analysis | Right click on one selected batch and choose either Usage (Top-Down) or Usage (Bottom-up). | The batch where-used list displays. |  |
| 6 | Analyze the batch where used list | The usage of the batch can be analyzed and the specific documents (such as batch master record, production orders and sales order) can be accessed via double click. |  |  |
| 7 | Analyze assigned Inspection lots | Mark one line in the Details (Usage) table and choose button Inspection Lots to review inspection lots assigned to the selected element. |  |  |
| 8 | Analyze material document | Choose Details again and choose Usage.Select one document and choose Documents. | The usage displays again and after selecting documents the respective material document display. |  |
| 9 | Go to the material document | Select the material document in the pop up and choose Choose (F2).To display the material document, you need further authorizations that are granted by your company, for example, SAP_BR_INVENTORY_MANAGER. | The material document displays.Note Your user has to have the appropriate authorizations. |  |

## Appendix

### Process Integration

N/A

### Preceding Processes

N/A

### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| Technical Completion of Production Order (Optional) | You can access Schedule Order Technical Completion Run (F3841) app as a Production Supervisor - Discrete Manufacturing to schedule a job to set production orders as Technical Completion.If you need to set a production order as Technical Completion separately, you can access Manage Material Coverage - New Version (F0251A) app as a Production Planner, find your production order and select Delete. |
| 3F0 - Event-Based Production Cost Posting | This procedure updates work-in-process calculation, overhead calculation, and variance calculation by linking the posting to the events.Note Start from CE2105, the default Best Practice content is based on event-based result analysis for new customer install and add new country only, rather than previous period-end posting. For existing customers (who activated content before 2105), the default remain unchanged to Period-End Closing – Plant (BEI) till customer makes the decision to switch. For migration to Event based from Periodic please refer [Production Settlement in Parallel Ledgers](https://help.sap.com/viewer/4032610758dc437089f0c28320eec93f/2105.500/en-US/e49a3770f22547a392455154f3eef6e2.html).If you are still using period-end posting, you may need to refer to non-standard Scope Item BEI - Period-End Closing – Plant. |
| Close Confirmed Production/Process Orders (Optional) | Search for Schedule Order Closing Runs - Close Production/Process Orders (F4305) app as a Production Supervisor - Discrete Manufacturing to schedule a job to set orders as Closed (CLSD). |
| BMC - Core Inventory Management | Complete the following activities:Perform the selected step you want to perform for the Blocked stock. |
| 5HL - Sell from Stock – Consumer Products | You can follow the test script to sell the produced Packed Coffee Beans and Displays from this scope item to the customer. |
| 2V0 - SAP Fiori Analytical Apps for Quality Management | You can follow the test script to analyze the defects and accepted/rejected inspection lots and characteristics in relevant timelines |

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
- related-to :: [[12-production-and-manufacturing/rework-processing-stock-manufactured-material-bjn-ae-test-script-1275]]
- related-to :: [[12-production-and-manufacturing/test-script-rework-processing-work-in-process-bjq-ae-1276]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6A9_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 176,675 chars in the whole document
