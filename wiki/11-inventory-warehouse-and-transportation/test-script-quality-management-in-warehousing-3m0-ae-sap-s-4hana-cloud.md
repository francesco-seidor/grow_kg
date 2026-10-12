---
id: 11-inventory-warehouse-and-transportation/test-script-quality-management-in-warehousing-3m0-ae-sap-s-4hana-cloud
title: "Test Script: Quality Management in Warehousing (3M0_AE) - SAP S/4HANA Cloud Public Edition (3M0_S4CLD2608_BPD_EN_AE)"
description: "SAP test script for scope item 3M0_AE: inspecting goods from production and suppliers in the warehouse (inspection lot, usage decision, putaway), Fiori and RF."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/ewm-internal-inspections]
aliases: [3M0_S4CLD2608_BPD_EN_AE]
keywords: [Warehouse Internal Inspections, quality management in warehousing, inspection lot, usage decision, inspection results, goods receipt, synchronous goods receipt, handling units, warehouse tasks, radio frequency devices]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3M0_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-957
topic: 11-inventory-warehouse-and-transportation/ewm-internal-inspections
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Quality Management in Warehousing (3M0_AE) - SAP S/4HANA Cloud Public Edition (3M0_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3M0_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Warehouse Internal Inspections** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Quality Management in Warehousing (3M0_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232853218)

[2 Prerequisites 4](#_Toc232853219)

[2.1 System Access 4](#_Toc232853220)

[2.2 Roles 4](#_Toc232853221)

[2.3 Additional Manual Configuration 5](#_Toc232853222)

[2.4 Master Data, Organizational Data, and Other Data 5](#_Toc232853223)

[2.5 Business Conditions 6](#_Toc232853224)

[3 Overview Table 8](#_Toc232853225)

[3.1 Quality Management in Warehouse (from Production) 8](#_Toc232853226)

[3.2 Quality Management in Warehouse (from Supplier) 9](#_Toc232853227)

[4 Test Procedures 11](#_Toc232853228)

[4.1 Quality Management in Warehouse (from Production) 11](#_Toc232853229)

[4.1.1 Create Handling Unit (Optional) 11](#_Toc232853230)

[4.1.1.1 Variant 1: With Fiori App – Automatic Packing 12](#_Toc232853231)

[4.1.1.2 Variant 2: With Fiori App – Packing at Workcenter 14](#_Toc232853232)

[4.1.1.3 Variant 3: With Radio Frequency Device 16](#_Toc232853233)

[4.1.2 Post Goods Receipt 19](#_Toc232853234)

[4.1.2.1 Option 1: Post Good Receipt for Inbound Delivery from Production 19](#_Toc232853235)

[4.1.2.1.1 Variant 1: With Fiori App 19](#_Toc232853236)

[4.1.2.1.2 Variant 2: With Radio Frequency Device 20](#_Toc232853237)

[4.1.2.2 Option 2: Post Synchronous Goods Receipt for Production Order 22](#_Toc232853238)

[4.1.3 Create Warehouse Tasks 25](#_Toc232853239)

[4.1.4 Confirm Warehouse Tasks 26](#_Toc232853240)

[4.1.4.1 Variant 1: With Fiori App 26](#_Toc232853241)

[4.1.4.2 Variant 2: With Radio Frequency Device 27](#_Toc232853242)

[4.1.5 Record Inspection Results 28](#_Toc232853243)

[4.1.6 Make Usage Decision 29](#_Toc232853244)

[4.1.7 Repack Handling Units (Optional) 30](#_Toc232853245)

[4.1.8 Create Ad Hoc Warehouse Task (Optional) 31](#_Toc232853246)

[4.1.9 Confirm Warehouse Tasks 32](#_Toc232853247)

[4.1.9.1 Variant 1: With Fiori App 32](#_Toc232853248)

[4.1.9.2 Variant 2: With Radio Frequency Device 33](#_Toc232853249)

[4.2 Quality Management in Warehouse (from Supplier) 33](#_Toc232853250)

[4.2.1 Capture Serial Number (Optional) 33](#_Toc232853251)

[4.2.2 Create Handling Unit (Optional) 34](#_Toc232853252)

[4.2.2.1 Variant 1: With Fiori App – Automatic Packing 35](#_Toc232853253)

[4.2.2.2 Variant 2: With Fiori App – Packing at Work Center 36](#_Toc232853254)

[4.2.2.3 Variant 3: With Radio Frequency Devices 39](#_Toc232853255)

[4.2.3 Post Goods Receipt 41](#_Toc232853256)

[4.2.3.1 Option 1: Post Good Receipt for Inbound Delivery from Procurement 42](#_Toc232853257)

[4.2.3.1.1 Variant 1: With Fiori App 42](#_Toc232853258)

[4.2.3.1.2 Variant 2: With Radio Frequency Devices 43](#_Toc232853259)

[4.2.3.2 Option 2: Post Synchronous Goods Receipt for Purchase Order 45](#_Toc232853260)

[4.2.4 Create Warehouse Tasks 48](#_Toc232853261)

[4.2.5 Confirm Warehouse Tasks 49](#_Toc232853262)

[4.2.5.1 Variant 1: With Fiori App 49](#_Toc232853263)

[4.2.5.2 Variant 2: With Radio Frequency Device 49](#_Toc232853264)

[4.2.6 Record Inspection Results 50](#_Toc232853265)

[4.2.7 Make Usage Decision 51](#_Toc232853266)

[4.2.8 Repack Handling Units (Optional) 53](#_Toc232853267)

[4.2.9 Create Ad Hoc Warehouse Task (Optional) 54](#_Toc232853268)

[4.2.10 Confirm Warehouse Tasks 55](#_Toc232853269)

[4.2.10.1 Variant 1: With Fiori App 55](#_Toc232853270)

[4.2.10.2 Variant 2: With Radio Frequency Device 56](#_Toc232853271)

[5 Appendix 57](#_Toc232853272)

[5.1 Process Integration 57](#_Toc232853273)

[5.1.1 Preceding Processes 57](#_Toc232853274)

[5.1.2 Succeeding Processes 57](#_Toc232853275)

[6 Attachment Handling 59](#_Toc232853276)

## Purpose

Overview

This scope item allows you to inspect products delivered from external suppliers and from production before putaway in the warehouse. The process starts with the creation of a purchase or production order and an inbound delivery relevant for processing in the warehouse. Once the goods arrive at the warehouse, the delivery is checked, and the products are packed into handling units as required. Afterwards, the goods receipt is posted and warehouse tasks are created to execute the movements to the quality area. At goods receipt posting, the system creates an inspection lot and changes the stock type to quality stock. A quality technician inspects the delivered goods and records the inspection results. Based on these results, the quality engineer makes a usage decision. At the end of the process, you create ad-hoc warehouse tasks to move the accepted products to a final storage bin. The rejected products stay in the quality area for further processing.

|  |
| --- |
| Note Since SAP S/4HANA 2111 Cloud Essentials edition, the following changes apply to this process:Upon the goods receipt from Production or Purchase Order, an Inspection Lot is created. The product is moved to the Quality Area / Quality Work Center for inspection instead of the Clarification Area.Automatic putaway Warehouse Task creation is enabled for Usage Decision with an acceptance usage code.Existing customers do NOT get the changes by upgrade and the process works as it did before. For more information, see chapter 2.3 [Additional Manual Configuration](#unique_2) [page ] 5 |

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data, and business conditions.

### System Access

|  |  |
| --- | --- |
|  | Details |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | Description | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- | --- |
| Warehouse Clerk (EWM) | Warehouse Clerk (EWM) | SAP_BR_WAREHOUSE_CLERK_EWM | Warehouse Office | SAP_BR_WAREHOUSE_CLERK_EWM |  |
| Warehouse Operative (EWM) | Warehouse Operative (EWM) | SAP_BR_WAREHOUSE_OPERATIVE_EWM | Warehouse Floor | SAP_BR_WAREHOUSE_OPERATIVE_EWM |  |
| Warehouse Clerk | Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Quality Technician | Quality Technician | SAP_BR_QUALITY_TECHNICIAN | Quality Inspection | SAP_BR_QUALITY_TECHNICIAN |  |
| Quality Engineer | Quality Engineer | SAP_BR_QUALITY_ENGINEER | Quality Engineering | SAP_BR_QUALITY_ENGINEER |  |

### Additional Manual Configuration

Before you start the testing, make sure that the steps in the [Warehouse Management Setup Guide.docx (Public)](https://support.sap.com/content/dam/SAAP/SAP_Activate/S4H_588%20Warehouse%20Management%20Setup.docx) published on the SAP Activate Roadmap Viewer are completed.

If you are working with a radio frequency device, carry out the steps described in Mobile RF Devices in Warehousing (63V).

|  |
| --- |
| Caution Since SAP S/4HANA Cloud Public Edition 2111, the following changes apply to this process:A Quality Area / Quality Work Center is available for processing Inspection Lots.Automatic putaway Warehouse Task creation is enabled for Usage Decision with an acceptance usage code.Customers who implement this Scope Item as of SAP S/4HANA Cloud Public Edition 2111 will be able to run the process with the changes mentioned above. However, customers who implemented this Scope Item prior to SAP S/4HANA Cloud Public Edition 2111 do not get the changes by upgrade and the process works as it was before. If you want to also apply the changes to the process, implement the following steps from the Warehouse Management Setup Guide:Specify Storage Type Search Sequence for PutawayMaintain Follow-Up ActionsCreate Storage Bin for Quality Area |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | QM001 | QM Regular | QM in Warehouse (from Supplier) |
| Material | SG29 | SEM29, PD, QM | QM in Warehouse (from Production) |
| Packaging Material | PMPALLET | Pallet |  |
| Packaging Material | PMPALLET_GTL | Pallet for GTL |  |
| Company Code | 3310 | Company Code 3310 |  |
| Purchase Organization | 3310 | Purchase Organization 3310 |  |
| Plant | 3310 |  |  |
| Storage Location | 335W |  |  |
| ERP Warehouse | 335 | Warehouse |  |
| EWM Warehouse | 3350 | Warehouse |  |
| Division | 00 |  |  |
| Distribution Channel | 10 |  |  |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

| MDS | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 1E1 - Quality Management in Discrete and Process Manufacturing | For Quality Management in Warehouse (from Production)Follow the instructions for the production order creation and release as described in Scope Item Quality Management in Discrete and Process Manufacturing in chapter Make-to-Order Production - Semi finished Goods Planning and Assembly (1BM) . Use the material SG29. Note that you need to use a warehouse-managed storage location for the goods receipt, for example 335W. |
| 3DV - Warehouse Production Integration | For Quality Management in Warehouse (from Production)Follow the instructions for the inbound delivery for the production order creation as described in Scope Item Warehouse Production Integration in chapter Create Inbound Delivery for Production Order.You can skip this step if you are to post synchronous goods receipt for production orders. |
| 1FM - Quality Management in Procurement | For Quality Management in Warehouse (from Supplier)Follow the instructions for the purchase order creation as described in Scope Item Quality Management in Procurement in chapter Create Purchase Order, using material QM001. Note that in step 4 Enter Purchase Order Data you need to use a warehouse-managed storage location, for example 335W.The confirmation control of the purchase order has to be inbound delivery. Navigate to the Item Detail section, and choose the Confirmation tab. In the Conf. Control field, select Inbound Delivery. However, leave this field as blank if you are to post synchronous goods receipt for purchase orders. |
| 3BR - Warehouse Inbound Processing | You have completed the step described in Warehouse Inbound Processing test script so that you have the stock to do the posting changes. |
| 2TX - Direct Procurement with Inbound Delivery | For Quality Management in Warehouse (from Supplier)Follow the instructions for the inbound delivery creation as described in scope item Direct Procurement with Inbound Delivery in chapter Option A: Create Inbound Delivery.You can skip this step if you are to post synchronous goods receipt for purchase orders. |

## Overview Table

### Quality Management in Warehouse (from Production)

This scope item consists of several process steps provided in the table below.

You find the test scripts listed below here:

- [1E1](https://me.sap.com/processnavigator/SolS/EARL_SolS-013/2308/SolP/1E1?region=DE)
- [3BT](https://me.sap.com/processnavigator/SolS/EARL_SolS-013/2308/SolP/3BT?region=DE)
- [3BW](https://me.sap.com/processnavigator/SolS/EARL_SolS-013/2308/SolP/3BW?region=DE)
- [3DV](https://me.sap.com/processnavigator/SolS/EARL_SolS-013/2308/SolP/3DV?region=DE)

| Process Step | Reference | Business Role | App / Transaction | Expected Results |
| --- | --- | --- | --- | --- |
| [Create Handling Unit (Optional)](#unique_9) [page ] 11 | 3DVProcess Step: . In the test script, go to Test Procedures > Create Handling Unit . | Warehouse Clerk (EWM) | Manage Inbound Deliveries – Warehouse (F7922) | Handling units are created. |
| [Post Goods Receipt](#unique_10) [page ] 19 | 3DVProcess Step: Post Goods Receipt | Warehouse Clerk (EWM) | Manage Inbound Deliveries – Warehouse (F7922) | Inspection lot is created and stock type is changed to Q. |
| [Create Warehouse Tasks](#unique_11) [page ] 25 | 3DVProcess Step: Create Putaway Warehouse Tasks | Warehouse Clerk (EWM) | Manage Inbound Deliveries – Warehouse (F7922) | Warehouse tasks are created. |
| [Confirm Warehouse Tasks](#unique_12) [page ] 26 | 3DVProcess Step: Confirm Putaway Warehouse Tasks | Warehouse Operative (EWM) | Process Warehouse Tasks (F4595) | Warehouse tasks are confirmed |
| [Record Inspection Results](#unique_13) [page ] 28 | Scope Item: 1E1Process Step: Record Inspection Results. | Quality Technician | Record Inspection Results (F1685A) | Inspection results are recorded. |
| [Make Usage Decision](#unique_14) [page ] 29 | Scope Item: 1E1Process Step: Record Usage Decision | Quality Engineer | Manage Usage Decisions (F2345) | Usage decision is made.System creates follow-up warehouse tasks. |
| [Repack Handling Units (Optional)](#unique_15) [page ] 30 | Scope Item: 3BWProcess Step: Repacking Handling Unit | Warehouse Clerk (EWM) | Pack Outbound Deliveries (F3193) | Handling units are repaeked. |
| [Create Ad Hoc Warehouse Task (Optional)](#unique_16) [page ] 31 | Scope Item: 3BTProcess Step: Create Ad Hoc Warehouse Task (Option 1) | Warehouse Clerk (EWM) | Create Product Warehouse Tasks (/SCWM/MONNAV_CR_P_WT) | Ad-hoc warehouse task is created. |
| [Confirm Warehouse Tasks](#unique_12) [page ] 26 | Scope Item: 3DVProcess Step: Confirm Putaway Warehouse Tasks | Warehouse Operative (EWM) | Process Warehouse Tasks - Picking (F3880) | Warehouse tasks are confirmed |

### Quality Management in Warehouse (from Supplier)

This scope item consists of several process steps provided in the table below.

You find the test scripts listed below here:

- [1FM](https://me.sap.com/processnavigator/SolS/EARL_SolS-013/2308/SolP/1FM?region=DE)
- [3BR](https://me.sap.com/processnavigator/SolS/EARL_SolS-013/2308/SolP/3BR?region=DE)
- [3BT](https://me.sap.com/processnavigator/SolS/EARL_SolS-013/2308/SolP/3BT?region=DE)
- [3BW](https://me.sap.com/processnavigator/SolS/EARL_SolS-013/2308/SolP/3BW?region=DE)

| Process Step | Reference | Business Role | App / Transaction | Expected Results |
| --- | --- | --- | --- | --- |
| [Create Handling Unit (Optional)](#unique_18) [page ] 34 | Scope Item: 3BRChapter: Create Handling UnitIn the test script, go to Test Procedures > Create Handling Unit . | Warehouse Clerk (EWM) | Manage Inbound Deliveries – Warehouse (F7922) | Handling units are created. |
| [Post Goods Receipt](#unique_19) [page ] 41 | Scope Item : 3BRChapter: Post Goods Receipt | Warehouse Clerk (EWM) | Manage Inbound Deliveries – Warehouse (F7922) | Inspection lot is created and stock type is changed to Q. |
| [Create Warehouse Tasks](#unique_20) [page ] 48 | Scope Item : 3BRProcess Step: Create Putaway Warehouse Tasks | Warehouse Clerk (EWM) | Manage Inbound Deliveries – Warehouse (F7922) | Warehouse tasks are created |
| [Confirm Warehouse Tasks](#unique_21) [page ] 49 | Scope Item : 3BRProcess Step: Confirm Warehouse Tasks | Warehouse Operative (EWM) | Process Warehouse Tasks - Picking (F3880) | Warehouse tasks are confirmed. |
| [Record Inspection Results](#unique_22) [page ] 50 | Scope Item : 1FMProcess Step: Record Inspection Results | Quality Technician | Record Inspection Results (F1685A) | Inspection results are recorded. |
| [Make Usage Decision](#unique_23) [page ] 51 |  | Quality Engineer | Record Usage Decision (QA11) | Usage decision is made.System creates follow-up warehouse tasks. |
| [Repack Handling Units (Optional)](#unique_24) [page ] 53 | Scope Item : 3BWProcess Step: Repacking Handling Unit | Warehouse Clerk (EWM) | Pack Outbound Deliveries (F3193) Pack Warehouse Stock (F3193) | Handling units are repacked. |
| [Create Ad Hoc Warehouse Task (Optional)](#unique_25) [page ] 54 | Scope Item : 3BTProcess Step: Create Ad Hoc Warehouse Task (Option 1) | Warehouse Clerk (EWM) | Create Product Warehouse Tasks (/SCWM/MONNAV_CR_P_WT) Create Product Warehouse Tasks | Ad-hoc warehouse task is created. |
| [Confirm Warehouse Tasks](#unique_26) [page ] 55 | Scope Item : 3BRProcess Step: Confirm Warehouse Tasks | Warehouse Operative (EWM) | Process Warehouse Tasks - Picking (F3880) | Warehouse tasks are confirmed. |

## Test Procedures

### Quality Management in Warehouse (from Production)

#### Create Handling Unit (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

|  |
| --- |
| Caution Before you proceed with the handling unit (HU) creation, a production order and an inbound delivery have to be created in the first step as described in chapter 2.4 Business Conditions. |

Purpose

In this process step, the Warehouse Clerk (EWM) selects the delivery, selects the Unpacked Items tab, and creates handling units. He or she can print the HU label by navigating from the app to the monitor.

|  |
| --- |
| Note This step applies if you have created an inbound delivery and will post goods receipt for the inbound delivery. If you are to post synchronous goods receipt for a production order, you can skip this step and create handling units in the next step when post synchronous goods receipt. |

Procedure

Refer to the process step Create Handling Unit in Scope Item Warehouse Production Integration (3DV).

In the test script, go to Test Procedures > Delivery-Based Goods Receipt from Production > Create Handling Unit .

You can find the document here [3DV](https://me.sap.com/processnavigator/SolS/EARL_SolS-013/2308/SolP/3DV?region=DE).

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

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

##### Option 1: Post Good Receipt for Inbound Delivery from Production

Purpose

The Warehouse Clerk (EWM) posts the goods receipt for the inbound delivery of the production order.

###### Variant 1: With Fiori App

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

###### Variant 2: With Radio Frequency Device

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

##### Option 2: Post Synchronous Goods Receipt for Production Order

Purpose

In this step, you post the goods receipt for a production order. An inspection lot will be created when the goods receipt is posted.

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
| 2 | Access the App | Open Post Goods Movement(MIGO). | The Goods Receipt Order screen is displayed. |  |
| 3 | Select Goods Receipt Order Screen | On the Goods Receipt Order screen, make the following entries and choose Enter.Goods Receipt: <Select>.Order: <Select>.Order Number: <Production Order number>.GR Goods Receipt: 101. | The items of the selected production order are displayed. |  |
| 4 | Enter Quantity | If required, check the quantity on the Quantity tab. |  |  |
| 5 | Check Storage Location | Select theWhere tab and check the storage location 105W.Note Note An additional storage location 105I and the corresponding availability group 002 can be introduced in the Cloud WM as an optional setup. Compared to the single storage location 105W / availability group 001 setup, the new setup can help distinguish stock that is still in the process of putaway and that is already in the warehouse.For example, the storage location 105I is used as the goods receipt storage location. During the goods receipt process, the stock remains in the storage location 105I and isn't available for sale (Stock Type F0 - Unrestricted Use in Putaway) until the putaway warehouse task(s) is/are confirmed. Once the putaway is finished, the stock is automatically posted to the storage location 105W and becomes available for sale (Stock Type F - Unrestricted Use in Warehouse).To enable the 105I storage location / availability setup, there are manual setup steps to be performed according to the instructions provided in the Warehouse Management Setup Guide. For more information, see chapter Additional Manual Configuration. |  |  |
| 6 | Create Handling Units (Optional) | If a packing instruction is available for the product on the Warehouse Management tab, you see the value 0 in the Unpacked Qnty AUoM field. The packaging proposal contains the following values:No. of HUsPack. MaterialHU TypeQty.AUoM (Quantity per HU in Alternative UoM)UnitQuantityBUoM (Base UoM)If no packaging proposals are available, create the handling units using one of the following options:Choose by Total Quantity and enter Packaging Material and No. of HUs.Choose by Quantity per HU and enter Quantity per HU and Packaging Material.Choose Adopt.Note Note Even if a packing instruction is available, you can delete the packaging proposal and create the handling units based on your own needs. However, once you choose Redetermine Packaging Proposal, the system reads the packing instruction and once again gives the packing proposal. |  |  |
| 7 | Check Storage Bin | On the Warehouse Management tab, enter the destination storage bin. E.g. storage typeS915 and storage bin PR-AREA.The default storage bin can be changed. E.g. storage typeS820 and storage bin QUAL-I01Note Note You can set a default destination bin for posting Goods Receipt in the Production Version of the Production Order. |  |  |
| 8 | Select Item Ok Indicator | Select the Item OK checkbox.Choose Check. Confirm the message Document is O.K. by choosing Enter. |  |  |
| 9 | Post | Choose Post. | The system displays the message: Material document 5xxxxxxxxx posted.Make a note of the material document number. |  |
| 10 | Select Display Material Document Screen | On the Goods Receipt Order screen, make the following entries and choose Enter:Display: <Select>.Material Document: <Select>.Material Document number: <Material Document number from the previous step>.Material Document Year:for example, 2024. | The selected material document is displayed. |  |
| 11 | Display Inspection Lot | On the Quantity tab, choose InspLot.Note Note Your CB user requires the Quality Technician role as the to display the inspection lot.Alternatively, you can display the inspection lot number by doing the following:On the Warehouse Management tab, choose Display Warehouse Document.Select the Warehouse Task and then choose List View -> Form View.In the Warehouse Task form view, find the inspection lot number in the Quality Insp. field of the Other Data section. |  |  |
| 12 | Check Inspection Lot | On the Display Inspection Lot screen, check the information such as material, inspection lot number and system status. |  |  |

#### Create Warehouse Tasks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Clerk creates warehouse tasks for putaway into the quality area or clarification zone for upcoming quality inspection.

|  |
| --- |
| Note This step applies if you have posted goods receipt for an inbound delivery. If you posted synchronous goods receipt for a purchase order, you can skip this step. |

Procedure

Refer to the process step Create Putaway Warehouse Tasks in scope item Warehouse Production Integration (3DV).

In the test script, go to Test Procedures > Delivery-Based Goods Receipt from Production > Create Putaway Warehouse Tasks .

You can find the document here [3DV](https://me.sap.com/processnavigator/SolS/EARL_SolS-013/2308/SolP/3DV?region=DE).

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

A putaway list is printed and handed over to the Warehouse Operative (EWM), who performs the warehouse tasks and confirms them in the system.

|  |
| --- |
| Note This step applies if you have posted goods receipt for an inbound delivery. If you posted synchronous goods receipt for a production order, you can skip this step. |

Procedure

Refer to the process step Confirm Putaway Warehouse Tasks in Scope Item Warehouse Production Integration (3DV).

In the test script, go to Test Procedures > Delivery-Based Goods Receipt from Production > Confirm Putaway Warehouse Tasks > Variant 1: with Fiori App .

You can find the document here [3DV](https://me.sap.com/processnavigator/SolS/EARL_SolS-013/2402/SolP/3DV?region=DE).

##### Variant 2: With Radio Frequency Device

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Operative (EWM) performs the warehouse tasks and confirms them in the system with mobile radio frequency device.

To work with the radio frequency framework, make sure all the steps as described in the setup instruction guide for scope item 63X - Mobile Radio Frequency Devices in Warehousing with QM have been performed.

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/ae167716e1c4d285f608c211dd2d0cab)

|  |
| --- |
| Note This step applies if you have posted goods receipt for an inbound delivery. If you posted synchronous goods receipt for a production order, you can skip this step. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Fiori Launchpad | Log on to the SAP Fiori launchpad as a Warehouse Operative (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open the SAP Fiori app Test RF Environment(/SCWM/RFUI)The app allows you to test working in an RF environment. For working with mobile RF devices, see also SAP Note 3048632. |  |  |
| 3 | Enter Data for RFUI | Whse No: 1750Resource: SHA1-1 or SHR1-1Dflt Dvc.: SE01Choose Enter.Note Note Use resource SHA1-1 for putting away to S001 or SHR1-1 for putting away to SB01. |  |  |
| 4 | Choose Menu | Choose 01 System-Guided > 02 SystemGuided Queue . |  |  |
| 5 | Enter Queue Name | In the Queue field, enter QI-820 or QI-970 for putaway into the Quality Area or Clarification Zone respectively. |  |  |
| 6 | Verify Source Bin and Enter HU | Note Note This step is only relevant, if you created handling units in step Create Handling Unit.Verify the Src.Bin (Source Bin)HU: < Enter the HU ID from previous step > |  |  |
| 7 | Verify the Source Information Fields | Verify the following fields if they are required:Src.Bin (Source Bin)Prod. (Product)Srce Qty (Source Quantity)ChooseEnter. |  |  |
| 8 | Verify the Destination Information fFelds | Verify the following fields, if they are required:Prod. (Product)ActQty (Quantity)Dest.Qty (Destination Quantity)DstBin (Destination Bin)Choose Enter. |  |  |
| 9 | Repeat Steps | Repeat steps 6 to 8 until no suitable warehouse orders are found. |  |  |
| 10 | Logoff RFUI | You can choose Back to the previous screens.Choose Logoff.Choose Save. |  |  |

#### Record Inspection Results

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Quality Technician executes the quality inspection and records inspection results for the inspection lot.

Procedure

Refer to the process step Record Inspection Results in Scope Item Quality Management in Discrete and Process Manufacturing (1E1).

In the test script, go to Test Procedures > Quality Management in Discrete Manufacturing - Goods Receipt from Production > Quality Inspection > Record Inspection Results . You can find the document here [1E1](https://me.sap.com/processnavigator/SolS/EARL_SolS-013/2402/SolP/1E1?region=DE).

#### Make Usage Decision

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection is done, and the inspection result is recorded. You must decide whether or not to accept the assembly depending on the inspection result.

Accept the inspection lot: Inspected stock is ok, so the received goods are accepted. The stock is posted to unrestricted stock (stock type “F”) and warehouse tasks for putaway will be created automatically upon usage decision.

Reject the inspection lot: Inspected stock is not ok, so the received goods are rejected and the follow-up activity to post the stock to blocked stock is triggered. The system posts the stock from quality stock (“Q”) to blocked stock (“B”). The stock stays in the clarification zone.

|  |
| --- |
| Note Since SAP S/4HANA 2111 cloud essentials edition, upon Goods Receipt from Production Order, products are moved to the Quality Area / Quality Work Center where the inspection lots are processed instead of the clarification area. Once the inspection lots are accepted upon usage decision, putaway warehouse task is created automatically.Existing customers do not get the changes by upgrade and the process works as it was before. For more information, please see chapter 2.3 [Additional Manual Configuration](#unique_2) [page ] 5 |

Further processing of the blocked stock does not belong to this process. It is contiued by other processes, for example return to vendor or scrapping.

Procedure

Refer to the process step Make Usage Decision in Scope Item Quality Management in Discrete and Process Manufacturing (1E1).

In the test script, go to Test Procedures > Quality Management in Discrete Manufacturing - Goods Receipt from Production > Quality Inspection > Make Usage Decision . You can find the document here [1E1](https://me.sap.com/processnavigator/SolS/EARL_SolS-013/2402/SolP/1E1?region=DE).

|  |
| --- |
| Note If you make a partial usage decision, depending on your inspection result, you can select in the decision column one of the following usage decision codes:Usage Decisions:A1 - Accepted-unrestricted stock .A3 - Accepted-unrestricted-sample-consumption.R1 - Rejected-blocked stock .R310 - Rejected-scrap (partial quantity).In case you accept the inspection lot, the corresponding follow-up action is the putaway to the final storage bin.In case you reject the inspection lot, the corresponding follow-up action is the putaway to the clarification zone. The stock is booked to blocked stock.In case you want to scrap the inspection lot, the corresponding follow-up action is scrap to cost center. The stock is scrapped and the costs are booked to a cost center.In case the sample is destroyed during the inspection, the corresponding follow-up action is the sample consumption. The sample quantity is posted goods issue as it is no longer usable after the inspection. |

#### Repack Handling Units (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Operative (EWM) repacks the handling unit (HU) to another handling unit.

Procedure

|  |
| --- |
| Caution This step is not optional, in case a partial quantity decision was made with different decisions for one pallet. The goal is to distribute the goods on different pallets, based on their stock type. |

Example: On a pallet of 12 PCs were 8 PCs decided as ok (accepted) and 4 PCs were decided as not ok (rejected). The 8 PCs of unrestricted stock (stock type “F”) are repacked onto HU 1, and the 4 PCs of blocked stock (stock type “B”) are repacked onto HU 2.

Refer to the process step Repacking Handling Unit in Scope Item Warehouse Internal Repacking (3BW).

In the test script, go to Test Procedures > Repacking Handling Unit . You can find the document here [3BW](https://me.sap.com/processnavigator/SolS/EARL_SolS-013/2402/SolP/3BW?region=DE).

#### Create Ad Hoc Warehouse Task (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If the goods were ok, they can be moved to the final putaway location. Therefore, an ad hoc warehouse task is created by the Warehouse Clerk (EWM).

|  |
| --- |
| Note Since SAP S/4HANA 2111 cloud essentials edition, automatic warehouse task creation upon usage decision is enabled in this process for new customers. Therefore this step is only required for existing customers. About how to enable the automatic putaway warehouse task creation upon usage decision for existing customers, please see [Additional Manual Configuration](#unique_2) [page ] 5. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Open the SAP Fiori launchpad as a Warehouse Clerk (EWM). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the SAP Fiori Create Product Warehouse Tasks(/SCWM/MONNAV_CR_P_WT) app. | The Create Product Warehouse Tasks(/SCWM/MONNAV_CR_P_WT) screen displays. |  |
| 3 | Decide your Filter Criteria | Enter Storage Type: For example, S970.Choose Execute. | The Create Product Warehouse Task screen displays. |  |
| 4 | Choose your Stock | Choose one of the stock lines and select More Methods > Create Warehouse Task. | The Create Warehouse Task dialog box (that requests for data) is displayed. |  |
| 5 | Create Warehouse Task | Create the warehouse task and enter the following data:Src Trgt Qty AUoM (Quantity): For example,8 PCDestination Bin and Destination Storage Type are filled automatically.Warehouse Process Type: for example, S997 - Putaway from Clarification.Choose Create WT. | The warehouse task is created, as you can see in the display log. A warehouse task list is automatically printed in the background.You must find the open product warehouse task in the monitor node warehouse task. Therefore, note down the warehouse task number. |  |
| 6 | Complete the Step | Note down the warehouse task number.Choose Continue to close the log and then choose Home or repeat the steps, if necessary. |  |  |

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

A putaway list is printed and handed over to the Warehouse Operative (EWM), who performs the warehouse tasks and confirms them in the system.

Procedure

Refer to the process step Confirm Putaway Warehouse Tasks in scope item Warehouse Production Integration (3DV).

In the test script, go to Test Procedures > Delivery-Based Goods Receipt from Production > Confirm Putaway Warehouse Tasks . You can find the document here [3DV](https://me.sap.com/processnavigator/SolS/EARL_SolS-013/2402/SolP/3DV?region=DE).

##### Variant 2: With Radio Frequency Device

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Operative (EWM) performs the warehouse tasks and confirms them in the system with a mobile radio frequency device.

To work with radio frequency framework, make sure all the steps as described in the Setup Instruction guide for scope item 63X - Mobile RF Devices in Warehousing with Quality Management in warehousing with QM have been performed:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/ae167716e1c4d285f608c211dd2d0cab)

Procedure

Refer to the process step Confirm Putaway Warehouse Tasks in scope item Warehouse Production Integration (3DV).

In the test script, go to Test Procedures > Delivery-Based Goods Receipt from Production > Confirm Putaway Warehouse Tasks > Variant 2: with Radio Frequency Device .

You can find the document here [3DV](https://me.sap.com/processnavigator/SolS/EARL_SolS-013/2402/SolP/3DV?region=DE).

### Quality Management in Warehouse (from Supplier)

#### Capture Serial Number (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, the Warehouse Clerk selects the delivery and enters the serial number for the material. You can skip this step if your product is not serial number-managed.

|  |
| --- |
| Note This step applies if you have created an inbound delivery and will post goods receipt for the inbound delivery. If you are to post synchronous goods receipt for a purchase order, you can skip this step. |

Procedure

Refer to the process step Capture Serial Number (Optional) in scope item Warehouse Inbound Processing (3BR).

In the test script, go to Test Procedures > Capture Serial Number . You can find the document here [3BR](https://me.sap.com/processnavigator/SolS/EARL_SolS-013/2402/SolP/3BR?region=DE).

#### Create Handling Unit (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

|  |
| --- |
|  |

Before you proceed with the handling unit creation, a purchase order and an inbound delivery have to be created in the first step as described in the Business Conditions.

Purpose

In this process step, the Warehouse Clerk selects the delivery, selects the tab "Unpacked Items" and creates handling units.

|  |
| --- |
| Note This step applies if you have created an inbound delivery and will post goods receipt for an inbound delivery. If you are to post synchronous goods receipt for a purchase order, you can skip this step and create handling units in the next step when posting synchronous goods receipt. |

##### Variant 1: With Fiori App – Automatic Packing

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
| Note The automatic packing works, if packing instructions are defined for the relevant product. |

|  |
| --- |
| Caution This step is mandatory for material TG21, as it needs to be placed in SB01, where the handling unit requirement is set.If the products are serial number-managed, you need to use the Variant 2: With Fiori App - Packing at Work Center. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Fiori Launchpad | Log on to the SAP Fiori launchpad as a Warehouse Clerk (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open the SAP Fiori app Manage Inbound Deliveries – Warehouse (F7922) . | The Manage Inbound Delivery screen appears. |  |
| 3 | Choose Filters | On the Manage Inbound Deliveries screen, choose Adapt Filters. | The Adapt Filters dialog box appears. |  |
| 4 | Select Fields for Filter | On the Adapt Filters dialog box, make sure the following fields are selected for the current filter:Purchase Order.Choose OK. |  |  |
| 5 | Search for Inbound Delivery | On the Manage Inbound Deliveries screen, make the following entries:Purchase Order: <your purchase order number>.Choose Go. | Your inbound delivery is displayed. |  |
| 6 | Select Inbound Delivery | On the Manage Inbound Deliveries screen, select your inbound delivery. | Your inbound delivery is displayed. |  |
| 7 | Choose Details | Choose button Details. | Inbound delivery details are displayed. |  |
| 8 | Select Unpacked Items | On the Manage Inbound Deliveries screen in the Items section, choose the Unpacked Items tab and select the items to be packed. | On the Manage Inbound Deliveries screen, choose Pack Automatically to pack all unpacked items automatically. |  |
| 9 | Decide Packing Options | If packing instructions are defined for all the delivery items, you can pack automatically. In this case, follow step 10.If no packing instructions arefined for all the delivery items, you can pack manually. In this case, follow steps 11 to 13. |  |  |
| 10 | Pack Automatically | On the Manage Inbound Deliveries screen, choose Pack Automatically to pack all unpacked items automatically based on the packing instructions. |  |  |
| 11 | Choose Create HU | Choose Create HUs or Create Mixed HUs. |  |  |
| 12 | Enter Packaging Material and Number of HUs | On the Create Handling Unit dialog box, make the following entries:Pack. Material: PMPALLET.Number of HUs: <number of handling units>. |  |  |
| 13 | Choose Create | Choose Create. | The Delivery Items have been removed from the Unpacked Items section. |  |
| 14 | Note Down your Delivery Number | Note down your delivery number for testing purposes. | On the Manage Inbound Deliveries screen on the Total Items tab, it shows No. of HUs: X. |  |

##### Variant 2: With Fiori App – Packing at Work Center

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
| Caution This step is mandatory for material TG21, as it needs to be placed in SB01, where the handling unit requirement is set.If the products are serial number-managed and are to be packed into HUs, you can assign serial numbers in this step. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on to the SAP Fiori Launchpad | Log on to the SAP Fiori launchpad as a Warehouse Clerk (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2. | Access the SAP Fiori App | Open the SAP Fiori app Manage Inbound Deliveries – Warehouse (F7922). | The Manage Inbound Deliveries – Warehouse (F7922) screen appears. |  |
| 3. | Choose Filters | On the Manage Inbound Deliveries screen, choose Adapt Filters. | The Adapt Filters dialog box appears. |  |
| 4. | Select Fields for Filter | On the Adapt Filters dialog box, make sure the following fields are selected for the current filter:Purchase Order.Choose OK. |  |  |
| 5. | Search for Inbound Delivery | On the Manage Inbound Deliveries screen, make the following entries:Purchase Order: <your purchase order number>.Choose Go. | The Manage Inbound Deliveries screen appears and your inbound delivery is displayed. |  |
| 6. | Choose Inbound Delivery | On the Manage Inbound Deliveries screen, choose your inbound delivery. | Your inbound delivery is displayed. |  |
| 7. | Go to Packing Work Center | On the Manage Inbound Deliveries screen, choose Packing. |  |  |
| 8. | Decide Packing Options | If packing instructions are defined for all the delivery items, you can pack automatically. In this case, follow step 9.If packing instructions are defined for some of the delivery items, you can pack those items based on packing proposals. In this case, follow steps 10 and 11.You can also pack completely manually. In this case, follow steps 12 to 14. |  |  |
| 9. | Pack Automatically | On the Work Center Packing for Inbound Delivery (Time Zone CET) screen, select all the delivery items and then choose Pack Automatically. | HUs have been created automatically according to the pre-defined Packing Instruction. |  |
| 10. | Pack with Packing Proposals | On the Work Center Packing for Inbound Delivery (Time Zone CET) screen, select one of the delivery items (with packing instruction defined) and then choose Packing Proposal. |  |  |
| 11. | Check Packing Proposals | In the Packing Proposal dialog box, check that the packaging material matches the packaging material maintained in the packing instruction for the supplier of the inbound delivery.The proposed quantities correspond the quantities of your packing instruction.Select the desired proposal and then choose Enter. | An HU has been created according to the pre-defined Packing Instruction. |  |
| 12. | Create HUs Manually | On the Work Center Packing for Inbound Delivery (Time Zone CET) screen, choose Create HU tab, and make the following entries:Pack. Material: PMPALLET.Number of HUs: <number of handling units>.Choose Execute.Take a note of the HU numbers created. |  |  |
| 13. | Repack Product | Choose Repack Product tab, and make the following entries:Delivery Number: <your Inbound Delivery Number>.Item Number: <item Number, for example 10>.Quantity: <quantity to be packed in the destination HU>.Unit of Measure: <UoM, for example PC>.Dest. HU: <one of the HU created in step 12>.Choose Execute. |  |  |
| 14. | Repeat Repacking Product | Repeat step 13 until all products have been repacked into HUs. |  |  |
| 15. | Enter Serial Numbers (optional) | At the lower left part of the screen, double click the product that has been packed into an HU, and then choose the Serial Nos tab.Enter the serial numbers manually for each unit of the material or choose Create SNs Automatically to allow the system assignment of the serial numbers.Note If the products are serial number-managed and are to be packed into HUs, you can assign serial numbers in this step. |  |  |
| 16. | Choose Save | Choose Save. |  |  |
| 17. | Exit the Packing Work Center | Choose Exit. |  |  |
| 18. | Note Down your Delivery Number | Note down your delivery number for testing purposes. | On the Manage Inbound Deliveries screen on the Total Items tab, it shows No. of Serial Numbers Entered: X / X. |  |

##### Variant 3: With Radio Frequency Devices

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
| Caution This step is mandatory for material TG21, as it needs to be placed in SB01, where the handling unit requirement is set.If the products are serial number-managed and are to be packed into HUs, you need to create handling units using Variant 2: with Fiori App - Packing at Work Center.For working with mobile RF devices, make sure all the steps as described in the Setup Instruction guide for scope item 63V - Mobile RF Devices in Warehousing have been performed. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Fiori Launchpad | Log on to the SAP Fiori launchpad as a Warehouse Operative (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open the SAP Fiori app Test RF Environment (/SCWM/RFUI)The app allows you to test working in an RF environment. For working with mobile RF devices, see also SAP Note [3048632](https://me.sap.com/notes/3048632). |  |  |
| 3 | Enter Data for RFUI | Whse No: 3350Resource: SHA1-1 or SHR1-1DefPresDvc: SE01Choose Enter. |  |  |
| 4 | Choose Menu | Choose 03 Inbound Processes > 02 Receiving of HUs > 01 Rec. HU By Delivery. |  |  |
| 5 | Enter Delivery Number | In the Delivery field, enter your delivery number. |  |  |
| 6 | Check Delivery Information | The inbound delivery is now displayed with the following information:DeliveryPartner (number and name)Warehouse Door (only displayed if applicable)No. of HUs (number of HUs that HUs that have been created up to this point of time)Choose Enter to proceed. |  |  |
| 7 | Check Delivery Status | Check the following information that shows the delivery process status:Proc.HUs: Y / YPck.Compl. : (X) or emptyGR Posted: XWT Created: EmptyNote The Proc.HUs field indicates the status of the HU processing. Y indicates the number of HUs that have been created. X indicates the number of HUs that have been processed.If all the unpacked products have been processed, the field Pck.Compl. is checked and you can go to process step Post Goods Receipt Variant 2: With Radio Frequency Devices. Otherwise go to step 8 to continue to create new HUs. |  |  |
| 8 | Create New HU | Choose New HU.On the next screen, enter the following values:Product: <Product Number>Actual Qty: <Quantity> <UoM>BstBefDate: <Best before Date, in format DD.MM.YYYY> (if applicable)Choose Next. |  |  |
| 9 | Enter Packaging Material | Enter values in the following fields:New P.Mat. (Packaging Material)Choose Enter. The HU type gets populated.Choose Next. |  |  |
| 10 | Check HU Information | Check the information of the newly created HU. Take a note of the following fields, if necessary:HU (HU number)Batch (Batch number)Styp (Stock Type)ProTyp (Warehouse Process Type)Choose Back. |  |  |
| 11 | Repeat Steps | Repeat steps 8 to 10 until all the unpacked products are packed into HUs. Partial packing is allowed. If each unpacked product is packed into Hus, the field Pck.Compl. is checked. |  |  |
| 12 | Logoff RFUI | You can choose Back to go to the previous screens.Note If you would like to post a goods receipt using the mobile RF devices, stay logged on in the app.Choose Logoff.Choose Save. |  |  |

#### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

##### Option 1: Post Good Receipt for Inbound Delivery from Procurement

Purpose

Goods receipt is posted. SAP S/4HANA is updated accordingly.

###### Variant 1: With Fiori App

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
| 1. | Log on to the SAP Fiori Launchpad | Log on to the SAP Fiori launchpad as a Warehouse Clerk (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2. | Access the SAP Fiori App | Open the SAP Fiori app Manage Inbound Deliveries – Warehouse (F7922). | The Manage Inbound Deliveries – Warehouse (F7922) screen appears. |  |
| 3. | Choose Filters | On the Manage Inbound Deliveries screen, choose Adapt Filters. | The Adapt Filters dialog box appears. |  |
| 4. | Select Fields for Filter | On the Adapt Filters dialog box, make sure the following fields are selected for the current filter:Planned Dlv. DatePurchase OrderChoose OK. |  |  |
| 5. | Search for Inbound Delivery | Planned Delivery Date/Time: <your planned delivery date/Time>.Purchase Order: <your purchase order number>.Choose Go. | The Manage Inbound Deliveries screen appears and your inbound delivery is displayed. |  |
| 6. | Choose Inbound Delivery | On the Manage Inbound Deliveries screen, choose your inbound delivery. | Your Inbound Delivery is displayed. |  |
| 7. | Choose Delivery Items | On the Manage Inbound Deliveries screen, choose your Delivery Items. |  |  |
| 8. | Post Goods Receipt | Choose Goods Receipt. | The following system message appears:Goods receipt posted. |  |

###### Variant 2: With Radio Frequency Devices

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

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/ad27f6503263c30b71125c03596bc081)

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Fiori Launchpad | Log on to the SAP Fiori launchpad as a Warehouse Operative (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open the SAP Fiori app Test RF Environment (/SCWM/RFUI)The app allows you to test working in an RF environment. For working with mobile RF devices, see also SAP Note [3048632](https://me.sap.com/notes/3048632). |  |  |
| 3 | Enter Data for RFUI | Whse No: 3350Resource: SHA1-1 or SHR1-1DefPresDvc: SE01Choose Enter. |  |  |
| 4 | Choose Menu | Choose 03 Inbound Processes > 02 Receiving of HUs > 01 Rec. HU By Delivery. |  |  |
| 5 | Enter Delivery Number | In the Delivery field, enter your delivery number. |  |  |
| 6 | Check Delivery Information | The inbound delivery is now displayed with the following information:DeliveryPartner (number and name)Warehouse Door (only displayed if applicable)No. of HUs (number of HUs that HUs that have been created up to this point of time)Choose Enter to proceed. |  |  |
| 7 | Check Delivery Status | Check the following information that shows the delivery process status:Proc.HUs: X / YPck.Compl. :X or emptyGR Posted:EmptyWT Created: EmptyNote The Proc.HUs field indicates the status of the HU processing. Y indicates the number of HUs that are created. X indicates the number of HUs that have been processed.If HUs have been created for all the unpacked products, the field Pck.Compl. is checked. |  |  |
| 8 | Post Goods Receipt | Choose > and then choose PostGRNote If no HUs are created, you can still post goods receipts for all the unpacked products. In this case, you receive a system message Delivery not fully packed. Continue?. Choose Yes to continue. | The field GR Posted is checked |  |
| 9 | Logoff RFUI | Choose Back to go to the the previous screens.Note If you would like to create putaway warehouse tasks using the mobile RF devices, stay logged on in the app.Choose Logoff.Choose Save. |  |  |

##### Option 2: Post Synchronous Goods Receipt for Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you post the synchronous goods receipt against the purchase order. An inspection lot will be created when the goods receipt is posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad as the Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Post Goods Movement(MIGO). | The Goods Receipt Purchase Order screen is displayed. |  |
| 3 | Select Goods Receipt Order Screen | On the Goods Receipt Purchase Order screen, make the following entries and choose Enter.Goods Receipt: <Select>.Purchasing Order: <Select>.Order number: <Purchase Order number>.GR Goods Receipt: 101. | The items of the selected purchase order are displayed. |  |
| 4 | Enter Quantity | If required, check the quantity on the Quantity tab. |  |  |
| 5 | Check Storage Location | Select the Where tab and check storage location105W.Note An additional storage location 105I and the corresponding availability group 002 can be introduced in the Cloud WM as an optional setup. Compared to the single storage location 105W / availability group 001 setup, the new setup can help distinguish stock that is still in the process of putaway and that is already in the warehouse.For example, the storage location 105I is used as the goods receipt storage location. During the goods receipt process, the stock remains in the storage location 105I and isn't available for sale (Stock Type F0 – Unrestricted Use in Putaway) until the putaway warehouse task(s) is/are confirmed. Once the putaway is finished, the stock is automatically posted to the storage location 105W and becomes available for sale (Stock Type F – Unrestricted Use in Warehouse).To enable the 105I storage location / availability setup, there are manual setup steps to be performed according to the instructions provided in the Warehouse Management Setup Guide. For more information, see chapter Additional Manual Configuration. |  |  |
| 6 | Enter the Batch Number (Optional) | On the Batch tab, make the following entries and choose Enter.Batch: <Batch Number>.To enter the batch number, you can use one of the following options:Select an existing batch numberEnter an external batch numberChoose Classification to create a new batch number (internal number assignment).Date of Manufacture: Maintain the date when necessarySLED/BBD: Maintain the date when necessary |  |  |
| 7 | Create Handling Units (Optional) | If a packing instruction is available for the product, you see the on the Warehouse Management tab that a value in the Unpacked Qnty AUoM field is 0. Then the packaging proposal contains the following values:No. of HUsPack. MaterialHU TypeQty.AUoM (Quantity per HU in Alternative UoM)UnitQuantityBUoM (Base UoM)If no packaging proposal is given, create handling units using one of the following options:Choose by Total Quantity and enter Packaging Material and No. of HUs.Choose by Quantity per HU and enter Quantity per HU and Packaging Material.Choose Adopt.Note Even if a packing instruction is available, you can delete the packaging proposal and create the handling units based on your own needs. However, once you choose Redetermine Packaging Proposal, the system reads the packing instruction and once again gives the packing proposal. |  |  |
| 8 | Check Storage Bin | On the Warehouse Management tab, check the default Storage Type: S910 and Storage Bin :GR-AREA.Note The default storage bin can be changed. E.g., Storage Type S820 and Storage Bin QUAL-I01 |  |  |
| 9 | Select Item OK Indicator | Select the Item OK checkbox.Choose Check. Confirm the message Document is O.K. by choosing Enter. |  |  |
| 10 | Post | Choose Post. | The system displays the message:Material document 5xxxxxxxxx postedMake a note of the material document number. |  |
| 11 | Select Display Material Document Screen | On the Goods Receipt Purchase Order screen, make the following entries and choose Enter.Display: <Select>Material Document: <Select>.Material Document number: <Material Document number from the previous step>.Material Document Year : for example 2024 | The items of the selected purchase order are displayed. |  |
| 12 | Display Inspection Lot | On the Quantity tab, choose InspLot.Note Your CB user requires the Quality Techniciana role as the to display the inspection lot.Alternatively, you can display the inspection lot number by doing the following:On the Warehouse Management tab, chooseDisplay Warehouse Document.Select the Warehouse Task and then choose List View -> Form View.In the Warehouse Task form view, find the inspection lot number in the Quality Inspection. field of the Other Data section. |  |  |
| 13 | Check Inspection Lot | On the Display Inspection Lot screen, check the information such as material, inspection lot number and system status. |  |  |

#### Create Warehouse Tasks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Clerk creates warehouse tasks for putaway into the quality area or clarification zone for upcoming quality inspection.

|  |
| --- |
| Note This step applies if you have posted goods receipt for an inbound delivery. If you posted synchronous goods receipt for a purchase order, you can skip this step. |

Procedure

Refer to the process step Create Putaway Warehouse Tasks in scope item Warehouse Inbound Processing (3BR).

In the test script, go to Test Procedures > Create Putaway Warehouse Tasks . You can find the document here [3BR](https://me.sap.com/processnavigator/SolS/EARL_SolS-013/2308/SolP/3BR?region=DE).

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

A putaway list is printed and handed over to the Warehouse Operative (EWM), who performs the warehouse tasks and confirms them in the system. Please note that the Warehouse Operative (EWM) can also confirm warehouse tasks using the Warehouse Monitor (/SCWM/MON) (Business Catalog WM - Monitoring) app.

|  |
| --- |
| Note This step applies if you have posted goods receipt for an inbound delivery. If you posted synchronous goods receipt for a purchase order, you can skip this step. |

Procedure

Refer to the process step Confirm Putaway Warehouse Tasks in scope item Mobile RF Devices in Warehousing with Quality Management (3BR).

In the test script, go to Test Procedures > Confirm Putaway Warehouse Tasks > Variant 1: With Fiori App.

You can find the document here [3BR](https://me.sap.com/processnavigator/SolS/EARL_SolS-013/2402/SolP/3BR?region=DE).

##### Variant 2: With Radio Frequency Device

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Operative (EWM) performs the warehouse tasks and confirms them in the system with mobile radio frequency device.

To work with radio frequency framework, make sure all the steps as described in the setup instruction guide for scope item 63X - Mobile RF Devices in Warehousing with Quality Management have been performed.

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/ae167716e1c4d285f608c211dd2d0cab)

|  |
| --- |
| Note This step applies if you have posted goods receipt for an inbound delivery. If you posted synchronous goods receipt for a purchase order, you can skip this step. |

Procedure

Refer to the process step Confirm Warehouse Tasks in scope item Warehouse Inbound Processing (3BR).

In the test script, go to Test Procedures > Confirm Warehouse Tasks > Variant 2: with Radio Frequency Device .

You can find the document here [3BR](https://me.sap.com/processnavigator/SolS/EARL_SolS-013/2402/SolP/3BR?region=DE).

#### Record Inspection Results

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The trading goods undergo a quality inspection to ensure that it meets the predefined quality requirements.

In this step, the Quality Technician records the inspection result for the required inspection characteristics.

Procedure

Refer to the process step Record Inspection Results in scope item Quality Management in Procurement (1FM).

In the test script, go to Test Procedures > Regular Quality Inspection Process > Quality Inspection > Record Inspection Results . You can find the document here [1FM](https://me.sap.com/processnavigator/SolS/EARL_SolS-013/2308/SolP/1FM?region=DE).

#### Make Usage Decision

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection is done, and the inspection result is recorded. You must decide whether or not to accept the assembly depending on the inspection result.

- Accept the Inspection Lot: Inspected stock is ok, so the received goods are accepted. The stock is posted to unrestricted stock (stock type “F”) and warehouse tasks for putaway will be created automatically upon usage decision.
- Reject the Inspection Lot: Inspected stock is not ok, so the received goods are rejected and the follow-up activity to post the stock to blocked stock is triggered. The system posts the stock from quality stock (“Q”) to blocked stock (“B”). The stock stays in the clarification zone.

|  |
| --- |
| Note Since SAP S/4HANA 2111 cloud essentials edition, upon goods receipt from purchase order, products are moved to the quality area / quality work center where the inspection lots are processed instead of the clarification area. Once the inspection lots are accepted upon usage decision, the putaway warehouse task is created automatically.Existing customers do not get the changes by upgrade and the process works as it was before. For more information, please see [Additional Manual Configuration](#unique_2) [page ] 5 |

Further processing of the blocked stock does not belong to this process. It is continued by other processes, for example return to vendor or scrapping.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Quality Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Record Usage Decision (QA11). | The Record Usage Decision: Initial Screen displays. |  |
| 3 | Select Extended Inspection Lot Selection | On the Record Usage Decision: Initial Screen, select Extended inspection lot selection in the top-right corner. | The Select Inspection Lots screen displays. |  |
| 4 | Filter your Inspection Lot | On the Select Inspection Lots screen, make the following entries:Delivery: <your inbound delivery number from previous step> |  |  |
| 5 | Choose Continue | Choose Continue. | The Record Usage Decision: Characteristic Overview screen appears, and your inspection lot is displayed. |  |
| 6 | Decide on Usage Decision - Partial Quantity or Collective Usage Decision | Decide for one of the following options:Make a Partial Quantity Decision: Please continue with step 7.Only make a Collective Usage Decision: Please continue with step 13. | Partial Quantity Decision: Make a usage decision only for a certain part of the inspection-relevant quantities. An example process is to accept certain quantities and put them to the final bin, in order to avoid a production stop caused by limited resources.Collective Usage Decision: Make a usage decision for all pieces of the inspection relevant quantities. |  |
| 7 | Make a Partial Quantity Decision | Select the WM Inspection. | The Stock based Q-Inspection without Work Center dialogbox appears and the stock items to be inspected are displayed. |  |
| 8 | Display Quality Inspection Details | Select one of the items, and choose Inspection can be created/changed in the Action column. | The Qual. Inspection details are displayed. |  |
| 9 | Add Inspection Document Item | In the Stock based Q-Inspection without Work Centerdialog box in the Qual. Inspection section, select the Add inspection document item. | In the Qual. Inspection section, a new row is added. |  |
| 10 | Distribute Available Quantities | Distribute the available quantities according to your inspection result. |  |  |
| 11 | Select Follow-Up Action | Depending on your inspection result, select in the Decision column one of the following usage decision codes for each of the rows:Usage Decisions:A1 - Accepted-unrestricted stock.A3 - Accepted-unrestricted-sample-consumption.R1 - Rejected-blocked stock.R310 - Rejected-scrap (partial quantity). | In case you accept the inspection lot, the corresponding follow-up action is the putaway to the final storage bin.In case you reject the inspection lot, the corresponding follow-up action is the putaway to the clarification zone. The stock is booked to blocked stock.In case you want to scrap the inspection lot, the corresponding follow-up action is scrap to cost center. The stock is scrapped and the costs are booked to a cost center.In case the sample is destroyed during the inspection, the corresponding follow-up action is the sample consumption. The sample quantity is posted goods issue as it is no longer usable after the inspection.Example:Total quantity: 12 PCsInspection Result: 8 PCs are ok, 4 PCs are not okCreate two lines:Row 1 - Quantity: 8 PCs, Decision: A1Row 2 - Quantity: 4 PCs, Decision: R1 |  |
| 12 | Select Take Over Partial Lot Inspection | Select Take Over Partial Lot Inspection. | The Record Usage Decision: Characteristic Overview screen appears. |  |
| 13 | Make a Collective Usage Decision | On the Record Usage Decision: Characteristic Overview screen, enter a usage decision code depending on your inspection result:UD Code:A1 - Accepted-unrestricted stock .A2 - Accepted-unrestricted - minor quality .A3 - Accepted-unrestricted-sample consumption .A9 - Accepted-automatic usage decision .R1 - Rejected-blocked stock .R210 - Rejected-return supplier w/o delivery .R220 - Rejected-return supplier with delivery . | You can also skip the partial quantity decision and only make a collective usage decision. |  |
| 14 | Choose Save | Choose Save. | On the Record Usage Decision: Initial Screen the following message appears:Usage decision for lot <Inspection Lot Number> is savedThe follow-up actions have been triggered. |  |

#### Repack Handling Units (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Operative (EWM) repacks the handling unit (HU) to another handling unit.

Procedure

|  |
| --- |
| Caution This step is not optional if you created a handling unit and if a partial quantity decision was made with different decisions for one pallet. The goal is to distribute the goods on different pallets, based on their stock type. |

Example: On a pallet of 12 PCs were 8 PCs decided as ok (accepted) and 4 PCs were decided as not ok (rejected). The 8 PCs of unrestricted stock (stock type “F”) are repacked onto HU 1, and the 4 PCs of blocked stock (stock type “B”) are repacked onto HU 2.

Refer to the process step Repacking Handling Unit in Scope Item Warehouse Internal Repacking (3BW).

In the test script, go to Test Procedures > Repacking Handling Unit . You can find the document here [3BW](https://me.sap.com/processnavigator/SolS/EARL_SolS-013/2402/SolP/3BW?region=DE).

#### Create Ad Hoc Warehouse Task (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If the goods were ok, they can be moved to the final putaway location. Therefore, an ad hoc warehouse task is created by the Warehouse Clerk (EWM).

|  |
| --- |
| Note Since SAP S/4HANA 2111 cloud essentials edition, automatic warehouse task creation upon usage decision is enabled in this process for new customers. Therefore this step is only required for existing customers. About how to enable the automatic putaway warehouse task creation upon usage decision for existing customers, please see [Additional Manual Configuration](#unique_2) [page ] 5. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on to SAP Fiori Launchpad | Open the SAP Fiori launchpad as a Warehouse Clerk (EWM). | The SAP Fiori launchpad is displayed. |  |
| 2. | Access the App | Open the SAP Fiori Create Product Warehouse Tasks (/SCWM/MONNAV_CR_P_WT) app. | The Create Product Warehouse Tasks (/SCWM/MONNAV_CR_P_WT) screen displays. |  |
| 3. | Decide your Filter Criteria | Enter Storage Type: For example, S970.Choose Execute. | The Create Product Warehouse Task screen displays. |  |
| 4. | Choose your Stock | Choose one of the stock lines (for product QM001) and select More Methods > Create Warehouse Task. | The Create Warehouse Task dialog box (that requests for data) is displayed. |  |
| 5. | Create Warehouse Task | Create the warehouse task and enter the following data:Src Trgt Qty AUoM (Quantity): For example,8 PCDestination Bin and Destination Storage Type are filled automatically.Warehouse Process Type: for example, S997 - Putaway from Clarification.Choose Create WT. | The warehouse task is created, as you can see in the display log. A warehouse task List is automatically printed in the background.You must find the open product warehouse task in the monitor node warehouse task. Therefore, note down the warehouse task number. |  |
| 6. | Complete the Step | Note down the warehouse task number.Choose Continue to close the log and then choose Home or repeat the steps, if necessary. |  |  |

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

A putaway list is printed and handed over to the warehouse operative. He or she performs the warehouse tasks and confirms them in the system. Please note that the Warehouse Clerk can also confirm warehouse tasks using the app Warehouse Monitor (/SCWM/MON) (Business Catalog WM - Monitoring).

Procedure

Refer to the process step Confirm Warehouse Tasks in Scope Item Warehouse Inbound Processing (3BR).

In the test script, go to Test Procedures > Confirm Warehouse Tasks > Variant 1: with Fiori App.

You can find the document here [3BR](https://me.sap.com/processnavigator/SolS/EARL_SolS-013/2402/SolP/3BR?region=DE).

##### Variant 2: With Radio Frequency Device

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Operative (EWM) performs the warehouse tasks and confirms them in the system with mobile radio frequency device.

To work with radio frequency framework, make sure all the steps as described in the setup instruction guide for scope item 63X - Mobile RF Devices in Warehousing with Quality Management have been performed.

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/ae167716e1c4d285f608c211dd2d0cab)

Procedure

Refer to the process step Confirm Warehouse Tasks in scope item Warehouse Inbound Processing (3BR).

In the test script, go to Test Procedures > Confirm Warehouse Tasks > Variant 2: with Radio Frequency Device .

You can find the document here [3BR](https://me.sap.com/processnavigator/SolS/EARL_SolS-013/2402/SolP/3BR?region=DE).

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

Please see chapter 2.4 Business Conditions.

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| Accounts Receivable (J59) | Post the incoming payment.Using the master data from this document, complete the following activities described in the test script:Accounts Receivable(J59) (Section Post Incoming Payments) |
| Accounts Payable (J60) | Outgoing Payment |
| Return to Supplier (BMK) (optional) | Dispose of the inventory by returning to the vendor. Do not process any other activities in this document after running the external process.Using the master data from this document, complete the following activities described in the test script: Return to Supplier (BMK) |
| Warehouse Ad Hoc Goods Issue (3BT) | Material can be scrapped.Using the master data from this document, you can initiate the scrapping process by creating a posting change and a warehouse task to move the material to be scrapped from the source bin to the scrapping zone. After the physical goods movement is completed, you post the unplanned goods issue as described in the test script: Warehouse Ad Hoc Goods Issue (3BT) |
| Rework Processing - Stock-Manufactured Material (BJN) (optional) | Rework activities and material postings after production execution for the original material (including goods receipt of the product) with an additional rework production order.Using the master data from this document, complete the following activities described in the test script: Rework Processing - Stock-Manufactured Material (BJN) |
| Sales Order Fulfillment Monitoring (BKK) (optional) | Collection of periodic activities such as day ending activities.Using the master data from this document, complete the following activities described in the test script:Sales Order Fulfillment Monitoring(BKK) (Sections on Review Sales Documents blocked for billing, Review Billing Due List, Review Log of collective invoice creation and Review List Blocked (for accounting) Billing Documents) |
| Direct Procurement with Inbound Delivery (2TX) | After completing the steps of this scope item, an Supplier Invoice can be created as part of process Direct Procurement with Inbound Delivery (2TX). |

## Attachment Handling

In the SAP S/4HANA Cloud Public Edition, attachment service is a reusable user interface component which can be consumed by any FIORI application to attach documents. File attachments enable all kinds of media files being connected to business documents as additional information. For example, photos, videos, or documentation in form of plain text documents.

Use cases of the attachment service in the Cloud WM are the following, just to name a few:

- Inbound Process - Non-Acceptance of Delivery and Proof of SLA Violation
- Outbound Process - Visual Documentation of Complete and Error-free Packaging
- Outbound Process - Visual Documentation of Loading Security, Compliance to Regulations, SLAs

Attachment Service is an optional support feature for Cloud WM business objects. Attachments can be handled any time after the creation of an Cloud WM business object and any time before the end of the document’s lifecycle.

In this process you can use the following Fiori Apps to create, read, update or delete the following attachments:

- Warehouse Monitor for Inbound Deliveries or Handling Units respectively under nodes:
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
> Flagged while digesting this document, not verified: Warehouse number in RF steps differs: production-flow RF steps use Whse No 1750, supplier-flow RF steps use 3350, and the sample data lists EWM warehouse 3350 (ERP warehouse 335).

> [!warning] Conflict
> Flagged while digesting this document, not verified: Storage location differs: sample data and business conditions use 335W, but the synchronous goods receipt (MIGO) steps tell the tester to check storage location 105W (and optional 105I).

> [!warning] Conflict
> Flagged while digesting this document, not verified: Production-flow handling unit steps refer to materials SG124 and FG228, while the sample data table lists SG29 for the production flow and the supplier flow uses TG21 although sample data lists QM001.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[11-inventory-warehouse-and-transportation/test-script-warehouse-internal-inspections-5ok-ae-sap-s-4hana-cloud-pu]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3M0_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 106,917 chars in the whole document
