---
id: 15-retail-operations/in-store-customer-order-management-3hu-ae-test-script-sap-s-4hana-clou
title: "In-Store Customer Order Management (3HU_AE) - Test Script, SAP S/4HANA Cloud Public Edition (3HU_S4CLD2608_BPD_EN_AE)"
description: "SAP test script for scope item 3HU_AE: in-store customer orders with immediate or later pickup, replenishment, picking, handover; prerequisites and sample data."
cluster: 15-retail-operations
tags: [kb/retail-operations, topic/omnichannel-order-fulfillment]
aliases: [3HU_S4CLD2608_BPD_EN_AE]
keywords: [Omnichannel and In-Store Customer Order Fulfillment, in-store customer order management, immediate pickup, pickup at later date, in-store sales orders, serial number management, store picking requests, order handover, stock transport orders, goods receipt]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3HU_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-939
topic: 15-retail-operations/omnichannel-order-fulfillment
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# In-Store Customer Order Management (3HU_AE) - Test Script, SAP S/4HANA Cloud Public Edition (3HU_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3HU_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Omnichannel and In-Store Customer Order Fulfillment** in Retail Operations. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | In-Store Customer Order Management (3HU_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 4](#_Toc232852744)

[2 Prerequisites 5](#_Toc232852745)

[2.1 System Access 5](#_Toc232852746)

[2.2 Roles 5](#_Toc232852747)

[2.3 Master Data, Organizational Data, and Other Data 6](#_Toc232852748)

[2.4 Business Conditions 8](#_Toc232852749)

[2.5 Preliminary Steps 9](#_Toc232852750)

[2.5.1 Customer Maintenance Settings 9](#_Toc232852751)

[2.5.1.1 Define Schema for Customer Maintenance (Optional) 9](#_Toc232852752)

[2.5.1.2 Assign Template Customer to Schema 9](#_Toc232852753)

[2.5.1.3 Assign Schema to Store 10](#_Toc232852754)

[2.5.1.4 Define Grouping Schema and Assign Countries (Optional) 11](#_Toc232852755)

[2.5.1.5 Assign Grouping Schema to Store 12](#_Toc232852756)

[2.5.1.6 My Store Assignment 13](#_Toc232852757)

[2.5.2 Create Initial Stock 13](#_Toc232852758)

[2.5.3 Maintain Application Settings 14](#_Toc232852759)

[2.5.4 Maintain Default Settings 15](#_Toc232852760)

[3 Overview Table 17](#_Toc232852761)

[4 Test Procedures 21](#_Toc232852762)

[4.1 Sell from Store: Immediate Pickup 21](#_Toc232852763)

[4.1.1 Immediate Pickup of General Retail Articles 21](#_Toc232852764)

[4.1.1.1 Verify Consumer Registration 21](#_Toc232852765)

[4.1.1.2 Create Master Data for Registering a New Consumer (Optional) 22](#_Toc232852766)

[4.1.1.3 Create Sales Order and Generate Invoice 23](#_Toc232852767)

[4.1.1.4 Process Customer Order Payment from POS 25](#_Toc232852768)

[4.1.2 Immediate Pickup of Serial Number-Managed Retail Articles 26](#_Toc232852769)

[4.1.2.1 Verify Consumer Registration 26](#_Toc232852770)

[4.1.2.2 Create Master Data for Registering a New Consumer (Optional) 27](#_Toc232852771)

[4.1.2.3 Create Sales Order 28](#_Toc232852772)

[4.1.2.4 Create an Outbound Delivery with Serial Number of Product 29](#_Toc232852773)

[4.1.2.5 Generate Invoice 30](#_Toc232852774)

[4.1.2.6 Process Customer Order Payment from POS 32](#_Toc232852775)

[4.2 Sell from Store: Pickup at Later Date due to Stock Unavailability (Payment Done at Pickup) 32](#_Toc232852776)

[4.2.1 In-Store Operations 32](#_Toc232852777)

[4.2.1.1 Check Stock Availability in Store 32](#_Toc232852778)

[4.2.1.2 Verify Consumer Registration 33](#_Toc232852779)

[4.2.1.3 Create Master Data for Registering New Consumers (Optional) 34](#_Toc232852780)

[4.2.1.4 Create Sales Order 35](#_Toc232852781)

[4.2.1.5 Print Sales Order Document (Optional) 37](#_Toc232852782)

[4.2.2 Back-Office Operations from Distribution Center to Store 38](#_Toc232852783)

[4.2.2.1 Check Stock Overview 38](#_Toc232852784)

[4.2.2.2 Schedule Application Job to Create Stock Transport Order 39](#_Toc232852785)

[4.2.2.3 Create Stock Transport Order (Optional) 41](#_Toc232852786)

[4.2.2.4 Schedule Application Job to Create Replenishment Delivery for STO 42](#_Toc232852787)

[4.2.2.5 Pick, Pack, and Post Goods Issue for Replenishment Delivery from DC 43](#_Toc232852788)

[4.2.3 Back-Office Operations from External Supplier to Store 44](#_Toc232852789)

[4.2.3.1 Schedule Application Job to Create Purchase Order 44](#_Toc232852790)

[4.2.3.2 Create Purchase Order (Optional) 46](#_Toc232852791)

[4.2.3.3 Create Inbound Delivery for Purchase Order 47](#_Toc232852792)

[4.2.4 In-Store Operations 48](#_Toc232852793)

[4.2.4.1 Post Goods Receipt for STO/Outbound Delivery or Post Goods Receipt for PO/Inbound Delivery at Store 48](#_Toc232852794)

[4.2.4.2 Start Picking 49](#_Toc232852795)

[4.2.4.3 Verify Consumer Order Details and Hand Over 52](#_Toc232852796)

[4.2.4.4 Validate Follow-On Documents and Print Billing Document 54](#_Toc232852797)

[4.2.5 Process Customer Order Payment from POS 55](#_Toc232852798)

[5 Appendix 57](#_Toc232852799)

[5.1 Configuration (Optional) 57](#_Toc232852800)

[5.1.1 Define Basic Settings for Process Picking Requests 57](#_Toc232852801)

[5.1.1.1 Define Customizing Schema for Store Picking Requests 57](#_Toc232852802)

[5.1.1.2 Assign Customizing Schemas to Site for Picking Requests 58](#_Toc232852803)

[5.1.2 Define Schema for Handover Orders 58](#_Toc232852804)

[5.1.2.1 Define Schema for Handover Orders 58](#_Toc232852805)

[5.1.2.2 Assign Handover Orders Schema to Store (Optional) 59](#_Toc232852806)

[5.2 Optional Scenarios 59](#_Toc232852807)

[5.2.1 Select Withdraw Hyperlink to Withdraw 60](#_Toc232852808)

[5.2.2 Skip Assignment of Picking Container to Handover Shelf 61](#_Toc232852809)

## Purpose

Overview

In the typical in-store process, the customer gathers the products from the shelf, and pays at the cash-register. For specific purposes, it can be required that a sales order is created for the customer. For example, in case the product isn't available in the store and must be ordered for the customer. Another reason can be the need to document the sale, for example for warranty purposes, or to gather the serial number of a high-value article.

The process starts with capturing information about customer, like name, address, phone number, followed by entering product-related information, which is then stored in the sales order. Then, there are two main process variants, depending on whether the goods are available in the store, see below. In both scenarios, the process ends with the customer paying at the cash-register with reference to the billing document (which is created as a follow-on document to the sales order).

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

|  |
| --- |
| Note In the retail industry, specific terms differ from the standard terms used in other lines of business. Therefore, SAP solutions which provide business processes across multiple lines of businesses may use terms for the corresponding business objects, transactions, and user interfaces that deviate from the retail terminology. For integration and reuse reasons, the SAP S/4HANA Cloud Public Edition, retail, fashion, and vertical business business may thus include different terms that refer to the same concept. SAP intends to harmonize the terminology in the future.The following terms are used synonymously in this document:Table 1:Standard Terms in Lines of BusinessSAP S/4HANA Cloud Public Edition, retail, fashion, and vertical business businessMaterial, productArticleMaterial group, product groupMerchandise categoryPlant, locationSite (as superordinate term) - store and distribution center (DC) |

## Prerequisites

This chapter summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data, and business conditions.

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
| Warehouse Clerk (Retail) | SAP_BR_WAREHOUSE_CLERK_RFM | Retail Inventory Processing | SAP_RFM_SPT_INVTRY_PROCG_PC |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Retail Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Pricing Specialist (Retail) | SAP_BR_PRICING_SPCLST_RFM | Retail PricingRetail MarkupsRetail Sales Pricing | SAP_BR_PRICING_SPCLST_RFM |  |
| Administrator (Retail) | SAP_BR_ADMINISTRATOR_RFM | Administration - Retail | SAP_BR_ADMINISTRATOR_RFM |  |
| Configuration Expert - Business Network Integration | SAP_BR_CONF_EXPERT_BUS_NET_INT | Configuration Expert - Business Network Integration | SAP_BR_CONF_EXPERT_BUS_NET_INT |  |
| Purchaser (Retail) | SAP_BR_PURCHASER_RFM | Purchaser (Retail) | SAP_BR_PURCHASER_RFM |  |
| Receiving Specialist | SAP_BR_RECEIVING_SPECIALIST | Receiving Specialist | SAP_BR_RECEIVING_SPECIALIST |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT |  | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Single Article (Material or Product) | R_3018 | Gas Grill 3-Burner Black |  |
| Single Article (Material or Product) | R_3000 | Coffee maker, 12 cup, Black |  |
| Serial Number- Managed Article | R_8500 | Digital Camera Serial Number |  |
| Packaging Material (Article or Product) | R_CARTON | Carton |  |
| Packaging Material (Article or Product) | R_PALLET | Pallet |  |
| Packaging Material (Article or Product) | R_WIRE_BASKET | Wire Basket |  |
| One-time Sold-to Party/ Ship-to party/Payer | 33113005 | Consumer 2 AE |  |
| B2C Sold-to Party/ Ship-to party/Payer | 33113008 | Consumer 2 AE |  |
| Store (Site) | 3340 | Store 3340 AE |  |
| Store (Site) | 3341 | Store 3341 AE |  |
| Store (Site) | 3342 | Store 3342 AE |  |
| Store (Site) | 3343 | Store 3343 AE |  |
| Store (Site) | 3344 | Store 3344 AE |  |
| Distribution Center (DC) | 3350 | DC 3350 AE |  |
| Storage Location | 994A | St.Loc.Neg.Stock |  |
| Storage Location (DC) | 995A | Storage Loc. DC |  |
| Shipping Point | 99CC | SP Store Click and Collect |  |
| Shipping Point | 33RS | SP Store AE |  |
| Shipping Condition | 02 | Pick-up |  |
| Shipping Condition | 03 | Immediately |  |
| Sales Organization | 3310 | Dom. Sales Org |  |
| Distribution Channel | 40 | Store Sales |  |
| Division | 00 | Product Division 00 |  |
| Product Group (Material Group or Merchandise Category) | R6121001 | Gas Grills |  |
| Product Group (Material Group or Merchandise Category) | R4121002 | Coffee Makers |  |
| Product Group (Material Group or Merchandise Category) | R4141001 | Cameras |  |
| Supplier | 33213002 | Retail Food Supplier AE |  |
| Supplier | 33213001 | Retail Non-Food Supplier AE |  |
| Customizing Schema | 0001 | Customer Maintenance Schema Template |  |

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 5FH - Business Partners for Retail | You have completed the step described in the Business Partners for Retail (5FH) master data script. |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS (BNZ) master data script. Posting period is up to date. |

### Preliminary Steps

#### Customer Maintenance Settings

##### Define Schema for Customer Maintenance (Optional)

Purpose

The following procedure provides instructions to create a customizing schema.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to CBC Project Experience as Configuration Expert - Business Process Configuration |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Schema for Customer Maintenance.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Schema for Customer Maintenance screen is displayed. |  |
| 3 | Configure Define Schema for Customer Maintenance | Create the following settings:You should select an existing customizing schema and then click on Copy As.Provide name to customizing schema:Customizing Schema: <Use your own schema>Description: <Use your own description>and choose Copy. | Data Provided. |  |
| 4 | Save Customizing Schema | Click on Save to save Customizing Schema. | The Customizing Schema has been saved. |  |

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

##### Define Grouping Schema and Assign Countries (Optional)

Purpose

The following procedure provides instructions for creating a grouping schema and assign countries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Project Experience in SAP Central Business Configuration. |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Grouping Schema and Assign CountriesChoose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Grouping Schema and Assign Countries screen is displayed. |  |
| 3 | Create Grouping Schema | Choose New EntriesAdd Grouping Schema and Description and choose Save. | Data was saved message is displayed. |  |
| 4 | Assign Countries/Regions | Select Grouping Schema created above and Select Assign Countries/Regions from Dialog Structure.Choose "New Entries" and add Countries/Regions. | Data Provided. |  |
| 5 | Save | Choose Save. | The Grouping Schema has been saved. |  |

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

##### My Store Assignment

Purpose

With this process step, retail store associates can assign the required stores to themselves.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Retail Store Associate. |  |  |
| 2 | Open App | Open the My Store Assignment (F4334) app. | The My Store Assignment (F4334) app is displayed. |  |
| 3 | Assign Store | Search for a store in the list.Select the required Store.Select Assign Me. | The system displays a You were assigned to store <XXXX>. message. |  |

#### Create Initial Stock

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to set initial stock to execute this scope item.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk (Retail). | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Goods Receipt Other screen displays. |  |
| 3 | Enter Movement Type | Make the following entry and choose Enter.Executable Action in Transaction MIGO: Goods Receipt & Other |  |  |
| 4 | Enter Material | On the Goods Receipt Other Screen: Material tab, make the following entry, and choose Enter:Material : <Use an article> from the list of retail articles mentioned in Master Data, Organizational Data, and Other Data. |  |  |
| 5 | Enter Quantity Data | On the Goods Receipt Other Screen: Quantity tab, make the following entry, and choose Enter:Qty in Unit of Entry: <Enter your Qty>Unit of Entry: <Enter UoM of material> |  |  |
| 6 | Enter the Goods Receipt Other Screen: Where Tab | On the Goods Receipt Other Screen: Where tab, make the following entries and choose Enter:Movement Type: 561 (Receipt per initial entry of stock balances into unrestricted use)Plant: <Enter a Plant>Storage Location: <Enter a Storage Location> |  |  |
| 7 | Save Your Entries | Choose Post. |  |  |

#### Maintain Application Settings

Purpose

With this process step, retail store associates can set the application settings before selecting a picking request. After completing all necessary settings, associates can start picking products on the shop floor.

|  |
| --- |
| Note Set application settings only the first time a user is assigned to the store or when a setting needs to change. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Retail Store Associate. |  |
| 2 | Access App | Open the Process Picking Requests (F4643) app. | The Process Picking Requests (F4643) app screen is displayed with a list of picking requests. |
| 3 | Set Application Settings | Select Profile in the top right corner of the Process Picking Requests (F4643) screen.Go to Application Settings.Enter the following information in the Application Settings pop-up:Printer: <Printer assigned to your store>Label Type: RFM_ST_PKORD_BOX_LABEL_STD (Sample Form for Box Label Printing)Content List Type: RFM_ST_PKORD_CNTNT_LIST_STD (Sample Form for Content List Printing)Select OK. | The system displays an Application settings are saved message.The application settings are applied for the user. |

Result

The application settings are maintained for the user.

#### Maintain Default Settings

Purpose

With this process step, retail store associates can set the default settings such as sales organization, distribution channel and division for Manage In-Store Sales Orders app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Retail Store Associate. |  |  |
| 2 | Access App | Open Manage In-Store Sales Orders (F7141) app. | Manage In-Store Sales Orders (F7141) screen is displayed. |  |
| 3 | Set Default Settings | Select Profile in the top right corner of the Manage In-Store Sales Orders (F7141) screen.Go to Settings.Select Default Values.Enter the following information:SalesOrganization: 3310DistributionChannel: 40Division: 00Select Save. | The system displays an Your changes have been saved message.The default settings are applied for the user. |  |

Result

Default settings are maintained.

## Overview Table

This scope item consists of several process step provided in the table below.

Sell from Store: Immediate Pickup

Immediate Pickup of General Retail Articles

| Process Step | Business Role | App | Expected Results |
| --- | --- | --- | --- |
| [Verify Consumer Registration](#unique_17) [page ] 21 | Retail Store Associate | Display Customer (WDA0486) | Consumer details are verified, if consumer is already registered. |
| [Create Master Data for Registering a New Consumer (Optional)](#unique_18) [page ] 22 | Retail Store Associate | Create Customer (WDA0484) | Consumer master is created. |
| [Create Sales Order and Generate Invoice](#unique_19) [page ] 23 | Retail Store Associate | Manage In-Store Sales Orders (F7141) | Sales order is created, picking of the outbound delivery is triggered, goods issue for the outbound delivery is posted. |
| [Process Customer Order Payment from POS](#unique_20) [page ] 25 | Administrator (Retail) | Schedule POS Inbound Service (F5236) | Customer order payment information from a POS system to SAP S/4HANA Cloud Public Edition is transferred. |

Immediate Pickup of Serial Number-Managed Retail Articles

| Process Step | Business Role | App | Expected Results |
| --- | --- | --- | --- |
| [Verify Consumer Registration](#unique_21) [page ] 26 | Retail Store Associate | Display Customer (WDA0486) | Consumer details are verified, if consumer is already registered. |
| [Create Master Data for Registering a New Consumer (Optional)](#unique_22) [page ] 27 | Retail Store Associate | Create Customer (WDA0484) | Consumer master is created. |
| [Create Sales Order](#unique_23) [page ] 28 | Retail Store Associate | Manage In-Store Sales Orders (F7141) | Sales order is created. |
| [Create an Outbound Delivery with Serial Number of Product](#unique_24) [page ] 29 | Retail Store Associate | Create Outbound Delivery - With Order Reference (VL01N) | Delivery from sales order is created. Serial number is entered for serial number-managed product. |
| [Generate Invoice](#unique_25) [page ] 30 | Retail Store Associate | Manage In-Store Sales Orders (F7141) | Picking of the outbound delivery is triggered, goods issue for the outbound delivery is posted, invoice is generated and printed. |
| [Process Customer Order Payment from POS](#unique_26) [page ] 32 | Administrator (Retail) | Schedule POS Inbound Service (F5236) | Customer order payment information from a POS system to SAP S/4HANA Cloud Public Edition is transferred. |

Sell from Store: Pickup at Later Date due to Stock Unavailability (Payment Done at Pickup)

| Process Step | Business Role | App | Expected Results |
| --- | --- | --- | --- |
| In-Store Operations |  |  |  |
| [Check Stock Availability in Store](#unique_27) [page ] 32 | Retail Store Associate | Look Up Retail Products (F0431) | Estimated date for future stock availability at store by sourcing from DC or external supplier is checked. |
| [Verify Consumer Registration](#unique_28) [page ] 33 | Retail Store Associate | Display Customer (WDA0486) | Consumer details are verified, if consumer is already registered. |
| [Create Master Data for Registering New Consumers (Optional)](#unique_29) [page ] 34 | Retail Store Associate | Create Customer (WDA0484) | Consumer Master is created, |
| [Create Sales Order](#unique_30) [page ] 35 | Retail Store Associate | Manage In-Store Sales Orders (F7141) | Sales order is created. Store picking request is created. Also, account assigned purchase requisition or account assigned stock purchase requisition is created. Sales order document is also printed. |
| [Print Sales Order Document (Optional)](#unique_31) [page ] 37 | Retail Store Associate | Manage In-Store Sales Orders (F7141) | Sales order document is printed and handed over to consumer. |
| Back-Office Operations from Distribution Center to Store |  |  |  |
| [Check Stock Overview](#unique_32) [page ] 38 | Warehouse Clerk (Retail) | Stock - Multiple Materials (F1595) | The sales order stock is displayed in the column Unrestricted Stock, sales order number is displayed in the column Sales Order. |
| [Schedule Application Job to Create Stock Transport Order](#unique_33) [page ] 39 | Purchaser (Retail) | Schedule Purchasing Jobs - Advanced (F1702) | Stock transport order (STO) is created for transfer of stock from distribution center to store. |
| [Create Stock Transport Order (Optional)](#unique_34) [page ] 41 | Purchaser (Retail) | Create Purchase Order - Advanced (ME21N) | Stock transport order (STO) is created with reference to the purchase requisition for transfer of stock from distribution center to store, manually. |
| [Schedule Application Job to Create Replenishment Delivery for STO](#unique_35) [page ] 42 | Purchaser (Retail) | Schedule Delivery Creation (F2228) | Outbound delivery document with reference to stock transfer order (STO), is created |
| [Pick, Pack, and Post Goods Issue for Replenishment Delivery from DC](#unique_36) [page ] 43 | Shipping Specialist | Change Outbound Delivery (VL02N) | Material (article) is picked then packed. Handling units are generated. Goods issue is posted for the outbound delivery from the distribution center. |
| Back-Office Operations from External Supplier to Store |  |  |  |
| [Schedule Application Job to Create Purchase Order](#unique_37) [page ] 44 | Purchaser (Retail) | Manage Purchase Requisitions - Professional (F2229) | Purchase order (PO) is created with reference to the purchase requisition for procurement of product from external supplier to store. |
| [Create Purchase Order (Optional)](#unique_38) [page ] 46 | Purchaser (Retail) | Create Purchase Order - Advanced (ME21N) | Purchase order (PO) is created with reference to the purchase requisition for procurement of product from external supplier to store, manually. |
| [Create Inbound Delivery for Purchase Order](#unique_39) [page ] 47 | Receiving Specialist | Create Inbound Delivery (VL31N) | Inbound delivery document with reference to purchase order is created |
| In-Store Operations (Stock is replenished, Picking Initiated in Store) |  |  |  |
| [Post Goods Receipt for STO/Outbound Delivery or Post Goods Receipt for PO/Inbound Delivery at Store](#unique_40) [page ] 48For more information see section XX for scope item 5FY – In-Store Purchase Order Management | Retail Store Associate | Receive Products (F1248) | Goods receipt is posted against the stock transport order document or outbound delivery document or the purchase order document or inbound delivery document received at Store. Store associate is notified about stock reservation. After GR is posted, the stock is managed as sales order stock in the store. |
| [Start Picking](#unique_41) [page ] 49 | Retail Store Associate | Process Picking Requests (F4643) | Picking is started for the selected picking requests |
| In-Store Operations (Hand Over Orders to Consumers) |  |  |  |
| [Verify Consumer Order Details and Hand Over](#unique_42) [page ] 52 | Retail Store Associate | Hand Over Orders (F4639) | Details of the consumer’s order is verified using the mobile number, name or order number. |
| [Validate Follow-On Documents and Print Billing Document](#unique_43) [page ] 54 | Retail Store Associate | Manage In-Store Sales Orders (F7141) | Billing document is printed |
| [Process Customer Order Payment from POS](#unique_44) [page ] 55For more information see section 4.5 for scope item 3HV – Store Connectivity – Inbound | Administrator (Retail) | Schedule POS Inbound Service (F5236) | Background job for posting POS inbound for sale is scheduled. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Sell from Store: Immediate Pickup

#### Immediate Pickup of General Retail Articles

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
| 3 | Enter Parameters | Enter the below detail before selecting Continue:Customer: 33113008 | Display Customer: <xxxxxx> screen is displayed. |  |
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

Follow this step to create a sales order using the Manage In-Store Sales Order app. During this process, the system will initiate the picking of the outbound delivery, posting of goods issue for the outbound delivery, and generation of the associated follow-on documents. After the process is completed, you have the option to generate and print invoices.

Additionally, you can validate any updates on the sales order if needed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Retail Store Associate. |  |  |
| 2 | Access the App | Open Manage In-Store Sales Orders (F7141) app. | Manage In-Store Sales Orders (F7141) screen is displayed. |  |
| 3 | Go to App | On the Manage In-Store Sales Orders (F7141) screen, press Create button. | Sales Order screen is displayed. |  |
| 4 | Enter Data | In Basic Data section of General Information tab view, enter:Customer: <Enter your customer’s ID>NoteEnter the customer or sold-to-party ID of the respective customer if already registered or newly registered.If one-time customer or sold-to party is used, then after entering your sold-to party, go to Partners , select your Sold-to Party and select Change Address button.Enter or change any field value in the Change Address pop-up and select Change Address button, for instance, enter E-Mail.Customer References: <Order Reference Text>Shipping Conditions: 03In the Products table of the Products tab view, enter the following details:Product : R_3018Requested Quantity: <Order Quantity>Item Category : <Enter Item Category>, for instance TAN (Standard Item).Note Select Settings icon, on the View Settings pop-up, select Shipping Point checkbox and select OK.Site: <Enter your store>, for instance, 3340.Shipping Point: 33RSChoose Enter | Details are entered successfully. |  |
| 5 | Save the Order | Select Create. | Sales order is saved and Standard Order <order number> has been saved success message is displayed. |  |
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
| Note Refer Process Customer Order Payment from POS from Store Connectivity – Inbound (3HV) scope item. Also, customer order payment related payload should be referred to simulate the inbound payload with the aggregated information of payments for the sales took place in the Point-of-sales system. |

#### Immediate Pickup of Serial Number-Managed Retail Articles

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
| 3 | Enter Parameters | Enter the below detail before selecting Continue:Customer: 33113008 | Display Customer: <xxxxxx> screen is displayed. |  |
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

##### Create Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step explains how to create a sales order with serial number-managed product.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Retail Store Associate. |  |  |
| 2 | Access the App | Open Manage In-Store Sales Orders (F7141) app. | Manage In-Store Sales Orders (F7141) screen is displayed. |  |
| 3 | Go to App | On the Manage In-Store Sales Orders (F7141)screen, press Create button. | Sales Order screen pop-up is displayed. |  |
| 4 | Enter Data | In Basic Data section of General Information tab view, enter:Customer: <Enter your customer’s ID>NoteEnter the customer ID or sold-to-party ID of the respective customer if already registered or newly registered.If one-time customer or sold-to party is used, then after entering your customer, go to Partners tab, select your Sold-to Party and select Change Address button. Enter/change any field value in the Change Address pop-up and select Change Address button, for instance, enter E-MailShipping Conditions: 03Customer References: <Order Reference Text>In the Products table of the Products tab view, enter the following details:Product :R_8500Alternatively, choose Scan GTIN and scan product barcode using the camera on the device or manually enter product barcode number in the Enter Barcode pop-up and choose OK.Requested Quantity: <Order Quantity>Item Category: <Enter Item Category>, for instance TAN (Standard Item)Note Select Settings icon, on the View Settings pop-up, select the Shipping Point checkbox and select OK.Site: <Enter your store>, for instance, 3340Shipping Point: 33RSChoose Enter | Details are entered successfully. |  |
| 5 | Save the Order | Select Create. | Sales order is saved and Standard Order <order number> has been saved success message is displayed. |  |

##### Create an Outbound Delivery with Serial Number of Product

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step explains how to create an outbound delivery from a sales order and enter the serial number for serial number-managed product in it.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Retail Store Associate |  |  |
| 2 | Access the App | Open Create Outbound Delivery - With Order Reference (VL01N) app. | The Create Outbound Delivery - With Order Reference (VL01N) screen is displayed. |  |
| 3 | Search Sales Order | Make the following entries:Shipping Point: 33RSSelection Date: <the delivery selection date>Order: <the sales order number created previously>Choose Continue. |  |  |
| 4 | Enter Serial Number of Product | Select the serial number-managed item then go to Menu > Extras > Serial NumbersEnter serial number in the Serial Number column of the Maintain Serial Numbers pop-up and choose Continue. | Serial number of the product is entered in the outbound delivery. |  |
| 5 | Save the Outbound Delivery | Choose Save. | Information message Outbound Delivery xxxxxxxxx has been saved is displayed. |  |

##### Generate Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step triggers the picking of the outbound delivery, posts goods issue for the outbound delivery, generates and prints invoice and shows how to validate the updates on the sales order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Retail Store Associate. |  |  |
| 2 | Access the App | Open Manage In-Store Sales Orders (F7141) app. | Manage In-Store Sales Orders (F7141) screen is displayed. |  |
| 3 | Go to App | On the Manage In-Store Sales Orders (F7141) enter Sales Order : <the sales order number created previously> and select Go. | Resulting sales order is displayed in the Sales Orders table. |  |
| 4 | Generate Invoice | Select the resulting sales order and choose Generate Invoice button on the Sales Order screen. | Standard Order xxxxx has been saved message is displayed. Outbound delivery is processed with picked quantity, goods issue is posted and invoice is generated automatically. |  |
| 5 | Print Invoice (Optional) | Navigate back to the Manage In-Store Sales Orders (F7141) screen, enter Sales Order : <the sales order number created previously> and select Go.Select the resulting sales order and go to Process Flow tab and click on the Invoice, then select More Links from the Invoice Number pop-up.Select the Display Billing Documents hyperlink in the Define Link List pop-up.Go to Menu >Goto>Header> OutputSelect the output from the Output table and select Display Document. Select Print . | Invoice is previewed and printed. |  |
| 6 | Validate Follow-On Documents (Optional) | Navigate back to the Sales Orders screen and go to Process Flow tab.Click on the <Relevant Follow-On Document>, then select More Links from the <Relevant Follow-On Document> number pop-up.Select the Display <Relevant Follow - On Document> Documents hyperlink in the Define Link List pop-up to investigate the details of the subsequent document, for example, outbound delivery, invoice documents and accounting documents. | Generated documents are displayed to investigate the details. |  |

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
| Note Refer Process Customer Order Payment from POS from Store Connectivity – Inbound (3HV) scope item. Also, customer order payment related payload should be referred to simulate the inbound payload with the aggregated information of payments for the sales took place in the Point-of-sales system. |

### Sell from Store: Pickup at Later Date due to Stock Unavailability (Payment Done at Pickup)

#### In-Store Operations

##### Check Stock Availability in Store

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
| 3 | Search a product and check the stock information | Enter R_3018 or a search term, for instance, name of the product, product GTIN, etc. in the product search and select the product from the search result list. | Product details on the Information tab are displayed for the below fields:Product IDGTINStock QuantityWeightDistribution Center Stock QuantityExternally ProcuredNoteDistribution Center Stock Quantity field would contain the product’s stock information and the estimated planned delivery time from the distribution center (DC) supplying to the store.Externally Procured field contains product estimated planned delivery time information from the external supplier to the store. |  |

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
| 2 | Access the App | Open Display Customer (WDA0486) app. | Display Customer (WDA0486) screen is displayed. |  |
| 3 | Enter Parameters | Enter the below detail before selecting Continue:Customer: 33113008 | Display Customer (WDA0486) <xxxxxx> screen is displayed. |  |
| 4 | Check the details | Check the Customer type of the ConsumerCheck the details displayed in Address section. | The details are displayed and verified. |  |

##### Create Master Data for Registering New Consumers (Optional)

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

##### Create Sales Order

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
| 3 | Go to App | On the Manage In-Store Sales Orders (F7141) screen, choose Create . | Sales Order screen is displayed. |  |
| 4 | Enter Data | In Basic Data section of General Information tab view, enter:Customer: <Enter your customer’s ID>NoteEnter the customer or sold-to-party ID of the respective customer if already registered or newly registered.If one-time customer or sold-to party is used, then after entering your sold-to party, go to Partners , select your Sold-to Party and select Change Address button.Enter/change any field value in the Change Address pop-up and select Change Address button, for instance, enter E-Mail.Shipping Conditions: 02Customer References: <Order Reference Text>In the Products table of the Products tab view, enter the following details:Product : R_3018Requested Quantity: <Order Quantity>Item Category : <Enter Item Category>, for instance CBAB (Bought-In Item)Note Select Settings icon, on the View Settings pop-up, select Shipping Point checkbox and choose OK.Site: <Enter your store>, for instance, 3340.Shipping Point: 99CCPress Enter.Select the item to navigate to its details. Go to Delivery > Schedule Lines and enter the following and choose Apply:Sched. Line Category: <Enter Schedule Line Category>, for instance, CB (Indiv. Purchase Order)/ CU(IndivStockTransfOrd)Note Schedule line category is selected on the basis of where the stock can be procured from, that is, Distribution Center or External Supplier. The stock availability can be checked as described in chapter [Check Stock Availability in Store](#unique_27) [page ] 32. | Details are entered successfully. |  |
| 5 | Save the Order | Select Create. | Sales order is saved and Standard Order <order number > has been saved success message is displayed. |  |
| 6 | Display Sales Order Item Details | On the Sales Order screen, in the Products table of the Products tab, select an item to navigate to its details. | Item screen is displayed. |  |
| 7 | Note the Purchase Requisition Number per Sales Order Item. | Go to Delivery > Schedule LinesNote Select Settings icon, on the Columns pop-up, select the Purchase Requisition checkbox and choose OK. Switch to Show More per Row view.Make a note of the purchase requisition number for all the sales order items. |  |  |

##### Print Sales Order Document (Optional)

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

#### Back-Office Operations from Distribution Center to Store

##### Check Stock Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The goods are transferred from freely available stock to sales order stock automatically during creation of sales order using movement type 413. The stock overview reflects this transfer of products.

This process step shows you how to check the stock overview.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk (Retail). |  |  |
| 2 | Access the App | Open Stock - Multiple Materials (F1595) app. |  |  |
| 3 | Enter Plant, Material Data, and Sales Order | On the Stock - Multiple Materials (F1595) screen, select Adapt Filters then select the Sales Order in the Adapt Filters pop-up, select OK and then make the following entries:Material Number: R_3018Plant: 3350Sales Order:<order number>Select GoNote You may need to adapt column view settings to view Sales Order on the View Settings pop-up and select OK. | The sales order stock is displayed in the column Unrestricted Stock, sales order number is displayed in the column Sales Order. |  |

##### Schedule Application Job to Create Stock Transport Order

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
| 5 | Enter the Parameters | Choose Step 3In the Parameter section,Flag Per Requisition in New Purchase Order sectionMake the following entries in Item Specific Selection section (For Testing Purpose)Purchase Requisition : <Enter your stock transport requisition number created> | Parameters are entered |  |
| 6 | Check | Choose Check | Message is displayed indicating you can go ahead and schedule job. |  |
| 7 | Schedule | Choose Schedule | Automatic creation of Purchase Order from Requisition has been scheduledThe Application Jobs screen is displayed again, and the new job is displayed in the Jobs table |  |
| 8 | Navigate to Results | Check the newly create job row and choose the icon Navigate to the job Results in Results column. | Document (ID XXXXXXX) screen displays stock transport order number. |  |

##### Create Stock Transport Order (Optional)

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
| 2 | Access the App | Open Create Purchase Order - Advanced (ME21N). | The Create Purchase Order - Advanced (ME21N) screen displays. |  |
| 3 | Enter Purchase Order Document Type | Enter the following data:Order Type: UD (StockTranspOrderDel)Then choose Enter. |  |  |
| 4 | Enter Purchase Order Data | Enter the following data:Supplying Plant: 3350On the Org. Data tab:Purchasing Org.: 3310Purchasing Group: 001Company Code: 3310In the area of Overview Item:Purchase Requisition: <Enter your stock transport requisition number>Quantity: xThen choose Enter.Note Price should be determined automatically from purchasing info record | All data is entered, and the item details screen displays. |  |
| 5 | Save Stock Transport Order | Choose Save and when the stock transport order number is displayed, write it down for further use. | A new stock transport order is created. Stock transport order number is displayed. |  |

##### Schedule Application Job to Create Replenishment Delivery for STO

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

##### Pick, Pack, and Post Goods Issue for Replenishment Delivery from DC

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
| 6 | Open Outbound Delivery document again | On the Change Outbound Delivery (VL02N) app screen, enter <your outbound delivery document number> and choose Pack. |  |  |
| 7 | Enter Packaging Material | On the Processing of Handling Units for Outbound Delivery <Outbound Delivery Number> screen, under the Pack Material tab and under All Existing HUs (Available for Packing), enter <Your packaging Material> in the Packaging Materials column. | Handling units are generated. |  |
| 8 | Pack Material with Packaging Material | Mark the material and handling unit line items under Materials to Be Packed and All Existing HUs (Available for Packing) sections, respectively. Choose Pack. | The message Material was Packed is displayed. |  |
| 9 | Save the Outbound Delivery document | Select Save. | Outbound delivery document is saved. |  |
| 10 | Post Goods Issue | On the Change Outbound Delivery (VL02N) app screen, enter <your outbound delivery document number> and choose Post Goods Issue. | Goods issue is successful. Inventory stock is reduced from the supplying plant. |  |

#### Back-Office Operations from External Supplier to Store

##### Schedule Application Job to Create Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process the purchase requisition is automatically converted to a purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser (Retail). |  |  |
| 2 | Access the app | Navigate to Manage Purchase Requisitions - Professional (F2229) app. | Manage Purchase Requisitions – Professional screen is displayed. |  |
| 3 | Search the Purchase Requisition number | Enter the below value in the selection screen and press GoPurchase Requisition:<Enter your purchase requistion number> created above in chapter [Create Sales Order](#unique_30) [page ] 35. | Purchase Requisitions result list is displayed. |  |
| 4 | Select the Purchase Requisition | Select the row of Purchase Requisition from the Purchase Requisitions result list. | Display Purchase Requisition screen is displayed. |  |
| 5 | Change the Purchase Requisition | Click on Display/Change button. | Change Purchase Req. xxxxxxxx screen is displayed. |  |
| 6 | Select and assign source of supply | In the Item Details section, select the Source of Supply tab.Click on the button Assign Source of SupplyChoose a source of supply and click on Save. | Purchase requisition xxxxxxxx changed, message is displayed.. |  |
| 7 | Log on | Log on to the SAP Fiori launchpad as a Purchaser (Retail). |  |  |
| 8 | Access the app | Navigate to Schedule Purchasing Jobs - Advanced (F1702). | Application Jobs screen is displayed. |  |
| 9 | Create new job | Choose Create to create a new application job. | New Job: Automatic creation of Purchase Orders from Requisitions screen is displayed. |  |
| 10 | Enter job details | Enter the application job details in the Template Selection and Scheduling Options sections.Job Template: Automatic creation of Purchase Orders from RequisitionJob Name: Automatic creation of Purchase Orders from RequisitionChoose Step 2Flag Start ImmediatelyChoose Define Recurrence Pattern if required to change the Recurrence. | The template selection and scheduling options are defined. |  |
| 12 | Enter the Parameters | Choose Step 3In the Parameter section,Flag Per Requisition in New Purchase Order sectionMake the following entries in Item Specific Selection section (For Testing Purpose)Purchase Requisition: <Enter your purchase requisition number> created above in chapter [Create Sales Order](#unique_30) [page ] 35. | Parameters are entered. |  |
| 13 | Check | Choose Check. | Message is displayed indicating you can go ahead and schedule job. |  |
| 14 | Schedule | Choose Schedule. | Automatic creation of Purchase Order from Requisition has been scheduled.The Application Jobs screen is displayed again, and the new job is displayed in the Jobs table.. |  |
| 15 | Navigate to Results | Check the newly create job row and choose the icon Navigate to the job Results in Results column. | Document (ID XXXXXXX) screen is displayed purchase order number. |  |

##### Create Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

In this procedure, you create a purchase order with Confirmation Control Key for inbound delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the Purchaser (Retail) role. |  |  |
| 2 | Access the App | Open Create Purchase Order - Advanced (ME21N). |  |  |
| 3 | Enter Purchase Order Data | Enter the necessary data:Order type: NB Standard POSupplier: <Enter your own supplier>In the Header section, on the Org. Data tab:Purch. Org.:3310Purch. Group:001Company Code:3310In the Item Overview section:Material:R_3018Plant:3350Storage Location:995AQuantity:xNet Price:xIn the Item Detail section, on the Confirmations tab:Conf. Control:Confirmations |  |  |
| 4 | Save Purchase Order | Choose Save and when the purchase order number is displayed, write it down for further use. | Your purchase order is created and the PO number is displayed. |  |

##### Create Inbound Delivery for Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you manually create inbound delivery with reference to purchase order (PO).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Receiving Specialist. |  |  |
| 2 | Access App | Open Create Inbound Delivery (VL31N) app. | Create Inbound Delivery (VL31N) app screen is displayed. |  |
| 3 | Start Selection for Inbound Delivery creation | On the Create Inbound Delivery (VL31N) app screen, enter the following:Supplier: <Enter your supplier>Purchase Order: <your Purchase Order document number>Select Continue. |  |  |
| 4 | Update Putaway quantity | On the All Items table, enter the Putaway Qty | Putaway quantity is updated. |  |
| 5 | Save Inbound Delivery document | Select Save. | Inbound delivery document is created. |  |

#### In-Store Operations

##### Post Goods Receipt for STO/Outbound Delivery or Post Goods Receipt for PO/Inbound Delivery at Store

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

##### Start Picking

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

##### Verify Consumer Order Details and Hand Over

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

##### Validate Follow-On Documents and Print Billing Document

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

#### Process Customer Order Payment from POS

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure you can transfer customer order payment information from a POS system to SAP S/4HANA based on the method of payment, such as cash, cheques, payment cards, electronic cash, or electronic wallet using SOAP service.

Procedure

|  |
| --- |
| Note Please refer to chapter Process Customer Order Payment from POS in scope item Store Connectivity – Inbound (3HV). |

## Appendix

### Configuration (Optional)

Prerequisites

To carry out the following activities, the business role SAP_BR_BPC_EXPERT must be assigned to the user.

#### Define Basic Settings for Process Picking Requests

##### Define Customizing Schema for Store Picking Requests

Use

To execute the scope item, you must define the basic settings for Process Picking Requests application.

Procedure

1. Log on to the Project Experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. You can search for the configuration activity Define Basic Customizing Schema for Store Picking Requests to locate it in the tree view. Choose Open Documentation for the found line item to see more details. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).
3. The "Define Customizing Schema for Store screen is displayed.
4. Select New Entries button.
5. Enter values for Customizing Schema and Description. As per your preference, select the checkboxes for Print Content List, Print Label, ScanPick Request., Scan Handover Shelf and Skip Shelf Assignment.
6. Select Save.

Result

You have defined your settings for the Process Picking Requests (F4643) app.

##### Assign Customizing Schemas to Site for Picking Requests

Use

To execute the scope item, you must assign the relevant customizing schema having the basic setting for Process Picking Requests (F4643) app defined, to your store

Procedure

1. Log on to the Project Experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. You can search for the configuration activity Assign Customizing Schemas to Site for Picking Requests to locate it in the tree view. Choose Open Documentation for the found line item to see more details. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).
3. The "Assign Customizing Schemas to Site f screen is displayed.
4. Select New Entries button.
5. Enter the value for Plant: <Your Store> and CstgSchema: 0002.
6. Select Save.

Result

You have assigned the relevant customizing schema to your store.

#### Define Schema for Handover Orders

##### Define Schema for Handover Orders

Use

To execute the scope item, you must define the settings to withdraw picking request from the handover shelf.

Procedure

1. Log on to the Project Experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. You can search for the configuration activity Define Basic Customizing Settings for Handover Orders to locate it in the tree view. Choose Open Documentation for the found line item to see more details. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).
3. The "Define Schema for Handover Orders… screen is displayed.
4. Select New Entries button.
5. Enter values for Customizing Schema and Description. As per your preference, select the checkbox for Scn Hnd. Ov
6. Select Save.

Result

You have defined your settings to withdraw picking request from the handover shelf.

##### Assign Handover Orders Schema to Store (Optional)

Use

To execute the scope item, you must assign the relevant customizing schema having the basic setting for Hand Over Orders (F4639) app defined, to your store

Procedure

1. Log on to the Project Experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. You can search for the configuration activity Assign Handover Orders Schema to Store to locate it in the tree view. Choose Open Documentation for the found line item to see more details. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).
3. The "Assign Handover Orders Schema to St… screen is displayed.
4. Select New Entries button.
5. Enter the value for Plant and CstgSchema: 0002.
6. Select Save.

Result

You have assigned the relevant customizing schema to your store.

### Optional Scenarios

Prerequisites

To carry out the following activities, the business role SAP_BR_RFM_STORE_ASSOCIATE must be assigned to the user.

#### Select Withdraw Hyperlink to Withdraw

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check the status of orders placed in the handover shelf. You need to withdraw the ordered products from the handover shelf to hand over to the customer.

|  |
| --- |
| NoteThis process step must be followed when, in the [Define Schema for Handover Orders](#unique_50) [page ] 58 SSC UI, Customizing Schema - 0002 is assigned to your store.For more information related to viewing the configuration or assignment of your store to the existing configuration, see chapter [Define Schema for Handover Orders](#unique_50) [page ] 58This process step is an alternative to the process step Scan the Picking Request to Withdraw described in chapter [Verify Consumer Order Details and Hand Over](#unique_42) [page ] 52 of this document, for withdrawal of picking container from the handover shelf. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Pre-Process Steps for Withdrawal | As a prerequisite, repeat the process steps 4.1-4.13. |  |  |
| 2 | Select Handover Status | Select Handover Status on the top right of the screen.Note Reservation Hand Over (in case of unpaid orders) and Cancel Order buttons on the bottom of the screen are enabled once the entire order is withdrawn. | Handover Status pop-over screen is displayed containing the list of Picking Request, Picking Request Status their corresponding Handover Shelf Space numbers and the Withdraw hyperlink. |  |
| 3 | Select Withdraw hyperlink to withdraw | Select Withdraw hyperlink against the Handover Shelf Space and select Done. | The picking request is withdrawn from the handover shelf space or bin, the hyperlink text changes to Withdrawn and the user is navigated back to the Exceptions tab view. |  |
| 4 | Post-Process Steps to complete handover. | Repeat the process step Hand Over Orders is discribed in [Verify Consumer Order Details and Hand Over](#unique_42) [page ] 52 to complete the handover process. |  |  |

#### Skip Assignment of Picking Container to Handover Shelf

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to complete a picking process to keep the orders ready for handover to customers.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Scan all items | Scan all items in the picking request | Once all the products in picking request are scanned and placed in a picking container, Products Picked indicator is updated and progressed to full. Product list is also updated.After the last product of the products list is scanned and placed in the picking container, the message pop-up Content list have been printed for picking requests is displayed.Note If products belonging to a picking request is completely unavailable, then that picking request is not shown on the Handover Shelf screen. Also, the content list is not printed for that picking request. |  |
| 2 | Reprint content list(Optional) | Select Print Content List in the bottom right of the screen. On the Reprint Content List pop-up select the picking request for which content list must be reprinted and then select Reprint. | Reprint of content list is triggered for the selected picking request. |  |
| 3 | Finish picking or Pick More | Select Pick More on the Handover Shelf screen to pick more requests. Or, Select All Done on the Handover Shelf screen if picking of all requests is completed | You are navigated back to the Picking Requests screen to select and start picking of new requests, if Pick More is selected Or,You are navigated back to the SAP Fiori launchpad if All Done is selected. |  |

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
> Flagged while digesting this document, not verified: Schedule Delivery Creation (F2228) is assigned to the Purchaser (Retail) role in the Overview Table but the test procedure logs on as Shipping Specialist.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[15-retail-operations/test-script-omnichannel-order-fulfillment-for-retail-5fz-ae-sap-s-4han]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3HU_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 102,217 chars in the whole document
