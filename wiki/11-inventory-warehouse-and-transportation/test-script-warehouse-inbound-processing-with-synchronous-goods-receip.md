---
id: 11-inventory-warehouse-and-transportation/test-script-warehouse-inbound-processing-with-synchronous-goods-receip
title: "Test Script: Warehouse Inbound Processing with Synchronous Goods Receipt (5HN_AE) (5HN_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script (5HN, AE) for synchronous warehouse goods receipt, putaway warehouse tasks and clarification zone handling."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/ewm-inbound-processing]
aliases: [5HN_S4CLD2608_BPD_EN_AE]
keywords: [Warehouse Inbound Processing and SAP EWM Inbound Integration, synchronous goods receipt, goods receipt posting, stock transfer, putaway warehouse tasks, warehouse task confirmation, clarification zone, packing instructions, handling units, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5HN_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1098
topic: 11-inventory-warehouse-and-transportation/ewm-inbound-processing
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Warehouse Inbound Processing with Synchronous Goods Receipt (5HN_AE) (5HN_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5HN_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Warehouse Inbound Processing and SAP EWM Inbound Integration** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Warehouse Inbound Processing with Synchronous Goods Receipt (5HN_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232857117)

[2 Prerequisites 4](#_Toc232857118)

[2.1 System Access 4](#_Toc232857119)

[2.2 Roles 4](#_Toc232857120)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232857121)

[2.4 Business Conditions 6](#_Toc232857122)

[2.5 Preliminary Steps 7](#_Toc232857123)

[2.5.1 Define Default Values for Warehouse Clerk (EWM) 7](#_Toc232857124)

[2.5.2 Define Default Values for Warehouse Operative (EWM) 7](#_Toc232857125)

[2.5.3 Maintain Warehouse Product Attributes to Automatically Create Putaway Warehouse Tasks (Optional) 8](#_Toc232857126)

[2.5.4 Manage Packing Instruction (Optional) 9](#_Toc232857127)

[2.5.4.1 Create Packing Instruction 9](#_Toc232857128)

[2.5.4.2 Create Packing Instruction Determination 10](#_Toc232857129)

[3 Overview Table 12](#_Toc232857130)

[4 Test Procedures 14](#_Toc232857131)

[4.1 Post Goods Receipt without Purchase Order 14](#_Toc232857132)

[4.2 Post Goods Receipt from Stock Transfer 16](#_Toc232857133)

[4.3 Post Goods Receipt for Purchase Orders 20](#_Toc232857134)

[4.4 Display Material Document (Optional) 22](#_Toc232857135)

[4.5 Create Product Putaway Warehouse Tasks (Optional) 23](#_Toc232857136)

[4.6 Create HU Putaway Warehouse Tasks (Optional) 24](#_Toc232857137)

[4.7 Confirm Warehouse Tasks 26](#_Toc232857138)

[4.7.1 Variant 1: With Fiori App 26](#_Toc232857139)

[4.7.2 Variant 2: With Radio Frequency Device 27](#_Toc232857140)

[4.8 Clarification Zone (Optional) 29](#_Toc232857141)

[4.8.1 Check Material in Clarification Zone 29](#_Toc232857142)

[4.8.2 Create Warehouse Tasks from Clarification Zone to Final Bin 30](#_Toc232857143)

[4.8.3 Confirm Warehouse Tasks 32](#_Toc232857144)

[4.8.3.1 Variant 1: With Fiori App 32](#_Toc232857145)

[4.8.3.2 Variant 2: With Radio Frequency Device 33](#_Toc232857146)

[5 Appendix 36](#_Toc232857147)

[5.1 Process Integration 36](#_Toc232857148)

[5.1.1 Preceding Processes 36](#_Toc232857149)

[5.1.2 Succeeding Processes 37](#_Toc232857150)

## Purpose

Overview

This scope item describes the synchronous goods receipt for the external procurement process, where the procured products can post the goods receipt directly into the warehouse without involving delivery documents. In this process, products that are delivered with the intent to be stored in the warehouse are received and moved to a storage bin. During the goods receipt process, batches and handling units can be created. The putaway warehouse task creation can be triggered automatically to execute the movements in the warehouse. After moving the products to the final bin or the clarification zone (exceptional case), the warehouse tasks are confirmed accordingly.

|  |
| --- |
| Note Since SAP S/4HANA 2208 Cloud Essentials edition, the following changes apply to this process:Synchronous goods movements are enabled on warehouse level by default for goods movements that are not related to production or external procurement. These movements are posted now directly to the warehouse. This increases the stock synchronization between Inventory Management and embedded Warehouse Management with no deliveries and warehouse requests. See more details in[Configuration of Other Direct Goods Movements Using Post Goods Movement \| SAP Help Portal](https://help.sap.com/docs/SAP_S4HANA_CLOUD/87f9b54f9c4f4e75aff0061860a6589a/3ae43fa9b0614a89bb7e3fa7dde18787.html?q=configuration%20of%20other%20direct%20goods%20movements)However, if you still want to use the deliveries for movements that are not related to production or external procurement with the Post Goods Movement App, you can deactivate the default setting on warehouse level with SSC-UI Activate Synchronous Goods Movements in the Warehouse (ID 105672). In addition, the SSC-UI allows to activate synchronous goods movements for individual movement types. More information can be found in the help document for this SSC-UI. |

After moving the products to the final bin or the clarification zone (exceptional case), the warehouse tasks are confirmed accordingly.

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
| Material | TG21 | Trad.Good 21,Reorder Point,Batch-FIFO | Batch material, for Bulk Storage |
| Packaging Material | PMPALLET | Pallet |  |
| Packaging Material | PMPALLET_GTL | Pallet for GTL |  |
| Company Code | 3310 | Company Code 3310 |  |
| Purchase Organization | 3310 | Purchase Organization 3310 |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 335W | Storage Location for Cloud WM |  |
| ERP Warehouse | 335 | Warehouse |  |
| Warehouse | 3350 | Warehouse |  |
| Division | 00 | Product Division 00 |  |
| Distribution Channel | 10 | Direct Sales |  |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| All Scope Items |  |
| BNZ - Create New Open MM Posting Period - MDS | A new posting period was created as part of process BNZ- Create New Open MM Posting Period - MDS (Master Data Script).The posting period is up-to-date. |
| Synchronous (Direct) Goods Receipt for External Procurement |  |
| J45 - Procurement of Direct Materials | A purchase order was created as part of process J45 - Procurement of Direct Materials. At step Create Purchase Order, use a warehouse-managed storage location (for example, Storage Location 335W) and the material TG11 or TG21.Note An additional storage location 335I and the corresponding availability group 002 can be introduced in the Cloud WM as an optional setup. Compared to the single storage location 335W / availability group 001 setup, the new setup can help distinguish stock that is still in the process of putaway and that is already in the warehouse.For example, the storage location 335I is used as the goods receipt storage location. During the goods receipt process, the stock remains in the storage location 335I and isn't available for sale (Stock Type F0 – Unrestricted Use in Putaway) until the putaway warehouse task(s) is/are confirmed. Once the putaway is finished, the stock is automatically posted to the storage location 335W and becomes available for sale (Stock Type F – Unrestricted Use in Warehouse).To enable the 335I storage location / availability setup, there are manual setup steps to be performed according to the instructions provided in the Warehouse Management Setup Guide. For more information, see chapter Additional Manual Configuration. |
|  |  |

### Preliminary Steps

#### Define Default Values for Warehouse Clerk (EWM)

Use

In this step, you define the default warehouse number for Warehouse Clerk (EWM).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log onto SAP Fiori Launchpad | Open the Fiori Launch Pad as Warehouse Clerk (EWM) |  |  |
| 3. | Choose the User Icon | Choose Icon for the logon user.Choose Settings. |  |  |
| 4. | Enter Default Value | Choose Default Parameters.And make the following entry in the section Material Management:Warehouse No.: 3350.Choose Save. |  |  |

#### Define Default Values for Warehouse Operative (EWM)

Use

In this step, you define the default warehouse number for Warehouse Operative (EWM).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log onto SAP Fiori Launchpad | Open the Fiori Launch Pad as Warehouse Operative (EWM) |  |  |
| 2. | Choose the User Icon | Choose Icon for the logon user.Choose Settings. |  |  |
| 3. | Enter Default Value | Choose Default Values.And make the following entry in the section Material Management:Warehouse No.: 3350Choose Save. |  |  |

#### Maintain Warehouse Product Attributes to Automatically Create Putaway Warehouse Tasks (Optional)

Purpose

In this section, you maintain the warehouse product attributes using the Warehouse Monitor (/SCWM/MON) app. By assigning the process type determination indicator to a particular product, the system creates the putaway warehouse tasks automatically upon the goods receipt posting using MIGO.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk (EWM). |  |  |
| 2 | Access App | Open Warehouse Monitor (/SCWM/MON). | The Warehouse Management Monitor SAP - Warehouse Number XX50 screen is displayed. |  |
| 3 | Navigate to Warehouse Attribute | In the hierarchy in the left screen area, choose Product Master Data > Warehouse Attribute. |  |  |
| 4 | Enter Product Number | In the /SCWM/SAPLPROD_OVERVIEW dialog box, make the following entries:Basic Attributes section:Product Number: TG11 or TG21Choose Execute. |  |  |
| 5 | Select Product | On the Warehouse Management Monitor SAP - Warehouse Number screen, in the Warehouse Attributes area, selectproduct. |  |  |
| 6 | Choose Mass Change/Create | Choose More Methods > Mass Change/Create. |  |  |
| 7 | Make entries for Process Type Determination Indicator | In the /SCWM/SAPLPROD_OVERVIEW dialog box, make the following entries:In the Warehouse Data section:Proc.Type Det. Ind: S1 |  |  |
| 8 | Choose Execute | Choose Execute. |  |  |
| 9 | Confirm your changes | In the Warehouse Management Monitor SAP - Warehouse Number dialog box, choose Yes. | The following system message appears: 1 products save successfully. |  |

#### Manage Packing Instruction (Optional)

##### Create Packing Instruction

Purpose

In this step, you create a packing instruction.

A packing instruction serves as a template for the creation of a handling unit. With the packing instruction, you define the material(s) and packaging materials to be packed in a handling unit and the packaging material that creates the handling unit.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Handling Unit Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Master Data Specialist - Handling Unit Data Create Packing Instruction - Master Data (POP1). | The Create Packing Instruction: Initial screen displays. |  |
| 3 | Create Packing Instruction | To create a new packing instruction, choose Continue or Enter.If you want to create a packing instruction from the reference packing instruction, choose a reference packing instruction and then Enter. |  |  |
| 4 | Maintain the description of Packing Instruction | Enter the short text field for the description of the packing instruction. |  |  |
| 5 | Enter Packaging Material | Enter the packaging material number in field Component of item 10.Note The Item category P of item 10 means packaging materials. The first line is mandatory for every packing instruction because every packing instruction needs at least one packaging material. |  |  |
| 6 | Maintain Material and Target Quantity | In item 20, make the following entries:Item category: M MaterialComponent: Material number to be packed, for example, TG11 or TG21Target quantity: Quantity |  |  |
| 7 | Enter Check Profile | On the Admin.data tab, enter 01 in the Check Profile field.01 is the pre-delivered SAP Standard Profile. |  |  |
| 8 | Save | Choose Save.Make a note of the packing instruction number: _____. | A packing instruction is created. |  |

##### Create Packing Instruction Determination

Purpose

In this step, you create packing instruction determination records.

This function enables the system to find a packing instruction by specific characteristics. The condition technique is applied for this. You define a packing instruction that refers to specific characteristics, such as material and ship-to-party.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Handling Unit Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Determination Records - Master Data (POF1). | The Create Determination Recs for Pkg Instruction: Initial Screen displays. |  |
| 3 | Enter Determination Type | On the Create Determination Recs for Pkg Instruction: Init. Screen, make the following entry:Determination Type:0GRV – MIGO Vendor ReceiptChoose Enter.Note Note that for the determination of the packing instruction with determination types 0GRV only the following fields can be used:SupplierPlantMaterial |  |  |
| 4 | Choose a Key Combination | On the Key Combination screen, choose a key combination and select Choose.For example, choose Material/Vendor. |  |  |
| 5 | Enter the Packing Instruction Determination | On the Create Ship. pack. inst: Fast Entry screen, make the following entries:Material: TG11 or TG21.Supplier: 33300003.Packing instruction: <The Packing instruction number noted in the last section>. |  |  |
| 6 | Save | Choose Save. | The packing instruction determination is created. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage contains only contain the essential apps for performing the typical tasks of a business role.

You can find all other apps not included on the homepage using the search bar.

If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose Settings > App Finder.

| Process Step | Business Role | App / Transaction | Expected Results |
| --- | --- | --- | --- |
| [Post Goods Receipt without Purchase Order](#unique_15) [page ] 14 | SAP_BR_WAREHOUSE_CLERK | SAP Fiori App Post Goods Movement (MIGO) | The system displays the message:Material document 5xxxxxxxxx posted. |
| [Post Goods Receipt from Stock Transfer](#unique_16) [page ] 16 | SAP_BR_WAREHOUSE_CLERK | SAP Fiori App Post Goods Movement (MIGO) | The system displays the message:Material document 5xxxxxxxxx posted. |
| [Post Goods Receipt for Purchase Orders](#unique_17) [page ] 20 | SAP_BR_WAREHOUSE_CLERK | SAP Fiori App Post Goods Movement (MIGO) | The system displays the message:Material document 5xxxxxxxxx posted. |
| [Display Material Document (Optional)](#unique_18) [page ] 22 | SAP_BR_WAREHOUSE_CLERK | SAP Fiori App Post Goods Movement (MIGO) | The created warehouse tasks are displayed. |
| [Create Product Putaway Warehouse Tasks (Optional)](#unique_19) [page ] 23 | SAP_BR_WAREHOUSE_CLERK_EWM | SAP Fiori App Create Product Warehouse Tasks (/SCWM/MONNAV_CR_P_WT) | The warehouse task is created. |
| [Create HU Putaway Warehouse Tasks (Optional)](#unique_20) [page ] 24 | SAP_BR_WAREHOUSE_CLERK_EWM | SAP Fiori App Create HU Warehouse Tasks (/SCWM/MONNAV_CR_HUWT) | The warehouse task is created. |
| [Confirm Warehouse Tasks](#unique_21) [page ] 26 | SAP_BR_WAREHOUSE_OPERATIVE_EWM | SAP Fiori App Process Warehouse Tasks (F4595) | The following system message appears:Warehouse task xxx is to be confirmed.Warehouse task xxx was confirmed.. |
| Clarification Zone: |  |  |  |
| [Check Material in Clarification Zone](#unique_22) [page ] 29 | SAP_BR_WAREHOUSE_CLERK_EWM | SAP Fiori App Warehouse Monitor (/SCWM/MON) | The Available Stock is displayed. |
| [Create Warehouse Tasks from Clarification Zone to Final Bin](#unique_23) [page ] 30 | SAP_BR_WAREHOUSE_CLERK_EWM | SAP Fiori App Warehouse Monitor (/SCWM/MON) | The following system message appears:Warehouse task xxx created.Warehouse order xxx created. |
| [Confirm Warehouse Tasks](#unique_24) [page ] 32 | SAP_BR_WAREHOUSE_OPERATIVE_EWM | SAP Fiori App Process Warehouse Tasks (F4595) | The following system message appears:Warehouse task xxx is to be confirmed.Warehouse task xxx was confirmed. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Post Goods Receipt without Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you post the goods receipt without reference to purchase order. You can enter batch and/or create handling units during the goods receipt posting. As synchronous goods movement in warehouse is activated, the system posts the goods movements in Inventory Management and in the warehouse at the same time, if the goods movement posting is relevant for the warehouse.

More information can be found in chapter [Purpose](#unique_1) [page ] 1.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad as the SAP_BR_WAREHOUSE_CLERK. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). |  |  |
| 3 | Enter Selection Data | Make the following entries and choose Enter:Choose Goods Receipt in field Trans./Event.Choose Other in field Reference Document.Enter movement type 501.Choose Continue, if there is dialog box for Change to Default Values. |  |  |
| 4 | Enter Material | Choose the Material tab, and make the following entries:Material: <Material Number>, for example TG11Choose Enter. |  |  |
| 5 | Enter Quantity | Choose the Quantity tab, and make the following entries:Qty in Unit of Entry: <Quantity>Unit of Entry: <Unit>Choose Enter. |  |  |
| 6 | Enter Plant and Storage location Data | Choose the Where tab and make the following entries:Plant:3310.Storage Location:335W.Choose Enter.Note An additional storage location 335I and the corresponding availability group 002 can be introduced in the Cloud WM as an optional setup. Compared to the single storage location 335W / availability group 001 setup, the new setup can help distinguish stock that is still in the process of putaway and that is already in the warehouse.For example, the storage location 335I is used as the goods receipt storage location. During the goods receipt process, the stock remains in the storage location 335I and isn't available for sale (Stock Type F0 – Unrestricted Use in Putaway) until the putaway warehouse task(s) is/are confirmed. Once the putaway is finished, the stock is automatically posted to the storage location 335W and becomes available for sale (Stock Type F – Unrestricted Use in Warehouse).To enable the 335I storage location / availability setup, there are manual setup steps to be performed according to the instructions provided in the Warehouse Management Setup Guide. For more information, see chapter Additional Manual Configuration. |  |  |
| 7 | Enter the Batch Number (Optional) | On the Batch tab, make the following entries and choose Enter.Batch: <Batch Number>.To enter the batch number, you can use one of the following options:Select an existing batch number.Enter external batch number.Choose Classification to create a new batch number (internal number assignment).Date of Manufacture: Maintain the date when necessarySLED/BBD: Maintain the date when necessary |  |  |
| 8 | Create Handling Units (Optional) | On the Warehouse Management tab, create handling units using either of the following options:Choose by Total Quantity and enter Packaging Material and No. of HUs.Choose by Quantity per HU and enter Quantity per HU and Packaging Material.Choose Adopt. |  |  |
| 9 | Enter Storage Bin | On the Warehouse Management tab, make the following entries:Storage Bin :GR-AREA.Choose Enter. |  |  |
| 10 | Select Item ok Indicator | Select the Item OK checkbox.Choose Check. Confirm the message Document is O.K. by choosing Enter. |  |  |
| 11 | Post | Choose Post. | The system displays the messages:Material document xxxxxxxxxx posted.Make a note of the Material Document number. |  |

### Post Goods Receipt from Stock Transfer

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you post the goods receipt from Stock Transfer. You can enter batch and/or create handling units during the goods receipt posting. As synchronous goods movement in warehouse is activated, the system posts the goods movements in Inventory Management and in the warehouse at the same time, if the goods movement posting is relevant for the warehouse.

More information can be found in chapter [Purpose](#unique_1) [page ] 1.

Procedure

For One Step Stock Transfer with movement type 311

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad as the SAP_BR_WAREHOUSE_CLERK. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). |  |  |
| 3 | Enter Selection Data | Make the following entries and choose Enter.Choose Transfer Posting in field Trans./EventChoose Other in field Reference DocumentEnter movement type 311Choose Continue if there is dialog box for Change to Default Values. |  |  |
| 4 | Enter Material | Choose Transfer Posting tab, and make the following entries:Material: <Material Number>, for example TG11Plant: 3310.Stor.Loc. in From section:331A.Stor.Loc. in Dest section: 335WChoose Enter.Note Use the 335I as the destination storage location if you have the two availability groups setup for your warehouse, as described in the Preceding Processes for BMC. |  |  |
| 5 | Enter Quantity | Choose Quantity tab, and make the following entries:Qty in Unit of Entry: <Quantity>Unit of Entry: <Unit>Choose Enter. |  |  |
| 6 | Enter the Batch Number (Optional) | On the Batch tab, make the following entries and choose Enter.Batch: <Batch Number>.To enter the batch number, you can use one of the following options:Select an existing batch numberEnter external batch numberChoose Classification to create a new batch number (internal number assignment)Date of Manufacture: Maintain the date when necessary.SLED/BBD: Maintain the date when necessary. |  |  |
| 7 | Create Handling Units (Optional) | On the Warehouse Management tab, create handling units using either of the following options:Choose by Total Quantity and enter Packaging Material and No. of HUs.Choose by Quantity per HU and enter Quantity per HU and Packaging Material.Choose Adopt. |  |  |
| 8 | Enter Storage Bin | On the Warehouse Management tab, make the following entries:Storage Bin :GR-AREA.Choose Enter. |  |  |
| 9 | Select Item ok Indicator | Select Item OK checkbox.Choose Check. Confirm the message Document is O.K. by choosing Enter. |  |  |
| 10 | Post | Choose Post. | The system displays the message:Material document xxxxxxxxxx posted.Make a note of the Material Document number. |  |

For Two Steps Stock Transfer (Place to Storage Location) with movement type 315

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad as the SAP_BR_WAREHOUSE_CLERK. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). |  |  |
| 3 | Enter Selection Data | Make the following entries and choose Enter.Choose Place in Storage in field Trans./EventChoose Material Document in field Reference DocumentEnter the material document number from two steps stock transfer.Choose Execute |  |  |
| 4 | Enter the Batch Number (Optional) | On the Batch tab, make the following entries and choose Enter.Batch: <Batch Number>.To enter the batch number, you can use one of the following options:Select an existing batch numberEnter external batch numberChoose Classification to create a new batch number (internal number assignment)Date of Manufacture: Maintain the date when necessary.SLED/BBD: Maintain the date when necessary. |  |  |
| 5 | Create Handling Units (Optional) | On the Warehouse Management tab, create handling units using either of the following options:Choose by Total Quantity and enter Packaging Material and No. of HUs.Choose by Quantity per HU and enter Quantity per HU and Packaging Material.Choose Adopt. |  |  |
| 6 | Enter Storage Bin | On the Warehouse Management tab, make the following entries:Storage Bin :GR-AREA.Choose Enter. |  |  |
| 7 | Select Item ok Indicator | Select Item OK checkbox.Choose Check. Confirm the message Document is O.K. by choosing Enter. |  |  |
| 8 | Post | Choose Post. | The system displays the message:Material document xxxxxxxxxx posted.Make a note of the Material Document number. |  |

### Post Goods Receipt for Purchase Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you post the goods receipt against the purchase order. You can enter batch and/or create handling units before the goods receipt is posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad as the Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Goods Receipt Purchase Order screen is displayed. |  |
| 3 | Select Goods Receipt Order Screen | On the Goods Receipt Purchase Order screen, make the following entries and choose Enter.Goods Receipt: <Select>.Purchasing Order: <Select>.Order number: <Purchase Order number from the previous step>.GR goods receipt: 101. | The items of the selected purchase order are displayed. |  |
| 4 | Enter Quantity | If required, check the quantity on the Quantity tab. |  |  |
| 5 | Check Storage Location | Select Where tab and check storage location 335W.Note Use the 335I as the destination storage location if you have the two availability groups setup for your warehouse, as described in the Business Condition for J45. |  |  |
| 6 | Enter the Batch Number (Optional) | On the Batch tab, make the following entries and choose Enter.Batch: <Batch Number>.To enter the batch number, you can use one of the following options:Select an existing batch number.Enter an external batch number.Choose Classification to create a new batch number (internal number assignment).Date of Manufacture: Maintain the date when necessary.SLED/BBD: Maintain the date when necessary. |  |  |
| 7 | Create Handling Units (Optional) | Iif a packing instruction is available for the product on the Warehouse Management tab, the value in the Unpacked Qnty AUoM field is 0. Then the packaging proposal contains the following values:No. of HUsPack. MaterialHU TypeQty.AUoM (Quantity per HU in Alternative UoM)UnitQuantityBUoM (Base UoM)If no packaging proposal is given, create handling units using either of the following options:Choose by Total Quantity and enter Packaging Material and No. of HUs.Choose by Quantity per HU and enter Quantity per HU and Packaging Material.Choose Adopt.Note Even if a packing instruction is available, you can delete the packaging proposal and create the handling units based on your own needs. However, once you choose Redetermine Packaging Proposal, the system reads the packing instruction and once again gives the packing proposal. |  |  |
| 8 | Check Storage Bin | On the Warehouse Management tab, check the default Storage Type: S910 and Storage Bin :GR-AREA.Note The default storage bin can be changed. |  |  |
| 9 | Select Item ok Indicator | Select Item OK checkbox.Choose Check. Confirm the message Document is O.K. by choosing Enter. |  |  |
| 10 | Post | Choose Post. | The system displays the following messages:Material document 5xxxxxxxxx posted.Make a note of the Material Document number. |  |

### Display Material Document (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you display the material document for the goods receipt in the previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad as the Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Goods Receipt Purchase Order screen is displayed. |  |
| 3 | Select Display Material Document screen | On the Goods Receipt Purchase Order screen, make the following entries and choose Enter.Display: <Select>Material Document: <Select>.Material Document number: <Material Document number from the previous step>.Material Document Year : for example 2020 | The items of the selected purchase order display. |  |
| 4 | Display Stock Overview | On the Warehouse Management tab, choose Display Stock Overview. |  |  |
|  | Check Physical Stock | On the Physical Stock screen, check the product, HUs (if applicable) and the Storage Type / Storage Bin in which the stock is located after the goods receipt. |  |  |
| 5 | Display Warehouse Document | On the Warehouse Management tab, choose either of the two following options:If automatic Putaway WT creation is applicable to the product, choose Display Warehouse Document and Open Putaway WTs.If automatic putaway WT creation is not applicable to the product, choose Display Warehouse Document.Note You see the Display Warehouse Document and Open Putaway WTs if the automatic Putaway WT creation is not applicable to the product. |  |  |
| 6 | Check Warehouse Tasks | On the Warehouse Task screen, check that the goods receipt posting Warehouse Task was created and confirmed by the system.If the automatic putaway WT creation is applicable to the product, you also see the open putaway WT(s). | The Warehouse Task(s) created is displayed.Make a note of the putaway warehouse task number. |  |

### Create Product Putaway Warehouse Tasks (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is for creating ad-hoc warehouse task to move unpacked stock (no HU) from the goods receipt area to the final putaway storage type. This step is not required if the automatic WT creation is applicable to the product that you use.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log onto SAP Fiori Launchpad | Open the Fiori Launch Pad as a Warehouse Clerk (EWM). | The Fiori Launch Pad is displayed. |  |
| 2. | Access the App | Open Fiori Create Product Warehouse Tasks (/SCWM/MONNAV_CR_P_WT). | The Create Product Warehouse Tasks (/SCWM/MONNAV_CR_P_WT) screen displays. |  |
| 3. | Decide your filter criteria | Storage Type: S910.Choose Execute. | The Create Product Warehouse Task screen displays. |  |
| 4. | Choose your Stock | Choose a stock line from the previous step andMore Methods > Create Warehouse Task. | A dialog box requests for data Create Warehouse Task is displayed. |  |
| 5. | Create Warehouse Task | Create Warehouse Task and enter the following data:Src Trgt Qty AUoM (Quantity): <The quantity of the stock line>Warehouse Process Type: S116Destination Bin: <Leave Blank>Destination Storage Type and Storage Bin are determined by the system.Choose Create WT. | A warehouse task is created which you can see in the display log. A Warehouse Task List is automatically printed in the background.You must find the open product warehouse task in monitor node Warehouse Task. Therefore, note down the Warehouse Task and Warehouse Order number. |  |
| 6. | Complete the step | Choose Continue to close the log and then choose Home or repeat the steps if required. |  |  |

### Create HU Putaway Warehouse Tasks (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is for creating ad-hoc warehouse tasks to move packed (with HU) stock from the goods receipt area to the final putaway storage type. This step is not required if the automatic WT creation is applicable to the product that you use.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log onto SAP Fiori Launchpad | Open the SAP Fiori launchpad as a Warehouse Clerk (EWM). | The SAP Fiori launchpad is displayed. |  |
| 2. | Access the App | Open Create HU Warehouse Tasks (/SCWM/MONNAV_CR_HUWT). | Create HU Warehouse Tasks (/SCWM/MONNAV_CR_HUWT) |  |
| 3. | Enter filter criteria | Make the following entries:Storage Type: S910Choose Execute. |  |  |
| 4. | Select your Stock | Select one of the HU stock lines and choose More Methods > Create Warehouse Task. | A dialog box, that requests data (Create Warehouse Task), is displayed. |  |
| 5. | Create Warehouse Task | Create the warehouse task and enter the following data:Destination Bin: <Leave Blank>The Destination Storage Type and Storage Bin are determined by the system.Warehouse Process Type: S126Choose Create WT. | You can see the created warehouse task in the display log. A Warehouse Task List is automatically printed in the background.You must find the open HU warehouse task in the monitor node Warehouse Task. Therefore, note down the Warehouse Task and Warehouse Order number. |  |
| 6. | Complete the step | Choose Continue to close the log and then choose Home. Repeat the steps, if required. |  |  |

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

A Putaway List is printed and handed over to the Warehouse Operative (EWM) who performs the warehouse tasks and confirms them in the system. Note down that you can also confirm warehouse tasks using the app Warehouse Monitor (/SCWM/MON) (Business Catalog WM – Monitoring).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Fiori launchpad | Log on to the SAP Fiori launchpad as a Warehouse Operative (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open the SAP Fiori app Process Warehouse Tasks (F4595). | The Confirm Warehouse Tasks screen appears. |  |
| 3 | Enter Warehouse Task Number | On the Process Warehouse Tasks screen, make the following entries:Choose your Warehouse Task: <Your warehouse task number>.Choose Go. |  |  |
| 4 | Confirm Warehouse Task | Mark the checkbox for the selected warehouse task and choose Confirm.Note If you have the two availability groups setup for your warehouse, as soon as the putaway warehouse tasks are confirmed, the system automatically posts the stock type for this stock from ‘Unrestricted Use in Putaway (F0)’ to ’Unrestricted Use in Warehouse (F)’. | The following system message appears: Warehouse task confirmed. |  |

#### Variant 2: With Radio Frequency Device

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
| 2 | Access the SAP Fiori app | Open the SAP Fiori app Test RF Environment (/SCWM/RFUI) |  |  |
| 3 | Enter Data for RFUI | Whse No: 3350Resource: SHA1-1 or SHR1-1 .Dflt Dvc.: SE01.Choose Enter.Note Use resource SHA1-1 for putaway to S001.Use SHR1-1 for putaway to storage types other than S001 . |  |  |
| 4 | Choose Menu | Choose 01 System-Guided > 02 SystemGuided Queue. |  |  |
| 5 | Enter Queue Name | In the Queue field, enter SI-001, SI-F01,SI-B01 or SI-G01.Note It is likely that in the system-guided selection, certain unfinished warehouse activities may appear instead of the expected task.If this is the case, choose 03 Inbound Process > 03 Putaway > 03 Putaway by WO and enter the corresponding WO number in the Whse Order field to process the task. You can also choose 03 Inbound Process > 03 Putaway > 01 Putaway by HU and enter the corresponding HU number in the HU field to process the task. |  |  |
| 6 | Verify Source Bin | Verify the Src.Bin (Source Bin). |  |  |
| 7 | Enter HU | Note Only enter the handling unit, if you create a handling unit for GR.Enter the handling unit ID from step Create Handling Unit (Optional).HU: <The HU ID from the previous step> |  |  |
| 8 | Verify the Fields | Verify for the following fields, if they are required in the current screen and in the follow-up screens：Src.Bin (Source Bin)SrceHU (Source HU)Prod. (Product)ActQty (Quantity)DstBin (Destination Bin)Choose Enter |  |  |
| 9 | Repeat Steps | Repeat steps 6 -8 until no suitable warehouse orders are found. |  |  |
| 10 | Logoff RFUI | You can choose Back and go to the previous screens.Choose Logoff.Choose Save.Note If you have the two availability groups setup for your warehouse, as soon as the putaway warehouse tasks are confirmed, the system automatically posts the stock type for this stock from ‘Unrestricted Use in Putaway (F0)’ to ’Unrestricted Use in Warehouse (F)’. |  |  |

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

The Warehouse Clerk (EWM) checks the material that is on the clarification zone. In case of missing information (for example, PACI), the Warehouse Clerk (EWM) maintains the required information and decides what to do with the material.

|  |
| --- |
| Note The following reasons lead to destination bin Clarification Zone:No putaway control indicator (PACI) maintained for the productNo fix bin assignment for products with putaway control indicator to fix bin storage typeQuality- or blocked stockNo free bin in the storage type |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on to the SAP Fiori launchpad | Log on to the SAP Fiori launchpad as a Warehouse Clerk (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2. | Access the SAP Fiori app | Open the SAP Fiori app Warehouse Monitor (/SCWM/MON). | The Warehouse Monitor (/SCWM/MON) dialog box appears. |  |
| 3. | Enter Default Values | In the Warehouse Management Monitor dialog box, make the following entries:Warehouse Number: <your warehouse number>.Monitor: SAP. |  |  |
| 4. | Choose Execute | In the Warehouse Management Monitor dialog box, choose Execute. | The Warehouse Management Monitor SAP - Warehouse Number xxx screen appears. |  |
| 5. | Navigate to Available Stock | On the Warehouse Management Monitor SAP - Warehouse Number xxx screen, choose Stock and Bin > Storage Bin > Available Stock. |  |  |
| 6. | Display Available Stock | Choose the node Available Stock by double-clicking on it. | The /SCWM/SAPLSTOCK_OVERVIEW_MON dialog box appears. |  |
| 7. | Enter Product | On the /SCWM/SAPLSTOCK_OVERVIEW_MON dialog box, make the following entries:Storage Type: S970 - Clarification Zone |  |  |
| 8. | Choose Execute | On the /SCWM/SAPLSTOCK_OVERVIEW_MON dialog box, choose Execute. | The Available Stock is displayed. |  |

#### Create Warehouse Tasks from Clarification Zone to Final Bin

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
| 1. | Log on to the SAP Fiori launchpad | Log on to the SAP Fiori launchpad as a Warehouse Clerk (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2. | Access the SAP Fiori app | Open the SAP Fiori app Warehouse Monitor (/SCWM/MON). | The Warehouse Monitor (/SCWM/MON) dialog box appears. |  |
| 3. | Enter Default Values | On the Warehouse Management Monitor dialog box, make the following entries:Warehouse Number: <your warehouse number>. |  |  |
| 4. | Choose Execute | On the Warehouse Management Monitor dialog box, choose Execute. | The Warehouse Management Monitor SAP - Warehouse Number xxx screen appears. |  |
| 5. | Navigate to Available Stock | On the Warehouse Management Monitor SAP - Warehouse Number xxx screen, choose Stock and Bin > Storage Bin > Available Stock. |  |  |
| 6. | Display Available Stock | Choose the node Available Stock by double-clicking on it. | The /SCWM/SAPLSTOCK_OVERVIEW_MON dialog box appears. |  |
| 7. | Enter Product | On the /SCWM/SAPLSTOCK_OVERVIEW_MON dialog box, make the following entries:Storage Type: S970 - Clarification Zone |  |  |
| 8. | Choose Execute | On the /SCWM/SAPLSTOCK_OVERVIEW_MON dialog box, choose Execute. | The Available Stock is displayed. |  |
| 9. | Choose Stock | Choose the stock for which you want to create a warehouse task. |  |  |
| 10. | Choose More Methods | On the Warehouse Management Monitor SAP - Warehouse Number xxx screen, choose More Methods > Create Warehouse Task. | The Create Warehouse Task dialog box is displayed. |  |
| 11. | Enter Warehouse Task Data | On the Create Warehouse Task dialog box, make the following entries:Src Trgt Qty AUoM: <your quantity>.Whse Proc. Type: S997 - Putaway from Clarification. |  |  |
| 12. | Create Warehouse Task | On the Create Warehouse Task dialog box, choose Create WT. | The following system message appears:Warehouse task xxx createdWarehouse order xxx created |  |
| 13. | Note Down Warehouse Order Number | Note down the warehouse task and warehouse order number for testing purposes. |  |  |
| 14. | Choose Continue | Choose Continue. | In the Available Stock section, stock is not displayed anymore. |  |

#### Confirm Warehouse Tasks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A Warehouse Tasks List is printed and handed over to the Warehouse Operative (EWM). He or she performs the warehouse tasks and confirms them in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log onto the SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad as a Warehouse Operative (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2. | Access the SAP Fiori app | Open the SAP Fiori app Process Warehouse Tasks (F4595). |  |  |
| 3. | Enter Warehouse Task Number | On the Process Warehouse Tasks screen, make the following entries:Warehouse Task: <WT number noted down in the previous step>Choose Go. |  |  |
| 6. | Confirm Warehouse Task | Mark the check box for the selected warehouse task and choose Confirm | The following system message appears:Warehouse task confirmed |  |

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

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto the SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad as a Warehouse Operative (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open the SAP Fiori app Process Warehouse Tasks (F4595). |  |  |
| 3 | Enter Warehouse Task Number | On the Process Warehouse Tasks screen, make the following entries:Warehouse Task: <WT number noted down in the previous step>Choose Go. |  |  |
| 4 | Confirm Warehouse Task | Mark the check box for the selected warehouse task and choose Confirm.Note If you have the two availability groups setup for your warehouse, as soon as the putaway warehouse tasks are confirmed, the system automatically posts the stock type for this stock from ‘Unrestricted Use in Putaway (F0)’ to ’Unrestricted Use in Warehouse (F)’. | The following system message appears: Warehouse task confirmed |  |

##### Variant 2: With Radio Frequency Device

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
| 2 | Access the SAP Fiori app | Open the SAP Fiori app Test RF Environment (/SCWM/RFUI). |  |  |
| 3 | Enter Data for RFUI | Whse No: 3350Resource: SHA1-1 or SHR1-1DefPresDvc: SE01Choose Enter.Note Use resource SHA1-1 for putaway to S001.Use SHR1-1 for putaway to storage types other than S001 . |  |  |
| 4 | Choose Menu | Choose 01 System-Guided > 02 SystemGuided Queue. |  |  |
| 5 | Enter Queue Name | In the Queue field, enter SI-001, SI-F01,SI-B01 or SI-G01.Note It is likely that in the System-Guided Selection, certain unfinished warehouse activities may appear instead of the expected task.If this is the case, choose 03 Inbound Process > 03 Putaway > 03 Putaway by WO and enter the corresponding WO number in the Whse Order field to process the task. You can also choose 03 Inbound Process > 03 Putaway > 01 Putaway by HU and enter the corresponding HU number in the HU field to process the task. |  |  |
| 6 | Verify Source Bin | Verify the Src.Bin (Source Bin). |  |  |
| 7 | Enter HU | Note Only enter he HU, if you create a handling unit for GR.Enter the HU ID from step Create Handling Unit (Optional).HU: <The HU ID from the previous step> |  |  |
| 8 | Verify the fields | Verify the following fields, if they are required in the current screen and in the follow-up screens：Src.Bin (Source Bin)SrceHU (Source HU)Prod. (Product)ActQty (Quantity)DstBin (Destination Bin)Choose Enter |  |  |
| 9 | Repeat Steps | Repeat steps 6 to 8 until no suitable warehouse orders are found. |  |  |
| 10 | Logoff RFUI | You can choose Back to go to the previous screens.Choose Logoff.Choose Save.Note If you have the two availability groups setup for your warehouse, as soon as the putaway warehouse tasks are confirmed, the system automatically posts the stock type for this stock from ‘Unrestricted Use in Putaway (F0)’ to ’Unrestricted Use in Warehouse (F)’. |  |  |

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
| J45 - Procurement of Direct Materials | After completing the steps of this scope item, a Supplier Invoice can be created as part of process J45-Procurement of Direct Materials. |
| Synchronous Goods Receipt from other Storage Location |  |
| BMC - Core Inventory Management | At step One Step Stock Transfer, switch to use the data and app as described in chapter Post Goods Receipt from Stock Transfer in this test script.At step Two Steps Stock Transfer (Place to Storage Location), switch to use the data and app as described in chapter Post Goods Receipt from Stock Transfer in this test script.Note An additional storage location 335I and the corresponding availability group 002 can be introduced in the Cloud WM as an optional setup. Compared to the single storage location 335W / availability group 001 setup, the new setup can help distinguish stock that is still in the process of putaway and that is already in the warehouse.For example, the storage location 335I is used as the goods receipt storage location. During the goods receipt process, the stock remains in the storage location 335I and isn't available for sale (Stock Type F0 – Unrestricted Use in Putaway) until the putaway warehouse task(s) is/are confirmed. Once the putaway is finished, the stock is automatically posted to the storage location 335W and becomes available for sale (Stock Type F – Unrestricted Use in Warehouse).To enable the 335I storage location / availability setup, there are manual setup steps to be performed according to the instructions provided in the Warehouse Management Setup Guide. For more information, see chapter Additional Manual Configuration. |
| Synchronous Goods Receipt from Other Plant |  |
| BMH - Stock Transfer Without Delivery | A stock transfer order was created as part of process BMH - Stock Transfer Without Delivery. At step Optional: Create Stock Transfer Order (Without MRP), use a warehouse-managed storage location (for example, Storage Location 335W) and the material TG11 or TG21.At step Post Goods Receipt for Stock Transport Order, if you want to see or change the warehouse data, for example, storage bin, you can switch to use the data and app as described in chapter Post Goods Receipt from Purchase Order in this test script. Otherwise you can follow the step as described in BMH test script.Note An additional storage location 335I and the corresponding availability group 002 can be introduced in the Cloud WM as an optional setup. Compared to the single storage location 335W / availability group 001 setup, the new setup can help distinguish stock that is still in the process of putaway and that is already in the warehouse.For example, the storage location 335I is used as the goods receipt storage location. During the goods receipt process, the stock remains in the storage location 335I and isn't available for sale (Stock Type F0 – Unrestricted Use in Putaway) until the putaway warehouse task(s) is/are confirmed. Once the putaway is finished, the stock is automatically posted to the storage location 335W and becomes available for sale (Stock Type F – Unrestricted Use in Warehouse).To enable the 335I storage location / availability setup, there are manual setup steps to be performed according to the instructions provided in the Warehouse Management Setup Guide. For more information, see chapter Additional Manual Configuration. |

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| Procurement of Direct Materials (J45) | After completing the steps of this scope item, a Supplier Invoice can be created as part of process J45-Procurement of Direct Materials. |

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
- related-to :: [[11-inventory-warehouse-and-transportation/sap-ewm-integration-inbound-processing-from-supplier-2vj-ae-test-scrip]]
- related-to :: [[11-inventory-warehouse-and-transportation/test-script-sap-ewm-integration-batch-management-2vn-ae-sap-s-4hana-cl]]
- related-to :: [[11-inventory-warehouse-and-transportation/test-script-warehouse-inbound-processing-3br-ae-sap-s-4hana-cloud-publ]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5HN_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 61,145 chars in the whole document
