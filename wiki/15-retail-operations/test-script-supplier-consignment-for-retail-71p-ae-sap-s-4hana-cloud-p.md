---
id: 15-retail-operations/test-script-supplier-consignment-for-retail-71p-ae-sap-s-4hana-cloud-p
title: "Test Script: Supplier Consignment for Retail (71P_AE) - SAP S/4HANA Cloud Public Edition (71P_S4CLD2608_BPD_EN_AE)"
description: "SAP test script for scope item 71P_AE (AE localization): supplier consignment retail processes, roles, sample data, Fiori apps and step-by-step test procedures."
cluster: 15-retail-operations
tags: [kb/retail-operations, topic/retail-supplier-consignment]
aliases: [71P_S4CLD2608_BPD_EN_AE]
keywords: [Supplier Consignment for Retail, supplier consignment, consignment settlement, article master data, purchase orders, stock transport orders, returns, return to supplier, store picking, in-store customer orders]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/71P_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1201
topic: 15-retail-operations/retail-supplier-consignment
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Supplier Consignment for Retail (71P_AE) - SAP S/4HANA Cloud Public Edition (71P_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/71P_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Supplier Consignment for Retail** in Retail Operations. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Supplier Consignment for Retail (71P_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 5](#_Toc232859772)

[2 Prerequisites 6](#_Toc232859773)

[2.1 System Access 6](#_Toc232859774)

[2.2 Roles 6](#_Toc232859775)

[2.3 Master Data, Organizational Data, and Other Data 7](#_Toc232859776)

[2.4 Preliminary Steps 9](#_Toc232859777)

[2.4.1 Customer Maintenance Settings 9](#_Toc232859778)

[2.4.1.1 Assign Template Customer to Schema 9](#_Toc232859779)

[2.4.1.2 Assign Schema to Store 10](#_Toc232859780)

[2.4.1.3 Assign Grouping Schema to Store 11](#_Toc232859781)

[2.4.2 Assign Retail Store Associate (User Persona) to a Store (Optional) 12](#_Toc232859782)

[2.4.3 Maintain Application Settings 12](#_Toc232859783)

[2.4.4 Extend Article to E-commerce Channel 13](#_Toc232859784)

[3 Overview Table 15](#_Toc232859785)

[4 Test Procedures 23](#_Toc232859786)

[4.1 Create Master Data for Article for Consignment Processing 23](#_Toc232859787)

[4.1.1 Create Article Master Data 23](#_Toc232859788)

[4.1.1.1 Create Single Article 23](#_Toc232859789)

[4.1.1.1.1 Maintain Consignment Purchasing Info Record 35](#_Toc232859790)

[4.1.1.1.2 Create Sales Conditions 36](#_Toc232859791)

[4.1.1.1.3 Maintain Assortments 38](#_Toc232859792)

[4.2 Procurement from External Supplier 41](#_Toc232859793)

[4.2.1 Create Purchase Order 41](#_Toc232859794)

[4.2.2 Create Inbound Delivery 42](#_Toc232859795)

[4.2.3 Confirm Quantities for Putaway 43](#_Toc232859796)

[4.2.4 Post Goods Receipt for Inbound Delivery 44](#_Toc232859797)

[4.2.5 Check Stock Status 45](#_Toc232859798)

[4.3 Store Ordering from Distribution Center 46](#_Toc232859799)

[4.3.1 Create Stock Transport Order 46](#_Toc232859800)

[4.3.2 Create Replenishment Delivery for Stock Transfer Order 47](#_Toc232859801)

[4.3.3 Post Goods Issue for Delivery 48](#_Toc232859802)

[4.3.4 Check Stock in Transit 49](#_Toc232859803)

[4.3.5 Post Goods Receipt for Outbound Delivery 50](#_Toc232859804)

[4.3.6 Check Stock Status(Optional) 51](#_Toc232859805)

[4.4 Transfer Data to Point-of-Sale (POS) 52](#_Toc232859806)

[4.5 Process Point of Sales(POS) Transactions 52](#_Toc232859807)

[4.5.1 Schedule Job to Set Stock Situation 52](#_Toc232859808)

[4.5.2 Process Point-of-Sale (POS) Transactions 54](#_Toc232859809)

[4.6 Invoice Receipt from Consignment Withdrawal 54](#_Toc232859810)

[4.6.1 Create Consignment settlement 54](#_Toc232859811)

[4.7 Return From Stores 56](#_Toc232859812)

[4.7.1 Create Returns Stock Transport Order 56](#_Toc232859813)

[4.7.2 Create Outbound Delivery 57](#_Toc232859814)

[4.7.3 Perform Picking and Post Goods Issue for Outbound Delivery 58](#_Toc232859815)

[4.7.4 Check Inbound Delivery 59](#_Toc232859816)

[4.7.5 Perform Post Goods Receipt 60](#_Toc232859817)

[4.7.6 Check Stock Status(Optional) 61](#_Toc232859818)

[4.8 Return to Supplier 62](#_Toc232859819)

[4.8.1 Create Returns Purchase Order 62](#_Toc232859820)

[4.8.2 Create Outbound Delivery 64](#_Toc232859821)

[4.8.3 Pick and Post Goods Issue 65](#_Toc232859822)

[4.9 In-Store Inventory Management 66](#_Toc232859823)

[4.9.1 Look Up General Product Information 66](#_Toc232859824)

[4.9.2 Review Order Proposals 67](#_Toc232859825)

[4.10 In-Store Customer Order Management 68](#_Toc232859826)

[4.10.1 Sell from Store: Immediate Pickup 68](#_Toc232859827)

[4.10.1.1 Verify Consumer Registration 68](#_Toc232859828)

[4.10.1.2 Create Master Data for Registering a New Consumer (Optional) 69](#_Toc232859829)

[4.10.1.3 Create Sales Order and Generate Invoice 70](#_Toc232859830)

[4.10.1.4 Process Customer Order Payment from POS 72](#_Toc232859831)

[4.10.2 Sell from Store: Pickup at Later Date due to Stock Unavailability (Payment Done at Pickup) 73](#_Toc232859832)

[4.10.2.1 In-Store Operations 73](#_Toc232859833)

[4.10.2.1.1 Check Stock Availability in Store 73](#_Toc232859834)

[4.10.2.1.2 Verify Consumer Registration 74](#_Toc232859835)

[4.10.2.1.3 Create Master Data for Registering New Consumers (Optional) 75](#_Toc232859836)

[4.10.2.1.4 Create Sales Order 76](#_Toc232859837)

[4.10.2.1.5 Print Sales Order Document (Optional) 78](#_Toc232859838)

[4.10.2.2 Back-Office Operations from Distribution Center to Store 79](#_Toc232859839)

[4.10.2.2.1 Transfer Stock 79](#_Toc232859840)

[4.10.2.2.2 Schedule Application Job to Create Stock Transport Order 81](#_Toc232859841)

[4.10.2.2.3 Create Stock Transport Order (Optional) 82](#_Toc232859842)

[4.10.2.2.4 Schedule Application Job to Create Replenishment Delivery for STO 83](#_Toc232859843)

[4.10.2.2.5 Pick, Pack, and Post Goods Issue for Replenishment Delivery from DC 84](#_Toc232859844)

[4.10.2.3 In-Store Operations 85](#_Toc232859845)

[4.10.2.3.1 Post Goods Receipt for STO/Outbound Delivery 85](#_Toc232859846)

[4.10.2.3.2 Start Picking 86](#_Toc232859847)

[4.10.2.3.3 Verify Consumer Order Details and Hand Over 89](#_Toc232859848)

[4.10.2.3.4 Validate Follow-On Documents and Print Billing Document 91](#_Toc232859849)

[4.11 Omnichannel Order Fulfillment for Retail 93](#_Toc232859850)

[4.11.1 Click and Reserve - Order Fulfillment in Store (Stock is Available in the Store) 93](#_Toc232859851)

[4.11.1.1 Create Sales Orders 93](#_Toc232859852)

[4.11.1.2 Start Picking 95](#_Toc232859853)

[4.11.1.3 Look Over the Order Details for Handover 98](#_Toc232859854)

[4.11.1.4 Validate Sales Order Document and Subsequent Document Flow (Optional) 100](#_Toc232859855)

[4.11.1.5 Process Customer Order Payment from POS 101](#_Toc232859856)

[4.11.2 Click and Collect (Pre-Paid Order)- Order Fulfillment from Distribution Center to Store (Stock is Not Available in the Store) 102](#_Toc232859857)

[4.11.2.1 Create Sales Order 102](#_Toc232859858)

[4.11.2.2 Back-Office Operations from Distribution Centre to Store 104](#_Toc232859859)

[4.11.2.2.1 Transfer Stock 104](#_Toc232859860)

[4.11.2.2.2 Schedule Application Job to Create Stock Transport Order 106](#_Toc232859861)

[4.11.2.2.3 Create Stock Transport Order (Optional) 107](#_Toc232859862)

[4.11.2.2.4 Schedule Application Job to Create Replenishment Delivery for STO 108](#_Toc232859863)

[4.11.2.2.5 Pick, Pack, and Post Goods Issue for Replenishment Delivery from DC 109](#_Toc232859864)

[4.11.2.3 In-Store Operations 110](#_Toc232859865)

[4.11.2.3.1 Post Goods Receipt for STO/Outbound Delivery 110](#_Toc232859866)

[4.11.2.3.2 Verify Consumer Order Details 111](#_Toc232859867)

[4.11.2.3.3 Validate Sales Order Document and Subsequent Document Flow (Optional) 114](#_Toc232859868)

[4.11.3 Sell from Online Store, Delivery from Distribution Centre to Customer(Pre-Paid Order) 115](#_Toc232859869)

[4.11.3.1 Create Sales Order 115](#_Toc232859870)

[4.11.3.2 Back Office Operations in Distribution Centre 117](#_Toc232859871)

[4.11.3.2.1 Schedule Application Job for Outbound Delivery Creation 117](#_Toc232859872)

[4.11.3.2.2 Pick, Pack and Post Goods Issue for Outbound Delivery from Distribution Center 118](#_Toc232859873)

[4.11.3.2.3 Create Billing Document 119](#_Toc232859874)

[4.11.3.2.4 Validate Follow-On Documents (Optional) 120](#_Toc232859875)

[4.12 Sales from Distribution Center 121](#_Toc232859876)

[4.12.1 Create Sales Quotation 121](#_Toc232859877)

[4.12.2 Change Quotation Document (Optional) 123](#_Toc232859878)

[4.12.3 Create Sales Orders 124](#_Toc232859879)

[4.12.4 Create an Outbound Delivery 125](#_Toc232859880)

[4.12.5 Create Attachment for Delivery (Optional) 127](#_Toc232859881)

[4.12.6 Process Picking for Outbound Delivery 128](#_Toc232859882)

[4.12.7 Post Goods Issue for Outbound Delivery 129](#_Toc232859883)

[4.12.8 Create Billing Document 130](#_Toc232859884)

[4.12.9 Create Attachment for Billing Document (Optional) 131](#_Toc232859885)

[5 Appendix 133](#_Toc232859886)

[5.1 Physical Inventory for Stores (Optional) 133](#_Toc232859887)

## Purpose

Overview

In the consignment process, the supplier retains the complete (legal) ownership of the merchandise until the retailer sells it to a customer (buyer). From a financial perspective, the inventory is kept in the supplier account, and the retailer has non-valuated stocks in distribution centers and stores. For the retailer, an advantage of the consignment process is the reduced risk due to no capital tie up for the respective products. Additionally, the supplier can address customer's requirements without the need for its own sales force and marketing activities.

During article master maintenance, you can decide if supplier consignment is relevant for each site.​

It's essential that the consignment stock category is preserved in all goods movements. Consignment stock can be transferred from distribution center to stores, and more often, goods in consignment stock can be transferred across sites as necessary. In the point-of-sale (POS) inbound processing, the stock category is determined and the consignment inventory is adjusted. For the customer order-based sales process at store and distribution center, goods issues can be posted from the consignment stock.

All variations of return processes are supported – from store to the external supplier directly, or in two-steps process, which is from store to distribution center and then from distribution center to the supplier. In the stock overview, you can view if the inventory is company-owned by the retailer or consigned by a supplier.

Concerning the settlement, the supplier doesn't issue the invoice directly to the retailer after the merchandise arrives at the premises of the retailer. The retailer is liable to pay the supplier only when the stock is consumed. Thus, a retailer triggers a settlement through different types of movements, for example, from POS sales, from sales orders, or from other stock adjustments.

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

The test should be conducted with the following system:

| System | Details |
| --- | --- |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Master Data Specialist - Product Data (Retail) | SAP_BR_MD_SPCLST_ITEM_RFM | Master Data Specialist - Product Data (Retail) | SAP_BR_MD_SPCLST_ITEM_RFM |  |
| Assortment Specialist - Retail | SAP_BR_ASSTMT_SPCLST_RFM | Assortment Specialist - Retail | SAP_BR_ASSTMT_SPCLST_RFM |  |
| Purchaser (Retail) | SAP_BR_PURCHASER_RFM | Retail Purchasing / Retail Sourcing and Contracting | SAP_RFM_SPT_PURCHASING_PC / SAP_RFM_SPT_SOURCING_PC |  |
| Purchasing Manager | SAP_BR_PURCHASING_MANAGER | My Inbox | SAP_CORE_SPT_MYINBOX_PC |  |
| Receiving Specialist | SAP_BR_RECEIVING_SPECIALIST | Receiving | SAP_BR_RECEIVING_SPECIALIST |  |
| Warehouse Clerk (Retail) | SAP_BR_WAREHOUSE_CLERK_RFM | Retail Inventory Processing | SAP_RFM_SPT_INVTRY_PROCG_PC |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Inventory Manager (Retail) | SAP_BR_INVENTORY_MGR_RFM | Retail Inventory Management | SAP_RFM_SPT_INVTRY_MGMT_PC |  |
| Retail Store Associate | SAP_BR_RFM_STORE_ASSOCIATE | Store Operations | SAP_BR_RFM_STORE_ASSOCIATE |  |
| Administrator (Retail) | SAP_BR_ADMINISTRATOR_RFM | Administration - Retail | SAP_BR_ADMINISTRATOR_RFM |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Article | R_6500 | Polaroid Sunglasses |  |
| Merchandise Category | R5113003 | Sunglasses |  |
| Material Type | HAWA | Trading Goods |  |
| Material Category | 00 | Single Material |  |
| Division | 00 | Product Division 00 |  |
| Company Code | 3310 | Company Code 3310 |  |
| Sales Organization | 3310 | Dom. Sales Org |  |
| Purchasing Organization | 3310 | Purch. Org. 3310 |  |
| Distribution Channel | 10 | Direct Sales |  |
| Distribution Channel | 40 | Store Sales |  |
| Distribution Channel | 50 | Distribution |  |
| MRP Controller | 001 | MRP Controller 001 |  |
| Purchasing Group | 002 | Group 002 |  |
| Storage Location | 995A | Storage Loc. DC |  |
| Storage Location | 994A | St.Loc.Neg.Stock |  |
| Distribution Center | 3350 | DC 3350 AE |  |
| Distribution Center | 3391 | Ref DC 3391 AE |  |
| Store | 3340 | Store 3340 AE |  |
| Store | 3392 | Ref Store 3392 AE |  |
| Supplier | 33213001 | Retail Non-Food Supplier AE |  |
| Shipping point | 3350 | SP DC 3350 |  |
| Sold-to-Party/Ship-to-Party | 33113007 | Wholesale non-Food AE |  |
| B2C Sold-to Party/ Ship-to party/Payer | 33113008 | Consumer 1 AE |  |
| One-time Sold-to Party/ Ship-to party/Payer | 33113005 | Consumer 1 AE |  |

### Preliminary Steps

#### Customer Maintenance Settings

##### Assign Template Customer to Schema

Purpose

The following procedure provides instructions for assigning template customer to customizing schema.

|  |
| --- |
| Note To create a template customer, please refer Create Template Customer (Reference Consumer) in scope item Business Partners for Retail (5FH) |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Project Experience in SAP Central Business Configuration. |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign Template Customer to Schema.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Assign Template Customer to Schema screen is displayed. |  |
| 3 | Configure Assign Template Customer to Schema | Create the following settings:Choose Edit and add Template Customer against Customizing Schema. | Data provided. |  |
| 4 | Save | Choose Save. | The Customizing Schema has been saved. |  |

##### Assign Schema to Store

Purpose

The following procedure provides instructions for assigning site to customizing schema.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Project Experience in SAP Central Business Configuration. |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign Schema to Store.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Assign Schema to Store screen is displayed. |  |
| 3 | Assign Site | Add plant and schema.For example,Plant: 3340 (Store 3340 AE)Customizing Schema: <Use your own schema>Choose Enter. | Plant and schema description is displayed. |  |
| 4 | Save | Choose Save. | The Customizing Schema has been saved. |  |

##### Assign Grouping Schema to Store

Purpose

The following procedure provides instructions for assigning site to grouping schema.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Project Experience in SAP Central Business Configuration. |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign Grouping Schema to Store.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Assign Grouping Schema to Site screen is displayed. |  |
| 3 | Assign Site | Give plant and Grouping Schema and choose Enter. | Plant and Schema descriptions will appear. |  |
| 4 | Save | Choose Save. | The Grouping Schema has been saved. |  |

#### Assign Retail Store Associate (User Persona) to a Store (Optional)

Use

To filter the data provided in the SAP Fiori In-store Merchandising apps to the relevant store, the store associates need to be assigned to a certain store (site). The store assignment can be changed at any point in time in case a store associate is helping in another store. Perform this process step if store associate (user persona) is not assigned to a store yet or store assignment needs to be changed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Retail Store Associate. |  |  |
| 2 | Access the App | Open the app My Store Assignment (F4334) | The My Store Assignment (F4334) screen is displayed. |  |
| 3 | Search Your Store | Enter Store ID, Name, Postal Code or City of the store, for instance, enter 3340 and select Search | The store details are shown in the Stores section. |  |
| 4 | Select Store | Select 3340. |  |  |
| 5 | Assign Store | When selecting a store, the Assign Me button above the store list is activated. Select the button to store the assignment. | You were assigned to store <store ID> , success message is displayed. |  |

Result

With the assignment to a store, the data shown in the different SAP Fiori In-Store Merchandising apps is filtered to the assigned store, hence the user only has access to relevant information increasing the efficiency of the day-to-day work.

#### Maintain Application Settings

Use

You perform this activity to create freight value condition for the article.

Purpose

In this process step, as a retail store associate you set the application setting before selecting the picking request. Once all the necessary settings are done, you can start picking of products on the shop floor.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Retail Store Associate. |  |  |
| 2 | Access App | Open Process Picking Requests (F4643) app. | Process Picking Requests (F4643) app screen is displayed along with a list of picking requests |  |
| 3 | Set Application Settings | Go to Profile of <Name of Retail Store Associate> (User’s Profile) on the top right corner of the Process Picking Requests screen > Application Settings. Make the following entries in the Application Settings pop-up and select OKPrinter: <Printer assigned to your store>Label Type: RFM_ST_PKORD_BOX_LABEL_STD (Sample Form for Box Label Printing)Content List Type : RFM_ST_PKORD_CNTNT_LIST_STD (Sample Form for Content List Printing)Note Application settings need to be set only the first time when any user is assigned to the store or if setting must be changed. | Application settings are saved message is displayed and application settings is set for the retail store associate. |  |

Result

Application settings are maintained.

#### Extend Article to E-commerce Channel

|  |
| --- |
| Note This section is relevant, before you can test the scenario Sell from Online Store, Delivery from Distribution Center to Customer (Pre-Paid Order) in this document. |

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

In the procedure, you can change article using Maintain Article (MM42) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data (Retail). |  |  |
| 2 | Access the App | Open Maintain Article (MM42) app. | The Change Material (Initial Screen) is displayed. |  |
| 3 | Enter Article Basic Data | In the Change Material (Initial screen), enter article number defined for consignment articles as R_6500 in the Material. |  |  |
| 4 | Choose Views | Select Sales views and choose Continue. | The Change Material R_6500 (Sales) screen is displayed . |  |
| 5 | Enter Organizational Level Data | In Switch Validity Area, in the Areas of Validity section, enter descriptions for the following:Sales Unit: (PC)Sales Org.: (3310/ Dom. Sales Org)Distr. Channel: (60 - E-Commerce)Choose Continue. |  |  |
| 6 | Enter Sales Data | On the Change Material R_6500 (Sales) screen, make the following entries:(All the below should ideally get filled automatically, but if you need to maintain any deviation then you can go ahead and maintain)For sale from: <date>For sale till: <date>Item Cat. Group: (NORM)Cash Discount : (X)PP Det. Seq. (Purchase Price Determination Sequence): (01/ Standard with price determination)SP Determ. Seq. (Sales Price Determination Sequence): (01/ Calculate SP from planned markup)Save Calculated Price: (X)Valid from: today's date |  |  |
| 7 | Save Your Data | Choose Save. | Sales prices are created.Material R_6500 changed message appears on the status bar. |  |

## Overview Table

This scope item consists of several process steps that are listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Create Master Data for Article for Consignment Processing

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Single Article](#unique_13) [page ] 23 | Master Data Specialist - Product Data (Retail) | Create Article (MM41)Manage Product Master Data (F1602) | Single article is created. |
| [Maintain Consignment Purchasing Info Record](#unique_14) [page ] 35 | Master Data Specialist - Product Data (Retail) | Manage Purchasing Info Records (F1982) | Purchase info record for consignment is created. |
| [Create Sales Conditions](#unique_15) [page ] 36 | Master Data Specialist - Product Data (Retail) | Maintain Article (MM42) | Sales prices are created. |
| [Assign Consignment Article to Assortment Module Version](#unique_16) [page ] 38 | Assortment Specialist - Retail | Manage Assortment Modules (F4892) | Cosignment article is assigned to assortment module version. |
| [Assign Consignment Article to Distribution Center](#unique_17) [page ] 39 | Assortment Specialist - Retail | Assign Products to Distribution Centers (F4543) | Cosignment article is assigned to distribution center. |

Procurement from External Supplier

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Purchase Order](#unique_18) [page ] 41 | Purchaser (Retail) | Manage Purchase Orders (F0842A) | Purchase order is created. |
| [Create Inbound Delivery](#unique_19) [page ] 42 | Receiving Specialist | Create Inbound Delivery (VL31N) | Inbound delivery document is created. |
| [Confirm Quantities for Putaway](#unique_20) [page ] 43 | Receiving Specialist | Create Inbound Delivery (VL31N) | Inbound delivery document with putaway quantity updated is saved. |
| [Post Goods Receipt for Inbound Delivery](#unique_21) [page ] 44 | Warehouse Clerk | Post Goods Movement (MIGO) | The goods receipt is posted. |

Store Ordering from Distribution Center

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Stock Transport Order](#unique_22) [page ] 46 | Purchaser (Retail) | Create Purchase Order - Advanced (ME21N) | Stock transport order is created. |
| [Create Replenishment Delivery for Stock Transfer Order](#unique_23) [page ] 47 | Shipping Specialist | My Purchase Orders - Due for Delivery (VL10B) | Outbound delivery is created. |
| [Post Goods Issue for Delivery](#unique_24) [page ] 48 | Shipping Specialist | Change Outbound Delivery (VL02N) | Goods issue is successfully posted. |
| [Check Stock in Transit](#unique_25) [page ] 49 | Inventory Manager | Display Stock in Transit (WB5N) | Stock in transit information is displayed. |
| [Post Goods Receipt for Outbound Delivery](#unique_26) [page ] 50 | Retail Store Associate | Receive Products (F1248) | Goods receipt is posted successfully. |
| [Check Stock Status(Optional)](#unique_27) [page ] 51 | Warehouse Clerk | Stock - Multiple Materials (F1595) | Consignment stock is displayed. |

Transfer Data to Point of Sale (POS)

Process Point of Sales (POS) Transactions

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Schedule Job to Set Stock Situation](#unique_28) [page ] 52 | Administrator (Retail) | Schedule Consignment Stock Situation Determination (F7736) | Stock situation is determined and updated. |

Invoice Receipt from Consignment Withdrawal

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Consignment settlement](#unique_29) [page ] 54 | Accounts Payable Accountant | Create Logistics Consignment and Pipeline Settlement (MRKON) | Invoice is posted and settlement document is created. |

Return from Stores

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Returns Stock Transport Order](#unique_30) [page ] 56 | Purchaser (Retail) | Create Purchase Order - Advanced (ME21N) | Return stock transport order is created. |
| [Create Outbound Delivery](#unique_31) [page ] 57 | Shipping Specialist | My Purchase Orders - Due for Delivery (VL10B) | Outbound delivery is created. |
| [Perform Picking and Post Goods Issue for Outbound Delivery](#unique_32) [page ] 58 | Shipping Specialist | Change Outbound Delivery (VL02N) | Post goods issue is initiated. |
| [Check Inbound Delivery](#unique_33) [page ] 59 | Purchaser (Retail) | Create Purchase Order - Advanced (ME21N) | Inbound delivery number is displayed. |
| [Perform Post Goods Receipt](#unique_34) [page ] 60 | Receiving Specialist | Change Inbound Delivery (VL32N) | Goods receipt for inbound delivery is posted. |
| [Check Stock Status(Optional)](#unique_27) [page ] 51 | Receiving Specialist | Display Advanced Stock Overview (RWBE) | Consignment stock is displayed. |

Return to Supplier

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Returns Purchase Order](#unique_35) [page ] 62 | Purchaser (Retail) | Create Purchase Order - Advanced (ME21N) | Return purchase order is created. |
| [Create Outbound Delivery](#unique_36) [page ] 64 | Shipping Specialist | My Purchase Orders - Due for Delivery (VL10B) | Outbound delivery is created. |
| [Pick and Post Goods Issue](#unique_37) [page ] 65 | Shipping Specialist | Change Outbound Delivery (VL02N) | Post goods issue is posted. |

In-Store Inventory Management

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Look Up General Product Information](#unique_38) [page ] 66 | Retail Store Associate | Look Up Retail Products (F0431) | The store associate can view the stock level of a product as well as general information to inform the consumer. |
| [Review Order Proposals](#unique_39) [page ] 67 | Retail Store Associate | Order Products (F0752) | The store associate reviews and changes the order proposals. |

Sell from Store: Immediate Pickup

| Process Step | Business Role | App | Expected Results |
| --- | --- | --- | --- |
| [Verify Consumer Registration](#unique_40) [page ] 68 | Retail Store Associate | Display Customer (WDA_WSSD_CUST) | Consumer details are verified, if consumer is already registered. |
| [Create Master Data for Registering a New Consumer (Optional)](#unique_41) [page ] 69 | Retail Store Associate | Create Customer (WDA_WSSD_CUST) | Consumer master is created. |
| [Create Sales Order and Generate Invoice](#unique_42) [page ] 70 | Retail Store Associate | Manage Sales Orders (F1873) | Sales order is created. |
| [Process Customer Order Payment from POS](#unique_43) [page ] 72 | Administrator (Retail) | Schedule POS Inbound Service (F5236) | Customer order payment information is transferred from a POS system to SAP S/4HANA Cloud Public Edition. |

Sell from Store: Pickup at Later Date due to Stock Unavailability (Payment Done at Pickup)

| Process Step | Business Role | App | Expected Results |
| --- | --- | --- | --- |
| In-Store Operations |  |  |  |
| [Check Stock Availability in Store](#unique_44) [page ] 73 | Retail Store Associate | Look Up Retail Products (F0431) | Estimated date for future stock availability at store by sourcing from DC or external supplier is checked. |
| [Verify Consumer Registration](#unique_45) [page ] 74 | Retail Store Associate | Display Customer (WDA_WSSD_CUST) | Consumer details are verified, if consumer is already registered. |
| [Create Master Data for Registering New Consumers (Optional)](#unique_46) [page ] 75 | Retail Store Associate | Create Customer (WDA_WSSD_CUST) | Consumer Master is created, |
| [Create Sales Order](#unique_47) [page ] 76 | Retail Store Associate | Manage Sales Orders (F1873) | Sales order is created. Store picking request is created. Also, account assigned purchase requisition or account assigned stock purchase requisition is created. Sales order document is also printed. |
| [Print Sales Order Document (Optional)](#unique_48) [page ] 78 | Retail Store Associate | Manage Sales Orders (F1873) | Sales order document is printed and handed over to consumer. |
| Back-Office Operations from Distribution Center to Store |  |  |  |
| [Transfer Stock](#unique_49) [page ] 79 | Warehouse Clerk | Post Transfer Posting (MIGO_TR) | Move stock from unrestricted use of DC to sales order stock of DC. |
| [Schedule Application Job to Create Stock Transport Order](#unique_50) [page ] 81 | Purchaser (Retail) | Schedule Purchasing Jobs - Advanced (F1702) | Stock transport order (STO) is created for transfer of stock from distribution center to store. |
| [Create Stock Transport Order (Optional)](#unique_51) [page ] 82 | Purchaser (Retail) | Create Purchase Order - Advanced (ME21N) | Stock transport order (STO) is created with reference to the purchase requisition for transfer of stock from distribution center to store, manually. |
| [Schedule Application Job to Create Replenishment Delivery for STO](#unique_52) [page ] 83 | Shipping Specialist | Schedule Delivery Creation (F2228) | Outbound delivery document with reference to stock transfer order (STO), is created |
| [Pick, Pack, and Post Goods Issue for Replenishment Delivery from DC](#unique_53) [page ] 84 | Shipping Specialist | Change Outbound Delivery (VL02N) | Material (article) is picked then packed. Handling units are generated. Goods issue is posted for the outbound delivery from the distribution center. |
| In-Store Operations (Stock is replenished, Picking Initiated in Store) |  |  |  |
| [Post Goods Receipt for STO/Outbound Delivery](#unique_54) [page ] 85 | Retail Store Associate | Receive Products (F1248) | Goods receipt is posted against the stock transport order document or outbound delivery document or the purchase order document or inbound delivery document received at Store. Store associate is notified about stock reservation. After GR is posted, the stock is managed as sales order stock in the store. |
| [Start Picking](#unique_55) [page ] 86 | Retail Store Associate | Process Picking Requests (F4643) | Picking is started for the selected picking requests |
| In-Store Operations (Hand Over Orders to Consumers) |  |  |  |
| [Verify Consumer Order Details and Hand Over](#unique_56) [page ] 89 | Retail Store Associate | Hand Over Orders (F4639) | Details of the consumer’s order is verified using the mobile number, name or order number. |
| [Validate Follow-On Documents and Print Billing Document](#unique_57) [page ] 91 | Retail Store Associate | Manage Sales Orders (F1873) | Billing document is printed |

Click and Reserve - Order Fulfillment in Store (Stock is Available in the Store)

| Process Step | Business Role | App | Expected Results |
| --- | --- | --- | --- |
| [Create Sales Orders](#unique_58) [page ] 93 | Retail Store Associate | Create Sales Orders - VA01 (VA01) | Sales orders in SAP S/4HANA Cloud Public Edition starter system is simulated. |
| [Start Picking](#unique_59) [page ] 95 | Retail Store Associate | Process Picking Requests (F4643) | Picking is started for the selected store picking requests, product GTIN is scanned and handover shelf is assigned to the picking request. |
| [Look Over the Order Details for Handover](#unique_60) [page ] 98 | Retail Store Associate | Hand Over Orders (F4639) | Details of the selected order and the status of order placed in the handover shelf is displayed. Also, order withdrawal is done and order is handed over to the consumer. |
| [Validate Sales Order Document and Subsequent Document Flow (Optional)](#unique_61) [page ] 100 | Retail Store Associate | Manage Sales Orders (F1873) | Validate the updates on the sales order also the subsequent documents generated after completion of the picking and handover process. |
| [Process Customer Order Payment from POS](#unique_62) [page ] 101 | Administrator (Retail)Configuration Expert - Business Network Integration | Schedule POS Inbound Service (F5236)Overview Message Monitoring (F4515) | Point-of-sale (POS) financial transactions are transferred to the SAP S/4HANA Cloud Public Edition system. |

If the consumer wants to order more products in-store other than that ordered at web-shop, refer to section 4.1 of 3HU - In-Store Customer Order Management.

Click and Collect (Pre-Paid Order) - Order Fulfillment from Distribution Center to Store (Stock is Not Available in the Store)

| Process Step | Business Role | App | Expected Results |
| --- | --- | --- | --- |
| [Create Sales Order](#unique_63) [page ] 102 | Retail Store Associate | Create Sales Orders - VA01 (VA01) | Sales orders in SAP S/4HANA Cloud Public Edition Starter System is simulated. |
| Back-office Operations from Distribution Center to Store |  |  |  |
| [Transfer Stock](#unique_64) [page ] 104 | Warehouse Clerk | Post Transfer Posting (MIGO_TR) | Move stock from unrestricted use of DC to sales order stock of DC. |
| [Schedule Application Job to Create Stock Transport Order](#unique_65) [page ] 106 | Purchaser (Retail) | Schedule Purchasing Jobs - Advanced (F1702) | Stock transport order (STO) is created for transfer of stock from distribution center to store. |
| [Create Stock Transport Order (Optional)](#unique_66) [page ] 107 | Purchaser (Retail) | Create Purchase Order - Advanced (ME21N) | Stock transport order (STO) is created with reference to the purchase requisition for transfer of stock from distribution center to store, manually. |
| [Schedule Application Job to Create Replenishment Delivery for STO](#unique_52) [page ] 83 | Shipping Specialist | Schedule Delivery Creation (F2228) | Outbound delivery document with reference to STO, is created |
| [Pick, Pack, and Post Goods Issue for Replenishment Delivery from DC](#unique_67) [page ] 109 | Shipping Specialist | Change Outbound Delivery (VL02N) | Material (Article) is picked then packed. Handling units are generated. Goods issue is posted for the outbound delivery from the distribution center. |
| In-Store Operations |  |  |  |
| [Post Goods Receipt for STO/Outbound Delivery](#unique_68) [page ] 110 | Retail Store Associate | Receive Products (F1248) | Goods receipt is posted against the stock transport order document or outbound delivery received at Store. Store associate is notified about stock reservation. After GR is posted, the stock is managed as sales order stock in the store. |
| [Verify Consumer Order Details](#unique_69) [page ] 111 | Retail Store Associate | Hand Over Orders (F4639) | Details of the selected order and the status of order placed in the handover shelf is displayed. Also, order withdrawal is done and Order is handed over to the consumer. |
| [Validate Sales Order Document and Subsequent Document Flow (Optional)](#unique_70) [page ] 114 | Retail Store Associate | Manage Sales Orders (F1873) | Validate the updates on the sales order also the subsequent documents generated after completion of the picking and handover process. |

Sell from Online Store, Delivery from Distribution Center to Customer (Pre-Paid Order)

| Process Step | Business Role | App | Expected Results |
| --- | --- | --- | --- |
| [Create Sales Order](#unique_71) [page ] 115 | Retail Store Associate | Create Sales Orders - VA01 (VA01) | Sales orders in SAP S/4HANA Cloud Public Edition Starter System is simulated. |
| Back Office Operations in Distribution Center |  |  |  |
| [Schedule Application Job for Outbound Delivery Creation](#unique_72) [page ] 117 | Shipping Specialist | Schedule Delivery Creation (F2228) | Background job for outbound delivery document creation is scheduled. |
| [Pick, Pack and Post Goods Issue for Outbound Delivery from Distribution Center](#unique_73) [page ] 118 | Shipping Specialist | Change Outbound Delivery (VL02N) | Material (Article) is picked then packed. Handling units are generated. Goods issue is posted for the outbound delivery from the distribution center. |
| [Create Billing Document](#unique_74) [page ] 119 | Billing Clerk | Create Billing Documents (F0798) | Billing document with reference to outbound delivery, is created. |
| [Validate Follow-On Documents (Optional)](#unique_75) [page ] 120 | Retail Store Associate | Manage Sales Orders (F1873) | Successful creation of outbound delivery, goods issue and billing document is validated. |

Table 2: Sales from Distribution Center

| Process Step | Business Role | App | Expected Results |
| --- | --- | --- | --- |
| [Create Sales Quotation](#unique_76) [page ] 121 | Internal Sales Representative | Manage Sales Quotations (F1852) | Sales quotation is created |
| [Change Quotation Document (Optional)](#unique_77) [page ] 123 | Internal Sales Representative | Manage Sales Quotations (F1852) | Sales quotation is changed. |
| [Create Sales Orders](#unique_78) [page ] 124 | Internal Sales Representative | Create Sales Orders - VA01 (VA01) | Sales order is created. |
| [Create an Outbound Delivery](#unique_79) [page ] 125 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) | Delivery from sales order is created. |
| [Create Attachment for Delivery (Optional)](#unique_80) [page ] 127 | Shipping Specialist | Display Outbound Delivery (VL03N) | Attachment for delivery is created. |
| [Process Picking for Outbound Delivery](#unique_81) [page ] 128 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Picking for delivery is complete. |
| [Post Goods Issue for Outbound Delivery](#unique_82) [page ] 129 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Issue of goods against the delivery is posted. |
| [Create Billing Document](#unique_83) [page ] 130 | Billing Clerk | Create Billing Documents (F0798) | Billing document is created |
| [Create Attachment for Billing Document (Optional)](#unique_84) [page ] 131 | Billing Clerk | Manage Billing Documents (F0797) | Attachment for billing document is created. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Master Data for Article for Consignment Processing

#### Create Article Master Data

##### Create Single Article

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The single article is the standard product that is sold to the customer also known as material.

This article cannot be changed into a generic article and a generic article cannot be changed into a single article.

The following procedure provides instructions for creating single article master data. The SAP Fiori apps available to you are dependent on your assigned role. You can create single article in one of the following ways

Procedure: Option 1 - Create Single Article using Create Article Application

In the procedure you create article using Create Article (MM41) app.

There are different views to maintain an article:

Basic Data

Global article data are defined. These are not specific to a supplier, plant, or distribution chain, example:

- Possible units of measurements, weights and dimensions
- EAN code
- Description
- Product group assignment

Sales

Distribution chain-specific data are maintained for the article. This is for example a sales price for a defined distribution chain and sales unit of measurement. The data can be maintained for exceptions, even at plant or price list level.

Logistic Distribution Center

Plant-specific article data for distribution centers are maintained. Below are the following options:

- Defining data for all distribution centers
    - The data is maintained for the reference distribution center and valid for all distribution centers.
- Defining data for one distribution center
    - Exceptions can be maintained individually for relevant distribution center.

Logistic relevant data like storage location and replenishment data are maintained at this level.

Logistic Store Data

Plant-specific article data for stores are maintained. There are the following options:

- Defining data for all stores
    - The data is maintained for the reference stores and valid for all relevant stores.
- Defining data for one store
    - Exceptions can be maintained individually for relevant stores.

Logistic relevant data like storage location and replenishment data are maintained at this level.

POS Data

Article data which are required for communicating with point-of-sale (POS) systems are maintained. The data always relates to a single distribution chain for the Article. The data can be maintained for exceptions even at Plant level. Data such as receipt text for each sales unit is maintained.

There is the possibility to use a dedicated article as reference for the creation and field values are proposed from the reference.

If there is no specific reference article specified – data from the merchandise category reference article are proposed.

The proposed field values can always be adjusted if necessary for the new article.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data (Retail) |  |  |
| 2 | Access the SAP Fiori App | Open Create Article (MM41) app. | The Create Article (MM41) (Initial Screen) is displayed. |  |
| 3 | Enter Article Basic Data | In the Create Article (MM41) (Initial screen):Material: Article number (R_XXXX)Material type: Trading Goods/HAWA Trading GoodsMaterial Group: R5113003/SunglassesMaterial Category: Single material/00 Single materialSelect Enter. | If there is no particular reference article on the input screen, data from the merchandise category reference article is proposed on the various screens. It's possible to overwrite the data. |  |
| 4 | Choose Views | Select Basic data, Basic data 2, Sales, Logistics Dc, Logistics Store & POS views and choose , continue. |  |  |
| 5 | Enter Basic Data | From Create Article ...(Basic Data),, on the Basic data tab, enter a Article description (short text). | Create Article … (Basic Data) is displayed. |  |
| 6 | Enter Basic Data | In the Unit of measure/EANs/dimensions section, enter the following:Base Base Unit of Measure (PC)Number of Lower-level <value>Unit of Measure <value>Gross Weight (<value>)Unit of Weight (KG)Net Weight (<value>)EAN Category (IE - Instore EAN (int. assignment possible)) | Subscreen: Units of Measure/EAN’s/Dimensions.Enter the measurements and dimensions of the Article. |  |
| 7 | Navigate to Go to Additional data in Basic Data View: | In Short Text View enter the description in second language:Language ENMaterial Description <Value>In the Unit of Measure View maintain/check the following (for Alternate UOM):Length <value>Width <value>Height <value>Unit Of Dimension (CM)Volume <value>Volume Unit (M3)Gross Weight <value>Unit of Weight (KG)EAN Category (IE)In the Additional EANs view maintain the additional EANs for the unit of measures (optional):EAN category (IE)Alt unitThen select Go to Main Data | Basic Data screen is displayed.User can maintain multiple EANs for each unit of measure. |  |
| 8 | Enter Basic Data | In Groupings section:Division 00In General Data:Tax Class (1 - Full Tax)Valuation Class (3100- Trading goods)Country of Origin AEIn Internal logistics data:Supply Source (I - Stock Transfer Before Consignment Before Standard) C/Consignment Before StandardGenItemCatGroup (NORM)Loading Group (0001- Crane)Transportation Group (0001- On pallets )Variable Order Unit: 1/ActiveIn Content section:Net Contents <value>Gross Contents <value>Content Unit (KG)Comparison Price Unit (1)In Validity section (Optional):Valid from: <date>Valid to: <date>(default 31.12.9999, cannot be maintained)In Shelf Life Data section (Optional):Remaining Shelf LifeTotal Shelf LifePeriod indicatorStorage % | Shelf Life Data section: This section is only maintained if really applicable for the article.Note the date of production must be entered in the goods receipt. |  |
| 9 | Choose Views | Select Basic Data 2 View and choose continue/enter. | Create Article …(Basic data 2) view is displayed. |  |
| 10 | Enter Sales Period | In Sales period for Stores and Distribution CenterSales Period: storeFor sale fromFor sale tillSales Period: distribution centerFor sale fromFor sale till |  |  |
| 11 | Choose Views | Select Sales View and choose continue/enter. | Create Article …(Sales)view is displayed. |  |
| 12 | Enter Organizational Levels Data | In Switch Validity Area, in the Area of Validity section, enter values for the following:Sales Unit (PC)Sales Org. 3310/Dom. Sales OrgDistr. Channel (40/Store Sales)Select Continue. |  |  |
| 13 | Enter Sales Data | On the Create Article :Sales screen, make the following entries:(Few of the below ideally get filled automatically from the Reference Article for example item category group, cash discount,.):Sales Unit ( e.g. PC in case of Sales area 3310/40 )For Sale from <date>For Sale to <date>Item Category Group (NORM)Cash Discount (X)PP det. Seq.(Purchase Price determination Sequence) (01/ Standard with price determination)SP det Seq. (Sales price Determination Sequence) (01/ Calculate SP from planned markup)Final Price (<value>)Save Calculated Price (X) | Repeat the same step 11 and 12 for maintaining sales area – 3310/50 (For DC) – Pass Sales Unit as CARAdministrator can also maintain sales organization 3310 and distribution channel 10 for wholesale process. |  |
| 14 | Choose Views | Choose Logistics DC tab.Check for the below entries:In MRP Parameters:MRP Type: R1/Time-Phased Planning)Lot Size: EX/Lot-for-lot order quantity)Safety Stock: <value> By default it is 0Rounding profile: RDYP/ Retail Dynamic Rounding ProfileIn MRP Controller/Replenishment Data:MRP Controller: 001/MRP Controller 001Planning Cycle: P01/Order Day MondayPlanned Delivery Time: 5Supply Source: C/Consignment before StandardConsignment Control: C/Procurement for consignment stockIn General ControlParameters:Purchasing Group: 002/Group 002Tax Indicator: 1/Full TaxAutomatic PO: XAvailability Check: ST/Consider only StockIn Physical Inventory/Goods Issue/ Picking/ Shipping section:Loading Group: 0001/CraneIn Storage Data:Storage Location: 995A | Create Article …(Logistics DC) view is displayed.On the Create Article : Logistics DC screen, check the available entries. These are proposed based on the reference Article . Only changes must be maintainedRounding profile is a key that the system uses to adjust the order proposal quantity to deliverable units. |  |
| 15 | Navigate to MRP/Forecast Data inside Logistics DC View | In the MRP/Forecast View maintain or check for the below entries:In Procurement section:Procurement Type: F/External procurement (display only)Special Procurement: 10Stock Determination Group:0001In Control data section:Auto reset: XPress Back button to navigate back to Logistics DC view. |  |  |
| 16 | Choose Views | Choose Logistics Store tab.Check for the below entries:In MRP Parameters:MRP Type: RF/Replenish with dyn.Target StockConsignment Control: 1/Procurement from Consignment stockSafety Stock: <value> By default it is 0In Replenishment section:Target Coverage: 5In the Forecast Parameters:Forecast Model: K/Constant with smoothing factor adjustmentIn MRP Controller/Replenishment Data:Planned Delivery Time: 3Supply Source: I/Stock Transfer Before Consignment Before StandardIn General Control Parameters:Purchasing Group: 002/Group 002Tax Indicator: 1/Full taxAutomatic PO: XAvailability Check: ST(ST – Consider only stock)Negative Stock: XIn Storage Data:Storage Location: 994A | Create Article …(Logistics Store) view is displayed.On the Create Article : Logistics Store screen, These are proposed based on the reference Article . Check the available entries and do adjustments if necessary (for example supply source).Dynamic Target Stock is calculated at runtime during the planning run from forecast sales value. |  |
| 17 | Navigate to MRP/Forecast Data inside Logistics Store View | In the MRP/Forecast View maintain or check for the below entries:In Procurement section:Procurement Type: : F (External procurement)(display only)Stock Determination Group: 0001In the Number of Periods Required section:History Periods: 60Forecast Periods: 12In Control Data section:Initialization: XTrack Limit: 4(Value that specifies the amount by which the may deviate from the actual value.)Auto reset: XModel Selection Procedure: 2 (Analytical model selection procedure)Press Back button. | Administrator is navigated back to the Logistics Store view. |  |
| 18 | Choose Views | Choose POS tab.Enter Till receipt Text as mentioned below:Language Key: ENAlternate Unit: PCTill receipt text for Unit: <value> | Create Article …( POS) view is displayed.Maintain POS Text for distribution chain: 3310/40 (that is the relevant distribution chain for stores - in the case a different is proposed - the user should switch to this distribution chain)Maintain if necessary the text in different languages. Press the Insert Row (+) to add a new entry. |  |
| 19 | Save Your Data | At the bottom right of the display, choose Create to save your data. | The Create Article (Initial Screen) is displayed.The single article is created and saved.You can change or maintain or update the article created above, using Maintain Article (MM42) app. |  |

Procedure: Option 2 - Manage Product Master Data

In this procedure you can create product master data using the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data (Retail). |  |  |
| 2 | Access the SAP Fiori App | Open Manage Product Master Data (F1602) app. | The Manage Product Master Data (F1602) screen is displayed. |  |
| 3 | Choose Create New Product Master | In the Manage Product Master Data Manage Product Master Data (F1602) view, select Create button and select Single Article from the list. | The Create Master Data Record screen is displayed. |  |
| 4 | Enter Data for Mandatory Fields | In the Master Data Record sub-screen make the following entries:Product Number: for example,R_<XXXXX>You either enter any external alphanumeric ID, and that ID must start with an alphanumeric character, or if you provide no entry, the system automatically assigns a numeric ID.Product Type: Trading Goods(HAWA)Product Group: for example, R5113003/SunglassesBase Unit: for example, PCValuation Class: 3100/Trading GoodsTax Classification: 1/(Full Tax)Loading Group: 0001(Crane)Description: <any description> |  |  |
| 5 | Choose OK | In the Manage Product Master view, select OK. | The Manage Product Master view is displayed. |  |
| 6 | Enter General Information | In the Manage Product Master > General Information section, select Show More and enter the following details in the Content / Design section:Net Contents <value>(KG)Gross Contents <value>(KG)Comparison Price Unit (1)(KG) |  |  |
| 7 | Choose General Information - Descriptions | In the Manage Product Master > General Information > Descriptions view, choose Create. | Description in default language (for example, English) is already populated. |  |
| 8 | Enter Descriptions Data | In the Descriptions view, make the following entries:Language: for example, ArabicProduct: <your description> |  |  |
| 9 | Enter General Information - Base Unit of Measure Details | In the Manage Product Master > General Information > Base Unit of Measure sub-section, select Show More and make the following entries:GTIN: <user-input>GTIN Category: IEGross Weight: for example, 20Net Weight: for example, 20Weight Unit: for example, G |  |  |
| 10 | Enter Unit of Measure | In the Manage Product Master > General Information > Unit of Measure view, navigate to the details. |  |  |
| 11 | Enter Receipt Texts | In the Receipt Texts section, select CreateEnter Language and Text. | This text is relevant for the POS communication. |  |
| 12 | Press Apply button | Press Apply button to navigate back to main screen. |  |  |
| 13 | Choose Distributions Chains | In the Product screen, choose Distribution Chains tab. | The Distribution Chains tab is displayed. |  |
| 14 | Choose Create | In the Distribution Chains tab, choose Create | Distribution Chains is displayed in edit mode. |  |
| 15 | Enter Distribution Chains Data | In Distribution Chains, make following entries:In the GENERAL DATA - General Information section:Sales Organization: <Sales org number> 3310/Dom. Sales OrgNote The organization unit value is determined by what is offered in the value help.Distribution Channel: for example 40/Store SalesCash Discount: XIn the GROUPING TERMS section:Item Category Group: for example, NORM |  |  |
| 16 | Return to Main View | Choose Apply to return to Product screen. | The Product screen is displayed.Repeat step 18-19 to maintain the other distribution chains for example,3310/50 and 3310/10 . |  |
| 17 | Choose Distribution Centers | In the Product screen, choose Distribution Centers. | The Distribution Center tab is displayed. |  |
| 18 | Create Distribution Center relevant data | In the Distribution Centers view, choose Create. | The Distribution Center view is displayed. |  |
| 19 | Enter Distribution Center - General Information | In the General Information section, make following entries if not maintained:Check Stock Determination Group is set to Stock determination group 0001 (0001)Distribution Center: DC for example, 3391 (Reference DC comes by default, no need to enter explicitly and remain Non Editable) | The DC 3391 represents the reference distribution center for logistic data maintenance. DC 3391 is not an operational DC. Data maintained at reference DC level are inherited to all operational DCs and only exceptions for individual DCs must be maintained explicitly. |  |
| 20 | Enter Distribution Center - Sales Details | In the Sales section make following entry:Loading Grp: for example, 0001(Crane) |  |  |
| 21 | Enter Distribution Center - Purchasing Details | In Purchasing section:Purchasing Group: 002/Group 002Tax Indicator: 1/Full TaxSupply Source: C (Consignment Before Standard)Automatic Purchase Order allowed : X |  |  |
| 22 | Enter Distribution Center - MRP Data | In the MRP Data > MRP Data section, make following entries:MRP Type: For example, R1 – Time Phased PlanningMRP Controller: For example, 001/MRP Controller 001Planning Cycle: P01(Order Day Monday)Availability Check: for example, ST (Consider only Stock)In the MRP Data > Lot-Size Data section, make the following entry:Lot Sizing Procedure: for example EX/ Lot-for-lot order quantityIn the MRP Data > Procurement section, make the following entry:Planned Delivery Time: for example, 3Goods Receipt Processing Time: for example, 1Default Storage Location for external procurement: 995ASpecial Procurement Type: Consignment (10)Consignment Control: Procurement for Consignment Stock (1) |  |  |
| 23 | Return to Main Screen | Choose Apply to return to Product screen. | The Product screen is displayed. |  |
| 24 | Choose Stores | In the Product screen, choose Stores. | The Store tab is displayed. |  |
| 25 | Create Stores | In the Stores view, choose Create. | The Store view is displayed. |  |
| 26 | Enter Stores - General Information | In the General Information section, make following entries if not maintained:In General Section:Store: Store for example, 3392 (Reference Store comes by default, no need to enter explicitly and remain Non Editable)Negative Stock Allowed in Plant: XStock Determination Group:0001 | The store 3392 represents the reference store for logistic data maintenance. Store 3392 is not an operational store. Data maintained at reference store level are inherited to all operational stores and only exceptions for individual stores must be maintained explicitly. |  |
| 27 | Enter Stores - Sales Data | In the Sales Data section make following entry:Loading Grp: for example, 0001(Crane) |  |  |
| 28 | Enter Stores – Purchasing Data | In Purchasing Data:Purchasing Group: 002/Group 002Tax Indicator: 1/Full TaxSupply Source: I - Stock Transfer Before Consignment Before StandardAutomatic Purchase Order allowed : X |  |  |
| 29 | Enter Stores- MRP Data | In the MRP Data > MRP Data section, make following entries:MRP Type: For example, RF/Replenish with dyn.TargetStock.(Dynamic Target Stock gets calculated at runtime during the planning run from forecast sales value )Availability Check: for example, ST/ Consider only stockIn the MRP Data > Procurement section, make the following entry:Planned Delivery Time: for example, 3Goods Receipt Processing Time: for example, 1Default Storage Location for external procurement: 994AConsignment Control:Procurement for Consignment Stock (1) |  |  |
| 30 | Return to Main Screen | Choose Apply to return to Product screen. | The Product screen is displayed. |  |
| 31 | Save Your Data | Choose Create. | As a next step, you need to:Maintain purchasing Info record.You can change or maintain or update the article created above, using Maintain Article (MM42) app. |  |

###### Maintain Consignment Purchasing Info Record

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data (Retail). |  |  |
| 2 | Access the SAP Fiori App | Open Manage Purchasing Info Records (F1982) app | The Manage Purchasing Info Records (F1982) (Initial Screen) is displayed. |  |
| 3 | Choose Create button to create Info-record | Choose Create to create purchasing info record. | New Purchasing Info Record screen is displayed.Purchaser can maintain different kind of Inforecord via this app. For example, consignment, standard, sub-contracting and so on. |  |
| 4 | Enter Details in the Purchasing Info Record Screen | In the Purchasing Info Record screen, enter the below details:Purchasing Info Record category : (Consignment)Supplier Details (Vendor Details to be filled according to the article and suppliers dealing with the different kind of articles)Material : (Article Master created above)Purchasing Organization 3310/Purch. Org. 3310Purchasing group 002/Group 002Plant: No plant, Delete the defaulted valueDelivery and Quantity:Delivery Time in Days: (5)Order Unit: (PC)Standard Order Quantity: <value>Select Auto.Srcg (automatic sourcing).Confirmation Control: (Inbound Delivery)Go to Conditions section and select Create to enter the conditions | Purchasing view is displayed. |  |
| 5 | Enter Conditions | Conditions screen open up with a Condition PPR0. Maintain Validity dates and Amount for the same.Valid From <dates>Valid To <dates>Amount <value>Select Apply.Press Create button. | Consignment purchasing inforecord is created. |  |

###### Create Sales Conditions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

In the procedure, you can maintain additional sales prices for different unit of measurements using Maintain Article (MM42) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data (Retail). |  |  |
| 2 | Access the App | Open Maintain Article (MM42) app. | The Change Material (Initial Screen) is displayed. |  |
| 3 | Enter Article Basic Data | In the Change Material (Initial screen)Material: Article numberEnter Single Article,(<R_XXXXX>) |  |  |
| 4 | Choose Views | Select Sales views and choose Continue. | The Change Material R_XXXXX (Sales) screen is displayed . |  |
| 5 | Enter Sales Data | On the Change Material R_XXXXX (Sales) screen, make the following entries:(All the below should ideally get filled automatically, but if you need to maintain any deviation then you can go ahead and maintain)For sale from: <date>For sale till: <date>Item Cat. Group: NORMCash Discount : (X)PP Det. Seq. (Purchase Price Determination Sequence): (01/ Standard with price determination)SP Determ. Seq. (Sales Price Determination Sequence): (01/ Calculate SP from planned markup)Final price: (<value>)Save Calculated Price: (X) |  |  |
| 6 | Enter Organizational Level Data | In Switch Validity Area, in the Areas of Validity section, enter descriptions for the following:Sales Unit: (PC)Sales Org.: (3310/ Dom. Sales Org)Distr. Channel: (10 Distribution)Choose Continue. |  |  |
| 7 | Enter Sales Data | On the Change Material R_XXXXX (Sales) screen, make the following entries:(All the below should ideally get filled automatically, but if you need to maintain any deviation then you can go ahead and maintain)For sale from: <date>For sale till: <date>Item Cat. Group: NORMCash Discount : (X)PP Det. Seq. (Purchase Price Determination Sequence): (01/ Standard with price determination)SP Determ. Seq. (Sales Price Determination Sequence): (01/ Calculate SP from planned markup)Final price: (<value>)Save Calculated Price: (X) |  |  |
| 8 | Enter Organizational Level Data | In Switch Validity Area, in the Areas of Validity section, enter descriptions for the following:Sales Unit: (PC)Sales Org.: (3310/ Dom. Sales Org)Store:: (50 - Distribution)Choose Continue. |  |  |
| 9 | Enter Sales Data | On the Change Material R_XXXXX (Sales) screen, make the following entries:(All the below should ideally get filled automatically, but if you need to maintain any deviation then you can go ahead and maintain)For sale from: <date>For sale till: <date>Item Cat. Group: NORMCash Discount : (X)PP Det. Seq. (Purchase Price Determination Sequence): (01/ Standard with price determination)SP Determ. Seq. (Sales Price Determination Sequence): (01/ Calculate SP from planned markup)Final price: (<value>)Save Calculated Price: (X) |  |  |
| 10 | Save your Data | Choose SaveSales price are created. | Material R_XXXXX changed message appears on the status bar. |  |

###### Maintain Assortments

###### Assign Consignment Article to Assortment Module Version

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The article(s) can be assigned to the assortment module version in this process step. An assortment definition can be described as a relationship between products and stores. Therefore, the product assignment to the assortment module version is a vital step toward listing the product in a store.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Assortment Specialist - Retail. |  |  |
| 2 | Access App | Open the Manage Assortment Modules (F4892) app. | The app opens and displays list of available assortment modules as per selection criteria. |  |
| 3 | Search for Assortment Module | Set the Assortment Module CS_AE filter and chose Go. | The list report contains one line item with assortment module Assortment Module CS_AE. |  |
| 4 | Navigate to Assortment Module | In the list report, click the line item of assortment module Assortment Module CS_AEto trigger the navigation. | The object page of assortment module Assortment Module CS AE appears. |  |
| 5 | Start Product Assignment | In the Versions facet, click the line item of the version with valid-from date applicable as of today. | The Assign Products to Version dialog box appears. |  |
| 6 | Enter Required Data and Finish Product Assignment | In the Assign Products to Version dialog box, make the following entries and choose Assign:Products: R_<XXXXX>Select the Assign to Follow-on Versions checkbox. | The dialog box disappears, and the newly assigned product appears in the table of the Products facet.The line item contains the following data:Product: R_<XXXXX>Assigned From/To: <Your Start Date of the First Version> - <End Date of the First Version>. |  |

|  |
| --- |
| Note If you do not use a single article in the above-mentioned process but any other product category, the system automatically lists the necessary dependencies. Instead, you can also assign the variants or a selection thereof directly to the assortment module version, without using the generic article. If you assign a structured article to an assortment module version, the system automatically generates the necessary listing conditions and product master data for the components (depending on the configuration for structured articles). Finally, if you assign a full product, the system automatically generates listing conditions and product master data for the empties. |

###### Assign Consignment Article to Distribution Center

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You have already defined the relationship between the product and the store in the previous steps, that is, you have defined which product can be procured by which store. Subsequently, you have to assign the relevant products to the appropriate distribution center so that they are orderable.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Assortment Specialist - Retail. |  |  |
| 2 | Access App | Open the Assign Products to Distribution Centers (F4543) app. | The app opens and a list report with an empty result table appears. |  |
| 3 | Search for Products to Be Assigned | Set the Assigned to DC filter to No."Set the Product filter by entering <R_XXXX> and choose Go." | The list report contains "one line item with <R_XXXX>". |  |
| 4 | Start Product Assignment to Distribution Center | Select the product(s) created before by selecting the checkbox of each line item and choose Add Assignments. | The Assign Products to Distribution Centers dialog box appears. |  |
| 5 | Select Distribution Center and Finish Product Assignment to Distribution Center | In the Assign Products to Distribution Centers dialog box, search for distribution center 3350, select the corresponding checkbox, and choose Assign. | This is due to the fact that the Assigned to DC filter is set to No.After product has been assigned, the list does not display that product.This is due to the fact that the Assigned to DC filter is set to No. The product is now assigned to a distribution center and filter criteria is not matched. |  |
| 6 | Search for Assigned Products | Set the Assigned to DC filter to "Yes" and choose Go. | "Your article(s) created before appear" as line items in the result table of the list report. |  |
| 7 | Check for Correctness of Product Assignment | In the list report, click the line item of one of the products to trigger the navigation. | The object page of the product appears. Check whether the Product Assignments facet contains a line item with the following data:Distribution Center: 3350Assigned From: Current dateAssigned To: 31.12.9999 |  |

### Procurement from External Supplier

#### Create Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to formalize a specific requirement for a material from the supplier by creating a purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser (Retail). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Create Purchase Order - Advanced (ME21N). | The Create Purchase Orders Advanced screen is displayed. |  |
| 3 | Create Purchase Order data | Choose Create Purchase Order.On the Purchase Order Screen, make the following entries and choose Enter:In the General Information area:Supplier: 33213001Currency: AEDPurchasing Group: 002Purchasing Organization: 3310Company Code: 3310In the Items area, choose Create and make the following entries:Item Category: Consignment(K)Material: R_6500Order Quantity: X PCPlant: 3350Choose the item and go to the Purchase Order Item screen.Go to the Delivery Details area:Storage Location: 995AChoose Apply to go back to Purchase Order screen. |  |  |
| 4 | Save Purchase Order | Choose Order and when the purchase order number is displayed, write it down for further use. | The Purchase Order is created. |  |

#### Create Inbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you manually create inbound delivery with reference to purchase order (PO).

|  |
| --- |
| Note The supplier gives information on merchandise, quantities, and dates of delivery, which is stored in an inbound delivery document. It can be created manually as described. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Receiving Specialist. |  |  |
| 2 | Access App | Open Create Inbound Delivery (VL31N) app. | Create Inbound Delivery (VL31N) app screen is displayed. |  |
| 3 | Start Selection for Inbound Delivery Creation | On the Create Inbound Delivery (VL31N) app screen, enter the following:Supplier: 33213001Purchase Order:<your Purchase Order document number>Select Continue. |  |  |
| 4 | Save Inbound Delivery Document | Select Save. | Inbound delivery document is created. |  |

#### Confirm Quantities for Putaway

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you confirm putaway quantity for inbound delivery based on the physical check of the goods arrived at distribution centre.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Receiving Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Change Inbound Delivery (VL32N) app. | Change Inbound Delivery screen is displayed. |  |
| 3 | Open Inbound Delivery Document | Enter Inbound Delivery: <your Inbound Delivery document number> and choose Continue. | Overview of delivery document is displayed. |  |
| 4 | Specify Putaway Quantity | Navigate to the Item Overview tab.In the All Items table, scroll to the right to find the Putaway Qty column.Enter or adjust the putaway quantity if there is a difference between the delivery quantity and the quantity that has arrived. | Putaway quantity is updated. |  |
| 5 | Save Inbound Delivery | Choose Save. | Inbound delivery document with the updated putaway quantity is saved. |  |

#### Post Goods Receipt for Inbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you post goods receipt for inbound delivery to update the inventory information in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Warehouse Clerk. |  |  |
| 2 | Access the App | Open Post Goods Movement (MIGO) app. | The Goods Receipt screen is displayed. |  |
| 3 | Enter Inbound Delivery Number | Provide the values for the following entries and select Enter:Select Goods Receipt and Inbound Delivery from the dropdown and enter the following: Inbound Delivery Number: XXX Goods Movement Type: 101Select Enter. | The data with in the selected inbound delivery like article, quantities are displayed. |  |
| 4 | Check and Post the Goods Receipt for Inbound Delivery | Scroll to the bottom of the Goods Receipt Inbound Delivery xxxxxxxxxx screen, select to check the Item OK checkbox. Select Check on the bottom right of the screen. Select Post. | The goods receipt is posted.Message Material Document <Document number> posted. is displayed. |  |

#### Check Stock Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you check the stock situation (Consignment Stock) at the receiving distribution center.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launch Pad as a Warehouse Clerk. |  |  |
| 2 | Access the Application | Open Stock-Multiple Material(F1595) app. | The Stock-Multiple Materials app screen is displayed. |  |
| 3 | Enter Article | Enter ArticleDistribution center: 3350and press on GO button.Article:R_6500 | Stock Situation gets displayed with Special Stock Type ''K'' and Special Stock Description ‘Supplier Consignment' . |  |

### Store Ordering from Distribution Center

#### Create Stock Transport Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a stock transport order manually.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser (Retail). |  |  |
| 2 | Access the App | Open Create Purchase Order - Advanced (ME21N) app. | Create Purchase Order - Advanced (ME21N) screen is displayed. |  |
| 3 | Select Stock Transport Order Type | Select UD - StockTranspOrderDel from Order type drop down listNote Please don’t use Stock Transp. Order (UB) | Order type is selected, |  |
| 4 | Enter the parameters | Enter the following data:Supplying Plant: 3350In the Header area, Org. Data tab:Purch. Org: 3310Purch. Group: 002Company Code: 3310In Item Overview:Material: R_6500PO Quantity: 5Delivery Date: <any date in the future>Receiving Store: 3340Storage Location: 994A | Data entered |  |
| 5 | Save Stock Transport Order | Choose Save | StockTranspOrderDel created under the number XXXXXXXXXX message is displayedMake a note of the stock transport order |  |

#### Create Replenishment Delivery for Stock Transfer Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you manually create replenishment or outbound delivery with reference to stock transfer order (STO).

|  |
| --- |
| Note You can create outbound deliveries by scheduling background job which is in close alignment with the DC and their work shifts there. However, to test this scope outbound deliveries are created manually. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access App | Open My Purchase Orders - Due for Delivery (VL10B) app. | Purchase Orders, Fast Display screen is displayed. |  |
| 3 | Start Selection for Outbound Delivery Creation | On the entry screen of the Purchase Orders, Fast Display app, make the following entries and Select Execute:Remove Deliv. Creation Date (both from and to dates)Shipping point: 3350Go to Purchase Orders tab view, enter Purchasing Document:<STO Document Number> created in above step | A list of purchasing documents for the selected shipping point is displayed. |  |
| 4 | Select Purchasing Document for Outbound Delivery Creation | Mark your purchasing documents and select Background. | Outbound delivery document is created. |  |
| 5 | View the Created Outbound Delivery Document Number | Select Log for delivery creation, then select Documents on the right top of the Delivery Creation Log screen . | Outbound delivery document number is displayed. |  |

#### Post Goods Issue for Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, post the goods to remove them from the distribution center's inventory management system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access App | Open Change Outbound Delivery (VL02N) app. | Change Outbound Delivery (VL02N)screen is displayed. |  |
| 3 | Open Outbound Delivery Document | On the Change Outbound Delivery (VL02N) app screen, enter <your outbound delivery document number> and select Continue. |  |  |
| 4 | Specify Picked Quantity | Go to Picking tab and specify: Picked Qty : <Enter quantity equal to delivery quantity> | Picked quantity is updated. |  |
| 5 | Save the Outbound Delivery Document | Select Save. | Outbound delivery document is saved. |  |
| 6 | Post Goods Issue | On the Change Outbound Delivery (VL02N) app screen, enter <your outbound delivery document number> and select Post Goods Issue. | Goods issue is successful. Inventory stock is reduced from the supplying plant. |  |

#### Check Stock in Transit

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you check the stock in transit (Consignment Stock) after goods issue is completed from the supplying DC.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launch Pad as Inventory Manager |  |  |
| 2 | Access the Application | Open Display Stock in Transit(WB5N) app. | The Display Stock in Transit app screen is displayed. |  |
| 3 | Enter Article | Enter Article and press on Run button.Article:R_6500Issuing Plant:3350Receiving Plant:3340 | Stock in Transit situation gets displayed in Tree structure on left side of the application window, where user can see the information regarding Consignment Stock and Supplying Plant and Consignment Supplier information on the right side of the application window. |  |

#### Post Goods Receipt for Outbound Delivery

|  |
| --- |
| Note This process step of posting goods receipt in store is optional here as this is also part of the scope of 5FY - In-Store Purchase Order Management. So, you can do posting of goods receipt in store while going through the scope of 5FY - In-Store Purchase Order Management. |

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you match the receipt of goods in the store to the outbound delivery you created previously.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launch Pad as a Retail Store Associate. |  |  |
| 2 | Access the Application | Open Receive Products (F1248) app.Note In case user does not have store assignment, you get pop up to navigate to assign store app. Make sure that store 3340 is assigned to store associate user in My Store Assignment (F4334) app. | The Post Goods Receipt app screen is displayed. |  |
| 3 | Enter Outbound Delivery Number | Select Enter ID.In the Find a Document pop-up <Enter Outbound Delivery Number Created earlier>Select OK. | The selected outbound delivery details are displayed. |  |
| 4 | Check and Post the Goods Receipt for Outbound Delivery | In the Product section, toggle Checked on the bottom right of the screen. Select Post. | Document item was posted successfully message is displayed. |  |

#### Check Stock Status(Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you check the stock situation (Consignment Stock) at the receiving store.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launch Pad as a Warehouse Clerk. |  |  |
| 2 | Access the Application | Open Stock-Multiple Material(F1595) app. | The Stock-Multiple Materials app screen is displayed. |  |
| 3 | Enter Article | Enter Article and press on Go button.Article:R_6500Store:3340 | Stock Situation gets displayed with Special Stock Type K and Special Stock Description ‘Supplier Consignment' . |  |

### Transfer Data to Point-of-Sale (POS)

Point-of-sale (POS) systems in the stores must be provided with the data necessary to enable selling articles to consumers, such as sales prices and article master data (including article description, tax information, and Global Trade Item Number (GTIN) for scanning).

Supply the POS with all needed master data via an initial load, for example when a new store is opened.

Automatically update the POS with the changed article data in regular intervals.

In exceptional cases, you can manually start an immediate supply of the POS, such as for short-term sales price changes.

|  |
| --- |
| Note Refer to scope item Store Connectivity – Outbound (3I2) for more details. |

### Process Point of Sales(POS) Transactions

#### Schedule Job to Set Stock Situation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to schedule a job to Set Stock situation for Consignment processing.In consignment processing the stock situation is not always clear for example there can be both unrestricted use stock and consignment stock in system. This job checks the stock situation and records it in a table at article/site level. This is needed so that system can carry out explicit stock determination while posting POS sales.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launch Pad as a Administrator (Retail). |  |  |
| 2 | Access the Application | Open Schedule Consignment Stock Situation Determination (F7736) app. | The The Schedule Consignment Stock Situation Determination app screen is displayed. |  |
| 3 | Create a Job to Schedule the Consignment Stock Situation Determination | Select Create | The New Job: Schedule POS inbound Service is displayed with three steps of input.Template SelectionScheduling OptionsParameters |  |
| 4 | Input Template | Select Job Template: Schedule Consignment Stock Situation Determination and enter a Job Name.Choose Step 2. |  |  |
| 5 | Input Scheduling Options | Enter the Job Start date and time with a recurrence pattern (for example, Daily, Monthly or Weekly).Choose Step 3. |  |  |
| 6 | Input Parameters | Enter the following parameters to schedule the job:Selection ParametersEnter the Plant, for example, 3340, for which the job must be scheduled.Select the Include Previous Period checkbox, if required.Other ParametersDisplay Application Log checkbox is selected by default. |  |  |
| 7 | Schedule Job | Choose Schedule to schedule the created job. | Schedule Job screen with Status, Log, Results, Step, Description and so on is displayed. |  |

#### Process Point-of-Sale (POS) Transactions

Business transactions originating from point-of-sale (POS) solutions in the stores are regularly transferred and trigger the posting of relevant documents.

Relevant transactions include sales. Based on this, documents for goods movements and billing are created, as well as the respective financial postings. Optionally returns, customer order payments, and pure financial transactions can also be executed.

The processed sales data are the basis for follow-on processes like replenishment.

|  |
| --- |
| NoteRefer to scope item Store Connectivity – Inbound (3HV) for more details.In case of returns in store the POS Inbound posts goods receipts to unrestricted use stock. This can result in situation in system that you have both unrestricted use stock and consignment stock.When the system has both unrestricted use stock and consignment stock, the stock situation is determined in Schedule Job to Set Stock situation. Then POS inbound carry explicit stock determination and post the goods movement. |

### Invoice Receipt from Consignment Withdrawal

#### Create Consignment settlement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The liabilities should be cleared regularly towards the supplier because of goods issues from the supplier consignment stock. The consignment goods are settled with invoice receipt.

|  |
| --- |
| Note This step can be executed after completing sales related process steps - Process Point of Sales(POS) transaction, Sales from Distribution Center, In-store Customer Order Management, Omnichannel order fulfillment for Retail. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on the SAP Fiori launchpad as Accounts Payable Accountant | Log onto the SAP Fiori launchpad as Accounts Payable Accountant . | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Create Logistics Consignment and Pipeline Settlement (MRKON) . | The Consignment and Pipeline Settlement screen displays. |  |
| 3 | Enter parameter | On the selection screen, enter the following values then choose Enter:Company Code: 3310Supplier : 33213001Material Document: （optional） Enter the material document number created from the Point of Sales(POS) TransactionConsignment: SelectedPipeline: DeselectedSettle: SelectedWithdrawals Not Settled: Selected |  |  |
| 4 | Execute | Choose Execute. | The invoice is posted. |  |
| 5 | View settlement document | On the Logistic Consignment and Pipeline Settlement screen, you can see the invoice document number under column Doc. No.. | The settlement document is created. |  |

### Return From Stores

#### Create Returns Stock Transport Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a returns stock transport order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser (Retail). |  |  |
| 2 | Access the App | Open Create Purchase Order - Advanced (ME21N) app. | The Create Purchase Order - Advanced (ME21N) screen is displayed. |  |
| 3 | Enter Parameters | Select UD2 STO Del Return from dropdown listEnter the following details:Supplying Plant: 3350Doc.Date: <Current Date>Select Org.Data tabEnter below detailsPurch. Org: 3310Purch. Group: 002Company Code: 3310 | Required parameters are defined. |  |
| 4 | Enter Parameters | Expand Item Overview sectionEnter below details:Material: R_6500PO Quantity: 2Deliv. Date: < Provide any future date>Plant: 3340 |  |  |
| 5 | Parameters that Gets Determined Automatically | In Item Overview sectionStorage Location: 994AIn Confirmatons tab in Item Details sectionConf. Control : 0004-Inbound Delivery | Parameters determined automatically. |  |
| 6 | Enter Parameters | Select Returns tab in the Header section.From the Return Reason drop down list, select 003-Product damagedFrom the Follow-Up-Activity drop down list, select 0004-Ship to Other PlantChoose Copy to Items. | Parameters are provided. |  |
| 7 | Save Return Stock Transport Order | Choose Save. | Returns Stock Transport Order xxxxxxxxxxx created.Make a note of return stock transport order number. |  |

#### Create Outbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create the outbound delivery for the returns stock transport order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Shipping Specialist. |  |  |
| 2 | Access the App | Open My Purchase Orders - Due for Delivery (VL10B) app. | Purchase Orders, Fast Display screen is displayed. |  |
| 3 | Enter Parameters | Enter below detail,CalcRuleDefltDlvCrDt: <blank>Choose Purchase Orders and enter the below detail:Purchasing Document: <Return Stock Transport Order>Choose Execute. | Activities Due for Shipping "Purchase Orders, Fast Display" screen is displayed. |  |
| 4 | Create Outbound Delivery | Select the Return Stock Transport Order entryChoose Background. | See Log for information about creating deliveries message is displayed. |  |
| 5 | Check the Outbound Delivery Number | Choose the newly created line item with the same Return Stock Order entryFrom the <!-- image omitted: unnamed -->(More) icon drop down list, select Show/Hide Delivery. | Outbound Delivery number xxxxxxxxx is displayed in the Document coloumn.Make a note of outbound delivery number. |  |

#### Perform Picking and Post Goods Issue for Outbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to pick and post goods issue for outbound delivery created previously.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Shipping Specialist. |  |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N) app. | Change Outbound Delivery (VL02N) screen is displayed. |  |
| 3 | Enter Parameters | Enter the Outbound Delivery :<Provide Outbound Delivery number>Choose Continue. | RST Outbound Dlv. xxxxxx Change: Overview screen is displayed. |  |
| 4 | Enter the Picked Quantity | Choose Picking.In the All Items section,Enter the below field as value in Deliv.Qty ,Picked Qty: <Deliv.Qty>Choose Enter. | OvrllPickStatus is displayed as C (Fully Picked). |  |
| 5 | Post Goods Issue | Choose Post Goods Issue. | Post goods issue initiated. |  |

#### Check Inbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step you can check the inbound delivery for the return stock transport order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Purchaser (Retail). |  |  |
| 2 | Access the App | Open Display Purchase Order - Advanced (ME23N) app. | Display Purchase Order - Advanced (ME23N) screen is displayed. |  |
| 3 | Access Return Purchase Order | Choose Document Overview OnFrom the Selection Variants, select Purchase Orders. | Purchasing Document screen is displayed. |  |
| 4 | Access Returns Purchase Order | In the Program Selections section, enter below details:Purchasing Document : <Returns Purchase Order>Choose Execute. | Purchase Order is displayed in the Document overview section. |  |
| 5 | Select Return Purchase Order | Double click on the Return Purchase order. | Return purchase order is displayed. |  |
| 6 | Check Returns Overview | Choose Returns Tab,Choose Returns Overview. | Returns Overview for Returns Purchase Order xxxxxxxxxx screen is displayed. |  |
| 7 | Check Inbound Delivery | Check Inbound Delivery number in Document Number Column. | Inbound delivery number xxxxxxxx displayed.Make a note of inbound delivery number. |  |

#### Perform Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process, you perform post goods receipt for inbound delivery.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as a Receiving Specialist. |  |  |
| 2 | Access the App | Open Change Inbound Delivery (VL32N) app. | Change Inbound Delivery (VL32N) screen is displayed. |  |
| 3 | Enter Inbound Delivery Number | Enter the following detail:Inbound Delivery : <Inbound Delivery Number>Choose Continue. | Change Inbound Delivery XXXXXXXXX Change: Overview screen is displayed. |  |
| 4 | Parameter that Get Determined Automatically | In Item Overview section, enter the following detail:Putaway Qty: 2 | Parameters entered. |  |
| 5 | Change Storage Location | Storage location: 995A | Storage location is changed |  |
| 6 | Post Goods Receipt | Choose Post Goods Receipt. | Goods Receipt for inbound delivery XXXXXXXX posted (Material Document xxxxxxxxxx) message is displayed. |  |

#### Check Stock Status(Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you check the stock situation (Consignment Stock) at the store and receiving distribution center.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launch Pad as a Warehouse Clerk. |  |  |
| 2 | Access the Application | Open Stock-Multiple Material(F1595) app. | The Stock-Multiple Materials app screen is displayed. |  |
| 3 | Enter Article | Enter Article and press on Go button.Article:R_6500 | Stock Situation gets displayed with Special Stock Type K and Special Stock Description ‘Supplier Consignment' . |  |

### Return to Supplier

#### Create Returns Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to formalize a return an article (Supplier Consignment article) to the supplier by creating a return purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Purchaser (Retail). |  |  |
| 2 | Access the App | Open Create Purchase Order - Advanced (ME21N) app | The Create Purchase Order - Advanced (ME21N) screen is displayed. |  |
| 3 | Enter Parameters | Select NB Purchase Order from dropdown listNote For the retail consignment process only the classic return(NB) is supported and enhance return(NB2) is not supported.Enter the following details:Supplier: 33213001/ Retail Non-Food Supplier AEDoc.Date: <Current Date>Select Org.Data tabEnter below details:Purch. Org: 3310Purch. Group: 002Company Code: 3310 | Required parameters are defined. |  |
| 4 | Enter Parameters | Expand Item Overview sectionEnter below details:Material: R_6500PO Quantity: 2Item Category: KDeliv. Date: <Provide any future date>Plant: 3350Returns Item:x |  |  |
| 5 | Parameters that Gets Determined Automatically | In the Item Overview sectionStorage Location:995ACheck for the Shipping Tab with Shipping details e.g., Sales Org, Distribution Channel, Shipping Point, Delivery Type, Loading Group, Transportation Group etc. | Parameters determined automatically. |  |
| 6 | Save Returns PO to vendor | Choose Save. | Return Purchase order xxxxxxxxxxx created.Make a note of return purchase order. |  |

#### Create Outbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step outbound delivery is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Shipping Specialist |  |  |
| 2 | Access the App | Open My Purchase Orders - Due for Delivery (VL10B) app | Purchase Orders, Fast Display screen is displayed |  |
| 3 | Enter Parameters | Enter below detail,CalcRuleDefltDlvCrDt: <blank>Choose Execute.Go to Purchase Orders tab and enter below detailPurchasing Document: Return Purchase order number created in previous step | Activities Due for Shipping "Purchase Orders, Fast Display" screen is displayed |  |
| 4 | Create Outbound Delivery | Select the Return Purchase Orderentry.Choose Background. | See Log for information about creating deliveries message is displayed. |  |
| 5 | Check the Outbound Delivery Number | Choose the newly created line item with the same Return Purchase Order entryFrom the More menu, select Show/Hide Delivery | Outbound Delivery number xxxxxxxx is displayed in the Document coloumn.Make a note of outbound delivery number. |  |

#### Pick and Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step goods are picked, and goods issue is posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Shipping Specialist |  |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N) app. | Change Outbound Delivery (VL02N) screen is displayed. |  |
| 3 | Enter Parameters | Enter the Outbound Delivery : <Provide Outbound Delivery number>Choose Continue. | RST Outbound Dlv. xxxxxx Change: Overview screen is displayed |  |
| 4 | Enter the Picked Quantity | Choose PickingIn the All Items section,Enter the below field as value in Deliv.Qty ,Picked Qty : <2>ChooseEnter | OvrllPickStatus is displayed as C (Fully Picked). |  |
| 5 | Post Goods Issue | Choose Post Goods Issue. | Post goods issue initiated. |  |

### In-Store Inventory Management

#### Look Up General Product Information

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When approached by consumers, store associates can use the Look Up Retail Products (F0431) app to get details of a product and provide a better service for their customers. For example, if a certain product is still in stock. In case required components have been implemented, store associates are able to provide real-time stock information.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
|  | Log On | Log on to the SAP Fiori launchpad as a Retail Store Associate. |  |  |
| 2 | Access App | Open the Look Up Retail Products (F0431) app. | Look Up Retail Products (F0431)screen is displayed. |  |
| 3a | Scan a product (on mobile) | Select Scan to scan the barcode using the camera on the device to view the details of the associated product.Note Only possible on mobile device with SAP/Custom SAP Fiori Client. | Product details on the Information tab are displayed. |  |
| 3b | Search a Product (on a Web Browser) | Enter R_6500 or a search term, for instance, name of the product, product GTIN, etc. in the product search and select the product from the search result list. | Product details on the Information tab are displayed for the below fields:Product IDGTINStock QuantityAvailable StockDistribution Center Stock QuantityExternally ProcuredWeightNoteAvailable Stock and Distribution Center Stock Quantity field information would be displayed on app, only if the respective settings are enabled. (Refer to the Configuration activity section of the Set-Up Instructions from scope item 3HQ(In-store Merchandise Management)).Available Stock field would display available stocks (Available-to-Promise (ATP)) in store.This includes the consignment stock for the article.Distribution Center Stock Quantity field would display the ATP stock of a product at DC and the estimated planned delivery time from the distribution center (DC) supplying to the store.Externally Procured field would contain the product’s estimated planned delivery time information from the external supplier to the store |  |

#### Review Order Proposals

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With Order Products (F0752) app, store associates can review the current order proposals or create new order proposals for products on an ad hoc basis. The app displays detailed information about the open order quantities and the available stock as well as the promotion periods and the historical sales data.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Retail Store Associate. |  |  |
| 2 | Access app | Open the Order Products (F0752) app | All order proposals for the selected store are displayed. |  |
| 3 | Search product | Search for the product R_6500 or scan the barcode of a specific product or attributes like SunglassesChoose ENTER. | The list of products is filtered according to the entered filter criteria. |  |
| 4 | Filter | Select No Filter SelectedSelect Merchandise category and search R5113003Choose OK. | The filter helps to work on a small list of products. |  |
| 5 | Show order proposal | No Filter SelectedEnter the product ID R_6500 and Choose ENTER or enter the term in the product search Sunglasses and Choose ENTER Select a product from the search result list. | The detail view of the order proposal displays the following: the proposed and actual order quantity, whether the product is currently on current, expected, and allocated stock |  |
| 6 | Change order proposal | Adapt the quantity “1" and Choose ENTER on the product details of the line item. | The product detail view of the order product displays as the quantity is changed so the order quantity edit box color is changed to Green. |  |
| 7 | Leave the app | Select the SAP icon to navigate back to home. |  |  |

### In-Store Customer Order Management

#### Sell from Store: Immediate Pickup

##### Verify Consumer Registration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process helps you to verify an existing consumer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Retail Store Associate. |  |  |
| 2 | Access the App | Open Display Customer (WDA_WSSD_CUST) app. | Display Customer (WDA_WSSD_CUST) screen is displayed. |  |
| 3 | Enter Parameters | Enter the below detail before selecting Continue:Customer: AE- 33113008 | Display Customer: <xxxxxx> screen is displayed. |  |
| 4 | Check the details | Check the Customer type of the Consumer.Check the details displayed in Address section | The details are displayed and verified. |  |

##### Create Master Data for Registering a New Consumer (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process helps you to create a new consumer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Retail Store Associate. |  |  |
| 2 | Access the App | Open Create Customer (WDA_WSSD_CUST) app. | Create Customer (WDA_WSSD_CUST) screen is displayed. |  |
| 3 | Enter Parameters | Enter below detail:From the Customer Type dropdown list, select Private Customer.Enter below details in Address section:From the Title dropdown list, select, for example, Mr.,First Name: <Enter first name>Last Name: <Enter last name>Street: <Enter Street name>House Number: <Enter house number>City: <Enter city>Postal Code: <Enter postal code>Country/Region: <Enter country>Select Save.ORFrom the Customer Type dropdown list, select Business Customer.Title: CompanyName: <Enter name>Street: <Enter Street>House Number: <Enter house number>City: <Enter city>Postal Code: <Enter postal code>Country/Reg.: <Enter country>Choose Save. | Customer with the number xxxxxxx created message is displayed.Make a note of customer number. |  |

##### Create Sales Order and Generate Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step explains how to create a sales order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Retail Store Associate. |  |  |
| 2 | Access the App | Open Manage In-Store Sales Orders (F7141) app. | Manage In-Store Sales Orders (F7141) screen is displayed. |  |
| 3 | Go to App | On the Manage In-Store Sales Orders (F7141) screen, press Create button. | Create Sales Order pop-up is displayed. |  |
| 4 | Enter Data | In Basic Data section of General Information tab view, enter:Sold-to Party: <Enter your consumer’s ID>Note Enter the sold-to-party or consumer ID of the respective consumer if already registered or newly registered.If one-time sold-to party or consumer is used, then after entering your sold-to party, go to General Information > Partners > Select your Sold-to Party and select Change Address button. Enter/change any field value in the Change Address pop-up and select Change Address button, for instance, enter E-MailShipping Conditions: 03Customer References: <Order Reference Text>In the Sales Order Items table of the Items tab view, enter the following details:Product:R_6500Requested Quantity: <Order Quantity>Item Category: <Enter Item Category>, for instance TAN (Standard Item)Note Select Settings icon, on the View Settings pop-up, select the Plant and Shipping Point checkboxes and select OK.Plant: <Enter your store>, for instance, 3340Shipping Point: 33RSChoose Enter | Details are entered successfully. |  |
| 5 | Save the Order | Select Create. | Sales order is saved and Standard Order <order number> has been created success message is displayed. |  |
| 6 | Generate Invoice | Press Generate Invoice button on the Sales Order screen. | Standard Order xxxxx has been saved message is displayed.Outbound delivery is processed with picked quantity, goods issue is posted and invoice is generated automatically. |  |
| 7 | Print Invoice (Optional) | Navigate back to the Manage In-Store Sales Orders (F7141) screen, enter Sales Order : <the sales order number created previously> and select Go.Select the resulting sales order and go to Process Flow tab and click on the Invoice, then select More Links from the Invoice Number pop-up.Select the Display Billing Documents hyperlink in the Define Link List pop-up.Go to Menu >Goto> Header> OutputSelect the output from the Output table and select Display Document. Select Print . | Invoice is previewed and printed. |  |
| 8 | Validate Follow-On Documents (Optional) | Navigate back to the Sales Orders screen and go to Process Flow tab.Select the <Relevant Follow-On Document> and , then choose More Links from the <Relevant Follow-On Document> number pop-up.Select the Display <Relevant Follow-On Document> Documents hyperlink in the Define Link List pop-up to investigate the details of the subsequent document, for example, outbound delivery, invoice documents and accounting documents. | Generated documents are displayed to investigate the details. |  |

##### Process Customer Order Payment from POS

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure you can transfer customer order payment information from a POS system to SAP S/4HANA Cloud Public Edition based on the method of payment, such as cash, cheques, payment cards, electronic cash, or electronic wallet using SOAP service.

Procedure

|  |
| --- |
| Note Refer Process Customer Order Payment from POS from this scope item. Also, customer order payment related payload should be referred to simulate the inbound payload with the aggregated information of payments for the sales took place in the Point-of-sales system. |

#### Sell from Store: Pickup at Later Date due to Stock Unavailability (Payment Done at Pickup)

##### In-Store Operations

###### Check Stock Availability in Store

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When approached by consumers, store associates can use the Look Up Retail Products (F0431) app to get details of a product’s stock availability.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Retail Store Associate. |  |  |
| 2 | Access App | Open the Look Up Retail Products (F0431) app. | The product search page is displayed. |  |
| 3 | Search a product and check the stock information | Enter R_6500 or a search term, for instance, name of the product, product GTIN, etc. in the product search and select the product from the search result list. | Product details on the Information tab are displayed for the below fields:Product IDGTINStock QuantityWeightDistribution Center Stock QuantityExternally ProcuredNoteDistribution Center Stock Quantity field would contain the product’s stock information and the estimated planned delivery time from the distribution center (DC) supplying to the store.Externally Procured field contains product estimated planned delivery time information from the external supplier to the store. |  |

###### Verify Consumer Registration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process helps you to verify an existing consumer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Retail Store Associate. |  |  |
| 2 | Access the App | Open Display Customer (WDA_WSSD_CUST) app. | Display Customer (WDA_WSSD_CUST) screen is displayed. |  |
| 3 | Enter Parameters | Enter the below detail before selecting Continue:Customer: <For AE- 10113008> | Display Customer <xxxxxx> screen is displayed. |  |
| 4 | Check the details | Check the Customer type of the ConsumerCheck the details displayed in Address section. | The details are displayed and verified. |  |

###### Create Master Data for Registering New Consumers (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process helps you to create a new consumer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Retail Store Associate. |  |  |
| 2 | Access the App | Open Create Customer (WDA0484) app. | Create Customer (WDA0484) screen is displayed. |  |
| 3 | Enter Parameters | Enter below detail:From the Customer Type dropdown list, select Private Customer.Enter below details in Address section:From the Title dropdown list, select, for example, Mr.,First Name: <Enter first name>Last Name: <Enter last name>Street: <Enter Street name>House Number: <Enter house number>City: <Enter city>Postal Code: <Enter postal code>Country/Region: <Enter country>Select Save.ORFrom the Customer Type dropdown list, select Business Customer.Title: CompanyName: <Enter name>Street: <Enter Street>House Number: <Enter house number>City: <Enter city>Postal Code: <Ener postal code>Country/Reg.: <Enter country>Choose Save. | Customer with the number xxxxxxx created message is displayed.Make a note of customer number. |  |

###### Create Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step explains how to create a sales order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Retail Store Associate. |  |  |
| 2 | Access the App | Open Manage In-Store Sales Orders (F7141) app. | Manage In-Store Sales Orders (F7141) screen is displayed. |  |
| 3 | Go to App | On the Manage In-Store Sales Orders (F7141) screen, choose Create. | Create Sales Order pop up is displayed. |  |
| 4 | Enter Data | In Basic Data section of General Information tab view, enter:Sold-to Party: <Enter your consumer’s ID>NoteEnter the sold-to-party or consumer ID of the respective consumer if already registered or newly registered.If one-time sold-to party or consumer is used, then after entering your sold-to party, go to General Information > Partners , select your Sold-to Party and select Change Address button.Enter/change any field value in the Change Address pop-up and select Change Address button, for instance, enter E-Mail.Shipping Conditions: 02Customer References: <Order Reference Text>In the Sales Order Items table of the Items tab view, enter the following details:Product : R_6500Requested Quantity: <Order Quantity>Item Category : <Enter Item Category>, for instance CBAB (Bought-In Item).Note Select Settings icon, on the View Settings pop-up, select the Plant and Shipping Point checkboxes and select OK.Plant: <Enter your store>, for instance, 3340.Shipping Point: 99CCChoose Enter.Select the item to navigate to its details. Go to Delivery > Schedule Lines and enter the following and select Apply:Sched. Line Category: <Enter Schedule Line Category>, for instance, CU(IndivStockTransfOrd)Note Only the procurement from Distribution Center is supported for consignment and so only the schedule line category CU can be entered. | Details are entered successfully. |  |
| 5 | Save the Order | Select Create. | Sales order is saved and Standard Order <order number > has been created success message is displayed. |  |
| 6 | Display Sales Order Item Details | On the Sales Order screen, in the Sales Order Items table of the Items tab, select an item to navigate to its details. | Sales Order Itemscreen is displayed. |  |
| 7 | Note the Purchase Requisition Number per Sales Order Item. | Go to Delivery > Schedule LinesNote Select Settings icon, on the Add/Remove Columns pop-up, select the Purchase Requisition checkbox and select OK. Switch to Show Details view.Make a note of the purchase requisition number for all the sales order items. |  |  |

###### Print Sales Order Document (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step explains how to trigger print for a sales order document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Retail Store Associate . |  |  |
| 2 | Access the App | Open Manage In-Store Sales Orders (F7141) app. | Manage In-Store Sales Orders (F7141) screen is displayed. |  |
| 3 | Go to App | On the Manage In-Store Sales Orders (F7141) screen, enter Sales Order :<the sales order number created previously> and select Go. | Resulting sales order is displayed in the Sales Orders table. |  |
| 4 | Open the order details & Trigger print | Select the resulting sales order and go to Output Items tab.Click on Open File hyperlink and select Print on the document preview pop-up. | Sales order document printing is triggered. |  |

##### Back-Office Operations from Distribution Center to Store

###### Transfer Stock

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step explains move consignment stock of distribution center (DC) to sales order stock of DC.

|  |
| --- |
| Note In this process step, the withdrawal of consignment stock takes place when the consignment stock is transferred to sales order stock of distribution center. The system generates consignment settlement invoice based on the material document posted in the step. In case, the sales order is cancelled the stock will remain in the ownership of retailer. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. |  |  |
| 2 | Access the App | Open Post Transfer Posting (MIGO_TR) app. | The Transfer Posting Other screen is displayed. |  |
| 3 | Input Movement Type | On the Transfer Posting Other screen , enter: |  |  |
| 4 | Enter Material | In the Transfer Posting tab, make the following entries in the From section and select Enter:Material: R_6500Plant: 3350Location: 995AIn the Transfer Posting tab, make the following entries in the Dest section and select Enter:Location: 995AAlso, enter the following:Sales Order Number: <your sales order number created above in chapter [Create Sales Order](#unique_47) [page ] 76 of this document>Sales Order Item: <your sales order item>Qty in UnE: <material quantity to be transferred>, for instance, 1 PCNote Select Next Item icon to enter details for multiple items before posting.On the Where tab enter following:Movement Type: 413KVendor:33213001 |  |  |
| 5 | Save Your Entries | Select Post. | Material document <document number> posted success message is displayed. |  |

###### Schedule Application Job to Create Stock Transport Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process the stock transport requisition is automatically converted to a stock transport order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser (Retail). |  |  |
| 2 | Access the App | Navigate toSchedule Purchasing Jobs - Advanced (F1702) app | Schedule Purchasing Jobs - Advanced (F1702) screen is displayed. |  |
| 3 | Create new job | Choose Create to create a new application job | New Job: Automatic creation of Purchase Orders from Requisitions screen is displayed |  |
| 4 | Enter job details | Enter the application job details in the Template Selection and Scheduling Options sections.Job Template: Automatic creation of Purchase Orders from RequisitionJob Name: Automatic creation of Purchase Orders from RequisitionChoose Step 2Flag Start ImmediatelyChoose Define Recurrence Pattern if required to change the Recurrence. | The Template selection and scheduling options are defined |  |
| 5 | Enter the Parameters | Choose Step 3In the Parameter section,Flag Per Requisition in New Purchase Order sectionMake the following entries in Item Specific Selection section (For Testing Purpose)Purchase Requisition : <Enter your stock transport requisition number created> in chapter [Create Sales Order](#unique_47) [page ] 76. | Parameters are entered |  |
| 6 | Check | Choose Check | Message is displayed indicating you can go ahead and schedule job. |  |
| 7 | Schedule | Choose Schedule | Automatic creation of Purchase Order from Requisition has been scheduledThe Application Jobs screen is displayed again, and the new job is displayed in the Jobs table |  |
| 8 | Navigate to Results | Check the newly create job row and choose the icon Navigate to the job Results in Results column. | Document (ID XXXXXXX) screen displays stock transport order number. |  |

###### Create Stock Transport Order (Optional)

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser (Retail). | The Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Create Purchase Order - Advanced (ME21N). | Create Purchase Order - Advanced (ME21N) screen displays. |  |
| 3 | Enter Purchase Order Document Type | Enter the following data:Order Type: UD (StockTranspOrderDel)Then choose Enter. |  |  |
| 4 | Enter Purchase Order Data | Enter the following data:Supplying Plant: 3350On the Org. Data tab:Purchasing Org.: 3310Purchasing Group: 001Company Code: 3310In the area of Overview Item:Purchase Requisition: <Enter your stock transport requisition number created in[Create Sales Order](#unique_47) [page ] 76>Quantity: xThen choose Enter.Note Price should be determined automatically from purchasing info record | All data are entered, the item detail screen displays. |  |
| 5 | Save Stock Transport Order | Choose Save and when the stock transport order number is displayed, write it down for further use. | A new stock transport order is created. Stock transport order Number is displayed. |  |

###### Schedule Application Job to Create Replenishment Delivery for STO

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to schedule a background job for creating outbound deliveries.

This app can be used as an alternative instead of the manual creation of outbound deliveries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Delivery Creation (F2228). | The Application Jobs screen displays. The app automatically shows the history of application jobs. |  |
| 3 | Create Delivery Creation Schedule | Choose Create to define a new job. | The New Job screen is displayed. The Job Template should be defaulted as Schedule Delivery Creation for Purchase Order. |  |
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary, then choose Check. | The system displays the message Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A delivery creation job is scheduled. Screen goes back to Application Jobs. |  |
| 6 | Check Delivery Creation Job Log | On the Application Jobs screen, after job item’s status turned to Finish, choose Status symbol in the Log column.Note Choose the Magnifier, and the job list will refresh. | The job log details displays. |  |

###### Pick, Pack, and Post Goods Issue for Replenishment Delivery from DC

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you pick materials and to post issue of goods in order to remove the stock from the inventory management system of the DC.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access App | Open Change Outbound Delivery (VL02N) app. | Change Outbound Delivery (VL02N) app screen is displayed. |  |
| 3 | Open Outbound Delivery document | On the Change Outbound Delivery (VL02N) app screen, enter <your outbound delivery document number> and choose Continue. |  |  |
| 4 | Specify picked quantity | Go to Picking tab and specify: Picked Qty : <Enter quantity equal to delivery quantity> | Picked quantity is updated. |  |
| 5 | Save the Outbound Delivery document | Select Save. | Outbound Delivery Document is saved. |  |
| 6 | Post Goods Issue | On the Change Outbound Delivery (VL02N) app screen, enter <your outbound delivery document number> and choose Post Goods Issue. | Goods issue is successful. Inventory stock is reduced from the supplying plant. |  |

##### In-Store Operations

###### Post Goods Receipt for STO/Outbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you post receipt of goods in store against the earlier created stock transfer order or outbound delivery, purchase order or inbound delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launch Pad as a Retail Store Associate. |  |  |
| 2 | Access the application | Open Receive Products (F1248) app. | The Receive Products (F1248) screen is displayed. |  |
| 3 | Enter Document Number | Select Enter IDIn the Find a Document pop-up <Enter STO/ Outbound Delivery/PO/Inbound Delivery Number Created earlier>Select OK. | The selected document details are displayed. |  |
| 4 | Check and Post the Goods Receipt | In the Products section, toggle Checked and Delivery Completed. Select Post. | Document item was posted successfully message is displayed |  |
| 5 | Navigate to Process Picking Requests (F4643) app | Navigate to Process Picking Requests (F4643) app. Select Show Actions on the bottom right of the Receive Products (F1248) screen. Select Process Picking Requests. | Navigation to the Process Picking Requests (F4643) screen is successful, with order number and respective picking request details shown, whose receipt has been posted. |  |

###### Start Picking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step explains how to start picking of products on the shop floor.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launch Pad as a Retail Store Associate. |  |  |
| 2 | Access the Application | Open Process Picking Requests (F4643) app. | The Process Picking Requests (F4643) screen is displayed. |  |
| 3 | Select Picking Requests and Start Picking | Select picking requests in one of the following ways:Picking requests are queued in ascending order of their date of creation.To start picking the requests which came in first, select the checkboxes against the picking request numbers from the top of the list.If picking request of a particular status must be picked, for instance, picking requests with status Picking in Process or Not Picked. Select FilterSet the filter based on Status in the Select Filter pop- up,then select the resulting picking requests.If sales order number, Customer Reference or Your Reference for Sold-to Party maintained in the sales order is known then, enter either of these in the search field and select Search, then select the resulting picking requests.Label printing is applicable only when multiple picking requests are selected for picking process.After selecting the picking request, select Start Picking. | The Process Picking Requests (F4643) app will be redirected to the next page. Label printing for the selected picking request is triggered.List of products belonging to selected picking request is displayed with details like quantity and product GTIN. Products Picked indicator will be displayed on the left top.Note Label printing is applicable when multiple picking requests are selected for picking process. |  |
| 4 | Scan Product GTIN | Choose Scan GTIN on the bottom of the screen and scan using the camera on the device. | Details and quantity to be placed in the respective picking request container, is shown of the scanned product. If wrong GTIN is entered then Scanned product not found error message will be thrown to the user.Note App is handled to scan any of the products available in the picking request, it is not mandatory to scan in the sequence of the list of products. |  |
| 5 | Enter Quantity of Product | Enter product quantity based on the following cases:Case 1: For product which has a unit of measure (UoM) for which quantities can be in decimal, for example, if UoM in L(Litre), KG (Kilogram), and so on.Choose Scan Bar Code on the bottom of the screen and scan product barcode using the camera on the device or manually enter product barcode number in the Enter Bar Code pop-up and choose OK.NoteProduct Bar Code is product GTIN number (13 digits) plus weight of product(5 digits) , for instance, the barcode should be as follows to recognise decimal/whole quantities of a product: <GTIN> + 10000 = 100.00 kg <GTIN> + 00100 = 1.00 kg <GTIN> + 01000 = 10.00 kg<GTIN> + 00150 = 1.5 kg <GTIN> + 00050 = 0.50 kgThat is, if the product GTIN is ‘2150500000000’ and the weight/quantity to be picked is ‘1.5’, then the barcode is ‘215050000000000150’.Case 2: For product which has a unit of measure (UoM) for which quantities can only be whole, for example, if UoM in EA(Each), PC(Piece), and so on.Enter the quantity manually or use - and + to decrease/increase the quantity in Picked Qty in Base UoM column. | Case 1: The Picked Qty in Base UoM and Price column values are updated.Case 2: Picked quantity is entered for the product.Note Case 1: If you enter a wrong barcode then system is displayed You have not scanned GTIN of Requested product error message.Case 2: Ordered quantity is the maximum allowed quantity that can be entered while the minimum allowed is zero.If picked quantity is lesser (lesser than the lower tolerance limit) than the ordered quantity, then R3 Out of Stock will be set as Rejection Reason for Short Picking, for the corresponding sales order item in the background. |  |
| 6 | Scan Picking Request | Select Scan Picking Request (if multiple picking requests are selected for picking) at the bottom right of the screen and scan the picking request barcode on the box label using the camera on the device or manually enter the picking request barcode number in the Enter Bar Code pop-up and choose OK. orSelect OK (if single picking request is selected for picking) at the bottom right of the screen. | Picking request number is scanned. If wrong picking request number is entered, then Scanned picking request not found error message is displayed to userNote If a product must be placed into different picking containers, then the user is asked to scan and place the respective quantity of product into their corresponding picking container one after the other. |  |
| 7 | Finish Picking by Assigning Picking Container to Handover Shelf | Note Before following this process step, the configuration activity Define Customizing Schema for Store Picking Requests, Customizing Schema - 0001 has Is Standard checkbox marked, that is., Customizing Schema – 0001 is the default schema which is not assigned to any store and even no other schema is assigned to your store.To assign and place the picking container to a handover shelf after picking is complete and orders are ready to be handed over to the customer:Scan all items in the picking request.Select Print Content List on the bottom right of the screen. On the Reprint Content List pop-up select the picking request for which content list must be reprinted and then choose Reprint.Following are the two scenarios based on which handover shelf is assigned on the Handover Shelf screen:Scenario 1: If single picking request is selected:Select the picking request to which handover shelf is to be assignedOn the Information pop-up choose Scan and scan the handover shelf barcode using camera in the device or enter the barcode manually in the Enter Bar Code pop-up and choose OK.Scenario 2: If multiple requests are selected:Select Scan Picking Request at the bottom of the screen and scan the picking request number using the camera in the device.On the Information pop-up choose Scan and scan the handover shelf barcode using camera in the device or enter the barcode manually in the Enter Bar Code pop-up and choose OK.Select Pick MoreAll Done on the success pop-up if picking of all requests is completed. | Once all the products in picking request are scanned and placed in a picking container, Products PickedAfter the last product of the products list is scanned and placed in the picking container, the message pop-up Content list have been printed for picking requests is displayed.Note If products belonging to a picking request is completely unavailable, then that picking request is not shown on the Handover Shelf screen. Also, the content list is not printed for that picking request.Reprint of content list is triggered for the selected picking request.Handover shelf is assigned to all the picking requests.Success message You have placed all picked products in the handover shelf is displayedYou are navigated back to the Picking Requests screen to select and start picking of new requests, if Pick More is selected Or,You are navigated back to the SAP Fiori launchpad if All Done is selected. |  |

###### Verify Consumer Order Details and Hand Over

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to look inspect the details of any order which is ready to be handed over to the customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Retail Store Associate. |  |  |
| 2 | Access App | Open Hand Over Orders (F4639) app. | Hand Over Orders (F4639) app screen displays along with a list of orders ready to be handed over. |  |
| 3 | Verify Consumer Order Details | Verification of consumer orders is done by following stepsEnter dataFollowing are the different ways in which an order can be searched using this app:Enter the sales order number, Customer Reference or Your Reference for Sold-to-Party maintained in the sales order, either of these in Search above the order list and press Enter.Or,Select Scan Order and scan the order bar-code using the camera on the device.Filter Orders (Optional)Select Filter and select the desired Picking Request Status or Payment Status filter(s) on the Select Filter pop-up and choose OKCheck the details of the orderSelect the order item to look over its exceptions and other details. | The order list returns a line item of the order searched along with the details such as customer name, date and time of order pick-up by customer, order status, and payment status.The order list displays the filtered list of orders based on the Picking Request Status or Payment Status filter set by the user. The following filter values are displayed under Picking Request Status filter:On TrackPicking in ProgressPicking Request CreatedOrder due for CancellationHanded OverReservation Handed OverReturned to ShelfProduct UnavailableThe following filter values are displayed under Payment Status filter:PaidNot PaidOrder navigates to the Exceptions tab view which displays the details of the exception(s) in the order (short picked, substituted, or unavailable products), switching the tab to Product Details, displays the details of the fully picked products.Apart from exception and product details, the details of the order are displayed in the header. |  |
| 4 | Cancel Product (Optional) | To cancel any product, you can do the following:Select X button against the product in the Requested Product column.Choose OK on the Confirmation pop-up to cancel or reject the product. | Product is canceled message is displayed and the product line item is removed on cancellation. |  |
| 5 | Scan the Picking Request to Withdraw | Note Before following this process step, the configuration activity Define Customizing Schema for Store Picking Requests, Customizing Schema - 0001 has Is Standard checkbox marked, that is., Customizing Schema – 0001 is the default schema which is not assigned to any store also no other schema is assigned to your store.To withdraw the picking request, follow the steps:Select Handover Status on the top right of the screen.Note Reservation Hand Over (in case of unpaid orders) and Cancel Order buttons on the bottom of the screen are enabled once the entire order is withdrawn.Select Scan Picking Request on the top right corner of the Handover Status pop-over and scan the picking request bar-code of the order placed in the mentioned handover shelf space using the camera on the device or manually enter the picking request barcode number in the Enter Bar Code pop-up and choose OK and finally select Done. | Handover Status pop-over screen is displayed containing the list of Picking Request, Picking Request Status their corresponding Handover Shelf Space numbers and the Withdraw hyperlink.The picking request is withdrawn from the handover shelf space or bin, the hyperlink text changes to Withdrawn and the user is navigated back to the Exceptions tab view. |  |
| 6 | Hand Over Orders | Select Reservation Hand Over and select Yes on the Confirmation pop-up.Note Reservation Hand Over should be active only for Not Paid orders with picking request status On Track or Order Due for Cancellation. | A confirmation message Reservation handover processed is displayed on the screen. Order status changes to Reservation Handed Over and the user is navigated back to the order list screen.Now, the customer is expected to pay at POS. |  |

|  |
| --- |
| Note You can also skip assignment of picking container to handover shelf. For more information, see appendix of test script of scope item 3HU. |

###### Validate Follow-On Documents and Print Billing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows how to validate the subsequent documents generated after order sales in store and print billing document

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Retail Store Associate |  |  |
| 2 | Access the App | Open Manage In-Store Sales Orders (F7141) app. | Manage In-Store Sales Orders (F7141) screen is displayed. |  |
| 3 | Go to App | On the Manage In-Store Sales Orders (F7141) screen, enter Sales Order : <the sales order number created previously> and choose Go. | Resulting sales order is displayed in the Sales Orders table. |  |
| 4 | Validate Follow-On Documents | Select the resulting sales order and go to Process Flow tab, select the <Relevant Follow-On Document>, and choose More Links from the <Relevant Follow-On Document> number pop-up.Select the Display <Relevant Follow-On Document> Documents hyperlink in the Define Link List pop-up to investigate the details of the subsequent document, for example, outbound delivery, invoice documents and accounting documents. | Generated documents are displayed to investigate the details. |  |
| 5 | Print Invoice | Navigate back to the Sales Orders screen and go to Process Flow tab and click on the Invoice, then select More Links from the Invoice Number pop-up.Select the Display Billing Documents hyperlink in the Define Link List pop-up.Go to Menu > Goto > Header > OutputSelect the output from the Output table and select Display Document. Select Print | Invoice is previewed and printed |  |

### Omnichannel Order Fulfillment for Retail

#### Click and Reserve - Order Fulfillment in Store (Stock is Available in the Store)

##### Create Sales Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To execute this scope item, you must have sales orders which in turn creates store pick-up orders and picking requests based on the configurable split criteria.

|  |
| --- |
| Note This process step is intended to be executed to simulate sales orders in SAP S/4HANA Cloud Public Edition system. In real time, sales order creation would be triggered using an inbound service integration arrangement of the third-party web-shop with the SAP S/4HANA Cloud Public Edition system. |

Prerequisite

In order to test the scenario Click and Reserve- Order Fulfillment in Store (Stock is Available in the Store), see [Extend Article to E-commerce Channel](#unique_11) [page ] 13.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Log onto the SAP Fiori Launchpad as an Retail Store Associate. |  |  |
| 2. | Access the App | Open Manage Sales Orders (F1873) app. | Manage Sales Orders (F1873) screen is displayed. |  |
| 3 | Go to App | On the Manage Sales Order screen, select Create > Create Sales Order - VA01 option. | Create Sales Documents screen is displayed. |  |
| 4 | Enter data | Enter the following data:Order Type: ORSales Organization: 3310Distribution Channel: 60Division: 00Choose Continue. | Create Standard Order: Overview screen is displayed |  |
| 5 | Enter Header Data | In the header section, enter Sold-to Party: 33113005 and press EnterNow, in the Address From Master Data for Sold-to Party (Document Header) pop-up, enter <Name> in the Name section and <Telephone number> under the Communication section, then press EnterAlso enter Customer References: <Reference Document ID>, for instance, Customer PO number.Note Leave as blank if no reference needs to be maintained.Choose Menu > Goto > Header > ShippingShipping: 02 Pick-up |  |  |
| 6 | Enter Item Data | Choose Back to navigate back to the Create Standard Order: Overview screen.In the All Items table, enter the following details in different rows:Row 1:Material: R_6500Order Quantity: <Order Quantity>Item Category :<TAN>Store: 3340 |  |  |
| 7 | Save the Order | Choose Save.Note the order number for further use. | Sales order is saved and Standard Order <order number> has been saved success message is displayed. |  |

##### Start Picking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The step explains the process of initiating product picking in a store.Picking process involves single picking request or multiple picking requests. For an optimized picking experience, the list page sorts the oldest picking request first and then the picking request which got recently created and so on. In case of a short picked scenario, you have an option to substitute the original product with a substitute product to fulfill the short fall in ordered quantity.You can also print box labels and content lists during the picking process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Retail Store Associate. |  |  |
| 2 | Access App | Open Process Picking Requests (F4643) app. | Process Picking Requests (F4643) app screen is displayed along with a list of picking requests |  |
| 3 | Select Picking Requests and Start Picking | Select picking requests in one of the following ways:Picking requests are queued in ascending order of their date of creation.To start picking the requests which came in first, select the checkboxes against the picking request numbers from the top of the list.If picking request of a particular status must be picked, for instance, picking requests with status Picking in Process or Not Picked. Select FilterSet the filter based on Status in the Select Filter pop- up,then select the resulting picking requests.If sales order number is known then enter sales order number in the search field and select Search, then select the resulting picking requests.Label printing is applicable only when multiple picking requests are selected for picking process.After selecting the picking request, select Start Picking. | The Process Picking Requests (F4643) app will be redirected to the next page. Label printing for the selected picking request is triggered when picking is for multiple picking requests.List of products belonging to selected picking request is displayed with details like quantity and product GTIN. Products Picked indicator will be displayed on the left top.Note Label printing is applicable only when multiple picking requests are selected for picking process. |  |
| 4 | Print (or Re-print) Box Label Manually (Optional) | Select Print at the bottom of the screen.Select the checkbox against the picking request numbers for which box labels must be reprinted.Select Reprint on the Reprint Labels pop-up. | Re-print is triggered for the selected picking request. |  |
| 5 | Scan Product GTIN | Choose Scan GTIN on the bottom of the screen and scan using the camera on the device | Details and quantity to be placed in the respective picking request container is shown of the scanned product. If wrong GTIN is entered then Scanned product not found error message will be thrown to the user.Note App is handled to scan any of the products available in the picking request, it is not mandatory to scan in the sequence of the list of products. |  |
| 6 | Enter Quantity of Product | Enter product quantity based on the following cases:Case 1: For product which has a unit of measure (UoM) for which quantities can be in decimal, for example, if UoM in L(Litre), KG (Kilogram), etc. Choose Scan Bar Code on the bottom of the screen and scan product barcode using the camera on the device or manually enter product barcode number in the Enter Bar Code pop-up and choose OK.Note Product Bar Code is product GTIN number(13 Digits ) plus weight of product(5 Digits) , for instance, the barcode should be as follows to recognise decimal/whole quantities of a product:<GTIN> + 10000 = 100.00 kg <GTIN> + 00100 = 1.00 kg <GTIN> + 01000 = 10.00 kg<GTIN> + 00150 = 1.5 kg <GTIN> + 00050 = 0.50 kgThat is, if the product GTIN is ‘2150500000000’ and the weight/quantity to be picked is ‘1.5’, then the barcode would be ‘215050000000000150’.Case 2: For product which has a unit of measure (UoM) for which quantities can only be whole, for example, if UoM in EA (Each), PC (Piece), and so on.Enter the quantity manually or use - and + to decrease/increase the quantity in Picked Qty in Base UoM column. | Case 1: The Picked Qty in Base UoM and Price column values are updated.Case 2: Picked quantity is entered for the product.Note Case 1: If you enter a wrong barcode then system displays You have not scanned GTIN of Requested product error message.Case 2: Ordered quantity is the maximum allowed quantity that can be entered while the minimum allowed is zero.If picked quantity is lesser (lesser than the lower tolerance limit) than the ordered quantity, then R 3 Out of Stock will be set as Rejection Reason for Short Picking, for the corresponding sales order item in the background. |  |
| 7 | Scan Picking Request | To scan picking request while placing the products in their respective picking container, select Scan Picking Request (if multiple picking requests are selected for picking) at the bottom right of the screen and scan the picking request barcode on the box label using the camera on the device or manually enter the picking request barcode number in the Enter Bar Code pop-up and choose OK. orSelect OK (if single picking request is selected for picking) at the bottom right of the screen. | Picking request number is scanned. If wrong picking request number is entered, then Scanned picking request not found error message is displayed to user.Note If a product must be placed into different picking containers, then the user is asked to scan and place the respective quantity of product into their corresponding picking container one after the other. |  |
| 8 | Substitute a Product (Optional) | Select Out of Stock at the bottom right of the screen.Select Substitute on the Confirmation pop-up. Scan substitute product GTIN using the camera on the device.To scan a picking request, refer to step . | Substitute product is shown in the product list along with a Substitute Product tag and details of the ordered product in the header.Note When the substitute product GTIN is scanned, app is handled to validate that the substitute has the same unit of measure (UoM) and it belongs to the same product group as that of the ordered product.In case of partial fulfilment of requested product (when partial quantity of the ordered product is in stock and is picked), the confirmation pop-up will come up to ask to substitute the requested product with substitutes. |  |
| 9 | Post Unavailability of a Product (Optional) | Select Out of Stock at the bottom right of the screen.Select Unavailable on the Confirmation pop up. | Product removed from picking requests message is displayed and the product is posted with a zero quantity in the system.Note If the unavailable product belongs to multiple picking requests, then zero will be posted for all the picking requests. |  |
| 10 | Finish Picking by Assigning Picking Container to Handover Shelf | To assign and place the picking container to a handover shelf after picking is complete and orders are ready to be handed over to the customer:Scan all items in the picking requestSelect Print Content List on the bottom right of the screen. On the Reprint Content List pop-up select the picking request for which content list must be reprinted and then choose Reprint.Following are the two scenarios based on which handover shelf is assigned on the Handover Shelf screen:Scenario 1: If single picking request is selected:Select the picking request to which handover shelf is to be assignedOn the Information pop-up choose Scan and scan the handover shelf barcode using camera in the device or enter the barcode manually in the Enter Bar Code pop-up and choose OK.Scenario 2: If multiple requests are selected:Select Scan Picking Request at the bottom of the screen and scan the picking request number using the camera in the device or enter the barcode manually in the Enter Bar Code pop-up and choose OK.On the Information pop up choose Scan and scan the handover shelf barcode using camera in the device or enter the barcode manually in the Enter Bar Code pop-up and choose OK.Select Pick More on the success pop up to pick more requests. Or Select All Done on the success pop up if picking of all requests is completed. | Once all the products in picking request are scanned and placed in a picking container, Products Picked indicator is updated and progressed to full. Product list is also updated.After the last product of the products list is scanned and placed in the picking container, the message pop-up Content list have been printed for picking requests is displayed.Note If products belonging to a picking request is completely unavailable, then that picking request is not shown on the Handover Shelf screen. Also, the content list is not printed for that picking request.Reprint of content list is triggered for the selected picking request.Handover shelf is assigned to all the picking requests.Success message You have placed all picked products in the handover shelf is displayed.You are navigated back to the Picking Requests screen to select and start picking of new requests, if Pick More is selected.Or,You are navigated back to the SAP Fiori launchpad if All Done is selected. |  |

##### Look Over the Order Details for Handover

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to look inspect the details of any order which is ready to be handed over to the customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Retail Store Associate. |  |  |
| 2 | Access App | Open Hand Over Orders (F4639) app. | Hand Over Orders (F4639) app screen is displayed along with a list of orders ready to be handed over. |  |
| 3 | Enter Data | Following are the different ways in which an order can be searched using this app:Enter the sales order number, Customer Reference or Your Reference for Sold-to Party maintained in the sales order, either of these in Search above the order list and press Enter .OrSelect Scan Order and scan the order bar-code using the camera on the device or manually enter the picking request barcode number in the Enter Bar Code pop-up and choose OK. | The order list returns a line item of the order searched along with the details such as customer name, date and time of order pick-up by customer, order status, and payment status. |  |
| 4 | Filter Orders (Optional) | Select Filter and select the desired Picking Request Status or Payment Status filter(s) on the Select Filter pop-up and choose OK | The order list is displayed the filtered list of orders based on the Picking Request Status or Payment Status filter set by the user. The following filter values are displayed under Picking Request Status filter:On TrackPicking in ProgressPicking Request CreatedOrder due for CancellationHanded OverReservation Handed OverReturned to ShelfProduct UnavailableThe following filter values are displayed under Payment Status filter:PaidNot Paid |  |
| 5 | Check the details of the order | Select the order item to look over its exceptions and other details. | Order navigates to the Exceptions tab view which displays the details of the exception(s) in the order (short picked, substituted, or unavailable products), switching the tab to Product Details, displays the details of the fully picked products.Apart from exception and product details, the details of the order are displayed in the header. |  |
| 6 | Navigate for further product details (Optional) | Select the <product description hyper link> on either the Exceptions or Product Details screen.Select Back button to navigate back to the Hand Over Orders (F4639) app. | You navigate back to Hand Over Orders (F4639) app. |  |
| 7 | Cancel original or substituted product (Optional) | To cancel/reject the substituted product on the customer request:Select X button against the product in the Requested Product column.Note The substituted product is displayed along with the requested product for which substitution has been made.Choose OK on the Confirmation pop-up to cancel or reject the original or substituted product. | Product is canceled message is displayed and the original or substituted product line item is removed. |  |
| 8 | Scan the Picking Request to Withdraw | Select Handover Status on the top right of the screen.Note Hand Over (in case of paid orders), Reservation Hand Over (in case of unpaid orders) and Cancel Order buttons on the bottom of the screen are enabled once the entire order is withdrawn.Select Scan Picking Request on the top right corner of the Handover Status pop-over and scan the picking request bar-code of the order placed in the mentioned handover shelf space using the camera on the device or manually enter the picking request barcode number in the Enter Bar Code pop-up and choose OK and finally select Done | Handover Status pop-over screen is displayed containing the list of Picking Request, Picking Request Status their corresponding Handover Shelf Space numbers and the Withdraw hyperlink.The picking request is withdrawn from the handover shelf space or bin, the hyperlink text changes to Withdrawn and the user is navigated back to the Exceptions tab view. |  |
| 9 | Hand Over Orders | Select Reservation Hand Over on the Hand Over Orders screenNote Reservation Hand Over should be active only for Not Paid orders with picking request status On Track or Order Due for Cancellation. | A confirmation message Reservation Hand Over is processed is displayed on the screen. Order status changes to Reservation Handed Over and the user is navigated back to the order list screen. |  |

##### Validate Sales Order Document and Subsequent Document Flow (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows how to validate the updates on the sales order also the subsequent documents generated after order sales in store.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Retail Store Associate. |  |  |
| 2 | Access the App | Open Manage Sales Orders (F1873) app. | Manage Sales Orders (F1873) screen is displayed. |  |
| 3 | Go to App | On the Manage Sales Orders (F1873) screen, enter <your sales order number> in the Sales Order field. Select Go | Sales order line item is displayed in the search result. |  |
| 4 | Open the order details | Select the sales order line item. | Display Standard Order XXXXX: Overview screen is displayed. |  |
| 5 | Navigate to Document Flow | Select Display Document Flow, to investigate the details of the subsequent document, for example, outbound delivery, goods issue, invoice documents, material and accounting documents, select the document and choose Display Document. | Generated documents are displayed on the Document Flow screen. Further, selected documents are displayed to investigate the details. |  |

##### Process Customer Order Payment from POS

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure you can transfer customer order payment information from a POS system to SAP S/4HANA based on the method of payment, such as cash, cheques, payment cards, electronic cash, or electronic wallet using SOAP service.

Procedure

|  |
| --- |
| Note Refer Process Customer Order Payment from POS from scope item Store Connectivity – Inbound (3HV). Also, customer order payment related payload should be referred to simulate the inbound payload with the aggregated information of payments for the sales took place in the Point-of-sales system. |

#### Click and Collect (Pre-Paid Order)- Order Fulfillment from Distribution Center to Store (Stock is Not Available in the Store)

##### Create Sales Order

To execute this scope item, you must have sales orders which in turn creates store pick-up orders and picking requests based on the configurable split criteria.

|  |
| --- |
| Note This process step is intended to be executed to simulate sales orders in SAP S/4HANA Cloud Public Edition system. In real time, sales order creation would be triggered via an inbound service integration arrangement of the Third-Party Web-Shop with the SAP S/4HANA Cloud Public Edition system. |

Prerequisite

In order to test the scenario Click and Reserve- Order Fulfillment in Store (Stock is Available in the Store), see [Extend Article to E-commerce Channel](#unique_11) [page ] 13.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Log onto the SAP Fiori Launchpad as an Retail Store Associate. |  |  |
| 2. | Access the App | Open Manage Sales Orders (F1873) app. | Manage Sales Orders (F1873) screen is displayed. |  |
| 3 | Go to App | On the Manage Sales Order screen, select Create > Create Sales Order - VA01 option. | Create Sales Order pop-up is displayed. |  |
| 3. | Enter data | Enter the following data:Order Type: ORSales Organization: 3310Distribution Channel: 60Division: 00Choose Continue. | Create Standard Order: Overview screen is displayed |  |
| 4. | Enter Header Data | In the header section, enter Sold-to Party: 33113005 and press EnterNow, in the Address From Master Data for Sold-to Party (Document Header) pop-up, enter <Name> in the Name section and <Telephone number> under the Communication section, then press EnterAlso enter Customer References:<Reference Document ID>, for instance, Customer PO number.Note Leave as blank if no reference needs to be maintained.Choose Menu > Goto > Header > Shipping and enter Shipping : 02 Pick-up |  |  |
| 5 | Enter Item Data | Select Back button to navigate back to the Create Standard Order: Overview screenIn the All Items table, enter the following details in two different rows:Row 1:Material: R_6500Order Quantity: <Order Quantity>Item Category: CBABPlant: 3340Press Enter.Select the item then select Menu > Goto > Item > Schedule Linesand enter Sched. Line Cat.: CU.Press Enter.On the Standard Order: Purchase Order Scheduling screen, select Copy button in the Dely proposal section. |  |  |
| 6 | Navigate to Header Data | In the header section, select Display Header Details icon. | Create Standard Order: Header Data screen is displayed. |  |
| 7 | Assign Payment Card | Navigate to Electronic Payments tab, select Assign Payment Card button. | Payment Page is displayed in a new browser tab. |  |
| 8 | Enter Payment Card details | Enter the following information on the Payment Page browser tab:Credit Card Type: VISACard Number 4111111111111111Name on Card : <Enter card holder's name>Valid To : <Any Valid Future Month and Year >CVC: 111Select Submit then select Close on the Your payment card was successfully registered message Navigate back to the Create Standard Order: Header Data screen and select Confirm on the Assign Payment Card pop-up | Payment Card is added, and its details are displayed in the Electronic Payments table. |  |
| 9 | Save the Order | Select Save.Note the order number for further use. | Sales order is saved and Standard Order <order number> has been saved success message is displayed. |  |
| 10 | Note the Purchase Requisition Number per Sales Order Item | Go to Delivery > Schedule LinesNote Select Settings icon, on the Add/Remove Columns pop-up, select the Purchase Requisition checkbox and select OK. Switch to Show Details view.Make a note of the purchase requisition number for all the sales order items. |  |  |

##### Back-Office Operations from Distribution Centre to Store

###### Transfer Stock

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step explains move consignment stock of distribution center (DC) to sales order stock of DC.

|  |
| --- |
| Note In this process step, the withdrawal of consignment stock takes place when the consignment stock is transferred to sales order stock of distribution center. The system generates consignment settlement invoice based on the material document posted in the step. In case, the sales order is cancelled the stock will remain in the ownership of retailer. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. |  |  |
| 2 | Access the App | Open Post Transfer Posting (MIGO_TR) app. | The Post Transfer Posting (MIGO_TR)screen is displayed. |  |
| 3 | Input Movement Type | On the Transfer Posting Other screen, enter:Movement Type: 413K |  |  |
| 4 | Enter Material | In the Transfer Posting tab, make the following entries in the From section and select Enter:Material: <material number in your sales order number> created above in chapter [Create Sales Order](#unique_63) [page ] 102Location: 995AIn the Transfer Posting tab, make the following entries in the Dest section and select Enter:Plant: 3350Location: 995AAlso, enter the following:Sales Order Number: <your sales order number> created above in chapter [Create Sales Order](#unique_63) [page ] 102Sales Order Item: <your sales order item>Qty in UnE: <material quantity to be transferred>, for instance, 1 PCNote Select Next Item icon to enter details for multiple items before posting. |  |  |
| 5 | Save Your Entries | Select Post. | Material document posted success message is displayed. |  |

###### Schedule Application Job to Create Stock Transport Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process the stock transport requisition is automatically converted to a stock transport order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser (Retail) |  |  |
| 2 | Access the App | Navigate to Schedule Purchasing Jobs - Advanced (F1702) app | Navigate to Schedule Purchasing Jobs - Advanced (F1702) app screen is displayed. |  |
| 3 | Create new job | Choose Create to create a new application job | New Job: Automatic creation of Purchase Orders from Requisitions screen is displayed |  |
| 4 | Enter job details | Enter the application job details in the Template Information and Scheduling Options sections (Step 1).Job Template: Automatic creation of Purchase Orders from RequisitionJob Name: Automatic creation of Purchase Orders from RequisitionChoose Step 2Flag Start ImmediatelyChoose Define Recurrence Pattern if required to change the Recurrence. | The Template Information and scheduling options are defined |  |
| 5 | Enter the Parameters | Choose Step 3In the Parameter section,Flag Per Requisition in New Purchase Order sectionMake the following entries in Item Specific Selection section (For Testing Purpose)Purchase Requisition: <Enter your stock transport requisition number> | Parameters are entered |  |
| 6 | Check | Choose Check | Message is displayed indicating you can go ahead and schedule job. |  |
| 7 | Schedule | Choose Schedule | Automatic creation of Purchase Order from Requisition has been scheduledThe Application Jobs screen is displayed again, and the new job displays in the Jobs table |  |
| 8 | Navigate to Results | Check the newly create job row and choose the icon Navigate to the job Results in Results column | Document (ID XXXXXXX) screen is displayed stock transport order number. |  |

###### Create Stock Transport Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you create a stock transfer order (STO) manually in reference to the purchase requisition generated at sales order item.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser (Retail). |  |  |
| 2 | Access the App | Open Create Purchase Order - Advanced (ME21N) app. | Create Purchase Order - Advanced (ME21N) app screen is displayed. |  |
| 3 | Enter Order Document Type and other data | Enter the following data, then choose Enter.Order Type: StockTranspOrderDel or UD StockTranspOrderDel Supplying Plant: 3350On the Header / Org. Data tab:Company Code: 3310Purchasing Org.: 3310Purchasing Group: 001In Item Overview section:Purchase Requisition: <Enter your stock transport requisition number created above in section [Create Sales Order](#unique_63) [page ] 102 of this documentQuantity: xNote Price should be determined automatically from purchasing info record | All data are entered, the item detail screen is displayed. |  |
| 4 | Save Stock Transfer Order | Choose the Save button and when the stock transfer order number is displayed, write it down for further use. | A new stock transfer order is created. Order Number is displayed. |  |

###### Schedule Application Job to Create Replenishment Delivery for STO

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to schedule a background job for creating outbound deliveries.

This app can be used as an alternative instead of the manual creation of outbound deliveries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Delivery Creation (F2228). | The Application Jobs screen displays. The app automatically shows the history of application jobs. |  |
| 3 | Create Delivery Creation Schedule | Choose Create to define a new job. | The New Job screen is displayed. The Job Template should be defaulted as Schedule Delivery Creation for Purchase Order. |  |
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary, then choose Check. | The system displays the message Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A delivery creation job is scheduled. Screen goes back to Application Jobs. |  |
| 6 | Check Delivery Creation Job Log | On the Application Jobs screen, after job item’s status turned to Finish, choose Status symbol in the Log column.Note Choose the Magnifier, and the job list will refresh. | The job log details displays. |  |

###### Pick, Pack, and Post Goods Issue for Replenishment Delivery from DC

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you pick and pack to generate handling units for materials and to post issue of goods in order to remove the stock from the inventory management system of the DC.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access App | Open Change Outbound Delivery (VL02N) app. | Change Outbound Delivery (VL02N) app screen is displayed. |  |
| 3 | Open Outbound Delivery document | On the Change Outbound Delivery (VL02N) app screen, enter <your outbound delivery document number> and choose Continue. |  |  |
| 4 | Specify picked quantity | Go to Picking tab and specify: Picked Qty : <Enter quantity equal to delivery quantity> | Picked quantity is updated. |  |
| 5 | Save the Outbound Delivery document | Select Save. | Outbound Delivery Document is saved. |  |
| 6 | Post Goods Issue | On the Change Outbound Delivery (VL02N) app screen, enter <your outbound delivery document number> and choose Post Goods Issue. | Goods issue is successful. Inventory stock is reduced from the supplying plant. |  |

##### In-Store Operations

###### Post Goods Receipt for STO/Outbound Delivery

|  |
| --- |
| Note This process step of posting goods receipt in store is optional here as this is also part of the scope of 5FY - In-Store Purchase Order Management. So, posting goods receipt can in store can be done while going through the scope of 5FY - In-Store Purchase Order Management. |

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you post receipt of goods in store against the earlier created outbound delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launch Pad as a Retail Store Associate. |  |  |
| 2 | Access the application | Open Receive Products (F1248) app. | The Receive Products (F1248) screen is displayed. |  |
| 3 | Enter Document Number | Select Enter IDIn the Find a Document pop-up <Enter STO/Outbound Delivery Number Created earlier>,Select OK. | The selected Document details are displayed. |  |
| 4 | Check and Post the Goods Receipt | In the Product section, toggle Checked and Delivery Completed.Select Post. | Document item was posted successfully message is displayed |  |
| 5 | Navigate to Process Picking Requests app | Select Show Actions on the bottom right of the Receive Products screen.Select Process Picking Requests. | Navigation to the Process Picking Request screen is successful, with order number and respective picking request details shown, whose receipt has been posted. |  |

###### Verify Consumer Order Details

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to look inspect the details of any order which is ready to be handed over to the customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Retail Store Associate. |  |  |
| 2 | Access App | Open Hand Over Orders (F4639) app. | Hand Over Orders (F4639) app screen is displayed along with a list of orders ready to be handed over. |  |
| 3 | Enter Data | Following are the different ways in which an order can be searched using this app:Enter the sales order number, Customer Reference or Your Reference for Sold-to Party maintained in the sales order, either of these in Search above the order list and press ENTER.OrSelect Scan Order and scan the order bar-code using the camera on the device. | The order list returns a line item of the order searched along with the details such as customer name, date and time of order pick-up by customer, order status, and payment status. |  |
| 4 | Filter Orders (Optional) | Select Filter and select the desired Picking Request Status or Payment Status filter(s) on the Select Filter pop up and choose OK | The order list displays the filtered list of orders based on the Picking Request Status or Payment Status filter set by the user. The following filter values are displayed under Picking Request Status filter:On TrackPicking in ProgressPicking Request CreatedOrder due for CancellationHanded OverReservation Hand ed OverReturned to ShelfProduct UnavailableThe following filter values are displayed under Payment Status filter:PaidNot Paid |  |
| 5 | Check the details of the order | Select the order item to look over its exceptions and other details. | Order navigates to the Exceptions tab view which displays the details of the exception(s) in the order (short picked, substituted, or unavailable products), switching the tab to Product Details, displays the details of the fully picked products.Apart from exception and product details, the details of the order are displayed in the header. |  |
| 6 | Scan the Picking Request to Withdraw | Select Handover Status on the top right of the screen.Note Hand Over (in case of paid orders), Reservation Hand Over (in case of unpaid orders) and Cancel Order buttons on the bottom of the screen is enabled once the entire order is withdrawn.Select Scan Picking Request on the top right corner of the Handover Status pop-over and scan the picking request bar-code of the order placed in the mentioned handover shelf space using the camera on the device or manually enter the picking request barcode number in the Enter Bar Code pop-up and choose OK and finally select Done | Handover Status pop-over screen is displayed containing the list of Picking Request, Picking Request Status their corresponding Handover Shelf Space numbers and the Withdraw hyperlink.The picking request is withdrawn from the handover shelf space or bin, the hyperlink text changes to Withdrawn and the user is navigated back to the Exceptions tab view. |  |
| 7 | Cancel an Order (Optional) | To cancel an order in case they are overdue for collection:Select Cancel Order on the Exceptions tab viewNote Note Cancel Order should be active for all orders.Select <your reason for rejection> from the dropdown on the Rejection Details pop-up then choose OK.Note You can also execute this process to cancel an order customer request. | Order is rejected, the order status changes to Returned to Shelf and the user is navigated back to the order list screen. In the background, delivery document is deleted, sales order is rejected with the selected rejection reason. |  |
| 8 | Hand Over Orders | Select Hand Over on the Exceptions tab view.Note Hand Over should be active only for Paid orders with picking request status On Track or Order Due for Cancellation. | A confirmation message Hand Over is processed is displayed on the screen.The order status changes to Handed Over and the user is navigated back to the order list screen. |  |

###### Validate Sales Order Document and Subsequent Document Flow (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows how to validate the updates on the sales order also the subsequent documents generated after order sales in store.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Retail Store Associate. |  |  |
| 2 | Access the App | Open Manage Sales Orders (F1873) app. | Manage Sales Orders (F1873) screen is displayed. |  |
| 3 | Go to App | On the Manage Sales Order screen, enter <your sales order number> in the Sales Order field. Select Go | Sales order line item is displayed in the search result. |  |
| 4 | Open the order details | Select the sales order line item. | Display Standard Order XXXXX: Overview screen is displayed. |  |
| 5 | Navigate to Document Flow | Select Display Document Flow, to investigate the details of the subsequent document, for example, outbound delivery, goods issue, invoice documents, material and accounting documents, select the document and choose Display Document. | Generated documents are displayed on the Document Flow screen. Further, selected documents are displayed to investigate the details. |  |

#### Sell from Online Store, Delivery from Distribution Centre to Customer(Pre-Paid Order)

##### Create Sales Order

To execute this scope item, you must have sales orders created in the system.

|  |
| --- |
| Note This process step is intended to be executed to simulate sales orders in SAP S/4HANA Cloud Public Edition system. In real time, sales order creation would be triggered using an inbound service integration arrangement of the third-party web-shop with the SAP S/4HANA Cloud Public Edition system. |

Prerequisite

In order to test the scenario Click and Reserve- Order Fulfillment in Store (Stock is Available in the Store), see [Extend Article to E-commerce Channel](#unique_11) [page ] 13.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Log onto the SAP Fiori Launchpad as a Retail Store Associate. |  |  |
| 2. | Access the App | Open Manage Sales Orders (F1873) app. | Manage Sales Orders (F1873) screen is displayed. |  |
| 3. | Go to App | On the Manage Sales Orders (F1873) screen, select Create > Create Sales Order - VA01 option. | Create Sales Documents screen is displayed. |  |
| 4. | Enter data | Enter the following data:Order Type: ORSales Organization: 3310Distribution Channel: 60Division: 00Select Continue. | Create Standard Order: Overview screen is displayed |  |
| 5. | Enter Header Data | In the header section, enter Sold-to Party: 33113005 and press EnterNow, in the Address From Master Data for Sold-to Party (Document Header) pop-up, enter <Name> in the Name section and <Telephone number> under the Communication section, then press EnterAlso enter Customer References:<Reference Document ID>, for instance, Customer PO number.Note Leave as blank if no reference needs to be maintained.Select Display header details, navigate to Shipping tab view and enter Shipping Condition: 01 Standard |  |  |
| 6 | Enter Item Data | Select Back to navigate back to the Create Standard Order: Overview screen. In the All Items table, enter the following details in different rows and press ENTER:Row1:Material: R_6500Order Quantity: <Order Quantity>Item Category: TANPlant: 3350 |  |  |
| 7 | Navigate to Header Data | In the header section, select Display Header Details icon. | Create Standard Order: Header Data screen is displayed. |  |
| 8 | Assign Payment Card | Navigate to Electronic Payments tab, select Assign Payment Card button. Grant access by selecting Allow on the SAP GUI Security pop-up | Payment Page is displayed in a new browser tab. |  |
| 9 | Enter Payment Card details | Enter the following information on the Payment Page browser tab:Credit Card Type: VISACard Number: 4111111111111111Name on Card : <Enter card holder's name>Valid To : <Any Valid Future Month and Year>CVC: 111Choose Submit then choose Close on the Your payment card was successfully registered message Navigate back to the Create Standard Order: Header Data screen and select Confirm on the Assign Payment Card pop-up. | Payment Card is added, and its details are displayed in the Electronic Payments table. |  |
| 10 | Save the Order | Choose Back button to navigate back to the Create Standard Order: Overview screen. Choose Save. Note the order number for further use. | Sales order is saved and Standard Order <order number> has been saved success message is displayed. |  |

##### Back Office Operations in Distribution Centre

###### Schedule Application Job for Outbound Delivery Creation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step explains you how to schedule a background job for creating outbound deliveries. Schedule Delivery Creation (F2228) app can be used as an alternative instead of the manual creation of outbound deliveries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Schedule Delivery Creation (F2228) app. | The Schedule Delivery Creation (F2228) screen is displayed. The app automatically shows the history of application jobs. |  |
| 3 | Create Delivery Creation Schedule | Choose Create to define a new job. | The New Job: Schedule Delivery Creation for Sales Orders screen is displayed. |  |
| 4 | Enter job details | Enter the application job details in the Template Selection and Scheduling Options sections.Job Template: Schedule Delivery Creation for Sales OrdersJob Name: Schedule Delivery Creation for Sales OrdersChoose Step 2Flag Start ImmediatelyChoose Define Recurrence Pattern if required to change the Recurrence. | The Template Information and scheduling options are defined |  |
| 5 | Enter the Parameters | Choose Step 3In the Parameter section,Make the following entries in Sales Order section (For Testing Purpose)SD Document: <Enter your sales order document number created above in chapter [Create Sales Order](#unique_71) [page ] 115 of this document> | Parameters are entered |  |
| 6 | Check | Choose Check | Message is displayed indicating you can go ahead and schedule job. |  |
| 7 | Schedule | Choose Schedule | Automatic creation of Sales Order has been scheduled message is displayed.The Application Jobs screen displays again, and the new job displays in the Jobs table. |  |
| 8 | Check Delivery Creation Job Log | On the Application Jobs screen, after job item’s status turned to Finish, choose Status symbol in the Log column.Note Choose the Magnifier, and the job list will refresh. | The job log details is displayed. |  |

###### Pick, Pack and Post Goods Issue for Outbound Delivery from Distribution Center

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you pick and pack to generate handling units for materials and to post issue of goods in order to remove the stock from the inventory management system of the DC.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access App | Open Change Outbound Delivery (VL02N) app. | Change Outbound Delivery (VL02N) app screen is displayed. |  |
| 3 | Open Outbound Delivery document | On the Change Outbound Delivery (VL02N) app screen, enter <your outbound delivery document number> and choose Continue. |  |  |
| 4 | Specify picked quantity | Go to Picking tab and specify:Picked Qty : <Enter quantity equal to delivery quantity> | Picked quantity is updated. |  |
| 5 | Save the Outbound Delivery document | Select Save. | Outbound Delivery Document is saved. |  |
| 6 | Post Goods Issue | On the Change Outbound Delivery (VL02N) app screen, enter <your outbound delivery document number> and choose Post Goods Issue. | Goods issue is successful. Inventory stock is reduced from the supplying plant. |  |

###### Create Billing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you handle the billing.

Procedure

Table 3:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Documents screen displays. |  |
| 3 | Define Billing Settings | Choose Billing Settings, you can make the following settings as below:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: OFFAutomatically post billing documents: ONDisplay billing documents after creation: ONChoose delivery items to be billed and select quantities: OFF |  |  |
| 4 | Search for billing due list (optional) | In the search condition, use criteria if necessary. | Sales document(s) display in the result. |  |
| 5 | Select item(s) for billing | Select row(s) of SD Document created previously and choose button Create Billing Documents. | The Create Billing Document screen displays. |  |
| 6 | Maintain Billing Date | Choose billing type Invoice (F2) and maintain billing date, for example current date, then press button OK. | The draft billing document with TMP xxxxxx displays. |  |
| 7 | Save Billing Document | On the Manage Billing Document screen, choose Save.The draft version billing document with TMP xxxxxx turns into a saved billing document with ID xxxxxxxx, make a note of the billing document number: __________. | The system generates an invoice for billing. |  |
| 8 | ODN Number | Check whether the ODN number is generated for the billing document. | ODN number is generated in the Reference field. |  |

###### Validate Follow-On Documents (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows how to validate the updates on the sales order also the subsequent documents generated after order sales in store.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Retail Store Associate. |  |  |
| 2 | Access the App | Open Manage Sales Orders (F1873) app. | Manage Sales Orders (F1873) screen is displayed. |  |
| 3 | Go to App | On the Manage Sales Order screen, enter <your sales order number> in the Sales Order field. Select Go | Sales order line item is displayed in the search result. |  |
| 4 | Open the order details | Select the sales order line item. | Display Standard Order XXXXX: Overview screen is displayed. |  |
| 5 | Navigate to Document Flow | Select Display Document Flow, to investigate the details of the subsequent document, for example, outbound delivery, goods issue, invoice documents, material and accounting documents, select the document and choose Display Document. | Generated documents are displayed on the Document Flow screen. Further, selected documents are displayed to investigate the details. |  |

### Sales from Distribution Center

#### Create Sales Quotation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step explains how to create a sales quotation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. |  |  |
| 2 | Access the App | Open Manage Sales Quotations (F1852) app. |  |  |
| 3 | Navigate to Create Sales Quotation | On the Manage Sales Quotations (F1852) screen, select Create Quotation. | Create Quotations screen is displayed. |  |
| 4 | Enter Sales Document Type | Make the following entries and select Continue:Quotation Type : QTSales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 5 | Enter Quotation Details | Make the following entries and select Enter.Sold-to Party: 33113006Ship-to Party: 33113006Valid to: <Enter a Date>. For example, one year from todayIn the All Items table, enter the following details:Material: R_6500Order Quantity: <Quantity>Plant: 3350 |  |  |
| 6 | Select Save | Select Save. | The quotation document is created. |  |

#### Change Quotation Document (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step explains how to change the quotation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. |  |  |
| 2 | Access the App | Open Manage Sales Quotations (F1852) app. | The Manage Sales Quotations (F1852) screen is displayed. |  |
| 3 | Search for Sales Quotation | Enter search terms in filter bar and select Go.For example, enter <Sales Quotation Number> in Sales Quotation field. | Sales quotation is displayed in result list. |  |
| 4 | Navigate to Display Quotation | Select your sales quotation line item. On the Display Quotation < xxxxxxxx > : Overview screen, select Change. | The Change Quotation < xxxxxxxx > : Overview screen is displayed. |  |
| 5 | Change Quotation | Change following entry and select Enter:Order Quantity : <Enter a different quantity> |  |  |
| 6 | Save | Save your entries. | The quantity is changed in the quotation document. |  |

#### Create Sales Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step explains how to create a sales order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Log on to the SAP Fiori Launchpad as an Internal Sales Representative. |  |  |
| 2. | Access the App | Open Create Sales Orders - VA01 (VA01) app. | Create Sales Documents screen is displayed. |  |
| 3. | Enter data | Enter the following data and select Continue:Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00Note If a sales quotation exists, then select Create with Reference. Enter the quotation document number in Quot. field under Quotation tab view and select Copy. | Create Standard Order: Overview screen is displayed. |  |
| 4. | Enter Data | In the header section, enter:Sold-to Party:33113006Ship-to Party: 33113006Customer References: <Reference Document ID>, for instance, sales quotation document number.In the All Items table, enter the following details:Material: R_6500Order Quantity: <Order Quantity>Plant: 3350Select Enter | Details are copied from the reference document if sales order is selected to create with reference else if selected to create without reference then details are entered successfully.Note In case quotation exists for the given customer and material combination and you still select to create the sales order without its reference then Open quotations for item pop-up appears after you enter the customer and material details. You can select to proceed in one of the following ways:Select Continue or Cancel on the Open quotations for item pop-up to continue and complete sales order creation without the quotation reference. Or,Select List on the Open quotations for item pop-up, select the relevant SD document (quotation document) which you want to use as reference and select Copy. |  |
| 5 | Save the Order | Select Save. | A success message on save of a sales order is displayed. |  |

#### Create an Outbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step explains how to create an outbound delivery from a sales order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Create Outbound Deliveries - From Sales Orders (F0869A) app. | The Create Outbound Deliveries screen is displayed. |  |
| 3 | Search Sales Order | Make the following entries and choose Go:Shipping Point: 3350Planned Creation Date: <delivery selection date>Sales Document: <sales order number created earlier> |  |  |
| 4 | Create Delivery | Select your sales order items and choose Create Deliveries. | Creation of a delivery is initiated.Note Depending on the scope item settings, the availability is checked during delivery creation using the available inventory and replenishment lead time. Without sufficient stock, the created delivery has no confirmed quantities, and therefore does not start the warehouse management picking process. As soon as there is sufficient stock for delivery creation, the system creates a delivery with the starting of the picking process in warehouse management.To avoid open deliveries, ensure there is sufficient inventory quantity at the time for delivery creation. Additionally, you have the following options to restrict the creation of deliveries with no confirmed quantities:You may increase the replenishment lead time which is used during the availability check (has to be larger than the selection period used for delivery creation).You may change the customizing settings for the incompleteness procedure for delivery creation, so that only complete deliveries are saved.You may change the customizing settings for the used delivery item category. The Check quantity 0 field must be adapted to B = Situation Rejected with An Error Message. |  |
| 5 | Check Details | Choose Display Log. | The Analyze Delivery Log screen is displayed, delivery is created successfully. Delivery number is displayed on Deliveries tab.Note With the Analyze Delivery Logs app, you can display an overview of the logs of all the deliveries which have been created in your system. You can filter by, for example, Created by and other additional settings. If you select the arrow on the right of each delivery log entry, you can display the exact message type and text, and also the related sales document. |  |

#### Create Attachment for Delivery (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step explains how to create an attachment for outbound delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Display Outbound Delivery (VL03N) app. |  |  |
| 3 | Enter Outbound Delivery Number | In the Outbound Delivery field, enter <the outbound delivery number created in previous step> and select Continue. | The Outbound Delivery xxx Display: Overview screen is displayed. |  |
| 4 | Create Delivery Attachment | Select Change then select Services for Object > Create Attachment from the top menu. | A popup message File Upload is displayed. |  |
| 5 | Import File | Select OK in the File Upload pop-up.Select the document to be uploaded and select Open. | A message The attachment was successfully created is displayed. |  |
| 6 | Check Attachment | Select Services for Object > Attachment List from the top menu. | An attachment is displayed on the Service: Attachment List pop-up screen. |  |
| 7 | Save the Document | Select Save. | A message Outbound Delivery xxx has been saved is displayed. |  |

#### Process Picking for Outbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The picking process involves taking goods from a storage location and place the right quantity in a picking area where the goods are prepared for shipping. This process step explains how to pick goods before outbound delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD) app. | The Manage Outbound Deliveries - VL06O (VL06O_CLOUD) screen is displayed. |  |
| 3 | Select Picking | Select For Picking. |  |  |
| 4 | Enter Shipping Point | Make the following entries and select Execute: Under Organizat. Data section, select:Shipping Point: 3350Under the Picking Data section, selectOnly Picking Without WM: X | The Day’s Workload for Picking screen is displayed. |  |
| 5 | Change Outbound Deliveries | On the Day’s Workload for Picking, select <your delivery number> and select Change Outbound Deliveries. | The Outbound Delivery xxx Change: Overview screen is displayed. |  |
| 6 | Check Batch Split | Select Picking tab. |  |  |
| 7 | Enter Picked Quantity | Enter <quantity equal to delivery Qty> in Picked Qty field for picking related item(s). |  |  |
| 8 | Select Enter | Select Enter. |  |  |
| 9 | Select Save | Select Save. | A message Outbound Delivery xxx has been saved is displayed. |  |

#### Post Goods Issue for Outbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post goods issue for outbound delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD) app. | The Manage Outbound Deliveries - VL06O (VL06O_CLOUD) screen is displayed. |  |
| 3 | Enter Value in the Selection Screen | Choose For Goods Issue.In the Outbound Deliveries for Goods Issue screen, make the following entries and choose Execute.Shipping Point: 3350 | The Goods Issue for Outbound Deliveries to be Posted screen is displayed. |  |
| 4 | Post Good Issue | Select < your delivery > and choose Post Goods Issue.Enter <today’s date> in Act. Gds Mvmnt Date of the Specify Actual Goods Issue Date pop-up and choose Continue. | A message confirms about successful goods movement. |  |

#### Create Billing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step explains how to generate billing documents (invoice).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. |  |  |
| 2 | Access the App | Open Create Billing Documents (F0798) app. | The Create Billing Documents screen is displayed. |  |
| 3 | Define Billing Settings | Select Billing Settings in the bottom bar, you can make the following settings as below then select OK:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: OFFAutomatically post billing documents: ONDisplay billing documents after creation: ONChoose delivery items to be billed and select quantities: OFF |  |  |
| 4 | Search for Billing Due List (Optional) | In the search condition, use criteria if necessary. | Sales document(s) is displayed. |  |
| 5 | Select Item(s) for Billing | Select row(s) of SD Document created previously and select button Create Billing Documents. | A popup Create Billing Documents is displayed. |  |
| 6 | Maintain Billing Date | Select billing type Invoice (F2) and maintain Billing Date, for example <current date>, then select OK. | The draft billing document or invoice with ID < TMP xxxxxx > is displayed. |  |
| 7 | Save Billing Document | On the Manage Billing Documents screen, select Save. Make a note of the billing document number.Note The draft version billing document or invoice with ID TMPxxxxxx is converted into a saved billing document with ID xxxxxxxx. | The system generates an invoice for billing. |  |

#### Create Attachment for Billing Document (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step explains how to create an attachment for a billing document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. |  |  |
| 2 | Access the App | Open Manage Billing Documents (F0797) app. | The Manage Billing Documents (F0797) screen is displayed. |  |
| 3 | Search Billing | Make the following entry, and select Go:Billing Document: <Billing Document Number Created Previously> |  |  |
| 4 | Select Billing Number | On the Manage Billing Documents screen, select your billing document created in the previous step, and select Display. | The Manage Billing Documents screen is displayed. |  |
| 5 | Edit | On the Manage Billing Documents screen, select Edit. |  |  |
| 6 | Create Billing Attachment | Scroll down and select Upload in the Attachments section. |  |  |
| 7 | Import File | Select the document to be uploaded and select Open. | The attachment is successfully uploaded. |  |
| 8 | Check Attachment (Optional) | In the Attachments section, you can see the uploaded document. Select the document you want to open. |  |  |
| 9 | Select Save | Select Save. | A message Billing document saved is displayed. |  |

## Appendix

### Physical Inventory for Stores (Optional)

To get accurate stock situation in store you can perform a physical inventory count of articles. If you have articles in store with consignment stock then counting should be done by first creating separate physical inventory documents for articles with consignment stock. Follow the below steps -

1. Execute the steps from scope item Physical Inventory for Distribution Centers(5FS) to create physical inventory documents for articles with consignment stock. Note that you should create two physical inventory documents one for special stock (consignment stock) and one for unrestricted stock.

|  |
| --- |
| Note Process steps from In-Store Inventory Management (3HR) does not support articles with Consignment stock. |

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
> Flagged while digesting this document, not verified: Purchasing group is 002 in the article master and consignment PO steps but 001 in the optional manual STO steps (DC to store).

> [!warning] Conflict
> Flagged while digesting this document, not verified: Display Customer step uses customer 33113008 in one scenario but 10113008 in the later-pickup scenario, while the sample data lists 33113008.

## Connections
- part-of :: [[_cluster]]
- see-also :: [[10-procurement/test-script-scheduling-agreement-for-consignment-procurement-2ny-ae-sa]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/71P_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 227,976 chars in the whole document
