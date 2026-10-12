---
id: 11-inventory-warehouse-and-transportation/test-script-warehouse-outbound-processing-3bs-ae-sap-s-4hana-cloud-pub
title: "Test Script: Warehouse Outbound Processing (3BS_AE) - SAP S/4HANA Cloud Public Edition (3BS_S4CLD2608_BPD_EN_AE)"
description: "SAP test script for scope item 3BS (AE), Public Edition 2608: setup prerequisites and test steps for warehouse outbound picking, packing, loading, goods issue."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/ewm-outbound-to-customer]
aliases: [3BS_S4CLD2608_BPD_EN_AE]
keywords: [EWM Outbound Processing to Customer, warehouse outbound processing, test procedures, pick warehouse tasks, warehouse task confirmation, handling unit packing, radio frequency devices, serial numbers, advanced shipping and receiving, post goods issue]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3BS_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-922
topic: 11-inventory-warehouse-and-transportation/ewm-outbound-to-customer
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Warehouse Outbound Processing (3BS_AE) - SAP S/4HANA Cloud Public Edition (3BS_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3BS_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **EWM Outbound Processing to Customer** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Warehouse Outbound Processing (3BS_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232852200)

[2 Prerequisites 4](#_Toc232852201)

[2.1 System Access 4](#_Toc232852202)

[2.2 Roles 4](#_Toc232852203)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232852204)

[2.4 Additional Manual Configuration 8](#_Toc232852205)

[2.5 Business Conditions 8](#_Toc232852206)

[2.6 Preliminary Steps 9](#_Toc232852207)

[2.6.1 Define Default Values for Warehouse Clerk (EWM) 9](#_Toc232852208)

[2.6.2 Define Default Values for Warehouse Operative (EWM) 10](#_Toc232852209)

[2.6.3 Create Loading Point (Optional) 11](#_Toc232852210)

[2.6.4 Assign Door to Loading Point (Optional) 11](#_Toc232852211)

[2.6.5 Staging Area and Door Determination (Outbound) 12](#_Toc232852212)

[2.6.5.1 Variant 1:Without Advanced Shipping and Receiving 12](#_Toc232852213)

[2.6.5.2 Variant 2: With Advanced Shipping and Receiving (Optional) 13](#_Toc232852214)

[2.6.6 Access Sequence to Staging Areas and Door Determination 14](#_Toc232852215)

[2.6.7 Define Favorite Packaging Materials 15](#_Toc232852216)

[2.6.8 Manage Packing Instruction 16](#_Toc232852217)

[2.6.8.1 Create Packing Instruction 16](#_Toc232852218)

[2.6.8.2 Create Packing Instruction Determination 17](#_Toc232852219)

[2.6.9 Set up Output Parameter Determination for Printing Delivery Note 18](#_Toc232852220)

[3 Overview Table 20](#_Toc232852221)

[4 Test Procedures 22](#_Toc232852222)

[4.1 Assign Carrier (Optional) 22](#_Toc232852223)

[4.2 Create Pick Warehouse Tasks 23](#_Toc232852224)

[4.3 Confirm Pick Warehouse Tasks 24](#_Toc232852225)

[4.3.1 Variant 1: With Fiori App 24](#_Toc232852226)

[4.3.2 Variant 2: With Radio Frequency Devices 25](#_Toc232852227)

[4.4 Pack Goods into Shipping Handling Units (Optional) 27](#_Toc232852228)

[4.4.1 Variant 1: With Fiori App - Pack Outbound Deliveries 27](#_Toc232852229)

[4.4.2 Variant 2: With Fiori APP - Pack Handling Units – Advanced (/SCWM/PACK) 29](#_Toc232852230)

[4.4.3 Variant 3: With Radio Frequency Devices 30](#_Toc232852231)

[4.5 Enter Serial Number for Outbound Delivery Order (Optional) 32](#_Toc232852232)

[4.6 Set Deliveries to Ready for Shipping (Optional) 33](#_Toc232852233)

[4.7 Check Printed Delivery Note before Goods Issue (Optional) 34](#_Toc232852234)

[4.8 Print Loading Instruction (Optional) 35](#_Toc232852235)

[4.9 Loading (Optional) 36](#_Toc232852236)

[4.9.1 Variant 1: With Fiori App 37](#_Toc232852237)

[4.9.2 Variant 2: With Radio Frequency Devices 39](#_Toc232852238)

[4.10 Post Goods Issue 40](#_Toc232852239)

[4.11 Reverse Post Goods Issue (Optional) 41](#_Toc232852240)

[4.11.1 Reverse Goods Issue 42](#_Toc232852241)

[4.11.2 Release Stock 43](#_Toc232852242)

[4.11.3 Adjust Delivery Quantity 44](#_Toc232852243)

[4.11.4 Trigger Delivery Update 45](#_Toc232852244)

[5 Appendix 47](#_Toc232852245)

[5.1 Access Code Handling 47](#_Toc232852246)

[5.2 Attachment Handling 47](#_Toc232852247)

[5.3 Create Warehouse Task with Job Scheduling 48](#_Toc232852248)

[5.4 Process Integration 48](#_Toc232852249)

[5.4.1 Preceding Processes 48](#_Toc232852250)

[5.4.2 Succeeding Processes 55](#_Toc232852251)

## Purpose

Overview

With this process, products are picked, packed, and sent from your warehouse. This scope item supports different outbound process scenarios. For example, you can send ordered products to external customers, return products to suppliers, and supply products to internal customers.

The process starts with an outbound delivery that is relevant for processing in the warehouse. Warehouse tasks are created based on the outbound delivery. The physical process for picking is executed and then confirmed. If packing is required, a warehouse worker packs the products into shipping handling units. Serial numbers are captured in different steps depending on whether the product is managed on documentation level (documentation serialization) or stock level (serialization in stock). Finally, the goods issue is posted.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

|  |
| --- |
| Caution Testing in a 3-System LandscapeIn a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version (see the following [link](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/TestScripts/3BS_S4CLD2602_BPD_EN_AE.docx) ). |

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
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |
| Master Data Specialist - Handling Unit Data | SAP_BR_HU_MASTER_SPECIALIST | Master Data - Handling Units | SAP_BR_HU_MASTER_SPECIALIST |  |
| Master Data Specialist - Transportation Management | SAP_BR_TRANSP_MDSPEC | Transportation Master Data | SAP_BR_TRANSP_MDSPEC |  |
| Master Data Specialist - Handling Unit Data | SAP_BR_HU_MASTER_SPECIALIST | Master Data - Handling Units | SAP_BR_HU_MASTER_SPECIALIST |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | TG11 | Trading Good for Reg. Trading (MRP planning) | Storage |
| Material | TG12 | Trad.Good 12,Reorder Point,Reg.Trad. | Fixed Bin Storage |
| Material | TG14 | Trading material (Reorder point planning, bought in item) no batch | For process BDN – Sales of Non-Stock Item with Order-Specific Procurement. See Appendix > Process Integration > Preceding Processes chapter |
| Material | TG0016 | Trad. Good 0016,Reg. Proc. Serial No | General Storage, used for process with Serial Number. Documentation Serialization |
| Material | TG0018 | Trading Good 0018,PD,Regular Proc. | General Storage, used for process with Serial Number. Serialization on Stock |
| Material | TG21 | Trad.Good 21,Reorder Point,Batch-FIFO | Bulk Storage |
| Material | TG23 | Trad.Good 23,Reorder Point,Batch,Serialnr | Batch-managed with Serial Number Profile |
| Material | RM124 | RAW124,VB,Consumption,FixedBin |  |
| Material | TG0011 | Trading Good 0011,PD,Regular Proc. | General Storage |
| Material | TG0013 | Trad. Good 0013,PD,Regular Proc. | General Storage |
| Material | FGJIT03 | JIT Dummy Material for EWM Integration | General Storage |
| Material | RP001 | Empties,ND | General Storage |
| Material | SDBOMERLAHD | SD BOM Header ERLA (with Pricing, inventory management) | General Storage |
| Material | SDBOMLUMFHD | SD BOM Header LUMF(No pricing, no inventory) | General Storage |
| Packaging Material | PMPALLET | Pallet |  |
| Packaging Material | PMCARTON | Carton |  |
| Packaging Material | PMWIREBASKET | Wire basket |  |
| Packaging Material | PMPALLET_GTL | Pallet for GTL |  |
| Packaging Material | PMCARTON_GTL | Carton for GTL |  |
| Packaging Material | PMWIREBASKET_GTL | Wire basket for GTL |  |
| Carrier | 33300001 | Domestic AE Supplier 1 |  |
| Company Code | 3310 | Company Code 3310 |  |
| Purchase Organization | 3310 | Purchase Organization 3310 |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 335W | Storage Location for Cloud WM |  |
| ERP Warehouse | 335 | Warehouse |  |
| EWM Warehouse | 3350 | Warehouse |  |
| Custodian | 33413310 | Business Partner for Plant 3341 |  |
| Entitled to Dispose | 33413310 | Business Partner for Plant 3341 |  |
| Division | 00 | Product Division 00 |  |
| Distribution Channel | 10 | Direct Sales |  |
| Shipping Point | 3310 | Shipping Point 3310 |  |
| Ship to party | 33100003 | Domestic UAE Customer 3 |  |
| Sold to party | 33100003 | Domestic UAE Customer 3 |  |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BND | Create Customer Master - MDS |
| 2YX | Create Customer-Material Info Record - MDS |
| 3KS | Maintain Production Supply Area - MDS |
| 3KR | Maintain Storage Bins and Fixed Bin Assignments - MDS |
| 3KQ | Maintain Warehouse Products Attributes - MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/e61afa140c8f77e384eeb729750780bc)

Before you start the testing, please make sure that the steps in the [Warehouse Management Setup Guide.docx (Public)](https://support.sap.com/content/dam/SAAP/SAP_Activate/S4H_588%20Warehouse%20Management%20Setup.docx) published on SAP Activate Roadmap Viewer have been completed.

If you are working with a radio frequency device, carry out the steps described in Mobile RF Devices in Warehousing (63V).

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| All Scope Items |  |
| BNZ - Create New Open MM Posting Period - MDS | A new posting period was created as part of process BNZ - Create New Open MM Posting Period - MDS (Master Data Script).The posting period is up to date. |
| 2Q2 - Data Migration to SAP S/4HANA from Staging | This scope item is used as a predecessor.You can use the Migration Cockpit for setting up your warehouse stock with a provided template.This is option 1 of 3. You can also get stock via processing Scope Item 3BR - Warehouse Inbound Processing or 5HN - Warehouse Inbound Processing with Synchronous Goods Receipt. |
| 3BR - Warehouse Inbound Processing | This scope item is used as a predecessor.This is option 2 of 3, you can also get stock via processing the Scope Item 2Q2 - Data Migration to SAP S/4HANA from Staging or 5HN - Warehouse Inbound Processing with Synchronous Goods Receipt. |
| 5HN - Warehouse Inbound Processing with Synchronous Goods Receipt | This scope item is used as a predecessor.This is option 3 of 3, you can also get stock via processing the Scope Item 2Q2 - Data Migration to SAP S/4HANA from Staging or 3BR - Warehouse Inbound Processing. |
| Outbound to External Customer |  |
| BD9 - Sell from Stock | Complete the activity (Create Sales Order, Create Delivery) described in the test script.At the Create Sales Order step, before saving the delivery, select the order item and then choose More > Go to > Item > Shipping . In the Shipping section, enter the Stor.Loc. value of the warehouse-managed Storage Location (for example Storage Location 335W).Use the master data from this document. |

### Preliminary Steps

#### Define Default Values for Warehouse Clerk (EWM)

Use

In this step, you define the default warehouse number for the Warehouse Clerk (EWM).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log onto SAP Fiori Launchpad | Open the Fiori launchpad as Warehouse Clerk (EWM) |  |  |
| 2. | Choose the User Icon | Choose the Icon for the logon user.Choose Settings. |  |  |
| 3. | Enter Default Value | Choose Default Values.Make the following entry in the section Material Management:Warehouse No.: 3350Choose Save. |  |  |

#### Define Default Values for Warehouse Operative (EWM)

Use

In this step, you define the default warehouse number for the Warehouse Operative (EWM).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log onto SAP Fiori Launchpad | Open the Fiori launchpad as Warehouse Operative (EWM). |  |  |
| 2. | Choose the User Icon | Choose the Icon for the logon user.Choose Settings. |  |  |
| 3. | Enter Default Value | Choose Default Values.Make the following entry in the section Material Management:Warehouse No.:3350Choose Save. |  |  |

#### Create Loading Point (Optional)

Use

In this step, you create a loading point, which represents a collection of doors.

|  |
| --- |
| Note This setting is one of the prerequisite settings for using the Advanced Shipping and Receiving in the Cloud Warehouse Management. If the Advanced Shipping and Receiving is irrelevant to your business, you can skip this step. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Open the SAP Fiori launchpad with the Master Data Specialist - Transportation Management role. | The SAP Fiori launchpad is displayed. |  |
| 2. | Access the App | Open Manage Locations (F6225). | The Manage Location Master (F6225) screen displays. |  |
| 3. | Create New Location | On the Manage Locations screen, choose Create and make the following entries:Location: for example LP01.Location Type: Loading Point (1200)Choose Continue. |  |  |
| 4. | Enter Information | On the Location screen, make the following entries:Loc. Description: <description for location>Choose Create.Note Information such as address and identifcation are optional. | Message Object Created appears. |  |

#### Assign Door to Loading Point (Optional)

Use

In this step, you assign one door or several doors to a loading point.

For detailed steps on defining doors, please refer to the corresponding step in the [Warehouse Management Setup Guide.docx (Public)](https://support.sap.com/content/dam/SAAP/SAP_Activate/S4H_588%20Warehouse%20Management%20Setup.docx) published on SAP Activate Roadmap Viewer.

|  |
| --- |
| Note This setting is one of the prerequisite settings for using the Advanced Shipping and Receiving in the Cloud Warehouse Management. If the Advanced Shipping and Receiving is irrelevant to your business, you can skip this step. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Open the SAP Fiori launchpad with the Warehouse Clerk (EWM) role. | The SAP Fiori launchpad is displayed. |  |
| 2. | Access the App | Open Assign Warehouse Door (/SCWM/DOOR_SCU) | The Assign Warehouse Door (/SCWM/DOOR_SCU) screen displays. |  |
| 3. | Assign | On the Assign Warehouse Door screen, make the following entries:Whse Door: DR01Loading Point: LP01.Whse Door: DR02Loading Point: LP01.Choose Save.Note You will not be able to create new entries in this App. It is only possible to assign existing doors to loading points. |  |  |

#### Staging Area and Door Determination (Outbound)

Use

In this step, you define the logic in the outbound process to determine which outbound delivery order with respective materials should go to which Storage Bin in the Outbound Staging Area. This can help you distribute your materials by, for example carriers, for a better separation and planning.

##### Variant 1:Without Advanced Shipping and Receiving

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Open the SAP Fiori launchpad with the Warehouse Clerk (EWM) role. | The SAP Fiori launchpad is displayed. |  |
| 2. | Access the App | Open Determine Staging Area - Outbound (/SCWM/STADET_OUT) | The Determine Staging Area - Outbound (/SCWM/STADET_OUT) screen displays. |  |
| 3. | Create new entries | Create the first entry with the following values:Warehouse Number:3350.Sequence Number: 1Carrier: 33300001Staging Bay: GI-AREA-02Stg. Area Group: S920Choose Save. |  |  |
| 4. | Create new entries | Create the second entry with the following values:Warehouse Number: 3350Sequence Number: 1Staging Bay: GI-AREA-01Stg. Area Group: S920Whse Proc. Type: S210Choose Save. |  |  |

##### Variant 2: With Advanced Shipping and Receiving (Optional)

|  |
| --- |
| Note This setting is one of the prerequisite settings for using the Advanced Shipping and Receiving in the Cloud Warehouse Management. If the Advanced Shipping and Receiving is irrelevant to your business, you can skip this step. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Open the SAP Fiori launchpad with the Warehouse Clerk (EWM) role. | The SAP Fiori launchpad is displayed. |  |
| 2. | Access the App | Open Determine Staging Area - Outbound (/SCWM/STADET_OUT) | The Determine Staging Area - Outbound (/SCWM/STADET_OUT) screen displays. |  |
| 3. | Create new entries | Create the first entry with the following values:Warehouse Number:3350.Sequence Number: 1Carrier: 33300001Staging Bay: GI-AREA-02Stg. Area Group: S920Warehouse Door: DR02Choose Save. |  |  |
| 4. | Create new entries | Create the second entry with the following values:Warehouse Number: 3350Sequence Number: 1Whse Proc. Type: S210Staging Bay: GI-AREA-01Stg. Area Group: S920Warehouse Door: DR01Choose Save. |  |  |

#### Access Sequence to Staging Areas and Door Determination

Use

In this step, you create the access sequence that defines which combination of fields the system should use while searching for a match between the attributes of an out-bound document and a set of determination rules. The matching determination rule that the system finds is used to determine to which staging area a delivery item should be sent.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log onto SAP Fiori Launchpad | Open the SAP Fiori launchpad with the Warehouse Clerk (EWM) role. | The SAP Fiori launchpad is displayed. |  |
| 2. | Access the App | Open Define Access Sequence - Staging Areas - Outbound (/SCWM/STADET_ASS_OUT) | The Define Access Sequence - Staging Areas - Outbound screen displays. |  |
| 3. | Create New Entries | First Door DeterminationWarehouse Number: 3350Access Sequence Number: 1Use Carrier: XChoose Save. | Should be created. |  |
| 4. | Create New Entries | Second Door DeterminationWarehouse Number: 3350Access Sequence Number: 2Use Whse Proc. Type: XChoose Save. | Should be created. |  |

#### Define Favorite Packaging Materials

Use

In this step, you define the packaging material(s) that will be proposed when creating handling units at specific work centers.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Open the SAP Fiori launchpad with the Warehouse Clerk (EWM) role. | The SAP Fiori launchpad is displayed. |  |
| 2. | Access the App | Open Define Favorite Packaging Materials (/SCWM/TWSPACKMAT) | The Define Favorite Packaging Materials (/SCWM/TWSPACKMAT) screen is displays. |  |
| 3. | Enter Warehouse Number | At first, the dialog box displays Determine Work Area: Entry displays. Make the following entry:Warehouse Number: 3350Choose Continue. | The Define Favorite Packaging Materials screen is displays. |  |
| 4. | Switch the Mode | Choose Edit on the upper right. | The screen name changes to Define Favorite Packaging Materials: Change. |  |
| 5. | Choose New Entries | Once you have switched the mode, you can see different options.Choose New Entries. | The gray fields are open for editing your required packaging materials now. |  |
| 6. | Fill in Required Entries | Work Center: PackProduct: for example PMPALLETChoose Save. | A dialog box with the message Data was saved appears in the right corner. |  |

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
| 9 | Create Alternative Packing Instructions | Repeat step 2-8 to create an alternative Packing Instruction with the same component but different packing material and quantity. |  |  |

##### Create Packing Instruction Determination

Purpose

In this step, you create packing instruction determination records.

This function enables the system to find a packing instruction by specific characteristics. The condition technique is applied for this. You define a packing instruction that refers to specific characteristics, such as material and ship-to-party.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Handling Unit Data | The SAP Fiori launchpad is displays. |  |
| 2 | Access the App | Open Create Determination Records - Master Data (POF1) | The Pkg Instruction - Create Determination Recs: Initial Screen is displayed. |  |
| 3 | Enter Determination Type | On the Pkg Instruction - Create Determination Recs: Initial Screen, make the following entries, and choose Enter.Determination Type: 0OBD – Outbound Delivery.Choose Enter. |  |  |
| 4 | Choose a key combination | On the key combination screen, choose a key combination, and select Choose.For example, choose Material/ship-to party. |  |  |
| 5 | Enter the Packing Instruction Determination | On the Create Outbound Delivery (0OBD): Fast Entry screen, make the following entries:Material: for example, TG11Ship-to pt: <The customer number>Packing instruction: <The Packing instruction number noted in the previous section>Altern.pack.instr. 1: <The Alternative Packing instruction number noted in the previous section> |  |  |
| 6 | Save | Choose Save. | The packing instruction determination is created. |  |

#### Set up Output Parameter Determination for Printing Delivery Note

Purpose

In this step, you set up the Output Parameter Determination for printing a Delivery Note immediately when the Ready for Shipping status is set in the Outbound Delivery Order..

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Administrator | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Output Parameter Determination (APOC_WD_BRF_DEC_TAB_MAINTAIN). |  |  |
| 3 | Select Business Rules | Select the following business rules from the drop-down list:Show Rules for: Outbound DeliveryDetermination Step: Output Relevance |  |  |
| 4 | Maintain Business Rules | Choose Edit to switch to edit mode.Under Table Contents, select the checkbox of the first table entry and choose on the + icon to insert a new row into the Decision Table. In doing so, you should get the very first entry in the decision table.Note The Decision Table is processed sequentially, therefore the table entries should be arranged starting with the most specific ones, followed by more general ones. For productvie use, customers need to check that if parameters make sense. You can use – to remove row and use Move UP or Move Down to adjust the row sequence. |  |  |
| 5 | Enter Table Contents | Choose the three dots (…) below each field to enter conditions for the new entry and choose OK to confirm the inputs:Output Type is equal to DELIVERY_NOTEDocument Cat. - SD Document Category is equal to J (Delivery)StatDecntrlWhse contains any B,CWarehouse Execution is equal to 4 (Delivery is ready for Shipping)Relevance Indicator: X (true)Note If any of the above mentioned field does not exist in the table, you can choose Table Settings, then choose Insert Column > From Context Data Objects to add the required field into the table. |  |  |
| 6 | Check Object Consistency | Choose Activate to check object consistency and make the object active for productive use.In the Confirm Activation dialog box, choose Yes to activate. | A success message should be displayed. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App / Transaction |
| --- | --- | --- |
| [Assign Carrier (Optional)](#unique_23) [page ] 22 | Warehouse Clerk (EWM) | Manage Outbound Delivery Orders (F6498) |
| [Create Pick Warehouse Tasks](#unique_24) [page ] 23 | Warehouse Clerk (EWM) | Manage Outbound Delivery Orders (F6498) |
| [Confirm Pick Warehouse Tasks](#unique_25) [page ] 24 |  |  |
| [Variant 1: With Fiori App](#unique_26) [page ] 24 | Warehouse Operative (EWM) | Process Warehouse Tasks (F4595) |
| [Variant 2: With Radio Frequency Devices](#unique_27) [page ] 25 | Warehouse Operative (EWM) | Test RF Environment (/SCWM/RFUI) |
| Pack Goods into Shipping Handling Units (Optional) |  |  |
| [Variant 1: With Fiori App - Pack Outbound Deliveries](#unique_28) [page ] 27 | Warehouse Operative (EWM) | Pack Outbound Deliveries (F3193) |
| [Variant 2: With Fiori APP - Pack Handling Units – Advanced (/SCWM/PACK)](#unique_29) [page ] 29 | Warehouse Operative (EWM) | Pack Handling Units - Advanced (/SCWM/PACK) |
| [Variant 3: With Radio Frequency Devices](#unique_30) [page ] 30 | Warehouse Operative (EWM) | Test RF Environment (/SCWM/RFUI) |
| [Enter Serial Number for Outbound Delivery Order (Optional)](#unique_31) [page ] 32 | Warehouse Clerk (EWM) | Manage Outbound Delivery Orders (F6498) |
| [Set Deliveries to Ready for Shipping (Optional)](#unique_32) [page ] 33 | Warehouse Clerk (EWM) | Manage Outbound Delivery Orders (F6498) |
| [Check Printed Delivery Note before Goods Issue (Optional)](#unique_33) [page ] 34 | Shipping Specialist | Change Outbound Delivery (VL02N) |
| [Print Loading Instruction (Optional)](#unique_34) [page ] 35 | Warehouse Clerk (EWM) | Manage Outbound Delivery Orders (F6498) |
| [Loading (Optional)](#unique_35) [page ] 36 | Warehouse Clerk (EWM) | Load or Unload Freight Orders (/SCMTMS/ASR) |
| [Post Goods Issue](#unique_36) [page ] 40 | Warehouse Clerk (EWM) | Manage Outbound Delivery Orders (F6498) |
| [Reverse Post Goods Issue (Optional)](#unique_37) [page ] 41 |  |  |
| [Reverse Goods Issue](#unique_38) [page ] 42 | Warehouse Clerk (EWM) | Manage Outbound Delivery Orders (F6498) |
| [Release Stock](#unique_39) [page ] 43 | Warehouse Clerk (EWM) | Manage Outbound Delivery Orders (F6498) |
| [Adjust Delivery Quantity](#unique_40) [page ] 44 | Warehouse Clerk (EWM) | Manage Outbound Delivery Orders (F6498) |
| [Trigger Delivery Update](#unique_41) [page ] 45 | Warehouse Clerk (EWM) | Manage Outbound Delivery Orders (F6498) |

## Test Procedures

This section describes the test procedures for each process step that belongs to this scope item.

This Testscript describes all steps which are required to execute the outbound process from the product perspective.

You can execute the process also from HU perspective, but then you have some different steps especially related to material TG21 in step Confirm Pick Warehouse Tasks.

### Assign Carrier (Optional)

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
| 1 | Log onto SAP Fiori Launchpad | Open the SAP Fiori Launchpad with the Warehouse Clerk (EWM) role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Outbound Delivery Orders (F6498). | The Manage Outbound Delivery Orders (F6498) screen displays. |  |
| 3 | Enter Warehouse Number | Warehouse No: Enter your Warehouse Number, for example 3350. |  |  |
| 4 | Set Departure Date / Time for Route value | Departure Date for Route: Select the date/time range that your Outbound Delivery Order falls inChoose Go. | Your outbound delivery orders is visible now. |  |
| 5 | Select your Outbound Delivery Order | Select your delivery and choose Edit(1). | The Edit(1) dialog box displays. |  |
| 6 | Assign a Carrier | In the Edit(1) dialog box, select <Use Value Help> from the drop-down menu.In the Select: Carrier window, select a carrier of your choice, for example.33300001 and choose Save. |  |  |

### Create Pick Warehouse Tasks

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
| 1 | Log onto SAP Fiori Launchpad | Open the Fiori Launch Pad with the Warehouse Clerk (EWM) role. | The Fiori Launch Pad is displayed. |  |
| 2 | Access the App | Open Fiori Manage Outbound Delivery Orders (F6498). | The Manage Outbound Delivery Orders (F6498) screen displays. |  |
| 3 | Enter Warehouse Number | Warehouse No: Enter your Warehouse Number, for example 3350. |  |  |
| 4 | Set Departure Date / Time for Route value | Departure Date for Route: Select the date/time range that your Outbound Delivery Order falls inChoose Go. | Your outbound delivery orders is visible now. |  |
| 5 | Select your Outbound Delivery | Select your outbound delivery order. |  |  |
| 6 | Create Pick Warehouse Tasks | Choose Create Pick Warehouse Tasks.Caution In case of not enough stock, you can reduce the quantity of delivery item. | The WH Task is created. The picking list is automatically printed in the background. |  |
| 7 | Choose your Outbound Delivery Order to Display the ODO details | Choose your outbound delivery order by clicking the Outbound Delivery Order number. | The Outbound Delivery Order details is displayed on the right side of the screen. |  |
| 8 | Display Warehouse Tasks | In the Items section, choose Yes in the Open Warehouse Tasks field of any item to display the open warehouse tasks for that item.Note Due to display resolution or page size settings, the Yes is likely not displayed for the item in the Open Warehouse Tasks field. In this case, choose Show More per Row to make it visible.You can also choose Yes in the Process Relevant WTs field in the General Information section to display all warehouse task for the outbound delivery order. | The Process Warehouse Tasks screen is visible now. |  |
| 9 | Note the Warehouse Task number | Note down the appearing number. | Note down the task number. |  |

### Confirm Pick Warehouse Tasks

#### Variant 1: With Fiori App

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Pick List is printed in the step before and handed over now to the Warehouse Operative (EWM). He or she performs the warehouse tasks and confirms them in the system.

If the Warehouse Tasks involve products with C-Serial Number Profile (Serialization in Stock), please enter Serial Numbers in this step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Operative (EWM). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Fiori Process Warehouse Tasks (F4595). |  |  |
| 3 | Enter your Warehouse Task Number | On the Process Warehouse Tasks screen, make the following entries:Warehouse Task: <WT number noted down in the previous step>.Choose Go. |  |  |
| 4 | Check Warehouse Task Details | If the product is Serial Number managed on stock level (Seriliaziation in Stock), you have to enter Serial Number during picking WT confirmation. In this case, follow step 4-6. Otherwise go directly to step 7.Choose the Warehouse Task to go into the Warehouse Task details. |  |  |
| 5 | Choose Serial Number link | On the Warehouse Task screen in the Movement Data section, choose No. of Serial Numbers Entered: 0 / X. |  |  |
| 6 | Enter Serial Number and Confirm Warehouse Task | On the Serial Number Assignment screen, enter the serial numbers in the Enter Serial Number field one by one.The Serial Numbers entered here have to be the actual numbers assigned to the product / stock.Choose Okay when finished.Choose Confirm. | Serial numbers are entered.The No. of Serial Numbers Entered: 0 / X has become No. of Serial Numbers Entered: X / X.The following system message appears after confirming Warehouse Task: Warehouse task <Warehouse Task Number> confirmed. |  |
| 7 | Confirm Warehouse Task | Mark the checkbox for the selected warehouse task and choose Confirm. | The following system message appears: Warehouse task <Warehouse Task Number> confirmed. |  |

#### Variant 2: With Radio Frequency Devices

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Operative (EWM) performs the warehouse tasks and confirms them in the system with mobile radio frequency device.

|  |
| --- |
| Note For working with mobile RF devices, make sure all the steps as described in the Set-up instruction guide for scope item 63V - Mobile RF Devices in Warehousing have been performed. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Fiori Launchpad | Log on to the SAP Fiori launchpad as a Warehouse Operative (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open the SAP Fiori app Test RF Environment (/SCWM/RFUI)Note Here the app allows you to test working in an RF environment. For working with mobile RF devices, see also SAP Note [3048632](https://me.sap.com/notes/3048632). |  |  |
| 3 | Enter Data for RFUI | Whse No: 3350Resource: SHA1-1 or SHR1-1DefPresDvc: SE01Choose Enter.Note Use resource SHA1-1 for picking from S001, for example queue SO-001Use SHR1-1 for picking from storage types other than S001, for example queue SO-F01, SO-B01 and so on. |  |  |
| 4 | Choose Menu | Choose 01 System-Guided > 02 SystemGuided Queue. |  |  |
| 5 | Enter Queue Name | In the Queue field, enter SO-001, SO-F01, SO-B01 or SO-G01Choose Enter |  |  |
| 6 | Create Picking HU | Make the following entries:Pack.Mat: PMPALLETChoose Handling.The picking HU is created. |  |  |
| 7 | Choose Next | Scroll the screen to right with > and choose Next. |  |  |
| 8 | Enter or Verify the Source Information fields | Enter or verify the following fields if they are required:Src.Bin (Source Bin)SrceHU (Source HU)Prod. (Product)ActQty (Quantity)Choose Enter. |  |  |
| 9 | Verify the Destination Information Fields | Verify the following fields:DstBin (Destination Bin)Choose Enter. |  |  |
| 10 | Repeat Steps | Repeat step 6 - 9 until no suitable warehouse orders are found. |  |  |
| 11 | Logoff RFUI | You can choose Back to the previous screens.Choose Logoff.Choose Save. |  |  |

### Pack Goods into Shipping Handling Units (Optional)

#### Variant 1: With Fiori App - Pack Outbound Deliveries

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is to pack the confirmed warehouse tasks as preparation step for the final physical delivery outgoing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Open the SAP Fiori launchpad with the Warehouse Operative (EWM) role. | The SAP Fiori Launch Pad is displayed. |  |
| 2. | Access the App | Open Fiori Pack Outbound Deliveries (F3193). | The Pack Outbound Deliveries (F3193) screen displays. |  |
| 3. | Enter your Required Values | Work Center: PACKStorage Bin: For example GI-AREA-01Note The storage bin to be used is determined by the setting 'Staging Area and Door Determination' as described in the preliminary steps.Choose Start Packing. | The Pack Outbound Deliveries (F3193) screen displays with a new view. |  |
| 4. | Create Handling Unit | Fill in your Reference Number:Outbound Delivery Order. | A dialog box Create Shipping Handling Unit is displayed now. |  |
| 5. | Create Shipping Handling Unit | Select your favorite packaging material. Afterwards choose Create. | Your shipping unit is automatically created now. You can verify the shipping handling unit number on the upper right corner. |  |
| 6 | Select Stock to be Packed | Select the material to be packed and choose Pack. Repeat this step as long as your destination handling unit has the right value of materials and quantity according to your needs.Note You are asked to enter serial numbers if the product concerned is serial number-managed on documentation level (documentation serialization). | According to your pack steps, you see on the right side (Destination HU) your packed materials. |  |
| 7. | Printing Shipping HU Label | To print the manual shipping handling unit label, choose Print. | Your shipping HU label is printed now. |  |
| 8. | Close the Shipping Handling Unit | Choose Close for finalizing the pack process step.Then choose Leave for proceeding with the next step. | Consider that your destination handling unit is automatically created. The HU label is automatically printed. On the left corner below, you can verify the created status. |  |

#### Variant 2: With Fiori APP - Pack Handling Units – Advanced (/SCWM/PACK)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is to pack the confirmed warehouse tasks as preparation step for the final physical delivery outgoing.

|  |
| --- |
| Note You can automatically pack the items using Pack Automatically option. For more details, refer to [Warehouse Management](https://help.sap.com/docs/SAP_S4HANA_CLOUD/87f9b54f9c4f4e75aff0061860a6589a/4ecb88b8b2422afee10000000a42189e.html?locale=en-US). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log onto SAP Fiori Launchpad | Open the Fiori Launch Pad with the Warehouse Operative (EWM) role. | The Fiori Launch Pad is displayed. |  |
| 2. | Access the App | Open Fiori Pack Handling Units - Advanced (/SCWM/PACK). | The Work Center: Packing - General screen displays. |  |
| 3. | Enter your required values | Warehouse Number: 3350Work Center: PACKStorage Bin: For example, GI-AREA-01Note The Storage Bin to be used is determined by the setting ‘Staging Area and Door Determination’ as described in the Preliminary Steps.Warehouse Request: <your ODO number>Choose Execute. | The Work Center Packing Work Center (Time Zone CET) screen displays. |  |
| 4. | Prepare to Repack Product | Navigate to Repack Product tab.Enter the value Src HU/Bin: For example, GI-AREA-01Choose Stock.In the Stock dialog box, select the stock item and choose Choose Row. | Stock is selected. A packaging material and a quantity will be proposed if any packing instructions have been defined. |  |
| 5. | Determine Packing Material (Optional) | Note If you have defined multiple packing instructions, you can select the desired Packaging Material from a list.Select Alt. PM.In the Alternative Packing Proposals dialog box, select the Packaging Material of your choice and choose Choose Row. | The quantity proposal is taken over as quantity to be packed if it is defined in the work center (Take over Quantity). |  |
| 6 | Create Shipping Handling Unit | Enter the value Storage Bin: For example, GI-AREA-01Choose Execute. | Your shipping unit is automatically created now. |  |
| 7. | Repeat Packing Steps | Repeat step 4-6 until all the products are packed into HUs. |  |  |
| 8. | Save Packing Results | Choose Save. | According to your pack steps, you see your packed materials on the right side (Destination HU). |  |
| 9. | Printing Shipping HU Label | To print the manual shipping handling unit label, choose Print. | Your Shipping HU Label is printed now. |  |

#### Variant 3: With Radio Frequency Devices

Purpose

In this process step, the Warehouse Operative (EWM) repacks the outbound delivery order items into shipping handling units using a mobile RF device.

For Working with Mobile RF Devices, make sure all the steps as described in the Setup Instruction guide for scope item 63V - Mobile RF Devices in Warehousing have been performed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Fiori launchpad | Log on to the SAP Fiori launchpad as a Warehouse Operative (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open the SAP Fiori app Test RF Environment (/SCWM/RFUI)The app allows you to test working in an RF environment. For working with mobile RF devices, see also SAP Note [3048632](https://me.sap.com/notes/3048632). |  |  |
| 3 | Enter Data for RFUI | Whse No: 3350Resource: SHA1-1 or SHR1-1Dflt Dvc.: SE01Choose Enter. |  |  |
| 4 | Choose Menu | Choose 04 Outbound Process > 02 Packing > 03 Manually Repack HU Item. |  |  |
| 5 | Enter Source HU | In the Srce HU field, enter the picking HU of your outbound delivery order.Choose Enter. |  |  |
| 6 | Enter Product | In the Pr/SI/HU field, enter the product number.Choose Enter. |  |  |
| 7 | Enter Quantity | In the ActQty field, enter the quantity.Choose Enter. |  |  |
| 8 | Repack into Shipping HU | On the same screen, if you have a shipping HU available, enter the Shipping HU number in the DestHU field. Then choose Enter.Otherwise, choose > and then choose HUcrt.On the next screen, leave the Dest. HU field empty and choose Enter.On the next screen, make the following entries.Pack. Mat.: <Packing Material Number>Note The packaging material is proposed, if any packing instructions are defined for the product.Dest.Bin: <Destination Bin>Choose Next twice. |  |  |
| 9 | Repeat Steps | Repeat step 5 - 8 until all the products in the pick HUs are repacked into shipping HUs. |  |  |
| 10 | Logoff RFUI | You can choose Back to go to the previous screens.Note If you would like to post a goods receipt using the mobile RF devices, stay logged on in the App.Choose Logoff.Choose Save. |  |  |

### Enter Serial Number for Outbound Delivery Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You don’t need to perform this step if your product is NOT serial number-managed.

If the products have an A-Serial Number profile (documentation serialization) assigned and you haven’t entered any serial number in the previous Pack Goods into Ship-ping Handling Units (Optional) step because packing is irrelevant to your business, you need to do it in this step.

If the products have a C-Serial Number profile (serialization in stock) assigned, the serial numbers are already entered in the previous step Confirm Pick Warehouse Tasks.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Open the SAP Fiori Launch Pad with the Warehouse Clerk (EWM) role. | The SAP Fiori Launch Pad is displayed. |  |
| 2. | Access the App | Open Fiori Manage Outbound Delivery Orders (F6498). | The Manage Outbound Delivery Orders (F6498) screen displays. |  |
| 3. | Enter Warehouse Number | Warehouse No: Enter your Warehouse Number, for example 3350. |  |  |
| 4. | Set Departure Date / Time for Route Value | Departure Date for Route: <Select the date/time range that your Outbound Delivery Order falls in>Choose Go. | Your outbound delivery orders is visible now. |  |
| 5. | Choose your Outbound Delivery Order | Choose your outbound delivery order by choosing your outbound delivery order number | Your outbound delivery order details is displayed on the right side of the screen. |  |
| 6. | Choose Edit | Choose Edit in the outbound delivery order screen. |  |  |
| 7. | Select Item | Select one of the items of the outbound delivery order | The item details in displayed on the right side of the screen. |  |
| 8. | Enter Serial Number | In the Serial Numbers section, enter the serial numbers one by one.Choose Apply when finished. | Serial numbers are entered. |  |
| 9. | Save Document | Choose Save. |  |  |

### Set Deliveries to Ready for Shipping (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This functionality is only available for outbound processes to external recipients.

The Warehouse Clerk (EWM) sets outbound delivery orders to ‘Ready for Shipping’. This will automatically update the LE outbound delivery and (if transportation planning is used) the freight order.

|  |
| --- |
| Note This step is optional and shall be executed only under the following circumstances.6W2 - Manual Transportation Planning is the preceding process. See chapter Appendix > Process Integration > Preceding Processes for more process step details.6W3 - Transportation Execution is the preceding process. See chapter Appendix > Process Integration > Preceding Processes for more process step details.A delivery note is to be printed before the goods issue of the outbound delivery. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Log on to the SAP Fiori launchpad as a Warehouse Clerk (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2. | Access the SAP Fiori App | Open the SAP Fiori app Manage Outbound Delivery Orders (F6498). | The Manage Outbound Delivery Orders (F6498) dialog box appears. |  |
| 3. | Enter Warehouse Number | Warehouse No: Enter your Warehouse Number, for example 3350. |  |  |
| 4. | Set Departure Date / Time for Route Value | Departure Date for Route: <Select the date/time range that your Outbound Delivery Order falls in>Choose Go. | Your outbound delivery orders is visible now. |  |
| 5. | Select your Outbound Delivery | Select your outbound delivery order. |  |  |
| 6. | Set Ready for Shipping | Choose Set to Ready for Shipping. | The outbound delivery order has been set as ready for shipping. |  |

### Check Printed Delivery Note before Goods Issue (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A Delivery Note can be printed at a certain point in time after picking and before Goods Issue, for example when packing is completely finished for an ODO. Then the delivery note document can be attached to the carton/parcel that is ready to be shipped to the customer. In this step, you can check the Delivery Note that has been printed out.

|  |
| --- |
| Note An early printing of the Delivery Note before Goods Issue is only possible when the ‘Ready for Shipping’ status is set in the previous step Set Deliveries as ‘Ready for Shipping’ (Optional). After the status is set, the Outbound Delivery Order cannot be changed anymore. In exceptional situations, for example if a new item needs to be picked and packed after the printing of the delivery note, the Ready for Shipping status can be reverted and the ODO can be changed and then updated to Logistics Execution again. This shall result in the printing of a new delivery note that contains the latest changes.The printing of the Delivery Note can be triggered immediately when the Ready for Shipping status is set in the Outbound Dlievery Order. To achieve this, please see the step Set up Output Parameter Determination for Printing Delivery Note in the Preliminary Steps. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log onto SAP Fiori Launchpad | Open the Fiori Launch Pad with the Shipping Specialist role. | The Fiori Launch Pad is displayed. |  |
| 2. | Access the App | Open Fiori Change Outbound Delivery (VL02N). | The Change Outbound Delivery (VL02N) screen displays. |  |
| 3. | Enter Outbound Delivery Number | Enter your Outbound Delivery Order number.Choose Enter. | You have new options to choose. |  |
| 4. | Go to Delivery Output Control | On the Outbound Delivery XXXXXXXX Change: Overview screen, choose Menu > Extra > Delivery Output > Output Control . | Loading list is automatically printed. |  |
| 5. | Display / Print Delivery Note | Select the entry with Output Type DELIVERY_NOTE and then choose Display Document. | The printing of the Delivery Note has been triggered automatically when setting the Ready for Shipping status. You can print the document again in the document display page. |  |

### Print Loading Instruction (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create a list of loading instructions as an information for the carrier.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log onto SAP Fiori Launchpad | Open the SAP Fiori Launch Pad with the Warehouse Clerk (EWM) role. | The SAP Fiori Launch Pad is displayed. |  |
| 2. | Access the App | Open Fiori Manage Outbound Delivery Orders (F6498). | The Manage Outbound Delivery Orders (F6498) screen displays. |  |
| 3. | Enter Warehouse Number | Warehouse No: Enter your Warehouse Number, for example 3350. |  |  |
| 4. | Set Departure Date / Time for Route value | Departure Date for Route: Select the date/time range that your Outbound Delivery Order falls inChoose Go. |  |  |
| 5. | Select your Outbound Delivery Order | Select your Outbound Delivery Order which should be printed. |  |  |
| 6. | Print the Loading List | Choose Print loading Instruction. | Loading list is printed. |  |

### Loading (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you process loading with Advanced Shipping and Receiving in the warehouse with both Fiori App or Radio Frequency Device.

The Advanced Shipping and Receiving process is based on the TM freight order (FO). In EWM, an outbound delivery order with the Transportation Planning Type ‘F’ and status ‘Ready for Shipping’ is the basis for loading with Advanced Shipping and Receiving. Once a transportation vehicle is checked in the source location (warehouse), the loading activity can begin.

You can skip this step if the TM freight order is irrelevant to your process.

Prerequisites

Prerequisites for loading (see scope item 6W3 – Transportation Execution in Appendix > Process Integration > Preceding Processes).

For Freight Order or Freight Booking:

- Execution Status: Set to Ready for Transportation Execution
- Execution Status (Source): Set to Arrived
- Execution Status (Source): Set to Checked In

#### Variant 1: With Fiori App

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
| 1 | Log onto SAP Fiori Launchpad | Open the Fiori Launch Pad with the Warehouse Clerk (EWM) role. | The Fiori Launch Pad is displayed. |  |
| 2 | Access the App | Open Fiori app Load or Unload Freight Orders (/SCMTMS/ASR). | The Load or Unload Freight Orders (/SCMTMS/ASR) screen displays. |  |
| 3 | Find Freight Order | On the Load or Unload Freight Orders screen, make the following entries:Freight Order: <your freight order number>.Warehouse No: <your warehouse number, for example3350>.Choose Go. |  |  |
| 4 | Assign Door (Optional) | Note you can skip this step if you have done the following steps described in the Preliminary Steps chapter, as a door would have been assigned to the Freight Order automatically based on those settings:Create loading pointAssign door to loading pointDetermine Staging Area – OutboundOn the Edit Freight Orders screen, select the level of loading stop and then choose Door Assignment > Assign DoorIn the Assign Door dialog box, make the following entries:Loading/Unloading Point: <your loading point>.Warehouse Door: <your warehouse door>.Choose OK. | The following system message appears:Loading or unloading point XXXX and door XXXX of whse XXXX assigned to itemsWith the door assignment, a new loading stop is created for the combination of warehouse, door and loading point. |  |
| 5 | Arrive at Door | Select the level of the stop and then choose Warehouse Door Status > Set to Arrive at Door.Choose Save | The following messages appear:Status is set to “Arrived at Door”.Warehouse door status successfully updated for WH Loading Stop <Loading Stop> / <Whse No.> / <Door>. |  |
| 6 | Perform Loading | Select the Loading Stop and then choose Execution Status > Set Items to Loaded .Choose Save. | The following system message appears:Event Loading End for Item successfully reported.The loading status for the items under the stop is set to green. |  |
| 7 | Set stop to loading finished (Optional) | Select the Loading Stop and then choose Execution Status > Set Stop to Loading Finished.Choose Save. |  |  |
| 8 | Departure from Door | Select the Loading Stop and then choose Warehouse Door Status > Set to Departure from Door.Choose Save. | The following system message appears:Warehouse door status successfully updated for WH Loading Stop <Loading Stop> / <Whse No.> / <Door>.Status is set to "Departed from Door" |  |
| 9 | Post goods issue (Optional) | Select the Loading Stop and then choose Goods Movement > Post.Choose Save.The Goods issue has been posted for the Outbound Delivery Order.Note You can also post goods issue for the outbound delivery order in the next chapter Post Goods Issue. If you triggered the goods movement posting in this step, you can skip the step Post Goods Issue . | The following system message appears:Goods movement posting triggered for delivery <your delivery number>.The Goods issue has been posted for the Outbound Delivery Order. |  |

#### Variant 2: With Radio Frequency Devices

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Operative (EWM) performs the loading activity in the system with mobile Radio Frequency device.

|  |
| --- |
| Note Note For working with Mobile RF Devices, make sure all the steps as described in the Set-up Instruction guide for scope item 63V - Mobile RF Devices in Warehousing have been performed. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Fiori launchpad | Log on to the SAP Fiori launchpad as a Warehouse Operative (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open the SAP Fiori app Test RF Environment (/SCWM/RFUI)Note Here the App allows you to test working in an RF environment. For working with Mobile RF Devices, see also SAP Note [3048632](https://me.sap.com/notes/3048632). |  |  |
| 3 | Enter Data for RFUI | Whse No: 3350Resource: SHA1-1 or SHR1-1Dflt Dvc.: SE01Choose Enter. |  |  |
| 4 | Choose Menu | Choose 04 O utbound Process > 03 Loading > 01 Loading by Delivery. |  |  |
| 5 | Enter Outbound Delivery Order Number | In the Del. No. field, enter <Outbound Delivery Order number>Choose Enter |  |  |
| 6 | Check HU List | Press F1 to view the HU List |  |  |
| 7 | Load HU | Make the following entries:HU: <one of the HUs from the list>Choose Enter.The HU has been loaded. |  |  |
| 8 | Load Remaining HUs | Repeat step 7 until all the HUs are loaded. |  |  |
| 9 | Confirm Loading Completion | When seeing the 'Complete Loading?’ message, choose Yes. |  |  |
| 11 | Logoff RFUI | You can choose Back to the previous screens.Choose Logoff.Choose Save. |  |  |

### Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is for finalizing the outbound process via posting the done status.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto | Open the SAP Fiori Launchpad with the Warehouse Clerk (EWM) role. | The SAP Fiori Launch Pad is displayed. |  |
| 2 | Access the App | Open Fiori Manage Outbound Delivery Orders (F6498). | The Manage Outbound Delivery Orders (F6498) screen displays. |  |
| 3 | Enter Warehouse Number | Warehouse No: Enter your Warehouse Number, for example 3350. |  |  |
| 4 | Set Departure Date / Time for Route Value | Departure Date for Route: <Select the date/time range that your Outbound Delivery Order falls in>.Choose Go. | Your outbound delivery orders is visible now. |  |
| 5 | Select your Outbound Delivery | Select your outbound delivery order. |  |  |
| 6 | EWM: Post Goods Issue | Choose Post Goods Issue. | The goods issue is posted and has generated a warehouse material document. |  |

### Reverse Post Goods Issue (Optional)

Purpose

The goods issue has been posted and the outbound delivery is completed in the warehouse. Afterwards, if the user would like to edit – for example. the quantity – in the relevant sales order, the outbound delivery has to be reversed on the warehouse side.

|  |
| --- |
| Note If a billing document already exists, please make sure it is reversed before below steps. |

#### Reverse Goods Issue

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
| 1 | Log onto | Open the SAP Fiori Launch Pad with the Warehouse Clerk (EWM) role. | The SAP Fiori Launch Pad is displayed. |  |
| 2 | Access the App | Open Fiori Manage Outbound Delivery Orders (F6498). | The Manage Outbound Delivery Orders (F6498) screen displays. |  |
| 3 | Enter Warehouse Number | Warehouse No: Enter your Warehouse Number, for example 3350. |  |  |
| 4. | Set Departure Date / Time for Route Value | Departure Date for Route: <Select the date/time range that your Outbound Delivery Order falls in> |  |  |
| 5 | Include Completed Deliveries | Goods Issue : CompletedChoose Go. | Your outbound delivery orders are visible now. |  |
| 6 | Select your Outbound Delivery | Select your outbound delivery order. |  |  |
| 7 | Goods Issue Reversal | From the dropdown list next to the Goods Issue, choose Reverse Goods Issue. | The following system message appears: Goods issue was successfully reversed. |  |

#### Release Stock

Purpose

This step is to release the assignment of picked or reserved stock from the WR items, Handling Units or WTs. This makes the stock freely available again.

Once this step is completed, the stock is in the staging area without a reference to the outbound delivery and can be moved back to the warehouse afterwards.

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
| 1 | Log onto | Open the SAP Fiori Launch Pad with the Warehouse Clerk (EWM) role. | The SAP Fiori Launch Pad is displayed. |  |
| 2 | Access the App | Open Fiori Manage Outbound Delivery Orders (F6498). | The Manage Outbound Delivery Orders (F6498) screen displays. |  |
| 3 | Enter Warehouse Number | Warehouse No: Enter your Warehouse Number, for example 3350. |  |  |
| 4 | Set Departure Date / Time for Route Value | Departure Date for Route: <Select the date/time range that your Outbound Delivery Order falls in> | Your Outbound Delivery Orders is visible now. |  |
| 5 | Choose your Outbound Delivery Order | Choose your Outbound Delivery Order by clicking your outbound delivery order number. | Your outbound delivery order details is displayed on the right side of the screen. |  |
| 6 | Access Work Center Packing for Outbound Delivery App | In the Outbound Delivery Order screen, on the top right corner,select … Additional Options > Related Apps > Work Center Packing for Outbound Delivery .the delivery item line and choose Release Unpacked Stock. | The Work Center Packing for Outbound Delivery screen is open. |  |
| 7 | Release Stock | In the Work Center Packing for Outbound Delivery screen, select the unpacked stock (product) or packed stock (Handling Unit) and choose Release Stock. |  |  |
| 8 | Confirm System Message | Choose Yes in the confirmation dialog box (Stock will be released for selected objects. Do you want to continue?). |  |  |

#### Adjust Delivery Quantity

Purpose

This step is to set the delivery quantities to "0" so that the sales order can reopen.

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
| 1 | Log onto | Open the SAP Fiori Launch Pad with the Warehouse Clerk (EWM) role. | The SAP Fiori Launch Pad is displayed. |  |
| 2 | Access the App | Open Fiori Manage Outbound Delivery Orders (F6498). | The Manage Outbound Delivery Orders (F6498) screen displays. |  |
| 3 | Enter Warehouse Number | Warehouse No: Enter your Warehouse Number, for example 3350. |  |  |
| 4 | Set Departure Date / Time for Route Value | Departure Date for Route: <Select the date/time range that your Outbound Delivery Order falls in>Choose Go. | Your outbound delivery orders is visible now. |  |
| 5 | Choose your Outbound Delivery Order | Choose your Outbound Delivery Order by cliking your outbound delivery order number. | Your outbound delivery order details is displayed on the right side of the screen. |  |
| 6 | Adjust Delivery Quantity | In the Items section, select the delivery item and then choose Adjust Delivery Quantity. |  |  |
| 7 | Confirm System Message | Choose OK in the confirmation dialog box (do you really want to adjust the delivery quantity to the warehouse task quantity?) | The delivery quantity has been set to the quantity of your choice to reopen the sales order. |  |

#### Trigger Delivery Update

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is to synchronize the changes back to the outbound delivery in logistics.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log onto | Open the SAP Fiori Launch Pad with the Warehouse Clerk (EWM) role. | The SAP Fiori Launch Pad is displayed. |  |
| 2. | Access the App | Open Fiori Manage Outbound Delivery Orders (F6498). | The Manage Outbound Delivery Orders (F6498) screen displays. |  |
| 3. | Enter Warehouse Number | Warehouse No: Enter your Warehouse Number, for example3350. |  |  |
| 4. | Set Departure Date / Time for Route Value | Departure Date / Time for Route: <Select the date/time range that your Outbound Delivery Order falls in>.Choose Go. | Your outbound delivery orders is visible now. |  |
| 5. | Select your Outbound Delivery | Select your outbound delivery order. |  |  |
| 6. | EWM: Post Goods Issue | Choose Goods Issue. | The goods issue is posted and the quantity adjustment has been synchronized back to the outbound delivery in the logistics. You can use the app Display Outbound Delivery (VL03N) to check the delivery quantity and status. |  |

## Appendix

### Access Code Handling

You can enter or scan external access codes in the Product/Access code field during the packing process via the Pack Outbound Deliveries (F3193) app. The system triggers the mapped internal access codes in the backend to perform actions.

The following external access codes are currently supported:

| External Access Code | Function |
| --- | --- |
| S_CLOSE_HU | Close HU |
| S_CREATE_HU | Create HU |
| S_PACK_ALL | Pack all product items |
| S_PACK_ITEM | Pack one product item |

### Attachment Handling

In the SAP S/4HANA Cloud Public Edition, Attachment Service is a reusable user interface component which can be consumed by any FIORI application to attach documents. File attachments enable all kinds of media files being connected to business documents as additional information, such as photos, videos, or documentation in form of plain text documents.

Examples for use cases of the Attachment Service in the Warehouse Management Cloud:

- Inbound Process - Non-Acceptance of Delivery and Proof of SLA Violation
- Outbound Process - Visual Documentation of Complete and Error-free Packaging
- Outbound Process - Visual Documentation of Loading Security, Compliance to Regulations, SLAs

Attachment Service is an optional support feature for the WM Cloud business objects. Attachments can be handled any time after the creation of an Cloud WM business object and any time before the end of the document’s lifecycle.

In this process you can use the following Fiori Apps to create, read, update, or delete attachments:

- Warehouse Monitor for Outbound Delivery Orders or Handling Units respectively under nodes:
    - Outbound > Documents > Outbound Delivery Orders

### Create Warehouse Task with Job Scheduling

As of SAP S/4HANA CE 2002, the Fiori App Schedule Warehouse Task Creation - Picking is available for creating picking warehouse tasks for multiple outbound delivery orders.

You can still create warehouse tasks for each individual outbound delivery order with the Fiori App Run Outbound Process (F1704) – Deliveries. If you want to create warehouse tasks for multiple outbound delivery orders at the same time, you can use the Fiori app Schedule Warehouse Task Creation - Picking (F4505) as an alternative.

This app has the following features​:

- Creation of single run or recurring background WT creation jobs
- Definition of a recurrence pattern
- Filter criterial on: Warehouse Number, Document No/Type, Armin Data, Shipment Data, Product Data, etc.​
- List of all WT creation jobs with fields: Status, Log, Results, Steps, Description, Planned Start time, and Created By​
- Cancellation of unexecuted jobs
- Application job log​

To use the Fiori App, you have to log on as the Warehouse Clerk (EWM) - SAP_BR_WAREHOUSE_CLERK_EWM.

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

You may first have completed the following processes and conditions before you start with the test steps:

|  |
| --- |
| Note When running the following preceding processes along with the warehouse processes, make sure the material master data has been extended to your warehouse storage locations and the corresponding warehouse products have been created.Please refer to the Master Data Script BNF to create the storage location data for your material master data.Please refer to the Master Data Script 3KQ to create the corresponding warehouse products. |

|  |  |  |
| --- | --- | --- |
| Process |  | Business Condition |
| Outbound to External Customer |  |  |
| BD9 - Sell from Stock |  | See [Business Conditions](#unique_7) [page ] 8 |
| Return to Supplier |  |  |
| 3BU - Warehouse Posting Changes |  | Execute 3BU - Warehouse Posting Changes to block the stock to be returned to the supplier. |
| BMK - Return to Supplier |  | Complete the activity (Create Return Purchase Order, Create Return Delivery ) described in the test script.Make sure that you use the warehouse-managed Storage Location 335W in the Create Return Purchase Order step. |
| Outbound triggered by Goods Movement Posting |  |  |
| BMC - Core Inventory Management |  | Complete the activity (General Stock Scrapping: Goods Issue to Cost Center) using a warehouse-managed Storage Location (for example Storage Location 335W) and the materials in the chapter Master Data, Organizational Data, and Other Data. |
| BMC - Core Inventory Management |  | Complete the activity (one-step stock transfer).Make sure that you transfer from the Storage Location 335W. |
| Outbound from other Plant (Intracompany and Intercompany) |  |  |
| BME - Stock Transfer with Delivery |  | Complete the activity (Optional: Stock Transport Order (without MRP), Optional: Change Confirmation Control for Inbound Delivery, Create Replenishment Delivery for Stock Transport Order).Make sure that you use the warehouse-managed Storage Location 335W in the Stock Transport Order without MRP step.Note The BME scope item can be processed in combination with the following Warehouse Management and Transportantion Management scope items as of SAP S/4HANA Cloud Public Edition 2602:3BS - Warehouse Outbound Processing6W2 - Manual Transportation Planning6W3 - Transportation Execution |
| 2TS - Intercompany Stock Transfer Returns |  | Complete the activity (Create Returns Stock Transport Order, Create Outbound Delivery for Return Stock Transport Order).Make sure that you use the warehouse-managed Storage Location 335W in the Returns Stock Transport Order. |
| 5WI - Intra-Company Returns Stock Transfers |  | Complete the activity (Create Returns Stock Transport Order, Create Outbound Delivery for Return Stock Transport Order).Make sure that you use the warehouse-managed Storage Location 335W in the Returns Stock Transport Order. |
| Free of Charge Delivery |  |  |
| BDA – Free of Charge Delivery |  | Complete the activity (Create Sales Order, Create Delivery) described in the test script.At the Create Sales Order step, before saving the delivery, select the order item and then choose More > Goto > Item > Shipping . In the Shipping section, enter the Stor.Loc. value of the warehouse-managed Storage Location (for example Storage Location 335W).Use the master data from this document. |
| Free Goods Processing |  |  |
| BKA –Free Goods Processing |  | Complete the activities (Create Sales Order, and Create Delivery) described in the test script.At the Create Sales Order step, before saving the delivery, select the order item and then choose More > Goto > Item > Shipping . In the Shipping section, enter the Stor.Loc. value of the warehouse-managed Storage Location (for example Storage Location 335W).Use the master data TG11. |
| Sales Scheduling Agreements |  |  |
| 3NR – Sales Scheduling Agreements |  | Complete the activities (from Create Sales Scheduling Agreement step to Create Delivery step) described in the test script.At the Create Sales Scheduling Agreement step, before saving the Sales Scheduling Agreement, select the item and then choose More > Goto > Item > Shipping . In the Shipping section, enter the Stor.Loc. value of the warehouse-managed Storage Location (for example Storage Location 335W).Use the master data from this document.Note The 3NR scope item can be processed in combination with the following Warehouse Management and Transportation Management scope items as of SAP S/4HANA Cloud Public Edition 2608:3BS - Warehouse Outbound Processing6W2 - Manual Transportation Planning6W3 - Transportation Execution |
| Sales Scheduling Agreement with Consignment |  |  |
| 4LZ – Sales Scheduling Agreement with Consignment |  | Complete the activities (Create Sales Scheduling Agreements for Consignment step to Create Outbound Delivery step) described in the test script.At the Create Sales Scheduling Agreements for Consignment step, before saving the Sales Scheduling Agreement, select the item and then choose More > Goto > Item > Shipping . In the Shipping section, enter the Stor.Loc. value of the warehouse-managed Storage Location (for example Storage Location 335W).Use the master data TG14. |
| Customer Down Payment |  |  |
| BKJ – Sales Order Processing with Customer Down Payment |  | Complete the activities (from Create Sales Orders with Billing Plan step to Create Delivery step) described in the test script.At the Create Sales Orders with Billing Plan step, before saving the sales order, select the item and then choose More > Goto > Item > Shipping . In the Shipping section, enter the Stor.Loc. value of the warehouse-managed Storage Location (for example Storage Location 335W).Use the master data from this document. |
| Customer Consignment |  |  |
| 1IU – Customer Consignment |  | For Consignment Fill-UP, complete the activities (from Create Consignment Fill-Up Order step to Create Outbound Delivery step) described in the test script.At the Create Consignment Fill-Up Orders step, before saving the Sales Order, select the item and then choose More > Goto > Item > Shipping . In the Shipping section, enter the Stor.Loc. value of the warehouse-managed Storage Location (for example Storage Location 335W).Use the master data from this document.Note The 1IU scope item can be processed in combination with the following Warehouse Management and Transportantion Management scope items as of SAP S/4HANA Cloud Public Edition 2602:3BS - Warehouse Outbound Processing6W2 - Manual Transportation Planning6W3 - Transportation Execution |
| Sales of Non-Stock Item with Order-Specific Procurement |  |  |
| BDN – Sales of Non-Stock Item with Order-Specific Procurement |  | Complete the activities (Create Sales Orders step to Create Delivery step) described in the test script.At the Create Sales Orders step, before saving the Sales Order, select the item and then choose More > Goto > Item > Shipping . In the Shipping section, enter the Stor.Loc. value of the warehouse-managed Storage Location (e.g. Storage Location 335W).At the Post Goods Receipt step, when entering the Goods Recipient, enter the Stor.Loc. value of the warehouse-managed Storage Location (for example Storage Location 335W.Use the master data TG14. |
| Sales Order Processing for Sales Kits |  |  |
| 31Q – Sales Order Processing for Sales Kits |  | Complete the activities (Create Sales Orders step to Create Delivery step) described in the test script.At the Create Sales Orders step, before saving the Sales Order, select the item and then choose More > Goto > Item > Shipping . In the Shipping section, enter the Stor.Loc. value of the warehouse-managed Storage Location (for example Storage Location 335W). |
| Returnables Processing |  |  |
| BDW – Returnables Processing |  | Complete the activities described in either one of the following options of the test script.The Create Sales Orders step to Create Delivery step in chapter Sales Process Including Returnable Materials. At the Create Sales Orders step, before saving the Sales Order, select the item and then choose More > Goto > Item > Shipping . In the Shipping section, enter the Stor.Loc. value of the warehouse-managed Storage Location (e.g. Storage Location 335W)Create Outbound Delivery without Order Reference step in chapter Delivery Process for Returnable Materials. Before saving the Outbound Delivery, in the Picking tab, enter the the warehouse-managed Storage Location (for example 335W) in the SLoc field for the delivery items.Use the master data for trading goods and RP001. |
| Customer Returns |  |  |
| BKP - Customer Returns |  | Complete the activities described in either one of the following options of the test script.In Scenario 1: Goods are Returned to Seller• In the subchapter Create Free-of-Charge Delivery of chapter Refund Customer with Replacement Product (Option B), you create the outbound delivery for replacement product. You then execute picking and post goods issue with reference to the steps as described in this test script.In Scenario 2: Goods are Inspected at Customer Site• In the subchapter Create Free-of-Charge Delivery of chapter Refund Customer with Replacement Product, you create the outbound delivery for replacement product. You then execute picking and post goods issue with reference to the steps as described in this test script.In Scenario 3: Goods are Returned to Supplier via Seller• In the subchapter Create Free-of-Charge Delivery of chapter Refund Customer with Replacement Product (Option B), you create the outbound delivery for replacement product. You then execute picking and post goods issue with reference to the steps as described in this test script.In Scenario 1: Goods are Returned to Seller• You already chose the Follow-Up Activity: 0021 Send Back to Customer in step Perform Material Inspection. An outbound delivery for returning products to customer was created. In chapter Send Back to Customer (Option C) , you then execute picking and post goods issue with reference to the steps as described in this test script.In Scenario 3: Goods are Returned to Supplier via Seller• In the sub chapter Create Outbound Delivery of chapter Return Goods to Supplier via Seller, you create the outbound delivery for return purchase order. You then execute picking and post goods issue for return purchase order with reference to the steps as described in this test script.Note Make sure you use warehouse-managed storage location (e.g. Storage Location 175W) in the outbound delivery. If not, you use the app Change Outbound Delivery with role SAP_BR_SHIPPING_SPECIALIST to change the storage location. On the Picking tab, select the delivery item and enter the Stor.Loc. value of the warehouse-managed Storage Location (e.g. Storage Location335W). |
| 3XK – In-House Repair |  | In the 3XK – In-House Repair process, complete the activity Prepare and Release for Billing as described in the test script.Afterwards, execute the picking and post goods issue steps as descrbied in this test sript. |
| 5CX – Customer Returns for Sales Kits |  | In the 5CX – Customer Returns for Sales Kits process, complete the activity Create Free-of-Charge Delivery as described in the test script.At the Create Free-of-Charge Delivery step, after the delivery is created, on the Analyze Delivery Log screen, select the delivery number and then choose Change Outbound Delivery.On the Outbound Delivery XXXX change: Overview screen, before saving the Outbound Delivery, in the Picking tab, enter the the warehouse-managed Storage Location (for example 335W) in the SLoc field for the delivery items.Afterwards, execute the picking and post goods issue steps as described in this test script. |
| Just-In-Time Supply to Customer from Stock |  |  |
| 2EM - Just-In-Time Supply to Customer |  | For warehouse integration with Summarized JIT Call (Supply from Stock), make sure you fulfill the following steps under chapter Summarized JIT Calls (Supply from Stock) in scope item 2EM - Just-In-Time Supply to Customer:Create Just-In-Time Customer Master DataCreate Customer Supply Control RecordsCreate the Customer Supply Control with following data:Component Group Material FGJIT03Repetitive Manufacturing is Allowed: NoProduction Version: <Empty>Create Sales Scheduling AgreementYou create the sales scheduling agreement with material FGJIT03 and customer material number RP001JIT04. Before saving the sales scheduling agreement, select the item and then choose More > Goto > Item > Shipping. In the Shipping section, enter the Stor.Loc. value of the warehouse-managed Storage Location (for example Storage Location 335W).Create Customer Summarized Just-In-Time Call Manually (Optional)You create customer summarized JIT call with customer material number RP001JIT04.Create Outbound Delivery from Summarized JIT CallsYou create outbound delivery with component group FGJIT03.Ensure that you have stock for FGJIT03 in the warehouse managed storage location 335W. Get the stock via processing the scope item Warehouse Inbound Processing from the file. |
| Plant Maintenance |  |  |
| 4HH - Reactive Maintenance |  | Ensure the staging area determination has been maintained with Firori APP Staging Area Determination with Recipient Location.Complete activities (Create Maintenance Request step to Post Goods Issue step) described in the test script.At the Create and Plan Maintenance Order step, when adding stock material in the Material Overview tab, enter the Stor.Loc. value of the warehouse-managed Storage Location (for example Storage Location 335W) . |
| 4HI - Proactive Maintenance |  | Ensure the staging area determination has been maintained with Firori APP Staging Area Determination with Recipient Location.Complete activities (Time-Based Single Cycle Plan step to Post Goods Issue step) described in the test script.At the Create and Plan Maintenance Order step, when adding stock material in the Material Overview tab, enter the Stor.Loc. value of the warehouse-managed Storage Location (for example Storage Location 335W) . |
| Subcontracting |  |  |
| BMY - Subcontracting |  | Complete the activity (Create Purchase Order & Create Outbound Delivery) described in the test script.Make sure that you use the warehouse-managed Storage Location 335W in the Create Outbound Delivery step.Note The BMY scope item can be processed in combination with the following Warehouse Management and Transportantion Management scope items as of SAP S/4HANA Cloud Public Edition 2602:3BS - Warehouse Outbound Processing6W2 - Manual Transportation Planning6W3 - Transportation Execution |
| Transportation Management |  |  |
| 6W2 - Manual Transportation Planning |  | Scope item 6W2 - Manual Transportation Planning can be used in combination with the scope item 3BS, but it must be preceded by item BD9 - Sell from Stock.Complete the activity (Create Sales Order, Create Delivery) described in the test script BD9 - Sell from Stock.At the Create Sales Order step, before saving the delivery, enter the warehouse-managed Storage Location (for example Storage Location 335W).﻿﻿﻿In addition to the data described in scope item BD9 - Sell from Stock, enter the TM-specific data outlined in the Business Conditions for scope item 6W2 - Manual Transportation Planning, for example Shipping Condition: 06 - TM - Int. Planning.Complete all the tasks outlined in the scope item 6W2 test script.The process step "Trigger Delivery Creation" generates the delivery, which will be handled in the warehouse. |
| 6W3 - Transportation Execution |  | Scope item 6W3 - Transportation Execution can be used in combination with the scope item 3BS. The process step Post Goods Issue step must be performed as described in scope item 3BS.Prior to performing loading procedures in the warehouse, the freight order status must be updated to 'Ready for Transportation Execution.'To change the status of freight orders to 'Ready for Transportation Execution,' follow these steps:Execute the 'Outbound - Set Truck/Railcar Arrived and Checked-In' process step at the Shipping Point Location.Update the Execution Status to 'Ready for Transportation Execution.' |
| Advanced Intercompany Processes |  |  |
| 5D2 - Advanced Intercompany Sales |  | Complete the activities (from Create Sales Order step to Create Delivery step) described in the test script.At the Create Sales Order step, before saving the order, select the order item and then choose More > Goto > Item > Shipping . In the Shipping section, enter the Stor.Loc. value of the warehouse-managed storage location (for example, storage location 335W).Note The 5D2 scope item can be processed in combination with the following Warehouse Management and Transportantion Management scope items as of SAP S/4HANA Cloud Public Edition 2608:3BS - Warehouse Outbound Processing6W2 - Manual Transportation Planning6W3 - Transportation Execution |
| 5HP - Advanced Intercompany Stock Transfer |  | Complete the activities (from Create Intercompany Stock Transfer Order step to Create Outbound Delivery for Stock Transfer Order) described in the test script.Make sure that you use the warehouse-managed storage location 335W when creating outbound deliveries.Note The 5D2 scope item can be processed in combination with the following Warehouse Management and Transportantion Management scope items as of SAP S/4HANA Cloud Public Edition 2608:3BS - Warehouse Outbound Processing6W2 - Manual Transportation Planning6W3 - Transportation Execution |

#### Succeeding Processes

The process to be tested in this test script is part of a chain of integrated processes. After completing the activities in this test script, you can continue testing the following business process to complete the end-to-end processes.

| Process | Business Condition |
| --- | --- |
| BD9 - Sell from Stock | Complete activities starting from chapter described in the test script using the master data from this document. |
| BMK - Return to Supplier | Complete activities starting from chapter Create Credit Memo described in the test script of the scope item using the master data from this document. |
| BMC - Core Inventory Management | Complete activities starting from chapter Stock Overview - Single Material described in the test script of the scope item using the mas-ter data from this document. |
| BME - Stock Transfer with Delivery | Complete activities starting from chapter described in the test script of the scope item using the master data from this document. |
| BDA - Free of Charge Delivery | Complete activities starting from chapter Create Pro Forma Invoice described in the test script of the scope item using the master data from this document. |
| BKA - Free Goods Processing | Complete activities starting from chapter Create Billing Document described in the test script of the scope item using the master data from this document. |
| 3NR - Sales Scheduling Agreements | Complete activities starting from chapter Send Advance Shipping Notice- EDI Relevant described in the test script of the scope item using the master data from this document. |
| 4LZ - Sales Scheduling Agreement with Consignment | Complete activities starting from Check Stock Overview step in chapter Scheduling Agreement Consignment Fill-up as described in the test script of the scope item using the master data from this document. |
| BKJ - Sales Order Processing with Customer Down Payment | Complete activities starting from chapter Change Sales Orders (Remove Billing Block) described in the test script of the scope item using the master data from this document. |
| 1IU - Customer Consignment | Complete activities starting from Check Stock Overview step in chapter Consignment Fill-up as described in the test script of the scope item using the master data from this document. |
| 3XK – In-House Repair | Complete activities starting from chapter Complete Repair Object and Finalize In-House Repair (Optional) as described in the test script of the scope item. |
| 5CX – Customer Returns for Sales Kits | Complete activities starting from chapter Create Pro-forma Invoice as described in the test script of the scope item. |
| BDN - Sales of Non-Stock Item with Order-Specific Procurement | Complete activities starting from chapter Create Billing Document described in the test script of the scope item using the master data from this document. |
| 31Q - Sales Order Processing for Sales Kits | Complete activities starting from chapter Create Billing Document described in the test script of the scope item using the master data from this document. |
| BDW - Returnables Processing | Complete activities Starting from Display Pallet Stock step in chapter Sales Process Including Returnable Materials described in the test script. |
| 2EM - Just-In-Time Supply to Customer | Complete activities starting from chapter Create Billing Document described in the test script of the scope item using the master data from this document. |
| 4HH - Reactive Maintenance | Complete activities starting from chapter Submit Order for Scheduling described in the test script of the scope item using the master data from this document. |
| 4HI - Proactive Maintenance | Complete activities starting from chapter Submit Order for Scheduling described in the test script of the scope item using the master data from this document. |
| 6W3 - Transportation Execution | After completing chapter , continue with 6W3 step |

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
- related-to :: [[11-inventory-warehouse-and-transportation/sap-ewm-integration-outbound-processing-to-customer-2vk-ae-test-script]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3BS_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 101,486 chars in the whole document
