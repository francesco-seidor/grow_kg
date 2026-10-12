---
id: 15-retail-operations/test-script-retail-logistics-with-embedded-warehouse-management-69l-ae
title: Test Script - Retail Logistics with Embedded Warehouse Management (69L_AE) (69L_S4CLD2608_BPD_EN_AE)
description: "S/4HANA Cloud test script for scope item 69L_AE: embedded EWM inbound, outbound, physical inventory, posting changes, replenishment, prerequisites."
cluster: 15-retail-operations
tags: [kb/retail-operations, topic/retail-dc-warehouse-execution]
aliases: [69L_S4CLD2608_BPD_EN_AE]
keywords: [Retail DC Warehouse Execution (Embedded EWM or Third-Party…, embedded warehouse management, warehouse inbound processing, warehouse outbound processing, physical inventory, posting changes, stock replenishment, warehouse configuration, cycle counting, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/69L_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1152
topic: 15-retail-operations/retail-dc-warehouse-execution
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script - Retail Logistics with Embedded Warehouse Management (69L_AE) (69L_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/69L_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Retail DC Warehouse Execution (Embedded EWM or Third-Party WMS)** in Retail Operations. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Retail Logistics with Embedded Warehouse Management (69L_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232857512)

[2 Prerequisites 4](#_Toc232857513)

[2.1 System Access 4](#_Toc232857514)

[2.2 Roles 4](#_Toc232857515)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232857516)

[2.4 Additional Manual Configuration 7](#_Toc232857517)

[2.5 Business Conditions 7](#_Toc232857518)

[2.6 Preliminary Steps 9](#_Toc232857519)

[2.6.1 Configuration Automatic creation of Storage location 9](#_Toc232857520)

[2.6.2 Configuration for Define Default values for deliveries 9](#_Toc232857521)

[2.6.3 Configuration for Setting Warehouse Address 10](#_Toc232857522)

[2.6.4 Configuration for Define Warehouse Attributes 11](#_Toc232857523)

[2.6.5 Maintain Warehouse Product Attributes 12](#_Toc232857524)

[2.6.6 Create Storage Bin in Good Issue Area 13](#_Toc232857525)

[2.6.7 Define Default Values for Warehouse Clerk (EWM) 14](#_Toc232857526)

[2.6.8 Define Default Values for Warehouse Operative (EWM) 15](#_Toc232857527)

[2.6.9 Assign Fixed Storage Bins to Products 15](#_Toc232857528)

[2.6.10 Staging Area and Door Determination (Outbound) 16](#_Toc232857529)

[2.6.11 Access Sequence to Staging Areas and Door Determination 17](#_Toc232857530)

[2.6.12 Define Favorite Packaging Materials 18](#_Toc232857531)

[2.6.13 Define Deliveries View 18](#_Toc232857532)

[2.6.14 Assign User to Tolerance Group for Clearing 19](#_Toc232857533)

[2.6.15 Assign User to Tolerance Group for Difference Analyzer 20](#_Toc232857534)

[2.6.16 Define Cycle Counting Indicator 21](#_Toc232857535)

[2.6.17 Assign Cycle Counting Indicator 22](#_Toc232857536)

[2.6.18 Assign Fixed Bin 23](#_Toc232857537)

[3 Overview Table 25](#_Toc232857538)

[4 Test Procedures 28](#_Toc232857539)

[4.1 Warehouse Inbound Processing 28](#_Toc232857540)

[4.1.1 Change Stock Type (Optional) 28](#_Toc232857541)

[4.1.2 Create Handling Unit (Optional) 29](#_Toc232857542)

[4.1.3 Post Goods Receipt 30](#_Toc232857543)

[4.1.4 Create Putaway Warehouse Tasks 32](#_Toc232857544)

[4.1.5 Confirm Warehouse Tasks 33](#_Toc232857545)

[4.1.6 Clarification Zone (Optional) 34](#_Toc232857546)

[4.1.6.1 Check Material in Clarification Zone 34](#_Toc232857547)

[4.1.6.2 Create Warehouse Tasks from Clarification Zone to Final Bin 35](#_Toc232857548)

[4.1.6.3 Confirm Warehouse Tasks 37](#_Toc232857549)

[4.2 Warehouse Outbound Processing 38](#_Toc232857550)

[4.2.1 Assign Carrier (Optional) 38](#_Toc232857551)

[4.2.2 Create Pick Warehouse Tasks 39](#_Toc232857552)

[4.2.3 Confirm Warehouse Tasks 40](#_Toc232857553)

[4.2.4 Pack Goods into Shipping Handling Units (Optional) 41](#_Toc232857554)

[4.2.5 Print Loading Instruction (Optional) 42](#_Toc232857555)

[4.2.6 Post Goods Issue 43](#_Toc232857556)

[4.3 Warehouse Physical Inventory 44](#_Toc232857557)

[4.3.1 Variant 1: Create and Print Cycle Counting Document 44](#_Toc232857558)

[4.3.2 Variant 2: Create and Print Counting Document 45](#_Toc232857559)

[4.3.3 Enter Count Result 46](#_Toc232857560)

[4.3.4 Confirm Inventory Count Results 47](#_Toc232857561)

[4.3.5 Analyze Differences 49](#_Toc232857562)

[4.4 Warehouse Posting Changes 50](#_Toc232857563)

[4.4.1 Option 1: Posting Changes Triggered in Warehouse 50](#_Toc232857564)

[4.4.1.1 Posting Change 50](#_Toc232857565)

[4.4.2 Option 2: Posting Changes Triggered in Inventory Management 52](#_Toc232857566)

[4.4.2.1 Trigger Transfer Posting 52](#_Toc232857567)

[4.4.2.2 Create Warehouse Tasks for Posting Changes 53](#_Toc232857568)

[4.4.3 Confirm Warehouse Task for Posting Changes 55](#_Toc232857569)

[4.5 Replenishment in Warehousing 56](#_Toc232857570)

[4.5.1 Replenish Stock 56](#_Toc232857571)

[4.5.2 Schedule Job for Replenishment 57](#_Toc232857572)

[4.5.3 Check Replenishment Warehouse Tasks (Optional) 58](#_Toc232857573)

[4.5.4 Confirm Replenishment Warehouse Tasks 59](#_Toc232857574)

## Purpose

Overview

A distribution center is typically the logistical entry point of a retailer to the supply chain. It connects the procurement process from external suppliers with the distribution process to the stores. The goal of the distribution process is to shorten delivery cycles to the stores, ensuring that there are no out-of-stock situations.

To achieve this, a sophisticated warehouse management is key. The following activities are supported by the embedded warehouse management:

- Receive articles and put-away in the warehouse
- Use different variants of inbound processing
- Pick and pack products, and send them from your warehouse
- Plan and conduct regular physical inventory counts of actual quantities in the warehouse, comparing them with book inventory, and posting differences
- Transfer postings, such as changing the stock type from unrestricted to blocked stock
- Perform planned or automatic replenishment of fixed bins

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

|  |
| --- |
| Note In the retail industry, specific terms differ from the standard terms used in other lines of business. Therefore, SAP solutions which provide business processes across multiple lines of businesses may use terms for the corresponding business objects, transactions, and user interfaces that deviate from the retail terminology. For integration and reuse reasons, the SAP S/4HANA Cloud Public Edition, retail, fashion, and vertical business business may thus include different terms that refer to the same concept. SAP intends to harmonize the terminology in the future.The following terms are used synonymously in this document:Table 1:Standard Terms in Lines of BusinessSAP S/4HANA Cloud Public Edition, retail, fashion, and vertical business businessMaterial, productArticleMaterial group, product groupMerchandise categoryPlant, locationSite (as superordinate term) - store and distribution center (DC) |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

|  |  |
| --- | --- |
|  | Details |
| System | Accessible through SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Warehouse Clerk (EWM) | SAP_BR_WAREHOUSE_CLERK_EWM | Warehouse Office | SAP_BR_WAREHOUSE_CLERK_EWM |  |
| Warehouse Operative (EWM) | SAP_BR_WAREHOUSE_OPERATIVE_EWM | Warehouse Floor | SAP_BR_WAREHOUSE_OPERATIVE_EWM |  |
| Warehouse Clerk (Retail) | SAP_BR_WAREHOUSE_CLERK_RFM | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Article | R_7000 | Camera | Single article |
| Article | R_7003 | Camera bag | Generic articles are not supported for the EWM process. Use below generic article variants. |
| Article | R_7003001 | Camera bag, WHITE | Generic article Variant |
| Article | R_7003002 | Camera bag, BLACK | Generic article Variant |
| Article | R_7003003 | Camera bag, RED | Generic article Variant |
| Article | R_7003004 | Camera bag, BLUE | Generic article Variant |
| Packaging Material | R_CARTON | Carton |  |
| Packaging Material | R_PALLET | Pallet |  |
| Supplier | 33213001 | Retail Non-Food Supplier AE |  |
| Company Code | 3310 | Company Code 3310 |  |
| Purchasing Organization | 3310 | Purch. Org. 3310 |  |
| Plant | 3350 | DC 3350 AE |  |
| Storage Location | 995W | St.Loc. EWM DC |  |
| EWM Warehouse | 3350 | Warehouse |  |
| Division | 00 | Product Division 00 |  |
| Distribution Channel | 10 | Direct Sales |  |
| Shipping Point | 3350 | SP DC 3350 |  |
| Ship to party | 33113007 | Wholesale non-Food AE |  |
| Sold to party | 33113007 | Wholesale non-Food AE |  |
| Default Party Entitled | 3350 | DC 3350 AE |  |
| Sales Organization | 3310 | Dom. Sales Org |  |
| Warehouse Number | 335 | Warehouse |  |
| Carrier | 33300001 | Domestic AE Supplier 1 |  |

Warehouse-Specific Master Data

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Storage Type | S001 | Storage |  |
| Storage Type | SF01 | Fixed Bin Storage |  |
| Storage Type | SB01 | Bulk Storage |  |
| Storage Type | SG01 | General Storage |  |
| Storage Type | S970 | Clarification Zone |  |
| Storage Type | S820 | Quality Area |  |
| Storage Type | S840 | Scrapping Zone |  |
| Storage Type | S910 | Goods Receipt |  |
| Storage Type | S915 | Goods Receipt from Production |  |
| Storage Type | S920 | Goods Issue |  |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

- [Warehouse Management](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fsupport.sap.com%2Fcontent%2Fdam%2FSAAP%2FSAP_Activate%2FS4H_588%2520Warehouse%2520Management%2520Setup.docx) (published on SAP Activate Roadmap Viewer)
- Warehouse Inbound Processing:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/feddbd6f25c875b6623f5db0cf698660)

- Warehouse Outbound Processing:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/e61afa140c8f77e384eeb729750780bc)

- Warehouse Physical Inventory:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/94d961d12c4f0bc013f495cec9d52ac0)

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| Inbound from Supplier |  |
| 5FU - Inbound Logistics for Distribution Centers | A purchase order is created as a part of the preliminary process of 5FU - Inbound Logistics for Distribution Centers with Inbound delivery. Use a warehouse-managed storage location (for example, Storage location 995W) Supplier and the materials in the chapter master data, organizational data, and other data of this document (69L).Then, proceed with the inbound delivery creation as described in the scope item. |
| Outbound Processing |  |
| 5FV - Outbound Logistics for Distribution Centers | This scope item describes the outbound processing of merchandise from the distribution centre (DC) to stores.A stock transfer order needs to be created with the corresponding delivery.Use the master data from this document (69L). |
| Outbound to External Customer |  |
| 3HS - Sales from Distribution Center | Complete activity (Create Sales Order, Create Delivery) described in the test scriptAt the create sales order step, before saving the delivery, select the order item and then select More > Go to > Item > Shipping . In the Shipping section, enter the Stor. Loc. value of the warehouse-managed Storage Location (for example, Storage Location 995W).Use the master data from this document (69L). |
| Return to Supplier |  |
| 5FO - Returns to Supplier for Retail | Complete activity (Create Return Purchase Order, create outbound Delivery) described in the test script.Make sure that you use the warehouse-managed Storage Location 995W in the Create Return Purchase Order step.Use the master data from this document (69L). |
| Outbound Triggered by Goods Movement Posting |  |
| 5FQ - Inventory Management for Distribution Centers | Complete activity (General Stock Scrapping: Goods Issue to Cost Centre) using a warehouse-managed Storage Location (for example, Storage Location 995W)Use the materials in the chapter master data, organizational data, and other data. |
| Customer Consignment |  |
| 3HS - Sales from Distribution Center | For Consignment Fill-Up, complete the activities (from Create Consignment Fill-Up Order step to Create Outbound Delivery step) described in the Create Outbound Deliveryscope item Sales from Distribution Center (3HS).At the Create Consignment Fill-Up Orders step, before saving the Sales Order, select the item and then select More > Go to > Item > Shipping In the Shipping section, enter the Stor. Loc. value of the warehouse-managed Storage Location (for example, Storage Location 995W).Use the master data from this document (69L). |

### Preliminary Steps

#### Configuration Automatic creation of Storage location

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration as Configuration Expert - Business Process Configuration |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Create Storage Location Automatically.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Create Storage Location Automatically Change screen is displayed. |  |
| 3 | Configuration Create Storage Location Automatically | Create the following settings:For Movement type 657 - GD returns blocked, check ON Create SLoc. Automat. | The configuration is saved successfully |  |

#### Configuration for Define Default values for deliveries

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration as Configuration Expert - Business Process Configuration |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Default Values for Deliveries.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Default Values for Deliveries screen is displayed. |  |
| 3 | Configuration Define Default Values for Deliveries | Create the following settings:Select the warehouse and select DetailsMaintain the below entries and SaveShip-To-Party: <Ship-To-Party>Supplier: <Supplier>Shipping Point: 3310Sales Organization: 3310Distribution Channel: 10Division: 00 | The configuration is saved successfully |  |

#### Configuration for Setting Warehouse Address

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration as Configuration Expert - Business Process Configuration |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Set Warehouse Address.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Set Warehouse Address screen is displayed. |  |
| 3 | Configuration Set Warehouse Address | Create the following settings:Select New EntriesWarehouse Number: 3350Default Pty Entitld: |  |  |
| 4 | Save the configuration | Maintain the below address data entries and Save:Name:Street/House number:Postal Code/City:Country/Region:Time zone:Choose Enter. | The configuration is saved successfully |  |

#### Configuration for Define Warehouse Attributes

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration as Configuration Expert - Business Process Configuration |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Warehouse Attributes.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Warehouse Attributes: Change: Details screen is displayed. |  |
| 3 | Configuration Define Warehouse Attributes | Create the following settings:Select the warehouse and select DetailsMaintain the below entries and Save• Weight Unit: <Weight Unit>• Volume Unit: <Volume Unit>• Currency: <Currency>• Time Unit: <Time Unit>• Unit of Length: <Unit of Length>• Factory Calend.: <Factory Calendar>Note The SSCUI “Define Warehouse Attributes” allows the input of the units for weight, volume, length and time only if no values have been provided yet. As soon as the units are filled (and saved), the fields are closed for input. This ensures that the units are transported to the productive system only once. The currency and factory calendar can be changed anytime. | The configuration is saved successfully |  |

#### Maintain Warehouse Product Attributes

Use

In this chapter, you find a description of how to maintain warehouse product attributes with the Manage Product Master Data (F1602) application. This application can be used for single changes.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as the Master Data Specialist - Product Data.Note Master Data Specialist - Product Data – role: SAP_BR_MD_SPCLST_ITEM_RFM |  |  |
| 2 | Access App | Open Manage Product Master Data (F1602) app. |  |  |
| 3 | Enter Material Number | On the Manage Product Master Data (F1602) screen, enter the following data:Product: R_7000 or R_7003Select Go. | The material master data is displayed in the Product section. |  |
| 4 | Select Material | Select the row of the material master data. |  |  |
| 5 | Choose Warehouse Management | On the Product screen, select the Warehouse Management tab and go to Warehouse Management > Warehouse. |  |  |
| 6 | Edit Material Master Data | On the Product screen, select Edit. |  |  |
| 7 | Add Warehouse Data | In the Warehouse section, select the warehouse number for your warehouse.If your warehouse number does not exist, select Create. |  |  |
| 8 | Enter Values | On the Warehouse screen, enter the following data:In the General Information section:Warehouse: 3350Party Entitled to Dispose: <Business Partner ID for the Party Entitled to Dispose>Process Type Determination IndicatorCycle Counting IndicatorNote Only Warehouse and Party Entitled to Dispose are mandatory for input.In the Putaway section:Putaway Control Indicator: SG01In the Stock Removal section:Stock Removal Control Indicator: SG01In the Cloud Warehouse Management, the Putaway Control Indicator and the Stock Removal Control Indicator are maintained with the same value. However, in the replenishment process used in the warehouse, these two fields must be maintained differently to enable the process. |  |  |
|  | Create Storage Type Data for Replenishment | In the Storage Types section, select Create.On the New Record – Storage Type screen, enter the following data:In the General Information section:Storage Type: for example: SF01Maximum Number of Bins: <Number of Bins>In the Replenishment section:Minimum Replenishment Quantity / Display UoM: <Quantity> / <UoM>Minimum Quantity / Display UoM: <Quantity> / <UoM>Maximum Quantity / Display UoM: <Quantity> / <UoM> |  |  |
| 9 | Save Your Data | Select Apply and Save. | The warehouse data is saved. |  |

#### Create Storage Bin in Good Issue Area

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as the Warehouse Clerk (EWM). |  |  |
| 2 | Access App | Open Create Storage Bins(/SCWM/LS01). |  |  |
| 3 | Enter Storage Bin ID | On the Create Storage Bins(/SCWM/LS01) screen, enter the following data:Storage Bin: for example:-<Storage Bin ID>Choose Enter. |  |  |
| 4 | Enter Storage Bin Attributes | On the Storage Bin tab, enter the following data:Storage Type: S920Only the Storage Type field is mandatory. All of the other fields below are optional:Maximum WeightMax. VolumeAisleX CoordinateStackY CoordinateBin LevelZ CoordinateBin Angle |  |  |
| 5 | Save Your Data | Choose Save. | A system message tells you that the storage bin has been saved. |  |

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
| 3. | Enter Default Value | Choose Default Values.And make the following entry in the section Materials Management:Warehouse No.: 3350Choose Save. |  |  |

#### Assign Fixed Storage Bins to Products

Use

In this step, you assign fixed storage bins to products.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk (EWM) |  |  |
| 2 | Access the App | Open Assign Fixed Bins (/SCWM/BINMAT). |  |  |
| 3 | Enter the data | On the Assign Fixed Storage Bins screen, make the following entries:Warehouse Number: 3350.Product: R_7000 or R_7003 .Choose Run. |  |  |
| 4 | Maintain Fixed Bin | Choose Edit to switch to change mode.Choose Create.Make the following entry:WhN: 3350 .Disposal: 3350 .Storage Bin: for example:-SF01-03-04Product: R_7000 or R_7003.ChooseSave. |  |  |

#### Staging Area and Door Determination (Outbound)

Use

In this step, you define define the logic in the outbound process to determine which outbound delivery order with respective materials should go to which Storage Bin in the Outbound Staging Area. This can help you distribute your materials by, for example carriers, for a better separation and planning.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Open the SAP Fiori launchpad with the Warehouse Clerk (EWM) role. | The SAP Fiori launchpad is displayed. |  |
| 2. | Access the App | Open Determine Staging Area - Outbound (/SCWM/STADET_OUT) | The Determine Staging Area - Outbound (/SCWM/STADET_OUT) screen displays. |  |
| 3. | Create new entries | Create first entry by selecting Create New Entries with the following values:Warehouse Number:3350.Sequence Number: 1Carrier: 33300001Staging Bay: GI-AREA-02Stg. Area Group: S920Choose Save. |  |  |
| 4. | Create new entries | Create the second entry by selecting Next Entry with the following values:Warehouse Number: 3350Sequence Number: 1Staging Bay: GI-AREA-01Stg. Area Group: S920Whse Proc. Type: S210Choose Save. |  |  |

#### Access Sequence to Staging Areas and Door Determination

Use

In this step, you create the access sequence that defines which combination of fields the system should use while searching for a match between the attributes of an out-bound document and a set of determination rules. The matching determination rule that the system finds is used to determine to which staging area a delivery item should be sent.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log onto SAP Fiori Launchpad | Open the SAP Fiori launchpad with the Warehouse Clerk (EWM) role. | The SAP Fiori launchpad is displayed. |  |
| 2. | Access the App | Open Define Access Sequence - Staging Areas - Outbound (/SCWM/STADET_ASS_OUT) | The Define Access Sequence - Staging Areas - Outbound (/SCWM/STADET_ASS_OUT) screen displays. |  |
| 3. | Create new entries | First Door DeterminationWarehouse Number: 3350Use Carrier: XAccess Sequence Number: 1Choose Save. | Should be created. |  |
| 4. | Create new entries | Second Door DeterminationWarehouse Number: 3350Use Whse Proc. Type: XAccess Sequence Number: 2Choose Save. | Should be created. |  |

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
| 6. | Fill in Required Entries | Work Center: PackProduct: for example R_CARTONChoose Save. | A dialog box with the message Data was saved appears in the right corner. |  |

#### Define Deliveries View

Procedure

This step is optional for processes-related shipping of materials into the outside.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log onto SAP Fiori Launchpad | Open the SAP Fiori launchpad with the Warehouse Clerk (EWM) role. | The SAP Fiori launchpad is displayed. |  |
| 2. | Access the App | Open Run Outbound Process (F1704). | The Run Outbound Process (F1704) screen displays. |  |
| 3. | Change the view | Choose Standard and select the SAP-Delivery to Sales screen. | The view has changed. |  |
| 4. | Change the view | Choose Standard again and use then choose Manage.Switch the default from Standard to SAP -Delivery to Sales. Afterwards choose Save. | The Default Deliveries view is changed and saved now. |  |

#### Assign User to Tolerance Group for Clearing

Purpose

Here, you assign individual logon users to tolerance groups which have previously been defined in the system.

Generally, the assignment of users to tolerance groups determines whether a logon user can post differences or enter values within the tolerance boundaries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk (EWM). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Assign Tolerance Group - Count Confirmation (/SCWM/PI_USER). |  |  |
| 3 | Close Warning Message | If there’s a warning message for the initial value, choose Continue to confirm it. |  |  |
| 4 | Switch to Edit Mode | Choose Edit. |  |  |
| 5 | Assign to Tolerance Group | Choose New Entries and make the following entries:User: <User>.AA:<Activity Area>Tolerance Group: STOLCHECK.Note Choose STOLCHECK if you want to have the tolerance check, otherwise choose SNOTOLCHECK.Choose Save. |  |  |

#### Assign User to Tolerance Group for Difference Analyzer

Purpose

In this transaction, you assign individual logon users to tolerance groups which have previously been defined in the system configuration.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk (EWM). | The SAP Fiori launchpad is displayed |  |
| 2 | Access App | Open Assign Tolerance Group - Differences (/SCWM/PI_USER_DIFF). |  |  |
| 3 | Close Warning Message | If there is a warning message for the initial value, choose Continue to confirm it. |  |  |
| 4 | Switch to Edit Mode | Choose Edit. |  |  |
| 5 | Assign Tolerance Group (Original) | Choose New Entries to create entries as needed. Here, you need to make assignments to real users that you use in your system. Therefore, the following users given in angle brackets (<>) are only examples.If you log on as a background job user, enter the following data:User: <User>Tolerance Group: SNOTOLCHECKNote Choose STOLCHECK if you want to have the tolerance check. Otherwise, choose SNOTOLCHECK.Choose Save.Note If you choose SNOTOLCHECKs on company code level, there's still a maximum value limitation by default. If a physical inventory document exceeds value 100,000 on header level or 10,000 on item level, the user is not allowed to post any inventory differences for this document. However, the maximum value can be adjusted via the Maintain Physical Inventory Tolerance configuration step. |  |  |

#### Define Cycle Counting Indicator

Purpose

In this step, you define the sample counting indicator. For each indicator, you define

- the interval in work days after which a new physical inventory should be performed.
- the buffer time in work days.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration as Configuration Expert - Business Process Configuration. |  |  |
| 2 | Open Active Flexible Workflow | In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Configure Cycle Counting.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Cycle Counting screen is displayed. |  |
| 3 | Configure Cycle Counting | Create the following settings:Choose New Entries and enter the following data:1st Entry:Warehouse Number: 3350.CC Indicator: A .Interval: 60.Buffer: 5.2nd Entry:Warehouse Number: 3350.CC Indicator: B .Interval: 120.Buffer: 5.3rd Entry:Warehouse Number: 3350.CC Indicator: C .Interval: 240.Buffer: 5.Choose Save. |  |  |

#### Assign Cycle Counting Indicator

Purpose

In this step, you assign the cycle counting indicator to the product master. The maintenance of the cycle counting indicator is also supported in data migration of warehouse products (see the Data Migration to SAP S/4HANA from Staging (2Q2) scope item).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Master Data Specialist - Product Data.Note role Master Data Specialist - Product Data – role: SAP_BR_MD_SPCLST_ITEM_RFM |  |  |
| 2 | Choose App | Open Manage Product Master Data (F1602). |  |  |
| 3 | Enter Selection Data | Maintain the following selection value:Product: R_7000 or R_7003.Choose Go. |  |  |
| 4 | Select Product | Choose the entry of the product. |  |  |
| 5 | Choose Tab | Choose the Warehouse Management tab and then the Warehouse subtab. |  |  |
| 6 | Choose Warehouse | Choose the row for warehouse number 3350. |  |  |
| 7 | Enter Data | Maintain the following value:Cycle Counting Indicator: A.Note Depending on the counting interval for the product, you assign different cycle counting indicators.Choose Apply. |  |  |
| 8 | Save Data | Choose Save. |  |  |

#### Assign Fixed Bin

Purpose

In this step, you assign fixed storage bins to products.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk (EWM). |  |  |
| 2 | Access App | Open Assign Fixed Bins |  |  |
| 3 | Enter Data | On the Assign Fixed Storage Bin screen, enter the following data:Warehouse Number:3350Product: R_7000 or R_7003Choose Run. |  |  |
| 4 | Maintain Fixed Bin | Choose Edit to switch to change mode.Choose Create.Make the following entries:Warehouse Number: 3350Party Entitled to Dispose: 3350Storage Bin: for example:- SF01-03-03Product: R_7000 or R_7003Max.Qty: 100DisplayUoM Max. Qty: PCMin.Qty: 4DisplayUoM Min. Qty: PCChoose Save.Note If for storage type SF01, the replenishment level is set as Storage Bin Level for Fixed Bins by default, the stock levels are read for the invidual fixed bins. The replenishment quantites are calculated based on the stocks available in the bin compared to the required quantities. |  |  |

## Overview Table

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Warehouse Inbound Processing

| ID (Role Template) | Name (Role Template) | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Change Stock Type (Optional)](#unique_27) [page ] 28 | SAP_BR_WAREHOUSE_CLERK_EWM | Change Inbound Deliveries - Deliveries (F1706) | The following system message is displayed:Data was successfully saved |
| [Create Handling Unit (Optional)](#unique_28) [page ] 29 | SAP_BR_WAREHOUSE_CLERK_EWM | Change Inbound Deliveries - Deliveries (F1706) | The Delivery Items have been removed from the Unpacked Items section. |
| [Post Goods Receipt](#unique_29) [page ] 30 | SAP_BR_WAREHOUSE_CLERK_EWM | Change Inbound Deliveries - Deliveries (F1706) | The following system message is displayed:Goods receipt posted |
| [Create Putaway Warehouse Tasks](#unique_30) [page ] 32 | SAP_BR_WAREHOUSE_CLERK_EWM | Change Inbound Deliveries - Deliveries (F1706) | The following system message is displayed:Tasks created |
| [Confirm Warehouse Tasks](#unique_31) [page ] 33 | SAP_BR_WAREHOUSE_OPERATIVE_EWM | Process Warehouse Tasks (F4595) | The following system message is displayed:Warehouse task < xxx > to be confirmed.Warehouse task < xxx > was confirmed. |
| Clarification Zone: |  |  |  |
| [Check Material in Clarification Zone](#unique_32) [page ] 34 | SAP_BR_WAREHOUSE_CLERK_EWM | Warehouse Management Monitor Node Stock and Bin > Storage Bin > Available Stock | The Available Stock is displayed. |
| [Create Warehouse Tasks from Clarification Zone to Final Bin](#unique_33) [page ] 35 | SAP_BR_WAREHOUSE_CLERK_EWM | Warehouse Management Monitor Node Stock and Bin > Storage Bin > Available Stock > Monitor Method > Create Warehouse Task | The following system message is displayed:Warehouse task < xxx > created.Warehouse order <xxx> created . |
| [Confirm Warehouse Tasks](#unique_34) [page ] 37 | SAP_BR_WAREHOUSE_OPERATIVE_EWM | Process Warehouse Tasks (F4595) | The following system message is displayed:Warehouse task <xxx> to be confirmed .Warehouse task <xxx> is confirmed . |

Warehouse Outbound Processing

| ID (Role Template) | Name (Role Template) | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Assign Carrier (Optional)](#unique_35) [page ] 38 | SAP_BR_WAREHOUSE_CLERK_EWM | Run Outbound Process (F1704) |  |
| [Create Pick Warehouse Tasks](#unique_36) [page ] 39 | SAP_BR_WAREHOUSE_CLERK_EWM | Run Outbound Process (F1704) |  |
| [Confirm Warehouse Tasks](#unique_37) [page ] 40 | SAP_BR_WAREHOUSE_OPERATIVE_EWM | Process Warehouse Tasks (F4595) |  |
| [Pack Goods into Shipping Handling Units (Optional)](#unique_38) [page ] 41 | SAP_BR_WAREHOUSE_OPERATIVE_EWM | Pack Outbound Deliveries (F3193) |  |
| [Print Loading Instruction (Optional)](#unique_39) [page ] 42 | SAP_BR_WAREHOUSE_CLERK_EWM | Run Outbound Process (F1704) |  |
| [Post Goods Issue](#unique_40) [page ] 43 | SAP_BR_WAREHOUSE_CLERK_EWM | Run Outbound Process (F1704) |  |

Warehouse Physical Inventory

| ID (Role Template) | Name (Role Template) | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Variant 1: Create and Print Cycle Counting Document](#unique_41) [page ] 44 | SAP_BR_WAREHOUSE_OPERATIVE_EWM | Create Inventory Documents - Cycle Counting (/SCWM/PI_CC_CREATE) | A physical inventory document is created. |
| [Variant 2: Create and Print Counting Document](#unique_42) [page ] 45 | SAP_BR_WAREHOUSE_OPERATIVE_EWM | Create Inventory Documents - Physical Inventory (/SCWM/PI_DOC_CREATE) | The counting documents are created and printed. |
| [Enter Count Result](#unique_43) [page ] 46 | SAP_BR_WAREHOUSE_OPERATIVE_EWM | Count Physical Inventory - Paper-Driven Counting (F3340) | The count result is entered. |
| [Confirm Inventory Count Results](#unique_44) [page ] 47 | SAP_BR_WAREHOUSE_CLERK_EWM | Confirm Inventory Count Results (/SCWM/MONNAV_PI_CONF) | The inventory count results are checked and confirmed. |
| [Analyze Differences](#unique_45) [page ] 49 | SAP_BR_WAREHOUSE_CLERK_EWM | Analyze Differences (/SCWM/DIFF_ANALYZER) | All the differences are cleared, and a material document is created. |

Warehouse Posting Changes

| ID (Role Template) | Name (Role Template) | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Option 1: Posting Changes Triggered in Warehouse[Posting Change](#unique_46) [page ] 50 | SAP_BR_WAREHOUSE_CLERK_EWM | Create Posting Changes (/SCWM/MONNAV_CR_PC) | The stock change is posted. |
| Option 2: Posting Changes Triggered in Inventory Management[Trigger Transfer Posting](#unique_47) [page ] 52 | SAP_BR_WAREHOUSE_CLERK_EWM | Transfer Stock - In-Plant (F1061) | The transfer posting is triggered. |
| [Create Warehouse Tasks for Posting Changes](#unique_48) [page ] 53 | SAP_BR_WAREHOUSE_CLERK_EWM | Process Posting Change Item (/SCWM/MONNAV_PROC_PC) | The warehouse tasks are created for posting changes. |
| [Confirm Warehouse Task for Posting Changes](#unique_49) [page ] 55 | SAP_BR_WAREHOUSE_OPERATIVE_EWM | Process Warehouse Tasks (F4595) | The warehouse task is confirmed. |

Replenishment in Warehousing

| ID (Role Template) | Name (Role Template) | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Replenish Stock](#unique_50) [page ] 56 | SAP_BR_WAREHOUSE_CLERK_EWM | Replenish Stock (/SCWM/REPL) |  |
| [Schedule Job for Replenishment](#unique_51) [page ] 57 | SAP_BR_WAREHOUSE_CLERK_EWM | Schedule Replenishment (F4319) |  |
| [Check Replenishment Warehouse Tasks (Optional)](#unique_52) [page ] 58 | SAP_BR_WAREHOUSE_CLERK_EWM | Warehouse Monitor (/SCWM/MON) |  |
| [Confirm Replenishment Warehouse Tasks](#unique_53) [page ] 59 | SAP_BR_WAREHOUSE_OPERATIVE_EWM | Process Warehouse Tasks (F4595) |  |

## Test Procedures

### Warehouse Inbound Processing

#### Change Stock Type (Optional)

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
| 1 | Log on to the SAP Fiori launchpad | Log on to the SAP Fiori launchpad as a Warehouse Clerk (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open the SAP Fiori app Change Inbound Deliveries - Deliveries (F1706). | The Change Inbound Deliveries - Deliveries (F1706) screen appears. |  |
| 3 | Choose Filters | On the Change Inbound Deliveries screen, choose Adapt Filters. | The Adapt Filters dialog box appears. |  |
| 4 | Select Fields for Filter | On the Adapt Filters dialog box, make sure the following fields are selected for the current filter:Planned Delivery Date/TimeInbound DeliveryChoose OK. |  |  |
| 5 | Search for Inbound Delivery | On the Change Inbound Deliveries screen, make the following entries:Planned Delivery Date/Time: <your planned delivery date/Time>.Purchase Order: <your purchase order number>.Choose Go. | The Change Inbound Deliveries screen appears and your inbound delivery is displayed. |  |
| 6 | Select Inbound Delivery | On the Change Inbound Deliveries screen, choose your Inbound Delivery. | Your Inbound Delivery is displayed. |  |
| 7 | Edit Inbound Delivery | On the Change Inbound Deliveries screen, select Edit. |  |  |
| 8 | Change Stock Type | In the Stock Type column, make the following entries:Stock Type: Q or B. |  |  |
| 9 | Choose Save | Choose Save. | Data was successfully saved |  |

#### Create Handling Unit (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, the Warehouse Clerk (EWM) chooses the delivery. He or she chooses the Unpacked Items tab and creates handling units.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on to the SAP Fiori launchpad | Log on to the SAP Fiori launchpad as a Warehouse Clerk (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2. | Access the SAP Fiori app | Open the SAP Fiori app Change Inbound Deliveries - Deliveries (F1706). | The Change Inbound Deliveries - Deliveries (F1706) screen appears. |  |
| 3. | Choose Filters | On the Change Inbound Deliveries screen, choose Filters. | The Filters dialog box appears. |  |
| 4. | Enter Purchase Order Number | On the Filters dialog box, make the following entries:Purchase Order: <your purchase order number>. |  |  |
| 5. | Choose Go | Choose Go. | The Change Inbound Deliveries screen appears and your Inbound Delivery is displayed. |  |
| 6. | Choose Inbound Delivery | On the Change Inbound Deliveries screen, choose your Inbound Delivery. | Your Inbound Delivery is displayed. |  |
| 7. | Select Unpacked Items | On the Change Inbound Deliveries screen in the Items section, choose the Unpacked Items tab. |  |  |
| 8. | Choose Create HU | Choose Create HU. |  |  |
| 9. | Enter Packaging Material and Number of HUs | On the Create Handling Unit dialog box, make the following entries:Pack. Material: R_CARTON.Number of HUs: <number of handling units>. |  |  |
| 10. | Choose Create | Choose Create. | The Change Inbound Deliveries screen appears.The Delivery Items have been removed from the Unpacked Items section. |  |
| 11. | Note Down your Delivery Number | Note down your delivery number for testing purposes. |  |  |

#### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The goods receipt is being posted. SAP S/4HANA Cloud Public Edition system is being updated accordingly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on to the SAP Fiori launchpad | Log on to the SAP Fiori launchpad as a Warehouse Clerk (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2. | Access the SAP Fiori app | Open the SAP Fiori app Change Inbound Deliveries - Deliveries (F1706). | The Change Inbound Deliveries - Deliveries (F1706) screen appears. |  |
| 3. | Choose Filters | On the Change Inbound Deliveries screen, choose Adapt Filters. | The Adapt Filters dialog box appears. |  |
| 4. | Enter Purchase Order Number | On the Adapt Filters dialog box, make the following entries:Planned Dlv. Date: <your planned delivery date>.Purchase Order: <your purchase order number>. |  |  |
| 5. | Choose Go | Choose Go. | The Change Inbound Deliveries screen appears and your Inbound Delivery is displayed. |  |
| 6. | Choose Inbound Delivery | On the Change Inbound Deliveries screen, choose your Inbound Delivery. | Your Inbound Delivery is displayed. |  |
| 7. | Choose Delivery Items | On the Change Inbound Deliveries screen, choose your Delivery Items. |  |  |
| 8. | Post Goods Receipt | Choose Goods Receipt. | The following system message appears:Goods receipt posted. |  |

#### Create Putaway Warehouse Tasks

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
| 2. | Access the SAP Fiori app | Open the SAP Fiori app Change Inbound Deliveries - Deliveries (F1706). | The Change Inbound Deliveries - Deliveries (F1706)screen appears. |  |
| 3. | Choose Filters | On the Change Inbound Deliveries screen, choose Adapt Filters. | The Adapt Filters dialog box appears. |  |
| 4. | Enter Purchase Order Number | On the Adapt Filters dialog box, make the following entries:Purchase Order: <your purchase order number> |  |  |
| 5. | Choose Go | Choose Go. | The Change Inbound Deliveries screen appears and your Inbound Delivery is displayed. |  |
| 6. | Choose Inbound Delivery | On the Change Inbound Deliveries screen, choose your Inbound Delivery. | Your Inbound Delivery is displayed. |  |
| 7. | Choose Delivery Items | On the Change Inbound Deliveries screen, choose your Delivery Items. |  |  |
| 8. | Choose Create Tasks | Choose Create Tasks. | The following system message appears:Tasks created. |  |
| 9. | Choose Warehouse Tasks | In the Delivery Item section, choose Warehouse Tasks. | The warehouse task(s) created is displayed. Make a note of the warehouse task number. |  |

#### Confirm Warehouse Tasks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A Putaway List is printed and handed over to the Warehouse Operative (EWM). The user performs the warehouse tasks and confirms them in the system. Note that he or she can also confirm warehouse tasks using the app Warehouse Monitor (/SCWM/MON) (Business Catalog WM – Monitoring).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Fiori launchpad | Log on to the SAP Fiori launchpad as a Warehouse Operative (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open the SAP Fiori app Process Warehouse Tasks (F4595). | The Confirm Warehouse Tasks screen appears. |  |
| 3 | Enter Warehouse Task Number | On the Process Warehouse Tasks screen, make the following entries:Warehouse Task: <Your warehouse task number>.Choose Go. |  |  |
| 4 | Confirm Warehouse Task | Mark the checkbox for the selected warehouse task and choose Confirm. | The following system message appears: Warehouse task confirmed. |  |

#### Clarification Zone (Optional)

##### Check Material in Clarification Zone

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
| Note The following reasons lead to destination bin Clarification Zone:No putaway control indicator (PACI) maintained for the productNo fix bin assignment for products with putaway control indicator to fix bin storage typeQuality- or blocked stockNo free bin in the storage type |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on to the SAP Fiori Launchpad | Log on to the SAP Fiori launchpad as a Warehouse Clerk (EWM). |  |  |
| 2. | Access the SAP Fiori App | Open the SAP Fiori app Warehouse Monitor (/SCWM/MON). | The Warehouse Monitor (/SCWM/MON) dialog box appears. |  |
| 3. | Enter Default Values | On the Warehouse Management Monitor dialog box, make the following entries:Warehouse Number: <your warehouse number>Monitor: SAP |  |  |
| 4. | Choose Execute | On the Warehouse Management Monitor dialog box, choose Execute. | The Warehouse Management Monitor SAP - Warehouse Number xxx screen appears. |  |
| 5. | Navigate to Available Stock | On the Warehouse Management Monitor SAP - Warehouse Number xxx screen, choose Stock and Bin > Storage Bin > Available Stock. |  |  |
| 6. | Display Available Stock | Choose the node Available Stock by double-clicking on it. | The /SCWM/SAPLSTOCK_OVERVIEW_MON dialog box appears. |  |
| 7. | Enter Product | On the /SCWM/SAPLSTOCK_OVERVIEW_MON dialog box, make the following entries:ExampleStorage Type: S970 - Clarification Zone |  |  |
| 8. | Choose Execute | On the /SCWM/SAPLSTOCK_OVERVIEW_MON dialog box, choose Execute. | The Available Stock is displayed. |  |

##### Create Warehouse Tasks from Clarification Zone to Final Bin

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
| 1. | Log on to the SAP Fiori launchpad | Log on to the SAP Fiori launchpad as a Warehouse Clerk (EWM). |  |  |
| 2. | Access the SAP Fiori app | Open the SAP Fiori app Warehouse Monitor (/SCWM/MON). | The Warehouse Monitor (/SCWM/MON) dialog box appears. |  |
| 3. | Enter Default Values | On the Warehouse Management Monitor dialog box, make the following entries:Warehouse Number: <your warehouse number> |  |  |
| 4. | Choose Execute | On the Warehouse Management Monitor dialog box, choose Execute. | The Warehouse Management Monitor SAP - Warehouse Number xxx screen appears. |  |
| 5. | Navigate to Available Stock | On the Warehouse Management Monitor SAP - Warehouse Number xxx screen, choose Stock and Bin > Storage Bin > Available Stock. |  |  |
| 6. | Display Available Stock | Choose the node Available Stock by double-clicking on it. | The /SCWM/SAPLSTOCK_OVERVIEW_MON dialog box appears. |  |
| 7. | Enter Product | On the /SCWM/SAPLSTOCK_OVERVIEW_MON dialog box, make the following entries:Storage Type: S970 - Clarification Zone |  |  |
| 8. | Choose Execute | On the /SCWM/SAPLSTOCK_OVERVIEW_MON dialog box, choose Execute. | The Available Stock is displayed. |  |
| 9. | Choose Stock | Choose the stock for which you want to create a warehouse task. |  |  |
| 10. | Choose More Methods | On the Warehouse Management Monitor SAP - Warehouse Number xxx screen, choose More Methods > Create Warehouse Task. | The Create Warehouse Task dialog box is displayed. |  |
| 11. | Enter Warehouse Task Data | On the Create Warehouse Task dialog box, make the following entries:Src Trgt Qty AUoM: <your quantity>Whse Proc. Type: S997 - Putaway from Clarification |  |  |
| 12. | Create Warehouse Task | On the Create Warehouse Task dialog box, choose Create WT. | The following system message appears:Warehouse task xxx createdWarehouse order xxx created |  |
| 13. | Note Down Warehouse Order Number | Note down the Warehouse Task Number for testing purposes. |  |  |
| 14. | Choose Continue | Choose Continue. | In the Available Stock section, stock is not displayed anymore. |  |

##### Confirm Warehouse Tasks

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
| 1 | Log onto the SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad as a Warehouse Operative (EWM). |  |  |
| 2 | Access the SAP Fiori app | Open the SAP Fiori app Process Warehouse Tasks (F4595). |  |  |
| 3 | Enter Warehouse Task Number | On the Process Warehouse Tasks screen, make the following entries:Warehouse Task: <WT number noted down in the previous step>Choose Go. |  |  |
| 4 | Confirm Warehouse Task | Mark the checkbox for the selected warehouse task and choose Confirm. | The following system message appears: Warehouse task confirmed |  |

### Warehouse Outbound Processing

#### Assign Carrier (Optional)

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

#### Create Pick Warehouse Tasks

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

#### Confirm Warehouse Tasks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Pick List is printed in the step before and handed over now to the Warehouse Operative (EWM). He or she performs the warehouse tasks and confirms them in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Operative (EWM). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Fiori Process Warehouse Tasks (F4595). |  |  |
| 3 | Enter your Warehouse Task Number | On the Process Warehouse Tasks screen, make the following entries:Warehouse Task: <WT number noted down in the previous step>.Choose Go. |  |  |
| 4 | Confirm Warehouse Task | Mark the checkbox for the selected warehouse task and choose Confirm. | The following system message appears: Warehouse task <Warehouse Task Number> confirmed. |  |

#### Pack Goods into Shipping Handling Units (Optional)

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
| 1 | Log onto SAP Fiori Launchpad | Open the Fiori Launch Pad with the Warehouse Operative (EWM) role. | The Fiori Launch Pad is displayed. |  |
| 2 | Access the App | Open Fiori Pack Outbound Deliveries (F3193). | The Pack Outbound Deliveries (F3193) screen displays. |  |
| 3 | Enter your required values | Work Center: PACKStorage Bin: For example GI-AREA-01Choose Start Packing. | The Pack Outbound Deliveries (F3193) screen displays with a new view. |  |
| 4 | Create Handling Unit | Fill in your Reference Number:Outbound Delivery Order | A dialog box Create Shipping Handling Unit is displayed now. |  |
| 5 | Create Shipping Handling Unit | Select your favorite Packaging Material. Afterwards choose Create. | Your shipping unit is automatically created now. You can verify the Shipping Handling Unit number on the upper right corner. |  |
| 6 | Select stock to be packed | Select the material to be packed and choose Pack. Repeat this step as long as your destination handling unit has the right value of materials and quantity according to your needs. | According to your pack steps, you see ypour packed materials on the right side (Destination HU). |  |
| 7 | Printing Shipping HU Label | To print the manual shipping handling unit label, choose Print. | Your Shipping HU Label is printed now. |  |
| 8 | Close the Shipping Handling Unit | Choose Close for finalizing the pack process step.Then choose Leave for proceeding with the next step. | Note Consider that your destination handling unit is automatically created. The HU Label is automatically printed. On the left corner below, you can verify the created status. |  |

#### Print Loading Instruction (Optional)

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

#### Post Goods Issue

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

### Warehouse Physical Inventory

#### Variant 1: Create and Print Cycle Counting Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Operative (EWM) creates a physical inventory document for inventory counting.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Warehouse Operative (EWM). |  |  |
| 2 | Access App | Open Create Inventory Documents - Cycle Counting (/SCWM/PI_CC_CREATE). |  |  |
| 3 | Enter Selection Data | Maintain the following entries:Warehouse Number: 3350.Cycle Counting Indicator: A.Count Date: <Current date or date in the future>.Print PI Document: X.You can enter other selection data such as activity area, products, and storage bins.Choose Execute. | The PI document is created. |  |
| 4 | Create Physical Inventory Document | Select the line(s) for which a physical inventory should be processed.Choose Create.Note down the physical inventory document number. |  |  |

#### Variant 2: Create and Print Counting Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The warehouse operative creates the physical inventory document for inventory counting.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Operative (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Create Inventory Documents - Physical Inventory (/SCWM/PI_DOC_CREATE). |  |  |
| 3 | Enter Selection Data | Maintain the following entries:Warehouse Number: 3350.Physical Inventory Procedure: AL (Annual Physical Inventory (Storage-Bin-Specific))Note You can choose another physical inventory procedure, for example, HL, HS, or AS, according to your requirement.Count Date: <Current date or date in the future>Print PI Document: XYou can enter other selection data such as activity area, products, and storage bins.Choose Execute. | The PI document is created. |  |
| 4 | Create Physical Inventory Document | Select the lines for which a physical inventory should be processed.Choose Create.Note down the physical inventory document number. |  |  |

#### Enter Count Result

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Operative (EWM) enters the count result in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Operative (EWM). |  |  |
| 2 | Access App | Open Count Physical Inventory - Paper-Driven Counting (F3340). |  |  |
| 3 | Select Physical Inventory Document | Maintain the following selection values:Warehouse Number: 3350.Document Year: <Current Year>.Physical Inventory Document: <PI document created before>.Choose Go.Choose the PI document and choose Count. |  |  |
| 4 | Enter Count Results | Enter Counter.Enter Count Date and Time.If the count date is equal to the current date, you can leave the field blank as it is filled automatically.Enter Quantity and UoM.If the bin is empty, check 'Bin Empty'. |  |  |
| 5 | Save Your Changes | Choose Save. |  |  |

#### Confirm Inventory Count Results

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Clerk (EWM) checks the counting result and posts the difference. In case that the difference is outside tolerance, he or she can trigger the recounting.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk (EWM). |  |  |
| 2 | Access App | Open Confirm Inventory Count Results(/SCWM/MONNAV_PI_CONF). | The Enter warehouse number dialog box appears. |  |
| 3 | Enter warehouse number | In the Enter warehouse number dialog box, make the following entries:Warehouse No.: 1750. |  |  |
| 4 | Choose Continue. | Choose Continue. | The Confirm Inventory Count Result - Whse. <warehouse> (Time Zone <time zone>) screen appears. |  |
| 5 | Choose Set Selection Criteria. | On the Confirm Inventory Count Result - Whse. <warehouse> (Time Zone <time zone>) screen, choose Set Selection Criteria. | The /SCM/SAPLPI_HISTORY dialog box appears. |  |
| 6 | Search PI Document | In the /SCM/SAPLPI_HISTORY dialog box, make the following entries:Physical Inventory Status: COUN.Count Date: <Count Date you entered before>. |  |  |
| 7 | Choose Execute. | Choose Execute. | The screen displays an inventory count results table. |  |
| 8 | Select physical inventory document | Select one line with your physical inventory document. | The selected line is highlighted. |  |
| 9 | Choose More methods > Post Phys. Inv. Document. | Choose More methods > Post Phys. Inv. Document. | The Display Logs dialog box appears.The following system messages appear:Document <number> postedAction was executed successfully |  |
| 10 | Trigger Recount (optional) | If the selected PI document is not posted in the previous step, choose More methods > Recount Phys. Inv. Document to trigger the recounting. | The status of the PI document changes to RECO. A new PI document is created for recounting. |  |

#### Analyze Differences

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Clerk (EWM) posts the differences to the ERP to align the stock figures.

|  |
| --- |
| Note It is not possible to post the serial number differences on item level as this leads to problems upon lost and found of a serial number. See more details in note [2871065](https://me.sap.com/notes/2871065) |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on the SAP Fiori Launchpad as a Warehouse Clerk (EWM). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Analyze Differences(/SCWM/DIFF_ANALYZER). | The SAP dialog box appears. |  |
| 3 | Set Default Values | In the SAP dialog box, make the following entries:Warehouse No.: 1750.Phys. Inv. Diff.: X.WT Difference: X. |  |  |
| 4 | Choose Continue. | Choose Continue. | The Difference Analyzer - Warehouse<warehouse> (Time Zone <time zone>) screen appears. |  |
| 5 | Enter Product | On the Difference Analyzer - Warehouse<warehouse> (Time Zone <time zone>) screen, make the following entries:Find Product: <Product>Note Example: TG11 |  |  |
| 6 | Choose Search. | Choose Search. | The Differences – Cumulative table is displayed with records if differences were recorded before. |  |
| 7 | Select one record. | Select one record. | The selected line is highlighted. |  |
| 8 | Choose Post + Save. | Choose Post + Save. | The Post Differences? dialog box appears. |  |
| 9 | Choose Yes. | In the Post Differences? dialog box, choose Yes. | The following system message appears: Warehouse task <number> created. |  |

### Warehouse Posting Changes

#### Option 1: Posting Changes Triggered in Warehouse

##### Posting Change

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Posting change is initiated from the warehouse. For example, the Warehouse Clerk (EWM) wants to change the stock type from Unrestricted Use to Quality Inspection or to Blocked Stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk (EWM). |  |  |
| 2 | Access App | Open Create Posting Changes(/SCWM/MONNAV_CR_PC). | The Enter warehouse number dialog box appears. |  |
| 3 | Enter Warehouse Number | In the Enter warehouse number dialog box, make the following entries:Warehouse Number: 1750.Note: Skip this step if there's no dialog box to enter the warehouse number. |  |  |
| 4 | Choose Continue. | Choose Continue. | The /SCWM/SAPLSTOCK_OVERVIEW_MON dialog box appears. |  |
| 5 | Enter Product | In the /SCWM/SAPLSTOCK_OVERVIEW_MON dialog box, make the following entries:Product: <product>Note Example: TG11. |  |  |
| 6 | Choose Execute. | Choose Execute. | The Create Posting Change screen appears. |  |
| 7 | Select line | In the table Create Posting Change select the checkbox in one line. |  |  |
| 8 | Choose More Methods > Change Stock Type. | Choose More Methods > Change Stock Type. | The Change Stock Type dialog box appears. |  |
| 9 | Enter data | In the Change Stock Type dialog box, make the following entries:Stock Type: Q or B.Qty F. Post. Change: <Enter the quantity that you want to post the stock change for>.Whse Proc. Type: S400. |  |  |
| 10 | Choose Check Input (Enter). | Choose Check Input (Enter). | No error message appears. |  |
| 11 | Choose Create Posting Chg (F8). | Choose Create Posting Chg (F8). | The Display Logs dialog box appears.The following system messages appear:1 stock items created with quantity <quantity>Stock type for 1 stock items changed from F to BNote Example: if you entered stock type B and the stock type before was F.Warehouse task <number> createdWarehouse task <number> createdWarehouse order creation startedWarehouse order <number> created |  |
| 12 | Note down the warehouse task number. | Note down the warehouse task number. |  |  |
| 13 | Choose Continue. | In the Display Logs dialog box, choose Continue (Enter). | In the table Create Posting Change a new line with data you entered before is displayed. |  |

#### Option 2: Posting Changes Triggered in Inventory Management

##### Trigger Transfer Posting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Posting change is initiated from inventory management.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Transfer Stock - In-Plant(F1061). | The Transfer Stock – In-Plant screen is displayed. |  |
| 3 | Open Stock Overview | On the Transfer Stock – In-Plant screen, make the following entries:Material: TG11Plant: 1710 | The table Material by Storage Location is displayed. |  |
| 4 | Choose Transfer from Stock | Choose the Select icon beside the unrestricted stock for Storage Location175W that you want to transfer from. | The icons besides the other stock quantities change to the Target icon. |  |
| 5 | Choose Transfer to Blocked and Quality Stock | For stock transfer to blocked stock, choose the Target icon beside the blocked stock for Storage Location175W that you want to transfer to. | The Transfer Stock – In-Plant dialog box appears. |  |
| 6 | Enter quantity | In the Transfer Stock – In-Plant dialog box, make the following entries:Quantity: <your quantity> PC |  |  |
| 7 | Post | Choose Post. | The Success dialog box appears.The following system message appears:1 document has been created:Outbound Delivery Document<document number> |  |
| 8 | Choose OK. | In the Success dialog box, Choose OK. | The following system message appears:Outbound Delivery <document number> created |  |

##### Create Warehouse Tasks for Posting Changes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Clerk (EWM) creates warehouse tasks for posting changes.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk (EWM). |  |  |
| 2 | Access App | Open Process Posting Change Item(/SCWM/MONNAV_PROC_PC). | The /SCWM/SAPLWIP_POSTING_CHANGES dialog box appears. |  |
| 3 | Enter Data | In the SCWM/SAPLWIP_POSTING_CHANGES dialog box, make the following entries:Posting Change: <outbound delivery number from the previous step> |  |  |
| 4 | Choose Execute. | Choose Execute (F8). | The Process Posting ChangeItem screen appears.In the table Process Posting ChangeItem the document is displayed. |  |
| 5 | Select the checkbox | Select the checkbox in the line of the document. |  |  |
| 6 | Create WT in Background | Choose More Methods > Create WT in Background. | The Display Logs dialog box appears.The following system messages appear:Warehouse task <number> createdWarehouse order <number> created |  |
| 7 | Note down the warehouse task number. | Note down the warehouse task number. |  |  |
| 8 | Choose Continue. | In the Display Logs dialog box, choose Continue (Enter). |  |  |

#### Confirm Warehouse Task for Posting Changes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A put-away list / warehouse task list / pick list is printed and handed over to the Warehouse Operative (EWM), who performs the warehouse tasks and confirms them in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Operative (EWM). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Process Warehouse Tasks(F4595). | The Process Warehouse Tasks screen appears. |  |
| 3 | Enter Warehouse Task Number | On the Process Warehouse Tasks screen, make the following entries:Warehouse Task: <WT number noted down in the previous step> |  |  |
| 4 | Choose Go. | Choose Go. |  |  |
| 5 | Select the warehouse task checkbox. | Select the warehouse task checkbox. |  |  |
| 6 | Confirm Warehouse Task | Choose Confirm. | The following system message appears: Warehouse task <number> confirmed. |  |

### Replenishment in Warehousing

#### Replenish Stock

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can run through the following steps to perform a Planned Replenishment to create replenishment task(s).

In a real-life environment, you can schedule the Planned Replenishment Run as a regular background job.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad with theWarehouse Clerk (EWM) role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Replenish Stock (/SCWM/REPL). |  |  |
| 3 | Schedule Replenishment | On the Schedule Replenishment screen, make the following entries:Plnd Rplnshmt: X.Warehouse Number: 3350.Party Entitled to Dispose: 3350.Product: R_7000 or R_7003.Show Log Immediately: X .Choose Execute. |  |  |
| 4 | Perform Replenishment | On the Select Replenishment Items screen, check the proposed quantity to be replenished.Select the line item to be processed.Choose Perform ReplenishmentNote If the stock of R_7000 or R_7003 is not below the Min.Qty (4 PC) in the fixed storage bin, there is no replenishment proposal. The replenishment quantity is calculated as the difference between the maximum bin quantity and the current bin quantity, and then it is rounded to a multiple of the minimum replenishment quantity. You can maintain the minimum replenishment quantity in the product master via the Manage Product Master Data (F1602) app. See the details in the master data script Maintain Warehouse Products Attributes - MDS. If no minimum replenishment quantity is maintained in the product master, the system rounds the quantity with the basic Unit of Measure of the product. |  |  |

#### Schedule Job for Replenishment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to run job for warehouse replenishment.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk (EWM). | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Replenishment (F4319). |  |  |
| 3 | Enter Basic Parameters for New Job | Choose Create above the table.On the New Job screen, make the following entries:Job Template: Schedule Replenishment.Job Name: Schedule Replenishment for R_7000 or R_7003Choose Step 2. |  |  |
| 4 | Enter Scheduling Parameters for New Job | Choose Define Recurrence Pattern.On the Scheduling Information screen, make the following entries:Start Immediately: x.Recurrence Pattern: Single Run.Choose OK.Choose Step 3. |  |  |
| 5 | Enter Parameters | Parameters:Plnd Rplnshmnt: xWarehouse Number:3350Party Entitled to Dispose:3350Product:R_7000 or R_7003Execute in the Background:xShow Log Immediately:x |  |  |
| 6 | Schedule New Job | On the New Job screen, choose Schedule. | The new job is created and displays in the table of Application Jobs. |  |
| 7 | Refresh Application Jobs List | To check the status of the job you created, choose Go. | The Application Jobs table is refreshed. |  |
| 8 | Verify the Job Results | To see the outcome of the job, choose the icon in Results column. |  |  |

#### Check Replenishment Warehouse Tasks (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is for checking warehouse task from replenishment.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on to SAP Fiori Launchpad | Open the SAP Fiori Launchpad as a Warehouse Clerk (EWM). | The SAP Fiori launchpad is displayed. |  |
| 2. | Access the App | Open Warehouse Monitor (/SCWM/MON) |  |  |
| 3. | Select the node | On the Warehouse Management Monitor SAP - Warehouse Number xxxx screen, choose Documents > Warehouse Task. Double-click on the node. |  |  |
| 4. | Enter the selection data | Make the following entries:Whse Process Type: S310Product: R_7000 or R_7003.Choose Execute.Note down the warehouse task number. | The warehouse task for replenishment is displayed. |  |

#### Confirm Replenishment Warehouse Tasks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Operative (EWM) processes the replenishment warehouse task.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Operative (EWM). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Process Warehouse Tasks(F4595). |  |  |
| 3 | Enter Warehouse Task Number | On the Process Warehouse Tasks screen, make the following entries:Warehouse Task <WT number noted down in the previous step>.Choose Go. |  |  |
| 4 | Confirm Warehouse Task | Mark the checkbox for the selected warehouse task and choose Confirm. | The following system message appears: Warehouse task confirmed |  |

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
> Flagged while digesting this document, not verified: Sample data and preliminary steps use warehouse 3350, plant 3350, storage location 995W and articles R_7000/R_7003, but Confirm Inventory Count Results, Analyze Differences and Create Posting Changes use warehouse number 1750, and Transfer Stock - In-Plant uses plant 1710, storage location 175W and material TG11.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Define Default Values for Deliveries sets Shipping Point 3310, while the sample master data lists Shipping Point 3350 (SP DC 3350).

> [!warning] Conflict
> Flagged while digesting this document, not verified: Maintain Warehouse Product Attributes says Putaway and Stock Removal Control Indicators must be maintained differently for the replenishment process, yet the step enters SG01 for both.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[15-retail-operations/retail-logistics-with-third-party-warehouse-management-69m-ae-test-scr]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/69L_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 93,812 chars in the whole document
