---
id: 11-inventory-warehouse-and-transportation/test-script-sap-ewm-integration-batch-management-2vn-ae-sap-s-4hana-cl
title: "Test Script: SAP EWM Integration – Batch Management (2VN_AE), SAP S/4HANA Cloud Public Edition (2VN_S4CLD2608_BPD_EN_AE)"
description: "S/4HANA Cloud Public Edition test script for scope item 2VN (AE): batch creation in S/4HANA or EWM, PO, inbound delivery, goods receipt, putaway, batch checks."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/ewm-inbound-processing]
aliases: [2VN_S4CLD2608_BPD_EN_AE]
keywords: [Warehouse Inbound Processing and SAP EWM Inbound Integration, batch management, ewm integration, batch creation, test scripts, inbound delivery, purchase order creation, goods receipt posting, warehouse task putaway, batch information cockpit]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2VN_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-883
topic: 11-inventory-warehouse-and-transportation/ewm-inbound-processing
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: SAP EWM Integration – Batch Management (2VN_AE), SAP S/4HANA Cloud Public Edition (2VN_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2VN_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Warehouse Inbound Processing and SAP EWM Inbound Integration** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | SAP EWM Integration – Batch Management (2VN_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232850932)

[2 Prerequisites 4](#_Toc232850933)

[2.1 Additional Manual Configuration 4](#_Toc232850934)

[2.2 System Access 4](#_Toc232850935)

[2.3 Roles 4](#_Toc232850936)

[2.4 Master Data, Organizational Data, and Other Data 5](#_Toc232850937)

[2.5 Business Conditions 6](#_Toc232850938)

[3 Overview Table 7](#_Toc232850939)

[4 Test Procedures 9](#_Toc232850940)

[4.1 Option 1: Create Batch in the SAP S/4HANA Cloud Public Edition System 9](#_Toc232850941)

[4.1.1 Create Batch 9](#_Toc232850942)

[4.1.2 Create Purchase Order 10](#_Toc232850943)

[4.1.3 Create Inbound Delivery 12](#_Toc232850944)

[4.1.4 Post Goods Receipt in SAP EWM 13](#_Toc232850945)

[4.1.5 Check Material Document After Goods Receipt (Optional) 15](#_Toc232850946)

[4.1.6 Create Warehouse Tasks for Putaway in SAP EWM 17](#_Toc232850947)

[4.1.7 Putaway of Products in SAP EWM 18](#_Toc232850948)

[4.1.8 Check Inbound Delivery (Optional) 19](#_Toc232850949)

[4.1.9 Check Material Document After Putaway (Optional) 21](#_Toc232850950)

[4.1.10 Batch Information Cockpit - Display Batch (Optional) 22](#_Toc232850951)

[4.1.11 Check Physical Stock - Batch After Creation (Optional) 23](#_Toc232850952)

[4.1.12 Batch Information Cockpit - Change Batch (Optional) 25](#_Toc232850953)

[4.1.13 Check Physical Stock - After Batch Changes (Optional) 26](#_Toc232850954)

[4.2 Option 2: Create Batch in the SAP EWM System 28](#_Toc232850955)

[4.2.1 Create Purchase Order 28](#_Toc232850956)

[4.2.2 Create Inbound Delivery 29](#_Toc232850957)

[4.2.3 Create and Assign Batch in SAP EWM - Optional 30](#_Toc232850958)

[4.2.4 Maintain Batches for Product in SAP EWM (Optional) 32](#_Toc232850959)

[4.2.5 Post Goods Receipt in SAP EWM 33](#_Toc232850960)

[4.2.6 Check Material Document After Goods Receipt (Optional) 36](#_Toc232850961)

[4.2.7 Create Warehouse Tasks for Putaway in SAP EWM 37](#_Toc232850962)

[4.2.8 Putaway of Products in SAP EWM 39](#_Toc232850963)

[4.2.9 Check Inbound Delivery (Optional) 40](#_Toc232850964)

[4.2.10 Check Material Document After Putaway (Optional) 41](#_Toc232850965)

[4.2.11 Batch Information Cockpit - Display Batch (Optional) 43](#_Toc232850966)

[4.2.12 Check Physical Stock - Batch After Creation (Optional) 44](#_Toc232850967)

[4.2.13 Batch Information Cockpit - Change Batch (Optional) 45](#_Toc232850968)

[4.2.14 Check Physical Stock - After Batch Changes (Optional) 47](#_Toc232850969)

[4.3 Process Integration 48](#_Toc232850970)

[5 Appendix 49](#_Toc232850971)

[5.1 Preceding Processes 49](#_Toc232850972)

[5.2 Succeeding Processes 49](#_Toc232850973)

## Purpose

Overview

This scope item describes the basic integration of batches in the goods receipt process with SAP Extended Warehouse Management (EWM). It allows you to create batches in the SAP S/4HANA Cloud Public Edition and in the SAP EWM system as required. When creating batches in SAP S/4HANA Cloud Public Edition, the batch master record is distributed to the EWM system. During the creation of a purchase order, the business user can enter the batch number for each purchase order item. Once a purchase order is available, an inbound delivery is created and replicated to the SAP EWM system. The batch number is distributed as part of the delivery item. If you don't assign a specific batch in the purchase order / inbound delivery, you can search for a fitting batch or create a new one in SAP EWM. In this case, the batch data is transferred to the SAP S/4HANA Cloud Public Edition system.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/3a10753530b2c3cc9428573a7e542240)

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
| Quality Technician | SAP_BR_QUALITY_TECHNICIAN | Quality Inspection | SAP_BR_QUALITY_TECHNICIAN |  |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |
| Receiving Specialist | SAP_BR_RECEIVING_SPECIALIST | Receiving | SAP_BR_RECEIVING_SPECIALIST |  |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Administrator - Data Replication | SAP_BR_ADMINISTRATOR_DATA_REPL |  |  |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | TG21 | Trad.Good 21,Reorder Point,Batch-FIFOBatch Class: YB_BATCH Batch FIFO (first-in-first-out)Characteristic 1: Batch NumberCharacteristic 2: Supplier Batch Number |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 333D | Decentral EWM received on dock |  |
| Storage Location | 333S | Decentral EWM available for sales |  |
| Warehouse | 333 | Decentral EWM-managed warehouse in SAP S/4HANA |  |
| Purchasing Organization | 3310 | Purch. Org. 3310 |  |
| Purchasing Group | 001 | Group 001 |  |
| EWM Warehouse | 3330 | Decentral EWM warehouse |  |
| Batch Class | YB_BATCH | Batch FIFO (first-in-first-out) |  |
| Characteristic | YB_BATCH_NUMBER | Batch Number |  |
| Characteristic | YB_SUPPLIER_BATCH_NUMBER | Vendor Batch Number |  |
| Supplier | 33300001 | Domestic Supplier 1 |  |

You can find general information on how to create master data objects in the following Master Data Scripts (MDS):

| MDS | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |

|  |
| --- |
| Note Make sure that the following fields are filled out in business partner (BP) data before start testing:State tax Number (identification tab)ICMS Contributor (Control tab)IPI Contributor (Control tab)PIS Contributor (Control tab)COFINS Contributor (Control tab)ICMS-ST Contributor (Control tab)ISS Contributor (Control tab) (mandatory for buying services)In the Supplier role, on the Vendor: Tax Data tab, fill out the fields accordingly.Failure to complete the fields result in an error in the invoice entry process. |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS master data script. Posting Period is up to date. |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | System | Expected Results |
| --- | --- | --- | --- | --- |
| [Create Batch](#unique_9) [page ] 9 | Quality Technician | Create Batch (MSC1N) | SAP S/4HANA | The following system message appears: Creating batch numberBatch successfully saved. |
| [Create Purchase Order](#unique_10) [page ] 10 | Purchaser | Create Purchase Order - Advanced (ME21N) | SAP S/4HANA | The following system message appears: Standard PO created under the number your PO number. |
| [Create Inbound Delivery](#unique_11) [page ] 12 | Receiving Specialist | Inbound Deliveries for Purchase Orders (VL34) | SAP S/4HANA | The following system message appears: Inbound Delivery your inbound delivery number has been saved |
| [Post Goods Receipt in SAP EWM](#unique_12) [page ] 13 |  | Maintain Inbound Delivery | SAP Extended Warehouse Management | The following system message appears: Inbound Delivery number changed |
| [Check Material Document After Goods Receipt (Optional)](#unique_13) [page ] 15 | Inventory Manager | Material Documents Overview (F1077) | SAP S/4HANA | The Delivery Note is equal to the reference Warehouse Material Document from the previous step. |
| [Create Warehouse Tasks for Putaway in SAP EWM](#unique_14) [page ] 17 |  | Putaway for Inbound Delivery | SAP Extended Warehouse Management | The following system message appears: Warehouse order number created |
| [Putaway of Products in SAP EWM](#unique_15) [page ] 18 |  | Confirm Warehouse Task | SAP Extended Warehouse Management | The following system message appears: Warehouse task warehouse task number was confirmed |
| [Check Inbound Delivery (Optional)](#unique_16) [page ] 19 | Receiving Specialist | Display Inbound Delivery (VL33N) | SAP S/4HANA | In the Overall Status - Delivery table, check that the Overall Goods Movement Status is C Completely processed.In the Delivery Item Status (All Items) table, check that the Goods Movement Status for the items is C Completely processed. |
| [Check Material Document After Putaway (Optional)](#unique_17) [page ] 21 | Inventory Manager | Material Documents Overview (F1077) | SAP S/4HANA | The Delivery Note is equal to the reference Warehouse Material Document from the previous step. |
| [Batch Information Cockpit - Display Batch (Optional)](#unique_18) [page ] 22 | Quality Technician | Batch Information Cockpit (BMBC) | SAP S/4HANA | The Details (Batch Master) sub screen appears. |
| [Check Physical Stock - Batch After Creation (Optional)](#unique_19) [page ] 23 |  | Warehouse Management Monitor | SAP Extended Warehouse Management | The Display Batch screen appears. |
| [Batch Information Cockpit - Change Batch (Optional)](#unique_20) [page ] 25 | Quality Technician | Batch Information Cockpit (BMBC) | SAP S/4HANA | The following system message appears: Changing batch your batch number. |
| [Check Physical Stock - After Batch Changes (Optional)](#unique_21) [page ] 26 |  | Warehouse Management Monitor | SAP Extended Warehouse Management | The Display Batch screen appears. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Option 1: Create Batch in the SAP S/4HANA Cloud Public Edition System

This section describes test procedures for each process step that belongs to this scope item.

You have two options to create batches:

1. You create the batch in the SAP S/4HANA Cloud Public Edition system before you create the purchase order (option 1 described here).
2. You create the batch in the SAP EWM system when you maintain the inbound delivery (option 2 described later).

#### Create Batch

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Even when most batches are automatically created, it is also sometimes necessary to create batches manually. If you create a batch before the creation of a purchase order, you can enter the batch number directly in the purchase order item.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Fiori launchpad | Log on to the SAP Fiori launchpad as a Quality Technician. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Create Batch (MSC1N). | The Create Batch screen appears. |  |
| 3 | Enter Material and Plant | On the Create Batch screen, make the following entries:MaterialTG21Plant: 3310 |  |  |
| 4 | Choose Enter. | Choose Enter. | The Automatic batch number allocation dialog box appears. |  |
| 5 | In the Automatic batch number assignment dialog box, choose OK. | In the Automatic batch number assignment dialog box, choose OK. | The Basic Data 1 tab appears. |  |
| 6 | Enter Basic Data 1 | On the Basic Data 1 tab, make the following entries:Supplier Batch: 4711-today's date |  |  |
| 7 | Navigate to the Classification tab. | Navigate to the Classification tab. | Values for the batch class are displayed:Batch Number: <specific batch value>Vendor Batch Number: <Number under which the batch is managed at the supplier's> |  |
| 8 | Save your entries. | Save your entries. | The following system message appears: Creating batch batch numberBatch successfully saved. |  |
| 9 | Note down the Batch Number. | Note down the batch number. |  |  |

#### Create Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can use the Create Purchase Order - Advanced (ME21N) app to create a new purchase order (PO) from scratch.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Create Purchase Order - Advanced (ME21N). | The Create Purchase Order screen appears. |  |
| 3 | Enter Order Type and Supplier | Make the following entries:Order Type (Purchasing): Standard POSupplier (F0354): 33300001 |  |  |
| 4 | Expand Header | Choose Expand Header | Header data is displayed in detail. |  |
| 5 | Navigate to Org Data Tab | Navigate to the Org. Data tab. |  |  |
| 6 | Enter Organizational Data | On the Org. Data tab, make the following entries:Purch. Org.: 3310Purch. Group: 002Company Code: 3310 |  |  |
| 7 | Expand Items | Choose Expand Items. | The item table appears. |  |
| 8 | Enter Item | In the Items table, make the following entries:Material: TG21PO Quantity: 1Plnt: 3310 |  |  |
| 9 | Enter Storage Location Batch | In the Items table, make the following entries:Stor. Location: 333DBatch: batch numberNote Enter the batch number you've created in step Create Batch. Leave the batch number empty if you want to create the batch later in the following step of option 2: Create and Assign Batch in SAP EWM. |  |  |
| 10 | Navigate to Confirmations Tab | On the Item Details sub screen, navigate to the Confirmations tab. |  |  |
| 11 | Enter Confirmation Control | On the Confirmations tab, make the following entries:Conf. Control: Inbound Delivery. |  |  |
| 12 | Save Your Entries | Save your entries. | The following system message appears: Standard PO created under the number <your PO number> |  |
| 13 | Note Down Your Purchase Order Number | Note down your purchase order number for testing purposes. |  |  |

#### Create Inbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inbound delivery informs the SAP EWM system about relevant changes and updated data.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori launchpad | Log on to the SAP Fiori launchpad as a Receiving Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Create Inbound Delivery (VL31N) | The Create Inbound Delivery - Delivery screen appears. |  |
| 3 | Enter purchase order number | Make the following entries:Purchase Order: <your purchase order number> |  | I c |
| 4 | Choose Continue | Choose Continue. | The Inbound Delivery Create: Overview screen appears. |  |
| 5 | Save your entries | On the Inbound Delivery Create: Overview tab, save your entries. | The following system message appears: Inbound Delivery <number> was saved and distributed to the WMS |  |

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
| 2 | Choose Default Values (F5). | On the Maintain Inbound Delivery screen, choose Default Values(F5). | The Maintain Inbound Delivery - Warehouse Number dialog box appears. |  |
| 3 | Check or make the following entries | In the Maintain Inbound Delivery - Warehouse Number dialog box, check or make the following entries:Warehouse No.: 1730Goods Receipt Office: YWAREHOUSE-1730Ent. to Dispose: 17411710 |  |  |
| 4 | Choose Continue (Enter). | Choose Continue. |  |  |
| 5 | Choose Find Purchase Order | On the Maintain Inbound Delivery screen, from the Find drop down list, choose Purchase Order. |  |  |
| 6 | Enter purchase order number | Make the following entries:Find: Purchase Order your purchase order number |  |  |
| 7 | Choose Perform Search. | Choose Perform Search. | The following system message appears: One document was read.The Inbound Delivery appears in the table. |  |
| 8 | Select the Inbound Delivery. | Click on the row containing the inbound delivery document. | The inbound delivery line appears selected. (indicated by the highlighting).Once selected, the corresponding Items section below (showing Item Number 10 with Standard Delivery Item) will display the line items associated with that inbound delivery document. |  |
| 9 | Choose Menu > Inbound Delivery > Follow-On Functions > Pack (Ctrl+F3). | Choose Menu > Inbound Delivery > Follow-On Functions > Pack (Ctrl+F3). | The Work Center Packing for Inbound Delivery screen appears. |  |
| 10 | On the Work Center Packing for Inbound Delivery screen, navigate to the Create HU tab. | On the Work Center Packing for Inbound Delivery screen, navigate to the Create HU tab. |  |  |
| 11 | Enter packaging material | On the Create HU tab, make the following entries:Pack. Material: PMPAL00 |  |  |
| 12 | On the Create HU tab, choose Execute. | On the Create HU tab, choose Execute. | The following system message appears: HU number (PMPAL00) was constructed |  |
| 13 | Drag and drop inbound delivery item node to HU node. | On the Work Center Packing for Inbound Delivery screen, in the tree area drag the node with your product from the inbound delivery item. Drop it to the node with the HU number you created in the previous step. | The inbound delivery item is packed on the HU. |  |
| 14 | Choose Save and go back. | Choose Save and go back. | On the Status tab, the Status Type Packing is set to Completed. |  |
| 15 | On the Maintain Inbound Delivery screen, choose Check. | On the Maintain Inbound Delivery screen, choose Check. | The following system message appears: Activity was carried out successfully Blocked (Overall Status)It turns to Status Green. |  |
| 16 | Choose Goods Receipt. | Choose Goods Receipt. | The following system message appears: Inbound Delivery number changedIn the Document Flow tab in the document flow table, a new line with the document category Goods Receipt is added.On the Status tab, the Status Type Goods Receipt is set to Completed. |  |

#### Check Material Document After Goods Receipt (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Along with populating the warehouse with stock, there is also a financial posting in the SAP S/4HANA system.

The check step is to show you the material document along with its financial posting in the SAP S/4HANA system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad as a Inventory Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Choose Material Documents Overview (F1077). | The Material Documents Overview (F1077) screen appears. |  |
| 3 | Change Settings | On the Material Documents Overview (F1077) screen in section Material Documents, choose Settings on the right-hand side. | The View Settings dialog box appears. |  |
| 4 | View Settings | In the View Settings dialog box, select the column for Goods Movement Type. |  |  |
| 5 | Confirm | Choose OK. |  |  |
| 6 | Enter Selection Data | On top of the screen, make the following entries:Stock Change: STOCK INCREASEStock Change Level: PlantPlant: 3310Storage Location: 333DMaterial: TG21Posting Date: the date when you posted the goods receipt in the warehouse. |  |  |
| 7 | Check the Material Document | Choose Go. | The material documents are listed. |  |
| 8 | Note down Material Document Number | Note down the number of the Material Document Item with Goods Movement Type GR goods receipt (101). |  |  |
| 9 | Select Material Document | Choose the SAP S/4HANA Material Document. |  |  |
| 10 | Check Delivery Note Field | On the General Information tab, compare the Delivery Note with the reference Warehouse Material Document from the previous step. | The Delivery Note is equal to the reference Warehouse Material Document from the previous step. |  |
| 11 | Compare Item data | Compare the Item data of the Material Document Item with the item data of the Inbound Delivery Item of the SAP EWM system. | The Item data of the Material Document Item is equal to the item data of the Inbound Delivery Item of the SAP EWM system. |  |
| 12 | Navigate to the Process Flow tab | Navigate to the Process Flow tab. | The process flow documents are flagged with OK.The Accounting Document is displayed. |  |

#### Create Warehouse Tasks for Putaway in SAP EWM

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can create warehouse tasks manually using the transaction Putaway for Inbound Delivery.

Procedure

| Transaction Code | SAP EWM Menu |
| --- | --- |
| /SCWM/TODLV_I | SAP Menu > SCM Extended Warehouse Management > Extended Warehouse Management > Work Scheduling > Create Warehouse Task for Warehouse Request > Putaway for Inbound Delivery |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access Transaction | Access the transaction using one of the navigation options above. | The Create Warehouse Task - Warehouse Number number - Putaway screen appears. |  |
| 2 | Open Advanced Search | On the Create Warehouse Task - Warehouse Number number - Putaway screen, choose Open Advanced Search. | The Advanced Search sub screen appears. |  |
| 3 | Enter purchase order number | On the Advanced Search sub screen in the References section, make the following entries:Purchase Order: <your purchase order number> |  |  |
| 4 | Choose Advanced Search | Choose Advanced Search. | The warehouse request appears in the table. |  |
| 5 | Choose Close Advanced Search. | Choose Close Advanced Search. |  |  |
| 6 | Navigate to Warehouse Request tab. | Navigate to Warehouse Request tab. |  |  |
| 7 | Select All. | On the Warehouse Request tab in the table, choose Select All. |  |  |
| 8 | Choose Create + Save. | On the Warehouse Request tab, choose Create Warehouse Task. | The following system message appears: <number> warehouse tasks were created |  |
| 9 | Save your entries | Save your entries. | The following system message appears: Warehouse order <number> created |  |
| 10 | Note down the warehouse order | Note down the warehouse order for testing purposes. |  |  |

#### Putaway of Products in SAP EWM

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can confirm and save all warehouse tasks in one go, in the background. If you want to change data, you can also confirm individual warehouse tasks manually and then save them, in other words, confirm the individual warehouse tasks in the foreground. The following describes the manual confirmation in the foreground.

Procedure

| Transaction Code | SAP EWM Menu |
| --- | --- |
| /SCWM/TO_CONF | SAP Menu > SCM Extended Warehouse Management > Extended Warehouse Management > Execution > Confirm Warehouse Task |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access Transaction | Access the transaction using one of the navigation options above. | The Confirm Warehouse Task in Warehouse Number number screen appears. |  |
| 2 | Choose Find Warehouse Order | On the Confirm Warehouse Task in Warehouse Number <number> screen, from the Find dropdown list, choose Warehouse Order. |  |  |
| 3 | Enter warehouse order number | Make the following entries:Find: Warehouse Order your warehouse order number |  |  |
| 4 | Choose Perform Search. | Choose Perform Search. | The following system message appears: Selection produced number resultsThe warehouse order appears on the screen. |  |
| 5 | Select the Warehouse Order. | In the List View, select the Warehouse Order. |  |  |
| 6 | Choose Confirm in Foreground | Choose Confirm in Foreground. | The warehouse task(s) appear on the Product WT tab. |  |
| 7 | Navigate to the Product WT tab | Navigate to the Product WT tab. |  |  |
| 8 | Choose the warehouse task(s) | On the Product WT tab in the warehouse task table, select the warehouse task(s). |  |  |
| 9 | Choose Confirm in Foreground | Choose Confirm in Foreground. | The WT Status is updated to Confirmed in Foreground. |  |
| 10 | Save your entries | Save your entries. | The following system message appears: Warehouse task warehouse task number was confirmed |  |

#### Check Inbound Delivery (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you check the inbound deliveries in SAP S/4HANA, which were generated as a consequence of the goods receipt processing in SAP EWM.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad as a Receiving Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Display Inbound Delivery (VL33N). | The Display Inbound Delivery (VL33N) screen appears. |  |
| 3 | Enter Inbound Delivery | On the Display Inbound Delivery (VL33N) screen, make the following entries:Inbound Delivery: <inbound delivery number from step Create Inbound Delivery> |  |  |
| 4 | Choose Continue | On the Display Inbound Delivery (VL33N) screen, choose Continue. | The Inbound Delivery number Display: Overview screen appears. |  |
| 5 | Navigate to the Status Overview tab | Navigate to the Status Overview tab. |  |  |
| 6 | Check that the Overall Goods Movement Status is C Completely processed. | In the Overall Status - Delivery table, check that the Overall Goods Movement Status is C Completely processed. |  |  |
| 7 | Check that the Goods Movement Status for the items is C Completely processed. | In the Delivery Item Status (All Items) table, check that the Goods Movement Status for the items is C Completely processed. |  |  |
| 8 | Choose Document Flow. | On the Inbound Deliver<inbound delivery number> Display overview screen, choose Document Flow. | The Document Flow screen appears. |  |
| 9 | Note down the material document number for goods movement type TF SLoc to SLoc | On the Document Flow screen in the Document column, note down the material document number for the goods movement type TF SLoc to SLoc for testing purposes. |  |  |

#### Check Material Document After Putaway (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Along with populating the warehouse with stock, there is also a financial posting in the SAP S/4HANA system.

The check step is to show you the material document along with its financial posting in the SAP S/4HANA system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad as a Inventory Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Choose Material Documents Overview (F1077). | The Material Documents Overview (F1077) screen appears. |  |
| 3 | Change Settings | On the Material Documents Overview (F1077) screen in section Material Documents, choose Settings on the right-hand side. | The View Settings dialog box appears. |  |
| 4 | View Settings | In the View Settings dialog box, select the column for Goods Movement Type.Choose Storage Location (Transfer). |  |  |
| 5 | Confirm | Choose OK. |  |  |
| 6 | Enter Selection Data | On top of the screen, make the following entries:Stock Change: Transfer PostingStock Change Level: PlantExample:Plant: 3310Material Documents Overview (F1077): <your material document from the previous step> |  |  |
| 7 | Check the Material Document | Choose Go. | The material documents are listed. |  |
| 8 | Select Material Document | Choose the SAP S/4HANA Material Document. | The Material Documents Overview (F1077) screen appears. |  |
| 9 | Navigate to the Items tab | Navigate to the Items tab. | The Goods Movement Type is TF SLoc to SLoc (411).The Quantity is the amount you confirmed in the putaway before.The Receiving Storage Location is the available for sales storage location EWM Int AFS (103S). |  |
| 10 | Navigate to the Process Flow tab. | Navigate to the Process Flow tab. | The process flow documents are flagged with OK. |  |

#### Batch Information Cockpit - Display Batch (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With the Batch Information Cockpit (BMBC) app, you can display batches. It provides quick and easy access to batch-relevant information.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Fiori launchpad | Log on to the SAP Fiori launchpad as a Quality Technician. | The SAP Fiori launchpad opens. |  |
| 2 | Access the SAP Fiori app | Open Batch Information Cockpit (BMBC). | The Batch Information Cockpit screen appears. |  |
| 3 | Navigate to the Material tab | On the Batch Information Cockpit screen, navigate to the Material tab. |  |  |
| 4 | Enter material and plant | On the Material tab, make the following entries:Material: TG21Plant: 3310 |  |  |
| 5 | Execute Selection | On the Batch Information Cockpit screen, choose Execute Selection. | The Selection Result for Batches side panel appears. |  |
| 6 | Expand subtree | In the Selection Result for Batches side panel, choose Expand subtree. | The batch numbers for the current selection are displayed as tree nodes. |  |
| 7 | Choose one batch | Choose one batch in the Selection Result for Batches side panel. | The Details (Batch Master) sub screen appears. |  |
| 8 | Navigate to the Basic Data 1 tab. | Navigate to the Classification tab. |  |  |
| 9 | Note down batch data | Note down the Classification values.Batch NumberVendor Batch Number |  |  |

#### Check Physical Stock - Batch After Creation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After a batch was created in the SAP S/4HANA system, you want to check if the batch was transferred to the SAP EWM system.

Procedure

Access the activity using one of the following navigation options:

| Transaction Code | Easy Access Menu(SAP EWM) |
| --- | --- |
| /SCWM/MON | SCM Extended Warehouse Management > Extended Warehouse Management > Monitoring > Warehouse Management Monitor |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access Transaction | Access the transaction using one of the navigation options above. | The Warehouse Management Monitor dialog box appears. |  |
| 2 | Enter warehouse number and monitor | In the Warehouse Management Monitor dialog box, make the following entries:Warehouse Number: 3330Monitor: SAP |  |  |
| 3 | Choose Execute | In the Warehouse Management Monitor dialog box, choose Execute. | The Warehouse Management Monitor screen appears. |  |
| 4 | Expand folder Stock and Bin | On the Warehouse Management Monitor screen, expand folder Stock and Bin. |  |  |
| 5 | Double-click folder Physical Stock. | On the Warehouse Management Monitor screen, double-click folder Physical Stock. | The /SCM/SAPLSTOCK_OVERVIEW_MON dialog box appears. |  |
| 6 | Enter product and batch | In the /SCM/SAPLSTOCK_OVERVIEW_MON dialog box, make the following entries:Product (F2773): TG21Batch: your batch number |  |  |
| 7 | Choose Execute | In the /SCM/SAPLSTOCK_OVERVIEW_MON dialog box, choose Execute. | The Physical Stock sub screen appears. |  |
| 8 | Check batch number | In the Physical Stock sub screen, check that the batch number that you noted down in the SAP S/4HANA system appears in the table. |  |  |
| 9 | Choose the batch number in column Batch. | Choose the batch number in column Batch. | The Batch: Display screen appears. |  |
| 10 | Compare characteristic values | Compare characteristic values with the SAP S/4HANA system.Batch NumberVendor Batch Number | Characteristic values are equal in the SAP S/4HANA system and the SAP EWM system. |  |

#### Batch Information Cockpit - Change Batch (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With the Batch Information Cockpit (BMBC) app, you can directly call up the batch master for changing and displaying master data, classification data, and the batch where used list containing information about the lifecycle of a batch.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Fiori launchpad | Log on to the SAP Fiori launchpad as a Quality Technician. | The SAP Fiori launchpad opens. |  |
| 2 | Access the SAP Fiori app | Open Batch Information Cockpit (BMBC). | The Batch Information Cockpit screen appears |  |
| 3 | Navigate to the Material tab | On the Batch Information Cockpit screen, navigate to the Material tab. |  |  |
| 4 | Enter material and plant | On the Material tab, make the following entries:Material: TG21Plant: 3310 |  |  |
| 5 | Execute Selection | On the Batch Information Cockpit screen, choose Execute Selection. | The Selection Result for Batches side panel appears. |  |
| 6 | Expand subtree | In the Selection Result for Batches side panel, choose Expand subtree. | The batch numbers for the current selection are displayed as tree nodes. |  |
| 7 | Choose one batch | Choose one batch in the Selection Result for Batches side panel. | The Details (Batch Master) sub screen appears. |  |
| 8 | Note down a batch number | Note down a batch number for comparison in the SAP EWM system. |  |  |
| 9 | Navigate to the Basic Data 1 tab. | Navigate to the Basic Data 1 tab. |  |  |
| 10 | Choose Display - Change. | Choose Display - Change. | Fields get editable. |  |
| 11 | Change batch data | Change batch data.Supplier Batch: 4712-today's date |  |  |
| 12 | Navigate to the Classification tab. | Navigate to the Classification tab. | Values for the batch class are displayed:Batch Number: <specific batch value>Vendor Batch Number:<Number under which the batch is managed at the supplier's> |  |
| 13 | Save your entries | Save your entries. | The following system message appears: Changing batch <your batch number>. |  |

#### Check Physical Stock - After Batch Changes (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After a batch was changed in the SAP S/4HANA system, you want to check if the change was transferred to the SAP EWM system.

Procedure

| Transaction Code | Easy Access Menu(SAP EWM) |
| --- | --- |
| /SCWM/MON | SCM Extended Warehouse Management > Extended Warehouse Management > Monitoring > Warehouse Management Monitor |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access Transaction | Access the transaction using one of the navigation options above. | The Warehouse Management Monitor dialog box appears. |  |
| 2 | Enter warehouse number and monitor | In the Warehouse Management Monitor dialog box, make the following entries:Warehouse Number: 3330Monitor: SAP |  |  |
| 3 | Choose Execute | In the Warehouse Management Monitor dialog box, choose Execute. | The Warehouse Management Monitor screen appears. |  |
| 4 | Expand folder Stock and Bin | On the Warehouse Management Monitor screen, expand folder Stock and Bin. |  |  |
| 5 | Double-click folder Physical Stock. | On the Warehouse Management Monitor screen, double-click folder Physical Stock. | The /SCM/SAPLSTOCK_OVERVIEW_MON dialog box appears. |  |
| 6 | Enter product and batch | In the /SCM/SAPLSTOCK_OVERVIEW_MON dialog box, make the following entries:Product (F2773): TG21Batch: <your batch number> |  |  |
| 7 | Choose Execute | In the /SCM/SAPLSTOCK_OVERVIEW_MON dialog box, choose Execute. | The Physical Stock sub screen appears. |  |
| 8 | Check batch number | In the Physical Stock sub screen, check that the batch number that you noted down in the SAP S/4HANA system appears in the table. |  |  |
| 9 | Choose the batch number in column Batch. | Choose the batch number in column Batch. | The Batch: Display screen appears. |  |
| 10 | Compare characteristic values | Compare characteristic values with the SAP S/4HANA system.Batch NumberVendor Batch Number | Characteristic values are equal in the SAP S/4HANA system and the SAP EWM system. |  |

### Option 2: Create Batch in the SAP EWM System

In this option, you create the batch in the SAP EWM system when you maintain the inbound delivery.

#### Create Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can use the Create Purchase Order - Advanced (ME21N) app to create a new purchase order (PO) from scratch.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Create Purchase Order - Advanced (ME21N). | The Create Purchase Order screen appears. |  |
| 3 | Enter Order Type and Supplier | Make the following entries:Order Type (Purchasing): Standard POSupplier (F0354): 33300001 |  |  |
| 4 | Expand Header | Choose Expand Header | Header data is displayed in detail. |  |
| 5 | Navigate to Org Data Tab | Navigate to the Org. Data tab. |  |  |
| 6 | Enter Organizational Data | On the Org. Data tab, make the following entries:Purch. Org.: 3310Purch. Group: 002Company Code: 3310 |  |  |
| 7 | Expand Items | Choose Expand Items. | The item table appears. |  |
| 8 | Enter Item | In the Items table, make the following entries:Material: TG21PO Quantity: 1Plnt: 3310 |  |  |
| 9 | Enter Storage Location Batch | In the Items table, make the following entries:Stor. Location: 333DBatch: batch numberNote Enter the batch number you've created in step Create Batch. Leave the batch number empty if you want to create the batch later in the following step of option 2: Create and Assign Batch in SAP EWM. |  |  |
| 10 | Navigate to Confirmations Tab | On the Item Details sub screen, navigate to the Confirmations tab. |  |  |
| 11 | Enter Confirmation Control | On the Confirmations tab, make the following entries:Conf. Control: Inbound Delivery. |  |  |
| 12 | Save Your Entries | Save your entries. | The following system message appears: Standard PO created under the number <your PO number> |  |
| 13 | Note Down Your Purchase Order Number | Note down your purchase order number for testing purposes. |  |  |

#### Create Inbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inbound delivery informs the SAP EWM system about relevant changes and updated data.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori launchpad | Log on to the SAP Fiori launchpad as a Receiving Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Create Inbound Delivery (VL31N) | The Create Inbound Delivery - Delivery screen appears. |  |
| 3 | Enter purchase order number | Make the following entries:Purchase Order: <your purchase order number> |  | I c |
| 4 | Choose Continue | Choose Continue. | The Inbound Delivery Create: Overview screen appears. |  |
| 5 | Save your entries | On the Inbound Delivery Create: Overview tab, save your entries. | The following system message appears: Inbound Delivery <number> was saved and distributed to the WMS |  |

#### Create and Assign Batch in SAP EWM - Optional

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If the batch is not yet available in SAP EWM as a batch master record, then you can create the batch via the inbound delivery.

Procedure

| Transaction Code | SAP EWM Menu |
| --- | --- |
| /SCWM/PRDI | SAP Menu > SCM Extended Warehouse Management > Extended Warehouse Management > Delivery Processing > Inbound Delivery > Maintain Inbound Delivery |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access Transaction | Access the transaction using one of the navigation options above. | The Maintain Inbound Delivery screen appears |  |
| 2 | Choose Default Values (F5) | On the Maintain Inbound Delivery screen, choose Default Values (F5). | The Maintain Inbound Delivery - Warehouse Number dialog box appears. |  |
| 3 | Check or make the following entries | In the Maintain Inbound Delivery - Warehouse Numeber dialog box, check or make the following entries:Warehouse No. 3330Goods Receipt Office: YWAREHOUSE-3310Ent. to Dispose:33413310 |  |  |
| 4 | Choose Continue (Enter) | Choose Continue (Enter). |  |  |
| 5 | Choose Find Purchase Order | On the Maintain Inbound Delivery screen, choose Purchase Order from the Finddropdown list. |  |  |
| 6 | Enter Purchase Order Number | Make the following entries:Find Purchase order <your purchase order number> |  |  |
| 7 | Choose Perform Search. | Choose Perform Search. |  |  |
| 8 | Navigate to the Items tab. | Navigate to the Items tab. |  |  |
| 9 | On the Items tab, choose Batches > Create Batch . | On the Items tab, choose Batches > Create Batch . | The Display Logs dialog box appears.The following system messages appear:Document successfully locked for editing.Field Item: External Batch is a required field for the action Create Batch. |  |
| 10 | Choose Continue (Enter) | In the Display Logs dialog box, choose Continue (Enter). | The Vendor Batch field is editable. |  |
| 11 | Enter Supplier"s Batch | On the Items tab, make the following entries:Vendor Batch: 4711-today's date |  |  |
| 12 | On the Items tab, choose Batches → Create Batch. | On the Items tab, choose Batches → Create Batch. | The system draws a number from the defined number range for batches. The system creates a master record for this batch number.The batch number is displayed in the field Batch. |  |
| 13 | Note down the Batch Number. | Note down the batch number. |  |  |
| 14 | Save your entries. | Save your entries. |  |  |

#### Maintain Batches for Product in SAP EWM (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can enter Characteristics Valuations the in SAP EWM for a batch master record, that was created via the inbound delivery.

Procedure

| Transaction Code | SAP EWM Menu |
| --- | --- |
| /SCWM/WM_BATCH_MAINT | SAP Menu > SCM Extended Warehouse Management > Extended Warehouse Management > Master Data > Product > Maintain Batches for Product |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access Transaction | Access the transaction using one of the navigation options above. | The Maintain Batches for Product screen appears |  |
| 2 | On the Maintain Batches for Product screen, make entries | On the Maintain Batches for Product screen, make the following entries:Product: TG21Batch: <batch number from previous step> |  |  |
| 3 | Choose Change. | On the Maintain Batches for Product screen, choose Change. | The Batch: Change screen appears |  |
| 4 | On the Batch: Change screen, make entries | On the Batch: Change screen, make the following entries:<Characteristic> : <Value>Note You can check or change your own characteristic values here if necessary. |  |  |
| 5 | Save your entries. | Save your entries. |  |  |

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
| 2 | Choose Default Values (F5). | On the Maintain Inbound Delivery screen, choose Default Values(F5). | The Maintain Inbound Delivery - Warehouse Number dialog box appears. |  |
| 3 | Check or make the following entries | In the Maintain Inbound Delivery - Warehouse Number dialog box, check or make the following entries:Warehouse No.: 1730Goods Receipt Office: YWAREHOUSE-1730Ent. to Dispose: 17411710 |  |  |
| 4 | Choose Continue (Enter). | Choose Continue. |  |  |
| 5 | Choose Find Purchase Order | On the Maintain Inbound Delivery screen, from the Find drop down list, choose Purchase Order. |  |  |
| 6 | Enter purchase order number | Make the following entries:Find: Purchase Order your purchase order number |  |  |
| 7 | Choose Perform Search. | Choose Perform Search. | The following system message appears: One document was read.The Inbound Delivery appears in the table. |  |
| 8 | Select the Inbound Delivery. | Click on the row containing the inbound delivery document. | The inbound delivery line appears selected. (indicated by the highlighting).Once selected, the corresponding Items section below (showing Item Number 10 with Standard Delivery Item) will display the line items associated with that inbound delivery document. |  |
| 9 | Choose Menu > Inbound Delivery > Follow-On Functions > Pack (Ctrl+F3). | Choose Menu > Inbound Delivery > Follow-On Functions > Pack (Ctrl+F3). | The Work Center Packing for Inbound Delivery screen appears. |  |
| 10 | On the Work Center Packing for Inbound Delivery screen, navigate to the Create HU tab. | On the Work Center Packing for Inbound Delivery screen, navigate to the Create HU tab. |  |  |
| 11 | Enter packaging material | On the Create HU tab, make the following entries:Pack. Material: PMPAL00 |  |  |
| 12 | On the Create HU tab, choose Execute. | On the Create HU tab, choose Execute. | The following system message appears: HU number (PMPAL00) was constructed |  |
| 13 | Drag and drop inbound delivery item node to HU node. | On the Work Center Packing for Inbound Delivery screen, in the tree area drag the node with your product from the inbound delivery item. Drop it to the node with the HU number you created in the previous step. | The inbound delivery item is packed on the HU. |  |
| 14 | Choose Save and go back. | Choose Save and go back. | On the Status tab, the Status Type Packing is set to Completed. |  |
| 15 | On the Maintain Inbound Delivery screen, choose Check. | On the Maintain Inbound Delivery screen, choose Check. | The following system message appears: Activity was carried out successfully Blocked (Overall Status)It turns to Status Green. |  |
| 16 | Choose Goods Receipt. | Choose Goods Receipt. | The following system message appears: Inbound Delivery number changedIn the Document Flow tab in the document flow table, a new line with the document category Goods Receipt is added.On the Status tab, the Status Type Goods Receipt is set to Completed. |  |

#### Check Material Document After Goods Receipt (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Along with populating the warehouse with stock, there is also a financial posting in the SAP S/4HANA system.

The check step is to show you the material document along with its financial posting in the SAP S/4HANA system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad as a Inventory Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Choose Material Documents Overview (F1077). | The Material Documents Overview (F1077) screen appears. |  |
| 3 | Change Settings | On the Material Documents Overview (F1077) screen in section Material Documents, choose Settings on the right-hand side. | The View Settings dialog box appears. |  |
| 4 | View Settings | In the View Settings dialog box, select the column for Goods Movement Type. |  |  |
| 5 | Confirm | Choose OK. |  |  |
| 6 | Enter Selection Data | On top of the screen, make the following entries:Stock Change: STOCK INCREASEStock Change Level: PlantPlant: 3310Storage Location: 333DMaterial: TG21Posting Date: the date when you posted the goods receipt in the warehouse. |  |  |
| 7 | Check the Material Document | Choose Go. | The material documents are listed. |  |
| 8 | Note down Material Document Number | Note down the number of the Material Document Item with Goods Movement Type GR goods receipt (101). |  |  |
| 9 | Select Material Document | Choose the SAP S/4HANA Material Document. |  |  |
| 10 | Check Delivery Note Field | On the General Information tab, compare the Delivery Note with the reference Warehouse Material Document from the previous step. | The Delivery Note is equal to the reference Warehouse Material Document from the previous step. |  |
| 11 | Compare Item data | Compare the Item data of the Material Document Item with the item data of the Inbound Delivery Item of the SAP EWM system. | The Item data of the Material Document Item is equal to the item data of the Inbound Delivery Item of the SAP EWM system. |  |
| 12 | Navigate to the Process Flow tab | Navigate to the Process Flow tab. | The process flow documents are flagged with OK.The Accounting Document is displayed. |  |

#### Create Warehouse Tasks for Putaway in SAP EWM

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can create warehouse tasks manually using the transaction Putaway for Inbound Delivery.

Procedure

| Transaction Code | SAP EWM Menu |
| --- | --- |
| /SCWM/TODLV_I | SAP Menu > SCM Extended Warehouse Management > Extended Warehouse Management > Work Scheduling > Create Warehouse Task for Warehouse Request > Putaway for Inbound Delivery |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access Transaction | Access the transaction using one of the navigation options above. | The Create Warehouse Task - Warehouse Number number - Putaway screen appears. |  |
| 2 | Open Advanced Search | On the Create Warehouse Task - Warehouse Number number - Putaway screen, choose Open Advanced Search. | The Advanced Search sub screen appears. |  |
| 3 | Enter purchase order number | On the Advanced Search sub screen in the References section, make the following entries:Purchase Order: <your purchase order number> |  |  |
| 4 | Choose Advanced Search | Choose Advanced Search. | The warehouse request appears in the table. |  |
| 5 | Choose Close Advanced Search. | Choose Close Advanced Search. |  |  |
| 6 | Navigate to Warehouse Request tab. | Navigate to Warehouse Request tab. |  |  |
| 7 | Select All. | On the Warehouse Request tab in the table, choose Select All. |  |  |
| 8 | Choose Create + Save. | On the Warehouse Request tab, choose Create Warehouse Task. | The following system message appears: <number> warehouse tasks were created |  |
| 9 | Save your entries | Save your entries. | The following system message appears: Warehouse order <number> created |  |
| 10 | Note down the warehouse order | Note down the warehouse order for testing purposes. |  |  |

#### Putaway of Products in SAP EWM

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can confirm and save all warehouse tasks in one go, in the background. If you want to change data, you can also confirm individual warehouse tasks manually and then save them, in other words, confirm the individual warehouse tasks in the foreground. The following describes the manual confirmation in the foreground.

Procedure

| Transaction Code | SAP EWM Menu |
| --- | --- |
| /SCWM/TO_CONF | SAP Menu > SCM Extended Warehouse Management > Extended Warehouse Management > Execution > Confirm Warehouse Task |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access Transaction | Access the transaction using one of the navigation options above. | The Confirm Warehouse Task in Warehouse Number number screen appears. |  |
| 2 | Choose Find Warehouse Order | On the Confirm Warehouse Task in Warehouse Number <number> screen, from the Find dropdown list, choose Warehouse Order. |  |  |
| 3 | Enter warehouse order number | Make the following entries:Find: Warehouse Order your warehouse order number |  |  |
| 4 | Choose Perform Search. | Choose Perform Search. | The following system message appears: Selection produced number resultsThe warehouse order appears on the screen. |  |
| 5 | Select the Warehouse Order. | In the List View, select the Warehouse Order. |  |  |
| 6 | Choose Confirm in Foreground | Choose Confirm in Foreground. | The warehouse task(s) appear on the Product WT tab. |  |
| 7 | Navigate to the Product WT tab | Navigate to the Product WT tab. |  |  |
| 8 | Choose the warehouse task(s) | On the Product WT tab in the warehouse task table, select the warehouse task(s). |  |  |
| 9 | Choose Confirm in Foreground | Choose Confirm in Foreground. | The WT Status is updated to Confirmed in Foreground. |  |
| 10 | Save your entries | Save your entries. | The following system message appears: Warehouse task warehouse task number was confirmed |  |

#### Check Inbound Delivery (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you check the inbound deliveries in SAP S/4HANA, which were generated as a consequence of the goods receipt processing in SAP EWM.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad as a Receiving Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Display Inbound Delivery (VL33N). | The Display Inbound Delivery (VL33N) screen appears. |  |
| 3 | Enter Inbound Delivery | On the Display Inbound Delivery (VL33N) screen, make the following entries:Inbound Delivery: <inbound delivery number from step Create Inbound Delivery> |  |  |
| 4 | Choose Continue | On the Display Inbound Delivery (VL33N) screen, choose Continue. | The Inbound Delivery number Display: Overview screen appears. |  |
| 5 | Navigate to the Status Overview tab | Navigate to the Status Overview tab. |  |  |
| 6 | Check that the Overall Goods Movement Status is C Completely processed. | In the Overall Status - Delivery table, check that the Overall Goods Movement Status is C Completely processed. |  |  |
| 7 | Check that the Goods Movement Status for the items is C Completely processed. | In the Delivery Item Status (All Items) table, check that the Goods Movement Status for the items is C Completely processed. |  |  |
| 8 | Choose Document Flow. | On the Inbound Deliver<inbound delivery number> Display overview screen, choose Document Flow. | The Document Flow screen appears. |  |
| 9 | Note down the material document number for goods movement type TF SLoc to SLoc | On the Document Flow screen in the Document column, note down the material document number for the goods movement type TF SLoc to SLoc for testing purposes. |  |  |

#### Check Material Document After Putaway (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Along with populating the warehouse with stock, there is also a financial posting in the SAP S/4HANA system.

The check step is to show you the material document along with its financial posting in the SAP S/4HANA system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad as a Inventory Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Choose Material Documents Overview (F1077). | The Material Documents Overview (F1077) screen appears. |  |
| 3 | Change Settings | On the Material Documents Overview (F1077) screen in section Material Documents, choose Settings on the right-hand side. | The View Settings dialog box appears. |  |
| 4 | View Settings | In the View Settings dialog box, select the column for Goods Movement Type.Choose Storage Location (Transfer). |  |  |
| 5 | Confirm | Choose OK. |  |  |
| 6 | Enter Selection Data | On top of the screen, make the following entries:Stock Change: Transfer PostingStock Change Level: PlantExample:Plant: 3310Material Documents Overview (F1077): <your material document from the previous step> |  |  |
| 7 | Check the Material Document | Choose Go. | The material documents are listed. |  |
| 8 | Select Material Document | Choose the SAP S/4HANA Material Document. | The Material Documents Overview (F1077) screen appears. |  |
| 9 | Navigate to the Items tab | Navigate to the Items tab. | The Goods Movement Type is TF SLoc to SLoc (411).The Quantity is the amount you confirmed in the putaway before.The Receiving Storage Location is the available for sales storage location EWM Int AFS (103S). |  |
| 10 | Navigate to the Process Flow tab. | Navigate to the Process Flow tab. | The process flow documents are flagged with OK. |  |

#### Batch Information Cockpit - Display Batch (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With the Batch Information Cockpit (BMBC) app, you can display batches. It provides quick and easy access to batch-relevant information.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Fiori launchpad | Log on to the SAP Fiori launchpad as a Quality Technician. | The SAP Fiori launchpad opens. |  |
| 2 | Access the SAP Fiori app | Open Batch Information Cockpit (BMBC). | The Batch Information Cockpit screen appears. |  |
| 3 | Navigate to the Material tab | On the Batch Information Cockpit screen, navigate to the Material tab. |  |  |
| 4 | Enter material and plant | On the Material tab, make the following entries:Material: TG21Plant: 3310 |  |  |
| 5 | Execute Selection | On the Batch Information Cockpit screen, choose Execute Selection. | The Selection Result for Batches side panel appears. |  |
| 6 | Expand subtree | In the Selection Result for Batches side panel, choose Expand subtree. | The batch numbers for the current selection are displayed as tree nodes. |  |
| 7 | Choose one batch | Choose one batch in the Selection Result for Batches side panel. | The Details (Batch Master) sub screen appears. |  |
| 8 | Navigate to the Basic Data 1 tab. | Navigate to the Classification tab. |  |  |
| 9 | Note down batch data | Note down the Classification values.Batch NumberVendor Batch Number |  |  |

#### Check Physical Stock - Batch After Creation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After a batch was created in the SAP S/4HANA system, you want to check if the batch was transferred to the SAP EWM system.

Procedure

Access the activity using one of the following navigation options:

| Transaction Code | Easy Access Menu(SAP EWM) |
| --- | --- |
| /SCWM/MON | SCM Extended Warehouse Management > Extended Warehouse Management > Monitoring > Warehouse Management Monitor |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access Transaction | Access the transaction using one of the navigation options above. | The Warehouse Management Monitor dialog box appears. |  |
| 2 | Enter warehouse number and monitor | In the Warehouse Management Monitor dialog box, make the following entries:Warehouse Number: 3330Monitor: SAP |  |  |
| 3 | Choose Execute | In the Warehouse Management Monitor dialog box, choose Execute. | The Warehouse Management Monitor screen appears. |  |
| 4 | Expand folder Stock and Bin | On the Warehouse Management Monitor screen, expand folder Stock and Bin. |  |  |
| 5 | Double-click folder Physical Stock. | On the Warehouse Management Monitor screen, double-click folder Physical Stock. | The /SCM/SAPLSTOCK_OVERVIEW_MON dialog box appears. |  |
| 6 | Enter product and batch | In the /SCM/SAPLSTOCK_OVERVIEW_MON dialog box, make the following entries:Product (F2773): TG21Batch: your batch number |  |  |
| 7 | Choose Execute | In the /SCM/SAPLSTOCK_OVERVIEW_MON dialog box, choose Execute. | The Physical Stock sub screen appears. |  |
| 8 | Check batch number | In the Physical Stock sub screen, check that the batch number that you noted down in the SAP S/4HANA system appears in the table. |  |  |
| 9 | Choose the batch number in column Batch. | Choose the batch number in column Batch. | The Batch: Display screen appears. |  |
| 10 | Compare characteristic values | Compare characteristic values with the SAP S/4HANA system.Batch NumberVendor Batch Number | Characteristic values are equal in the SAP S/4HANA system and the SAP EWM system. |  |

#### Batch Information Cockpit - Change Batch (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With the Batch Information Cockpit (BMBC) app, you can directly call up the batch master for changing and displaying master data, classification data, and the batch where used list containing information about the lifecycle of a batch.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Fiori launchpad | Log on to the SAP Fiori launchpad as a Quality Technician. | The SAP Fiori launchpad opens. |  |
| 2 | Access the SAP Fiori app | Open Batch Information Cockpit (BMBC). | The Batch Information Cockpit screen appears |  |
| 3 | Navigate to the Material tab | On the Batch Information Cockpit screen, navigate to the Material tab. |  |  |
| 4 | Enter material and plant | On the Material tab, make the following entries:Material: TG21Plant: 3310 |  |  |
| 5 | Execute Selection | On the Batch Information Cockpit screen, choose Execute Selection. | The Selection Result for Batches side panel appears. |  |
| 6 | Expand subtree | In the Selection Result for Batches side panel, choose Expand subtree. | The batch numbers for the current selection are displayed as tree nodes. |  |
| 7 | Choose one batch | Choose one batch in the Selection Result for Batches side panel. | The Details (Batch Master) sub screen appears. |  |
| 8 | Note down a batch number | Note down a batch number for comparison in the SAP EWM system. |  |  |
| 9 | Navigate to the Basic Data 1 tab. | Navigate to the Basic Data 1 tab. |  |  |
| 10 | Choose Display - Change. | Choose Display - Change. | Fields get editable. |  |
| 11 | Change batch data | Change batch data.Supplier Batch: 4712-today's date |  |  |
| 12 | Navigate to the Classification tab. | Navigate to the Classification tab. | Values for the batch class are displayed:Batch Number: <specific batch value>Vendor Batch Number:<Number under which the batch is managed at the supplier's> |  |
| 13 | Save your entries | Save your entries. | The following system message appears: Changing batch <your batch number>. |  |

#### Check Physical Stock - After Batch Changes (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After a batch was changed in the SAP S/4HANA system, you want to check if the change was transferred to the SAP EWM system.

Procedure

| Transaction Code | Easy Access Menu(SAP EWM) |
| --- | --- |
| /SCWM/MON | SCM Extended Warehouse Management > Extended Warehouse Management > Monitoring > Warehouse Management Monitor |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access Transaction | Access the transaction using one of the navigation options above. | The Warehouse Management Monitor dialog box appears. |  |
| 2 | Enter warehouse number and monitor | In the Warehouse Management Monitor dialog box, make the following entries:Warehouse Number: 3330Monitor: SAP |  |  |
| 3 | Choose Execute | In the Warehouse Management Monitor dialog box, choose Execute. | The Warehouse Management Monitor screen appears. |  |
| 4 | Expand folder Stock and Bin | On the Warehouse Management Monitor screen, expand folder Stock and Bin. |  |  |
| 5 | Double-click folder Physical Stock. | On the Warehouse Management Monitor screen, double-click folder Physical Stock. | The /SCM/SAPLSTOCK_OVERVIEW_MON dialog box appears. |  |
| 6 | Enter product and batch | In the /SCM/SAPLSTOCK_OVERVIEW_MON dialog box, make the following entries:Product (F2773): TG21Batch: <your batch number> |  |  |
| 7 | Choose Execute | In the /SCM/SAPLSTOCK_OVERVIEW_MON dialog box, choose Execute. | The Physical Stock sub screen appears. |  |
| 8 | Check batch number | In the Physical Stock sub screen, check that the batch number that you noted down in the SAP S/4HANA system appears in the table. |  |  |
| 9 | Choose the batch number in column Batch. | Choose the batch number in column Batch. | The Batch: Display screen appears. |  |
| 10 | Compare characteristic values | Compare characteristic values with the SAP S/4HANA system.Batch NumberVendor Batch Number | Characteristic values are equal in the SAP S/4HANA system and the SAP EWM system. |  |

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

## Appendix

### Preceding Processes

You may first have completed the following processes and conditions before you start with the test steps:

| Process | Business Condition |
| --- | --- |
|  |  |

### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| SAP EWM Integration – Warehouse Stock Handling (2YL) | After you completed the business process of integration batch management, you can continue with internal warehouse processes. |
| SAP EWM Integration – Outbound Processing to Customer(2VK) | After you completed the business process of integration batch management, you can continue with the outbound to customer process with the batch-managed material. |
| Direct Procurement with Inbound Delivery(2TX) | After you have completed the business process steps of 2VN: SAP EWM Integration – Batch Management you can continue with the step Create Supplier Invoice of scope item Direct Procurement with Inbound Delivery(2TX). |

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
> Flagged while digesting this document, not verified: Post Goods Receipt in SAP EWM (both options) uses Warehouse No. 1730, Goods Receipt Office YWAREHOUSE-1730 and Ent. to Dispose 17411710, whereas the sample data and the Option 2 batch-creation step use EWM warehouse 3330 (YWAREHOUSE-3310, 33413310) and the stock checks use 3330.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Sample data gives Purchasing Group 001, but the Create Purchase Order steps enter Purch. Group 002.

> [!warning] Conflict
> Flagged while digesting this document, not verified: The Overview Table names the delivery app 'Inbound Deliveries for Purchase Orders (VL34)' while the procedure uses Create Inbound Delivery (VL31N).

## Connections
- part-of :: [[_cluster]]
- related-to :: [[11-inventory-warehouse-and-transportation/sap-ewm-integration-inbound-processing-from-supplier-2vj-ae-test-scrip]]
- related-to :: [[11-inventory-warehouse-and-transportation/test-script-warehouse-inbound-processing-3br-ae-sap-s-4hana-cloud-publ]]
- related-to :: [[11-inventory-warehouse-and-transportation/test-script-warehouse-inbound-processing-with-synchronous-goods-receip]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2VN_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 80,592 chars in the whole document
