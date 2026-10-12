---
id: 13-quality-ehs-and-compliance/test-script-quality-management-in-discrete-and-process-manufacturing-1
title: "Test Script: Quality Management in Discrete and Process Manufacturing (1E1_AE) (1E1_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 1E1 (AE): QM inspections, SPC control charts and usage decisions in discrete and process manufacturing."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/quality-inspection-in-manufacturing]
aliases: [1E1_S4CLD2608_BPD_EN_AE]
keywords: [Quality Inspection in Manufacturing, quality management, quality inspection, inspection results recording, usage decision, control charts, inspection plan, master inspection characteristics, discrete manufacturing, process manufacturing]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1E1_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-712
topic: 13-quality-ehs-and-compliance/quality-inspection-in-manufacturing
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Quality Management in Discrete and Process Manufacturing (1E1_AE) (1E1_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1E1_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Quality Inspection in Manufacturing** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Quality Management in Discrete and Process Manufacturing (1E1_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 4](#_Toc232846675)

[2 Prerequisites 5](#_Toc232846676)

[2.1 System Access 5](#_Toc232846677)

[2.2 Roles 5](#_Toc232846678)

[2.3 Master Data, Organizational Data, and Other Data 6](#_Toc232846679)

[2.4 Business Conditions 8](#_Toc232846680)

[2.5 Preliminary Steps 8](#_Toc232846681)

[2.5.1 Assign Class Characteristic 8](#_Toc232846682)

[2.5.2 Create and Assign Class Characteristics to Batch Class 9](#_Toc232846683)

[2.5.3 Create Master Inspection Characteristic for SPC 12](#_Toc232846684)

[2.5.4 Create Master Inspection Characteristic with Reference to Class Characteristic 14](#_Toc232846685)

[2.5.5 Create Product Master with Quality Management 16](#_Toc232846686)

[2.5.6 Create a Bill of Materials 18](#_Toc232846687)

[2.5.7 Create Master Recipe with Quality Management 19](#_Toc232846688)

[2.5.8 Create Production Versions 20](#_Toc232846689)

[2.5.9 Create Inspection Plan 21](#_Toc232846690)

[2.5.10 Initial Raw Material Stock 23](#_Toc232846691)

[3 Overview Table 25](#_Toc232846692)

[4 Test Procedures 29](#_Toc232846693)

[4.1 Quality Management in Discrete Manufacturing 29](#_Toc232846694)

[4.1.1 Quality Management in Discrete Manufacturing - Goods Receipt from Production 29](#_Toc232846695)

[4.1.1.1 Make-to-Order Production – Semifinished Goods Planning and Assembly (1BM) 29](#_Toc232846696)

[4.1.1.2 Display Inspection Plan for Inspection Characteristics 31](#_Toc232846697)

[4.1.1.3 Post Goods Receipt for Production Order 32](#_Toc232846698)

[4.1.1.4 Display Material Stock Before Quality Inspection 33](#_Toc232846699)

[4.1.1.5 Display Quality Technician Overview (Optional) 34](#_Toc232846700)

[4.1.1.6 Display Open Inspection Lots 35](#_Toc232846701)

[4.1.1.7 Quality Inspection 36](#_Toc232846702)

[4.1.1.7.1 Display Inspection Methods 37](#_Toc232846703)

[4.1.1.7.2 Record Inspection Results 38](#_Toc232846704)

[4.1.1.7.3 Display Quality Engineer Overview (Optional) 40](#_Toc232846705)

[4.1.1.7.4 Make Usage Decision 42](#_Toc232846706)

[4.1.1.8 Display Material Stock after Quality Inspection 44](#_Toc232846707)

[4.1.1.9 Display Inspection Results History (Optional) 45](#_Toc232846708)

[4.1.2 Quality Management in Discrete Manufacturing - Within Production Process 46](#_Toc232846709)

[4.1.2.1 Make-to-Stock Production – Discrete Manufacturing (BJ5) 46](#_Toc232846710)

[4.1.2.2 Display Routing for Inspection Characteristics 49](#_Toc232846711)

[4.1.2.3 Display Quality Technician Overview (Optional) 50](#_Toc232846712)

[4.1.2.4 Display Open Inspection Lots 51](#_Toc232846713)

[4.1.2.5 Quality Inspection 52](#_Toc232846714)

[4.1.2.5.1 Display Inspection Methods 52](#_Toc232846715)

[4.1.2.5.2 Record Inspection Results Before Activation of the Control Chart 53](#_Toc232846716)

[4.1.2.5.3 Analyze and Activate Control Chart (Optional) 55](#_Toc232846717)

[4.1.2.5.4 Record Inspection Result After Activation of the Control Chart 57](#_Toc232846718)

[4.1.2.5.5 Display Quality Engineer Overview (Optional) 57](#_Toc232846719)

[4.1.2.5.6 Make Usage Decision 59](#_Toc232846720)

[4.1.2.6 Confirm Production Order Operation 60](#_Toc232846721)

[4.1.2.7 Review Production Order 61](#_Toc232846722)

[4.1.2.8 Make-to-Stock Production – Discrete Manufacturing (BJ5) 63](#_Toc232846723)

[4.1.3 Quality Management Within Production Process - Make-to-Stock Production of a Batch Managed Material 64](#_Toc232846724)

[4.1.3.1 Create Raw Material Stock 64](#_Toc232846725)

[4.1.3.2 Create and Release Production Order 65](#_Toc232846726)

[4.1.3.3 Goods Issue of Batch-Managed Components via Pick List 66](#_Toc232846727)

[4.1.3.4 Confirm Production Operations 67](#_Toc232846728)

[4.1.3.5 Execute Quality Inspection With Inspection Points 69](#_Toc232846729)

[4.1.3.6 Confirm Production Operations 70](#_Toc232846730)

[4.1.3.7 Post Goods Receipt for Order 71](#_Toc232846731)

[4.1.3.8 Make Usage Decision 72](#_Toc232846732)

[4.1.3.9 Review Batch Data (Optional) 72](#_Toc232846733)

[4.2 Quality Management in Process Manufacturing 73](#_Toc232846734)

[4.2.1 Quality Management in Process Manufacturing – In-Process Inspection for Semi Finished Goods 74](#_Toc232846735)

[4.2.1.1 Create Process Orders 74](#_Toc232846736)

[4.2.1.2 Display Open Inspection Lot (Optional) 75](#_Toc232846737)

[4.2.1.3 Results Recording for Inspection Point Before Activation of Control Chart 75](#_Toc232846738)

[4.2.1.4 Analyze and Activate Control Chart (Optional) 76](#_Toc232846739)

[4.2.1.5 Results Recording for Inspection Point After Activation of Control Chart 77](#_Toc232846740)

[4.2.1.6 Record Usage Decision 78](#_Toc232846741)

[4.2.1.7 Confirm Production 79](#_Toc232846742)

[4.2.1.8 Post Goods Receipt for Process Order 81](#_Toc232846743)

[4.2.2 Quality Management in Process Manufacturing - Goods Receipt from Production for Semi Finished Goods 82](#_Toc232846744)

[4.2.2.1 Display Open Inspection Lot (Optional) 82](#_Toc232846745)

[4.2.2.2 Record Inspection Results 82](#_Toc232846746)

[4.2.2.3 Record Usage Decision 83](#_Toc232846747)

[4.2.3 Review Batch Data (optional) 84](#_Toc232846748)

[5 Appendix 86](#_Toc232846749)

[5.1 Succeeding Processes 86](#_Toc232846750)

## Purpose

Overview

This scope item manages quality inspection in discrete and process manufacturing processes. Quality inspection activities are relevant during the production process or at goods receipt from production: At goods receipt, the material is posted to quality inspection stock and an inspection lot is created based on an inspection plan. The quality technician records the inspection results and the quality engineer makes a usage decision (acceptance or rejection of the material) and posts the material to unrestricted or blocked stock or to scrap. During the production process, a quality operation within the production order or process order triggers the quality inspection. The quality technician records the inspection results for inspection points. Based on the inspection point valuation, the quality operation is confirmed with the respective yield and scrap amounts and the inspection lot is closed by making a usage decision. In case of rejected characteristics, a defect is automatically recorded.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

|  |
| --- |
| Note This scope item does not contain detailed test procedures for quality inspection in process manufacturing. For specific configuration steps, refer to SAP Note [2964352](https://me.sap.com/notes/2964352) .To run through QM in process manufacturing, scope item Make-to-Stock – Process Manufacturing Based on Process Order (BJ8) must be activated. |

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
| Quality Technician | SAP_BR_QUALITY_TECHNICIAN | Quality Inspection | SAP_BR_QUALITY_TECHNICIAN |  |
| Quality Engineer | SAP_BR_QUALITY_ENGINEER | Quality Engineering | SAP_BR_QUALITY_ENGINEER |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |
| Production Engineer - Discrete Manufacturing | SAP_BR_PRODN_ENG_DISC | Production Engineering - Discrete Manufacturing | SAP_BR_PRODN_ENG_DISC |  |
| Production Operator - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC | Production Execution - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC |  |
| Production Supervisor - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC | Production Management - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC |  |
| BOM Engineer | SAP_BR_BOM_ENGINEER | Bills Of Material | SAP_BR_BOM_ENGINEER |  |
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Products / Product Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |
| Production Engineer - Process Manufacturing | SAP_BR_PRODN_ENG_PROC | Production Engineer - Process Manufacturing | SAP_BR_PRODN_ENG_PROC |  |
| Production Supervisor - Process Manufacturing | SAP_BR_PRODN_SUPERVISOR_PROC | Production Management - Process Manufacturing | SAP_BR_PRODN_SUPERVISOR_PROC |  |
| Production Operator - Process Manufacturing | SAP_BR_PRODN_OPTR_PROC | Production Execution - Process Manufacturing | SAP_BR_PRODN_OPTR_PROC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company is created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure:

Manufacturing

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Material | SG29 | Semi-Finished Product for discrete manufacturing with Quality Management |  |
| Material | FG129 | Finished Product for discrete manufacturing with Quality Management |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331B | Std. storage 2 | For production storage location |

Bill of Material Structure

This overview shows the bill of material structure and the usage of each component.

| Material | Level | Material Type | Unit | Characteristic of material |
| --- | --- | --- | --- | --- |
| FG129 | 0 | FERT | PC | Finished Product for discrete manufacturing with Quality Management |
| RM20 | 1 | ROH | PC | External procured |
| SG29 | 1 | HALB | PC | Semi-Finished Product for discrete manufacturing with Quality Management |
| RM124 | 2 | ROH | PC | External procured |

| Material | Level | Material Type | Unit | Characteristic of material |
| --- | --- | --- | --- | --- |
| QM006 | 0 | FERT | PC | Finished Product for discrete manufacturing with Quality Management |
| RMPI002 | 1 | ROH | PC | External procured |
| RMPI003 | 1 | ROH | PC | External procured |
| RMPI004 | 1 | ROH | PC | External procured |
| RMPI005 | 1 | ROH | PC | External procured |

For more information about creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNR | Create Product Master of type "Raw Material" - MDS |
| BNS | Create Product Master of type "Semi-Finished Good" - MDS |
| BNT | Create Product Master of type "Finished Good" - MDS |
| BNQ | Create Quality Inspection Plan - MDS |
| BNY | Create Quality Management Attributes for Material/Product Master - MDS |

### Business Conditions

Before this scope item can be tested, the following business condition must be met.

| Scope Item | Business Condition |
| --- | --- |
| BNU - Create Costing Run - MDS | Complete all steps in the test script. |
| BNZ - Create New Open MM Posting Period - MDS | Complete all steps in the master data script. Posting Period is up to date. |
| 1BM - Make-to-Order Production – Semifinished Goods Planning and Assembly | To run through this scope item, it must be possible to produce materials. |
| BJ5 - Make-to-Stock Production – Discrete Manufacturing | To run through this scope item, it must be possible to produce materials. |
| BNY - Create Quality Management Attributes for Material/Product Master - MDS | Complete all steps in the master data script for inspection type 03 and 04. |
| BJ8 - Make-to-Stock – Process Manufacturing Based on Process Order | To run through QM in process manufacturing, this scope item must be activated. |

### Preliminary Steps

#### Assign Class Characteristic

Purpose

The link between master inspection characteristics (MIC) and class characteristics enables the automatic transfer of inspection results to the batch classification. 2 class characteristics ( QM_ABSMAX_3310, QM_OK_NOK_3310) have already been created, and linked to corresponding MICs (ABSMAX, VISINSP). But the assignment between characteristics and batch class is not pre-delivered yet, which requires you check and do the assignment manually.

In this step, you assign the 2 class characteristics to Batch Class YB_QM which is assigned to demo material QM006.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a BOM Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Classes (CL02). |  |  |
| 3 | Enter Class Name | Make the following entries and press Enter.Class: YB_QMClass Type: 023 |  |  |
| 4 | Go to Char. Tab | Choose the Char. tab. Typically, the following characteristics shall be already assigned for you:LOBM_QSCORELOBM_UDCODE |  |  |
| 5 | Assign Characteristics | Assign or append the following pre-defined characteristics:QM_ABSMAX_3310QM_OK_NOK_3310 | If already assigned, it can be ignored. |  |
| 6 | Save | Choose Save. |  |  |

#### Create and Assign Class Characteristics to Batch Class

Purpose

The material master is assigned to a batch class. The additional class characteristics are created and linked to master inspection characteristics, which enables the automatic transfer of inspection results to the batch classification. The class characteristics from the batch class are automatically valuated at inspection completion (usage decision), based on the inspection results.

When you enter a class characteristic and link it to a master inspection characteristic, certain control indicators and values from this class characteristic are transferred to the master inspection characteristic.

|  |
| --- |
| Note You can only have a 1:1 relationship between a class characteristic and a master inspection characteristic, therefore you cannot reference the same class characteristic in several master inspection characteristics. |

Procedure

This procedure requires at least two class characteristics for further processing:

One class characteristic of Data TypeNumeric format, such as Density.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a BOM Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Characteristics (CT04). | The Characteristics screen displays.Note This is a common screen for create, change, and display mode. |  |
| 3 | Enter a Characteristic Name | Make the following entry and choose the Create icon.Characteristic: <Density> | The Basic data options are displayed.Note The value in the Valid from field is auto-populated. |  |
| 4 | Enter Basic Data | Make the following entries and choose Save:Basic data section:Description: <Enter your description>Status: Released (default)Format section:Data Type: <Numeric Format>Number of Chars: for example, <3>Value assignment section:Choose the Single-value option. | Note Other fields for chosen format are required in the Format section. Maintain them accordingly. |  |
| 5 | Enter Values for Check | On the Values tab, in the Allowed Values section, enter the values allowed for this characteristic.Allowed Values: for example, <100 –200> |  |  |
| 6 | Save the Characteristic | Choose Save. | The characteristic is created. |  |

One class characteristic of Data TypeCharacter Format, such as Color comparison.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a BOM Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Characteristics (CT04). | The Characteristics screen displays.Note This is a common screen for create, change, and display mode. |  |
| 3 | Enter a Characteristic Name | Make the following entry and choose the Create icon.Characteristic: <Color comparison> | The Basic data options are displayed.Note The value in the Valid from field is auto-populated. |  |
| 4 | Enter Basic Data | Make the following entries and choose Save:Basic data section:Description: <Enter your description>Status: Released (default)Format section:Data Type: <Character Format>Number of Chars: for example, <13>Value assignment section:Choose the Single-value option. | NoteOther fields for chosen format are required in the Format section. Maintain them accordingly.Assignment of Selected Set is required. On the Values tab, choose Other Value Check, choose Catalog Char and Copy. Enter the value allowed for this characteristic. |  |
| 5 | Enter Values for Check | On the Values tab, in the Selected Set section, enter the values allowed for this characteristic.Plant: 3310Selected Set: for example, <QUAL01> |  |  |
| 6 | Save the Characteristic | Choose Save. | The characteristic is created. |  |

Use the created class characteristics to assign these characteristics to the class. Optionally, you can also assign further available characteristics such as YB_BATCH_NUMBER (batch number).

| Test Step # | Test Step Name | Instruction | Expected Result | Comments | Pass / Fail / Comment |
| --- | --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a BOM Engineer. | The SAP Fiori launchpad displays. |  |  |
| 2 | Access the App | Open Manage Classes (CL02). | The Class screen displays.Note This is a common screen for create, change, and display mode. |  |  |
| 3 | Enter a Class Name | Make the following entries and choose the Change icon:Class: <YB_BATCH>Class Type: 023 | The Change Class screen displays. |  |  |
| 4 | Enter the Char. Tab | Choose the Char. tab and make the following entries to assign the characteristics you have created to this class, and then press Enter:In the Char. column:Char.: <Density>Char.: <Color comparison>Choose Save. | The Description and Data Type fields of the characteristics are automatically filled in with values. |  |  |

#### Create Master Inspection Characteristic for SPC

Purpose

To support Statistical Process Control (SPC), create a master inspection characteristic with corresponding control indicators.

Procedure

Create a quantitative reference master inspection characteristic based on the process step Create Master Inspection Characteristics from Master Data Script BNQ - Create Quality Inspection Plan - MDS. Additionally, set the following parameters for the quantitative master inspection characteristic (for example YPIQNSPC) in Characteristic Control Indicators: SPC Characteristic .

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Master Inspection Characteristic (QS21). | The Create Master Inspection Characteristic: Initial Screen displays. |  |
| 3 | Create a Quantitative Master Inspection Characteristic | On the Create Master Inspection Characteristic: Initial Screen, make the following entries:Plant: 3310Master Insp. Charac: for example, <YPIQNSPC>Valid From: <current date>Choose Master Inspection Characteristic. | The Create Master Inspection Characteristic: General Data screen displays.Note Some data is copied from the class characteristic to the master inspection characteristic. Furthermore, depending on the class characteristic settings, some control indicators of the master inspection characteristic cannot be changed. |  |
| 4 | Enter General Data for Quantitative Characteristic | From Create Master Inspection Characteristic: General Data:Status: Released.Quantitative Char: SelectedShort Text: for example, SPC MIC for Process ManufacturingSearch Field: for example, SPC MIC for Process Manufacturing |  |  |
| 5 | Edit Control Indicators for Quantitative Characteristics | Choose Control Indicators. In the Edit Characteristic Control Indicators dialog, select the following options:Sampling ProcedureSPC CharacteristicSumm. RecordingRequired Char.Choose Continue and select these additional options:Fixed ScopeNo DocumentationRecord Measured ValsRR Change DocsChoose Continue. |  |  |
| 6 | Save Your Data | Choose Save. | Your data is saved. |  |

#### Create Master Inspection Characteristic with Reference to Class Characteristic

Purpose

The link between master inspection characteristics and class characteristics allows you to transfer results of a quality inspection to the batch classification.

When you enter a class characteristic and link it to a master inspection characteristic, certain control indicators and values from this class characteristic are transferred to the master inspection characteristic.

|  |
| --- |
| Note You can only have a 1:1 relationship between a class characteristic and a master inspection characteristic. This means you cannot reference the same class characteristic in multiple master inspection characteristics. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Master Inspection Characteristic (QS21). | The Create Master Inspection Characteristic: Initial Screen displays. |  |
| 3 | Create Quantitative Master Inspection Characteristic | On the Create Master Inspection Characteristic: Initial Screen, make the following entries:Plant: 3310Master Insp. Charac: for example, <YPIQN01>Valid From: <current date>Class Characteristic: <Density> (numeric format)Choose Master Inspection Characteristic. | The Create Master Inspection Characteristic: General Data view displays.Note Some data is copied from the class characteristic to the master inspection characteristic. Furthermore, depending on the class characteristic settings, some control indicators of the master inspection characteristic cannot be changed. |  |
| 4 | Enter General Data for Quantitative Characteristic | From Create Master Inspection Characteristic: General Data, set Status: Released. |  |  |
| 5 | Edit Control Indicators for Quantitative Characteristics | Choose Control Indicators. In the Edit Characteristic Control Indicators, select the following options:Sampling ProcedureSumm. RecordingRequired Char.Choose Continue and select these additional options:Fixed ScopeNo DocumentationRecord Measured ValsRR Change DocsChoose Continue. |  |  |
| 6 | Enter Target Value | In the Tolerance Keys dialog, make the following entry:Target Value: for example, 101Choose Continue. |  |  |
| 7 | Save Your Data | Choose Save. | Your data is saved. |  |
| 8 | Create Qualitative Master Inspection Characteristic | On the Create Master Inspection Characteristic: Initial Screen, make the following entries:Plant: 1010Master Insp. Charac: for example, <YPIQL01>Valid From: <current date>Class Characteristic: <COLORCOMPARISON> (character format)Choose Master Inspection Characteristic. |  |  |
| 9 | Enter General Data for Qualitative Characteristic | From Create Master Inspection Characteristic: General Data, set Status: Released. |  |  |
| 10 | Edit Control Indicators for Qualitative Characteristics | Choose Control Indicators. In the Edit Characteristic Control Indicators dialog, select the following options:Sampling ProcedureSumm. RecordingRequired Char.Choose Continue to select more options:Fixed ScopeNo DocumentationRR Change DocsChoose Continue to exit the edit mode. |  |  |
| 11 | Save Your Data | Choose Save. | Your data is saved. |  |

For each master inspection characteristic, you can perform additional steps (e.g. Assign Inspection Method or Enable Defect Recording) according to process step Create Master Inspection Characteristics from Master Data Script BNQ - Create Quality Inspection Plan - MDS.

#### Create Product Master with Quality Management

Purpose

The following procedure provides instructions for replicating the semi-finished, batch-managed good product master of scope item BJ8 with quality management. This is required to activate the usage of in-process quality inspection and quality inspection for goods receipt from process order and enable the continued usage of both scope items.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Material (MM01). | The Create Material screen displays. |  |
| 3 | Copy semi-finished material from scope item | On the Initial Screen, make the following entries:Material Number: SGQMIndustry: Mechanical EngineeringMaterial Type: Semifinished ProductCopy from: SG24 (semi-finished good that is used in scope item BJ8)Press Enter.Choose Select View(s). In the Select View(s) dialog, choose the Select All icon (excluding the Classification, Quality Management and Forecasting views). Then choose Org. Levels.In the Organizational Levels dialog, make the following entries:Plant: 3310 and Copy From 3310Stor. Loc.: 331B and Copy From : 331BSales Org.: 3310 and Copy From: 3310Distr. Channel: 10 and Copy From : 10Select Organizational Levels/Profiles Only on Request.Choose Continue (Enter).Validate each view and navigate forward by pressing Enter. Once all views are validated, you are asked to save the data. Choose Yes (save). |  |  |
| 4 | Add or Change Batch Class Assignment | Open Create Material (MM01).On the Initial Screen, enter Material SGQM. Choose Continue and choose Continue again.Choose Select View(s). In the Select View(s) dialog, select Classification and choose Continue (enter).Enter Class<YB_BATCH> and press Enter.Choose Save. |  |  |
| 5 | Extend Material with Quality Management | Open Create Material (MM01).On the Initial Screen, enter Material SGQM. Choose Continue and choose Continue again.Choose Select View(s). In the Select View(s) dialog, select Quality Management.In the Quality Management view, choose Org. Levels. Enter Plant 3310, and choose Continue.Choose Insp. Setup and choose Create Inspection Types.In the Inspection Setup Data dialog, assign semi-finished material SGQM with two Inspection Types:03 in-process inspection04 goods receipt from productionSelect Active for both inspection types once they are assigned tot the material.Choose Continue.Note The Insp. Type Details screen varies per inspection type. Entering of procurement data is not required. |  |  |
| 6 | Save Your Data | Choose Save. | Your data is saved. |  |

#### Create a Bill of Materials

Purpose

Create a new bill of materials to structure the components that are used for manufacturing. The list contains components, with the quantity and unit of measure for each component. A component might be a raw material or a semi-finished material. The bill of material structure is copied from existing scope items and adapted to include the newly created semi-finished material.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a BOM Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain Bill Of Material - Create, change & display BOMs (F1813). |  |  |
| 3 | Select exiting BOM for copy | In the filter section, make the following entries:Plant : 3310BOM Usage: ProductionMaterial: material number of semi-finished product of reused scope item, such as SG24 for scope item BJ8Choose Go. |  |  |
| 4 | Copy existing BOM | Choose the BOM to be copied and choose Copy BOM.In the Copy BOM dialog, enter the following data:Plant: 3310BOM Usage: ProductionMaterial: SGQMChoose Copy BOM. |  |  |
| 5 | Save Your Data | Choose Create. | The BOM for semi-finished material is saved. |  |

Alternatively, you can execute Master Data Script BNK - Create Material BOM for Production and Sales, Process Step Create Production Bill of Material (Change Number is optional) to create your own Bill of Material structure.

#### Create Master Recipe with Quality Management

Purpose

The master recipe describes an enterprise-specific process in process industries without relating to a specific order. You can either create your own master recipe (Alternative 1) or replicate the master recipe of BJ8 of material SG24 (Alternative 2). The procedure describes how the master recipe is extended with one phase that represents the in-process quality inspection.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Engineer - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Master Recipe (C201). | The Create Master Recipe: Initial Screen displays. |  |
| 3a | Alternative 1: Create your own master recipe | Execute the Procedure of Master Data Script 3X9 - Create Master Recipe - MDS for semi-finished material xx.Note Inspection material assignment or production version is not required, and this will be done in the next step of this article. |  |  |
| 3b | Alternative 2: Copy master recipe from scope item | On the Initial Screen enter the following data and then go back.Material: SGQMPlant: 3310Profile: YPI1Choose Choose Template, choose Master Recipe, and choose Continue. Specify the recipe group to be copied and choose Continue.Note You can use the value help to search, for example, material SG24.Set the Status of the master recipe to 4-released (general) and press Enter. |  |  |
| 5 | Set Up QM data for recipe | In the Recipe Header sub-tab, choose Quality Management, enter the following data and then go back.Insp. Points: <101 Time-based>Dynamic Modification is optional.Go back. |  |  |
| 6 | Add a Phase | On the Operations sub-tab choose Insert OperationActivity: 0025Phase Indicator: XSuperior Operation: Operation ID 0010Control Key: QM01Description: <Enter a description for the operation>Press Enter and double-click the phase you created. |  |  |
| 7 | Set Up of Quality Data of Phase | On the General data sub-tab, choose QM Data, enter the following data and then go back.Inspection Point Completion: Automatic valuation based on insp. point definitionTime-related: <select> TFac. <30> <MIN>Press Enter and go back. |  |  |
| 8 | Set Up for Inspection Characteristics of Phase | On the General Data sub-tab, choose Insp. Characs, enter the following data and then go back.Master Inspection Characteristic: YPIQNSPC(quantitative master inspection characteristic enabled for SPC from previous step) and press Enter.Sampling Procedure: <YSPCFIX5>Sample Unit of Meas.: <CCM>SPC Criterion: <Task List Characteristic/Inspection Lot>Press Enter. | Note The sampling procedure determines the chart type. Evaluate if the chart type of the pre-delivered sampling procedure fulfills your requirements. |  |
| 9 | Save Your Data | Save your entries. | Master recipe is extended with Quality Management.Master data setup for in-process inspection with SPC is completed. |  |

#### Create Production Versions

Purpose

Create a production version using the newly created master data for processing production processes to avoid replicating the finished material.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Production Engineer - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Process Production Versions (F6400). |  |  |
| 3 | Create a Production Version for Semi-finished Good | Make the following entries and choose Go:Material: SGQMPlant: 3310 |  |  |
| 4 | Check Production Version Proposals | On the Production Version Proposals tab, you can find proposals for creating a new production version if the corresponding BOM/task list combination does not exist yet.You can go through the proposal details by choosing the proposal and make possible changes. |  |  |
| 5 | Accept Proposal | Choose the production version proposal and choose Create. | A new production version is created based on the proposed parameters. You can find it under the Existing Production Versions tab. |  |

#### Create Inspection Plan

Purpose

If material quality is supposed to be inspected upon goods receipt from production, one of the prerequisites is that an inspection plan is available. The inspection plan is newly created for goods receipt from production of material SGQM.

Procedure

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Test Step # | Test Step Name | Instruction | Expected Result |  |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Inspection Plan (QP01). | The Create Inspection Plan: Initial Screen displays. |  |
| 3 | Enter Data | On the Create Inspection Plan: Initial Screen, make the following entries:Material: SGQMPlant: 3310Key Date: for example, <today>Choose Continue. | The Create Inspection Plan: Header Details screen displays when there is no plan available for the specified material/plant combination.Note If there is a plan available, choose a group from the dialog box. The Inspection Plan Create: Task List Overview screen displays. Choose New Entries to create a new inspection plan. |  |
| 4 | Maintain Header Details | On the Create Inspection Plan: Header Details screen, make the following entries:Usage: Choose from the value help list for usage purpose, for example, 5 Goods receiptStatus: Choose from the value help list, for example, 4 Released (General)Lot size: Within 1 to 99,999, for example, 999 pcChoose Operations. | The Inspection Plan Create: Operation Overview screen displays. |  |
| 5 | Enter Operation Data (Overview) | On the Inspection Plan Create: Operation Overview screen, make the following entries:Operation Number: for example, 0010Work Center: Choose work center, for example, QMLABSControl Key: Choose a control key, for example, QM01Description: Provide a descriptionSelect the operation line item, and then choose Operation.Note If the Operation button is not available, choose More > Operation . | The Create Inspection Plan: Operation Details screen displays.Note The control key influences the planning and processing of inspection operation, for example whether or not inspection characteristics must be maintained for an inspection operation. |  |
| 6 | Operation Data (Details) | On the Create Inspection Plan: Operation Details screen, scroll to review the Recording View: Single Values and Summarized Results (Default View).Choose Back to return to the Operation Overview screen. |  |  |
| 7 | Enter Inspection Characteristics | Select the operation line and choose Inspection Characteristics.Assign Master Inspection Characteristics YPIQN01 with Sampling Procedure YPERCIN2Assign Master Inspection Characteristics YPIQL01 with Sampling Procedure YPERCIN1 | Detailed information is displayed. |  |
| 8 | Save Your Data | Choose Save. | Your data is saved. |  |

#### Initial Raw Material Stock

Purpose

In a real business case, raw materials are usually purchased from external vendors that can be covered by the standard purchasing process. This process step shows you how to directly post initial stock to the storage location.

|  |
| --- |
| Note You can either post initial stock directly to the storage location or refer to the process of Procurement of Direct Materials (J45) or Scheduling Agreements in Procurement (BMR). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). |  |  |
| 3 | Choose Goods Receipt-Other | Make the following entries and press Enter:Trans./Event: Goods ReceiptReference Document: OtherMovement Type: 561 |  |  |
| 4 | Specify Material | On the Material tab, make the following entry:Material: RM09 | Ensure that detailed data is expanded. |  |
| 5 | Specify Quantity | On the Quantity tab, make the following entry:Qty in Unit of Entry: 1000 |  |  |
| 6 | Specify Plant and Storage Location | On the Where tab, make the following entries:Plant: 3310Storage Location: 331B |  |  |
| 7 | Check Item | Press Enter, and ensure Item OK is selected. |  |  |
| 8 | Add Other Materials | Choose Next Item, then repeat steps 4 to 7 for the following materials:Material: RM19Material: RM30 |  |  |
| 9 | Post Goods Movement | Choose Post. | Material document XXX is posted.Materials are available in stock. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| Quality Management in Discrete Manufacturing |  |  |  |
| Quality Management in Discrete Manufacturing - Goods Receipt from Production |  |  |  |
| [Make-to-Order Production – Semifinished Goods Planning and Assembly (1BM)](#unique_18) [page ] 29 | See scope item 1BM | See scope item 1BM | See scope item 1BM |
| [Display Inspection Plan for Inspection Characteristics](#unique_19) [page ] 31 | Quality Technician | Display Inspection Plan (QP03) | The Display Inspection Plan: Initial screen displays. |
| [Post Goods Receipt for Production Order](#unique_20) [page ] 32 | Warehouse Clerk | Post Goods Receipt for Production Order (F3110) | Goods movements are posted. |
| [Display Material Stock Before Quality Inspection](#unique_21) [page ] 33 | Warehouse Clerk | Stock - Single Material (F1076) | The Stock - Single Material (F1076) screen displays. |
| [Display Quality Technician Overview (Optional)](#unique_22) [page ] 34 | Quality Technician | Quality Technician Overview (F2361) | The Quality Technician Overview (F2361) screen displays. |
| [Display Open Inspection Lots](#unique_23) [page ] 35 | Quality Technician | Manage Inspection Lots (F2343) | The Manage Inspection Lots screen displays. |
| [Display Inspection Methods](#unique_24) [page ] 37 | Quality Technician | Display Inspection Methods (F0311A) | The Inspection Method screen displays. |
| [Record Inspection Results](#unique_25) [page ] 38 | Quality Technician | Record Inspection Results (F1685A) | The Record Inspection Results screen displays. |
| [Display Quality Engineer Overview (Optional)](#unique_26) [page ] 40 | Quality Engineer | Quality Engineer Overview (F2360) | The Quality Engineer Overview (F2360) screen displays. |
| [Make Usage Decision](#unique_27) [page ] 42 | Quality Engineer | Manage Usage Decisions (F2345) | The Manage Usage Decisions (F2345) screen displays. |
| [Display Material Stock after Quality Inspection](#unique_28) [page ] 44 | Warehouse Clerk | Stock - Single Material (F1076) | The Stock - Single Material screen displays. |
| [Display Inspection Results History (Optional)](#unique_29) [page ] 45 | Quality Engineer | Display Results History (F2428) | The Display Results History (F2428) screen displays. |
| Quality Management in Discrete Manufacturing - Within Production Process |  |  |  |
| [Make-to-Stock Production – Discrete Manufacturing (BJ5)](#unique_30) [page ] 46 | See scope item BJ5 | See scope item BJ5 | See scope item BJ5 |
| [Display Routing for Inspection Characteristics](#unique_31) [page ] 49 | Production Engineer - Discrete Manufacturing | Display Routing (CA03) | The Display Routing: Initial Screen screen displays. |
| [Display Quality Technician Overview (Optional)](#unique_32) [page ] 50 | Quality Technician | Quality Technician Overview (F2361) | The Quality Technician Overview screen displays. |
| [Display Open Inspection Lots](#unique_33) [page ] 51 | Quality Technician | Manage Inspection Lots (F2343) | The Manage Inspection Lots (F2343) screen displays. |
| [Display Inspection Methods](#unique_34) [page ] 52 | Quality Technician | Display Inspection Methods (F0311A) | The Inspection Method screen displays. |
| [Record Inspection Results Before Activation of the Control Chart](#unique_35) [page ] 53 | Quality Technician | Record Inspection Results - Hierarchical Worklist (QE51N) | The Record Inspection Results - Hierarchical Worklist screen displays. |
| [Analyze and Activate Control Chart (Optional)](#unique_36) [page ] 55 | Quality Engineer | Manage Control Charts (F2810) |  |
| [Record Inspection Result After Activation of the Control Chart](#unique_37) [page ] 57 | Quality Technician | Record Inspection Results - Hierarchical Worklist (QE51N) | The Record Inspection Results - Hierarchical Worklist screen displays. |
| [Display Quality Engineer Overview (Optional)](#unique_38) [page ] 57 | Quality Engineer | Quality Engineer Overview (F2360) | The Quality Engineer Overview (F2360) screen displays. |
| [Make Usage Decision](#unique_39) [page ] 59 | Quality Engineer | Manage Usage Decisions (F2345) | The Manage Usage Decisions (F2345) screen displays. |
| [Confirm Production Order Operation](#unique_40) [page ] 60 | Production Operator - Discrete Manufacturing | Confirm Production Operation (F3069) | The Enter Time Ticket for Product Order screen displays. |
| [Review Production Order](#unique_41) [page ] 61 | Production Supervisor - Discrete Manufacturing | Manage Production Orders (F2336) | The Manage Production Orders screen displays. |
| [Make-to-Stock Production – Discrete Manufacturing (BJ5)](#unique_42) [page ] 63 | See scope item BJ5 | See scope item BJ5 | See scope item BJ5 |
| [Quality Management Within Production Process - Make-to-Stock Production of a Batch Managed Material](#unique_43) [page ] 64 |  |  |  |
| [Create Raw Material Stock](#unique_44) [page ] 64 | Warehouse Clerk | Post Goods Movement (MIGO) | The Post Goods Movement (MIGO) screen displays. |
| [Create and Release Production Order](#unique_45) [page ] 65 | See scope item BJ5 | See scope item BJ5 | See scope item BJ5 |
| [Goods Issue of Batch-Managed Components via Pick List](#unique_46) [page ] 66 | Production Operator - Discrete Manufacturing | Pick Components for Production Orders (CO27) | The Picking List: Initial Screen displays. |
| [Confirm Production Operations](#unique_47) [page ] 67 | Production Operator - Discrete Manufacturing | Confirm Production Operation (F3069) | The Enter Order and Operation screen displays. |
| [Execute Quality Inspection With Inspection Points](#unique_48) [page ] 69 | Quality Technician | Record Results for Inspection Points (F2689) | The Record Results for Inspection Points screen displays. |
| [Confirm Production Operations](#unique_49) [page ] 70 | Production Operator - Discrete Manufacturing | Confirm Production Operation (F3069) | The Enter Order and Operation screen displays. |
| [Post Goods Receipt for Order](#unique_50) [page ] 71 | Warehouse Clerk | Post Goods Movement (MIGO) | The Post Goods Movement (MIGO) screen displays. |
| [Make Usage Decision](#unique_51) [page ] 72 | Quality Engineer | Manage Usage Decisions (F2345) | The Manage Usage Decisions (F2345) screen displays. |
| [Review Batch Data (Optional)](#unique_52) [page ] 72 | Quality Technician | Manage Batches (F2462) | The Manage Batches screen displays. |
| Quality Management in Process Manufacturing |  |  |  |
| Quality Management in Process Manufacturing – In-Process Inspection for Semi Finished Goods |  |  |  |
| [Create Process Orders](#unique_53) [page ] 74 | Production Supervisor - Process Manufacturing | Create Process Order (COR1) |  |
| [Display Open Inspection Lot (Optional)](#unique_54) [page ] 75 | Quality Technician | Manage Inspection Lots (F2343) |  |
| [Results Recording for Inspection Point Before Activation of Control Chart](#unique_55) [page ] 75 | Quality Technician | Record Inspection Results - Hierarchical Worklist (QE51N) |  |
| [Analyze and Activate Control Chart (Optional)](#unique_56) [page ] 76 | Quality Engineer | Manage Control Charts (F2810) |  |
| [Results Recording for Inspection Point After Activation of Control Chart](#unique_57) [page ] 77 | Quality Technician | Record Inspection Results - Hierarchical Worklist (QE51N) |  |
| [Record Usage Decision](#unique_58) [page ] 78 | Quality Technician | Manage Inspection Lots (F2343) |  |
| [Confirm Production](#unique_59) [page ] 79 | Production Operator - Process Manufacturing | Confirm Process Order Phase (COR6N) |  |
| [Post Goods Receipt for Process Order](#unique_60) [page ] 81 | Warehouse Clerk | Post Goods Movement (MIGO) |  |
| Quality Management in Process Manufacturing - Goods Receipt from Production for Semi Finished Goods |  |  |  |
| [Display Open Inspection Lot (Optional)](#unique_61) [page ] 82 | Quality Technician | Manage Inspection Lots (F2343) |  |
| [Record Inspection Results](#unique_62) [page ] 82 | Quality Technician | Record Inspection Results - Hierarchical Worklist (QE51N) |  |
| [Record Usage Decision](#unique_63) [page ] 83 | Quality Engineer | Manage Usage Decisions (F2345) |  |
| [Review Batch Data (optional)](#unique_64) [page ] 84 | Quality Technician | Manage Batches (F2462) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Quality Management in Discrete Manufacturing

#### Quality Management in Discrete Manufacturing - Goods Receipt from Production

##### Make-to-Order Production – Semifinished Goods Planning and Assembly (1BM)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this scope item, the component SG29 must be produced.

| Master Data | Value | Comments |
| --- | --- | --- |
| Material | RM124 | Raw material, used in Initial Material Stock step |
| Material | SG29 | Semi-finished goods |
| Plant | 3310 |  |

You can follow the simplified procedures described as follows in this document. Or for a complete scenario, you can execute relevant steps from the Make-to-Order Production – Semifinished Goods Planning and Assembly (1BM) test script, using the master data from this document.

- Create Initial Material Stock
- Create Planned Independent Requirements
- Material Requirements Planning
- Monitor Material Coverage
- Create Production Order
- Release Production Order
- Confirm Production Order for Semi-Finished Product

Procedure

The simplified procedures are described as follows.

Create Initial Material Stock

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Stock (F1062). | The Manage Stock screen displays. |  |
| 3 | Specify Material and Plant | Make the following entries and choose Enter:Material: RM124Plant: 3310 | For a detailed materials list, see the Bill of Materials structure list in Master Data, Organizational Data, and Other Data. |  |
| 4 | Select Storage Location | Choose button in column Unrestricted-Use Stock, line Std. storage 2 (331B). | The dialogue box Manage Stock is displayed. |  |
| 5 | Enter Quantity | Make the following entries and choose Post:Stock Change: Initial EntryQuantity: 100 PCDocument Date: <Date>Posting Date: <Date> | A success message is displayed and stock is increased by the specified amount. |  |
| 6 | Check Material Document (Optional) | Click Material document xxx/yyyy created and review document details. | Document is OK. |  |

Create Production Order and Release Production Order

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Production Order (CO01). | The Production Order Create: Initial Screen displays. |  |
| 3 | Enter the Order Information | Make the following entries and choose Continue:Material: SG29Production Plant: 3310 | The Production Order Create: Header screen displays. |  |
| 4 | Enter the Order Details | Make the following entries:Quantities - Total Qty: for example, 100 PCScheduling - Type: <Current Date>and choose Enter. | A message All checked materials in order are available appears. Otherwise, please check the initial material stock. |  |
| 5 | Release Order | Choose Release Order. | Releases are carried out. |  |
| 6 | Save | Choose Save and make a note of your production order number. | Order number XXX is saved. |  |

##### Display Inspection Plan for Inspection Characteristics

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you display the inspection plan that is related to the semifinished goods. The inspection plan defines all inspection characteristics used later in the quality inspection.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Display Inspection Plan (QP03). | The Display Inspection Plan: Initial Screen displays. |  |
| 3 | Enter Selection Fields | Make the following entries and choose Continue.Material: SG29Plant: 3310 |  |  |
| 4 | Go to Inspection Characteristics Overview Screen | Select the entry for Operation 0010 and choose Inspection Characteristics.Note If you could not find Inspection Characteristics in your screen, choose Menu > Goto > Inspection Characteristic Overview . | The Display Inspection Plan: Characteristic Overview screen displays. |  |
| 5 | Review the Inspection Characteristics | There are two Master Inspection Characteristics: one is Qualitative – Surface, the other is Quantitative – Length. | You have now reviewed the inspection characteristics for which data has to be maintained later. |  |

##### Post Goods Receipt for Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you post the goods receipt from production after completing a production order. This is required to perform a quality inspection for the assembled material.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Post Goods Receipt for Production Order (F3110). | The Post Goods Receipt for Production Order screen displays. |  |
| 3 | Enter Process Order | Make the following entries and choose Enter.Order Number: XXXX (From previous steps) | Screen name adapts after entries are made. |  |
| 4 | Enter Quantity | Make the following entries and press Enter.Delivered: for example, 100 PC | Note By default, stock type unrestricted-use is selected. However, as quality inspection at goods receipt from production is set up in the material master of the respective material, the stock will be posted to stock type quality inspection, instead. |  |
| 5 | Post Goods Movement | Choose Post. | A success message containing material document ID is displayed and the goods movement is posted. The material is posted to quality inspection stock. A quality inspection lot with inspection type 04 (Goods receipt inspection from production) is created to check the quality of the assembly.Make a note of the material document number: __________ |  |

##### Display Material Stock Before Quality Inspection

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this optional step, a review of the subassembly material stock is done. Due to quality inspection, the material is not available for other processing.

Prerequisite

The goods receipt from production order was posted for the subassembly material directly to quality inspection stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as an Inventory Manager. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Stock - Single Material (F1076). | The Stock - Single Material (F1076) screen displays. |  |
| 3 | Enter Material | Make the following entries and press Enter.Material: SG29 | Stock for the material is displayed. |  |
| 4 | Check Stock Quantity | Check the Quality Inspection Stock under the plant 3310. |  |  |
| 5 | Manage Stock | Choose Manage Stock at the bottom of the screen. | The list of stock in different storage locations is displayed. |  |
| 6 | Log On | Log on to the SAP Fiori launchpad as a Quality Technician. | The SAP Fiori launchpad displays. |  |
| 7 | Check Inspection Lots | Open the app Manage Inspection Lots (F2343).Make the following entries and choose Go:Material: SG29Plant: 3310 | The Inspection Lots for the selected material are displayed. |  |

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

The goods receipt from production order was posted for the subassembly material directly to quality inspection stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Quality Technician Overview (F2361). | The Quality Technician Overview (F2361) screen displays.You can get an overview of the inspection lots with open results recording and the inspection lots without an inspection plan. |  |

##### Display Open Inspection Lots

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection lot is used to record the results of the inspection operation. In this optional step, the references to the Goods Receipt and Production Order are verified as well as the sample size used for quality inspection reviewed.

Prerequisite

In this scope item, the inspection lot is created automatically upon goods receipt for the production order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Inspection Lots (F2343). | The Manage Inspection Lots (F2343) screen displays. |  |
| 3 | Filter Fields | Make the following entries and choose Go:Plant: 3310Material: SG29Material Document: Obtained from previous step | If Material Document is not displayed in the Filters, choose Adapt Filters. On the popup screen Adapt Filters, select Material Document and choose OK. Choose Go. |  |
| 4 | Select the Corresponding Inspection Lot | In the inspection lot list, select the inspection lot. |  |  |
| 5 | Check Inspection Lot | In the Origin tab, verify the referenced production order and material document. | The production order number and material document number from which the inspection lot originates are displayed. |  |
| 6 | Check Inspection Lot – Quantities | Under Origin , check the sample size. | The size of the sample for quality inspection is displayed (10% of inspection lot quantity). |  |

##### Quality Inspection

Purpose

The assembly undergoes a quality inspection to ensure that it meets the predefined quality requirements.

In this step, the quality technician records the inspection result for the required inspection characteristics. Afterwards, the quality engineer completes the inspection with a usage decision.

Prerequisite

The inspection is processed based on inspection lot. In this scope item, the inspection lot has been created automatically upon goods receipt for the production order.

###### Display Inspection Methods

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection method is reviewed with attached document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Display Inspection Methods (F0311A). | The Inspection Method screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Plant: 3310Inspection Method: SURFACE |  |  |
| 4 | Select Inspection Methods | In the Inspection Methods list, click the Inspection Method Surface. | Inspection Method is displayed. |  |
| 5 | Review Inspection Method Details and the attached Document (Optional) | Verify the General Information.Under Documents, check the document. |  |  |

###### Record Inspection Results

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The quality technician executes the quality inspection and records inspection results for the inspection lot.

Procedure

Record Inspection Results for one Inspection Lot

If inspection results shall be recorded for one or only a few inspection lots, execute the following process flow:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Quality Technician. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Record Inspection Results (F1685A) | The Record Inspection Results screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.If Order is not displayed in the Filters, choose Adapter Filters. On the popup screen Adapter Filters, select Order and choose OK. Choose Go.Plant: 3310Material: SG29Order: <from previous step>. |  |  |
| 4 | Select the Corresponding Inspection Lot | In the inspection lot list, select the inspection lot.Choose Record Multiple Results at top of the table. |  |  |
| 5 | Enter Inspection Result | Depending on the inspection result, select one of the following two options:Positive ResultSurface: Code Group - Code: SURFACE 0020 (Smooth)Length: Mean Value (CM): : 160Negative ResultSurface: Code Group - Code: SURFACE 0010 (Rough)Length: Mean Value (CM): : 90 | For the qualitative characteristic (surface) the search help is needed to select a value. For the quantity characteristic (length) a number can be entered directly.The valuation and close are performed automatically, and the status is set to Valuated.The default number of inspected objects is calculated based on the sample size reviewed in an earlier step. The number of inspected objects can be manually changed. As well a number of nonconforming objects can be maintained directly in the respective fields for every inspection characteristic. |  |
| 6 | Save Inspection Lot | Choose Save. | The inspection lot is saved. QM Inspection for manufactured goods has been performed and result recorded. |  |

Optional: Process-Optimized Results Recording for Multiple Inspection Lots

If inspection results shall be recorded for several inspection lots at the same time, execute the following process flow.

|  |
| --- |
| Caution Note that this app can only be used for quality inspections with master inspection characteristics. It is not possible to capture inspection results for inspections with plan characteristics. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Technician. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Record Inspection Results in Table Form (F3365). | The Record Inspection Results in Table Form screen displays. |  |
| 3 | Enter Filter Fields | Maintain filter values and choose Go. | A list of inspection lots is displayed. |  |
| 4 | Select Inspection Lots and Inspection Characteristics | Select the inspection lots for which inspection results shall be recorded and choose Record Multiple Results.In the dialogue box Select Characteristics for Result Recording, select the master inspection characteristics for which inspection results shall be recorded and choose button OK. | The Record Inspection Results in Table Form screen displays.Note The system creates one table line item per inspection lot operation. Each master inspection characteristic is displayed in a separate column. The valuation of the inspection characteristic is displayed in a separate adjacent column. If a master inspection characteristic is assigned to another inspection operation, the respective table field is grayed out. |  |
| 5 | Show Inspection Details (Optional) | Click one inspection characteristic in the table and choose Show Details. | The side panel opens and detailed inspection data are displayed (e.g. inspection specifications, master inspection characteristic, inspection method, test equipment, and inspection remarks). |  |
| 6 |  | Choose Settings button in the upper right corner of the table. In the Define Column Properties dialogue box, select Work Center and choose OK. | An additional Work Center column is displayed. |  |
| 7 | Enter Inspection Results | Enter inspection results. See above for example data. | For qualitative results, a corresponding value help is provided. Quantitative inspection results can be entered directly.Note Depending on the defined valuation mode (check inspection method details), the valuation is either done automatically by the system or must be done manually by the user.If an inspection result requires an inspection remark (check master inspection characteristic settings), it is not possible to navigate to the next inspection result. Open Details side panel and maintain the inspection remark in section Remarks. |  |
| 8 | Save Inspection Data | Choose Save. | Inspection results are saved and a success message is displayed. |  |

###### Display Quality Engineer Overview (Optional)

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
| 6 | In Card: Inspection Lots with Defects (optional) | (In case negative inspection results have been recorded) Select one of the inspection lot origins, then you will be directed to app Manage Defects (F2649) automatically. Choose the relevant defect ID to check the details of the defect. | The defect details are displayed. |  |
| 7 | In Card: Top Defective Materials (optional) | (In case negative inspection results have been recorded) Select one of the materials inspected, then you will be directed to app Manage Defects (F2649) automatically. Choose the relevant defect ID to check the details of the defect. | The defect details are displayed. |  |
| 8 | In Card: Top Defects (optional) | (In case negative inspection results have been recorded) Select one of the defect codes recorded, then you will be directed to app Manage Defects (F2649) automatically. Choose the relevant defect ID to check the details of the defect. |  |  |

###### Make Usage Decision

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection is done and the inspection result is recorded. You must decide whether or not to accept the assembly depending on the inspection result. If you do not want to use the Quality Engineer Overview (F2360), you can open the Manage Usage Decisions (F2345) app directly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Usage Decisions (F2345). | The Manage Usage Decisions (F2345) screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go:Plant: 3310Material: SG29Usage Decision Made: NoMaterial Document: Obtained from previous step | If Material Document is not displayed in the Filters, choose Adapt Filters. On the popup screen Adapt Filters, select Material Document and choose OK. Choose Go. |  |
| 4 | Select the Corresponding Inspection Lot | In the inspection lot list, select the inspection lot. |  |  |
| 5 | Display Defects | Scroll down to the Defects area. Check the details of Defects. | Only available if you have recorded a Negative result. For a surface rejection, there will be a surface defect, for a length rejection, there will be a tolerance defect displayed. |  |
| 6 | Enable Edit | Choose Edit. In the Attachments section choose Upload, select the path and add the document. | For example, you can upload pictures to visualize the defect. |  |
| 7 | Enter UD code | Go to the Usage Decision area. Depending on the inspection result, select one of the following two options via search help and confirm with Choose.Positive Result:UD code: UD04 A1 (Accepted - unrestricted stock)Negative Result:UD code: UD04 R1 (Rejected-blocked Stock)UD code: UD04 R320 Rejected–scrap (complete quantity) | If the dialogue Some required characteristics are still open. Do you want to force inspection completion? appears, choose Yes.The corresponding stock posting is processed automatically in background for the complete quantity for Usage Decision codes A1, R1, and R320. |  |
| 8 | Modify Stock Posting (Optional) | In the Inspection Lot Stock section, enter the quantities to be posted to different stock types. | Note If you want to scrap a partial quant with UD code R310, you can split the quantity and post to To Unrestricted Use and To Scrap, respectively. It is also possible to transfer the (partial or full) quant to a different material if, for example, inspection results show that the product is of higher/lower quality than initially planned in the production order and the higher/lower quality corresponds to different materials. |  |
| 9 | Save Usage Decision | Choose Save. | The usage decision is made with regard to the manufactured goods. The system automatically triggers the material movements if associated with the usage decision code.Positive Result: The usage decision made for the inspection is Quality Inspection Passed. A goods movement is posted automatically from quality inspection stock to unrestricted use stock for the assembly SG29 .Negative Result: The usage decision made for the inspection is Quality Inspection Failed. A goods movement is posted automatically from quality inspection stock to blocked stock for the assembly SG29 . |  |

##### Display Material Stock after Quality Inspection

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this optional step, we now verify the material movement done based on the usage decision codes by looking again at the material stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Warehouse Clerk. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Stock - Single Material (F1076). | The Stock - Single Material (F1076) screen displays. |  |
| 3 | Enter Selection Fields | Make the following entries and choose Enter.Material: SG29 |  |  |
| 4 | Check Stock Quantity | Check the changed quantities of the Quality Inspection Stock, Unrestricted Use Stock (in case of positive usage decision) or Blocked Stock (in case of negative usage decision). | The stock quantities for subassembly material SG29 are updated based on the quality inspection and respective usage decision of the previous steps. |  |

##### Display Inspection Results History (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this optional step, an overview about the history of inspection result is shown. For each Inspection Characteristic are several statistical values and the development for recorded results are illustrated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Display Results History (F2428). | The Results History screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Aggregation Level: Master Inspection Characteristic Version |  |  |
| 4 | Select Inspection Characteristic | Select an Inspection Characteristic, for example, Length. | Information is provided about the selected characteristics for process control, for example:A diagram displays the development of the recorded results for this characteristic with lower and upper limit.Statistical Values for Control Chart and Process Capability, for example, Variance. |  |

#### Quality Management in Discrete Manufacturing - Within Production Process

##### Make-to-Stock Production – Discrete Manufacturing (BJ5)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this scope item, the component FG129 must be produced.

| Master Data | Value | Comments |
| --- | --- | --- |
| Material | RM20 | Raw material, used in Create Initial Material Stock step |
| Material | SG29 | Semi-Finished Goods, used in the step: Create Initial Material Stock |
| Material | FG129 | Finished product |
| Plant | 3310 |  |

You can follow the simplified procedures described as follows in this document. Or for a complete scenario, you can execute relevant steps from the Make-to-Stock Production – Discrete Manufacturing (BJ5) test script, using the master data from this document.

- Create Initial Material Stock
- Create Planned Independent Requirements
- Material Requirements Planning
- Monitor Material Coverage
- Create Production Order
- Release Production Order
- Confirm Production Order for SemiFinished Product

Procedure

The simplified procedures are described as follows.

Create Initial Material Stock (for RM20 and SG29)

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Stock (F1062). | The Manage Stock screen displays. |  |
| 3 | Specify Material and Plant | Make the following entries and choose Enter:Material: RM20 or SG29Plant: 3310 |  |  |
| 4 | Select Storage Location | Choose button in column Unrestricted-Use Stock, line Std. storage 2 (331B). | The Manage Stock pop-up is displayed. |  |
| 5 | Enter Quantity | Make the following entries and choose Post:Stock Change: Initial EntryQuantity: 100 PCDocument Date: <Date>Posting Date: <Date> | A success message is displayed and stock is increased by the specified amount. |  |
| 6 | Check Material Document (Optional) | Click Material document xxx/yyyy created and review document details. | Document is O.K. |  |

Create Production Order and Release Production Order

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On to SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Create Production Order (CO01). | The Production Order Create: Initial screen displays. |  |
| 3 | Enter the Order Information | Make the following entries:Material: FG129Production Plant: 3310and choose Enter. | The Production Order Create: Header screen displays. |  |
| 4 | Enter the Order Details | Make the following entries and choose Enter:Quantities - Total Qty: for example, 100 PCScheduling - Type: <Current Date> | A message All checked materials in order are available appears. Otherwise, please check the initial material stock. |  |
| 5 | Release Order | Choose Release Order. | Releases are carried out. |  |
| 6 | Save | Choose Save and make a note of your production order number. | Order number XXX is saved. |  |

Confirming Assembly Activities (Finished Goods) for operation 0010.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Confirm Production Operation (F3069). | The Enter Order and Operation screen displays. |  |
| 3 | Enter Production Order and Operation | On the Enter Order and Operation screen, make the following entries and choose Enter:Order: The order number you noted for the material Finished Good MTS (FG129)Operation: 0010 |  |  |
| 4 | Enter Fields in Quantities Section | In Quantities section, make the following entries:Yield: <Enter the amount you want to Confirm>Scrap: <Enter the amount you want to Scrap>Rework: <Enter the amount you want to Rework>Reason for Variance: <Enter the variance reason if required, for example, 0001> |  |  |
| 5 | Save your entries | Click Post and Complete to make final confirmation for this operation. | Confirmation has been created. |  |

Result

A production order for material FG129 was created, which contains an operation (0020) for quality inspection.

##### Display Routing for Inspection Characteristics

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

An inspection during production is triggered by the release of a production order. When you save the production order, an inspection lot is generated for operation 0020. An inspection lot for an inspection during production is not stock relevant.

In this step we review the automatically created inspection point for operation 0020 as well as the inspection characteristics which will have to be maintained in the Quality inspection step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Engineer - Discrete Manufacturing. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Display Routing (CA03). | The Display Routing: Initial Screen displays. |  |
| 3 | Enter Selection Fields | Make the following entries and choose Continue.Material: FG129Plant: 3310 |  |  |
| 4 | Review the Inspection Points Setting | Double-click Operation 0020.Scroll down to the Quality Management: Inspection Points section.After reviewing, choose Back. | A Time-related inspection point is defined for this operation in the routing. |  |
| 5 | Review the Inspection Characteristics | Select Operation 0020 and choose Inspection Characteristics.There are three Master Inspection Characteristics: One is Qualitative – SurfaceThe others are Quantitative - Length and Diameter | If Inspection Characteristics is not displayed, choose More. In the dialogue box, find Inspection Characteristics. |  |

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
| 2 | Access the App | Open Quality Technician Overview (F2361). | The Quality Technician Overview (F2361) screen displays.You can get an overview of the inspection lots with open results recording and the inspection lots without an inspection plan. |  |

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
| 3 | Enter Filter Fields | Make the following entries and choose Go.Plant: 3310Material: FG129Inspection Lot Status: Outstanding |  |  |
| 4 | Select the Corresponding Inspection Lot | In the inspection lot list, select the inspection lot with column Production Order equals to the Production Order: XXX (from previous step). | The Production Order number assigned with Inspection Lot.If the Production Order column does not appear, please choose the button Settings. In the View Settings dialog box, select Production Order and choose OK. |  |
| 5 | Check Inspection Lot | Under Origin, check the sample size. | The sample size is automatically calculated for the inspection lot, using the definition of sampling procedures, which are assigned to the inspection characteristics and reviewed in an earlier step. |  |

##### Quality Inspection

###### Display Inspection Methods

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection method is reviewed with attached document.

Prerequisite

The step of BNQ in Business Conditions is completed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Technician. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Inspection Methods (F0311A). | The Inspection Method screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Plant: 3310Inspection Method: SURFACE |  |  |
| 4 | Select Inspection Methods | In the Inspection Methods list, click the Inspection Method Surface. | Inspection Method is displayed. |  |
| 5 | Check Inspection Method and the Attached Document | Verify the General Information.Under Documents, check the document. |  |  |

###### Record Inspection Results Before Activation of the Control Chart

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you perform the inspection and record the result to decide if you can go on with the next operation of the production order. The result is recorded in the inspection lot according to the defined inspection parameters in the routing.

The master inspection characteristic diameter is valuated leveraging a SPC control chart. If the control chart has not been activated, yet, the user must valuate the characteristic manually. After activation of the control chart, the respective characteristic is automatically valuated by the system according to the control charts action limits.

As it is currently not possible to specify the control charts limits manually, a minimal amount of data points must have been collected before the card can be activated.

Prerequisite

The inspection is processed based on inspection lot. In this scope item, the inspection lot is automatically created upon release of the production order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Record Inspection Results - Hierarchical Worklist (QE51N). | The Results Recording Worklist screen displays.Note The app Record Results for Inspection Points (F2689) can be used as an alternative to capture inspection results for inspection points. However, manual valuation of an inspection characteristic with an inactive SPC card is only possible using the Record Inspection Results - Hierarchical Worklist (QE51N) app. |  |
| 3 | Enter Selection Fields | Make the following entries and choose Execute.Plant： 3310Insp. Lot Origin： 03Material: FG129 | The Results Records: Characteristic Overview screen displays. |  |
| 4 | Select the Corresponding Inspection Lot | On the left pane, expand the corresponding inspection lot which you want to record a result. | If a dialogue appears asking to save, choose Cancel. |  |
| 5 | Choose the First Inspection Point | Choose the first inspection point Date/Time which is under the activity 0020 Final work and quality inspection Work Center Work for machine/person. | The Record Results: Characteristic Overview page opens. |  |
| 6 | Enter Inspection Result for the First Inspection Point | Depending on the inspection result, select one of the following two options and then confirm with Choose.Positive ResultSurface – Result: 0020 (Smooth)Length – Result: 170Diameter – Result: 20.0, 20.3, 20.1, 19.8, 19.9Manual Valuation: acceptNegative ResultSurface – Result: 0010 (Rough)Length – Result: 90Diameter – Result: 20.9, 21.0, 20.0, 21.1, 21.3Manual Valuation: reject | For the qualitative characteristic surface the search help is needed to select a value.For the quantitative characteristic length a number can be entered directly.For the quantitative characteristic diameter five independent values need to be input and the system will calculate the mean value. |  |
| 7 | Close the First Inspection Point | Choose Enter. | The valuation and close are performed automatically for characteristics surface and length. Characteristic diameter must be valuated manually until there is an active control chart.. The status is set to 5 Processing is completed. |  |
| 8 | Save the First Inspection Point | Choose Save.Optional: Confirm produced quantity, e.g. 25 pc | The first inspection point is saved. |  |
| 9 | Create the Next Inspection Point | Choose Next Inspection (Shortest Interval 30 Min) which is under the activity 0020 Final work and quality inspection Work Center Work for machine/person with a click. | The next inspection point is created with current Date/Time.Normally, the next inspection point is created after 30 minutes. |  |
| 10 | Enter Inspection Result for the Next Inspection Point | Depending on the inspection result, select one of the following two options:Positive Result: see aboveNegative Result: see above | For the qualitative characteristic surface the search help is needed to select a value.For the quantitative characteristic length a number can be entered directly.For the quantitative characteristic diameter five independent values need to be input and the system will calculate the mean value.Note If you want to use the function of control chart, please repeat this step to have enough data for the system to calculate the warnings and control limits. |  |
| 11 | Close the Next Inspection Point | Choose Enter. | The valuation and close are performed automatically for characteristics surface and length. Characteristic diameter must be valuated manually until there is an active control chart.The status is set to 5 Processing is completed. |  |
| 12 | Save the Next Inspection Point | Choose Save.Optional: Confirm produced quantity, e.g. 25 pc | The next inspection point is saved. Quality Inspection for in-process control is performed and the result is recorded. |  |

###### Analyze and Activate Control Chart (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can display the control chart in graphical and tabular form. If you have collected enough data that describes the statistical variation of your manufacturing process, you can execute this step to activate a control chart. After activating a control chart, the corresponding inspection characteristics will be valuated against this control chart.

Prerequisite

For your control chart, enough (valid, e.g. statistically reliable) data must be available for the system to calculate warning and control limits.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open app Manage Control Charts (F2810). |  |  |
| 3 | Enter Selection Fields | Make the following entries and press Enter:Plant: 3310Master Insp. Charac: DiameterMaterial: FG129 |  |  |
| 4 | Check Visual Filters (Optional) | Switch visual filter from compact filter to get different filters, for example, Quality control chart by work center. |  |  |
| 5 | Check Number of Deviations (Optional) | In the Chart View, the number of deviations per time is displayed. Adapt visualization to analyze data. |  |  |
| 6 | Select the Corresponding Control Chart | In the Table View, select a control chart. | The control charts page displays. |  |
| 7 | Display and Analyze Control Chart Data | In the header, time progression of recorded results and statistical information are displayed.In the chart part, a respective graph with all the inspection results recorded is displayed.Statistical Information, Bill of Operations, Characteristic are also available for analysis. |  |  |
| 8 | Activate Control Chart | In the header, choose Calculate and Activate. | Control chart is active and can therefore be used for automatic valuation of inspection characteristics. |  |
| 9 | Deactivate Control Chart (Optional) | If a control chart has become obsolete, it can be deactivated. Select the respective line item in the list table and choose Complete. | Control chart is deactivated.Note Execute this step only when this control chart is obsolete. |  |

###### Record Inspection Result After Activation of the Control Chart

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform the inspection and record the result to decide if you can go on with the next operation of the production order. The result is recorded in the inspection lot according to the defined inspection parameters in the routing.

Prerequisite

The inspection is processed based on inspection lot. In this scope item, the inspection lot is automatically created upon release of the production order.

Procedure

Record inspection results as described in chapter Record Inspection Result Before Activation of the Control Chart. As characteristic diameter is now automatically valuated leveraging a SPC control chart, the manual valuation described above is not necessary here.

###### Display Quality Engineer Overview (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection is done and the inspection result is recorded. You must decide whether or not to accept the inspection lot depending on the inspection result. As an optional entry point for making this usage decision, you can use the app Quality Engineer Overview (F2360). Furthermore, the Quality Engineer Overview (F2360) app displays inspection lots without an inspection plan (e.g. if automatic assignment of an inspection plan is not set up in the material master or if automatic assignment failed), inspection lots without usage decision, inspection lots ready for usage decision. If negative inspection results are recorded, you can check the detect details in app Manage Defects (F2649) directed from the app Quality Engineer Overview (F2360) via the cards Inspection Lots with Defects, Top Defective Materials, or Top Defective Codes.

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
| 6 | In Card: Inspection Lots with Defects (optional) (Cloud only) | (In case negative inspection results have been recorded) Select one of the inspection lot origins, then you will be directed to app Manage Defects (F2649) automatically. Choose the relevant defect ID to check the details of the defect. | The defect details are displayed. |  |
| 7 | In Card: Top defective materials (optional) (Cloud only) | (In case failed inspection results have been recorded) Select one of the materials inspected, then you will be directed to app Manage Defects (F2649) automatically. Choose the relevant defect ID to check the details of the defect. | The defect details are displayed. |  |
| 8 | In Card: Top defective codes (optional) (Cloud only) |  |  |  |
| 9 | In Card: Exceeded Action Limits (optional) (Cloud only) | (In case Deviations exist in results recording with control chart management) Select the bar of the deviation by work center, then you will be directed to app Manage Control Charts (F2810)Manage Control Charts automatically. Refer to step [Analyze and Activate Control Chart (Optional)](#unique_36) [page ] 55 for more details. |  |  |

###### Make Usage Decision

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection is done and the inspection result is recorded. You must inform the Production Operator – Discrete Manufacturing of the inspection results to confirm the operation 0020 in the production order and to go on with the next processing step.

After recording of the inspection result by the quality technician, the quality engineer can now make a usage decision.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Usage Decisions (F2345). | The Manage Usage Decisions (F2345) screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Plant: 3310Material: FG129Usage Decision Made: No |  |  |
| 4 | Click the Corresponding Inspection Lot | In the inspection lot list, select the inspection lot with column Production Order: XXXX (From previous step). | If the Production Order column does not appear, please choose the Settings button. In the View Settings dialog box, select Production Order and choose OK. |  |
| 5 | Review of Inspection Points | Select the tab Inspection Points, and review the detailed inspection results recorded previously. (From previous step – Create Production Order for Final Assembly) |  |  |
| 6 | Display Defects | Scroll down to the Defects area. Check the details of Defects. | Only available when you have recorded a Negative result. |  |
| 7 | Enter UD code | Choose Edit and select the tab Usage Decision. The UD code you select depends on the Inspection Result, please select one of the following two options:Positive ResultUD code: UD03 A (Accepted)Negative ResultUD code: UD03 R (Rejected) |  |  |
| 8 | Save Usage Decision | Choose Save. | Usage decision has been made for in process control inspection lot.Following a positive usage decision, you can now confirm the operation of the production order and perform the next operation of the production order. |  |

##### Confirm Production Order Operation

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
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Confirm Production Operation (F3069). | The Perform Work screen displays. |  |
| 3 | Enter Production Order and Operation | On the Perform Work screen, make the following entries and Choose Enter:Order: XXX (from previous steps)Operation: 0020 |  |  |
| 4 | Enter Fields in Quantities Section | In Quantities section, make the following entries:Yield: Quantity of prod. order less scrapScrap: Quantity of products that did not successfully pass the quality inspection |  |  |
| 5 | Save your entries | Click Post and Complete to make final confirmation for this operation. | Confirmation has been created. |  |

##### Review Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the release or confirm of finished goods orders is performed, the production supervisor could display and check the order using the app Manage Production Orders for the Finished Good MTS FG129.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Production Orders (F2336) | The Manage Production Orders (F2336) screen displays. |  |
| 3 | Select Production Order | On the Manage Production Orders (F2336) screen, make the following entries:To check Default Area of Responsibilities (supervisor), select the user (from the top corner):App Settings > Area of Responsibility Production Supervisor . Check only this entry is displayed.3310MTS DI - Valuated (YB1)Click Adapt Filters to display more selection filter. Click More filters under Material and Plant. Check the checkbox for Material and Plant and click Go. Click OK. Material and Material fields are then added to filter bar.Material: FG129Plant: 3310Click Go to execute. | Selected order displays. |  |
| 4 | Check detailed operations status | Check detailed information for selected production operations.Issue:Empty if there is no issue for production order.Delay or Missing Components / PRT issue or Quantity Deviation / Quality Issue information shows if relevant issue exists.Components:Material, total quantity and Issued / open quantity information for order components displaysOrder Schedule:Detailed operation information with relevant work center, confirmed quantity, start and end time displays.Work Center Schedule:The relevant order that covering the same work center capacity (operation is partially confirmed) displayed.Operations not Started:The relevant order that would cover the same work center capacity (operation is released) displayed.Confirmation:Detailed confirmation information with Yield, Scrap, Rework quantity displays if confirmation executed.Inspection:Detailed inspection lots information displays if existed | Detailed operations status displays. |  |

##### Make-to-Stock Production – Discrete Manufacturing (BJ5)

Procedure

To execute this activity, process the following steps using the master data from this document (see also table below):

| Master data | Value | Comments |
| --- | --- | --- |
| Production Order | XXX | From previous steps |
| Operation Number | 0030 | Last Operation Number |
| Material | FG129 | Finished product |
| Plant | 3310 |  |

Steps to process from scope item Make-to-Stock Production – Discrete Manufacturing(BJ5)

Final Confirmation of Production (Finished Goods)

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Confirm Production Operation (F3069). | The Perform Work screen displays. |  |
| 3 | Enter Production Order and Operation | On the Perform Work screen, make the following entries and choose Enter:Order: XXX (from previous steps)Operation: 0030 |  |  |
| 4 | Enter Fields in Quantities Section | In Quantities section, make the following entries:Yield: <Enter the amount you want to Confirm>Scrap: <Enter the amount you want to Scrap> |  |  |
| 5 | Save your entries | Click Post and Complete to make final confirmation for this operation. | Confirmation has been created. |  |

Posting Goods Receipt for Production Order

Execute step Post Goods Receipt for Production Order of process variant Quality Management in Discrete Manufacturing - Goods Receipt from Production with the following parameters:

- Order Number: XXXX (From previous steps)

Result

The production order was finally confirmed and goods receipt posted.

#### Quality Management Within Production Process - Make-to-Stock Production of a Batch Managed Material

Purpose

In this process, the batch-managed semi-finished product QM006 (e.g. bottled blue ink) is produced. The routing contains a quality-inspection operation with inspection points in order to monitor the quality during the production process.

##### Create Raw Material Stock

Purpose

In a real business case, the materials are usually purchased from external suppliers. In that case, process is covered by the standard purchasing or subcontracting processes. For the purpose of this test, we post initial stock directly to the Issue Storage Location.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Warehouse Clerk. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | Screen name adapts according to entries. |  |
| 3 | Choose Goods Receipt - Other | Make the following entries and press Enter:Trans./Event: Goods ReceiptReference Document: OtherMovement Type: 561 | Screen name after entries are made. |  |
| 4 | Specify Material | On the Material tab, make the following entries:Material: RMPI002 | Ensure that detail data is expanded. |  |
| 5 | Specify Quantity | On the Quantity tab, make the following entries:Qty in Unit of Entry: For example, 1000 |  |  |
| 6 | Specify Plant and Storage Location | On the Where tab, make the following entries:Plant: 3310Storage location: 331B |  |  |
| 7 | Check Item | Press Enter, and ensure Item OK is selected. |  |  |
| 8 | Add Other Materials | Choose Next Item, then repeat the steps 4 to 7 for the following materials:Material: RMPI003Material: RMPI004Material: RMPI005 |  |  |
| 9 | Post Goods Movement | Choose Post. | Material document XXX posted.Materials are available in stock. |  |

##### Create and Release Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

For demo purposes, we directly create a production order without a planned production order. For a more comprehensive process, please review scope item BJ5 or 2UG.

Procedure

|  |
| --- |
| Note The example data is set up such that the production order is released automatically (check production scheduling profile YB0005 on tab Work Scheduling in the material master) before the batch is created on the Goods Receipt tab of the Production Order. Therefore, the inspection lot might not contain the batch number as the lot is created automatically at release of the order. The user has the following options:Manually maintain the inspection lot ID in app Manage Inspection Lots (F2343) or Record Usage Decision (QA11).Assign a different production scheduling profile in the material master that does not automatically release the order (e.g. YB0001).Change settings of production scheduling profile YB0005 in SSC-UI so that the order is not automatically released. |

Refer to test procedure Quality Management in Discrete Manufacturing - Within Production Process, step Make-to-Stock Production - Discrete Manufacturing (BJ5), procedure Create Production Order and Release Production Order with the following data:

- Material: QM006
- Production Plant: 3310
- Quantities - Total Qty: 100 kg
- Scheduling - Type: Current Date
- Make sure that a new batch has been created on tab Goods Receipt of the production order.
- Note Order ID: _____________________________
- Note Batch Number: _______________________

##### Goods Issue of Batch-Managed Components via Pick List

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The withdrawal of the raw materials is used for the order. This withdrawal can be done by using the picking list or doing a manual goods issue.

|  |
| --- |
| Note If the material is set for backflush (in material master or resource), the withdrawing is done automatically after you confirm the operation or the whole order. Backflushing should not be used for batch-managed components (to ensure that the physically picked and consumed batch is the same as the recorded batch). |

Prerequisites

Ensure that sufficient material is present on stock. If not enough stock is present, execute Create Raw Material Stock in the preliminary steps of this scope item.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori Launchpad displays. |  |
| 2 | Access App | Open Pick Components for Production Orders (CO27). | The Picking List: Initial Screen displays. |  |
| 3 | Enter Restriction and Execute | Make the following entries and choose Execute:Profile: 000002Production Order: <XXXX> (from previous steps)Plant: 3310 | The Order Information System: Detail List of Components screen displays. |  |
| 4 | Picking Raw Materials | Select the relevant reservations and choose the upper left Picking. | The Picking list screen displays. On this screen, a list of all the selected reservations is displayed. |  |
| 5 | Batch Determination | Some materials are management by batch (for example RMPI002, RMPI003, RMPI004, and RMPI005). Select corresponding line item(s) and choose Batch Determination. | The Batch Determination MM: Select Batches screen displays. |  |
| 6 | Enter Detail | Make the following entries and Choose Copy.Split quantity: <Quantity>. | Back to Picking list screen.If multiple line items were selected in step 5, the Picking list screen is displayed after completion of the last line item. |  |
| 7 | Post | Choose Post to post the goods movements. | The goods movements have been posted. |  |

##### Confirm Production Operations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In the process industry, GR and GI postings are usually done immediately during the physical movements of the materials to ensure batch traceability and data consistency. Order confirmations with backflush are done at shift end or day end. The sum of the GI and GR quantity for the given order is then recorded within the confirmation and scrap quantities (optional). The time ticket confirmation allows recording either the default times for machine and labor usage, or record actual times for major deviations.

After a production operation is completed, the production operator confirms the production operation in the system so that the next operation can be started. He reports quantities (e.g. yield, scrap, rework) and times (e.g. machine preparation time, labor time, etc.).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Confirm Production Operation (F3069). | The Enter Order and Operation screen displays. |  |
| 3 | Enter Order and Operation | Make the following entries and choose Go:Order: <Order ID>Operation: 0010 | The Confirm Production Operation screen displays. |  |
| 4 | Check Quantities and Post Confirmation | On the Quantities tab, enter quantities:Yield: <enter the amount you want to confirm>If the actual quantity is not equal to the planned quantity, make respective entries:Scrap: <enter the amount you want to scrap>Reason for variance: <Select an entry>Choose Post and Complete.Optional: Review/change data on tab Activities before posting:Machine: <enter the setup time you want to confirm for this operation>Labor: <enter the setup time you want to confirm for this operation> | Production order operation is confirmed and completed. |  |
| 5 | Check Material Movements (Optional) | In Material Movements section, check the material list. | The system shows you an overview table of all materials for which the withdrawing is done automatically with the confirmation of the operation.The material RMPI001 is set for backflush (in material master) so that the withdrawing is done automatically after you confirm the operation. |  |
| 6 | Post Confirmation | Choose Post and Complete, execute steps 3 - 5 for operation 0020 of the same production order. | Production order operation is confirmed and completed. |  |

##### Execute Quality Inspection With Inspection Points

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the quality technician performs the quality inspection and records the inspection result(s) in order to decide whether the next operation of the production order can be executed. The result is recorded in the inspection lot according to the defined inspection parameters in the routing. Here, time-based inspection points are used for result recording. Leveraging inspection points, you can have several inspections and can record multiple sets of characteristic results for a single operation. Each inspection point is valuated separately with a coded valuation.

Prerequisite

The inspection is processed based on inspection lot. In this scope item, the inspection lot is automatically created upon release of the production order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access App | Open Record Results for Inspection Points (F2689). | The Record Results for Inspection Points screen displays. |  |
| 3 | Execute Search | If not already shown, expand search header, make the following entries and choose Go:Order: <Order ID> | Order is displayed in the result list. |  |
| 4 | Open Inspection Points | Click on the line item of the search result. | A list of inspection points is displayed. If inspection point data have not been captured, the default for the first inspection point is displayed. |  |
| 5 | Create New Inspection Point | Click the pencil icon to create a new inspection point | Record Results for Inspection Points screen is displayed. |  |
| 6 | Maintain Inspection Results | Maintain the following inspection results (either positive or negative):a) Positive ResultVisual Inspection: QUAL01 – OKAbsorption Maximum: 450 nmValuation: Accepted (A)b) Negative ResultVisual Inspection: QUAL01 – NOKAbsorption Maximum: 440 nmValuation: Rejected (R)Choose Save. | Inspection point data is saved and the system displays the list of inspection points. |  |
| 7 | Create New Inspection Point and Maintain Inspection Results (Optional) | Create a new inspection point as described in step 5 and maintain inspection results as described in step 6. | Further inspection points with inspection results are captured. |  |

##### Confirm Production Operations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

Confirm production operations 0030 and 0040 as described in chapter Confirm Production Operations.

##### Post Goods Receipt for Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

The purpose of this activity is to post the goods receipt for the production order. You may post goods receipt for the total quantity or partial quantities if the production has not finished, yet. In the latter case, the partially completed production operations should be confirmed without the final completion status until production is completed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Post Goods Movement (MIGO). | Screen adapts according to entries. |  |
| 3 | Choose Goods Receipt - Other | Make the following entries and press Enter:Trans./Event: Goods ReceiptReference Document: OrderOrder Number: XXXX (from previous steps)Make sure that the correct movement type (101) is entered. |  |  |
| 4 | Enter a Date of Manufacture | Data on the Material, Quantity, Where and Batch tabs are derived from the order information.Enter a Date of Manufacture on tab Batch. |  |  |
| 5 | Check Item | Ensure Item OK is selected. | The Goods Receipt screen displays. |  |
| 6 | Post Goods Movement | Choose Post. | Material document XXX posted.Materials are available in stock. |  |

##### Make Usage Decision

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In order to close the inspection lot, the quality engineer makes a usage decision. As the inspection lot of origin 03 is not stock-relevant, there is no follow-up action assigned to the usage decision code that triggers a goods movement.

Procedure

Refer to test procedure Quality Management in Discrete Manufacturing - Within Production Process, step Quality Inspection – Make Usage Decision and make either a positive or negative usage decision (depending on the inspection results).

##### Review Batch Data (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

In order to transfer inspection results to batch characteristics, the inspection lot must contain the batch number. Please make sure that the prerequisites mentioned in chapter Create and Release Production Order are fulfilled.

Purpose

The batch class YB_QM is assigned to the batch-managed material QM006. The batch class contains characteristics for information related to the usage decision (usage decision code and quality score) as well as inspection characteristics. In this step, the batch classification of the produced batch is displayed.

By transferring inspection results to classification data, the data can be used for example in a batch-search strategy to find products with specified characteristics.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access App | Open Manage Batches (F2462). | The Manage Batches screen displays. |  |
| 3 | Execute Search | Maintain the following search fields and choose Go:Material: QM006Batch: <Batch Number> (Obtained at order creation)Plant: 3310 | Search result displays. |  |
| 4 | Navigate to Batch Details | Choose the line item of the respective batch by clicking the triangle displayed on the right. | Batch details are displayed on screen Batch. |  |
| 5 | Review Data | Review tabs:General Information displays the manufacturing date entered during goods receiptClassification displays the classification data of the batch. The fields Quality Score Usage Decision and Usage Decision are automatically populated with the usage decision data. The fields QM: Absorption Maximum and QM: OK / Not OK are populated at the valuation of an inspection point. If multiple inspection points have been captured, data originates from the last inspection point. | Batch information is reviewed. |  |

### Quality Management in Process Manufacturing

Purpose

This procedure focuses on in-process quality inspections and inspections upon goods receipt from production as an extension to scope item BJ8 - Make-to-Stock – Process Manufacturing Based on Process Order. Not all steps are required to run through this end-to-end business scenario.

|  |
| --- |
| Note For detailed instructions about end-to-end business processes in process manufacturing based on process order (In-Process Inspection for Semi Finished Good), refer to scope item BJ8 - Make-to-Stock – Process Manufacturing Based on Process Order. |

#### Quality Management in Process Manufacturing – In-Process Inspection for Semi Finished Goods

##### Create Process Orders

Purpose

This process step shows you how to create process orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Process Order (COR1). |  |  |
| 3 | Enter Order Information | Make the following entries:Material Number: SGQMProduction Plant: 3310Process Order Type: YBM2Choose Continue. |  |  |
| 4 | Enter General Data | Under the tab General Data, enter the following entries:Total Qty : for example, <5>Type: Current DatePress Enter and choose Save. | The process order is created. |  |

##### Display Open Inspection Lot (Optional)

Purpose

In this optional step, the references to the Order and the status are verified.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Technician. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Inspection Lots (F2343). | The Manage Inspection Lots screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Plant: 3310Material: SGQMInspection Lot Status: Outstanding |  |  |
| 4 | Select the Corresponding Inspection Lot | In the inspection lot list, choose the inspection lot where the column Production Order matches the value of the Order: XXX from the previous step. | If the Production Order column does not appear, choose the Settings icon. In the View Settings dialog box, select Production Order and choose OK. |  |
| 5 | Check Inspection Lot | In the header area, check the status. | Inspection Lot is Released. |  |

##### Results Recording for Inspection Point Before Activation of Control Chart

Purpose

In this step the result is recorded in the inspection lot according to the defined inspection parameters in the recipe. The master inspection characteristic enabled for SPC is valuated leveraging an SPC control chart. Since the control chart has not been activated yet, the user must valuate the characteristic manually. After activation of the control chart, the respective characteristic is automatically valuated according to the control charts action limits. As it is currently not possible to specify the control charts limits manually, a minimal amount of data points must be collected before the chart is activated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Technician. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Record Inspection Results - Hierarchical Worklist (QE51N) | The Results Recording Worklist screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Execute.Plant: 3310Insp. Lot Origin: 03 (Production)Material: SGQMDefault Next Inspection Point: selected | The inspection point is displayed. |  |
| 4 | In Process Result Recording | In the Record Results: Characteristic Overview, enter an inspection result for the characteristic and press Enter.Note Ensure that the standard deviation (Std. Dev.) is entered. This is required for the used control chart type and must be done manually for characteristics with summarized results recording. |  |  |
| 5 | Characteristic Valuation | Choose the Valuate icon to valuate the entered inspection result manually. | Characteristics is accepted. |  |
| 6 | Save | Save the result recording. | Inspection point is valuated and saved. |  |
| 7 | Record Results for the Next Inspection Point | Repeat Step 2-6 for the next inspection points. |  |  |

##### Analyze and Activate Control Chart (Optional)

Purpose

If you have collected enough data that describes the statistical variation of your manufacturing process, you can execute this step to activate a control chart. After activating a control chart, the corresponding inspection characteristics will be valuated against this control chart.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Control Charts (F2810). |  |  |
| 3 | Enter Selection Fields | Make the following entries and choose Go.Plant: 3310Material: SGQM |  |  |
| 4 | Select the Corresponding Control Chart | In the Control Charts table, choose a control chart for your inspection. | The control charts page displays. |  |
| 5 | Display and Analyze Control Chart Data | In the header area, time progression of recorded results and statistical information are displayed.In the chart part, a respective graph with all the inspection results recorded is displayed.Statistical Information, Bill of Operations, and Characteristic are also available for analysis. |  |  |
| 6 | Activate Control Chart | In the header area, choose Calculate and Activate. | The control chart is active and can therefore be used for automatic valuation of inspection characteristics. |  |
| 7 | Deactivate Control Chart (Optional) | If a control chart has become obsolete, it can be deactivated. Select the respective line item in the list table and choose Complete. | The control chart is deactivated.Note Execute this step only when this control chart is obsolete. |  |

##### Results Recording for Inspection Point After Activation of Control Chart

Purpose

After activating the control chart, the corresponding inspection characteristics are valuated against this control chart.

Procedure

Chapter [Results Recording for Inspection Point Before Activation of Control Chart](#unique_55) [page ] 75 describes how to record inspection results. Since characteristic YPIQNSPC is now automatically valuated leveraging an SPC control chart, the manual valuation described above is not necessary here.

##### Record Usage Decision

Purpose

The inspection is completed, and the inspection results are recorded. Use this step to perform usage decision for inspection lots. Since the inspection lot of origin 03 is not stock-relevant, no follow-up action is assigned to the usage decision code that triggers a goods movement.

Prerequisites

To perform the usage decision for batch-managed inspected materials, assign the batch within the inspection lot. In the in-process inspection, the batch number is transferred from the process order into the inspection lot during inspection lot creation.

Based on the customizing of the production scheduling profile used in scope item BJ8 - Make-to-Stock – Process Manufacturing Based on Process Order, the batch is not automatically created and cannot be manually added to the process order before its release. This is because the process order gets released automatically. Therefore, you must assign the batch manually to the inspection lot.

| Test Step # | Test Step Name | Instruction | Expected Result | Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Inspection Lots (F2343). | The Manage Inspection Lots screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Plant: 3310Material: SGQMInspection Lot Origin: ProductionInspection Lot Status: Outstanding |  |  |
| 4 | Select the Corresponding Inspection Lot | In the inspection lot list, choose the inspection lot where the column Production Order matches the value of the Order: XXX from the previous step.Choose Change Inspection Lot from the pop-up card. | If the Production Order column does not appear, choose the Settings icon. In the View Settings dialog box, select Production Order and choose OK. |  |
| 5 | Assign Batch | In the header area, choose Create Batch or enter a batch manually. |  |  |
| 6 | Save Inspection Lot | Choose Save. | The batch is assigned to Inspection Lot. Note down the batch number. |  |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Usage Decisions (F2345). | The Manage Usage Decisions screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Inspection Lot Origin: ProductionPlant: 3310Material: SGQMUsage Decision Made: No |  |  |
| 4 | Click the Corresponding Inspection Lot | In the inspection lot list, choose the inspection lot where the column Production Order matches the value of the Process Order: XXXX from the previous step. | If the Production Order column does not appear, choose the Settings icon. In the View Settings dialog box, select Production Order and choose OK. |  |
| 5 | Review of Inspection Points | Choose the tab Inspection Points and review the detailed inspection results recorded previously. |  |  |
| 6 | Display Defects (optional) | Scroll down to the Defects area. Check the details of defects. | Only available when you have activated defects recording in master data and recorded a negative result. |  |
| 7 | Enter UD code | Choose Edit. Choose the tab Usage Decision. The UD code you select depends on the Inspection Result. Choose one of the following two options:Positive ResultUD code: UD03 A (Accepted)Negative ResultUD code: UD03 R (Rejected) |  |  |
| 8 | Save Usage Decision | Choose Save. | Usage decision is made for the in-process control inspection lot. |  |

##### Confirm Production

Purpose

The confirmation documents include the processing status of orders, operations, phases, and individual capacities. It is an instrument to control orders. The time ticket confirmation allows recording either the default times for machine and labor usage, or actual times for major deviations. Backflushed materials are posted automatically during respective phase confirmations. This process step shows you how to confirm production. You can post scrap quantities as an option. If no major deviations occur, you need to confirm only the last phase (milestone). Using milestone confirmation, all prior phases are confirmed automatically.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Confirm Process Order Phase (COR6N). | The Enter Time Ticket for Process Order screen displays. |  |
| 3 | Enter Confirmation Option | Make the following entries and then press Enter.Order: XXXX (from previous steps)Press Enter or select phase (0025 for SGQM) from search help of the Phase field.Confirm.type: Final confirmation | If the system shows the message Total quantity confirmed not equal to planned quantity to be confirmed, press Enter to ignore it. |  |
| 4 | Propose Actual Data | Choose Actual Data.Make the following entries:Scrap: <enter the amount you want to Scrap>Yield: <Based on the origin quantities minus Scrap>Reason for Var: <Enter scarp reason if need>, for example, 0001 | The Quantities and Activities will be filled automatically. |  |
| 5 | Save Confirmation | Save your entries. | The final confirmation of the last operation is carried out. Costs and activity quantities are recalculated in proportion to the yield quantity.Backflushed components are issued with the confirmation posting automatically (packaging material RM15 within the confirmation of orders for finished product PI FG29). |  |

##### Post Goods Receipt for Process Order

Purpose

When quality inspection of type 04 is activated, this activity triggers the Quality Inspection on Goods Receipt from Production. The semi-finished good is posted to quality inspection stock and an inspection lot is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Initial screen displays. |
| 3 | Enter Process Order | Make the following entries and then press Enter:Trans./Event: Goods ReceiptReference Document: OrderOrder Number: XXXX (from previous steps)Movement Type: 101 | Screen name adapts after entries are made. |
| 4 | Enter Date of Manufacture | Choose the Batch tab, and make the following entries:Date of Manufacture: Current Date | Note Please be informed that instruction of step 4 is only available for SAP delivered standard content as some customizing changes in SSCUI could make things different.Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |
| 5 | Check Item | Select item OK. | Ensure that detailed data is expanded. |
| 6 | Post Goods Movement | Choose Post. | The goods movements are posted. The batch number is created automatically during the posting. Production date and shelf life expiration date are recorded within the batch master of the finished product. |

#### Quality Management in Process Manufacturing - Goods Receipt from Production for Semi Finished Goods

##### Display Open Inspection Lot (Optional)

Purpose

In this optional step, you verify the references to the orders and batches. You also review the material documents and sample sizes used for quality inspection.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Inspection Lots (F2343). | The Manage Inspection Lots screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Plant: 3310Material: SGQMInspection Lot Status: Outstanding |  |  |
| 4 | Select the Corresponding Inspection Lot | In the inspection lot list, choose the inspection lot where the column Production Order matches the value of the Order: XXX from the previous step. | If the Production Order column does not appear, choose the Settings icon. In the View Settings dialog box, select Production Order and choose OK. |  |
| 5 | Check Inspection Lot | In the header area, check the batch number.Under the Origin tab, check the material document and sample size.Under the General tab, check the task group and counter. | Batch number is visible. |  |

##### Record Inspection Results

Purpose

In this process step, the in-process inspection results on goods receipt from production are recorded for material SGQM. This allows you to inspect the goods received from production before they are posted out of inspection stock when you make the usage decision.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Quality Technician. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Record Inspection Results - Hierarchical Worklist (QE51N). | The Results Recording screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Plant: 3310Insp. Lot Origin: 04 (Goods receipt from Production)Material: SGQMBatch: As noted in previous chapterIf Batch is not displayed as a filter, choose Filters. In the popup dialog Filters, choose Materials. Select Batch and choose OK. Choose Go. | Note down the inspection lot number. |  |
| 4 | Select the Corresponding Inspection Lot | In the inspection lot list, choose the inspection lot and click on Record Multiple Results. |  |  |
| 5 | Enter Inspection Result | On the Record Results: Characteristic Overview screen, enter an inspection result for the characteristics. | A green tick is displayed when the characteristics get valuated. |  |
| 6 | Save Inspection Lot | Choose Save. | The inspection lot is saved. |  |

##### Record Usage Decision

Purpose

The inspection is completed, and the inspection results are recorded. In this process step, the appropriate batch is evaluated concerning its usage. With Inspection Type 04, the material movement is done based on the usage decision codes.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Usage Decisions (F2345). | The Manage Usage Decisions screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Inspection Lot Origin: Goods Receipt from ProductionPlant: 3310Material: SGQMUsage Decision Made: No |  |  |
| 4 | Click the Corresponding Inspection Lot | In the inspection lot list, choose the inspection lot where the column Order matches the value of the Process Order: XXXX from the previous step. | If the Order column does not appear, choose the Settings icon. In the View Settings dialog box, select Production Order and choose OK. |  |
| 5 | Display Defects (optional) | Scroll down to the Defects area. Check the details of defects. | Only available if you have activated defects recording in master data and recorded a triggering result. |  |
| 6 | Enter UD code | Choose Edit. Choose the tab Usage Decision. The UD code you select depends on the Inspection Result. Choose one of the following two options:Positive Result, posting to unrestricted stockUD code: UD04 A1 (Accepted unrestricted stock)Negative Result, posting to blocked stockUD code: UD04 R1 (Rejected blocked stock) |  |  |
| 7 | Save Usage Decision | Choose Save. | Usage decision and goods movement have been made for inspection lot. |  |
| 8 | Review Material Stock (optional) | Scroll down to the Material Document area. Go to Stock Overview and evaluate the current stock. |  |  |

#### Review Batch Data (optional)

Purpose

The batch class is assigned to the batch-managed material SGQM. The batch class contains characteristics for information related to the inspection characteristics. By transferring inspection results to classification data, the data can be used, for example, in a batch-search strategy to find products with specified characteristics.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access App | Open Manage Batches (F2462). | The Manage Batches screen displays. |  |
| 3 | Execute Search | Maintain the following fields and choose Go:Material: SGQMBatch: <Batch Number>Plant: 3310 | The search result displays. |  |
| 4 | Navigate to Batch Details | Display the line item of the respective batch by choosing the arrow icon to the right. | Batch details are displayed on screen Batch. |  |
| 5 | Review Data | Review these tabs:The General Information tab displays the manufacturing date entered during goods receiptThe Classification tab displays the classification data of the batch. The created and assigned class characteristics in step [Create Master Inspection Characteristic with Reference to Class Characteristic](#unique_10) [page ] 14 and [Create Product Master with Quality Management](#unique_11) [page ] 16 are populated at the valuation of an inspection point (if multiple inspection points have been captured, data originates from the last inspection point) or respectively from Post-Process Inspection. | Batch information is reviewed. |  |

## Appendix

### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| 3F0 (Event-Based Production Cost Posting) | This procedure updates work-in-process calculation, overhead calculation, and variance calculation by linking the posting to the events.Note Start from CE2105, the default Best Practice content is based on event-based result analysis for new customer install and add new country only, rather than previous period-end posting. For existing customers (who activated content before 2105), the default remain unchanged to Period-End Closing – Plant BEI till customer makes the decision to switch. For migration to Event based from Periodic please refer [Production Settlement in Parallel Ledgers](https://help.sap.com/viewer/4032610758dc437089f0c28320eec93f/LATEST/en-US/e49a3770f22547a392455154f3eef6e2.html). If you are still using period-end posting, you may need to refer to non-standard Scope Item BEI - Period-End Closing – Plant. |
| BMC - Core Inventory Management | Complete the following activities:Perform the selected step you want to perform for the Blocked stock. |

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
- related-to :: [[13-quality-ehs-and-compliance/test-script-quality-management-in-discrete-manufacturing-consumer-prod]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1E1_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 151,518 chars in the whole document
