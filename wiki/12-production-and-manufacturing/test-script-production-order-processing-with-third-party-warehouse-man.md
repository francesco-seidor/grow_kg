---
id: 12-production-and-manufacturing/test-script-production-order-processing-with-third-party-warehouse-man
title: "Test Script: Production Order Processing with Third-Party Warehouse Management (2RU_AE) (2RU_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 2RU_AE: production/process order processing with a third-party WMS, with prerequisites and test steps."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/third-party-wms-production]
aliases: [2RU_S4CLD2608_BPD_EN_AE]
keywords: [Production with Third-Party Warehouse Management, production order processing, third-party warehouse management, material staging, process order processing, automatic backflush, production order confirmation, business roles, master data, initial material stock]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2RU_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-856
topic: 12-production-and-manufacturing/third-party-wms-production
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Production Order Processing with Third-Party Warehouse Management (2RU_AE) (2RU_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2RU_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Production with Third-Party Warehouse Management** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Production Order Processing with Third-Party Warehouse Management (2RU_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232849860)

[2 Prerequisites 4](#_Toc232849861)

[2.1 System Access 4](#_Toc232849862)

[2.2 Roles 4](#_Toc232849863)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232849864)

[2.4 Additional Manual Configuration 7](#_Toc232849865)

[2.5 Business Conditions 7](#_Toc232849866)

[2.6 Initial Material Stock 7](#_Toc232849867)

[2.7 Material Storage Location View Extension 9](#_Toc232849868)

[3 Overview Table 10](#_Toc232849869)

[4 Test Procedures 12](#_Toc232849870)

[4.1 Production Order Processing for Semifinished Product without Automatic Backflush of Components – and All Storage Locations Managed by 3rd Party WMS 12](#_Toc232849871)

[4.1.1 Create and Release Production Order 12](#_Toc232849872)

[4.1.2 Material Staging 13](#_Toc232849873)

[4.1.3 Check Web Services Message and Execute on Delivery in WMS 14](#_Toc232849874)

[4.1.4 Pick Components for Production 15](#_Toc232849875)

[4.1.5 Confirm Production Order for Semifinished Product 16](#_Toc232849876)

[4.1.6 Post Goods Receipt for Production Order (Optional) 17](#_Toc232849877)

[4.1.7 Check Web Services Message and Execute on Delivery in WMS 18](#_Toc232849878)

[4.1.8 Check Stock Information 19](#_Toc232849879)

[4.2 Production Order Processing for Semifinished Product with Automatic Backflush of Components – and Production Storage Location is Managed Centrally 20](#_Toc232849880)

[4.2.1 Create and Release Production Order 20](#_Toc232849881)

[4.2.2 Material Staging 21](#_Toc232849882)

[4.2.3 Check Web Services Message and Execute on Delivery in WMS 22](#_Toc232849883)

[4.2.4 Confirm Production Order for Semifinished Product 23](#_Toc232849884)

[4.2.5 Check Web Services Message and Execute on Delivery in WMS 24](#_Toc232849885)

[4.2.6 Check Stock Information 25](#_Toc232849886)

[4.3 Process Order Processing for Semifinished Product without Automatic Backflush of Components – and All Storage Locations Managed by 3rd Party WMS 26](#_Toc232849887)

[4.3.1 Create Process Order 26](#_Toc232849888)

[4.3.2 Pick Components for Process Order 27](#_Toc232849889)

[4.3.3 Check Web Services Message and Execute on Delivery in WMS 29](#_Toc232849890)

[4.3.4 Confirm Process Order for Semifinished Product 29](#_Toc232849891)

[4.3.5 Posting Goods Receipt for Process Order 30](#_Toc232849892)

[4.3.6 Check Web Services Message and Execute on Delivery in WMS 31](#_Toc232849893)

[4.3.7 Check Stock Information 32](#_Toc232849894)

[5 Appendix 34](#_Toc232849895)

[5.1 Process Integration 34](#_Toc232849896)

[5.1.1 Succeeding Processes 34](#_Toc232849897)

[5.2 SAP Application Interface Framework 34](#_Toc232849898)

## Purpose

Overview

The scope item covers production processes. The business part of the processes, including creation and confirmation of production or process orders, is performed in the SAP S/4HANA Cloud Public Edition system. The decentralized third-party warehouse management system runs processes required for the physical and logical goods movements. The two variants of the process include material staging to ensure that all needed components or raw materials are available for production, and the goods receipt of the finished goods after production confirmation. The first variant is without automatic backflush of the components and with the assumption that all involved storage locations are managed by third-party warehouse management solution. The other variant works with automatic backflush and the assumption of a centrally managed production storage.

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
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |
| Production Supervisor - Process Manufacturing | SAP_BR_PRODN_SUPERVISOR_PROC | Production Management - Process Manufacturing | SAP_BR_PRODN_SUPERVISOR_PROC |  |
| Production Operator - Process Manufacturing | SAP_BR_PRODN_OPTR_PROC | Production Execution - Process Manufacturing | SAP_BR_PRODN_OPTR_PROC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure. If you have installed an SAP Best Practices baseline package, you can use the following baseline package sample data:

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Material | SG224 | SEMI224,MTO,PD,Subassembly |  |
| Material | RM124 | RAW124,VB,Consumption,FixedBin |  |
| Material | FG228 | FIN228, MTO, PD, FifoProduction material with batch |  |
| Material | RM122 | RAW122,PD,Batch-Fifo,ProcureImportProduction material with batch |  |
| Material | SG24 | SEMI24,PD,Batch-FifoSemifinished Product PI, batch managed |  |
| Material | RM09 | RAW09,PD,Batch-FifoRaw material, batch-managed, external procured |  |
| Material | RM19 | RAW19,PD,Batch-Fifo,LeanQMRaw material, batch-managed, external procured |  |
| Material | RM30 | RAW30,VB,Batch-FifoRaw material, batch-managed, external procured |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Storage Location | 331B | Std. storage 2Production Storage location |  |
| Storage Location (WMS) | 331I | 3rd party WMStorage location for raw-material + finished goods (managed by decentralized WMS) |  |
| Storage Location (WMS) | 331J | 3rd party WMS-ProductionProduction Storage location (managed by decentralized WMS) |  |
| Shipping Point | 3310 | Shipping Point 3310 |  |
| Sales Organization | 3310 | Shipping Point 3310 |  |
| Distribution Channel | 33 | 33 |  |
| Division | 00 | Product Division 00 |  |

Bill of Material Structure

This overview shows the bill of material structure and the usage of each component if you have activated all optional enhancements.

| Material | Level | Material Type | Unit | Characteristic of Material | Optional Enhancements |
| --- | --- | --- | --- | --- | --- |
| FG226 | 0 | FERT | PC | Finished Good for MT0 processing with batch and serial number processing | Batch processing for Finished Good optionally |
| SG224 | 1 | SEMI | PC | Internal production of subassembly (MTO strategy) |  |
| RM124 | 2 | RAW | PC | External procured using Fixed Bin |  |
| RM122 | 1 | RAW | PC | External procured with Batch Management (FIFO-Strategy) | Initial Stock Posting |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNR | Create Product Master of type "Raw Material" - MDS |
| BNS | Create Product Master of type "Semi-Finished Good" - MDS |
| BNT | Create Product Master of type "Finished Good" - MDS |
| BND | Create Customer Master - MDS |
| BNE | Create Supplier Master - MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/5b82b02ebb1b11ac0312250f55944cfe)

### Business Conditions

Before this scope item can be tested, the following business condition must be met.

| Scope Item | Business Condition |
| --- | --- |
| BNU - Create Costing Run - MDS | You have completed the steps described in BNU master data script (Product Costing section). |
| 1ZQ - Logistics with Third-Party Warehouse Management | Prerequisite |
| BLF - Batch Management | Prerequisite (only if batch managed materials are used) |

### Initial Material Stock

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

|  |
| --- |
| Note Material master data must be extended to store location views. Refer to the master data script [Master Data, Organizational Data, and Other Data](#unique_5) [page ] 5. |

To create batch for batch material, refer to scope item BLF Batch Management.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad using the role Inventory Manager. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Manage Stock (F1062). | The Manage Stock screen is displayed. |  |
| 3 | Input Material | Make the following entries and select them from the right drop-down list:Material: <material>, for example, RM124Plant: 3310(Optional) Batch: batch number (for batch material only, for example RM122). | The stock overview for the material is displayed. |  |
| 4 | Select Stock | Select the icon beside the stock that you want to add initial stock, for example:Storage Location:331B / 331IUnrestricted-Use Stock | A dialog box is opened. The Storage Location, Stock Type, and Current Quantity are displayed according to your entries in the previous steps. |  |
| 5 | Add Initial Entry | Make the following entries and choose Post:Document Date: <today>Posting Date: <today>Stock Change: Initial EntryQuantity: <enter a number> | The system displays the following message. The stock has been added.1 document has been created: Material Document XXXXXXXXXX/20XX |  |

### Material Storage Location View Extension

Purpose

This process step shows you how to ensure the third-party WMS managed storage location views are extended for all relevant materials.

Procedure

1. Check if Storage Location: 331I or 331J views are already extended referring to section [Master Data, Organizational Data, and Other Data](#unique_5) [page ] 5.
2. If not, log on to SAP Fiori launchpad to extend views for the relevant materials.

## Overview Table

The scope item Production Order Processing with Third-Party Warehouse Management consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction / APPs | Expected Results |
| --- | --- | --- | --- |
| Production Order Processing for Semifinished Product without Automatic Backflush of Components - and All Storage Locations Managed by 3rd Party WMS |  |  |  |
| [Create and Release Production Order](#unique_11) [page ] 12 | Production Supervisor - Discrete Manufacturing | Create Production Order (CO01) |  |
| [Material Staging](#unique_12) [page ] 13 | Production Operator - Discrete Manufacturing | Stage Materials for Production (MF60) |  |
| [Check Web Services Message and Execute on Delivery in WMS](#unique_13) [page ] 14 | External System | Pick components and provide them to production supply area and send confirmation back |  |
| [Pick Components for Production](#unique_14) [page ] 15 | Production Operator - Discrete Manufacturing | Pick Components for Production Orders (CO27) |  |
| [Confirm Production Order for Semifinished Product](#unique_15) [page ] 16 | Production Operator - Discrete Manufacturing | Confirm Production Order Operation (CO11N). | The Enter Time Ticket for Production Order screen is displayed. |
| [Post Goods Receipt for Production Order (Optional)](#unique_16) [page ] 17 | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843) |  |
| [Check Web Services Message and Execute on Delivery in WMS](#unique_17) [page ] 18 | External System | Post Goods Receipt of finished goods and send confirmation back |  |
| Production Order Processing for Semifinished Product with Automatic Backflush of Components - and Production Storage Location is Managed Centrally |  |  |  |
| [Create and Release Production Order](#unique_18) [page ] 20 | Production Supervisor - Discrete Manufacturing | Create Production Order (CO01) | The Monitor Material Coverage Net and Individual Segments screen is displayed. |
| [Material Staging](#unique_19) [page ] 21 | Production Operator - Discrete Manufacturing | Stage Materials for Production (MF60) |  |
| [Check Web Services Message and Execute on Delivery in WMS](#unique_20) [page ] 22 | External System | Provide components for production supply area and send back confirmation |  |
| [Confirm Production Order for Semifinished Product](#unique_21) [page ] 23 | Production Operator - Discrete Manufacturing | Confirm Production Order Operation (CO11N). | The Enter Time Ticket for Production Order screen is displayed. |
| [Check Web Services Message and Execute on Delivery in WMS](#unique_22) [page ] 24 | External System | Post Goods Receipt for finished goods and send back confirmation |  |
| Process Order Processing for Semifinished Product without Automatic Backflush of Components – and All Storage Locations Managed by 3rd Party WMS |  |  |  |
| [Create Process Order](#unique_23) [page ] 26 | Production Supervisor - Process Manufacturing | Create Process Order (COR1) |  |
| [Pick Components for Process Order](#unique_24) [page ] 27 | Production Supervisor - Process Manufacturing | Pick Components for Process Orders (COIK) |  |
| [Check Web Services Message and Execute on Delivery in WMS](#unique_25) [page ] 29 | External System | Provide components for production supply area and send back confirmation |  |
| [Confirm Process Order for Semifinished Product](#unique_26) [page ] 29 | Production Supervisor - Process Manufacturing | Confirm Process Order Phase (COR6N). |  |
| [Posting Goods Receipt for Process Order](#unique_27) [page ] 30 | Warehouse Clerk | Post Goods Movement (MIGO) |  |
| [Check Web Services Message and Execute on Delivery in WMS](#unique_28) [page ] 31 | External System | Post Goods Receipt for semi-finished goods and send back confirmation |  |
| [Check Stock Information](#unique_29) [page ] 32 | Warehouse Clerk | Display Warehouse Stock - Deprecated (MB52) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Production Order Processing for Semifinished Product without Automatic Backflush of Components – and All Storage Locations Managed by 3rd Party WMS

#### Create and Release Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This scope item is focusing on the integration part of the process. It starts with the creation of a production order.

Prerequisite

The inventory needs to be checked before creating the production order to make sure, that not enough stock is available for the raw material or component in storage location 331J (which is the production storage location). If there is enough stock, no material staging is needed – and with that also no stock transfer/delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as a Production Supervisor - Discrete Manufacturing (PRODN_SUPERVISOR_DISC). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Create Production Order (CO01). | The Production Order Create: Initial Screen is displayed. |  |
| 3 | Select Initial Values | Enter the following entries:Material : SG224Production Plant : 3310Order Type: YBM1Choose Continue. | The Production order Create: Header screen is displayed. |  |
| 4 | Maintain Header Values | Choose General > Quantities > Total Qty , enter 10.Scroll down to the Scheduling section, in the Type field, select Current date.Choose tab Goods Receipt (On the system message window, choose Continue), in the Receipt > Stor. Loc. field, enter 331I.Select Tab Components, for component RM124, deselect the flag for Backflush and change the storage location to 331J.Caution Make sure you have unchecked Backflush and change the storage location to 331J before saving the production order.Choose Release Order tab at the top menu, on the Release Order screen, choose Release Order button. | Message：Order has missing parts (see log) (=> This message is wanted to allow material staging.)The Release Order screen is displayed.Message: Release carried out(Please check log) |  |
| 5 | Save Order | Choose Save. | Message: Order number xxx saved. |  |

#### Material Staging

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Ensure that enough stock of the raw material and all components is available in the production area.

|  |
| --- |
| Note Ensure that enough stock is available in the storage location where the raw materials are located.But for demo purposes, there is no stock of the raw material RM124 in the production storage location (331B and 331J). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori launchpad as a Production Operator - Discrete Manufacturing (PRODN_OPTR_DISC). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Stage Materials for Production (MF60). | The Material Staging for Planned Orders screen is displayed. |  |
| 3 | Enter Order Information | On the Material Staging for Planned Orders screen, make the following entries:Plant: 3310Selection Horizon for Reqmts: <today + 3 days>Choose tab Production/Process Orders, in the Production Orders/Process Orders section, enter the following:Order: <Production Order Number you noted>Choose Execute. |  |  |
| 4 | Check the Pull List | Select the entry and choose Replenishment Proposals. | The Pull List: Storage Location Level screen is displayed.One line with the chosen raw material or component should be displayed because there is not enough stock for this material available in 331J which is the storage location for the production.The field Quantity staged is filled. |  |
| 5 |  | Mark the line, choose tab Replenishment Elements, and make the following entries:RepLoc: 331I.(Optional) Batch: batch number(for batch material only)Mark the line, and then choose Stage and Save. | A new grid is opened at the bottom of the screen.In the current release, no message is displayed when using storage locations that are managed by 3rd Party. |  |

#### Check Web Services Message and Execute on Delivery in WMS

|  |
| --- |
| Note Steps described in this chapter need to be processed in a 3rd-party WMS system. |

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Pick the needed components for the production and provide them to the production supply area.

Send confirmation back.

|  |
| --- |
| Note Check the corresponding configuration and receiving message in your 3rd-party WMS to get the required business data for completing all the necessary operational processes in the 3rd-party system. |

#### Pick Components for Production

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The components need to be picked to be ready for production.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as a Production Operator - Discrete Manufacturing (PRODN_OPTR_DISC). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Pick Components for Production Orders (CO27). | The Picking List: Initial Screen is displayed. |  |
| 3 | Enter Order Information | In the field Production Order, enter the order number, and choose Execute. | The Order Information System: Detail List of Components screen is displayed. |  |
| 4 | Perform Picking | Mark the row with RM124, and choose Picking.Enter a quantity and mark the row with RM124.Choose Post. | The Picking List screen is displayed. |  |

#### Confirm Production Order for Semifinished Product

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The confirmation documents the processing status of orders, operations, sub-operations. It is an instrument for controlling orders. Here you have to confirm the operations of the production order for the production material. When you confirm the last operation, the system generates a goods movement document for the production material. The backflush is carried out together with the confirmation steps. Via the confirmation, the goods receipt for the production material will also be executed automatically.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as a Production Operator - Discrete Manufacturing (PRODN_OPTR_DISC). | The SAP Fiori Launchpad is displayed. |  |
| 2. | Access the App | Open Confirm Production Order Operation (CO11N). | The Enter Time Ticket for Production Order screen is displayed. |  |
| 3. | Enter Time Ticket for Production Order | On the Enter Time Ticket for Production Order screen, make the following entries:Order: <Production Order Number you noted>Operation: for example, <operation 0010>Confirm.type: select Final Confirmation.Press Enter to show related information of the production order. |  |  |
| 4. | Fill Yield Field and To Confirm-Labor Field | Ensure that you have pressed Enter before this step.In the Quantities > Yield field, enter the amount you want to confirm.Go to the Activities section, in the To Be Confirmed and Unit fields, for Setup, enter a value (for example, <10> and <Unit of Hour(H)>) for the labor time and confirm with Enter. |  |  |
| 5. | Choose Goods Movements | Choose Goods Movements screen. | For operation number 0010, no goods movement are displayed because the components are already picked for production.For operation number 0020, the goods receipt of the finished goods is triggered. |  |
| 6. | Save Your Entries | Choose Post to save. | Confirmation saved. |  |
| 7. | Repeat Steps | Repeat steps 3 to 6 for all remaining operations and save your entries. |  |  |

#### Post Goods Receipt for Production Order (Optional)

|  |
| --- |
| Note Steps described in this chapter might be required for finished goods FG228. |

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to post the goods receipt for the production order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori launchpad | Log on to the SAP Fiori launchpad as Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Post Goods Receipt for Production Order (F3110). | The Post Goods Receipt for Production Order screen displays. |  |
| 3 | Enter Details | On the Post Goods Receipt for Production Order screen, make the following entries and press Enter:Production Order: <Production Order Number> (From previous step) | Presettings might be changed by other processes. Check if the value in the Action field is Goods Receipt and the value in the Reference field should be Order. If not, maintain the same. |  |
| 4 | Check | In the Items section, select the item. |  |  |
| 5 | Post | Choose Post. | Goods receipt for production order has been done. |  |

#### Check Web Services Message and Execute on Delivery in WMS

|  |
| --- |
| Note Steps described in this chapter need to be processed in a 3rd-party WMS system. |

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Post goods receipt of finished goods and send confirmation back.

|  |
| --- |
| Note Check the corresponding configuration and receiving message in your 3rd-party WMS to get the required business data for completing all the necessary operational processes in the 3rd-party system. |

#### Check Stock Information

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this section the updated stock information is checked.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Display Warehouse Stock - Deprecated (MB52). | The Display Warehouse Stocks of Material screen displays. |  |
| 3 | Enter material | Make the following entries:Material: <Material number>Plant :<Plant>Storage Location: <Storage Location>Press Enter. | The Display Warehouse Stocks of Material shows. |  |
| 4 | Check stock | Check if the stock information is now updated and the decreased stock of the 3rd party WMS managed storage location is displayed |  |  |

### Production Order Processing for Semifinished Product with Automatic Backflush of Components – and Production Storage Location is Managed Centrally

#### Create and Release Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This scope item is focusing on the integration part of the process. It starts with the creation of a production order.

Prerequisite

The inventory needs to be checked before creating the production order to make sure, that not enough stock is available for the raw material or component in storage location 331B (which is the production storage location). If there is enough stock, no material staging is needed – and with that also no stock transfer/delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing (PRODN_SUPERVISOR_DISC). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Create Production Order (CO01). | The Production Order Create: Initial Screen is displayed. |  |
| 3 | Select Initial Values | Enter the following entries:Material: SG224Production Plant: 3310Order Type: YBM1Choose Continue. | The Production order Create: Header screen is displayed. |  |
| 4 | Maintain Header Values | Choose General > Quantities > Total Qty , enter 10.Scroll down to the Scheduling section, in the Type field, select Current date.Choose tab Goods Receipt (In the system message dialog, choose Continue). In the Receipt > Stor.Location field, enter 331I.Choose Components, for component RM124, select the flag for Backflush. Ensure a centrally managed Storage Location, such as 331B is used here.Choose Release Order tab at the top menu, on the Release Order screen, choose Release Order button. | Message：Order has missing parts (see log) (=> This message is needed to allow material staging.)The Release Order screen is displayed.Message: Release carried out(Please check log) |  |
| 5 | Save Order | Choose Save. | Message: Order number xxx saved. |  |

#### Material Staging

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Ensure that enough stock is available of the raw material and all components in production area.

|  |
| --- |
| Note Ensure that enough stock is available in the storage location where the raw materials are located.But for demo purpose, no stock of the raw material RM124 in the production storage location (331B and 331J). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as a Production Operator - Discrete Manufacturing (PRODN_OPTR_DISC). | The SAP Fiori Launchpad is displayed. |  |
| 2. | Access the App | Open Stage Materials for Production (MF60). | The Material Staging for Planned Orders screen is displayed. |  |
| 3. | Enter Order Information | On the Material Staging for Planned Orders screen, make the following entries:Plant: 3310Selection Horizon for Reqmts: <today + 3 days>Choose Tab Production/Process Orders, in the Production Orders/Process Orders section, enter the following:Order: <Production Order Number you noted>.Choose Execute. |  |  |
| 4. | Check the Pull List | Check the entry and choose Replenishment Proposals. | The Pull List: Storage Location Level screen is displayed.One line with RM124 should appear because there is not enough stock for this material available in 331B which is the storage location for the production.The field Quantity staged is filled. |  |
| 5. |  | Mark the line, then choose tab Replenishment Elements and make the following entry:RepLoc: 331IMark the line, then choose Stage and Save. | A new grid is opened at the bottom of the screen.In the current release, no message is displayed when using storage locations that are managed by 3rd Party.Outbound Delivery is created. |  |

#### Check Web Services Message and Execute on Delivery in WMS

|  |
| --- |
| Note Steps described in this chapter need to be processed in a 3rd-party WMS system. |

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

Provide components for production supply area and send back confirmation.

|  |
| --- |
| Note Check the corresponding configuration and receiving message in your 3rd-party WMS to get the required business data for completing all the necessary operational processes in the 3rd-party system. |

#### Confirm Production Order for Semifinished Product

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The confirmation documents the processing status of orders, operations, sub-operations. It is an instrument for controlling orders. Here you have to confirm the operations of the production order for semi-finished material SF Subassembly SG224. When you confirm the last operation, the system generates a goods movement document for SF Subassembly SG224. The backflush is carried out together with the confirmation steps. Via the confirmation, the goods receipt for semifinished material SG224 will also be executed automatically.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as a Production Operator - Discrete Manufacturing (PRODN_OPTR_DISC). | The SAP Fiori Launchpad is displayed. |  |
| 2. | Access the App | Open Confirm Production Order Operation (CO11N). | The Enter Time Ticket for Production Order screen is displayed. |  |
| 3. | Enter Time Ticket for Production Order | On the Enter Time Ticket for Production Order screen, make the following entries:Order: <Production Order Number you noted>Operation: for example, <operation 0010>Confirm.type: select Final Confirmation.Press Enter to show related information of the production order. |  |  |
| 4. | Fill Yield Field and To Confirm-Labor Field | Ensure that you have pressed Enter before this step.In the Quantities > Yield field, enter the amount you want to confirm.Go to the Activities section, in the To Be Confirmed and Unit fields, for Setup, enter a value (for example, <10> and <Unit of Hour(H)>) for the labor time and confirm with Enter. |  |  |
| 5. | Choose Goods Movements | Choose Goods Movements screen. | The system shows you an overview table of all materials for which the withdrawing is done automatically with the confirmation of the operation.For operation number 0010, the material RM124 is set for backflush (in material master) so that the withdrawing is done automatically after you confirm the operation.For operation number 0020, goods receipt for the finished good SG224 is automatically created. |  |
| 6. | Save Your Entries | Choose Post to save. | Confirmation saved. |  |
| 7. | Repeat Steps | Repeat steps 3 to 6 for operation number 0020 and save your entries. |  |  |

#### Check Web Services Message and Execute on Delivery in WMS

|  |
| --- |
| Note Steps described in this chapter need to be processed in a 3rd-party WMS system. |

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Post Goods Receipt for finished goods and send back confirmation.

|  |
| --- |
| Note Check the corresponding configuration and receiving message in your 3rd-party WMS to get the required business data for completing all the necessary operational processes in the 3rd-party system. |

#### Check Stock Information

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this section the updated stock information is checked.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Display Warehouse Stock - Deprecated (MB52). | The Display Warehouse Stocks of Material screen displays. |  |
| 3 | Enter material | Make the following entries:Material: <Material number>Plant :<Plant>Storage Location: <Storage Location>Press Enter. | The Display Warehouse Stocks of Material shows. |  |
| 4 | Check stock | Check if the stock information is now updated and the decreased stock of the 3rd party WMS managed storage location is displayed |  |  |

### Process Order Processing for Semifinished Product without Automatic Backflush of Components – and All Storage Locations Managed by 3rd Party WMS

#### Create Process Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create process order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Process Order (COR1). |  |  |
| 3 | Enter Parameters | Make the following entries and choose Continue:Material Number: SG24Production Plant: 3310Process Order Type: YBM2 |  |  |
| 4 | Enter General Data | On the General Data tab, make the following entries:Total Qty: <Total Qty>Scheduling - Type: Current date |  |  |
| 5 | Enter Goods Receipt Data | On the Goods Receipt tab, make the following entries:Receipt - Stor. Loc.: 331I |  |  |
| 6 | Choose Material List | Choose Material List on the upper part of the screen. | The Create Process Order: Material List screen displays. |  |
| 7 | Change the Storage Location of Material | For each material, change the storage location to one managed by 3rd Party WMS, for example, 331I.Note Manually changing storage locations to the 3rd-Party WMS managed one for materials is required here only for demo purposes. You can skip this manual step by maintaining default production storage location (Prod. stor. location) for your own material. |  |  |
| 8 | Save | Choose Save.Make a note of this Process Order number: __________. | Process Order is saved.Note In this scenario, process order is configured as automatically released. |  |

#### Pick Components for Process Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The released process order is now ready for picking. All materials that are moved to the production storage location can be issued to the process order using the pick list.

|  |
| --- |
| Note Ensure that enough stock is available in the storage location where the materials are located. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Production Operator - Process Manufacturing. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Pick Components for Process Orders (COIK). | The Picking List: Initial screen displays. |  |
| 3 | Enter Restriction and Execute | Make the following entries and then choose Execute.Profile: 000002Process Order: XXXX (from previous steps)Plant: 3310 | The Order Information System: Detail List of Components screen displays. |  |
| 4 | Picking Raw Materials | Select the relevant reservation and choose Picking.Note If you have changed the storage location of all your components to a 3rd-party WMS managed storage location, you can multi-select all the components. In this case, movement of all components will be recorded in one outbound delivery. | The Picking list screen displays. On this screen, a list of all the selected reservation is displayed. |  |
| 5 | Perform Batch Determination | Select the component you want to pick and choose Batch Determination. | The Batch Determination MM: Select Batches screen displays.If the system shows the message Batch determination was carried out without selection specification , ignore it.If during batch determination only part of the required quantity is found to be available, the unconfirmed quantity remains as an open line item within the picking list. You should then delete the line item from the picking list before saving, as this line item cannot be posted. |  |
| 6 | Copy Batch Determination Result | Choose Copy. Repeat this step for all the components. | The Picking list screen displays. And batch numbers have been determined. |  |
| 7 | Post Goods Movements | Choose Post. | In the current release, no message is displayed when using storage locations that are managed by 3rd Party.Outbound Delivery will be created for components that have 3rd-party WMS managed storage location. |  |

#### Check Web Services Message and Execute on Delivery in WMS

|  |
| --- |
| Note Steps described in this chapter need to be processed in a 3rd-party WMS system. |

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Check whether the Web Services message successfully reaches your third-party WMS. Pick the needed components for the process order and provide them to the production supply area.

Send confirmation back.

|  |
| --- |
| Note Check the corresponding configuration and receiving message in your 3rd-party WMS to get the required business data for completing all the necessary operational processes in the 3rd-party system. |

#### Confirm Process Order for Semifinished Product

Purpose

The confirmation documents include the processing status of orders, operations, phases, and individual capacities. It's an instrument to control the order. The time ticket confirmation allows recording either the default times for machine and labor usage, or record actual times for major deviations. You can post scrap quantities as an optional. If no major deviations occurred, only the last phase (milestone) must be confirmed. Using milestone confirmation, all prior phases are confirmed automatically.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Production Operator - Process Manufacturing. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Confirm Process Order Phase (COR6N). | The Enter Time Ticket for Process Order screen displays. |  |
| 3 | Enter Confirmation Option | Make the following entries and then choose Enter.Order: XXXX (from previous steps)Choose Enter or select phase (0040) from search help of Phase field.Confirm.type: Final confirmationClear open reservations: X | If the system shows the message Total quantity confirmed not equal to planned quantity to be confirmed, press Enter to ignore it. |  |
| 4 | Propose Actual Data | Choose Actual Data.Make the changes for the following fields:Scrap: <enter the amount you want to Scrap>Yield: <Based on the origin quantities minus Scrap>Reason for Var: Enter scarp reason if need. For example, 0001 | The Quantities and Activities will be filed automatically. |  |
| 5 | Save Confirmation | Save your entries. | The final confirmation of the last operation is carried out. Costs and activity quantities are recalculated in proportion to the yield quantity. |  |

#### Posting Goods Receipt for Process Order

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
| 3 | Enter Process Order | Make the following entries and then choose Enter.Action: Goods ReceiptReference: OrderOrder number: XXXX (From previous steps)Movement Type: 101 | Screen name adapts after entries are made. |  |
| 4 | Enter Date of Manufacture | Choose the Batch tab, then make the following entries:Date of Manufacture: Current Date | Note This step is only available for SAP delivered standard content as some customizing changes in SSCUI could make things different.Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |  |
| 5 | Check Item | Select item OK. | Ensure that detail data is expanded. |  |
| 6 | Post Goods Movement | Choose Post. | The batch number is created automatically during the posting. Production date and shelf-life expiration date are recorded within the batch master of the finished product. |  |

#### Check Web Services Message and Execute on Delivery in WMS

|  |
| --- |
| Note Steps described in this chapter need to be processed in a 3rd-party WMS system. |

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Check whether the Web Services message successfully reaches your third-party WMS. Post Goods Receipt for semi-finished goods and send back confirmation.

|  |
| --- |
| Note Check the corresponding configuration and receiving message in your 3rd-party WMS to get the required business data for completing all the necessary operational processes in the 3rd-party system. |

#### Check Stock Information

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this section the updated stock information is checked.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Display Warehouse Stock - Deprecated (MB52). | The Display Warehouse Stocks of Material screen displays. |  |
| 3 | Enter material | Make the following entries:Material: <Material number>Plant: <Plant>Storage Location: <Storage Location>Press Enter. | The Display Warehouse Stocks of Material shows. |  |
| 4 | Check stock | Check if the stock information is now updated. |  |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| 3F0 (Event-Based Production Cost Posting) | This procedure updates work-in-process calculation, overhead calculation, and variance calculation by linking the posting to the events.Note Starting from CE2105, the default Best Practice content is based on event-based result analysis for new customers to install and add new countries/regions only, rather than previous period-end posting. For existing customers (who activated content before 2105), the default remains unchanged to Period-End Closing – Plant (BEI) till customers decide to switch. For migration to event based from Periodic, refer to [Production Settlement in Parallel Ledgers](https://help.sap.com/viewer/4032610758dc437089f0c28320eec93f/LATEST/en-US/e49a3770f22547a392455154f3eef6e2.html). If you are still using period-end posting, you may need to refer to the non-standard Scope Item BEI - Period-End Closing – Plant. |

### SAP Application Interface Framework

Your system can exchange data messages with other systems, for example third-party Warehouse Management System, using various interface technologies. The Message Monitoring enables you to monitor these interfaces and their data messages, and execute error handling (if enabled) in a single framework.

For the features of AIF, please refer to the following links:

[https://help.sap.com/viewer/1cefaed5b7a3471cb08564e54d5ba866/3.0/en-US/d02c5cc67114450e848b74dfa6b11efb.html](https://help.sap.com/viewer/1cefaed5b7a3471cb08564e54d5ba866/3.0/en-US/d02c5cc67114450e848b74dfa6b11efb.html)

[https://help.sap.com/viewer/f544846954f24b9183eddadcc41bdc3b/1805.500/en-US/b0e61556c5317c65e10000000a44147b.html](https://help.sap.com/viewer/f544846954f24b9183eddadcc41bdc3b/1805.500/en-US/b0e61556c5317c65e10000000a44147b.html)

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
- related-to :: [[11-inventory-warehouse-and-transportation/test-script-logistics-with-third-party-warehouse-management-1zq-ae-793]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2RU_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 57,470 chars in the whole document
