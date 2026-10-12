---
id: 11-inventory-warehouse-and-transportation/sap-ewm-integration-delivery-based-production-integration-2vm-ae-test
title: "SAP EWM Integration – Delivery-Based Production Integration (2VM_AE) – Test Script, SAP S/4HANA Cloud Public Edition… (2VM_S4CLD2608_BPD_EN_AE)"
description: "Test script for scope item 2VM_AE: staging components from SAP EWM to production and receiving finished goods back into EWM via delivery-based integration."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/ewm-production-integration]
aliases: [2VM_S4CLD2608_BPD_EN_AE]
keywords: [EWM Production Supply and Receipt, delivery-based production integration, material staging, ewm outbound delivery order, warehouse tasks, goods issue, expected goods receipt, inbound delivery, goods receipt, putaway]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2VM_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-882
topic: 11-inventory-warehouse-and-transportation/ewm-production-integration
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# SAP EWM Integration – Delivery-Based Production Integration (2VM_AE) – Test Script, SAP S/4HANA Cloud Public Edition… (2VM_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2VM_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **EWM Production Supply and Receipt** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | SAP EWM Integration – Delivery-Based Production Integration (2VM_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232850891)

[2 Prerequisites 4](#_Toc232850892)

[2.1 Additional Manual Configuration 4](#_Toc232850893)

[2.2 System Access 4](#_Toc232850894)

[2.3 Roles 4](#_Toc232850895)

[2.4 Master Data, Organizational Data, and Other Data 5](#_Toc232850896)

[2.5 Business Conditions 7](#_Toc232850897)

[2.6 Preliminary Steps 7](#_Toc232850898)

[2.6.1 Create Control Cycle for WM 7](#_Toc232850899)

[2.6.2 Initial Stock Upload 8](#_Toc232850900)

[2.6.2.1 Data Files for Initial Stock Upload 8](#_Toc232850901)

[2.6.2.2 Adopt Business Partner ID in .csv Files When Deviating from Default Business Partner Number 8](#_Toc232850902)

[2.6.2.3 Upload Initial Stock 8](#_Toc232850903)

[3 Overview Table 11](#_Toc232850904)

[4 Test Procedures 13](#_Toc232850905)

[4.1 Anonymous Forecast and MRP 13](#_Toc232850906)

[4.1.1 Create Planned Independent Requirements 13](#_Toc232850907)

[4.1.2 Material Requirements Planning at Plant Level 14](#_Toc232850908)

[4.1.3 Evaluate Stock/Requirements Situation 15](#_Toc232850909)

[4.2 Convert Planned Order to Production Order 16](#_Toc232850910)

[4.3 Review Material Availability Status for Production Orders 18](#_Toc232850911)

[4.4 Release Production Order 19](#_Toc232850912)

[4.5 Material Staging for Production Order 21](#_Toc232850913)

[4.6 Display EWM Outbound Delivery Order in SAP EWM 23](#_Toc232850914)

[4.7 Create Warehouse Task for Staging in SAP EWM 24](#_Toc232850915)

[4.8 Confirm Warehouse Task for Staging in SAP EWM 26](#_Toc232850916)

[4.9 Post Goods Issue in SAP EWM 27](#_Toc232850917)

[4.10 Check Stock Situation 29](#_Toc232850918)

[4.11 Check Goods Movement for Outbound Delivery for Production Supply (Optional) 30](#_Toc232850919)

[4.12 Confirm Production Operations 31](#_Toc232850920)

[4.13 Generate Expected Goods Receipt Document 32](#_Toc232850921)

[4.14 Create Inbound Delivery with Reference to Expected Goods Receipt in SAP EWM 34](#_Toc232850922)

[4.15 Post Goods Receipt with Reference to Inbound Delivery in SAP EWM 36](#_Toc232850923)

[4.16 Check Material Document (Optional) 38](#_Toc232850924)

[4.17 Create Putaway Warehouse Task for Inbound Delivery 39](#_Toc232850925)

[4.18 Putaway of Products in SAP EWM 41](#_Toc232850926)

[4.19 Check Inbound Delivery (Optional) 42](#_Toc232850927)

[5 Appendix 44](#_Toc232850928)

[5.1 Generate Expected Goods Receipt Documents in SAP EWM 44](#_Toc232850929)

[5.2 Process Integration 45](#_Toc232850930)

[5.2.1 Succeeding Processes 45](#_Toc232850931)

## Purpose

Overview

In this scope item, you manage the staging and consumption of components from the warehouse to production and the receiving and storage of finished products from production into the warehouse. You trigger material staging that leads to the creation of an outbound delivery that is replicated to SAP Extended Warehouse Management (EWM).

The corresponding outbound delivery order (ODO) in SAP EWM serves as the main document for material staging. A warehouse clerk creates warehouse tasks for staging with reference to the ODO. The warehouse worker moves the goods to the production supply area and confirms the warehouse tasks. A goods issue is automatically posted by the system. The stock is transferred from the EWM-managed to the production storage location and is now available for consumption.

After the production process is finished, the generation of expected goods receipts (EGR) documents initiates the receiving of the finished goods from production into the warehouse.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/78be832e03dd6e53acaed719341361fa)

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
| Production Supervisor - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC | Production Management - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC |  |
| Production Operator - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC | Production Execution - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |
| Receiving Specialist | SAP_BR_RECEIVING_SPECIALIST | Receiving | SAP_BR_RECEIVING_SPECIALIST |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 333D | Decentral EWM received on dock |  |
| Storage Location | 333S | Decentral EWM available for sales |  |
| Warehouse | 333 | Decentral EWM-managed warehouse in SAP S/4HANA |  |
| Production Supply Area | PSA-I003 |  |  |
| Material | SG124 | Semifinished Good Subassembly |  |
| Material | RM124 | RAW Material Ext. Procurement Consumption based |  |
| Bill of Material | BoM for SG124, alternative BoM 3 | Alternative BoM number 3 | PSA value assigned to component RM124 in the BoM |

Organizational Master Data in the SAP EWM System:

| Org. Master Data | Value | Master Data Details | Comments |
| --- | --- | --- | --- |
| Supply Chain Unit | YWAREHOUSE-3330 |  |  |
| EWM Warehouse Number | 3330 |  |  |
| Custodian | 33413310 |  |  |
| Entitled to Dispose | 33413310 |  |  |
| Goods Receipt Office | PL1010 |  |  |

Warehouse-Specific Master Data:

| Org. Data | Value | Org. Data Details | Comments |
| --- | --- | --- | --- |
| Storage Type | Y001 | General Storage |  |
| Storage Type | Y002 | General Storage Picking Area |  |
| Storage Type | Y915 | Goods Receipt in Production |  |

| MDS | Description |
| --- | --- |
| BNR | Create Product Master of type "Raw Material" - MDS |
| BNS | Create Product Master of type "Semi-Finished Good" - MDS |
| BNK | Create Material BOM for Production and Sales - MDS |
| 3KS | Maintain Production Supply Area - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS master data script. Posting Period is up to date. |

### Preliminary Steps

#### Create Control Cycle for WM

Purpose

In this activity, you create a control cycle that can be used for in-house production in the Production Supply Area. In the control cycle, you define the demand source, the supply source, and the material staging indicator. The Material Staging Indicator defines the method of how needed materials can be supplied for production with the assistance of the warehouse management system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori launchpad | Log on to the SAP Fiori Launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Control Cycle for WM (LPK1). | The Create Control Cycle displays. |  |
| 3 | Enter the data | Make the following entries and choose Continue:Material: RM124Plant: 3310Supply Area: PSA-I003 | The Create Control Cycle: Data Screen (WM) screen displays. |  |
| 4 | Enter the Control Cycle Details | Make the following entries and choose Enter:Destination section:Staging Ind.: 3Source section:Stor. Location: 333SWarehouse No.: 333 | The Destination Stor. Location and Source Issuing Plant fields are automatically filled by the system.The Source Warehouse No. is not for input initially and will be automatically filled after entering the Source Storage Location. | Staging indicator 3 is used for Release Order Parts. If you use Pick Parts, use Staging Indicator 1. |
| 5 | Save | Choose Save | You have created control cycle for material RM124. |  |

#### Initial Stock Upload

##### Data Files for Initial Stock Upload

In order to run this business process, you may need to create stock for the example products.

To provide full pallets into the General Storage (StType Y001) and General Storage Picking Area (StType Y002), you can apply the ‘isu_Y001_Y002_ProInt.csv’ file:

The CSV file is contained in the file Initial_Stock_Upload_Data_DE.zip, which can be downloaded from the SAP Note 2620457.

##### Adopt Business Partner ID in .csv Files When Deviating from Default Business Partner Number

The sample .csv files provided for you to use when uploading the stock data contain a default ID,

33413310

This ID is for the business partner (representing the plant) which is used in its roles as Owner and Party Entitled to Dispose.

If you change the default ID, for example, because your plant has a different ID and/or you used a different prefix, other than

33413310, you update that value for the business partner in all .csv files. Otherwise, the upload transaction fails, indicating that the business partner does not exist.

You must find and replace the business partner ID, 33413310, with your actual ID in all of the provided files.

##### Upload Initial Stock

Use

In a real business case, the raw materials are purchased from external suppliers; in that case that process is covered by the standard purchasing processes. For the purpose of this test, we post initial stock upload directly to the Storage Locations 333S, which is triggered from EWM.

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you upload the initial stock.

Procedure

| Transaction Code | SAP EWM Menu |
| --- | --- |
| /SCWM/ISU | SAP Menu > SCM Extended Warehouse Management > Extended Warehouse Management > Interfaces > Data Upload > Stock Data Transfer |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the Transaction | Access the transaction using one of the navigation options above. |  |  |
| 2 | Enter the Data | On the Stock Data Transfer screen, ensure that the following fields are complete:Warehouse Number: 3330Language: EnglishNumber of HUs per posting: 50Do not Post Data in ERP:Local File: XDisplay Data:X |  |  |
| 3 |  | Choose Open Folder.Choose Import.Locate the following .csv files on your computer.isu_Y001_Y_002_ProInt.csvChoose Upload the File for Initial Stock Upload Open.The system displays the path and file name of the selected .csv file.On the Stock Data Transfer screen, choose Upload.Choose OK. | On the Stock Data Transfer screen, the uploaded rows from the .csv file are displayed. |  |
| 4 | Upload the Initial Stock | Choose Start Stock Data transfer (F8)Record the number of the warehouse material document for later use. | Upload the File for Initial Stock the message Warehouse Material Document ########## is displayed in the lower part of the screen. |  |

Result

The material document has been saved and is being stored in the database.

## Overview Table

Procedure

This scope item consists of several process steps provided in the table below.

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Planned Independent Requirements](#unique_13) [page ] 13 | Production Planner | Maintain PIRs (F3445) | The Maintain PIRs (F3445) screen displays. |
| [Material Requirements Planning at Plant Level](#unique_14) [page ] 14 | Production Planner | Schedule MRP Runs (F1339) | The Schedule MRP Runs (F1339) screen displays. |
| [Evaluate Stock/Requirements Situation](#unique_15) [page ] 15 | Production Planner | Monitor Material Coverage Net/Individual Segments | The Monitor Material Coverage - Net Segments (F0247A) screen displays. |
| [Convert Planned Order to Production Order](#unique_16) [page ] 16 | Production Planner | Manage Material Coverage - New Version (F0251A) | The Manage Material Coverage screen displays. |
| [Review Material Availability Status for Production Orders](#unique_17) [page ] 18 | Production Supervisor - Discrete Manufacturing | Manage Production Orders (F2336) | The Manage Production Orders (F2336) screen displays. |
| [Release Production Order](#unique_18) [page ] 19 | Production Supervisor - Discrete Manufacturing | Manage Production Orders (F2336) | The Manage Production Orders (F2336) screen displays. |
| [Material Staging for Production Order](#unique_19) [page ] 21 | Production Operator - Discrete Manufacturing | Stage Materials for Production (MF60) | The Material Staging for Planned Orders screen displays. |
| [Display EWM Outbound Delivery Order in SAP EWM](#unique_20) [page ] 23 |  | /SCWM/PRDO | The Maintain Outbound Delivery Order screen displays |
| [Create Warehouse Task for Staging in SAP EWM](#unique_21) [page ] 24 |  | /SCWM/TODLV_O | The Create Warehouse Task - Warehouse Number number - Stock Removal screen appears |
| [Confirm Warehouse Task for Staging in SAP EWM](#unique_22) [page ] 26 |  | /SCWM/TO_CONF | The Confirm Warehouse Task in Warehouse Number number screen appears. |
| [Post Goods Issue in SAP EWM](#unique_23) [page ] 27 |  | /SCWM/PRDO | The Maintain Outbound Delivery Order screen displays |
| [Check Stock Situation](#unique_24) [page ] 29 | Inventory Manager | Stock - Single Material | The Stock - Single Material screen displays. |
| [Check Goods Movement for Outbound Delivery for Production Supply (Optional)](#unique_25) [page ] 30 | Inventory Manager | Material Documents Overview (F1077) | The Material Documents Overview (F1077) screen appears. |
| [Confirm Production Operations](#unique_26) [page ] 31 | Production Operator - Discrete Manufacturing | Confirm Production Order Operation (CO11N) | The Enter Time Ticket for Production Order screen displays. |
| [Generate Expected Goods Receipt Document](#unique_27) [page ] 32 | Receiving Specialist | Expected Goods Receipt (F3298) | The Expected Goods Receipt (F3298) screen appears |
| [Create Inbound Delivery with Reference to Expected Goods Receipt in SAP EWM](#unique_28) [page ] 34 |  | /SCWM/GRPI | The GR Preparation - Production (Warehouse Number number) screen appears. |
| [Post Goods Receipt with Reference to Inbound Delivery in SAP EWM](#unique_29) [page ] 36 |  | /SCWM/GR | The Goods Receipt (Warehouse Number number> screen appears. |
| [Check Material Document (Optional)](#unique_30) [page ] 38 | Inventory Manager | Material Documents Overview (F1077) | The Material Documents Overview (F1077) screen is displayed. |
| [Create Putaway Warehouse Task for Inbound Delivery](#unique_31) [page ] 39 |  | /SCWM/TODLV_I | The Create Warehouse Task - Warehouse Number number - Putaway screen appears. |
| [Putaway of Products in SAP EWM](#unique_32) [page ] 41 |  | /SCWM/TO_CONF | The Confirm Warehouse Task in Warehouse Number number screen appears. |
| [Check Inbound Delivery (Optional)](#unique_33) [page ] 42 | Receiving Specialist | Display Inbound Delivery (VL33N) | The Display Inbound Delivery (VL33N) screen appears. |

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

Planned independent requirements are used to perform demand management functions. A planned independent requirement contains one planned quantity and one date, or a number of planned independent requirements schedule lines, such as one planned quantity split over time according to dates.

|  |
| --- |
| Note Instead of creating a single requirement, sometimes a requirements plan that includes one or more planned independent requirements can be maintained for mass processing. In this case, the requirements are grouped and maintained under a requirement plan number. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori launchpad | Log on to the SAP Fiori Launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage PIRs (Obsolete) - Replaced by “Maintain PIRs” (F1079). | The Manage PIRs (Obsolete) - Replaced by “Maintain PIRs” (F1079) screen displays. |  |
| 3 | Check Default Area of Responsibility | On the Manage PIRs (Obsolete) - Replaced by “Maintain PIRs” (F1079) screen, click your user name and choose Area of Responsibility.Check that only this entry is displayed there: Plant 1 AE | If there is no entry Plant 1 AE in the Area of Responsibility screen, choose Add to select it and then choose OK. For other plant entries in the Area of Responsibility screen, choose Delete to remove the others and then choose OK. |  |
| 4 | Select Material | On the Manage PIRs (Obsolete) - Replaced by “Maintain PIRs” (F1079) screen, enter material SG124 as a filter. |  |  |
| 5 | Filter Result | Choose Go to execute. | Material item displays. |  |
| 6 | Select Material Item | Choose the material item to display the Draft PIRs field. | The Manage PIRs (Obsolete) - Replaced by “Maintain PIRs” (F1079) view displays. |  |
| 7 | Draft PIRs | Add 8 PC. |  |  |
| 8 | Save PIRs draft | Choose Save Draft (bottom right). | The PIRs Draft is saved. |  |
| 9 | Release PIRs | Choose Release PIRs (bottom right). | The PIRs are released. |  |

#### Material Requirements Planning at Plant Level

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The aim of material requirement planning is to tailor available capacities and receipts on time to suit requirement quantities. You can use MRP or consumption-based planning for this purpose. Single-item multilevel requirement planning is performed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori launchpad | Log on to the SAP Fiori Launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule MRP Runs (F1339). | The Schedule MRP Runs (F1339). screen displays. |  |
| 3 | Enter Basic Parameters for New Job | Choose New (middle right section). In the New Jobs screen, make the following entries:Job Template: Material Requirement Planning (MRP).Job Name: MRP for SG124.Start Immediately: X.Plant: 3310.Material: SG124.All Order BOM Components: x.Planning Mode: 1. |  |  |
| 4 | Schedule New Job | On the New Job screen, choose Schedule (bottom-right section). | The new job is created and it displays in the table of Schedule MRP Runs (F1339). |  |
| 5 | Refresh Application Jobs List | To check the status of the job you created, choose Go at the top-right section of the screen. | The Schedule MRP Runs (F1339) table is refreshed. |  |

#### Evaluate Stock/Requirements Situation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the requirement planning has been performed, you want to display the stock/requirements situation for the semifinished good SG124 in the stock/requirements list.

Prerequisite

Requirement planning has been carried out.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori launchpad | Log on to the SAP Fiori Launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Material Coverage Net/Individual Segments. | The Monitor Material Coverage - Net Segments (F0247A) screen displays. |  |
| 3 | Select Material | Mark the checkbox for the following materials, and then choose Manage Materials (bottom right).Material: SG124 | The Material screen and Material Details screen display. |  |
| 4 | Review Stock/Requirements List | Choose the corresponding material on the Material screen on the left. | The detailed Stock/Requirements List for each material displays. |  |
| 5 | Display Planned Order | From the list on the Material screen on your left, select the material for which you want to check the planned order.Material: SG124On the Material Details screen, choose PldOrd number in column MRP Element.Note The BOM explosion during the MRP run has generated dependent requirements for the demand-driven planned components. If inventory does not cover the requirements, planned orders are created for in-house-produced materials and purchase requisitions for externally procured materials. | The selected planned order displays on the screen.If there is no shortage for those materials, the planned order will not be generated.If you want to display more information about the planned order, on the right bottom of this dailog box, choose Open Planned Order. |  |

### Convert Planned Order to Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The daily MRP run creates planned orders for goods that are to be produced internally. When the planned opening date is reached, the planned orders are converted to production orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori launchpad | Log on to the SAP Fiori Launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Material Coverage - New Version (F0251A). | The Find Material screen displays. |  |
| 3 | Select Material | Enter Material number and select Plant and Shortage Definition. Then choose OK.Material: SG124Plant: 3310Shortage Definition: MRP Standard | The Manage Material Coverage screen display. |  |
| 4 | Find Planned Order | Choose the generated planned order.Note If no planned orders were generated, there is sufficient stock for material SG124. Increase the PIRs quantity and test from the beginning with create PIRs and run MRP | The PlOrd order number dialog box appears. |  |
| 5 | Change Planned Order | Choose Open…Planned Order. | The Change Planned Order: Stock order screen appears. |  |
| 6 | On the Change Planned Order: Stock order screen, in the Other Data section, changes the Production Version from 0001 to 0099. | On the Change Planned Order: Stock order screen, in the Other Data section, change the Production Version from 0001 to 0099. | The Production Version 000X uses an Alternative BoM 3, with which the production with PSA is enabled. |  |
| 7 | Save your entries | Save your entries | The following system message appears: Planned order number changed |  |
| 8 | Choose Back. | Choose Back. | The Manage Material Coverage screen appears. |  |
| 9 | On the Manage Material Coverage screen, select the planned order. | On the Manage Material Coverage screen, Select Convert from Action dropdown list. | The Planned Order <PlOrd number> dialog box appears. |  |
| 10 | Convert to Production Order. | In the Change Planned Order <PlOrd number> dialog box, choose Convert to Production Orderand confirm End Date and Quantity.Choose OK. |  |  |
| 11 | Choose OK. | To confirm the conversion, choose OK. | The following system message appears: Production order number has been created |  |
| 12 | Make a note of the Production Order number | Make a note of the Production Order number: __________. |  |  |

### Review Material Availability Status for Production Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

Production orders are created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori launchpad | Log on to the SAP Fiori Launchpad as a Production Supervisor - Discrete Manufacturing . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Choose Home on top of the screen to open All My Apps list.In the App list, choose Production Control (Discrete) - Order Management and then choose Manage Production Orders (F2336). | The Manage Production Orders (F2336) screen displays. |  |
| 3 | Check Default Area of Responsibility(supervisor) | On the Manage Production Orders (F2336) screen, make the following entries:To check Default Area of Responsibility (supervisor), select the user (from the top-left corner): App Settings > Area of Responsibility Production Supervisor. Check only this entry is displayed:Plant 1: 3310.MTS DI - Valuated (YB1). | If no entry Plant 1 3310 in the Area of Responsibility(Supervisor) screen, choose Add to select it and then choose OK .For other plant entries in the Area of Responsibility (Supervisor) screen, choose Delete to remove the others and then choose OK. |  |
| 4 | Select Production Order | On the Manage Production Orders (F2336) screen, enter the following search condition as filter.Choose Adapt Filters to display more selection filter. Choose More filters under Production Orders. Check the checkbox for Maintain Default Values and Production Plant and choose OK.Choose Go.Status: Created.Material: SG124.Production Plant: 3310.Choose Go to execute. | The Manage Production Orders (F2336) screen displays.Material and Production Plant fields are then added to filter bar. |  |
| 5 | Review Material availability status | Check the Missing Components icon on the right part of the order.Select the icon to display missing parts list. | The Issue Details dialog box appears.The following missing parts are expected for SG124.Components Missing.RM124The shortage of raw materials to be supplied after the Material Staging step. |  |

### Release Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A release at order operation level results in the order and all its operations being released. The order and the operations receive the status REL (released).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori launchpad | Log on to the SAP Fiori Launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Production Orders (F2336). | The Manage Production Orders (F2336) screen displays. |  |
| 3 | Check Default Area of Responsibility(supervisor) | On the Manage Production Orders (F2336) screen, make the following entries:To check Default Area of Responsibility (supervisor), select the user (from the top-left corner): App Settings > Area of Responsibility Production Supervisor .Check that only this entry is displayed:3310.MTS DI - Valuated (YB1). | If no entry Plant 1 3310 in the Area of Responsibility(Supervisor) screen, choose add to select it and then choose OK. For other plant entries on the Area of Responsibility (Supervisor) screen, choose Delete to remove the others and then choose OK |  |
| 4 | Select Production Order | Enter the following search condition as filter.Choose Adapt Filters to display more selection filter. choose More filters under ‘Material’ and ‘Plant’. Check the checkbox for Material and Plant and choose Go. Choose OK. Material and Plant fields are then added to filter bar.Status: CreatedMaterial:SG124.Plant: 3310.Choose Go to execute. | The Manage Production Orders (F2336) screen displays. |  |
| 5 | Select Order | On the Manage Production Orders (F2336) screen, Select your Production Order by checking the checkbox beside the order number.Choose Edit. | The Manage Production Orders (F2336) screen displays. |  |
| 6 | Edit Order | On the Production Order Change: Header screen.In Goods Receipt tab page Receipt section, make the following entries:Stor. Location: 333S. |  |  |
| 7 | Execute Release | Choose More > Functions > Release. | The Release Order dialog box appears. |  |
| 8 | Release Order. | In the Release Order dialog box, choose Release Order. | The following system message appears: Release carried out (Please check log) |  |
| 9 | Save your entries | Save your entries | The following system message appears: Order number <number> saved |  |

### Material Staging for Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you stage materials for production.In case, there is sufficient stock available on the production storage location no line items are generated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori launchpad | Log on to the SAP Fiori Launchpad as Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Stage Materials for Production (MF60). | The Material Staging for Planned Orders screen displays. |  |
| 3 | Enter Details | On the Material Staging for Planned Orders screen, make the following entries:Staging Types.Select the SLoc Level checkbox.Select the EWM Rel. Parts checkbox.Plant: 3310. | The Pull List: Storage Location Level screen displays. |  |
| 4 | Set Global Settings | Select More - Global Settings (F5).In the Display section, uncheck the Stor.loc. view w/o kanban parts checkbox.Choose Continue. |  |  |
| 5 | Navigate to the Production/Process Orders tab. | Navigate to the Production/Process Orders tab. |  |  |
| 6 | Enter Order | On the Production/Process order tab, make the following entries:Production Order: <your production Order Number>.Components Materials: RM124. |  |  |
| 7 | Choose Execute. | Choose Execute. | The Pull List: Storage Location Level screen appears. |  |
| 8 | Choose Replenishment Elements | Select the required line items from the left-hand margin and choose Replenishment Proposal from the top of the screen. | The Quantity staged field is populated. |  |
| 9 | Choose Replenishment Elements | Review the staged quantity and choose Replenishment Elements. | The Replen. Elements table appears. |  |
| 10 | Check or Enter Replenishment Storage Location | On the bottom half of the split screen, select the lines and check or make the following entries:Replenishment storage location: 333S. |  |  |
| 11 | Choose Stage | Select the Replenishment Element line and then choose Stage at the middle of the screen. | The Staging cell is populated with Element Checked: OK. |  |
| 12 | Save | Choose Save. | Missing materials are transferred to the shop floor from the designated storage area. The shortage of raw material for production order is supplied with this step. |  |

### Display EWM Outbound Delivery Order in SAP EWM

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Check whether outbound delivery order in EWM is created for staging.

Procedure

| Transaction Code | /SCWM/PRDO |
| --- | --- |
| /SCWM/PRDO | SAP Menu > SCM Extended Warehouse Management > Extended Warehouse Management > Delivery Processing > Outbound Delivery > Maintain Outbound Delivery Order . |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access Transaction | Access the transaction using one of the navigation options above. |  |  |
| 2 | Maintain Default Values | If the Maintain Default Values dialog box appears, make the following entries:Warehouse No.: 3330. | The Maintain Outb. Deliv. Order - Warehouse No 3330 screen appears. |  |
| 3 | Choose Continue (Enter). | In the Maintain Default Values dialog box, choose Continue (Enter). |  |  |
| 4 | Maintain Default Values | On the Maintain Outb. Deliv. Order - Warehouse No 3330 screen, choose Maintain Default Values or F5 | The Maintain Default Values dialog box appears. |  |
| 5 | Check Default Values | In the Maintain Default Values dialog box, make or check the following entries:Warehouse No: 3330. |  |  |
| 6 | Choose Continue (Enter). | In the Maintain Default Values dialog box, choose Continue (Enter). |  |  |
| 7 | Open Advanced Search | On the Maintain Outbound Delivery Order - Warehouse Number number screen, choose Open Advanced Search. | The Advanced Search sub screen appears |  |
| 8 | Enter purchase order number | On the Advanced Search sub screen in the Search Crit. 1 tab, make the following entries:Document Type: OPS.Goods Issue Status (Item): 1. |  |  |
| 9 | Choose Advanced Search | Choose Advanced Search. | The following system message appears: Number Documents Read.The Outbound Delivery appears in the table. |  |
| 10 | Choose Close Advanced Search. | Choose Close Advanced Search. |  |  |
| 11 | In the search result, select an Outbound Delivery Order. | In the search result, choose a Outbound Delivery Order. |  |  |
| 12 | Note down the Document | Note down the Outbound Delivery Order number |  |  |
| 13 | Navigate to the Reference Documents tab. | Navigate to the Reference Documents tab. |  |  |
| 14 | On the Reference Documents tab, check the ERP document field. | On the Reference Documents tab, check the Reference Document Number field. |  |  |
| 15 | Note down Reference Document Number | Make a note of the Reference Document Number (SAP S/4HANA Outbound Delivery) number: __________. |  |  |

### Create Warehouse Task for Staging in SAP EWM

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Create warehouse tasks for outbound delivery order.

Procedure

| Transaction Code | SAP EWM Menu |
| --- | --- |
| /SCWM/TODLV_O | SAP Menu > SCM Extended Warehouse Management > Extended Warehouse Management > Work Scheduling > Create Warehouse Task for Warehouse Request > Stock Removal for Outbound Delivery Order |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access Transaction | Access the transaction using one of the navigation options above. | The Create Warehouse Task - Warehouse Number number - Stock Removal screen appears. |  |
| 2 | Maintain Default Values | If the Maintain Default Values dialog box appears, make the following entries:Warehouse No: 3330. | The Create Warehouse Task - Warehouse Number number - Stock Removal screen appears. |  |
| 3 | Choose Continue (Enter). | In the Maintain Default Values dialog box, choose Continue (Enter). |  |  |
| 4 | Maintain Default Values | On the Create Warehouse Task - Warehouse Number 3330 - Stock Removal , choose Maintain Default Values or F5 | The Maintain Default Values dialog box appears |  |
| 5 | Check Default Values | In the Maintain Default Values dialog box, make or check the following entries:Warehouse No: 3330. |  |  |
| 6 | Choose Continue (Enter). | In the Maintain Default Values dialog box, choose Continue (Enter). |  |  |
| 7 | Enter warehouse request number | Make the following entries:Find: Warehouse Request your warehouse request numberNote Enter the Document number from the previous step. |  |  |
| 8 | Choose Perform Search. | Choose Perform Search. | The Warehouse Request appears in the table. |  |
| 9 | Navigate to Warehouse Request tab. | Navigate to Warehouse Request tab. |  |  |
| 10 | Select All. | On the Warehouse Request tab in the table, choose Select All. |  |  |
| 11 | Choose Create + Save. | On the Warehouse Request tab, choose Create Warehouse Task. | The following system message appears: <number> warehouse tasks were created |  |
| 12 | Save your entries | Save your entries. | The following system message appears: Warehouse order <number> createdYou can also choose the Message Log (Shift F12) to display created Warehouse Order number. |  |
| 13 | Note down the warehouse order | Note down the warehouse order for testing purposes. |  |  |

### Confirm Warehouse Task for Staging in SAP EWM

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Confirm warehouse tasks for outbound delivery order.

Procedure

| Transaction Code | SAP EWM Menu |
| --- | --- |
| /SCWM/TO_CONF | SAP Menu > SCM Extended Warehouse Management > Extended Warehouse Management > Execution > Confirm Warehouse Task |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access Transaction | Access the transaction using one of the navigation options above. | The Confirm Warehouse Task in Warehouse Number <number> screen appears. |  |
| 2 | Choose Find Warehouse Order | On the Confirm Warehouse Task in Warehouse Number <number> screen, from the Find dropdown list choose Warehouse Order. |  |  |
| 3 | Enter warehouse order number | Make the following entries:Find: Warehouse Order your warehouse order number. |  |  |
| 4 | Choose Perform Search. | Choose Perform Search. | The following system message appears: Selection produced <number> results.The Warehouse Order appears in the View. |  |
| 5 | Select the Warehouse Order. | In the List View choose the Warehouse Order. |  |  |
| 6 | Choose Confirm in Foreground | Choose Confirm in Foreground. | The warehouse task(s) appear on the tab Product WT. |  |
| 7 | Navigate to the Product WT tab | Navigate to the Product WT tab. |  |  |
| 8 | Choose the warehouse task(s) | On the Product WT tab in the warehouse task table, choose the warehouse task(s). |  |  |
| 9 | Choose Confirm in Foreground | Choose Confirm in Foreground. | WT Status is updated to Confirmed in Foreground. |  |
| 10 | Save your entries | Save your entries | The following system message appears: Warehouse task <warehouse task number> was confirmed |  |

### Post Goods Issue in SAP EWM

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The goods issue (GI) is posted for the staging outbound delivery.

Procedure

| Transaction Code | /SCWM/PRDO |
| --- | --- |
| /SCWM/PRDO | SAP Menu > SCM Extended Warehouse Management > Extended Warehouse Management > Delivery Processing > Outbound Delivery > Maintain Outbound Delivery Order |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access Transaction | Access the transaction using one of the navigation options above. |  |  |
| 2 | Maintain Default Values | If the Maintain Default Values dialog box appears, make the following entries:Warehouse No: 3330. | The Maintain Outb. Deliv. Order - Warehouse No 3330screen appears. |  |
| 3 | Choose Continue (Enter). | In the Maintain Default Values dialog box, choose Continue (Enter). |  |  |
| 4 | Maintain Default Values | On the Maintain Outb. Deliv. Order - Warehouse No 3330 screen, choose Maintain Default Values or F5. | The Maintain Default Values dialog box appears. |  |
| 5 | Check Default Values | In the Maintain Default Values dialog box, make or check the following entries:Warehouse No: 3330. |  |  |
| 6 | Choose Continue (Enter). | In the Maintain Default Values dialog box, choose Continue (Enter). |  |  |
| 7 | Enter Outbound Delivery Order number | On the Maintain Outbound Delivery Order - Warehouse Number number screen, make the following entries:Find: Outbound Delivery Order your Outbound Delivery Order number.Note Enter the Outbound Delivery Order number from the previous step. | The Advanced Search sub screen appears. |  |
| 8 | Choose Perform Search. | Choose Perform Search. | The Warehouse Request appears in the table. |  |
| 9 | Select an Outbound Delivery Order. | In the search result, choose the Outbound Delivery Order. |  |  |
| 10 | Post Goods Issue | Choose Goods Issue + Save. |  |  |

### Check Stock Situation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Check in the SAP S/4HANA system if the stock is staged to the production supply storage location.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori launchpad | Open the SAP Fiori Launchpad as a Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Open App | Open Stock - Single Material. | The Stock - Single Material screen displays. |  |
| 3 | Enter Material number | On the Stock - Single Material screen, make the following entry:Material: RM124. | The Stock overview on the Plant/Storage Location level is displayed. |  |
| 4 | Check stock | Check the stock for plant 3310 and storage location 331B. | The required stock for the production order is displayed in the Unrestricted-Use Stock segment. |  |

### Check Goods Movement for Outbound Delivery for Production Supply (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Check in SAP S/4HANA whether the goods issue material document is posted for outbound delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori Launchpad as a Inventory Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Choose Material Documents Overview (F1077). | The Material Documents Overview (F1077) screen appears. |  |
| 3 | Change Settings | In section Material Documents, choose Settings on the right-hand side. | The View Settings dialog box appears. |  |
| 4 | View Settings | In the View Settings dialog box, choose the column for Goods Movement Type. |  |  |
| 5 | Confirm | Choose OK. |  |  |
| 6 | Enter Selection Data | On the top of the screen, make the following entries:Stock Change: Transfer Posting.Stock Change Level: Plant.Plant: 3310.Storage Location: 333S.Material:RM124.Posting Date: <the date when you putaway the stock in the warehouse.>. |  |  |
| 7 | Check the Material Document | Choose Go. | Material documents are listed. |  |
| 8 | Note down Material Document Number | Note down the number of the Material Document Item with Goods Movement Type: TF SLoc to SLoc (411). |  |  |
| 9 | Select Material Document | Choose SAP S/4HANA Material Document. |  |  |
| 10 | Check Delivery Note Field | On the General Information tab, compare the Delivery Note with the reference Warehouse Material Document from the previous step. | The Delivery Note is equal to the reference Warehouse Material Document from the previous step. |  |

### Confirm Production Operations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Confirm the production order to post consumption via backflush.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori launchpad | Log on to the SAP Fiori Launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Confirm Production Operation (F3069). | The Perform Work screen displays. |  |
| 3 | Enter Production Order and Operation | On the Perform Work screen, make the following entries:Order: Production Order Number you noted down.Operation: For example, operation 0010. |  |  |
| 4 | Enter Fields in Quantities Section | In section Quantities, make the following entries:Yield :enter the amount you want to Confirm.Scrap :enter the amount you want to Scrap. |  |  |
| 5 | Check Material Movements | In section Material Movements, check the material list. | The system shows you an overview table of all materials for which the withdrawing is done automatically with the confirmation of the operation.The material RM124 is set for backflush (in the material master) so that the withdrawing is done automatically after you confirm the operation. |  |
| 6 | Enter Fields in Activities Section | In section Activities, make the following entries:Setup :enter the setup time you want to confirm for this operationMachine: enter the machine time you want to confirm for this operationLabor :enter the labor time you want to confirm for this operation |  |  |
| 7 | Save your entries | Choose Post and Complete to make final confirmation for this operation. | Confirmation has been created. If you want to make a partial confirmation, you can choose Post. |  |
| 8 | Repeat Steps | Go back and repeat the steps 3–7 for operation number 0020 and save your entries. |  |  |

### Generate Expected Goods Receipt Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Generate an Expected Goods Receipt (EGR) document for the production order. You can also perform this step in the SAP EWM system as a ‘Pull’ method with transaction code /SCWM/ERP_EGR_DELETE.

Use

In this process, the expected goods receipt functionality is used for the production order based on the creation of inbound deliveries in EWM. The EGR is created in the SAP S/4HANA system.

|  |
| --- |
| Note Alternatively, the EGR document can be created in the SAP EWM system. If you choose to do so, you can refer to chapter Create EGR Document in the SAP EWM System in the Appendix. |

In productive systems, this job is scheduled as a background job. For more information, see the Solution Operation Guide for SAP EWM in the SAP Help Portal.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori launchpad | Log on to the SAP Fiori Launchpad as a Receiving Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Expected Goods Receipt (F3298) | The Expected Goods Receipt (F3298) screen appears. |  |
| 3 | Create new Entry | On the Expected Goods Receipt screen, choose New. | The Schedule Expected Goods Receipt screen appears. |  |
| 4 | Select Job Template | On the New Job screen in the General Information tab, make the following entries:Job Template: Expected Goods Receipt .Job Name: Expected Goods Receipt for SG124. |  |  |
| 5 | Select Scheduling Options | On the Scheduling Options tab, make the following entries:choose Start Immediately checkbox. |  |  |
| 6 | Select Parameters | On the Parameters tab, make the following entries:In the SAP EWM Parameters section:Warehouse Number: 333.Choose the Create Expected Goods Receipts in the Delivery Date/Scheduled End Date: Time Range sectionSelection Start Date: Production Order date - one week.Selection Start Time: 00:00:00.Selection End Date: Production Order date + one week.Selection End Time: 23:59:59. |  |  |
| 7 | Select the Activate PP Selection checkbox. | In the Selection Area for Production Orders/Process Orders section, make the following entries:Choose Activate PP Selection checkbox.Order: <Production Order Number you noted down>. |  |  |
| 8 | Deselect the Activate PO/SA Selection checkbox. | In the Selection Area for Purchase Orders/Scheduling Agreements section, deselect the Activate PO/SA Selection checkbox. |  |  |
| 9 | Choose Check | On the New Job screen, choose Check. | The following system message appears:You can go ahead and schedule the job. |  |
| 10 | Choose Schedule | On the New Job screen, choose Schedule. | The following system message appears:Job Expected Goods Receipt for SG124 has been scheduled. |  |

### Create Inbound Delivery with Reference to Expected Goods Receipt in SAP EWM

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Create an inbound delivery in SAP EWM with reference to expected goods receipt document.

Procedure

| Transaction Code | SAP EWM Menu |
| --- | --- |
| /SCWM/GRPI | SCM Extended Warehouse Management > Extended Warehouse Management > Delivery Processing > Inbound Delivery > GR Preparation - Production |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access Transaction | Access the transaction using one of the navigation options above. | The GR Preparation - Production (Warehouse Number <number>) screen appears. |  |
| 2 | Maintain Default Values | If the SAP dialog box appears, make the following entries:Warehouse No:3330. |  |  |
| 3 | Choose Continue (Enter). | In the SAP dialog box, choose Continue (Enter). |  |  |
| 4 | Maintain Default Values | On the GR Preparation - Production (Warehouse Number number) screen, choose Maintain Default Values or F5 | The GR Preparation - Production (Warehouse Number <number>) dialog box appears. |  |
| 5 | Check Default Values | In the GR Preparation - Production (Warehouse Number number) dialog box, make or check the following entries:Warehouse No: 3330.Choose Without TU checkbox. |  |  |
| 6 | Choose Continue (Enter). | In the GR Preparation - Production (Warehouse Number number) dialog box, choose Continue (Enter). |  |  |
| 7 | Choose Find Manufacturing Order | On the GR Preparation - Production (Warehouse Number <number>) screen, from the Find dropdown list choose Manufacturing Order. |  |  |
| 8 | Enter warehouse order number | Make the following entries:Find: Manufacturing Order <your production order number>. |  |  |
| 9 | Choose Execute Search. | Choose Execute Search. | The following system message appears: Search completed; see message log for details. |  |
| 10 | Select all items | On the left screen area, choose all items. |  |  |
| 11 | Choose Set Copying Flag for Selection. | Choose Set Copying Flag for Selection. |  |  |
| 12 | Choose Copy Flagged Item. | Choose Copy Flagged Item. | The GR Preparation - Production (Warehouse Number <number>) dialog box appears. |  |
| 13 | Choose Continue (Enter). | The GR Preparation - Production (Warehouse Number <number>) dialog box, choose Continue (Enter). | The selected items appear in the document table. |  |
| 14 | Check item details | In the document table, choose one line in and choose Switch to Form View. |  |  |
| 15 | Check the following values: | Check the following values:Quantity .UoM.Whse Proc Type.Goods Mvt Bin. |  |  |
| 16 | Save your entries | Save your entries. | The following system message appears:Inbound Delivery GR Manufacturing <number> created |  |
| 17 | Note down the Inbound Delivery number | Note down the Inbound Delivery GR Manufacturing number. |  |  |

### Post Goods Receipt with Reference to Inbound Delivery in SAP EWM

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Post a goods receipt in SAP EWM based on the inbound delivery created in the previous step.

| Transaction Code | SAP EWM Menu |
| --- | --- |
| /SCWM/GR | SCM Extended Warehouse Management > Extended Warehouse Management > Delivery Processing > Inbound Delivery → Physical Goods Receipt |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access Transaction | Access the transaction using one of the navigation options above. | The Goods Receipt (Warehouse Number number) screen appears. |  |
| 2 | Maintain Default Values | If the SAP dialog box appears, make the following entries:Warehouse No: 3330. |  |  |
| 3 | Choose Continue (Enter) | In the SAP dialog box, choose Continue (Enter). |  |  |
| 4 | Maintain Default Values | On the Goods Receipt (Warehouse Number number) screen, choose Maintain Default Values or F5. | The Goods Receipt (Warehouse Number number) dialog box appears. |  |
| 5 | Check Default Values | In the Goods Receipt (Warehouse Number number) dialog box, make or check the following entries:Warehouse No: 3330. |  |  |
| 6 | Choose Continue (Enter) | In the Goods Receipt (Warehouse Number number) dialog box, choose Continue (Enter). |  |  |
| 7 | Choose Find Inbound Delivery | On the Goods Receipt (Warehouse Number number) screen, from the Find dropdown list, choose Inbound Delivery. |  |  |
| 8 | Enter Inbound Delivery number | Make the following entries:Find: Inbound Delivery your Inbound Delivery number. |  |  |
| 9 | Choose Execute Search | Choose Execute Search. | The following system message appears: Search completed; see message log for details. |  |
| 10 | Select the Inbound Delivery | In the List View, choose the Inbound Delivery. |  |  |
| 11 | Choose Pack | Choose Pack. | The Work Center Packing for Inbound Delivery screen appears. |  |
| 12 | On the Work Center Packing for Inbound Delivery screen, navigate to the Create HU tab | On the Work Center Packing for Inbound Delivery screen, navigate to the Create HU tab. |  |  |
| 13 | Enter packaging material | On the Create HU tab, make the following entries:Pack. Material: PMPAL00. |  |  |
| 14 | On the Create HU tab, choose Execute | On the Create HU tab, choose Execute. | The following system message appears: HU <number> (PMPAL00) was constructed |  |
| 15 | Drag and drop inbound delivery item node to HU node | On the Work Center Packing for Inbound Delivery screen, in the tree area drag the node with your product from the inbound delivery item. Drop it to the node with the HU number you created in the previous step. | The inbound delivery item is packed on the HU. |  |
| 16 | Choose Save and go back | Choose Save and go back. |  |  |
| 17 | On the Work Center Packing for Inbound Delivery screen, choose Check | On the Work Center Packing for Inbound Delivery screen, choose Check. | The following system message appears: Activity was carried out successfullyBlocked (Overall Status) turns to Status Green. |  |
| 18 | Post Goods Receipt | Choose the Post GR checkbox and then choose Post Goods Receipt. |  |  |

### Check Material Document (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Along with populating the warehouse with stock, there is also a financial posting in the SAP S/4HANA system. The check step is to show you the material document along with its financial posting in the SAP S/4HANA system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori Launchpad with the Inventory Manager role. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Choose Material Documents Overview (F1077) . | The Material Documents Overview (F1077) screen appears. |  |
| 3 | Change Settings | In section Material Documents, choose Settings on the right-hand side. | The View Settings dialog box appears. |  |
| 4 | View Settings | In the View Settings dialog box, choose the column for Goods Movement Type. |  |  |
| 5 | Confirm | Choose OK. |  |  |
| 6 | Enter Selection Data | On top of the screen, make the following entries:Stock Change: STOCK INCREASE.Stock Change Level: Plant.Plant: 3310.Storage Location: 333D.Material: SG124Posting Date: <the date when you putaway the stock in the warehouse.>. |  |  |
| 7 | Check the Material Document | Choose Go. | Material documents are listed. |  |
| 8 | Note down Material Document Number | Note down the number of the Material Document Item with Goods Movement Type GR goods receipt (101). |  |  |
| 9 | Select Material Document | Choose SAP S/4HANA Material Document. |  |  |
| 10 | Check Delivery Note Field | On the General Information tab, compare the Delivery Note with the reference warehouse material document from the previous step. | The Delivery Note is equal to the reference warehouse material document from the previous step. |  |

### Create Putaway Warehouse Task for Inbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Transaction Code | SAP EWM Menu |
| --- | --- |
| /SCWM/TODLV_I | SAP Menu > SCM Extended Warehouse Management > Extended Warehouse Management > Work Scheduling > Create Warehouse Task for Warehouse Request > Putaway for Inbound Delivery |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access Transaction | Access the transaction using one of the navigation options above. | The Create Warehouse Task - Warehouse Number number - Putaway screen appears. |  |
| 2 | Maintain Default Values | On the Create Warehouse Task - Warehouse Number number - Putaway screen, choose Maintain Default Values or F5 | The Maintain Default Values dialog box appears. |  |
| 3 | Check Default Values | In the Maintain Default Values dialog box, make or check the following entries:Warehouse No: 3330. |  |  |
| 4 | Choose Continue (Enter). | In the Maintain Default Values dialog box, choose Continue (Enter). |  |  |
| 5 | Open Advanced Search | On the Create Warehouse Task - Warehouse Number number - Putaway screen, choose Open Advanced Search. | The Advanced Search sub screen appears. |  |
| 6 | Enter Manufacturing Order number | On the Advanced Search sub screen in the References section, make the following entries:Manufacturing Order: your production order number. |  |  |
| 7 | Choose Advanced Search | Choose Advanced Search. | The warehouse request appears in the table. |  |
| 8 | Choose Close Advanced Search. | Choose Close Advanced Search. |  |  |
| 9 | Navigate to Warehouse Request tab. | Navigate to Warehouse Request tab. |  |  |
| 10 | Select All. | On the Warehouse Request tab in the table, choose Select All. |  |  |
| 11 | Choose Create + Save. | On the Warehouse Request tab, choose Create Warehouse Task. | The following system message appears: Number warehouse tasks were created |  |
| 12 | Save your entries | Save your entries | The following system message appears: Warehouse order number created |  |
| 13 | Note down the warehouse order | Note down the warehouse order for testing purposes. |  |  |

### Putaway of Products in SAP EWM

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Transaction Code | SAP EWM Menu |
| --- | --- |
| /SCWM/TO_CONF | SAP Menu > SCM Extended Warehouse Management > Extended Warehouse Management > Execution > Confirm Warehouse Task |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access Transaction | Access the transaction using one of the navigation options above. | The Confirm Warehouse Task in Warehouse Number number screen appears. |  |
| 2 | Choose Find Warehouse Order | On the Confirm Warehouse Task in Warehouse Number number screen, from the Find dropdown list choose Warehouse Order. |  |  |
| 3 | Enter warehouse order number | Make the following entries:Find: Warehouse Order your warehouse order number. |  |  |
| 4 | Choose Perform Search. | Choose Perform Search. | The following system message appears: Selection produced number results.The Warehouse Order appears in the View. |  |
| 5 | Select the Warehouse Order. | In the List View, choose the Warehouse Order. |  |  |
| 6 | Choose Confirm in Foreground | Choose Confirm in Foreground. | The warehouse task(s) appear on the Product WT tab. |  |
| 7 | Save your entries | Save your entries. | The following system message appears: Warehouse task warehouse task number was confirmed |  |

### Check Inbound Delivery (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Check the completion status and goods receipt material document within the inbound delivery in SAP S/4HANA.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori Launchpad as a Receiving Specialist. | The Fiori Launch Pad is displayed. |  |
| 2 | Access the App | Open Display Inbound Delivery (VL33N). | The Display Inbound Delivery (VL33N) screen appears. |  |
| 3 | Enter Inbound Delivery | On the Display Inbound Delivery (VL33N) screen, make the following entries:Inbound Delivery: inbound delivery number. |  |  |
| 4 | Choose Continue | On the Display Inbound Delivery (VL33N) screen, choose Continue. | The Inbound Delivery number Display: Overview screen appears. |  |
| 5 | Navigate to the Status Overview tab | Navigate to the Status Overview tab. |  |  |
| 6 | Check that the Overall Goods Movement Status is C – Completely processed. | In the Overall Status - Delivery table, check Overall Goods Movement Status is C – Completely processed. |  |  |
| 7 | Check that the Goods Movement Status for the items is C – Completely processed. | In the Delivery Item Status (All Items) table, check Goods Movement Status for the items is C – Completely processed. |  |  |

## Appendix

### Generate Expected Goods Receipt Documents in SAP EWM

Purpose

This is another option to create an EGR document in SAP EWM instead of creating it in the SAP S/4HANA system.

The expected goods receipt functionality is used for PO-based creation of inbound deliveries in EWM. The EGR creation can be initiated in the SAP EWM system using the procedure described below.

Procedure

| Transaction Code | SAP EWM Menu |
| --- | --- |
| /SCWM/ERP_EGR_DELETE | SCM Extended Warehouse Management > Extended Warehouse Management > Delivery Processing > Inbound Delivery > → Expected Goods Receipt > Generate Or Delete Expected Goods Receipt |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access Transaction | Access the transaction using one of the navigation options above. | The Deletion/Creation of Expected Goods Receipt screen appears. |  |
| 2 | Make the following entries | On the Deletion/Creation of Expected Goods Receipt screen, make the following entries:ERP Warehouse Number: 333.Choose Manufacturing Order.Order: <Production Order number>.Choose Free Interval.Period: <date, time> To <date, time>.Choose Program Mode: Only Create. |  |  |
| 3 | Choose Execute | On the Deletion/Creation of Expected Goods Receipt screen, choose Execute. | The system log screen displays. |  |
| 4 | Check system log | Make a note of the EGR document number: __________. | The Expected Goods Receipt document is created. |  |

Result

You have created an EGR document in the EWM system with which you can create an inbound delivery document.

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| SAP EWM Integration – Warehouse Stock Handling | After you completed the business process of SAP EWM Integration - Delivery-Based Production Integration you can continue with internal warehouse processes. |
| SAP EWM Integration – Outbound Processing to Customer | After you completed the business process of SAP EWM Integration - Delivery-Based Production Integration you can continue with the outbound to customer process with the batch-managed material. |
| Period-End Closing – Plant | These are executed collectively as a part of month-end closing. For more information on the month-end closing procedure, see the Period-End Closing – Plant(BEI) test script.Note Note that month-end closing can only be executed once a month. |

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
> Flagged while digesting this document, not verified: Check Stock Situation tells the tester to check stock in storage location 331B, while every other step (control cycle, release, staging, goods issue check) uses storage location 333S as the production supply location.

> [!warning] Conflict
> Flagged while digesting this document, not verified: The Overview Table assigns Confirm Production Order Operation (CO11N) to Production Operator - Discrete Manufacturing, but the procedure section logs on as Production Supervisor - Discrete Manufacturing and opens Confirm Production Operation (F3069).

> [!warning] Conflict
> Flagged while digesting this document, not verified: The Overview Table lists Maintain PIRs (F3445) for creating planned independent requirements, while the procedure opens Manage PIRs (Obsolete) - Replaced by Maintain PIRs (F1079).

## Connections
- part-of :: [[_cluster]]
- related-to :: [[11-inventory-warehouse-and-transportation/atualizar-area-de-abastecimento-da-producao-mds-3ks-344]]
- related-to :: [[11-inventory-warehouse-and-transportation/maintain-production-supply-area-mds-3ks-341]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-3ks-343]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-3ks-345]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2VM_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 74,746 chars in the whole document
