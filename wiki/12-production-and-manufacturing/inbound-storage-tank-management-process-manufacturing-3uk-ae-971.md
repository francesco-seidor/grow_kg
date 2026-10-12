---
id: 12-production-and-manufacturing/inbound-storage-tank-management-process-manufacturing-3uk-ae-971
title: Inbound Storage Tank Management – Process Manufacturing (3UK_AE) (3UK_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 3UK_AE: receive a batch into a day tank, mix with main tank batch via process order, with QM."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/storage-tank-management]
aliases: [3UK_S4CLD2608_BPD_EN_AE]
keywords: [Storage Tank Management and Tank Trailer Filling, storage tank management, batch mixing, process orders, batch determination, goods receipt, quality inspection, usage decision, purchase orders, goods issue]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3UK_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-971
topic: 12-production-and-manufacturing/storage-tank-management
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Inbound Storage Tank Management – Process Manufacturing (3UK_AE) (3UK_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3UK_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Storage Tank Management and Tank Trailer Filling** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Inbound Storage Tank Management – Process Manufacturing (3UK_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Inbound Storage Tank Management – Process Manufacturing (3UK_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232853694)

[2 Prerequisites 4](#_Toc232853695)

[2.1 System Access 4](#_Toc232853696)

[2.2 Roles 4](#_Toc232853697)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232853698)

[2.4 Business Conditions 7](#_Toc232853699)

[2.5 Preliminary Steps 7](#_Toc232853700)

[2.5.1 Assign Class Characteristic 7](#_Toc232853701)

[2.5.2 Create Info Record for Material SG1010 8](#_Toc232853702)

[2.5.3 Stock Initiation for Batch #1 into Main Tank 9](#_Toc232853703)

[3 Overview Table 11](#_Toc232853704)

[4 Test Procedures 13](#_Toc232853705)

[4.1 Receive Batch #2 into Day Tank 13](#_Toc232853706)

[4.1.1 Create Purchase Order 13](#_Toc232853707)

[4.1.2 Post Goods Receipt for Purchase Order 14](#_Toc232853708)

[4.1.3 Display Material Stock before Quality Inspection 15](#_Toc232853709)

[4.1.4 Display Open Inspection Lot 16](#_Toc232853710)

[4.1.5 Record Inspection Results 17](#_Toc232853711)

[4.1.6 Make Usage Decision 18](#_Toc232853712)

[4.1.7 Display Material Stock after Quality Inspection 19](#_Toc232853713)

[4.2 Batch Mixing in Main Tank 20](#_Toc232853714)

[4.2.1 Create Process Order for Mixing 20](#_Toc232853715)

[4.2.2 Execute Batch Determination in Process Order 22](#_Toc232853716)

[4.2.3 Review Process Order 23](#_Toc232853717)

[4.2.4 Goods Issue of Batch-Managed Components 24](#_Toc232853718)

[4.2.4.1 Goods Issue Via Pick List 24](#_Toc232853719)

[4.2.4.2 Manual Goods Issue (instead of Picking List) 25](#_Toc232853720)

[4.2.5 Confirm Process Order 26](#_Toc232853721)

[4.2.6 Post Goods Receipt for Process Order 27](#_Toc232853722)

[4.2.7 Display Material Stock before Quality Inspection 28](#_Toc232853723)

[4.2.8 Display Open Inspection Lot 29](#_Toc232853724)

[4.2.9 Record Inspection Results 30](#_Toc232853725)

[4.2.10 Make Usage Decision 31](#_Toc232853726)

[4.2.11 Display Material Stock after Quality Inspection 32](#_Toc232853727)

[4.3 Review Manufacturing Object Pages (Optional) 33](#_Toc232853728)

[5 Appendix 35](#_Toc232853729)

[5.1 Succeeding Processes 35](#_Toc232853730)

## Purpose

Overview

This scope item enables the storage tank management process, which supports the procurement of a new batch into the day tank and then mixing of this new batch with an existing batch in the main tank with a special mixing process order type. Quality inspection, results recording, and usage decision are performed both on the externally procured batch and the batch after mixing.

The characteristics of storage tank management are:

- Separate storage locations are created for day tank and main tank.
- An existing batch is already available on the main tank.
- Only one batch can normally be managed on these storage tanks.
- Batch determination is at order level.

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
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Quality Technician | SAP_BR_QUALITY_TECHNICIAN | Quality Inspection | SAP_BR_QUALITY_TECHNICIAN |  |
| Quality Engineer | SAP_BR_QUALITY_ENGINEER | Quality Engineering | SAP_BR_QUALITY_ENGINEER |  |
| Production Planner | SAP_BR_PRODN_PLNR | Production Planning | SAP_BR_PRODN_PLNR |  |
| Production Supervisor - Process Manufacturing | SAP_BR_PRODN_SUPERVISOR_PROC | Production Management - Process Manufacturing | SAP_BR_PRODN_SUPERVISOR_PROC |  |
| Production Operator - Process Manufacturing | SAP_BR_PRODN_OPTR_PROC | Production Execution - Process Manufacturing | SAP_BR_PRODN_OPTR_PROC |  |
| Production Engineer - Process Manufacturing | SAP_BR_PRODN_ENG_PROC | Production Engineering - Process Manufacturing | SAP_BR_PRODN_ENG_PROC |  |
| BOM Engineer | SAP_BR_BOM_ENGINEER | Bills Of Material | SAP_BR_BOM_ENGINEER |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure:

Table 1: Manufacturing

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Material | SG1010 | SEMI1010, PD, Silo material with batch | Silo material |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331Q | Std. storage 25 | Main storage tank for batch mixing |
| Storage Location | 331T | Std. storage 24 | Goods receipt from Procurement |

Bill of Materials Structure

This overview shows the bill of materials structure and the usage of each component.

Table 2: BOM Header

| Material | Usage | Base quantity | Unit | Material description |
| --- | --- | --- | --- | --- |
| SG1010 | 1 | 1000 | L | SEMI1010, PD, Silo material with batch |

Table 3: BOM Item

| Item | Item Category | Component | Quantity | Unit | Material description |
| --- | --- | --- | --- | --- | --- |
| 0010 | L | SG1010 | 1000 | L | SEMI1010, PD, Silo material with batch |

|  |
| --- |
| Note The costing relevancy check box for the BOM item should be unselected, as it is simple mixing and there is no real material consumption cost. Check and unselect with following steps:Log on to the SAP Fiori launchpad as a Production Engineer - Process Manufacturing (SAP_BR_PRODN_ENG_PROC).Open Maintain Bill Of Material - Create, change & display BOMs (F1813).Enter the search criteria, find and choose the BOM.In the Components tab, select the Item 0010 (Component: SG1010). Choose Status/Long Text tab, remove value X in the Relevancy to Costing field. Choose Apply.Save the BOM. The message Material BOM saved displays. |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 4: Master Data Script Reference

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
| BEG - Standard Cost Calculation | You have completed the step described in the Test Scrip BEG. |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the test script BNZ. Posting Period is up to date. |

### Preliminary Steps

#### Assign Class Characteristic

Purpose

The link between master inspection characteristics (MIC) and class characteristics enables the automatic transfer of inspection results to the batch classification. 2 class characteristics ( YQ_PURITY_3310, YQ_VISQ01_3310) have already been created, and linked to corresponding MICs (PURITY, VISQ01). But the assignment between characteristics and batch class is not pre-delivered yet, which requires you check and do the assignment manually.

In this step, you assign the 2 class characteristics to Batch Class YQ_SILO which is assigned to demo material SG1010.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a BOM Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Classes (CL02). |  |  |
| 3 | Enter Class Name | Make the following entries and choose Enter.Class: YQ_SILOClass Type: 023 |  |  |
| 4 | Go to Char. Tab | Select the Char. tab. Typically, following characteristics shall be already assigned for you:YB_BATCH_NUMBER |  |  |
| 5 | Assign Characteristics | Assign or append following pre-defined characteristics:YQ_PURITY_3310,YQ_VISQ01_3310 | If already assigned, it can be ignored. |  |
| 6 | Save | Choose Save. |  |  |

#### Create Info Record for Material SG1010

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Open Manage Purchasing Info Records | Choose Manage Purchasing Info Records (F1982). | The Manage Purchasing Info Records (F1982) screen displays. |  |
| 3 | Open New Purchasing Info Record | Choose icon Create. | The Purchasing Info Record Screen displays. |  |
| 4 | Enter Header Data | Make the following entries:Purchasing Info Record Category: <Standard>Purchasing Organization: 3310Supplier: 33300001Purchasing Group: 001Material Group: L003Material: SG1010 | Header data is added. |  |
| 5 | Enter Delivery and Quantity Data | Make the following entries:Delivery Time in Days: <XX>, for example, 2Order Unit: LStandard Order Quantity: for example, 100Goods-Receipt-Based Invoice Verification: unmarked | Delivery and Quantity Data is added. |  |
| 6 | Enter Condition Data | In the Conditions section, choose the Create icon. Enter the following data:Valid From: <Today’s Date>Amount: 0.15Pricing Unit: 1Valid To: 12/31/9999Currency: AEDChoose the Apply icon. | Condition Data is added |  |
| 7 | Save Your Data | Choose Create. | A purchasing info record is saved.Note down the purchasing info record number. |  |

#### Stock Initiation for Batch #1 into Main Tank

Purpose

This process step shows you how to post the initial stock in the Main Tank 331Q. If there is already one batch existing in the Main Tank, you can ignore this step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | Screen name adapts according to entries. |  |
| 3 | Choose Goods Receipt-Other | Make the following entries and choose Enter.Trans./Event: Goods ReceiptReference Document: OtherMovement Type: 561 | Screen name adapts after entries are made. |  |
| 4 | Specify Material | In the Material tab, make the following entries:Material: SG1010 | Ensure that detail data is expanded. |  |
| 5 | Specify Quantity | In the Quantity tab, make the following entries:Qty in Unit of Entry: 100 |  |  |
| 6 | Specify Plant and Storage Location | In the Where tab, make the following entries:Plant: 3310Storage location: 331Q |  |  |
| 7 | Check Item | Press Enter and ensure Item OK is selected. |  |  |
| 8 | Post Goods Movement | Choose Post. | Material document XXX posted. |  |

Result

Batch #1 exists in the Main Tank.

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| Receive Batch #2 into Day Tank |  |  |  |
| [Create Purchase Order](#unique_11) [page ] 13 | Purchaser | Manage Purchase Orders (F0842A) | Purchase Order is created. |
| [Post Goods Receipt for Purchase Order](#unique_12) [page ] 14 | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843) | Goods receipt for PO is posted. |
| [Display Material Stock before Quality Inspection](#unique_13) [page ] 15 | Warehouse Clerk | Stock - Single Material (F1076) | Material stock is displayed. The goods receipt quantity from previous step is shown in the quality stock. |
| [Display Open Inspection Lot](#unique_14) [page ] 16 | Quality Technician | Manage Inspection Lots (F2343) | The open inspection lots are displayed. The Quality Engineer can select the next inspection lot he or she wants to record the usage decision for. |
| [Record Inspection Results](#unique_15) [page ] 17 | Quality Technician | Record Inspection Results (F1685A) | Inspection results are recorded. |
| [Make Usage Decision](#unique_16) [page ] 18 | Quality Engineer | Record Usage Decision (QA11) | Usage decision is posted. |
| [Display Material Stock after Quality Inspection](#unique_17) [page ] 19 | Warehouse Clerk | Stock - Single Material (F1076) | Material stock is displayed. The stock quantity is shown in unrestricted if accepted by usage decision. |
| Batch Mixing in Main Tank |  |  |  |
| [Create Process Order for Mixing](#unique_18) [page ] 20 | Production Supervisor - Process Manufacturing | Create Process Order (COR1) | Process Order for mixing is created. |
| [Execute Batch Determination in Process Order](#unique_19) [page ] 22 | Production Supervisor - Process Manufacturing | Change Process Order (COR2) | Assign batches to be mixed into Process Order. |
| [Review Process Order](#unique_20) [page ] 23 | Production Supervisor - Process Manufacturing | Display Process Order (COR3) |  |
| Goods Issue of Batch-Managed Components |  |  |  |
| [Goods Issue Via Pick List](#unique_21) [page ] 24 | Production Operator - Process Manufacturing | Pick Components for Process Orders (COIK) | Components under Picking List are posted. |
| [Manual Goods Issue (instead of Picking List)](#unique_22) [page ] 25 | Warehouse Clerk | Post Goods Movement (MIGO) | Goods movements are posted. |
| [Confirm Process Order](#unique_23) [page ] 26 | Production Operator - Process Manufacturing | Confirm Process Order Phase (COR6N) | Process order is confirmed. |
| [Post Goods Receipt for Process Order](#unique_24) [page ] 27 | Warehouse Clerk | Post Goods Movement (MIGO) | The goods receipt for the process order is posted. |
| [Display Material Stock before Quality Inspection](#unique_25) [page ] 28 | Warehouse Clerk | Stock - Single Material (F1076) | Material stock is displayed. The goods receipt quantity from previous step is shown in the quality stock. |
| [Display Open Inspection Lot](#unique_26) [page ] 29 | Quality Technician | Manage Inspection Lots (F2343) | The open inspection lots are displayed. |
| [Record Inspection Results](#unique_27) [page ] 30 | Quality Technician | Record Inspection Results (F1685A) | Inspection results are recorded. |
| [Make Usage Decision](#unique_28) [page ] 31 | Quality Engineer | Record Usage Decision (QA11) | Usage decision is posted. |
| [Display Material Stock after Quality Inspection](#unique_29) [page ] 32 | Warehouse Clerk | Stock - Single Material (F1076) | Material stock is displayed. The stock quantity is shown in unrestricted if accepted by usage decision. |
| [Review Manufacturing Object Pages (Optional)](#unique_30) [page ] 33 | Production Planner |  |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Receive Batch #2 into Day Tank

#### Create Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a purchase order for the silo material directly.

|  |
| --- |
| Note You can either create purchase order directly or referring to the process of Procurement of Direct Materials (J45) for other options to create purchase order. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Open Manage Purchase Orders | Open Manage Purchase Orders (F0842A). | The Manage Purchase Orders screen displays with a list of existing Purchasing Document Items. |  |
| 3 | Start Purchase Order creation | Without making any selection, choose Create. | The New Purchase Order screen displays. |  |
| 4 | Enter Purchase Order Data | Make the following entries:General Information tab:Supplier: 33300001Company Code: 3310Purchasing Org.: 3310Purchasing Group: 001Currency: AEDOn the tab Items, add an item via icon Create. Choose the arrow at the end of the new item row, and the Purchase Order Item screen displays. Make the following entries:General Information tab:Material: SG1010Plant: 3310Order Quantity: 100Storage Location: 331T(Day Tank)Schedule Lines tab:Delivery Date: <a date in the future>Choose Apply. | Back to the Purchase Order screen. |  |
| 5 | Save Purchase Order | Choose the Order to save the purchase order. | A new Purchase Order is created. The system displays the message Purchase Order has been saved. Note down Purchase Order number. |  |

#### Post Goods Receipt for Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Goods ordered by a purchase order arrive at warehouse. This process step shows you how to post the goods receipt.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Receipt for Purchasing Document (F0843). |  |  |
| 3 | Search Purchase Order | Enter Purchase Order from previous step.Note If system suggests Purchasing Document XXXX not yet released, log on as a Purchasing Manager and approve it through My Inbox - All Items (F0862) App. You can refer to Procurement of Direct Materials (J45) scope item for more details. | The system displays the data for the goods receipt. If the Storage Location is not specified in the Purchase Order, it needs to be maintained now (331T Day Tank). |  |
| 4 | Post | Select the item. Choose Post. | The Post Goods Receipt screen displays. The system displays the message Material document xxx posted. |  |

#### Display Material Stock before Quality Inspection

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to review the material stock. Due to quality inspection, the material is not available for other processing.

Prerequisite

The goods receipt from purchase order was posted for the silo material to quality inspection stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Stock - Single Material (F1076). |  |  |
| 3 | Enter Selection | Make the following entries and press Enter:Material: <SG1010> | Stock for the material displays. |  |
| 4 | Check Stock Quantity | Batch number of Batch #2 is automatically created under storage location 331T, and the quantity is under Quality Inspection Stock. | Quantity received is posted into quality stock. |  |

#### Display Open Inspection Lot

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection lot is used to record the results of the inspection operation. This process step shows you how to verify the references to the goods receipt and purchase order as well as the sample size used for quality inspection reviewed.

Prerequisite

In this scope item, the inspection lot is created automatically upon goods receipt for the purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Technician. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Inspection Lots (F2343). | The Manage Inspection Lots screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go:Inspection Lot Origin: Goods ReceiptPlant: 3310Material: SG1010Inspection Lot Status: Outstanding | If the required filter doesn’t display in the Filters, choose Adapt Filters and choose the proper one. |  |
| 4 | Select Inspection Lot | In the inspection lot list, select the inspection lot which you created before. | Inspection lot displays. |  |
| 5 | Check Information | Under Origin, verify the referenced purchase order and material document.Under Result, choose the Inspection Operation, and verify the Characteristics need to be inspected.Make a note of the inspection lot number: __________. | Detailed information displays for the inspection lot. |  |

#### Record Inspection Results

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to record inspection results for the inspection lot.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Technician. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Record Inspection Results (F1685A). | The Record Inspection Results screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Plant: 3310Material: SG1010Purchase Order: <Purchase Order number from previous step> | If purchase order doesn’t display in the Filters, choose Adapt Filters. Select Purchase Order and choose OK. Choose Go.You can also use Inspection Lot number as filter. |  |
| 4 | Select Inspection Lot | In the inspection lot list, choose the inspection lot for which inspection results shall be recorded. | Two characteristics display to be inspected. |  |
| 5 | Enter Inspection Result | Choose Edit. Record results for each Master Inspection Characteristic (MIC) and make evaluation according to the inspection results.For MIC Purity:Inspection Results - Mean Value (%): 95Status / Valuation: AcceptFor MIC Visual Inspection:Inspection Results - Code Group - Code: QUAL01 - OKStatus / Valuation: Accept | After valuation for each MIC, the Status would change to Valuated. |  |
| 6 | Save Inspection Data | Choose Save. | Inspection results are saved. |  |

#### Make Usage Decision

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection is done and the inspection result is recorded. This process step shows you how to decide whether to accept the silo material depending on the inspection result or not.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Record Usage Decision (QA11). |  |  |
| 3 | Enter Inspection Lot | On the Record Usage Decision: Initial Screen, enter corresponding Inspection Lot number and choose Continue. | The Record Usage Decision: Characteristic Overview screen displays. |  |
| 4 | Check Characteristics | In the table under the Characteristics tab, choose the right arrow Other charac. list to expand Characteristics list.Check the Characteristics and inspection results recorded for each one. | Characteristics list displays. |  |
| 5 | Enter UD Code | Scroll down to the Usage Decision area, choose UD code and confirm with Choose.UD code: A1 (Accepted - unrestricted stock) | Note For demonstration purpose, we choose UD code A1 to accept the quantity into unrestricted stock. In real business case, you may want to select other UD code depending on the inspection results. You can refer to Quality Management in Procurement (1FM) scope item for more details. |  |
| 8 | Save Usage Decision | Choose Save. | The usage decision is made for the material. The system automatically triggers the material movements associated with the usage decision code. |  |

#### Display Material Stock after Quality Inspection

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to verify the material movement done based on the usage decision codes by looking again at the material stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Stock - Single Material (F1076). |  |  |
| 3 | Enter Selection | Make the following entries and press Enter:Material: <SG1010> | Stock for the material displays. |  |
| 4 | Check Stock Quantity | Batch #2 quantity is now under Unrestricted-Use Stock in storage location 331T. | The stock quantities are updated. |  |

### Batch Mixing in Main Tank

#### Create Process Order for Mixing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create process order for mixing batches.

Prerequisite

Batches are in place in the Main Tank and Day Tank respectively. Note down the two batches you need to mix.

Batch #1 in Main Tank (storage location 331Q): Batch number 1: ____________; Quantity 1: ____________. (You created in Stock Initiation for Batch #1 into Main Tank as described in Preliminary Steps.)

Batch #2 in Day Tank (storage location 331T): Batch number 2: ____________; Quantity 2: ____________. (You created in Receive Batch #2 into Day Tank from Procurement.)

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Process Order (COR1). |  |  |
| 3 | Enter Parameters | Make the following entries and choose Continue:Material Number: SG1010Production Plant: 3310Process Order Type: YQ10 |  |  |
| 4 | Enter General Data | On the General Data tab, make the following entries:Total Qty: <sum of quantities of the two batches>, for example, 200Scheduling - Type: Current date |  |  |
| 5 | Enter Goods Receipt Data | On the Goods Receipt tab, make the following entries:Receipt - Stor. Loc.: 331Q |  |  |
| 6 | Save | Choose Save.Make a note of this Process Order number: __________. | Process Order is saved.Note In this scenario, process order is configured as automatically released. |  |

#### Execute Batch Determination in Process Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to assign which batches need to be mixed for the process order.

Prerequisite

Process Order is already created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Process Order (COR2). |  |  |
| 3 | Enter Process Order Number | Make the following entries and choose Continue:Process order: <Process Order number you created> |  |  |
| 4 | Choose Material List | Choose Material List on the upper part of the screen. | The Change Process Order: Material List screen displays. |  |
| 5 | Perform Batch Determination | On the Change Process Order: Material List screen, one item of the silo material is listed in the Material List table. Select the item, and choose the Execute batch determinant symbolon at the top of the Material List table. | The Batch Determination CO: Select Batches screen displays.If the system shows the message Batch determination was carried out without selection specification, ignore it. |  |
| 6 | Copy Batch Determination Result | Batch #1 and Batch #2 are to be listed under Batch Selection part.Check the batch number and quantity, and choose Copy. |  |  |
| 7 | Check Material List | On the Change Process Order: Material List screen, another two items would appear in the Material List table, which is Batch #1 and Batch #2 respectively. Verify if relevant information is correct.Batch #1:Batch: Batch number #1Requirement Quantity: Quantity 1Storage Location: Main Tank 331QBatch #2:Batch: Batch number #2Requirement Quantity: Quantity 2Storage Location: Day Tank 331T |  |  |
| 8 | Save | Choose Save. | Batch #1 and Batch #2 are assigned to the Process Order. |  |

#### Review Process Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to review the created process order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Process Order (COR3). | The Display Process Order: Initial screen displays. |  |
| 3 | Enter Process Order Number | Make the following entry and choose Enter.Process Order: XXXX (From previous steps) | The Display Process Order: Header - General Data screen displays.On this screen, you can find the order’s detailed information. |  |

#### Goods Issue of Batch-Managed Components

Purpose

The withdrawal of the raw materials is used for the process order. This withdrawal can be done by using the picking list or doing a manual goods issue.

##### Goods Issue Via Pick List

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The released process order is now ready for picking. All materials that are moved to the production storage location can be issued to the process order using the pick list. This process step shows you how to post goods issue via pick list.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Pick Components for Process Orders (COIK). | The Picking List: Initial screen displays. |  |
| 3 | Enter Restriction and Execute | Make the following entries and then choose Execute.Profile: 000002Process Order: XXXX (from previous steps)Plant: 3310 | The Order Information System: Detail List of Components screen displays. |  |
| 4 | Picking Raw Materials | Batch #1 and Batch #2 should be listed for the order. Select them and choose Picking. |  |  |
| 5 | Post Goods Movements | Choose Post. | The goods movements for the two batches are posted. |  |

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
| 3 | Enter Process Order | Make the following entries and then choose Enter.Trans./Event: Goods IssueReference Document: OrderOrder Number: XXXX (from previous steps)Movement Type: 261 | The screen name adapts after entries are made. |  |
| 4 | Check Each Item | For each item displays, select Item OK. | Ensure that detail data is expanded. |  |
| 5 | Post Goods Movements | Choose Post. | The goods movements for the two batches are posted. |  |

#### Confirm Process Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The confirmation documents contain the processing status of order, operations, phases and individual capacities. It is an instrument to control the order. The time ticket confirmation allows recording either the default times for machine and labour usage, or actual times for major deviations. We can post scrap quantities as an optional. This process step shows you how to confirm the process order phase.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Confirm Process Order Phase (COR6N). | The Enter Time Ticket for Process Order screen displays. |  |
| 3 | Enter Confirmation Option | Make the following entries and then choose Enter.Order: XXXX (from previous steps)Phase: 0020Confirm Type: Final confirmation | If the system shows the message Total quantity confirmed not equal to planned quantity to be confirmed, choose Enter to ignore it. |  |
| 4 | Propose Actual Data Instruction | Choose Actual Data, which fills the Quantities and Activities automatically. |  |  |
| 5 | Save Confirmation | Choose Save. | Confirmation for Order XXXX is saved. |  |

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
| 3 | Enter Process Order | Make the following entries and then choose Enter:Trans./Event: Goods ReceiptReference Document: OrderOrder number: XXXX (from previous steps)Movement Type: 101 | Screen name adapts after entries are made. |  |
| 4 | Check Product | Check the products listed in the table. On the Where tab, make sure Storage Location is maintained.Storage Location: Main Tank 331Q. | Ensure that detail data is expanded. |  |
| 5 | Check Item | Select Item OK and choose Check in the lower right corner. In the Display logs dialog box, choose Continue. | The batch number is created automatically. |  |
| 6 | Post Goods Movement | Choose Post. | The goods movements are posted. |  |

#### Display Material Stock before Quality Inspection

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display the stock status of Batch #1, Batch #2 and the new batch after mixing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Stock - Single Material (F1076) |  |  |
| 3 | Enter Selection | Make the following entries and press Enter:Material: <SG1010> | Stock for the material displays. |  |
| 4 | Check New Batch after Mixing | The quantity of Batch #1 in Main Tank (storage location 331Q), unrestricted stock, and the quantity of Batch #2 in Day Tank (storage location 331T), unrestricted stock are gone, because they have been consumed by the process order confirmation.A new stock of the total stock quantity is posted in the Quality Inspection Stock, in Main Tank (storage location 331Q). | Stock status and quantities are verified for the new batch after mixing. Make a note of this new batch number. |  |

#### Display Open Inspection Lot

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to review the open inspection lot.

Prerequisite

In this scope item, the inspection lot is created automatically upon goods receipt for the process order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Technician. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Inspection Lots (F2343). | The Manage Inspection Lots (F2343) screen displays. |  |
| 3 | Filter Fields | Make the following entries and choose Go:Inspection Lot Origin: <Goods Receipt from Production>Plant: 3310Material: SG1010Inspection Lot Status: Outstanding |  |  |
| 4 | Select the Corresponding Inspection Lot | In the Inspection Lots table, select the corresponding inspection lot. |  |  |
| 5 | Check Inspection Lot | On the Origin tab, verify the referenced process order and material document.Check other details.Make a note of the inspection lot number: __________. | The process order number and material document number from which the inspection lot originates display. |  |

#### Record Inspection Results

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to enter and assign the QM results to the appropriate inspection lot for the new batch.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Technician. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Record Inspection Results (F1685A) | The Record Inspection Results screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go:Plant: 3310Material: SG1010Order: <Process Order number from previous step>. | If Order doesn't display in the Filters, choose Filters. Select Order and choose OK. Choose Go.You can also use Inspection Lot number as filter. |  |
| 4 | Select the Corresponding Inspection Lot | On the Inspection Lots tab, choose the inspection lot for which inspection results shall be recorded. | Two characteristics display to be inspected. |  |
| 5 | Enter Inspection Result | Choose Edit. Record results for each Master Inspection Characteristic (MIC) and make evaluation according to the inspection results.For MIC Purity:Inspection Results - Mean Value (%): 95Status / Valuation: AcceptFor MIC Visual Inspection:Inspection Results - Code Group - Code: QUAL01 - OKStatus / Valuation: Accept | After valuation for each MIC, the Status would change to Valuated. |  |
| 6 | Save Inspection Lot | Choose Save. | The inspection lot is saved. QM Inspection for manufactured goods has been performed and result recorded. |  |

#### Make Usage Decision

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection is done and the inspection result is recorded. This process step shows you how to decide whether or not to accept the silo material depending on the inspection result.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Record Usage Decision (QA11). |  |  |
| 3 | Enter Inspection Lot | On the Record Usage Decision: Initial Screen, enter corresponding Inspection Lot number and choose Continue. | The Record Usage Decision: Characteristic Overview screen displays. |  |
| 4 | Check Characteristics | In the table on the Characteristics tab, choose the right arrow Other charac. list to expand Characteristics list.Check the Characteristics and inspection results recorded for each one. | Characteristics list displays. |  |
| 5 | Enter UD Code | Scroll down to the Usage Decision area, choose UD code and confirm with Choose.UD code: A1 (Accepted - unrestricted stock) | Note: For demonstration purpose, we choose UD code A1 to accept the quantity into unrestricted stock. In real business case, you may want to select other UD code depending on the inspection results. You can refer to Quality Management in Discrete and Process Manufacturing (1E1) for more details. |  |
| 8 | Save Usage Decision | Choose Save. | The usage decision is made for the material. The system automatically triggers the material movements associated with the usage decision code. |  |

#### Display Material Stock after Quality Inspection

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to verify the done material movement based on the usage decision codes by looking again at the material stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Stock - Single Material (F1076). |  |  |
| 3 | Enter Selection | Make the following entries and press Enter:Material: <SG1010> | Stock for the material displays. |  |
| 4 | Check Stock Quantity | The quantity of the new batch is now in the Unrestricted-Use Stock column for storage location 331Q. |  |  |

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
| 2 | Start Search | Choose the Search icon on the upper right part of the screen. | An input field displays. |  |
| 3 | Search Criteria | Make the following entry and choose Search:BOM Header Material: <Material> (see the Master Data, Organizational Data, and Other Data section) | The system displays a list of objects that use the selected material. |  |
| 4 | Display Object | In the All field, choose the Down arrow button.Select an object and choose Search. | The list of objects is limited to the object type selected. If no object is selected, a message displays instead. |  |
| 5 | Tailor the Result Display | Under the search line, choose a symbol (for example, filter, display as table, sort, and so on) to filter the results list. | The results list is filtered according to your selections. |  |
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

## Connections
- part-of :: [[_cluster]]
- related-to :: [[12-production-and-manufacturing/test-script-tank-trailer-filling-with-residuals-42n-ae-997]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3UK_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 54,887 chars in the whole document
