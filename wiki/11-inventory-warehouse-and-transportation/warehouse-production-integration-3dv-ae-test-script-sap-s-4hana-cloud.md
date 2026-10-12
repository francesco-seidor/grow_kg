---
id: 11-inventory-warehouse-and-transportation/warehouse-production-integration-3dv-ae-test-script-sap-s-4hana-cloud
title: "Warehouse Production Integration (3DV_AE) - Test Script, SAP S/4HANA Cloud Public Edition (3DV_S4CLD2608_BPD_EN_AE)"
description: "SAP test script for scope item 3DV_AE: staging material to production and goods receipt/putaway of finished goods via Fiori or RF, with prerequisites."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/ewm-production-integration]
aliases: [3DV_S4CLD2608_BPD_EN_AE]
keywords: [EWM Production Supply and Receipt, warehouse production integration, material staging, goods receipt from production, warehouse tasks, putaway warehouse tasks, handling units, radio frequency devices, packing instructions, production orders]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3DV_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-928
topic: 11-inventory-warehouse-and-transportation/ewm-production-integration
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Warehouse Production Integration (3DV_AE) - Test Script, SAP S/4HANA Cloud Public Edition (3DV_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3DV_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **EWM Production Supply and Receipt** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Warehouse Production Integration (3DV_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Warehouse Production Integration (3DV_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232852321)

[2 Prerequisites 4](#_Toc232852322)

[2.1 System Access 4](#_Toc232852323)

[2.2 Roles 4](#_Toc232852324)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232852325)

[2.4 Additional Manual Configuration 8](#_Toc232852326)

[2.5 Business Conditions 8](#_Toc232852327)

[2.6 Preliminary Steps 9](#_Toc232852328)

[2.6.1 Define Default Values for Warehouse Clerk (WM) 9](#_Toc232852329)

[2.6.2 Define Default Values for Warehouse Operative (WM) 9](#_Toc232852330)

[2.6.3 Assign Fixed Storage Bins to Component 10](#_Toc232852331)

[2.6.4 Create Control Cycle 11](#_Toc232852332)

[2.6.5 Change Production Order 11](#_Toc232852333)

[2.6.5.1 Change Production Order for Material SG124 12](#_Toc232852334)

[2.6.5.2 Change Production Order for Material FG228 12](#_Toc232852335)

[2.6.6 Create Initial Stock for Component 13](#_Toc232852336)

[2.6.6.1 Create Initial Stock for Component Using Migration Cockpit 14](#_Toc232852337)

[2.6.6.2 Initial Stock Posting for the Material of BoM 14](#_Toc232852338)

[2.6.7 Manage Packing Instruction 15](#_Toc232852339)

[2.6.7.1 Create Packing Instruction 15](#_Toc232852340)

[2.6.7.2 Create Packing Instruction Determination 16](#_Toc232852341)

[3 Overview Table 18](#_Toc232852342)

[4 Test Procedures 20](#_Toc232852343)

[4.1 Material Staging for Production 20](#_Toc232852344)

[4.1.1 Release Production Order 20](#_Toc232852345)

[4.1.2 Material Staging for Production Order 22](#_Toc232852346)

[4.1.3 Create Staging Warehouse Tasks 24](#_Toc232852347)

[4.1.4 Confirm Staging Warehouse Tasks 25](#_Toc232852348)

[4.1.4.1 Variant 1: With Fiori App 25](#_Toc232852349)

[4.1.4.2 Variant 2: With Radio Frequency Devices 26](#_Toc232852350)

[4.1.5 Post Goods Issue for Staging 28](#_Toc232852351)

[4.2 Confirm Production Operations for Subassembly 29](#_Toc232852352)

[4.3 Delivery-Based Goods Receipt from Production 30](#_Toc232852353)

[4.3.1 Create Inbound Delivery for Production Order 31](#_Toc232852354)

[4.3.2 Create Handling Unit 32](#_Toc232852355)

[4.3.2.1 Variant 1: With Fiori App – Automatic Packing 32](#_Toc232852356)

[4.3.2.2 Variant 2: With Fiori App – Packing at Workcenter 34](#_Toc232852357)

[4.3.2.3 Variant 3: With Radio Frequency Device 37](#_Toc232852358)

[4.3.3 Post Goods Receipt 39](#_Toc232852359)

[4.3.3.1 Variant 1: With Fiori App 40](#_Toc232852360)

[4.3.3.2 Variant 2: With Radio Frequency Device 41](#_Toc232852361)

[4.3.4 Create Putaway Warehouse Tasks 43](#_Toc232852362)

[4.3.4.1 Variant 1: With Fiori App 43](#_Toc232852363)

[4.3.4.2 Variant 2: With Radio Frequency Device 44](#_Toc232852364)

[4.3.5 Confirm Putaway Warehouse Tasks 47](#_Toc232852365)

[4.3.5.1 Variant 1: With Fiori App 47](#_Toc232852366)

[4.3.5.2 Variant 2: With Radio Frequency Devices 48](#_Toc232852367)

[5 Appendix 51](#_Toc232852368)

[5.1 Process Integration 51](#_Toc232852369)

[5.1.1 Preceding Processes 51](#_Toc232852370)

[5.1.2 Succeeding Processes 53](#_Toc232852371)

[5.2 Attachment Handling (Optional) 53](#_Toc232852372)

## Purpose

Overview

With this business process, you can integrate the supply of products to production and the receipt of finished products from production into your warehouse. You first trigger the staging of material that is requested by production. This activity results in an outbound delivery that is distributed to the warehouse as an outbound delivery order (non-WM-managed production supply area). Further process steps such as the creation of warehouse tasks are initiated based on these documents. A warehouse operative moves the material to the production supply area and confirms the warehouse tasks accordingly. If the production storage location is not WM-managed, the goods issue must be posted for the outbound delivery to make the material available for consumption at the production storage location. Finally, the finished goods from production – to be stored in the warehouse – are received and moved to the final bin.

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
| Production Supervisor - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC | Production Management - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC |  |
| Production Operator - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC | Production Execution - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC |  |
| Warehouse Clerk (EWM) | SAP_BR_WAREHOUSE_CLERK_EWM | Warehouse Office | SAP_BR_WAREHOUSE_CLERK_EWM |  |
| Warehouse Operative (EWM) | SAP_BR_WAREHOUSE_OPERATIVE_EWM | Warehouse Floor | SAP_BR_WAREHOUSE_OPERATIVE_EWM |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Master Data Specialist - Handling Unit Data | SAP_BR_HU_MASTER_SPECIALIST | Master Data - Handling Units | SAP_BR_HU_MASTER_SPECIALIST |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | SG124 | SEMI124, PD, Subassembly | 1 PAL = 8 PCUse this material to test the MM-IM-managed production supply process. |
| Material | RM124 | RAW124, VB, Consumption, FixedBin | 1 PAL = 100 PCComponent for SG124. |
| Material | CM-MLFL-KM-VXX | Multilevel Forklifter | This is a multilevel configurable material. One of its component is also a configurable material. Use this material for integration with Make-to-Order Production with Variant Configuration. |
| Material | CM-FL-V00 | Configurable Forklifter | This is a single level configurable material. Use this material for integration with Make-to-Order Production with Variant Configuration and Make-to-Stock Production with Variant Configuration. |
| Material | FG-FL-MV-V00 | Forklifter Material Variant | This is a material variant. Use this material for integration with Make-to-Stock Production with Variant Configuration. |
| Material | FG-FL-MV-V01 | Forklifter Material Variant | This is a material variant. Use this material for integration with Make-to-Stock Production with Variant Configuration. |
| Material | FG-FL-MV-V02 | Forklifter Material Variant | This is a material variant. Use this material for integration with Make-to-Stock Production with Variant Configuration. |
| Material | FG228 | FIN228,MTO,PD,Batch-Fifo,SerialNo | Use this material to test goods receipt from production within an MTO scenario. |
| Material | SG22 | SEMI22,PD,Phantom | Component for FG228 |
| Material | SG25 | SEMI25,PD,ExternalProcurement | Component for FG228 |
| Material | RM122 | RAW122,PD,Batch-Fifo,ProcureImport | Component for FG228 |
| Material | RM128 | RAW128,PD,Consignment | Component for FG228 |
| Material | RM120 |  | Component for FG228 |
| Material | SG224 | SEMI224,MTO,PD,Subassembly | Component for FG228 |
| Material | RM27 | RAW27,PD,PackagingBox | Component for FG228 |
| Production Version | 0001 | Production Version 1 | Production versions of materials FG126, FG228, SG22 and SG224 |
| Production Version | 0090 | Production Version 90 | Production version of material SG124 |
| Packaging Material | PMPALLET_GTL | Pallet for GTL |  |
| Company Code | 3310 |  |  |
| Plant | 3310 |  |  |
| (Replenishment) Storage Location | 335W |  |  |
| Production Supply Area | PSA_01 | IM-managed Sloc | This is a production supply area in an MM-IM-managed storage location. Use this to stage material for production where the source storage location is WM-managed and the destination storage location is MM-IM-managed. |
| Warehouse Number | 335 |  |  |

Organizational Master Data in Warehouse:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Warehouse | 3350 |  |  |
| Custodian | 33413310 |  |  |
| Entitled to Dispose | 33413310 |  |  |

Warehouse-Specific Master Data:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Storage Type | SF01 | Fixed Bin Storage |  |
| Storage Type | SB01 | Bulk Storage |  |
| Storage Type | S105 | Production Supply |  |
| Storage Type | S915 | Goods Receipt from Production |  |
| Storage Type | S970 | Clarification Zone |  |
| Storage Type | S001 | Storage |  |
| Storage Type | SG01 | General Storage |  |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

| MDS | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| 3KQ | Maintain Warehouse Products Attributes - MDS |
| 3KR | Maintain Storage Bins and Fixed Bin Assignments - MDS |
| 3KS | Maintain Production Supply Area - MDS |
| 40D | Create Production Supply Area - MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/9fd25d2778494202ed3151a2dff72670)

Before you start the testing, please make sure that the steps in the [Warehouse Management Setup Guide.docx (Public)](https://support.sap.com/content/dam/SAAP/SAP_Activate/S4H_588%20Warehouse%20Management%20Setup.docx) published on SAP Activate Roadmap Viewer have been completed.

If you are working with a radio frequency device, carry out the steps described in Mobile RF Devices in Warehousing (63V).

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | You’ve completed the step described in the Create New Open MM Posting Period - MDS (BNZ) master data script. The posting period is up to date. |
| BJ5 - Make-to-Stock Production – Discrete Manufacturing | Planned orders are a prerequisite for the process. Make sure the following steps are fulfilled:Anonymous Forecast and MRPCreate Planned Independent RequirementsMaterial Requirements Planning at Plant LevelEvaluate Stock/Requirements SituationProduction Order Conversion and Available-to-Promise CheckConversion to Production Orders for Subassembly and Final AssemblyNote down the production order number for SG124. |
| BJE - Make-to-Order Production – Finished Goods Sales and Final Assembly | To test an MTO process, perform below test steps in BJE - Make-to-Order Production – Finished Goods Sales and Final Assembly.When creating the sales order, before saving, select the order item and then choose More > Go to > Item > Shipping . In section Shipping, enter the Storage Location value as a warehouse-managed storage location (e.g. Storage Location 335W). In section Production Processing, proceed until the completion of the Confirm Assembly Activities step. Afterwards, continue with step Create Inbound Delivery for Production Order in this test script. Use material FG228.MTO Sales Processing (Material w/o Sales Order BoM)Down Payment ProcessingProduction PlanningProduction Processing |

### Preliminary Steps

#### Define Default Values for Warehouse Clerk (WM)

Purpose

In this step, you can define the default warehouse number for the Warehouse Clerk (EWM).

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk (EWM). |  |  |
| 2 | Choose Avatar | Choose your avatar.Then, choose Settings. |  |  |
| 3 | Enter Default Value | Choose Default Values.Enter the following data:Warehouse Number: 3350.Choose Save. |  |  |

#### Define Default Values for Warehouse Operative (WM)

Purpose

In this step, you can define the default warehouse number for the Warehouse Operative (EWM).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Operative (EWM). | The Fiori launchpad is displayed. |  |
| 2 | Choose Avatar | Choose your avatar.Then, choose Settings. |  |  |
| 3 | Enter Default Value | Choose Default Values.In the Material Management section, enter the following data:Warehouse Number: 3350.Choose Save. |  |  |

#### Assign Fixed Storage Bins to Component

Purpose

In this step, you assign fixed storage bins to products.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk (EWM). | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Assign Fixed Bins (/SCWM/BINMAT). | The Assign Fixed Storage Bins screen displays. |  |
| 3 | Enter Data | On the Assign Fixed Storage Bins screen, enter the following data:Warehouse Number: 3350Product: RM124 .Choose Run. |  |  |
| 4 | Maintain Fixed Bin | Choose Edit to switch to change mode.Choose Create.Enter the following data:WhN: 3350.Disposal: 33413310Storage Bin: SF01-03-04 .Product: RM124 .Choose Save. |  |  |
|  |  |  |  |  |

#### Create Control Cycle

Purpose

In this activity, you create a control cycle that can be used for in-house production in the production supply area. In the control cycle, you define the demand source, the supply source, and the material staging indicator. The material staging indicator defines the method of how needed materials can be supplied for production with the assistance of the warehouse management system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Create Control Cycle for WM (LPK1). | The Create Control Cycle: Initial Screen (WM) screen is displayed. |  |
| 3 | Enter Data | Make the following entries and choose Enter.Material: RM124 .Plant: 3310.Supply Area: PSA_01. | The Create Control Cycle: Data Screen (WM) screen is displayed. |  |
| 4 | Enter Control Cycle Details | Make the following entries and choose Enter.In the Destination section:Staging Ind.: 3 (Release Order Part).In the Source section:Stor. Location: 335W.Choose Enter.Warehouse No.: 335.In the Destination Bin Assignment section:Destination Bin: PROD-SUPPLYChoose Save. | The Destination Stor. Location and Source Issuing Plant fields are automatically filled by the system.The Source Warehouse No. is not for input initially and it is automatically filled after entering the Source Storage Location.You’ve created the control cycle for material RM124 . |  |

#### Change Production Order

Purpose

In this step, you adjust data in the production order for the materials SG124 and FG228.

##### Change Production Order for Material SG124

Purpose

In this step, you adjust data in the production order for material SG124.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Supervisor - Discrete Manufacturing. |  |  |
| 2 | Access App | Open Change Production Order(CO02). | The Manage Production Orders (Original) screen is displayed. |  |
| 3 | Enter Order Number | Enter the order for SG124 and choose Continue. |  |  |
| 4 | Update Order Quantity | Make the following changes:Total Qty: 1 PAL. |  |  |
| 5 | Update Storage Location | Choose the Goods Receipt tab.Update the storage location as follows:Stor. Loc.: 335W. |  |  |
| 6 | Update Production Version | Choose More > Functions > Read PP Master Data.On the Read PP master data screen, update the production version as follows:Production Version: 0090.Choose Continue. |  | Update Production Version |
| 7 | Save | Save your entries. | A system message tells you that the corresponding order number is saved. |  |

##### Change Production Order for Material FG228

Purpose

In this step, you adjust data in the production order for material SG124.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Supervisor - Discrete Manufacturing. |  |  |
| 2 | Access App | Open Change Production Order(CO02). | The Manage Production Orders (Original) screen is displayed. |  |
| 3 | Enter Order Number | Enter the order for FG228 and choose Continue. |  |  |
| 4 | Update Storage Location | Choose the Goods Receipt tab.Update the storage location as follows:Stor. Loc.: 335W. |  |  |
| 5 | Save | Save your entries. | A system message tells you that the corresponding order number is saved. |  |

#### Create Initial Stock for Component

Purpose

Create enough raw material stock for staging to production.

Prerequisite

Before creating initial material stocks, we recommend that you check the stock levels for the finished and semi-finished goods. To do that, log onto the SAP Fiori launchpad as a Production Plan-ner, and open the Manage Material Coverage (F0251A) app. Remove stock or increase the requirement quantity if there is already a sufficient amount of stock available. Otherwise, no planned orders can be generated later.

|  |
| --- |
| Note Example: For the following semi-finished materials planned orders must be created during the step Material Requirements Planning at Plant Level: SG124 |

Procedure

During the process step Material Requirements Planning at Plant Level of scope item Make-to-Stock Production - Discrete Manufacturing (BJ5) receipt elements are created. Depending on the elements created in the MRP run, refer to Procurement of Direct Materials (J45) or Scheduling Agreements in Procurement (BMR) test scripts for processing externally-procured materials.

Use process step Post Goods Receipt for Purchase Orders from scope item Warehouse Inbound Processing with Synchronous Goods Receipt (5HN) to receive stock in the warehouse.

|  |
| --- |
| Note Example: For the following raw materials sufficient stock in the warehouse must exist: RM124 |

##### Create Initial Stock for Component Using Migration Cockpit

Refer to the Data Migration to SAP S/4HANA from Staging (2Q2) scope item to create initial stock for RM124 in the SF01 fixed-bin storage type and for RM224 in the SG01 general storage type of the 335W warehouse. Execute the whole process.

You can find the document here [2Q2](https://me.sap.com/processnavigator/SolS/EARL_SolS-013/2308/SolP/2Q2?region=DE).

##### Initial Stock Posting for the Material of BoM

|  |
| --- |
| Note Initial stock posting is not required if you want to excute complete procurement or semifinished component production processes for selected materials in the multilevel BoM of FG228 and FG227.For the semifinished material SG224, you can either post initial stock here, or run through Make-to-Order Production – Semifinished Goods Planning and Assembly (1BM) scope item first to produce enough stock before creating sales orders for finished goods.For the semifinished material SG21, you can either post initial stock here, or run through Make-to-Stock Production – Repetitive Manufacturing (BJH) scope item to produce enough stock via repetitive manufacturing process.For the remaining semifinished and raw materials in the multilevel BoM of FG228 or FG227 you can post initial stock. |

Purpose

This process step shows you how to post initial stock for BoM materials of FG228 and FG227.

|  |
| --- |
| Note Alternatively, you can run the procurement scope items. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO) | The Goods Receipt Other - XXX (your user name) screen displays. |  |
| 3 | Enter Details | Choose Goods Receipt and Others on top of the screen.In the Detail Data section, make the following entries and press Enter. Select Next Item icon to add entries.On the Where tab:Goods Movement Type: 561 (Init.entry of stBal.)Plant: 3310Storage Location: 331BOn the Quantity tab:Quantity: <Quantity>, for example, <100>On the Material tab:Material: <BOM Material>, see the Bill of Material Structure for FG228 and FG227 in the Master Data, Organizational Data, and Other Data section for a detailed materials list.Run through Make-to-Order Production – Semifinished Goods Planning and Assembly (1BM) test script if you do not want to post initial stock for SG224.Select Item OK, and choose Check. | A message displays: The Document is OK. You also post initial stock for material RM20 in case you test with material FG227. |  |
| 4 | Post | Confirm the message that the batch has been created and choose Post. | A message displays: Material document XXXXXXXX posted. |  |

#### Manage Packing Instruction

##### Create Packing Instruction

Purpose

In this step, you create a packing instruction.

A packing instruction serves as a template for the creation of a handling unit. In a packing instruction, you define the materials and packaging materials to be packed in a handling unit.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Handling Unit Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Packing Instruction - Master Data (POP1). | The Create Packing Instruction: Initial screen displays. |  |
| 3 | Create Packing Instruction | To create a new packing instruction, choose Continue or Enter.If you want to create a packing instruction from a reference packing instruction, choose a reference packing instruction and then Enter. |  |  |
| 4 | Maintain the description of Packing Instruction | Enter the short text field for the description of the packing instruction. |  |  |
| 5 | Enter Packaging Material | Enter the package material number in field Component of item 10, for example PMPALLET.The Item category P of item 10 means packaging materials. The first line is mandatory for every packing instruction because every packing instruction needs at least 1 packaging material. |  |  |
| 6 | Maintain material and target quantity | In item 20, make the following entries:Item category: M Material.Component: Material number to be packed, for example, SG124.Target quantity: Quantity |  |  |
| 7 | Enter Check Profile | On the Admin.data tab, enter 01 in the Check Profile field.01 is the pre-delivered SAP Standard Profile. |  |  |
| 8 | Save | Choose Save.Make a note of the packing instruction number: _____. | A packing instruction is created. |  |
| 9 | Create Alternative Packing Instructions | Repeat steps 2 to 8 to create an alternative Packing Instruction with the same component, but different packing material and quantity. |  |  |

##### Create Packing Instruction Determination

Purpose

In this step, you create packing instruction determination records.

This function enables the system to find a packing instruction by specific characteristics. The condition technique is applied for this. You define a packing instruction that refers to specific characteristics, such as material and ship-to-party.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Handling Unit Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Determination Records - Master Data (POF1). | The Pkg Instruction - Create Determination Recs: Initial screen is displayed. |  |
| 3 | Enter Determination Type | On the Pkg Instruction - Create Determination Recs: Initial screen, make the following entries:Determination Type: 0IBD – Inbound Delivery WM.Choose Enter.Note For the determination of the packing instruction with determination types 0IBD only the following fields can be used:Warehouse NumberVendorMaterial |  |  |
| 4 | Choose a key combination | On the key combination screen, choose a key combination, and select Choose.For example, choose WhseNmbr/Vendor/Material. |  |  |
| 5 | Enter the Packing Instruction Determination | On the Create Inbound Delivery WM (0IBD): Fast Entry screen, make the following entries:Warehouse Number: for example, 1050Supplier: <The supplier number>Material: for example SG124Packing instruction: <The Packing instruction number noted in the previous section>Altern.pack.instr. 1 : <The Alternative Packing instruction number noted in the previous section> |  |  |
| 6 | Save | Choose Save. | The packing instruction determination is created. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Material Staging for Production](#unique_22) [page ] 20 |  |  |  |
| [Release Production Order](#unique_23) [page ] 20 | Production Supervisor - Discrete Manufacturing | Manage Production Orders (F2336) | You have released the production order. |
| [Material Staging for Production Order](#unique_24) [page ] 22 | Production Operator - Discrete Manufacturing | Stage Materials for Production (MF60) |  |
| [Create Staging Warehouse Tasks](#unique_25) [page ] 24 | Warehouse Clerk (EWM) | Manage Outbound Delivery Orders (F6498) | You have created the staging warehouse tasks. |
| [Confirm Staging Warehouse Tasks](#unique_26) [page ] 25 |  |  | You have confirmed the staging warehouse tasks. |
| [Variant 1: With Fiori App](#unique_27) [page ] 25 | Warehouse Operative (EWM) | Process Warehouse Tasks - Picking (F3880) |  |
| [Variant 2: With Radio Frequency Devices](#unique_28) [page ] 26 | Warehouse Operative (EWM) | Test RF Environment (/SCWM/RFUI) |  |
| [Post Goods Issue for Staging](#unique_29) [page ] 28 | Warehouse Clerk (EWM) | Manage Outbound Delivery Orders (F6498) | You have posted the goods issue for staging. |
| [Confirm Production Operations for Subassembly](#unique_30) [page ] 29 | Production Operator - Discrete Manufacturing | Confirm Production Operation (F3069) |  |
| [Delivery-Based Goods Receipt from Production](#unique_31) [page ] 30 |  |  |  |
| [Create Inbound Delivery for Production Order](#unique_32) [page ] 31 | Warehouse Clerk | Post Goods Movement (MIGO) |  |
| [Create Handling Unit](#unique_33) [page ] 32 |  |  | You have created the handling unit. |
| [Variant 1: With Fiori App – Automatic Packing](#unique_34) [page ] 32 | Warehouse Clerk (EWM) | Manage Inbound Deliveries – Warehouse (F7922) |  |
| [Variant 2: With Fiori App – Packing at Workcenter](#unique_35) [page ] 34 | Warehouse Clerk (EWM) | Manage Inbound Deliveries – Warehouse (F7922) |  |
| [Variant 3: With Radio Frequency Device](#unique_36) [page ] 37 | Warehouse Operative (EWM) | Test RF Environment (/SCWM/RFUI) |  |
| [Post Goods Receipt](#unique_37) [page ] 39 | Warehouse Clerk (EWM) | Manage Inbound Deliveries – Warehouse (F7922) | You have posted the goods receipt. |
| [Variant 1: With Fiori App](#unique_38) [page ] 40 | Warehouse Clerk (EWM) | Manage Inbound Deliveries – Warehouse (F7922) |  |
| [Variant 2: With Radio Frequency Device](#unique_39) [page ] 41 | Warehouse Operative (EWM) | Test RF Environment (/SCWM/RFUI) |  |
| [Create Putaway Warehouse Tasks](#unique_40) [page ] 43 | Warehouse Clerk (EWM) | Manage Inbound Deliveries – Warehouse (F7922) | You have created putaway warehouse tasks. |
| [Variant 1: With Fiori App](#unique_41) [page ] 43 | Warehouse Clerk (EWM) | Manage Inbound Deliveries – Warehouse (F7922) |  |
| [Variant 2: With Radio Frequency Device](#unique_42) [page ] 44 | Warehouse Operative (EWM) | Test RF Environment (/SCWM/RFUI) |  |
| [Confirm Putaway Warehouse Tasks](#unique_43) [page ] 47 |  |  | You have confirmed the putaway warehouse tasks. |
| [Variant 1: With Fiori App](#unique_44) [page ] 47 | Warehouse Operative (EWM) | Process Warehouse Tasks - Putaway (F4150) |  |
| [Variant 2: With Radio Frequency Devices](#unique_45) [page ] 48 | Warehouse Operative (EWM) | Test RF Environment (/SCWM/RFUI) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Material Staging for Production

In this section, you stage material for production.

#### Release Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A release at order operation level results in the order and all its operations being released. The order and the operations receive the REL (released) status.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Production Orders (F2336). | The Manage Production Orders (F2336) screen is displayed. |  |
| 3 | Check Default Area of Responsibility (Supervisor) | On the Manage Production Orders screen, maintain the following entries:Check the default area of responsibility (supervisor) by choosing your avatar (from the top-left corner) and selecting App Settings > Area of Responsibility Production Supervisor. Check that only this entry is displayed:Plant 1 AE 3310.MTS DI - Valuated (YB1). | If there's no Plant 1 AE3310 entry in the Area of Responsibility (Supervisor) dialog box, choose Add to select it and then OK. For other plant entries in the Area of Responsibility (Supervisor) dialog box, choose Delete to remove the others and then choose OK. |  |
| 4 | Select Production Order | On the Manage Production Orders (F2336) screen, enter the following search conditions as a filter.Choose Adapt Filters to display more selection filters. Choose More filters under Production Orders. Select the checkbox for Material and Production Plant and choose OK. Then, choose Go. The Material and Production Plant fields are then added to the filter bar.Status: Created.Material: SG124 .Production Plant: 3310.Choose Go to execute. | The Manage Production Orders (F2336) screen is displayed. |  |
| 5 | Select Order | On the Manage Production Orders (F2336) screen, select your production order by choosing the checkbox beside the order number.Choose Edit. | The Manage Production Orders (F2336) screen is displayed. |  |
| 6 | Execute Release | Choose Menu > Functions > Release . | In case there is a sufficient quantity of components on stock, the system message Release carried out is displayed. Continue with step 8.In case there is insufficient stock, the Release Order dialog box is displayed. Continue with step 7. |  |
| 7 | Release Order | Choose Release Order. | A system message tells you that the release is carried out, and refers to the log. |  |
| 8 | Save | Save your entries. | A system message tells you that the corresponding order number is saved. |  |

#### Material Staging for Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you stage materials for production using production supply area PSA_01 and materials FG126 and SG124 .

If there is sufficient stock available in the production storage location 331B, no line items are generated.

|  |
| --- |
| Note PSA_01 is Production Supply Area in an inventory managed storage location. To work with WM-managed production supply area , for example PSA_02, you can refer to the process as described in scope item 5HO - Warehouse Production Integration with Synchronous Goods Receipt |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Stage Materials for Production (MF60). | The Material Staging for Planned Orders screen is displayed. |  |
| 3 | Enter Details | On the Material Staging for Planned Orders screen, make the following entries:Staging TypesSelect the SLocLevel checkbox.Plant: 3310.Selection Horizon for Remts: <date must be in the future - after scheduled start date of the production order>.ComponentsNote Material: RM124Production Supply Area: PSA_01. | The Pull List: Storage Location Level screen is displayed. |  |
| 4 | Navigate to Production/Process Orders Tab | Navigate to the Production/Process Orders tab. |  |  |
| 5 | Enter Order | On the Production/Process Orders tab, make the following entries:Production Order: <your production order number>. |  |  |
| 6 | Choose Global Settings | Choose Global Settings. | The Global Settings dialog box appears. |  |
| 7 | Navigate to Dialog Control Tab | In the Global Settings dialog box, choose Dialog Control. |  |  |
| 8 | Make Entries | On the Dialog Control tab, in the logging section, select the display message log automatically checkbox. |  |  |
| 9 | Choose Continue | Choose Continue. |  |  |
| 10 | Choose Execute | On the Material Staging for Production / Process Orders screen, choose Execute.If the following system message is displayed: Supply area at storage location level only partly effective, just choose Enter. | The Pull List: Storage Location Level screen is displayed. |  |
| 11 | Choose Replenishment Elements | On the Pull List: Storage Location Level screen, select the required line items from the left-hand margin and choose Replenishment Proposal at the top of the screen. | The Quantity staged field is populated. |  |
| 12 | Choose Replenishment Elements | Review the staged quantity and choose Replenishment Elements. | The Replen. Elements table is displayed. |  |
| 13 | Check or Enter Replenishment Storage Location | At the bottom half of the split screen, select the lines and check or make the following entries:Replenishment storage location: 335W. |  |  |
| 14 | Choose stage | Select the Replenishment Element line and choose Stage at the center of the screen. | The Staging cell is populated with Element Checked: OK. |  |
| 15 | Choose Save | Choose Save.Note down the delivery number.Note The delivery is not yet saved in the data base. Make sure to complete the next step before you search your delivery in the system. | The log with the following system message appears: EWM release order delivery <delivery number> successfully generated for RM124 |  |
| 16 | Choose Back | Choose Exit in the upper right corner of the screen. | The following system message appears: Data posted successfully. |  |

#### Create Staging Warehouse Tasks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create pick warehouse tasks for the staging process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk (EWM). |  |  |
| 2 | Access App | Manage Outbound Delivery Orders (F6498) | The Manage Outbound Delivery Orders (F6498) screen displays |  |
| 3 | Enter Warehouse Number | On the Manage Outbound Delivery Orders screen, make the following entries.Warehouse No: 3350. |  |  |
| 4 | Select Filters | On the Manage Outbound Delivery Orders screen, select Adapt Filters. | The Adapt Filters dialog box is displayed. |  |
| 5 | Select Filters | In the Adapt Filters dialog box, find Document Number. Select the checkbox for Document Number and choose OK. | The Document Number filter criteria is displayed on the Manage Outbound Delivery Orders screen. |  |
| 6 | Enter Filter Criteria | On the Manage Outbound Delivery Orders screen, enter your Delivery, and choose Go. |  |  |
| 7 | Create Warehouse Tasks | Mark your outbound delivery and choose Create Pick Warehouse Tasks to create the warehouse tasks. | The following system message appears: Pick warehouse task(s) created. |  |
| 8 | Choose Outbound Delivery Order | Choose your Outbound Delivery Order to find the created warehouse task. | The Outbound Delivery Order details are displayed on the right side of the screen. |  |
| 9 | Choose Warehouse Tasks | Scroll down to the Others section and choose Yes under Process Relevant WTs . | The Process Warehouse Tasks screen is displayed. |  |
| 10 | Note Down Warehouse Task Number | Note down the warehouse task number. |  |  |

#### Confirm Staging Warehouse Tasks

In this section, you confirm the staging warehouse tasks you created in the previous steps. You can confirm the warehouse tasks using a Fiori app or using radio frequency devices.

##### Variant 1: With Fiori App

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A put-away list / warehouse tasks list / pick list is printed and handed over to the Warehouse Operative (EWM), who performs the warehouse tasks and confirms them in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Operative (EWM). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Process Warehouse Tasks - Picking (F3880). |  |  |
| 3 | Enter your Warehouse Task | On the Process Warehouse Tasks - Picking screen, make the following entries:Warehouse Task: <WT number noted down in the previous step>.Choose Go. |  |  |
| 4 | Confirm Warehouse Task | Mark the checkbox for the selected warehouse task and choose Confirm. | The following system message appears: Warehouse task confirmed. |  |

##### Variant 2: With Radio Frequency Devices

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Operative (EWM) performs the warehouse tasks and confirms them in the system with mobile radio frequency device.

|  |
| --- |
| Note To work with mobile RF devices, make sure all the steps as described in the set up instruction guide for scope item 63W - Mobile RF Devices in Warehousing with Production Integration are performed. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Fiori launchpad | Log on to the SAP Fiori Launchpad as a Warehouse Operative (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open the SAP Fiori app Test RF Environment (/SCWM/RFUI)Note The app allows you to test working in an RF environment. For working with mobile RF devices, see also SAP Note [3048632](https://me.sap.com/notes/3048632). |  |  |
| 3 | Enter Data for RFUI | Whse No: 3350Resource: SHR1-1Dflt Dvc.: SE01Choose Enter. |  |  |
| 4 | Choose Menu | Choose 01 System-Guided > 02 SystemGuided Queue. |  |  |
| 5 | Enter Queue Name | In the Queue field, enter for example SR-F01-105.Choose Enter. |  |  |
| 6 | Create Picking HU | Make the following entries:Pack.Mat: PMPALLETChoose Handling.The picking HU is created. |  |  |
| 7 | Choose Next | Scroll the screen to the right with > and choose Next. |  |  |
| 8 | Enter or Verify the Source Information fields | Enter or verify the following fields, if they are required:Src.Bin (Source Bin)Prod. (Product)ActQty (Quantity)Choose Enter. |  |  |
| 9 | Verify the Destination information fields | Verify the following fields:DstBin (Destination Bin)Choose Enter. |  |  |
| 10 | Repeat Steps | Repeat steps 6 to 9 until no suitable warehouse orders are found. |  |  |
| 11 | Log off RFUI | You can choose Back to go to the previous screens.Choose Logoff.Choose Save. |  |  |

#### Post Goods Issue for Staging

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you post the goods issue (GI) for the staging outbound delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk (EWM). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Manage Outbound Delivery Orders (F6498) | The Manage Outbound Delivery Orders (F6498) screen displays |  |
| 3 | Enter Warehouse Number | On the Manage Outbound Delivery Orders screen, make the following entries.Warehouse No: 3350. |  |  |
| 4 | Select Filters | On the Manage Outbound Delivery Orders screen, select Adapt Filters. | The Adapt Filters dialog box is displayed. |  |
| 5 | Select Filters | In the Adapt Filters dialog box, find Document Number. Select the checkbox for Document Number and choose OK. | The Document Number filter criteria is displayed on the Manage Outbound Delivery Orders screen. |  |
| 6 | Enter Filter Criteria | On the Manage Outbound Delivery Orders screen, enter your Delivery, and choose Go. |  |  |
| 7 | Create Warehouse Tasks | Mark your outbound delivery and choose Post Goods Issue to post goods issue for your delivery. | The following system message appears: Goods issue posted. |  |

### Confirm Production Operations for Subassembly

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The confirmation documents include the processing status of orders, operations, sub-operations, and individual capacities. It's an instrument for controlling orders. This process step shows you how to confirm subassembly production order operations for semifinished material SG124 . A goods movement document is generated when the last operation is confirmed. The backflush is carried out together with the confirmation steps.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Confirm Production Operation (F3069). |  |  |
| 3 | Enter Production Order and Operation | On the Enter Order and Operation screen, make the following entries and choose Go:Order: <Production Order Number for semifinished goods>Operation: <operation number> for example, <0010> |  |  |
| 4 | Enter Quantities Data | In the Quantities section, make the following entries:Yield: <Quantity of prod. order less scrap>Scrap: <scrap amount> |  |  |
| 5 | Check Material Movements | In the Material Movements section, check the material list.Note The system shows you an overview materials table for which the material withdraws are done along with operation confirmation.The material RM124 , is set for backflush (in material master) for withdraws to be done automatically after the operation is confirmed. |  |  |
| 6 | Enter Activities Data and Save | In the Activities section, make the following entries:Setup: <setup time>Machine: <machine time>Labor: <labor time>For partial confirmation, choose Post.For final confirmation, choose Post and Complete. | Confirmation is made. |  |
| 7 | Repeat Steps | Go back and repeat steps 3 to 6 for Operation 0020. |  |  |
| 8 | Good Receipt | When all Operations are finally confirmed all materials consumed in production are backflushed. | backflush for all consumed materials is done. |  |

### Delivery-Based Goods Receipt from Production

Purpose

This section describes the warehouse task creation and processing for goods receipt from production.

|  |
| --- |
| Note The realization of the goods receipt process based on deliveries or synchronous goods movements isn't dependent on how the staging is done earlier in the process. In this example, you staged material to production using the IM-managed PSA PSA_01 with the corresponding materials FG126 and SG124. You book a goods receipt from production using deliveries. |

#### Create Inbound Delivery for Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the Warehouse Clerk creates the inbound delivery for the production order by posting the goods receipt (GR) for the production order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Post Goods Movement (MIGO). |  |  |
| 3 | Post Goods Receipt | Choose Goods Receipt and Order.Enter the released production order that you’ve created in the previous step.Goods Movement Type: 101 (GR Goods Receipt).Choose Enter. Then, choose Where tab.Storage Location: 335W.Check Item Ok.Choose Post.Note An additional storage location 335I and the corresponding availability group 002 can be introduced in the Cloud WM as an optional setup. Compared to the single storage location 335W / availability group 001 setup, the new setup can help distinguish stock that is still in the process of putaway and that is already in the warehouse.For example, the storage location 335I is used as the goods receipt storage location. During the goods receipt process, the stock remains in the storage location 335I and isn't available for sale (Stock Type F0 – Unrestricted Use in Putaway) until the putaway warehouse task(s) is/are confirmed. Once the putaway is finished, the stock is automatically posted to the storage location 335W and becomes available for sale (Stock Type F – Unrestricted Use in Warehouse).To enable the 335I storage location / availability setup, there are manual setup steps to be performed according to the instructions provided in the Warehouse Management Setup Guide. For more information, see chapter Additional Manual Configuration. |  |  |
| 4 | Note Down Inbound Delivery Number | Note down the inbound delivery number. |  |  |

#### Create Handling Unit

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This section describes the creation of handling units as preparation for the putaway of products.

##### Variant 1: With Fiori App – Automatic Packing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, the Warehouse Clerk chooses the delivery and creates handling units for Unpacked Items. The Warehouse Clerk can push a single button and then the system automatically packs all delivery items based on the packing instructions defined upfront (enabled by the Unified Package Builder).

|  |
| --- |
| Note The automatic packing works, if packing instructions are defined for the relevant product. |

Handling unit management is not a general prerequisite of production integration. In this example process, creating handling units is mandatory only due to the bulk storage type to which material SG124 is put away to. Therefore, using material SG124, you create handling units and pack your material in this step.

In case you want to store unpacked material, you should use the general storage type, the standard storage type, or your own storage type without HU requirements instead.

Skip this step, if you are using configurable materials and material variants. For material FG228, this step is optional.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Fiori Launchpad | Log on to the SAP Fiori launchpad as a Warehouse Clerk (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open the SAP Fiori app Manage Inbound Deliveries – Warehouse (F7922). | The Manage Inbound Deliveries – Warehouse (F7922) screen appears. |  |
| 3 | Choose Filters | On the Manage Inbound Deliveries screen, choose AdaptFilters. | The AdaptFilters dialog box appears. |  |
| 4 | Select Fields for Filter | On the Adapt Filters dialog box, make sure the following fields are selected for the current filter:Planned Delivery Date/TimeManufacturing Order.Choose OK. |  |  |
| 5 | Search for Inbound Delivery | On the Manage Inbound Deliveries screen, make the following entries:Manufacturing Order: <your production order number>.Adjust the Planned Delivery Date/Time, if necessary.Choose Go. | Your inbound delivery is displayed. |  |
| 6 | Select Inbound Delivery | On the Manage Inbound Deliveries screen, select your inbound delivery. |  |  |
| 7 | Choose Details | Choose button Details. | Inbound delivery details are displayed. |  |
| 8 | Select Unpacked Items | On the Manage Inbound Deliveries screen in the Items section, choose the Unpacked Items tab and select the items to be packed. |  |  |
| 9 | Decide Packing Options | If packing instructions are defined for all the delivery items, you can pack automatically. In this case, follow step 10.If no packing instructions are defined for all the delivery items, you can pack manually. In this case, follow steps 11 to 13. |  |  |
| 10 | Pack Automatically | On the Manage Inbound Deliveries – Warehouse screen, choose Pack Automatically to pack all unpacked items automatically based on the packing instructions. |  |  |
| 11 | Choose Create HU | Choose Create Mixed HUs. |  |  |
| 12 | Enter Packaging Material and Number of HUs | In the Create Handling Unit dialog box, make the following entries:Pack. Material: PMPALLETNumber of HUs: <number of handling units> |  |  |
| 13 | Choose Create | Choose Create. | The delivery items are removed from the Unpacked Items section. |  |
| 14 | Note Down your Delivery Number | Note down your delivery number for testing purposes. | On the Manage Inbound Deliveries screen on the Total Items tab, it showsNo. of H U : X |  |

##### Variant 2: With Fiori App – Packing at Workcenter

Purpose

In this process step, the Warehouse Clerk (EWM) creates handling units for unpacked items in the packing work center. Automatic packing is also enabled by the Unified Package Builder, if packing instructions are defined upfront for the relevant product.

Handling unit management is not a general prerequisite of production integration. In this example process, creating handling units is mandatory only due to the bulk storage type to which material SG124 is put away to. Therefore, using material SG124, you create handling units and pack your material in this step.

In case you want to store unpacked material, you should use the general storage type, the standard storage type, or your own storage type without HU requirements instead.

Skip this step if you are using configurable materials and material variants. For material FG228, this step is optional.

If the products have the C-serial number profile (serialization in stock) assigned and are to be packed into HUs, you can assign serial numbers in this step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Fiori Launchpad | Log on to the SAP Fiori launchpad as a Warehouse Clerk (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open the SAP Fiori app Manage Inbound Deliveries – Warehouse (F7922). | The Manage Inbound Delivery screen appears. |  |
| 3 | Choose Filters | On the Manage Inbound Deliveries screen, choose AdaptFilters. | The Adapt Filters dialog box appears. |  |
| 4 | Select Fields for Filter | On the Adapt Filters dialog box, make sure the following fields are selected for the current filter:Planned Delivery Date/TimeManufacturing Order.Choose OK. |  |  |
| 5 | Search for Inbound Delivery | On the Manage Inbound Deliveries screen, make the following entries:Manufacturing Order: <your production order number>.Adjust the Planned Delivery Date/Time, if necessary.Choose Go. | Your inbound delivery is displayed. |  |
| 6 | Select Inbound Delivery | On the Manage Inbound Deliveries screen, select your inbound delivery. |  |  |
| 7 | Choose Details | Choose button Details. | Inbound delivery details are displayed. |  |
| 8 | Go to Packing Work Center | On the Manage Inbound Deliveries screen, choose Related Apps – Work Center Packing for Inbound Delivery. |  |  |
| 9 | Decide Packing Options | If packing instructions are defined for all the delivery items, you can pack automatically. In this case, follow step 10.If packing instructions are defined for some of the delivery items, you can pack those items based on packing proposals. In this case, follow steps 11 and 12.You can also pack completely manually. In this case, follow steps 13 to 15. |  |  |
| 10 | Pack Automatically | On the Work Center Packing for Inbound Delivery (Time Zone CET) screen, select all the delivery items and then choose Pack Automatically. | HUs are created automatically according to the predefined packing instruction. |  |
| 11 | Pack with Packing Proposals | On the Work Center Packing for Inbound Delivery (Time Zone CET) screen, select one of the delivery items (with Packing Instruction defined) and then choose Packing Proposal. |  |  |
| 12 | Check Packing Proposals | In the Packing Proposal dialog box, check that the packaging material matches the packaging material maintained in the packing instruction for the vendor of the inbound delivery.The proposed quantities correspond to the quantities of your packing instruction.Select the desired proposal and then choose Enter. | An HU is created according to the predefined packing instruction. |  |
| 13 | Create HUs Manually | On the Work Center Packing for Inbound Delivery (Time Zone CET) screen, choose the Create HU tab. Make the following entries:Pack. Material PMPALLET.Number of HUs: <number of handling units>Choose Execute.Take a note of the HU numbers created. |  |  |
| 14 | Repack Product | Choose the Repack Product tab and make the following entries:Delivery Number: <your Inbound Delivery Number>Item Number: <item Number, for example 10>Quantity: <quantity to be packed in the destination HU>Unit of Measure: <UoM, for example PC>Dest. HU: <one of the HU created in step 12>Choose Execute. |  |  |
| 15 | Repeat Repacking Product | Repeat step 14 until all products have been repacked into HUs. |  |  |
| 16 | Enter Serial Numbers (optional) | At the lower left part of the screen, double click the product that has been packed into an HU, and then choose the Serial Nos tab.Enter the serial numbers manually for each unit of the material or choose Create SNs Automatically to allow the system assignment of the serial numbers.Note If the product has the C-serial number profile (Serialization in Stock) assigned, you can assign the serial numbers with this step. Otherwise, you can skip this step. |  |  |
| 17 | Choose Save | Choose Save. |  |  |
| 18 | Exit the Packing Work Center | Choose Exit. |  |  |
| 19 | Note Down your Delivery Number | Note down your delivery number for testing purposes. | On the Manage Inbound Deliveries screen on the Total Items tab, it shows No. of Serial Numbers Entered: X / X. |  |

##### Variant 3: With Radio Frequency Device

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, the Warehouse Operative (EWM) creates handling units (HUs) for unpacked products by delivery using a mobile RF device.

Handling unit management is not a general prerequisite of production integration. In this example process, creating handling units is mandatory only due to the bulk storage type to which material SG124 is put away to. Therefore, using material SG124, you create handling units and pack your material in this step. In case you want to store unpacked material, you should use the general storage type, the standard storage type, or your own storage type without HU requirements instead.

Skip this step, if you are using configurable materials and material variants. For material FG228, this step is optional.

If the products have the C-serial number profile (Serialization in Stock) assigned and are to be packed into HUs, you need to create handling units using Variant 2: With Fiori App.

For working with mobile RF devices, make sure all the steps as described in the set up instruction guide for scope item 63W - Mobile RF Devices in Warehousing with Production Integration are performed.

Procedure

| Test Step # | Test Step Name | Instruction | Pass/Fail/Comment |
| --- | --- | --- | --- |
| 1 | Log on to the SAP Fiori Launchpad | Log on to the SAP Fiori launchpad as a Warehouse Operative (EWM). |  |
| 2 | Access the SAP Fiori App | Open the SAP Fiori app Test RF Environment(/SCWM/RFUI)The app allows you to test working in an RF environment. For working with mobile RF devices, see also SAP Note 3048632. |  |
| 3 | Enter Data for RFUI | Whse No: 1750Resource: SHA1-1 or SHR1-1Dflt Dvc.: SE01Choose Enter. |  |
| 4 | Choose Menu | Choose 03 Inbound Processes > 02 Receiving of HUs > 01 Rec. HU By Delivery . |  |
| 5 | Enter Delivery Number | In the Delivery field, enter your delivery number and choose Enter. |  |
| 6 | Check Delivery Information | The inbound delivery is now displayed with the following information:DeliveryPartner (number and name)Warehouse Door (only displayed, if applicable)No. of HUs (number of HUs that HUs that have been created up to this point of time)Choose Enter to proceed. |  |
| 7 | Check Delivery Status | Check the following information that shows the delivery process status:Proc.HUs: X / YPck.Compl. (Packing Complete)GR PostedNote Note The Proc.HUs field indicates the status of the HU processing. Y indicates the number of HUs that have been created. X indicates the number of HUs that have been posted to the goods receipt.If all the unpacked products are processed, the field Pck.Compl. is checked and you can go to process step Post Goods Receipt Variant 2: With Radio Frequency Devices. Otherwise go to step 8 to continue to create new HUs. |  |
| 8 | Create New HU | Choose New HU.On the next screen, enter the following values:Product: <Product Number>Actual Qty: <Quantity> <UoM>BstBefDate: <Best before Date> (if applicable)Choose Next. |  |
| 9 | Enter Packaging Material | Enter values in the following fields:New P.Mat. (Packaging Material)Choose Enter. The HUtType is populated.Choose Next. |  |
| 10 | Check HU Information | Check the information of the newly created HU. Take a note of the following fields, if necessary:HU (HU number)SN (Serial Number)Batch (Batch number)Styp (Stock Type)ProTyp (Warehouse Process Type)Choose Back |  |
| 11 | Repeat Steps | Repeat steps 8 to 10 until all the unpacked products are packed into HUs and the field Pck.Compl. is checked. |  |
| 12 | Logoff RFUI | You can choose Back to go to the previous screens.Note Note If you would like to post a goods receipt using the mobile RF devices, stay logged on in the app.Choose Logoff.Choose Save. |  |

#### Post Goods Receipt

Purpose

This section describes the posting of the goods receipt from production.

##### Variant 1: With Fiori App

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Clerk (EWM) posts the goods receipt for the inbound delivery of the production order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk (EWM). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Inbound Deliveries – Warehouse (F7922). |  |  |
| 3 | Select Filters | On the Manage Inbound Deliveries screen, select AdaptFilters. | The Adapt Filters dialog box is displayed. |  |
|  | Select Fields for Filter | On the Adapt Filters dialog box, make sure the following fields are selected for the current filter:Planned Delivery Date/TimeManufacturing Order.Choose OK. |  |  |
| 5 | Search for Inbound Delivery | On the Manage Inbound Deliveries screen, make the following entries:Manufacturing Order: <your production order number>.Adjust the Planned Delivery Date/Time, if necessary.Choose Go. | Your inbound delivery is displayed. |  |
| 6 | Select Inbound Delivery | On the Manage Inbound Deliveries screen, select your Inbound Delivery. |  |  |
|  | Choose Details | Choose button Details. | Inbound delivery details are displayed. |  |
| 8 | Select Delivery Items | On the Manage Inbound Deliveries screen, select your Delivery Items. |  |  |
| 9 | Optional: Enter Serial Number | Enter the serial number, if required. |  |  |
| 10 | Post Goods Receipt | Choose Goods Receipt. | A system message tells you that the goods receipt is posted. |  |

##### Variant 2: With Radio Frequency Device

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, the Warehouse Operative (EWM) posts the goods receipt for the inbound delivery for the production order using a mobile RF device.

|  |
| --- |
| Note If no handling units are to be created for unpacked products, you can still use the RF device to post a goods receipt, but it is impossible to create putaway warehouse tasks with it. |

|  |
| --- |
| Note For working with Mobile RF Devices, make sure all the steps as described in the setup instruction guide for scope item 63W - Mobile RF Devices in Warehousing with Production Integration have been performed. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Fiori Launchpad | Log on to the SAP Fiori launchpad as a Warehouse Operative (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open the SAP Fiori app Test RF Environment(/SCWM/RFUI).The app allows you to test working in an RF environment. For working with mobile RF devices, see also SAP Note 3048632. |  |  |
| 3 | Enter Data for RFUI | Whse No: 1750Resource: SHA1-1 or SHR1-1DefPresDvc: SE01Choose Enter. |  |  |
| 4 | Choose Menu | Choose 03 Inbound Processes > 02 Receiving of HUs > 01 Rec. HU By Delivery . |  |  |
| 5 | Enter Delivery Number | In the Delivery field, enter your delivery number. |  |  |
| 6 | Check Delivery Information | The inbound delivery is now displayed with the following information:DeliveryPartner (number and name)Warehouse Door (only displayed if applicable)No. of HUs (number of HUs that HUs that have been created up to this point of time)Choose Enter to proceed. |  |  |
| 7 | Check Delivery Status | Check the following information that shows the delivery process status:Proc.HUs: X / Y.Pck.Compl.: X.GR Posted.Note Note The Proc.HUs field indicates the status of the HU processing. Y indicates the number of HUs that are created. X indicates the number of HUs that are posted to the goods receipt.If HUs are created for all the unpacked products, the field Pck.Compl. is checked. |  |  |
| 8 | Post Goods Receipt | Choose > and then choose PostGR.Note Note If no HUs are created, you can still post a goods receipt for all the unpacked products. In this case, you receive a system messageDelivery not fully packed. Continue?.Choose Yes to continue. | The GR Posted field is checked. |  |
| 9 | Logoff RFUI | You can choose Back to go to the previous screens.Note Note If you would like to create putaway warehouse tasks using the mobile RF devices, stay logged on in the app.Choose Logoff.Choose Save. |  |  |

#### Create Putaway Warehouse Tasks

Purpose

This section describes the creation of putaway warehouse tasks to move the products from the production area to the final bin.

##### Variant 1: With Fiori App

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Clerk (EWM) creates warehouse tasks for putaway.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk (EWM). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Inbound Deliveries – Warehouse (F7922). |  |  |
| 3 | Select Filters | On the Manage Inbound Deliveries screen, select Adapt Filters. | The Adapt Filters dialog box is displayed. |  |
|  | Select Fields for Filter | On the Adapt Filters dialog box, make sure the following fields are selected for the current filter:Planned Delivery Date/TimeManufacturing Order.Choose OK. |  |  |
| 5 | Search for Inbound Delivery | On the Manage Inbound Deliveries screen, make the following entries:Manufacturing Order: <your production order number>.Adjust the Planned Delivery Date/Time if necessary.Choose Go. | Your Inbound Delivery is displayed. |  |
| 6 | Select Inbound Delivery | On the Manage Inbound Deliveries screen, select your Inbound Delivery. |  |  |
| 7 | Choose Details | Choose button Details. | Inbound delivery details are displayed. |  |
| 8 | Select Delivery Items | Select your Delivery Items. |  |  |
| 9 | Choose Create Tasks | Choose Create Putaway Tasks Automatically. | A system message tells you that the tasks have been created. |  |
| 10 | Choose Warehouse Tasks | In the Items section, choose Yes in the Open PutawayWarehouse Tasks field. | The warehouse task(s) created is displayed. Make a note of the warehouse task number. |  |

##### Variant 2: With Radio Frequency Device

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Warehouse Operative (EWM) creates warehouse tasks for putaway using the Radio Frequency Device.

|  |
| --- |
| Note Warehouse Task creation with RF devices is only applicable for handling units. If the goods receipt is posted for unpacked products, create putwawy warehouse tasks using the Fiori App as described in variant 1. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Fiori launchpad | Log on to the SAP Fiori launchpad as a Warehouse Operative (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open the SAP Fiori app Test RF Environment(/SCWM/RFUI)The app allows you to test working in an RF environment. For working with Mobile RF Devices, see also SAP Note [3048632](https://me.sap.com/notes/3048632). |  |  |
| 3 | Enter Data for RFUI | Whse No: 3350Resource: SHA1-1 or SHR1-1DefPresDvc: SE01Choose Enter. |  |  |
| 4 | Choose Menu | Choose 03 Inbound Processes > 02 Receiving of HUs > 01 Rec. HU By Delivery . |  |  |
| 5 | Enter Delivery Number | In the Delivery field, enter your delivery number. |  |  |
| 6 | Check Delivery Information | The inbound delivery is now displayed with the following information:DeliveryPartner (number and name)Warehouse Door(only displayed if applicable)No. of HUs (number of HUs that HUs that have been created up to this point of time)Choose Enter to proceed. |  |  |
| 7 | Check Delivery Status | Check the following information that shows the delivery process status:Proc.HUs: Y / YPck.Compl.: XGR Posted: XNote:The Proc.HUs field indicates the status of the HU processing. Y indicates the number of HUs that have been created and that have been posted via goods receipt.The Pck.Compl. field is checked to indicate the packing is completed.The GR Posted field is checked to indicate the goods receipt posting is completed.Note As it is not allowed to post a partial goods receipt for an inbound delivery in the Cloud WM, you get an error message, if you try to create warehouse tasks before the goods receipt posting is completed: E: Cannot create WT for warehouse request XXXX, goods receipt missing. |  |  |
| 8 | Display HU List | Choose List. |  |  |
| 9 | Enter HU Sequence Number | Enter one of the HU sequence numbers in the field.Choose Enter. The HU selected is displayed.Choose Enter again to go to the HU detail screen. |  |  |
| 10 | Check HU Information | Check the information of the HU.Choose Enter. |  |  |
| 11 | Create Warehouse Task | Choose CrWT. | The WT Created field is now checked. |  |
| 12 | Go Back to Display HU List | Choose Back to go to the previous screen where HU list can be selected. |  |  |
| 13 | Repeat Steps | Repeat step 8 to 12 until warehouse tasks are created for all the Handling Units. |  |  |
| 14 | Logoff RFUI | You can choose Back to got to the previous screens.Note If you would like to Confirm Warehouse Tasks using the Mobile RF Devices, stay logged on in the app.You can also confirm the created warehouse tasks right away, instead of confirming them later from the queue selection, as described in the next step Confirm Warehouse Tasks - Variant 2: with Radio Frequency Devices.Choose Logoff.Choose Save. |  |  |

#### Confirm Putaway Warehouse Tasks

This section describes the confirmation of the previously created warehouse tasks.

##### Variant 1: With Fiori App

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A putaway list / warehouse tasks list / pick list is printed and handed over to the Warehouse Operative (EWM), who performs the warehouse tasks and confirms them in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Operative (EWM). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Process Warehouse Tasks - Putaway (F4150) |  |  |
| 3 | Enter Warehouse Task Number | On the Process Warehouse Tasks screen, make the following entries:Warehouse Task: <WT number noted down in the previous step>Choose Go. |  |  |
| 4 | Confirm Warehouse Task | Mark the checkbox for the selected warehouse task and choose ConfirmNote If you have the two availability groups setup for your warehouse, as soon as the putaway warehouse tasks are confirmed, the system automatically posts the stock type for this stock from ‘Unrestricted Use in Putaway (F0)’ to ’Unrestricted Use in Warehouse (F)’. | The following system message appears:Warehouse task confirmed. |  |

##### Variant 2: With Radio Frequency Devices

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Operative (EWM) performs the warehouse tasks and confirms them in the system with a mobile radio frequency device.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as a Warehouse Operative (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open the SAP Fiori app Test RF Environment(/SCWM/RFUI)The app allows you to test working in an RF environment. For working with mobile RF devices, see also SAP Note 3048632. |  |  |
| 3 | Enter Data for RFUI | Whse No: 1750Resource: SHA1-1 or SHR1-1DefPresDvc: SE01Choose Enter.Note Note Use resource SHA1-1 for putting away to S001 or SHR1-1 for putting away to SB01. |  |  |
| 4 | Choose Menu | Choose 01 System-Guided > 02 SystemGuided Queue . |  |  |
| 5 | Enter Queue Name | In the Queue field, enter SI-001, if your are putting away to S001 or SI-B01 if you are putting away to SB01. |  |  |
| 6 | Verify Source Bin and Enter HU | Note Note This step is only relevant, if you created handling units in step Create Handling Unit.Verify the Src.Bin (Source Bin)HU: < Enter the HU ID from previous step > |  |  |
| 7 | Verify the Source Information Fields | Verify the following fields if they are required:Src.Bin (Source Bin)Prod. (Product)Srce Qty (Source Quantity)ChooseEnter. |  |  |
| 8 | Verify the Destination Information Fields | Verify the following fields, if they are required:Prod. (Product)ActQty (Quantity)Dest.Qty (Destination Quantity)DstBin (Destination Bin)Choose Enter. |  |  |
| 9 | Repeat Steps | Repeat steps 6 to 8 until no suitable warehouse orders are found. |  |  |
| 10 | Logoff RFUI | You can choose Back to the previous screens.Choose Logoff.Choose Save.Note Note If you have the two availability groups setup for your warehouse, as soon as the putaway warehouse tasks are confirmed, the system automatically posts the stock type for this stock from ‘Unrestricted Use in Putaway (F0)’ to ’Unrestricted Use in Warehouse (F)’. |  |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

You may first have completed the following processes and conditions before you start with the test steps.

|  |
| --- |
| Note When running the following preceding processes along with the warehouse processes, make sure the material master data has been extended to your warehouse storage locations and the corresponding warehouse products have been created.Please refer to the Master Data Script BNF to create the storage location data for your material master data.Please refer to the Master Data Script 3KQ to create the corresponding warehouse products. |

| Scope Item ID | Business Condition |
| --- | --- |
| BJ5 - Make-to-Stock Production – Discrete Manufacturing | Planned orders are a prerequisite for the process. Make sure the following steps are fulfilled:Anonymous Forecast and MRPCreate Planned Independent RequirementsMaterial Requirements Planning at Plant LevelEvaluate Stock/Requirements SituationProduction Order Conversion and Available-to-Promise CheckConversion to Production Orders for Subassembly and Final AssemblyNote down the production order number for SG124. |
| 1YT - Make-to-Order Production with Variant Configuration | To store configurable material in the warehouse, perform the below steps of the business process 1YT - Make-to-Order Production with Variant Configuration.When creating the sales order, before saving, select the order item and then choose More > Go to > Item > Shipping . In section Shipping, enter the Storage Location value as a warehouse-managed storage location (e.g. Storage Location 335W). In section Manufacturing Steps Production Order Processing, proceed until the completion of the confirm assembly activities step. After this, continue with the Create Inbound Delivery for Production Order step within this test script.Note The scope item Make-to-Order Production with Variant Configuration (1YT) needs to be activated before you can test this business condition. After the activation of Make-to-Order Production with Variant Configuration (1YT), extend the configurable material sample master data to the warehouse storage location 335W of plant 3310 by following the section Create Product Master Data - Storage Location Data in master data script Create Product Master of Type "Configurable Material" (2T7). Then, create the warehouse attributes by following the master data script Create Warehouse Attributes for Material/Product Master (3KQ).Create Sales Quotation for Configurable Material (Optional)Create Sales Order with Reference to Sales Quotation (Optional)Create Sales Order with Configurable MaterialCreate Down Payment RequestPost Down PaymentManufacturing Steps Production Order Processing |
| 21D - Make-to-Stock Production with Variant Configuration | You can alternatively perform the below steps from business process 21D - Make-to-Stock Production with Variant Configuration to store configurable material and material variants in the warehouse. When creating the sales order, before saving, select the order item and then choose More > Go to > Item > Shipping . In section Shipping, enter the storage location value as a warehouse-managed storage location (e.g. Storage Location 335W). In section Production Execution, proceed until the completion of the Production Execution Final Confirmation of Production Operations for Final Assembly step. After this, continue with the Create Inbound Delivery for Production Order step within this test script. Once the material has been stored successfully, return to 21D - Make-to-Stock Production with Variant Configuration and perform the Sales Order Processing step.Note The scope item Make-to-Order Production with Variant Configuration (1YT) needs to be activated before you can test this business condition. After the activation of Make-to-Stock Production with Variant Configuration, extend the configurable material sample master data to the warehouse storage location 335W of plant 3310 by section Create Product Master Data - Storage Location Data in master data script Create Product Master of Type "Configurable Material" (2T7). Then, create the warehouse attributes by following the master data script Create Warehouse Attributes for Material/Product Master (3KQ).Production PlanningProduction ExecutionSales Order ProcessingCreate Sales Order With Material Variant |
| BJE - Make-to-Order Production – Finished Goods Sales and Final Assembly | To test an MTO process, perform below test steps in BJE - Make-to-Order Production – Finished Goods Sales and Final Assembly.When creating the sales order, before saving, select the order item and then choose More > Go to > Item > Shipping . In section Shipping, enter the Storage Location value as a warehouse-managed storage location (e.g. Storage Location 335W). In section Production Processing, proceed until the completion of the Confirm Assembly Activities step. Afterwards, continue with step Create Inbound Delivery for Production Order in this test script. Use material FG228.MTO Sales Processing (Material w/o Sales Order BoM)Down Payment ProcessingProduction PlanningProduction Processing |

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| BJ5 - Make-to-Stock Production – Discrete Manufacturing | To complete the whole process for the GI for production section in this scope item, follow up with the Confirm Production Operations for Subassembly step in test script Make-to-Stock Production – Discrete Manufacturing (BJ5).To continue the process after the whole GR from Production section, follow up with the Production Order Processing for Final Assembly step in test script Make-to-Stock Production – Discrete Manufacturing (BJ5). |
| 1YT - Make-to-Order Production with Variant Configuration | Complete activities from the chapter Delivery and Billing Processing described in the test script of the scope item. |
| 21D - Make-to-Stock Production with Variant Configuration | Complete activities from the chapter Delivery and Billing Processing described in the test script of the scope item. |
| BJE - Make-to-Order Production – Finished Goods Sales and Final Assembly | To complete activities from the chapter Delivery Processing described in the test script of the scope item, proceed with test script Warehouse Outbound Processing (3BS).Complete activities from the chapter Billing Process described in the test script of the scope item. |

### Attachment Handling (Optional)

In the SAP S/4HANA Cloud Public Edition, Attachment Service is a reusable user interface component which can be consumed by any FIORI application to attach documents. File attachments enable all kinds of media files being connected to business documents as additional information. For example, photos, videos, or documentation in form of plain text documents.

In the following you find some examples for use cases of the Attachment Service in the Cloud WM:

- Inbound Process - Non-Acceptance of Delivery and Proof of SLA Violation
- Outbound Process - Visual Documentation of Complete and Error-free Packaging
- Outbound Process - Visual Documentation of Loading Security, Compliance to Regulations, SLAs

Attachment Service is an optional support feature for Cloud WM business objects. Attachments can be handled any time after the creation of an Cloud WM business object and any time before the end of the document’s lifecycle.

In this process you can use the following SAP FIORI apps to create, read, update or delete the attachments:

- Manage Inbound Deliveries – Warehouse (F7922) for Inbound Deliveries
- Warehouse Monitor for Outbound Delivery Orders or Inbound Deliveries or Handling Units respectively under theses nodes:
    - Outbound > Documents > Outbound Delivery Orders or
    - Inbound > Documents > Inbound Delivery

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
> Flagged while digesting this document, not verified: Warehouse number is 3350 in sample data and in most steps, but the RF steps in Create Handling Unit (Variant 3), Post Goods Receipt (Variant 2) and Confirm Putaway Warehouse Tasks (Variant 2) enter Whse No 1750 (the packing instruction determination example uses 1050); the RF putaway-creation variant uses 3350.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[11-inventory-warehouse-and-transportation/atualizar-area-de-abastecimento-da-producao-mds-3ks-344]]
- related-to :: [[11-inventory-warehouse-and-transportation/maintain-production-supply-area-mds-3ks-341]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-3ks-343]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-3ks-345]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3DV_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 91,311 chars in the whole document
