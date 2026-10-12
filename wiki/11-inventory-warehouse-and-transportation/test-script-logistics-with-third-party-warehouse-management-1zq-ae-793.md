---
id: 11-inventory-warehouse-and-transportation/test-script-logistics-with-third-party-warehouse-management-1zq-ae-793
title: "Test Script: Logistics with Third-Party Warehouse Management (1ZQ_AE) (1ZQ_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 1ZQ_AE: stock transfers, procurement, sales and returns integrated with a third-party WMS."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/third-party-warehouse-management, topic/third-party-wms-production]
aliases: [1ZQ_S4CLD2608_BPD_EN_AE]
keywords: [Logistics with Third-Party Warehouse Management, third-party wms integration, warehouse web services, stock transfers, two-step stock transfer, partial goods receipt, procurement process, outbound delivery, customer returns, return to supplier]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1ZQ_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-793
topic: 11-inventory-warehouse-and-transportation/third-party-warehouse-management
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Logistics with Third-Party Warehouse Management (1ZQ_AE) (1ZQ_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1ZQ_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Logistics with Third-Party Warehouse Management** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Logistics with Third-Party Warehouse Management (1ZQ_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Logistics with Third-Party Warehouse Management (1ZQ_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 4](#_Toc232848664)

[2 Prerequisites 5](#_Toc232848665)

[2.1 System Access 5](#_Toc232848666)

[2.2 Roles 5](#_Toc232848667)

[2.3 Master Data, Organizational Data, and Other Data 6](#_Toc232848668)

[2.4 Additional Manual Configuration 8](#_Toc232848669)

[2.5 Business Conditions 8](#_Toc232848670)

[2.6 Preliminary Steps 9](#_Toc232848671)

[2.6.1 Create Info Record 10](#_Toc232848672)

[3 Overview Table 11](#_Toc232848673)

[4 Test Procedures 15](#_Toc232848674)

[4.1 Inventory Management Processes 15](#_Toc232848675)

[4.1.1 Create Initial Stock Posting 15](#_Toc232848676)

[4.1.1.1 Confirm Inbound Delivery in WMS 17](#_Toc232848677)

[4.1.1.2 Reverse Goods Receipt (Optional) 17](#_Toc232848678)

[4.1.1.3 Check Stock Information 18](#_Toc232848679)

[4.1.2 Create Stock Transfer from Non 3rd Party WMS Managed Storage Location to 3rd Party WMS Managed Storage Location 19](#_Toc232848680)

[4.1.3 Create Stock Transfer from 3rd Party WMS Managed Storage Location to 3rd Party WMS Managed Storage Location – Different Stock Type 20](#_Toc232848681)

[4.1.4 Create Scrap Posting 21](#_Toc232848682)

[4.1.5 Create Stock Transfer from 3rd Party WMS Managed Storage Location to 3rd Party WMS Managed Storage Location 23](#_Toc232848683)

[4.1.5.1 Confirm Outbound Delivery in WMS 24](#_Toc232848684)

[4.1.5.2 Reverse Goods Issue (Optional) 24](#_Toc232848685)

[4.1.5.3 Check Stock Information 24](#_Toc232848686)

[4.1.6 Two Step Stock Transfer from Non 3rd Party WMS Managed Storage Location to 3rd Party WMS Managed Storage Location 25](#_Toc232848687)

[4.1.6.1 Remove Stock from Non 3rd Party WMS Managed Storage Location 26](#_Toc232848688)

[4.1.6.2 Place Stock to 3rd Party WMS Managed Storage Location 27](#_Toc232848689)

[4.1.6.3 Confirm Inbound Delivery in WMS 28](#_Toc232848690)

[4.1.6.4 Check Stock Information 28](#_Toc232848691)

[4.1.7 Two Step Stock Transfer from 3rd Party WMS Managed Storage Location to 3rd Party WMS Managed Storage Location 29](#_Toc232848692)

[4.1.7.1 Confirm Outbound Delivery in WMS 30](#_Toc232848693)

[4.1.7.2 Check Inbound Delivery Number in SAP S/4HANA Cloud Public Edition 31](#_Toc232848694)

[4.1.7.3 Confirm Inbound Delivery in WMS 32](#_Toc232848695)

[4.1.7.4 Check Stock Information 32](#_Toc232848696)

[4.2 Procurement Process 33](#_Toc232848697)

[4.2.1 Create Purchase Order 33](#_Toc232848698)

[4.2.2 Create Inbound Delivery 35](#_Toc232848699)

[4.2.3 Goods Receipt in Third-Party WMS 36](#_Toc232848700)

[4.2.3.1 Partial Goods Receipt in Third-Party WMS (Optional) 36](#_Toc232848701)

[4.3 Sales Process 37](#_Toc232848702)

[4.3.1 Create Sales Order 38](#_Toc232848703)

[4.3.2 Create Outbound Delivery 39](#_Toc232848704)

[4.3.3 Update Outbound Delivery from WMS (Optional) 40](#_Toc232848705)

[4.3.4 Picking and Goods Issue in Third-Party WMS 41](#_Toc232848706)

[4.3.5 Receive Split Outbound Delivery (Optional) 41](#_Toc232848707)

[4.3.6 Receive Outbound Delivery Confirmation 42](#_Toc232848708)

[4.4 Customer Returns 43](#_Toc232848709)

[4.4.1 Create Returns Order 43](#_Toc232848710)

[4.4.2 Perform Picking 45](#_Toc232848711)

[4.4.3 Post Goods Receipt 46](#_Toc232848712)

[4.4.4 Perform Material Inspection 47](#_Toc232848713)

[4.4.5 Post Stock Transfer 48](#_Toc232848714)

[4.4.6 Goods Receipt in Third-Party WMS 49](#_Toc232848715)

[4.4.7 Check Stock Information 49](#_Toc232848716)

[4.5 Return to Supplier 50](#_Toc232848717)

[4.5.1 Create Return Purchase Order 50](#_Toc232848718)

[4.5.2 Create Return Delivery 52](#_Toc232848719)

[4.5.3 Check Web Services Message and Execute in WMS 53](#_Toc232848720)

[4.5.4 Check Confirmation in SAP S/4HANA Cloud Public Edition 53](#_Toc232848721)

[5 Appendix 54](#_Toc232848722)

[5.1 Process Integration 54](#_Toc232848723)

[5.2 SAP Application Interface Framework 54](#_Toc232848724)

## Purpose

Overview

The scope item covers sales, procurement, stock transfer, and return processes. The business part of the processes – including sales order creation, purchase order creation, and quantity-based inventory management – are performed in the SAP S/4HANA Cloud Public Edition system. The decentralized third-party warehouse management system runs all processes required for the physical and logical goods movements. The integration is covered by asynchronous SOAP APIs. The following interfaces are available:

- Warehouse Shipping Order – Send to Warehouse (B2B)
- Warehouse Shipping Advice – Receive from Warehouse (B2B)
- Warehouse Stock Transfer Shipment Advice – Send to Warehouse (B2B)
- Warehouse Stock Transfer Receipt Advice – Receive from Warehouse (B2B)
- Split Outbound Delivery – Receive from Warehouse (B2B)
- Split Outbound Delivery Confirmation – Send to Warehouse (B2B)
- Warehouse Intermediate Update – Receive from Warehouse (B2B)
- Warehouse Intermediate Update Confirmation – Send to Warehouse (B2B)
- Warehouse Shipping Advice Cancel Request – Receive from Warehouse (B2B)
- Warehouse Shipping Advice Cancel Confirm – Send to Warehouse (B2B)
- Warehouse Stock Transfer Receipt Advice Cancel Request – From Warehouse (B2B)
- Warehouse Stock Transfer Receipt Advice Cancel Confirm – To Warehouse (B2B)
- Stock Transfer Partial Receipt Advice – from Warehouse (B2B)
- Stock Transfer Partial Receipt Advice Confirmation – to Warehouse (B2B)
- Stock Transfer Partial Receipt Cancel Advice – from Warehouse (B2B)
- Stock Transfer Partial Receipt Cancel Confirmation – to Warehouse (B2B)
- Stock Transfer Final Receipt Advice – from Warehouse (B2B)
- Stock Transfer Final Receipt Advice Confirmation – to Warehouse (B2B)

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
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Receiving Specialist | SAP_BR_RECEIVING_SPECIALIST | Receiving | SAP_BR_RECEIVING_SPECIALIST |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Returns and Refund Clerk | SAP_BR_RETURNS_REFUND_CLERK | Customer Returns | SAP_BR_RETURNS_REFUND_CLERK |  |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |

### Master Data, Organizational Data, and Other Data

SAP Best Practices Standard Values based on a new global template will be used once available. In the table you still see the master data used for the current baseline.

Essential master and organizational data was created in your SAP S/4HANA Cloud Public Edition system in the implementation phase, such as the data that reflects the organizational structure of your company and the master data that suits its operational focus, for example, master data for materials, vendors, and customers.

This master data usually consists of standardized SAP Best Practices default values, and enables you to go through the process steps of this scope item.

|  |
| --- |
| Note Additional Master Data (Default Values)You can test the scope item with other SAP Best Practices default values that have the same characteristics. |

Check your SAP system to find out which other material master data exists.

|  |
| --- |
| Note Using Your Own Master DataYou can also use customized values for any material or organizational data for which you have created master data. For more information about creating master data, see the Master Data Procedures documentation. |

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Material for sales process | TG11 | Trading Good for Reg. Trading (MRP planning)No serial number, no batch. | See sections [Business Conditions](#unique_6) [page ] 8 and [Preliminary Steps](#unique_7) [page ] 9. |
| Material for sales process | TG22 with batch | Trad.Good 22,Reorder Point,Batch-ExpDNo serial number, batch | See sections [Business Conditions](#unique_6) [page ] 8 and [Preliminary Steps](#unique_7) [page ] 9. |
| Sold-to Party | 33100003 | Domestic UAE Customer 3 | Test Customer |
| Ship-to party | 33100003 | Domestic UAE Customer 3 |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331I | 3rd party WM | Specific storage location representing the storage location managed by Third-Party WMS |
| Storage Location | 331J | 3rd party WMS-Production | Specific storage location representing the storage location managed by Third-Party WMS - Production |
| Storage Location | 331K | 3rd party WMS-Return | Specific storage location representing the storage location managed by Third-Party WMS - Return |
| Shipping Point | 3310 | Shipping Point 3310 |  |
| Sales Organization | 3310 | Dom. Sales Org |  |
| Distribution Channel | 10 | Direct Sales |  |
| Division | 00 | Product Division 00 |  |
| Purchasing Organization | 3310 | Purch. Org. 3310 |  |
| Purchasing group | 001/002 | Group 001/Group 002 |  |
| Vendor | 33300001 | Domestic UAE Supplier 1 |  |
| Material for procurement process | TG0013 | Trad. Good 0013,PD,Regular Proc.Trading Good for Regular Procurement (PD planning) |  |
| Material for procurement process | RM122 Raw Material with batch | RAW122,PD,Batch-Fifo,ProcureImportTrading Good for Regular Procurement (PD planning) |  |
| Warehouse Number | 001 |  | Only needed in WM system |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BNR | Create Product Master of type "Raw Material" - MDS |
| BNS | Create Product Master of type "Semi-Finished Good" - MDS |
| BNT | Create Product Master of type "Finished Good" - MDS |
| BND | Create Customer Master - MDS |
| BNE | Create Supplier Master - MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/6d624f9c38bf3ba792a2d40a6512dd00)

### Business Conditions

The business process described in this Test Script is based on and extracted from other scope items. The other scope items shows, for example, a sales process in much more complexity and might consist of more steps and activities than this test script. They need to be activated because they are a prerequisite for this test script.

| Scope Item | Business Condition |
| --- | --- |
| J45 - Procurement of Direct Materials | To run through this scope item, the materials must be available in stock. If you use trading goods (HAWA) you can either:Run through the Procurement of Direct Materials (J45) process,Or create stock using FLP tile Post Goods Movement (for details see the [Preliminary Steps](#unique_7) [page ] 9 section). |
| BD9 - Sell from Stock | This scope item is prerequisite and covers a more detailed sales process with additional steps, for example, print order confirmation that might be added to the sales scenarios described here. |
| 1MI - Delivery Processing Without Order Reference | This scope item is prerequisite and covers some additional steps, e.g. add freight costs, create billing document. |
| BMC - Core Inventory Management | This scope item is prerequisite to this scope item. |
| BMK - Return to Supplier | This scope item is prerequisite to this scope item. |
| BKP - Customer Returns | This scope item is prerequisite to this scope item and provides detailed steps for customer return processes. |
| BLF - Batch Management | This scope item is prerequisite to this scope item (If batch managed materials are used). |
| BDD - Lean Customer Returns | This scope item is prerequisite to customer returns processes described in the 1ZQ scope item and provides detailed steps for lean customer returns processes. |

### Preliminary Steps

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

To run through the sales process, the materials must be available in stock.

Procedure

|  |
| --- |
| Note All steps described in the Setup Guide have been performed by your system administrator. |

Check the stock level. If the stock is not sufficient, go through chapter [Create Initial Stock Posting](#unique_9) [page ] 15.

To create batch for the batch material, run test script BLF:Batch Management.

#### Create Info Record

Purpose

In this procedure, you create info records for procure process.

Procedure

For detailed operations of creating purchasing info record, please refer to Master Data Script - BHD - Create Purchasing Info Record - MDS.

Result

The Purchasing info records are created.

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Table 2: Inventory Management Processes

| Process Step | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Create Initial Stock Posting](#unique_9) [page ] 15 | Warehouse Clerk | Post Goods Movement (MIGO) |  |
| [Confirm Inbound Delivery in WMS](#unique_12) [page ] 17 | External System | Execute Goods Receipt, send out confirmation to SAP S/4HANA Cloud Public Edition |  |
| [Reverse Goods Receipt (Optional)](#unique_13) [page ] 17 | External System | Reverse Goods Receipt |  |
| [Check Stock Information](#unique_14) [page ] 18 | Warehouse Clerk | Display Warehouse Stock - Deprecated (MB52) |  |
| [Create Stock Transfer from Non 3rd Party WMS Managed Storage Location to 3rd Party WMS Managed Storage Location](#unique_15) [page ] 19 | Warehouse Clerk | Post Goods Movement (MIGO) |  |
| [Create Stock Transfer from 3rd Party WMS Managed Storage Location to 3rd Party WMS Managed Storage Location – Different Stock Type](#unique_16) [page ] 20 | Warehouse Clerk | Transfer Stock - In-Plant (F1061) |  |
| [Create Scrap Posting](#unique_17) [page ] 21 | Inventory Manager | Post Goods Movement (MIGO) |  |
| [Create Stock Transfer from 3rd Party WMS Managed Storage Location to 3rd Party WMS Managed Storage Location](#unique_18) [page ] 23 | Inventory Manager | Post Goods Movement (MIGO) |  |
| [Update Outbound Delivery from WMS (Optional)](#unique_19) [page ] 40 | External System | Update Outbound Delivery from WMS |  |
| [Confirm Outbound Delivery in WMS](#unique_20) [page ] 24 | External System | Post Goods Issue, send out confirmation to SAP S/4HANA Cloud Public Edition |  |
| [Reverse Goods Issue (Optional)](#unique_21) [page ] 24 | External System | Reverse Goods Issue |  |
| [Check Stock Information](#unique_22) [page ] 24 | Warehouse Clerk | Display Warehouse Stock - Deprecated (MB52) |  |
| Two Step Stock Transfer from Non 3rd Party WMS Managed Storage Location to 3rd Party WMS Managed Storage Location |  |  |  |
| [Remove Stock from Non 3rd Party WMS Managed Storage Location](#unique_23) [page ] 26 | Warehouse Clerk | Transfer Stock - In-Plant (F1061) |  |
| [Place Stock to 3rd Party WMS Managed Storage Location](#unique_24) [page ] 27 | Warehouse Clerk | Transfer Stock - In-Plant (F1061) |  |
| [Confirm Inbound Delivery in WMS](#unique_25) [page ] 28 | External System | Execute Goods Receipt, send out confirmation to SAP S/4HANA Cloud Public Edition |  |
| [Check Stock Information](#unique_26) [page ] 28 | Inventory Manager | Display Warehouse Stock - Deprecated (MB52) |  |
| Two Step Stock Transfer from 3rd Party WMS Managed Storage Location to 3rd Party WMS Managed Storage Location |  |  |  |
| [Update Outbound Delivery from WMS (Optional)](#unique_19) [page ] 40 | External System | Update Outbound Delivery from WMS |  |
| [Two Step Stock Transfer from 3rd Party WMS Managed Storage Location to 3rd Party WMS Managed Storage Location](#unique_27) [page ] 29 | Warehouse Clerk | Transfer Stock - In-Plant (F1061) |  |
| [Confirm Outbound Delivery in WMS](#unique_28) [page ] 30 | External System | Post Goods Issue, Send out confirmation to SAP S/4HANA Cloud Public Edition |  |
| [Check Inbound Delivery Number in SAP S/4HANA Cloud Public Edition](#unique_29) [page ] 31 | Shipping Specialist | Display Outbound Delivery (VL03N) |  |
| [Confirm Inbound Delivery in WMS](#unique_30) [page ] 32 | External System | Execute Goods Receipt, send out confirmation to SAP S/4HANA Cloud Public Edition |  |
| [Check Stock Information](#unique_31) [page ] 32 | Warehouse Clerk | Display Warehouse Stock - Deprecated (MB52) |  |

Table 3: Procurement Process

| Process Step | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Create Purchase Order](#unique_32) [page ] 33 | Purchaser | Create Purchase Order - Advanced (ME21N) |  |
| [Create Inbound Delivery](#unique_33) [page ] 35 | Receiving Specialist | Inbound Deliveries for Purchase Orders (VL34) |  |
| [Goods Receipt in Third-Party WMS](#unique_34) [page ] 36 | External System | Post goods receipt, confirmation delivery sent out to SAP S/4HANA Cloud Public Edition |  |
| [Partial Goods Receipt in Third-Party WMS (Optional)](#unique_35) [page ] 36 | External System | Post partial goods receipt, confirmation delivery sent out to SAP S/4HANA Cloud Public Edition |  |

Table 4: Sales Process

| Process Step | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Create Sales Order](#unique_36) [page ] 38 | Internal Sales Representative | Create Sales Orders - VA01 (VA01) | The Create Sales Document screen displays. |
| [Create Outbound Delivery](#unique_37) [page ] 39 | Shipping Specialist | Create Outbound Delivery - With Order Reference (VL01N) |  |
| [Update Outbound Delivery from WMS (Optional)](#unique_19) [page ] 40 | External System | Update Outbound Delivery from WMS |  |
| [Picking and Goods Issue in Third-Party WMS](#unique_38) [page ] 41 | External System | Execute Picking, Split of delivery, Goods issue, Confirmation delivery sent out to SAP S/4HANA Cloud Public Edition |  |
| [Receive Split Outbound Delivery (Optional)](#unique_39) [page ] 41 | Shipping Specialist | Display Outbound Delivery (VL03N) |  |
| [Receive Outbound Delivery Confirmation](#unique_40) [page ] 42 | Shipping Specialist | Display Outbound Delivery (VL03N) |  |

Table 5: Customer Returns

| Process Step | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Create Returns Order](#unique_41) [page ] 43 | Returns and Refund Clerk | Manage Customer Returns (F1708) |  |
| [Perform Picking](#unique_42) [page ] 45 | Shipping Specialist | Manage Outbound Deliveries (F0867A) |  |
| [Post Goods Receipt](#unique_43) [page ] 46 | Shipping Specialist | Manage Outbound Deliveries (F0867A) |  |
| [Perform Material Inspection](#unique_44) [page ] 47 | Receiving Specialist | Enter Inspection Results - From Warehouse (MSR_INSPWH) |  |
| [Post Stock Transfer](#unique_45) [page ] 48 | Warehouse Clerk | Transfer Stock - In-Plant (F1061) |  |
| [Goods Receipt in Third-Party WMS](#unique_46) [page ] 49 | External System | Goods receipt, storage, send out confirmation |  |
| [Check Stock Information](#unique_22) [page ] 24 | Warehouse Clerk | Display Warehouse Stock - Deprecated (MB52) |  |

Table 6: Return to Supplier

| Process Step | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Create Return Purchase Order](#unique_47) [page ] 50 | Purchaser | Create Purchase Order - Advanced (ME21N) |  |
| [Create Return Delivery](#unique_48) [page ] 52 | Shipping Specialist | My Purchase Orders - Due for Delivery (VL10B) |  |
| [Check Web Services Message and Execute in WMS](#unique_49) [page ] 53 | External System | Execute Picking, Post Goods Issue, send out confirmation to SAP S/4HANA Cloud Public Edition |  |
| [Check Confirmation in SAP S/4HANA Cloud Public Edition](#unique_50) [page ] 53 | Shipping Specialist | Display Outbound Delivery (VL03N) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Inventory Management Processes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this section several different inventory processes are described with the involvement of a storage location that is managed by a 3rd-Party Warehouse Management Systems (WMS).

The transfer of goods from one storage location to another storage location inside one plant, where at least one of the storage location is managed by third-party WMS, needs to be announced to the WMS. If the third-party WMS managed storage location is the sending location, an outbound delivery Web Services Message needs to be created. In case the third-party WMS managed storage location is the receiving location, an inbound delivery Web Services Message needs to be created. The material document creation and the inventory posting in the SAP S/4HANA Cloud Public Edition system happen when the confirmation from the third-party WMS about the physical movement comes back to SAP S/4HANA Cloud Public Edition.

The test procedure here only describes the SAP S/4HANA Cloud Public Edition part, but not the receiving steps on the WMS-side because this depends on the WMS in use.

|  |
| --- |
| Note The Scope Item 1ZQ - Logistics with Third-Party Warehouse Management only covers goods movement initiated by SAP S/4HANA Cloud Public Edition.Synchronizing goods movement initiated by the 3rd Party WMS to SAP S/4HANA Cloud Public Edition is out of the scope of this Scope Item.If you would like to have such 3rd Party WMS initiated goods movement in your business processes, to avoid stock inconsistencies between the two systems, you can refer to KBA 3122832 as a starting point to build your own solution. |

#### Create Initial Stock Posting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This section describes how to create a initial stock posting triggered from SAP S/4HANA Cloud Public Edition for a 3rd party WMS managed storage location.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Post Goods Movement (MIGO). | The Goods Receipt Other screen displays. | It only displays it that way if, it was your last transaction. So the action for the User should be to select field Reference Document for MIGO TransactionOther. |
| 3 | Input Movement Type | Make the following entry and press Enter.Executable Action in Transaction MIGO: Goods ReceiptReference Document for MIGO Transaction: Other |  |  |
| 4 | Input on the Goods Receipt Other screen: Material tab | On the Goods Receipt Other screen: Material tab, make the following entry and press Enter:Material : <Material number> |  |  |
| 5 | Input on the Goods Receipt Other screen: Quantity tab | On the Goods Receipt Other screen: Quantity tab, make the following entry and press Enter:Qty in Unit of Entry: Qty in UOMUnit of Entry: PC |  |  |
| 6 | Input on the Goods Receipt Other screen: Where tab | On the Goods Receipt Other screen: Where tab, make the following entries and press Enter:Movement Type: 561 – Receipt per initial entry of stock balances into unr.-usePlant: <Plant>Storage Location: <Storage Location> |  |  |
| 7 | (Optional) Input on the Goods Receipt Other screen: Batch tab | Batch: Batch number (for batch material only, for example TG22.Date of Manufacture: <a date>. |  |  |
| 8 | Save your entries | Choose Post. | Delivery XXXX created |  |

##### Confirm Inbound Delivery in WMS

Purpose

In this section the Inbound delivery Web Services message is received in the Third-party WMS. Some follow up processes need to be done there:

- Execute Goods Receipt
- Confirmation transfer sent out to SAP S/4HANA Cloud Public Edition

The steps are not described here in detail because it might be any 3rd Party WMS.

##### Reverse Goods Receipt (Optional)

If incorrect confirmation information has been sent from the Third-party WMS that needs to be reversed and reprocessed, the goods receipt of inbound delivery can be reversed by Third-party WMS via the following Web Services interface:

- Cancel Warehouse Stock Transfer Receipt Advice Request – Receive from Warehouse

Once the goods receipt is successfully reversed in SAP S/4HANA Cloud Public Edition System, a confirmation message which includes the delivery number will be sent to the 3rd Party WMS via the Web Service interface.

- Cancel Warehouse Stock Transfer Receipt Advice Confirmation

After the successful reversal, the goods receipt of the inbound delivery can be later posted again with correct information as described in previous step Goods Receipt.

|  |
| --- |
| Note Reversal of goods receipt from 3PL warehouse system is also supported for other types of inbound delivery processes, for example, Procurement Process, Customer Returns.Reversal of goods receipt is on the entire inbound delivery document. Reversal of goods receipt on a certain line item is not supported. |

##### Check Stock Information

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
| 3 | Enter material | Make the following entries:Material: <Material number>Plant: <Plant>Storage Location: <Storage Location>(Optional) Go to Settings section, and make the following entries:Display Batch Stocks: CheckChoose Run. | The Display Warehouse Stocks of Material is shown. |  |
| 4 | Check stock | Check if the stock information is now updated and the stock of the 3rd party WMS managed storage location displays. |  |  |

#### Create Stock Transfer from Non 3rd Party WMS Managed Storage Location to 3rd Party WMS Managed Storage Location

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this section a stock transfer between a non 3rd party WMS managed storage location as the sender and a 3rd party WMS managed storage location as a receiver. This stock transfer leads to the creation of an inbound delivery which will be transferred to WMS.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Transfer Stock - In-Plant (F1061). | The Transfer Stock-In-Plant screen displays. |  |
| 3 | Enter Material | Enter the following information:MaterialPlant | The stock situation in the different storage locations assigned to the plant is shown. |  |
| 4 | Move stock from a non 3rd party managed storage location to a 3rd party managed storage location | Click on <!-- image omitted: unnamed -->behind the unrestricted-use stock of a Non 3rd Party WMS Managed Storage Location (for example, 331A).Click on <!-- image omitted: unnamed -->behind a 3rd party WMS managed storage location (for example, 331I).When the pop-up opens, enter the quantity you want to transfer.Choose Post.Note down the stock numbers to be able to compare it when the confirmation is posted. | A new windows open: Transfer Stock – in PlantA message is shown: Material document /0000 createdThe numbers are not yet updated – this happens when the confirmation from WMS system comes back |  |
| 5 | Check Creation of Web Services Message | Inbound Delivery Web Services Message is created. |  |  |

Execute both step [Confirm Inbound Delivery in WMS](#unique_12) [page ] 17 and [Check Stock Information](#unique_22) [page ] 24 (or [Reverse Goods Receipt (Optional)](#unique_13) [page ] 17) to follow up in WMS and check the results.

#### Create Stock Transfer from 3rd Party WMS Managed Storage Location to 3rd Party WMS Managed Storage Location – Different Stock Type

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this section a stock transfer between two different stock types in a 3rd party WMS managed storage location as the sender and a receiver.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Transfer Stock - In-Plant (F1061). | The Transfer Stock-In-Plant screen displays. |  |
| 3 | Enter Material | Enter the following information:MaterialPlant | The stock situation in the different storage locations assigned to the plant is shown. |  |
| 4 | Move stock from one stock type to another stock type in a 3rd party managed storage location | Click on <!-- image omitted: unnamed -->behind the unrestricted-use stock of the 3rd party WMS managed storage location (for example, 331I).Click on <!-- image omitted: unnamed -->behind the stock-in-quality stock of the same storage location (for example, 331I).When the pop-up opens, enter the quantity you want to transfer.Choose Post.Note down the stock numbers to be able to compare it when the confirmation is posted | A new windows open: Transfer Stock – in PlantA message is shown: Material document /0000 createdThe numbers are not yet updated – this happens when the confirmation from WMS system comes back | It should work from any stock type (unrestricted-use, blocked, stock in quality inspection, returns) to any other |
| 5 | Check Creation of Web Services Message | Outbound Delivery Web Services Message is created. |  |  |

Execute both step [Confirm Outbound Delivery in WMS](#unique_20) [page ] 24 and [Check Stock Information](#unique_22) [page ] 24 (or [Reverse Goods Receipt (Optional)](#unique_13) [page ] 17) to follow up in WMS and check the results.

#### Create Scrap Posting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This section describes how to create a initial stock posting triggered from SAP S/4HANA Cloud Public Edition for a 3rd party WMS managed storage location.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Post Goods Movement (MIGO). | The Goods Movement screen displays. |  |
| 3 | Screen Settings | In the upper area, enter the following data and press Enter:First box: Goods IssueSecond box: otherMovement Type: 551 | Entries are made. |  |
| 4 | Enter Material Data | Enter the following data and press Enter:Material: TG11 | Entries are made. |  |
| 5 | Enter Quantity | Enter the following data in TAB Quantity and press Enter:Quantity:<Qty in Unit of Entry> |  |  |
| 6 | Enter Organization Data | Enter the following data in the Where tab and press Enter:Plant: 3310Storage Location: 331IReason for Movement: 0001Checkbox Item OK: <select> |  |  |
| 7 | (Optional) Enter Batch Info | Enter the following data in the Batch tab and press Enter:Batch: choose a batch (for batch material only). |  |  |
| 8 | Maintain Profitability Segment | Enter the following data in the Account Assignment tab and press Enter:Cost Center: <Cost Center> |  |  |
| 9 | Confirm Entries | Choose Continue. |  |  |
| 10 | Post Goods Issue | Choose Post. | The goods are removed from stock with quantity and value. The goods value is posted to the account and to COPA. |  |

Execute step [Confirm Outbound Delivery in WMS](#unique_20) [page ] 24 and [Check Stock Information](#unique_22) [page ] 24 to follow up in WMS and check the results

#### Create Stock Transfer from 3rd Party WMS Managed Storage Location to 3rd Party WMS Managed Storage Location

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this section a stock transfer between a 3rd party WMS managed storage location as the sender and a 3rd party WMS managed storage location as a receiver. This stock transfer leads to the creation of an outbound delivery which will be transferred to WMS.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Post Goods Movement (MIGO). |  | Alternative SAP GUI: should be transaction MIGO or MIGO_TR |
| 3 | Screen Settings | In the upper area, enter the following data and press Enter:First box: Transfer PostingSecond box: otherMovement Type: 311Material: TG0013Plant: 3310From Storage Location: 331ITo Storage Location: 331J or 331KQty in Unit:5 PC(Optional) Batch: choose a batch (for batch material only).Choose Post. | Message: Delivery xxx created. |  |
| 5 | Check creation of Web Services Message | Outbound Delivery Web Services Message should be created. |  |  |

##### Confirm Outbound Delivery in WMS

Purpose

In this section the outbound delivery Web Services message is received in the Third-party WMS. Some follow up processes need to be done there:

- Execute Goods Issue
- Confirmation transfer sent out to SAP S/4HANA Cloud Public Edition

The steps are not described here in detail because it might be any 3rd Party WMS.

##### Reverse Goods Issue (Optional)

If incorrect confirmation information has been sent from the Third-party WMS that needs to be reversed and reprocessed, the goods issue of outbound delivery can be reversed by Third-party WMS via the following Web Services interface:

- Warehouse Shipping Advice Cancel Request

Once the goods issue is successfully reversed in SAP S/4HANA Cloud Public Edition system, a confirmation message which includes the delivery number will be sent to the 3rd Party WMS via the Web Service interface.

- Warehouse Shipping Advice Cancel Confirm

After the successful reversal, the goods issue of the outbound delivery can be later posted again with correct information as described in previous step.

|  |
| --- |
| Note Reversal of goods issue from 3PL warehouse system is also supported for other types of outbound delivery processes, for example: Sales Process, Return to Supplier.Reversal of goods issue is on the entire outbound delivery document. Reversal of goods issue on a certain line item is not supported.Reversal of goods issue will not affect split deliveries. Once an outbound delivery has been split into new deliveries, each delivery will be processed independently. |

##### Check Stock Information

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

#### Two Step Stock Transfer from Non 3rd Party WMS Managed Storage Location to 3rd Party WMS Managed Storage Location

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this section a two-step stock transfer between an IM-managed or non third-party Warehouse Management Systems (WMS) managed storage location as a sender and a third-party WMS managed storage location as a receiver is described. The stock transfer needs to be done in two steps - first to post the stock into the Stock Transfer of the receiving storage location. The second step is to post the stock into the unrestricted-use stock of the receiving storage location.

##### Remove Stock from Non 3rd Party WMS Managed Storage Location

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori launchpad | Log on to the SAP Fiori launchpad with the Warehouse Clerk role. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Transfer Stock - In-Plant (F1061). | The Transfer Stock - In-Plant screen displays. |  |
| 3 | Open Stock Overview | Enter the following data in the appropriate fields and Enter:Plant: 3310Material: TG11(For Batch Material, also select the Batch number) | The stock situation in the different storage locations assigned to the plant is shown. |  |
| 4 | Select Transfer from Stock | Select the icon <!-- image omitted: unnamed -->beside the Unrestricted-Use Stock in storage location that you want to transfer from,for example, a non 3rd Party WMS Managed Storage Location 331A. | The icons beside different stock types change. |  |
| 5 | Select Transfer to Stock | Select the icon <!-- image omitted: unnamed -->right of the column Stock Transfer (Storage Location) in the final target storage location that you want to transfer to, for example, a 3rd Party WMS Managed Storage Location 331I. Stock type Stock Transfer (Storage Location) is for stock in transit. | A dialog box opens. Storage Locations and Stock Types are selected according to your entries in the previous steps. |  |
| 6 | Enter Quantity | Enter the quantity that you want to transfer:Quantity: x PC |  |  |
| 7 | Post | Choose Post. | The system displays a message: Material document xxx created.The stock is moved from Unrestricted-Use Stock in 331A to Stock Transfer (Storage Location) in 331I. |  |

##### Place Stock to 3rd Party WMS Managed Storage Location

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Select Transfer from Stock Type - Stock Transfer (Storage Location) | Note In real-world scenarios, this procedure – placing the stock to the target 3rd party WMS managed storage location, might be conducted a certain period of time after the completion of the first removal procedure by the other warehouse clerks (it may take time to transfer the stock from one storage location to another as they're located in different cities). Here for the demo purposes, we use the same user right after the completion of the first removal procedure.Open Transfer Stock - In-Plant (F1061), select the icon <!-- image omitted: unnamed -->right of the column Stock Transfer (Storage Location) in storage location where stock in transit are stored (by previous procedure), for example 331I. | The icons beside different stock types change. |  |
| 2 | Select Transfer to Stock Type - Unrestricted-Use Stock | Select the icon <!-- image omitted: unnamed -->beside the Unrestricted-Use Stock in storage location that you want to transfer to as the final storage location, for example 331I. | A dialog box opens. Storage Locations and Stock Types are selected according to your entries in the previous steps. |  |
| 3 | Enter Quantity | Enter the quantity that you want to transfer:Quantity: x PC |  |  |
| 4 | Post | Choose Post. | The system displays a message: Inbound delivery document xxx created.The stock is transferred from Stock Transfer (Storage Location) to Unrestricted-Use Stock, stock will be updated once the confirmation from WMS received and processed in SAP S/4HANA Cloud Public Edition. |  |
| 5 | Check Creation of Web Services Message | Check an Inbound Delivery Web Services Message is created for the stock transfer. |  |  |

##### Confirm Inbound Delivery in WMS

Purpose

In this section the Inbound delivery Web Services message is received in the Third-party WMS. Some follow up processes need to be done there:

- Execute Goods Receipt
- Confirmation transfer sent out to SAP S/4HANA Cloud Public Edition

The steps are not described here in detail because it might be any 3rd Party WMS.

##### Check Stock Information

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
| 4 | Check stock | Check if the stock information is now updated and the updated Unrestricted Unit of the 3rd party WMS managed storage location is displayed. |  |  |

#### Two Step Stock Transfer from 3rd Party WMS Managed Storage Location to 3rd Party WMS Managed Storage Location

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this section a two-step stock transfer between a third-party Warehouse Management Systems (WMS) managed storage location as a sender and a third-party WMS managed storage location as a receiver is described. In this case, only one manual step - remove stock from the source storage location, is needed in the SAP S/4HANA Cloud Public Edition. Because the SAP S/4HANA Cloud Public Edition system automatically created a new inbound delivery for the second step - place stock to the target storage location.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori launchpad | Log on to the SAP Fiori launchpad with the Warehouse Clerk role. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Transfer Stock - In-Plant (F1061). | The Transfer Stock screen displays. |  |
| 3 | Open Stock Overview | Enter the following data in the appropriate fields and Enter:Plant: 3310Material: TG11(For Batch Material, also select the Batch number) | The stock situation in the different storage locations assigned to the plant is shown. |  |
| 4 | Select Transfer from Stock | Select the icon <!-- image omitted: unnamed -->beside the Unrestricted-Use Stock in storage location that you want to transfer from,for example, a 3rd Party WMS Managed Storage Location 331I. | The icons beside different stock types change. |  |
| 5 | Select Transfer to Stock | Select the icon <!-- image omitted: unnamed -->right of the column Stock Transfer (Storage Location) in storage location that you want to transfer to. for example, a 3rd Party WMS Managed Storage Location for Return - 331K. Stock type Stock Transfer (Storage Location) is for stock in transit. | A dialog box opens. Storage Locations and Stock Types are selected according to your entries in the previous steps. |  |
| 6 | Enter Quantity | Enter the quantity that you want to transfer:Quantity: x PC |  |  |
| 7 | Post | Choose Post. | The system displays a message: Outbound Delivery document xxx created. |  |
| 8 | Check Creation of Web Services Message | Outbound Delivery and its Web Services Message are created. |  |  |

##### Confirm Outbound Delivery in WMS

Purpose

In this section the outbound delivery is replicated in the Third-party WMS. Some follow up processes need to be done in WMS:

- Execute Goods Issue against outbound delivery
- Confirmation message sent out to SAP S/4HANA Cloud Public Edition
- Once the confirmation message received and processed successfully in SAP S/4HANA Cloud Public Edition, the stock will be removed from Unrestricted-Use Stock in 331I to Stock Transfer (Storage Location) in 331K.
- An inbound delivery for placing the stock to the target storage location will then be automatically created and sent to your WMS.

The steps are not described here in detail because it might be any 3rd Party WMS.

##### Check Inbound Delivery Number in SAP S/4HANA Cloud Public Edition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this section you check the delivery number of the Inbound Delivery automatically created with the confirmation of Outbound Delivery in SAP S/4HANA Cloud Public Edition. As Inbound delivery Web Services Message is received in the 3rd Party WMS, once you have the Inbound Delivery number, you can continue to process the document in the 3rd Party WMS.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Display Outbound Delivery (VL03N). | The Display Outbound Delivery screen displays. |  |
| 3 | Open Outbound Delivery | Enter the Outbound Delivery number you noted down in previous steps and choose Continue. | The Outb.Deliv.Gds Mvmnt xxx Display: Overview screen displays. |  |
| 4 | Check Inbound Delivery Number | Choose Document Flow and note down the Inbound Delivery number. |  |  |

##### Confirm Inbound Delivery in WMS

The follow-up processes need to be done in the 3rd Party WMS:

- Execute Goods Receipt against the inbound delivery
- Confirmation message sent out to SAP S/4HANA Cloud Public Edition

The steps are not described here in detail because it might be any 3rd Party WMS.

Once the inbound delivery is confirmed and sent back to the SAP S/4HANA Cloud Public Edition, stock in transit will be placed to the Unrestricted-Use Stock of the target 3rd Party WMS managed storage location.

|  |
| --- |
| Note If you target storage location is non 3rd Party WMS Managed, for example, you have a two-step stock transfer between a third-party WMS managed storage location 331I as a sender and a non third-party WMS managed storage location 331A as a receiver, to place the stock in transit to the Unrestricted-Use Stock of the target storage location, it is recommended to post goods receipt directly with reference to the automatically created inbound delivery in the SAP S/4HANA Cloud Public Edition. For details, kindly refer to[2724138](https://me.sap.com/notes/2724138) |

##### Check Stock Information

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
| 4 | Check stock | Check if the stock information is now updated and the updated Unrestricted Unit of the 3rd party WMS managed storage location is displayed. |  |  |

### Procurement Process

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Purchaser creates a purchase order for a material (raw material, semi-finished, finished, trading goods) that is managed in warehouse by a Third-party WM system. Based on the PO, an Inbound Delivery is created. This step triggers the creation of Web Services Message that will be transferred to the warehouse system. When the goods are delivered, in the warehouse system a goods receipt is posted. The internal warehouse processes are not detailed out – it’s considered as a black box. Based on the incoming Inbound Delivery Confirmation Web Services Message, the goods receipt is automatically posted on SAP S/4HANA Cloud Public Edition side.

#### Create Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you create a purchase order for stock material directly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Purchase Order - Advanced (ME21N). | The Create Purchase Order Advanced screen displays with a list of existing Purchasing Document Items. |  |
| 3 | Start Purchase Order creation | Without making any selection, choose Create. | The Create Purchase Order screen displays. |  |
| 4 | Enter Purchase Order data | Enter all of the necessary data.General Data:Supplier: 33300001Org. Data:Purchasing Org.:3310Purchasing Group:001Company Code: 3310In the Items section:Material: TG0013Quantity: <Quantity>Net Price: xPlant: 3310Storage Location: 331I(Optional) Batch: batch number (for batch material only).In the Items section, choose Delivery Schedule:Delivery date: <date in the future>In the Items section, choose Confirmations:Conf. Control > Inbound Delivery | The Create Purchase Order screen displays. |  |
| 5 | Save Purchase Order | Choose Save to save the Purchase Order. | A new Purchase Order is created. The system displays the message: Purchase order xxx created. |  |

#### Create Inbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create the inbound deliveries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad using the Role Receiving Specialist. | The Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Inbound Deliveries for Purchase Orders (VL34). | The Generation of Inbound Deliveries screen displays. |  |
| 3 | Create Inbound Delivery | Make the following entries then choose Execute:Document Number: XXX (Enter the purchase order number created in previous step)Delivery Date: XXX Delete the default date and enter the delivery date in purchase orderTest Run: uncheckedThe Inbound Delivery Number is displayed, write it down for further use. | A new Inbound Delivery is created.The Inbound Delivery Number is displayed. |  |

#### Goods Receipt in Third-Party WMS

Purpose

WMS receives the inbound delivery web service message. When goods arrive at the warehouse, the goods receipt is booked in WMS and the following processes such as quality checks in goods receipt area and storing goods in storage bins are managed and performed only in WMS according to your WMS-specific settings. Afterwards, the inbound delivery confirmation web service message needs to be created and sent to the SAP S/4HANA Cloud Public Edition system.

##### Partial Goods Receipt in Third-Party WMS (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Partial Goods Receipt web service interfaces support immediate posting of partial goods receipts upon the physical arrival of goods, facilitating real-time inventory updates and seamlessly replicating the piece-by-piece partial receipt process from third-party Warehouse Management System (WMS) into SAP S/4HANA Cloud Public Edition.

Previously, only full inbound delivery quantities could be posted in SAP S/4HANA Cloud Public Edition at one time. This limitation caused delayed inventory synchronization and misalignment between third-party logistics (3PL) stock and SAP stock. With the Partial Goods Receipt SOAP APIs, the system doesn't synchronize stock until all goods in the inbound delivery are acknowledged into the warehouse. The APIs natively support multiple consecutive partial goods receipt postings for goods processed in different waves. Related succeeding processes include cancelling incorrectly posted partial receipts for error correction and providing final receipt of the inbound delivery after all physical receipts are finalized.

With the following Partial Goods Receipt web service interfaces, users can receive and confirm the goods in one inbound delivery through multiple messages.

- Stock Transfer Partial Receipt Advice – from Warehouse (B2B)
- Stock Transfer Partial Receipt Advice Confirmation – to Warehouse (B2B)
- Stock Transfer Partial Receipt Cancel Advice – from Warehouse (B2B)
- Stock Transfer Partial Receipt Cancel Confirmation – to Warehouse (B2B)
- Stock Transfer Final Receipt Advice – from Warehouse (B2B)
- Stock Transfer Final Receipt Advice Confirmation – to Warehouse (B2B)

The following example describes partial goods receipt processing:

| Step | Action | Inbound API from 3PL to SAP S/4HANA Cloud Public Edition | Outbound API from SAP S/4HANA Cloud Public Edition to 3PL |
| --- | --- | --- | --- |
| 1 | Create a purchase order (for a total of 100 PCs) in SAP S/4HANA Cloud Public Edition | N/A | N/A |
| 2 | Create an inbound delivery (100 PCs) against the purchase order in SAP S/4HANA Cloud Public Edition | N/A | Warehouse Stock Transfer Shipment Advice – Send to Warehouse (B2B)(This is the normal delivery replication API, which distributes the inbound delivery to the 3PL warehouse system.) |
| 3 | The 3PL warehouse needs to process inbound receipts in multiple wavesFirst partial receipt (40 PCs) | Stock Transfer Partial Receipt Advice(With a unique warehouse document number representing the first partial receipt) | Stock Transfer Partial Receipt Advice Confirmation(After the partial goods receipt is processed and posted successfully in SAP S/4HANA Cloud Public Edition) |
| 4 | Second partial receipt (50 PCs) | Stock Transfer Partial Receipt Advice(With another unique warehouse document number representing the second partial receipt) | Stock Transfer Partial Receipt Advice Confirmation(After the partial goods receipt is processed and posted successfully in SAP S/4HANA Cloud Public Edition) |
| 5 | Later, the second wave is processed incorrectly and needs to be canceled.Cancel the second receipt (50 PCs) | Stock Transfer Partial Receipt Cancel Advice(With the unique warehouse document number representing the second partial receipt) | Stock Transfer Partial Receipt Cancel Confirmation(After the cancellation is processed and posted successfully in SAP S/4HANA Cloud Public Edition) |
| 6 | Repost the corrected receipt (55 PCs) | Stock Transfer Partial Receipt Advice(With a new unique warehouse document number representing the repost partial receipt) | Stock Transfer Partial Receipt Advice Confirmation(After the partial goods receipt is processed and posted successfully in SAP S/4HANA Cloud Public Edition) |
| 7 | Finalize the delivery(To confirm the actual total of 95 PCs instead of the original delivery quantity) | Stock Transfer Final Receipt Advice(The message contains ActualDeliveryQuantity and ActualDeliveryQtyInBaseUnit) | Stock Transfer Final Receipt Advice Confirmation(The delivery quantity changes to 95 PCs in the inbound delivery, and the status of the inbound delivery is set to complete.) |

|  |
| --- |
| Note The warehouse document ID is the key to the partial receipt and cancellation of partial receipt processes (only numbers are allowed, with a maximum of 12 digits). |

### Sales Process

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process describes a sample sales process with Third-party WMS integration. The communication with the Third-party WMS takes place by Outbound delivery, Delivery split, and Delivery confirmation. The process starts with the creation of a delivery or a sales order of goods, that are stored and delivered out of a warehouse which is operated by a Third-party WMS. The WMS received an Outbound Delivery Web Services Message with the needed information to pick the ordered goods and to prepare the delivery. If a split of the delivery is needed, e.g. because not all items could be delivered in one single delivery, the WMS informs the SAP S/4HANA Cloud Public Edition system via a delivery split Web Services Message about the split (While using Web Services interface, once the split delivery is created successfully, a confirmation message which includes the number of newly split delivery will be sent to the 3rd Party WMS). After the goods issue in the warehouse, the confirmation of the delivery is also send to the SAP S/4HANA Cloud Public Edition system where follow-up processes could happen, e.g. proof of delivery.

#### Create Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This section describes how to create a sales order.

Prerequisite

Check the stock level of the material before you create the sales order. Make sure the stock is sufficient.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Sales Orders - VA01 (VA01). | The Create Sales Document screen displays. |  |
| 3 | Enter the Order type OR (Standard Order) | On the Create Sales Document screen, make the following entries and press Enter:Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 4 | Enter Order Details | On the Create Standard Order: Overview screen, make the following entries:Sold-to Party: <Customer Number>, for example, 33100003Ship-to Party: <Customer Number>, for example, 33100003Cust. Reference: <reference number>. Enter a customer purchase order number as reference.Material Number: <material number>Quantity: <great than 1>, for example, <10 PC>(Optional) Go to Item Detail tab, make the following entries:Batch: choose a batch (for batch material only). |  |  |
| 5 | Save Document | Choose Save Document.Make a note of the sales order number: __________.Note The created sales order might need to be approved first before you proceed with follow-up activities. For details, refer to chapter Process Sales Order Approval in the Sell from Stock (BD9) test script. | The order is saved and the order confirmation is printed out. |  |

#### Create Outbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This section describes how to create an outbound delivery based on a sales order. The outbound delivery is the vehicle to inform the WMS about the activities which need to happen in the warehouse.

Procedure

The SAP S/4HANA Cloud Public Edition system automatically creates a Web Services message based on the outbound delivery and sends it to the Third-party WMS. This outbound Web Services message can be checked in the SAP S/4HANA Cloud Public Edition system.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Outbound Delivery - With Order Reference (VL01N). |  |  |
| 3 | Enter Order information | Make the following entry and choose Continue:Shipping Point : 3310Order: <order number from the chapter before> |  |  |
| 4 | Save the Outbound delivery | Change Storage Location into 331IDelivery Quantity: <10>Batch (Optional): the batch number (for batch material only).Check the data.Choose Save.Make a note of the outbound delivery number:________.. | Outbound delivery is created. |  |

#### Update Outbound Delivery from WMS (Optional)

Multiple updates for an outbound delivery distributed to the third-party WMS can be triggered by the third-party WMS before final confirmation of goods issue via the following Web Services interface:

- Warehouse Intermediate Update => Warehouse Intermediate Update Inbound
- Warehouse Intermediate Update Confirmation => Warehouse Intermediate Update Confirmation Outbound

#### Picking and Goods Issue in Third-Party WMS

Purpose

The outbound delivery Web services message is received in the third-party WMS. Some follow-up processes need to be done there:

- Execute picking
- Update outbound delivery from WMS
- Split of the delivery
- Goods issue
- Confirmation delivery sent out to SAP S/4HANA Cloud Public Edition

The steps are not described here in details because it can be any third-party WMS.

#### Receive Split Outbound Delivery (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In case the sales order cannot get fulfilled in one delivery, a delivery split is performed by third-party WMS. This information is sent back to the SAP S/4HANA Cloud Public Edition system and could be checked there.

|  |
| --- |
| NoteTo split the original outbound delivery into two outbound deliveries in the SAP S/4HANA Cloud Public Edition System, delivery split information is sent to the SAP S/4HANA Cloud Public Edition System from the third-party WMS via either of the following interfaces:Split Outbound Delivery InboundDetermination of the delivery number of the newly split delivery:While using web service interface, delivery number of the newly split delivery is determined during the creation of the new delivery in the SAP S/4HANA Cloud Public Edition system after Split Outbound Delivery Inbound Web Services message is processed. Once the split delivery is created successfully, a confirmation message which includes the number of newly split delivery will be sent to the third-party WMS via the Web Service interface - Split Outbound Delivery Confirmation Outbound. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Outbound Delivery (VL03N). |  |  |
| 3 | Check Created Document | Enter the split outbound delivery number and press Enter. Check the delivery details. |  |  |

#### Receive Outbound Delivery Confirmation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When the delivery is completed in the third-party WMS, this information is send back to SAP S/4HANA Cloud Public Edition. This section describes how to check the related documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Outbound Delivery (VL03N). |  |  |
| 3 | Check Created Document | Enter the outbound delivery number and press Enter.Check the delivery details. |  |  |

### Customer Returns

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process describes a sample customer return process with third-party WMS integration. The process begins with the creation of a return order. Upon saving the return order, a returns delivery is automatically generated. Quality inspections are typically required upon receipt of the goods. For additional information regarding the customer return process, please refer to scope item BKP - Customer Returns.

Because decisions made during the customer return and quality inspection process have an impact on subsequent financial and logistical operations, it's recommended to perform inspections in a centrally managed storage location. Upon final decision made, the goods are ready to be stored in a third-party WMS-controlled storage location, and a stock transfer posting can be processed to transfer the goods to their final destination in the warehouse storage location.

If you manage your warehouse and logistics in-house using a third-party WMS system instead of outsourcing to a third-party logistics provider, you can set the storage location to a third-party WMS-managed location directly in your Return Order. Then the returns delivery is created and distributed to your third-party WMS. Perform the two chapters [Perform Picking](#unique_42) [page ] 45 and [Post Goods Receipt](#unique_43) [page ] 46 in your third-party WMS for the returns delivery and the corresponding confirmation message will be expected in SAP S/4HANA Cloud Public Edition to trigger the goods receipt posting in SAP S/4HANA Cloud Public Edition. Depending on different customer return decisions and logistical follow-up activities, the follow-up goods movements generate several delivery documents during this process. Your third-party WMS is required to respond to every follow-up delivery in the correct sequence. Please test according to your own customer return process if you do need to directly receive the returned goods into a third-party WMS-managed storage location and perform inspections there.

If you prefer BDD – Lean Customer Returns without quality inspection recorded in SAP S/4HANA Cloud Public Edition, you can set the storage location to a third-party WMS-managed location directly in your Lean Return Order. This applies whether you manage your warehouse and logistics in-house or outsource to a third-party logistics provider. A returns delivery is created with reference to the lean returns order and distributed to the third-party WMS. Upon the corresponding confirmation message received in SAP S/4HANA Cloud Public Edition, system performs the goods receipt posting to the valuated unrestricted-use stock. For detailed steps on how to create a lean return order, a returns delivery, and a credit memo, please refer to BDD – Lean Customer Returns.

#### Create Returns Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity you create a return order.

Procedure

You must have billing document or sales order document as reference (refer to Business Conditions).

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Returns and Refund Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Customer Returns (F1708). |  |  |
| 3 | Navigate to New Customer Return Screen | Choose Create Customer Return. | The New Customer Return screen is displayed. |  |
| 4 | Search for billing (sales) document to be referenced | Choose Show Filter Bars if it is hidden.Choose Adapt Filters if your desired filter is not shown.Enter the following selection criteria in the filter bar and choose Go:SD Document: <sales order number or billing document number, which are created previously> | Billing (sales) documents are displayed in the Reference Documents table. |  |
| 5 | Create Return | Choose Create for the sales order the return should be created. | The Create Return from Order x dialog box displays. |  |
| 6 | Maintain return | Make the following entries:Return Reason: for example, customer ordered too muchQuantity:<Quantity>Choose Create. | The Edit Customer Return sceen displays. |  |
| 7 | Edit Customer Return | Choose Save and Release.Go back to Manage Customer Returns. | The General Information screen displays. |  |
| 8 | Check Adv. Returns Delivery | Find and choose the Customer Return you just created.On the Display Customer Return screen, choose Process Flow: Check dependent documents in process flow. Make a note of the follow-up document numbers for further use.Display Return delivery. | The dependent documents display. |  |

#### Perform Picking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, picking is done for return delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Outbound Deliveries (F0867A). | The Outbound Delivery Monitor screen is displayed. |  |
| 3 | Choose Picking | Choose For Picking. |  |  |
| 4 | Enter Shipping point | Make the following entries and choose Execute:Shipping Point: for example, 331R. |  |  |
| 5 | Change outbound delivery | On the Day's Workload for Picking screen, select your delivery number and choose Change Outbound Deliveries. |  |  |
| 6 | Enter picked quantity | On the Picking tab, input quantity equal to delivery quantity in the Picked Qty field.(Optional) Batch:batch number (for batch material only). |  |  |
| 7 | Choose Enter | Choose Enter. |  |  |
| 8 | Save | Choose Save. | The delivery has been picked. |  |

#### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When the returned material is received, goods receipt is posted for return delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |
| 2 | Access the SAP Fiori App | Open Manage Outbound Deliveries (F0867A). | The Outbound Delivery Monitor screen displays. |
| 3 | Choose Good Issue | Choose For Goods Issue. |  |
| 4 | Enter Shipping point | Make the following entries and choose Execute:Shipping Point: for example, 331R. |  |
| 5 | Post Good Issue | Mark the relevant delivery and choose Post Goods Issue. Choose today’s date from the dialog box. | The goods issue is posted. |

#### Perform Material Inspection

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you save the inspection results.

Prerequisite

The returned goods are received. During goods receipt for returns an inspection lot is created automatically.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Receiving Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Enter Inspection Results - From Warehouse (MSR_INSPWH). | The Worklist Selection of Deliveries screen displays. |  |
| 3 | Maintain selection criteria | Enter the following entries and choose Execute:Delivery items waiting for inspection: <select>Delivery: <Enter return delivery number> | The Change: Material Inspection in Warehouse for Delivery screen displays. |  |
| 4 | Choose Item tab | Choose the Item tab. |  |  |
| 5 | Maintain Inspection Result | In the Inspection Result subarea, enter the following data and press Enter:Inspection Code: <Enter inspection code>Inspected quantity: <Enter inspected quantity>If the Confirmation of Redetermination dialog box appears, choose Yes to confirm. |  |  |
| 6 | Maintain Follow-Up Activity | In the Logistical Follow-Up subarea, enter the following data and press Enter:Follow-Up Activity: <Enter follow-up activity>Note Choose appropriate follow-up activity according to inspection code. For example, choose follow-up activity Transfer to Free Available Stock responding to inspection code 0001. |  |  |
| 7 | Check Inspection Status | On the Header tab, in the Basic Data subarea, Inspection status shows Inspected, which means all received material is inspected completely. | All received material is inspected completely. |  |
| 8 | Save and Confirm | Choose Save and Confirm | Inspection result is recorded. |  |
| 9 | Perform Necessary Goods Movements | Perform all the necessary goods movements according to the Follow-Up Activity you decided in earlier steps. | Expected goods movements are posted correctly. For example, the goods are posted into your own un-restricted stock. |  |

#### Post Stock Transfer

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you move the returned goods to a storage location which is managed by decentralized WMS.

Prerequisite

The inspection is finished and the returned good is available in unrestricted stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Transfer Stock - In-Plant (F1061). | The Transfer Stock-In-Plant screen displays. |  |
| 3 | Enter Material | Enter the following entries and press Enter:MaterialPlant | Stock information displays |  |
| 4 | Create stock movement | Click on the arrow (up) for Returns (331R) and unrestricted Stock.Click on the arrow (down) for 3rd Party WMS ( 331I ) and unrestricted Stock.Maintain the quantity and choose Post. | The Transfer stock in Plant window displays.Success message appears. |  |

#### Goods Receipt in Third-Party WMS

Context

WMS receives the inbound delivery Web Services message. When the goods arrive at the warehouse, the goods receipt is posted in WMS and the following process like storage of the goods in storage bins is done in WMS. In addition, the inbound delivery confirmation Web Services message needs to be created and sent to SAP S/4HANA Cloud Public Edition system.

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

### Return to Supplier

#### Create Return Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is to create a return purchase order for the supplier.

Prerequisite

Check the stock level of the material before you create the return purchase order. Make sure the stock is sufficient in the return storage location. To transfer material into the return storage location, go through [Create Stock Transfer from 3rd Party WMS Managed Storage Location to 3rd Party WMS Managed Storage Location](#unique_18) [page ] 23.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Purchase Order - Advanced (ME21N). | The Create Purchase Order screen displays. |  |
| 3 | Initial entry for return order | Make the following entries and press Enter:Order type: Standard POSupplier : 33300006Under the Header section, in the Org. Data tab, make following entries and press Enter:Purchasing Org: 3310Purchasing Group : 001Company Code: 3310On the Item Overview section, make following entries and press Enter:Material : for example,TG0013Quantity : X PCNet. Price :XAEDPlant: 3310Storage Location: 331KReturns Item: <Select the checkbox>(Optional) Batch: batch number(for batch material only).In the Items section, choose Delivery Schedule:Delivery Date: <date in the future> | All data is entered, the Item Detail screen displays. |  |
| 4 | Save Purchase Order | Choose Save and when the purchase order number is displayed, write it down for further use. | A new Purchase Order is created.Purchase Order Number displays. |  |

#### Create Return Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This section describes how to create an outbound delivery based on a return purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open My Purchase Orders - Due for Delivery (VL10B). | The Purchase Order, Fast Display screen displays. |  |
| 3 | Enter data for PO Display | In the head area:Purchase Order: <enter the purchase order number from the step before>Choose Execute. | The Activities Due for Shipping "Purchase Order, Fast Display" displays. |  |
| 4 | Create delivery | Select the line of Purchase Order from the list. Choose Background to create delivery in the background.Two lines are displayed now. Select the one with the green arrow and choose Log for Delivery Creation. | The Delivery Creation Log screen displays.The number of the delivery displays. |  |
| 5 | Check Delivery number | Choose Documents.Note down the return delivery number shown in the Document field. |  |  |

#### Check Web Services Message and Execute in WMS

Purpose

The outbound delivery Web Services message is received in the third-party WMS. Some follow-up processes need to be done there:

- Execute picking
- Update outbound delivery from WMS
- (Optional) Split of the delivery
- Goods issue
- Confirmation delivery sent out to SAP S/4HANA Cloud Public Edition

#### Check Confirmation in SAP S/4HANA Cloud Public Edition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This section describes how to check the status of the return delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays |  |
| 2 | Access the App | Open Display Outbound Delivery (VL03N). | The Display Outbound Delivery screen displays. |  |
| 3 | Enter Delivery Number | Enter Delivery number in the Outbound Delivery field and press Enter. | The Returns (Pur. Ord.) Display Overview screen displays. |  |
| 4 | Check Status | Choose Status Overview tab.Check Goods Movement status. | Goods Movement Status of the delivery should be C. |  |

## Appendix

### Process Integration

The process to be tested in this test script only focuses on the integration to Third-Party Warehouse Management Systems across several business processes.

| BD9 - Sell from Stock |
| --- |
| 1MI - Delivery Processing Without Order Reference |
| BMC - Core Inventory Management |
| J45 - Procurement of Direct Materials |
| BMK - Return to Supplier |
| BKP - Customer Returns |
| BLF - Batch Management |
| BDD - Lean Customer Returns |

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
- see-also :: [[15-retail-operations/test-script-retail-logistics-with-embedded-warehouse-management-69l-ae]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1ZQ_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 95,779 chars in the whole document
