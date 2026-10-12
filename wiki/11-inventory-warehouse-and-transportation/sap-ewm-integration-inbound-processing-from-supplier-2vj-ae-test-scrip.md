---
id: 11-inventory-warehouse-and-transportation/sap-ewm-integration-inbound-processing-from-supplier-2vj-ae-test-scrip
title: SAP EWM Integration – Inbound Processing from Supplier (2VJ_AE) – Test Script (2VJ_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 2VJ_AE: PO, expected goods receipt or inbound delivery, goods receipt and putaway in SAP EWM."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/ewm-inbound-processing]
aliases: [2VJ_S4CLD2608_BPD_EN_AE]
keywords: [Warehouse Inbound Processing and SAP EWM Inbound Integration, ewm inbound processing, expected goods receipt, inbound delivery, purchase order creation, goods receipt posting, warehouse tasks, putaway, material documents, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2VJ_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-879
topic: 11-inventory-warehouse-and-transportation/ewm-inbound-processing
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# SAP EWM Integration – Inbound Processing from Supplier (2VJ_AE) – Test Script (2VJ_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2VJ_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Warehouse Inbound Processing and SAP EWM Inbound Integration** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| SAP EWM Integration – Inbound Processing from Supplier (2VJ_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | SAP EWM Integration – Inbound Processing from Supplier (2VJ_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232850826)

[2 Prerequisites 4](#_Toc232850827)

[2.1 Additional Manual Configuration 4](#_Toc232850828)

[2.2 System Access 4](#_Toc232850829)

[2.3 Roles 4](#_Toc232850830)

[2.4 Master Data, Organizational Data, and Other Data 5](#_Toc232850831)

[2.5 Business Conditions 6](#_Toc232850832)

[3 Overview Table 7](#_Toc232850833)

[3.1 Alternative 1: Process / Document Flow with Expected Goods Receipt 7](#_Toc232850834)

[3.2 Alternative 2: Process / Document Flow with Inbound Delivery 7](#_Toc232850835)

[3.3 Process Steps for Both Alternative 1 and Alternative 2 8](#_Toc232850836)

[4 Test Procedures 9](#_Toc232850837)

[4.1 Alternative 1: Process / Document Flow with Expected Goods Receipt 9](#_Toc232850838)

[4.1.1 Create Purchase Order 9](#_Toc232850839)

[4.1.2 Option 1: Generate Expected Goods Receipt Documents 11](#_Toc232850840)

[4.1.3 Option 2: Generate Expected Goods Receipt Documents in SAP EWM 13](#_Toc232850841)

[4.1.4 Create an Inbound Delivery with Reference to Expected Goods Receipt in SAP EWM 14](#_Toc232850842)

[4.1.5 Check Inbound Delivery (Optional) 16](#_Toc232850843)

[4.2 Alternative 2: Process / Document Flow with Inbound Delivery 17](#_Toc232850844)

[4.2.1 Create Purchase Order 17](#_Toc232850845)

[4.2.2 Create Inbound Delivery 19](#_Toc232850846)

[4.3 Post Goods Receipt in SAP EWM 20](#_Toc232850847)

[4.4 Create Warehouse Tasks for Putaway in SAP EWM 22](#_Toc232850848)

[4.5 Putaway of Products in SAP EWM 24](#_Toc232850849)

[4.6 Check Inbound Delivery (Optional) 25](#_Toc232850850)

[4.7 Check Material Document (Optional) 26](#_Toc232850851)

[5 Appendix 28](#_Toc232850852)

[5.1 Process Integration 28](#_Toc232850853)

[5.1.1 Succeeding Processes 28](#_Toc232850854)

[5.1.2 Preceding Processes 28](#_Toc232850855)

## Purpose

Overview

This scope item enables you to order goods from suppliers and to perform the putaway in your warehouse. The process begins with the creation of a purchase order and an inbound delivery in the SAP S/4HANA Cloud Public Edition system. If the delivery is relevant to processing in SAP Extended Warehouse Management (EWM), the inbound delivery document is replicated to the SAP EWM system, where it generates an inbound delivery notification that in turn leads to an inbound delivery.

Alternatively, the warehouse can be informed about incoming goods by using an expected goods receipt (EGR) document. You can transfer the expected goods receipt information to the SAP EWM system in one of two ways: pull data from SAP S/4HANA Cloud Public Edition from within SAP EWM, or push the data from SAP S/4HANA Cloud to SAP EWM. The EGR document contains data for a purchase order and enables you to create an inbound delivery in SAP EWM that is replicated to the SAP S/4HANA Cloud Public Edition.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/f7ae9000fb3596368b0b556f1fbd3bd7)

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
| Receiving Specialist | SAP_BR_RECEIVING_SPECIALIST | Receiving | SAP_BR_RECEIVING_SPECIALIST |  |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

|  |  |  |  |
| --- | --- | --- | --- |
| Data | Sample Value | Detail |  |
| Material | TG11 | Trading Good for Reg. Trading (MRP planning) |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 333D | Decentral EWM Rec. on Dock |  |
| Storage Location | 333S | Decentral EWM available for sales |  |
| Warehouse | 333 | Decentral EWM-managed warehouse in SAP S/4HANA |  |
| Purchasing Organization | 3310 | Purch. Org. 3310 |  |
| Purchasing Group | 002 | Group 002 |  |
| Company Code | 3310 | Company Code 3310 |  |
| EWM Warehouse | 3330 | Decentral EWM warehouse |  |

You can find more information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

| MDS | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS master data script. Posting Period is up to date. |

## Overview Table

This scope item consists of several process steps provided in the tables below.

### Alternative 1: Process / Document Flow with Expected Goods Receipt

| Process Step | Business Role | App/ Transaction | System | Expected Results |
| --- | --- | --- | --- | --- |
| [Create Purchase Order](#unique_10) [page ] 9 | Purchaser | Create Purchase Order - Advanced (ME21N) | SAP S/4HANA | The following system message appears: Standard PO created under the number your PO number. |
| [Option 1: Generate Expected Goods Receipt Documents](#unique_11) [page ] 11 | Receiving Specialist | Expected Goods Receipt (F3298) | SAP S/4HANA | Expected Goods Receipt maintenance pushes Goods Receipt Notification to EWM in a background job. |
| [Option 2: Generate Expected Goods Receipt Documents in SAP EWM](#unique_12) [page ] 13 |  | /SCWM/ERP_EGR_DELETE | SAP Extended Warehouse Management | Creation of an EGR document in the EWM system with which an inbound delivery document can be created. |
| [Create an Inbound Delivery with Reference to Expected Goods Receipt in SAP EWM](#unique_13) [page ] 14 |  | /SCWM/GRPE | SAP Extended Warehouse Management | Inbound Delivery with Reference to EGR is created and information is replicated to ERP. |
| [Check Inbound Delivery (Optional)](#unique_14) [page ] 16 | Receiving Specialist | Display Inbound Delivery (VL33N) | SAP S/4HANA | Check the status of the inbound delivery in SAP S/4HANA, which was generated as a consequence of the goods receipt processing in SAP EWM. |

### Alternative 2: Process / Document Flow with Inbound Delivery

| Process Step | Business Role | App/ Transaction | System | Expected Results |
| --- | --- | --- | --- | --- |
| [Create Purchase Order](#unique_16) [page ] 17 | Purchaser | Create Purchase Order - Advanced (ME21N) | SAP S/4HANA | The following system message appears: Standard PO created under the number your PO number. |
| [Create Inbound Delivery](#unique_17) [page ] 19 | Receiving Specialist | Create Inbound Delivery (VL31N) | SAP S/4HANA | The following system message appears: Inbound Delivery your inbound delivery number has been saved |

### Process Steps for Both Alternative 1 and Alternative 2

| Process Step | Business Role | App/ Transaction | System | Expected Results |
| --- | --- | --- | --- | --- |
| [Post Goods Receipt in SAP EWM](#unique_19) [page ] 20 |  | /SCWM/PRDI | SAP Extended Warehouse Management | The following system message appears: Inbound Delivery number changed |
| [Check Material Document (Optional)](#unique_20) [page ] 26 | Inventory Manager | Material Documents Overview (F1077) | SAP S/4HANA | The Delivery Note is equal to the reference Warehouse Material Document from the previous step. |
| [Create Warehouse Tasks for Putaway in SAP EWM](#unique_21) [page ] 22 |  | /SCWM/TODLV_I | SAP Extended Warehouse Management | The following system message appears: Warehouse order number created |
| [Putaway of Products in SAP EWM](#unique_22) [page ] 24 |  | /SCWM/TO_CONF | SAP Extended Warehouse Management | The following system message appears: Warehouse task warehouse task number was confirmed |
| [Check Inbound Delivery (Optional)](#unique_23) [page ] 25 | Receiving Specialist | Display Inbound Delivery (VL33N) | SAP S/4HANA | In the Overall Status - Delivery table, check Overall Goods Movement Status is C Completely processed.In the Delivery Item Status (All Items) table, check Goods Movement Status for the items is C Completely processed. |
| [Check Material Document (Optional)](#unique_20) [page ] 26 | Inventory Manager | Material Documents Overview (F1077) | SAP S/4HANA | In the Material Documents table, the Storage Location is EWM Int ROD 103D and the Goods Movement Type is TF SLoc to SLoc (411). |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Alternative 1: Process / Document Flow with Expected Goods Receipt

#### Create Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can use the app Create Purchase Order - Advanced (ME21N) to create a new purchase order (PO) from scratch.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad as a Purchaser. | The SAPMULTIDRAG SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Create Purchase Order - Advanced (ME21N). | The Create Purchase Order - Advanced (ME21N) screen appears. |  |
| 3 | Enter order type and supplier | On the Create Purchase Order screen, make the following entries:Order Type (Purchasing): Standard POSupplier33300001 |  |  |
| 4 | Expand header | Choose Expand Header | Header data is displayed in detail. |  |
| 5 | Navigate to the Org. Data tab | Navigate to the Org. Data tab |  |  |
| 6 | Enter organizational data | On the Org. Data tab, make the following entries:Purch. Org.: 3310Purch. Group: 002Company Code: 3310 |  |  |
| 7 | Expand Items | Choose Expand Items | The item table appears. |  |
| 8 | Enter Item | In the Items table make the following entries:Material: TG11PO Quantity: 1OUn: PALPlant:3310Goods Receipt: yesInvoice Receipt: <selected>Storage Location: 333D |  |  |
| 9 | Choose Enter. | Choose Enter. |  |  |
| 10 | Navigate to the Confirmations tab | On the Item Details sub screen, navigate to the Confirmations tab. |  |  |
| 11 | Enter confirmation control | On the Confirmations tab,Conf. Control: Inbound Delivery |  |  |
| 12 | Save your entries | Save your entries | The following system message appears: Standard PO created under the number <your PO number>. |  |
| 13 | Note down your purchase order number | Note down your purchase order number for testing purposes. |  |  |

#### Option 1: Generate Expected Goods Receipt Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process, the expected goods receipt functionality is used for PO based creation of inbound deliveries in EWM. The EGR is created in the SAP S/4HANA system.

|  |
| --- |
| Note In productive systems, this job is scheduled as a background job. For more information about background jobs, see the Solution Operation Guide for SAP EWM in the SAP Help Portal. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Open the SAP Fiori Launchpad as a Receiving Specialist. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Expected Goods Receipt (F3298). | The Expected Goods Receipt (F3298) screen appears. |  |
| 3 | Create new Entry | On the Application Jobs screen, choose Create. | The New Job screen appears. |  |
| 4 | Select Job Template | On the New Job screen on the General Information tab, make the following entries:Job Template: Expected Goods ReceiptJob Name: Expected Goods Receipt |  |  |
| 5 | Select Scheduling Options and define Recurrence Pattern | On the Scheduling Options tab, choose Step 2 and then choose Define Recurrence Pattern. |  |  |
| 6 | Select Scheduling Options | On the Scheduling Information dialog box, make the following entries:Start Immediately: XRecurrence Pattern: Single Run |  | For testing purposes, you can select the option Start Immediately |
| 7 | Choose Ok | Choose OK. |  |  |
| 8 | Select Parameters | Choose Step 3, on the Parameters tab in the Parameter section, make the following entries:Warehouse Number:333Create Expected Goods Receipt:XSelection Start Date: <current date - 1 year>Selection Start Time: 00:00:00Selection End Date: <current date + 1 year>Selection End Time: 23:59:59Activate PO/SA Selection: XPurchasing document: <your purchase order number> |  |  |
| 9 | Schedule Job | Choose Schedule. | The following system message appears: Job Expected Goods Receipt has been scheduled. |  |
| 10 | Update Jobs |  | The Jobs table is updated. |  |
| 11 | Select your entry | Select the entry that you have created. | You can use the Planned Start and Created By filters to find your entry in the list. |  |
| 12 | Navigate to the Results column | Navigate to the Results column. |  |  |
| 13 | Select the button Navigate to the job results | Select Navigate to the job details for your job. | The Job Details screen appears. |  |
| 14 | View the Results | On the Scheduling Options tab in the Run Details section, select the document next to the field Results. | The following system messages appear: 1 correct EGR documents for purchase order or scheduling agreement. Inbound delivery creation is successful. Expected GR document simulated. |  |

|  |
| --- |
| Note In a productive system environment, there is usually a background job continuously creating EGR in the connected EWM system. |

Result

The SAP S/4HANA system selects the Purchase Orders and initiates the creation of EGR document in the connected SAP EWM based on the purchase order data. In case of errors, check the messages displayed in the log.

#### Option 2: Generate Expected Goods Receipt Documents in SAP EWM

Purpose

This is another option to create an EGR document in SAP EWM instead of creating it in the SAP S/4HANA system.

The expected goods receipt functionality is used for PO-based creation of inbound deliveries in EWM. You can initiate the EGR creation in the SAP EWM system using the procedure described below.

Procedure

| Transaction Code | SAP EWM Menu |
| --- | --- |
| /SCWM/ERP_EGR_DELETE | SCM Extended Warehouse Management > Extended Warehouse Management > Delivery Processing > Inbound Delivery > Generate Or Delete Expected Goods Receipt |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access Transaction | Access the transaction using one of the navigation options above. | The Deletion/Creation of Expected Goods Receipt screen appears. |  |
| 2 | Make the following entries | On the Deletion/Creation of Expected Goods Receipt screen, make the following entries:Example:ERP Warehouse Number: 333Purchase Order: Purchase Order number from step Create Purchase OrderFree Interval: XPeriod: <current date - 1 year> 00:00:00To: <current date + 1 year>23:59:59Program Mode: Only Create |  |  |
| 3 | Choose Execute | On the Deletion/Creation of Expected Goods Receipt screen, choose Execute. | The following system message appears:Finish document creationFinish GRN/EGR document creation/deletion |  |

Result

You have created an EGR document in the EWM system with which you can create an inbound delivery document.

#### Create an Inbound Delivery with Reference to Expected Goods Receipt in SAP EWM

Purpose

Upon the arrival of the goods, the Goods Receipt clerk searches for Advanced Shipping Notification (ASN) data, which will transfer electronically (B2B or EDI communication) by the supplier. The main reference for this search is the supplier's delivery note number, which is printed on the physical delivery note.

If no ASN data exists in the EWM system, it is now created with reference to the EGR information. Business-wise this is maintaining an inbound delivery (→ ASN) with reference to the PO Item(s).

Upon the creation of the inbound delivery, the external delivery note IDN (ASN) can enter and later use it as reference criterion for Goods Receipt.

Prerequisites

EGR documents based on the SAP S/4HANA purchase orders exist in your EWM system.

Procedure

| Transaction Code | SAP EWM Menu |
| --- | --- |
| /SCWM/GRPE | SCM Extended Warehouse Management > Extended Warehouse Management > Delivery Processing > Inbound Delivery > GR Preparation - External Procurement |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access Transaction | Access the transaction using one of the navigation options above. | The GR Preparation: External Procurement screen appears. |  |
| 2 |  | On the GR Preparation: External Procurement screen, choose Default Values (F5). | The GR Preparation: External Procurementdialog box appears. |  |
| 3 | Check or make the following entries | In the Maintain Inbound Delivery - Warehouse Number dialog box, check or make the following entries:Warehouse Number: 3330Goods Receipt Office: YWAREHOUSE-3330Entitled to Dispose: 33413310Select Expected GR: XSel. Inbound Deliveries: XWithout TU: X |  |  |
| 4 | Choose Continue (Enter). | Choose Continue (Enter). |  |  |
| 5 | Search for Purchase Order document | On the GR Preparation: External Procurement screen, choose Purchase Order in the Find dropdown menu to search for a purchase order document. |  |  |
| 6 | Make the following entries | On the GR Preparation: External Procurement screen, make the following entries:Purchase Order: <Purchase Order number document ID from step 4.1.1 Create Purchase Order> |  |  |
| 7 | Choose Execute | On the GR Preparation: External Procurement screen, choose Execute Search. | The system displays the EGR document items on the left screen area. |  |
| 8 | Select items | Select all items for your PO.Then choose the Copying Flag from the toolbar. | The selected EGR items are flagged for copying. |  |
| 9 | Copy items | Choose the Copy Flagged Item from the toolbar. | A dialog box appears. |  |
| 10 | Enter ASN Number | In the dialog box, enter the inbound delivery header data as follows:ASN: <your ASN number> |  | For example, ASN-45-#### where #### are the last “significant” digits of the corresponding Purchase Order ID.Example: ASN-45-0031 |
| 11 | Choose Continue | Choose Continue (Enter) | The EGR items are copied to the inbound delivery. |  |
| 12 | Choose Save | Choose Save |  |  |
| 13 | Note down the ERP Document Number | Note down the ERP Document number on your ID sheet |  |  |
| 14 | Note down ASN Number | GR Preparation: External Procurement (WarehouseNote down the ASN (Delivery Note) Number on your ID sheet |  |  |
| 15 | Choose Exit | Choose Exit |  |  |

Result

You have created the inbound delivery in the SAP EWM system based on the EGR document and the system replicated it back to the SAP S/4HANA system.

#### Check Inbound Delivery (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can check the inbound deliveries in SAP S/4HANA, that generated as a consequence of the goods receipt processing in SAP EWM.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad as a Receiving Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Display Inbound Delivery (VL33N). | The Display Inbound Delivery (VL33N) screen appears. |  |
| 3 | Enter Inbound Delivery | On the Display Inbound Delivery (VL33N) screen, make the following entries:Inbound Delivery: ERP Document number from step 4.1.4 Create an Inbound Delivery with Reference to Expected Goods Receipt in SAP EWM |  |  |
| 4 | Choose Continue | On the Display Inbound Delivery (VL33N) screen, choose Continue. | The Inbound Delivery number Display: Overview screen appears. |  |
| 5 | Navigate to the Status Overview tab | Navigate to the Status Overview tab |  |  |
| 6 | Check that the Overall Goods Movement Status is A Not yet processed. | In the Overall Status - Delivery table, check that the Overall Goods Movement Status is A Not yet processed. |  |  |

Please continue with step 4.3 [Post Goods Receipt in SAP EWM](#unique_19) [page ] 20.

### Alternative 2: Process / Document Flow with Inbound Delivery

#### Create Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can use the app Create Purchase Order - Advanced (ME21N) to create a new purchase order (PO) from scratch.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad as a Purchaser. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Create Purchase Order - Advanced (ME21N). | The Create Purchase Order - Advanced (ME21N) screen appears. |  |
| 3 | Enter order type and supplier | On the Create Purchase Order - Advanced (ME21N) screen, make the following entries:Order Type (Purchasing): Standard POSupplier.: 33300001 |  |  |
| 4 | Expand header | Choose Expand Header. | Header data is displayed in detail. |  |
| 5 | Navigate to the Org. Data tab | Navigate to the Org. Data tab |  |  |
| 6 | Enter organizational data | On the Org. Data tab, make the following entries:Purchase Org.: 3310Purchase Group: 002Company Code: 3310 |  |  |
| 7 | Expand Items | Choose Expand Items. | The item table appears. |  |
| 8 | Enter Item | In the Items table, make the following entries:Material TG11PO Quantity: 1OUn: PALPlant:3310Storage Location: 333D |  |  |
| 9 | Choose Enter. | Choose Enter. |  |  |
| 10 | Navigate to the Confirmations tab | On the Item Details sub screen, navigate to the Confirmations tab. |  |  |
| 11 | Enter confirmation control | On the Confirmations tab, make the following entries:Conf. Control: Inbound Delivery |  |  |
| 12 | Save your entries | Save your entries. | The following system message appears: Standard PO created under the number <your PO number>. |  |
| 13 | Note down your purchase order number | Note down your purchase order number for testing purposes. |  |  |

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
| 1 | Log on | Open the SAP Fiori launchpad as a Receiving Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Create Inbound Delivery (VL31N). |  |  |
| 3 | Enter purchase order number | On the Create Inbound Delivery screen, make the following entries:Purchase Order: your purchase order number |  |  |
| 4 | Choose Continue | Choose Continue. | The Inbound Delivery Create: Overview screen appears. |  |
| 5 | Save your entries | On the Inbound Delivery Create: Overview tab, save your entries. | The following system message appears: Inbound Delivery number was saved and distributed to the WMS |  |

### Post Goods Receipt in SAP EWM

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inbound delivery is used as a working object in the inbound delivery process.

You can use this document in delivery processing when executing the following actions:

- Registering the delivery in the yard
- Placing the delivery into stock (putaway)
- Canceling the "delivery putaway"
- Adjusting the delivery quantity to the quantity posted in the goods receipt (in case of over delivery or under delivery)
- Adjusting the delivery quantity and the transferred quantity

In this case, the delivery quantity is adjusted to the quantity posted in the goods receipt. The quantity in the inbound delivery notification is also adjusted and a new inbound delivery is created.

- Posting a goods movement
- Canceling a goods movement
- Creating items
- Deleting items

You can save, validate, and delete an inbound delivery.

Procedure

| Transaction Code | SAP EWM Menu |
| --- | --- |
| /SCWM/PRDI | SAP Menu > SCM Extended Warehouse Management > Extended Warehouse Management > Delivery Processing > Inbound Delivery > Maintain Inbound Delivery |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access Transaction | Access the transaction using one of the navigation options above. | The Maintain Inbound Delivery screen appears. |  |
| 2 | Choose Default Values (F5). | On the Maintain Inbound Delivery screen, choose Default Values (F5). | The Maintain Inbound Delivery - Warehouse Number dialog box appears. |  |
| 3 | Check or make the following entries | In the Maintain Inbound Delivery - Warehouse Number dialog box, check or make the following entries:Warehouse No.: 3330Goods Receipt Office:YWAREHOUSE-3330Entitled to Dispose: 33413310 |  |  |
| 4 | Choose Continue (Enter) | Choose Continue(Enter). |  |  |
| 5 | Choose Find Purchase Order | On the Maintain Inbound Delivery screen, from the Find dropdown list chooses Purchase Order. |  |  |
| 6 | Enter purchase order number | Make the following entries:Find: Purchase Order <your purchase order number> |  |  |
| 7 | Choose Perform Search. | Choose Perform Search. | The following system message appears: One document was read.The Inbound Delivery appears in the table. |  |
| 8 | Select the Inbound Delivery. | In the List ViewInbound Delivery. |  |  |
| 9 | In the Inbound Delivery menu, choose Follow-On Functions → Pack select the . | In the Inbound Delivery menu, choose Follow-On Functions > Pack. | The Work Center Packing for Inbound Delivery screen appears. |  |
| 10 | select theOn the Work Center Packing for Inbound Delivery screen, navigate to the Create HU tab | On the Work Center Packing for Inbound Delivery screen, navigate to the Create HU tab. |  |  |
| 11 | Enter packaging material | On the Create HU tab, make the following entries:Package Material: PMPAL00 |  |  |
| 12 | On the Create HU tab, choose Execute. | On the Create HU tab, choose Execute. | The following system message appears: HU <number> (PMPAL00) was constructed |  |
| 13 | Drag and drop inbound delivery item node to HU node. | On the Work Center Packing for Inbound Delivery screen, in the tree area drag the node with your product from the inbound delivery item and drop it to the node with the HU number you created in the previous step. | The inbound delivery item is packed on the HU. |  |
| 14 | Choose Save and go back. | Choose Save and go back. |  |  |
| 15 | On the Maintain Inbound Delivery screen, choose Goods Receipt.. | On the Maintain Inbound Delivery screen, choose Goods Receipt. | The following system message appears: Inbound Delivery <number> changedIn the Document Flow tab, in the document flow table a new line with document category Goods Receipt is added.On the Status tab, the Status Type Goods Receipt is set to Completed. |  |

### Create Warehouse Tasks for Putaway in SAP EWM

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can create warehouse tasks manually using the user interface for Putaway for Inbound Delivery.

Procedure

| Transaction Code | SAP EWM Menu |
| --- | --- |
| /SCWM/TODLV_I | SAP Menu > SCM Extended Warehouse Management > Extended Warehouse Management > Work Scheduling > Create Warehouse Task for Warehouse Request > Putaway for Inbound Delivery |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access Transaction | Access the transaction using one of the navigation options above. | The Create Warehouse Task - Warehouse Number number - Putaway screen appears. |  |
| 2 | Open Advanced Search | On the Create Warehouse Task - Warehouse Number number - Putaway screen, choose Open Advanced Search. | The Advanced Search sub screen appears. |  |
| 3 | Enter purchase order number | On the Advanced Search sub screen in the References section, make the following entries:Purchase Order: your purchase order number |  |  |
| 4 | Choose Advanced Search | Choose Advanced Search. | The warehouse request appears in the table. |  |
| 5 | Choose Close Advanced Search. | Choose Close Advanced Search. |  |  |
| 6 | Navigate to Warehouse Request tab. | Navigate to Warehouse Request tab. |  |  |
| 7 | Select All. | On the Warehouse Request tab in the table, choose Select All. |  |  |
| 8 | Choose Create + Save. | On the Warehouse Request tab, choose Create + Save. | The following system message appears: Warehouse order number created. |  |
| 9 | Note down the warehouse order | Note down the warehouse order for testing purposes. |  |  |

### Putaway of Products in SAP EWM

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
| 2 | Choose Find Warehouse Order | On the Confirm Warehouse Task in Warehouse Number number screen, from the Find drop down list choose Warehouse Order. |  |  |
| 3 | Enter warehouse order number | Make the following entries:Find: Warehouse Order your warehouse order number |  |  |
| 4 | Choose Perform Search. | Choose Perform Search. | The following system message appears: Selection produced number results.The Warehouse Order appears in the View. |  |
| 5 | Select the Warehouse Order. | In the List View, select the Warehouse Order. |  |  |
| 6 | Choose Confirm in Foreground | Choose Confirm in Foreground. | The warehouse task(s) appear on the tab Product WT. |  |
| 7 | Navigate to the Product WT tab | Navigate to the Product WT tab. |  |  |
| 8 | Choose the warehouse task(s) | On the Product WT tab in the warehouse task table, select the warehouse task(s). |  |  |
| 9 | Choose Confirm in Foreground | Choose Confirm in Foreground. | WT Status is updated to Confirmed in Foreground |  |
| 10 | Save your entries | Save your entries. | The following system message appears: Warehouse task warehouse task number was confirmed |  |

### Check Inbound Delivery (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can check the inbound deliveries in SAP S/4HANA, which generated as a consequence of the Inbound Delivery creation in SAP EWM.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad as a Receiving Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Display Inbound Delivery (VL33N). | The Display Inbound Delivery (VL33N) screen appears. |  |
| 3 | Enter Inbound Delivery | On the Display Inbound Delivery (VL33N)screen, make the following entries:Inbound Delivery: <ERP Document number from step Create an Inbound Delivery with Reference to Expected Goods Receipt in SAP EWM> |  |  |
| 4 | Choose Continue | On the Display Inbound Delivery (VL33N) screen, choose Continue. | The Inbound Delivery number Display: Overview screen appears. |  |
| 5 | Navigate to the Status Overview tab | Navigate to the Status Overview tab. |  |  |
| 6 | Check that the Overall Goods Movement Status is C Completely processed. | In the Overall Status - Delivery table, check that the Overall Goods Movement Status is C - Completely processed. |  |  |
| 7 | Check that the Goods Movement Status for the items is C Completely processed. | In the Delivery Item Status (All Items) table, check that the Goods Movement Status for the items is C - Completely processed. |  |  |
| 8 | Choose Document Flow. | On the Inbound Delivery <number> Display: Overview screen, choose Document Flow. | The Document Flow screen appears. |  |
| 9 | Note down the material document number for goods movement type TF SLoc to SLoc. | On the Document Flow screen in the Document column, note down the material document number for the goods movement type TF SLoc to SLoc for testing purposes. |  |  |

### Check Material Document (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The check step is to show you the material document in the SAP S/4HANA system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad as a Inventory Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Choose Material Documents Overview (F1077). | The Material Documents Overview (F1077) screen appears. |  |
| 3 | Change Settings | In section Material Documents, choose Settings on the right-hand side. | The View Settings dialog box appears. |  |
| 4 | View Settings | In the View Settings dialog box, select the column for Goods Movement Type. |  |  |
| 5 | Confirm | Choose OK. |  |  |
| 6 | Enter Selection Data | On top of the screen, make the following entries:Stock Change: TRANSFER POSTINGStock Change Level: PlantExample:Plant: 3310<Material Document Number from the previous step Check Inbound Delivery> |  |  |
| 7 | Check the Material Document | Choose Go. | Material document is listed. |  |
| 8 | Check the Storage Location | Select Material Document number, check Receiving Storage Location is EWM Int AFS 333S. |  |  |
| 9 | Check the Goods Movement Type | In the Material Documents table, check Goods Movement Type is TF SLoc to SLoc (411). | The delivery note is equal to the reference warehouse material document from the previous step. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| Real-Time Reporting and Monitoring for Procurement (1JI) | The Procurement Overview Page gives the Purchaser the most important and relevant information at a glance - instead of navigating through many different transactions and reports.The Global Filter helps the Purchaser to focus the entire Procurement Overview Page to view all information according to specific suppliers, material groups, purchasing groups and more.Via contextual navigation the Purchaser can immediately act upon the displayed information by accessing the app or the object instance or know more detailed information in the corresponding KPI Drill-Downs. |
| Direct Procurement with Inbound Delivery(2TX) | After you have completed the business process steps of 2VJ Inbound Processing, you can continue with the step Create Supplier Invoice of scope item Direct Procurement with Inbound Delivery(2TX). |

#### Preceding Processes

First you need to complete the following processes and conditions before you start with the test steps:

| Process | Business Condition |
| --- | --- |
| Direct Procurement with Inbound Delivery (2TX) - Create Purchase Order Manually | Refer to the process step Create Purchase Order Manually in Scope Item Direct Procurement with Inbound Delivery (2TX) Test Script. Purchase Order was manually created. This process would then start with step Maintenance of Expected Goods Receipt.In the test script, go to Test Procedures > Create Purchase Order Manually . You can find the document here [2TX](https://me.sap.com/processnavigator/SolS/EARL_SolS-013/2308/SolP/2TX?region=DE). |

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
> Flagged while digesting this document, not verified: The Overview Table expects the material document Storage Location to be 'EWM Int ROD 103D', while the Check Material Document procedure expects Receiving Storage Location 'EWM Int AFS 333S' (and the sample data lists 333D and 333S, not 103D).

## Connections
- part-of :: [[_cluster]]
- related-to :: [[11-inventory-warehouse-and-transportation/test-script-sap-ewm-integration-batch-management-2vn-ae-sap-s-4hana-cl]]
- related-to :: [[11-inventory-warehouse-and-transportation/test-script-warehouse-inbound-processing-3br-ae-sap-s-4hana-cloud-publ]]
- related-to :: [[11-inventory-warehouse-and-transportation/test-script-warehouse-inbound-processing-with-synchronous-goods-receip]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2VJ_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 45,275 chars in the whole document
