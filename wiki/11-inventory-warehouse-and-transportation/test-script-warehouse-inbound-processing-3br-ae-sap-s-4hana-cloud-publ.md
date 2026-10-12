---
id: 11-inventory-warehouse-and-transportation/test-script-warehouse-inbound-processing-3br-ae-sap-s-4hana-cloud-publ
title: "Test Script: Warehouse Inbound Processing (3BR_AE) - SAP S/4HANA Cloud Public Edition (3BR_S4CLD2608_BPD_EN_AE)"
description: "Test script for SAP scope item 3BR (AE): Cloud WM inbound from delivery to putaway - batches, serials, HUs, GR, WTs, GR reversal, clarification zone, RF."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/ewm-inbound-processing]
aliases: [3BR_S4CLD2608_BPD_EN_AE]
keywords: [Warehouse Inbound Processing and SAP EWM Inbound Integration, warehouse inbound processing, inbound delivery, goods receipt posting, putaway warehouse tasks, warehouse task confirmation, handling units, packing instructions, goods receipt reversal, clarification zone]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3BR_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-921
topic: 11-inventory-warehouse-and-transportation/ewm-inbound-processing
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Warehouse Inbound Processing (3BR_AE) - SAP S/4HANA Cloud Public Edition (3BR_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3BR_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Warehouse Inbound Processing and SAP EWM Inbound Integration** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Warehouse Inbound Processing (3BR_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232852173)

[2 Prerequisites 4](#_Toc232852174)

[2.1 System Access 4](#_Toc232852175)

[2.2 Roles 4](#_Toc232852176)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232852177)

[2.4 Additional Manual Configuration 6](#_Toc232852178)

[2.5 Business Conditions 7](#_Toc232852179)

[2.6 Preliminary Steps 7](#_Toc232852180)

[2.6.1 Define Default Values for Warehouse Clerk (EWM) 7](#_Toc232852181)

[2.6.2 Define Default Values for Warehouse Operative (EWM) 8](#_Toc232852182)

[2.6.3 Assign Fixed Storage Bins to Products 9](#_Toc232852183)

[2.6.4 Manage Packing Instruction 9](#_Toc232852184)

[2.6.4.1 Create Packing Instruction 9](#_Toc232852185)

[2.6.4.2 Create Packing Instruction Determination 10](#_Toc232852186)

[3 Overview Table 12](#_Toc232852187)

[4 Test Procedures 15](#_Toc232852188)

[4.1 Assign or Create Batch (Optional) 15](#_Toc232852189)

[4.2 Change Stock Type (Optional) 16](#_Toc232852190)

[4.3 Capture Serial Number (Optional) 18](#_Toc232852191)

[4.4 Create Handling Unit (Optional) 20](#_Toc232852192)

[4.4.1 Variant 1: With Fiori App – Automatic Packing 20](#_Toc232852193)

[4.4.2 Variant 2: With Fiori App – Packing at Work Center 22](#_Toc232852194)

[4.4.3 Variant 3: With Radio Frequency Devices 25](#_Toc232852195)

[4.5 Post Goods Receipt 27](#_Toc232852196)

[4.5.1 Variant 1: With Fiori App 27](#_Toc232852197)

[4.5.2 Variant 2: With Radio Frequency Devices 28](#_Toc232852198)

[4.6 Create Putaway Warehouse Tasks 30](#_Toc232852199)

[4.6.1 Variant 1: With Fiori App 30](#_Toc232852200)

[4.6.2 Variant 2: With Radio Frequency Devices 32](#_Toc232852201)

[4.7 Reverse Goods Receipt (Optional) 34](#_Toc232852202)

[4.7.1 Cancel Putaway Warehouse Tasks 34](#_Toc232852203)

[4.7.2 Reverse Goods Receipt 35](#_Toc232852204)

[4.8 Confirm Warehouse Tasks 37](#_Toc232852205)

[4.8.1 Variant 1: With Fiori App 37](#_Toc232852206)

[4.8.2 Variant 2: With Radio Frequency Devices 38](#_Toc232852207)

[4.9 Clarification Zone (Optional) 40](#_Toc232852208)

[4.9.1 Check Material in Clarification Zone 40](#_Toc232852209)

[4.9.2 Create Warehouse Tasks from Clarification Zone to Final Bin 42](#_Toc232852210)

[4.9.3 Confirm Warehouse Tasks 43](#_Toc232852211)

[4.9.3.1 Variant 1: With Fiori App 43](#_Toc232852212)

[4.9.3.2 Variant 2: With Radio Frequency Devices 44](#_Toc232852213)

[5 Appendix 47](#_Toc232852214)

[5.1 Attachment Handling 47](#_Toc232852215)

[5.2 Process Integration 47](#_Toc232852216)

[5.2.1 Preceding Processes 47](#_Toc232852217)

[5.2.2 Succeeding Processes 50](#_Toc232852218)

## Purpose

Overview

In this process, products that are delivered with the intent to be stored in the warehouse are received and moved to a storage bin. This scope item allows different variants of inbound processing, such as inbound from supplier, inbound from another storage location, and inbound from another plant.

The process starts with an inbound delivery that is relevant for processing in the warehouse. Once the products arrive at the warehouse, batches and serial numbers can be assigned to the inbound delivery items and handling units can be created. Afterwards, the goods receipt is posted and warehouse tasks are created to execute the movements in the warehouse.

After moving the products to the final bin or the clarification zone (exceptional case), the warehouse tasks are confirmed accordingly.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

|  |
| --- |
| Note Caution Testing in a 3-System LandscapeIn a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape. |

### System Access

This section describes test procedures for each process step that belongs to this scope item.

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
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
| Material | TG11 | Trading Good for Reg. Trading (MRP planning) | For Storage |
| Material | TG12 | Trad.Good 12,Reorder Point,Reg.Trad. | For Fixed Bin Storage |
| Material | TG21 | Trad.Good 21,Reorder Point,Batch-FIFO | For Bulk Storage |
| Material | TG23 | Trad.Good 23,Reorder Point,Batch,Serialnr | Batch-managed with Serial Number Profile |
| Material | TG0011 | Trading Good 0011,PD,Regular Proc. | General Storage |
| Material | TG0013 | Trad. Good 0013,PD,Regular Proc. | General Storage |
| Material | TG0016 | Trad. Good 0016,Reord. Pt.,Reg. Proc. SerialNo | General Storage, used for process with serial numberSerial Number Profile SNPA |
| Material | TG0018 | Trading Good 0018,PD,Regular Proc. | General Storage, used for process with serial numberSerial Number Profile SNPC |
| Packaging Material | PMPALLET | Pallet |  |
| Packaging Material | PMPALLET_GTL | Pallet for GTL |  |
| Company Code | 3310 | Company Code 3310 |  |
| Purchase Organization | 3310 | Purchase Organization 3310 |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 335W | Warehouse |  |
| Storage Location | 335I | Warehouse |  |
| ERP Warehouse | 335 | Warehouse |  |
| Warehouse | 3350 | Warehouse |  |
| Division | 00 | Product Division 00 |  |
| Distribution Channel | 10 | Direct Sales |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/Setup/3BR_Set-Up_EN_XX.pdf)

Before you start the testing, please make sure that the steps in the [Warehouse Management Setup Guide.docx (Public)](https://support.sap.com/content/dam/SAAP/SAP_Activate/S4H_588%20Warehouse%20Management%20Setup.docx) published on SAP Activate Roadmap Viewer have been completed.

If you are working with a radio frequency device, carry out the steps described in Mobile RF Devices in Warehousing (63V).

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| All Scope Items |  |
| BNZ - Create New Open MM Posting Period - MDS | A new posting period was created as part of process BNZ- Create New Open MM Posting Period - MDS (Master Data Script).The posting period is up-to-date. |
| Inbound from Supplier |  |
| 2TX - Direct Procurement with Inbound Delivery | A purchase order was created as part of process 2TX- Direct Procurement with Inbound Delivery. At step Create Purchase Order Manually, follow the Option B: Create Purchase Order with Inbound Delivery. At step Create Inbound Deliveries, follow the Option A: Create Inbound Delivery. In both steps, use a warehouse-managed storage location, for example, Storage Location 335W (Stock in Warehouse) in the single storage location / availability group setup, or the storage location 335I (Stock in Putaway) in the two storage locations / availability groups setup. Also use the materials in the chapter Master Data, Organizational Data, and Other Data.Afterwards, an inbound delivery is created as part of process 2TX- Direct Procurement with Inbound Delivery.Note An additional storage location 335I and the corresponding availability group 002 can be introduced in the Cloud WM as an optional setup. Compared to the single storage location 335W / availability group 001 setup, the new setup can help distinguish stock that is still in the process of putaway and that is already in the warehouse.For example, the storage location 335I is used when creating a purchase order or an inbound delivery. During the inbound process, the stock remains in the storage location 335I and isn't available for sale (Stock Type F0 – Unrestricted Use in Putaway) until the putaway warehouse task(s) is/are confirmed. Once the putaway is finished, the stock is automatically posted to the storage location 335W and becomes available for sale (Stock Type F – Unrestricted Use in Warehouse).To enable the 335I storage location / availability setup, there are manual setup steps to be performed according to the instructions provided in the Warehouse Management Setup Guide. For more information, see chapter Additional Manual Configuration. |

### Preliminary Steps

#### Define Default Values for Warehouse Clerk (EWM)

Use

In this step, you define the default warehouse number for Warehouse Clerk (EWM).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log onto SAP Fiori Launchpad | Open the SAP Fiori Launchpad as Warehouse Clerk (EWM) |  |  |
| 2. | Choose the User Icon | Choose Icon for the logon user.Choose Settings. |  |  |
| 3. | Enter Default Value | Choose Default Values.Make the following entry in the section Material Management:Warehouse No.: 3350Choose Save. |  |  |

#### Define Default Values for Warehouse Operative (EWM)

Use

In this step, you define the default warehouse number for Warehouse Operative (EWM).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log onto SAP Fiori Launchpad | Open the SAP Fiori Launchpad as Warehouse Operative (EWM) |  |  |
| 2. | Choose the User Icon | Choose Icon for the logon user.Choose Settings. |  |  |
| 3. | Enter Default Value | Choose Default Values.And make the following entry in the section Material Management:Warehouse No.: 3350Choose Save. |  |  |

#### Assign Fixed Storage Bins to Products

Use

In this step, you assign fixed storage bins to products.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk (EWM) |  |  |
| 2 | Access the App | Open Assign Fixed Bins (/SCWM/BINMAT). |  |  |
| 3 | Enter the data | On the Assign Fixed Storage Bins screen, make the following entries:Warehouse Number: 3350.Product: TG12 .Choose Run. |  |  |
| 4 | Maintain Fixed Bin | Choose Edit to switch to change mode.Choose Append Row.Make the following entry:WhN: 3350 .Disposal: 33413310 .Storage Bin: SF01-03-04Product: TG12.ChooseSave. |  |  |

#### Manage Packing Instruction

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
| 6 | Maintain material and target quantity | In item 20, make the following entries:Item category: M Material.Component: Material number to be packed, for example, TG11.Target quantity: Quantity. |  |  |
| 7 | Enter Check Profile | In the Admin.data tab, enter 01 in the Check Profile field.01 is the pre-delivered SAP Standard Profile. |  |  |
| 8 | Save | Choose Save.Make a note of the packing instruction number: _____. | A packing instruction is created. |  |
| 9 | Create Alternative Packing Instructions | Repeat steps 2 to 8 to create an alternative packing instruction with the same component but different packing material and quantity. |  |  |

##### Create Packing Instruction Determination

Purpose

In this step, you create packing instruction determination records.

This function enables the system to find a packing instruction by specific characteristics. The condition technique is applied for this. You define a packing instruction that refers to specific characteristics, such as material and ship-to-party.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Handling Unit Data | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Determination Records - Master Data (POF1). | The Pkg Instruction - Create Determination Recs: Initial Screen is displayed. |  |
| 3 | Enter Determination Type | On the Pkg Instruction - Create Determination Recs: Initial Screen, make the following entries, and choose Enter.Determination Type: 0IBD – Inbound Delivery WM.Choose Enter.Note For the determination of the packing instruction with determination types 0IBD, only the following fields can be used:Warehouse NumberSupplierMaterial |  |  |
| 4 | Choose a key combination | On the key combination screen, choose a key combination, and select Choose.For example, choose WhseNmbr/Vendor/Material. |  |  |
| 5 | Enter the Packing Instruction Determination | On the Create Inbound Delivery WM (0IBD): Fast Entry screen, make the following entries:Warehouse Number:, for example 3350Supplier: <The supplier number>Material: for example TG11Packing instruction: <The Packing instruction number noted in the previous section>Altern.pack.instr. 1: <The Alternative Packing instruction number noted in the previous section> |  |  |
| 6 | Save | Choose Save. | The packing instruction determination is created. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App / Transaction | Expected Results |
| --- | --- | --- | --- |
| [Assign or Create Batch (Optional)](#unique_14) [page ] 15 | SAP_BR_WAREHOUSE_CLERK_EWM | Manage Inbound Deliveries – Warehouse (F7922) | One of the following system messages appear:Document was saved successfully.Data was successfully saved. |
| [Change Stock Type (Optional)](#unique_15) [page ] 16 | SAP_BR_WAREHOUSE_CLERK_EWM | Manage Inbound Deliveries – Warehouse (F7922) | The following system message appears: Data was successfully saved. |
| [Capture Serial Number (Optional)](#unique_16) [page ] 18 | SAP_BR_WAREHOUSE_CLERK_EWM | Manage Inbound Deliveries – Warehouse (F7922) |  |
| Create Handling Unit (Optional) |  |  | The Delivery Items have been removed from the Unpacked Items section. |
| [Variant 1: With Fiori App – Automatic Packing](#unique_17) [page ] 20 | SAP_BR_WAREHOUSE_CLERK_EWM | Manage Inbound Deliveries – Warehouse (F7922) |  |
| [Variant 2: With Fiori App – Packing at Work Center](#unique_18) [page ] 22 | SAP_BR_WAREHOUSE_CLERK_EWM | Manage Inbound Deliveries – Warehouse (F7922) |  |
| [Variant 3: With Radio Frequency Devices](#unique_19) [page ] 25 | SAP_BR_WAREHOUSE_OPERATIVE_EWM | Test RF Environment (/SCWM/RFUI) |  |
| Post Goods Receipt |  |  | The following system message appears: Goods receipt posted. |
| [Variant 1: With Fiori App](#unique_20) [page ] 27 | SAP_BR_WAREHOUSE_CLERK_EWM | Manage Inbound Deliveries – Warehouse (F7922) |  |
| [Variant 2: With Radio Frequency Devices](#unique_21) [page ] 28 | SAP_BR_WAREHOUSE_OPERATIVE_EWM | Test RF Environment (/SCWM/RFUI) |  |
| Create Putaway Warehouse Tasks |  |  | The following system message appears: Tasks created. |
| [Variant 1: With Fiori App](#unique_22) [page ] 30 | SAP_BR_WAREHOUSE_CLERK_EWM | Manage Inbound Deliveries – Warehouse (F7922) |  |
| [Variant 2: With Radio Frequency Devices](#unique_23) [page ] 32 | SAP_BR_WAREHOUSE_OPERATIVE_EWM | Test RF Environment (/SCWM/RFUI) |  |
| [Reverse Goods Receipt (Optional)](#unique_24) [page ] 34 |  |  |  |
| [Cancel Putaway Warehouse Tasks](#unique_25) [page ] 34 | SAP_BR_WAREHOUSE_CLERK_EWM | Manage Inbound Deliveries – Warehouse (F7922) |  |
| [Reverse Goods Receipt](#unique_26) [page ] 35 | SAP_BR_WAREHOUSE_CLERK_EWM | Manage Inbound Deliveries – Warehouse (F7922) |  |
| Confirm Warehouse Tasks |  |  | The following system message appears:Warehouse task xxx is to be confirmed.Warehouse task xxx was confirmed. |
| [Variant 1: With Fiori App](#unique_27) [page ] 37 | SAP_BR_WAREHOUSE_OPERATIVE_EWM | Process Warehouse Tasks (F4595) |  |
| [Variant 2: With Radio Frequency Devices](#unique_28) [page ] 38 | SAP_BR_WAREHOUSE_OPERATIVE_EWM | Test RF Environment (/SCWM/RFUI) |  |
| Clarification Zone: |  |  |  |
| [Check Material in Clarification Zone](#unique_29) [page ] 40 | SAP_BR_WAREHOUSE_CLERK_EWM | Warehouse Management Monitor Node Stock and Bin > Storage Bin > Available Stock | The Available Stock is displayed. |
| [Create Warehouse Tasks from Clarification Zone to Final Bin](#unique_30) [page ] 42 | SAP_BR_WAREHOUSE_CLERK_EWM | Warehouse Management Monitor Node Stock and Bin > Storage Bin > Available StockMonitor Method Create Warehouse Task | The following system message appears:Warehouse task xxx created.Warehouse order xxx created. |
| Confirm Warehouse Tasks |  |  | The following system message appears:Warehouse task xxx is to be confirmedWarehouse task xxx was confirmed |
| [Variant 1: With Fiori App](#unique_31) [page ] 43 | SAP_BR_WAREHOUSE_OPERATIVE_EWM | Process Warehouse Tasks (F4595) |  |
| [Variant 2: With Radio Frequency Devices](#unique_32) [page ] 44 | SAP_BR_WAREHOUSE_OPERATIVE_EWM | Test RF Environment (/SCWM/RFUI) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Assign or Create Batch (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Before posting the goods receipt, the Warehouse Clerk (EWM) can create a batch. Even when most batches are automatically created, it is also sometimes necessary to create batches manually.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
|  | Log on to the SAP Fiori launchpad | Log on to the SAP Fiori launchpad as a Warehouse Clerk (EWM). | The SAP Fiori Launchpad is displayed. |  |
|  | Access the SAP Fiori app | Open the SAP Fiori app Manage Inbound Deliveries – Warehouse (F7922). | The Manage Inbound Deliveries screen appears. |  |
|  | Choose Filters | On the Manage Inbound Deliveries screen, choose Adapt Filters. | The Adapt Filters dialog box appears. |  |
|  | Select Fields for Filter | On the Adapt Filters dialog box, make sure the following fields are selected for the current filter:Purchase Order.Choose OK. |  |  |
|  | Search for Inbound Delivery | On the Manage Inbound Deliveries screen, make the following entries:Purchase Order: <your purchase order number>.Choose Go. | Your inbound delivery is displayed. |  |
|  | Select Inbound Delivery | On the Manage Inbound Deliveries screen, choose your Inbound Delivery. |  |  |
|  | Choose Details | Choose button Details. | Inbound delivery details are displayed. |  |
|  | Choose Edit | Choose Edit to change the inbound delivery. |  |  |
|  | Choose Create Batch or Assign Existing Batch | Select a line item.In case you want to create a new Batch, proceed with step Create Batch.In case you want to assign an existing batch, proceed with step Assign Existing Batch. |  |  |
|  | Create Batch | Choose Create Batch. | The Create Batch dialog box appears. |  |
|  | Enter Batch Data | On the Create Batch dialog box, make the following entries:Batch: <specific batch value>Vendor Batch: <number under which the batch is managed at the supplier's> .BBD/ SLED: <date> . |  |  |
|  | Choose Ok | Choose Ok. |  |  |
|  | Assign Existing Batch | In the Batch Column, make the following entries:Batch: <existing batch number> . |  |  |
|  | Choose Save | Choose Save. | One of the following system messages appear:O bject saved |  |

### Change Stock Type (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In case the delivered items are of poor quality, the Warehouse Clerk (EWM) can change the stock type to Q- or B-Stock. Then the items are sent to the clarification zone.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
|  | Log on to the SAP Fiori launchpad | Log on to the SAP Fiori launchpad as a Warehouse Clerk (EWM). | The SAP Fiori Launchpad is displayed. |  |
|  | Access the SAP Fiori app | Open the SAP Fiori app Manage Inbound Deliveries – Warehouse (F7922). | The Manage Inbound Deliveries screen appears. |  |
|  | Choose Filters | On the Manage Inbound Deliveries screen, choose Adapt Filters. | The Adapt Filters dialog box appears. |  |
|  | Select Fields for Filter | On the Adapt Filters dialog box, make sure the following fields are selected for the current filter:Planned Delivery Date/TimePurchase OrderDocument NumberChoose OK. |  |  |
|  | Search for Inbound Delivery | On the Manage Inbound Deliveries screen, make the following entries:Planned Delivery Date/Time: <your planned delivery date/Time>.Purchase Order: <your purchase order number>.OrDocument Number: <your delivery number>Choose Go. | Your inbound delivery is displayed. |  |
|  | Select Inbound Delivery | On the Manage Inbound Deliveries screen, select your Inbound Delivery. |  |  |
|  | Choose Details | Choose button Details. | Inbound delivery details are displayed. |  |
|  | Edit Inbound Delivery | On the Manage Inbound Deliveries screen, choose Edit. |  |  |
|  | Choose Details | Select the item and choose button Details. | The item details are shown on the right side of the screen. |  |
|  | Change Stock Type | In the General Information of the item details, in the Stock Type field, make the following entries:Stock Type: Q or B.Choose Apply |  |  |
|  | Choose Save | Choose Save. | Data was successfully saved |  |

### Capture Serial Number (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, the Warehouse Clerk selects the delivery and enters the serial numbers for the products.

If the products are serial number-managed, you can enter the serial numbers in this step. Alternatively, you can also enter the serial numbers in the Create Handling Unit (Optional) - Variant 2: With Fiori App - Packing at Work Center, if packing is relevant to your products.

For the serial number-managed products, see the Master Data, Organizational Data, and Other Data chapter.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
|  | Log on to the SAP Fiori launchpad | Log on to the SAP Fiori launchpad as a Warehouse Clerk (EWM). | The SAP Fiori Launchpad is displayed. |  |
|  | Access the SAP Fiori app | Open the SAP Fiori app Manage Inbound Deliveries – Warehouse (F7922). | The Manage Inbound Delivery screen appears. |  |
|  | Choose Filters | On the Manage Inbound Deliveries screen, select Adapt Filters. | The Adapt Filters dialog box appears. |  |
|  | Select Fields for Filter | On the Adapt Filters dialog box, make sure the following fields are selected for the current filter:Planned Delivery Date/TimeDocument NumberPurchase Order.Choose OK. |  |  |
|  | Search for Inbound Delivery | On the Manage Inbound Deliveries screen, make the following entries:Planned Delivery Date/Time: <your planned delivery date/Time>.Purchase Order: <your purchase order number>.OrDocument Number: <your delivery number>Choose Go. | Your inbound delivery is displayed. |  |
|  | Select Inbound Delivery | On the Manage Inbound Deliveries screen, select your Inbound Delivery. |  |  |
|  | Choose Details | Choose button Details. | Inbound delivery details are displayed. |  |
|  | Choose Edit | Choose Edit to change the inbound delivery. |  |  |
|  | Choose Details | Select the item and choose button Details | Item details are displayed on the right side of the screen. |  |
|  | Choose Serial Number | On the right screen, choose tab page Serial Numbers. |  |  |
|  | Choose Assign Serial Numbers | In the Serial Numbers tag page, choose Assign Serial Numbers.Note It is possible to inherit serial numbers from the SAP S/4HANA inbound delivery document. It is also possible to change these inherited serial numbers in the Cloud WM in-bound delivery document. The SAP S/4HANA inbound delivery should be updated with the serial numbers entered in the EWM delivery document.The serial number is maximum 18 characters long. |  |  |
|  | Enter Serial Number | On the Serial Number Assignment screen, enter the serial numbers in the Serial Number field one by one. You may also delete the already assigned serial numbers and assign different serial numbers.Choose Apply when finished. | The Serial Numbers have been entered.. |  |
|  | Note down your Delivery number | Note down your delivery number for testing purposes. |  |  |

### Create Handling Unit (Optional)

#### Variant 1: With Fiori App – Automatic Packing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, the Warehouse Clerk (EWM) chooses the delivery. The Warehouse Clerk (EWM) creates handling units for Unpacked Items and can push a single button and then the system automatically packs all delivery items based on the packing instructions defined upfront (enabled by the unified package builder).

|  |
| --- |
| Note Note The automatic packing works, if packing instructions are defined for the relevant product. |

|  |
| --- |
| Note Caution This step is mandatory for material TG21, as it needs to be placed in SB01, where the handling unit requirement is set.If the products are serial number-managed, you need to use the Variant 2: With Fiori App - Packing at Work Center. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
|  | Log on to the SAP Fiori Launchpad | Log on to the SAP Fiori launchpad as a Warehouse Clerk (EWM). | The SAP Fiori Launchpad is displayed. |  |
|  | Access the SAP Fiori App | Open the SAP Fiori app Manage Inbound Deliveries – Warehouse (F7922). | The Manage Inbound Delivery. screen appears. |  |
|  | Choose Filters | On the Manage Inbound Deliveries screen, choose Adapt Filters. | The Adapt Filters dialog box appears. |  |
|  | Select Fields for Filter | On the Adapt Filters dialog box, make sure the following fields are selected for the current filter:Purchase Order.Choose OK. |  |  |
|  | Search for Inbound Delivery | On the Manage Inbound Deliveries screen, make the following entries:Purchase Order: <your purchase order number>.Choose Go. | Your inbound delivery is displayed. |  |
|  | Select Inbound Delivery | On the Manage Inbound Deliveries screen, select your inbound delivery. |  |  |
|  | Choose Details | Choose button Details. | Inbound delivery details are displayed. |  |
|  | Select Unpacked Items | On the Manage Inbound Deliveries screen in the Items section, choose the Unpacked Items tab and select the items to be packed. |  |  |
|  | Decide Packing Options | If packing instructions are defined for all the delivery items, you can pack automatically. In this case, follow step 10.If no packing instructions arefined for all the delivery items, you can pack manually. In this case, follow steps 11 to 13. |  |  |
|  | Pack Automatically | Choose Pack Automatically to pack all unpacked items automatically based on the packing instructions. |  |  |
|  | Choose Create HU | Choose Create HUs or Create Mixed HUs. |  |  |
|  | Enter Packaging Material and Number of HUs | On the Create Handling Unit dialog box, make the following entries:Pack. Material: PMPALLET.Number of HUs: <number of handling units>. |  |  |
|  | Choose Create | Choose Create. | The Delivery Items have been removed from the Unpacked Items section. |  |
|  | Note Down your Delivery Number | Note down your delivery number for testing purposes. | On the Manage Inbound Deliveries screen on the Total Items tab, it shows No. of HUs: X. |  |

#### Variant 2: With Fiori App – Packing at Work Center

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, the Warehouse Clerk (EWM) creates handling units for unpacked items in the packing work center. Automatic packing is also enabled by the unified package builder, if packing instructions have been defined upfront for the relevant product.

|  |
| --- |
| Note Caution This step is mandatory for material TG21, as it needs to be placed in SB01, where the handling unit requirement is set.If the products are serial number-managed and are to be packed into HUs, you can assign serial numbers in this step. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
|  | Log on to the SAP Fiori Launchpad | Log on to the SAP Fiori launchpad as a Warehouse Clerk (EWM). | The SAP Fiori Launchpad is displayed. |  |
|  | Access the SAP Fiori App | Open the SAP Fiori app Manage Inbound Deliveries – Warehouse (F7922). | The Manage Inbound Delivery. screen appears. |  |
|  | Choose Filters | On the Manage Inbound Deliveries screen, choose Adapt Filters. | The Adapt Filters dialog box appears. |  |
|  | Select Fields for Filter | On the Adapt Filters dialog box, make sure the following fields are selected for the current filter:Purchase Order.Choose OK. |  |  |
|  | Search for Inbound Delivery | On the Manage Inbound Deliveries screen, make the following entries:Purchase Order: <your purchase order number>.Choose Go. | Your inbound delivery is displayed. |  |
|  | Select Inbound Delivery | On the Manage Inbound Deliveries screen, select your inbound delivery. |  |  |
|  | Choose Details | Choose button Details. | Inbound delivery details are displayed. |  |
|  | Go to Packing Work Center | On the Manage Inbound Deliveries screen, choose Related Apps – Work Center Packing for Inbound Delivery. |  |  |
|  | Decide Packing Options | If packing instructions are defined for all the delivery items, you can pack automatically. In this case, follow step 10.If packing instructions are defined for some of the delivery items, you can pack those items based on packing proposals. In this case, follow steps 11 and 12.You can also pack completely manually. In this case, follow steps 13 to 15. |  |  |
|  | Pack Automatically | On the Work Center Packing for Inbound Delivery (Time Zone CET) screen, select all the delivery items and then choose Pack Automatically. | HUs have been created automatically according to the pre-defined Packing Instruction. |  |
|  | Pack with Packing Proposals | On the Work Center Packing for Inbound Delivery (Time Zone CET) screen, select one of the delivery items (with packing instruction defined) and then choose Packing Proposal. |  |  |
|  | Check Packing Proposals | In the Packing Proposal dialog box, check that the packaging material matches the packaging material maintained in the packing instruction for the supplier of the inbound delivery.The proposed quantities correspond the quantities of your packing instruction.Select the desired proposal and then choose Enter. | An HU has been created according to the pre-defined Packing Instruction. |  |
|  | Create HUs Manually | On the Work Center Packing for Inbound Delivery (Time Zone CET) screen, choose Create HU tab, and make the following entries:Pack. Material: PMPALLET.Number of HUs: <number of handling units>.Choose Execute.Take a note of the HU numbers created. |  |  |
|  | Repack Product | Choose Repack Product tab, and make the following entries:Delivery Number: <your Inbound Delivery Number>.Item Number: <item Number, for example 10>.Quantity: <quantity to be packed in the destination HU>.Unit of Measure: <UoM, for example PC>.Dest. HU: <one of the HU created in step 12>.Choose Execute. |  |  |
|  | Repeat Repacking Product | Repeat step 13 until all products have been repacked into HUs. |  |  |
|  | Enter Serial Numbers (optional) | At the lower left part of the screen, double click the product that has been packed into an HU, and then choose the Serial Nos tab.Enter the serial numbers manually for each unit of the material or choose Create SNs Automatically to allow the system assignment of the serial numbers.Note If the products are serial number-managed and are to be packed into HUs, you can assign serial numbers in this step. |  |  |
|  | Choose Save | Choose Save. |  |  |
|  | Exit the Packing Work Center | Choose Exit. |  |  |
|  | Note Down your Delivery Number | Note down your delivery number for testing purposes. | On the Manage Inbound Deliveries screen on the All Items tab, it shows Serial Numbers: X / X. |  |

#### Variant 3: With Radio Frequency Devices

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, the Warehouse Operative (EWM) creates handling units for unpacked products by delivery using a mobile RF device.

|  |
| --- |
| Note Caution This step is mandatory for material TG21, as it needs to be placed in SB01, where the handling unit requirement is set.If the products are serial number-managed and are to be packed into HUs, you need to create handling units using Variant 2: with Fiori App - Packing at Work Center.For working with mobile RF devices, make sure all the steps as described in the Setup Instruction guide for scope item 63V - Mobile RF Devices in Warehousing have been performed. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
|  | Log on to the SAP Fiori Launchpad | Log on to the SAP Fiori launchpad as a Warehouse Operative (EWM). | The SAP Fiori Launchpad is displayed. |  |
|  | Access the SAP Fiori App | Open the SAP Fiori app Test RF Environment(/SCWM/RFUI)The app allows you to test working in an RF environment. For working with mobile RF devices, see also SAP Note 3048632. |  |  |
|  | Enter Data for RFUI | Whse No: 1750Resource: SHA1-1 or SHR1-1Dflt Dvc.: SE01Choose Enter. |  |  |
|  | Choose Menu | Choose 03 Inbound Processes > 02 Receiving of HUs > 01 Rec. HU By Delivery . |  |  |
|  | Enter Delivery Number | In the Delivery field, enter your delivery number. |  |  |
|  | Check Delivery Information | The inbound delivery is now displayed with the following information:DeliveryPartner (number and name)Warehouse Door (only displayed if applicable)No. of HUs (number of HUs that HUs that have been created up to this point of time)Choose Enter to proceed. |  |  |
|  | Check Delivery Status | Check the following information that shows the delivery process status:Proc.HUs: Y / YPck.Compl. : (X) or emptyGR Posted: XWT Created: EmptyNote Note Note The Proc.HUs field indicates the status of the HU processing. Y indicates the number of HUs that have been created. X indicates the number of HUs that have been processed.If all the unpacked products have been processed, the field Pck.Compl. is checked and you can go to process step Post Goods Receipt Variant 2: With Radio Frequency Devices. Otherwise go to step 8 to continue to create new HUs. |  |  |
|  | Create New HU | Choose New HU.On the next screen, enter the following values:Product: <Product Number>Actual Qty: <Quantity> <UoM>BstBefDate: <Best before Date, in format DD.MM.YYYY> (if applicable)Choose Next. |  |  |
|  | Enter Packaging Material | Enter values in the following fields:New P.Mat. (Packaging Material)Choose Enter. The HU type gets populated.Choose Next. |  |  |
|  | Check HU Information | Check the information of the newly created HU. Take a note of the following fields, if necessary:HU (HU number)Batch (Batch number)Styp (Stock Type)ProTyp (Warehouse Process Type)Choose Back. |  |  |
|  | Repeat Steps | Repeat steps 8 to 10 until all the unpacked products are packed into HUs. Partial packing is allowed. If each unpacked product is packed into Hus, the field Pck.Compl. is checked. |  |  |
|  | Logoff RFUI | You can choose Back to go to the previous screens.Note Note Note If you would like to post a goods receipt using the mobile RF devices, stay logged on in the app.Choose Logoff.Choose Save. |  |  |

### Post Goods Receipt

#### Variant 1: With Fiori App

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The goods receipt is being posted. SAP S/4HANA is being updated accordingly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Fiori Launchpad | Log on to the SAP Fiori launchpad as a Warehouse Clerk (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open the SAP Fiori app Manage Inbound Deliveries – Warehouse (F7922). | The Manage Inbound Delivery. screen appears. |  |
| 3 | Choose Filters | On the Manage Inbound Deliveries screen, choose Adapt Filters. | The Adapt Filters dialog box appears. |  |
| 4 | Select Fields for Filter | On the Adapt Filters dialog box, make sure the following fields are selected for the current filter:Planned Dlv. DatePurchase OrderChoose OK. |  |  |
| 5 | Search for Inbound Delivery | On the Manage Inbound Deliveries screen, make the following entries:Planned Delivery Date/Time: <your planned delivery date/Time>.Purchase Order: <your purchase order number>.Choose Go. | Your inbound delivery is displayed. |  |
| 6 | Select Inbound Delivery | On the Manage Inbound Deliveries screen, select your inbound delivery. |  |  |
|  | Choose Details | Choose button Details. | Inbound delivery details are displayed. |  |
| 8 | Select Delivery Items | On the Manage Inbound Deliveries screen, select your Delivery Items. |  |  |
| 9 | Post Goods Receipt | Choose Goods Receipt. | The following system message appears:Goods receipt posted. |  |

#### Variant 2: With Radio Frequency Devices

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, the Warehouse Operative (EWM) posts a goods receipt for deliveries using a mobile RF device.

If no handling units are to be created for unpacked products, you can still use the RF device to post the goods receipt. However, it is impossible to create putaway warehouse tasks with it.

For working with mobile RF devices, make sure all the steps as described in the setup instruction guide for scope item 63V - Mobile RF Devices in Warehousing are performed.

[Link to Set-Up Instructions](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/Setup/63V_Set-Up_EN_XX.pdf)

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Fiori Launchpad | Log on to the SAP Fiori launchpad as a Warehouse Operative (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open the SAP Fiori app Test RF Environment(/SCWM/RFUI)The app allows you to test working in an RF environment. For working with mobile RF devices, see also SAP Note 3048632. |  |  |
| 3 | Enter Data for RFUI | Whse No: 1750Resource: SHA1-1 or SHR1-1Dflt Dvc.: SE01Choose Enter. |  |  |
| 4 | Choose Menu | Choose 03 Inbound Processes > 02 Receiving of HUs > 01 Rec. HU By Delivery . |  |  |
| 5 | Enter Delivery Number | In the Delivery field, enter your delivery number. |  |  |
| 6 | Check Delivery Information | The inbound delivery is now displayed with the following information:DeliveryPartner (number and name)Warehouse Door (only displayed if applicable)No. of HUs (number of HUs that HUs that have been created up to this point of time)Choose Enter to proceed. |  |  |
| 7 | Check Delivery Status | Check the following information that shows the delivery process status:Proc.HUs: X / YPck.Compl. :X or emptyGR Posted:EmptyWT Created: EmptyNote Note Note The Proc.HUs field indicates the status of the HU processing. Y indicates the number of HUs that are created. X indicates the number of HUs that have been processed.If HUs have been created for all the unpacked products, the field Pck.Compl. is checked. |  |  |
| 8 | Post Goods Receipt | Choose > and then choose PostGRNote Note Note If no HUs are created, you can still post goods receipts for all the unpacked products. In this case, you receive a system message Delivery not fully packed. Continue?. Choose Yes to continue. | The field GR Posted is checked |  |
| 9 | Logoff RFUI | Choose Back to go to the the previous screens.Note Note Note If you would like to create putaway warehouse tasks using the mobile RF devices, stay logged on in the app.Choose Logoff.Choose Save. |  |  |

### Create Putaway Warehouse Tasks

#### Variant 1: With Fiori App

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The goods receipt is being posted. SAP S/4HANA is being updated accordingly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Fiori Launchpad | Log on to the SAP Fiori launchpad as a Warehouse Clerk (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open the SAP Fiori app Manage Inbound Deliveries – Warehouse (F7922). | The Manage Inbound Delivery. screen appears. |  |
| 3 | Choose Filters | On the Manage Inbound Deliveries screen, choose Adapt Filters. | The Adapt Filters dialog box appears. |  |
| 4 | Select Fields for Filter | On the Adapt Filters dialog box, make sure the following fields are selected for the current filter:Planned Dlv. DatePurchase OrderChoose OK. |  |  |
| 5 | Search for Inbound Delivery | Planned Delivery Date/Time: <your planned delivery date/Time>.Purchase Order: <your purchase order number>.Choose Go. | Your inbound delivery is displayed. |  |
| 6 | Select Inbound Delivery | On the Manage Inbound Deliveries screen, select your inbound delivery. |  |  |
|  | Choose Details | Choose button Details. | Inbound delivery details are displayed. |  |
| 8 | Select Delivery Items | On the Manage Inbound Deliveries screen, select your delivery items. |  |  |
| 9 | Choose Create Warehouse Tasks | Choose Create Putaway Tasks Automatically. | The following system message appears:Tasks created. |  |
| 10 | Choose Warehouse Tasks | In the Items section, choose Yes in the Open PutawayWarehouse Tasks field. | The warehouse task(s) created is displayed. Make a note of the warehouse task number. |  |

#### Variant 2: With Radio Frequency Devices

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Operative (EWM) creates warehouse tasks for putaway using a radio frequency device.

|  |
| --- |
| Note Warehouse task creation with RF devices is only applicable for handling units. If the goods receipt is posted for unpacked products, create putwawy warehouse tasks using the Fiori App as described in variant 1. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Fiori Launchpad | Log on to the SAP Fiori launchpad as a Warehouse Operative (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open the SAP Fiori app Test RF Environment(/SCWM/RFUI)The app allows you to test working in an RF environment. For working with mobile RF devices, see also SAP Note 3048632. |  |  |
| 3 | Enter Data for RFUI | Whse No: 1750Resource: SHA1-1 or SHR1-1Dflt Dvc.: SE01Choose Enter. |  |  |
| 4 | Choose Menu | Choose 03 Inbound Processes > 02 Receiving of HUs > 01 Rec. HU By Delivery . |  |  |
| 5 | Enter Delivery Number | In the Delivery field, enter your delivery number. |  |  |
| 6 | Check Delivery Information | The inbound delivery is now displayed with the following information:DeliveryPartner (number and name)Warehouse Door (only displayed if applicable)No. of HUs (number of HUs that HUs that have been created up to this point of time)Choose Enter to proceed. |  |  |
| 7 | Check Delivery Status | Check the following information that shows the delivery process status:Proc.HUs: Y / YPck.Compl. :X or emptyGR Posted:XWT Created: EmptyNote Note The Proc.HUs field indicates the status of the HU processing. Y indicates the number of HUs that are created and have been processed.The Pck.Compl. field is checked to indicate that the packing is completed.The GR Posted field is checked to indicate that the goods receipt posting is completed.It is not allowed to post a partial goods receipt for an inbound delivery in the Cloud WM. Therefore, if you try to create warehouse tasks before the goods receipt posting is completed, you get an error message E: Cannot create WT for warehouse request XXXX, goods receipt missing. |  |  |
| 8 | Create Warehouse Task | Choose NewWT.Note Note You can also create warehouse task for each Handling Unit one after another. In doing so, you can choose List, enter the HU number and choose CrWT in the HU detail screen. | The WT Created field is now checked. |  |
| 9 | Logoff RFUI | Choose Back to go to the the previous screens.Note Note Note If you would like to create putaway warehouse tasks using the mobile RF devices, stay logged on in the app.You can also confirm the created warehouse tasks right away, instead of confirming them later from the queue selection as de-scribed in the next step Confirm Warehouse Tasks - Variant 2: with Radio Frequency Devices.Choose Logoff.Choose Save. |  |  |

### Reverse Goods Receipt (Optional)

Purpose

You want to reverse the Goods Receipt of an inbound delivery distributed to the Cloud WM.

|  |
| --- |
| Note You can reverse the goods receipt of the stock through app Manage Inbound Deliveries – Warehouse (F7922). If any of the following restrictions apply to one of the items, the GRR will not be possible:Putaway status is already completed – Warehouse Tasks for putaway to a final Storage Type have been confirmed.There are open Warehouse Tasks for any items.Any Item that is Quality Inspection relevant and the Usage Decision is already made.Stock content has been changed, for example goods receipt was posted using a handling unit and this handling unit has been deleted, or the stock type has been changed with a posting change. |

#### Cancel Putaway Warehouse Tasks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Before reversing the goods receipt, you have to cancel open putaway warehouse tasks for any items in the inbound delivery. Confirmed putaway warehouse tasks cannot be cancelled.

You can skip this step if no putaway warehouse tasks have been created so far.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
|  | Log on to the SAP Fiori launchpad | Log on to the SAP Fiori launchpad as a Warehouse Clerk (EWM). | The SAP Fiori Launchpad is displayed. |  |
|  | Access the SAP Fiori app | Open the SAP Fiori app Manage Inbound Deliveries – Warehouse (F7922). | The Manage Inbound Deliveries - Deliveries screen appears. |  |
|  | Choose Filters | On the Manage Inbound Deliveries screen, choose Adapt Filters. | The Adapt Filters dialog box appears. |  |
|  | Select Fields for Filter | On the Adapt Filters dialog box, make sure the following fields are selected for the current filter:Planned Delivery Date/ Time.Inbound Delivery.Choose OK. |  |  |
|  | Search for Inbound Delivery | On the Manage Inbound Deliveries screen, make the following entries:Planned Delivery Date/Time: <your planned delivery date/Time>.Inbound Delivery: <your Inbound Delivery number>.Choose Go. | Your inbound delivery is displayed. |  |
|  | Select Inbound Delivery | On the Manage Inbound Deliveries screen, select your Inbound Delivery. |  |  |
|  | Choose Details | Choose button Details. | Inbound delivery details are displayed. |  |
|  | Display Warehouse Tasks | On the Manage Inbound Deliveries screen, choose Yes in the Open PutawayWarehouse Tasks fieldin the delivery item line(s). | The Process Warehouse Tasks screen appears and the open warehouse tasks are displayed. |  |
|  | Cancel Warehouse Tasks | On the Process Warehouse Tasks screen, select all the warehouse tasks, and then choose Cancel. |  |  |
|  | Confirm System Message | Choose Yes in the confirmation dialog box (Do you want to cancel the selected warehouse tasks?). |  |  |

#### Reverse Goods Receipt

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
|  | Log on to the SAP Fiori Launchpad | Log on to the SAP Fiori launchpad as a Warehouse Clerk (EWM). | The SAP Fiori Launchpad is displayed. |  |
|  | Access the SAP Fiori App | Open the SAP Fiori app Manage Inbound Deliveries – Warehouse (F7922). | The Manage Inbound Deliveries - Deliveries screen appears. |  |
|  | Choose Filters | On the Manage Inbound Deliveries screen, choose Adapt Filters. | The Adapt Filters dialog box appears. |  |
|  | Select Fields for Filter | On the Adapt Filters dialog box, make sure the following fields are selected for the current filter:Planned Delivery Date/ TimeInbound DeliveryChoose OK. |  |  |
|  | Search for Inbound Delivery | On the Manage Inbound Deliveries screen, make the following entries:Planned Delivery Date/Time: <your planned delivery date/Time>.Inbound Delivery: <your Inbound Delivery number>.Choose Go. | Your inbound delivery is displayed. |  |
|  | Select Inbound Delivery | On the Manage Inbound Deliveries screen, select your inbound delivery. |  |  |
|  | Reverse Goods Receipt | On the Manage Inbound Deliveries screen, choose Open Menu button of the Post Goods Receipt and then choose Reverse Goods Receipt. |  |  |
|  | Confirm System Message | Choose Yes in the confirmation dialog boxDo you really want to reverse the goods receipt?. | The following system message appears:Goods receipt reversal was successful.Goods Receipt Status is now back to Not Started. |  |

|  |
| --- |
| Note Note: There are different business use cases where the Goods Receipt reversal is not necessary or applicable.Entry of quantity differences during putaway:If you want to enter a different quantity than the one that is in the inbound delivery during putaway, you don’t have to reverse the whole inbound delivery. Instead, you can enter differences during the confirmation of warehouse tasks with app Confirm Warehouse Tasks - Advanced. In this case, you must enter an exception code for the confirmation. For example with exception code DIFD, if you're changing the quantity when confirming a putaway warehouse task, the changed quantity reduces the quantity of the inbound delivery item.Creation of return delivery:If the putaway warehouse tasks have already been confirmed, you will not be able to reverse the goods receipt. In this case, you need to create a return purchase order, based on which you can create an outbound delivery, pick the stock and post goods issue. Follow the steps described in scope item Return to Supplier (BMK) as well as the instructions described in the Business Conditions of this test script. |

### Confirm Warehouse Tasks

#### Variant 1: With Fiori App

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The goods receipt is being posted. SAP S/4HANA is being updated accordingly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Fiori Launchpad | Log on to the SAP Fiori launchpad as a Warehouse Clerk (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open the SAP Fiori app Process Warehouse Tasks - (F4595). | The Confirm Warehouse Tasks screen appears. |  |
| 3 | Enter Warehouse Task Number | On the Process Warehouse Tasks screen, make the following entries:Warehouse Task: <Your warehouse task number>.Choose Go. |  |  |
| 4 | Check Warehouse Task Details | If you would like to check the serial numbers assigned, follow step 4-7. Otherwise go directly to step 7.Choose the Warehouse Task to go into the Warehouse Task details. |  |  |
| 5 | Choose Serial Number link | On the Warehouse Task screen, in the Movement Data section, choose No. of Serial Numbers Entered: X / X. |  |  |
| 6 | Check Serial Number | On the Serial Number Assignment screen, check the serial numbers in the List of Serial Numbers.Choose Cancel twice to go back to the Process Warehouse Task screen. |  |  |
| 7 | Confirm Warehouse Task | Mark the checkbox for the selected warehouse task and choose Confirm. | The following system message appears:Warehouse task confirmed.. |  |

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

For working with mobile RF devices, make sure all the steps as described in the setup instruction guide for scope item 63V - Mobile RF Devices in Warehousing have been performed.

[Link to Set-Up Instructions](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/Setup/63V_Set-Up_EN_XX.pdf)

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Fiori Launchpad | Log on to the SAP Fiori launchpad as a Warehouse Operative (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open the SAP Fiori app Test RF Environment(/SCWM/RFUI)Note The app allows you to test working in an RF environment. For working with mobile RF devices, see also SAP Note [3048632](https://me.sap.com/notes/3048632). |  |  |
| 3 | Enter Data for RFUI | Whse No: 1750Resource: SHA1-1 or SHR1-1DefPresDvc.: SE01Choose Enter.Note Use resource SHA1-1 for putting away to S001.Use SHR1-1 for putting away to storage types other than S001. |  |  |
| 4 | Choose Menu | Choose 01 System-Guided > 02 SystemGuided Queue. |  |  |
| 5 | Enter Queue Name | In the Queue field, enter SI-001, SI-F01, SI-B01, SI-G01, or SI-970. |  |  |
| 6 | Verify Source Bin and Enter HU | Note This step is only relevant, if you create handling unit for a goods receipt.Verify the Src.Bin (Source Bin)HU: < Enter the HU ID from step Create Handling Unit (Optional)> |  |  |
| 7 | Verify the Source information fields | Verify the following fields, if they are required:Src.Bin (Source Bin)Prod. (Product)Srce Qty (Source Quantity)Choose Enter. |  |  |
| 8 | Verify the Destination Information fields | Verify the following fields, if they are required:Prod. (Product)ActQty (Quantity)Dest.Qty (Destination Quantity)DstBin (Destination Bin)Choose Enter. |  |  |
| 9 | Repeat Steps | Repeat steps 6 to 8 until no suitable warehouse orders are found. |  | All putaway warehouse tasks have been confirmed. |
| 10 | Logoff RFUI | Choose Back to go to the the previous screens.Choose Logoff.Choose Save.Note If you have the two availability groups setup for your warehouse as described in the Business Condition for 2TX, as soon as the putaway warehouse tasks are confirmed, the system automatically posts the stock type for this stock from ‘Unrestricted Use in Putaway (F0)’ to ’Unrestricted Use in Warehouse (F)’. |  |  |

### Clarification Zone (Optional)

#### Check Material in Clarification Zone

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Clerk (EWM) checks the material that is on the clarification zone. In case of missing information (for example, PACI), they maintain the required information and decide what to do with the material.

|  |
| --- |
| Note Note The following reasons lead to destination bin Clarification Zone:No putaway control indicator (PACI) maintained for the productNo fix bin assignment for products with putaway control indicator to fix bin storage typeQuality- or blocked stockNo free bin in the storage type |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
|  | Log on to the SAP Fiori Launchpad | Log on to the SAP Fiori launchpad as a Warehouse Clerk (EWM). | The SAP Fiori Launchpad is displayed. |  |
|  | Access the SAP Fiori App | Open the SAP Fiori app Warehouse Monitor(/SCWM/MON). | The Warehouse Monitor(/SCWM/MON) dialog box appears. |  |
|  | Enter Default Values | On the Warehouse Management Monitor dialog box, make the following entries:Warehouse Number: <your warehouse number>Monitor: SAP |  |  |
|  | Choose Execute | On the Warehouse Management Monitor dialog box, choose Execute. | The Warehouse Management Monitor SAP - Warehouse Number xxx screen appears. |  |
|  | Navigate to Available Stock | On the Warehouse Management Monitor SAP - Warehouse Number xxx screen, choose Stock and Bin > Storage Bin > Available Stock . |  |  |
|  | Display Available Stock | Choose the node Available Stock by double-clicking on it. | The /SCWM/SAPLSTOCK_OVERVIEW_MON dialog box appears. |  |
|  | Enter Product | On the /SCWM/SAPLSTOCK_OVERVIEW_MON dialog box, make the following entries:ExampleStorage Type: S970 - Clarification Zone |  |  |
|  | Choose Execute | On the /SCWM/SAPLSTOCK_OVERVIEW_MON dialog box, choose Execute. | The Available Stock is displayed. |  |

#### Create Warehouse Tasks from Clarification Zone to Final Bin

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Clerk (EWM) creates Warehouse Tasks for Putaway.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
|  | Log on to the SAP Fiori launchpad | Log on to the SAP Fiori launchpad as a Warehouse Clerk (EWM). | The SAP Fiori Launchpad is displayed. |  |
|  | Access the SAP Fiori app | Open the SAP Fiori app Warehouse Monitor(/SCWM/MON). | The Warehouse Monitor(/SCWM/MON) dialog box appears. |  |
|  | Enter Default Values | On the Warehouse Management Monitor dialog box, make the following entries:Warehouse Number: <your warehouse number> |  |  |
|  | Choose Execute | On the Warehouse Management Monitor dialog box, choose Execute. | The Warehouse Management Monitor SAP - Warehouse Number xxx screen appears. |  |
|  | Navigate to Available Stock | On the Warehouse Management Monitor SAP - Warehouse Number xxx screen, choose Stock and Bin > Storage Bin > Available Stock . |  |  |
|  | Display Available Stock | Choose the node Available Stock by double-clicking on it. | The /SCWM/SAPLSTOCK_OVERVIEW_MON dialog box appears. |  |
|  | Enter Product | On the /SCWM/SAPLSTOCK_OVERVIEW_MON dialog box, make the following entries:Storage Type: S970 - Clarification Zone |  |  |
|  | Choose Execute | On the /SCWM/SAPLSTOCK_OVERVIEW_MON dialog box, choose Execute. | The Available Stock is displayed. |  |
|  | Choose Stock | Choose the stock for which you want to create a warehouse task. |  |  |
|  | Choose More Methods | On the Warehouse Management Monitor SAP - Warehouse Number xxx screen, choose More Methods > Create Warehouse Task . | The Create Warehouse Task dialog box is displayed. |  |
|  | Enter Warehouse Task Data | On the Create Warehouse Task dialog box, make the following entries:Src Trgt Qty AUoM: <your quantity>Whse Proc. Type: S997 - Putaway from Clarification |  |  |
|  | Create Warehouse Task | On the Create Warehouse Task dialog box, choose Create WT. | The following system message appears:Warehouse task xxx createdWarehouse order xxx created |  |
|  | Note Down Warehouse Order Number | Note down the Warehouse Task Number for testing purposes. |  |  |
|  | Choose Continue | Choose Continue. | In the Available Stock section, stock is not displayed anymore. |  |

#### Confirm Warehouse Tasks

##### Variant 1: With Fiori App

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A Warehouse Tasks List is printed and handed over to the Warehouse Operative (EWM). He or she performs the warehouse tasks and confirms them in the system.

|  |
| --- |
| Note If the warehouse tasks involve products with the C-serial number profile (serialization in stock), use the SAP Fiori app Confirm Warehouse Tasks - Advanced (/SCWM/TO_CONF) instead. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Fiori Launchpad | Log on to the SAP Fiori launchpad as a Warehouse Clerk (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open the SAP Fiori app Process Warehouse Tasks (F4595). |  |  |
| 3 | Enter Warehouse Task Num-ber | On the Process Warehouse Tasks screen, make the following entries:Warehouse Task: <WT number noted down in the previous step>Choose Go. |  |  |
| 4 | Confirm Warehouse Task | Mark the checkbox for the selected warehouse task and choose Confirm. | The following system message appears: Warehouse task confirmed |  |

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

For working with mobile RF devices, make sure all the steps as described in the setup instruction guide for scope item 63V - Mobile RF Devices in Warehousing are performed.

[Link to Set-Up Instructions](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/Setup/63V_Set-Up_EN_XX.pdf)

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Fiori Launchpad | Log on to the SAP Fiori launchpad as a Warehouse Operative (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open the SAP Fiori app Test RF Environment(/SCWM/RFUI)The app allows you to test working in an RF environment. For working with mobile RF devices, see also SAP Note 3048632. |  |  |
| 3 | Enter Data for RFUI | Whse No: 1750Resource: SHA1-1 or SHR1-1Dflt Dvc.: SE01Choose Enter. |  |  |
| 4 | Choose Menu | Choose 01 System-Guided > 02 SystemGuided Queue . |  |  |
| 5 | Enter Queue Name | In the Queue field, enter SI-001, SI-F01, SI-B01, or SI-G01. |  |  |
| 6 | Verify Source Bin and Enter HU | Note Note This step is only relevant if you create handling unit for a goods receipt.Verify the Src.Bin (Source Bin)HU: <Enter the HU ID from step Create Handling Unit (Optional)> |  |  |
| 7 | Verify the Source information fields | Verify the following fields, if they are required:Src.Bin (Source Bin)Prod. (Product)Srce Qty (Source Quantity)Choose Enter |  |  |
| 8 | Verify the Destination Information fields | Verify the following fields, if they are required:Prod. (Product) |  |  |
| 9 | Repeat Steps | Repeat steps 6 to 8 until no suitable warehouse orders are found. |  | All the putaway warehouse tasks have been confirmed. |
| 10 | Logoff RFUI | You can choose Back to go to the previous screens.Choose Logoff.Choose Save.Note Note If you have the two availability groups setup for your warehouse, as described in the Business Condition for 2TX, as soon as the putaway warehouse tasks are confirmed, the system automatically posts the stock type for this stock from ‘Unrestricted Use in Putaway (F0)’ to ’Unrestricted Use in Warehouse (F)’. |  |  |

## Appendix

### Attachment Handling

File attachments enable all kinds of media files being connected to business documents as additional information. For example, photos, videos, or documentation in form of plain text documents.

In the following you find some use cases of the attachment service in the Cloud WM:

- Inbound Process - Documentation of Non-Acceptance of Delivery and Proof of SLA Violation
- Outbound Process - Visual Documentation of Complete and Error-free Packaging with photos or videos
- Outbound Process - Visual Documentation of Loading Security, Compliance to Regulations, SLAs with photos or videos

Attachment Service is an optional support feature for Cloud WM business objects. Attachments can be handled anytime after the creation of an Cloud WM business object and anytime before the end of the document’s lifecycle. The attached objects are deleted when the document is deleted.

In this process you can use the following SAP Fiori Apps to create, read, update, or delete the attachments:

- Manage Inbound Deliveries – Warehouse (F7922) for Inbound Deliveries
- Warehouse Monitor for Inbound Deliveries respectively under nodes:
    - Inbound > Documents > Inbound Delivery

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

You may first have completed the following processes and conditions before you start with the test steps.

|  |
| --- |
| Note Note When running the following preceding processes along with the warehouse processes, make sure the material master data has been extended to your warehouse storage locations and the corresponding warehouse products have been created.Please refer to the Master Data Script BNF to create the storage location data for your material master data.Please refer to the Master Data Script 3KQ to create the corresponding warehouse products. |

| Scope Item ID | Business Condition |
| --- | --- |
| Inbound from Supplier |  |
| 2TX - Direct Procurement with Inbound Delivery | A purchase order was created as part of process 2TX - Direct Procurement with Inbound Delivery. At step Create Purchase Order Manually, follow the Option B: Create Purchase Order with Inbound Delivery. At step Create Inbound Deliveries, follow the Option A: Create Inbound Delivery. In both steps, use a warehouse-managed storage location, for example, Storage Location 335W (Stock in Warehouse) in the single storage location / availability group setup, or the storage location 335I (Stock in Putaway) in the two storage locations / availability groups setup. Also use the materials in the chapter Master Data, Organizational Data, and Other Data.Afterwards, an inbound delivery is created as part of process 2TX - Direct Procurement with Inbound Delivery.Note An additional storage location 335W and the corresponding availability group 002 can be introduced in the Cloud WM as an optional setup. Compared to the single storage location 335W / availability group 001 setup, the new setup can help distinguish stock that is still in the process of putaway and that is already in the warehouse.For example, the storage location 335I is used when creating a purchase order or an inbound delivery. During the inbound process, the stock remains in the storage location 335I and isn't available for sale (Stock Type F0 – Unrestricted Use in Putaway) until the putaway warehouse task(s) is/are confirmed. Once the putaway is finished, the stock is automatically posted to the storage location 335W and becomes available for sale (Stock Type F – Unrestricted Use in Warehouse).To enable the 335I storage location / availability setup, there are manual setup steps to be performed according to the instructions provided in the Warehouse Management Setup Guide. For more information, see chapter Additional Manual Configuration. |
| Inbound from Customer Returns |  |
| BKP - Customer Returns | Goods were sold as part of process BD9 - Customer Returns, which can be used for further processing in the BKP- Customer Returns process.In the BKP- Customer Returns process, for both Scenario 1: Goods are Returned to Seller and Scenario 3: Goods are Returned to Supplier via Seller, when you create a return order, you specify the follow-up activity 0001 - Receive into Plant. The corresponding return delivery is created along with the return order. The return delivery number can be found in the process flow of the return order. You then receive the return products into warehouse with reference to the steps as described in this test script.Once you finish the goods receipt and confirm the putaway warehouse task, you continue with the step Perform Material Inspection as described in BKP - Customer Returns. |
| BMK - Return to Supplier | In the BKP- Customer Returns process, if you (the seller) have decided to ship the material back to supplier and the supplier sends a replacement material, you execute the following chapters mentioned in the test script BMK - Return to Supplier:Receive Replacement Material (Optional)An inbound delivery delivery for replacement product was created. You then receive the replacement products into warehouse with rerefence to the steps as described in this test script. |
| BDD - Lean Customer Returns | In the BDD- Lean Customer Returns process, you have created a return order with storage location 335W, you execute the following chapters mentioned in the test script BDD - Lean Customer ReturnsCreate Returns DeliveryAn inbound delivery for return products is created. You then receive the return products into warehouse with reference to the steps as described in this test script.Once you finish the goods receipt and confirm the putaway warehouse task, you continue with the step Remove Billing Block as described in BDD – Lean Customer Returns.Note:The returned stock is received as unrestricted used stock in warehouse which is available for MRP and ATP immediately. If you want the returned stock to be excluded from MRP and ATP, you can configure a new return storage location, for example,ZZ5R. |
| BDW - Returnables Processing | In the BDW - Returnables Processing process, you have created a return order with storage location 335W, you execute the following chapters mentioned in the test script BDW - Returnables ProcessingCreate Pallets Return Sales OrderAn inbound delivery for return products is created automatically. You then receive the return products into warehouse with reference to the steps as described in this test script.Once you finish the goods receipt and confirm the putaway warehouse task, you continue with the step Display Pallets Stock as described in BDW - Returnables Processing. |
| 1IU - Customer Consignment | In the 1IU - Customer Consignment process, you have created a Consignment Pick-Up order with storage location 335W, you execute the following chapters mentioned in the test script 1IU - Customer ConsignmentCreate Returns DeliveryAn inbound delivery for return products is created. You then receive the return products into warehouse with reference to the steps as described in this test script.Note:The returned stock is received as unrestricted used stock in warehouse which is available for MRP and ATP immediately. If you want the returned stock to be excluded from MRP and ATP, you can configure a new return storage location, for example,ZZ5R. |
| 3XK – In-House Repair | In the 3XK – In-House Repair, you create a return order before the in-house repair. You execute the following chapters mentioned in the test script 3XK – In-House Repair with storage location 335W:Create Customer Returns OrderA return delivery from customer is created. You then receive the returned product into warehouse with rerefence to the steps as described in this test script. |
| 5CX – Customer Returns for Sales Kits | In the 5CX – Customer Returns for Sales Kits process, you create a return order to return individual products that are bundled into sales kits. You execute the following chapters mentioned in the test script 5CX – Customer Returns for Sales Kits with storage location 335W:Create Returns OrderA return delivery is created. You then receive the returned product into warehouse with rerefence to the steps as described in this test script. |
| Inbound from Other Storage Location |  |
| BMC - Core Inventory Management | A one-step stock transfer was executed as part of process BMC- Core Inventory Management. Select the warehouse-managed storage location, for example Storage Location 335W that you want to transfer to. |
| Inbound from other Plant (Intracompany and Inter-Company) |  |
| BME - Stock Transfer with Delivery | A stock transport order was created as part of process BME - Stock Transfer with Delivery, using a WM-managed storage location (e.g. Storage Location 105W and the materials in the chapter Master Data, Organizational Data, and Other Data.Afterwards, a replenishment delivery for STO was created.In addition, the step Pick and Post Goods Issue for Stock Transfer Order was executed as described in process BME - Stock Transfer with Delivery. This step triggers the creation of an inbound delivery in the receiving plant. |
| 2TS - Intercompany Stock Transfer Returns | In the 2TS – Intercompany Stock Transfer Returns, you have created a return stock transfer order with storage location 335Wyou execute the following chapters mentioned in the test script 2TS – Intercompany Stock Transfer ReturnsPerform Picking and Post Goods Issue for Outbound DeliveryAn inbound delivery for return products is created. You then receive the return products into the warehouse with reference to the steps as described in this test script. |
| 5WI - Intra-Company Returns Stock Transfers | In the 5WI – Intra-Company Returns Stock Transfers, you have created a return stock transfer order with storage location 335W, you execute the following chapters mentioned in the test script 5WI – Intra-Company Returns Stock TransfersPerform Picking and Post Goods Issue for Outbound DeliveryAn inbound delivery for return products is created. You then receive the return products into the warehouse with reference to the steps as described in this test script. |

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| Direct Procurement with Inbound Delivery (2TX) | After completing the steps of this scope item, a Supplier Invoice can be created as part of process 2TX – Direct Procurement with Inbound Delivery. |
| Customer Returns (BKP) | Once you finish the goods receipt and confirm the putaway warehouse task, you continue with the step Perform Material Inspection as described in BKP - Customer Returns. |
| Return to Supplier (BMK) | In the BKP- Customer Returns process, if you (the seller) have decided to ship the material back to supplier and the supplier sends a replacement material, you execute the following chapters mentioned in the test script BMK -Return to Supplier:Receive Replacement Material (Optional)An inbound delivery delivery for replacement product was created. You then receive the replacement products into warehouse with rerefence to the steps as described in this test script. |
| Lean Customer Returns (BDD) | Once you finish the goods receipt and confirm the putaway warehouse task, you continue with the step Remove Billing Block as described in BDD – Lean Customer Returns. |
| Returnables Processing (BDW) | Once you finish the goods receipt and confirm the putaway warehouse task, you continue with the step Display Pallets Stock as described in BDW – Returnables Processing. |
| Customer Consignment (1IU) | Once you finish the goods receipt and confirm the putaway warehouse task, you continue with the step Check Stock Overview as described in 1IU – Customer Consignment. |
| 3XK – In-House Repair | Once you finish the goods receipt and confirm the putaway warehouse task, you continue with the step Perform Material Inspection as described in 3XK – In-House Repair. |
| 5CX – Customer Returns for Sales Kits | Once you finish the goods receipt and confirm the putaway warehouse task, you continue with the step Perform Material Inspection as described in 5CX – Customer Returns for Sales Kits. |
| Core Inventory Management (BMC) (Optional) | You should be able to view the Stock Overview and the Material Documents after the stock movement. |
| Intercompany Stock Transfer Returns (2TS) | Once you finish the goods receipt and confirm the putaway warehouse task, you continue with the step Perform Material Inspection as described in 2TS - Intercompany Stock Transfer Returns. |
| Intra-Company Returns Stock Transfers (5WI) | Once you finish the goods receipt and confirm the putaway warehouse task, you continue with the step Perform Material Inspection as described in 5WI - Intra-Company Returns Stock Transfers. |

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
> Flagged while digesting this document, not verified: RF test steps log on with Whse No 1750, while the master data table and default-value steps use warehouse 3350 (ERP warehouse 335, plant 3310).

> [!warning] Conflict
> Flagged while digesting this document, not verified: The optional two-storage-location note names 335I as the additional storage location in Business Conditions, but the same note in Preceding Processes says 'additional storage location 335W' compared to the single 335W setup.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Create Handling Unit RF 'Check Delivery Status' shows GR Posted: X although it precedes goods receipt posting, while Post Goods Receipt RF shows GR Posted: Empty before posting.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[11-inventory-warehouse-and-transportation/sap-ewm-integration-inbound-processing-from-supplier-2vj-ae-test-scrip]]
- related-to :: [[11-inventory-warehouse-and-transportation/test-script-sap-ewm-integration-batch-management-2vn-ae-sap-s-4hana-cl]]
- related-to :: [[11-inventory-warehouse-and-transportation/test-script-warehouse-inbound-processing-with-synchronous-goods-receip]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3BR_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 89,773 chars in the whole document
