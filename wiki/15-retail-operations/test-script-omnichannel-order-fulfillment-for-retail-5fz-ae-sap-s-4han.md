---
id: 15-retail-operations/test-script-omnichannel-order-fulfillment-for-retail-5fz-ae-sap-s-4han
title: "Test Script: Omnichannel Order Fulfillment for Retail (5FZ_AE) - SAP S/4HANA Cloud Public Edition (5FZ_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 5FZ_AE: click-and-collect, click-and-reserve and DC-to-customer retail order fulfillment steps."
cluster: 15-retail-operations
tags: [kb/retail-operations, topic/omnichannel-order-fulfillment]
aliases: [5FZ_S4CLD2608_BPD_EN_AE]
keywords: [Omnichannel and In-Store Customer Order Fulfillment, omnichannel order fulfillment, click and collect, click and reserve, store picking, order handover, sales order creation, stock transport orders, outbound delivery, billing documents]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5FZ_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1094
topic: 15-retail-operations/omnichannel-order-fulfillment
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Omnichannel Order Fulfillment for Retail (5FZ_AE) - SAP S/4HANA Cloud Public Edition (5FZ_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5FZ_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Omnichannel and In-Store Customer Order Fulfillment** in Retail Operations. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Omnichannel Order Fulfillment for Retail (5FZ_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232856436)

[2 Prerequisites 4](#_Toc232856437)

[2.1 System Access 4](#_Toc232856438)

[2.2 Roles 4](#_Toc232856439)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232856440)

[2.4 Additional Manual Configuration 7](#_Toc232856441)

[2.5 Business Conditions 7](#_Toc232856442)

[2.6 Preliminary Steps 8](#_Toc232856443)

[2.6.1 Create Initial Stock 8](#_Toc232856444)

[2.6.2 Assign Retail Store Associate (User Persona) to a Store (Optional) 9](#_Toc232856445)

[2.6.3 Maintain Merchandise Category Based on Picking Sequence (Optional) 10](#_Toc232856446)

[2.6.4 Maintain Application Settings 11](#_Toc232856447)

[2.6.5 Create Freight Condition 12](#_Toc232856448)

[2.6.5.1 Create Delivery Cost Header Condition 12](#_Toc232856449)

[2.6.5.2 Create Delivery Cost Item Condition 13](#_Toc232856450)

[3 Overview Table 14](#_Toc232856451)

[4 Test Procedures 17](#_Toc232856452)

[4.1 Click and Reserve - Order Fulfillment in Store (Stock is Available in the Store) 17](#_Toc232856453)

[4.1.1 Create Sales Orders 17](#_Toc232856454)

[4.1.2 Start Picking 19](#_Toc232856455)

[4.1.3 Look Over the Order Details for Handover 22](#_Toc232856456)

[4.1.4 Validate Sales Order Document and Subsequent Document Flow (Optional) 25](#_Toc232856457)

[4.1.5 Process Customer Order Payment from POS 25](#_Toc232856458)

[4.2 Click and Collect (Pre-Paid Order)- Order Fulfillment from Distribution Center to Store (Stock is Not Available in the Store) 26](#_Toc232856459)

[4.2.1 Create Sales Order 26](#_Toc232856460)

[4.2.2 Back-Office Operations from Distribution Center to Store 30](#_Toc232856461)

[4.2.2.1 Check Stock Overview 30](#_Toc232856462)

[4.2.2.2 Schedule Application Job to Create Stock Transport Order 31](#_Toc232856463)

[4.2.2.3 Create Stock Transport Order (Optional) 32](#_Toc232856464)

[4.2.2.4 Schedule Application Job to Create Replenishment Delivery for STO 33](#_Toc232856465)

[4.2.2.5 Pick, Pack, and Post Goods Issue for Replenishment Delivery from DC 34](#_Toc232856466)

[4.2.3 In-Store Operations 36](#_Toc232856467)

[4.2.3.1 Post Goods Receipt for STO/Outbound Delivery 36](#_Toc232856468)

[4.2.3.2 Start Picking 37](#_Toc232856469)

[4.2.3.3 Verify Consumer Order Details 39](#_Toc232856470)

[4.2.3.4 Validate Sales Order Document and Subsequent Document Flow (Optional) 42](#_Toc232856471)

[4.3 Sell from Online Store, Delivery from Distribution Center to Customer (Pre-Paid Order) 43](#_Toc232856472)

[4.3.1 Create Sales Order 43](#_Toc232856473)

[4.3.2 Back-Office Operations in Distribution Center 45](#_Toc232856474)

[4.3.2.1 Schedule Application Job for Outbound Delivery Creation 45](#_Toc232856475)

[4.3.2.2 Pick, Pack and Post Goods Issue for Outbound Delivery from Distribution Center 47](#_Toc232856476)

[4.3.2.3 Create Billing Document 48](#_Toc232856477)

[4.3.2.4 Validate Follow-On Documents (Optional) 49](#_Toc232856478)

[5 Appendix 51](#_Toc232856479)

[5.1 Optional Scenarios 51](#_Toc232856480)

[5.1.1 Create Sales Order 51](#_Toc232856481)

[5.1.2 Select Withdraw 54](#_Toc232856482)

[5.1.3 Take Over Picking Request from Another Store Associate 55](#_Toc232856483)

[5.1.4 Unassign Picking Request 56](#_Toc232856484)

[5.1.5 Reassign Picking Request 57](#_Toc232856485)

[5.1.6 Skip Assignment of Picking Container to Handover Shelf 58](#_Toc232856486)

## Purpose

Overview

In today’s retail environment, retailers must account for the situation where a consumer buys merchandise online and picks it up in a store. This benefits both the consumer and the retailer. For consumers, it eliminates the risk of missed deliveries, theft of delivered items, and unnecessary shipping charges. For retailers, it's more cost-effective than home delivery and opens up opportunities for additional sales once the consumer is in the store.

This scope item describes the fulfillment of orders placed online by consumers to be picked up in the stores. Consumers can order articles using e-commerce and pick them up at a store of their choice. This is known as buy online, pick-up in store (BOPIS) or Click-and-Collect.

Two main process steps are supported: First, the process of picking the articles from the sales floor, and second, the handover of the merchandise to the consumers. To cater for requirements of different retailer’s formats, processes can be set up flexibly (for example, small fashion boutique vs. grocery retailer).

A process variant is the Click-and-Reserve, where the merchandise isn't paid using e-commerce channels, but after handover in the store.

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
| Warehouse Clerk (Retail) | SAP_BR_WAREHOUSE_CLERK_RFM | Retail Inventory Processing | SAP_RFM_SPT_INVTRY_PROCG_PC |  |
| Retail Store Manager | SAP_BR_RFM_STORE_MANAGER | Store Management | SAP_BR_RFM_STORE_MANAGER |  |
| Retail Store Associate | SAP_BR_RFM_STORE_ASSOCIATE | Retail Store Operations | SAP_BR_RFM_STORE_ASSOCIATE |  |
| Configuration Expert - Business Network Integration | SAP_BR_CONF_EXPERT_BUS_NET_INT | Business Network Integration / Business Network Integration - Concur Integration / Business Network Integration - Output Control / Business Network Integration - Data Replication / Configuration Expert - Business Network Integration Cross Applications | SAP_BR_CONF_EXPERT_BUS_NET_INT |  |
| Administrator (Retail) | SAP_BR_ADMINISTRATOR_RFM | Administration - Retail | SAP_BR_ADMINISTRATOR_RFM |  |
| Purchaser (Retail) | SAP_BR_PURCHASER_RFM | Retail Purchasing / Retail Sourcing and Contracting | SAP_BR_PURCHASER_RFM |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |
| Pricing Specialist (Retail) | SAP_BR_PRICING_SPCLST_RFM | Retail PricingRetail Markups | SAP_BR_PRICING_SPCLST_RFM |  |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales | SAP_BR_INTERNAL_SALES_REP |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

|  |
| --- |
| Note Screen sequence may vary depending on the article you choose during testing. |

| Master / Org. Data | Value | Master / Org. Data Details | Comments |
| --- | --- | --- | --- |
| Single Article (Material or Product) | R_4017 | Lobster Product with weight embedded GTIN |  |
| Single Article (Material or Product) | R_4018 | Prawns Product with weight embedded GTIN, substitute product for R_4017 |  |
| Single Article (Material or Product) | R_2000 | Low fat milk, 1,5 % |  |
| Single Article (Material or Product) | R_2003 | Organic Low fat milk, 1,5 %Substitute product for R_2000 |  |
| Single Article (Material or Product) | R_1039 | My Best bread roll - italian |  |
| Single Article (Material or Product) | R_1040 | My Best bread roll - classicSubstitute product for R_1039 |  |
| Variant Article (Material or Product) | R_1003001 | Chocolate, Whole-Milk, Diet |  |
| Sales set Product (Material or Article) | R_1052 | My Best Blond Shampoo & Conditioner |  |
| Packaging Material (Article or Product) | R_CARTON | Carton |  |
| Packaging Material (Article or Product) | R_PALLET | Pallet |  |
| Packaging Material (Article or Product) | R_WIRE_BASKET | Wire Basket |  |
| One-time Sold-to Party/ Ship-to party/Payer | 33113005 | Consumer 1 AE |  |
| Storage location | 994A | St.Loc.Neg.Stock |  |
| Storage location | 995A | Storage Loc. DC |  |
| Shipping point | 99CC | SP Store Click and Collect |  |
| Store (Site) | 3340 | Store 3340 AE |  |
| Store (Site) | 3341 | Store 3341 AE |  |
| Store (Site) | 3342 | Store 3342 AE |  |
| Store (Site) | 3343 | Store 3343 AE |  |
| Store (Site) | 3344 | Store 3344 AE |  |
| Distribution Center (DC) | 3350 | DC 3350 AE |  |
| Sales organization | 3310 | Dom. Sales Org |  |
| Distribution channel | 60 | E-Commerce |  |
| Division | 00 | Product Division 00 |  |
| Shipping Condition | 02 | Pick-up |  |
| Shipping Condition | 01 | Standard |  |
| Product Group (Material Group or Merchandise Category) | R1111003 | Seafood |  |
| Product Group (Material Group or Merchandise Category) | R1182002 | Milk |  |
| Product Group (Material Group or Merchandise Category) | R1171001 | Bread |  |
| Product Group (Material Group or Merchandise Category) | R1202001 | Sweets |  |
| Product Group (Material Group or Merchandise Category) | R2121002 | Hair Care |  |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/a696c6a1999355e0903fb9a26e43e52f)

### Business Conditions

Before testing this scope item across various scenarios, ensure that the corresponding business conditions are met.

| Scope Item ID | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS (BNZ) master data script. Posting period is up to date. |
| 1S2 - Digital Payments | You have completed activating digital payments in SAP S/4HANA Cloud Public Edition. With this, you can add payment card information to your orders which is a pre-requisite if functionality of pre-paid orders is relevant as part of the processing of this scope item. |
| 1Z1 -Digital Payments – Sales | You have completed setting-up digital payments in SAP S/4HANA Cloud Public Edition. With this, you can add payment card information to your orders which is a pre-requisite if functionality of pre-paid orders is relevant as part of the processing of this scope item. |
| 5FW - My Store Management | You have completed the step of assigning store associates to store which is a pre-requisite to maintain picking sequence |

|  |
| --- |
| Note To manage the payment status of sales orders in a click-and-collect business scenario, you can choose the following options:SAP Digital Payments Add-On: If you prefer to use the SAP digital payments add-on capabilities, open a support ticket to activate the Digital Payments(1S2) and Digital Payments – Sales (1Z1) scope items. Please visit SAP Signavio Process Navigator for more information on these scope items.Other: If you do not wish to use the SAP digital payments add-on, you will need to implement the BAdI Maintain Sales Order Payment Status (RFM_STR_PICK_ORD_PAYT_STS_MOD) to influence the payment status of the click-and-collect sales order. |

### Preliminary Steps

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

#### Maintain Merchandise Category Based on Picking Sequence (Optional)

Use

To optimize the picking of e-commerce orders which are fulfilled in stores, a sequence based on merchandise categories is maintained.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Retail Store Manager. |  |  |
| 2 | Access the App | Open the Maintain Picking Sequence (F4711) app. | The Maintain Picking Sequence (F4711) app is displayed. |  |
| 3 | Download Excel file | In the Maintain Picking Sequence (F4711) app, select the Download Picking Sequence button. Select Download on the Information pop-up. | The picking sequence excel sheet is downloaded. |  |
| 4 | Maintain Product Group sequence in Excel | Product Group sequence is rearranged as per user requirement in the excel and should get saved without any error. | Changes are allowed and excel sheet is saved. |  |
| 5 | Upload the Excel file | In the Maintain Picking Sequence (F4711) app, select the Upload Picking Sequence button then drop the excel file or select Upload on the Upload Picking Sequence pop-up and choose the file to upload. | Once the excel sheet is uploaded successfully same should appear in the app. |  |

Result

Picking sequence is maintained.

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

#### Create Freight Condition

##### Create Delivery Cost Header Condition

Use

You perform this activity to create delivery cost header condition for the article.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Pricing Specialist (Retail). |  |  |
| 2 | Access App | Open Manage Prices - Sales (F4111) app. | Manage Prices - Sales (F4111) screen is displayed. |  |
| 3 | Enter values | On the Manage Prices - Sales (F4111) screen , select Create and enter the following details and Select ENTER:Condition Type : EFH2Condition Table: <Select the relevant condition table and access sequence from menu help>, for instance, 307Note Condition record can be created at distribution chain or customer level, Access Sequence – 020 / 010 for Condition Table – 307, the Customer field value must be entered according to the chosen condition table.Sales Organization: 3310Distribution Channel: 60Condition Amount or Ratio: <Enter an amount> | Change Material (Purchasing) screen is displayed. |  |
| 4 | Save the record | Select Save. | The condition record is saved. |  |

Result

Delivery cost header condition is created.

##### Create Delivery Cost Item Condition

Use

You perform this activity to create delivery cost item condition for the article.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Pricing Specialist (Retail). |  |  |
| 2 | Access App | Open Manage Prices - Sales (F4111) app. | Manage Prices - Sales (F4111) screen is displayed. |  |
| 3 | Enter values | On the Manage Prices - Sales (F4111) screen, select Create and enter the following details and Select ENTER:Condition Type: EFI1Condition Table: <Select the relevant condition table and access sequence from menu help>, for instance, 304/4BFNote Condition record can be created at product or material group level, Access Sequence – 010 / 020 for Condition table – 304/4BF respectively, the Product or Material Group field value must be entered according to the chosen condition table.Product/Material Group: <Enter your product or material group>Sales Organization: 3310Distribution Channel: 60Condition Amount or Ratio: <Enter an amount> | Change Material (Purchasing) screen is displayed. |  |
| 4 | Save the record | Select Save. | The condition record is saved. |  |

Result

Delivery cost header item is created.

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Click and Reserve - Order Fulfillment in Store (Stock is Available in the Store)

| Process Step | Business Role | App | Expected Results |
| --- | --- | --- | --- |
| [Create Sales Orders](#unique_15) [page ] 17 | Internal Sales Representative | Create Sales Orders - VA01 (VA01) | Sales orders in SAP S/4HANA Cloud Public Edition starter system is simulated. |
| [Start Picking](#unique_16) [page ] 19 | Retail Store Associate | Process Picking Requests (F4643) | Picking is started for the selected store picking requests, product GTIN is scanned and handover shelf is assigned to the picking request. |
| [Look Over the Order Details for Handover](#unique_17) [page ] 22 | Retail Store Associate | Hand Over Orders (F4639) | Details of the selected order and the status of order placed in the handover shelf is displayed. Also, order withdrawal is done and order is handed over to the consumer. |
| [Validate Sales Order Document and Subsequent Document Flow (Optional)](#unique_18) [page ] 25 | Retail Store Associate | Manage Sales Orders (F1873) | Validate the updates on the sales order also the subsequent documents generated after completion of the picking and handover process. |
| [Process Customer Order Payment from POS](#unique_19) [page ] 25 | Administrator (Retail)Configuration Expert - Business Network Integration | Schedule POS Inbound Service (F5236)Overview Message Monitoring (F4515) | Point-of-sale (POS) financial transactions are transferred to the SAP S/4HANA Cloud Public Edition system. |
|  |  |  |  |

If the consumer wants to order more products in-store other than that ordered at web-shop, refer to section 4.1 of 3HU - In-Store Customer Order Management.

Click and Collect (Pre-Paid Order) - Order Fulfillment from Distribution Center to Store (Stock is Not Available in the Store)

| Process Step | Business Role | App | Expected Results |
| --- | --- | --- | --- |
| [Create Sales Order](#unique_20) [page ] 26 | Internal Sales Representative | Create Sales Orders - VA01 (VA01) | Sales orders in SAP S/4HANA Cloud Public Edition starter system is simulated. |
| [Back-Office Operations from Distribution Center to Store](#unique_21) [page ] 30 |  |  |  |
| [Check Stock Overview](#unique_22) [page ] 30 | Warehouse Clerk (Retail) | Stock - Multiple Materials (F1595) | The sales order stock is displayed in the column Unrestricted Stock, sales order number is displayed in the column Sales Order. |
| [Schedule Application Job to Create Stock Transport Order](#unique_23) [page ] 31 | Purchaser (Retail) | Schedule Purchasing Jobs - Advanced (F1702) | Stock transport order (STO) is created for transfer of stock from distribution center to store. |
| [Create Stock Transport Order (Optional)](#unique_24) [page ] 32 | Purchaser (Retail) | Create Purchase Order - Advanced (ME21N) | Stock transport order (STO) is created with reference to the purchase requisition for transfer of stock from distribution center to store, manually. |
| [Schedule Application Job to Create Replenishment Delivery for STO](#unique_25) [page ] 33 | Shipping Specialist | Schedule Delivery Creation (F2228) | Outbound delivery document with reference to STO, is created |
| [Pick, Pack, and Post Goods Issue for Replenishment Delivery from DC](#unique_26) [page ] 34 | Shipping Specialist | Change Outbound Delivery (VL02N) | Material (Article) is picked then packed. Handling units are generated. Goods issue is posted for the outbound delivery from the distribution center. |
| [In-Store Operations](#unique_27) [page ] 36 |  |  |  |
| [Post Goods Receipt for STO/Outbound Delivery](#unique_28) [page ] 36 | Retail Store Associate | Receive Products (F1248) | Goods receipt is posted against the stock transport order document or outbound delivery received at Store. Store associate is notified about stock reservation. After GR is posted, the stock is managed as sales order stock in the store. |
| [Start Picking](#unique_29) [page ] 37 | Retail Store Associate | Process Picking Requests (F4643) | Picking is started for the selected store picking requests, product GTIN is scanned and handover shelf is assigned to the picking request. |
| [Verify Consumer Order Details](#unique_30) [page ] 39 | Retail Store Associate | Hand Over Orders (F4639) | Details of the selected order and the status of order placed in the handover shelf is displayed. Also, order withdrawal is done and Order is handed over to the consumer. |
| [Validate Sales Order Document and Subsequent Document Flow (Optional)](#unique_31) [page ] 42 | Retail Store Associate | Manage Sales Orders (F1873) | Validate the updates on the sales order also the subsequent documents generated after completion of the picking and handover process. |

Sell from Online Store, Delivery from Distribution Center to Customer (Pre-Paid Order)

| Process Step | Business Role | App | Expected Results |
| --- | --- | --- | --- |
| [Create Sales Order](#unique_32) [page ] 43 | Internal Sales Representative | Create Sales Orders - VA01 (VA01) | Sales orders in SAP S/4HANA Cloud Public Edition Starter System is simulated. |
| [Back-Office Operations in Distribution Center](#unique_33) [page ] 45 |  |  |  |
| [Schedule Application Job for Outbound Delivery Creation](#unique_34) [page ] 45 | Shipping Specialist | Schedule Delivery Creation (F2228) | Background job for outbound delivery document creation is scheduled. |
| [Pick, Pack and Post Goods Issue for Outbound Delivery from Distribution Center](#unique_35) [page ] 47 | Shipping Specialist | Change Outbound Delivery (VL02N) | Material (Article) is picked then packed. Handling units are generated. Goods issue is posted for the outbound delivery from the distribution center. |
| [Create Billing Document](#unique_36) [page ] 48 | Billing Clerk | Create Billing Documents (F0798) | Billing document with reference to outbound delivery, is created. |
| [Validate Follow-On Documents (Optional)](#unique_37) [page ] 49 | Retail Store Associate | Manage Sales Orders (F1873) | Successful creation of outbound delivery, goods issue and billing document is validated. |

## Test Procedures

This chapter describes the test procedures for each process step that belongs to this scope item.

### Click and Reserve - Order Fulfillment in Store (Stock is Available in the Store)

#### Create Sales Orders

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
| Note In a real-time scenario, sales orders can be created in the SAP S/4HANA Cloud Public Edition system through an inbound service (for example, Sales Order (A2A) API) integration with the third-party web shop.However, for testing purposes, we recommend using the Manage Sales Orders (F1873) app as outlined in the test procedure below. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Log onto the SAP Fiori Launchpad as an Internal Sales Representative. |  |  |
| 2. | Access the App | Open app. | Manage Sales Orders (F1873) screen is displayed. |  |
| 3 | Go to App | On the Manage Sales Order screen, select Create > Create Sales Order VA01 option. | Create Sales Documents screen is displayed. |  |
| 4 | Enter data | Enter the following data:Order Type: ORSales Organization: 3310Distribution Channel: 60Division: 00Select Continue. | Create Standard Order: Overview screen is displayed |  |
| 5 | Enter Header Data | In the header section, enter Sold-to Party: 33113005 and press EnterNow, in the Address From Master Data for Sold-to Party (Document Header) pop-up, enter <Name> in the Name section and <Telephone number> under the Communication section, then press EnterAlso enter Customer References:<Reference Document ID>, for instance, Customer PO number.Note Leave as blank if no reference needs to be maintained.Select Display header details, navigate to Shipping tab view and enterShipping Cond.: 02 Pick-up |  |  |
| 6 | Enter Item Data | Select Back to navigate back to the Create Standard Order: Overview screen.In the All Items table, enter the following details in different rows:Row1:Material: R_2000Order Quantity: <Order Quantity>Item Category: TANPlant: 3340Row2:Material: R_4017Order Quantity: <Order Quantity>Item Category: TANPlant: 3340Row3:Material: R_1039Order Quantity: <Order Quantity>Item Category: TANPlant: 3340Row4:Material: R_1003001Order Quantity: <Order Quantity>Item Category: TANPlant: 3340 |  |  |
| 7 | Save the Order | Select Save.Note the order number for further use. | Sales order is saved and Standard Order <order number> has been saved success message is displayed. |  |

#### Start Picking

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

#### Look Over the Order Details for Handover

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

#### Validate Sales Order Document and Subsequent Document Flow (Optional)

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

#### Process Customer Order Payment from POS

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

### Click and Collect (Pre-Paid Order)- Order Fulfillment from Distribution Center to Store (Stock is Not Available in the Store)

#### Create Sales Order

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
| Note In a real-time scenario, sales orders can be created in the SAP S/4HANA Cloud Public Edition system through an inbound service (for example, Sales Order (A2A) API) integration with the third-party web shop.However, for testing purposes, we recommend using the Manage Sales Orders (F1873) app as outlined in the test procedure below. |

Prerequisite

Ensure the SAP digital payments scope is activated to manage payments for sales orders before following the test procedure below. For more information, see [Business Conditions](#unique_7) [page ] 7.

|  |
| --- |
| Note If you do not wish to use SAP digital payment capabilities, refer to [Create Sales Order](#unique_39) [page ] 51 for more information. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as an Internal Sales Representative . |  |  |
| 2 | Access the App | Open Manage Sales Orders (F1873) app. | Manage Sales Orders (F1873) screen is displayed. |  |
| 3 | Go to App | On the Manage Sales Order screen, select Create > Create Sales Order VA01 option. | Create Sales Order pop-up is displayed. |  |
| 4 | Enter data | Enter the following data:Order Type: ORSales Organization:3310Distribution Channel: 60Division: 00Choose Continue. | Create Standard Order: Overview screen is displayed |  |
| 5 | Enter Header Data | In the header section, enter Sold-to Party:33113005 and press EnterNow, in the Address From Master Data for Sold-to Party (Document Header) pop-up, enter <Name> in the Name section and <Telephone number> under the Communication section, then press Enter.Also enter Customer References:<Reference Document ID>, for instance, Customer PO number.Note Leave as blank if no reference needs to be maintained.Choose Menu > Goto > Header > Shipping and enter Shipping Cond.: 02 Pick-up. |  |  |
| 6 | Enter Item Data | Choose Back button to navigate back to the Create Standard Order: Overview screen.In the All Items table, enter the following details in two different rows:Row1:Material: R_2000Order Quantity: <Order Quantity>Item Category: CBABPlant: 3340Press Enter.Select the item. Then choose Menu > Goto > Item > Schedule Lines .Enter Sched. Line Cat.: CUPress Enter.On the Standard Order: Purchase Order Scheduling screen, choose Copy button in the Dely proposal section.Row2:Material: R_4017Order Quantity: <Order Quantity>Item Category: CBABPlant: 3340Press Enter.Select the item. Then choose Menu > Goto > Item > Schedule Lines .Enter Sched. Line Cat.: CUPress Enter.On the Standard Order: Purchase Order Scheduling screen, choose Copy button in the Dely proposal section.Row3:Material: R_1039Order Quantity: <Order Quantity>Item Category: CBABPlant: 3340Press Enter.Select the item. Then choose Menu > Goto > Item > Schedule Lines .Enter Sched. Line Cat.: CU.Press Enter.On the Standard Order: Purchase Order Scheduling screen, choose Copy button in the Dely proposal section.Row4:Material: R_1003001Order Quantity: <Order Quantity>Item Category: CBABPlant: 3340Press Enter.Select the item. Then select Menu > Goto > Item > Schedule Lines .Enter Sched. Line Cat.: CU.Press Enter.On the Standard Order: Purchase Order Scheduling screen, choose Copy button in the Dely proposal section. |  |  |
| 7 | Navigate to Header Data | In the header section, choose Display Header Details icon. | Create Standard Order: Header Data screen is displayed. |  |
| 8 | Assign Payment Card | Navigate to Electronic Payments tab. Choose Assign Payment Card button. | Payment Page is displayed in a new browser tab. |  |
| 9 | Enter Payment Card details | Enter the following information on the Payment Page browser tab:Credit Card Type: VISACard Number : 4111111111111111Name on Card : <Enter card holder's name>Valid To : <Any Valid Future Month and Year >CVC: 111Choose Submit . Then choose Close on the Your payment card was successfully registered. message. Navigate back to the Create Standard Order: Header Data screen and choose Confirm on the Assign Payment Card pop-up.Choose Back button to navigate back to the Create Standard Order: Overview screen. | Payment Card is added, and its details are displayed in the Electronic Payments table. |  |
| 10 | Save the Order | Choose Save.Note the order number for further use. | Sales order is saved and Standard Order <order number> has been saved success message is displayed. |  |
| 11 | Access the App | Open Create Sales Orders (F3893) | Create Sales Orders (F3893) app is displayed. |  |
| 12 | Note the Purchase Requisition Number per Sales Order Item | On the Create Sales Orders (F3893) screen, enter Sales Order : <the sales order number created previously> and choose Go.Select the resulting sales order. Then select an item and Display Item Details and go to Schedule Lines tab.Make a note of the purchase requisition number for all the sales order items. |  |  |

Next Steps

[Check Stock Overview](#unique_22) [page ] 30

#### Back-Office Operations from Distribution Center to Store

This section describes the back-office process which starts with moving product stock from unrestricted use of Distribution Center (DC) to sales order stock. After this the stock transport requisition is converted to stock transfer order (STO), followed by replenishment delivery creation via scheduled job and finally picking, packing and issue of goods from DC to store.

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
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser (Retail) |  |  |
| 2 | Access the App | Navigate to Schedule Purchasing Jobs - Advanced (F1702) app | Navigate to Schedule Purchasing Jobs - Advanced (F1702) app screen is displayed. |  |
| 3 | Create new job | Choose Create to create a new application job | New Job: Automatic creation of Purchase Orders from Requisitions screen is displayed |  |
| 4 | Enter job details | Enter the application job details in the Template Information and Scheduling Options sections (Step 1).Job Template: Automatic creation of Purchase Orders from RequisitionJob Name: Automatic creation of Purchase Orders from RequisitionChoose Step 2Flag Start ImmediatelyChoose Define Recurrence Pattern if required to change the Recurrence. | The Template Information and scheduling options are defined |  |
| 5 | Enter the Parameters | Choose Step 3In the Parameter section,Flag Per Requisition in New Purchase Order sectionMake the following entries in Item Specific Selection section (For Testing Purpose)Purchase Requisition: <Enter your stock transport requisition number> | Parameters are entered |  |
| 6 | Check | Choose Check | Message is displayed indicating you can go ahead and schedule job. |  |
| 7 | Schedule | Choose Schedule | Automatic creation of Purchase Order from Requisition has been scheduledThe Application Jobs screen is displayed again, and the new job displays in the Jobs table |  |
| 8 | Navigate to Results | Check the newly create job row and choose the icon Navigate to the job Results in Results column | Document (ID XXXXXXX) screen is displayed stock transport order number. |  |

##### Create Stock Transport Order (Optional)

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
| 3 | Enter Order Document Type and other data | Enter the following data, then choose Enter.Order Type: StockTranspOrderDel or UD StockTranspOrderDel Supplying Plant: 3350On the Header / Org. Data tab:Company Code: 3310Purchasing Org.: 3310Purchasing Group: 001In Item Overview section:Purchase Requisition: <Enter your stock transport requisition number created above in section [Create Sales Order](#unique_20) [page ] 26 of this documentQuantity: xNote Price should be determined automatically from purchasing info record | All data are entered, the item detail screen is displayed. |  |
| 4 | Save Stock Transfer Order | Choose the Save button and when the stock transfer order number is displayed, write it down for further use. | A new stock transfer order is created. Order Number is displayed. |  |

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

Next Steps

[Post Goods Receipt for STO/Outbound Delivery](#unique_28) [page ] 36

#### In-Store Operations

This section describes the process of goods receipt in store from the DC, followed by picking and handover of order and finally validating the updates on sales order and subsequent documents generated as part of the process.

##### Post Goods Receipt for STO/Outbound Delivery

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

##### Start Picking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The step explains the process of initiating product picking in a store. Picking process involves single picking request or multiple picking requests. For an optimized picking experience, the list page sorts the oldest picking request first and then the picking request that got created recently and so on. You can also print box labels and content lists during the picking process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Retail Store Associate. |  |  |
| 2 | Access App | Open Process Picking Requests (F4643) app. | Process Picking Requests (F4643) app screen is displayed along with a list of picking requests. |  |
| 3 | Select picking requests and start picking | Select picking requests in one of the following ways:Picking requests are queued in ascending order of their date of creation.To start picking the requests which came in first, select the checkboxes against the picking request numbers from the top of the list.If picking request of a particular status must be picked, for instance, picking requests with status Picking in Process or Not Picked. Select Filter Set the filter based on Status in the Select Filter pop- up,then select the resulting picking requests.If sales order number, Customer Reference or Your Reference for Sold-to Party maintained in the sales order is known then, enter either of these in the search field and select Search, then select the resulting picking requests.Label printing is applicable only when multiple picking requests are selected for picking process.After selecting the picking request, select Start Picking. | The Process Picking Requests (F4643) app will be redirected to the next page. Label printing for the selected picking request is triggered.List of products belonging to selected picking request is displayed with details like quantity and product GTIN. Products Picked indicator will be displayed on the left top.Note Label printing is applicable only when multiple picking requests are selected for picking process. |  |
| 4 | Scan Product GTIN and Provide Product Quantity | Choose Scan GTIN on the bottom of the screen and scan using the camera on the device.Enter product quantity based on the following cases:Case 1: For product which has a unit of measure (UoM) for which quantities can be in decimal, for example, if UoM in L(Litre), KG (Kilogram), etc. Choose Scan Bar Code on the bottom of the screen and scan product barcode using the camera on the device or manually enter product barcode number in the Enter Bar Code pop-up and choose OK.Note Product Bar Code is product GTIN number(13 Digits ) plus weight of product(5 Digits) , for instance, the barcode should be as follows to recognise decimal/whole quantities of a product: <GTIN> + 10000 = 100.00 kg <GTIN> + 00100 = 1.00 kg <GTIN> + 01000 = 10.00 kg<GTIN> + 00150 = 1.5 kg <GTIN> + 00050 = 0.50 kgi.e., if the product GTIN is ‘2150500000000’ and the weight/quantity to be picked is ‘1.5’, then the barcode would be ‘215050000000000150’.Case 2: For product which has a unit of measure (UoM) for which quantities can only be whole, for example, if UoM in EA(Each), PC(Piece), etc.Enter the quantity manually or use - and + to decrease/increase the quantity in Picked Qty in Base UoM column. | Case 1: The Picked Qty in Base UoM and Price column values are updated.Case 2: Picked quantity is entered for the product.Note Case 1: If you enter a wrong barcode then system displays You have not scanned GTIN of Requested product error message.Case 2: Ordered quantity is the maximum allowed quantity that can be entered while the minimum allowed is zero.If picked quantity is lesser (lesser than the lower tolerance limit) than the ordered quantity, then R3 Out of Stock will be set as Rejection Reason for Short Picking, for the corresponding sales order item in the background. |  |
| 5 | Scan Picking Request | Select Scan Picking Request (if multiple picking requests are selected for picking) at the bottom right of the screen and scan the picking request barcode on the box label using the camera on the device or manually enter the picking request barcode number in the Enter Bar Code pop-up and choose OK.orSelect OK (if single picking request is selected for picking) at the bottom right of the screen. | Picking request number is scanned. If wrong picking request number is entered, then Scanned picking request not found error message is displayed to userNote If a product must be placed into different picking containers, then the user is asked to scan and place the respective quantity of product into their corresponding picking container one after the other. |  |
| 6 | Assign Picking Container to Handover Shelf | Scan all items in the picking requestSelect Print Content List on the bottom right of the screen. On the Reprint Content List pop-up select the picking request for which content list must be reprinted and then choose Reprint.Following are the two scenarios based on which handover shelf is assigned on the Handover Shelf screen:Scenario 1: If single picking request is selected:Select the picking request to which handover shelf is to be assignedOn the Information pop-up choose Scan and scan the handover shelf barcode using camera in the device or enter the barcode manually in the Enter Bar Code pop-up and choose OK.Scenario 2: If multiple requests are selected:Select Scan Picking Request at the bottom of the screen and scan the picking request number using the camera in the device.On the Information pop-up choose Scan and scan the handover shelf barcode using camera in the device or enter the barcode manually in the Enter Bar Code pop-up and choose OK.Select Pick More on the success pop-up to pick more requests. Or Select All Done on the success pop-up if picking of all requests is completed | Once all the products in picking request are scanned and placed in a picking container, Products Picked indicator is updated and progressed to full. Product list is also updated.After the last product of the products list is scanned and placed in the picking container, the message pop-up Content list have been printed for picking requests is displayed.Note Note If products belonging to a picking request is completely unavailable, then that picking request is not shown on the Handover Shelf screen. Also, the content list is not printed for that picking request.Reprint of content list is triggered for the selected picking request.You are navigated back to the Picking Requests screen to select and start picking of new requests, if Pick More is selected OrYou are navigated back to the SAP Fiori launchpad if All Done is selected. |  |

##### Verify Consumer Order Details

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
| 3 | Go to App | On the Manage Sales Order screen, enter <your sales order number> in the Sales Order field. Select Go | Sales order line item is displayed in the search result. |  |
| 4 | Open the order details | Select the sales order line item. | Display Standard Order XXXXX: Overview screen is displayed. |  |
| 5 | Navigate to Document Flow | Select Display Document Flow, to investigate the details of the subsequent document, for example, outbound delivery, goods issue, invoice documents, material and accounting documents, select the document and choose Display Document. | Generated documents are displayed on the Document Flow screen. Further, selected documents are displayed to investigate the details. |  |

### Sell from Online Store, Delivery from Distribution Center to Customer (Pre-Paid Order)

#### Create Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create a sales order with necessary details as per your business requirement.

|  |
| --- |
| Note In a real-time scenario, sales orders can be created in the SAP S/4HANA Cloud Public Edition system through an inbound service (for example, Sales Order (A2A) API) integration with the third-party web shop.However, for testing purposes, we recommend using the Manage Sales Orders (F1873) app as outlined in the test procedure below. |

Prerequisite

Ensure the SAP digital payment scope is activated to meet the prepaid order requirements from the distribution center.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Internal Sales Representative. |  |  |
| 2 | Access the App | Open Manage Sales Orders (F1873) app. | Manage Sales Orders (F1873) screen is displayed. |  |
| 3 | Go to App | On the Manage Sales Orders (F1873) screen, select Create > Create Sales Order VA01 option. | Create Sales Documents screen is displayed. |  |
| 4 | Enter data | Enter the following data:Order Type: ORSales Organization: 3310Distribution Channel: 60Division: 00Select Continue. | Create Standard Order: Overview screen is displayed |  |
| 5 | Enter Header Data | In the header section, enter Sold-to Party: 33113005 and press EnterNow, in the Address From Master Data for Sold-to Party (Document Header) pop-up, enter <Name> in the Name section and <Telephone number> under the Communication section, then press EnterAlso enter Customer References:<Reference Document ID>, for instance, Customer PO number.Note Leave as blank if no reference needs to be maintained.Select Display header details, navigate to Shipping tab view and enter Shipping Cond.: 01 Standard |  |  |
| 6 | Enter Item Data | Select Back to navigate back to the Create Standard Order: Overview screen. In the All Items table, enter the following details in different rows and press ENTER:Row1:Material: R_2000Order Quantity: <Order Quantity>Item Category: TANPlant: 3350Row2:Material: R_4017Order Quantity: <Order Quantity>Item Category: TANPlant: 3350Row3:Material: R_1039Order Quantity: <Order Quantity>Item Category: TANPlant: 3350Row4:Material: R_1003001Order Quantity: <Order Quantity>Item Category: TANPlant: 3350 |  |  |
| 7 | Navigate to Header Data | In the header section, select Display Header Details icon. | Create Standard Order: Header Data screen is displayed. |  |
| 8 | Assign Payment Card | Navigate to Electronic Payments tab, select Assign Payment Card button. Grant access by selecting Allow on the SAP GUI Security pop-up | Payment Page is displayed in a new browser tab. |  |
| 9 | Enter Payment Card details | Enter the following information on the Payment Page browser tab:Credit Card Type: VISACard Number : 4111111111111111Name on Card : <Enter card holder's name>Valid To : <Any Valid Future Month and Year >CVC: 111Select Submit then select Close on the Your payment card was successfully registered message Navigate back to the Create Standard Order: Header Data screen and select Confirm on the Assign Payment Card pop-up.Select Back button to navigate back to the Create Standard Order: Overview screen. | Payment Card is added, and its details are displayed in the Electronic Payments table. |  |
| 10 | Save the Order | Select Save.Note the order number for further use. | Sales order is saved and Standard Order <order number> has been saved success message is displayed. |  |

#### Back-Office Operations in Distribution Center

##### Schedule Application Job for Outbound Delivery Creation

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
| 5 | Enter the Parameters | Choose Step 3In the Parameter section,Make the following entries in Sales Order section (For Testing Purpose)SD Document: <Enter your sales order document number created above in chapter [Create Sales Order](#unique_32) [page ] 43 of this document> | Parameters are entered |  |
| 6 | Check | Choose Check | Message is displayed indicating you can go ahead and schedule job. |  |
| 7 | Schedule | Choose Schedule | Automatic creation of Sales Order has been scheduled message is displayed.The Application Jobs screen displays again, and the new job displays in the Jobs table. |  |
| 8 | Check Delivery Creation Job Log | On the Application Jobs screen, after job item’s status turned to Finish, choose Status symbol in the Log column.Note Choose the Magnifier, and the job list will refresh. | The job log details is displayed. |  |

##### Pick, Pack and Post Goods Issue for Outbound Delivery from Distribution Center

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
| 6 | Open Outbound Delivery document again | On the Change Outbound Delivery (VL02N) app screen, enter <your outbound delivery document number> and choose Pack. |  |  |
| 7 | Enter Packaging Material | On the Processing of Handling Units for Outbound Delivery <Outbound Delivery Number> screen, under the Pack Material tab and under All Existing HUs (Available for Packing), enter <Your packaging Material> in the Packaging Materials column. | Handling units are generated. |  |
| 8 | Pack Material with Packaging Material | Mark the material and handling unit line items under Materials to Be Packed and All Existing HUs (Available for Packing) sections, respectively. Choose Pack. | The message Material was Packed is displayed. |  |
| 9 | Save the Outbound Delivery document | Select Save. | Outbound delivery document is saved. |  |
| 10 | Post Goods Issue | On the Change Outbound Delivery (VL02N) app screen, enter <your outbound delivery document number> and choose Post Goods Issue. | Goods issue is successful. Inventory stock is reduced from the supplying plant. |  |

##### Create Billing Document

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

Table 2:

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

##### Validate Follow-On Documents (Optional)

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

## Appendix

### Optional Scenarios

Prerequisites

To carry out the following activities, the business role SAP_BR_RFM_STORE_ASSOCIATE must be assigned to the user.

#### Create Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If you prefer not to activate the SAP digital payments scope items, you must implement the BAdI Maintain Sales Order Payment Status (RFM_STORE_PICK_ORD_PAYT_STS) to maintain the payment status of the click-and-collect sales order.

|  |
| --- |
| Note Refer to the Setting Up Omnichannel Order Fulfillment for Retail (5FZ)) for how to define your payment terms before proceeding with the test procedure below. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Log onto the SAP Fiori Launchpad as an Internal Sales Representative . |  |  |
| 2. | Access the App | Open Manage Sales Orders (F1873) app. | Manage Sales Orders (F1873) screen is displayed. |  |
| 3 | Go to App | On the Manage Sales Order screen, select Create > Create Sales Order VA01 option. | Create Sales Order pop-up is displayed. |  |
| 4. | Enter data | Enter the following data:Order Type: ORSales Organization:3310Distribution Channel: 60Division: 00Select Continue. | Create Standard Order: Overview screen is displayed |  |
| 5. | Enter Header Data | In the header section, enter Sold-to Party:33113005 and press EnterNow, in the Address From Master Data for Sold-to Party (Document Header) pop-up, enter <Name> in the Name section and <Telephone number> under the Communication section, then press EnterAlso enter Customer References:<Reference Document ID>, for instance, Customer PO number.Note Leave as blank if no reference needs to be maintained.Under the Sales tab view, enter: Pyt Terms: RPT1 (Prepaid Commerce Orders)Select Menu > Goto > Header > Shipping and enter Shipping Cond.: 02 Pick-up |  |  |
| 6 | Enter Item Data | Select Back button to navigate back to the Create Standard Order: Overview screenIn the All Items table, enter the following details in two different rows:Row1:Material:R_2000Order Quantity: <Order Quantity>Item Category: CBABPlant: 3340Press EnterSelect the item then select Menu > Goto > Item > Schedule Linesand enter Sched. Line Cat.: CUPress EnterOn the Standard Order: Purchase Order Scheduling screen select Copy button in the Dely proposal section.Row2:Material:R_4017Order Quantity: <Order Quantity>Item Category: CBABPlant: 3340Press EnterSelect the item then select Menu > Goto > Item > Schedule Linesand enter Sched. Line Cat.: CUPress EnterOn the Standard Order: Purchase Order Scheduling screen select Copy button in the Dely proposal section.Row3:Material:R_1039Order Quantity: <Order Quantity>Item Category: CBABPlant: 3340Press EnterSelect the item then select Menu > Goto > Item > Schedule Linesand enter Sched. Line Cat.: CUPress EnterOn the Standard Order: Purchase Order Scheduling screen select Copy button in the Dely proposal section.Row4:Material:R_1003001Order Quantity: <Order Quantity>Item Category: CBABPlant: 3340Press EnterSelect the item then select Menu > Goto > Item > Schedule Linesand enter Sched. Line Cat.: CUPress EnterOn the Standard Order: Purchase Order Scheduling screen select Copy button in the Dely proposal section. |  |  |
| 7 | Save the Order | Select Save.Note the order number for further use. | Sales order is saved and Standard Order <order number> has been saved success message is displayed. |  |
| 8 | Access the App | Open Create Sales Orders (F3893) | Create Sales Orders (F3893) app is displayed. |  |
| 9 | Note the Purchase Requisition Number per Sales Order Item | On the Create Sales Orders (F3893)screen, enter Sales Order : <the sales order number created previously> and select Go.Select the resulting sales order then select an item and Display Item Details and go to Schedule Lines tab.Make a note of the purchase requisition number for all the sales order items. |  |  |

Next Steps

- [Back-Office Operations from Distribution Center to Store](#unique_21) [page ] 30
- [In-Store Operations](#unique_27) [page ] 36

#### Select Withdraw

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

|  |
| --- |
| NoteThis process step must be followed when, in the Define Schema for Handover Orders (Optional) in Set Up Instruction Omnichannel Order Fulfillment for Retail(5FZ) configuration activity, Customizing Schema - 0002 is assigned to your store.For more information related to viewing the configuration or assignment of your store to the existing configuration, please refer to the chapters Define Schema for Handover Orders (Optional) and Assign Handover Orders Schema to Store (Optional) in Set Up Instruction Omnichannel Order Fulfillment for Retail(5FZ).This process step is an alternative to the process step Scan the Picking Request to Withdraw described in chapter Look Over the Order Details for Handover of this document, for withdrawal of picking container from the handover shelf. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Pre-Process Steps for Withdrawal | As a prerequisite, repeat the process steps mentioned in chapters Create Sales Orders, Start Picking and Look Over the Order Details for Handover |  |  |
| 2 | Select Handover Status | Select Handover Status on the top right of the screen.Note Reservation Hand Over (in case of unpaid orders) and Cancel Order buttons on the bottom of the screen is enabled once the entire order is withdrawn. | Handover Status pop-over screen is displayed containing the list of Picking Request, Picking Request Status their corresponding Handover Shelf Space numbers and the Withdraw hyperlink. |  |
| 3 | Select Withdraw hyperlink to withdraw | Select Withdraw hyperlink against the Handover Shelf Space and select Done. | The picking request is withdrawn from the handover shelf space or bin, the hyperlink text changes to Withdrawn and the user is navigated back to the Exceptions tab view. |  |
| 4 | Post-Process Steps to complete handover. | Repeat the process step Hand Over Orders in thr chapter Look Over the Order Details for Handover till Process Customer Order Payment from POS to complete the handover process. |  |  |

#### Take Over Picking Request from Another Store Associate

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to take over the picking requests from another store associate whose picking was in process. In this scenario, a store associate could not complete picking due to some reason and willing to hand over the picking requests to the colleague.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Retail Store Associate. |  |  |
| 2 | Access App (Optional) | Open Process Picking Requests (F4643) app.Note Ignore this step if you are already on the Process Picking Requests (F4643) app. | Process Picking Requests (F4643) app screen is displayed along with a list of picking requests |  |
| 3 | Select Take Over | Select Take Over on the right side above the list of picking requests on the Picking Request screen. | Picking Requests Takeover pop-up is displayed, displaying a list of picking requests being processed by other store associates of the store. |  |
| 4 | Search for the picking request to be taken over | Enter <the username of the associate processing the picking request> in Search or simply look for the picking request number in the list to be taken over. |  |  |
| 5 | Select and assign the picking request | Select the checkbox against the picking request number to be taken over and then choose OK. | Selected picking requests are assigned to you message is displayed and the selected picking requests are assigned to you. |  |

#### Unassign Picking Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process steps shows how you can unassign the picking requests from your list of picking requests while picking is yet to be started for the picking request.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Retail Store Associate. |  |  |
| 2 | Access App | Open Process Picking Requests (F4643) app. |  |  |
| 3 | Select picking requests and start picking | Select picking requests which has to be unassigned from your user, by selecting the checkboxes against the picking request numbers.After selecting the picking request, select Start Picking. | The Process Picking Requests (F4643) app will be redirected to the next page. |  |
| 4 | Select Unassign | Choose Unassign on the top right side of the left navigation pane. | Confirmation pop-up is displayed. |  |
| 5 | Confirm Unassignment | Select OK on the Confirmation pop-up to unassign user. | You are unassigned from the selected picking requests message is displayed. The picking request will be unassigned from your user. Also, status of the picking request is reverted to Not Picked. |  |

#### Reassign Picking Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows how to reassign the picking requests which is to another user (retail store associate).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Retail Store Associate. |  |  |
| 2 | Access App | Open Process Picking Requests (F4643) app. |  |  |
| 3 | Select picking requests and start picking | Select picking requests which has to be reassigned to another user, by selecting the checkboxes against the picking request numbers.After selecting the picking request, select Start Picking. | The Process Picking Requests (F4643) app will be redirected to the next page. |  |
| 4 | Select Reassign | Choose Reassign on the top right side of the left navigation pane. | Reassign User pop-up is displayed displaying the list of store associates to whom picking requests can be reassigned. |  |
| 5 | Search for the associate to whom picking request need to be reassigned | Enter <username> in Search or simply look for the store associate. |  |  |
| 6 | Select and reassign the picking request | Select the radio button against the <store associate name> to whom picking request number is to be reassigned and then select OK. | Selected picking requests are reassigned to <store associate name> message is displayed, and your picking requests will be reassigned to the selected store associate with the picking request status being Picking in Process. |  |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Retail Store Associate. |  |  |
| 2 | Access App | Open Process Picking Requests (F4643) app. |  |  |
| 3 | Scan all items | Scan all items in the picking request | Once all the products in picking request are scanned and placed in a picking container, Products Picked indicator is updated and progressed to full. Product list is also updated.After the last product of the products list is scanned and placed in the picking container, the message pop-up Content list have been printed for picking requests is displayed.Note If products belonging to a picking request is completely unavailable, then that picking request is not shown on the Handover Shelf screen. Also, the content list is not printed for that picking request. |  |
| 4 | Reprint content list(Optional) | Select Print Content List in the bottom right of the screen. On the Reprint Content List pop-up select the picking request for which content list must be reprinted and then select Reprint. | Reprint of content list is triggered for the selected picking request. |  |
| 5 | Finish picking or Pick More | Select Pick More on the Handover Shelf screen to pick more requests. Or Select All Done on the Handover Shelf screen if picking of all requests is completed | You are navigated back to the Picking Requests screen to select and start picking of new requests, if Pick More is selected OrYou are navigated back to the SAP Fiori launchpad if All Done is selected . |  |

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
> Flagged while digesting this document, not verified: The BAdI for click-and-collect sales order payment status is named RFM_STR_PICK_ORD_PAYT_STS_MOD in the Business Conditions note but RFM_STORE_PICK_ORD_PAYT_STS in the Appendix Create Sales Order purpose; the two names differ within the same document.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[15-retail-operations/in-store-customer-order-management-3hu-ae-test-script-sap-s-4hana-clou]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5FZ_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 110,889 chars in the whole document
