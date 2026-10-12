---
id: 11-inventory-warehouse-and-transportation/warehouse-advanced-production-integration-6ni-ae-test-script-sap-s-4ha
title: "Warehouse Advanced Production Integration (6NI_AE) - Test Script, SAP S/4HANA Cloud Public Edition (6NI_S4CLD2608_BPD_EN_AE)"
description: "Test script for SAP S/4HANA Cloud scope item 6NI_AE: staging, consumption posting/reversal and PSA clearance between shop floor and EWM, via Fiori and RF."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/ewm-production-integration]
aliases: [6NI_S4CLD2608_BPD_EN_AE]
keywords: [EWM Production Supply and Receipt, advanced production integration, production material request, material staging, production supply area, warehouse tasks, component consumption, consumption reversal, psa clearance, production order release]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6NI_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1185
topic: 11-inventory-warehouse-and-transportation/ewm-production-integration
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Warehouse Advanced Production Integration (6NI_AE) - Test Script, SAP S/4HANA Cloud Public Edition (6NI_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6NI_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **EWM Production Supply and Receipt** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Warehouse Advanced Production Integration (6NI_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Warehouse Advanced Production Integration (6NI_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232858941)

[2 Prerequisites 4](#_Toc232858942)

[2.1 System Access 4](#_Toc232858943)

[2.2 Roles 4](#_Toc232858944)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232858945)

[2.4 Business Conditions 9](#_Toc232858946)

[2.5 Preliminary Steps 11](#_Toc232858947)

[2.5.1 Define Default Values for Warehouse Clerk (WM) 11](#_Toc232858948)

[2.5.2 Define Default Values for Warehouse Operative (WM) 11](#_Toc232858949)

[2.5.3 Assign Fixed Storage Bins to Component 12](#_Toc232858950)

[2.5.4 Create Control Cycle 13](#_Toc232858951)

[2.5.5 Assign Bins to PSA 14](#_Toc232858952)

[2.5.6 Create Initial Stock for Components 17](#_Toc232858953)

[2.5.7 Maintain Warehouse Product Attributes to Automatically Create Putaway Warehouse Tasks (Optional) 18](#_Toc232858954)

[2.5.8 Manage Packing Instruction (Optional) 20](#_Toc232858955)

[2.5.8.1 Create Packing Instruction 20](#_Toc232858956)

[2.5.8.2 Create Packing Instruction Determination 21](#_Toc232858957)

[3 Overview Table 23](#_Toc232858958)

[4 Test Procedures 24](#_Toc232858959)

[4.1 Release Production Order 24](#_Toc232858960)

[4.2 Trigger Creation of Production Material Request 25](#_Toc232858961)

[4.3 Check Production Material Request (Optional) 27](#_Toc232858962)

[4.4 Create Staging Warehouse Tasks 28](#_Toc232858963)

[4.5 Confirm Staging Warehouse Tasks 29](#_Toc232858964)

[4.5.1 Variant 1: With Fiori App 29](#_Toc232858965)

[4.5.2 Variant 2: With Radio Frequency Devices 31](#_Toc232858966)

[4.6 Post Consumption of Components 33](#_Toc232858967)

[4.6.1 Variant 1: Confirm Production Operations for Subassembly 33](#_Toc232858968)

[4.6.2 Variant 2: Post Consumption of Components in Warehouse 35](#_Toc232858969)

[4.6.2.1 Variant 1: With Fiori App 35](#_Toc232858970)

[4.6.2.2 Variant 2: With Radio Frequency Devices 37](#_Toc232858971)

[4.7 Reverse Consumption of Components (Optional) 38](#_Toc232858972)

[4.7.1 Variant 1: With Fiori App 39](#_Toc232858973)

[4.7.2 Variant 2: With Radio Frequency Devices 40](#_Toc232858974)

[4.8 Clear Production Supply Area (Optional) 41](#_Toc232858975)

[4.9 Confirm Warehouse Task for PSA Clearance (Optional) 43](#_Toc232858976)

[4.9.1 Variant 1: With Fiori App 43](#_Toc232858977)

[4.9.2 Variant 2: With Radio Frequency Devices 44](#_Toc232858978)

[5 Appendix 47](#_Toc232858979)

[5.1 Process Integration 47](#_Toc232858980)

[5.1.1 Preceding Processes 47](#_Toc232858981)

[5.1.2 Succeeding Processes 48](#_Toc232858982)

## Purpose

Overview

Advanced production integration allows you to have real-time material flow between shop floor and warehouse. You can plan the staging of components to production over a period of time, so that PSA capacity is reasonably used. You can monitor and control the staging process. Consumption can be posted directly from WM and the consumption status can be monitored using an app or RF. Consumption posting can be reversed directly from WM using an app or RF.

You can receive produced stock as soon as the goods receipt request is triggered from the shop floor (both the Post Goods Movement app and the RF are available for the use). You can also clear stock reference on left-over stock from the production supply area, and move them back to the warehouse, after the manufacturing process is complete. In that way, you can free up some capacity from the production supply area for other staging activities, using an app or RF.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

This section describes test procedures for each process step that belongs to this scope item.

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/87807ffd176c4dbca23d97ff1ec0705c.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Production Supervisor - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC | Production Management - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC |  |
| Warehouse Clerk (EWM) | SAP_BR_WAREHOUSE_CLERK_EWM | Warehouse Office | SAP_BR_WAREHOUSE_CLERK_EWM |  |
| Warehouse Operative (EWM) | SAP_BR_WAREHOUSE_OPERATIVE_EWM | Warehouse Floor | SAP_BR_WAREHOUSE_OPERATIVE_EWM |  |
| Production Operator - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC | Production Execution - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC |  |
| Master Data Specialist - Handling Unit Data | SAP_BR_HU_MASTER_SPECIALIST | Master Data - Handling Units | SAP_BR_HU_MASTER_SPECIALIST |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | FG526 | FIN526,MTS-DI,PD,Batch-Fifo,SerialNo | Use this material to test the production integration with production material request and goods receipt with synchronized goods movements. |
| Material | SG524 | SEMI524,PD,Subassembly,AdvProdInt | Component for FG526. |
| Material | FG726 | FIN726,MTS-DI,PD,Batch-Fifo,SerialNo | Use this material to test the production integration with production material request and delivery-based goods receipt. |
| Material | SG724 | SEMI724,PD,Subassembly,AdvProdInt | Component for FG726. |
| Material | FG826 | FIN826,MTS-DI,PD,Batch-Fifo,SerialNo | Use this material to test the production integration with production material request, activated backflush for raw material components and goods receipt with synchronized goods movements. |
| Material | SG824 | SEMI824,PD,Subassembly,AdvProdInt | Component for FG826. |
| Material | RM124 | RAW124, VB, Consumption, FixedBin | 1 PAL = 100 PCComponent for SG824. |
| Material | RM324 | RAW324,VB,Consumption,NoStag | 1 PAL = 100 PCComponent for SG524 and SG724 |
| Material | RM424 | RAW424,VB,Consumption,CrossOrd,Batch | 1 PAL = 100 PCComponent for SG524 and SG724 |
| Material | RM524 | RAW524,VB,Consumption,SingOrd,SerialNo | 1 PAL = 100 PCComponent for SG524 and SG724 |
| Material | FG428 | FIN428,MTO,PD,Fifo | Use this material to test the production integration with production material request in a make-to-order scenario and goods receipt with synchronized goods movements. |
| Material | SG224 | SEMI224,MTO,PD,Subassembly | Component for FG428. |
| Production Version | 0001 | Production Version 1 | Production version for materials FG526, SG524, FG726, SG724 and FG428 |
| Packaging Material | PMPALLET |  |  |
| Packaging Material | PMPALLET_GTL | Pallet for GTL |  |
| Company Code | 3310 |  |  |
| Plant | 3310 |  |  |
| Storage Location | 335W |  |  |
| Production Supply Area (PSA) | PSA_03 | PSA for advanced production integration |  |
| Warehouse Number | 335 |  |  |

Organizational Master Data in Warehouse:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Warehouse | 3350 |  |  |
| Custodian | 17411710 |  |  |
| Entitled to Dispose | 17411710 |  |  |

Warehouse-Specific Master Data:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Storage Type | SF01 | Fixed Bin Storage |  |
| Storage Type | S105 | Production Supply |  |
| Storage Type | S915 | Goods Receipt from Production |  |
| Storage Type | S970 | Clarification Zone |  |
| Storage Type | S001 | Storage |  |
| Storage Type | SG01 | General Storage |  |

Product Structures

|  |
| --- |
| Note Material stocks can be managed in Inventory Management. You manage the quantities and values of stocks in several storage locations. In comparison, Warehouse Management allows you to map your entire warehouse complex in detail to storage bin level. |

Product Structure FG428

Use this material to test the production integration with production material request in a make-to-order scenario and goods receipt with synchronized goods movements.

| Material | Description | Inventory Management | Warehouse Management | Assembly Quantity | Unit |
| --- | --- | --- | --- | --- | --- |
| FG428 | FIN428,MTO,PD,Fifo |  | X | 1 | PC |
| SG224 | SEMI224,MTO,PD,Subassembly |  | X | 2 | PC |
| SG224 | SEMI224,MTO,PD,Subassembly |  | X | 100 | PC |
| RM124 | RAW124, VB, Consumption, FixedBin |  | X | 100 | PC |

Product Structure FG526

Use this material to test the production integration with production material request and goods receipt with synchronized goods movements.

| Material | Description | Inventory Management | Warehouse Management | Assembly Quantity | Unit |
| --- | --- | --- | --- | --- | --- |
| FG526 | FIN526,MTS-DI,PD,Batch-Fifo,SerialNo | X |  | 1 | PC |
| SG524 | SEMI524,PD,Subassembly,AdvProdInt |  | X | 2 | PC |
| SG524 | SEMI524,PD,Subassembly,AdvProdInt |  | X | 2 | PC |
| RM324 | RAW324,VB,Consumption,NoStag |  | X | 2 | PC |
| RM424 | RAW424,VB,Consumption,CrossOrd,Batch |  | X | 2 | PC |
| RM524 | RAW524,VB,Consumption,SingOrd,SerialNo |  | X | 2 | PC |

Product Structure FG726

Use this material to test the production integration with production material request and delivery-based goods receipt.

| Material | Description | Inventory Management | Warehouse Management | Assembly Quantity | Unit |
| --- | --- | --- | --- | --- | --- |
| FG726 | FIN726,MTS-DI,PD,Batch-Fifo,SerialNo | X |  | 1 | PC |
| SG724 | SEMI724,PD,Subassembly,AdvProdInt |  | X | 2 | PC |
| SG724 | SEMI524,PD,Subassembly,AdvProdInt |  | X | 2 | PC |
| RM324 | RAW324,VB,Consumption,NoStag |  | X | 2 | PC |
| RM424 | RAW424,VB,Consumption,CrossOrd,Batch |  | X | 2 | PC |
| RM524 | RAW524,VB,Consumption,SingOrd,SerialNo |  | X | 2 | PC |

Product Structure FG826

Use this material to test the production integration with production material request, activated backflush for raw material components and goods receipt with synchronized goods movements.

| Material | Description | Inventory Management | Warehouse Management | Assembly Quantity | Unit |
| --- | --- | --- | --- | --- | --- |
| FG826 | FIN826,MTS-DI,PD,Batch-Fifo,SerialNo | X |  | 1 | PC |
| SG824 | SEMI824,PD,Subassembly,AdvProdInt |  | X | 2 | PC |
| SG824 | SEMI824,PD,Subassembly,AdvProdInt |  | X | 2 | PC |
| RM124 | RAW124, VB, Consumption, FixedBin |  | X | 2 | PC |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

| MDS | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| 3KQ | Maintain Warehouse Products Attributes - MDS |
| 3KR | Maintain Storage Bins and Fixed Bin Assignments - MDS |
| 3KS | Maintain Production Supply Area - MDS |
| 40D | Create Production Supply Area - MDS |

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | You’ve completed the step described in the Create New Open MM Posting Period - MDS (BNZ) master data script. The posting period is up to date. |
| BJ5 - Make-to-Stock Production – Discrete Manufacturing | Planned orders are a prerequisite for the process. Make sure the following steps are fulfilled:Anonymous Forecast and MRPCreate Planned Independent RequirementsNote Caution: Contrary to scope item BJ5 - Make-to-Stock Production – Discrete Manufacturing enter a quantity of 1 for PIR for 1 period (current period+ 1) for testing purposes.Reason: in the goods receipt process the serial number of every single piece needs to be entered later.Material Requirements Planning at Plant LevelEvaluate Stock/Requirements SituationProduction Order Conversion and Available-to-Promise CheckConversion to Production Orders for Subassembly and Final AssemblyNote Caution: Contrary to scope item BJ5 - Make-to-Stock Production – Discrete Manufacturing the release of the production order must be performed before material staging.There are several sets of material master data available for testing the process variants in this test script. Refer to below table for an overview of the scenarios and the associated materials. Once you created the production order, note down the production order number for the semifinished goods:Table 1:ScenarioMaterial MasterGoods receipt with synchronized goods movementFG526, SG524, RM324, RM424, RM524Goods receipt with synchronized goods movement, backflush componentFG826, SG824, RM124Goods receipt with deliveriesFG726, SG724, RM324, RM424, RM524 |
| BJE - Make-to-Order Production – Finished Goods Sales and Final Assembly | Planned orders are a prerequisite for the process. Make sure the steps in following sections are fulfilled:MTO Sales Processing (Material w/o Sales Order BoM)Down Payment ProcessingProduction PlanningProduction ProcessingIn section Production Processing, execute step Create Production Order only. Use material FG428. Once you created the production order, note down the production order number for the finished good:Table 2:ScenarioMaterial MasterGoods receipt with synchronized goods movementFG428, SG224 |
| 5HN - Warehouse Inbound Processing with Synchronous Goods Receipt | After the process step Material Requirements Planning at Plant Level of scope item Make-to-Stock Production – Discrete Manufacturing (BJ5), receipt elements are created. Depending on the elements created in the MRP run, refer to Procurement of Direct Materials (J45) or Scheduling Agreements in Procurement (BMR) test scripts for processing externally-sourced materials. Use process step Post Goods Receipt for Purchase Orders from scope item Warehouse Inbound Processing with Synchronous Goods Receipt (5HN) to receive stock in the warehouse. |

### Preliminary Steps

#### Define Default Values for Warehouse Clerk (WM)

Purpose

In this step, you can define the default warehouse number for the Warehouse Clerk (EWM).

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
|  | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk (EWM). |  |  |
|  | Choose Avatar | Choose Icon for the logon user.Choose Settings. |  |  |
|  | Enter Default Value | Choose Default Values.And make the following entry in the section Material Management:Warehouse Number: 1750.Choose Save. |  |  |

#### Define Default Values for Warehouse Operative (WM)

Purpose

In this step, you can define the default warehouse number for the Warehouse Operative (EWM).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
|  | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Operative (EWM). |  |  |
|  | Choose Avatar | Choose Icon for the logon user.Choose Settings. |  |  |
|  | Enter Default Value | Choose Default Values.And make the following entry in the section Material Management:Warehouse Number: 1750.Choose Save. |  |  |

#### Assign Fixed Storage Bins to Component

Purpose

In this step, you assign fixed storage bins to products.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
|  | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk (EWM). | The SAP Fiori launchpad displays. |  |
|  | Access App | Open Assign Fixed Bins(/SCWM/BINMAT). | The Maintain Fixed Storage Bins screen displays. |  |
|  | Enter Data | On the Assign Fixed Storage Bins screen, make the following entries:Warehouse Number: 1750Product: RM124. |  |  |
|  | Choose Run. | Choose Run. | The Warehouse Number <number>: Display Fixed Storage Bins screen appears. |  |
|  | Maintain Fixed Bin | On the Warehouse Number <number>: Display Fixed Storage Bins screen, choose Edit. |  |  |
|  | Choose Create | On the Warehouse Number <number>: Display Fixed Storage Bins screen, choose Create. |  |  |
|  | Make entries | On the Warehouse Number <number>: Display Fixed Storage Bins screen, make or check the following entries:WhN: 1750.Disposal: 17411710Storage Bin: SF01-03-04.Product: RM124. |  |  |
|  | Save | Save your entries | The following system message appears: Changes were saved. |  |

#### Create Control Cycle

Purpose

In this activity, you create a control cycle that can be used for in-house production in the production supply area. In the control cycle, you define the demand source, the supply source, and the material staging indicator. The material staging indicator defines the method of how needed materials can be supplied for production with the assistance of the warehouse management system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
|  | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad is displayed. |  |
|  | Access App | Open Create Control Cycle for WM(LPK1). | The Create Control Cycle: Initial Screen (WM) screen is displayed. |  |
|  | Enter Data | On the Create Control Cycle: Initial Screen (WM) screen, make the following entries:Material: RM324Plant: 1710.Supply Area: PSA_03. |  |  |
|  | Choose Enter | Choose Enter. | The Create Control Cycle: Data Screen (WM) screen is displayed. |  |
|  | Enter Control Cycle Details | Make the following entries:In the Destination section:Staging Ind.: 5 (EWM Staging)In the Source section:Stor. Location: 175W | The Destination Stor. Location, Destination Warehouse Number, Source Issuing Plant, and Source Warehouse No fields are automatically filled by the system. |  |
|  | Choose Save | Choose Save. | The following system message appears: Control cycle RM324 1710 PSA_03 will be created. |  |
|  | Repeat for remaining Components | Repeat above steps and create control cycles for materials RM124, RM424, RM524 and SG224. | You have created control cycles for WM staging of materials RM124, RM424, RM524 and SG224. |  |

#### Assign Bins to PSA

Purpose

In this activity, you manage the storage bins that are used for production supply at the level of the production supply area. You assign each of them to a production supply area, a party entitled to dispose, and a product. You maintain additional attributes related to the production supply process such as staging methods, quantities, and the warehouse process types used for creation of the staging warehouse tasks and the warehouse tasks for clearing the PSA.

|  |
| --- |
| Note Note:Warehouse process type S220 is required to create a picking warehouse task for Single Order Staging scenario.Warehouse Process Type S320 is required to create an internal stock movement warehouse task for Cross Order Staging scenario.Warehouse Process Type S325 is required to create an internal stock movement warehouse task for moving stock from PSA back to warehouse storage. |

Assign Bins to PSA Overview Table

| Product | Storage Bin | Staging Method | Type of Quantity Calculatio | Replenishment Quantity | Minimum Production Quantity in PSA | Unit | Staging Warehouse Process Type | Clear PSA Warehouse Process Type |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RM324 | PROD-SUPPLY-3 | Not Relevant for Staging |  |  |  |  |  |  |
| RM424 | PROD-SUPPLY-4 | Cross-Order Staging | Quantity-Based Calculation | 4 | 200 | PC | S320 | S325 |
| RM524 | PROD-SUPPLY-5 | Single-Order Staging | Quantity-Based Calculation | 4 | 200 | PC | S220 | S325 |
| RM124 | PROD-SUPPLY-6 | Single-Order Staging | Quantity-Based Calculation | 4 | 200 | PC | S220 | S325 |
| SG224 | PROD-SUPPLY-7 | Single-Order Staging | Quantity-Based Calculation | 10 | 200 | PC | S220 | S325 |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
|  | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk (EWM). |  |  |
|  | Access App | Open Assign Bin to PSA(/SCWM/PSASTAGE2). | The Determine Work Area: Entry dialog box appears. |  |
|  | Make Entries | In the Determine Work Area: Entry dialog box, make the following entries:Party Entitled to Dispose:17411710Supply Area: PSA_03 /1710Note Note: For the field Supply Area, use the value help. |  |  |
|  | Choose Enter | Choose Apply (Enter). | The Assign Bin to PSA: Change screen appears. |  |
|  | Choose New Entries | On the Assign Bin to PSA: Change screen, choose New Entries. | The New Entries: Details of Added Entries screen appears. |  |
|  | Make Entries | On the New Entries: Details of Added Entries screen, make the following entries:Product: RM324In the Assign Bin to PSA section:Storage Bin: PROD-SUPPLY-3Staging Method: Not Staging RelevantQty Calc. Type: No Quantity Calculation |  |  |
|  | Choose Enter. | Choose Enter. |  |  |
|  | Choose Save | Save your entries. | The following system message appears:Data was savedYou have created an entry for material RM324.The New Entries: Added Entries screen appears. |  |
|  | Choose Cancel | On the New Entries: Added Entries screen, choose Cancel to return to the Assign Bin to PSA: Change screen. | The Assign Bin to PSA: Change screen appears. |  |
|  | Repeat the Steps | Repeat steps 5 to 8 and make the following entries:For material RM424Product: RM424In the Assign Bin to PSA section:Storage Bin: PROD-SUPPLY-4Staging Method: Cross-Order StagingQty Calc. Type: Quantity-Based CalculationChoose Enter.Replmt Qty: 4Min.Prd.Qty PSA: 200Unit: PCStaging WPT: S320Clear PSA WPT: S325For material RM524:Product: RM524In the Assign Bin to PSA section:Storage Bin: PROD-SUPPLY-5Staging Method: Single-Order StagingQty Calc. Type: Quantity-Based CalculationChoose Enter.Replmt Qty: 4Min.Prd.Qty PSA: 200Unit: PCStaging WPT: S220Clear PSA WPT: S325For material RM124:Product: RM124In the Assign Bin to PSA section:Storage Bin: PROD-SUPPLY-6Staging Method: Single-Order StagingQty Calc. Type: Quantity-Based CalculationChoose Enter.Replmt Qty: 4Min.Prd.Qty PSA: 200Unit: PCStaging WPT: S320Clear PSA WPT: S325For material SG224:Product: SG224In the Assign Bin to PSA section:Storage Bin: PROD-SUPPLY-7Staging Method: Single-Order StagingQty Calc. Type: Quantity-Based CalculationChoose Enter.Replmt Qty: 10Min.Prd.Qty PSA: 200Unit: PCStaging WPT: S220Clear PSA WPT: S325 | You have created entries for material RM124, RM424, RM524, and SG224. |  |

#### Create Initial Stock for Components

Purpose

Create enough raw material stock for staging to production.

Prerequisite

Before creating initial material stocks, we recommend that you check the stock levels for the finished and semi-finished goods. To do that, log onto the SAP Fiori launchpad as a Production Planner, and open the Manage Material Coverage (F0251A) app. Remove stock or increase the requirement quantity if there is already a sufficient amount of stock available. Otherwise, no planned orders can be generated later.

|  |
| --- |
| Note Example: For the following semi-finished materials planned orders must be created during the step Material Requirements Planning at Plant Level:SG224SG524SG724SG824 |

Procedure

During the process step Material Requirements Planning at Plant Level of scope item Scheduling Agreements in Procurement (BJ5), receipt elements are created. Depending on the elements created in the MRP run, refer to Procurement of Direct Materials (J45) or Scheduling Agreements in Procurement (BMR) test scripts for processing externally-procured materials.

Use process step Post Goods Receipt for Purchase Orders from scope item Warehouse Inbound Processing with Synchronous Goods Receipt to receive stock in the warehouse.

|  |
| --- |
| Note Example: For the following raw materials sufficient stock in the warehouse must exist:RM124RM324RM424RM524 |

#### Maintain Warehouse Product Attributes to Automatically Create Putaway Warehouse Tasks (Optional)

Purpose

In this section, you maintain the warehouse product attributes using the Warehouse Monitor(/SCWM/MON) app. Setting the Process Type Determination Indicator results in the creation of putaway warehouse tasks automatically after the goods receipt was posted.

|  |
| --- |
| Note Note In case a semi-finished product is to be used as a component for a subsequent production step for final assembly of a finished product, you have the opportunity to move the product to the subsequent PSA without having to carry out the putaway process first. For this, you enter a target PSA in the production version of the product. When automatic warehouse task creation is activated as described in this section, upon goods receipt of the semi-finished product, the system creates a warehouse task towards the bin associated with this PSA via the control cycle for the material and PSA. You can find the target PSA field in the 'Other Data' section in the production version. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
|  | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk (EWM). |  |  |
|  | Access App | Open Warehouse Monitor(/SCWM/MON). | The Warehouse Management Monitor SAP - Warehouse Number XX50 screen is displayed. |  |
|  | Navigate to Warehouse Attribute | In the hierarchy in the left screen area, double click Product Master Data > Warehouse Attribute . |  |  |
|  | Enter Product Number | In the /SCWM/SAPLPROD_OVERVIEW dialog box, make the following entries:Basic Attributes section:Product Number: SG524, SG724, SG824 or FG428.Choose Execute. |  |  |
|  | Select Product | On the Warehouse Management Monitor SAP - Warehouse Number screen, in the Warehouse Attributes area, select the product. |  |  |
|  | Choose Mass Change/Create | Choose More Methods > Mass Change/Create . |  |  |
|  | Make entries for Process Type Determination Indicator | In the /SCWM/SAPLPROD_OVERVIEW dialog box, make the following entries:Note It is not possible to pack the goods before putaway if automatic putaway warehouse task creation is enabled.In the Warehouse Data section:Proc.Type Det. Ind: S1. |  |  |
|  | Choose Execute | Choose Execute. |  |  |
|  | Confirm your changes | In the Warehouse Management Monitor SAP - Warehouse Number dialog box, choose Yes. | The following system message appears:1 products save d . |  |

#### Manage Packing Instruction (Optional)

##### Create Packing Instruction

Purpose

In this step, you create a packing instruction.

A packing instruction serves as a template for the creation of a handling unit. In a packing instruction, you define the materials and packaging materials to be packed in a handling unit.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
|  | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Handling Unit Data | The SAP Fiori launchpad displays. |  |
|  | Access the App | Open Create Packing Instruction - Master Data(POP1). | The Create Packing Instruction: Initial screen displays. |  |
|  | Create Packing Instruction | On the Create Packing Instruction: Initial screen, choose Continue or choose Enter to create a new packing instruction.Note Note: You can also enter a name for the packing instruction. If you do not enter a name, the system assigns a key automatically.If you want to create a packing instruction from a reference packing instruction, choose a reference packing instruction and then Enter. | The Create Packing Instruction: Components screen appears. |  |
|  | Make entries | On the Create Packing Instruction: Components screen, make the following entries:Short Text: < short text for the description of the packing instruction>Note Example: SG524 on palletsItem No.Item CategoryComponentTarget Quantity10PPMPALLET120MSG5248Note Note: The items should be entered in the following order:Load carrier (item category P)Packed goods (item category M). |  |  |
|  | Navigate to the Admin.data tab | Navigate to the Admin.data tab. |  |  |
|  | Enter Check Profile | On the Admin.data tab, make the following entries:Check Profile: 01 |  |  |
|  | Save | Save your entries. | The following system message appears: PackInstructn <number> saved successfully. |  |
|  | Note down the packing instruction number | Note down the packing instruction number for future reference. |  |  |
|  | Repeat steps 3 to 8 for materials SG724, SG824 and FG428 | Repeat steps 3 to 8 for materials SG724, SG824 and FG428. |  |  |

##### Create Packing Instruction Determination

Purpose

In this step, you create packing instruction determination records.

This function enables the system to find a packing instruction by specific characteristics. The condition technique is applied. You define a packing instruction that refers to specific characteristics, such as material.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
|  | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Handling Unit Data | The SAP Fiori launchpad displays. |  |
|  | Access the App | Open Create Determination Records - Master Data(POF1). | The Pkg Instruction - Create Determination Recs: Initial Screen is displayed. |  |
|  | Enter Determination Type | On the Pkg Instruction - Create Determination Recs: Initial Screen, make the following entries:For material SG524, SG824 or FG428:Determination Type: 0GRP – MIGO Production ReceiptFor material SG724:Determination Type: 0IBD: – Inbound Delivery WM |  |  |
|  | Choose Enter | Choose Enter | The Key Combination dialog box appears. |  |
|  | Choose Material | In the Key Combination dialog box, choose Material. |  |  |
|  | Choose Choose | In the Key Combination dialog box, choose Choose. | The Create MIGO Production Rcpt (0GRP) : Fast Entry screen appears. |  |
|  | Enter Material and Packing Instruction | On the Create MIGO Production Rcpt (0GRP) : Fast Entry screen, make the following entries:* Material* Packing InstructionSG524<number>SG824<number>FG428<number> |  |  |
|  | Save | Save your entries. | The following system message appears: Condition records saved. |  |
|  | Repeat steps 3 to 8 for material SG724:Determination Type: 0IBD: – Inbound Delivery WM | Repeat steps 3 to 8 for material SG724:Determination Type: 0IBD: – Inbound Delivery WM |  |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Release Production Order [page ] 21 | Production Supervisor - Discrete Manufacturing | Manage Production Orders (F2336) | You have released the production order. |
| Trigger Creation of Production Material Request [page ] 23 | Production Supervisor - Discrete Manufacturing | Manage Production Orders (F2336) | You have created a production material request. |
| Check Production Material Request (Optional) [page ] 24 | Warehouse Clerk (EWM) | Display Production Material Requests (/SCWM/MONNAV_PMR) |  |
| Create Staging Warehouse Tasks [page ] 25 | Warehouse Clerk (EWM) | Create Warehouse Tasks - Staging for Production(/SCWM/STAGE) | You have created the staging warehouse tasks. |
| Confirm Staging Warehouse Tasks [page ] 26 | Warehouse Clerk (EWM) | Process Warehouse Tasks - Internal Movements(F4595) | You have confirmed the staging warehouse tasks. |
| Post Consumption of Components [page ] 31 | Warehouse Clerk (EWM)Warehouse Operative (EWM) | Post Consumption - Production(/SCWM/MFG_CONSUMPTION)Test RF Environment (/SCWM/RFUI) | You posted the consumption of the required components. |
| Reverse Consumption of Components (Optional) [page ] 36 | Warehouse Clerk (EWM)Warehouse Operative (EWM) | Post Consumption - Production(/SCWM/MFG_CONSUMPTION)Test RF Environment (/SCWM/RFUI) | The consumption of the component was reversed. |
| Clear Production Supply Area (Optional) [page ] 40 | Warehouse Clerk (EWM) | Clear Production Supply Areas (/SCWM/MFG_STAGING_REVERSAL) | You created warehouse tasks to move components from PSA back to the final storage bin. |
| Confirm Warehouse Task for PSA Clearance (Optional) [page ] 41 | Warehouse Operative (EWM) | Process Warehouse Tasks (F4595) | You have confirmed the warehouse tasks to move the components back to the final storage bin. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Release Production Order

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
|  | Log On | Log on to the SAP Fiori Launchpad as a Production Supervisor - Discrete Manufacturing | The SAP Fiori Launchpad opens. |  |
|  | Access App | Open Manage Production Orders(F2336). | The Manage Production Orders(F2336) screen appears. |  |
|  | Check Default Area of Responsibility (Supervisor) | Choose the user icon and select App Settings. Choose tab Production Supervisors.In the AOR Status column, choose the button to assign or unassign entries, and make sure only the following entries are assigned:Plant 1 US (1 7 10)MTS DI - Valuated (YB1) |  |  |
|  | Choose Back | Choose Back. |  |  |
|  | Select Production Order | On the Manage Production Orders screen, choose Adapt Filters to display more filter options. In the Adapt Filters dialog box, select Material and ProductionPlant and choose OK.Enter the following filter criteria, and choose Go:Status: Created.Material: SG524, SG724, SG824 or FG428.Production Plant: 1710. | The Material and Production Plant fields are added to filter bar.The searched order is displayed. |  |
|  | Note down production order number | Note down your production order number: ______________ |  |  |
|  | Select Order | On the Manage Production Orders(F2336) screen, select your production order by choosing the checkbox beside the order number. |  |  |
|  | Choose Edit. | Choose Edit. | The Production O rder Change: Header screen appears. |  |
|  | Release Order | On the Production O rder Change: Header screen,choose Release Order . | The following system message appears: R elease carried out |  |
|  | Save | Save your entries. | The Information dialog box appears.The following system message appears: Order number <number> saved. |  |
|  | Choose Exit | In the Information dialog box, choose Exit. |  |  |

### Trigger Creation of Production Material Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you trigger the creation of the production material request by executing the WM material staging function. The production material request is a representation of the manufacturing order in warehouse management.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
|  | Log On | Log on to the SAP Fiori Launchpad as a Production Supervisor - Discrete Manufacturing | The SAP Fiori Launchpad opens. |  |
|  | Access App | Open Manage Production Orders(F2336). | The Manage Production Orders(F2336) screen appears. |  |
|  | Check Default Area of Responsibility (Supervisor) | Choose the user icon and select App Settings. Choose tab Production Supervisors.In the AOR Status column, choose the button to assign or unassign entries, and make sure only the following entries are assigned:Plant 1US (1710)MTS DI - Valuated (YB1) |  |  |
|  | Choose Back | Choose Back. |  |  |
|  | Select Production Order | On the Manage Production Orders screen, choose Adapt Filters to display more filter options. In the Adapt Filters dialog box, select Material and ProductionPlant and choose OK.Enter the following filter criteria, and choose Go:Status: ReleasedMaterial: SG524, SG724, SG824 or FG428.Production Plant: 1710. | The Material and Production Plant fields are added to filter bar.The searched order is displayed. |  |
|  | Select Order | On the Manage Production Orders(F2336) screen, select your production order by choosing the checkbox beside the order number. |  |  |
|  | Choose Edit. | Choose Edit. | The Production Order Change: Header screen appears. |  |
|  | Execute WM Material Staging | On the Production order Change: Header screen, choose Menu > Functions > WM Material Staging > Execute . | The following system message appears: Material staging was executed successfully. |  |
|  | Save | Save your entries. | The Information dialog box appears.The following system message appears: Order number <number> saved. |  |
|  | Choose Exit | In the Information dialog box, choose Exit. |  |  |

### Check Production Material Request (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you verify that the production material request was created successfully.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
|  | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk (EWM). | The SAP Fiori Launchpad opens. |  |
|  | Access App | Open Display Production Material Requests(/SCWM/MONNAV_PMR). | The Production Material Request screen appears. |  |
|  | Set Filter Criteria | On the Production Material Request screen, choose Set Selection Criteria. | A dialog box with filter options appears. |  |
|  | Set Filter Criteria | In the dialog box with the filter criteria, make the following entries:Manufacturing Order: <your order number> |  |  |
|  | Choose Execute | Choose Execute. | The Production Material Request screen appears.The Production Material Request associated with your manufacturing order is listed. |  |
|  | Select PMR | On the Production Material Request screen, select the line item with your production material request and choose Mat.Req.Items. | The Material Request Items section appears on the bottom half of the screen. |  |
|  | Verify Items | On the Production Material Request screen, in the Material Request Items section, verify that there is a line item for each component:RM124 as component for SG824SG224 as component for FG428RM324,RM424, and RM524 as components for SG524 and SG724with the corresponding staging methods and associated staging bins. | There is a line item for each component. |  |

### Create Staging Warehouse Tasks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create warehouse tasks for the staging process. The warehouse tasks are for moving the components from the storage bin to the production supply area.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
|  | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk (EWM). | The SAP Fiori Launchpad opens. |  |
|  | Access App | Open Create Warehouse Tasks - Staging for Production(/SCWM/STAGE). | The Schedule Staging for Production screen, appears. |  |
|  | Make Entries | On the Schedule Staging for Production screen, make the following entries:Warehouse Number: 1750Manufacturing Order: <your manufacturing order>Select the Period ends at specific time checkbox.In the Date and Time input fields, enter values after the requirement date of your manufacturing order.Deselect the Test Mode checkbox. |  |  |
|  |  | Choose Run. | The Display Logs screen appearsOn the bottom section, the following system messages appear for each warehouse order created:Warehouse order <warehouse order number> created |  |
|  |  | Note down the warehouse order numbers. |  |  |

### Confirm Staging Warehouse Tasks

In this section, you confirm the staging warehouse you created in the previous step.

#### Variant 1: With Fiori App

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A warehouse tasks list / pick list is printed and handed over to the Warehouse Operative (EWM), who performs the warehouse tasks and confirms them in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Operative (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Process Warehouse Tasks (F4595). | The Process Warehouse Tasks (F4595) screen appears. |  |
| 3 | Enter your Warehouse Order | On the Process Warehouse Tasks screen, make the following entries:Warehouse Order: <Warehouse Order Number from previous step>Choose Go. | The Warehouse Tasks associated with your warehouse order are displayed. |  |
| 4 | Choose Warehouse Task | On the Process Warehouse Tasks screen, in the Warehouse Tasks section, choose a Warehouse Task to go into the warehouse task details. | The Warehouse Task screen is displayed. |  |
| 5 | Maintain Pick-HU | On the Warehouse Task screen, in the Movement Data tab, choose Maintain Pick-HU. | The Maintain Pick-HU dialog box is displayed. |  |
| 6 | Create Pick-HU | In the Maintain Pick-HU dialog box, choose Create Pick-HU. | The Create Pick-HU dialog box is displayed. |  |
| 7 | Enter Packaging Material | In the Create Pick-HU dialog box, enter a Packaging Material, for example PMPALLET, and choose Create. | The Maintain Pick-HU dialog box with the newly created Pick-HU is displayed. Note down the HU number. |  |
| 8 | Return to Warehouse Task Screen | In the Maintain Pick-HU dialog box, choose Close. | The Warehouse Task screen is displayed and the Destination Handling Unit dropdown menu is populated with the HU number. |  |
| 9 | Check Warehouse Task Details | For material RM424:Material RM424 is a batched-managed material. To maintain the batches, continue with steps 10–11.For material RM524:Material RM524 is a serialized material. To maintain serial numbers, continue with steps 12–13.For material RM124 and SG224:Continue with step 14. | The Warehouse Task screen is displayed. |  |
| 10 | Maintain Batch (optional) | On the Warehouse Task screen, on the Movement Data tab, choose the batch value help, if the batch is not selected automatically. | The Select: Batch dialog box is displayed. |  |
| 11 | Select Batch (optional) | In the Select: Batch dialog box, in the Items section, select a batch. Continue with step 14. | The Select: Batch dialog box closes. You have selected a batch. |  |
| 12 | Maintain Serial Number (optional) | On the Warehouse Task screen, in the Movement Data section, choose No. of Serial Numbers Entered: X / X. | The Serial Number Assignment dialog box is displayed. |  |
| 13 | Enter Serial Number (optional) | In the Serial Number Assignment dialog box, enter serial numbers in the Enter Serial Number input field until a serial number for every item is selected. Choose OK. Continue with step 14. | You have assigned serial numbers. |  |
| 14 | Confirm Warehouse Task | On the Warehouse Task screen, choose Confirm. | You have confirmed the warehouse task.The following system message appears:Warehouse task <warehouse task number> confirmed. |  |
| 15 | Repeat for other warehouse orders | Repeat steps 3 to 14 for the other warehouse orders from chapter Create Staging Warehouse Tasks. |  |  |

#### Variant 2: With Radio Frequency Devices

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Operative (EWM) performs the warehouse tasks and confirms them in the system with a mobile Radio Frequency device.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Operative (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open the SAP Fiori app Test RF Environment (/SCWM/RFUI).Note The app allows you to test working in an RF environment. For working with mobile RF devices, see also SAP Note [3048632](https://me.sap.com/notes/3048632). |  |  |
| 3 | Enter Data for RFUI | Whse No: 1750Resource: SHR1-1DefPresDvc: SE01Choose Enter. |  |  |
| 4 | Choose Menu | Choose 01 System-Guided > 02 SystemGuided Queue. |  |  |
| 5 | Enter Queue Name | In the Queue field, enter SR-F01-105 to find the warehouse task for component RM124. For all other components, enter SR-001-105.Choose Enter. |  |  |
| 6 | Create Picking HU | Make the following entries:Pack.Mat: PMPALLETChoose HUCrt. | The picking HU is created. |  |
| 7 | Choose Next | Scroll the screen to the right using the icon > and choose Next. |  |  |
| 8 | Enter or Verify the Source and Destination Information Fields | Enter or verify the following fields, if required:Src.Bin (Source Bin)SrceHU (Source HU)Prod. (Product)ActQty (Quantity)DestHU (Destination HU)Choose Enter. |  |  |
| 9 | Enter Serial Number (optional) | Enter a serial number and choose Enter in the following field: SNEnter serial numbers for the complete quantity.Field SNsCrt: XX / XX indicates the total number of required entries and the number of entries already made.Choose Save. |  |  |
| 10 | Verify the Destination Information Fields | Verify the following fields:DstBin (Destination Bin)Choose Enter. |  |  |
| 11 | Repeat Steps | Repeat steps 6 to 8 until no suitable warehouse orders are found. |  |  |
| 12 | Logoff RFUI | You can choose Back to go to the previous screens.Choose Logoff.Choose Save. |  |  |

### Post Consumption of Components

In this section, you post the consumption of the components for your production material request/ production order. You can either post consumption by confirming the production order operations, if the components are set up to backflush or consume the components directly in your warehouse. In case you are testing the process variant with backflush components (materials FG826 and SG824 , proceed with the Confirm Production Operations for Subassembly step. For non-backflush components, proceed with the Post Consumption of Components in Warehousestep.

#### Variant 1: Confirm Production Operations for Subassembly

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The confirmation documents include the processing status of orders, operations, sub-operations, and individual capacities. It's an instrument for controlling orders. This process step shows you how to confirm subassembly production order operations for semifinished material SG824. A goods movement document is generated when the last operation is confirmed. The backflush is carried out together with the confirmation steps.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
|  | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
|  | Access the App | Open Confirm Production Operation(F3069). |  |  |
|  | Enter Production Order and Operation | On the Enter Order and Operation screen, make the following entries and choose Go:Order: <Production Order Number>Operation: <operation number> for example 0010 |  |  |
|  | Enter Quantities Data | In the Quantities section, make the following entries:Yield: <Quantity of prod. order less scrap>Scrap: <scrap amount> |  |  |
|  | Check Material Movements | In the Material Movements section, check the material list.Note The system shows you an overview materials table, for which the material withdraws are done along with operation confirmation.The material RM124 is set for backflush (in material master) for withdraws to be done automatically after the operation is confirmed. |  |  |
|  | Enter Activities Data and Save | In the Activities section, make the following entries:Setup: <setup time>Machine: <machine time>Labor: <labor time>For partial confirmation, choose Post.For final confirmation, choose Post and Complete. | Confirmation is made. |  |
|  | Repeat Steps | Go back and repeat steps 3 to 6 for Operation0020 and 0030. |  |  |
|  | Good Receipt | When all operations are finally confirmed, all materials consumed in production are backflushed. | Backflush for all consumed materials is done. |  |

#### Variant 2: Post Consumption of Components in Warehouse

In this section, you post the consumption of the components for your production material request/ production order for materials SG524, SG724 or FG428 in your warehouse.

|  |
| --- |
| Note Note: . If the component requirement is greater than 2, repeat the following steps:Create Staging Warehouse TasksConfirm Staging Warehouse TasksVariant 2: Post Consumption of Components in WarehouseContinue repeating these steps until the complete component requirement is satisfied, as the replenishment quantity is set at 2 per iteration.See step Assign Bins to PSA. |

##### Variant 1: With Fiori App

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Clerk (EWM) posts the consumption of the components for the production material request using a Fiori app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk (EWM). | The SAP Fiori Launchpad opens. |  |
| 2 | Access App | Open Post Consumption - Production (/SCWM/MFG_CONSUMPTION). | The Consumption by Production screen appears. |  |
| 3 | Choose Settings | On the Consumption by Production screen, choose Settings on the upper left corner. | The Default Values dialog box appears. |  |
| 4 | Make Entries | In the Maintain Default Values dialog box, make the following entries:Warehouse Number: 1750Choose OK. | The Consumption by Production screen appears. |  |
| 5 | Enter Order Details | On the Consumption by Production - Warehouse Number 1750 screen, make the following entries:Manufacturing Order: <your manufacturing order number for SG524, SG724, or FG428>Choose Consumption. | The Consumption by Production - Manufacturing Order: <your manufacturing order number>, Warehouse 1750 screen appears. |  |
| 6 | Choose a Stock Item | On the Consumption by Production - Manufacturing Order <your manufacturing order number>, Warehouse 1750 screen, in the Stock for Consumption section, choose a stock item of component RM424, RM524 or SG224 you want to post the consumption for. | The Consumption Posting and Additional Manufacturing Order Information sections are updated with information of the stock item you selected. |  |
| 7 | Choose Serial Number/UII (optional) | In case of component RM524, as it is serial number managed, choose Serial Number/UII in the Consumption Posting section if serial numbers was not assigned during staging warehouse task confirmation. | The Serial Number Range dialog box appears. |  |
| 8 | Make Entries for Serial Numbers (optional) | In the Serial Number Range dialog box, enter serial numbers. You can enter numbers individually by entering a single number in field From Serial Number or enter a range by filling fields From Serial Number and To Serial Number.Choose Assign Serial Numbers/UII. Assign Serial Numbers for the complete quantity. | In the Serial Number Range dialog box, in the table in the bottom section, the Serial Numbers you entered are displayed. You have assigned Serial Numbers for the components. |  |
| 9 | Close Dialog Box (optional) | In the Serial Number Range dialog box, choose Close. | The Consumption by Production - Manufacturing Order: <your manufacturing order number>, Warehouse 1750 screen appears. |  |
| 10 | Enter Consumption Posting Details | In the Consumption Posting section, make the following entries:Quantity to consume: <the quantity you want to consume> |  |  |
| 11 | Choose Post Consumption | Choose Post Consumption. | The following system message appears: Stock consumed successfully |  |
| 12 | Repeat Steps 6 to 8 | Repeat steps 6 to 8 until the required quantities of each component are consumed. | You posted the consumption of the required components. |  |

##### Variant 2: With Radio Frequency Devices

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Operative (EWM) posts the consumption of the components for the production material request using a radio frequency device.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Operative (EWM). | The SAP Fiori Launchpad opens. |  |
| 2 | Access App | Open the SAP Fiori app Test RF Environment (/SCWM/RFUI).Note The app allows you to test working in an RF environment. For working with mobile RF devices, see also SAP Note [3048632](https://me.sap.com/notes/3048632). |  |  |
| 3 | Enter Data for RFUI | Make the following entries:Whse No: 1750Resource: SHR1-1DefPresDvc: SE01Choose Enter. |  |  |
| 4 | Choose Menu | Choose 04 Outbound Process > 04 Consumption > 01 Consumption by Manu. Order. |  |  |
| 5 | Enter Manufacturing Order | Make the following entries:ManufOrd: <your manufacturing order number for SG524, SG724, or FG428>Choose Enter. |  |  |
| 6 | Enter HU Number | Make the following entries:HU/Bin: <number of pick HU from previous step>Choose Enter. |  |  |
| 7 | Enter Component | Make the following entries if not selected automatically:Product: RM424, RM524 or SG224Choose Enter. |  |  |
| 8 | Enter Quantity | Make the following entries:ConsQty: <quantity to be consumed>Choose Enter. | The component has been consumed. |  |
| 9 | Repeat Steps from 6 to 8 | Repeat Steps from 6 to 8 until all required components are consumed. |  |  |

### Reverse Consumption of Components (Optional)

In this section, you reverse the consumption of the components in the previous step for your production material request in the warehouse. You can reverse the consumption using a Fiori app or using radio frequency devices.

|  |
| --- |
| Note Note This step is only relevant for materials SG524, SG724 and FG428 without backflush components, where you have posted the consumption of the components following section Variant 2: Post Consumption of Components in Warehouse. |

#### Variant 1: With Fiori App

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Clerk (EWM) reverses the consumption posts of the components for the production material request using an SAP Fiori app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk (EWM). | The SAP Fiori Launchpad opens. |  |
| 2 | Access App | Open Post Consumption - Production (/SCWM/MFG_CONSUMPTION). | The Consumption by Production screen appears. |  |
| 3 | Choose Settings | On the Consumption by Production screen, choose Settings on the upper left corner. | The Default Values dialog box appears. |  |
| 4 | Make Entries | In the Default Values dialog box, make the following entries:Warehouse Number: 1750Choose OK. | The Consumption by Production screen appears. |  |
| 5 | Enter Order Details | On the Consumption by Production screen, make the following entries:Manufacturing Order: <your manufacturing order number for material SG524, SG724 or FG428>Choose Reversal. | The Reversal by Production - Manufacturing Order <your manufacturing order number>, Warehouse 1750 screen appears. |  |
| 6 | Choose a Stock Item | On the Reversal by Production - Manufacturing Order: <your manufacturing order number>, Warehouse 1750 screen, in the Consumed Stock section, choose a stock item you want to reverse the consumption for. | The Reversal Posting and Additional Manufacturing Order Information sections are updated with information of the stock item you selected. |  |
| 7 | Enter Reversal Posting Details | In the Reversal Posting section, make the following entries:Reversal Quantity: <quantity you want to reverse>Note In case you want to reverse the consumption of serialized material RM524 partially, specify the serial numbers to post the reversal for. Follow steps 8-10. Otherwise continue with step 11. |  |  |
| 8 | Choose Serial Number/UII (optional) | In case you want to reverse the consumption of serialized material RM524 partially, choose Serial Number/UII in the Reversal Posting section. | The Serial Number Range dialog box appears. |  |
| 9 | Make Entries for Serial Numbers (optional) | In the Serial Number Range dialog box, enter serial numbers. You can enter numbers individually by entering a single number in field From Serial Number or enter a range by filling fields From Serial Number and To Serial Number.Choose Assign Serial Numbers/UII. | In the Serial Number Range dialog box, in the table in the bottom section, the Serial Numbers you entered are displayed. You have assigned Serial Numbers for the components. |  |
| 10 | Choose Close | In the Serial Number Range dialog box, choose Close. |  |  |
| 11 | Choose Post Reversal | Choose Post Reversal. | The following system message appears: Stock reversal successful. |  |
| 12 | Repeat Steps 6 to 12 | Repeat steps 6 to 12, if you want to reverse the consumption of other components. |  |  |

#### Variant 2: With Radio Frequency Devices

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Operative (EWM) reverses the consumption posts of the components for the production material request using a radio frequency device.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Operative (EWM). | The SAP Fiori Launchpad opens. |  |
| 2 | Access App | Open the Test RF Environment app (/SCWM/RFUI).Note The app allows you to test working in an RF environment. For working with mobile RF devices, see also SAP Note [3048632](https://me.sap.com/notes/3048632). |  |  |
| 3 | Enter Data for RFUI | Make the following entries:Whse No: 1750Resource: SHR1-1DefPresDvc: SE01Choose Enter. |  |  |
| 4 | Choose Menu | Choose 04 Outbound Process > 04 Consumption > 01 Rev. Cons. by MO/HU. |  |  |
| 5 | Enter Manufacturing Order | Make the following entries:ManufOrd: <your manufacturing order number for material SG524, SG724 or FG428>Choose Enter. |  |  |
| 6 | Enter HU Number | Make the following entries:HU/: <number of pick HU from previous step>Choose Enter. |  |  |
| 7 | Enter Quantity | Make the following entries:RevQty: <quantity to reverse the consumption for>Choose Enter.Note: In case you want to reverse the consumption of material RM524, as it is serialized, enter the full quantity consumed. Reversing the consumption of partial quantities is not supported for serialized components in RF environment. | The consumption of the component was reversed. |  |

### Clear Production Supply Area (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create warehouse tasks to move material, which hasn’t been consumed during the production process from the production supply area back to the final storage bin.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk (EWM). | The SAP Fiori Launchpad opens. |  |
| 2 | Access App | Open Clear Production Supply Areas(/SCWM/MFG_STAGING_REVERSAL). | The Clear Production Supply Areas(/SCWM/MFG_STAGING_REVERSAL) screen appears. |  |
| 3 | Choose Settings | On the Clear Production Supply Area screen, choose Settings on the top left. | The Maintain Default Values dialog box appears. |  |
| 4 | Apply Settings | In the Maintain Default Values dialog box, make the following entries:Warehouse Number: 1750Hours in Past (Consumption Posting): 500Choose Enter. | The Clear Production Supply Area screen appears. |  |
| 5 | Enter Search Criteria | On the Clear Production Supply Area - 1750 screen, in the Search Criteria section, set the following criteria:From the left dropdown list, select Production Supply Area as search criteria.From the dropdown list in the center, select equals to as search operator.In the right value field, enter PSA_03 / 1710 using the value help.Choose Search. | In the bottom half of the screen, in the Stock Without Released Production Material Request section, the stock items matching your search criteria appear. |  |
| 6 | Release Stock from PMR (optional) | On the Clear Production Supply Area - 1750 screen, in the Stock Without Released Production Material Request Section, select the stock items you want to release from the PMR.Choose Release Reference Document. | The following system message appears: <number of selected stock items> stock items released.The selected stock items no longer have references to a production material request or manufacturing order. |  |
| 7 | Create WT | On the Clear Production Supply Area - 1750 screen, in the Stock Without Released Production Material Request section, select a stock items.Choose Create Warehouse Task. | The following system message appears: Warehouse task <WT number> created.Note down the warehouse task number |  |

### Confirm Warehouse Task for PSA Clearance (Optional)

To confirm the warehouse tasks created to move material back from PSA to the storage bin, follow up with Confirm Warehouse Tasks step in Warehouse Inbound Processing test script.

In step Variant 1: With Fiori App, use app Process Warehouse Tasks(F4595) and search for your warehouse tasks with the help of the warehouse task numbers from previous step. In step Variant 2: With Radio Frequency Devices use queue SR-105-001.

#### Variant 1: With Fiori App

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A Putaway List is printed and handed over to the Warehouse Operative (EWM). The user performs the warehouse tasks and confirms them in the system. Note that he or she can also confirm warehouse tasks using the app Warehouse Monitor (/SCWM/MON) (Business Catalog WM – Monitoring).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as a Warehouse Operative (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open the SAP Fiori app Process Warehouse Tasks (F4595). | The Confirm Warehouse Tasks screen appears. |  |
| 3 | Enter Warehouse Task Number | On the Process Warehouse Tasks screen, make the following entries:Warehouse Task: <Your warehouse task number>.Choose Go. |  |  |
| 4 | Check Warehouse Task Details | If you would like to check the Serial Numbers assigned, follow step 4–7. Otherwise go directly to step 7.Choose the Warehouse Task to go into the Warehouse Task details. |  |  |
| 5 | Choose Serial Number link | On the Warehouse Task screen, in the Movement Data section, choose No. of Serial Numbers Entered: X / X. |  |  |
| 6 | Check Serial Number | On the Serial Number Assignment screen, check the serial numbers in the List of Serial Numbers.Choose Cancel twice to go back to the Process Warehouse Task screen. |  |  |
| 7 | Confirm Warehouse Task | Mark the checkbox for the selected Warehouse Task and choose Confirm. | The following system message appears:Warehouse task confirmed. |  |

#### Variant 2: With Radio Frequency Devices

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Operative (EWM) performs the warehouse tasks and confirms them in the system with a mobile Radio Frequency device.

|  |
| --- |
| Note For working with mobile RF devices, make sure all the steps as described in the Setup Instruction guide for scope item 63V - Mobile RF Devices in Warehousing have been performed. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as a Warehouse Operative (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open the SAP Fiori app Test RF Environment (/SCWM/RFUI).Note The app allows you to test working in an RF environment. For working with mobile RF devices, see also SAP Note [3048632](https://me.sap.com/notes/3048632). |  |  |
| 3 | Enter Data for RFUI | Whse No: 1750Resource: SHA1-1DefPresDvc: SE01Choose Enter. |  |  |
| 4 | Choose Menu | Choose 01 System-Guided > 02 SystemGuided Queue. |  |  |
| 5 | Enter Queue Name | In the Queue field, enter SR-105-001.Choose Enter. |  |  |
| 6 | Choose Next | Scroll the screen to the right using the icon > and choose Next. |  |  |
| 7 | Verify the Source Information Fields | Verify the following fields, if they are required:Src.Bin (Source Bin)SrcHU (Source HU)Prod. (Product)ActQty (Actual Quantity)Choose Enter. |  |  |
| 8 | Verify the Destination Information Fields | Verify the following fields, if they are required:Prod. (Product)ActQty (Quantity)Dest.Qty (Destination Quantity)DstBin (Destination Bin)Choose Enter. |  |  |
| 9 | Repeat Steps | Repeat steps 6 to 8 until no suitable warehouse orders are found. |  |  |
| 10 | Logoff RFUI | You can choose Back to go to the previous screens.Choose Logoff.Choose Save. |  |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

The following processes and conditions can proceed this process.

| Process | Business Condition |
| --- | --- |
| BJ5 - Make-to-Stock Production – Discrete Manufacturing | Planned orders are a prerequisite for the process. Make sure the following steps are fulfilled:Anonymous Forecast and MRPCreate Planned Independent RequirementsMaterial Requirements Planning at Plant LevelEvaluate Stock/Requirements SituationProduction Order Conversion and Available-to-Promise CheckConversion to Production Orders for Subassembly and Final AssemblyThere are several sets of material master data available for testing the process variants in this test script. Refer to below table for an overview of the scenarios and the associated materials. Once you created the production order, note down the production order number for the semifinished goods:Table 3:ScenarioMaterial MasterGoods receipt with synchronized goods movementFG526, SG524, RM324, RM424, RM524Goods receipt with synchronized goods movement, backflush componentFG826, SG824, RM124Goods receipt with deliveriesFG726, SG724, RM324, RM424, RM524 |
| BJE - Make-to-Order Production – Finished Goods Sales and Final Assembly | Planned orders are a prerequisite for the process. Make sure the steps in following sections are fulfilled:MTO Sales Processing (Material w/o Sales Order BoM)Down Payment ProcessingProduction PlanningProduction ProcessingIn section Production Processing, execute step Create Production Order only. Use material FG428. Once you created the production order, note down the production order number for the finished good:Table 4:ScenarioMaterial MasterGoods receipt with synchronized goods movementFG428, SG224 |

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| BJ5 - Make-to-Stock Production – Discrete Manufacturing | To complete the production process, follow up with the process step Confirm Production Operations for Subassembly in the Make-to-Stock Production – Discrete Manufacturing test script.Note Note This succeeding process is relevant for materials SG524 and SG724. |
| BJE - Make-to-Order Production – Finished Goods Sales and Final Assembly | To complete the production process, follow up with the process step Confirm Assembly Activities in the Production Processing section in - Make-to-Order Production – Finished Goods Sales and Final Assembly test script.Note Note This succeeding process is relevant for materials FG428. |
| 5HO - Warehouse Production Integration with Synchronous Goods Receipt | To receive and putaway the semifinished goods SG524, SG824 or finished good FG428 in the warehouse, follow up with the process steps in section Goods Receipt from Production with Synchronous Goods Movements in the Warehouse Production Integration with Synchronous GoodsReceipt test script. As SG524, SG824 and FG428 arent set up for automatic goods receipt with confirmation of the production order steps, step Post Goods Receipt for Production Orders (Optional) is mandatory. |
| 3DV - Warehouse Production Integration | To receive and putaway the semifinished good SG724 in the warehouse, follow up with the process steps in section Delivery-Based Goods Receipt from Production in the Warehouse Production Integration test script. |

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
> Flagged while digesting this document, not verified: Sample organizational data (company code 3310, plant 3310, storage location 335W, warehouse number 335, warehouse 3350) disagrees with the values used in the test steps (plant 1710, warehouse number 1750, storage location 175W, PSA_03 / 1710).

> [!warning] Conflict
> Flagged while digesting this document, not verified: RM124 staging warehouse process type is S220 in the Assign Bins to PSA overview table, but the procedure step for RM124 enters Staging WPT S320 (S320 is described as the Cross-Order Staging type while RM124 is Single-Order Staging).

> [!warning] Conflict
> Flagged while digesting this document, not verified: Replenishment quantity for RM424/RM524/RM124 is 4 in the Assign Bins to PSA table, yet the Post Consumption note says the replenishment quantity is set at 2 per iteration.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[11-inventory-warehouse-and-transportation/atualizar-area-de-abastecimento-da-producao-mds-3ks-344]]
- related-to :: [[11-inventory-warehouse-and-transportation/maintain-production-supply-area-mds-3ks-341]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-3ks-343]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-3ks-345]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6NI_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 78,879 chars in the whole document
