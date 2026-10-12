---
id: 11-inventory-warehouse-and-transportation/test-script-sap-ewm-integration-stock-transport-orders-2vl-ae-sap-s-4h
title: "Test Script: SAP EWM Integration – Stock Transport Orders (2VL_AE), SAP S/4HANA Cloud Public Edition (2VL_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 2VL_AE: stock transport orders with SAP EWM, in three EWM/inventory-managed transfer scenarios."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/intracompany-stock-transfers]
aliases: [2VL_S4CLD2608_BPD_EN_AE]
keywords: [Stock Transfers Within a Company Code, stock transport orders, sap ewm integration, test scripts, stock transfer, replenishment delivery, warehouse tasks, goods issue, goods receipt, putaway]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2VL_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-881
topic: 11-inventory-warehouse-and-transportation/intracompany-stock-transfers
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: SAP EWM Integration – Stock Transport Orders (2VL_AE), SAP S/4HANA Cloud Public Edition (2VL_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2VL_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Stock Transfers Within a Company Code** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | SAP EWM Integration – Stock Transport Orders (2VL_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232850840)

[2 Prerequisites 4](#_Toc232850841)

[2.1 Additional Manual Configuration 4](#_Toc232850842)

[2.2 System Access 4](#_Toc232850843)

[2.3 Roles 4](#_Toc232850844)

[2.4 Master Data, Organizational Data, and Other Data 5](#_Toc232850845)

[2.5 Business Conditions 6](#_Toc232850846)

[3 Preliminary Steps 7](#_Toc232850847)

[3.1 Initial Stock Upload in Supplying Warehouse 7](#_Toc232850848)

[3.1.1 Data Files for Initial Stock Upload 7](#_Toc232850849)

[3.1.2 Adopt Business Partner ID in .csv Files When Deviating from Default Business Partner Number 7](#_Toc232850850)

[3.1.2.1 Upload Initial Stock 7](#_Toc232850851)

[4 Creating Stock in Supplying Plant 10](#_Toc232850852)

[5 Create User Settings for Transaction /SCWM/PRDO 11](#_Toc232850853)

[6 Check Stock Level for the EWM Products 12](#_Toc232850854)

[7 Overview Table 13](#_Toc232850855)

[8 Test Procedures 16](#_Toc232850856)

[8.1 Stock Transfer Between EWM Managed Storage Location 16](#_Toc232850857)

[8.1.1 Create Stock Transport Order 16](#_Toc232850858)

[8.1.2 Create Replenishment Delivery for Stock Transport Order 17](#_Toc232850859)

[8.1.3 Check Outbound Delivery Orders in SAP EWM (Optional) 19](#_Toc232850860)

[8.1.4 Create Warehouse Tasks Manually in SAP EWM 20](#_Toc232850861)

[8.1.5 Pick Warehouse Orders in SAP EWM 20](#_Toc232850862)

[8.1.6 Post Goods Issue for Outbound Delivery Order in SAP EWM 21](#_Toc232850863)

[8.1.7 Check Status of Stock Transfer 22](#_Toc232850864)

[8.1.8 Check Inbound Delivery (Optional) 23](#_Toc232850865)

[8.1.9 Post Goods Receipt in SAP EWM 24](#_Toc232850866)

[8.1.10 Create Warehouse Tasks for Putaway in SAP EWM 25](#_Toc232850867)

[8.1.11 Putaway of Products in SAP EWM 26](#_Toc232850868)

[8.1.12 Check Status of Stock Receipt 27](#_Toc232850869)

[8.2 Stock Transfer from Inventory Managed Storage Location to EWM Managed Storage Location 28](#_Toc232850870)

[8.2.1 Create Stock Transport Order 28](#_Toc232850871)

[8.2.2 Create Replenishment Delivery for Stock Transport Order 30](#_Toc232850872)

[8.2.3 Pick and Post Goods Issue for Stock Transport Order 31](#_Toc232850873)

[8.2.4 Check Status of Stock Transfer 32](#_Toc232850874)

[8.2.5 Check Inbound Delivery (Optional) 33](#_Toc232850875)

[8.2.6 Post Goods Receipt in SAP EWM 34](#_Toc232850876)

[8.2.7 Create Warehouse Tasks for Putaway in SAP EWM 35](#_Toc232850877)

[8.2.8 Putaway of Products in SAP EWM 36](#_Toc232850878)

[8.2.9 Check Status of Stock Receipt 37](#_Toc232850879)

[8.3 Stock Transfer from EWM Managed Storage Location to Inventory Managed Storage Location 38](#_Toc232850880)

[8.3.1 Create Stock Transport Order 38](#_Toc232850881)

[8.3.2 Create Replenishment Delivery for Stock Transport Order 40](#_Toc232850882)

[8.3.3 Check Outbound Delivery Orders in SAP EWM (Optional) 41](#_Toc232850883)

[8.3.4 Create Warehouse Tasks Manually in SAP EWM 42](#_Toc232850884)

[8.3.5 Pick Warehouse Orders in SAP EWM 43](#_Toc232850885)

[8.3.6 Post Goods Issue for Outbound Delivery Order in SAP EWM 44](#_Toc232850886)

[8.3.7 Check Status of Stock Transfer 45](#_Toc232850887)

[8.3.8 Check Inbound Delivery 45](#_Toc232850888)

[8.3.9 Post Goods Receipt for Stock Transport Order 46](#_Toc232850889)

[8.3.10 Check Status of Stock Receipt 47](#_Toc232850890)

## Purpose

Overview

Using stock transport orders, you can execute a stock transfer process from one plant to another within the same company code. The process starts with the creation of a stock transport order. A warehouse clerk at the shipping plant monitors the materials due for shipment and creates deliveries as required. Once a delivery is created, the system replicates it to the SAP Extended Warehouse Management (EWM) system, where an outbound delivery order is created. Warehouse tasks are created with reference to the outbound delivery order and the physical process for picking is executed. After the goods issue is posted in the SAP EWM system and sent back to the SAP S/4HANA Cloud Public Edition, an inbound delivery is created and replicated to SAP EWM automatically. This document serves as the starting point for the inbound process in the receiving plant.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/59dede30672930d654d1b779f7890167)

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
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Receiving Specialist | SAP_BR_RECEIVING_SPECIALIST | Receiving | SAP_BR_RECEIVING_SPECIALIST |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

| Data | Sample Value | Details | Comment |
| --- | --- | --- | --- |
| Material | TG11 | Trading Good for Reg. Trading (MRP planning) |  |
| Company Code | 3310 | Company Code 3310 |  |
| Sales Organization | 3310 | Dom. Sales Org |  |
| Plant | 3310 |  |  |
| Storage Location | 333D |  |  |
| Storage Location | 333S |  |  |
| Warehouse | 333 |  |  |
| EWM Warehouse | 3330 |  |  |
| Division | 00 |  |  |
| Distribution Channel | 00 |  |  |
| Shipping Point | 3310 |  |  |
| Ent. To Dispose | 33413310 |  |  |
| Plant | 3320 |  |  |
| Storage Location | 334D |  |  |
| Storage Location | 334S |  |  |
| ERP Warehouse | 334 |  |  |
| EWM Warehouse | 3340 |  |  |
| Shipping Point | 3320 |  |  |

For more information on creating master data objects, refer to the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

| MDS | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |

### Business Conditions

Procedure

| Scope Item ID | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS |  |
| BME - Stock Transfer with Delivery |  |

## Preliminary Steps

### Initial Stock Upload in Supplying Warehouse

#### Data Files for Initial Stock Upload

The different .csv data files referred to in the following sections of this process are available as attachments to the SAP Note [2620457](https://launchpad.support.sap.com/#/notes/2620457) of the solution package.

Attached to the SAP Note are the following .zip files:

Initial_Stock_Upload_Data_DE.zip

The zip file contains all necessary data to populate stock for the example products.

To provide full pallets only into the High Rack (StType Y001), you apply the following .csv file:

isu_Y001_STO.csv

#### Adopt Business Partner ID in .csv Files When Deviating from Default Business Partner Number

The sample .csv files provided for you to use when uploading the stock data contain a default ID,

33413320

This ID is for the business partner (representing the plant) which is used in its roles as Owner and Party Entitled to Dispose.

If you change the default ID, for example, because your plant has a different ID and/or you used a different prefix, other than 33413320,

you need to update that value for the business partner in all .csv files. Otherwise, the upload transaction fails, indicating that the business partner does not exist.

You must find and replace the business partner ID, 33413320 with your actual ID in all of the provided files.

##### Upload Initial Stock

Purpose

In a real business case, the materials are purchased from external suppliers; in that case that process is covered by the standard purchasing processes. For the purpose of this test, we post initial stock upload directly to the Storage Locations 334S.

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
| /SCWM/ISU | SAP Menu > SCM Extended Warehouse Management > Extended Warehouse Management > Interfaces > Data Upload > Stock Data Transfer |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the Transaction | Access the transaction using one of the navigation options above. |  |  |
| 2 | Enter the Data | In the Stock Data Transfer screen, ensure that the following fields are complete:Warehouse Number: 3340.Language: English.Number of HUs per posting: 50.Do not Post Data in ERP:Local File: X.Display Data:X. |  |  |
| 3 | Upload the File for Initial Stock Upload | Choose Open Folder.Choose Import.Locate the*.csv files on your computer.isu_Y001_STO.csvChoose Open.The system displays the path and file name of the selected .csv file.On the Stock Data Transfer screen, choose Upload.Choose OK. | On the Stock Data Transfer screen, the uploaded rows from the .csv file are displayed. |  |
| 4 | Upload the Initial Stock | Choose Start Stock Data transfer (F8)Record the number of the warehouse material document for later use. | The message Warehouse Material Document is displayed in the lower part of the screen. |  |

## Creating Stock in Supplying Plant

Purpose

In a real business case, the materials are purchased from external suppliers; in that case that process is covered by the standard purchasing or subcontracting processes. For the purpose of this test, we post initial stock directly to the storage locations.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori launchpad | Log on to the SAP Fiori Launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Post Goods Movement screen displays. |  |
| 3 | Select Goods Receipt Other | Choose Goods Receipt - Other. |  |  |
| 4 | Choose Goods Receipt-Other | Make the following entries:Movement type: 561Material number: For example TG11Quantity: For example, 100 PCPlant: 3320Storage location: 332A |  |  |
| 5 | Check | Choose Check. | Document is OK. |  |
| 6 | Post | Choose Post. | The Material document XXX posted and materials are available in stock. |  |

## Create User Settings for Transaction /SCWM/PRDO

Use

In this step, you can set up user settings that are necessary for transaction: /SCWM/PRDO.

Procedure

1. Access the transaction using one of the following navigation options:

| Transaction Code | Easy Access Menu(SAP EWM) |
| --- | --- |
| /SCWM/PRDO | SCM Extended Warehouse Management > Extended Warehouse Management > Delivery Processing > Outbound Delivery > Maintain Outbound Delivery Orders |

1. In the dialog box, make the following entries:

| Field Name | Description | User Action and Values | Comment |
| --- | --- | --- | --- |
| Warehouse Number |  | 3340 |  |
| Shipping Office |  | YWAREHOUSE-3340 |  |
| Ent. To Dispose |  | 33413320 |  |

1. Choose Continue (Enter).

|  |
| --- |
| Note If the dialog box does not appear, you may choose Default Values (F5). |

## Check Stock Level for the EWM Products

Procedure

1. Access the transaction using one of the following navigation options:

| Transaction Code | Easy Access Menu(SAP EWM) |
| --- | --- |
| /SCWM/MON | SCM Extended Warehouse Management > Extended Warehouse Management > Monitoring > Warehouse Management Monitor |

1. In the Warehouse Management Monitor dialog box, make the following entries:

| Field Name | Description | User Action and Values | Comment |
| --- | --- | --- | --- |
| Warehouse Number |  | 3340 |  |
| Monitor |  | SAP | SAP Cross Industries Warehouse |

1. Choose Execute (F8).
2. In the hierarchy in the left screen area, choose Stock and Bin → Available Stock.
3. On the /SCWM/SAPLSTOCK_OVERVIEW_MON screen, make the following entries:

| Field Name | Description | User Action and Values | Comment |
| --- | --- | --- | --- |
| Product Number |  | TG11 |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Stock Transfer Between EWM-Managed Storage Location:

| Process Step, Report, or Item | Business Role | App Name / Transaction | Expected Results |
| --- | --- | --- | --- |
| r[Create Stock Transport Order](#unique_15) [page ] 16 | Purchaser | Create Purchase Order - Advanced (ME21N) |  |
| [Create Replenishment Delivery for Stock Transport Order](#unique_16) [page ] 17 | Shipping Specialist | My Purchase Orders - Due for Delivery (VL10B) |  |
| [Check Outbound Delivery Orders in SAP EWM (Optional)](#unique_17) [page ] 19 |  | Change Outbound Delivery (VL02N) |  |
| [Check Status of Stock Transfer](#unique_18) [page ] 22 | Warehouse Clerk | Stock - Single Material (F1076) |  |
| [Check Inbound Delivery (Optional)](#unique_19) [page ] 23 | Receiving Specialist | Display Inbound Delivery (VL33N) |  |
| [Post Goods Receipt in SAP EWM](#unique_20) [page ] 24 |  | /SCWM/PRDI |  |
| [Create Warehouse Tasks for Putaway in SAP EWM](#unique_21) [page ] 25 |  | /SCWM/TODLV_I |  |
| [Putaway of Products in SAP EWM](#unique_22) [page ] 26 |  | /SCWM/TO_CONF |  |
| [Check Status of Stock Receipt](#unique_23) [page ] 27 | Warehouse Clerk | Stock - Single Material (F1076) |  |

Stock Transfer from Inventory-Managed Storage Location to EWM-Managed Storage Location:

| Process Step, Report, or Item | Business Role | App Name / Transaction | Expected Results |
| --- | --- | --- | --- |
| r[Create Stock Transport Order](#unique_24) [page ] 28 | Purchaser | Create Purchase Order - Advanced (ME21N) |  |
| [Create Replenishment Delivery for Stock Transport Order](#unique_25) [page ] 30 | Shipping Specialist | My Purchase Orders - Due for Delivery (VL10B) |  |
| [Pick and Post Goods Issue for Stock Transport Order](#unique_26) [page ] 31 |  | /SCWM/PRDO |  |
| [Create Warehouse Tasks Manually in SAP EWM](#unique_27) [page ] 42 |  | /SCWM/PRDO |  |
| [Pick Warehouse Orders in SAP EWM](#unique_28) [page ] 43 |  | /SCWM/TO_CONF |  |
| [Post Goods Issue for Outbound Delivery Order in SAP EWM](#unique_29) [page ] 44 |  | /SCWM/PRDO |  |
| [Check Status of Stock Receipt](#unique_30) [page ] 37 | Warehouse Clerk | Stock - Single Material (F1076) |  |
| [Check Inbound Delivery (Optional)](#unique_31) [page ] 33 | Receiving Specialist | Display Inbound Delivery (VL33N) |  |
| [Post Goods Receipt in SAP EWM](#unique_32) [page ] 34 |  | /SCWM/PRDI |  |
| [Create Warehouse Tasks for Putaway in SAP EWM](#unique_33) [page ] 35 |  | /SCWM/TODLV_I |  |
| [Putaway of Products in SAP EWM](#unique_34) [page ] 36 |  | /SCWM/TO_CONF |  |
| [Check Status of Stock Receipt](#unique_30) [page ] 37 | Warehouse Clerk | Stock - Single Material (F1076) |  |

Stock Transfer from EWM-Managed Storage Location to Inventory Managed Storage Location

| Process Step, Report, or Item | Business Role | App Name / Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Stock Transport Order](#unique_35) [page ] 38 | Purchaser | Create Purchase Order - Advanced (ME21N) |  |
| [Create Replenishment Delivery for Stock Transport Order](#unique_36) [page ] 40 | Shipping Specialist | My Purchase Orders - Due for Delivery (VL10B) |  |
| [Check Outbound Delivery Orders in SAP EWM (Optional)](#unique_37) [page ] 41 |  | /SCWM/PRDO |  |
| [Create Warehouse Tasks Manually in SAP EWM](#unique_27) [page ] 42 |  | /SCWM/PRDO |  |
| [Pick Warehouse Orders in SAP EWM](#unique_28) [page ] 43 |  | /SCWM/TO_CONF |  |
| [Post Goods Issue for Outbound Delivery Order in SAP EWM](#unique_29) [page ] 44 |  | /SCWM/PRDO |  |
| [Check Status of Stock Transfer](#unique_38) [page ] 45 | Warehouse Clerk | Stock - Single Material (F1076) |  |
| [Check Inbound Delivery](#unique_39) [page ] 45 | Receiving Specialist | Display Inbound Delivery (VL33N) |  |
| [Post Goods Receipt for Stock Transport Order](#unique_40) [page ] 46 | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843) |  |
| [Check Status of Stock Receipt](#unique_41) [page ] 47 | Warehouse Clerk | Stock - Single Material (F1076) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Stock Transfer Between EWM Managed Storage Location

#### Create Stock Transport Order

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
| 1 | Log on to SAP Fiori launchpad | Open the SAP Fiori Launchpadas a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Create Purchase Order | Open Create Purchase Order - Advanced (ME21N). | Create Purchase Order - Advanced (ME21N) screen displays. |  |
| 3 | Enter Purchase Order Document Type | Enter the following data:Order Type: UD (StockTranspOrderDel).Then choose Enter. |  |  |
| 4 | Enter Purchase Order data | Enter the following data:Supplying Plant: 3320.On the Org. Data tab:Purchasing Org.: 3310.Purchasing Group: 002.Company Code: 3310.In the area of Item Overview:Material: TG11PO Quantity: 1Order Unit: PALNote The system converts 1 PAL into 48 PC automatically.Delivery Date: any date in the future.Plant: 3310.Storage Location: 333S.On the Partners tab of header details:Partner Function: VN.Number:33413320.Then choose Enter.Choose tab page Confirmations.Enter the following data:Conf. Control: Inbound Delivery, then choose Enter.Currently the system triggers an availability check. Based on the results of the checks, if requested availability cannot be fulfilled, the Confirmation Proposal screen shows up and the user needs to make decision based on the result of the checks. | All data are entered, the item detail screen displays. |  |
| 5 | Save Purchase Order | Choose Save and when the purchase order number is displayed, write it down for further use. | A new Purchase Order is created. Purchase Order Number displays.Write down the Stock Transport Order number for further usage. |  |

#### Create Replenishment Delivery for Stock Transport Order

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
| 1 | Log on to SAP Fiori launchpad | Open the SAP Fiori Launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open My Purchase Orders - Due for Delivery (VL10B). | The Goods Movement screen displays. |  |
| 3 | Enter data for PO display | Choose the Purchase Orders tab and make the following entries then choose Execute.Shipping Point / Receiving Point: 3320.Delivery Creation dates (From): delivery creation From date Delete the default date.Delivery Creation dates (To): delivery creation To date Delete the default date .CalcRuleDefltDlvCrDt:Purchasing Document: Choose a Stock transport order that created in step: Create Stock Transport Order. | The Activities Due for Shipping Purchase Orders, Fast Display screen appears. PO due to delivery is listed out. |  |
| 4 | Create delivery | Select stock transport orders from the list. Choose Background to create delivery in background. | The Activities Due for Shipping Purchase Orders, Fast Display screen appears. |  |
| 5 | Check delivery number | Choose More > Show/Hide Delivery , and note down the delivery number shown in the SD Doc. field. | A delivery is created. |  |
| 6 | Choose Delivery | Choose Delivery Number. | The System navigates you to the delivery display screen. |  |
| 7 | Change Delivery | Choose Display > Change .In the item line, enter the following data:Storage Location: 334S. |  |  |
| 8 | Save Delivery | Choose Save. |  |  |

#### Check Outbound Delivery Orders in SAP EWM (Optional)

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
| /SCWM/PRDO | SCM Extended Warehouse Management > Extended Warehouse Management > Delivery Processing > Outbound Delivery > Maintain Outbound Delivery Order. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the Transaction | Access the transaction using one of the navigation options above. |  |  |
| 2 | Enter Default Value | Choose Default Value.Make the following entries:Warehouse Number: 3340.Shipping Office: YWAREHOUSE-3340.Entitled To Dispose: 33413320.Choose Enter. |  |  |
| 3 | Search Outbound Delivery Order | On the Maintain Outbound Delivery Order- Warehouse No. XXXX screen, choose ERP Document beside the field Find.Enter the number of the delivery from the previous step.Choose Perform Search. |  |  |
| 4 | Note the EWM Outbound Delivery | Note the Outbound Deliveries Document Number. |  |  |
| 5 | Stay in the Transaction | Do not close the screen and continue with the next step. |  |  |

#### Create Warehouse Tasks Manually in SAP EWM

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
| /SCWM/PRDO | SCM Extended Warehouse Management > Extended Warehouse Management > Delivery Processing > Outbound Delivery > Maintain Outbound Delivery Order |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Continue from Previous Step |  |  |  |
| 2 | Create Warehouse tasks manually | Select Outbound Delivery order and use the menu More > Outbound Delivery Order > Follow-on Functions > Warehouse Task on upper-left screen.Select all Warehouse request and choose Create + Save Warehouse Task.Note down the warehouse order number. |  |  |

#### Pick Warehouse Orders in SAP EWM

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
| /SCWM/TO_CONF | SCM Extended Warehouse Management > Extended Warehouse Management > Excecution > Confirm Warehouse Task |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access Transaction | Access the transaction using one of the navigation options above. |  |  |
| 2 | Search Warehouse Order | Enter the Warehouse Order Number and choose Execute Search |  |  |
| 3 | Confirm the Picking | Choose Confirm + Save. |  |  |

#### Post Goods Issue for Outbound Delivery Order in SAP EWM

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
| /SCWM/PRDO | SCM Extended Warehouse Management > Extended Warehouse Management > Delivery Processing > Outbound Delivery > Maintain Outbound Delivery Order |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access Transaction | Access the transaction using one of the navigation options above. |  |  |
| 2 | Search Outbound Delivery Order | On the Maintain Outbound Delivery Order- Warehouse No. XXXX screen, choose ERP Document beside the field Find.Enter the number of the delivery from the previous step.Choose Perform Search. | Outbound Delivery Orders that have a route depart. Date (corresponds to the delivery date in the sales order and outbound delivery) within the selection period display in the page. |  |
| 3 | Post Goods Issue | Select your ODOs, and choose Goods Issue + Save. |  |  |

#### Check Status of Stock Transfer

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
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Stock - Single Material (F1076). | The Stock - Single Material screen displays. |  |
| 3 | Enter Transfer Order data | Enter material TG11 and choose Enter. | You receive an overview of the material. This concerns all material that have left the supplying plant and have not yet reached the receiving plant. |  |

#### Check Inbound Delivery (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you check the (SAP S/4HANA) Inbound deliveries, which are created automatically upon the goods issue for outbound delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori Launchpad as a Receiving Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Display Inbound Delivery (VL33N). | The Inbound delivery screen displays. |  |
| 3 | Select Inbound Delivery | On the Display Inbound Delivery (VL33N) screen, choose F4 (Matchcode Search).In the Delivery (1) dialog box, choose External delivery number of supplier.If you cannot see this option, choose the button with 3 full stop sign on the right-hand side and choose it from the dropdown list.Make the following entry:External Delivery ID: <00+Replenishment Delivery Number>.Choose Find.Double-click to select the inbound delivery based on the external delivery number. |  |  |
| 4 | Display Inbound Delivery | On the Display Inbound Delivery (VL33N) screen, choose Enter.On the Inbound Delivery Display: Overview screen, go to the Status Overview tab page. |  |  |

#### Post Goods Receipt in SAP EWM

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
| /SCWM/PRDI | SAP Menu > SCM Extended Warehouse Management > Extended Warehouse Management > Delivery Processing > Inbound Delivery > Maintain Inbound Delivery |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access Transaction | Access the transaction using one of the navigation options above. | The Maintain Inbound Delivery screen appears. |  |
| 2 | Enter Default Value | Choose Default Values.Make the following entries:Warehouse Number: 3330.Shipping Office: YWAREHOUSE-3330.Entitled To Dispose: 33413310.Choose Enter. |  |  |
| 3 | Choose Find Purchase Order | On the Maintain Inbound Delivery screen, from the Find drop down list choose Purchase Order. |  |  |
| 4 | Enter purchase order number | Make the following entries:Find: Purchase Order <your stock Transport order number>. |  |  |
| 5 | Choose Perform Search. | Choose Perform Search. | The following system message appears: One document was readThe Inbound Delivery appears in the View | . |
| 6 | Select the Inbound Delivery Notification. | In the List View, select the Inbound Delivery. |  |  |
| 7 | Choose Goods Receipt. | Choose Goods Receipt. | The following system message appears: <UI text> |  |

#### Create Warehouse Tasks for Putaway in SAP EWM

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
| /SCWM/TODLV_I | SAP Menu > SCM Extended Warehouse Management Extended Warehouse Management > Work Scheduling > Create Warehouse Task for Warehouse Request > Putaway for Inbound Delivery |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access Transaction | Access the transaction using one of the navigation options above. | The Create Warehouse Task - Warehouse Number <number> - Putaway screen appears. |  |
| 2 | Open Advanced Search | On the Create Warehouse Task - Warehouse Number > number > Putaway screen, choose Open Advanced Search. | The Advanced Search sub screen appears. |  |
| 3 | Enter purchase order number | On Advanced Search sub screen in the References section, make the following entries:Purchase Order: <your purchase order number> |  |  |
| 4 | Choose Advanced Search | Choose Advanced Search. | The warehouse requests appear in the table. |  |
| 5 | Navigate to Warehouse Request tab. | Navigate to Warehouse Request tab. |  |  |
| 6 | Select All. | On Warehouse Request tab in the table, choose Select All. |  |  |
| 7 | Choose Create + Save. | On Warehouse Request tab, choose Create+ Save. | The following system message appears: <number> warehouse tasks were created |  |
| 8 | Note down the warehouse order | Note down the warehouse order for testing purposes. |  |  |

#### Putaway of Products in SAP EWM

Procedure

| Transaction Code | SAP EWM Menu |
| --- | --- |
| /SCWM/TO_CONF | SAP Menu > SCM Extended Warehouse Management > Extended Warehouse Management > Execution > Confirm Warehouse Task |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access Transaction | Access the transaction using one of the navigation options above. | The Confirm Warehouse Task in Warehouse Number <number> screen appears. |  |
| 2 | Choose Find Warehouse Order | On the Confirm Warehouse Task in Warehouse Number <number> screen, from the Find drop down list choose Warehouse Order. |  |  |
| 3 | Enter warehouse order number | Make the following entries:Find: Warehouse Order <your warehouse order number> |  |  |
| 4 | Choose Perform Search. | Choose Perform Search. | The following system message appears: Selection produced <number> resultsThe Warehouse Order appears in the View. |  |
| 5 | Select the Warehouse Order. | In the List View, select the Warehouse Order. |  |  |
| 6 | Create Pick-HU | Choose tab page Pick-HU.Choose Create (the option before the Delete option).Choose Switch to Form View.Make the following entries:Pack. Material: PMPAL00.Choose Create HU (the option after the Delete option). |  |  |
| 7 | Choose Confirm in Foreground | Choose Confirm in Foreground. | The warehouse task(s) appear on Product WT tab. |  |
| 8 | Choose the warehouse task(s) | On the Product WT tab, choose the warehouse task(s). |  |  |
| 9 | Choose Confirm in Foreground | Choose Confirm in Foreground. | WT Status is updated to Confirmed in Foreground. |  |
| 10 | Save your entries | Save your entries | The following system message appears: Warehouse task <warehouse task number> was confirmed |  |

Adjust the following process overview table to suit your scope item by listing all process step, report, or items described in this document (see example below).

#### Check Status of Stock Receipt

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
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Stock - Single Material (F1076). | The Stock - Single Material screen displays. |  |
| 3 | Enter Transfer Order data | Enter material TG11 and choose Enter. | You receive an overview of the material. This concerns all material that has reached the receiving plant. |  |

### Stock Transfer from Inventory Managed Storage Location to EWM Managed Storage Location

#### Create Stock Transport Order

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
|  | Log on to SAP Fiori launchpad | Open the SAP Fiori Launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Create Purchase Order | Open Create Purchase Order - Advanced (ME21N). | Create Purchase Order - Advanced (ME21N) screen displays. |  |
| 3 | Enter Purchase Order Document Type | Enter the following data:Order Type: UD (StockTranspOrderDel).Then choose Enter. |  |  |
| 4 | Enter Purchase Order data | Enter the following data:Supplying Plant: 3320.On the Org. Data tab:Purchasing Org.: 3310.Purchasing Group: 002.Company Code: 3310.In the area of Item Overview:Material: TG11PO Quantity: 1Order Unit: PALNote The system converts 1 PAL into 48 PC automatically.Delivery Date: any date in the future.Plant: 3310Storage Location: 333S.On the Partners tab of header details:Partner Function: VN.Number:33413320.Then choose Enter.Choose Confirmation tab.Enter the following data:Conf. Control: Inbound DeliveryThen choose Enter.Currently the system triggers an availability check. Based on the results of the checks, if requested availability cannot be fulfilled, the confirmation proposal screen shows up and the user needs to make decision based on the result of the checks. | All data are entered, the item detail screen displays. |  |
| 5 | Save Purchase Order | Choose Save and when the purchase order number is displayed, write it down for further use. | A new Purchase Order is created. Purchase Order Number is displayed.Write down the Stock Transport Order number for further usage. |  |

#### Create Replenishment Delivery for Stock Transport Order

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
| 1 | Log on to SAP Fiori launchpad | Open the SAP Fiori Launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open My Purchase Orders - Due for Delivery (VL10B). | The Goods Movement screen displays. |  |
| 3 | Enter data for PO display | Choose the Purchase Orders tab and make the following entries then choose Execute:Shipping Point/Receiving Point: 3320Delivery Creation dates (From): delivery creation From date Delete the default dateDelivery Creation dates (To): delivery creation To date Delete the default dateCalcRuleDefltDlvCrDt:Purchasing Document: Choose a Stock Transport Order that created in step: Create Stock Transport Order | The Activities Due for Shipping Purchase Orders, Fast Display screen appears. PO due to delivery is listed out. |  |
| 4 | Create delivery | Select stock transport orders from the list. Choose Background to create delivery in background. | The Activities Due for Shipping Purchase Orders, Fast Display screen appears. |  |
| 5 | Check delivery number | Choose More > Show/Hide Delivery , note down the delivery number shown in the SD Document field. | A delivery is created. |  |

#### Pick and Post Goods Issue for Stock Transport Order

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
| 1 | Log on to SAP Fiori launchpad | Log on to the SAP Fiori Launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). | The Change Outbound Deliver screen displays. |  |
| 3 | Enter delivery number | On the Change Outbound Delivery (VL02N) screen, enter the delivery document number from the earlier section and choose Continue. | The Replenishment Dlv. XXXXXXXX Change: Overview screen displays. |  |
| 4 | Enter picking data | Choose Picking tab, and make the following entries:Picked Qty: 48 PC.Choose Save. | The system shows the message: Replenishment Dlv. XXXXXXXX has been saved. The screen return to the Change Outbound Delivery screen. |  |
| 5 | Post goods issue | On the Change Outbound Delivery (VL02N) screen, choose Post Goods Issue. |  |  |

#### Check Status of Stock Transfer

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
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Stock - Single Material (F1076). | The Stock - Single Material screen displays. |  |
| 3 | Enter Transfer Order data | Enter material TG11 and choose Enter. | You receive an overview of the material. This concerns all material that has left the supplying plant and has not yet reached the receiving plant. |  |

#### Check Inbound Delivery (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can check the (SAP S/4HANA) Inbound deliveries, which are created automatically upon the goods issue for outbound delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori Launchpad as a Receiving Specialist. | The Fiori Launch Pad is displayed. |  |
| 2 | Access the App | Open Display Inbound Delivery (VL33N). | The Inbound delivery screen is displayed. |  |
| 3 | Select Inbound Delivery | On the Display Inbound Delivery (VL33N) screen, choose F4 (Matchcode Search).In the Delivery (1) dialog box, choose External delivery number of supplier.If you cannot see this option, choose the button with 3 full stop sign on the right-hand side and choose it from the dropdown menu.Make the following entry:External Delivery ID: <00+Replenishment Delivery Number>Choose Find.Double-click to select the inbound delivery based on the external delivery number. |  |  |
| 4 | Display Inbound Delivery | On the Display Inbound Delivery (VL33N) screen, choose Enter.On the Inbound Delivery Display: Overview screen, go to the Status Overview tab page. |  |  |

#### Post Goods Receipt in SAP EWM

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
| /SCWM/PRDI | SAP Menu > SCM Extended Warehouse Management > Extended Warehouse Management > Delivery Processing > Inbound Delivery > Maintain Inbound Delivery |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access Transaction | Access the transaction using one of the navigation options above. | The Maintain Inbound Delivery screen appears. |  |
| 2 | Enter Default Value | Choose Default ValuesMake the following entries:Warehouse Number: 3330.Shipping Office: YWAREHOUSE-3330.Entitled To Dispose: 33413310.Choose Enter. |  |  |
| 3 | Choose Find Purchase Order | On the Maintain Inbound Delivery screen, from the Find dropdown list, choose Purchase Order. |  |  |
| 4 | Enter purchase order number | Make the following entries:Find: Purchase Order <your stock Transport order number> . |  |  |
| 5 | Choose Perform Search. | Choose Perform Search. | The following system message appears: One document was read.The Inbound Delivery appears in the View. |  |
| 6 | Select the Inbound Delivery Notification. | In the List View select the Inbound Delivery. |  |  |
| 7 | Choose Goods Receipt. | Choose Goods Receipt. | The following system message appears: <UI text> |  |

#### Create Warehouse Tasks for Putaway in SAP EWM

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
| /SCWM/TODLV_I | SAP Menu > SCM Extended Warehouse Management > Extended Warehouse Management > Work Scheduling > Create Warehouse Task for Warehouse Request > Putaway for Inbound Delivery . |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access Transaction | Access the transaction using one of the navigation options above. | The Create Warehouse Task - Warehouse Number <number> - Putaway screen appears. |  |
| 2 | Open Advanced Search | On the Create Warehouse Task > Warehouse Number > <number> > Putaway screen, choose Open Advanced Search. | The Advanced Search sub screen appears |  |
| 3 | Enter purchase order number | On the Advanced Search sub screen in the References section, make the following entries:Purchase Order: <your purchase order number> |  |  |
| 4 | Choose Advanced Search | Choose Advanced Search. | The warehouse requests appear in the table. |  |
| 5 | Navigate to Warehouse Request tab. | Navigate to Warehouse Request tab. |  |  |
| 6 | Select All. | On Warehouse Request tab in the table, choose Select All. |  |  |
| 7 | Choose Create + Save. | On Warehouse Request tab, choose Create + Save. | The following system message appears: <number> warehouse tasks were created |  |
| 8 | Note down the warehouse order | Note down the warehouse order for testing purposes. |  |  |

#### Putaway of Products in SAP EWM

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
| 1 | Access Transaction | Access the transaction using one of the navigation options above. | The Confirm Warehouse Task in Warehouse Number <number> screen appears. |  |
| 2 | Choose Find Warehouse Order | On the Confirm Warehouse Task in Warehouse Number <number> screen, from the Find dropdown list choose Warehouse Order. |  |  |
| 3 | Enter warehouse order number | Make the following entries:Find: Warehouse Order <your warehouse order number>. |  |  |
| 4 | Choose Perform Search. | Choose Perform Search. | The following system message appears: Selection produced <number> results.The Warehouse Order appears in the View. |  |
| 5 | Select the Warehouse Order. | In the List View, select Warehouse Order. |  |  |
| 6 | Create Pick-HU | Choose tab page Pick-HU.Choose Create(the button before the Delete)Choose Switch to Form ViewMake the following entries:Pack. Material: PMPAL00Choose Create HU(the button after the Delete) |  |  |
| 7 | Choose Confirm in Foreground | Choose tab page Product WT.Choose Confirm in Foreground. | WT Status is updated to Confirmed in Foreground. |  |
| 10 | Save your entries | Save your entries | The following system message appears: Warehouse task <warehouse task number> was confirmed |  |

Adjust the following process overview table to suit your scope item by listing all process step, report, or items described in this document (see example below).

#### Check Status of Stock Receipt

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
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Stock - Single Material (F1076). | The Stock - Single Material screen displays. |  |
| 3 | Enter Transfer Order data | Enter material TG11 and choose Enter. | You receive an overview of the material. This concerns all material that has reached the receiving plant. |  |

### Stock Transfer from EWM Managed Storage Location to Inventory Managed Storage Location

#### Create Stock Transport Order

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
| 1 | Log on to SAP Fiori launchpad | Open the SAP Fiori Launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Create Purchase Order | Open Create Purchase Order - Advanced (ME21N). | Create Purchase Order - Advanced (ME21N) screen displays. |  |
| 3 | Enter Purchase Order Document Type | Enter the following data:Order Type: UD (StockTranspOrderDel).Then choose Enter. |  |  |
| 4 | Enter Purchase Order data | Enter the following data:Supplying Plant: 3310.On the Org. Data tab:Purchasing Org.: 3310.Purchasing Group: 002.Company Code: 3310.In the area of Item Overview:Material: TG11PO Quantity: 1Order Unit: PALNote System converts 1 PAL into 48 PC automatically.Delivery Date: any date in the future.Plant: 3320.Storage Location: 332A.On the Partners tab of header details:Partner Function: VN.Number:33413310.Then choose Enter.Choose tab Confirmation.Enter the following data:Conf. Control: Inbound Delivery.Then choose Enter.Currently the system triggers an availability check. Based on the results of the checks, if requested availability cannot be fulfilled, the confirmation proposal screen shows up and the user needs to make decision based on the result of the checks. | All data are entered, the item detail screen displays. |  |
| 5 | Save Purchase Order | Choose Save and when the purchase order number is displayed, write it down for further use. | A new Purchase Order is created. Purchase Order Number is displayed.Write down the Stock Transport Order number for further usage. |  |

#### Create Replenishment Delivery for Stock Transport Order

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
| 1 | Log on to SAP Fiori launchpad | Open the SAP Fiori Launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open My Purchase Orders - Due for Delivery (VL10B). | The Goods Movement screen displays |  |
| 3 | Enter data for PO display | Choose Purchase Orders tab and make the following entries then choose Execute:Shipping Point / Receiving Point: 3310.Delivery Creation dates (From): delivery creation From date Delete the default date .Delivery Creation dates: (To): delivery creation To date Delete the default date .CalcRuleDefltDlvCrDt:Purchasing Document: Choose a Stock Transport Order that created in step: Create Stock Transport Order. | The Activities Due for Shipping Purchase Orders, Fast Display screen appears. PO due to delivery is listed out. |  |
| 4 | Create delivery | Select stock transport orders from the list. Choose Background to create delivery in background. | The Activities Due for Shipping Purchase Orders, Fast Display screen appears. |  |
| 5 | Check delivery number | Choose More > Show/Hide Delivery , and note down the delivery number shown in the SD Doc. field. | A delivery is created. |  |
| 6 | Choose Delivery | Choose the delivery number | The System navigates you to the delivery display screen. |  |
| 7 | Change Delivery | Choose Display > Change .In the item line, enter the following data:Storage Location: 333S. |  |  |
| 8 | Save Delivery | Choose Save. |  |  |

#### Check Outbound Delivery Orders in SAP EWM (Optional)

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
| /SCWM/PRDO | SCM Extended Warehouse Management > Extended Warehouse Management > Delivery Processing > Outbound Delivery > Maintain Outbound Delivery Order |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the Transaction | Access the transaction using one of the navigation options above. |  |  |
| 2 | Enter Default Value | Choose Default Values.Make the following entries:Warehouse Number: 3330.Shipping Office: YWAREHOUSE-3330.Ent. To Dispose: 33413310.Choose Enter. |  |  |
| 3 | Search Outbound Delivery Order | On the Maintain Outbound Delivery Order- Warehouse No. XXXX screen, choose ERP Document beside the field Find.Enter the number of the delivery from the previous step.Choose Perform Search. |  |  |
| 4 | Note the EWM Outbound Delivery | Note the outbound deliveries document number. |  |  |
| 5 | Stay in the Transaction | Do not close the screen and continue with the next step. |  |  |

#### Create Warehouse Tasks Manually in SAP EWM

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
| /SCWM/PRDO | SCM Extended Warehouse Management > Extended Warehouse Management > Delivery Processing > Outbound Delivery > Maintain Outbound Delivery Order |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Continue from Previous Step |  |  |  |
| 2 | Create Warehouse tasks manually | Select Outbound Delivery order and use the menu More > Outbound Delivery Order > Follow-on Functions > Warehouse Task on upper-left screen.Select all warehouse request and choose the Create + Save Warehouse Task.Note down the warehouse order number. |  |  |

#### Pick Warehouse Orders in SAP EWM

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
| /SCWM/TO_CONF | SCM Extended Warehouse Management > Extended Warehouse Management > Excecution > Confirm Warehouse Task |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access Transaction | Access the transaction using one of the navigation options above. |  |  |
| 2 | Search Warehouse Order | Enter the warehouse order number and choose Execute Search |  |  |
| 3 | Confirm the Picking | Choose Confirm + Save. |  |  |

#### Post Goods Issue for Outbound Delivery Order in SAP EWM

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
| /SCWM/PRDO | SCM Extended Warehouse Management > Extended Warehouse Management > Delivery Processing > Outbound Delivery > Maintain Outbound Delivery Order |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access Transaction | Access the transaction using one of the navigation options above. |  |  |
| 2 | Search Outbound Delivery Order | On the Maintain Outbound Delivery Order- Warehouse No. XXXX screen, choose ERP Document beside the field Find.Enter the number of the delivery from the previous step.Choose Perform Search. | Outbound Delivery Orders that have a Route Depart. Date (corresponds to the delivery date in the sales order and outbound delivery) within the selection period display in the page. |  |
| 3 | Post Goods Issue | Choose your ODOs, and choose Goods Issue + Save. |  |  |

#### Check Status of Stock Transfer

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
| 1 | Log on | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Stock - Single Material (F1076). | The Stock - Single Material screen displays. |  |
| 3 | Enter Transfer Order data | Enter material TG11 and choose Enter. | You receive an overview of the material. This concerns all material that has left the supplying plant and has not yet reached the receiving plant. |  |

#### Check Inbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you check the (SAP S/4HANA) inbound deliveries, which are created automatically upon the goods issue for outbound delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori Launchpad as a Receiving Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Change Inbound Delivery (VL32N). | The Inbound delivery screen is displayed. |  |
| 3 | Select Inbound Delivery | On the Change Inbound Delivery (VL32N) screen, choose F4 (Matchcode Search).In the Delivery (1) dialog box, choose External delivery number of supplier.If you cannot see this option, choose the icon with 3 full stop signs on the right-hand side and choose it from the dropdown list.Make the following entry:External Delivery ID: <00+Replenishment Delivery Number>.Choose Find.Double-click to select the inbound delivery based on the external delivery number. |  |  |
| 4 | Display Inbound Delivery | On the Change Inbound Delivery (VL32N) screen, choose Enter.For the delivery items, enter the following data:Putaway QtyOn the Inbound Delivery Display: Overview screen, go to the Status Overview tab page to check the inbound delivery status.Choose Save. |  |  |

#### Post Goods Receipt for Stock Transport Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can perform this activity when you want to check the inbound delivery for stock transport order and post goods receipt.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Open Post Goods Receipt for Inbound Delivery | Open Post Goods Receipt for Inbound Delivery (F2502). | The Post Goods Receipt for Inbound Delivery screen displays. |  |
| 3 | Enter Delivery | Enter the inbound delivery you checked in the previous step. |  |  |
| 4 | Post Goods Receipt | Select the delivery item and choose Post. |  |  |
| 5 | Confirm the Message | Choose OK to confirm the material document. |  |  |

#### Check Status of Stock Receipt

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
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Stock - Single Material (F1076). | The Stock - Single Material screen displays. |  |
| 3 | Enter Transfer Order data | Enter material TG11 and choose Enter. | You receive an overview of the material. This concerns all material that has reached the receiving plant. |  |

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
> Flagged while digesting this document, not verified: The Overview Table disagrees with the test procedures on several apps: for 8.1 it lists VL02N for 'Check Outbound Delivery Orders' while the procedure uses /SCWM/PRDO; for 8.2 it lists /SCWM/PRDO for 'Pick and Post Goods Issue' while the procedure uses VL02N; for 8.3 it lists VL33N (Display Inbound Delivery) and F0843 while the procedures use VL32N (Change Inbound Delivery) and F2502.

> [!warning] Conflict
> Flagged while digesting this document, not verified: The Overview Table for the 8.2 scenario lists EWM outbound steps (Create Warehouse Tasks Manually, Pick Warehouse Orders, Post Goods Issue, pointing to pages 42-44) that have no matching procedure in section 8.2 and belong to section 8.3.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[11-inventory-warehouse-and-transportation/test-script-cross-plant-transfer-posting-1p7-ae-752]]
- related-to :: [[11-inventory-warehouse-and-transportation/test-script-stock-transfer-with-delivery-bme-ae-sap-s-4hana-cloud-publ]]
- related-to :: [[11-inventory-warehouse-and-transportation/test-script-stock-transfer-without-delivery-bmh-ae-sap-s-4hana-cloud-p]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2VL_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 68,395 chars in the whole document
