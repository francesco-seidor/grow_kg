---
id: 11-inventory-warehouse-and-transportation/test-script-warehouse-production-integration-with-synchronous-goods-re
title: "Test Script: Warehouse Production Integration with Synchronous Goods Receipt (5HO_AE) (5HO_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud 2608 test script for scope item 5HO_AE: staging material to production and synchronous goods receipt into the EWM warehouse."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/ewm-production-integration]
aliases: [5HO_S4CLD2608_BPD_EN_AE]
keywords: [EWM Production Supply and Receipt, synchronous goods receipt, warehouse production integration, material staging, staging warehouse tasks, putaway warehouse tasks, control cycle, production order confirmation, component consumption posting, packing instructions]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5HO_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1099
topic: 11-inventory-warehouse-and-transportation/ewm-production-integration
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Warehouse Production Integration with Synchronous Goods Receipt (5HO_AE) (5HO_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5HO_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **EWM Production Supply and Receipt** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Warehouse Production Integration with Synchronous Goods Receipt (5HO_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232857186)

[2 Prerequisites 4](#_Toc232857187)

[2.1 System Access 4](#_Toc232857188)

[2.2 Roles 4](#_Toc232857189)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232857190)

[2.4 Business Conditions 7](#_Toc232857191)

[2.5 Preliminary Steps 8](#_Toc232857192)

[2.5.1 Define Default Values for Warehouse Clerk (WM) 8](#_Toc232857193)

[2.5.2 Define Default Values for Warehouse Operative (WM) 9](#_Toc232857194)

[2.5.3 Assign Fixed Storage Bins to Component 10](#_Toc232857195)

[2.5.4 Create Control Cycle 10](#_Toc232857196)

[2.5.5 Create Initial Stock for Component 12](#_Toc232857197)

[2.5.5.1 Create Initial Stock for Component using Migration Cockpit 12](#_Toc232857198)

[2.5.5.2 Initial Stock Posting for the Material of BoM 12](#_Toc232857199)

[2.5.6 Maintain Warehouse Product Attributes to Automatically Create Putaway Warehouse Tasks (Optional) 13](#_Toc232857200)

[2.5.7 Manage Packing Instruction (Optional) 15](#_Toc232857201)

[2.5.7.1 Create Packing Instruction 15](#_Toc232857202)

[2.5.7.2 Create Packing Instruction Determination 16](#_Toc232857203)

[3 Overview Table 18](#_Toc232857204)

[4 Test Procedures 20](#_Toc232857205)

[4.1 Material Staging for Production 20](#_Toc232857206)

[4.1.1 Release Production Order 20](#_Toc232857207)

[4.1.2 Staging Release Order Parts for Production 21](#_Toc232857208)

[4.1.3 Staging Pick Parts for Production 23](#_Toc232857209)

[4.1.4 Create Staging Warehouse Tasks 24](#_Toc232857210)

[4.1.5 Material Staging with Ad-Hoc Movements (Optional) 26](#_Toc232857211)

[4.1.6 Confirm Staging Warehouse Tasks 27](#_Toc232857212)

[4.1.6.1 Variant 1: With Fiori App 27](#_Toc232857213)

[4.1.6.2 Variant 2: With Radio Frequency Devices 29](#_Toc232857214)

[4.2 Confirm Production Operations for Subassembly 31](#_Toc232857215)

[4.3 Post Consumption of Components 32](#_Toc232857216)

[4.4 Goods Receipt from Production with Synchronous Goods Movements 34](#_Toc232857217)

[4.4.1 Post Goods Receipt for Production Orders (Optional) 34](#_Toc232857218)

[4.4.2 Display Material Document (Optional) 36](#_Toc232857219)

[4.4.3 Pack Finished Material (Optional) 37](#_Toc232857220)

[4.4.4 Create HU Putaway Warehouse Task (Optional) 39](#_Toc232857221)

[4.4.5 Create Product Putaway Warehouse Tasks (Optional) 40](#_Toc232857222)

[4.4.6 Confirm Putaway Warehouse Tasks 41](#_Toc232857223)

[4.4.6.1 Variant 1: With Fiori App 42](#_Toc232857224)

[4.4.6.2 Variant 2: With Radio Frequency Devices 43](#_Toc232857225)

[5 Appendix 45](#_Toc232857226)

[5.1 Process Integration 45](#_Toc232857227)

[5.1.1 Succeeding Processes 45](#_Toc232857228)

## Purpose

Overview

This scope item describes the integration of warehouse production with synchronous goods receipt, where the produced products can post goods receipts directly into the warehouse without involving delivery documents. With this business process, you can integrate the supply of products to production and the receipt of finished products from production into your warehouse. You first trigger the staging of material that is requested by production. This activity results in a posting change delivery (warehouse-managed production supply area). Further process steps (such as the creation of warehouse tasks) are initiated based on this document. A warehouse operative moves the material to the production supply area and confirms the warehouse tasks accordingly. The produced products can post goods receipts directly into the warehouse without involving delivery documents. Finally, the finished goods from production – to be stored in the warehouse – are moved to the final bin.

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
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Warehouse Clerk (EWM) | SAP_BR_WAREHOUSE_CLERK_EWM | Warehouse Office | SAP_BR_WAREHOUSE_CLERK_EWM |  |
| Warehouse Operative (EWM) | SAP_BR_WAREHOUSE_OPERATIVE_EWM | Warehouse Floor | SAP_BR_WAREHOUSE_OPERATIVE_EWM |  |
| Master Data Specialist - Handling Unit Data | SAP_BR_HU_MASTER_SPECIALIST | Master Data - Handling Units | SAP_BR_HU_MASTER_SPECIALIST |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | RM124 | RAW124, VB, Consumption, FixedBin | 1 PAL = 100 PCComponent for SG424 and SG624. |
| Material | RM224 | RAW224,VB, Consumption | 1 PAL = 100 PCComponent for SG424 and SG624. |
| Material | RM624 | RAW624,VB, Consumption | 1 PAL = 100 PCComponent for SG624. |
| Material | FG426 | FIN426, MTS-DI, PD, SerialNo, bin-managed PSA | Use this material to test the WM-managed production supply process with automatic goods receipt posting from production. |
| Material | SG424 | SEMI424, PD, Subassembly, bin-managed PSA | 1 PAL = 8 PCUse this material to test the WM-managed production supply process with automatic goods receipt posting from production. |
| Material | FG626 | FIN626, MTS-DI, PD, SerialNo, bin-managed PSA | Use this material instead of FG426 to test the WM-managed production supply process with manual goods receipt posting from production. |
| Material | SG624 | SEMI624, PD, Subassembly, bin-managed PSA | 1 PAL = 8 PCUse this material instead of SG424 to test the WM-managed production supply process with manual goods receipt posting from production. |
| Material | FG328 | FIN328,MTO,PD,Batch-Fifo,SerialNo | Use this material to test Goods Receipt from Production within an MTO-Scenario |
| Material | SG22 | SEMI22,PD,Phantom | Component for FG328 |
| Material | SG25 | SE-MI25,PD,ExternalProcurement | Component for FG328 |
| Material | RM122 | RAW122,PD,Batch-Fifo,ProcureImport | Component for FG328 |
| Material | RM128 | RAW128,PD,Consignment | Component for FG328 |
| Material | RM120 |  | Component for FG328 |
| Material | SG224 | SEMI224,MTO,PD,Subassembly | Component for FG328 |
| Material | RM27 | RAW27,PD,PackagingBox | Component for FG328 |
| Production Version | 0001 | Production Version 1 | Production Versions of Materials FG426, SG424, FG626, SG624, FG328, SG22 and SG224 |
| Packaging Material | PMPALLET |  |  |
| Packaging Material | PMPALLET_GTL | Pallet for GTL |  |
| Company Code | 3310 |  |  |
| Plant | 3310 |  |  |
| (Replenishment) Storage Location | 335W |  |  |
| Production Supply Area | PSA_02 | WM-managed Sloc | This is a production supply area in an WM-managed storage location. Use this to stage material for production where the source and the destination storage locations are WM-managed. |
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

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | You’ve completed the step described in the Create New Open MM Posting Period - MDS (BNZ) master data script. The posting period is up to date. |
| BJ5 - Make-to-Stock Production – Discrete Manufacturing | Planned orders are a prerequisite for the process. Make sure the following steps are fulfilled:Anonymous Forecast and MRPCreate Planned Independent RequirementsMaterial Requirements Planning at Plant LevelEvaluate Stock/Requirements SituationProduction Order Conversion and Available-to-Promise CheckConversion to Production Orders for Subassembly and Final AssemblyUse materials FG426 and SG424 or FG626 and SG624.Note that for material SG424, automatic Goods Receipt is active. The system will automatically post Goods Receipt from Production once you confirm the last production operation step. With material SG624, you post Goods Receipt from Production manually. |
| BJE - Make-to-Order Production – Finished Goods Sales and Final Assembly | To test an MTO process, perform below test steps in BJE - Make-to-Order Production – Finished Goods Sales and Final Assembly.When creating the sales order, before saving, select the order item and then choose More > Go to > Item > Shipping . In section Shipping, enter the Storage Location value as a warehouse-managed storage location (for example Storage Location 335W). In section Production Processing, proceed until the completion of the Confirm Assembly Activities step. After this, continue with step Post Goods Receipt for Production Orders (Optional) in this test script. Use material FG328.MTO Sales Processing (Material w/o Sales Order BoM)Down Payment ProcessingProduction PlanningProduction Processing |
| 3BR - Warehouse Inbound Processing | You have completed the step described in Warehouse Inbound Processing test script so that you have the stock to do the posting changes. |

### Preliminary Steps

#### Define Default Values for Warehouse Clerk (WM)

Purpose

In this step, you can define the default warehouse number for the Warehouse Clerk (EWM).

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk (EWM). |  |  |
| 2 | Choose Avatar | Choose Icon for the logon user.Choose Settings. |  |  |
| 3 | Enter Default Value | Choose Default Values.And make the following entry in the section Material Management:Warehouse Number: 3350.Choose Save. |  |  |

#### Define Default Values for Warehouse Operative (WM)

Purpose

In this step, you can define the default warehouse number for the Warehouse Operative (EWM).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Operative (EWM). |  |  |
| 2 | Choose Avatar | Choose Icon for the logon user.Choose Settings. |  |  |
| 3 | Enter Default Value | Choose Default Values.And make the following entry in the section Material Management:Warehouse Number: 3350.Choose Save. |  |  |

#### Assign Fixed Storage Bins to Component

Purpose

In this step, you assign fixed storage bins to products.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk (EWM). |  |  |
| 2 | Access App | Open Assign Fixed Bins (/SCWM/BINMAT). |  |  |
| 3 | Enter Data | On the Maintain Fixed Storage Bins screen, enter the following data:Warehouse Number: 3350.Product: RM124.Choose Run. |  |  |
| 4 | Maintain Fixed Bin | Choose Edit to switch to change mode.Choose Append Row.Enter the following data:WhN: 3350.Disposal: 33413310Storage Bin: SF01-03-04.Product: RM124.Choose Save. |  |  |

#### Create Control Cycle

Purpose

In this activity, you create a control cycle that can be used for in-house production in the production supply area. In the control cycle, you define the demand source, the supply source, and the material staging indicator. The material staging indicator defines the method of how needed materials can be supplied for production with the assis-tance of the warehouse management system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Create Control Cycle for WM (LPK1). | The Create Control Cycle: Initial Screen (WM) screen is displayed. |  |
| 3 | Enter Data | On the Create Control Cycle: Initial Screen (WM) screen, make the following entries:Material :RM124.Plant: 3310.Supply Area: PSA_02. |  |  |
| 4 | Choose Enter | Choose Enter. | The Create Control Cycle: Data Screen (WM) screen is displayed. |  |
| 5 | Enter Control Cycle Details | On the Create Control Cycle: Data Screen (WM) screen, make the following entries:In the Destination section:Staging Ind.: 3 (Release Order Part).In the Source section:Stor. Location: 335W.Warehouse No.: 335.In the Destination Bin Assignment section:Destination Bin: PROD-SUPPLY-2 | The Destination Stor. Location, Destination Warehouse Number, Source Issuing Plant and Source Warehouse No fields are automatically filled by the system. |  |
| 6 | Choose Save | Choose Save. | The following system message appears: Control cycle RM124 1010 PSA_02 is created.You have created the control cycle for staging material RM124 as Release Order Part. |  |
| 7 |  | Repeat the steps using following data to create a control cycle for material RM224 and RM624 as Pick Part:Material :RM224 or RM624.Plant: 3310.Supply Area: PSA_02.In the Destination section:Staging Ind.: 1 (Pick Part).In the Source section:Stor. Location: 335W.Warehouse No.: 335.In the Destination Bin Assignment section:Destination Bin: PROD-SUPPLY-2. | The following system message appears: Control cycle RM224 1010 PSA_02 is created.You have created the control cycle for staging material RM224 and RM624as Pick Part. |  |

#### Create Initial Stock for Component

##### Create Initial Stock for Component using Migration Cockpit

Refer to the Data Migration to SAP S/4HANA from Staging (2Q2) scope item to create initial stock for RM124 in the SF01 fixed and RM224 in the SG01 general storage type and RM624 in the S001 Standard Storage type of the 335W warehouse. Execute the whole process.

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

#### Maintain Warehouse Product Attributes to Automatically Create Putaway Warehouse Tasks (Optional)

Purpose

In this section, you maintain the warehouse product attributes using the Warehouse Monitor (/SCWM/MON) app. Setting the Process Type Determination Indicator, results in the creation of putaway warehouse tasks automatically after the goods receipt was posted.

|  |
| --- |
| Note In case a semi-finished product is to be used as a component for a subsequent production step for final assembly of a finished product, you have the opportunity to move the product to the subsequent PSA without having to carry out the putaway process first. For this, you enter a target PSA in the production version of the product. When automatic warehouse task creation is activated as described in this section, upon goods receipt of the semi-finished product, the system will create a warehouse task towards the bin associated with this PSA via the control cycle for the material and PSA. You can find the target PSA field in the 'Other Data' section in the production version. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk (EWM). |  |  |
| 2 | Access App | Open Warehouse Monitor (/SCWM/MON) | The Warehouse Management Monitor SAP - Warehouse Number XX50 screen is displayed. |  |
| 3 | Navigate to Warehouse Attribute | In the hierarchy in the left screen area, choose Product Master Data > Warehouse Attribute. |  |  |
| 4 | Enter Product Number | In the /SCWM/SAPLPROD_OVERVIEW dialog box, make the following entries:Basic Attributes section:Product Number: SG424 or SG624Choose Execute. |  |  |
| 5 | Select Product | On the Warehouse Management Monitor SAP - Warehouse Number screen, in the Warehouse Attributes area, select the product. |  |  |
| 6 | Choose Mass Change/Create | Choose More Methods > Mass Change/Create . |  |  |
| 7 | Make entries for Process Type Determination Indicator | In the /SCWM/SAPLPROD_OVERVIEW dialog box, make the following entries:Note It is not possible to pack the goods before putaway if automatic putaway warehouse task creation is enabled.In the Warehouse Data section:Proc.Type Det. Ind: S1. |  |  |
| 8 | Choose Execute | Choose Execute. |  |  |
| 9 | Confirm your changes | In the Warehouse Management Monitor SAP - Warehouse Number dialog box, choose Yes. | The following system message appears:1 products save successfully. |  |

#### Manage Packing Instruction (Optional)

##### Create Packing Instruction

Purpose

In this step, you create a packing instruction.

A packing instruction serves as a template for the creation of a handling unit. In a packing instruction, you define the materials and packaging materials to be packed in a handling unit.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Handling Unit Data | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Packing Instruction - Master Data (POP1). | The Create Packing Instruction: Initial screen displays. |  |
| 3 | Create Packing Instruction | To create a new packing instruction, choose Continue or choose Enter.If you want to create a packing instruction from a reference packing instruction, choose a reference packing instruction and then Enter. |  |  |
| 4 | Maintain the description of Packing Instruction | Enter the short text field for the description of the packing instruction. |  |  |
| 5 | Enter Packaging Material | Enter the package material number in field Component of item 10, for example PMPALLET.The Item category P of item 10 means packaging materials. The first line is mandatory for every packing instruction because every packing instruction needs at least 1 packaging material. |  |  |
| 6 | Maintain material and target quantity | In item 20, make the following entries:Item category: M Material.Component: Material number to be packed, for example, SG624 or SG424.Target quantity: Quantity, for example 1. |  |  |
| 7 | Enter Check Profile | In the Admin.data tab, enter 01 in the Check Profile field.01 is the pre-delivered SAP Standard Profile. |  |  |
| 8 | Save | Choose Save.Make a note of the packing instruction number: _____. | A packing instruction is created. |  |

##### Create Packing Instruction Determination

Purpose

In this step, you create packing instruction determination records.

This function enables the system to find a packing instruction by specific characteristics. The condition technique is applied for this. You define a packing instruction that refers to specific characteristics, such as material and plant.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Handling Unit Data | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Determination Records - Master Data (POF1). | The Pkg Instruction - Create Determination Recs: Initial Screen is displayed. |  |
| 3 | Enter Determination Type | On the Pkg Instruction - Create Determination Recs: Initial Screen, make the following entries, and choose Enter.Determination Type: 0GRP – MIGO Production ReceiptChoose Enter.Note Note that for the determination of the packing instruction with determination types 0GRP, the following key combinations are available:Material/VendorMaterial/PlantMaterial |  |  |
| 4 | Choose a key combination | On the key combination screen, choose a key combination, and select Choose.For example, choose Material/Plant. |  |  |
| 5 | Enter the Packing Instruction Determination | On the Create MIGO Production Rcpt (0GRP): Fast Entry screen, make the following entries:Plant: for example 1710.Material: SG624 or SG424.Packing instruction: <The Packing instruction number noted in the last section> |  |  |
| 6 | Save | Choose Save. | The packing instruction determination is created. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Material Staging for Production](#unique_20) [page ] 20 |  |  |  |
| [Release Production Order](#unique_21) [page ] 20 | Production Supervisor - Discrete Manufacturing | Manage Production Orders (F2336) | You have released the production order. |
| [Staging Release Order Parts for Production](#unique_22) [page ] 21 | Production Operator - Discrete Manufacturing | Stage Materials for Production (MF60) |  |
| [Staging Pick Parts for Production](#unique_23) [page ] 23 | Production Supervisor - Discrete Manufacturing | Change Production Order (CO02) | You have created the inbound deliv-ery for the production order. |
| [Create Staging Warehouse Tasks](#unique_24) [page ] 24 | Warehouse Clerk (EWM) | Process Posting Change Item (/SCWM/MONNAV_PROC_PC) | You have created the staging ware-house tasks. |
| [Material Staging with Ad-Hoc Movements (Optional)](#unique_25) [page ] 26 | Warehouse Clerk (EWM) | Create Product Warehouse Tasks (/SCWM/MONNAV_CR_P_WT) |  |
| [Confirm Staging Warehouse Tasks](#unique_26) [page ] 27 | Warehouse Clerk (EWM) | Process Warehouse Tasks (F4595) | You have confirmed the staging warehouse tasks. |
| [Confirm Production Operations for Subassembly](#unique_27) [page ] 31 |  |  |  |
| [Post Consumption of Components](#unique_28) [page ] 32 | Warehouse Clerk | Post Goods Movement (MIGO) |  |
| [Goods Receipt from Production with Synchronous Goods Movements](#unique_29) [page ] 34 |  |  |  |
| [Post Goods Receipt for Production Orders (Optional)](#unique_30) [page ] 34 | Warehouse Clerk | Post Goods Movement (MIGO) |  |
| [Display Material Document (Optional)](#unique_31) [page ] 36 | Warehouse Clerk | Post Goods Movement (MIGO). |  |
| [Pack Finished Material (Optional)](#unique_32) [page ] 37 |  |  |  |
| [Create HU Putaway Warehouse Task (Optional)](#unique_33) [page ] 39 | Warehouse Clerk (EWM) | Create HU Warehouse Tasks (/SCWM/MONNAV_CR_HUWT) |  |
| [Create Product Putaway Warehouse Tasks (Optional)](#unique_34) [page ] 40 | Warehouse Clerk (EWM) | Create Product Warehouse Tasks (/SCWM/MONNAV_CR_P_WT) |  |
| [Confirm Putaway Warehouse Tasks](#unique_35) [page ] 41 | Warehouse Operative (EWM) | Confirm Warehouse Tasks (/SCWM/MONNAV_WT_CONF) |  |

## Test Procedures

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
| 3 | Check Default Area of Responsibility (Supervisor) | On the Manage Production Orders screen, maintain the following entries:Check the default area of responsibility (supervisor) by choosing your avatar (from the top-left corner) and selecting App Settings > Area of Responsibility Production Supervisor . Check that only this entry is displayed:Plant 1 AE 3310.MTS DI - Valuated (YB1). | If there's no Plant 1 AE 3310 entry in the Area of Responsibility (Supervisor) dialog box, choose Add to select it and then OK. For other plant entries in the Area of Responsibility (Supervisor) dialog box, choose Delete to remove the others and then choose OK. |  |
| 4 | Select Production Order | On the Manage Production Orders (F2336) screen, enter the following search conditions as a filter.Choose Adapt Filters to display more selection filters. Choose More filters under Production Orders. Select the checkbox for Material and Production Plant and choose OK. Then, choose Go. The Material and Production Plant fields are then added to the filter bar.Status: Created.Material: SG424 or SG624.Production Plant: 3310.Choose Go to execute. | The Manage Production Orders (F2336) screen is displayed. |  |
| 5 | Select Order | On the Manage Production Orders (F2336) screen, select your production order by choosing the checkbox beside the order number.Choose Edit. | The Manage Production Orders (F2336) screen is displayed. |  |
| 6 | Execute Release | Choose Menu > Functions > Release . |  |  |
| 7 | Release Order | Choose Release Order. | A system message tells you that the release has been carried out, and refers to the log. |  |
| 8 | Save | Save your entries. | A system message tells you that the corresponding order number has been saved. |  |

#### Staging Release Order Parts for Production

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This section describes the warehouse task creation and processing for the supply of material RM124 to production, which is a component of both materials SG424 and SG642. Component RM124 is staged using the Release Order Parts method and production Supply Area PSA_02. If there is sufficient stock available in the PROD_SUPPLY_2 bin, no line items are generated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Operator - Discrete Manufacturing . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Stage Materials for Production (MF60). | The Material Staging for Planned Orders screen is displayed. |  |
| 3 | Enter Details | On the Material Staging for Planned Orders screen, make the following entries:Staging TypesSelect the EWM Rel. Parts checkbox.Deselect the SLocLevel checkbox.Plant: 3310.Selection Horizon for Remts: <date must be in the future - after scheduled start date of the production order>.ComponentsMaterial: RM124.Production Supply Area: PSA_02. | The Pull List: EWM Release Order Parts screen is displayed. |  |
| 4 | Choose Global Settings | Choose Global Settings. | The Global Settings dialog box appears. |  |
| 5 | Navigate to Dialog Control Tab | In the Global Settings dialog box, choose Dialog Control. |  |  |
| 6 | Make Entries | On the Dialog Control tab. In the logging section, select the Display message log automatically checkbox. |  |  |
| 7 | Choose Continue | Choose Continue. |  |  |
| 8 | Choose Execute | On the Material Staging for Planned Orders screen, choose Execute. | The Pull List: EWM Release Order Parts screen is displayed. |  |
| 9 | Choose Replenishment Elements | On the Pull List: EWM Release Order Parts screen, select the required line items from the left-hand margin and choose Replenishment Proposal at the top of the screen. | The Quantity staged field is populated. |  |
| 10 | Choose Replenishment Elements | Review the staged quantity and choose Replenishment Elements. | The Replen. Elements table is displayed. |  |
| 11 | Check or Enter Replenishment Storage Location | At the bottom half of the split screen, select the Replenishment Element line and check or make the following entries:Replenishment Storage Location: 335W. |  |  |
| 12 | Choose Stage | Select the Replenishment Element line and choose Stage at the center of the screen. | The Staging cell is populated with Element Checked: OK. |  |
| 13 | Choose Save | Choose Save.Note down the delivery number.Note The delivery is not yet saved in the data base. Make sure to complete the next step before you search your delivery in the system. | The log with the following system message appears: EWM release order delivery <delivery number> successfully generated for RM124 |  |
| 14 | Choose Exit | Choose Exit in the upper right corner of the screen. | The following system message appears: Data posted successfully |  |

#### Staging Pick Parts for Production

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This section describes the warehouse task creation and processing for the supply of material RM224 and RM624 to production, RM224 is a component of both materials SG424 and SG624. RM624 is a component of SG624. Component RM224 and RM624 are staged using the Pick Parts method and production Supply Area PSA_02. If there is sufficient stock available in the PROD_SUPPLY_2 bin, no line items are generated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Supervisor - Discrete Manufacturing . |  |  |
| 2 | Access App | Open Change Production Order (CO02). | The Production Order Change: Initial Screen screen is displayed. |  |
| 3 | Enter Order Number | Enter the order for SG424 or SG624 and choose Continue. | The Production order Change: Header screen is displayed. |  |
| 4 | Execute Material Staging | On the Production order Change: Header screen, choose More > Functions > WM Material Staging > Execute . |  |  |
| 5 | Save your Changes | Choose Save. | The following system message appears: Order number <your order number> saved |  |

#### Create Staging Warehouse Tasks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create posting change warehouse tasks for the staging process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk (EWM). |  |  |
| 2 | Access App | Open Process Posting Change Item (/SCWM/MONNAV_PROC_PC). | The /SCWM/SAPLWIP_POSTING_CHANGES dialog box appears. |  |
| 3 | Enter Warehouse Number | If a system message asks you to enter a warehouse number, enter 335 and choose Continue. |  |  |
| 4 | Enter Selection Criteria | In the /SCWM/SAPLWIP_POSTING_CHANGES dialog box, make the following entries:Product: RM124End Date Whse Act:<Date>. |  |  |
| 5 | Choose Execute | Choose Execute. | The Process Posting Change Item screen appears. |  |
| 6 | Choose your delivery | On the Process Posting Change Item screen, choose your delivery. |  |  |
| 7 | Create Warehouse Tasks | Choose More methods > Create WT in Background to create the warehouse tasks. | The Display logs dialog box with the following system messages appears: Warehouse task <your warehouse task number> createdWarehouse order <your warehouse order number> created |  |
| 8 | Note Down Warehouse Task Number | Note down the warehouse task number. |  |  |
| 9 | Repeat the Steps | Repeat the above steps making the following entries to stage the second component:Product: RM224 and RM624.End Date Whse Act: <Current Date>. |  |  |

#### Material Staging with Ad-Hoc Movements (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you supply production with the required components using ad-hoc movements. This allows you to stage components to the production supply area (PSA) quickly, in the case of unplanned excess consumption.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log onto SAP Fiori Launchpad | Open the SAP Fiori Launchpad as a Warehouse Clerk (EWM). | The SAP Fiori launchpad is displayed. |  |
| 2. | Access the App | Open Create Product Warehouse Tasks (/SCWM/MONNAV_CR_P_WT). | The /SCWM/SAPLSTOCK_OVERVIEW_MON dialog box appears. |  |
| 3. | Enter filter criteria | In the /SCWM/SAPLSTOCK_OVERVIEW_MON dialog box, make the following entries:For component RM124:Storage Type: SF01.Product: RM124.For component RM224:Storage Type: SG01.Product: RM224.For component RM624:Storage Type: S001.Product: RM624. |  |  |
| 4 | Choose Execute | Choose Execute. | The Create Product Warehouse Task screen displays. |  |
| 5 | Select your Stock Line | On the Create Product Warehouse Task screen, select the stock line item. |  |  |
| 6 | Choose Create Warehouse Task | Choose More Methods > Create Warehouse Task. | The Create Warehouse Task dialog box appears. |  |
| 7 | Create Warehouse Task | In the Create Warehouse Task dialog box, make the following entries:Src Trgt Qty AUoM (Quantity): For example 1.Destination Bin: PROD-SUPPLY-2.Destination Storage Type is automatically filled.Warehouse Process Type: S401. |  |  |
| 8 | Choose Create WT | Choose Create WT.Note down the warehouse task number. | The Display logs dialog box with the following system messages appears:Warehouse task <your warehouse task number> createdWarehouse order <your warehouse order number> created |  |
| 9 | Complete the step | Choose Continue to close the log. |  |  |

#### Confirm Staging Warehouse Tasks

In this section, you confirm the staging warehouse tasks you created in the previous steps. You can confirm the warehouse tasks using a Fiori App or using Radio Frequency Devices.

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
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Operative (EWM) | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Process Warehouse Tasks (F4595). |  |  |
| 3 | Enter your Warehouse Task | Enter the warehouse task you noted down in the previous step.Choose Go. |  |  |
| 4 | Check Warehouse Task details (optional) | If you would like to create a pick HU, assign serial sumbers or batches, follow step 5-13.Otherwise go directly to step 14.Choose the Warehouse Task to go into the warehouse task details | The Warehouse Task screen is displayed. |  |
| 5 | Maintain Pick-HU (optional) | On the Warehouse Task screen, in the Movement Data tab, choose Maintain Pick-HU. | The Maintain Pick-HU dialog box is displayed. |  |
| 6 | Maintain Pick-HU (optional) | In the Maintain Pick-HU dialog box, select Create Pick-HU. | The Create Pick-HU dialog box is displayed. |  |
| 7 | Maintain Pick-HU (optional) | In the Create Pick-HU dialog box, enter a Packagin Material, for example PMPALLET, and choose Create. | The Maintain Pick-HU dialog box with the newly created Pick-HU is displayed. Note down the HU number. |  |
| 8 | Maintain Pick-HU (optional) | In the Maintain Pick-HU dialog box, select Close. | The Warehouse Task Screen is displayed and the Destination Handling Unit dropdown menu is populated with the HU number. |  |
| 9 | Maintain Batch (optional) | In the Warehouse Task screen, in the Movement Data tab, select a batch if required and not selected automatically by choosing the value help. | The Select: Batch dialg box is displayed. |  |
| 10 | Maintain Batch (optional) | In the Select: Batch dialog box, in the Items section, select a batch. | The Select: Batch dialog box closes. You have selected a batch. |  |
| 11 | Maintain Serial Number (optional) | On the Warehouse Task screen, in the Movement Data section, choose No. of Serial Numbers Entered: X / X. | The Serial Number Assignment dialog box is displayed. |  |
| 12 | Maintain Serial Number (optional) | In the Serial Number Assignment dialog box, enter serial numbers in the Enter Serial Number input field until a serial number for every item is selected. | You have assigned serial numbers. |  |
| 13 | Return to Process Ware-house Tasks screen (optional) | In the Warehouse Task screen, choose Cancel to return to the Process Warehouse Tasks screen. | The Warehouse Task screen is displayed. |  |
| 14 | Confirm Warehouse Task | Mark the checkbox for the selected warehouse task and choose Confirm. | You have confirmed the warehouse task. |  |

##### Variant 2: With Radio Frequency Devices

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
| 1. | Log on to the SAP Fiori launchpad | Log on to the SAP Fiori launchpad as a Warehouse Operative (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2. | Access the SAP Fiori app | Open the SAP Fiori app Test RF Environment (/SCWM/RFUI)The app allows you to test working in an RF environment. For working with mobile RF devices, see also SAP Note [3048632](https://me.sap.com/notes/3048632). |  |  |
| 3 | Enter Data for RFUI | Whse No: 3350Resource: SHR1-1Dflt Dvc.: SE01Choose Enter. |  |  |
| 4 | Choose Menu | Choose 01 System-Guided > 02 SystemGuided Queue. |  |  |
| 5 | Enter Queue Name | For Component RM124:In the Queue field, enter SR-F01-105.For Component RM224:In the Queue field, enter for example SR-G01-105.For Component RM624:In the Queue field, enter for example SR-001-105.Choose Enter. |  |  |
| 6 | Create Picking HU | Make the following entries:Pack.Mat: PMPALLETChoose HUCrt.The picking HU is created. |  |  |
| 7 | Choose Next | Scroll the screen to the right using the icon > and choose Next. |  |  |
| 8 | Enter or Verify the Source Information Fields | Enter or verify the following fields, if they are required:Src.Bin (Source Bin)SrceHU (Source HU)Prod. (Product)ActQty (Quantity)Choose Enter. |  |  |
| 9 | Enter Serial Number (optional) | Enter a serial number and choose enter in the following field:SNEnter serial numbers for the complete quantity.Field SNsCrt: XX / XX indicates the total number of required entries and the number of entries already made.Choose Save. |  |  |
| 10 | Verify the Destination Information Fields | Verify the following fields:DstBin (Destination Bin)Choose Enter. |  |  |
| 11 | Repeat Steps | Repeat steps 6 to 8 until no suitable warehouse orders are found. |  |  |
| 12 | Logoff RFUI | You can choose Back to go to the previous screens.Choose Logoff.Choose Save. |  |  |

### Confirm Production Operations for Subassembly

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The confirmation documents include the processing status of orders, operations, sub-operations, and individual capacities. It's an instrument for controlling orders. This process step shows you how to confirm subassembly production order operations for semifinished material SG424 and SG624. A goods movement document is generated when the last operation is confirmed. The backflush is carried out together with the confirmation steps.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Confirm Production Order Operation (CO11N). |  |  |
| 3 | Enter Production Order and Operation | On the Enter Order and Operation screen, make the following entries and choose Go:Order: <Production Order Number for semifinished goods>Operation: <operation number> for example, <0010> |  |  |
| 4 | Enter Quantities Data | In the Quantities section, make the following entries:Yield: <Quantity of prod. order less scrap>Scrap: <scrap amount> |  |  |
| 5 | Check Material Movements | In the Material Movements section, check the material list.Note The system shows you an overview materials table for which the material withdraws are done along with operation confirmation.The material RM124 , is set for backflush (in material master) for withdraws to be done automatically after the operation is confirmed. |  |  |
| 6 | Enter Activities Data and Save | In the Activities section, make the following entries:Setup: <setup time>Machine: <machine time>Labor: <labor time>For partial confirmation, choose Post.For final confirmation, choose Post and Complete. | Confirmation is made. |  |
| 7 | Repeat Steps | Go back and repeat steps 3 to 6 for Operation 0020. |  |  |
| 8 | Goods Issue and Goods Receipt | When all operations are fully confirmed, the materials consumed during production are backflushed.For material SG424, goods receipt is automatically posted upon the confirmation of the last operation.Note If a packing instruction is created for SG424, the system will automatically create handling units based on the packing instructions at the time of goods receipt. It is controlled by the field “Automatic Packing in Sync. Goods Receipt to Bin” in the Production Schedul-ing Profile assigned to the product. |  |  |

### Post Consumption of Components

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You post the withdrawal of the raw materials that are used for the order. This withdrawal can be done by doing a manual goods issue.

|  |
| --- |
| Note If the material is set for backflush (in material master or resource), the withdrawing is done automatically after you confirm the operation or the whole order.This step is only required for production order of SG624 and its component RM624. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Open the SAP Fiori launchpad as the Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2. | Access the App | Open Post Goods Movement (MIGO). | The Initial screen displays. |  |
| 3. | Enter Selection Data | Make the following entries and choose Enter:Action: Goods IssueReference: OrderOrder number: <Order ID> (from previous steps)Movement Type: 261 | The screen name adapts after entries are made. |  |
| 4. | Check and Enter Warehouse Data | For each item, on the Warehouse Management tab, make the following entries:Storage Bin :<Storage Bin which contains material stock>.HU: <HU for the Material if applicable>Choose Enter. | Ensure that detail data is expanded. |  |
| 5. | Check Each Item | For each item, select Item OK. | Ensure that detail data is expanded. |  |
| 6. | Post Goods Movements | Choose Post. | The goods movements have been posted. |  |

### Goods Receipt from Production with Synchronous Goods Movements

Purpose

This section describes the putaway process from production for materials SG424 and SG624. For material SG424, the system will post goods receipt automatically once you confirm the last Production Operation step. For material SG624, you post Goods Receipt manually.

#### Post Goods Receipt for Production Orders (Optional)

Purpose

In this step, you post the goods receipt against the production order for material SG624

or

FG328 manually. You can enter batch and/or create handling units before the goods receipt is posted.

|  |
| --- |
| Note For material SG424, the Goods Receipt will be automatically posted to the PR-AREA bin once you confirm the last production order operation step. Therefore, skip this step when testing using material SG424. |

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
| 1 | Log on | Open the SAP Fiori Launchpad as the Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO) . | The Goods Receipt Order screen is displayed. |  |
| 3 | Select Goods Receipt Order screen | On the Goods Receipt Order screen, make the following entries and choose Enter.Goods Receipt: <Select>.Order: <Select>.Order number: <Production Order number from the previous step>.GR goods receipt: 101. | The items of the selected production order are displayed. |  |
| 4 | Enter Quantity | If required, check the quantity on the Quantity tab. |  |  |
| 5 | Check storage location | Select Where tab and check Storage Location 335W.Note An additional storage location 335I and the corresponding availability group 002 can be introduced in the Cloud WM as an optional setup. Compared to the single storage location 335W / availability group 001 setup, the new setup can help distinguish stock that is still in the process of putaway and that is already in the warehouse.For example, the storage location 335I is used as the goods receipt storage location. During the goods receipt process, the stock remains in the storage location 335I and isn't available for sale (Stock Type F0 – Unrestricted Use in Putaway) until the putaway warehouse task(s) is/are confirmed. Once the putaway is finished, the stock is automatically posted to the storage location 335W and becomes available for sale (Stock Type F – Unrestricted Use in Warehouse).To enable the 335I storage location / availability setup, there are manual setup steps to be performed according to the instructions provided in the Warehouse Management Setup Guide. For more information, see chapter Additional Manual Configuration. |  |  |
| 6 | Create Handling Units (Optional) | On the Warehouse Management tab, if a packing instruction is available for the product, you shall see the value in the Unpacked Qnty AUoM field is 0 and the packaging proposal with the following values:No. of HUsPack. MaterialHU TypeQty.AUoM (Quantity per HU in Alternative UoM)UnitQuantityBUoM (Base UoM)If no packaging proposals are available, create handling units using either of the following options:Choose by Total Quantity and enter Packaging Material and No. of HUs.Choose by Quantity per HU and enter Quantity per HU and Packaging Material.Choose Adopt.Note Even if a packing instruction is available, you can delete the packaging proposal and create the handling units based on your own needs. However, once you choose Redetermine Packaging Proposal, the system will read the packing instruction and once again give the packing proposal. |  |  |
| 8 | Check Storage Bin | On the Warehouse Management tab, check the default storage type S915 and storage bin PR-AREA.The default storage bin can be changed. |  |  |
| 8 | Select Item ok Indicator | Select Item OK checkbox.Choose Check. Confirm the message Document is O.K. by choosing Enter. |  |  |
| 9 | Post | Choose Post. | The system displays the message: Material document 5xxxxxxxxx posted.Make a note of the Material Document number. |  |

#### Display Material Document (Optional)

Purpose

In this step, you display the material document for the goods receipt in the previous step.

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
| 1 | Log on | Open the SAP Fiori Launchpad as the Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO) . | The Goods Receipt Order screen is displayed. |  |
| 3 | Select Display Material Document screen | On the Goods Receipt Purchase Order screen, make the following entries and choose Enter.Display: <Select>.Material Document: <Select>.Material Document number: <Material Document number from the previous step>.Material Document Year:for example, 2024. | The items of the selected purchase order display. |  |
| 4 | Display Stock Overview | On the Warehouse Management tab, choose Display Stock Overview. |  |  |
| 5 | Check Physical Stock | On the Physical Stock screen, check the Product, HUs (if applicable) and the Storage Type/Storage Bin in which the stock is located after the Goods Receipt. |  |  |
| 6 | Display Warehouse Document | On the Warehouse Management tab, choose either of the two following options:If automatic Putaway WT creation is applicable to the product, choose Display Warehouse Document & Open Putaway WTs.If automatic Putaway WT creation is not applicable to the product, choose Display Warehouse Document.You will not see the Display Warehouse Document & Open Putaway WTs if automatic Putaway WT creation is not applicable to the product. |  |  |
| 7 | Check Warehouse Tasks | On the Warehouse Task screen, check the goods receipt posting warehouse task(s)s that has been created and confirmed by the system.If automatic Putaway WT creation is applicable to the product, you will also see the open Putaway WT(s). | The Warehouse Task(s) created is displayed.Make a note of the Putaway warehouse task number. |  |

#### Pack Finished Material (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Operative (EWM) packs the loose product into a handling unit (HU).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Operative (EWM). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Pack Warehouse Stock (F3738). |  |  |
| 3 | Enter Data | Make the following entries:Work Center: PACKStorage Bin: CL-AREAChoose Enter.Choose Start Packing. |  |  |
| 4 | Enter Data | Make the following entries:Handling Unit/Storage Bin: <Enter the Storage Bin where product stock exists>Product/Access Code:Choose Enter. | The products in the HU or the storage bin are displayed. |  |
| 5 | Enter Data to Create HU | Select one of the favorite packaging materials or select other packaging material in the Other Packaging Materials field.Enter the target handling unit number or leave it blank to let the system propose automatically.Choose Create. | The destination HU is created and displayed on the right-hand side of the screen. |  |
| 6 | Choose Items | Choose the product and choose Pack.Note If you want to pack all the items, you can choose Pack All. If you want to pack a partial quantity of the product, you can choose Partially Pack. |  |  |
| 7 | Close HU | The selected products are displayed on the right-hand side.If you want to print the HU, choose Print.Choose Close. |  |  |

#### Create HU Putaway Warehouse Task (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is for creating HU warehouse tasks to move packed material from the PR-AREA to the destination storage bin in the warehouse.

|  |
| --- |
| Note Skip this step if you set the system to automatically create warehouse tasks after goods receipt from production. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log onto SAP Fiori Launchpad | Open the SAP Fiori Launchpad as a Warehouse Clerk (EWM). | The SAP Fiori launchpad is displayed. |  |
| 2. | Access the App | Open Create HU Warehouse Tasks (/SCWM/MONNAV_CR_HUWT) |  |  |
| 3. | Enter filter criteria | Make the following entries.Storage Type: S915.Handling Unit: <Handling Unit created in the previous step>.Choose Execute. |  |  |
| 4. | Select your Stock | Select one of the stock lines and choose More Methods > Create Warehouse Task. | A dialog box that requests data (Create Warehouse Task) is displayed. |  |
| 5. | Create Warehouse Task | In the Create warehouse task dialog box enter the following data:Destination Bin: <Leave blank>Warehouse Process Type: S126.Choose Create WT. | The display log with the created warehouse task is displayed. A warehouse task list is automatically printed in the background.Note down the warehouse task number. |  |
| 6. | Complete the step | Note down the warehouse task number.Choose Continue to close the log. |  |  |

#### Create Product Putaway Warehouse Tasks (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is for creating warehouse tasks to move material from the PR-AREA to the destination storage bin in the warehouse.

|  |
| --- |
| Note Skip this step, if you set the system to automatically create warehouse tasks after goods receipt from production or in case you already created an HU warehouse task for putaway. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log onto SAP Fiori Launchpad | Open the SAP Fiori Launchpad as a Warehouse Clerk (EWM) . | The SAP Fiori launchpad is displayed. |  |
| 2. | Access the App | Open Create Product Warehouse Tasks (/SCWM/MONNAV_CR_P_WT). | The Create Product Warehouse Tasks (/SCWM/MONNAV_CR_P_WT) screen displays. |  |
| 3. | Enter filter criteria | Make the following entires:Storage Type: S915.Product: FG328, SG624 or SG424.Product: FG012Choose Execute. | The Create Product Warehouse Task screen displays. |  |
| 4. | Select your Stock | Select one of the stock lines and choose More Methods > Create Warehouse Task. | A dialog box that requests for data (Create Warehouse Task) is displayed. |  |
| 5. | Create Warehouse Task | In the Create Warehouse Task dialog box enter the following data:Trgt Qty AUoM (Quantity): For example, 1Destination Bin: <Leave Blank>Warehouse Process Type: S116.Choose Create WT. | The display log with the created warehouse is displayed. A warehouse task list is automatically printed in the background.Note down the warehouse task number. |  |
| 6. | Complete the step | Note down the warehouse task number.Choose Continue to close the log. |  |  |

#### Confirm Putaway Warehouse Tasks

In this section, you confirm the putaway warehouse tasks you created in the previous steps. You can confirm the warehouse tasks using a Fiori App or using Radio Frequency Devices.

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
| 2 | Access App | Open the SAP Fiori App Confirm Warehouse Tasks (/SCWM/MONNAV_WT_CONF). | The Warehouse Task dialog box is displayed. |  |
| 3 | Enter Warehouse Task Number | In the Warehouse Tasks dialog box, make the following entries:Warehouse Task: <WT number noted down in the previous step>.Choose Go. |  |  |
| 4 | Confirm Warehouse Task | Mark the check box for the selected warehouse task and choose More Methods > Confirm WT in Background.Note If you have the two availability groups setup for your warehouse, as soon as the putaway warehouse tasks are confirmed, the system automatically posts the stock type for this stock from ‘Unrestricted Use in Putaway (F0)’ to ’Unrestricted Use in Warehouse (F)’. | The display log with the following system messages appears:.Warehouse task is to be confirmedWarehouse task was confirmed. |  |

##### Variant 2: With Radio Frequency Devices

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
| 1 | Log on to the SAP Fiori launchpad | Log on to the SAP Fiori launchpad as a Warehouse Operative (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open the SAP Fiori app Test RF Environment (/SCWM/RFUI)The app allows you to test working in an RF environment. For working with mobile RF devices, see also SAP Note [3048632](https://me.sap.com/notes/3048632). |  |  |
| 3 | Enter Data for RFUI | Whse No: 3350Resource: SHA1-1DefPresDvc: SE01Choose Enter.Note Use resource SHA1-1 for putting away to S001. |  |  |
| 4 | Choose Menu | Choose 01 System-Guided > 02 SystemGuided Queue. |  |  |
| 5 | Enter Queue Name | In the Queue field, enter SI-001. |  |  |
| 6 | Verify Source Bin and Enter HU | Note This step is only relevant if you created handling units in step Post Goods Receipt for Production Orders (Optional ) or Pack Finished Material (Optional).Verify the Src.Bin (Source Bin)HU: < Enter the HU ID from previous step > |  |  |
| 7 | Verify the Source information fields | Verify the following fields, if they are required:Src.Bin (Source Bin)Prod. (Product)Srce Qty (Source Quantity)ChooseEnter . |  |  |
| 8 | Verify the Destination Information fields | Verify the following fields, if they are required:Prod. (Product)ActQty (Quantity)Dest.Qty (Destination Quantity)DstBin (Destination Bin)Choose Enter. |  |  |
| 9 | Repeat Steps | Repeat steps 6 to 8 until no suitable warehouse orders are found. |  |  |
| 10 | Logoff RFUI | You can choose Back to the previous screens.Choose Logoff.Choose Save.Note If you have the two availability groups setup for your warehouse, as soon as the putaway warehouse tasks are confirmed, the system automatically posts the stock type for this stock from ‘Unrestricted Use in Putaway (F0)’ to ’Unrestricted Use in Warehouse (F)’. |  |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| BJ5 - Make-to-Stock Production – Discrete Manufacturing | To complete the whole process for the GI for production section in this scope item, follow up with the Confirm Production Operations for Subassembly step in test script Make-to-Stock Production – Discrete Manufacturing (BJ5).To continue the process after the whole GR from Production section, follow up with the Production Order Processing for Final Assembly step in test script Make-to-Stock Production – Discrete Manufacturing (BJ5). |
| 3BS - Warehouse Outbound Processing | To ship goods to the customer, proceed with test script Warehouse Outbound Processing (3BS). |

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
> Flagged while digesting this document, not verified: Create Control Cycle expected result reads 'Control cycle RM124 1010 PSA_02 is created' although the entries specify Plant 3310; the message shows plant 1010.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Initial Stock Posting section refers to BoM materials of FG228 and FG227 (with SG224, SG21, RM20) and storage location 331B, and a putaway step filters Product FG012, none of which are in the sample data table (FG426, SG424, FG626, SG624, FG328).

## Connections
- part-of :: [[_cluster]]
- related-to :: [[11-inventory-warehouse-and-transportation/atualizar-area-de-abastecimento-da-producao-mds-3ks-344]]
- related-to :: [[11-inventory-warehouse-and-transportation/maintain-production-supply-area-mds-3ks-341]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-3ks-343]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-3ks-345]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5HO_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 72,390 chars in the whole document
