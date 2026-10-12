---
id: 12-production-and-manufacturing/test-script-planning-and-production-in-other-plant-consumer-products-7
title: "Test Script: Planning and Production in Other Plant – Consumer Products (7DN_AE), SAP S/4HANA Cloud Public Edition (7DN_S4CLD2608_BPD_EN_AE)"
description: "SAP test script, scope item 7DN_AE: cross-plant MRP, process/production orders, sales order, delivery and billing for Consumer Products (plants 3310, 3320)."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/mrp-and-predictive-mrp]
aliases: [7DN_S4CLD2608_BPD_EN_AE]
keywords: [Material Requirements Planning and Predictive MRP, cross-plant production planning, planned independent requirements, material requirements planning, process orders, production orders, production confirmation, goods receipt, pick list goods issue, sales order processing]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7DN_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1211
topic: 12-production-and-manufacturing/mrp-and-predictive-mrp
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Planning and Production in Other Plant – Consumer Products (7DN_AE), SAP S/4HANA Cloud Public Edition (7DN_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7DN_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Material Requirements Planning and Predictive MRP** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Planning and Production in Other Plant – Consumer Products (7DN_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232860571)

[2 Prerequisites 4](#_Toc232860572)

[2.1 System Access 4](#_Toc232860573)

[2.2 Roles 4](#_Toc232860574)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232860575)

[2.4 Additional Manual Configuration 9](#_Toc232860576)

[2.5 Business Conditions 9](#_Toc232860577)

[2.6 Preliminary Steps 10](#_Toc232860578)

[2.6.1 Enhance Material Master 10](#_Toc232860579)

[2.6.2 Initial Material Stock for plant **3320** 11](#_Toc232860580)

[2.6.3 Initial Material Stock for plant **3310** 12](#_Toc232860581)

[3 Overview Table 14](#_Toc232860582)

[4 Test Procedures 17](#_Toc232860583)

[4.1 Anonymous Forecast and MRP 17](#_Toc232860584)

[4.1.1 Create Planned Independent Requirements 17](#_Toc232860585)

[4.1.2 Material Requirements Planning at Plant Level 19](#_Toc232860586)

[4.1.3 Evaluate Stock/Requirements Situation 21](#_Toc232860587)

[4.2 Production of Semifinished Material 23](#_Toc232860588)

[4.2.1 Create Process Order 24](#_Toc232860589)

[4.2.1.1 Option 1: Convert Planned Orders to Process Orders 24](#_Toc232860590)

[4.2.1.2 Option 2: Create Process Order Manually 25](#_Toc232860591)

[4.2.2 Review Process Order (Optional) 26](#_Toc232860592)

[4.2.3 Execute Goods Issue via Pick List 28](#_Toc232860593)

[4.2.4 Monitor Order Progress (Optional) 29](#_Toc232860594)

[4.2.5 Confirm Production 31](#_Toc232860595)

[4.2.6 Post Goods Receipt for Process Order 32](#_Toc232860596)

[4.2.7 Review Process Order Confirmation 34](#_Toc232860597)

[4.3 Sales Order Processing 36](#_Toc232860598)

[4.3.1 Create Sales Order 36](#_Toc232860599)

[4.4 Packaging Process 38](#_Toc232860600)

[4.4.1 Material Requirements Planning at plant level 38](#_Toc232860601)

[4.4.2 Evaluate Stock/Requirements Situation 39](#_Toc232860602)

[4.4.3 Convert Planned Order to Production Order 41](#_Toc232860603)

[4.4.4 Review Production Order (Optional) 42](#_Toc232860604)

[4.4.5 Manual Goods Issue 43](#_Toc232860605)

[4.4.6 Monitor Order Progress (Optional) 44](#_Toc232860606)

[4.4.7 Confirm Production Order incl. Component Backflush 45](#_Toc232860607)

[4.4.8 Post Goods Receipt for Production Order 47](#_Toc232860608)

[4.5 Delivery Processing 48](#_Toc232860609)

[4.5.1 Create Delivery with Order Reference 48](#_Toc232860610)

[4.5.2 Execute Picking 49](#_Toc232860611)

[4.5.3 Post Goods Issue 51](#_Toc232860612)

[4.6 Billing Process 52](#_Toc232860613)

[4.6.1 Create Billing Document 52](#_Toc232860614)

[5 Appendix 55](#_Toc232860615)

[5.1 Succeeding Processes 55](#_Toc232860616)

## Purpose

Overview

This scope item describes a cross-plant production planning and execution process tailored for the Consumer Products Industry. The process involves two plants: Plant 1 serves as the planning and packaging plant using production orders, while Plant 2 produces semifinished materials using process manufacturing.

The process begins with creating a demand forecast for the finished goods, represented by Planned Independent Requirements (PIRs) in Plant 1. Based on these PIRs, Material Requirements Planning (MRP) generates a production plan for finished goods and explodes the entire bill of material structure across both plants. As a result, the demand for semifinished component production, packaging, and raw materials is planned in both plants, depending on the BOM structure.

The production process starts by converting a planned order to a process order or directly creating a process order in Plant 2. Subsequently, goods issue of components, confirmation of production, and goods receipt of the semifinished goods are executed. Plant 1 hosts all major packaging materials, including those relevant for Plant 2. The withdrawal via pick list is executed cross-plant: Cartons are posted directly in Plant 1, even though Plant 2 consumes the material, while Plant 2 picks and posts other components. Moreover, the goods receipt of the semifinished material is posted directly in Plant 1, even though production takes place in Plant 2, eliminating the need for a separate stock transfer process.

Plant 1 stores the semifinished material until a customer places an order for the finished material, triggering the packaging process. The MRP run creates convertible planned orders according to customer requirements. The packaging process begins with converting these planned orders to production orders. After production and goods receipt of the finished material in the unrestricted stock, the system can deliver the sales order and initiate the billing process.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

System Access

Table 1:

| System | Details |
| --- | --- |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

Table 2:

| Name (Role Template) | ID (Role Template) | Description (Space Template) | ID (Space Template) | Log On |
| --- | --- | --- | --- | --- |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Production Planner | SAP_BR_PRODN_PLNR | Production Planning | SAP_BR_PRODN_PLNR |  |
| Production Supervisor - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC | Production Management - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC |  |
| Production Supervisor - Process Manufacturing | SAP_BR_PRODN_SUPERVISOR_PROC | Production Management - Process Manufacturing | SAP_BR_PRODN_SUPERVISOR_PROC |  |
| Production Operator - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC | Production Management - Process Manufacturing | SAP_BR_PRODN_OPTR_DISC |  |
| Production Operator - Process Manufacturing | SAP_BR_PRODN_OPTR_PROC | Production Execution - Process Manufacturing | SAP_BR_PRODN_OPTR_PROC |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Products / Product Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure.

| Data | Sample Value | Description | Other Attributes |
| --- | --- | --- | --- |
| Material | FG0505 | Pallet Cookies | Planning material (plant 3310), MTS processing for discrete industry, batch managed |
| Material | SG0505 | Carton Cookies | Production in other plant (plant 3320), MTS process manufacturing for semifinished product, batch managed |
| Material | RM0510 | Butter | Raw material, batch managed, external procurement |
| Material | RM0511 | Sugar | Raw material, batch managed, external procurement |
| Material | RM0512 | Syrup | Raw material, batch managed, external procurement |
| Material | RM0513 | Wheat Flour | Raw material, batch managed, external procurement |
| Material | PK0512 | Pallet | Packaging material, no batch, external procurement |
| Material | PK0513 | Label | Packaging material, no batch, external procurement |
| Material | PK0514 | Carton | Packaging material, no batch, external procurement |
| Material | PK0515 | Foil | Packaging material, no batch, external procurement |
| Material | PK0516 | Bag | Packaging material, batch managed , external procured |

Organization Data

| Data | Sample Value | Description | Other Attributes |
| --- | --- | --- | --- |
| Plant | 3310 | Plant 1 AE |  |
| Company Code | 3310 | Company Code 3310 |  |
| Storage Location | 331A | Std. storage 1 |  |
| Storage Location | 331B | Std. storage 2 |  |
| Storage Location | 331C | Raw mat. stoloc. |  |
| Controlling Area | A000 | Controlling Area A000 |  |
| Cost center | 33101301 | Manufacturing 1 (AE) |  |
| Plant | 3320 | Plant 2 AE |  |
| Company Code | 3310 | Company Code 3310 |  |
| Storage Location | 332A | Std. storage 1 |  |
| Storage Location | 332B | Std. storage 2 |  |
| Storage Location | 332C | Raw mat. stoloc. |  |
| Controlling Area | A000 | Controlling Area A000 |  |
| Cost center | 33101301 | Manufacturing 1 (AE) |  |

Bill of Material Structure

| Material | Level | Material Type | Unit | Characteristics of Material | Component Quantity | Component UOM |
| --- | --- | --- | --- | --- | --- | --- |
| FG0505 | 0 | FERT | PC | Finished Good DI, batch managed | 1 | PC |
| PK0512 | 1 | VERP | PC | Packaging material, no batch, external procured | 1 | PC |
| PK0513 | 1 | VERP | PC | Packaging material, no batch, external procured | 1 | PC |
| PK0515 | 1 | VERP | PC | Packaging material, batch managed, external procured | 40 | M |
| SG0505 | 1 | HALB | PC | Semifinished Product PI, batch managedProduction in other plant 3320 | 63 | PC |

Plant 3320

| Material | Level | Material Type | Unit | Characteristics of Material | Component Quantity | Component UOM |
| --- | --- | --- | --- | --- | --- | --- |
| SG0505 | 1 | HALB | PC | Semifinished product process manufacturing, batch managedGoods Receipt in plant 3310 | 1 | PC |
| RM0510 | 2 | ROH | KG | Raw material, batch managed, external procured | 0,8 | KG |
| RM0511 | 2 | ROH | KG | Raw material, batch managed, external procured | 0,8 | KG |
| RM0512 | 2 | ROH | L | Raw material, batch managed, external procured | 0,2 | L |
| RM0513 | 2 | ROH | KG | Raw Material, Batch Managed, External Procurement | 2,2 | KG |
| PK0513 | 2 | VERP | PC | Packaging material, no batch, external procured | 1 | PC |
| PK0514 | 2 | VERP | PC | Packaging material, no batch, external procuredWithdrawal from plant (3310) | 1 | PC |
| PK0516 | 2 | VERP | PC | Packaging material, batch managed, external procured | 20 | PC |

Resource

| Resource | Plant | Work Center Category | Resource Description |
| --- | --- | --- | --- |
| CC050001 | 3320 | 0008 | Production Line Cookie |

Work Center

| Work Center | Plant | Work Center Category | Resource Description |
| --- | --- | --- | --- |
| CC050002 | 3310 | 0001 | Packaging Line Cookie |

Routing

Create a routing for finished product FG0505 plant 3310

Production Version:

Create production versions for the finished product FG0505 using the BOM and routing created in the above steps in plant 3310.

For semifinished material SG0505 use master recipe and BOM from previous step for the production version creation in plant 3320.

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) .

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNR | Create Product Master of type "Raw Material" - MDS |
| BNS | Create Product Master of type "Semi-Finished Good" - MDS |
| BNT | Create Product Master of type "Finished Good" - MDS |
| 3Y1 | Create Product Master of Type "Packaging" - MDS |
| BNJ | Create Production Work Center - MDS |
| BNK | Create Material BOM for Production and Sales - MDS |
| BNL | Create Routing - MDS |
| 3X8 | Create Resource - MDS |
| 3X9 | Create Master Recipe - MDS |
| BLD | Create Production Version - MDS |
| 2ZW | Create Batch Management Master Data - MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/005791a252bce683c34e577d68998211)

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| BEG - Standard Cost Calculation | You have completed the step described in the test script. |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the steps described in the master data script. Posting Period is up to date. |
| J58 - Accounting and Financial Close | Execute to create open posting periods. |
| BLF - Batch Management | The settings must be available in the system. |
| BNU - Create Costing Run - MDS | You have completed the steps described in the master data script. |

### Preliminary Steps

#### Enhance Material Master

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Material (MM02) | The screen name adapts accordingly. |  |
| 3 | Enter Material Basic Data | On the Create Material (Initial Screen) screen, make the following entry:Material: SG0505Click on Select View(s). | The Select View(s) view displays. |  |
| 4 | Choose Views | On the Select View(s) Window, Select MRP2 and Choose Org. Levels. | The Organizational Levels view displays. |  |
| 5 | Choose Org. Level | On the Organizational Levels window, make the following entry:Plant: 3310Click on Continue. |  |  |
| 6 | Enter MRP/Planning Data | In the Change Material SG0505 (Semifinished Product) view, on the MRP 2 tab, in the Procurement section, make the following entry:Special Procurement: Y1 | The MRP 2 view displays. |  |
| 7 | Save Your Data | Choose Save. |  |  |

#### Initial Material Stock for plant 3320

Purpose

In a real business scenario, initial material stock are usually purchased from external vendors that can be covered by the standard purchasing processing. This process step shows you how to directly post initial stock to the storage location.

|  |
| --- |
| Note You can either post initial stock directly to the storage location or referring to the process of Procurement of Direct Materials (J45). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The screen name adapts accordingly. |  |
| 3 | Choose Goods Receipt-Other | Make the following entries and choose Enter:Action: Goods ReceiptReference: OtherMovement Type: 561 | The screen name adapts after entries are made. |  |
| 4 | Specify Material | On the Material tab, make the following entry:Material: RM0510 | Ensure that detail data is expanded. |  |
| 5 | Specify Quantity | On the Quantity tab, make the following entry:Qty in Unit of Entry : 2000 |  |  |
| 6 | Specify Plant and Storage Location | On the Where tab, make the following entries:Plant: 3320Storage Location: 332C |  |  |
| 7 | Check Item | Press Enter and ensure Item OK is selected. |  |  |
| 8 | Add Other Materials | Choose Next Item, then repeat steps 4 to 7 for the following data:MaterialQty in Unit of EntryRM05112000RM05121000RM051310000PK05132000PK05142000PK051630000 |  |  |
| 9 | Post Goods Movement | Choose Post. | Material document XXX is posted.Materials are available in unrestricted stock. |  |

#### Initial Material Stock for plant 3310

Purpose

In a real business case, the raw materials are usually purchased from external vendors that can be covered by the standard purchasing processing. This process step shows you how to directly post initial stock to the storage location.

|  |
| --- |
| Note You can either post initial stock directly to the storage location or referring to the process of Procurement of Direct Materials (J45). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The screen name adapts accordingly. |  |
| 3 | Choose Goods Receipt-Other | Make the following entries and choose Enter:Action: Goods ReceiptReference: OtherMovement Type: 561 | The screen name adapts after entries are made. |  |
| 4 | Specify Material | On the Material tab, make the following entry:Material: PK0512 | Ensure that detail data is expanded. |  |
| 5 | Specify Quantity | On the Quantity tab, make the following entry:Qty in Unit of Entry: 1000 |  |  |
| 6 | Specify Plant and Storage Location | On the Where tab, make the following entries:Plant: 3310Storage Location: 331C |  |  |
| 7 | Check Item | Press Enter and ensure Item OK is selected. |  |  |
| 8 | Add Other Materials | Choose Next Item, then repeat the steps 4 to 7 for the following materials:Material:PK0513Material:PK0515Material:PK0514 |  |  |
| 9 | Post Goods Movement | Choose Post. | Material document XXX is posted.Materials are available in unrestricted stock. |  |

## Overview Table

This scope item consists of several process steps provided in the attached file below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Anonymous Forecast and MRP |  |  |  |
| [Create Planned Independent Requirements](#unique_12) | Production Planner | Maintain PIRs (F3445) | Independent Requirements for Finished Goods are created. |
| [Material Requirements Planning at Plant Level](#unique_13) [page ] 19 | Production Planner | Schedule MRP Runs (F1339) | The MRP run has been executed for two plants. |
| [Evaluate Stock/Requirements Situation](#unique_14) [page ] 21 | Production Planner | Monitor Stock / Requirements List - Old Version (MD04)Monitor Material Coverage - Net / Individual Segments (F2101A) | Stock/Requirements situation for the planned materials is analyzed. |
| Production of Semifinished Material |  |  |  |
| Create Process Order - [Option 1: Convert Planned Orders to Process Orders](#unique_15) [page ] 24 | Production Planner | Manage Material Coverage - New Version (F0251A) | A process order is created. |
| Create Process Order - [Option 2: Create Process Order Manually](#unique_16) [page ] 25 | Production Supervisor - Process Manufacturing | Create Process Order (COR1) | A process order is created. |
| [Review Process Order (Optional)](#unique_17) [page ] 26 | Production Supervisor - Process Manufacturing | Display Process Order (COR3) | The process order is reviewed. |
| [Execute Goods Issue via Pick List](#unique_18) [page ] 28 | Production Operator - Process Manufacturing | Pick Components for Process Orders (COIK) | The Goods issue of components is posted. |
| [Monitor Order Progress (Optional)](#unique_19) [page ] 29 | Production Supervisor - Process Manufacturing | Manage Process Orders (F4587)Monitor Order Progress (CO46) | The order progress for the process order is monitored. |
| [Confirm Production](#unique_20) [page ] 31 | Production Operator - Process Manufacturing | Confirm Process Order Phase (COR6N). | The process order is confirmed. |
| [Post Goods Receipt for Process Order](#unique_21) [page ] 32 | Warehouse Clerk | Post Goods Receipt for Process Order (F6352). | The goods receipt for the process order is posted. |
| [Review Process Order Confirmation](#unique_22) [page ] 34 | Production Supervisor - Process Manufacturing | Manage Process Orders (F4587) | The order confirmations are reviewed. |
| Sales Order Processing |  |  |  |
| [Create Sales Order](#unique_23) [page ] 36 | Internal Sales Representative | Manage Sales Orders (F1873) | The sales order is created. |
| Packaging Process |  |  |  |
| [Material Requirements Planning at plant level](#unique_24) [page ] 38 | Production Planner | Schedule MRP Runs (F1339) | The MRP run has been executed. |
| [Evaluate Stock/Requirements Situation](#unique_25) [page ] 39 | Production Planner | Monitor Material Coverage - Net / Individual Segments (F2101A) | Stock/Requirements situation for the planned materials is analyzed. |
| [Convert Planned Order to Production Order](#unique_26) [page ] 41 | Production Planner | Manage Material Coverage - New Version (F0251A) | The production order is created. |
| [Review Production Order (Optional)](#unique_27) [page ] 42 | Production Supervisor - Discrete Manufacturing | Manage Production Operations (F2335) | The production order is reviewed. |
| [Manual Goods Issue](#unique_28) [page ] 43 | Warehouse Clerk | Post Goods Movement (MIGO) | The goods issue has been posted manually. |
| [Monitor Order Progress (Optional)](#unique_29) [page ] 44 | Production Supervisor - Discrete Manufacturing | Monitor Order Progress (CO46) | The order progress is monitored. |
| [Confirm Production Order incl. Component Backflush](#unique_30) [page ] 45 | Production Operator - Discrete Manufacturing | Confirm Production Operation (F3069) | The order operations are confirmed. |
| [Post Goods Receipt for Production Order](#unique_31) [page ] 47 | Warehouse Clerk | Post Goods Movement (MIGO) | The goods receipt has been posted. |
| Delivery Processing |  |  |  |
| [Create Delivery with Order Reference](#unique_32) [page ] 48 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A).Change Outbound Delivery (VL02N) | Outbound delivery is created for sales order. |
| [Execute Picking](#unique_33) [page ] 49 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | The outbound delivery is picked. |
| [Post Goods Issue](#unique_34) [page ] 51 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD)Display Outbound Delivery (VL03N) | The Goods issue for the delivery is posted. |
| Billing Process |  |  |  |
| [Create Billing Document](#unique_35) [page ] 52 | Billing Clerk | Create Billing Documents (F0798)Manage Billing Documents (F0797) | The billing document is created. |

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

For the finished material planning strategy 52 (Planning w/o Final Assembly and w/o MTO) is setup. Production quantities can be planned relatively effectively by means of planned independent requirements for the finished product. It is possible to use information from the sales forecast, or from the Sales Information System, or other planning tools to plan production quantities. Only the procurement of the component is triggered before the sales order stage. Final assembly takes place after a sales order has been entered. The Planned Independent Requirements are consumed by the sales order creation.

This process step shows you how to create Planned Independent Requirements (PIRs). A PIR contains one planned quantity and one date, or a number of planned independent requirements schedule lines, such as one planned quantity split according to dates.

|  |
| --- |
| Note Instead of creating a single requirement, sometimes one or more planned independent requirements can be maintained and included in a requirement plan for mass processing. In this case, the requirements are grouped and maintained under a requirement plan number. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Planner. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Maintain PIRs (F3445). | The Maintain PIRs screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, choose Area of Responsibility.On My Area of Responsibility screen, check if the below entry is assigned:Plant 1 AE (3310)MRP Controller 001 (001)Choose AOR Status if the status for the above entry is not yet assigned.Choose AOR Status to unassign the rest of other entries. |  |  |
| 4 | Select Material Items | On the Maintain PIRs screen, make the following entries and choose Go:Plant: 3310Period Indicator: Weekly(W)Version Active : Yes, No, N/AMaterial: FG0505 | The searched material item displays. If the material filter is not directly available choose Adapt Filters, select the Material Filter, enter the desired material and choose OK.Note If no PIRs for FG0505 have been maintained in the system before, the selection is empty in the app. In that case please leave this app and access the app Create PIRs (MD61), make the following entries on the Create Planned Independent Requirements: Initial Screen and choose Continue:Plant: 3310Period Indicator: Weekly (W)Version: 00Material: FG0505Choose Save and restart with step 1. |  |
| 5 | Edit PIRs. | Select the material item and choose Edit in the upper right corner of the screen.On the Edit PIRs screen, enter quantities per week, for example:Week 1 (current week + 1 week): 50 PCWeek 2 (current week + 2 weeks): 50 PCWeek 3 (current week + 3 weeks): 30 PCWeek 4 (current week + 4 weeks): 20 PCWeek 5 (current week + 5 weeks): 50 PCWeek 6 (current week + 6 weeks): 50 PCVersion Active: YES | Note If already stock for FG0505 is available, increase the quantity for PIR of current week + 1 for the stock already available. As an alternative, remove the stock to get planned orders in next step. |  |
| 6 | Save PIR's | Choose Save in the bottom right corner of the screen. | The PIRs saved. |  |

#### Material Requirements Planning at Plant Level

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows how to use Material Requirement Planning (MRP) to tailor available capacities and receipts on time to suit requirement quantities. Starting from finished material in plant 3310, a single-item multi-level requirement planning is performed cross-plant for plants 3310 and 3320.

Prerequisite

The Make-to-Stock finished goods are planned at plant level. There is now a requirement for FG0505 in plant 3310.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Planner. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Schedule MRP Runs (F1339). | The Schedule MRP Runs screen displays. |  |
| 3 | Create New Job | Choose Create.On the New Job screen, make the following entries:For 1. Template Selection section:Job Template: Material Requirements Planning (MRP)Job Name: MRP for FG0505Choose Step 2.For 2. Scheduling Options section:Start Immediately: <select>Choose Define Recurrence Pattern.On the Scheduling Information screen, make the following entries:Start Immediately: <select>Recurrence Pattern: Single RunChoose OK.Choose Step 3.For 3. Parameters section:Plant: 3310Material: FG0505Changed BOM Components: <select>Stock Transfer Materials: <select>Scheduling: 2Planning Mode: 1Choose Check at the bottom right.Choose Schedule. | A message appears: You can go ahead and schedule the job.Note There is no need to select all plants in scope for this particular process. The requirements from Planning plant 3310 are transferred automatically to production plant 3320, where the planning for the semifinished material takes place and all planning relevant components are considered as well. |  |
| 4 | Refresh Application Jobs List | To check the job’s status, enter MRP for FG0505 in the search box and choose Go at the top right section of the screen. | The new job is created and is displayed in the Jobs table when refreshed. |  |

#### Evaluate Stock/Requirements Situation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display the stock/requirements situation for Make-to-Stock finished goods (FG0505) and the components relevant for production (semifinished, packaging and raw materials) in the stock/requirements list after the requirement planning is performed.

|  |
| --- |
| Note The app Monitor Material Coverage - Net/Individual Segments is not showing preplanning segments that are created for the finished material based on the planning strategy. Therefore the app Monitor Stock /Requirements List is used for finished material FG0505. |

Prerequisite

Requirement planning is carried out.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Stock / Requirements List - Old Version (MD04). | The Stock/Requirements List: Initial Screen screen displays. |  |
| 3 | Select Material | Make the following entries and choose Continue:Material: FG0505Plant: 3310 | The Stock / Requirements List is displayed. |  |
| 4 | Review Stock / Requirements List | Review the planning results for material FG0505 in plant 3310.The planned orders in the Preplanning w/o Assembly section are INDR planned orders that are not convertible and used only for planning purposes only.Choose Back twice. | The detailed stock / requirements list for each material displays. |  |
| 5 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). | The Monitor Material Coverage - Net and Individual Segments screen displays. |  |
| 6 | Check Area of Responsibility | Choose the user icon and select App Settings. In the MRP Settings dialog box, choose Area of Responsibility.Check if only this entry displays, and choose OK:Plant 1 AE 3310 and New Plant 3320MRP Controller (001)Choose + to select this entry if not displayed; choose the Delete icon to remove any other plant entries and then choose OK. |  |  |
| 7 | Select Material | Search in the Material bar, select the following materials and then choose Go.Material: SG0505Material: RM0510Material: RM0511Material: RM0512Material: RM0513Material: PK0512Material: PK0513Material: PK0514Material: PK0515Material: PK0516Select following plants and then choose Go.Plant: 3310Plant: 3320 | The Material and Material Details subscreens display. |  |
| 8 | Display Details for each material | Select all the materials and choose Manage Materials.Note The BOM explosion during the MRP run has generated dependent requirements for the demand-driven planned components. If there is not enough inventory to fulfill the requirements, planned orders and purchase requisitions are created for both inhouse-produced and externally-procured materials. | The selected planned order displays.Note The planned order is generated only when there is shortage for these materials.If you want to display more information of the planned order, choose Document Info at the bottom of the dialog box. |  |
| 9 | Review Stock / Planning Situation for Semifinished Material | Choose the sections for material SG0505 in plants 3310 and 3320.On the Material Details subscreen, review the planning results (requirements are transferred from plant 3310 to plant 3320).On the Material Details subscreen, choose PldOrd XXX in the MRP Element column.Choose Back. | The detailed stock / requirements list for the semifinished material is displayed and can be reviewed. |  |
| 10 | Display Stock situation of Raw and Packaging Materials | Check for the other materials the stock / planning situation of Raw materials and Packaging materials as well. | The detailed stock / requirements list for each material is displayed and can be reviewed. |  |

### Production of Semifinished Material

The semifinished material is produced in production plant 3320 which is process industry managed and hence production is executed with process orders. The component PK0514 is needed for production but consumed from packaging plant 3310 directly. To avoid additional stock posting steps, the semifinished material produced in plant 3320 is directly posted to packaging plant 3310 for further processing.

#### Create Process Order

##### Option 1: Convert Planned Orders to Process Orders

Purpose

Daily MRP run creates planned orders for goods to be produced internally. This process step shows you how to convert the planned orders to process orders for semifinished materials when reached the planned start date.

Prerequisite

The MRP run has generated planned orders for SG0505 (semifinished material).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Convert Planned Orders - to Process Orders (COR8). | The Collective Conversion of Planned Orders: Initial Screen screen displays. |  |
| 3 | Select Material | Enter the following data and choose Execute.Planning Plant: 3310Production Plant: 3320Material: SG0505 | The Collective Conversion of Planned Orders: List screen displays. |  |
| 4 | Find Planned Order | Check the generated planned orders.If no planned orders are generated, it could be because SG0505 has sufficient amount of stock in store. In this case, remove some stock or enhance the amount for PIRs for SG0505 and run MRP again to generate planned orders. |  |  |
| 5 | Convert Planned Order to Process Order | Select the line with the planned order you want to convert. Choose Convert Planned Order for the selected planned order (PldOrd XXX).Note The conversion of the planned order can be executed from both plants, 3310 and 3320 (depending on authorizations). | The process order is created.Process Order Number ___________________. |  |

##### Option 2: Create Process Order Manually

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create process orders with status created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Process Order (COR1). | The Create Process Order: Initial Screen displays. |  |
| 3 | Enter Restriction | Make the following entries and choose Continue:Material Number: SG0505Planning Plant: 3310Confirm the warning that production will be executed in plant 3320. |  |  |
| 4 | Create Process Order: Header - General Data | Make the following entries and choose Save:Total Qty: <your quantity>Start : <today plus 1 week> |  |  |
| 5 | Validate Control Key | Choose Operations.Make sure, that the YPI1 entry is maintained in the Control Key field for all phases and subphases.Choose Back. |  |  |
| 6 | Save your order | Choose Save. | Process order is created and released in one stepMake a note of the process order number _______________________. |  |

#### Review Process Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to review created process orders. It is possible to perform this step with different SAP Fiori apps. We provide two options you can leverage, and you can choose either one of them.

Procedure

Option 1:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Process Order (COR3). | The Display Process Order: Initial Screen screen displays. |  |
| 3 | Enter Process Order Number | Make the following entry and choose Continue.Process Order: XXXX (From previous steps) | The Display Process Order: Header - General Data screen displays.On this screen, you find the order’s detailed information.Process orders are reviewed and checked within your responsibility area. |  |
| 4 | Review Material List | Choose button Material List.This list provides all components to be consumed. Please verify that component PK0514 is consumed directly from plant 3310 storage location, even though process order is created for plant 3320. All other components will be consumed from plant 3320.Choose Back. | Process order components are reviewed. |  |
| 5 | Navigate to Output Management | Select Menu > Process Order > Output > Manage Output Items . | The Overview Output Management: Output screen displays. |  |
| 6 | Check Output Item | On the Overview Output Management: Output screen, you could check output item lists in the Output section.Typically, following two items should be listed with status of Completed:Output Type: PICK_LIST; Channel: PRINTOutput Type: ORDER_DATA_LIST; Channel: PRINT |  |  |
| 7 | Display PDF Document | Select the output item with Channel: PRINT, and choose Display Document.Close the displayed document. | PDF document displays for the selected item. |  |
| 8 | Leave Order | Choose Back to leave the order. |  |  |

Option 2:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Process Orders (F4587). |  |  |
| 3 | Select AOR | If this is your first time to access the app, a welcome page would appear asking you to select your area of responsibility.Otherwise, choose your user name and the App Settings icon.On the My Area of Responsibility - Production Supervisor screen, choose Production Supervisor.Choose the following entry displayed:Plant 3310 AE / YB2Plant 3320 AE / YB2 |  |  |
| 4 | Choose the Process Order | In the process order list, find your process order and choose it.Process Order: XXXX (From previous steps) | In the header area, you can switch between Compact Filter and Visual Filter, to find a proper way to search for your process order number. |  |
| 5 | Review Process Order | In the detailed page of the process order, move to the Components section and select Settings. Select Storage Location in addition and choose OK.Please verify that component PK0514 is consumed directly from plant 3310 storage location 331C, even though process order is created for plant 3320. All other components will be consumed from plant 3320 storage location 332C. |  |  |
| 6 | Check Long Text Copied from Planned Order (Optional) | If any long text is maintained for the planned order, you can check it in the converted process order.In the Process Orders section, select an order and choose Edit Order in the upper right corner.On the Change Process Order: Header - General Data screen, choose icon Create Long Text next to Process Order number, and check the text.Choose Back to leave the process order. | The long text maintained in the planned order is copied to the converted process order. |  |

#### Execute Goods Issue via Pick List

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how all batch materials can be issued to the process order using the pick list when the released process order is ready for picking. The pick list can be used cross-plant (in this test case, the cartons PK0514 are stored in the packaging plant 3310 in storage location 331C but will be issued via pick list from a process order created within production plant 3320).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Pick Components for Process Orders (COIK). | The Picking List: Initial Screen displays. |  |
| 3 | Enter Restriction and Execute | Make the following entries and then choose Execute.Profile: 000002Process Order: <XXXX> (from previous steps) | The Order Information System: Detail List of Components screen displays. |  |
| 4 | Picking Raw Materials | Select the relevant reservations and choose Picking. | The Picking list screen displays. On this screen, a list of all the selected reservations displays. |  |
| 5 | Perform Batch Determination for Batch-managed Components | Select the picking lines for following batch-managed material and choose Batch Determination:Material: RM0510Material: RM0511Material: RM0512Material: RM0513Material: PK0516 | The Batch Determination MM: Select Batches screen displays.If the system shows the message Batch determination was carried out without selection specification, ignore it.If during batch determination only part of the required quantity is found to be available, the unconfirmed quantity remains as an open line item within the picking list. You should then delete the line item from the picking list before saving, as this line item cannot be posted. |  |
| 6 | Copy Batch Determination Result | Choose Copy. | The Picking list screen displays again. In addition, the batch numbers have been determined. |  |
| 7 | Post Goods Movements | Choose Post. | The goods movements are posted. |  |

#### Monitor Order Progress (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to monitor process orders. It is possible to perform this step with different SAP Fiori apps. We provide two options you can leverage, and you can choose either one of them.

Procedure

Option 1:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Process Orders (F4587). |  |  |
| 3 | Select AOR | If this is your first time to access the app, a welcome page would appear asking you to select your area of responsibility.Otherwise, choose your user name and the App Settings icon.On the My Area of Responsibility - Production Supervisor screen, choose Production Supervisor.Choose the following entry displayed:Plant 3320 AE / YB2 |  |  |
| 4 | Choose the Process Order | In the process order list, find your process order and choose it.Process Order: XXXX (From previous steps) | In the header area, you can switch between Compact Filter and Visual Filter, to find a proper way to search for your process order number. |  |
| 5 | Review Process Order | In the detailed page of the process order, review relevant information. |  |  |

Option 2:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Order Progress (CO46). | The Order Progress Report: Selection Screen displays. |  |
| 3 | Enter Overall Profile | Make the following entry and choose the Production/Process Order tab.Overall Profile: SAP000000002 |  |  |
| 4 | Enter Process Order Number | Make the following entry and choose Execute.Production/Process Order: XXXX (from previous steps) | The Stock/Requirements List as of XX hrs screen displays.You can review the required lists, such as order header and components lists. |  |

#### Confirm Production

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The confirmation documents include the processing status of order, operations, phases and individual capacities. It is an instrument to control the order. The time ticket confirmation allows recording either the default times for machine and labour usage, or actual times for major deviations. This process step shows you how to confirm production. You can post scrap quantities optional.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Confirm Process Order Phase (COR6N). | The Enter Time Ticket for Process Order screen displays. |  |
| 3 | Enter Confirmation Option | Make the following entries and then choose Enter.Order: XXXX (from previous steps)Choose Enter or select phase 0020 for material SG0505 from search help of Phase field.Confirm.type: Final confirmationClear open reservations: X | If the system shows the message Total quantity confirmed not equal to planned quantity to be confirmed, press Enter to ignore it. |  |
| 4 | Propose Actual Data | Choose Actual Data.Make the changes for the following fields:Scrap: <Enter the amount you want to Scrap>Yield: <Based on the origin quantities minus Scrap>Reason for Var: <Enter scrap reason if need>, for example, 0001 | The Quantities and Activities will be filed automatically. |  |
| 5 | Save Confirmation | Save your entries. | The final confirmation of the last operation is carried out. Costs and activity quantities are recalculated in proportion to the yield quantity. |  |

#### Post Goods Receipt for Process Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Even though the production has been carried out in plant 3320, the goods receipt will be posted directly in plant 3310 and material SG0505 is directly available for further processing (packaging).

You may post goods receipt for the total quantity, but usually already partial quantities of the products are required for further processing, such as consumption for further production or subsequent deliveries for sales orders.

It is possible to perform this step with different SAP Fiori apps. We provide two options you can leverage, and you can choose either one of them.

Procedure

Option 1

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as Warehouse Clerk. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Post Goods Receipt for Process Order (F6352). |  |  |
| 3 | Enter Process Order | Make the following entry and then press Enter.Process Order: XXXX (From previous steps) | The details of the order is listed. |  |
| 4 | Enter Date of Manufacturing for FG0505 | Find the Order item and choose it.Choose the Batch tab and enter a batch number (optional) and the Date of Manufacturing. |  |  |
| 5 | Post Goods Movement | Ensure the item is selected and choose Post. | The goods movements are posted. The batch number is created automatically during the posting if not entered manually in previous step. Production date and shelf life expiration date are recorded within the batch master. |  |

Option 2

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as Warehouse Clerk. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Initial screen displays. |  |
| 3 | Enter Process Order | Make the following entries and then press Enter:Action: Goods ReceiptReference: OrderProcess Order: XXXX (From previous steps)Movement Type: 101 | Screen name adapts after entries are made. |  |
| 4 | Enter Date of Manufacture | Choose the Batch tab and enter a batch number (optional) and the Date of Manufacturing. |  |  |
| 5 | Check Item | Select item OK. | Ensure that detail data is expanded. |  |
| 6 | Post Goods Movement | Choose Post. | The goods movements are posted. The batch number is created automatically during the posting if not maintained manually. Production date and shelf life expiration date are recorded within the batch master. |  |

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
| 2 | Access the App | Open Manage Process Orders (F4587). |  |  |
| 3 | Select AOR | If this is your first time to access the app, a welcome page would appear asking you to select your area of responsibility.Otherwise, choose your user name and the App Settings icon.On the My Area of Responsibility - Production Supervisor screen, choose Production Supervisor.Choose Add or Delete to add or remove entries, and make sure following entry displays:Plant 3320 AE/ YB2 |  |  |
| 4 | Choose the Process Order | In the process order list, find your process order and choose it.Process Order: XXXX (From previous steps) | In the header area, you can switch between Compact Filter and Visual Filter, to find a proper way to search for your process order number. |  |
| 5 | Review Process Order | In the detailed page of the process order, review confirmations of the process order. |  |  |

Option 2:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Process Order Confirmation (CORT). | The Display Process Order Confirmation: Initial Screen displays. |  |
| 3 | Enter Process Order | Make the following entry and then choose Enter.Process Order: XXXX (from previous steps) | The Process Order Confirmation Display: Details screen displays.Confirmations are reviewed and checked within your responsibility area. |  |

Option 3:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Process Order Operations. |  |  |
| 3 | Choose Filter Style | In the header part, you can switch between Compact Filter and Visual Filter, which provides you different styles for filter. |  |  |
| 4 | Enter Process Order Number | Choose Compact Filter, make the following entry and choose Go.Process Order: XXXX (from previous steps) | Operation list displays. |  |

### Sales Order Processing

#### Create Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

According to the planning strategy, the final assembly takes place after a sales order has been entered. The planned independent requirements are consumed during sales order creation.

This process step shows you how to create Sales Order directly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Order screen displays. |  |
| 3 | Navigate to Create Sales Order Screen | On the Manage Sales Order screen, choose Create Sales Orders - VA01. |  |  |
| 4 | Enter the Order Type and the Sales Organization | On the Create Sales Documents screen, make the following entries and choose Continue:Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 5 | Enter Order Details | On the Create Standard Order: Overview screen, make the following entries:Sold-to Party: 33100001Ship-to Party: 33100001Customer Reference: <Enter a reference number>Req. Deliv. Date: <Today plus 1 month>Material Number: FG0505Order Quantity: <5 PC>Double click on Item 10.Choose tab Conditions.Enter condition type PPR0.Enter price. |  |  |
| 6 | ATP Check | If the Review Availability Check Result screen displays:Check the Confirmed Delivery Date and Confirmed Quantity in Requirements. Make a note of the Delivery Date.Choose Apply. |  |  |
| 7 | Save Document | Choose Save. Make a note of the sales order number. | The order is saved. |  |

|  |
| --- |
| Note If you maintain different material prices by Ledger (scope item 1ZT - Managing Material Price Changes and Inventory Values) and want to do Ledger specific sales order costing, please refer to the scope item BEG - Standard Cost Calculation and its step Appendix > Manage Order BOM Cost Estimates in Parallel Valuation. |

### Packaging Process

The Packaging process is triggered by the sales order (see previous step). The semifinished material is preplanned, produced in advance and directly posted to the packag-ing plant for immediate availability. The packaging process can start immediately after customer order creation.

#### Material Requirements Planning at plant level

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

The Make-to-Stock finished goods are planned at plant level. There is now a requirement for FG0505 in plant 3310.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Planner. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Schedule MRP Runs (F1339). | The Schedule MRP Runs screen displays. |  |
| 3 | Create New Job | Choose Create.On the New Job screen, make the following entries:For 1. Template Selection section:Job Template: Material Requirements Planning (MRP)Job Name: MRP for FG0505Choose Step 2.For 2. Scheduling Options section:Start Immediately: <select>Choose Define Recurrence Pattern.On the Scheduling Information screen, make the following entries:Start Immediately: <select>Recurrence Pattern: Single RunChoose OK.Choose Step 3.For 3. Parameters section, make the following entries:Plant: 3310Material: FG0505Changed BOM Components: <select>Stock Transfer Materials: <select>Scheduling: 2Planning Mode: 1Choose Check at the bottom right.Choose Schedule. | A message appears: You can go ahead and schedule the job. |  |
| 4 | Refresh Application Jobs List | To check the job’s status, enter MRP for FG0505 in the search box and choose Go at the top right section of the screen. | The new job is created and is displayed in the Jobs table when refreshed. |  |

#### Evaluate Stock/Requirements Situation

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
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). | The Monitor Material Coverage - Net and Individual Segments screen displays. |  |
| 3 | Check Area of Responsibility | Choose the user icon, select App Settings > Area of Responsibility , and make sure only following values are assigned:Plant 1 AE (3310)MRP Controller 001(001)Choose AOR status button of this entry if not assigned, choose AOR status button of the corresponding entry to unassign any other entry then choose Back. |  |  |
| 4 | Select Material | Select the checkbox of the following material, and then choose Manage Materials.Material: FG0505 | The Manage Material Coverage screen displays. |  |
| 5 | Check Planned Order | Find the generated planned order, and make a note of the number of this Planned Order.Stay in this page for following processing. | An individual Planned Order is created for the Sales Order you created before. |  |

#### Convert Planned Order to Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Daily MRP run creates planned orders for materials to be produced internally. This process step shows you how to convert the planned orders to production orders for finished materials when reached the planned start date.

Prerequisite

The MRP run has generated convertible planned orders for FG0505. The Planned Independent Requirements have been reduced for that amount.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Material Coverage - New Version (F0251A). | The Manage Material Coverage screen displays with Find Material dialog box. |  |
| 3 | Select Material | Enter the following data in the Find Material dialog box and choose OK.Material: FG0505Plant: 3310Shortage Definition: MRP Standard | The Manage Material Coverage screen displays. |  |
| 4 | Find Planned Order | Check the generated planned orders.If no planned orders are generated, it could be because FG0505 has sufficient amount of stock in store. In this case, remove some stock. Go back to create PIRs and run MRP again to generate planned orders. |  |  |
| 5 | Add Planned Order Long Text (Optional) | Click on the planned order number (PldOrd XXXX) under column MRP Element. In the quickview screen, choose Open Planned Order.On the Change Planned Order: Stock order screen, choose tab Long Text, enter the text, and choose Save. | The long text maintained here can be later copied to the converted production order. |  |
| 6 | Convert Planned Order to Production Order | Select Convert from Edit dropdown list in the Actions column for a planned order (PldOrd XXXX).In the Convert Planned Order XXXX dialog box, choose Convert to Production Order radio button, confirm End Date and Quantity. Choose OK. | The production order is created.Production Order Number ___________________. |  |

#### Review Production Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display and check the production order for finished goods after its release or confirmation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Production Operations (F2335). | The Manage Production Operations screen displays. |  |
| 3 | Select AOR | If this is your first time to access the app, a welcome page would appear asking you to select your area of responsibility.Otherwise, choose your user name and the App Settings icon.On the My Area of Responsibility - Production Supervisor screen, choose Production Supervisor.Choose the following entry displayed:3310/ YB5 |  |  |
| 4 | Select Production Order | On the Manage Production Operations screen, choose Adapt Filters to display more filter options.In the Adapt Filters dialog box, choose More Filters select Material and Plant and choose OK.Enter the following filters criteria and choose Go.Material: FG0505Plant: 3310 | The Material and Plant fields are then added to filter bar.Selected order displays.Operations of production order must be in status Released. |  |
| 5 | Check Detailed Operations StatusCheck Details of Production Order | Check detailed information for selected production operations.Operation Issues:Empty if there is no production order issue.Delay or Missing Components / PRT issue or Quantity Deviation / Quality Issue information shows if relevant issue exists.Components:Material, total quantity and Issued / open quantity information for order components displays.Order Schedule:Detailed operation information with relevant work center, confirmed quantity, start and end time displays.Work Center Schedule:The relevant order covering the same work center capacity (Operations in Progress) displays.Operations not Started:The relevant order that would cover the same work center capacity (operation is released) displays.Confirmation:Detailed confirmation information with Yield, Scrap, Rework quantity displays if confirmation has been executed.Inspection:Detailed inspection lots information displays if existed. | Detailed operations status displays. |  |

#### Manual Goods Issue

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
| 3 | Enter Production Order | Make the following entries and then choose Enter.Trans./Event: Goods IssueReference Document: OrderOrder number: XXXX (from previous steps)Movement Type: 261 | The screen name adapts after entries are made. |  |
| 4 | Perform Batch Determination for Batch-managed Material | For item with batch managed material, navigate to the Quantity tab in the Detail Data section, choose Stock Determ. icon besides Qty.Material: SG0505 | The Batch Determination MM: Select Batches screen displays. |  |
| 5 | Copy Batch Determination Result | Check the required batch and choose Copy. | The Goods Issue Order XXXX screen displays. In addition, the batch numbers have been determined. |  |
| 6 | Check Each Item | For each item shown, select Item OK. | Ensure that detail data is expanded. |  |
| 7 | Post Goods Movements | Choose Post. | The goods movements have been posted. |  |

#### Monitor Order Progress (Optional)

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
| 2 | Access the App | Open Monitor Order Progress (CO46). | The Order Progress Report: Selection Screen displays. |  |
| 3 | Enter Overall Profile | Make the following entry and choose the Production/Process Order tab.Overall Profile: SAP000000002 |  |  |
| 4 | Enter Process Order Number | Make the following entry and choose Execute.Production/Process Order: XXXX (from previous steps) | The Stock/Requirements List as of XX hrs screen displays.You can review the required lists, such as order header and components lists. |  |

#### Confirm Production Order incl. Component Backflush

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The confirmation documents include the processing status of orders, operations, sub-operations, and individual capacities. It is an instrument for controlling orders. This process step shows you how to use time event confirmation.

Prerequisite

The production order for finished material FG0505 is released.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Confirm Production Operation (F3069). | The Enter Order and Operation screen displays. |  |
| 3 | Enter Production Order and Operation | On the Enter Order and Operation screen, make the following entries and choose Go:Order: <production order number for material FG0505>Operation: <operation number>, for example, <0010> | The Confirm Production Operation screen displays. |  |
| 4 | Enter Quantities Data | In the Quantities section, make the following entries and press Enter:Yield: <yield amount>Scrap: <scrap amount> |  |  |
| 5 | Enter Activities Data | In the Activities section, make the following entries:Setup: <setup time>Machine: <machine time>Labor: <labor time> |  |  |
| 6 | Check Material Movements | In the Material Movements section, you can see all materials set for automatic goods movements (goods receipt and goods issue). | The system displays an overview table of all materials for which the withdrawing is automatically done with the confirmation of the operation.Note There are no materials set for backflush (in material master) or automatic goods receipt and no materials are displayed in the table for this confirmation |  |
| 7 | Save Your Entries | For partial confirmation, choose Post.For final confirmation, choose Post and Complete. | Confirmation is made. |  |

#### Post Goods Receipt for Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post the goods receipt for production order for packaging process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). |  |  |
| 3 | Enter Goods Receipt Order | Choose Goods Receipt > Order in the header area and make the following entries:Order: <production order number for finished goods FG0505>GR goods receipt: <101>Document date: <default>Posting date: <default>On the General tab, next to the Printer icon, select Print via Output Control (mouseover) checkbox, and choose Individual Slip. |  |  |
| 4 | Enter Quantity | On the Quantity tab, confirm production order quantities.On the Where tab, enter the following entry:Storage Location: 331A (Std. storage 1)On the Batch tab, enter Date of Manufacture as today's date. |  |  |
| 5 | Set Item OK and Post | Select the Item OK checkbox and choose Post. | The system displays the message Material document 500xxxxxxx posted. |  |

### Delivery Processing

#### Create Delivery with Order Reference

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Create Outbound Deliveries - From Sales Orders (F0869A). | The Create Outbound Deliveries screen displays. |  |
| 3 | Search Sales Order | Make the following entries and choose Go:Shipping Point: 3310Planned Creation Date: <Delivery selection date>Sales Document: <Sales order number> |  |  |
| 4 | Create Delivery | Select your sales order items and choose Create Deliveries. | Creation of a delivery is triggered. |  |
| 5 | Check Details | Choose Display Log. | The Analyze Delivery Log screen displays, delivery is created successfully. Delivery number displays on Deliveries tab. |  |

|  |
| --- |
| Note Depending on the scope item settings, the availability is checked at the delivery creation using the available inventory and replenishment lead time. Without sufficient stock, the created delivery has no confirmed quantities, and therefore does not start the warehouse management picking process. As soon as there is sufficient stock for delivery creation, the system creates a delivery with the starting of the picking process in warehouse management. |

To avoid open deliveries, ensure there is sufficient inventory quantity at the time for delivery creation. Additionally, you have the following options to restrict the creation of deliveries with no confirmed quantities.

You may increase the replenishment lead time which is used during the availability check (has to be larger than the selection period used for delivery creation).

You may change the customization settings for the incompleteness procedure for delivery creation, so that only complete deliveries may be saved.

You may change the customization settings for the used delivery-item-category. The Check quantity 0 field must be adapted to B = Situation Rejected with An Error Message.

|  |
| --- |
| Note With the Analyze Delivery Logs app, you can display an overview about the logs of all the deliveries which have been created in your system. You can filter by, for example, Created by and other additional settings. If you select the arrow on the right of each delivery log entry you can display the exact message type and text and also the related sales document. |

Printing form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). |  |  |
| 3 | Issue Delivery Output | On the Change Outbound Delivery (VL02N) screen, enter the Delivery Number, and choose Continue.From the Outbound Delivery xxxxxxxx Change: Overview screen, choose Menu > Extras > Delivery Output > Output Control . | The Outbound Delivery: Output screen displays. |  |
| 4 | Print Preview | On the Outbound Delivery: Output screen, select the line with the DELIVERY_PICK_LIST Output Type, and choose Display Document. | A preview of the print document is displayed. |  |
| 5 | Print Delivery Pick List | From the preview of the document, choose Print. | The delivery pick list is printed. |  |

#### Execute Picking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The picking process involves taking goods from a storage location and staging the right quantity in a picking area where the goods are prepared for shipping. This process step shows you how to pick deliveries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Choose Picking | Choose For Picking. |  |  |
| 4 | Enter Shipping Point | Make the following entries, and choose Execute:Shipping Point/Receiving Pt: 3310Under the Picking Data tab, selectOnly Picking Without WM: X |  |  |
| 5 | Change Outbound Deliveries | From Day’s Workload for Picking, select <Delivery number>, and choose Change Outbound Deliveries. |  |  |
| 6 | Check Batch Split | Choose the Picking tab, check if batch split exists in the Batch Split Indicator column. |  |  |
| 7 | Enter Picked Quantity | If batch split exists, choose Batch Split Exists to expand sub item(s), enter <quantity equal to delivery Qty> in Picked Qty field for sub item.If batch split doesn't exist, enter <quantity equal to delivery Qty> in Picked Qty field for picking related item(s).In the Batch field, enter the batch number for material FG0505 |  |  |
| 8 | Choose Enter | Choose Enter. |  |  |
| 9 | Save | Choose Save. | The delivery has been decided. |  |

#### Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post goods issues for delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Open Outbound Delivery Monitor | Choose For Goods Issue. Make the following entry and choose Execute.Shipping Point/Receiving Pt: 3310 |  |  |
| 4 | Post Goods Issue | Select your outbound delivery note, and choose Post Goods Issue.Select today’s date from the dialog box, and choose Continue. | A message confirms the goods issue has been posted. |  |

Printing Form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Outbound Delivery (VL03N). | The Display Outbound Delivery screen displays. |  |
| 3 | Issue Delivery Output | In the Outbound Delivery field, enter <Outbound Delivery Number>, and choose Continue.On the Outbound Delivery xxxxxxxx Display: Overview screen, choose Menu > Extras > Delivery Output > Output Control. | The Delivery: Output screen displays. |  |
| 4 | Print Preview | On the Outbound Delivery: Output screen, select the line with the Output Type Delivery Note, and choose Display Document. | A preview of the print document is displayed. |  |
| 5 | Print Delivery Note | From the preview of the document, choose Print. | The delivery note is printed. |  |

### Billing Process

#### Create Billing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to handle the billing. Create a billing document referring to the delivery created in the previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798) . | The Create Billing Documents screen displays. |  |
| 3 | Define Billing Settings | Choose Billing Settings, you can make the following settings as below and click OK:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: OFFAutomatically post billing documents: ONDisplay billing documents after creation: ONChoose delivery items to be billed and select quantities: OFF |  |  |
| 4 | Search for billing due list | In the search condition, use criteria if necessary. | Sales document(s) display in the result. |  |
| 5 | Select item(s) for billing | Select row(s) of SD Document created previously and choose button Create Billing Documents. | The Create Billing Document pop up displays. |  |
| 6 | Maintain Billing Date | Choose the billing type Invoice (F2) and maintain billing date, for example current date, then press button OK. | The draft billing document with TMP xxxxxx displays. |  |
| 7 | Save Billing Document | On the Manage Billing Documents screen, choose Save.The draft version billing document with TMP xxxxxx turns into a saved billing document with ID xxxxxxxx, make a note of the billing document number: __________. | The system generates an invoice for billing. |  |

Manage Billing Documents

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Billing Documents (F0797) . | The Manage Billing Documents screen displays. |  |
| 3 | Search Billing Document | Enter the Billing document number recorded in the previous step. Choose Enter. | The billing document created in the previous step displays |  |
| 4 | Display Billing document | Select the billing document item, and choose Display. | The billing document displays. |  |
| 5 | Check Output Condition | Choose the last assignment block - Output Items. | There is one entry in the item and the output type is BILLING_DOCUMENT. |  |
| 6 | Display Print Preview | Choose Preview. | Preview for PDF document displays. |  |
| 7 | Cancel Billing Document (Optional) | Select a certain billing document and choose Cancel Billing Docs. | Message Billing Documents Canceled displays. |  |
| 8 | Update New Attachment (Optional) | In the Edit mode, add, delete and update the attachments. Save your changes by pressing the Save button in the footer bar. |  |  |
| 9 | Update New Text (Optional) | In the Edit mode, you can add, delete and update these texts. Save your changes by pressing the Save button in the footer bar. |  |  |

## Appendix

### Succeeding Processes

The following processes and conditions can succeed this process.

| Process | Business Condition |
| --- | --- |
| Technical Completion of Orders (Optional) | You can access Schedule Order Technical Completion Run (F3841) app as a Production Supervisor - Process Manufacturing to schedule a job to set production orders as Technical Completion.If you need to set a production order as Technical Completion separately, you can access Manage Material Coverage - New Version (F0251A) app as a Production Planner, find your production order and select Delete. |
| Close Confirmed Production/Process Orders (Optional) | Search for Schedule Order Closing Runs - Close Production/Process Orders (F4305) app as a Production Supervisor - Process Manufacturing to schedule a job to set orders as Closed (CLSD). |
| 3F0 - Event-Based Production Cost Posting | This procedure updates work-in-process calculation, overhead calculation, and variance calculation by linking the posting to the events.Note Start from SAP S/4HANA Cloud Public Edition2105, the default Best Practice content is based on event-based result analysis for new customer install and add new country only, rather than previous period-end posting. For existing customers (who activated content before 2105), the default remain unchanged to Period-End Closing – Plant (BEI) till customer makes the decision to switch. For migration to Event based from Periodic please refer [Production Settlement in Parallel Ledgers](https://help.sap.com/viewer/4032610758dc437089f0c28320eec93f/2105.500/en-US/e49a3770f22547a392455154f3eef6e2.html).If you are still using period-end posting, you may need to refer to non-standard Scope Item BEI - Period-End Closing – Plant. |
| BEI - Period-End Closing – Plant | Use this scope item to execute period-end closing. |

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
> Flagged while digesting this document, not verified: Internal inconsistency on batch management of PK0515 (Foil): the master data table lists it as 'Packaging material, no batch, external procurement' while the plant 3310 BOM table lists it as 'Packaging material, batch managed, external procured' (component quantity 40 M).

## Connections
- part-of :: [[_cluster]]
- related-to :: [[12-production-and-manufacturing/test-script-material-requirements-planning-j44-ae-sap-s-4hana-cloud-pu]]
- related-to :: [[12-production-and-manufacturing/test-script-sap-s-4hana-cloud-public-edition-predictive-material-and-r]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7DN_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 91,802 chars in the whole document
