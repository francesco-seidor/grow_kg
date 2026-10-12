---
id: 12-production-and-manufacturing/material-replenishment-with-kanban-external-procurement-1e3-ae-test-sc
title: "Material Replenishment with Kanban – External Procurement (1E3_AE) – Test Script, SAP S/4HANA Cloud Public Edition (1E3_S4CLD2608_BPD_EN_AE)"
description: "SAP test script for scope item 1E3_AE (UAE): Kanban external procurement, event-driven Kanban and procurement to cost center, with master data, roles and steps."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/kanban-in-house-production]
aliases: [1E3_S4CLD2608_BPD_EN_AE]
keywords: ["Kanban Replenishment (In-House Production, External…", kanban replenishment, classic kanban, event-driven kanban, kanban control cycles, external procurement, procurement to cost center, kanban container status, scheduling agreements, summarized jit call]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1E3_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-713
topic: 12-production-and-manufacturing/kanban-in-house-production
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Material Replenishment with Kanban – External Procurement (1E3_AE) – Test Script, SAP S/4HANA Cloud Public Edition (1E3_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1E3_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Kanban Replenishment (In-House Production, External Procurement, Stock Transfer)** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Material Replenishment with Kanban – External Procurement (1E3_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Material Replenishment with Kanban – External Procurement (1E3_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232846751)

[2 Prerequisites 4](#_Toc232846752)

[2.1 System Access 4](#_Toc232846753)

[2.2 Roles 4](#_Toc232846754)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232846755)

[2.4 Business Conditions 8](#_Toc232846756)

[2.5 Preliminary Steps 8](#_Toc232846757)

[2.5.1 Check Configuration (Optional) 8](#_Toc232846758)

[2.5.1.1 Check Configuration - Define External Procurement Strategies 8](#_Toc232846759)

[2.5.1.2 Check Configuration - Define JIT Call Profile 9](#_Toc232846760)

[2.5.2 Create Master Data for Procedure - Classic Kanban: External Procurement with Requirements Planning 10](#_Toc232846761)

[2.5.2.1 Create Info Record 10](#_Toc232846762)

[2.5.2.2 Create Scheduling Agreement 11](#_Toc232846763)

[2.5.2.3 Manage Source List 13](#_Toc232846764)

[2.5.2.4 Control Cycle for Classic Kanban: External Processing with Requirements Planning 14](#_Toc232846765)

[2.5.2.5 Maintain Output Control for Kanban Summarized JIT Call 15](#_Toc232846766)

[2.5.3 Create Master Data for Procedure - Event-driven Kanban: External Processing with Purchase Order 16](#_Toc232846767)

[2.5.3.1 Define MRP Area 16](#_Toc232846768)

[2.5.3.2 Assign MRP Area to Material 19](#_Toc232846769)

[2.5.3.3 Create Info Record 20](#_Toc232846770)

[2.5.3.4 Control Cycle for Event-driven Kanban: External Processing with Purchase Order 22](#_Toc232846771)

[2.5.4 Create Master Data for Procedure - Procurement to Cost Center 23](#_Toc232846772)

[2.5.4.1 Create Purchasing Contract 23](#_Toc232846773)

[2.5.4.2 Control Cycle for Procurement to Cost Center 24](#_Toc232846774)

[2.5.5 Create Product Cost Collectors 25](#_Toc232846775)

[2.5.6 Create Preliminary Cost for the Product Cost Collectors 26](#_Toc232846776)

[2.5.7 Initialize Material Stock (Optional) 27](#_Toc232846777)

[3 Overview Table 28](#_Toc232846778)

[4 Test Procedures 30](#_Toc232846779)

[4.1 Classic Kanban: External Procurement with Requirements Planning 30](#_Toc232846780)

[4.1.1 Create Planned Independent Requirements 30](#_Toc232846781)

[4.1.2 Material Requirements Planning 32](#_Toc232846782)

[4.1.3 Check Dependent Requirement of Material RM233-4 33](#_Toc232846783)

[4.1.4 Release Scheduling Agreement 34](#_Toc232846784)

[4.1.5 Set Available Kanban to EMPTY 35](#_Toc232846785)

[4.1.6 Posting the Goods Receipt for External Procurement 37](#_Toc232846786)

[4.1.6.1 Option A: Change the Kanban to FULL 37](#_Toc232846787)

[4.1.6.2 Option B: Goods Receipt for JIT Call 38](#_Toc232846788)

[4.1.7 Precalculation of Kanbans for Future Requirements (Optional) 39](#_Toc232846789)

[4.1.8 Release Proposal of Kanbans Required for Future Period (Optional) 40](#_Toc232846790)

[4.1.9 Unlock New Kanbans (Optional) 42](#_Toc232846791)

[4.1.10 Alert for Delayed Replenishments - Creation of Replenishment Elements / JIT Calls (Optional) 43](#_Toc232846792)

[4.1.11 Alert for Delayed Replenishments - Evaluation of Replenishment Elements / JIT Calls (Optional) 44](#_Toc232846793)

[4.2 Event-driven Kanban: External Processing and PDF Print of Kanban Card 45](#_Toc232846794)

[4.2.1 Create Event-Driven Kanban 45](#_Toc232846795)

[4.2.2 Print the Kanban Card 46](#_Toc232846796)

[4.2.3 Variant 1: Set Kanban to FULL 47](#_Toc232846797)

[4.2.4 Variant 2: Goods Receipt 48](#_Toc232846798)

[4.2.5 Set Available Kanban to EMPTY 49](#_Toc232846799)

[4.3 Classic Kanban: Procurement to Cost Center 51](#_Toc232846800)

[4.3.1 Set Kanban to Empty 51](#_Toc232846801)

[4.3.2 Set Kanban to Full 52](#_Toc232846802)

[4.4 Analyze Kanban Control Cycles Analysis (Optional) 53](#_Toc232846803)

[4.5 Monitor Replenishment Situation (Optional) 54](#_Toc232846804)

[4.6 Review Manufacturing Object Pages 55](#_Toc232846805)

[5 Appendix 57](#_Toc232846806)

[5.1 Process Integration 57](#_Toc232846807)

[5.2 Kanban Status - Status Change/Kanban Signal 57](#_Toc232846808)

[5.2.1 Classification of the Processing Status of Kanban Container 57](#_Toc232846809)

## Purpose

Overview

The Kanban method for controlling production and material flow is based on the actual stock quantity in production. Material that is required on a regular basis is continually provided in small quantities into production. With Kanban, instead of being pushed through production by higher-level planning, materials are called from the supply source by production at the manufacturing level where they are needed (pull principle). Replenishment or production of a material is only triggered when a higher production level requires the material. This replenishment is triggered directly in production using previously maintained master data.

Kanban replenishment is commonly used in – but not restricted to – repetitive manufacturing environments when a production process requires that the same or similar products are produced over a certain period at a certain rate per period. The products produced always follow the same sequence through the machines and work centers in production. Routings tend to be simple and do not vary much.

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
| Production Supervisor - Repetitive Manufacturing | SAP_BR_PRODN_SUPERVISOR_RPTV | Production Management - Repetitive Manufacturing | SAP_BR_PRODN_SUPERVISOR_RPTV |  |
| Production Planner - Lean Manufacturing | SAP_BR_PRODN_PLNR_LEAN_MFG | Production Planning - Lean Manufacturing | SAP_BR_PRODN_PLNR_LEAN_MFG |  |
| Production Operator - Repetitive Manufacturing | SAP_BR_PRODN_OPTR_RPTV | Production Execution - Repetitive Manufacturing | SAP_BR_PRODN_OPTR_RPTV |  |
| Production Operator - Lean Manufacturing | SAP_BR_PRODN_OPTR_LEAN_MFG | Production Execution - Lean Manufacturing | SAP_BR_PRODN_OPTR_LEAN_MFG |  |
| Production Operator - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC | Production Execution - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC |  |
| Production Supervisor - Lean Manufacturing | SAP_BR_PRODN_SUPVR_LEAN_MFG | Production Supervision - Lean Manufacturing | SAP_BR_PRODN_SUPVR_LEAN_MFG |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Cost Accountant - Production | SAP_BR_PRODN_ACCOUNTANT | Product Costing | SAP_BR_PRODN_ACCOUNTANT |  |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company is created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure:

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Material | FG233 |  |  |
| Material | SG234 |  |  |
| Material | SG233 |  |  |
| Material | RM234 |  |  |
| Material | RM233-1 |  |  |
| Material | RM233-2 | Demo material for Event-driven Kanban: External Processing with Purchase Order |  |
| Material | RM233-4 | Demo material for Classic Kanban: External Procurement with Requirements Planning |  |
| Material | RM235 |  |  |
| Material | RM233-7 | Not included in BOM structure. Demo material for Classic Kanban: Procurement to Cost Center |  |
| Vendor | 33300002 | Domestic UAE Supplier 2 |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Storage Location | 331B | Std. storage 2 |  |
| Storage Location | 331C | Raw mat. stoloc. |  |
| Storage Location | 331E | Kanban |  |

Bill of Material Structure

This overview shows the bill of material structure and the usage of each component if you have activated all optional enhancements.

| Material | Level | Material Type | Unit | Characteristic of Material | Optional Enhancements |
| --- | --- | --- | --- | --- | --- |
| FG233 | 0 | FERT | PC |  |  |
| SG234 | 1 | SEMI | PC |  |  |
| RM235 | 2 | RAW | PC |  |  |
| SG233 | 1 | SEMI | PC |  |  |
| RM234 | 2 | RAW | PC |  |  |
| RM233-1 | 1 | RAW | PC |  |  |
| RM233-2 | 1 | RAW | PC |  |  |
| RM233-4 | 1 | RAW | PC |  |  |

For more information about creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNT | Create Product Master of type "Finished Good" - MDS |
| BNS | Create Product Master of type "Semi-Finished Good" - MDS |
| BNR | Create Product Master of type "Raw Material" - MDS |
| BNE | Create Supplier Master - MDS |
| 40D | Create Production Supply Area - MDS |
| BNJ | Create Production Work Center - MDS |
| BNK | Create Material BOM for Production and Sales - MDS |
| BNL | Create Routing - MDS |
| BLD | Create Production Version - MDS |

### Business Conditions

Before this scope item can be tested, the following business condition must be met.

| Scope Item | Business Condition |
| --- | --- |
| BEG - Standard Cost Calculation | You have completed the step described in the Test Script Standard Cost Calculation (BEG). |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS (BNZ) master data script. Posting Period is up to date. |

### Preliminary Steps

This Business Process Documentation contains process steps that must be completed before you can start to work through the standard Business Process Documentation of selected logistics scenarios.

#### Check Configuration (Optional)

##### Check Configuration - Define External Procurement Strategies

Purpose

The necessary customizing settings to run through some basic scenarios have already been created as pre-configured SAP Best Practice content. You can check detailed entries through available Self-Service Configuration UI (SSCUI). For demonstration of SAP Best Practice scope item, you may not be able to adapt pre-configured SAP Best Practice content. If necessary, you can create your own entries according to your business requirement.

| Key of Pre-delivered Replenishment Strategy | Description |
| --- | --- |
| PD01 | Purchase Order |
| PD20 | Scheduling Agreement |
| PD30 | Stock Transport Order |
| PDA7 | Summarized JIT Call (MRP, Alerts) |

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

- Configure Your Solution:

In the SAP S/4HANA Cloud Public Edition system, in the SAP Fiori launchpad, open Manage Your Solution (F1241) app as a Configuration Expert - Business Process Configuration and go to Configure Your Solution.

In the Application Area listbox, select Manufacturing.

In the Sub Application Area listbox, select Kanban.

In Item Name, choose Replenishment Strategies.

Choose Configure of the Define External Procurement Strategies (ID: 104055) step.

- SAP Central Business Configuration:

Log on to the project experience in SAP Central Business Configuration.

Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define External Procurement Strategies.

Choose Open Documentation for the found line item to see more details about this configuration activity.

Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.

##### Check Configuration - Define JIT Call Profile

Purpose

The necessary customizing settings to run through some basic scenarios have already been created as pre-configured SAP Best Practice content. You can check detailed entries through available Self-Service Configuration UI (SSCUI). For demonstration of SAP Best Practice scope item, you may not be able to adapt pre-configured SAP Best Practice content. If necessary, you can create your own entries according to your business requirement.

| Key of Pre-delivered Profile | Description |
| --- | --- |
| PD01 | Kanban (no summary) |
| PD02 | Kanban (by plant, unloading point) |
| PD03 | Kanban (summary by plant) |
| PD04 | Kanban (by plant, unloading point, PSA) |

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

- Configure Your Solution:

In the SAP S/4HANA Cloud Public Edition system, in the SAP Fiori launchpad, open Manage Your Solution (F1241) app using the business role Configuration Expert - Business Process Configuration and go to Configure Your Solution.

In the Application Area listbox, select Manufacturing.

In the Sub Application Area listbox, select Kanban.

In Item Name, select Kanban Summarized JIT Call Process.

Choose Define JIT Call Profile (ID: 104317).

Choose Configure.

- SAP Central Business Configuration:

Log on to the project experience in SAP Central Business Configuration.

Go to the Business Processes Configuration app. Search for the configuration activity Define JIT Call Profile and navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).

#### Create Master Data for Procedure - Classic Kanban: External Procurement with Requirements Planning

##### Create Info Record

Procedure

If the info record for the material RM233-4 and supplier 33300002 already exists in the system, you can skip this step. Otherwise, you need to create info record for the pair.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Purchasing Info Record (ME11). | The Create Info Record: Initial Screen displays. |  |
| 3 | Enter Initial Data | Make the following entries and press Enter:Supplier: 33300002Material: RM233-4Purchasing Org.: 3310Plant: 3310Select the Standard checkbox, then press Enter. | The Create Info Record: General Data screen displays. |  |
| 4 | Choose Purch.Org.Data 1 | Choose Purch.Org.Data 1. | The Create Info Record: Purch. Organization Data 1 screen displays. |  |
| 5 | Enter Item Data | Enter the following values:Pl. Deliv. Time: <X Day>Purch.Group: 001Tol. Underdl.: <XX%>Tol. Overdl.: <XX%>Standard Qty: <100>Net Price: <3.75>Price unit: <1 pc>Tax Code: <Input Tax Code>Note When the TDT(time dependent tax) is activated via SSCUI 101016 (Define Tax Codes for Sales and Purchases) for Country of company code and Tax Code is given, the Tax Rate Valid From field is mandatory. You can enter current date, which will be adjusted to validity start date of tax code according to the setting in SSCUI.When the RITA (Registration for Indirect Taxation Abroad) is activated, tax registration country is maintained for company code in SSCUI 103464 (Activate RITA and Maintain Tax Registration Countries) and tax code is given, the Tax Country field is mandatory, in which the country ID of company code is given as a default value, but you can change to the valid country ID that is maintained in SSCUI accordingly.Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration.Press Enter. |  |  |
| 6 | Save | Choose Save. |  |  |

##### Create Scheduling Agreement

Purpose

This activity is used to create the scheduling agreement for the material and supplier combination. For example, material RM233-4 and supplier 33300002, directly or without reference to any preceding purchasing documents like Purchase Requisition, if it has not been maintained yet.

If the scheduling agreement is already present in the system, then feel free to skip this step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Purchase Scheduling Agreements (F2179) . |  |  |
| 3 | Create Scheduling Agreement | Select Create to create a new scheduling agreement. |  |  |
| 4 | Enter Header Data | Create a new scheduling agreement with the following data:Supplier: 33300002Agreement type: LPA (SA With Release doc.)Validity Start: <today>Validity End: <MM/DD/YYYY>, for example, today + 720 daysPurchasing Group: 001Purchasing Organization: 3310 |  |  |
| 5 | Add Items to Scheduling Agreement | From the New Purchase Scheduling Agreement view, choose the Items facets and select Create. | The New Scheduling Agreement Item view displays. |  |
| 6 | Enter Item Data | On the Items facets view, make the following entries:In the General Information viewPlant: 3310Material: RM233-4In the Quantity and Price viewTarget Quantity: 10000Net Order Price: <Defaulted from Info record>In the GR/IR Control viewKanban Indicator: Y (Scheduling Agreement for Summarized JIT Call)In the Output Control view,JIT Indicator: 1(Automatically)Choose Apply at the bottom of the view. |  |  |
| 7 | Save | Return to the New Purchase Scheduling Agreement header view and choose Create at the bottom of the view.Make a note of the schedule agreement number. | A schedule agreement is created. |  |

##### Manage Source List

Purpose

This process step shows you how to maintain the contract as the source.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Source Lists (F1859). |  |  |
| 3 | Maintain the Filter of Source List | In the filter, make the following entries:Material: RM233-4Plant: 3310Then choose Go. |  |  |
| 4 | Check the Source List | If there is one item that valid in the period, ignore the following steps, if it doesn’t have one item, then continue. |  |  |
| 5 | Create Source List | Choose Create. | The Source List screen is displayed. |  |
| 6 | Enter Detailed Data | Enter the values in the following fields:Material: RM233-4Plant: 3310 |  |  |
| 7 | Generate Source List | In the new line appeared under Source Lists area, enter following parameters and choose Enter:Valid From: for example, <today>Valid to: for example, <end of next year>Agreement: scheduling agreement that created in the previous preliminary step Create Scheduling Agreement sectionAgreement Item: agreement item created before, for example, <10> |  |  |
| 8 | Maintain Parameters | Choose the created source list, on the General Information screen,Materials Planning: 2Choose Apply. |  |  |
| 9 | Save the Source List | Choose Create. | The source list is saved. |  |

##### Control Cycle for Classic Kanban: External Processing with Requirements Planning

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Production Planner - Lean Manufacturing. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Kanban Control Cycles (PKMC). |  |  |
| 3 | Navigate to Create Control Cycle Screen | Make the following entries and choose Edit.Plant: 3310Choose Create Control Cycle. | The Create Control Cycle screen displays. |  |
| 4 | Enter the selection details | Make the following entries and choose Continue:Classic Kanban: SelectedMaterial: RM233-4Supply Area: KANBAN_01Lifecycle status: Released | The Control Cycle Maintenance: Change screen displays. |  |
| 5 | Enter the Control Cycle Details | Make the following entries:Number of Containers: 2Container Quantity: 200Maximum Empty Containers: 1Number of Load Carriers: 0In the next part, choose the Replenishment Strategy tab. On this tab, select External Procurement and enter the value <PDA7>, then choose Enter.The tab changes its title from Replenishment strategy to External Procurement. Continue to enter the following entries:Agreement: The Scheduling Agreement you created in previous stepItem Value: 10Choose another tab Flow Control, make the following entry:JIT Call Prof: PD01Choose another tab Kanban Calculation, make the following entries:Calc. Type: 1Calc. Profile: PD01Choose another tab Print Control, make the following entry under Print Kanban Card:Print Queue: DEFAULT | The Purchasing Org and Vendor fields are automatically filled by the system when the Agreement number is entered. |  |
| 6 | Save | Choose Save Control Cycle. | You have created an external Kanban control cycle for material RM233-4 . |  |

##### Maintain Output Control for Kanban Summarized JIT Call

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Output Parameter Determination (APOC_WD_BRF_DEC_TAB_MAINTAIN). |  |  |
| 3 | Access the Customizing Path (for SAP S/4HANA Cloud Private Edition system) | For SAP S/4HANA Cloud Private Edition system, access IMG activity IMG > Cross-Application Components > Output Control > Define Business Rules for Output Determination .Transaction Code: OPD.Note Please check and make sure Output Control for Summarized JIT Call is activated. Access IMG activity IMG > Cross-Application Components > Output Control > Manage Application Object Type Activation , you should see following entry:Application Object Type: SUMMARIZED_JIT_CALLStatus: Application Active |  |  |
| 4 | Choose Show Rules for | On the Show Rules for field, choose the triangle button and choose Summarized JIT Call from the dropdown list. |  |  |
| 5 | Choose the Determination Step and Maintain Table Contents | On the Determination Step Field, choose the triangle button.Choose Channel, and maintain the following entry in Table Contents.Entry 1 as below:Output type: SUMMARIZED_JIT_CALL (Summarized JIT Call)Role: LFChannel: PRINT (Printout)Exclusive Indicator: – (false)Choose Printer Settings, and maintain the following entry in Table Contents.Entry 1 as below:Output type: SUMMARIZED_JIT_CALL (Summarized JIT Call)Role: LFPrint Queue: <your queue>Number of Copies: 1Note To maintain Table Contents.Choose Edit on Output Parameter Determination.Choose Insert New Row if a new row has to be added.Choose the triangle button on the field to be maintained.Choose Direct Value Input on the dropdown list.Input the value.Choose Activate, on the popup screen choose yes to save.Choose Display. |  |  |

#### Create Master Data for Procedure - Event-driven Kanban: External Processing with Purchase Order

##### Define MRP Area

Purpose

The purpose of this activity is to define an MRP area used in Kanban external processing, assigned with pre-defined Kanban Storage Location. This step can only be executed once, and if such MRP area already exists, skip this step.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Filter Selection Criteria | On the Configure Your Solution: Realize Phase screen, select the values as shown below:Application Area: ManufacturingSub Application Area: Material Requirements Planning | A search result list is displayed in the All Items area. |  |
| 5 | Find the Entry | In the All Items area, choose the following entry: Master Data. | The Configure Your Solution - Master Data screen displays. |  |
| 6 | Navigate to SSCUI 103068 | In the Configuration Steps section, navigate to step Define MRP Areas for Plant/Storage Locations. Choose Configure in the Actions column. | The Define MRP Areas for Plant/Storage Locations: Change screen displays. |  |
| 7 | Check if MRP Area Exists | Check if MRP area already exists with below parameter combination:MRP Area Type: 02 Storage LocationPlant: 3310Receiving Location: 331EIf the previous combination exists, you can use this MRP Area in subsequent procedure to assign it to material master, and ignore remaining steps in this procedure; if not, perform the following steps 8–10 for MRP definition. |  |  |
| 8 | New Entry | On the screen Define MRP Areas for Plant/Storage Locations: Change, choose New Entries. | The New Entries: Details of Added Entries screen displays. |  |
| 9 | Input Parameters | On the screen New Entries: Details of Added Entries, make the following entries:MRP Area: for example, KANBAN3310MRP Area Type: 02 Storage LocationMRP Area Text: <Description>Plant: 3310Press Enter, and make the following entry:Receiving Location: 331E |  |  |
| 10 | Save | Choose Save.Note If such MRP area already exists, you will get an error message indicating that the storage location is assigned to several MRP areas. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define MRP Areas for Plant/Storage Locations | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define MRP Areas for Plant/Storage Locations.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define MRP Areas for Plant/Storage Lo-cations: Change screen displays. |  |
| 3 | Check if MRP Area Exists | Check if MRP area already exists with below parameter combination:MRP Area Type: 02 Storage LocationPlant: 3310Receiving Location: 331EIf the previous combination exists, you can use this MRP Area in subsequent procedure to assign it to material master, and ignore remaining steps in this procedure; if not, perform the following steps 4–6 for MRP definition. |  |  |
| 4 | New Entry | On the screen Define MRP Areas for Plant/Storage Locations: Change, choose New Entries. | The New Entries: Details of Added Entries screen displays. |  |
| 5 | Input Parameters | On the screen New Entries: Details of Added Entries, make the following entries:MRP Area: for example, KANBAN3310MRP Area Type: 02 Storage LocationMRP Area Text: <Description>Plant: 3310Press Enter, and make the following entry:Receiving Location: 331E |  |  |
| 6 | Save | Choose Save.Note If such MRP area already exists, you will get an error message indicating that the storage location is assigned to several MRP areas. |  |  |

##### Assign MRP Area to Material

Purpose

The purpose of this activity is to assign an MRP area to material RM233-2 .

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Material (MM02). | The Change Material (Initial Screen) screen displays. |  |
| 3 | Enter Material | On the Change Material (Initial Screen) screen, make the following entry:Material: RM233-2Choose Select View(s). | The Select View(s) dialog displays. |  |
| 4 | Select Views | Select the MRP 1 view, and choose Org. Levels. | The Organizational Levels dialog displays. |  |
| 5 | Organizational Levels | In the popup dialog Organizational Levels, make the following entries:Plant: 3310Storage Location: <Leave it blank>Choose Continue. | The Change Material XXX screen displays. |  |
| 6 | Check if MRP Area exists | Navigate to the MRP 1 tab, and find section MRP Areas.If MRP Area Exists is selected (flagged), please skip the remaining steps; if not selected, go on with next steps to assign one MRP Area. |  |  |
| 7 | Input MRP Area | Choose button MRP Areas. In the popup table Overview: MRP Areas, you need to maintain one line to assign the MRP Area.For field MRP Area, open Value Help. Input below Restrictions and choose Go:MRP Area Type: 02 (Storage Location)Receiving Location: 331EThere should be only one search result, choose this MRP Area, and choose OK. |  |  |
| 8 | Input other parameters | Double-click the line you created and make the following entry on the MRP 1 tab:MRP Type: ND |  |  |
| 9 | Adopt | Choose Adopt twice, and make sure the MRP Area Exists is selected (flagged) now. | The MRP Area Exists is flagged now. |  |
| 10 | Save | On the Change Material screen, choose Save. | The MRP area is assigned to material RM233-2 . |  |

##### Create Info Record

Procedure

If the info record for the material RM233-2 and supplier 33300002 already exists in the system, you can skip this step. Otherwise, you need to create info record for the pair.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Purchasing Info Record (ME11). | The Create Info Record: Initial Screen displays. |  |
| 3 | Enter Initial Data | Make the following entries and press Enter:Supplier: 33300002Material: RM233-2Purchasing Org.: 3310Plant: 3310Select the Standard checkbox, and press Enter. | The Create Info Record: General Data screen displays. |  |
| 4 | Choose Purch.Org.Data 1 | Choose Purch.Org.Data 1. | The Create Info Record: Purch. Organization Data 1 screen displays. |  |
| 5 | Enter Item Data | Enter the following values:Pl. Deliv. Time: <X Day>Purch.Group: 001Tol. Underdl.: <XX%>Tol. Overdl.: <XX%>Standard Qty: <100>Net Price: <3.75>Price unit: <1 pc>Tax Code: <Input Tax Code>Note When the TDT(time dependent tax) is activated via SSCUI 101016 (Define Tax Codes for Sales and Purchases) for Country of company code and Tax Code is given, the Tax Rate Valid From field is mandatory. You can enter current date, which will be adjusted to validity start date of tax code according to the setting in SSCUI.When the RITA (Registration for Indirect Taxation Abroad) is activated, tax registration country is maintained for company code in SSCUI 103464 (Activate RITA and Maintain Tax Registration Countries) and tax code is given, the Tax Country field is mandatory, in which the country ID of company code is given as a default value, but you can change to the valid country ID that is maintained in SSCUI accordingly.Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration.Press Enter. |  |  |
| 6 | Save | Choose Save. | A purchasing info record for consigned procurement is saved. |  |

##### Control Cycle for Event-driven Kanban: External Processing with Purchase Order

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner - Lean Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Kanban Control Cycles (PKMC). |  |  |
| 3 | Navigate to Create Control Cycle Screen | Make the following entries and choose Edit.Plant: 3310Choose Create Control Cycle. | The Create Control Cycle screen displays. |  |
| 4 | Enter the Selection Details | Make the following entries and choose Continue:Event-Driven Kanban: SelectedMaterial: RM233-2Supply Area: KANBAN_04Lifecycle status: Released | The Control Cycle Maintenance: Change screen displays. |  |
| 5 | Enter the Control Cycle Details | Make the following entry:Container Quantity: 100In the next part, choose the Replenishment Strategy tab. On this tab, select External Procurement and enter the value <PD01>, and then choose Enter.The tab changes its title from Replenishment strategy to External Procurement. Continue to enter the following entries:Purchasing Org: 3310Supplier: 33300002Choose another tab Print Control, and make the following entries under Print Kanban Card:Print Queue: DEFAULTForm Template: PP_KANBAN_CARD |  |  |
| 6 | Save | Choose Save Control Cycle | You created an external Kanban control cycle for material RM233-2 . |  |

#### Create Master Data for Procedure - Procurement to Cost Center

##### Create Purchasing Contract

Purpose

This activity is used to create the purchasing contract for the material and supplier combination (material RM233-7 and supplier 33300002), if it has not been maintained yet.

If the purchasing contract is already present in the system, feel free to skip this step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Purchase Contract (ME31K). |  |  |
| 3 | Enter Data | Create a new contract with following data and press Enter:Supplier: 33300002Agreement Type: MK (Quantity Contract)Agreement Date: <today>In the Organizational Data section,Purchasing Organization: 3310Purchasing Group: 001In the Default Data for Items section,Acct Assignment Cat.: K (Cost Center)Plant: 3310 |  |  |
| 4 | Enter Header Data | On the Create Contract: Header Data screen, make the following entries and press Enter:Validity End: <today + 1 year> |  |  |
| 5 | Enter Item Data | On the Create Contract: Item Overview screen, in the first row (Item 10) under Outline Agreement Items, make the following entries and press Enter:Material: RM233-7Targ. Qty: 10,000Net Price: 1 |  |  |
| 6 | Enter Account Assignment Data | On the popup Account Assignment for Item 0010 screen, make the following entries and press Enter:G/L Account: <Default>Cost Center: 33101302 |  |  |
| 7 | Enter Additional Data | Select the Item, choose Menu > Item > More functions > Additional Data , make the following entries and press Enter:Kanban Indicator: X (Replenishment Element for Kanban) |  |  |
| 8 | Save | Choose Save at the bottom.Make a note of the contract number. | A purchasing contract is created. |  |

##### Control Cycle for Procurement to Cost Center

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner - Lean Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Kanban Control Cycles (PKMC). |  |  |
| 3 | Navigate to Create Control Cycle Screen | Make the following entries and choose Edit:Plant: 3310Choose Create Control Cycle. | The Create Control Cycle screen displays. |  |
| 4 | Enter the Selection Details | Make the following entries and choose Continue:Classic Kanban: SelectedMaterial: RM233-7Supply Area: KANBAN_04Lifecycle status: Released | The Control Cycle Maintenance: Change screen displays. |  |
| 5 | Enter the Control Cycle Details | Make the following entries:Number of Containers: 2Container Quantity: 5In the next part, choose the Replenishment Strategy tab. In this tab page, select External Procurement and enter the value <PDC1>, then choose Enter.The tab changes its title from Replenishment strategy to External Procurement. Continue to enter the following entries, and then press Enter:Purchasing Org: 3310Supplier: 33300002Agreement:<The Purchasing Contract you created in previous step>Item Value: 10Choose another tab Flow Control, make the following entry:Cost Center: <Defaulted from Purchasing Contract> |  |  |
| 6 | Save | Choose Save Control Cycle | You created an external Kanban control cycle for material RM233-7. |  |

#### Create Product Cost Collectors

Purpose

This step can only be executed if product cost planning is activated.

|  |
| --- |
| Note The product cost collector might have already been created in connection with other scope items. To have a check if the related ones are already created, please use the App Maintain Product Cost Collectors (KKF6N) with the selection based on the given material/plant data. In case the product cost collector already exists, the selectable entry on the left panel will be displayed and this step can be skipped. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Production. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Product Cost Collectors - Production Versions - Collective (KKF6M). | The Create Multiple Product Cost Collector for Production Versions screen displays. |  |
| 3 | Enter Relevant Values | Make the following entries and choose Execute.Plant: 3310Order Type: YBMROnly Repetitive Mfg Mat.: <select>Caution Once the product cost collector is created, it can't be created again with the same data. |  |  |
| 4 | Select Production Versions | The Select Production Versions screen could display if there is more than one production version or more than one material. | The Select Production Versions screen may display if there is more than one production version or more than one material. |  |
| 5 | Save | Select the row for the production version of materials FG233 and SG233 . Choose Save. | The message log displays. |  |
| 6 | Exit | Choose Exit. |  |  |

#### Create Preliminary Cost for the Product Cost Collectors

Purpose

In this topic, you create preliminary costs for the product cost collectors.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Production. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Preliminary Cost Estimate - Product Cost Collectors (MF30). | The Creation of Preliminary Cost Estimates For Product Cost Collectors screen displays. |  |
| 3 | Enter Relevant Values | Make the following entries and choose Execute.Costing Date : <Current Date>Plant: 3310 |  |  |

#### Initialize Material Stock (Optional)

Purpose

If you want to execute the whole production process for finished goods FG233, you can post initial stock for other necessary components, for example, RM234, RM233-1 , SG234 , SG233 .

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Stock (F1062). | The Manage Stock (F1062) screen displays. |  |
| 3 | Input Material | Make the following entries and press Enter:Material: <Material>Plant: Plant 1 AE3310 | The stock overview for the material displays. |  |
| 4 | Select Stock | Select the icon next to the stock where you want to add initial stock.For example:Storage Location: 331BUnrestricted Use Stock | In a dialog box, the Storage Location, Stock Type and Current Quantity fields display per your entries in previous steps. |  |
| 5 | Add Initial Entry | Make the following entries and choose Post:Document Date: <Today>Posting Date: <Today>Stock Change: Initial EntryQuantity: <Enter a quantity> | The system displays the following message. The stock has been added.1 document has been created: Material Document XXXXXXXXXX/20XX |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/APPs | Expected Results |
| --- | --- | --- | --- |
| Classic Kanban: External Procurement with Requirements Planning |  |  |  |
| [Create Planned Independent Requirements](#unique_25) [page ] 30 | Production Planner | Maintain PIRs (F3445) |  |
| [Material Requirements Planning](#unique_26) [page ] 32 | Production Planner | Schedule MRP Runs (F1339) |  |
| [Check Dependent Requirement of Material RM233-4](#unique_27) [page ] 33 | Production Planner | Monitor Material Coverage - Net / Individual Segments (F2101A) |  |
| [Release Scheduling Agreement](#unique_28) [page ] 34 | Purchaser | Manage Purchase Scheduling Agreements (F2179) |  |
| [Set Available Kanban to EMPTY](#unique_29) [page ] 35 | Production Operator - Lean Manufacturing | Set Kanban Container Status (F3717) |  |
| Posting the Goods Receipt for External Procurement |  |  |  |
| [Option A: Change the Kanban to FULL](#unique_30) [page ] 37 | Production Operator - Lean Manufacturing | Set Kanban Container Status (F3717) |  |
| [Option B: Goods Receipt for JIT Call](#unique_31) [page ] 38 | Production Operator - Lean Manufacturing | Goods Receipt for JIT Call (PJWE) |  |
| [Precalculation of Kanbans for Future Requirements (Optional)](#unique_32) [page ] 39 | Production Planner - Lean Manufacturing | Kanban Calculation (PK07) |  |
| [Release Proposal of Kanbans Required for Future Period (Optional)](#unique_33) [page ] 40 | Production Planner - Lean Manufacturing | Check Kanban Calculation Result (PK08N) |  |
| [Unlock New Kanbans (Optional)](#unique_34) [page ] 42 | Production Planner - Lean Manufacturing | Unlock Kanban Containers (PK09) |  |
| [Alert for Delayed Replenishments - Creation of Replenishment Elements / JIT Calls (Optional)](#unique_35) [page ] 43 | Production Planner - Lean Manufacturing | Display Kanbans: Demand View (PK13N) |  |
| [Alert for Delayed Replenishments - Evaluation of Replenishment Elements / JIT Calls (Optional)](#unique_36) [page ] 44 | Production Planner - Lean Manufacturing | Due Kanban Replenishment Elements (PKAL) |  |
| Event-driven Kanban: External Processing and PDF Print of Kanban Card |  |  |  |
| [Create Event-Driven Kanban](#unique_37) [page ] 45 | Production Planner - Lean Manufacturing | Kanban Board (F4630) |  |
| [Print the Kanban Card](#unique_38) [page ] 46 | Production Planner - Lean Manufacturing | Collective Kanban Print (PK17) |  |
| [Variant 1: Set Kanban to FULL](#unique_39) [page ] 47 | Production Operator - Lean Manufacturing | Set Kanban Container Status (F3717) |  |
| [Variant 2: Goods Receipt](#unique_40) [page ] 48 | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843) |  |
| [Set Available Kanban to EMPTY](#unique_41) [page ] 49 | Production Operator - Lean Manufacturing | Set Kanban Container Status (F3717) |  |
| Classic Kanban: Procurement to Cost Center |  |  |  |
| [Set Kanban to Empty](#unique_42) [page ] 51 | Production Operator - Lean Manufacturing | Kanban Board (F4630) |  |
| [Set Kanban to Full](#unique_43) [page ] 52 | Production Operator - Lean Manufacturing | Kanban Board (F4630) |  |
| [Analyze Kanban Control Cycles Analysis (Optional)](#unique_44) [page ] 53 | Production Supervisor - Lean Manufacturing | Kanban Control Cycles Analysis (F5235) |  |
| [Monitor Replenishment Situation (Optional)](#unique_45) [page ] 54 | Production Supervisor - Lean Manufacturing | Kanban Board (F4630) |  |
| [Review Manufacturing Object Pages](#unique_46) [page ] 55 | Production Planner | Search |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Classic Kanban: External Procurement with Requirements Planning

Purpose

You can perform the automatic Kanban calculation. The system calculates on the basis of existing requirements and your specified calculation parameters, either the number of Kanban containers (cards) that are to circulate in a control cycle or the quantity of material to be procured per Kanban container.

With the number of Kanban containers and the quantity of material per container, the material circulation and the stock of material in the control cycle are defined. To ensure the lowest possible stock of material while simultaneously achieving a secure material supply, the setting of these two values must be optimized. Because the requirement situation often fluctuates considerably in many industries, it is necessary to check and adjust these values with the automatic Kanban calculation on a regular basis.

In this scenario, you precalculate the number of Kanbans you need in a specific period (month) for material RM233-4.

Prerequisites

The Kanban control cycle for material RM233-4 is maintained and independent requirements exist.

#### Create Planned Independent Requirements

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Planned Independent Requirements (PIRs) are used to perform demand management functions. A planned independent requirement contains one planned quantity and one date, or a number of planned independent requirements schedule lines, that is, splitting one planned quantity according to dates.

|  |
| --- |
| Note Instead of creating a single requirement, sometimes a requirement plan that includes one or more planned independent requirements can be maintained for mass processing. In this case, the requirements are grouped and maintained under a requirement plan number. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain PIRs (F3445). | The Maintain PIRs screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, choose Area of Responsibility.On the My Area of Responsibility screen, check if the below entry is assigned:Plant 1 AE (3310)MRP Controller 001 (001)Choose AOR Status if the status for the above entry is not yet assigned.Choose AOR Status to unassign the rest of other entries. Then choose Back.Please note that you need to maintain this AOR Status correctly when you go through the whole test script. |  |  |
| 4 | Select Material Items | On the Maintain PIRs screen, make the following entries:Plant: 3310Period Indicator: Weekly (W)Version Active: Select all optionsSearch: FG233 |  |  |
| 5 | Filter Result | Choose Go to execute. | Material item displays. |  |
| 6 | Edit PIRs | Select the material item, and choose Edit on the upper-right part of the screen.On the screen, enter quantities per period, for example:PIR: 100And make sure the version is active.Version Active: YES |  |  |
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

The aim of material requirements planning is to tailor available capacities and receipts on time to suit requirements quantities. You can use MRP or consumption-based planning for this purpose. Single-item multi-level requirement planning is performed for plant 3310.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule MRP Runs (F1339). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create.On the New Job screen, make the following entries:For 1. Template Selection section:Job Template: Material Requirement Planning (MRP)Job Name: <MRP for FG233>Choose Step 2.For 2. Scheduling Options section:Start Immediately: <select>Choose Define Recurrence Pattern.On the Scheduling Information screen, make the following entries:Start Immediately: XRecurrence Pattern: Single RunChoose OK.Choose Step 3.For 3 Parameters section:Plant: 3310Material: FG233Changed BOM Components: selectPlanning Mode: 1Choose Check at the bottom right.Choose Schedule. | A message appears: You can go ahead and schedule the job. |  |
| 4 | Refresh Application Jobs List | To check the job’s status, enter MRP for FG233 in the search box and choose Go at the top-right section of the screen. | The new job is created and is displayed in the Application Jobs table when refreshed. |  |

#### Check Dependent Requirement of Material RM233-4

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you check whether dependent requirements for RM233-4 exist.

Prerequisite

The independent requirement planning for material FG233 is done and a planning run is finished.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). |  |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, check if the toggle button of Manage Material Coverage - New Version (F0251A) is on.Turn it on if the toggle button is off. | If the toggle button is on, continue with following steps to navigate to Manage Material Coverage - New Version (F0251A).If the toggle button is off, you will be navigated to Check Material Coverage - Old Version (F0251).The following steps are described with the toggle button on. |  |
| 4 | Select Material | In the search area, make the following entries and choose Go.Material: RM233-4Select the filtered rows and choose Manage Materials. | The Manage Material Coverage screen displays. |  |
| 5 | Check the Dependent Requirement | Review the Dependent Requirement of the material RM233-4, then choose Home. | You've checked the data available for RM233-4. |  |

#### Release Scheduling Agreement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to release scheduling agreement delivery schedule with forecast schedule.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Purchase Scheduling Agreements. |  |  |
| 3 | Find Scheduling Agreement Number | Find the appropriate scheduling agreement through the search criteria, such as: Supplier 33300002 , Agreement Type LPA (SA With Release doc.), Purchasing Organization3310, then choose Go. | The desired scheduling agreement displays on the Manage Scheduling Agreements list page . |  |
| 4 | Release of Schedule at Scheduling Agreement Level | On the Purchase Scheduling Agreements list, select the schedule agreement and choose Release in the right upper corner.Select Release: Forecast and JIT Schedule. In the Release: Forecast and JIT Schedule dialog box, choose Release.OrSelect Forecast Schedule, in the Release: Forecast Schedule dialog box, choose Release.And select JIT Schedule, in the Release: JIT Schedule dialog box, choose Release.In the Release Result Log dialog box, choose Close. | Release of schedule shall be with green status. |  |

#### Set Available Kanban to EMPTY

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you set an available Kanban to EMPTY to trigger the external procurement of RM233-4 .

Prerequisite

The Kanban control cycle for material RM233-4 is created.

Procedure

It is possible to change Kanban Container's status using different Fiori apps. You may choose one of them to execute the task in this step (set to EMPTY) and the subsequent steps (for example, set to FULL) where applicable. Here we provide two options for you, you can choose either one of them.

Option 1:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Lean Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Set Kanban Container Status (F3717). |  |  |
| 3 | Select the Kanban | Select a Kanban container on the left part of the screen. Choose Value Help icon to open Select: Barcode window. Choose Show Filters to make following entries and press Enter.Plant: 3310Production Supply Area: KANBAN_01From the Items list, choose one of the Kanban for RM233-4 with Current Status WAIT or FULL. | The Kanban you entered is displayed. |  |
| 4 | Check Kanban Information | On the right part of the screen, check following entry:Target Status: EMPTY |  |  |
| 5 | Set the Kanban to Empty | On the left part of the screen, choose Save at the bottom. | Setting an available Kanban to EMPTY creates a JIT (Just In Time) call for material RM233-4 . |  |

Option 2:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Lean Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Kanban Board (F4630).Note You can find the app under category Production Control - Kanban Monitoring. |  |  |
| 3 | Search | Make following entries and search and choose Go:Plant: 3310.Production Supply Area: KANBAN_01.Material: RM233-4 |  |  |
| 4 | Select Kanban Container | In the Control Cycle, choose one Kanban Container with status WAIT or FULL. You can check the legend for description of visual elements.Container Details panel will display at the right side. You can check detailed information. |  |  |
| 5 | Set the Kanban to Empty | Choose Set to EMPTY above the list. | Setting an available Kanban to EMPTY creates a JIT(Just In Time) call for material RM233-4 . |  |

#### Posting the Goods Receipt for External Procurement

Purpose

You can post goods receipt for external procurement either by changing the Kanban container to FULL or by posting GR for JIT call. You can choose one of the options to proceed.

##### Option A: Change the Kanban to FULL

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you change the status of the Kanban you processed in previous step to FULL for material RM233-4 .

Prerequisite

The status of the KANBAN is set to EMPTY previously.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Lean Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Set Kanban Container Status (F3717). |  |  |
| 3 | Select the Kanban | Select a Kanban container on the left part of the screen. Choose Value Help icon to open Select: Barcode window. Choose Show Filters to make following entries and press Enter.Plant: 3310Production Supply Area: KANBAN_01From the Items list, choose one of the Kanban for RM233-4 with Current Status EMPTY. | The Kanban you entered displays. |  |
| 4 | Check Kanban Information | On the right part of the screen, check following entry:Target Status: FULL |  |  |
| 5 | Set the Kanban to Full | On the left part of the screen, choose Save at the bottom. | Setting the empty Kanban to FULL executes a goods receipt in production storage location and a reduction of scheduling line for the amount delivered.The stock is increased for the Kanban amount.The scheduling lines are deleted for the delivered amount. |  |

##### Option B: Goods Receipt for JIT Call

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post goods receipt for JIT call. It is useful especially when you want to post partial quantities of individual items of a summarized JIT call, or for more containers at once.

Prerequisite

The status of the KANBAN is set to EMPTY previously.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Lean Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Goods Receipt for JIT Call (PJWE). |  |  |
| 3 | Input JIT Call Number | Enter the number of the appropriate production JIT call, and choose Adopt.JIT Call Number: XXXXNote If you set the indicator In background, the system automatically executes this goods receipt in background mode. |  |  |
| 4 | Check Quantity | On the Goods Receipt for JIT Call: Item Overview screen, check the quantity for which you want to post the goods receipt and change if necessary. |  |  |
| 5 | Post | Choose Post GR. | The system posts the goods receipt. |  |

#### Precalculation of Kanbans for Future Requirements (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you precalculate the Kanbans you need for the next period (month).

Prerequisite

The Kanban control cycle for material RM233-4 is created and dependent requirements for material RM233-4 exist.

|  |
| --- |
| Note If you want to specify other requirement types to be taken into account in the kanban calculation in addition to the dependent requirements that are already assigned to a production supply area (PSA), you can use the app Distribution for Kanban Calculation (PKDIS). |

|  |
| --- |
| Note If predictive material and resource planning (pMRP) functionality is enabled, it allows to calculate dependent PIRs for Kanban materials that are non-MRP relevant. For more information, see [Taking Further Requirement Types into Account](https://help.sap.com/viewer/84dbf30eedb4450983dc3d1c81b71996/latest/en-US/ed5ebd534f22b44ce10000000a174cb4.html). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner - Lean Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Kanban Calculation (PK07). | The Create Change Proposal For Kanban Control Cycles screen displays. |  |
| 3 | Enter the Selection Data | Make following entries and choose Execute.Plant: 3310Definition of period - From Date: <Today's date>To date: <Date at least 2 month in future>Material: RM233-4In the dialog box, check if a calculation of the Kanban cycle has taken place.Choose Continue. |  |  |
| 4 | Exit | Choose Home. | You have created a proposal for future requirements of Kanbans for material RM233-4. |  |

#### Release Proposal of Kanbans Required for Future Period (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you check the proposal for future Kanban requirements before you release the proposal.

Prerequisite

You have performed a Kanban calculation and a proposal is available.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner - Lean Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Check Kanban Calculation Result (PK08N) | The Initial Screen: Check Results of Kanban Calculation screen displays. |  |
| 3 | Enter the Selection Data | Make following entries and press Enter.Plant: 3310Material: RM233-4 | The Check Results of Kanban Calculation (Plant 3310) screen displays. |  |
| 4 | Check the Result | If the results are feasible, mark the line and choose Menu > Edit > Adopt > Next Change > For Selected . The New No. of Kanbans field is filled with the precalculated number. |  |  |
| 5 | Save | Choose Save. | You have accepted the proposal for Kanbans and changed the number of Kanbans in control cycle. |  |

|  |
| --- |
| Note If you want to specify other requirement types to be taken into account in the kanban calculation in addition to the dependent requirements that are already assigned to a production supply area (PSA), you can use Distribution for Kanban Calculation app. |

#### Unlock New Kanbans (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If Kanbans are created during Kanban calculation release, their statuses are locked. When they are really needed, they have to be unlocked.

Prerequisite

You have released a Kanban calculation where new kanbans are needed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner - Lean Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Unlock Kanban Containers (PK09). | The Unlock Kanbans screen displays. |  |
| 3 | Enter the Selection Data | Make the following entries and choose Run:Plant: 3310Supply Area: KANBAN_01Material: RM233-4 |  |  |
| 4 | Unlock Kanbans | Expand details to check the Kanbans with a locked indicator. Select the Kanbans with a blocked indicator for material RM233-4 and choose Unlock Kanbans.Confirm the message with Yes. |  |  |
| 5 | Exit | Choose Exit. | You have unlocked the new Kanbans for material RM233-4 . They are now ready for use. |  |

#### Alert for Delayed Replenishments - Creation of Replenishment Elements / JIT Calls (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you set more than the maximum allowed number of Kanbans to EMPTY to force the creation of alerting, in which case causes delayed replenishments.

Prerequisite

The Kanban control cycle for material RM233-4 is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner - Lean Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Kanbans: Demand View (PK13N). | The Kanban Board: Demand Source View, Initial Screen displays. |  |
| 3 | Select the Kanban | Make following entries and press Enter.Plant: 3310Production Supply Area: KANBAN_01 | The Kanban Board: Demand Source View From XX:XX Time screen displays. |  |
| 4 | Check the Control Cycle | Mark the correct line and choose Menu > Goto > Display Control Cycle . Check the maximum number of empty containers (here is 1).Choose Back. |  |  |
| 5 | Set More Kanban to EMPTY | Select the line of Kanban and choose Set to Empty.Make sure that there are in total more empty Kanbans than the number checked two steps ago (in this case at least two). |  |  |
| 6 | Check the Kanban Information | Double-click the empty Kanban to display the replenishment information. |  |  |
| 7 | Exit | Choose Home. | You have set more than the maximum allowed number of Kanbans to EMPTY. This results in alerts concerning delayed replenishment elements. |  |

#### Alert for Delayed Replenishments - Evaluation of Replenishment Elements / JIT Calls (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you check the alerts caused by previous step.

Prerequisite

The Kanban control cycle for material RM233-4 is created. Also more than the maximum allowed number of Kanbans have the status EMPTY.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner - Lean Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Due Kanban Replenishment Elements (PKAL). | The Delayed Replenishment Elements screen displays. |  |
| 3 | Check All Delayed Replenishment Elements for Material RM233-4 | Make following entries and choose Execute.Plant: 3310Delivery Date: <Tomorrow's Date>Trigger Alerts: XMaterial : RM233-4These alerts are caused by the situation that more than the maximum allowed number of Kanbans has the status EMPTY, for example, the replenishment of the Kanbans listed is delayed or the booking in system hasn't taken place yet. | The Delayed Replenishment Elements screen displays. |  |
| 4 | Exit | Choose Home. | You have checked the alerts caused by the fact that more than the maximum allowed number of Kanbans has the status EMPTY. |  |

### Event-driven Kanban: External Processing and PDF Print of Kanban Card

In event-driven Kanban, material provision is not based on a predefined number of Kanbans or a predefined Kanban quantity. Instead, it is based on actual material consumption. The material is not continually provided and replenished at a supply area. It is only replenished when specifically requested. In this case, the material is procured externally with purchase orders.

#### Create Event-Driven Kanban

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create a Kanban for material RM233-2 .

Prerequisite

The control cycle for material RM233-2 is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner - Lean Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Kanban Board (F4630). |  |  |
| 3 | Filter and Locate | Make following entries and press Enter.Plant: 3310Production Supply Area: KANBAN_04 |  |  |
| 4 | Create an Empty Kanban | In the control cycle of material RM233-2 , choose + Create Containers. | The Create Containers screen displays. |  |
| 5 | Enter Details of Kanban | Check the parameters and choose Create.Requested Quantity: <Default quantity of containers, for example 100> | An empty event-driven container is created. |  |
| 6 | Check the Kanban Information | Choose the empty kanban container to display the replenishment information and the Purchasing Order. |  |  |

#### Print the Kanban Card

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you print the Kanban card.

If you want to print the Kanban card physically, you need to install SAP Cloud Print Manager for Pull Integration. For details, refer to SAP note [3048273](https://me.sap.com/notes/3048273) and scope item Output Management (1LQ). After successfully setting up the printer, you can create your own print queue and assign it to the Kanban control cycle.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner - Lean Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Collective Kanban Print (PK17). | The Collective Kanban Print screen displays. |  |
| 3 | Select Supply Area | Make the flowing entries and choose Execute.Plant: 3310Material: RM233-2 |  |  |
| 4 | Print the Kanban Card | Expand the list.Select the checkbox of your Kanban ID.Choose Print Kanbans.Choose Yes to confirm the Print Kanbans information. | The Kanban card is printing. |  |
| 5 | Display Kanban (Optional) | If you want to check detailed information for the Kanban, select the checkbox of your Kanban ID, and choose Display Kanban. |  |  |
| 6 | Back | Choose Home. |  |  |

Result

Administrator can check technical status of the printing queue through the app Maintain Print Queues (F1260).

#### Variant 1: Set Kanban to FULL

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you set a Kanban to full for material RM233-2 .

Prerequisite

The control cycle for material RM233-2 is created and one Kanban has the status Empty. The Purchasing Order is released.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Lean Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Set Kanban Container Status (F3717). |  |  |
| 3 | Select the Kanban | Select a Kanban container on the left part of the screen. Choose Value Help icon to open Select: Barcode window. Choose Show Filters to make following entries and press Enter.Plant: 3310Production Supply Area: KANBAN_04From the Items list, choose one of the Kanban for RM233-2 with Current Status EMPTY. | The Kanban you entered displays. |  |
| 4 | Check Kanban Information | On the right part of the screen, check the following entry:Target Status: FULL |  |  |
| 5 | Set the Kanban to Full | On the left part of the screen, choose Save at the bottom. | The Kanban status is changed to FULL, which automatically results in a goods receipt in the storage location. |  |

#### Variant 2: Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you set a Kanban to full for material RM233-2 .

Prerequisite

The control cycle for material RM233-2 is created and one Kanban has the status Empty.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Receipt for Purchasing Document (F0843) |  |  |
| 3 | Enter Purchase Order | Enter the purchase order ID and choose Enter.Purchase Document: <Purchase Order from Create Kanban step> |  |  |
| 4 | Select Item | From the Items section, select the goods receipt item to be posted.Material: RM233-2Quantity: <Quantity> | The Post button is activated. |  |
| 5 | Post | Choose Post. | The goods receipt to a purchase order with Kanban indicator automatically results in a status change of the Kanban to Full. This corresponds to the purchase order. |  |

#### Set Available Kanban to EMPTY

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you set an available Kanban to Empty. The status change to empty results in an event-driven Kanban process in the deletion of the Kanban.

|  |
| --- |
| Note You can also use Delete Event-Driven Kanban Containers – Job Scheduling app, to schedule background jobs for triggering the deletion of event-driven kanban containers. |

Prerequisite

The Kanban has the status Full.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Lean Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Set Kanban Container Status (F3717). |  |  |
| 3 | Select the Kanban | Select a Kanban container on the left part of the screen. Choose Value Help icon to open Select: Barcode window. Choose Show Filters to make following entries and press Enter.Plant: 3310Production Supply Area: KANBAN_04From the Items list, choose one of the Kanban for RM233-2 with Current StatusFULL. | The Kanban you entered displays. |  |
| 4 | Check Kanban Information | On the right part of the screen, check the following entry:Target Status: EMPTY |  |  |
| 5 | Set the Kanban to Empty | On the left part of the screen, choose Save at the bottom. | By setting an available Kanban to EMPTY, the Kanban is deleted. No stock changes take place in this step. |  |

### Classic Kanban: Procurement to Cost Center

In this procedure, you procure bulk material using external procurement via Kanban. This bulk material is not included in the bill of material for the assembly and cannot, therefore, be assigned to just one assembly. For this reason, you must post the costs of this bulk material to a cost center as material overhead costs. In this case, the system posts the material to the cost center when a kanban container is set to Full. The material is therefore not available at the storage location.

#### Set Kanban to Empty

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you set an available Kanban container to status Empty to trigger external procurement.

Prerequisite

The corresponding control cycle is properly maintained.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Lean Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Kanban Board (F4630). |  |  |
| 3 | Filter | Make following entries and choose Go.Plant: 3310Production Supply Area: KANBAN_04Material: RM233-7 |  |  |
| 4 | Set Kanban Container to Empty | In the control cycle for selected material, select one Kanban Container with current status Wait or Full, and choose Set to EMPTY above. | The Kanban container status is changed to Empty, and replenishment is triggered. |  |
| 5 | Check Container Details | Choose the empty kanban container to display more information in the Container Details panel.Note down Purchase Order number for further check. |  |  |

Result

Purchaser can check the generated purchase order item through Fiori app Manage Purchase Orders (F0842A). In the Purchase Order Item Account Assignment part, you will find the cost center is correctly assigned.

#### Set Kanban to Full

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you set an empty Kanban to status Full to post the material to cost center directly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Lean Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Kanban Board (F4630). |  |  |
| 3 | Filter | Make following entries and choose Go.Plant: 3310Production Supply Area: KANBAN_04Material: RM233-7 |  |  |
| 4 | Set Kanban to Empty | In the control cycle for selected material, select one Kanban Container with current status Empty, and choose Set to FULL above. | Container status is changed from Empty to Full. The material is posted to the cost center and thus not available at the storage location. |  |
| 5 | Check Container Details | Choose the full kanban container to display more information in the Container Details panel.Note down Material Document number for further check. |  |  |

Result

Inventory Manager can check the generated material document through Fiori app Material Documents Overview (F1077).

### Analyze Kanban Control Cycles Analysis (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can evaluate your kanban control cycles with the flexibility in selection, aggregation and visualization. You can first get insights into the overall kanban replenishment situation at the aggregated level, and then drill-down to the details by selecting the dimensions and measures of your interest. This enables you to identify critical situations early and quickly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Lean Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Kanban Control Cycles Analysis (F5235). |  |  |
| 3 | Filter | Filter by dimensions like plant, production supply area, material, and others. For example:Plant: 3310Choose Go. | Under default layout, the stacked chart will illustrate the percentage of kanban container distribution for each status. In the table, the kanban control cycles are displayed with their number of containers, number of empty containers, and number of containers with error. |  |
| 4 | View Mode | On the upper right part of the screen, you can toggle between different view modes by selecting different icons:Chart and Table ViewChart ViewTable View |  |  |
| 5 | View Settings | Choose Settings icon to open View Settings window.You can check and adjust how the Dimensions and Measures are shown in this analysis app. |  |  |
| 6 | Navigate | You can explore the app with rich set of visualization elements (a range of chart types, drill down, and so on) to better evaluate your kanban control cycle situation.Note In the upper left corner, you can take advantage of preset view variants from the dropdown list. You can create and manage views under My Views. |  |  |

### Monitor Replenishment Situation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You may need to monitor the replenishment situation during the whole process. The kanban board is a tool for monitoring circulating kanban containers and evaluations, providing an overview of work progress and material consumption. The status of the kanban containers and the error situations are represented by different colors. You can also use the kanban board to trigger the kanban signal.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Lean Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Kanban Board (F4630).Note You can find the app under category Production Control - Kanban Monitoring. |  |  |
| 3 | Search | You can restrict selection by certain search criteria. Make following entries and choose Go:Plant: 3310Production Supply Area: <Production Supply Area>Material: <Material> |  |  |
| 4 | Check Kanban Container | The kanban containers are represented in different colors according to their status. Choose one Kanban Container. | The Container Details panel displays at the right side where you can check detailed information. |  |
| 5 | Kanban Correction | If the desired status change results in an error, the error message is displayed in the details panel of the kanban container. You can use the Correct Kanban app to correct the Kanban Container with ERROR status. |  |  |

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

### Process Integration

For the complete production process, you can refer to corresponding business processes mentioned in below test script depending on your production environment:

BJH: Make-to-Stock Production – Repetitive Manufacturing

BJ5: Make-to-Stock Production – Discrete Manufacturing

### Kanban Status - Status Change/Kanban Signal

#### Classification of the Processing Status of Kanban Container

The course of Kanban Container processing is controlled and made visible through setting the Kanban Containers to appropriate status. Usually, only the statuses "Empty" and "Full" are used. As a rule, if a material in a Kanban Container has been used and a Kanban Container is then set to "Empty", this Kanban Container status automatically triggers the replenishment process. The source of supply (producer, supplier) receives the signal to fill up the Kanban Container again. When the full Kanban Container arrives back at the demand source (the consumer), the latter sets the Kanban Container to the status "Full" and the goods receipt is posted for the material. Normally, Kanban Container is possible with both statuses "Empty" and "Full".

| Status – Description | Business Condition |
| --- | --- |
| Waiting – 1 | Indicates that although the material has been consumed, the supply source is not yet to supply any more of it. This status is also set if a new Kanban Container has been created.If a new Kanban Container has been included in the control cycle and no replenishment has yet been triggered, it has the status "Waiting" and can then be set to "Empty" by the demand source (consumer). |
| In Process – 3 / In Transit – 4 | The statuses "In Process" and "In Transit" are set by the supply source (supplier) to inform the demand source (consumer) that the Kanban Containers are either being processed or are in transit.If you use Kanban Containers with purchase orders, the status of a Kanban Container is automatically set to IN TRANSPORT if an inbound delivery has been generated for the order. |
| Full – 5 | The status "Full" is assigned by the demand source (consumer) upon receipt of the container or if the goods receipt has been posted for the kanban. Exception: Decoupling of Status Change and Goods Receipt Posting. |
| In Use -6 | The status "In Use" is set by the demand source to inform the supply source which Kanban Containers are currently being emptied. (This status can only be set on the kanban board.) |
| Error – 9 | The status "Error" is set only by the system. It is set if an error occurs during the processing of a Kanban Container. This may happen, for instance, if a Kanban Container is set to "Empty" and a purchase order is simultaneously to be created. If the desired vendor is invalid at this time, it does not make sense to resolve the situation in dialog mode here. The status of the Kanban Container is then set to "Error" with an appropriate system message.If you have specified in Customizing for Kanban that only an error message is to be issued when a certain error occurs, the kanban status is not set to "Error". For more information, see: Error Handling. |
| Empty – 2 | The status "Empty" is set by the demand source (consumer) when the kanban quantity has been consumed. Depending on the replenishment strategy, this immediately triggers replenishment. |

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
- related-to :: [[12-production-and-manufacturing/test-script-material-replenishment-with-kanban-in-house-production-4b3]]
- related-to :: [[12-production-and-manufacturing/test-script-material-replenishment-with-kanban-stock-transfer-4b4-ae-s]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1E3_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 96,603 chars in the whole document
