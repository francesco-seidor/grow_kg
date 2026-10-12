---
id: 11-inventory-warehouse-and-transportation/test-script-handling-unit-management-4mm-ae-sap-s-4hana-cloud-public-e
title: "Test Script: Handling Unit Management (4MM_AE) - SAP S/4HANA Cloud Public Edition 2608 (4MM_S4CLD2608_BPD_EN_AE)"
description: "SAP test script (UAE localization, 4MM_AE) for Handling Unit Management: packing in deliveries, HU inventory, physical inventory and HU in manufacturing; prerequisites and steps."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/handling-unit-management]
aliases: [4MM_S4CLD2608_BPD_EN_AE]
keywords: [Handling Unit Management, packing outbound delivery, packing inbound delivery, automatic packing, packing instructions, hu inventory management, physical inventory, discrete manufacturing, process manufacturing, repetitive manufacturing]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4MM_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1036
topic: 11-inventory-warehouse-and-transportation/handling-unit-management
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Handling Unit Management (4MM_AE) - SAP S/4HANA Cloud Public Edition 2608 (4MM_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4MM_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Handling Unit Management** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 28-08-26 |
| --- | --- |
|  | Handling Unit Management (4MM_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 4](#_Toc239510567)

[2 Prerequisites 5](#_Toc239510568)

[2.1 System Access 5](#_Toc239510569)

[2.2 Roles 5](#_Toc239510570)

[2.3 Master Data, Organizational Data, and Other Data 7](#_Toc239510571)

[2.4 Business Conditions 9](#_Toc239510572)

[2.5 Preliminary Steps 10](#_Toc239510573)

[2.5.1 Configure Delivery Item Generation for Packaging Material (Optional) 10](#_Toc239510574)

[2.5.2 Create Packaging Material 12](#_Toc239510575)

[2.5.3 Define Settings to Enable Automatic Packing (Optional) 13](#_Toc239510576)

[2.5.3.1 Display Condition Tables 13](#_Toc239510577)

[2.5.3.2 Check Access Sequences 15](#_Toc239510578)

[2.5.3.3 Maintain New Condition Types 17](#_Toc239510579)

[2.5.3.4 Maintain Determination Procedures 19](#_Toc239510580)

[2.5.3.5 Change Procedures in Packaging Transaction Profile 21](#_Toc239510581)

[2.5.4 Manage Packing Instruction 22](#_Toc239510582)

[2.5.4.1 Create Packing Instruction 22](#_Toc239510583)

[2.5.4.2 Create Packing Instruction Determination 23](#_Toc239510584)

[2.5.5 Create an Outbound Delivery 25](#_Toc239510585)

[2.5.6 Create a Purchase Order 26](#_Toc239510586)

[2.5.7 Create an Inbound Delivery 27](#_Toc239510587)

[2.5.8 Configure the HU Requirement Setting for Storage Location 28](#_Toc239510588)

[2.5.9 Create a Production Order 30](#_Toc239510589)

[2.5.10 Create a Process Order 31](#_Toc239510590)

[2.5.11 Create a Sales Order 31](#_Toc239510591)

[2.5.12 Create Product Cost Collectors 32](#_Toc239510592)

[3 Overview Table 34](#_Toc239510593)

[4 Test Procedures 37](#_Toc239510594)

[4.1 Execute Packing for Outbound Delivery 37](#_Toc239510595)

[4.1.1 Execute Manual Packing 37](#_Toc239510596)

[4.1.2 Execute Automatic Packing 38](#_Toc239510597)

[4.1.3 Check the Outbound Delivery 40](#_Toc239510598)

[4.2 Execute Packing for Inbound Delivery 41](#_Toc239510599)

[4.2.1 Execute Manual Packing 41](#_Toc239510600)

[4.2.2 Execute Automatic Packing 43](#_Toc239510601)

[4.3 Inventory Management with Handling Units 44](#_Toc239510602)

[4.3.1 Create Non-assigned Handling Units in Handling Unit Managed Storage Location 44](#_Toc239510603)

[4.3.2 Transfer from Storage Location to Storage Location (Pick) 46](#_Toc239510604)

[4.3.3 Transfer from Storage Location to Storage Location (Putaway) 47](#_Toc239510605)

[4.3.4 Reverse Goods Movement 48](#_Toc239510606)

[4.4 Physical Inventory with Handling Units 48](#_Toc239510607)

[4.4.1 Check Stock Information 48](#_Toc239510608)

[4.4.2 Create Non-assigned Handling Units in Handling Unit Managed Storage Location 49](#_Toc239510609)

[4.4.3 Create Physical Inventory Document and Perform Physical Inventory with Handling Units 51](#_Toc239510610)

[4.4.4 Clear Differences from Physical Inventory Document 52](#_Toc239510611)

[4.4.5 Analyze Physical Inventory Document 53](#_Toc239510612)

[4.4.6 Delete Inventoried Status of Handling Units 54](#_Toc239510613)

[4.4.7 Delete Physical Inventory Document 56](#_Toc239510614)

[4.5 Discrete Manufacturing with Handling Units 56](#_Toc239510615)

[4.5.1 Create Planned Handling Units 56](#_Toc239510616)

[4.5.2 Create Handling Units 58](#_Toc239510617)

[4.5.3 Post Goods Receipt for Handling Units 59](#_Toc239510618)

[4.6 Process Manufacturing with Handling Units 61](#_Toc239510619)

[4.6.1 Material Staging with Handling Unit 61](#_Toc239510620)

[4.6.1.1 Pick Components with Handling Unit 61](#_Toc239510621)

[4.6.1.2 Post Goods Issue with Handling Unit 62](#_Toc239510622)

[4.6.1.3 Create Planned Handling Units 63](#_Toc239510623)

[4.6.2 Create Handling Units 64](#_Toc239510624)

[4.6.3 Post Goods Receipt for Handling Units 65](#_Toc239510625)

[4.7 Repetitive Manufacturing with Handling Units 67](#_Toc239510626)

[4.7.1 Create Planned Handling Units 67](#_Toc239510627)

[4.7.2 Create Handling Units 68](#_Toc239510628)

[4.7.3 Confirm Repetitive Manufacturing for Handling Units 70](#_Toc239510629)

[5 Appendix 72](#_Toc239510630)

[5.1 Process Integration 72](#_Toc239510631)

[5.1.1 Succeeding Processes 72](#_Toc239510632)

## Purpose

Overview

A handling unit is a physical unit consisting of packaging materials (load carriers or packing material) and the goods contained on or in it. A handling unit is always a combination of products and packaging materials. All the information contained in the product items (for example, about batches) is retained in the handling units and is always available.

This scope item sets up packaging of materials in outbound, inbound, inventory, and production, including batches and serial numbers. Because it only includes the steps for packaging, it requires a standard process scope item to work with.

This scope item does not have its own master data and only describes the steps for packing (it is not self-contained with a complete E2E process). It can be used for goods movements with handling units in inbound, production, outbound and inventory.

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
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |
| Master Data Specialist - Handling Unit Data | SAP_BR_HU_MASTER_SPECIALIST | Master Data - Handling Units | SAP_BR_HU_MASTER_SPECIALIST |  |
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Products / Product Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Production Supervisor - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC | Production Management - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC |  |
| Production Operator - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC | Production Operator - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC |  |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Production Supervisor - Repetitive Manufacturing | SAP_BR_PRODN_SUPERVISOR_RPTV | Production Management - Repetitive Manufacturing | SAP_BR_PRODN_SUPERVISOR_RPTV |  |
| Production Operator - Repetitive Manufacturing | SAP_BR_PRODN_OPTR_RPTV | Production Execution - Repetitive Manufacturing | SAP_BR_PRODN_OPTR_RPTV |  |
| Production Supervisor - Process Manufacturing | SAP_BR_PRODN_SUPERVISOR_PROC | Production Management - Process Manufacturing | SAP_BR_PRODN_SUPERVISOR_PROC |  |
| Production Operator - Process Manufacturing | SAP_BR_PRODN_OPTR_PROC | Production Execution - Process Manufacturing | SAP_BR_PRODN_OPTR_PROC |  |
| Production Planner | SAP_BR_PRODN_PLNR | Production Planning | SAP_BR_PRODN_PLNR |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the provided sample data to go through the test procedure.

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Material | TG11 | Trading Good for Reg. Trading (MRP planning) | See Business Conditions and Preliminary Steps sections. |
| Material | TG12 | Trad.Good 12,Reorder Point,Reg.Trad. | See Business Conditions and Preliminary Steps sections. |
| Material | TG20 | Trading Good for Reg. Trading (reorder point planning) | Only use if you have activated the building block Batch Management (BLG) (BLH)(BLJ) (BLP).See Business Conditions and Preliminary Steps sections. |
| Material | TG21 | Trad.Good 21,Reorder Point,Batch-FIFO | Only use if you have activated the building block Batch Management (BLG) (BLH)(BLJ) (BLP).See Business Conditions and Preliminary Steps sections. |
| Material | TG22 | Trad.Good 22,Reorder Point,Batch-ExpD | Only use if you have activated the building block Batch Management (BLG) (BLH)(BLJ) (BLP).See Business Conditions and Preliminary Steps sections. |
| Material | FG126 | Finished Good MTS for Discrete Industry (PD planning) | Only use if you have activated the building block Batch Management (BLG) (BLH)(BLJ) (BLP).See Business Conditions and Preliminary Steps sections. |
| Material | FG29 | FIN29,MTS-PI,PD,Batch-ExpirationDate |  |
| Material | SG21 | SEMI21,PD,RepetitiveManuf. |  |
| Material | TG0013 | Trad. Good 0013,PD,Regular Proc. |  |
| Sold-To Party | 33100003 | Domestic UAE Customer 3 | You can test the scope item using another domestic customer. |
| Ship-To Party | 33100003 | Domestic UAE Customer 3 |  |
| Payer | 33100003 | Customer domestic 03 |  |
| Plant | 3310 | Plant 1 AE |  |
| Plant | 3320 | Plant 2 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Storage Location | 331B | Std. storage 2 |  |
| Storage Location | 332A | Std. storage 1 |  |
| Storage Location | 331H | HU Managed STL |  |
| Shipping Point | 3310 | Shipping Point 3310 |  |
| Sales Organization | 3310 | Dom. Sales Org |  |
| Distribution Channel | 10 | Direct Sales |  |
| Division | 00 | Product Division 00 |  |
| Purchasing Organization | 3310 | Purch. Org. 3310 |  |
| Purchasing Group | 001/002 | Group 001/Group 002 |  |
| Vendor | 33300001 | Domestic UAE Supplier 1 |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BND | Create Customer Master - MDS |
| 3Y1 | Create Product Master of Type "Packaging" - MDS |

### Business Conditions

Before this scope item can be tested, the following business condition must be met.

| Scope Item | Business Condition |
| --- | --- |
| J45 - Procurement of Direct Materials | To run through this scope item, the materials must be available in stock. If you use trading goods (HAWA) you can either:Run through the Procurement of Direct Materials processOr create stock using the SAP Fiori Launchpad tile Post Goods Movement (for details see Preliminary Steps section). |
| BD9 - Sell from Stock | Go through Sell from Stock. |
| 1MI - Delivery Processing Without Order Reference | Go through Delivery Processing without Order Reference. |
| 2TX - Delivery Processing Without Order Reference | Go through Delivery Processing Without Order Reference. |
| BJH - Make-to-Stock Production – Repetitive Manufacturing | Go through Make-to-Stock Production - Repetitive Manufacturing. |
| BJ5 - Make-to-Stock Production – Discrete Manufacturing | Go through Make-to-Stock Production - Discrete Manufacturing. |
| BJ8 - Make-to-Stock – Process Manufacturing Based on Process Order | Go through Make-to-Stock - Process Manufacturing Based on Process Order. |

### Preliminary Steps

#### Configure Delivery Item Generation for Packaging Material (Optional)

Purpose

This procedure enables automatic generation of delivery items for packaging materials when the packaging itself needs to be priced, accounted for, or stock tracked like normal goods.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Filter Selection Criteria | Search for SSCUI 103665 Maintain Packaging Material Types. | All entries under the same context section are listed. |  |
| 5 | Access the SSCUI | Choose the corresponding configuration line item, find the SSCUI 103665 Maintain Packaging Material Types from Configuration Steps, and then choose Configure. | The Packaging Material Type screen displays. |  |
| 6 | Choose the Packaging Material Type | Double-click on the packaging material type you want to enable generation of the delivery item. | Detailed configuration screen displays. |  |
| 7 | Select the Field Generate Delivery Items | Make sure to select the field Generate Delivery Item.Note SAP standard packaging material types are not allowed to be modified. To enable this feature, create your own packaging material type.Double check if the proper number range has been assigned to the packaging material type. Go to SSCUI 103440 Assign Number Range Intervals to Packaging Material Type/Plant/StrgLocation. | The Generate Delivery Item field is selected. |  |
| 8 | Check the Field Plant Determination | Make sure the plant can be automatically determined. For example, B - Plant can be determined from the first item that was packed. | The plant can be automatically determined for the consumed packaging material. |  |
| 9 | Save the Configuration | Choose Save and go back to the Configure Your Solution: Realize Phase screen. | Your configuration is saved. |  |
| 10 | Filter Selection Criteria | Search for SSCUI 102123 Define Delivery Types. | All entries under the same context section are listed. |  |
| 11 | Access the SSCUI | Choose the corresponding configuration line item, find the SSCUI 102123 Define Delivery Types from Configuration Steps, and then choose Configure. | The Define Delivery Types screen displays. |  |
| 12 | Choose the Delivery Type | Double-click on the delivery type you want to enable generation of the delivery item. | Detailed configuration screen displays. |  |
| 13 | Select the Field Generation of Delivery Items for HU Packaging Materials | Make sure to select the field Generation of Delivery Items for HU Packaging Materials. | The field Generation of Delivery Items for HU Packaging Materials is selected. |  |
| 14 | Save the Configuration | Choose Save. | Your configuration is saved. |  |

SAP Central Business Configuration

| Step | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the Configuration Activity | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Maintain Packaging Material Types.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Packaging Material Type Configuration screen displays. |  |
| 3 | Choose the Packaging Material Type | Double-click on the packaging material type you want to enable the delivery item generation. | Detailed configuration screen displays. |  |
| 4 | Select the Field Generate Delivery Items | Make sure to select the field Generate Delivery Items.Note SAP standard packaging material types are not allowed to be modified. To enable this feature, create your own packaging material type.Double check if the proper number range has been assigned to the packaging material type. Go to SSCUI 103440 Assign Number Range Intervals to Packaging Material Type/Plant/StrgLocation. | The field Generate Delivery Items is selected. |  |
| 5 | Check the Field Plant Determination | Make sure the plant can be automatically determined. For example, B - Plant can be determined from the first item that was packed. | The plant can be automatically determined for the consumed packaging material. |  |
| 6 | Save the Configuration | Choose Save and go back to the Configure Your Solution: Realize Phase screen. | Your configuration is saved. |  |
| 7 | Access the Configuration Activity | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Delivery Types.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Delivery Types Configuration screen displays. |  |
| 8 | Choose the Delivery Type | Double-click on the delivery type you want to enable the delivery item generation. | Detailed configuration screen displays. |  |
| 9 | Select the Field Generation of Delivery Items for HU Packaging Materials | Make sure to select the field Generation of Delivery Items for HU Packaging Materials. | The field Generation of Delivery Items for HU Packaging Materials is selected. |  |
| 10 | Save the Configuration | Choose Save. | Your configuration is saved. |  |

#### Create Packaging Material

Purpose

This process step shows you how to create sample packaging materials.

Packaging materials are intended to enclose or hold together the materials that are to be packed. This means the material that is to be packed can be packed into or onto the packaging material.

Procedure

For detailed operations on creating packaging materials, refer to Master Data Script – Create Product Master of Type "Packaging" - MDS (3Y1). You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) .

|  |
| --- |
| Note Review your created packaging material master data:Master Data Tab/ViewFieldValue / CommentsSales: General/PlantPackaging Material TypeDouble check if delivery item should be generated for the packaging material. Change to the newly created Packaging Material Type if needed.Sales: sales org. 2Gen.item cat. Grp (General item category group)NORM applies to the packaging materials purchased from the packaging material producers. The packing dialog does not currently support returnable packaging materials.Sales: sales org. 2Item Category GroupVERP: non-billable packaging materialsVERB: billable packaging materials |

#### Define Settings to Enable Automatic Packing (Optional)

##### Display Condition Tables

Purpose

Use the SSC-UI Create Condition Tables for Packing Instructions Determination to check condition tables.

|  |
| --- |
| Note You can’t create or update condition tables, this step is just for review. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Filter Selection Criteria | Choose the following entries in filter bar and choose Enter:Application Area: LogisticsSub Application Area: Handling Unit Management | All entries display in Handling Unit Management section. |  |
| 5 | Find the Entry | Find the entry with Automatic Packing item name and choose arrow at the item end. | The Configure Your Solution - Automatic Packing screen displays. |  |
| 6 | Navigate to Create Condition Tables for Packing Instructions Determination Screen | In Configuration Steps section, choose Configure in the Actions column for Display Condition Tables for Packing Instructions Determination step. | The Change View " Display Condition Tables for Packing Instructions Determination": Overview screen displays. |  |
| 7 | Enter the Table Number | Choose the table number you want to check and Choose Display.For example,Table Number: 100 Material/ship-to party | The Display Condition Table (Packing Obj. Determ. Packing Object): Field screen displays. |  |
| 8 | Check the Selected Fields of the Table | For example, for Table 100, you can see:MaterialShip-to party |  |  |

SAP Central Business Configuration:

| Step | Step Name | Instruction | Expected Result | Example |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the Configuration Activity | Go to the Business Processes Configuration app and search for the following activity: Display Condition Tables for Packing Instructions Determination.Choose the line item in the search result to see more details about this configuration activity.Choose the Go to Activity button to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad using access level BPC_EXPERT. | The Display Condition Tables for Packing Instructions Determination screen displays. |  |
| 3 | Enter the Table Number | Choose the table number you want to check and choose Display.For example,Table Number: 100 Material/ship-to party | The Display Condition Table (Packing Obj. Determ. Packing Object): Field screen displays. |  |
| 4 | Check the Selected Fields of the Table | For example, for Table 100, you can see:MaterialShip-to party |  |  |

##### Check Access Sequences

Purpose

Use the SSC-UI Define Access Sequence for Packing Instructions Determination to maintain access sequences.

|  |
| --- |
| Note You can’t create or update condition tables, this step is just for review. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Filter Selection Criteria | Choose the following entries in filter bar and choose Enter:Application Area: LogisticsSub Application Area: Handling Unit Management | All entries display in Handling Unit Management section. |  |
| 5 | Find the Entry | Find the entry with Automatic Packing item name and choose arrow at the item end. | The Configure Your Solution - Automatic Packing screen displays. |  |
| 6 | Navigate to Define Access Sequence for Packing Instructions Determination Screen | In Configuration Steps section, choose Configure in the Actions column for Define Access Sequence for Packing Instructions Determination step. | The Change View "Define Access Sequence for Packing Instructions Determination": Overview screen displays. |  |
| 7 | Find the Entry | Choose the entry you want to check and Choose Accesses in the left of the screen.For example,SHIP: Det. Shipping/Pack. Inst. | The Change View "Define Access Sequence for Packing Instructions D.." screen displays. |  |
| 8 | Check the Access Sequence | Check the steps of the access sequence.For example,No.: 70Table Number: 110Description: Material/ship-to party/usageNo.: 80Table Number: 100Description: Material/ship-to partyNo.: 90Table Number: 90Description: Material |  |  |

SAP Central Business Configuration:

| Step | Step Name | Instruction | Expected Result | Example |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the Configuration Activity | Go to the Business Processes Configuration app and search for the following activity: Define Access Sequence for Packing Instructions Determination.Choose the line item in the search result to see more details about this configuration activity.Choose the Go to Activity button to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad using access level BPC_EXPERT. | The Define Access Sequence for Packing Instructions Determination screen displays. |  |
| 3 | Find the Entry | Choose the entry you want to check and Choose Accesses in the left of the screen.For example,SHIP: Det. Shipping/Pack. Inst. | The Change View "Define Access Sequence for Packing Instructions D.." screen displays. |  |
| 4 | Check the Access Sequence. | Check the steps of the access sequence.For example,No.: 70Table Number: 110Description: Material/ship-to party/usageNo.: 80Table Number: 100Description: Material/ship-to partyNo.: 90Table Number: 90Description: Material |  |  |

##### Maintain New Condition Types

Purpose

Use the SSC-UI Define Determination Type for Packing Instructions to maintain condition types.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Filter Selection Criteria | Choose the following entries in filter bar and press Enter:Application Area: LogisticsSub Application Area: Handling Unit Management | All entries display in Handling Unit Management section. |  |
| 5 | Find the Entry | Find the entry with Automatic Packing item name and choose arrow at the item end. | The Configure Your Solution - Automatic Packing screen displays. |  |
| 6 | Navigate to Define Determination Type for Packing Instructions Screen | In Configuration Steps section, choose Configure in the Actions column for Define Determination Type for Packing Instructions step. | The Change View "Define Determination Type for Packing Instr..": Overview screen displays. |  |
| 7 | Change the Entry | Choose the Condition Type you want to change, and change the Access Sequence and then choose Save.For example,Condition Type SHIP : Ship. pack. inst.Access Sequence: SHIP Det. Shipping/Pack. Inst | The Condition Type was saved. |  |

SAP Central Business Configuration:

| Step | Step Name | Instruction | Expected Result | Example |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the Configuration Activity | Go to the Business Processes Configuration app and search for the following activity: Define Determination Type for Packing Instr...Choose the line item in the search result to see more details about this configuration activity.Choose the Go to Activity button to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad using access level BPC_EXPERT. | The Define Determination Type for Packing Instr.. screen displays. |  |
| 3 | Change the Entry | Choose the Condition Type you want to change, and change the Access Sequence and then choose Save.For example,Condition Type SHIP : Ship. pack. inst.Access Sequence: SHIP Det. Shipping/Pack. Inst | The Condition Type was saved. |  |

##### Maintain Determination Procedures

Purpose

Use the SSC-UI Define Procedure for Packing Instructions Determination to maintain determination procedures.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Filter Selection Criteria | Choose the following entries in filter bar and press Enter:Application Area: LogisticsSub Application Area: Handling Unit Management | All entries are displayed in the Handling Unit Management section. |  |
| 5 | Find the Entry | Find the entry with Automatic Packing item name and choose the arrow icon at the end. | The Configure Your Solution - Automatic Packing screen displays. |  |
| 6 | Navigate to Define Procedure for Packing Instructions Determination Screen | In the Configuration Steps section, choose Configure in the Actions column for the Define Procedure for Packing Instructions Determination step. | The Change View "Define Procedure for Packing Instructions Determination": Overview screen displays. |  |
| 7 | Find the Entry | Select the entry you want to change and double-click Control on the left side of the screen.For example:000001: Pack in shipping | The Change View "Define Procedure for Packing Instructions D.." screen displays. |  |
| 8 | Change Procedures in Packaging Instructions | Enter the steps of Determination Types in the procedure, and choose Save.For example:Step 10: SHIP Ship. pack. inst.Step 20: STOC Whse pack. Inst.Step 30: RMAT Ref.Mat.Pack. Instr. | The procedure is saved. |  |

SAP Central Business Configuration:

| Step | Step Name | Instruction | Expected Result | Example |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the Configuration Activity | Go to the Business Processes Configuration app and search for the following activity: Define Procedure for Packing Instructions Determination.Choose the line item in the search result to see more details about this configuration activity.Choose the Go to Activity button to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad using access level BPC_EXPERT. | The Define Procedure for Packing Instructions Determination screen displays. |  |
| 3 | Find the Entry | Select the entry you want to change and double-click Control on the left side of the screen.For example:000001: Pack in shipping | The Change View "Define Procedure for Packing Instructions D. ."screen displays. |  |
| 4 | Change Procedures in Packaging Instructions | Enter the steps of Determination Types in the procedure and choose Save.For example:Step 10: SHIP Ship. pack. inst.Step 20: STOC Whse pack. Inst.Step 30: RMAT Ref.Mat.Pack. Instr. | The Procedure was saved. |  |

##### Change Procedures in Packaging Transaction Profile

Purpose

Use the SSC-UI Maintain Packing Transaction Profile to change procedures in Packaging Transaction Profile.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Filter Selection Criteria | Choose the following entries in filter bar and press Enter:Application Area: LogisticsSub Application Area: Handling Unit Management | All entries are displayed in the Handling Unit Management section. |  |
| 5 | Find the Entry | Find the entry with Automatic Packing item name and choose arrow at the item end. | The Configure Your Solution - Automatic Packing screen displays. |  |
| 6 | Navigate to Maintain Packing Transaction Profile Screen | In the Configuration Steps section, choose Configure in the Actions column for the Maintain Packing Transaction Profile step. | The Change View "Maintain Packing Transaction Profile": Overview screen displays. |  |
| 7 | Find the Entry | Double-click the entry you want to change.For example:0002: Outbound Delivery | The Change View "Maintain Packing Transaction Profile Determination": Details screen displays. |  |
| 8 | Change Procedures in Packaging Transaction Profile | Enter the field Determ. proc. for pkg instrs., and choose Save.Determ. proc. for pkg instrs: 000001 Pack in shipping | Packing Transaction Profile is saved. |  |

SAP Central Business Configuration:

| Step | Step Name | Instruction | Expected Result | Example |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the Configuration Activity | Go to the Business Processes Configuration app and search for the following activity: Maintain Packing Transaction Profile.Choose the line item in the search result to see more details about this configuration activity.Choose the Go to Activity button to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad using access level BPC_EXPERT. | The Maintain Packing Transaction Profile screen displays. |  |
| 3 | Find the Entry | Double-click the entry you want to change.For example,0002: Outbound Delivery | The Change View "Maintain Packing Transaction Profile Determination": Details screen displays. |  |
| 4 | Change Procedures in Packaging Transaction Profile | Enter the field Determ. proc. for pkg instrs., and choose Save.Determ. proc. for pkg instrs: 000001 Pack in shipping | Packing Transaction Profile is saved. |  |

#### Manage Packing Instruction

##### Create Packing Instruction

Purpose

In this step, you create a Packing Instruction.

A packing instruction serves as a template for the creation of a handling unit. In a packing instruction, you define the materials and packaging materials to be packed in a handling unit.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Handling Unit Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Packing Instruction - Master Data (POP1). | The Create Packing Instruction: Initial screen displays. |  |
| 3 | Create Packing Instruction | To create a new Packing Instruction, choose Continue or press Enter.If you want to create packing instruction from reference packing instruction, choose a reference packing instruction and press Enter. |  |  |
| 4 | Maintain the description of Packing Instruction | Enter the short text field for the description of Packing Instruction. |  |  |
| 5 | Enter Packaging Material | Enter the packaging material number created in the last section in field Component of item 10.Note The Item category P of item 10 means packaging materials. The first line is mandatory for every packing instruction because every packing instruction needs at least 1 packaging material.Note Please ensure that you have assigned the Packaging Material Type, for example, SP21 in the view Sales: General/Plant when creating the Packaging Material that you’re going to enter here. For details, refer to previous chapter Create Packaging Material. |  |  |
| 6 | Maintain material and target quantity | In item 20, make the following entries:Item category: M MaterialComponent: Material number to be packed, for example, TG11Target Quantity: 1 |  |  |
| 7 | Enter Check Profile | On the Admin.data tab, enter 01 in the Check Profile field.01 is the pre-delivered SAP Standard Profile. |  |  |
| 8 | Save | Choose Save.Make a note of the packing instruction number: _____. | A packing instruction is created. |  |

##### Create Packing Instruction Determination

Purpose

In this step, you create Packing Instruction Determination Records.

This function enables the system to find a packing instruction by specific characteristics. The condition technique is applied for this. You define a packing instruction that refers to specific characteristics, such as material and ship-to-party.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Handling Unit Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Determination Records - Master Data (POF1). | The Create Determination Recs for Pkg Instruction: Init.Screen displays. |  |
| 3 | Enter Determination Type for Outbound Delivery | On the Pkg Instruction - Create Determination Recs: Initial Screen, make the following entry, and press Enter:Determination Type: For example, SHIP, for outbound delivery |  |  |
| 4 | Choose a Key Combination | In the key combination window, choose a key combination, and choose Choose.For example, choose Material/Ship-to-Party. |  |  |
| 5 | Enter the Packing Instruction Determination | On the Create Ship. pack. inst: Fast Entry screen, make the following entries:Material: <material number>, for example, TG11Ship-to-pt: 33100003Packing instruction: <The Packing instruction number noted in the last section>. |  |  |
| 6 | Save | Choose Save. | Packing Instruction Determination Record for outbound delivery is created. |  |
| 7 | Enter Determination Type for Inbound Delivery | Choose Back.On the Pkg Instruction - Create Determination Recs: Initial Screen, make the following entries, and choose Enter:Determination Type: For example, RCPT for inbound delivery. |  |  |
| 8 | Choose a Key Combination | In the key combination window, choose a key combination, and select Choose.For example, choose Material. |  |  |
| 9 | Enter the Packing Instruction Determination | On the Create In. del. pack. ins. (RCPT) : Fast Entry screen, make the following entries:Material: <material number>, for example, TG0013Packing Instruction: <The Packing instruction number noted in the last section> |  |  |
| 10 | Save | Choose Save. | Packing Instruction Determination Record for outbound delivery is created. |  |

#### Create an Outbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create an outbound delivery for packing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist . |  |  |
| 2 | Access the App | Open Create Outbound Delivery - Without Order Reference (VL01NO). | The Create Outbound Delivery Without Order Reference screen displays. |  |
| 3 | Enter Key Data for Outbound Delivery Creation | On the Create Outbound Delivery Without Order Reference screen, make the following entries, and choose Enter:Shipping Point: 3310Delivery Type: LOSales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 4 | Enter Delivery Details | On the Delivery without Reference Create: Overview screen, make the following entries:Ship-to Party: 33100003Planned GI: <Planned goods movement date>, for example, <Today's Date>Material Number: <Material number>, for example, TG11Deliv. Quantity: Quantity , For example, 1 PCNote If any warning pop up comes, please ignore it.(Optional) Batch: batch number (for batch material only). |  |  |
| 5 | Save Document | Choose Save Document.Make a note of the delivery number: __________. | An outbound delivery is created. |  |

#### Create a Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you create a purchase order for an inbound delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Purchase Order - Advanced (ME21N). | The Create Purchase Order Advanced screen displays with a list of existing purchasing document items. |  |
| 3 | Start Purchase Order Creation | Without making any selection, choose Create. | The Create Purchase Order screen displays. |  |
| 4 | Enter Purchase Order Data | Enter all of the necessary data.Order Type: for example, NB Standard POSupplier: 33300001On the Org. Data tab:Purchasing Org.: 3310Purchasing Group: 001Company Code: 3310In the Items section:Material: <Material Number>, for example TG0013Quantity: <Quantity>Net Price: xPlant: 3310(Optional) Batch: batch number (for batch material only).In the Items section, choose Delivery Schedule:Delivery date: <date in the future>In the Items section, choose Confirmations:Conf. Control > Inbound Delivery | The Create Purchase Order screen displays. |  |

#### Create an Inbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create an inbound delivery for packing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Receiving Specialist. |  |  |
| 2 | Access the App | Open Create Inbound Delivery (VL31N). | The Create Inbound Delivery screen displays. |  |
| 3 | Create Inbound Delivery | Make the following entries and press Enter:Supplier : <enter your supplier>Purchase Order: <the created purchase document number>Delivery Date: <the delivery selection date> |  |  |
| 4 | Maintain Batch Number (Optional) | Make the following entries in Item section:Batch: <batch number> (for batch material only).You can enter a batch number manually or let system create a batch number automatically.Note This step only applies to the materials that use batch management. |  |  |
| 5 | Save | Choose Save. | The inbound delivery is created.Make a note of the delivery order number for subsequent use. ___________ |  |

#### Configure the HU Requirement Setting for Storage Location

Purpose

Use the SSC-UI HU Requirement for Storage Locations to set a storage location as Handling Unit Managed.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Filter Selection Criteria | Choose the following entries in filter bar and press Enter:Application Area: LogisticsSub Application Area: Handling Unit Management | All entries are displayed in the Handling Unit Management section. |  |
| 5 | Find the Entry | Find the entry with General Settings item name and choose arrow at the item end. | The Configure Your Solution - General Settings screen displays. |  |
| 6 | Navigate to HU Requirement for Storage Locations Screen | In Configuration Steps section, choose Configure in the Actions column for the HU Requirement for Storage Locations step. | The HU Requirement for Storage Locations screen displays. |  |
| 7 | Change HU requirement setting for Storage Location | Enter the field Partner storLoc and HU reumnt in the following line, and choose Save.Plant: 3310Storage Location: for example, 331HPartner storLoc: 331AHU reqmnt: Selected | The HU requirement settings are saved. |  |

SAP Central Business Configuration:

| Step | Step Name | Instruction | Expected Result | Example |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the Configuration Activity | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: HU Requirement for Storage Locations.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The HU Requirement for Storage Locations screen displays. |  |
| 3 | Change HU requirement setting for Storage Location | Enter the field Partner storLoc and HU reumnt in the following line, and choose Save.Plant: 3310Storage Location: for example, 331HPartner storLoc: 331AHU reqmnt: Selected | The HU requirement settings are saved. |  |

#### Create a Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The step to create a production order is described in test script Make-to-Stock Production – Discrete Manufacturing (BJ5). The production order is for a later use for processes in Discrete Manufacturing with Handling Units.

Use the following data to create the production order and then release it.

Table 2:

| Field | Value |
| --- | --- |
| Material | FG126 |
| Control Key for Operation | YBP1 |

Note down the production order number for later use.

#### Create a Process Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The step to create a process order is described in test script Make-to-Stock – Process Manufacturing Based on Process Order (BJ8). The process order is for a later use for processes in Process Manufacturing with Handling Units.

Use the following data to create the process order.

Table 3:

| Field | Value |
| --- | --- |
| Material | FG29 |
| Prodn.Supervisor | YB2 |
| Process Order Type | YBM2 |

Note down the process order number for later use.

#### Create a Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a sales order for a later use for processes in Repetitive Manufacturing with Handling Units.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. |  |  |
| 2 | Access the App | Open Create Sales Orders - VA01 (VA01). | The Create Sales Documents screen displays. |  |
| 3 | Enter Data | On the Create Sales Documents screen, make the following entries and choose Continue:Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00 | The Create Standard Order: Overview screen displays. |  |
| 4 | Enter Scheduling Agreement Details | On the Create Standard Order: Overview screen, make the following entries:Sold-To Party: 33100003Ship-To Party: 33100003Customer Reference: Sales order number from customerMaterial Number: SG21Quantity : <Quantity>, for example, 20Customer Material Number: CUST - SG21Amount : <Amount>, for example, 30 |  |  |
| 5 | Save Document | Choose Save.Make a note of the sales order number: __________. | The sales order is saved. |  |

#### Create Product Cost Collectors

Purpose

This step can only be executed if product cost planning is activated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Production. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Product Cost Collectors - Production Versions - Collective (KKF6M). | The Create Multiple Product Cost Collector for Production Versions screen displays. |  |
| 3 | Enter Relevant Values | Make the following entries and choose Execute.Plant: 3310Material: SG21Order Type: YBMROnly Repetitive Mfg Mat.: <select>Note Once the product cost collector is created, it can't be created again with the same data. |  |  |
| 6 | Exit | Choose Exit. |  |  |

## Overview Table

This scope item consists of several process steps that are listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App / Transaction | Expected Results |
| --- | --- | --- | --- |
| Execute Packing For Outbound Delivery |  |  |  |
| [Execute Manual Packing](#unique_25) [page ] 37 | Shipping Specialist | Change Outbound Delivery (VL02N) | Packing for an outbound delivery is completed. |
| [Execute Automatic Packing](#unique_26) [page ] 38 | Shipping Specialist | Change Outbound Delivery (VL02N) |  |
| [Check the Outbound Delivery](#unique_27) [page ] 40 | Shipping Specialist | Display Outbound Delivery (VL03N) | A delivery item for packing material is generated. |
| Execute Packing for Inbound Delivery |  |  |  |
| [Execute Manual Packing](#unique_28) [page ] 41 | Receiving Specialist | Change Inbound Delivery (VL32N) |  |
| [Execute Automatic Packing](#unique_29) [page ] 43 | Receiving Specialist | Change Inbound Delivery (VL32N) |  |
| Inventory Management with Handling Units |  |  |  |
| [Create Non-assigned Handling Units in Handling Unit Managed Storage Location](#unique_30) [page ] 44 | Inventory Manager | Create and Process Handling Units - Non-Assigned Handling Units (HU02) |  |
| [Transfer from Storage Location to Storage Location (Pick)](#unique_31) [page ] 46 | Inventory Manager | Post Goods Movement - Handling Units (VLMOVE) |  |
| [Transfer from Storage Location to Storage Location (Putaway)](#unique_32) [page ] 47 | Inventory Manager | Post Goods Movement - Handling Units (VLMOVE) |  |
| [Reverse Goods Movement](#unique_33) [page ] 48 | Inventory Manager | Reverse Goods Movement - Handling Units (HUCANC) |  |
| Physical Inventory with Handling Units |  |  |  |
| [Check Stock Information](#unique_34) [page ] 48 | Inventory Manager | Display Stock Overview (MMBE) |  |
| [Create Non-assigned Handling Units in Handling Unit Managed Storage Location](#unique_35) [page ] 49 | Inventory Manager | Create and Process Handling Units - Non-Assigned Handling Units (HU02) |  |
| [Create Physical Inventory Document and Perform Physical Inventory with Handling Units](#unique_36) [page ] 51 | Inventory Manager | Create Inventory Documents - Handling Units (HUINV01) |  |
| [Clear Differences from Physical Inventory Document](#unique_37) [page ] 52 | Inventory Manager | Clear Differences from Inventory Documents - Handling Units (HUINV05) |  |
| [Analyze Physical Inventory Document](#unique_38) [page ] 53 | Inventory Manager | Analyze Inventory Documents - Handling Units (HUINV04) |  |
| [Delete Inventoried Status of Handling Units](#unique_39) [page ] 54 | Inventory Manager | Display Inventory Documents - Handling Units (HUINV07) |  |
| [Delete Physical Inventory Document](#unique_40) [page ] 56 | Inventory Manager | Process Inventory Documents - Handling Units (HUINV02) |  |
| Process Manufacturing with Handling Units |  |  |  |
| Material Staging with Handling Unit |  |  |  |
| [Pick Components with Handling Unit](#unique_41) [page ] 61 | Production Operator - Process Manufacturing | Pick Components with Handling Unit (COPAWA) |  |
| [Post Goods Issue with Handling Unit](#unique_42) [page ] 62 | Production Operator - Process Manufacturing | Post Goods Issue with Handling Unit (COWBHUWA) |  |
| [Create Planned Handling Units](#unique_43) [page ] 63 | Production Supervisor - Process Manufacturing | Create Planned Handling Units (COP1) |  |
| [Create Handling Units](#unique_44) [page ] 64 | Production Supervisor - Process Manufacturing | Create Handling Units (COP2) |  |
| [Post Goods Receipt for Handling Units](#unique_45) [page ] 65 | Production Operator - Process Manufacturing | Enter Goods Receipt for Handling Units (COWBHUWE) |  |
| Discrete Manufacturing with Handling Units |  |  |  |
| [Create Planned Handling Units](#unique_46) [page ] 56 | Production Supervisor - Discrete Manufacturing. | Create Planned Handling Units (COP1) |  |
| [Create Handling Units](#unique_47) [page ] 58 | Production Supervisor - Discrete Manufacturing. | Create Handling Units (COP2). |  |
| [Post Goods Receipt for Handling Units](#unique_48) [page ] 59 | Production Operator - Discrete Manufacturing | Enter Goods Receipt for Handling Units (COWBHUWE) |  |
| Repetitive Manufacturing with Handling Units |  |  |  |
| [Create Planned Handling Units](#unique_49) [page ] 67 | Production Supervisor - Repetitive Manufacturing | Create Planned Handling Units (MFP1) |  |
| [Create Handling Units](#unique_50) [page ] 68 | Production Supervisor - Repetitive Manufacturing | Create Handling Units (MFP2) |  |
| [Confirm Repetitive Manufacturing for Handling Units](#unique_51) [page ] 70 | Production Operator - Repetitive Manufacturing | Confirm Repetitive Manufacturing for Handling Units (MFHU) |  |

## Test Procedures

This section describes procedures for each process step that belongs to this scope item.

### Execute Packing for Outbound Delivery

#### Execute Manual Packing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can execute packing for delivery items right in an outbound delivery.

|  |
| --- |
| Note To proceed with packing, make sure you go through chapters under Preliminary Steps and already have an outbound delivery created. You can also refer to standard processes in Sell from Stock (BD9) or Delivery Processing Without Order Reference (1MI) about detailed instructions regarding creation of outbound delivery. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). | The Change Outbound Delivery screen displays. |  |
| 3 | Enter the Outbound Delivery Number | On the Change Outbound Delivery screen, enter the outbound delivery number and press Enter. |  |  |
| 4 | Choose Packing | In the header section, choose Pack. |  |  |
| 5 | Select Packaging Materials | In the All Existing HUs (Available for Packing) section of the screen, enter a Packaging Material and press Enter. A Handling Unit No. is automatically generated. Select both the Material and Handling Unit line items. Validate the quantity to pack. Choose Pack.Note There are also alternative options for packing:New HU if full: If you want to pack items completely, but do not know in advance how many handling units you require.New HU per x HUs: If you want to pack a specific constant number of handling units into a higher-level handling unit.New HU per part. qty of matrl: If you are packing a delivery item completely, but want to distribute the quantity in equal amounts over several handling units. |  |  |
| 6 | Maintain Serial Numbers (Optional) | On the Total Content tab, choose the material being packed, and then choose Serial Nos..Enter the serial numbers on the Maintain Serial Numbers screen.Note This step only applies to the materials that use serial number management. |  |  |
| 7 | Check General Overview | Choose General Overview in the header section to have a visualized hierarchy of all handling units. |  |  |
| 8 | Save Your Outbound Delivery | Choose Save to save packing results and your outbound delivery. | The packing results together with the outbound delivery are saved. |  |

#### Execute Automatic Packing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can execute automatic packing for delivery items right in an outbound delivery.

Automatic packing allows you to use packing instructions to create handling units automatically in outbound deliveries. The system automatically determines the packing instructions for the materials to be packed and then the material is packed according to the packing instructions that were found.

|  |
| --- |
| Note To proceed with packing, make sure you go through chapters under Preliminary Steps and already have an outbound delivery created. You can also refer to standard processes in Sell from Stock (BD9) or Delivery Processing Without Order Reference (1MI) about detailed instructions regarding creation of outbound delivery. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). | The Change Outbound Delivery screen displays. |  |
| 3 | Enter the Outbound Delivery Number | On the Change Outbound Delivery screen, enter the outbound delivery number and press Enter. |  |  |
| 4 | Choose Packing | In the header section, choose Pack. |  |  |
| 5 | Choose Automatic Packing | On the Processing of Handling Units for Outbound Delivery screen, choose Automatic Packing. | Handling units were created automatically based on the packing instruction that was determined according to the Packing Instruction Determination you maintained in the preliminary steps. |  |
| 6 | Maintain Serial Numbers (Optional) | On the Total Content tab, choose the material being packed, and then choose Serial Nos..Enter the serial numbers on the Maintain Serial Numbers screen.In addition, the Create serial number automatically field can be set if the required serial numbers are created by the system automatically.Note This step only applies to the materials that use serial number management. |  |  |
| 7 | Check General Overview | Choose General Overview in the header section to have a visualized hierarchy of all handling units. |  |  |
| 8 | Check the Handling Units | On the General Overview screen, choose (+) of each Handling Unit to expand the line items.Check the material and quantity packed in each Handling Unit which were created according to the packing instruction in the section Create Packing Instruction. |  |  |
| 9 | Save Your Outbound Delivery | Choose Save to save packing results and your outbound delivery. | The packing results together with the outbound delivery are saved. |  |

#### Check the Outbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can check outbound delivery information in this process step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Outbound Delivery (VL03N). | The Display Outbound Delivery screen displays. |  |
| 3 | Enter the Outbound Delivery Number | On the Display Outbound Delivery screen, enter the outbound delivery number and press Enter. | The Delivery: Output screen displays. |  |
| 4 | Check the Delivery Item for Packing Material Is Generated (Optional) | If you want to deduct packaging material stock automatically, the packaging material in the outbound delivery must be generated as a delivery item. Complete [Configure Delivery Item Generation for Packaging Material (Optional)](#unique_7) [page ] 10 in Preliminary Steps.The delivery item for packaging material is generated using the following item categories:HUPM: non-billable packaging materialHUPB: billable packaging material | The delivery item for packing material is generated. |  |
| 5 | Check General Overview of Packing | In the header section, choose the Pack icon, and then navigate to the Total Content tab to have a visualized hierarchy of all handling units. | A visualized hierarchy of all handling units is displayed. |  |

### Execute Packing for Inbound Delivery

#### Execute Manual Packing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can execute packing for delivery items right in an inbound delivery.

To proceed with packing, make sure you go through chapters under Preliminary Steps and already have an inbound delivery created. You can also refer to standard procurement processes in the Scope Items about detailed instructions regarding creation of inbound delivery:

- Procurement of Direct Materials(J45)
- Logistics with Third-Party Warehouse Management (1ZQ)
- Direct Procurement with Inbound Delivery(2TX)

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Receiving Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Inbound Delivery (VL32N). | The Change Inbound Delivery screen displays. |  |
| 3 | Enter the Inbound Delivery Number | On the Change Inbound Delivery screen, enter the inbound delivery number and choose Continue. |  |  |
| 4 | Choose Packing | In the header section, choose Pack. |  |  |
| 5 | Select Packaging Materials | In the All Existing HUs (Available for Packing) section of the screen, enter a <Packaging Material> and choose Enter. A handling unit No. is automatically generated. Select both line items of material and handling unit, then choose Pack.Note There are also alternative options for packing:New HU If Full: If you want to pack items completely, but do not know in advance how many handling units you require.New HU per x HUs: If you want to pack a specific constant number of handling units into a higher-level handling unit.New HU per part. qty of matrl: If you are packing a delivery item completely but want to distribute the quantity in equal amounts over several handling units. |  |  |
| 5 | Maintain Packed Quantities | On the Total Content tab, you can maintain the Packed Quantity for each Handling Unit. |  |  |
| 6 | Maintain Serial Numbers (Optional) | To maintain serial numbers of the material that uses serial number management, you can refer to step 7 in [Execute Manual Packing](#unique_25) [page ] 37 of Chapter .Note This step only applies to the materials that use serial number management. |  |  |
| 7 | Check General Overview | Choose General Overview in the header section to have a visualized hierarchy of all handling units. |  |  |
| 8 | Save Your Inbound Delivery | Choose Save to save packing results and your inbound delivery. | Packing results together with the inbound delivery is saved. |  |

#### Execute Automatic Packing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can execute packing for delivery items right in an inbound delivery.

To proceed with packing, make sure you go through chapters under Preliminary Steps and already have an inbound delivery created. You can also refer to standard procurement processes in the Scope Items about detailed instructions regarding creation of inbound delivery:

- Procurement of Direct Materials(J45)
- Logistics with Third-Party Warehouse Management (1ZQ)
- Direct Procurement with Inbound Delivery(2TX)

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Receiving Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Inbound Delivery (VL32N). | The Change Inbound Delivery screen displays. |  |
| 3 | Enter the Inbound Delivery Number | On the Change Inbound Delivery screen, enter the inbound delivery number and choose Continue.Note Make sure the delivery you enter has the correct status and is available for packing. |  |  |
| 4 | Choose Packing | In the header section, choose Pack. |  |  |
| 5 | Choose Automatic Packing | On the Processing of Handling Units for Inbound Delivery screen, choose Automatic Packing. | Handling units were created automatically based on the packing instruction you maintained. |  |
| 6 | Maintain Serial Numbers (Optional) | To maintain serial numbers of the material that uses serial number management, you can refer to step 6 in [Execute Automatic Packing](#unique_26) [page ] 38 of chapter .Note This step only applies to the materials that use serial number management. |  |  |
| 7 | Check General Overview | Choose General Overview in the header section to have a visualized hierarchy of all handling units. |  |  |
| 8 | Check the Handling Units | In the General Overview screen, choose the (+) of each handling unit to expand the line items.Check the material and quantity packed in each handling unit which were created according to the packing instruction in the section [Create Packing Instruction](#unique_14) [page ] 22. |  |  |
| 9 | Save Your Inbound Delivery | Choose Save to save packing results and your inbound delivery. | The packing results together with the inbound delivery are saved. |  |

### Inventory Management with Handling Units

#### Create Non-assigned Handling Units in Handling Unit Managed Storage Location

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create handling units in HU-managed storage location.

Procedures

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad dis-plays. |
| 2 | Access the App | Open Create and Process Handling Units - Non-Assigned Handling Units (HU02). | The Create and Process Available Non-Assigned Handling Units screen displays. |
| 3 | Choose Pack Material | In the header section, choose Pack Material. |  |
| 4 | Select Packaging Materials | In the All Existing HUs (Available for Packing) section, enter a packaging material and choose Enter:Packaging Material: PMPALLETA handling unit number is automatically generated. | Make a note of the Handling Unit number: _____. |
| 5 | Select Material to Be Packed | In the Material to Be Packed section, enter the following data and choose Enter:Material: material number, for example, TG11Partial Qty: 5Total Quantity: 20Plant: 3310Stor. Loc.:331ADest. Stor. Location: 331H(Optional) Batch: <batch number> (for batch material only). |  |
| 6 | Pack the material | Select both line items of Material and Handling Unit, then choose New HU per part. qty of matrl. | Material is packed.Make a note of the Handling Unit numbers created: _________.Those HUs will be used in the test scenario below to perform inventory on. |
| 7 | Maintain Serial Numbers (Optional) | To maintain serial numbers of the material that uses serial number management , you can refer to step 7 in [Execute Manual Packing](#unique_25) [page ] 37 of chapter .Note This step only applies to the materials that use serial number management. |  |
| 8 | Check General Overview | Choose General Overview in the header section to have a visualized hierarchy of all handling units. |  |
| 9 | Save Packing Data | Choose Save to save the packing data. |  |

#### Transfer from Storage Location to Storage Location (Pick)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to transfer handling units from storage location to storage location (pick).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement - Handling Units (VLMOVE). | The Goods Movements for Handling Units and Materials screen displays. |  |
| 3 | Select the Data for Goods Movement | Make the following entries:Process: select Transfer from storage location to storage location (pick)Storage Location: for example, 331AHandling Units: <a handling unit you created in the previous step>Choose Copy HU.Note Do not use the handling unit number you have used in Transfer from Plant to Plant (pick) and Transfer from Plant to Plant (Putaway) topics. | The Goods Movements for Handling Units and Materials screen displays. |  |
| 4 | Post Goods Movement | In the Handling Units section, select the Handling Unit you want to move and choose Post Goods Movement. | A message appears that Packaging data was saved. Material document was created.Make a note of the created material document number: __________ |  |

#### Transfer from Storage Location to Storage Location (Putaway)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to transfer handling units from storage location to storage location (putaway).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement - Handling Units (VLMOVE). | The Goods Movements for Handling Units and Materials screen displays. |  |
| 3 | Select the Data for Goods Movement | Make the following entries:Process: select Transfer from storage location to storage location (putaway)Storage Location: Enter the storage location used in the previous step, for example, 331AHandling Units: <a handling unit you created in the previous step>Choose Copy HU. | The Goods Movements for Handling Units and Materials screen displays. |  |
| 4 | Post Goods Movement | In the Handling Units section, select the Handling Unit you want to move and choose Post Goods Movement. | A message appears that Packaging data was saved. Material document is created.Make a note of the created material document number: __________ |  |

#### Reverse Goods Movement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to reverse goods movement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Reverse Goods Movement - Handling Units (HUCANC). | The Reverse Goods Movement with Handling Units screen displays. |  |
| 3 | Select Material Document | Make the following entries:Material Document: <Material Document you noted in the previous steps>Choose Execute. | A message appears that Material document was cancelled. |  |

### Physical Inventory with Handling Units

#### Check Stock Information

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this section the stock information is checked.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Stock Overview (MMBE). | The Stock Overview screen displays. |  |
| 3 | Enter material | Make the following entries:Material: TG11Plant: 3310Storage Location: 331HChoose Execute. | The Stock Overview: Basic List screen displays. |  |
| 4 | Display Stock Information | Make a note of the unrestricted use quantity of material TG11 under storage location 331H: _____. |  |  |

#### Create Non-assigned Handling Units in Handling Unit Managed Storage Location

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create handling units in hu-managed storage location.

Procedures

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |
| 2 | Access the App | Open Create and Process Handling Units - Non-Assigned Handling Units (HU02). | The Create and Process Available Non-Assigned Handling Units screen displays. |
| 3 | Choose Pack Material | In the header section, choose Pack Material. |  |
| 4 | Select Packaging Materials | In the All Existing HUs (Available for Packing) section of the screen, enter a Packaging Material and choose Enter.Packaging Material: PMPALLETA Handling Unit Number is automatically generated. | Make a note of the Handling Unit number: _____. |
| 5 | Select Material to be Packed | In the Material to Be Packed section, enter the following data and choose Enter:Material: for example, TG11Partial Qty: for example, 5Total Quantity: for example, 20Plant: 3310Stor. Loc.: 331ADest. Stor. Location: 331H |  |
| 6 | Pack the Material | Select both line items of Material and Handling Unit, then choose New HU per part. qty of matr. | Material is packed.Make a note of the Handling Unit numbers created: ________.Those HUs will be used in the test scenario below to perform inventory on. |
| 7 | Check General Overview | Choose General Overview in the header section to have a visualized hierarchy of all handling units. |  |
| 8 | Save Packing Data | Choose Save to save the packing data. |  |

#### Create Physical Inventory Document and Perform Physical Inventory with Handling Units

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create physical inventory documentation and perform physical Inventory with handling units.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Inventory Documents - Handling Units (HUINV01). | The Select HUs and Create Physical Inventory Documents screen displays. |  |
| 3 | Select the Material | Make the following entries:Material: TG11Plant: 3310Storage Location: 331HHU with Cumulated Mat. Items: SelectedChoose Execute. | The List of All Inventoriable Handling Units screen displays. |  |
| 4 | Create Physical Inventory Document | On the selection screen, make sure to only select the HUs you have created in the prerequisite step.Choose Create physical inventory document. | A message should appear that the physical inventory document has been created.Make a note of the created physical inventory document number: __________ |  |
| 5 | Go Back to the SAP Fiori Launchpad | Choose Back and go back to the SAP Fiori launchpad. |  |  |
| 6 | Access the App | Open Enter Count Results for Inventory Documents - Handling Units (HUINV03). | The Enter Count Results for HU Inventory Docs. screen displays. |  |
| 7 | Enter the Inventory Document Number | Enter the inventory document number and choose Execute. | The Enter Count Result for Document screen displays. |  |
| 8 | Mark HUs as Existing HUs | Mark all HUs as existing by selecting the HU Exists checkbox in every row. |  |  |
| 9 | Choose the First HU | Choose the first HU and choose Inventory Items for HU. | The Inventory Items for HU screen displays. |  |
| 10 | Enter the Actual Inventory Quantity | Enter the actual physical quantity counted of material TG11, press Enter, and then choose Back. For example, 4 PCs, which is decreased by 1 PC from the original quantity. |  |  |
| 11 | Change the DoesNotExt Indicator | Change the Indicator for the last HU to DoesNotExt and choose Save. | Physical Inventory results are saved. |  |

#### Clear Differences from Physical Inventory Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to clear the physical inventory documentation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Clear Differences from Inventory Documents - Handling Units (HUINV05). | The Clear Differences from Inventory Documents screen displays. |  |
| 3 | Enter the Inventory Document Number | Enter the inventory document number created in the previous step and choose Execute. | The Post Physical Inventory screen displays. |  |
| 4 | Clear Differences from Physical Inventory Document | Choose All Items at the top of the screen and choose Select All in the table selection menu and make sure all items are selected.Choose Clear Items at the top of the screen. | A message that the physical inventory document has been posted displays. |  |
| 5 | Go Back to the SAP Fiori Launchpad | Choose Back to go back to the SAP Fiori launchpad. |  |  |
| 6 | Access the App | Open Display Stock Overview (MMBE). | The Stock Overview screen displays. |  |
| 7 | Enter Material | Make the following entries:Material: TG11Plant: 3310Storage Location: 331HChoose Execute. | The Stock Overview: Basic List screen displays. |  |
| 8 | Display Stock Information | Check the unrestricted use quantity of material TG11 under storage location 331H. | The unrestricted use quantity is updated accordingly. |  |

#### Analyze Physical Inventory Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to analyze the physical inventory documentation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Analyze Inventory Documents - Handling Units (HUINV04). | The Analysis of Phys. Inv. Docs screen displays. |  |
| 3 | Enter the Inventory Document Number | Enter the inventory document number used in the previous step, and choose Execute. | The Value Analysis of Inventory screen displays. |  |
| 4 | Check the Physical Inventory Document | Choose All Items at the top of the screen.Check the quantity in the HU and ensure that the quantity adjustments correspond to the counts you have entered in the previous step. |  |  |

#### Delete Inventoried Status of Handling Units

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to delete inventoried status of handling units.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Inventory Documents - Handling Units (HUINV07). | The Displays of Inventory Documents (incl. Deleted Items) screen displays. |  |
| 3 | Enter the Inventory Document Number | Enter the inventory document number you noted in the step [Create Physical Inventory Document and Perform Physical Inventory with Handling Units](#unique_36) [page ] 51.Choose Execute. | The Display Inventory screen displays.Make a note of the Handling Unit number(s) in the Inventory Unit: _____. |  |
| 4 | Go Back to the SAP Fiori Launchpad | Choose back to go back to the SAP Fiori launchpad. | The SAP Fiori launchpad displays. |  |
| 5 | Access the App | Open Create Inventory Documents - Handling Units (HUINV01). | The Select HUs and Create Physical Inventory Documents screen displays. |  |
| 6 | Select the Material | Make the following entries:Handling Unit: <Handling Unit number noted in step 3>Plant: 3310Storage Location: 331HHU with Cumulated Mat. Items: CheckedChoose Execute. | The purpose of this step is to reconfirm that the HUs are not available for another round of inventory.If a message with No handling units found with the required criteria is shown, that is correct. |  |
| 7 | Go back to the SAP Fiori launchpad | Choose back and go back to the SAP Fiori launchpad. | The SAP Fiori launchpad displays. |  |
| 8 | Access the App | Open Delete Inventoried Status- Handling Units. | The Delete Inventoried Status for HU screen displays. |  |
| 9 | Enter the Handling Unit Number | Make the following entries:Handling Unit: <Handling Unit number noted in step 3>Plant: 3310Storage Location: 331HChoose Execute. | The Handling Units with Status Phys. Inventoried screen displays. |  |
| 10 | Select the Handling Unit Number | Select the handling unit number and choose Save. | The handling units disappear on the list.The inventoried status of the handling unit is deleted. |  |

#### Delete Physical Inventory Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to delete the physical inventory documentation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Process Inventory Documents - Handling Units (HUINV02). | The Process a Phys. Inventory Document screen displays. |  |
| 3 | Enter the Inventory Document Number | Enter the inventory document number, and choose Execute. | The Process Inventory screen displays. |  |
| 4 | Delete the Physical Inventory Document | On the selection screen, choose the item you want to delete.Choose Delete Document at the top of the screen and choose Yes. | The physical inventory document has been deleted. |  |

### Discrete Manufacturing with Handling Units

#### Create Planned Handling Units

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create planned product Handling Units with the status planned for production orders.

|  |
| --- |
| Note In this section, we only describe the process about how to create Planned Handling Units without reference to certain customer requirements.However, to assign the creation of planned handling units for certain customer requirements to dedicated persons, you can also use the following apps:Create Planned Handling Units - Without Reference (COP11)Create Planned Handling Units - Reference to Sales Orders (COP12)Create Planned Handling Units - Reference to Deliveries (COP13)Create Planned Handling Units - Reference to Stock Transport Orders (COP14)Create Planned Handling Units - Documents due for Delivery (COPP1) |

Before you proceed with the steps below, make sure you have created a prerequisite document, for example, the production order as described in section [Create a Production Order](#unique_20) [page ] 30 in Preliminary Steps.

To continue with packing, also make sure you go through the chapters under Preliminary Steps and already have a packing instruction for material FG126 created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. |  |  |
| 2 | Access the App | Open Create Planned Handling Units (COP1).Note The default interface of the app Create Planned Handling Units (COP1) is for Create Planned Handling Units - Without Reference (COP11). You can also be redirected to app Create Planned Handling Units - Reference to Sales Orders (COP12), Create Planned Handling Units - Reference to Deliveries (COP13), Create Planned Handling Units - Reference to Stock Transport Orders (COP14) by choosing Packing for Sales Order, Pack for Delivery or Pack for stock transfer order on the top left part of the screen. | The Plan End Product HUs Without Reference to Sales Requirement screen displays. |  |
| 3 | Enter Order Number | Make the following entry and press Enter:Order: <Production Order Number from the previous step> | The quantity to be packed is displayed in the field To Be Pckd.The packing proposals are created with automatic packing.Note The packing proposals is created based on the packing instruction that was determined according to the Packing Instruction Determination you maintained in the preliminary steps. |  |
| 4 | Save the Handling Units | Choose Create and Save Handling Units. | Handling units are generated according to the HU proposals. |  |

#### Create Handling Units

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to group the material produced from a production order with handling units.

|  |
| --- |
| Note In this section, we only describe the process of how to create Handling Units without reference to certain customer requirements.However, to assign the creation of production handling units for certain customer requirements to dedicated persons, you can also use the following apps:Create Handling Units - Without Reference (COP21)Create Handling Units - Reference to Sales Orders (COP22)Create Handling Units - Reference to Deliveries (COP23)Create Handling Units - Reference to Stock Transport Orders (COP24)Create Handling Units - Documents due for Delivery (COPP2) |

Before you proceed with the steps below, make sure you have created a prerequisite document, for example, Production Order as described in section [Create a Production Order](#unique_20) [page ] 30 in Preliminary Steps.

To proceed with packing, make sure you go through chapters under Preliminary Steps and already have a packing instruction for material FG126 created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Handling Units (COP2). | The Pack End Products Without Reference to Customer Reqmt screen displays. |  |
| 3 | Enter Order Number | Make the following entries and choose Enter:Order: <Production Order Number from the previous step> | The packing proposals are created with automatic packing. |  |
| 4 | Save the Handling Units | Choose Create and Save Handling Units. | Handling units are generated according to the HU proposals. |  |

|  |
| --- |
| Note You can then continue with the processes described in scope item BJ5 - Make-to-Stock Production – Discrete Manufacturing. |

#### Post Goods Receipt for Handling Units

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post goods receipts for the material produced grouped in handling units.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Enter Goods Receipt for Handling Units (COWBHUWE) | The Enter Goods Receipt: New Item screen displays. |  |
| 3 | Enter Handling Unit Number | In the Selection of Handling Unit area, enter the number of one of the handling units you created in the previous steps and choose Enter. | The handling unit you entered displays. |  |
| 4 | Confirm the Stock Information | Check for example the quantity or storage location are correctly maintained and choose Post. | Goods receipt of handling unit is posted. |  |
| 5 | Log Off | Choose Sign Out to log off. |  |  |
| 6 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 7 | Access the App | Open Display Stock Overview (MMBE). | The Stock Overview screen displays. |  |
| 8 | Enter Material | Make the following entries:Material: FG126Plant: 3310Storage Location: 331BChoose Execute. | The Stock Overview: Basic List screen displays. |  |
| 9 | Display Handling Unit Information in Storage Location | Select the Storage Location: 331B and then open the Handling Units view by choosing Menu > Environment > Handling Unit | The HU Monitor: Selected Handling Units screen displays. |  |

|  |
| --- |
| Note You can then continue with processes described in scope item: BJ5 - Make-to-Stock Production – Discrete Manufacturing |

### Process Manufacturing with Handling Units

#### Material Staging with Handling Unit

##### Pick Components with Handling Unit

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Use this procedure to pick components for a manufacturing order and pack them into a handling unit using the Pick Components with Handling Unit (COPAWA) app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open the Pick Components with Handling Unit (COPAWA) app. | The Picking for Manufacturing Order screen displays. |  |
| 3 | Enter the Order Number | In the Order field, enter an order number, and then choose Continue. | The Picking for Manufacturing Order screen displays order data details. |  |
| 4 | Copy Open Reservation | Choose the Open Reservations tab.Select a reservation item for a material. For example: SG24. Choose Copy. | The system copies the reservation item to the Materials tab. |  |
| 5 | Enter Batch Number (Optional) | On the Materials tab, make the following entries and press Enter:Batch: <Batch Number>Storage Location: 331A | The system may display the message Batch split has been carried out. Choose Continue to dismiss the message. |  |
| 6 | Enter Packaging Material | In the Packaging Material field, enter a material, for example:PMPALLET. |  |  |
| 7 | Pack the Material | Select the material item for SG24, and then choose Pack. If an information message about the packaging material displays, choose Continue. | A handling unit number is generated and displayed in the Higher-level HU column. Make a note of the handling unit number. |  |
| 8 | Verify the Handling Unit Hierarchy | Choose the HU Hierarchy tab to verify the handling unit. |  |  |
| 9 | Confirm the Picking | Select the handling unit row, and then choose Confirm. | The picking is confirmed. |  |

##### Post Goods Issue with Handling Unit

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Use this procedure to post a goods issue for the picked components with the handling unit created in the previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open the Post Goods Issue with Handling Unit (COWBHUWA) app. | The Enter Goods Issue: New Item screen displays. |  |
| 3 | Propose the Handling Unit | In the Handling Unit field under Selection of Handling Unit, enter the handling unit number from the previous step.Choose Propose HU. | The HUs for Goods Issue Posting table displays the handling unit with detailed information.The message Handling unit XX has been transferred displays. |  |
| 4 | Post the Goods Issue | Select the handling unit row, and then choose Post. | The goods issue is posted successfully.The following message goods movements have been successfully executed displays. |  |

##### Create Planned Handling Units

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create planned product Handling Units with the status planned for process orders.

|  |
| --- |
| Note In this section, we only describe the process about how to create Planned Handling Units without reference to certain customer requirements.However, to assign the creation of planned handling units for certain customer requirements to dedicated persons, you can also use the following apps:Create Planned Handling Units - Without Reference (COP11)Create Planned Handling Units - Reference to Sales Orders (COP12)Create Planned Handling Units - Reference to Deliveries (COP13)Create Planned Handling Units - Reference to Stock Transport Orders (COP14)Create Planned Handling Units - Documents due for Delivery (COPP1) |

Before you proceed with steps below, make sure you have created a prerequisite document, for example, Process Order as described in section [Create a Process Order](#unique_21) [page ] 31 in Preliminary Steps.

To continue with packing, also make sure you go through chapters under Preliminary Steps and already have a packing instruction for material FG29 created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Process Manufacturing. |  |  |
| 2 | Access the App | Open Create Planned Handling Units (COP1). | The Plan End Product HUs Without Reference to Sales Requirement screen displays. |  |
| 3 | Enter Order Number | Make the following entry and choose Enter:Order: <Process Order Number from the previous step> | The quantity to be packed is displayed in the field To Be Pckd. The packing proposals are created with automatic packing based on the packing instruction previously created. |  |
| 4 | Save the Handling Units | Choose Create and Save Handling Units. | The handling units are generated according to the HU proposals. |  |

#### Create Handling Units

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to group the material produced from a process order with handling units.

|  |
| --- |
| Note In this section, we only describe the process of how to create Handling Units without reference to certain customer requirements.However, to assign the creation of production handling units for certain customer requirements to dedicated persons, you can also use the following apps:Create Handling Units - Without Reference (COP21)Create Handling Units - Reference to Sales Orders (COP22)Create Handling Units - Reference to Deliveries (COP23)Create Handling Units - Reference to Stock Transport Orders (COP24)Create Handling Units - Documents due for Delivery (COPP2) |

Before you proceed with the steps below, make sure you have created a prerequisite document, for example, Process Order as described in section [Create a Process Order](#unique_21) [page ] 31 in Preliminary Steps.

To proceed with packing, make sure you go through chapters under Preliminary Steps and already have a packing instruction for material FG29 created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Production Supervisor - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Handling Units (COP2) | The Pack End Products Without Reference to Customer Reqmt screen displays. |  |
| 3 | Enter Order Number | Make the following entries and choose Enter:Order: <Order Number from the previous step> | The packing proposals are created with automatic packing. |  |
| 4 | Save the Handling Units | Choose Create and Save Handling units. | Handling units are generated according to the HU proposals. |  |

|  |
| --- |
| Note You can then continue with processes described in scope item BJ8 - Make-to-Stock – Process Manufacturing Based on Process Order. |

#### Post Goods Receipt for Handling Units

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post goods receipts for the material produced grouped in handling units.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Enter Goods Receipt for Handling Units (COWBHUWE) | The Enter Goods Receipt: New Item screen displays. |  |
| 3 | Enter Handling Unit number | In the Selection of Handling Unit area, enter the number of one of the handling units you created in the previous steps and choose Enter. | The handling unit you entered displays. |  |
| 4 | Confirm the Stock Information | Check for example the quantity or storage location are correctly maintained and choose Post. | Goods receipt of handling unit is posted. |  |
| 5 | Log Off | Choose Sign Out to log off. |  |  |
| 6 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 7 | Access the App | Open Display Stock Overview (MMBE). | The Stock Overview screen displays. |  |
| 8 | Enter Material | Make the following entries:Material: FG29Plant: 3310Storage Location: 331BChoose Execute. | The Stock Overview: Basic List screen displays. |  |
| 9 | Display Handling Unit Information in Storage Location | Select the Storage Location: 331B and then open the Handling Units view by selecting Menu > Environment > Handling Unit | The HU Monitor: Selected Handling Units screen displays. |  |

|  |
| --- |
| Note You can then continue with processes described in scope item: BJ8 - Make-to-Stock – Process Manufacturing Based on Process Order |

### Repetitive Manufacturing with Handling Units

#### Create Planned Handling Units

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create planned handling units with the status planned for materials in repetitive manufacturing.

|  |
| --- |
| Note In this section, we only describe the process about how to create Planned Handling Units with reference to a Sales Order.However, to assign the creation of planned handling units for certain customer requirements to dedicated persons, you can also use the following apps:Create Planned Handling Units - Without Reference (MFP11)Create Planned Handling Units - Reference to Sales Orders (MFP12)Create Planned Handling Units - Reference to Deliveries (MFP13)Create Planned Handling Units - Reference to Stock Transport Orders (MFP14)Create Planned Handling Units - Documents due for Delivery (MFPP1) |

Before you proceed with the steps below, make sure you have created a prerequisite document, for example, a sales order as described in section [Create a Sales Order](#unique_22) [page ] 31 in Preliminary Steps. You can also create a planned order directly. For details, refer to scope item Make-to-Stock Production – Repetitive Manufacturing (BJH).

To proceed with packing, make sure you go through the chapters under Preliminary Steps and already have a packing instruction for material SG21 created.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Repetitive Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Planned Handling Units (MFP1). | The Plan End Product HUs Without Reference to Sales Requirement screen displays. |  |
| 3 | Choose Packing for Sales Order | Choose Packing for Sales Order. | The Plan End Product HUs for Sales Order screen displays. |  |
| 4 | Enter Order Number | Make the following entries and choose Enter:Sales Order: <Sales Order Number from the previous prerequisite step>Item: 10Plant: 3310Storage Loc: 331ATo Be Pckd: <Quantity>, for example, 20 | The packing proposals are created with automatic packing based on the packing instruction previously created. |  |
| 5 | Save the Handling Units | Choose Create and Save Handling Units. | Handling units are generated according to the HU proposals. |  |

#### Create Handling Units

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to group the material produced in repetitive manufacturing with handling units.

|  |
| --- |
| Note In this section, we only describe the process of how to create Handling Units without reference to certain customer requirements.However, to assign the creation of production handling units for certain customer requirements to dedicated persons, you can also use the following apps:Create Handling Units - Without Reference (MFP21)Create Handling Units - Reference to Sales Orders (MFP22)Create Handling Units - Reference to Deliveries (MFP23)Create Handling Units - Reference to Stock Transport Orders (MFP24)Create Handling Units - Documents due for Delivery (MFPP2) |

Before you proceed with the steps below, make sure you have created a prerequisite document, for example, Production Order as described in section [Create a Production Order](#unique_20) [page ] 30 in Preliminary Steps.

To proceed with packing, make sure you go through chapters under Preliminary Steps and already have a packing instruction for material SG21 created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Repetitive Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Handling Units (MFP2). | The Repetitive Manufacturing: Create Plnnd HUs w/o Ref. to Ord. screen displays. |  |
| 3 | Enter order number | Make the following entries and choose Enter:Material: SG21Plan: 3310Stor.Loc: 331BBatch(Optional): | The packing proposals are created with automatic packing. |  |
| 4 | Save the Handling Units | Choose Create and Save Handling Units. | Handling units are generated according to the HU proposals. |  |
| 5 | Confirm Handling Units | Refer to [Confirm Repetitive Manufacturing for Handling Units](#unique_51) [page ] 70 to confirm the generated handling units. | Handling units generated are confirmed. |  |

|  |
| --- |
| Note You can then continue with processes described in scope item BJH - Make-to-Stock Production – Repetitive Manufacturing. |

#### Confirm Repetitive Manufacturing for Handling Units

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to confirm handling units created in packing for repetitive manufacturing where you post the goods receipt of the contained materials and the goods issue of the components in one step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Repetitive Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Confirm Repetitive Manufacturing for Handling Units (MFHU) | The HU Backflush in Repetitive Manufacturing screen displays. |  |
| 3 | Enter Handling Unit Number | Enter the number of one of the handling units you created in the previous steps and choose Enter:Handling Unit: <Handling Unit number>Note You can also confirm repetitive manufacturing from requirement of planned orders. This process is described in Scope Item BJH Make-to-Stock Production – Repetitive Manufacturing. | The handling unit you entered displays. |  |
| 4 | Enter and Confirm the Stock Information | Check for example the quantity and Production Version are correctly maintained and choose Save. | The message Handling unit backflush completed displays. Goods receipt of contained materials and the goods issue of the components. |  |
| 5 | Log Off | Choose Sign Out to log off. |  |  |
| 6 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 7 | Access the App | Open Display Stock Overview (MMBE). | The Stock Overview screen displays. |  |
| 8 | Enter Material | Make the following entries:Material: SG21Plant: 3310Storage Location: 331BChoose Execute. | The Stock Overview: Basic List screen displays. |  |
| 9 | Display Handling Unit Information in Storage Location | Select the Storage Location: 331B and then open the Handling Units view by selecting Menu > Environment > Handling Unit | The HU Monitor: Selected Handling Units screen displays. |  |

|  |
| --- |
| Note You can then continue with processes described in scope item: BJH - Make-to-Stock Production – Repetitive Manufacturing |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Scope Item | Comment |
| --- | --- |
| BD9 - Sell from Stock | Go through steps after chapter Handling Unit Management (Optional) in BD9 - Sell from Stock |
| 1MI - Delivery Processing Without Order Reference | Go through steps after chapter Execute Packing (Optional) in 1MI - Delivery Processing without Order Reference. |
| 2TX - Direct Procurement with Inbound Delivery | Go through steps after chapter Create Inbound Deliveries. |
| BJH - Make-to-Stock Production – Repetitive Manufacturing | Go through Make-to-Stock Production - Repetitive Manufacturing. |
| BJ5 - Make-to-Stock Production – Discrete Manufacturing | Go through Make-to-Stock Production - Discrete Manufacturing. |

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
- see-also :: [[11-inventory-warehouse-and-transportation/test-script-warehouse-internal-repacking-3bw-ae-925]]
- see-also :: [[02-business-partner-and-product-master-data/stammdatenskript-produktstamm-vom-typ-verpackung-anlegen-sds-3y1-388]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4MM_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 121,501 chars in the whole document
