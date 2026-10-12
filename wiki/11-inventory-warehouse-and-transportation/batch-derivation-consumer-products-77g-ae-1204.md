---
id: 11-inventory-warehouse-and-transportation/batch-derivation-consumer-products-77g-ae-1204
title: Batch Derivation – Consumer Products (77G_AE) (77G_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 77G_AE: one- and two-level batch derivation in consumer products, with SSCUI setup, MRP, process orders and batch cockpit."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/batch-management-master-data]
aliases: [77G_S4CLD2608_BPD_EN_AE]
keywords: [Batch Management Master Data, batch derivation, batch derivation configuration, derivation strategies, one-level batch derivation, two-level batch derivation, process orders, batch information cockpit, production versions, planned independent requirements]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/77G_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1204
topic: 11-inventory-warehouse-and-transportation/batch-management-master-data
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Batch Derivation – Consumer Products (77G_AE) (77G_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/77G_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Batch Management Master Data** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Batch Derivation – Consumer Products (77G_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Batch Derivation – Consumer Products (77G_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 4](#_Toc232859948)

[2 Prerequisites 5](#_Toc232859949)

[2.1 System Access 5](#_Toc232859950)

[2.2 Roles 5](#_Toc232859951)

[2.3 Master Data, Organizational Data, and Other Data 6](#_Toc232859952)

[2.4 Business Conditions 9](#_Toc232859953)

[2.5 SSCUIs 9](#_Toc232859954)

[2.5.1 Maintain Number Range for Batch Derivation ID 9](#_Toc232859955)

[2.5.2 Maintain Number Range for Batch Derivation Condition Records 11](#_Toc232859956)

[2.5.3 Define Access Sequences to Determine Sending Batches 12](#_Toc232859957)

[2.5.4 Define Strategy Types to Determine Sending Batches 14](#_Toc232859958)

[2.5.5 Define Search Procedures to Determine Sending Batches 16](#_Toc232859959)

[2.5.6 Define Access Sequences to Determine Receiving Batches 18](#_Toc232859960)

[2.5.7 Define Strategy Types to Determine Receiving Batches 19](#_Toc232859961)

[2.5.8 Define Search Procedures to Determine Receiving Batches 21](#_Toc232859962)

[2.5.9 Define Derivation Event 22](#_Toc232859963)

[2.6 Preliminary Steps 24](#_Toc232859964)

[2.6.1 Manage Derivation Strategies – Sender 24](#_Toc232859965)

[2.6.2 Manage Derivation Strategies – Receiver 25](#_Toc232859966)

[2.6.3 Create Initial Material Stock 27](#_Toc232859967)

[3 Overview Table 30](#_Toc232859968)

[4 Test Procedures 33](#_Toc232859969)

[4.1 Make Decision to run One- or Two-Level Batch Derivation 33](#_Toc232859970)

[4.1.1 Manage Production Versions 33](#_Toc232859971)

[4.2 Anonymous Forecast and MRP 34](#_Toc232859972)

[4.2.1 Create Planned Independent Requirements 34](#_Toc232859973)

[4.2.2 Material Requirements Planning at Plant Level 36](#_Toc232859974)

[4.2.3 Evaluate Stock/Requirements Situation 38](#_Toc232859975)

[4.3 One-level Batch Derivation 40](#_Toc232859976)

[4.3.1 Process Order Creation and Processing for Finished Material 40](#_Toc232859977)

[4.3.1.1 Create Process Order 40](#_Toc232859978)

[4.3.1.1.1 Option 1: Convert Planned Order to Process Orders 40](#_Toc232859979)

[4.3.1.1.2 Option 2: Create Process Order Manually 41](#_Toc232859980)

[4.3.1.2 Review Process Order 42](#_Toc232859981)

[4.3.1.3 Post Goods Issue of Batch Managed Components 44](#_Toc232859982)

[4.3.1.4 Monitor Order Progress (Optional) 45](#_Toc232859983)

[4.3.1.5 Confirm Production incl. Component Backflush 47](#_Toc232859984)

[4.3.1.6 Post Goods Receipt for Process Order 48](#_Toc232859985)

[4.3.1.7 Review Process Order Confirmation 50](#_Toc232859986)

[4.4 Two-Level Batch Derivation 52](#_Toc232859987)

[4.4.1 Process Order Creation and Processing for Seminfinished Material 52](#_Toc232859988)

[4.4.1.1 Create Process Order 52](#_Toc232859989)

[4.4.1.1.1 Option 1: Convert Planned Order to Process Orders 52](#_Toc232859990)

[4.4.1.1.2 Option 2: Create Process Order Manually 53](#_Toc232859991)

[4.4.1.2 Review Process Order 55](#_Toc232859992)

[4.4.1.3 Post Goods Issue of Batch Managed Components 57](#_Toc232859993)

[4.4.1.4 Monitor Order Progress (Optional) 58](#_Toc232859994)

[4.4.1.5 Confirm Production and Post Goods Receipt 60](#_Toc232859995)

[4.4.2 Process Order Creation and Processing for Finished Material 61](#_Toc232859996)

[4.4.2.1 Create Process Order 61](#_Toc232859997)

[4.4.2.1.1 Option 1: Convert Planned Order to Process Orders 61](#_Toc232859998)

[4.4.2.1.2 Option 2: Create Process Order Manually 62](#_Toc232859999)

[4.4.2.2 Review Process Order 64](#_Toc232860000)

[4.4.2.3 Post Goods Issue of Batch Managed Components 66](#_Toc232860001)

[4.4.2.4 Monitor Order Progress (Optional) 67](#_Toc232860002)

[4.4.2.5 Confirm Production incl. Component Backflush 69](#_Toc232860003)

[4.4.2.6 Post Goods Receipt for Process Order 70](#_Toc232860004)

[4.4.2.7 Review Process Order Confirmation 71](#_Toc232860005)

[4.5 Monitor Batch Derivation 73](#_Toc232860006)

[4.6 Batch Information Cockpit - Top-Down and Bottom-Up Analysis 74](#_Toc232860007)

[5 Appendix 77](#_Toc232860008)

[5.1 Process Integration 77](#_Toc232860009)

[5.2 Preceding Processes 77](#_Toc232860010)

[5.3 Succeeding Processes 77](#_Toc232860011)

## Purpose

Overview

This document outlines the production and packaging processes in the Consumer Products Industry, focusing on batch derivation of the earliest manufacturing date from component batches to the produced material. Condition records maintain the relevant inheritance characteristics. The goods receipt posting of finished products after production serves as a derivation event. Batch derivation can be performed at one or more manufacturing levels, with two alternative processes described: a single-step and a two-step batch derivation. At the start, you choose between these alternatives by selecting a corresponding production version.

The process begins with creating a demand forecast for finished goods, represented by Planned Independent Requirements (PIRs). Based on PIRs, Material Requirements Planning (MRP) generates a production plan for finished goods and explodes the entire bill of material structure. This results in planned production for finished products, semifinished products (in two-step batch derivation), and purchase requirements.

In the two-step batch derivation process, production starts with converting a planned order into a process order or directly creating a process order for the semifinished product. The goods issue of components (one or more batches per component), production confirmation, and goods receipt of the semifinished product are then executed.

The packing process applies to both single-level and two-step batch derivation. It begins with converting a planned order to a process order or directly creating a process order for the finished product. The goods issue of components, production confirmation, and goods receipt of the finished product follow.

You can check the results of the one-step or two-level batch derivation in the derivation monitor. The Batch Cockpit is available for batch traceability checks. Manual derivation is possible but not included in this scenario.

|  |
| --- |
| Note Because of the alternatives, there are process steps that are only relevant for two-stage batch derivation. They are marked in the header of the different sections of the test script. Moreover, some process steps need to be executed differently depending on the selected alternative, these differences are noted within in the particular steps. |

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
| Master Data Specialist - Batch Data | SAP_BR_BATCH_MASTER_SPCLST | Master Data - Batch | SAP_BR_BATCH_MASTER_SPCLST |  |
| Quality Technician | SAP_BR_QUALITY_TECHNICIAN | Quality Inspection | SAP_BR_QUALITY_TECHNICIAN |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Production Engineer - Process Manufacturing | SAP_BR_PRODN_ENG_PROC | Production Engineering - Process Manufacturing | SAP_BR_PRODN_ENG_PROC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure.

Material Master Data

| Data | Sample Value | Description | Other Attributes |
| --- | --- | --- | --- |
| Material | FG0504 | Sweets (Carton) | MTS processing for process industry with batch derivation |
| Material | SG0504 | Sweets (Bag) | Semifinished Product, batch managed |
| Material | RM0507 | Carton | Packaging material, no batch, external procurement |
| Material | SG0510 | Sweets (Bag) | Semifinished Product, batch managed |
| Material | SG0507 | Sweet Green | Semifinished Product, batch managed |
| Material | SG0508 | Sweet Red | Semifinished Product, batch managed |
| Material | SG0509 | Sweet Yellow | Semifinished Product, batch managed |
| Material | RM0509 | Viewing Window Bag | Raw material, batch managed |

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

BOM Alternative 01 – One-stage batch derivation

| Material | Level | Material Type | Unit | Characteristics of Material | Component Quantity | Component UOM |
| --- | --- | --- | --- | --- | --- | --- |
| FG0504 | 0 | FERT | PC | MTS processing for process industry with batch processing |  |  |
| RM0507 | 1 | ROH | PC | Packaging material, no batch, external procured |  |  |
| SG0504 | 1 | HALB | PC | Semifinished Product PI, batch managed |  |  |

BOM Alternative 02 – Two-stage batch derivation

| Material | Level | Material Type | Unit | Characteristics of Material | Component Quantity | Component UOM |
| --- | --- | --- | --- | --- | --- | --- |
| FG0504 | 0 | FERT | PC | MTS processing for process industry with batch processing |  |  |
| RM0507 | 1 | ROH | PC | Packaging material, no batch, external procured |  |  |
| SG0510 | 1 | HALB | PC | Semifinished Product PI, batch managed |  |  |
| SG0507 | 2 | HALB | PC | Semifinished Product PI, batch managed |  |  |
| SG0508 | 2 | HALB | PC | Semifinished Product PI, batch managed |  |  |
| SG0509 | 2 | HALB | PC | Semifinished Product PI, batch managed |  |  |
| RM0509 | 2 | ROH | PC | Raw material, batch managed |  |  |

Resource

| Resource | Plant | Resource Category | Resource Description |
| --- | --- | --- | --- |
| BS050003 | 3310 | 0008 | Packaging Line |
| BV050003 | 3310 | 0008 | Packaging Line 2 |

For more information on creating your own master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

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

Before this scope item can be tested, the following business condition must be met.

| Scope Item | Business Condition |
| --- | --- |
| BEG - Standard Cost Calculation | You have completed the step described in the Standard Cost Calculation (BEG) test script. |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS (BNZ) master data script. Posting Period is up to date. |
| J58 - Accounting and Financial Close | Execute to create open posting periods. |
| BLF - Batch Management | The settings must be available in the system. |

### SSCUIs

#### Maintain Number Range for Batch Derivation ID

Purpose

In this activity, you maintain number range for Batch Derivation ID.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Configure your solution | Select Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Filter Selection Criteria | Choose the following entries in filter bar and press Enter:Application Area: LogisticsSub Application Area: Batch Management | All entries display in All Items section. |  |
| 5 | Access SSCUI | Find the entry with item name Number Ranges for Batch Derivation and choose arrow at the item end. | The Configure Your Solution – Number Ranges for Batch Derivation screen displays. |  |
| 6 | Access SSCUI | In Configuration Steps section, choose Configure in column Actions for step Maintain Number Range for Batch Derivation ID – SSCUI 103730 and then Intervals. Finally, click on the icon Display <-> Change and choose Insert Line. | The Edit Intervals: Batch Derivation ID, Object DRVNO screen displays. |  |
| 7 | Maintain Settings and Save | Create a new entry, add the following information, click Enter and choose Save.Number Range No: 01From Number: 0000000001To Number: 9999999999 | The step Maintain Number Range for Batch Derivation ID is updated. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open General Business Data | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Maintain Number Range for Batch Derivation ID or SSCUI 103730.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Edit Intervals: Batch Derivation ID, Object DRVNO screen displays. |  |
| 3 | Maintain Settings and Save | Click on Edit Intervals and Choose Insert Line to create a new entry, add the following information, click Enter and choose Save.Number Range No: 01From Number: 0000000001To Number: 9999999999 | The step Maintain Number Range for Batch Derivation ID is updated. |  |

#### Maintain Number Range for Batch Derivation Condition Records

Purpose

In this activity, you maintain number range for Batch Derivation Condition Records. The Number ranges are set to ensure consistent identification of derivation objects and condition records.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Configure your solution | Select Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Filter Selection Criteria | Choose the following entries in filter bar and press Enter:Application Area: LogisticsSub Application Area: Batch Management | All entries display in All Items section. |  |
| 5 | Access SSCUI | Find the entry with item name Number Ranges for Batch Derivation and choose arrow at the item end. | The Configure Your Solution – Number Ranges for Batch Derivation screen displays. |  |
| 6 | Access SSCUI | In Configuration Steps section, choose Configure in column Actions for step Maintain Number Range for Batch Derivation Condition Records – SSCUI 103729 and then Intervals. Finally, click on the icon Display <-> Change and choose Insert Line. | The Edit Intervals: Batch Derivation, Object KONR screen displays. |  |
| 7 | Maintain Settings and Save | Create a new entry, add the following information, click Enter and choose Save.Number Range No: 01From Number: 0000000001To Number: 9999999999 | The step Maintain Number Range for Batch Derivation Condition Records is updated. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open General Business Data | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Maintain Number Range for Batch Derivation Condition Records or SSCUI 103729.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Edit Intervals: Batch Derivation, Object KONR screen displays. |  |
| 3 | Maintain Settings and Save | Click on Edit Intervals and Choose Insert Line to create a new entry, add the following information, click Enter and choose Save.Number Range No: 01From Number: 0000000001To Number: 9999999999 | The step Maintain Number Range for Batch Derivation Condition Records is updated. |  |

#### Define Access Sequences to Determine Sending Batches

Purpose

In this activity, you define access sequences to determine sending batches.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Configure your solution | Select Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Filter Selection Criteria | Choose the following entries in filter bar and press Enter:Application Area: LogisticsSub Application Area: Batch Management | All entries display in All Items section. |  |
| 5 | Access SSCUI | Find the entry with item name Determine Sending Batches in Batch Derivation and choose arrow at the item end. | The Configure Your Solution – Determine Sending Batches in Batch Derivation screen displays. |  |
| 6 | Access SSCUI | In Configuration Steps section, choose Configure in column Actions for step Define Access Sequences to Determine Sending Batches – SSCUI 103732. | The Change View Define Access Sequences to Determine Sending Batches: Display screen displays. |  |
| 7 | Maintain Settings and Save | Enter the following settings and choose Save.Access Sequences:Access SequenceDescriptionBDS1Sender Mat./ Receiver Mat.Accesses:No.TableDescription10012Receiving material + sending material20010Sender Material Number | The step Define Access Sequences to Determine Sending Batches is updated. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open General Business Data | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Access Sequences to determine Sending Batches or SSCUI 103732.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View Define Access Sequences to Determine Sending Batches: Display screen displays. |  |
| 3 | Maintain Settings and Save | Enter the following settings and choose Save.Access Sequences:Access SequenceDescriptionBDS1Sender Mat./ Receiver Mat.Accesses:No.TableDescription10012Receiving material + sending material20010Sender Material Number | The step Define Access Sequences to Determine Sending Batches is updated. |  |

#### Define Strategy Types to Determine Sending Batches

Purpose

In this activity, you define strategy types to determine sending batches.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Configure your solution | Select Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Filter Selection Criteria | Choose the following entries in filter bar and press Enter:Application Area: LogisticsSub Application Area: Batch Management | All entries display in All Items section. |  |
| 5 | Access SSCUI | Find the entry with item name Determine Sending Batches in Batch Derivation and choose arrow at the item end. | Configure Your Solution – Determine Sending Batches in Batch Derivation screen displays. |  |
| 6 | Access SSCUI | In Configuration Steps section, choose Configure in column Actions for step Define Strategy Types to Determine Sending Batches – SSCUI 103734. | “Define Strategy Types to Determine Sending Batches: Display“ screen displays. |  |
| 7 | Maintain Settings and Save | Choose New Entries, make the following entries and Save.Condition Types:Condition Type: Z05SDescription: Sender/Receiver Mat.Access Sequence: BDS1Description: Sender/Receiver Mat. | The step Define Strategy Types to Determine Sending Batches is updated. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open General Business Data | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Strategy Types to Determine Sending Batches or SSCUI 103734.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | “Define Strategy Types to Determine Sending Batches: Display“ screen displays. |  |
| 3 | Maintain Settings and Save | Choose New Entries, make the following entries and Save.Condition Types:Condition Type: Z05SDescription: Sender/Receiver Mat.Access Sequence: BDS1Description: Sender/Receiver Mat. | The step Define Strategy Types to Determine Sending Batches is updated. |  |

#### Define Search Procedures to Determine Sending Batches

Purpose

In this activity, you define search procedures to determine sending batches.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Configure your solution | Select Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Filter Selection Criteria | Choose the following entries in filter bar and press Enter:Application Area: LogisticsSub Application Area: Batch Management | All entries display in All Items section. |  |
| 5 | Access SSCUI | Find the entry with item name Determine Sending Batches in Batch Derivation and choose arrow at the item end. | Configure Your Solution – Determine Sending Batches in Batch Derivation screen displays. |  |
| 6 | Access SSCUI | In Configuration Steps section, choose Configure in column Actions for step Define Search Procedures to Determine Sending Batches – SSCUI 103736. | The “Define Search Procedures to Determine Sending Batches: Change“ screen displays. |  |
| 7 | Maintain Settings and Save | Choose New Entries, make the following settings and Save.Procedures:Procedure: Z05S01Description: Sender/Rec MaterialPress Enter. Select Procedure and double click Control data to follow below steps. Choose New Entries.Step: 1Counter: 1Condition Type: Z05SDescription: Sender/Rec Material | The step Define Search Procedures to Determine Sending Batches is updated. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open General Business Data | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Search Procedures to Determine Sending Batches or SSCUI 103736.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The “Define Search Procedures to Determine Sending Batches: Change“ screen displays. |  |
| 3 | Maintain Settings and Save | Choose New Entries, make the following settings and Save.Procedures:Procedure: Z05S01Description: Sender/Rec MaterialPress Enter. Select Procedure and double click Control data to follow below steps. Choose New Entries.Step: 1Counter: 1Condition Type: Z05SDescription: Sender/Rec Material | The step Define Search Procedures to Determine Sending Batches is updated. |  |

#### Define Access Sequences to Determine Receiving Batches

Purpose

In this activity, you define access sequences to determine receiving batches.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Configure your solution | Select Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Filter Selection Criteria | Choose the following entries in filter bar and press Enter:Application Area: LogisticsSub Application Area: Batch Management | All entries display in All Items section. |  |
| 5 | Access SSCUI | Find the entry with item name Determine Receiving Batches in Batch Derivation and choose arrow at the item end. | Configure Your Solution – Determine Receiving Batches in Batch Derivation screen displays. |  |
| 6 | Access SSCUI | In Configuration Steps section, choose Configure in column Actions for step Define Access Sequences to Determine Receiving Batches – SSCUI 103731. | The Change View Define Access Sequences to Determine Receiving Batches: Display screen displays. |  |
| 7 | Maintain Settings and Save | Enter the following settings and choose Save.Access Sequences:Access Sequence; Description: BDR1; MatNumber/MatTypeAccesses:No.; Table; Description: 10; 001; Material NumberNo.; Table; Description: 20; 002; Material Type | The step Define Access Sequences to Determine Receiving Batches is updated. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open General Business Data | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Access Sequences to determine receiving Batches or SSCUI 103731.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | Change View Define Access Sequences to Determine Receiving Batches: Display screen displays. |  |
| 3 | Maintain Settings and Save | Enter the following settings and choose Save.Access Sequences:Access Sequence; Description: BDR1; MatNumber/MatTypeAccesses:No.; Table; Description: 10; 001; Material NumberNo.; Table; Description: 20; 002; Material Type | The step Define Access Sequences to Determine Receiving Batches is updated. |  |

#### Define Strategy Types to Determine Receiving Batches

Purpose

In this activity, you define strategy types to determine receiving batches.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Configure your solution | Select Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Filter Selection Criteria | Choose the following entries in filter bar and press Enter:Application Area: LogisticsSub Application Area: Batch Management | All entries display in All Items section. |  |
| 5 | Access SSCUI | Find the entry with item name Determine Receiving Batches in Batch Derivation and choose arrow at the item end. | The Configure Your Solution – Determine Receiving Batches in Batch Derivation screen displays. |  |
| 6 | Access SSCUI | In Configuration Steps section, choose Configure in column Actions for step Define Strategy Types to Determine Receiving Batches – SSCUI 103733. | The Change View Define Strategy Types to Determine Receiving Batches: Change screen displays. |  |
| 7 | Maintain settings and save | Choose New Entries, make the following entries and Save:Condition Types:Condition Type: Z05RDescription: MatNumber / MatTypeAccess Sequence: BDR1Description: MatNumber / MatType | The step Define Strategy Types to Determine Receiving Batches is updated. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open General Business Data | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Strategy Types to Determine Receiving Batches or SSCUI 103733.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View Define Strategy Types to Determine Receiving Batches: Change screen displays. |  |
| 3 | Maintain settings and save | Choose New Entries, make the following entries and Save:Condition Types:Condition Type: Z05RDescription: MatNumber / MatTypeAccess Sequence: BDR1Description: MatNumber / MatType | The step Define Strategy Types to Determine Receiving Batches is updated. |  |

#### Define Search Procedures to Determine Receiving Batches

Purpose

In this activity, you define search procedures to determine receiving batches.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Configure your solution | Select Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Filter Selection Criteria | Choose the following entries in filter bar and press Enter:Application Area: LogisticsSub Application Area: Batch Management | All entries display in All Items section. |  |
| 5 | Access SSCUI | Find the entry with item name Determine Receiving Batches in Batch Derivation and choose arrow at the item end. | Configure Your Solution – Determine Receiving Batches in Batch Derivation screen displays. |  |
| 6 | Access SSCUI | In Configuration Steps section, choose Configure in column Actions for step Define Search Procedures to Determine Receiving Batches – SSCUI 103735. | The “Define Search Procedures to Determine Receiving Batches: Change“ screen displays. |  |
| 7 | Maintain Settings and Save | Choose New Entries, make the following settings and Save.Procedures:Procedure: Z05R01Description: MatNumber/MatTypePress Enter. Select Procedure and double click Control data to follow below steps. Choose New Entries.Step: 1Counter: 1Condition Type: Z05RDescription: MatNumber/MatType | The step Define Search Procedures to Determine Receiving Batches is updated. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open General Business Data | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Search Procedures to Determine Receiving Batches or SSCUI 103735.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The “Define Search Procedures to Determine Receiving Batches: Change“ screen displays. |  |
| 3 | Maintain Settings and Save | Choose New Entries, make the following settings and Save.Procedures:Procedure: Z05R01Description: MatNumber / MatTypePress Enter. Select Procedure and double click Control data to follow below steps. Choose New Entries.Step: 1Counter: 1Condition Type: Z05RDescription: MatNumber / MatType | The step Define Search Procedures to Determine Receiving Batches is updated. |  |

#### Define Derivation Event

Purpose

In this activity, you define Derivation Event.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Configure your solution | Select Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Filter Selection Criteria | Choose the following entries in filter bar and press Enter:Application Area: LogisticsSub Application Area: Batch Management | All entries display in All Items section. |  |
| 5 | Access SSCUI | Find the entry with item name Further Settings for Batch Derivation screen and choose arrow at the item end. | The Configure Your Solution – Further Settings for Batch Derivation screen displays. |  |
| 6 | Access SSCUI | In Configuration Steps section, choose Configure in column Actions for step Define Derivation Events – SSCUI 103728. | The “Define Derivation Events: Display“ screen displays. |  |
| 7 | Maintain Settings and Save | Choose New Entries, enter the following settings and choose Save.First EntryDerivation Event: Goods Receipt for Process/ Production OrderReceiver Procedure: Z05R01Sender Procedure: Z05S01Derivation Type: StaticDialog Control: Always HideSecond EntryDerivation Event: Manual DerivationReceiver Procedure: Z05R01Sender Procedure: Z05S01Derivation Type: StaticDialog Control: Display when "Errors" | The step Define Derivation Events is updated. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open General Business Data | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Derivation Events or SSCUI 103738.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The “Define Derivation Events: Display“ screen displays. |  |
| 3 | Maintain Settings and Save | Choose New Entries, enter the following settings and choose Save.First EntryDerivation Event: Goods Receipt for Process/ Production OrderReceiver Procedure: Z05R01Sender Procedure: Z05S01Derivation Type: StaticDialog Control: Always HideSecond EntryDerivation Event: Manual DerivationReceiver Procedure: Z05R01Sender Procedure: Z05S01Derivation Type: StaticDialog Control: Display when "Errors" | The step Define Derivation Events is updated. |  |

### Preliminary Steps

#### Manage Derivation Strategies – Sender

Purpose

This step is to define rules for batch derivation. For each derivation strategy, you can specify the conditions under which batch derivation is to be triggered and which batch attribute is derived. These conditions are referred to as condition records.

|  |
| --- |
| Note This step needs to be executed only the first time you run through the scenario. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as a Master Data Specialist - Batch Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Derivation Strategies - Sender (DVS2). | Derivation - Change Search Strategy: Initial screen is displayed. |  |
| 3 | Choose Strategy type | Make the following entries and choose Change:Strategy Type: Z05SChoose Key Combination Receiving material + sending material on the popup and press Choose. | Change Sender/Receiver (Z05S): Selection screen is displayed. |  |
| 4 | Choose Receiver Material | Make following settings and choose Execute:Receiver Material: FG0504 | Change Sender/Receiver (Z05S): Fast Entry screen is displayed. |  |
| 5 | Choose Sender Material | Choose button Create.Make following settings, select entry created, and choose button Details:Sender Material: SG0504Press Enter and choose button Details.In the Send Attributes table make the following settings:Attribute: HSDAT |  |  |
| 6 | Save your entries | Choose button Save. | The batch derivation strategy for sending materials is saved. |  |
| 7 | Repeat Steps | Repeat steps 3 to 6 and exchange Sender Material with following values:Sender Material: SG0507Sender Material: SG0508Sender Material: SG0509 |  |  |

#### Manage Derivation Strategies – Receiver

Purpose

This step is to define rules for batch derivation. For each derivation strategy, you can specify the conditions under which batch derivation is to be triggered and which batch attribute is derived. These conditions are referred to as condition records

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Batch Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Derivation Strategies - Receiver (DVR2). | Derivation - Change Search Strategy: Initial screen is displayed. |  |
| 3 | Choose Strategy type | Make the following entries and choose Change:Strategy Type: Z05RChoose Key Combination Material Number on the Pop up and press Choose. | Change MatNumber / MatT (Z05R): Selection screen is displayed. |  |
| 4 | Choose Receiver Material | Make following settings and choose Execute:Receiver Material: FG0504 | Change MatNumber / MatT (Z05R): Fast Entry screen is displayed. |  |
| 5 | Choose Receiver Material Settings | Chosse button Create.Make following settings, select entry created and choose button Details:Receiver Material: FG0504Press Enter and choose button Details.In the Attributes table make the following settings:Attribute: HSDATMark the Entry and choose tab Rules.In the Rules for Controlling Derivation section, make the following settings:Sender Field Empty: WarningLevels in Batch Where-Used List: 2In the Rules for Value Selection if more than one Sender section, choose the following setting:Comparative: Minimum |  |  |
| 6 | Save your entries | Choose button Save. | The batch derivation strategy for receiving materials is saved. |  |

#### Create Initial Material Stock

Purpose

In a real business case, the raw materials are usually purchased from external vendors that can be covered by the standard purchasing processing. This process step shows you how to directly post initial stock to the storage location.

|  |
| --- |
| Note You can either post initial stock directly to the storage location or referring to the process of Procurement of Direct Materials (J45) or Scheduling Agreements in Procurement (BMR). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | Screen name adapts accordingly. |  |
| 3 | Choose Goods Receipt-Other | Make the following entries and choose Enter:Trans./Event: Goods ReceiptReference Document: OtherMovement Type: 561 | Screen name adapts after entries are made. |  |
| 4 | Specify Material | On the Material tab, make the following entries:Material: SG0504 | Ensure that detail data is expanded. |  |
| 5 | Specify Quantity | On the Quantity tab, make the following entries:Qty in Unit of Entry: 4000 |  |  |
| 6 | Specify Plant and Storage Location | On the Where tab, make the following entries:Plant: 3310Storage Location: 331B |  |  |
| 7 | Check Item | Press Enter, and ensure Item OK is selected. |  |  |
| 8 | Batch | Choose Tab Batch and make following entries:Batch Number: <Batch Number 1>Date of Manufacture: <Today´s Date> |  |  |
| 9 | Add Other Materials | Choose Next Item, then repeat the steps 4 to 8 for the following data (all other data remain the same than mentioned above):Data set 2:Material: RM0507Plant: 3310Storage Location: 331CQty in Unit of Entry: 10000Note Data sets 3-6 are needed only for two-stage batch derivation processData set 3:Material: SG0507Plant: 3310Storage Location: 331CQty in Unit of Entry: 4000Batch: <Batch Number> (optional)Date of Manufacturing: <current date – 1 week>Data set 4:Material: SG0508Plant: 3310Storage Location: 331CQty in Unit of Entry: 4000Batch: <Batch Number> (optional)Date of Manufacturing: <current date – 2 weeks>Data set 5:Material: SG0509Plant: 3310Storage Location: 331CQty in Unit of Entry: 4000Batch: <Batch Number> (optional)Date of Manufacturing: <current date – 2 weeks>Data set 6:Material: RM0509Plant: 3310Storage Location: 331CQty in Unit of Entry: 4000Batch: <Batch Number> (optional)Date of Manufacturing: <current date – 1 week> |  |  |
| 10 | Post Goods Movement | Choose Post. | Material document XXX is posted and materials are available in stock. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the home page will only contain the essential apps for performing the typical tasks of a business role.

You can find all other apps not included on the home page using the search bar.

If you want to personalize the home page and include the hidden apps, navigate to your user profile and choose Settings > App Finder .

| Process Step | Business Role | Transaction/App | Expected Output |
| --- | --- | --- | --- |
| Make Decision to run One or Two Level Batch Derivation |  |  |  |
| [Manage Production Versions](#unique_20) [page ] 33 | Production Engineer - Process Manufacturing | Manage Production Versions - C223 (C223) | Production Versions are maintained. |
| Anonymous Forecast and MRP (One- and Two-Stage Batch Derivation) |  |  |  |
| [Create Planned Independent Requirements](#unique_21) [page ] 34 | Production Planner | Maintain PIRs (F3445) | Independent Requirements for Finished Goods are created. |
| [Material Requirements Planning at Plant Level](#unique_22) [page ] 36 | Production Planner | Schedule MRP Runs (F1339) | Planned Independent Requirements for Finished Materials and also the components are planned. |
| [Evaluate Stock/Requirements Situation](#unique_23) [page ] 38 | Production Planner | Monitor Material Coverage - Net / Individual Segments (F2101A) | Stock/Requirements situation for the planned materials is analyzed. |
| One-Level Batch Derivation |  |  |  |
| Process Order Creation and Processing for Finished Material |  |  |  |
| Create Process Order |  |  |  |
| Create Process Order - [Option 1: Convert Planned Order to Process Orders](#unique_24) [page ] 40 | Production Planner | Manage Material Coverage - New Version (F0251A) | A process order is created. |
| Create Process Order - [Option 2: Create Process Order Manually](#unique_25) [page ] 41 | Production Supervisor - Process Manufacturing | Create Process Order (COR1) | A process order is created. |
| [Review Process Order](#unique_26) [page ] 42 | Production Supervisor - Process Manufacturing | Display Process Order (COR3) | A process order is reviewed. |
| [Post Goods Issue of Batch Managed Components](#unique_27) | Warehouse Clerk | Post Goods Movement (MIGO) | The goods issue of batch managed components is executed. |
| [Monitor Order Progress (Optional)](#unique_28) [page ] 45 | Production Supervisor - Process Manufacturing | Manage Process Orders (F4587) | The order progress is reviewed. |
| [Confirm Production incl. Component Backflush](#unique_29) [page ] 47 | Production Operator - Process Manufacturing | Confirm Process Order Phase (COR6N) | The production order is confirmed and the goods receipt of non batch managed components is posted. |
| [Post Goods Receipt for Process Order](#unique_30) [page ] 48 | Warehouse Clerk | Post Goods Receipt for Process Order (F6352) | Goods receipt is posted for Process Order. |
| [Review Process Order Confirmation](#unique_31) [page ] 50 | Production Supervisor - Process Manufacturing | Manage Process Orders (F4587) | Confirmations of process order is reviewed. |
| Two-Level Batch Derivation |  |  |  |
| Process Order Creation and Processing for Semi finished Material |  |  |  |
| Create Process Order |  |  |  |
| [Option 1: Convert Planned Order to Process Orders](#unique_32) [page ] 52 | Production Planner | Manage Material Coverage - New Version (F0251A) | A Process Order is created. |
| [Option 2: Create Process Order Manually](#unique_33) [page ] 53 | Production Supervisor - Process Manufacturing | Create Process Order (COR1) | A process order is created. |
| [Review Process Order](#unique_34) [page ] 55 | Production Supervisor - Process Manufacturing | Display Process Order (COR3) | A process order is reviewed. |
| [Post Goods Issue of Batch Managed Components](#unique_35) [page ] 57 | Warehouse Clerk | Post Goods Movement (MIGO) | The goods issue of batch managed components is executed. |
| [Monitor Order Progress (Optional)](#unique_36) [page ] 58 | Production Supervisor - Process Manufacturing | Manage Process Orders (F4587) | The order progress is reviewed. |
| [Confirm Production and Post Goods Receipt](#unique_37) [page ] 60 | Production Operator - Process Manufacturing | Confirm Process Order Phase (COR6N) | The production order is confirmed and the goods receipt of non batch managed components is posted. |
| Process Order Creation and Processing for Finished Material |  |  |  |
| Create Process Order |  |  |  |
| [Option 1: Convert Planned Order to Process Orders](#unique_38) [page ] 61 | Production Planner | Manage Material Coverage - New Version (F0251A) | A process order is created. |
| [Option 2: Create Process Order Manually](#unique_39) [page ] 62 | Production Supervisor - Process Manufacturing | Create Process Order (COR1) | A process order is created. |
| [Review Process Order](#unique_40) [page ] 64 | Production Supervisor - Process Manufacturing | Display Process Order (COR3) | A process order is reviewed. |
| [Post Goods Issue of Batch Managed Components](#unique_41) [page ] 66 | Warehouse Clerk | Post Goods Movement (MIGO) | The goods issue of batch managed components is executed. |
| [Monitor Order Progress (Optional)](#unique_42) [page ] 67 | Production Supervisor - Process Manufacturing | Manage Process Orders (F4587) | The order progress is reviewed. |
| [Confirm Production incl. Component Backflush](#unique_43) [page ] 69 | Production Operator - Process Manufacturing | Confirm Process Order Phase (COR6N) | The production order is confirmed and the goods receipt of non batch managed components is posted. |
| [Post Goods Receipt for Process Order](#unique_44) [page ] 70 | Warehouse Clerk | Post Goods Receipt for Process Order (F6352) | Goods receipt is posted for Process Order. |
| [Review Process Order Confirmation](#unique_45) [page ] 71 | Production Supervisor - Process Manufacturing | Manage Process Orders (F4587) | Confirmations of process order is reviewed. |
| [Monitor Batch Derivation](#unique_46) [page ] 73 | Master Data Specialist - Batch Data | Monitor Derivation (DVMO) | The automatic batch derivation is monitored. |
| [Batch Information Cockpit - Top-Down and Bottom-Up Analysis](#unique_47) [page ] 74 | Quality Technician | Batch Information Cockpit (BMBC) | A batch analysis is performed. |

## Test Procedures

### Make Decision to run One- or Two-Level Batch Derivation

The batch derivation can be realized as one-level or multi-level batch derivation. The test script provides according to the selected set of master data the possibility to run an one- or two-level process.

The selection of the corresponding set of master data is realized via production versions. As an alternative, production orders can be created manually.

#### Manage Production Versions

Purpose

For the finished good two alternative production versions are available in the system. One of them should be used for automatic sourcing during MRP run, the other one can only be selected manually.

For one-level batch derivation, the production version 0001 is relevant for automatic sourcing, for the two-level batch derivation the production version 0002.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as a Production Engineer - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Production Versions - C223 (C223). | Production Version: Mass Processing screen is displayed |  |
| 3 | Select Production Version | Make the following entries for the selection conditions and choose Continue:Plant: 3310Material: FG0504 | Production Versions are displayed. |  |
| 4 | Adopt Production Version | For one-level batch derivation make the following settings:For production version 0001 open the selection for field Lock and choose Not LockedProduction version 0002 open the selection for field Lock and choose Locked for automatic sourcing or Not Locked.For two-level batch derivation make the following settings:For production version 0001 open the selection for field Lock and choose Locked for automatic sourcing.For production version 0002 open the selection for field Lock and choose Not Locked . |  |  |
| 5 | Save your entries | Press Enter. On the Pop Up New Selection of Production Version choose button Yes to save your entry. |  |  |

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
| 4 | Select Material Items | On the Maintain PIRs screen, make the following entries and choose Go:Plant: 3310Period Indicator: Weekly(W)Version Active: Select all optionsMaterial: FG0504 | The searched material item displays. If the material filter is not directly available choose Adapt Filters, select the Material Filter, enter the desired material and choose OK.Note If no PIRs for FG0504 have been maintained in the system before, the selection is empty in the app. In that case please leave this app and access the app Create PIRs (MD61), make the following entries on the Create Planned Independent Requirements: Initial Screen and choose Continue:Plant: 3310Period Indicator: Weekly (W)Version: 00Material: FG0504Choose Save and restart with step 1. |  |
| 5 | Edit PIRs | Select the material item and choose Edit in the upper right corner of the screen.On the Edit PIRs screen, enter quantities per week, for example:Week 1 (current week + 1 week): 30 PCWeek 2 (current week + 2 weeks): 40 PCWeek 3 (current week + 3 weeks): 50 PCWeek 4 (current week + 4 weeks): 20 PCWeek 5 (current week + 5 weeks): 10 PCWeek 6 (current week + 6 weeks): 60 PCVersion is Active: YES | Note If already stock for FG0504 is available, increase the quantity for PIR of current week + 1 for the stock already available. As an alternative, remove the stock to get planned orders in next step. |  |
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

The Make-to-Stock finished goods are planned at plant level. There is now a requirement for FG0504 in plant 3310.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Planner. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Schedule MRP Runs (F1339). | The Schedule MRP Runs screen displays. |  |
| 3 | Create New Job | Choose Create.On the New Job screen, make the following entries:For 1. Template Selection section:Job Template: Material Requirements Planning (MRP)Job Name: MRP for FG0504Choose Step 2.For 2. Scheduling Options section:Start Immediately: <select>Choose Define Recurrence Pattern.On the Scheduling Information screen, make the following entries:Start Immediately: XRecurrence Pattern: Single RunChoose OK.Choose Step 3.For 3. Parameters section:Plant: 3310Material: FG0504Changed BOM Components: selectStock Transfer Materials: selectScheduling: 2Planning Mode: 1Choose Check at the bottom right.Choose Schedule. | A message appears: You can go ahead and schedule the job. |  |
| 4 | Refresh Application Jobs List | To check the job’s status, enter MRP for FG0504 in the search box and choose Go at the top right section of the screen. | The new job is created and is displayed in the Application Jobs table when refreshed. |  |

#### Evaluate Stock/Requirements Situation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display the stock/requirements situation for Make-to-Stock finished goods FG0504 and the components relevant for production (finished, packaging and raw materials) in the stock/requirements list after the requirement planning is performed.

Prerequisite

Requirement planning is carried out.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). | The Monitor Material Coverage - Net / Individual Segments (F2101A) screen displays. |  |
| 3 | Check Area of Responsibility (Optional) | Choose the user icon and select App Settings. In the MRP Settings dialog box, choose Area of Responsibility.Check if only this entry displays, and choose OK:Plant 1 AE 3310MRP Controller (001)Choose + to select this entry if not displayed; choose the Delete icon to remove any other plant entries and then choose OK. |  |  |
| 4 | Select Material | Search in the Material bar, select the following materials and then choose Go.Material: FG0504Material: SG0504Material: RM0507For two-stage batch derivation please select as well:Material: SG0510Material: RM0509Material: SG0507Material: SG0508Material: SG0509 | The Material and Material Details screens display. |  |
| 5 | Review Stock / Requirements List | Select the following materials on the Material screen and choose Manage Materials.Material: FG0504 | The detailed stock / requirements list for each material displays. |  |
| 6 | Display Planned Order | From the list on the Material sub screen, check the planned order of the material FG0504.On the Material Details sub screen, choose PldOrd XXX in the MRP Element column.Note The BOM explosion during the MRP run has generated dependent requirements for the demand-driven planned components. If there is not enough inventory to fulfill the requirements, planned orders and purchase requisitions are created for both in house-produced and externally-procured materials. | The selected planned order displays.Note The planned order is generated only when there is storage for these materials.If you want to display more information of the planned order, choose Open... > Planned Order at the bottom right of the dialog box. |  |
| 7 | Display Stock situation of Semifinished and Packaging Materials | Return to the Materials Overview screen, select following materials and choose Manage MaterialsMaterial: SG0504Material: RM0507For two-stage batch derivation please select:Material: SG0510Material: RM0507Material: RM0509Material: SG0507Material: SG0508Material: SG0509 |  |  |

### One-level Batch Derivation

If you choose one-level batch derivation in chapter Make Decision for One- or Two-Level Batch Derivation, please continue with this section. If you choose two-level batch derivation, skip this section and continue with Section Two-Level Batch Derivation.

#### Process Order Creation and Processing for Finished Material

##### Create Process Order

###### Option 1: Convert Planned Order to Process Orders

Purpose

Daily MRP run creates planned orders for goods to be produced internally. This process step shows you how to convert the planned orders to process orders for finished materials when reached the planned start date.

Prerequisite

The MRP run has generated planned orders for FG0504 (finished material).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Material Coverage - New Version (F0251A). | The Manage Material Coverage screen displays. |  |
| 3 | Select Material | On the Manage Material Coverage screen, enter the following data and choose GO.Material: FG0504Plant: 3310Shortage Definition: MRP Standard | The Manage Material Coverage screen displays. |  |
| 4 | Find Planned Order | Check the generated planned orders.If no planned orders are generated, it could be because FG0504 has sufficient amount of stock in store. In this case, remove some stock or enhance the amount for PIRs for FG0504 and run MRP again to generate planned orders. |  |  |
| 5 | Add Planned Order Long Text (Optional) | Click on the planned order number (PldOrd XXXX) under column MRP Element. In the pop-up dialog PldOrd XXXX, choose Open and then choose Planned Order in the resulting pop-up.On the Change Planned Order screen, check the field Production Version is 0001.On the Change Planned Order screen, choose tab Long Text, enter the text, and choose Save. | The long text maintained here can be later copied to the converted process order. |  |
| 6 | Convert Planned Order to Process Order | Select Convert from Edit dropdown list in the Actions column for a planned order (PldOrd XXX).In the Convert Planned Order XXX dialog box, choose Convert to Process Order, confirm Delivery Date and Quantity. Choose Convert.Choose the Refresh button on the top of the material overview section, scroll to the created process order and note down the process order number for material FG0504. | The process order is created.Process Order Number ___________________. |  |

###### Option 2: Create Process Order Manually

Purpose

This process step shows you how to create process orders with status created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Process Manufacturing . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Process Order (COR1). | The Create Process Order: Initial Screen displays. |  |
| 3 | Enter Restriction | Make the following entries and choose Continue:Material Number: FG0504Production Plant: 3310Process Order Type: YBM2 | The system displays a list of all planned orders, which match the restriction. |  |
| 4 | Create Process Order: Header - General Data | Make the following entries and choose Save:Total QTY: <your quantity>Start : <today>End : <today plus 1 week> |  |  |
| 5 | Validate Control Key | Choose Operations.Make sure, that the YPI1 entry is maintained in the Control Key field for all phases and sub phases.Choose Back. |  |  |
| 6 | Validate Production Version | Choose Master Data.Check the production Version. The production version must be 0001 for one-stage batch derivation.To switch choose the button next to the production version and choose cont. on the pop-up. Change the entry for production version in the next pop up and choose Continue. Confirm the information pop up. |  |  |
| 7 | Save your order | Choose Save. | Process order is created.Make a note of the process order number. |  |

##### Review Process Order

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
| 3 | Select AOR | If this is your first time to access the app, a welcome page would appear asking you to select your area of responsibility.Otherwise, choose your user name and the App Settings icon.On the Area of Responsibility - Production Supervisor screen, choose Production Supervisor.Choose Add or Delete to add or remove entries, and make sure following entry displays:Plant 1 AE/ MTS PI valuated (YB2) |  |  |
| 4 | Choose the Process Order | In the process order list, find your process order and choose it.Process Order: XXXX (from previous steps) | Note In the header area, you can switch between Compact Filter and Visual Filter, to find a proper way to search for your process order number. |  |
| 5 | Review Process Order | In the detailed page of the process order, review relevant information. |  |  |
| 6 | Check Long Text Copied from Planned Order (Optional) | If any long text is maintained for the planned order, you can check it in the converted process order.Choose Edit Order in the upper right corner.On the Change Process Order: Header screen, choose icon Change Long Text next to Process Order number, and check the text. | The long text maintained in the planned order is copied to the converted process order. |  |

##### Post Goods Issue of Batch Managed Components

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The withdrawal of the raw materials is used for the process order. This withdrawal can be done by using the picking list or doing a manual goods issue.

|  |
| --- |
| Note If the material is set for backflush (in material master or resource), the withdrawing is done automatically after you confirm the operation or the whole order. Backflushing should not be used for batch-managed components (to ensure that the physically picked and consumed batch is the same as the recorded batch). |

Prerequisites

Ensure that sufficient material is present on stock. You can check the stock levels using the app Monitor Stock / Requirements List - Old Version (MD04) available for the Production Planner role.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Initial screen displays. |  |
| 3 | Enter Process Order | Make the following entries and then press Enter:Trans./Event: Goods IssueReference Document: OrderOrder number: XXXX (from previous steps)Movement Type: 261 | The screen name adapts after entries are made. |  |
| 4 | Check Each Item | For each item displays, select Item OK. | Note Ensure that detail data is expanded. |  |
| 5 | Perform Batch Determination | Choose tab Quantity and button Stock Determ. | The Batch Determination MM: Select Batches screen displays. |  |
| 6 | Copy Batch Determination Result | Add quantities to the required batches and choose Copy. | The Goods Issue Order XXXX screen displays. In addition, the batch numbers have been determined.If you selected more that one batch, additional lines are created. |  |
| 7 | Post Goods Movements | Choose Post. | The goods movements have been posted. |  |

##### Monitor Order Progress (Optional)

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

##### Confirm Production incl. Component Backflush

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
| 3 | Enter Confirmation Option | Make the following entries and then choose Enter.Order: XXXX (from previous stepsPhase: 0020Confirm.type: Final confirmationClear open reservations: X | Note If the system shows the message Total quantity confirmed not equal to planned quantity to be confirmed, press Enter to ignore it. |  |
| 4 | Propose Actual Data | Choose Actual Data.Make the changes for the following fields:Scrap: <enter the amount you want to scrap>Yield: <Based on the origin quantities minus scrap>Reason for Var: < Enter scrap reason if needed>, for example, 0001 | The Quantities and Activities will be filed automatically.If you want to check your backflushed components (required for material FG0504), continue with step 5 of this table. Else proceed directly with step 6. |  |
| 5 | Check Backflushed Components | Choose Goods Movements. | The Enter Confirmation for Production Order: Goods Movement screen displays. Check the material entries and quantities.The final confirmation of the last operation has been carried out. Backflushed components are issued with the confirmation posting automatically (packaging material RM0507 within the confirmation of orders for Finished Product PI FG0504). |  |
| 6 | Save Confirmation | Click Post. | The final confirmation of the last operation is carried out. Costs and activity quantities are recalculated in proportion to the yield quantity. |  |

##### Post Goods Receipt for Process Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to post the goods receipt for the process order. You may post goods receipt for the total quantity, but usually already partial quantities of the products are required for further processing, such as consumption for further production or subsequent deliveries for sales orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as Warehouse Clerk. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Initial screen displays. |  |
| 3 | Enter Process Order | Make the following entries and then press Enter:Trans./Event: Goods ReceiptReference Document: OrderOrder number: XXXX (from previous steps)Movement Type: 101 | Screen name adapts after entries are made. |  |
| 4 | Enter Date of Manufacture | Choose the Batch tab and enter a batch number (optional). Do not enter a production date and choose enter.Note The production date is filled automatically due to derivation rules assigned to the material. |  |  |
| 5 | Check Item | Select item OK. | Ensure that detail data is expanded. |  |
| 6 | Post Goods Movement | Choose Post. | The goods movements are posted. The batch number is created automatically during the posting. Production date and shelf life expiration date are recorded within the batch master of the finished product. |  |

##### Review Process Order Confirmation

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
| 3 | Select AOR | If this is your first time to access the app, a welcome page would appear asking you to select your area of responsibility.Otherwise, choose your user name and the App Settings icon.On the Area of Responsibility screen, choose Production Supervisor.Choose Add or Delete to add or remove entries, and make sure following entry displays:Plant 1 AE/ MTS PI valuated (YB2) |  |  |
| 4 | Choose the Process Order | In the process order list, find your process order and choose it.Process Order: XXXX (from previous steps) | In the header area, you can switch between Compact Filter and Visual Filter, to find a proper way to search for your process order number. |  |
| 5 | Review Process Order | In the detailed page of the process order, review conformations of the process order. |  |  |

Option 2:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Process Order Confirmation (CORT). | The Display Process Order Confirmation: Initial screen displays. |  |
| 3 | Enter Process Order | Make the following entries and then choose Enter.Process Order: XXXX (from previous steps) | The Process Order Confirmation Display: Details screen displays.Confirmations are reviewed and checked within your responsibility area. |  |

Option 3:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Process Order Operations (F5323). |  |  |
| 3 | Choose Filter Style | In the header part, you can switch between Compact Filter and Visual Filter, which provides you different styles for filter. |  |  |
| 4 | Enter Process Order Number | Choose Compact Filter, make the following entries and choose Go.Process Order: XXXX (from previous steps) | Operation list displays. |  |

### Two-Level Batch Derivation

If you choose two-level batch derivation in chapter Make Decision for One- or Two-Level Batch Derivation, please continue with this section.

|  |
| --- |
|  |

You must have skipped previous section One-Level Batch Derivation

#### Process Order Creation and Processing for Seminfinished Material

##### Create Process Order

###### Option 1: Convert Planned Order to Process Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Daily MRP run creates planned orders for goods to be produced internally. This process step shows you how to convert the planned orders to process orders for semifinished materials when reached the planned start date.

Prerequisite

The MRP run has generated planned orders for SG0510 (semifinished material).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Material Coverage - New Version (F0251A). | The Manage Material Coverage screen displays. |  |
| 3 | Select Material | On the Manage Material Coverage screen, enter the following data and choose GO.Material: SG0510Plant: 3310Shortage Definition: MRP Standard | The Manage Material Coverage screen displays with more details. |  |
| 4 | Find Planned Order | Check the generated planned orders.If no planned orders are generated, it could be because SG0510 has sufficient amount of stock in store. In this case, remove some stock or enhance the amount for PIRs for FG0504 and run MRP again to generate planned orders. |  |  |
| 5 | Add Planned Order Long Text (Optional) | Click on the planned order number (PldOrd XXXX) under column MRP Element. In the pop-up dialog PldOrd XXXX, choose Open... and then choose Planned Order in the resulting pop-up.On the Change Planned Order screen, check if the field Production Version is 0001 .On the Change Planned Order screen, choose tab Long Text, enter the text, and choose Save. | The long text maintained here can be later copied to the converted process order. |  |
| 6 | Convert Planned Order to Process Order | Select Convert from Edit dropdown list in the Actions column for a planned order (PldOrd XXX).In the Convert Planned Order XXX dialog box, choose Convert to Process Order, confirm Delivery Date and Quantity. Choose Convert.Choose the Refresh button on the top of the material overview section, scroll to the created process order and note down the process order number for material SG0510. | The process order is created.Process Order Number ___________________. |  |

###### Option 2: Create Process Order Manually

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
| 3 | Enter Restriction | Make the following entries and choose Continue:Material Number: SG0510Production Plant: 3310Process Order Type: YBM2 |  |  |
| 4 | Create Process Order: Header - General Data | Make the following entries and press Enter:Total QTY: <your quantity>Start : <today>End : <today plus 1 week> |  |  |
| 5 | Validate Control Key | Choose Operations.Make sure, that the YBP3 entry is maintained in the Control Key field for phase 0020.Choose Back. |  |  |
| 6 | Save your order | Choose Save. | Process order is created.Make a note of the process order number _______________________. |  |

##### Review Process Order

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
| 3 | Select AOR | If this is your first time to access the app, a welcome page would appear asking you to select your area of responsibility.Otherwise, choose your user name and the App Settings icon.On the Area of Responsibility - Production Supervisor screen, choose Production Supervisor.Choose Add or Delete to add or remove entries, and make sure following entry displays:Plant 1 AE/ MTS PI valuated (YB2) |  |  |
| 4 | Choose the Process Order | In the process order list, find your process order and choose it.Process Order: XXXX (from previous steps) | Note In the header area, you can switch between Compact Filter and Visual Filter, to find a proper way to search for your process order number. |  |
| 5 | Review Process Order | In the detailed page of the process order, review relevant information. |  |  |
| 6 | Check Long Text Copied from Planned Order (Optional) | If any long text is maintained for the planned order, you can check it in the converted process order.Choose Edit Order in the upper right corner.On the Change Process Order: Header screen, choose icon Change Long Text next to Process Order number, and check the text. | The long text maintained in the planned order is copied to the converted process order. |  |

##### Post Goods Issue of Batch Managed Components

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The withdrawal of the raw materials is used for the process order. This withdrawal can be done by using the picking list or doing a manual goods issue.

|  |
| --- |
| Note If the material is set for backflush (in material master or resource), the withdrawing is done automatically after you confirm the operation or the whole order. Backflushing should not be used for batch-managed components (to ensure that the physically picked and consumed batch is the same as the recorded batch). |

Prerequisites

Ensure that sufficient material is present on stock. You can check the stock levels using the app Monitor Stock / Requirements List - Old Version (MD04) available for the Production Planner role.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Initial screen displays. |  |
| 3 | Enter Process Order | Make the following entries and then press Enter:Trans./Event: Goods IssueReference Document: OrderOrder number: XXXX (from previous steps)Movement Type: 261 | The screen name adapts after entries are made. |  |
| 4 | Check Each Item | For each item displays, select Item OK. | Note Ensure that detail data is expanded. |  |
| 5 | Perform Batch Determination | Choose tab Quantity and button Stock Determ. | The Batch Determination MM: Select Batches screen displays. |  |
| 6 | Copy Batch Determination Result | Add quantities to the required batches and choose Copy. | The Goods Issue Order XXXX screen displays. In addition, the batch numbers have been determined.If you selected more that one batch, additional lines are created. |  |
| 7 | Post Goods Movements | Choose Post. | The goods movements have been posted. |  |

##### Monitor Order Progress (Optional)

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

##### Confirm Production and Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The confirmation documents include the processing status of order, operations, phases and individual capacities. It is an instrument to control the order. The time ticket confirmation allows recording either the default times for machine and labor usage, or actual times for major deviations. Back flushed materials will be posted automatically during respective phase confirmations. This process step shows you how to confirm production. You can post scrap quantities as an optional. If no major deviations occurred, only the last phase (milestone) must be confirmed. Using milestone confirmation, all prior phases are confirmed automatically.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Confirm Process Order Phase (COR6N). | The Enter Time Ticket for Process Order screen displays. |  |
| 3 | Enter Confirmation Option | Make the following entries and then choose Enter.Order: XXXX (from previous steps)Phase: 0020Confirm.type: Final confirmationClear open reservations: X | If the system shows the message Total quantity confirmed not equal to planned quantity to be confirmed, press Enter to ignore it. |  |
| 4 | Propose Actual Data | Choose Actual Data.Make the changes for the following fields:Scrap: <enter the amount you want to scrap>Yield: <Based on the origin quantities minus scrap>Reason for Var: < Enter scrap reason if needed>, for example, 0001 | The Quantities and Activities will be filled automatically.If you want to check your back flushed components (required for material SG0510), continue with step 5 of this table. Else proceed directly with step 6. |  |
| 5 | Check Semi -finished Material | Choose Goods Movements.On the Pop up enter the production date (today) in the field Expiry date/Manu.date and choose Enter.The Enter Confirmation for Production Order: Goods Movement screen displays. Check the material entry and quantity.Enter a batch number (optional). |  |  |
| 6 | Save Confirmation | Click Post. | The final confirmation of the last operation has been carried out. The goods receipt of the semi-finished material is posted. Costs and activity quantities are recalculated in proportion to the yield quantity. |  |

#### Process Order Creation and Processing for Finished Material

##### Create Process Order

###### Option 1: Convert Planned Order to Process Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Daily MRP run creates planned orders for goods to be produced internally. This process step shows you how to convert the planned orders to process orders for finished materials when reached the planned start date.

Prerequisite

The MRP run has generated planned orders for FG0504 (finished material).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Material Coverage - New Version (F0251A). | The Manage Material Coverage screen displays. |  |
| 3 | Select Material | On the Manage Material Coverage screen, enter the following data and choose GO.Material: FG0504Plant: 3310Shortage Definition: MRP Standard | The Manage Material Coverage screen displays. |  |
| 4 | Find Planned Order | Check the generated planned orders.If no planned orders are generated, it could be because FG0504 has sufficient amount of stock in store. In this case, remove some stock or enhance the amount for PIRs for FG0504 and run MRP again to generate planned orders. |  |  |
| 5 | Add Planned Order Long Text (Optional) | Click on the planned order number (PldOrd XXXX) under column MRP Element. In the pop-up dialog PldOrd XXXX, choose Open and then choose Planned Order in the resulting pop-up.On the Change Planned Order screen, check the field Production Version is 0002.On the Change Planned Order screen, choose tab Long Text, enter the text, and choose Save. | The long text maintained here can be later copied to the converted process order. |  |
| 6 | Convert Planned Order to Process Order | Select Convert from Edit dropdown list in the Actions column for a planned order (PldOrd XXX).In the Convert Planned Order XXX dialog box, choose Convert to Process Order, confirm Delivery Date and Quantity. Choose Convert.Choose the Refresh button on the top of the material overview section, scroll to the created process order and note down the process order number for material FG0504. | The process order is created.Process Order Number ___________________. |  |

###### Option 2: Create Process Order Manually

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Process Manufacturing . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Process Order (COR1). | The Create Process Order: Initial Screen displays. |  |
| 3 | Enter Restriction | Make the following entries and choose Continue:Material Number: FG0504Production Plant: 3310Process Order Type: YBM2 | The system displays a list of all planned orders, which match the restriction. |  |
| 4 | Create Process Order: Header - General Data | Make the following entries and choose Save:Total QTY: <your quantity>Start : <today>End : <today plus 1 week> |  |  |
| 5 | Validate Control Key | Choose Operations.Make sure, that the YPI1 entry is maintained in the Control Key field for all phases and sub phases.Choose Back. |  |  |
| 6 | Validate Production Version | Choose Master Data.Check the production Version. The production version must be 0002 for one-stage batch derivation.To switch choose the button next to the production version and choose cont. on the pop-up. Change the entry for production version in the next pop up and choose Continue. Confirm the information pop up. |  |  |
| 7 | Save your Order | Choose Save. | Process order is created.Make a note of the process order number. |  |

##### Review Process Order

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
| 3 | Select AOR | If this is your first time to access the app, a welcome page would appear asking you to select your area of responsibility.Otherwise, choose your user name and the App Settings icon.On the Area of Responsibility - Production Supervisor screen, choose Production Supervisor.Choose Add or Delete to add or remove entries, and make sure following entry displays:Plant 1 AE/ MTS PI valuated (YB2) |  |  |
| 4 | Choose the Process Order | In the process order list, find your process order and choose it.Process Order: XXXX (from previous steps) | Note In the header area, you can switch between Compact Filter and Visual Filter, to find a proper way to search for your process order number. |  |
| 5 | Review Process Order | In the detailed page of the process order, review relevant information. |  |  |
| 6 | Check Long Text Copied from Planned Order (Optional) | If any long text is maintained for the planned order, you can check it in the converted process order.Choose Edit Order in the upper right corner.On the Change Process Order: Header screen, choose icon Change Long Text next to Process Order number, and check the text. | The long text maintained in the planned order is copied to the converted process order. |  |

##### Post Goods Issue of Batch Managed Components

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The withdrawal of the raw materials is used for the process order. This withdrawal can be done by using the picking list or doing a manual goods issue.

|  |
| --- |
| Note If the material is set for backflush (in material master or resource), the withdrawing is done automatically after you confirm the operation or the whole order. Backflushing should not be used for batch-managed components (to ensure that the physically picked and consumed batch is the same as the recorded batch). |

Prerequisites

Ensure that sufficient material is present on stock. You can check the stock levels using the app Monitor Stock / Requirements List - Old Version (MD04) available for the Production Planner role.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Initial screen displays. |  |
| 3 | Enter Process Order | Make the following entries and then press Enter:Trans./Event: Goods IssueReference Document: OrderOrder number: XXXX (from previous steps)Movement Type: 261 | The screen name adapts after entries are made. |  |
| 4 | Check Each Item | For each item displays, select Item OK. | Note Ensure that detail data is expanded. |  |
| 5 | Perform Batch Determination | Choose tab Quantity and button Stock Determ. | The Batch Determination MM: Select Batches screen displays. |  |
| 6 | Copy Batch Determination Result | Add quantities to the required batches and choose Copy. | The Goods Issue Order XXXX screen displays. In addition, the batch numbers have been determined.If you selected more that one batch, additional lines are created. |  |
| 7 | Post Goods Movements | Choose Post. | The goods movements have been posted. |  |

##### Monitor Order Progress (Optional)

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

##### Confirm Production incl. Component Backflush

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
| 3 | Enter Confirmation Option | Make the following entries and then choose Enter.Order: XXXX (from previous stepsPhase: 0020Confirm.type: Final confirmationClear open reservations: X | Note If the system shows the message Total quantity confirmed not equal to planned quantity to be confirmed, press Enter to ignore it. |  |
| 4 | Propose Actual Data | Choose Actual Data.Make the changes for the following fields:Scrap: <enter the amount you want to scrap>Yield: <Based on the origin quantities minus scrap>Reason for Var: < Enter scrap reason if needed>, for example, 0001 | The Quantities and Activities will be filed automatically.If you want to check your backflushed components (required for material FG0504), continue with step 5 of this table. Else proceed directly with step 6. |  |
| 5 | Check Backflushed Components | Choose Goods Movements. | The Enter Confirmation for Production Order: Goods Movement screen displays. Check the material entries and quantities.The final confirmation of the last operation has been carried out. Backflushed components are issued with the confirmation posting automatically (packaging material RM0507 within the confirmation of orders for Finished Product PI FG0504). |  |
| 6 | Save Confirmation | Click Post. | The final confirmation of the last operation is carried out. Costs and activity quantities are recalculated in proportion to the yield quantity. |  |

##### Post Goods Receipt for Process Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to post the goods receipt for the process order. You may post goods receipt for the total quantity, but usually already partial quantities of the products are required for further processing, such as consumption for further production or subsequent deliveries for sales orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as Warehouse Clerk. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Initial screen displays. |  |
| 3 | Enter Process Order | Make the following entries and then press Enter:Trans./Event: Goods ReceiptReference Document: OrderOrder number: XXXX (from previous steps)Movement Type: 101 | Screen name adapts after entries are made. |  |
| 4 | Enter Date of Manufacture | Choose the Batch tab and enter a batch number (optional). Do not enter a production date and choose enter.Note The production date is filled automatically due to derivation rules assigned to the material. |  |  |
| 5 | Check Item | Select item OK. | Ensure that detail data is expanded. |  |
| 6 | Post Goods Movement | Choose Post. | The goods movements are posted. The batch number is created automatically during the posting. Production date and shelf life expiration date are recorded within the batch master of the finished product. |  |

##### Review Process Order Confirmation

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
| 3 | Select AOR | If this is your first time to access the app, a welcome page would appear asking you to select your area of responsibility.Otherwise, choose your user name and the App Settings icon.On the Area of Responsibility screen, choose Production Supervisor.Choose Add or Delete to add or remove entries, and make sure following entry displays:Plant 1 AE/ MTS PI valuated (YB2) |  |  |
| 4 | Choose the Process Order | In the process order list, find your process order and choose it.Process Order: XXXX (from previous steps) | In the header area, you can switch between Compact Filter and Visual Filter, to find a proper way to search for your process order number. |  |
| 5 | Review Process Order | In the detailed page of the process order, review conformations of the process order. |  |  |

Option 2:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Process Order Confirmation (CORT). | The Display Process Order Confirmation: Initial screen displays. |  |
| 3 | Enter Process Order | Make the following entries and then choose Enter.Process Order: XXXX (from previous steps) | The Process Order Confirmation Display: Details screen displays.Confirmations are reviewed and checked within your responsibility area. |  |

Option 3:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Process Order Operations (F5323). |  |  |
| 3 | Choose Filter Style | In the header part, you can switch between Compact Filter and Visual Filter, which provides you different styles for filter. |  |  |
| 4 | Enter Process Order Number | Choose Compact Filter, make the following entries and choose Go.Process Order: XXXX (from previous steps) | Operation list displays. |  |

### Monitor Batch Derivation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step you can use the app Monitor Derivation to control previously performed derivations (receiver batches, attributes and their values, messages).

After a derivation is performed for the first time, it can have one of three statuses:

Success: The derivation was performed without errors.

Warning: For at least one attribute, one of the rules in the condition record is set to Warning, and the corresponding situation has occurred (for example, a sent attribute was empty). The system displays a warning for this derivation, but the derivation is still carried out. In other words, the receiver batch is changed.

Error: For at least one attribute, one of the rules in the condition record is set to Error, and the corresponding situation has occurred (for example, the receiving attribute already contained a different value). The derivation is canceled, that is, no attributes for the receiver batch are changed – not even the attributes where no error occurred.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as a Master Data Specialist - Batch Data. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Monitor Derivation (DVMO). | The Derivation monitor view displays. |  |
| 3 | Select Batches | Make the following entries and then press ExecuteMaterial: FG0504Plant: 3310Status of New Derivation: x Success | The batch with derivated characteristics is displayed. |  |

### Batch Information Cockpit - Top-Down and Bottom-Up Analysis

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this functionality you can identify which batches are delivered to which customer and which raw material batches are used for the production of which finished product. You can adapt the selection in the Batch Information Cockpit to customer-specific requirements by creating user-specific groups. You can get additional information by using subsequent actions.

In this case the evaluation is limited to the production process. As soon as you have purchased the raw materials and/or delivered the finished good FG0504 to a customer the evaluation is automatically enhanced with these information.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Batch Information Cockpit (BMBC). | The Batch Information Cockpit screen displays. |  |
| 3 | Select Batches | On the Batch Information Cockpit screen, make the following entries.Go to the Material tab.Material: FG0504Plant:3310Note For batch class and characteristics relevant materials, refer to [Master Data, Organizational Data, and Other Data](#unique_5) [page ] 6 section.Choose Execute Selection. | One or multiple batches are displayed in the left screen area Selection Result for Batches. The standard sorting is done per material number. |  |
| 4 | Expand Selection | In the section Selection Result for Batches. Select the checkbox for FG0504 and then choose Expand subtree or Expand node. | The selection result is analyzed and a batch for further investigation is identified. |  |
| 5 | Start Analysis | Right-click on one selected batch and choose either Usage (Top-Down) or Usage (Bottom-up). | The batch where-used list displays. |  |
| 6 | Analyze the Batch Where Used List | The usage of the batch can be analyzed and the specific documents (such as batch master record, production orders and sales order) can be accessed via double click. |  |  |
| 7 | Analyze Material Document | Choose Details again and select Usage.Select one document and choose Documents. | The usage displays again and after selecting documents the respective material document display. |  |
| 8 | Go to the Material Document | Choose the material document in the pop up dialog and choose Choose (F2).To display the material document, you need further authorizations that are granted by your company, for example, SAP_BR_INVENTORY_MANAGER. | The material document displays.Note that your user has to have the appropriate authorizations. |  |

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
| 3F0 - Event-Based Production Cost Posting | This procedure updates work-in-process calculation, overhead calculation, and variance calculation by linking the posting to the events.Note Start from CE2105, the default Best Practice content is based on event-based result analysis for new customer install and add new country only, rather than previous period-end posting. For existing customers (who activated content before 2105), the default remain unchanged to Period-End Closing - Plant (BEI) till customer makes the decision to switch. For migration to Event based from Periodic please refer [Production Settlement in Parallel Ledgers](https://help.sap.com/viewer/4032610758dc437089f0c28320eec93f/2105.500/en-US/e49a3770f22547a392455154f3eef6e2.html).If you are still using period-end posting, you may need to refer to non-standard Scope Item BEI - Period-End Closing - Plant. |
| Close Confirmed Production/Process Orders (Optional) | Search for Schedule Order Closing Runs - Close Production/Process Orders (F4305) app as a Production Supervisor - Discrete Manufacturing to schedule a job to set orders as Closed (CLSD). |

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
- related-to :: [[11-inventory-warehouse-and-transportation/master-data-script-create-batch-management-master-data-mds-2zw-299]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-2zw-301]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-2zw-303]]
- related-to :: [[11-inventory-warehouse-and-transportation/script-de-dados-mestre-criar-dados-mestre-de-administracao-de-lotes-2z]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/77G_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 129,884 chars in the whole document
