---
id: 15-retail-operations/empties-for-retail-5fk-ae-test-script-sap-s-4hana-cloud-public-edition-part-01
title: "Empties for Retail (5FK_AE) - Test Script, SAP S/4HANA Cloud Public Edition (5FK_S4CLD2608_BPD_EN_AE) — part 1 of 2"
description: "Test script for SAP S/4HANA Cloud scope item 5FK_AE Empties for Retail: prerequisites, master data, procurement, returns, inventory, store order fulfillment."
cluster: 15-retail-operations
tags: [kb/retail-operations, topic/empties-management-retail]
aliases: []
keywords: [Empties Management for Retail, empties handling, empties bill of material, article master data, price conditions, procurement from supplier, stock transfer orders, returns processing, physical inventory, stock adjustment]
sources: ["raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5FK_S4CLD2608_BPD_EN_AE.docx#lines-1-3124"]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1080
topic: 15-retail-operations/empties-management-retail
language: EN
part: 1/2
created: 2026-10-12
updated: 2026-10-12
---

# Empties for Retail (5FK_AE) - Test Script, SAP S/4HANA Cloud Public Edition (5FK_S4CLD2608_BPD_EN_AE) — part 1 of 2

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5FK_S4CLD2608_BPD_EN_AE.docx`, part 1 of 2 (lines 1–3124 of the extracted text), extracted with `mammoth`. Grouped under **Empties Management for Retail** in Retail Operations. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Empties for Retail (5FK_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Empties for Retail (5FK_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 5](#_Toc232856486)

[2 Prerequisites 6](#_Toc232856487)

[2.1 System Access 6](#_Toc232856488)

[2.2 Roles 6](#_Toc232856489)

[2.3 Master Data, Organizational Data, and Other Data 7](#_Toc232856490)

[2.4 Business Conditions 9](#_Toc232856491)

[2.5 Preliminary Steps 9](#_Toc232856492)

[2.5.1 Create Purchase Conditions for Empties 9](#_Toc232856493)

[2.5.2 Create Sales Conditions for Empties 10](#_Toc232856494)

[2.5.3 Create Sales Conditions for Full Article 12](#_Toc232856495)

[2.5.4 Extend Articles to E-Commerce Channel 14](#_Toc232856496)

[2.5.4.1 Extend Empties 14](#_Toc232856497)

[2.5.4.2 Extend Full Article 16](#_Toc232856498)

[2.5.5 My Store Assignment 18](#_Toc232856499)

[2.5.6 In-Store Inventory Management 19](#_Toc232856500)

[2.5.6.1 Configure Define Basic Settings for Count Stock Ad hoc 19](#_Toc232856501)

[2.5.6.2 Display Physical Inventory Document 20](#_Toc232856502)

[2.5.6.3 Delete Active Physical Inventory Document (Optional) 21](#_Toc232856503)

[2.5.6.4 Overview of Stock for Single Material 22](#_Toc232856504)

[2.5.6.5 Analyze Stock Overview for Empties 22](#_Toc232856505)

[2.5.6.6 Set Initial Stock for Article (Optional – Only if Stock not Available) 23](#_Toc232856506)

[2.5.6.7 Set up the Printer 25](#_Toc232856507)

[2.5.7 In-Store Customer Order Management 25](#_Toc232856508)

[2.5.7.1 Customer Maintenance Settings 25](#_Toc232856509)

[2.5.7.1.1 Define Schema for Customer Maintenance (Optional) 25](#_Toc232856510)

[2.5.7.1.2 Assign Template Customer to Schema 26](#_Toc232856511)

[2.5.7.1.3 Assign Schema to Store 27](#_Toc232856512)

[2.5.7.1.4 Define Grouping Schema and Assign Countries (Optional) 28](#_Toc232856513)

[2.5.7.1.5 Assign Grouping Schema to Store 29](#_Toc232856514)

[2.5.7.2 Create Initial Stock 29](#_Toc232856515)

[2.5.7.3 Maintain Application Settings 30](#_Toc232856516)

[2.5.7.4 Maintain Default Settings 31](#_Toc232856517)

[3 Overview Table 33](#_Toc232856518)

[4 Test Procedures 40](#_Toc232856519)

[4.1 Create Master Data for Empties and Full Article (Optional) 40](#_Toc232856520)

[4.1.1 Create Empties and Full Article 40](#_Toc232856521)

[4.1.1.1 Create Empties 40](#_Toc232856522)

[4.1.1.2 Create Full Article and Maintain Components 49](#_Toc232856523)

[4.1.2 Maintain Assortments for Full Article 64](#_Toc232856524)

[4.1.2.1 Assign Full Article to Assortment Module 64](#_Toc232856525)

[4.1.2.2 Assign Full Article to Distribution Center 65](#_Toc232856526)

[4.1.3 Create Purchase Conditions for Empties 66](#_Toc232856527)

[4.1.4 Create Sales Conditions for Empties 68](#_Toc232856528)

[4.1.5 Create Sales Conditions for Full Article 69](#_Toc232856529)

[4.2 Procurement from External Supplier (Full Article) 72](#_Toc232856530)

[4.2.1 Create Purchase Order Directly 72](#_Toc232856531)

[4.2.2 Create Inbound Delivery 73](#_Toc232856532)

[4.2.3 Confirm Quantities for Putaway 74](#_Toc232856533)

[4.2.4 Post Goods Receipt for Inbound Delivery 75](#_Toc232856534)

[4.2.5 Analyze Stock Overview (Optional) 76](#_Toc232856535)

[4.2.6 Analyze Stock Overview for Empties 77](#_Toc232856536)

[4.3 Store Ordering from Distribution Center (Full Article) 77](#_Toc232856537)

[4.3.1 Create Stock Transfer Order 77](#_Toc232856538)

[4.3.2 Create Replenishment Delivery for Stock Transfer Order 79](#_Toc232856539)

[4.3.3 Pick and Post Goods Issue for Delivery 80](#_Toc232856540)

[4.3.4 Post Goods Receipt for Outbound Delivery 81](#_Toc232856541)

[4.3.5 Analyze Stock Overview (Optional) 82](#_Toc232856542)

[4.3.6 Analyze Stock Overview for Empties 82](#_Toc232856543)

[4.4 Transfer Data to Point-of-Sale (POS) 83](#_Toc232856544)

[4.5 Process Point-of-Sale (POS) Transactions 83](#_Toc232856545)

[4.6 Returns from Store (Untied Empties) 84](#_Toc232856546)

[4.6.1 Create Returns Stock Transport Order 84](#_Toc232856547)

[4.6.2 Create Outbound Delivery 85](#_Toc232856548)

[4.6.3 Perform Picking and Post Goods Issue for Outbound Delivery 86](#_Toc232856549)

[4.6.4 Check Inbound Delivery 87](#_Toc232856550)

[4.6.5 Perform Post Goods Receipt 88](#_Toc232856551)

[4.6.6 Analyze Stock Overview for Empties 89](#_Toc232856552)

[4.7 Returns to Supplier (Untied Empties) 90](#_Toc232856553)

[4.7.1 Create Returns Purchase Order 90](#_Toc232856554)

[4.7.2 Monitor Returns Purchase Order 91](#_Toc232856555)

[4.7.3 Create Outbound Delivery 93](#_Toc232856556)

[4.7.4 Pick and Post Goods Issue 94](#_Toc232856557)

[4.7.5 Analyze Stock Overview for Empties 95](#_Toc232856558)

[4.8 Returns from Store (Full Article) 95](#_Toc232856559)

[4.8.1 Create Returns Stock Transport Order 95](#_Toc232856560)

[4.8.2 Create Outbound Delivery 97](#_Toc232856561)

[4.8.3 Perform Picking and Post Goods Issue for Outbound Delivery 98](#_Toc232856562)

[4.8.4 Check Inbound Delivery 99](#_Toc232856563)

[4.8.5 Perform Post Goods Receipt 100](#_Toc232856564)

[4.8.6 Analyze Stock Overview for Empties 101](#_Toc232856565)

[4.9 Returns to Supplier (Full Article) 102](#_Toc232856566)

[4.9.1 Create Returns Purchase Order 102](#_Toc232856567)

[4.9.2 Monitor Returns Purchase Order 103](#_Toc232856568)

[4.9.3 Create Outbound Delivery 105](#_Toc232856569)

[4.9.4 Pick and Post Goods Issue 106](#_Toc232856570)

[4.9.5 Analyze Stock Overview for Empties 107](#_Toc232856571)

[4.10 In-Store Inventory Management 108](#_Toc232856572)

[4.10.1 Perform Physical Inventory 108](#_Toc232856573)

[4.10.1.1 Create Physical Inventory Document 108](#_Toc232856574)

[4.10.1.2 Display Physical Inventory Document 109](#_Toc232856575)

[4.10.1.3 Perform Physical Inventory Count 110](#_Toc232856576)

[4.10.1.4 Approve or Reschedule Stock Counts 112](#_Toc232856577)

[4.10.1.5 Post Inventory Count Differences 113](#_Toc232856578)

[4.10.1.6 Analyze Stock Overview - Single Material 114](#_Toc232856579)

[4.10.1.7 Analyze Stock Overview for Empties 115](#_Toc232856580)

[4.10.2 Count Stock Ad hoc 116](#_Toc232856581)

[4.10.2.1 Analyze Stock Overview - Single Material 118](#_Toc232856582)

[4.10.2.2 Analyze Stock Overview for Empties 118](#_Toc232856583)

[4.10.3 Adjust Mass Stock - Options 119](#_Toc232856584)

[4.10.3.1 Adjust Mass Stock (Option 1) 119](#_Toc232856585)

[4.10.3.2 Adjust Mass Stock with Add Claim (Option 2) 121](#_Toc232856586)

[4.10.4 Transfer of Product 123](#_Toc232856587)

[4.11 In-Store Customer Order Management 124](#_Toc232856588)

[4.11.1 Sell from Store: Immediate PickUp 124](#_Toc232856589)

[4.11.1.1 Immediate Pickup of General Retail Articles 124](#_Toc232856590)

[4.11.1.1.1 Verify Consumer Registration 124](#_Toc232856591)

[4.11.1.1.2 Create Master Data for Registering New Consumers (Optional) 125](#_Toc232856592)

[4.11.1.1.3 Create Sales Order and Generate Invoice 126](#_Toc232856593)

[4.11.1.1.4 Process Customer Order Payment from POS 128](#_Toc232856594)

[4.12 Sell from Online Store, Delivery from Distribution Center to Customer (Full Article) 129](#_Toc232856595)

[4.12.1 Create Sales Order 129](#_Toc232856596)

[4.12.2 Back-Office Operations in Distribution Center 131](#_Toc232856597)

[4.12.2.1 Schedule Application Job for Outbound Delivery Creation 131](#_Toc232856598)

[4.12.2.2 Pick and Post Goods Issue for Outbound Delivery from Distribution Center 132](#_Toc232856599)

[4.12.2.3 Create Billing Document 133](#_Toc232856600)

[4.12.2.4 Validate Follow-On Documents (Optional) 134](#_Toc232856601)

[4.13 Click-and-Reserve (Payment at Store) - Order Fulfillment in Store (Stock is Available in the Store) 135](#_Toc232856602)

[4.13.1 Create Sales Orders 135](#_Toc232856603)

[4.13.2 Start Picking 137](#_Toc232856604)

[4.13.3 Look Over the Order Details for Handover 140](#_Toc232856605)

[4.13.4 Validate Sales Order Document and Subsequent Document Flow (Optional) 143](#_Toc232856606)

[4.13.5 Process Customer Order Payment from POS 143](#_Toc232856607)

[4.14 Click-and-Collect (Pre-Paid Order)- Order Fulfillment in Store (Stock is Available in the Store) 144](#_Toc232856608)

[4.14.1 Create Sales Order 144](#_Toc232856609)

[4.14.2 Start Picking 145](#_Toc232856610)

[4.14.3 Look Over the Order Details for Handover 149](#_Toc232856611)

[4.14.4 Validate Sales Order Document and Subsequent Document Flow (Optional) 151](#_Toc232856612)

## Purpose

Overview

Some retailers sell articles to which deposit-relevant packaging articles are assigned to. Consumers buy the packaging article with the main article and pay a deposit price for it. This packaging article can later be returned by the consumer and the deposit is refunded.

Beverages are the most common example. In some countries or regions, the empty bottle (and potentially also the crate containing multiple bottles) are subject to deposit handling. For example, an empty bottle is sold along with the lemonade (the full article), and twelve empty bottles and an empty crate are sold together with a crate of lemonade.

The article master for the full article is set up with a bill of material, reflecting the assignment of the full article to the relevant empties. The relationship of full and empty articles is carried through all supply chain processes and respective operational documents, starting with the procurement from external suppliers (purchase orders), and ending with the sale to consumer (sales in the store).

In inventory management, two types of empties stock are distinguished. The tied empties stock reflects the quantities attached to the full articles, but the untied stock considers only the inventory of stand-alone empties (for example, an empty bottle returned by the consumer on its way back to the supplier). Inventory reporting considers both types of stock. From a financial perspective, tied and untied empties are typically held in different accounts.

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

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Purchaser (Retail) | SAP_BR_PURCHASER_RFM | Purchasing | SAP_BR_PURCHASER_RFM |  |
| Receiving Specialist | SAP_BR_RECEIVING_SPECIALIST | Receiving | SAP_BR_RECEIVING_SPECIALIST |  |
| Retail Store Manager | SAP_BR_RFM_STORE_MANAGER | Retail Store Manager | SAP_BR_RFM_STORE_MANAGER |  |
| Warehouse Clerk (Retail) | SAP_BR_WAREHOUSE_CLERK_RFM | Warehouse Clerk (Retail) | SAP_BR_WAREHOUSE_CLERK_RFM |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Pricing Specialist (Retail) | SAP_BR_PRICING_SPCLST_RFM | Retail PricingRetail Markups | SAP_BR_PRICING_SPCLST_RFM |  |
| Inventory Manager (Retail) | SAP_BR_INVENTORY_MGR_RFM | Inventory Manager (Retail) | SAP_BR_INVENTORY_MGR_RFM |  |
| Master Data Specialist - Product Data (Retail) | SAP_BR_MD_SPCLST_ITEM_RFM | Master Data Specialist - Product Data (Retail) | SAP_BR_MD_SPCLST_ITEM_RFM |  |
| Assortment Specialist - Retail | SAP_BR_ASSTMT_SPCLST_RFM | Assortment Specialist - Retail | SAP_BR_ASSTMT_SPCLST_RFM |  |
| Retail Store Associate | SAP_BR_RFM_STORE_ASSOCIATE | Store Operations | SAP_BR_RFM_STORE_ASSOCIATE |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Administrator (Retail) | SAP_BR_ADMINISTRATOR_RFM | Administration - Retail | SAP_BR_ADMINISTRATOR_RFM |  |
| Configuration Expert - Business Network Integration | SAP_BR_CONF_EXPERT_BUS_NET_INT | Business Network Integration / Business Network Integration - Concur Integration / Business Network Integration - Output Control / Business Network Integration - Data Replication / Configuration Expert - Business Network Integration Cross Applications | SAP_BR_CONF_EXPERT_BUS_NET_INT |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Article | R_2010 | Lemonade | Header |
| Article | R_2011 | Empty bottle | Component |
| Article | R_2012 | Crate for empties | Component |
| Material Type | FULL,EMPT | Full Products,Empties (Retail) |  |
| Material Category | 00 | Single Material |  |
| Company Code | 3310 | Company Code 3310 |  |
| Purchasing Organization | 3310 | Purch. Org. 3310 |  |
| Purchasing Group | 001 | Group 001 |  |
| Purchasing Group | 002 | Group 002 |  |
| Sales Organization | 3310 | Dom. Sales Org |  |
| Distribution Channel | 405060 | Store SalesDistributionE-Commerce | Note The channel 60 is relevant, before you can test the scenario Sell from Online Store, Delivery from Distribution Center to Customer (Full Article) in this scope item. Also kindly check the [Business Conditions](#unique_6) [page ] 9. |
| Supplier | 33213002 | Retail Food Supplier AE |  |
| Distribution Center | 3350 | DC 3350 AE |  |
| Store | 3340 | Store 3340 AE |  |
| Storage Location | 994A | St.Loc.Neg.Stock |  |
| Storage Location | 995A | Storage Loc. DC |  |
| MRP Controller | 001 | MRP Controller 001 |  |

### Business Conditions

Before you can test the scenario Sell from Online Store, Delivery from Distribution Center to Customer (Full Article) in this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 5FZ - Omnichannel Order Fulfillment for Retail | You need to get scope item Omnichannel Order Fulfillment for Retail (5FZ) activated, before you want to use scenario Sell from Online Store, Delivery from Distribution Center to Customer (Full Article). |

### Preliminary Steps

#### Create Purchase Conditions for Empties

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity to create purchase conditions for empties.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data (Retail). |  |  |
| 2 | Access the App | Open Create Price Conditions - Purchasing (MEK1) app. | Create Price Conditions - Purchasing (MEK1) screen is displayed. |  |
| 3 | Enter Values | On the Create Price Conditions - Purchasing (MEK1) screen, enter the following details and select ENTER:Condition Type: PPR0 (Default Gross Price) and select ENTERKey Combination: <Select the relevant key combination from menu help>, for instance, <“Empties” Prices (Material-Dependent)> and select Choose.Enter <Empties> <R_2011, R_2012>Enter <Amount>Enter “Unit” <Currency> |  |  |
| 4 | Save the Record | Choose Save. | The condition record is saved. |  |

Result

Purchase conditions for empties are created.

|  |
| --- |
| NoteIf you want to operate in more than one country, please create new articles for full and empties and maintain purchase conditions if amount and currencies are different.Purchase info records should not be maintained for empties. |

#### Create Sales Conditions for Empties

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity to create sales condition for empties in stores and distribution center.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Pricing Specialist (Retail). |  |  |
| 2 | Access the App | Open Manage Prices - Sales (F4111) app. | Manage Prices - Sales (F4111) screen is displayed. |  |
| 3 | Enter Values | On the Manage Prices - Sales (F4111) screen, select Create and enter the following details and select ENTER:Condition Type: ESP0 (Sales Price Store)Condition Table: <Select the relevant condition table and access sequence from menu help>, for instance, 118 Product and press Enter.Note Condition record should be created at article level, Access – 005 for Condition Table – 118.Product: <Empties> <R_2011, R_2012>Condition Amount or Ratio: <Enter an amount> and <Currency> |  |  |
| 4 | Save the Record | Choose Save. | The condition record is saved. |  |
| 5 | Enter Values | On the Manage Prices - Sales (F4111) screen, select Create and enter the following details and select ENTER:Condition Type: ESP2 (Sales Price DC)Condition Table: <Select the relevant condition table and access sequence from menu help>, for instance, 118 Product and press Enter.Note Condition record should be created at article level, Access – 005 for Condition Table – 118.Product: <Empties> <R_2011, R_2012>Condition Amount or Ratio: <Enter an amount> and <Currency> |  |  |
| 6 | Save the Record | Choose Save. | The condition record is saved. |  |

Result

Sales conditions for empties are created.

|  |
| --- |
| Note If you want to operate in more than one country, please create new articles for full and empties and maintain sales conditions if amount and currencies are different. |

#### Create Sales Conditions for Full Article

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
| 3 | Enter Article Basic Data | In the Change Material (Initial screen)Material: Article numberEnter Full Article,<R_2010> |  |  |
| 4 | Choose Views | Select Sales views and choose Continue. | The Change Material R_2010 (Sales) screen is displayed . |  |
| 5 | Enter Organizational Level Data | In Switch Validity Area, in the Areas of Validity section, enter descriptions for the following:Sales Unit: (PC)Sales Org.: (3310/ Dom. Sales Org)Distr. Channel: (50 - Distribution)Choose Continue. |  |  |
| 6 | Enter Sales Data | On the Change Material R_2010 (Sales) screen, make the following entries:(All the below should ideally get filled automatically, but if you need to maintain any deviation then you can go ahead and maintain)For sale from: <date>For sale till: <date>Item Cat. Group: (FULL)Cash Discount : (X)PP Det. Seq. (Purchase Price Determination Sequence): (01/ Standard with price determination)SP Determ. Seq. (Sales Price Determination Sequence): (01/ Calculate SP from planned markup)Final price: (<value>)Save Calculated Price: (X) |  |  |
| 7 | Save Your Data | Choose Save. | Sales prices are created.Material R_2010 changed message appears on the status bar. |  |
| 8 | Choose Views | Select Sales views and choose Continue. | The Change Material R_2010 (Sales) screen is displayed . |  |
| 9 | Enter Organizational Level Data | In Switch Validity Area, in the Areas of Validity section, enter descriptions for the following:Sales Unit: (CRT)Sales Org.: (3310/ Dom. Sales Org)Distr. Channel: (40 - Store Sales)Choose Continue. |  |  |
| 10 | Enter Sales Data | On the Change Material R_2010 (Sales) screen, make the following entries:(All the below should ideally get filled automatically, but if you need to maintain any deviation then you can go ahead and maintain)For sale from: <date>For sale till: <date>Item Cat. Group: (FULL)Cash Discount : (X)PP Det. Seq. (Purchase Price Determination Sequence): (01/ Standard with price determination)SP Determ. Seq. (Sales Price Determination Sequence): (01/ Calculate SP from planned markup)Final price: (<value>)Save Calculated Price: (X) |  | Repeat the same steps 9 and 10 for maintaining distribution chain – CRT/3310/50. |
| 11 | Save Your Data | Choose Save. | Sales prices are created.Material R_2010 changed message appears on the status bar. |  |

#### Extend Articles to E-Commerce Channel

##### Extend Empties

|  |
| --- |
| Note This section is relevant, before you can test the scenario Sell from Online Store, Delivery from Distribution Center to Customer (Full Article) in this scope item. For more information, see [Business Conditions](#unique_6) [page ] 9. |

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
| 3 | Enter Article Basic Data | In the Change Material (Initial screen)Material: Article numberEnter Empties,(<R_2011>, <R_2012>) |  |  |
| 4 | Choose Views | Select Sales views and choose Continue. | The Change Material R_2011 (Sales) screen is displayed . |  |
| 5 | Enter Organizational Level Data | In Switch Validity Area, in the Areas of Validity section, enter descriptions for the following:Sales Unit: (PC)Sales Org.: (3310/ Dom. Sales Org)Distr. Channel: (60 - E-Commerce)Choose Continue. |  |  |
| 6 | Enter Sales Data | On the Change Material R_2011 (Sales) screen, make the following entries:(All the below should ideally get filled automatically, but if you need to maintain any deviation then you can go ahead and maintain)For sale from: <date>For sale till: <date>Item Cat. Group: (EMPT)Cash Discount : (X)PP Det. Seq. (Purchase Price Determination Sequence): (01/ Standard with price determination)SP Determ. Seq. (Sales Price Determination Sequence): (01/ Calculate SP from planned markup)Save Calculated Price: (Uncheck the box) |  |  |
| 7 | Save Your Data | Choose Save. | Sales prices are created.Material R_2011 changed message appears on the status bar. |  |

##### Extend Full Article

|  |
| --- |
| Note This section is relevant, before you can test the scenario Sell from Online Store, Delivery from Distribution Center to Customer (Full Article) in this scope item. Also kindly check the [Business Conditions](#unique_6) [page ] 9. |

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
| 3 | Enter Article Basic Data | In the Change Material (Initial screen)Material: Article numberEnter Full Article,(<R_2010>) |  |  |
| 4 | Choose Views | Select Sales views and choose Continue. | The Change Material R_2010 (Sales) screen is displayed . |  |
| 5 | Enter Organizational Level Data | In Switch Validity Area, in the Areas of Validity section, enter descriptions for the following:Sales Unit: (PC)Sales Org.: (3310/ Dom. Sales Org)Distr. Channel: (60 - E-Commerce)Choose Continue. |  |  |
| 6 | Enter Sales Data | On the Change Material R_2010 (Sales) screen, make the following entries:(All the below should ideally get filled automatically, but if you need to maintain any deviation then you can go ahead and maintain)For sale from: <date>For sale till: <date>Item Cat. Group: (FULL)Cash Discount : (X)PP Det. Seq. (Purchase Price Determination Sequence): (01/ Standard with price determination)SP Determ. Seq. (Sales Price Determination Sequence): (01/ Calculate SP from planned markup)Final price: (<value>)Save Calculated Price: (X) |  |  |
| 7 | Save Your Data | Choose Save. | Sales prices are created.Material R_2010 changed message appears on the status bar. |  |
| 8 | Choose Views | Select Sales views and choose Continue. | The Change Material R_2010 (Sales) screen is displayed . |  |
| 9 | Enter Organizational Level Data | In Switch Validity Area, in the Areas of Validity section, enter descriptions for the following:Sales Unit: (CRT)Sales Org.: (3310/ Dom. Sales Org)Distr. Channel: (60 - E-Commerce)Choose Continue. |  |  |
| 10 | Enter Sales Data | On the Change Material R_2010 (Sales) screen, make the following entries:(All the below should ideally get filled automatically, but if you need to maintain any deviation then you can go ahead and maintain)For sale from: <date>For sale till: <date>Item Cat. Group: (FULL)Cash Discount : (X)PP Det. Seq. (Purchase Price Determination Sequence): (01/ Standard with price determination)SP Determ. Seq. (Sales Price Determination Sequence): (01/ Calculate SP from planned markup)Final price: (<value>)Save Calculated Price: (X) |  |  |
| 11 | Save Your Data | Choose Save. | Sales prices are created.Material R_2010 changed message appears on the status bar. |  |

#### My Store Assignment

Purpose

With this process step, retail store associates can assign the required stores to themselves.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Retail Store Associate. |  |  |
| 2 | Open App | Open the My Store Assignment (F4334) app. | The My Store Assignment (F4334) app is displayed. |  |
| 3 | Assign Store | Search for a store in the list.Select the required Store.Select Assign Me. | The system displays a You were assigned to store <XXXX>. message. |  |

#### In-Store Inventory Management

##### Configure Define Basic Settings for Count Stock Ad hoc

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration as Configuration Expert - Business Process Configuration |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Basic Settings for Count Stock Ad hoc.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Basic Settings for Count Stock Ad hoc screen is displayed. |  |
| 3 | Configure Define Basic Settings for Count Stock Ad hoc | Create the following settings:Check ON Enable Automatic Posting |  |  |
| 4 | Save the configuration | Select Save | The configuration is saved successfully. |  |

##### Display Physical Inventory Document

Use

This preliminary step is to check if there is an existing PI document for the combination of an article, site, and storage location.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Inventory Manager (Retail). |  |  |
| 2 | Access the app | Open Physical Inventory Analysis (W0058) app. |  |  |
| 3 | Adopt filters | Choose Adapt Filters and select the below options under AdditionalMaterial :Plant :Storage Location :Choose OK |  |  |
| 4. | Enter details | Enter the below details in Standard SectionMaterial :Plant :Storage Location :Is Difference Posted: <Delete if any default value is selected in this field>Choose GO |  |  |
| 5. | Check the Physical Inventory Document | In Navigation Panel, under Available Fields:Add Physical Inventory Document either for row or for column by selecting below options:Select this option for row axis Add field Physical Inventory Document to row axis orSelect this option for column axis Add field Physical Inventory Document to column axis.Physical Inventory DocumentMaterialAll the details of the physical inventory displays under Data Analysis tabSelect Physical Inventory Document field and choose Drill Down > Add Drill DownSelect "Is Deleted" option under Available Fields.Choose OK | PI document number for the combination of an article, site, and storage location is displayed. |  |
| 6 | Note Active PI | Search for the PI Document number havingIs Deleted : #(No)Note the PI document number.In case of no active PI document, proceed to step Overview of Stock– Single Material | Active PI document number noted |  |

Result

Active PI document checked for the combination of an article, site, and storage location.

##### Delete Active Physical Inventory Document (Optional)

Use

This process step is in continuation to the previous step [Display Physical Inventory Document](#unique_14) [page ] 20 to delete the active Physical Inventory (PI) document. This step is only applicable when there is an active PI document for the combination of an article, site, and storage location.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Inventory Manager (Retail) |  |  |
| 2 | Access App | Open Manage Physical Inventory Documents (F0379A) app. |  |  |
| 3 | Manage Physical Inventory | Enter the Physical Inventory Document: XXXX ([Display Physical Inventory Document](#unique_14) [page ] 20) and select Go. | Physical inventory document is displayed. |  |
| 4 | Display the Physical Inventory Document | Select the arrow on right hand side to display the physical inventory document details. | Physical inventory document is displayed. |  |
| 5 | Delete Physical Inventory Document | Select Delete.Popup window is displayed for the confirmation as below:Do you want to delete physical inventory document XXXXXXXXX XXXX?.Note: The document is deleted and disappears from your list.In the popup screen, select Delete. | A message is displayed as physical inventory document XXXXXXXXX XXXX Deleted |  |

Result

Active PI document for the combination of an article, site, and storage location deleted.

##### Overview of Stock for Single Material

Use

To execute this scope item, the article has stock available in unrestricted use stock. The following preliminary steps must be executed to ensure the stock availability for all the process steps in this scope item.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Inventory Manager (Retail). |  |  |
| 2 | Access the app | Open Stock - Single Material (F1076) app. |  |  |
| 3 | Enter Material | Make the following entries:Material: R_2010Select Enter | The Stock – Single Material screen is displayed with stock of material R_2010 in all the sites and storage locations. |  |

Result

Unrestricted stock is checked for the material.

##### Analyze Stock Overview for Empties

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, the tied and untied stock of empties are displayed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk (Retail). |  |  |
| 2 | Access the Application | Open Display Empties Stock (WBF1) app. | Stock Overview for Empties screen displays. |  |
| 3 | Enter the Parameters | Enter the following data under Select. Criteria:“Empties“ material: R_2011 and R_2012Plant: 3340Choose Execute. | Stock Overview for Empties screen displays with the details of empties material entered. |  |
| 4 | Verify the Stock Details | Stock details of the empties material displays. | Stock details of empties material is displayed. |  |

##### Set Initial Stock for Article (Optional – Only if Stock not Available)

Use

To execute this scope item, the article must have stock available. The following preliminary steps must be executed only if there is no unrestricted use stock available for any of the 3 materials used in the test script. This step is to ensure the stock availability for all the process steps in this scope item.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Warehouse Clerk (Retail). |  |  |
| 2 | Access the app | Open Post Goods Movement (MIGO) app.The Transaction/Event and reference document will be updated automatically based on your last activity in MIGO transaction. |  |  |
| 3 | Input movement type | Make the following entry below and select ENTER:Trans./Event : Goods ReceiptReference Document: OtherInit.entry of StBalance : 561 | Entry accepted. |  |
| 4 | Enter article | In the detail data section : Material tab, Make the following entry:Material : R_2010And select ENTERNote Enter the articles without unrestricted use stock. | Article accepted. |  |
| 5 | Enter quantity data | In the detail data section: Quantity tab, Make the following entry:Qty in Unit of Entry : 10/ CRTExt. Amount LC: 1000Select ENTER | Qty and unit accepted. |  |
| 6 | Input on the goods receipt other screen: where tab | In the detail data section: Where tab, Make the following entries:Goods Movement Type: 561 (Receipt per initial entry of stock balances into unrestricted use)Plant: for example 3340Storage Location: 994ASelect ENTER | Values are accepted and shows check and post below screen. |  |
| 7 | Check your entries | Select CheckIf there is no errors in the data entered, a confirmation message Document Is O.K. is displayed. | Material document is checked. |  |
| 8 | Save your entries | Select PostNote Repeat the steps in case there are more than one article without unrestricted use stock (as per the quantities mentioned in the respective test procedure). | Material document is created. |  |

Result

Stock is created for the material.

##### Set up the Printer

Use

To execute this scope item, the printer set up must be completed. The following preliminary steps must be executed to ensure the printer setup for transfer products process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Retail Store Associate. |  |  |
| 2 | Access the app | Open Transfer Products (F2449) app. |  |  |
| 3 | Setup printer | Printer needs to be set by navigating through User profile - Application Setting and select the required printer from the dropdown list and select Close. | Printer needs to be displayed in the dropdown list to be selected. |  |

Result

Printer is assigned.

#### In-Store Customer Order Management

##### Customer Maintenance Settings

###### Define Schema for Customer Maintenance (Optional)

Purpose

The following procedure provides instructions to create a customizing schema.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to CBC Project Experience as Configuration Expert - Business Process Configuration |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Schema for Customer Maintenance.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Schema for Customer Maintenance screen is displayed. |  |
| 3 | Configure Define Schema for Customer Maintenance | Create the following settings:You should select an existing customizing schema and then click on Copy As.Provide name to customizing schema:Customizing Schema: <Use your own schema>Description: <Use your own description>and choose Copy. | Data Provided. |  |
| 4 | Save Customizing Schema | Click on Save to save Customizing Schema. | The Customizing Schema has been saved. |  |

###### Assign Template Customer to Schema

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

###### Assign Schema to Store

Purpose

The following procedure provides instructions for assigning site to customizing schema.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Project Experience in SAP Central Business Configuration. |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign Schema to Store.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Assign Schema to Store screen is displayed. |  |
| 3 | Assign Site | Add plant and schema.For example,Plant: 3340 (Store 3340 AE)Customizing Schema: <Use your own schema>Choose Enter. | Plant and schema description is displayed. |  |
| 4 | Save | Choose Save. | The Customizing Schema has been saved. |  |

###### Define Grouping Schema and Assign Countries (Optional)

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

###### Assign Grouping Schema to Store

Purpose

The following procedure provides instructions for assigning site to grouping schema.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Project Experience in SAP Central Business Configuration. |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign Grouping Schema to Store.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Assign Grouping Schema to Site screen is displayed. |  |
| 3 | Assign Site | Give plant and Grouping Schema and choose Enter. | Plant and Schema descriptions will appear. |  |
| 4 | Save | Choose Save. | The Grouping Schema has been saved. |  |

##### Create Initial Stock

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

##### Maintain Application Settings

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

##### Maintain Default Settings

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

This scope item consists of several process steps that are listed in the following table:

If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.

You can find all other apps not included on the homepage using the search bar.

If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose Settings > App Finder .

Create Master Data for Empties and Full Article (Optional)

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Empties](#unique_29) [page ] 40 | Master Data Specialist - Product Data (Retail) | Create Article (MM41)Manage Product Master Data (F1602) | Empties article is created. |
| [Create Full Article and Maintain Components](#unique_30) [page ] 49 | Master Data Specialist - Product Data (Retail) | Create Article (MM41)Maintain Article (MM42)Manage Product Master Data (F1602) | Full article is created with required components. |
| [Assign Full Article to Assortment Module](#unique_31) [page ] 64 | Assortment Specialist - Retail | Manage Assortment Modules (F4892) | Full article is assigned to assortment module. |
| [Assign Full Article to Distribution Center](#unique_32) [page ] 65 | Assortment Specialist - Retail | Assign Products to Distribution Centers (F4543) | Full article is assigned to distribution center. |
| [Create Purchase Conditions for Empties](#unique_33) [page ] 66 | Master Data Specialist - Product Data (Retail) | Create Price Conditions - Purchasing (MEK1) | Purchase conditions for empties are created. |
| [Create Sales Conditions for Empties](#unique_34) [page ] 68 | Pricing Specialist (Retail) | Manage Prices - Sales (F4111) | Sales conditions for empties are created. |
| [Create Sales Conditions for Full Article](#unique_35) [page ] 69 | Master Data Specialist - Product Data (Retail) | Maintain Article (MM42) | Sales conditions for Full Article is created. |

Procurement from External Supplier (Full Article)

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Purchase Order Directly](#unique_36) [page ] 72 | Purchaser (Retail) | Create Purchase Order - Advanced (ME21N) | Purchase Order will be generated. |
| [Create Inbound Delivery](#unique_37) [page ] 73 | Receiving Specialist | Create Inbound Delivery (VL31N) | Inbound delivery document with reference to purchase order is created. |
| [Confirm Quantities for Putaway](#unique_38) [page ] 74 | Receiving Specialist | Change Inbound Delivery (VL32N) | Inbound Delivery document is updated with confirmed putaway quantities. |
| [Post Goods Receipt for Inbound Delivery](#unique_39) [page ] 75 | Warehouse Clerk | Post Goods Movement (MIGO) | Goods receipt is posted for the inbound delivery when goods arrive at DC. |
| [Analyze Stock Overview (Optional)](#unique_40) [page ] 76 | Inventory Manager | Stock - Single Material (F1076) | Stock Overview of Materials is displayed. |
| [Analyze Stock Overview for Empties](#unique_41) [page ] 77 | Warehouse Clerk (Retail) | Display Empties Stock (WBF1) | Stock Overview of Empties are displayed. |

Store Ordering from Distribution Center (Full Article)

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Stock Transfer Order](#unique_42) [page ] 77 | Purchaser (Retail) | Create Purchase Order - Advanced (ME21N) | Stock transfer order (STO) is created. |
| [Create Replenishment Delivery for Stock Transfer Order](#unique_43) [page ] 79 | Shipping Specialist | My Purchase Orders - Due for Delivery (VL10B) | Outbound delivery document with reference to STO is created. |
| [Pick and Post Goods Issue for Delivery](#unique_44) [page ] 80 | Shipping Specialist | Change Outbound Delivery (VL02N) | Material is picked then packed. Handling units are generated. Goods issue is posted for the Outbound Delivery. |
| [Post Goods Receipt for Outbound Delivery](#unique_45) [page ] 81 | Retail Store Associate | Receive Products (F1248) | Goods receipt is posted against the outbound delivery document. |
| [Analyze Stock Overview (Optional)](#unique_40) [page ] 76 | Inventory Manager | Stock - Single Material (F1076) | Stock Overview of Materials is displayed. |
| [Analyze Stock Overview for Empties](#unique_46) [page ] 89 | Warehouse Clerk (Retail) | Display Empties Stock (WBF1) | Stock Overview of Empties are displayed. |
| [Transfer Data to Point-of-Sale (POS)](#unique_47) [page ] 83 |  |  |  |
| [Process Point-of-Sale (POS) Transactions](#unique_48) [page ] 83 |  |  |  |

Returns from Store (Untied Empties)

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Returns Stock Transport Order](#unique_49) [page ] 84 | Purchaser (Retail) | Create Purchase Order - Advanced (ME21N) | STO del return stock transport order is created. |
| [Create Outbound Delivery](#unique_50) [page ] 85 | Shipping Specialist | My Purchase Orders - Due for Delivery (VL10B) | Ourbound delivery for returns stock transport order is created. |
| [Perform Picking and Post Goods Issue for Outbound Delivery](#unique_51) [page ] 86 | Shipping Specialist | Change Outbound Delivery (VL02N) | Post Goods Issue is posted. |
| [Check Inbound Delivery](#unique_52) [page ] 87 | Purchaser (Retail) | Display Purchase Order - Advanced (ME23N) | Auto created inbound delivery is noted. |
| [Perform Post Goods Receipt](#unique_53) [page ] 88 | Receiving Specialist | Change Inbound Delivery (VL32N) | Post Goods Receipt is performed for inbound delivery. |
| [Analyze Stock Overview for Empties](#unique_46) [page ] 89 | Warehouse Clerk (Retail) | Display Empties Stock (WBF1) | Stock Overview of Empties are displayed. |

Returns to Supplier (Untied Empties)

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Returns Purchase Order](#unique_54) [page ] 90 | Purchaser (Retail) | Create Purchase Order - Advanced (ME21N) | Return purchase order is created. |
| [Monitor Returns Purchase Order](#unique_55) [page ] 91 | Purchaser (Retail) | Display Purchase Order - Advanced (ME23N) | Processing status of return purchase order turns green. |
| [Create Outbound Delivery](#unique_56) [page ] 93 | Shipping Specialist | My Purchase Orders - Due for Delivery (VL10B) | Outbound delivery created. |
| [Pick and Post Goods Issue](#unique_57) [page ] 94 | Shipping Specialist | Change Outbound Delivery (VL02N) | Post goods issue posted. |
| [Analyze Stock Overview for Empties](#unique_41) [page ] 77 | Warehouse Clerk (Retail) | Display Empties Stock (WBF1) | Stock Overview of Empties are displayed. |

Returns from Store (Full Article)

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Returns Stock Transport Order](#unique_58) [page ] 95 | Purchaser (Retail) | Create Purchase Order - Advanced (ME21N) | STO del return stock transport order is created. |
| [Create Outbound Delivery](#unique_50) [page ] 85 | Shipping Specialist | My Purchase Orders - Due for Delivery (VL10B) | Ourbound delivery for returns stock transport order is created. |
| [Perform Picking and Post Goods Issue for Outbound Delivery](#unique_51) [page ] 86 | Shipping Specialist | Change Outbound Delivery (VL02N) | Post Goods Issue is posted. |
| [Check Inbound Delivery](#unique_52) [page ] 87 | Purchaser (Retail) | Display Purchase Order - Advanced (ME23N) | Auto created inbound delivery is noted. |
| [Perform Post Goods Receipt](#unique_53) [page ] 88 | Receiving Specialist | Change Inbound Delivery (VL32N) | Post Goods Receipt is performed for inbound delivery. |
| [Analyze Stock Overview for Empties](#unique_46) [page ] 89 | Warehouse Clerk (Retail) | Display Empties Stock (WBF1) | Stock Overview of Empties are displayed. |

Returns to Supplier (Full Article)

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Returns Purchase Order](#unique_59) [page ] 102 | Purchaser (Retail) | Create Purchase Order - Advanced (ME21N) | Return purchase order is created. |
| [Monitor Returns Purchase Order](#unique_55) [page ] 91 | Purchaser (Retail) | Display Purchase Order - Advanced (ME23N) | Processing status of return purchase order turns green. |
| [Create Outbound Delivery](#unique_56) [page ] 93 | Shipping Specialist | My Purchase Orders - Due for Delivery (VL10B) | Outbound delivery created. |
| [Pick and Post Goods Issue](#unique_57) [page ] 94 | Shipping Specialist | Change Outbound Delivery (VL02N) | Post goods issue posted. |
| [Analyze Stock Overview for Empties](#unique_41) [page ] 77 | Warehouse Clerk (Retail) | Display Empties Stock (WBF1) | Stock Overview of Empties are displayed. |

In-Store Inventory Management

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Physical Inventory Document](#unique_60) [page ] 108 | Inventory Manager (Retail) | Create Documents - Physical Inventory (WV31) | Physical Inventory Document is created for Store. |
| [Display Physical Inventory Document](#unique_61) [page ] 109 | Inventory Manager (Retail) | Manage Physical Inventory Documents (F0379A) | Physical Inventory Document is displayed |
| [Perform Physical Inventory Count](#unique_62) [page ] 110 | Retail Store Associate | Count Stock (F1512) | A before planned physical inventory is executed by the store associate by entering the quantity for the to be counted articles. |
| [Approve or Reschedule Stock Counts](#unique_63) [page ] 112 | Retail Store Manager | Manage Stock Counting (F1512) | The store manager is monitoring the counts and can approve them or request a recount in case of high deviations. |
| [Post Inventory Count Differences](#unique_64) [page ] 113 | Inventory Manager (Retail) | Manage Physical Inventory Documents (F0379A) | The inventory manager can review and post the count difference |
| [Analyze Stock Overview - Single Material](#unique_65) [page ] 114 | Inventory Manager (Retail) | Stock - Single Material (F1076) | Updated count is displayed in stock overview |
| [Analyze Stock Overview for Empties](#unique_66) [page ] 115 | Warehouse Clerk (Retail) | Display Empties Stock (WBF1) | Stock Overview of Empties are displayed. |
| [Count Stock Ad hoc](#unique_67) [page ] 116 | Retail Store Associate |  |  |
| [Analyze Stock Overview - Single Material](#unique_65) [page ] 114 | Inventory Manager (Retail) | Stock - Single Material (F1076) | Updated count is displayed in stock overview |
| [Analyze Stock Overview for Empties](#unique_66) [page ] 115 | Warehouse Clerk (Retail) | Display Empties Stock (WBF1) | Stock Overview of Empties are displayed. |
| [Adjust Mass Stock (Option 1)](#unique_68) [page ] 119 | Retail Store Associate | Adjust Mass Stock (F4959) | The store associate adjusts the stock as example an item was discovered in the shelf unaccounted for. |
| [Adjust Mass Stock with Add Claim (Option 2)](#unique_69) [page ] 121 | Retail Store Associate | Adjust Mass Stock (F4959) | The store associate is adjusting stack and creating a claim for another cost centre. |
| [Transfer of Product](#unique_70) [page ] 123 | Retail Store Associate | Transfer Products (F2449) | A stock transfer order is created, containing the scanned articles. |

In-Store Customer Order Management

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Verify Consumer Registration](#unique_71) [page ] 124 | Retail Store Associate | Display Customer (WDA0486) | Consumer details are verified, if consumer is already registered. |
| [Create Master Data for Registering New Consumers (Optional)](#unique_72) [page ] 125 | Retail Store Associate | Create Customer (WDA0484) | Consumer master is created. |
| [Create Sales Order and Generate Invoice](#unique_73) [page ] 126 | Retail Store Associate | Manage In-Store Sales Orders (F7141) | Sales order is created, picking of the outbound delivery is triggered, goods issue for the outbound delivery is posted. |
| [Process Customer Order Payment from POS](#unique_74) [page ] 128 | Administrator (Retail) | Schedule POS Inbound Service (F5236) | Customer order payment information from a POS system to SAP S/4HANA Cloud Public Edition is transferred. |

Sell from Online Store, Delivery from Distribution Center to Customer (Full Article)

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Sales Order](#unique_75) [page ] 129 | Retail Store Associate | Create Sales Orders - VA01 (VA01) | Sales orders in SAP S/4HANA Cloud Public Edition Starter System is simulated. |
| [Schedule Application Job for Outbound Delivery Creation](#unique_76) [page ] 131 | Shipping Specialist | Schedule Delivery Creation (F2228) | Background job for outbound delivery document creation is scheduled. |
| [Pick and Post Goods Issue for Outbound Delivery from Distribution Center](#unique_77) [page ] 132 | Shipping Specialist | Change Outbound Delivery (VL02N) | Material (Article) is picked. Handling units are generated. Goods issue is posted for the outbound delivery from the distribution center. |
| [Create Billing Document](#unique_78) [page ] 133 | Billing Clerk | Create Billing Documents (F0798) | Billing document with reference to outbound delivery, is created. |
| [Validate Follow-On Documents (Optional)](#unique_79) [page ] 134 | Retail Store Associate | Manage Sales Orders (F1873) | Successful creation of outbound delivery, goods issue and billing document is validated. |

Click-and-Reserve (Payment at Store) - Order Fulfillment in Store (Stock is Available in the Store)

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Sales Orders](#unique_80) [page ] 135 | Retail Store Associate | Create Sales Orders - VA01 (VA01) | Sales orders in SAP S/4HANA Cloud Public Edition starter system is simulated. |
| [Start Picking](#unique_81) [page ] 137 | Retail Store Associate | Process Picking Requests (F4643) | Picking is started for the selected store picking requests, product GTIN is scanned and handover shelf is assigned to the picking request. |
| [Look Over the Order Details for Handover](#unique_82) [page ] 140 | Retail Store Associate | Hand Over Orders (F4639) | Details of the selected order and the status of order placed in the handover shelf is displayed. Also, order withdrawal is done and order is handed over to the consumer. |
| [Validate Sales Order Document and Subsequent Document Flow (Optional)](#unique_83) [page ] 143 | Retail Store Associate | Manage Sales Orders (F1873) | Validate the updates on the sales order also the subsequent documents generated after completion of the picking and handover process. |
| [Process Customer Order Payment from POS](#unique_84) [page ] 143 | Administrator (Retail)Configuration Expert - Business Network Integration | Schedule POS Inbound Service (F5236)Overview Message Monitoring (F4515) | Point-of-sale (POS) financial transactions are transferred to the SAP S/4HANA Cloud Public Edition system. |

Click-and-Collect (Pre-Paid Order)- Order Fulfillment in Store (Stock is Available in the Store)

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Sales Order](#unique_85) [page ] 144 | Retail Store Associate | Create Sales Orders - VA01 (VA01) | Sales orders in SAP S/4HANA Cloud Public Edition Starter System is simulated. |
| [Start Picking](#unique_81) [page ] 137 | Retail Store Associate | Process Picking Requests (F4643) | Picking is started for the selected store picking requests, product GTIN is scanned and handover shelf is assigned to the picking request. |
| [Look Over the Order Details for Handover](#unique_82) [page ] 140 | Retail Store Associate | Hand Over Orders (F4639) | Details of the selected order and the status of order placed in the handover shelf is displayed. Also, order withdrawal is done and order is handed over to the consumer. |
| [Validate Sales Order Document and Subsequent Document Flow (Optional)](#unique_83) [page ] 143 | Retail Store Associate | Manage Sales Orders (F1873) | Validate the updates on the sales order also the subsequent documents generated after completion of the picking and handover process. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Master Data for Empties and Full Article (Optional)

This section is required only if you want to create your own master data for business process testing otherwise please use master data provided in the [Master Data, Organizational Data, and Other Data](#unique_5) [page ] 7.

#### Create Empties and Full Article

##### Create Empties

Procedure

In the procedure you can create article using Create Article (MM41) app.

Table 2: Option 1 - Create Article

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data (Retail). |  |  |
| 2 | Access the SAP Fiori App | Open Create Article (MM41) app. | The Create Material (Initial Screen) is displayed. |  |
| 3 | Enter Article Basic Data | In the Create Material (Initial screen)Material: Article number (<R_YYYYY>)Material type: Empties (Retail)/EMPT Empties (Retail)Material Group: (R7112001/Empties)Material Category: Single Material/00 |  |  |
| 4 | Choose Views | Select Basic data, Basic data 2, Sales, Logistics DC, Logistics Store & POS views and choose continue. | Create Material … (Basic Data) opens. |  |
| 5 | Enter Basic Data | From Create Material ...(Basic Data), on the Basic data tab, enter a Article description (short text). |  |  |
| 6 | Enter Basic Data | In the Units of measure/EANs/dimensions section, enter the following: (All the below should ideally get filled automatically (only except EAN Category) from the Reference Article, but if you need to maintain any deviation then you can go ahead and maintain)Base Unit of Measure (PC)Gross Weight (<value>)Unit of Weight (KG)Net Weight (<value>)EAN Category (IE - Instore EAN (int. assignment possible))Volume (<value>)Volume Unit (L) |  |  |
| 7 | Enter Basic Data | From the Basic data tab enter the descriptions for the following:In Internal logistics data:Purchasing Group (002/Group 002)Supply Source (4 - Stock Transfer Before Standard)GenItemCatGroup (EMPT)Loading Group (0002/Forklift)Transportation Group (0001/On pallets)Variable Order Unit (1/Active)In General Data:Tax Class (1- Full tax)Valuation Class (3050 – Packaging and empties)In Validity Section:Valid from: <date>Valid to: <date> (default 31.12.9999, cannot be maintained)In Shelf-Life Data Section:Remaining Shelf Life: (0)Total Shelf Life: (0)Period indicatorp: (D)Storage %: (0) |  | The system message “The EAN will be determined internally on the basis of the EAN category displays” |
| 8 | Navigate to Go to Additional Data in Basic Data View | In Short Text View enter/check the description and language:Language ArabicMaterial Description <Value>Then Press Go to Main Data | Basic Data Screen appears |  |
| 9 | Choose Views | Select Basic Data 2 View and enter the descriptions for the following:Packaging Mat. Type - SP11(Car int./ext. closed)Allowed Packaging Weight <Value>Allowed Packaging Volume <Value>Excess Weight Tolerance <Value>Excess Volume Tolerance <Value> | Create Material …(Basic data 2) view opens. |  |
| 10 | Enter Sales Period | If necessary, adjust Sales period for Stores and Distribution Center.Sales Period: storeFor sales from <date>For sales till <date>Sales Period: distribution centerFor sales from <date>For sales till <date> |  |  |
| 11 | Choose Views | Select Sales View and choose to continue/enter. | Create Material …(Sales) view displays. |  |
| 12 | Enter Organizational Levels Data | Choose Switch Validity Area, in the Areas of Validity section, enter descriptions for the following:Sales Unit (PC)Sales Org. (3310/ Dom. Sales Org)Distr. Channel (40 - Store Sales)Choose Continue. |  |  |
| 13 | Enter Sales Data | On the Create Material: Sales screen, make the following entries:(All the below should ideally get filled automatically from the Reference Article, but if you need to maintain any deviation then you can go ahead and maintain)For Sales from <date>For Sales to <date>Item Category Group (EMPT)PP det. Seq. (Purchase Price determination Sequence) (01/ Standard with price determination)SP det Seq. (Sales price Determination Sequence) (01/ Calculate SP from planned markup)Save Calculated Price (Uncheck the box) |  | Repeat the same steps 11 and 12 for maintaining Sales Area – 3310/50 (For DC) for Sales unit PC.Repeat the same steps 11 and 12 for maintaining Sales Area – 3310/60 (For DC) for Sales unit PC before you can test the scenario Sell from Online Store, Delivery from Distribution Center to Customer (Full Article) in this scope item. Also kindly check the [Business Conditions](#unique_6) [page ] 9. |
| 14 | Choose Views | Select Logistics DC View and choose to continue/ enter.Check for the below entries:In MRP Parameters:MRP Type: ND (No Planning)Forecast Parameters:Forecast model – 0Period Indicator : WIn MRP Controller/Replenishment Data:Supply Source: 1 (Standard)In General Control Parameters:Purchasing Group: 002/Group 002Tax Indicator: 1 (Full tax)Availability Check: NC/ No ATP CheckIn Physical Inventory/Goods Issue/ Picking/ Shipping section:Loading Group: 0002/ForkliftIn Storage Data:Storage Location: 995A | Create Material … (Logistics DC) view displays. | On the Create Material: Logistics DC screen, check the available entries. These are proposed based on the reference Article. Only changes must be maintained. |
| 15 | Navigate to Accounting inside Logistics DC View | In the Price and Value section maintain the Price Control as V.Note Price control settings for empties can be changed to Standard (S) in the Article Master. |  |  |
| 16 | Choose Views | Select Logistics Store View and choose to continue/enter.Check for the below entries:In MRP Parameters:MRP Type: ND/ No PlanningIn the Forecast Parameters:Forecast Model: 0/No forecast/no external modelIn MRP Controller/Replenishment Data:Supply Source: 4 (Stock Transfer Before Standard)In General Control Parameters:Purchasing Group: 002/Group 002Tax Indicator: 1(Full tax)Availability Check: NC/ No ATP CheckNegative Stock: XIn Storage Data:Storage Location: 994A | Create Material … (Logistics Store) view displays. | On the Create Material: Logistics Store screen, Check the available entries and do adjustments if necessary (e.g., supply source) |
| 17 | Navigate to Accounting inside Logistics Store View | In the Price and Value section maintain the Price Control as V.Note Price control settings for empties can be changed to Standard (S) in the Article Master. |  |  |
| 18 | Navigate to MRP/Forecast Data inside Logistics Store View | In the MRP/Forecast Data maintain or check for the below entries:In Procurement Section :Procurement Type : F (External Procurement)In the Number of periods required section:History Periods: 60Forecast Periods: 12In Control data Section:Initialization: XTrack Limit: 4(Value that specifies the amount by which the forcast value may deviate from the actual value.)Select check box - Autom.resetModel Selection Procedure: 2 (Analytical model selection procedure)Press Back button | Administrator will be navigated back to the Logistics Store view. |  |
| 19 | Choose Views | Select POS View and choose to continue/ enter.Enter Till receipt Text as mentioned below:Language Key: ENAlternate Unit: PCTill receipt text for Unit: <value> | Create Material …(POS) view displays. | Maintain POS Text for distribution chain: 3310/40Maintain, if necessary, the text in different languages. Press the button: additional data |
| 20 | Save Your Data | At the bottom right of the display, choose Create to save your data. | The Create Material (Initial Screen) appears.The empty article is created and saved. | You can change or maintain or update the article created above, via Maintain Article (MM42) app. |

Procedure

In this procedure you can create product master data using the Manage Product Master Data (F1602) app.

Table 3: Option 2 - Manage Product Master Data

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data (Retail). |  |  |
| 2 | Access the SAP Fiori App | Open Manage Product Master Data (F1602). | The Manage Product Master Data (F1602) screen is displayed. |  |
| 3 | Choose Create New Product Master | In the Manage Product Master Data (F1602) view, Click on Create button and select Single Article from the list. | The Create Master Data Record screen displays. |  |
| 4 | Enter Data for Mandatory Fields | In the Master Data Record Subscreen make the following entries:Product Number: for example, <R_ZZZZZ>Note You either enter any external alphanumeric ID, and that ID must start with an alphanumeric character, or if you provide no entry, the system automatically assigns a numeric ID.Product Type: Empties (Retail) (EMPT)Product Group: Empties (R7112001)Base Unit: for example, PCValuation Class: Packaging and empties (3050)Tax Classification: 1 (Full Tax)Loading Group: 0002/ForkliftDescription: <any description> |  |  |
| 5 | Choose OK | In the Manage Product Master view, choose OK. | The Manage Product Master view is displayed. |  |
| 6 | In General Information - Basic Data | In the Manage Product Master > General Information > Basic Data view.Division: 00In the Manage Product Master > General Information > Basic Data >. | Description in default language (for example, English) is already populated. |  |
| 7 | In General Information - Descriptions | In the Manage Product Master > General Information > Description’s view, screen, choose Create. | Description in default language (for example, Arabic) is already populated. |  |
| 8 | Enter Descriptions Data | In the Descriptions view, make the following entries:Language: for example, ArabicProduct Description: <your description> |  |  |
| 9 | In General Information | In the Manage Product Master > General Information > Base Unit of Measure view (Show more), make the following entry:GTINGTIN Category: IEWeightsGross Weight: <value>Net Weight: <value>Volume: <value> L |  |  |
| 10 | Choose Unit of Measure | In the Manage Product Master > General Information > Unit of Measure, choose the Unit of Measure (e.g. PC) and navigate to the details. |  |  |
| 11 | Enter Receipt Texts | In the Receipt Texts under Unit of Measure Texts, select Create.Enter Language and Text. |  |  |
| 12 | Enter Dimensions Data | In the Dimensions > Weight section, enter the following:Gross Weight: for example, 0.200Net Weight: for example, 0.200Weight Unit: for example, KG |  |  |
| 13 | Choose Distributions Chains | In the Product screen, choose Distribution Chains tab. | The Distribution Chains tab displays. |  |
| 14 | Choose Create | In the Distribution Chains tab, choose Create | Distribution Chains opens in Edit Mode. |  |
| 15 | Enter Distribution Chains Data | In Distribution Chains, make following entries:In the GENERAL DATA - General Information section:Sales Organization: <Sales org number> (3310/ Dom. Sales Org)Note The organization unit value is determined by what is offered in the value help.Distribution Channel: for example, 40 - Store SalesIn the GROUPING TERMS section:Item Category Group: for example, EMPT |  |  |
| 16 | Return to Main View | Choose Apply to return to Product screen. | The Product screen appears. | Repeat steps 12 to 14 to maintain other distribution chains e.g.,3310/50.Repeat the same steps 12 to 14 for maintaining Sales Area – 3310/60 for Sales unit PC before you can test the scenario Sell from Online Store, Delivery from Distribution Center to Customer (Full Article) in this scope item. Also kindly check the [Business Conditions](#unique_6) [page ] 9. |
| 17 | Choose Distribution Center Data | In the Product screen, choose Distribution center. | The Distribution Center tab displays. |  |
| 18 | Create Distribution Center | In the Distribution center view, choose Create. | The Distribution Center view opens. |  |
| 19 | Enter Distribution Center - General Information | In the General Information section, make following entries:Distribution Center: Distribution center number for example, 3391 (Reference DC comes by default, no need to enter explicitly and remain Non Editable)Loading Grp: for example, 0002(Forklift) (Sales Data) |  | Similarly, Administrator can maintain for different DC. |
| 20 | Enter Distribution Center - MRP Data | In the MRP Data > MRP Data section, make following entries:Availability Check: for example, NC(No ATP Check)MRP Type: For example, ND (No MRP) |  |  |
| 21 | Enter Distribution Center - Storage Location | In the Storage > Storage Locations > Distribution Center - Storage Locations section, choose Create and make following entries:Storage Location: 995A |  |  |
| 22 | Return to Main Screen | Choose Apply to return to Product screen. | The Product screen displays. |  |
| 23 | Create Stores | In the Stores view, choose Create. | The Store view opens. |  |
| 24 | Enter Stores - General Information | In the General Information section, make following entries if not maintained:Store: Store number for example, 3392 (Reference Store comes by default, no need to enter explicitly and remain Non Editable)Negative Stock Allowed in Plant: X |  | Similarly, Administrator can maintain for different Stores |
| 25 | Enter Loading Group Under Sales Data | In the Sales Data section make following entry:Loading Grp: for example, 0002(Forklift) |  |  |
| 26 | Enter Stores - MRP Data | In the MRP Data > MRP Data section, make following entries:Availability Check: for example, NC/No ATP CheckMRP Type: For example, ND/No MRP |  |  |
| 27 | Enter Store - Storage Location | In the Storage > Storage Locations > Store - Storage Locations section, choose Create and make following entries:Storage Location: 994A |  |  |
| 28 | Return to Main Screen | Choose Apply to return to Product screen. | The Product screen displays. |  |
| 29 | Save Your Data | Choose Create. | System message displays that object is saved. |  |

##### Create Full Article and Maintain Components

Procedure

In the procedure you can create article using Create Article (MM41) app.

Table 4: Option 1 - Create Article

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data (Retail). |  |  |
| 2 | Access the SAP Fiori App | Open Create Article (MM41) app. | The Create Material (Initial Screen) is displayed. |  |
| 3 | Enter Article Basic Data | In the Create Material (Initial screen)Material: Article number (<R_XXXXX>)Material type: Full Products/ FULL Full ProductsMaterial Group: (R1161002/Soft DrinksMaterial Category: Single Material/00 |  |  |
| 4 | Choose Views | Select Basic data, Basic data 2, Sales, Logistics DC, Logistics Store & POS views and choose to continue. | Create Material (Basic Data) opens. |  |
| 5 | Enter Basic Data | From Create Material ... (Basic Data), on the Basic data tab, enter an article description (short text). |  |  |
| 6 | Enter Basic Data | In the Units of measure/EANs/dimensions section, enter the following: (All the below should ideally get filled automatically (only except EAN Category) from the Reference Article, but if you need to maintain any deviation then you can go ahead and maintain)Base Unit of Measure (PC)Gross Weight (<value>)Unit of Weight (KG)Net Weight (<value>)EAN Category (IE - Instore EAN (int. assignment possible)) (Maintain for all UOMs)Alternate Unit of Measure (CRT)Volume (<value>)Volume Unit (L)Maintain conversion factor for the alternate UOM (CRT):Number <Value>Lower-level unit (PC)Select Order Unit and Delivery Unit radio button for the Alternate UOM i.e. CRT in this case. |  |  |
| 7 | Enter Basic Data | From the Basic data tab enter the descriptions for the following:In Internal logistics data:Purchasing Group (002/Group 002)Supply Source (4 - Stock Transfer Before Standard)GenItemCatGroup (FULL)Loading Group (0001/Crane)Transportation Group (0001/On pallets)Variable Order Unit (1/Active)In General Data:Tax Class (1- Full tax)Valuation Class (3100 – Trading Goods)W/ Empties BOM (X)In Content Section:Net Contents <value>Gross Contents <value>Content Unit (L)Comparison Price Unit (1)In Validity Section:Valid from: <date>Valid to: <date> (default 31.12.9999, cannot be maintained)In Shelf-Life Data Section:Remaining Shelf Life: (0)Total Shelf Life: (0)Period indicator: (D)Storage %: (0) |  | The system message “The EAN will be determined internally on the basis of the EAN category displays” |
| 8 | Navigate to Go to Additional Data in Basic Data View: | In Short Text View enter/check the description and language:Language (EN)Material Description <Value>In the Unit of Measure View maintain/check the following (for Alternate UOM):Gross Weight <value>Unit of Weight (KG)EAN (IE - Instore EAN (int. assignment possible))Then Press Go to Main Data | Basic Data Screen appears |  |
| 9 | Enter Basic Data | Press Components button and navigate to Create Empties BOM screen.Enter the Unit of Measure (PC) and press ENTER.Enter the Component (Empties article created above (e.g., <R_YYYYY>) details with quantity and UOM (e.g., PC)Press back button | Once the components and description are completed, you move to the next tab, Basic data 2 view. |  |
| 10 | Choose Views | Select Basic Data 2 View and choose to continue/enter. | Create Material … (Basic data 2) view opens. |  |
| 11 | Enter Sales Period | If necessary, adjust Sales period for Stores and Distribution Center.Sales Period: storeFor sales from <date>For sales till <date>Sales Period: distribution centerFor sales from <date>For sales till <date> |  |  |
| 12 | Choose Views | Select Purchasing View and choose Continue. | Create Material …(Purchasing) view is displayed. |  |
| 13 | Enter Organizational Levels Data | Choose Switch Validity Area, in the Areas of Validity section, enter descriptions for the following:Purchasing Org. (3310/ Dom. Sales Org)Supplier 33213002/Retail Food Supplier AEChoose Continue. |  |  |
| 14 | Enter Purchasing Data | On the Create Material: Purchasing screen, make the following entries:Purchasing Group (002/Group 002)Var. Order Unit (1/Active)Regular Supplier (X)Net Price (<value>) |  | As a next step, you need to maintain purchasing Info record.Disclaimer: Regular Supplier value makes sense, only if the customer is operating in one country and has several vendors for this article and one should be the preferred vendor. |
| 15 | Choose Views | Select Sales View and choose continue/enter. | Create Material …(Sales) view displays. |  |
| 16 | Enter Organizational Levels Data | Choose Switch Validity Area, in the Areas of Validity section, enter descriptions for the following:Sales Unit: (PC)Sales Org. (3310/ Dom. Sales Org)Distr. Channel (40 - Store Sales)Choose Continue. |  |  |
| 17 | Enter Sales Data | On the Create Material:Sales screen, make the following entries:(All the below should ideally get filled automatically from the Reference Article, but if you need to maintain any deviation then you can go ahead and maintain)For Sales from <date>For Sales to <date>Item Category Group (FULL)Cash Discount (X)PP det. Seq. (Purchase Price determination Sequence) (01/ Standard with price determination)SP det Seq. (Sales price Determination Sequence) (01/ Calculate SP from planned markup)Final Price (<value>)Save Calculated Price (X) |  | Repeat the same steps 15 and 16 for maintaining distribution chain – CRT/3310/40Repeat the same steps 15 and 16 for maintaining distribution chain – PC/3310/50Repeat the same steps 15 and 16 for maintaining distribution chain – CRT/3310/50Repeat the same steps 15 and 16 for maintaining distribution chain – PC/3310/60 before you can test the scenario Sell from Online Store, Delivery from Distribution Center to Customer (Full Article) in this scope item. Also kindly check the [Business Conditions](#unique_6) [page ] 9Repeat the same steps 15 and 16 for maintaining distribution chain – CRT/3310/60 before you can test the scenario Sell from Online Store, Delivery from Distribution Center to Customer (Full Article) in this scope item. Also kindly check the [Business Conditions](#unique_6) [page ] 9 |
| 18 | Choose Views | Select Logistics DC View and choose to continue/ enter.Check for the below entries:In MRP Parameters:MRP Type: R1 (Time-Phased Planning)Lot Size: EX (Lot-for-lot order quantity)Safety Stock: <value> By default it is 0Rounding profile: RDYP/ Retail Dynamic Rounding ProfileIn MRP Controller/Replenishment Data:MRP Controller: 001/MRP Controller 001Planning Cycle: P01 (Order Day Monday)Planned Delivery Time: 5Supply Source: 1 (Standard)In General Control Parameters:Purchasing Group: 002/Group 002Tax Indicator: 1 (Full tax)Automatic PO: XAvailability Check: ST(Consider only Stock)In Physical Inventory/Goods Issue/ Picking/ Shipping section:Loading Group: 0001/CraneIn Storage Data:Storage Location: 995A | Create Material … (Logistics DC) view displays. | On the Create Material: Logistics DC screen, check the available entries. These are proposed based on the reference Article. Only changes must be maintainedRounding Profile is a Key that the system uses to adjust the order proposal quantity to deliverable units. |
| 19 | Navigate to MRP/Forecast Data inside Logistics DC View | In the MRP/Forecast Data maintain or check for the below entries:In Procurement Section:Procurement Type: F (External Procurement)In Scheduling Section:Schedule Margin key: 001In Control data Section:Select check box - Autom.resetPress Back button | Administrator will be navigated back to the Logistics Dc view. |  |
| 20 | Choose Views | Select Logistics Store View and choose to continue/enter.Check for the below entries:In MRP Parameters:MRP Type: RF/ Replenish with dyn.TargetStock(Dynamic Target Stock gets calculated at runtime during the planning run from forecast sales value )Safety Stock: <value> By default it is 0In Replenishment parameters Section:Target Coverage: 5In the Forecast Parameters:Forecast Model: K/ Constant with smoothing factor adjustmentIn MRP Controller/Replenishment Data:Planned Delivery Time: 3Supply Source: 4 (Stock Transfer Before Standard)In General Control Parameters:Purchasing Group: 002/Group 002Tax Indicator: 1(Full tax)Automatic PO: XAvailability Check: ST/ Consider only stockNegative Stock: XIn Storage Data:Storage Location: 994A | Create Material … (Logistics Store) view displays. | On the Create Material: Logistics Store screen, Check the available entries and do adjustments if necessary (e.g. supply source) |
| 21 | Navigate to MRP/Forecast Data inside Logistics Store View | In the MRP/Forecast Data maintain or check for the below entries:In Procurement Section :Procurement Type : : F (External Procurement)In the Number of periods required section:History Periods: 60Forecast Periods: 12In Control data Section:Initialization: XTrack Limit: 4(Value that specifies the amount by which the forecast value may deviate from the actual value.)Select check box - Autom.resetModel Selection Procedure: 2 (Analytical model selection procedure)Press Back button | Administrator will be navigated back to the Logistics Store view. |  |
| 22 | Choose Views | Select POS View and choose to continue/ enter.Enter Till receipt Text as mentioned below:Language Key: ENAlternate Unit: PCTill receipt text for Unit: <value> | Create Material …( POS) view displays. | Maintain POS Text for distribution chain: 3310/40Maintain if necessary the text in differentlanguages. Press the button: additional data |
| 23 | Save Your Data | At the bottom right of the display, choose Create to save your data. | The Create Material (Initial Screen) appears.The Full Article is created and saved. |  |

Maintain Components in alternate UOM via Maintain Article App

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. |  |  |
| 2 | Access the SAP Fiori App | Open Maintain Article (MM42) app. | The Change Material (Initial Screen) is displayed. |  |
| 3 | Enter Article Basic Data | In the Change Material (Initial screen)Material: Article number (<R_XXXXX>) |  |  |
| 4 | Choose Basic data View | Select Basic data and choose to continue. | Change Material <R_XXXXX> (Basic Data) opens. |  |
| 5 | Press Component button | Change Empties Bom screen appears.Enter Unit of MeasureCRT and Press Enter |  |  |
| 6 | Add Component for alternate UOM | Add Components and quantity in the Component OverviewEnter the Components (Empties article created above e.g., <R_YYYYY> & <R_ZZZZZ> details with quantity and UOM (e.g., PC)Press Back button to go back to Change Material (Basic data) screen. |  |  |
| 7 | Save the Article | Press Save button. | Article gets saved |  |

Procedure

In this procedure you can create product master data using the Manage Product Master Data (F1602) app.

Table 5: Option 2 - Manage Product Master Data

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data (Retail). |  |  |
| 2 | Access the SAP Fiori App | Open Manage Product Master Data (F1602). | The Manage Product Master Data screen is displayed. |  |
| 3 | Choose Create New Product Master | In the Manage Product Master Data (F1602) view, Click on Create button and select Single Article from the list. | The Create Master Data Record screen is displayed. |  |
| 4 | Enter Data for Mandatory Fields | In the Master Data Record Subscreen make the following entries:Product Number: for example, <R_VVVVV>Note You either enter any external alphanumeric ID, and that ID must start with an alphanumeric character, or if you provide no entry, the system automatically assigns a numeric ID.Product Type: Full Products (FULL)Product Group: R1161002/Soft DrinksBase Unit: for example, PCValuation Class: 3100 – Trading goodsTax Classification: 1 (Full Tax)Loading Group: 0001/CraneDescription: <any description> |  |  |
| 5 | Choose OK | In the Manage Product Master view, choose OK. | The Manage Product Master view is displayed. |  |
| 6 | In General Information à Basic Data | In the Manage Product Master > General Information > Basic Data view.Division: 00Has Empties: XIn the Manage Product Master > General Information > Basic Data >.Content/Design viewNet Contents: <Value> LGross Contents: <Value> LComparison Price Unit: <Value> L | Description in default language (for example, Arabic) is already populated. |  |
| 7 | In General Information à Descriptions | In the Manage Product Master > General Information > Descriptions view, screen, choose Create. | Description in default language (for example, Arabic) is already populated. |  |
| 8 | Enter Descriptions Data | In the Descriptions view, make the following entries:Language: for example, ArabicProduct Description: <your description> |  |  |
| 9 | In General Information | In the Manage Product Master > General Information > Base Unit of Measure view (Show more), make the following entry:GTINGTIN Category: IEWeightsGross Weight: <value>Net Weight: <value>VolumeVolume: <value> L |  |  |
| 10 | Choose Unit of Measure | In the Manage Product Master > General Information > Unit of Measure, choose the Unit of Measure (e.g. PC) and navigate to the details. |  |  |
| 11 | Enter Receipt Texts | In the Receipt Texts under Unit of Measure Texts, select Create.Enter Language and Text. |  |  |
| 12 | Enter Dimension Data | In the Weight section, enter the following:Gross Weight: for example, 0.960Net Weight: for example 0.960Weight Unit: for example, KGVolume: <Value> L |  |  |
| 13 | Enter Components Data | In the Components section, enter the following:Product: Enter the Component (Empties article created above (e.g., <R_YYYYY>) details with quantity and UOM (e.g., PC)QuantityPress Apply |  |  |
| 14 | Add an alternate Unit of Measure | In the Manage Product Master > General Information > Unit of Measure view, and click on Create button | New order – Unit of Measure Screen open |  |
| 15 | Enter Unit of Measure | In the General Information section: Enter Unit of measure, CRT |  |  |
| 16 | Enter Conversion factor | In the Conversion Factor section:Enter Units/Quantity – Alternate Unit of Measure <value> for e.g. 1Enter Units/Quantity – Base Unit of Measure <value> for e.g., 10 |  |  |
| 17 | Enter Weight Data | In the Weight section, enter the following:Gross Weight: for example, 9.600Net Weight: Ideally this should get auto filled by defaultWeight Unit: for example, KG |  |  |
| 18 | Enter GTIN for the alternate UOM | In the GTINs section à GTINs -unit of Measure press create button and assign GTIN category IE and press ENTER. |  |  |
| 19 | Return to Main Screen | Choose the back arrow to return to the main screen. | The Product Master screen appears. |  |
| 20 | Enter Delivery Unit of measure | In the Manage Product Master > General Information > Reference Values maintain Delivery Unit of Measure (CRT). |  |  |
| 21 | Choose Distributions Chains | In the Product screen, choose Distribution Chains tab. | The Distribution Chains tab displays. |  |
| 22 | Choose Create | In the Distribution Chains tab, choose Create | Distribution Chains opens in Edit Mode. |  |
| 23 | Enter Distribution Chains Data | In Distribution Chains, make following entries:In the GENERAL DATA - General Information section:Sales Organization: <Sales org number> (3310/ Dom. Sales Org)Note The organization unit value is determined by what is offered in the value help.Distribution Channel: for example, 40 - Store SalesCash Discount: XIn the GROUPING TERMS section:Item Category Group: for example, FULL |  |  |
| 24 | Return to Main View | Choose Apply to return to Product screen. | The Product screen appears. | Repeat steps 20 and 21 to maintain other distribution chains e.g., 3310/50.Repeat steps 20 and 21 to maintain other distribution chains e.g., 3310/60 before you can test the scenario Sell from Online Store, Delivery from Distribution Center to Customer (Full Article) in this scope item. Also kindly check the [Business Conditions](#unique_6) [page ] 9. |
| 25 | Choose Purchasing Data | In the Product screen, choose Purchasing. | The Purchasing view is displayed. |  |
| 26 | Enter Purchasing Data | In the Purchasing section, enter Order Unit of Measure as CRT. |  |  |
| 27 | Choose Distribution Center Data | In the Product screen, choose Distribution center. | The Distribution Center tab displays. |  |
| 28 | Create Distribution Center | In the Distribution center view, choose Create. | The Distribution Center view opens. |  |
| 29 | Enter Distribution Center - General Information | In the General Information section, make following entries:Distribution Center: Distribution center number for example, 3391 (Reference DC comes by default, no need to enter explicitly and remain Non Editable)Loading Grp: for example, 0001 - Crane (Sales Data) |  | Similarly, Admin can maintain for different DC. |
| 30 | Enter Distribution Center - MRP Data | In the MRP Data > MRP Data section, make following entries:Availability Check: for example, ST (Consider only stock)MRP Type: For example,, R1 (Time-Phased Planning)MRP Controller: For example, 001/MRP Controller 001 |  |  |
| 31 | Enter Distribution Center - Lot-Size Data | In the MRP Data > Lot-Size Data section, make the following entry:Lot Sizing Procedure: for example,, EX/ Lot-for-lot order quantity |  |  |
| 32 | Enter Distribution Center - Procurement Data | In the MRP Data > Procurement section, make the following entry:Planned Delivery Time: for example, 3Planning Calendar: P01 |  |  |
| 33 | Enter Distribution Center - Storage Location | In the Storage > Storage Locations > Distribution Center - Storage Locations section, choose Create and make following entries:Storage Location: 995A |  |  |
| 34 | Return to Main Screen | Choose Apply to return to Product screen. | The Product screen displays. |  |
| 35 | Create Stores | In the Stores view, choose Create. | The Store view opens. |  |
| 36 | Enter Stores - General Information | In the General Information section, make following entries if not maintained:Store: Store number for example, 3392 (Reference Store comes by default, no need to enter explicitly and remain Non Editable)Negative Stock Allowed in Plant: X |  | Similarly, Admin can maintain for different Stores |
| 37 | Enter Loading group under Sales Data | In the Sales Data section make following entry:Loading Grp: for example, 0001(Crane) |  |  |
| 38 | Enter Stores - MRP Data | In the MRP Data > MRP Data section, make following entries:Availability Check: for example, ST/Consider only stockMRP Type: For example, RF/Replenish with dyn.TargetStock(Dynamic Target Stock gets calculated at runtime during the planning run from forecast sales value)In the MRP Data > Store Replenishment Data section, make following entries:Target Range of Coverage: 5 DAY |  |  |
| 39 | Enter Store - Procurement Data | In the MRP Data > Procurement section, make the following entry:Planned Delivery Time: for example, 3Goods Receipt Processing Time: for example, 1 |  |  |
| 40 | Enter Store - Storage Location | In the Storage > Storage Locations > Store - Storage Locations section, choose Create and make following entries:Storage Location: 994A |  |  |
| 41 | Return to Main Screen | Choose Apply to return to Product screen. | The Product screen displays. |  |
| 42 | Save Your Data | Choose Create. | System message displays that object is saved. | As a next step,You need to maintain purchasing Info record.You can change or maintain or update the article created above, via Maintain Article (MM42) app. |
| 43 | Access the SAP Fiori App | Open Manage Purchasing Info Records (F1982) app | The Manage Purchasing Info Records (F1982) (Initial Screen) is displayed. |  |
| 44 | Choose Create button to create Info-record | Choose Create to create purchasing info record. | New Purchasing Info Record screen is displayed.Purchaser can maintain different kind of Inforecord via this app. For example, consignment, standard, sub-contracting and so on. |  |
| 45 | Enter Details in the Purchasing Info Record Screen | In the Purchasing Info Record screen, enter the below details:P urchasing Info Record category : (Standard)Supplier Details 33213002/Retail Food Supplier AEMaterial : <R_VVVVV>Purchasing Organization 3310/Purch. Org. 3310Purchasing group 002/Group 002Delivery and Quantity:Delivery Time in Days: (5)Order Unit: (CRT)Standard Order Quantity: <value>Confirmation Control: (Inbound Delivery) | Purchasing view is displayed. |  |
| 46 | Enter Conditions | Conditions screen open up with a Condition PPR0. Select Create and maintain validity dates and amount for the same.Valid From <dates>Valid To <dates>Amount <value>Choose Apply.Select Create. | Article gets updated with the purchasing info record. |  |

Maintain Components in alternate UOM via Product Master App

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Product Master Data (F1602) app. | Manage Product Master Data screen is displayed. |  |
| 3 | Search for the Full Article | In the filter section, enter the full article created above and press GOProduct: Article number (<R_VVVVV>) | You will see the filtered result, where you will see your Full Article. |  |
| 4 | Click on the filtered result to see details of the Full Article | Click on the Filtered article | Product Details in display mode appears |  |
| 5 | Press EDIT button to add the component details | Press Edit button | Product Details appear in change mode |  |
| 6 | Navigate to the General Information à Unit of Measure | Select alternate unit of measure Crate (CRT) and navigate to the details. | Unit of Measure details screen appear |  |
| 7 | Navigate to Components section and Add Component for alternate UOM | In the Components section, enter the following:Product: Empties article (e.g., <R_YYYYY> & <R_ZZZZZ>)QuantityPress Apply |  |  |
| 8 | Save the Article | Press Save button. | Article gets saved |  |

#### Maintain Assortments for Full Article

##### Assign Full Article to Assortment Module

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You assign the full article to the assortment module version.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Assortment Specialist - Retail. |  |  |
| 2 | Access the App | Open Manage Assortment Modules (F4892) app. | The app opens and a list report with an empty result table appears. |  |
| 3 | Search for Assortment Module | Set the Assortment Module filter by entering Assortment Module ER AE and choose Go. | The list report contains one line item with assortment module. |  |
| 4 | Navigate to Assortment Module | In the list report, click the line item of assortment module Assortment Module ER AE to trigger the navigation. | The object page of assortment module Assortment Module ER AE appears. |  |
| 5 | Navigate to First Version | In the Versions facet, click the line item of the version which has the earliest valid-from date (that is, the lowest line item). | The object page of the first assortment module version appears. |  |
| 6 | Start Product Assignment | In the table toolbar of the Products facet, choose Assign. | The Assign Products to Version dialog box appears. |  |
| 7 | Enter Required Data and Finish Product Assignment | In the Assign Products to Version dialog box, make the following entries and choose Assign:Products: <Full Article>(<R_XXXXX>, <R_VVVVV>)Select Assign to Follow-on Versions checkbox. | The dialog box disappears, and the newly assigned product appears in the table of the Products facet.The line item contains the following data:Products: <Full Article>(<R_XXXXX>, <R_VVVVV>)Assigned From/To: <Your Start Date of the First Version> - <End Date of the First Version>.Full Article is listed along with components (Empties). |  |

|  |
| --- |
| NoteEmpties are listed automatically along with Full Article. The status of assignment to module stays as "No" for empties.Kindly refer to scope item Assortments (3I5) for more details. |

##### Assign Full Article to Distribution Center

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You assign the full article to a distribution center.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Assortment Specialist - Retail. |  |  |
| 2 | Access the App | Open Assign Products to Distribution Centers (F4543) app. | The app opens and a list report with an empty result table appears. |  |
| 3 | Search for Products to Be Assigned | Set the Product filter by entering product <Full Article>, (e.g.) <R_XXXXX>, <R_VVVVV> and choose Go. |  |  |
| 4 | Start Product Assignment to Distribution Center | Select product by selecting the checkbox and choose Add Assignments. | The Products to Distribution Centers Assign dialog box appears. |  |
| 5 | Select Distribution Center and Finish Product Assignment to Distribution Center | In the Assign Products to Distribution Centers dialog box, search for distribution center 3350, select the corresponding checkbox, and choose Assign. | After the Full Article has been assigned, the list report displays an empty result table. |  |
| 6 | Search for Assigned Products | Set the Assigned to DC filter to Yes and choose Go. | Full Article appears as line item in the result table of the list report. |  |
| 7 | Check for Correctness of Product Assignment | In the list report, click the line item of Full Article to trigger the navigation. | The object page of the product appears. Check whether the Product Assignments facet contains a line item with the following data:Distribution Center: 3350Assigned From: <Current date>Assigned To: 31.12.9999Full Article is listed along with components (Empties). |  |

|  |
| --- |
| NoteEmpties are listed automatically along with Full Article. The status of assignment to DC stays as "No" for empties.Kindly refer to scope item Assortments (3I5) for more details. |

#### Create Purchase Conditions for Empties

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity to create purchase conditions for empties.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data (Retail). |  |  |
| 2 | Access the App | Open Create Price Conditions - Purchasing (MEK1) app. | Create Price Conditions - Purchasing (MEK1) screen is displayed. |  |
| 3 | Enter Values | On the Create Price Conditions - Purchasing (MEK1) screen, enter the following details and select ENTER:Condition Type: PPR0 (Default Gross Price) and select ENTERKey Combination: <Select the relevant key combination from menu help>, for instance, <“Empties” Prices (Material-Dependent)> and select Choose.Enter <Empties>(<R_YYYYY>, <R_ZZZZZ>)Enter <Amount>Enter “Unit” <Currency> |  |  |
| 4 | Save the Record | Choose Save. | The condition record is saved. |  |

Result

Purchase conditions for empties are created.

|  |
| --- |
| NoteIf you want to operate in more than one country, please create new articles for full and empties and maintain purchase conditions if amount and currencies are different.Purchase info records should not be maintained for empties. |

#### Create Sales Conditions for Empties

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity to create sales condition for empties in stores and distribution center.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Pricing Specialist (Retail). |  |  |
| 2 | Access the App | Open Manage Prices - Sales (F4111) app. | Manage Prices - Sales (F4111) screen is displayed. |  |
| 3 | Enter Values | On the Manage Prices - Sales (F4111) screen, select Create and enter the following details and select ENTER:Condition Type: ESP0 (Sales Price Store)Condition Table: <Select the relevant condition table and access sequence from menu help>, for instance, 118 Product and press Enter.Note Condition record should be created at article level, Access – 005 for Condition Table – 118.Product: <Empties>(<R_YYYYY>, <R_ZZZZZ>)Condition Amount or Ratio: <Enter an amount> and <Currency> |  |  |
| 4 | Save the Record | Choose Save. | The condition record is saved. |  |
| 5 | Enter Values | On the Manage Prices - Sales (F4111) screen, select Create and enter the following details and select ENTER:Condition Type: ESP2 (Sales Price DC)Condition Table: <Select the relevant condition table and access sequence from menu help>, for instance, 118 Product and press Enter.Note Condition record should be created at article level, Access – 005 for Condition Table – 118.Product: <Empties>(<R_YYYYY>, <R_ZZZZZ>)Condition Amount or Ratio: <Enter an amount> and <Currency> |  |  |
| 6 | Save the Record | Choose Save. | The condition record is saved. |  |

Result

Sales conditions for empties are created.

|  |
| --- |
| Note If you want to operate in more than one country, please create new articles for full and empties and maintain sales conditions if amount and currencies are different. |

#### Create Sales Conditions for Full Article

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
| 3 | Enter Article Basic Data | In the Change Material (Initial screen)Material: Article numberEnter Full Article,(<R_XXXXX>, <R_VVVVV>) |  |  |
| 4 | Choose Views | Select Sales views and choose Continue. | The Change Material R_XXXXX (Sales) screen is displayed . |  |
| 5 | Enter Organizational Level Data | In Switch Validity Area, in the Areas of Validity section, enter descriptions for the following:Sales Unit: (PC)Sales Org.: (3310/ Dom. Sales Org)Distr. Channel: (50 - Distribution)Choose Continue. |  |  |
| 6 | Enter Sales Data | On the Change Material R_XXXXX (Sales) screen, make the following entries:(All the below should ideally get filled automatically, but if you need to maintain any deviation then you can go ahead and maintain)For sale from: <date>For sale till: <date>Item Cat. Group: (FULL)Cash Discount : (X)PP Det. Seq. (Purchase Price Determination Sequence): (01/ Standard with price determination)SP Determ. Seq. (Sales Price Determination Sequence): (01/ Calculate SP from planned markup)Final price: (<value>)Save Calculated Price: (X) |  |  |
| 7 | Save Your Data | Choose Save. | Sales prices are created.Material R_XXXXX changed message appears on the status bar. |  |
| 8 | Choose Views | Select Sales views and choose Continue. | The Change Material R_XXXXX (Sales) screen is displayed . |  |
| 9 | Enter Organizational Level Data | In Switch Validity Area, in the Areas of Validity section, enter descriptions for the following:Sales Unit: (CRT)Sales Org.: (3310/ Dom. Sales Org)Distr. Channel: (40 - Store Sales)Choose Continue. |  |  |
| 10 | Enter Sales Data | On the Change Material R_XXXXX (Sales) screen, make the following entries:(All the below should ideally get filled automatically, but if you need to maintain any deviation then you can go ahead and maintain)For sale from: <date>For sale till: <date>Item Cat. Group: (FULL)Cash Discount : (X)PP Det. Seq. (Purchase Price Determination Sequence): (01/ Standard with price determination)SP Determ. Seq. (Sales Price Determination Sequence): (01/ Calculate SP from planned markup)Final price: (<value>)Save Calculated Price: (X) |  | Repeat the same steps 9 and 10 for maintaining distribution chain – CRT/3310/50. |
| 11 | Save Your Data | Choose Save. | Sales prices are created.Material R_XXXXX changed message appears on the status bar. |  |

### Procurement from External Supplier (Full Article)

#### Create Purchase Order Directly

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process, purchase order is created directly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser (Retail). |  |  |
| 2 | Access the App | Open Create Purchase Order - Advanced (ME21N) app. | Create Purchase Order intial screen is displayed. |  |
| 3 | Enter Purchase Order Data | Enter all of the necessary data:Order type: NB Standard POSupplier: 33213002In Header section, on the Org. Data tab, make the following entries:Purchasing Org.: 3310Purchasing Group: 001Company Code: 3310In Items section,Material: R_2010Plant: 3350Storage Location: 995A(Automatically determines)Quantity: 100Unit of Measure: CRTNet Price: XX(Automatically determines) | Purchase order details provided. |  |
| 4 | Save the Purchase Order | Choose Save. | Purchase order is created with full product and empties.Make a note of the purchase order number. |  |

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
| 3 | Start Selection for Inbound Delivery Creation | On the Create Inbound Delivery (VL31N) app screen, enter the following:Supplier: 33213002Purchase Order:<your Purchase Order document number>Select Continue. |  |  |
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

#### Analyze Stock Overview (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the stock overview is displayed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Inventory Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Stock - Single Material (F1076) . | The Stock Single Material screen is displayed. |  |
| 3 | Enter Material | Enter the following entry in the Material field.Select the material from the interactive value help.Material: R_2010 | The Stock Overview for the Material is shown. |  |
| 4 | Change View | You need to choose the icon Chart View in order to change to a graphical view. | A Bar Chart for the stock by Plant / Storage Location is displayed. |  |
| 5 | Back to SAP Fiori Launchpad | Choose Home to go back to the SAP Fiori launchpad. | The SAP Fiori launchpad is displayed. |  |

#### Analyze Stock Overview for Empties

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, the tied and untied stock of empties are displayed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk (Retail). |  |  |
| 2 | Access the Application | Open Display Empties Stock (WBF1) app. | Stock Overview for Empties screen displays. |  |
| 3 | Enter the Parameters | Enter the following data under Select. Criteria:“Empties“ material: R_2011 and R_2012Plant: 3350Choose Execute. | Stock Overview for Empties screen displays with the details of empties material entered. |  |
| 4 | Verify the Stock Details | Stock details of the empties material displays. | Stock details of empties material is displayed. |  |

### Store Ordering from Distribution Center (Full Article)

#### Create Stock Transfer Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you create a stock transfer order (STO) manually.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser (Retail). |  |  |
| 2 | Access the App | Open Create Purchase Order - Advanced (ME21N) app. | Create Purchase Order - Advanced (ME21N) app screen is displayed. |  |
| 3 | Enter Order Document Type and Other Data | Enter the following data, then select Enter:Order Type: StockTranspOrderDel or UD StockTranspOrderDelSupplying Plant: 3350On the Header / Org. Data tab:Company Code: 3310Purchasing Org.: 3310Purchasing Group: 001In Item Overview section:Material: R_2010Plant: 3340Storage Location: 994APO Quantity: xUnit of Measure: CRT | Data is entered. The item detail screen is displayed. |  |
| 4 | Save Stock Transfer Order | Select Save and when the stock transfer order number is displayed, note it down for further use. | A new stock transfer order is created. order number is displayed. |  |

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
| 3 | Start Selection for Outbound Delivery Creation | On the entry screen of the Purchase Orders, Fast Display app, make the following entries and Select Execute:Remove Deliv. Creation Date (both from and to dates)Shipping point: 3350Go to Purchase Orders tab view, enter Purchasing Document:STO Document Number created earlier, in chapter [Create Stock Transfer Order](#unique_42) [page ] 77. | A list of purchasing documents for the selected shipping point is displayed. |  |
| 4 | Select Purchasing Document for Outbound Delivery Creation | Mark your purchasing documents and select Background. | Outbound delivery document is created. |  |
| 5 | View the Created Outbound Delivery Document Number | Select Log for delivery creation, then select Documents on the right top of the Delivery Creation Log screen . | Outbound delivery document number is displayed. |  |

#### Pick and Post Goods Issue for Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you pick and post the goods issue to remove them from the distribution center's inventory management system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access App | Open Change Outbound Delivery (VL02N) app. |  |  |
| 3 | Open Outbound Delivery Document | On the Change Outbound Delivery (VL02N) app screen, enter <your outbound delivery document number> and select Continue. |  |  |
| 4 | Specify Picked Quantity | Go to Picking tab and specify: Picked Qty : <Enter quantity equal to delivery quantity> for full article | Picked quantity is updated for full article. |  |
| 5 | Save the Outbound Delivery Document | Select Save. | Outbound delivery document is saved. |  |
| 6 | Post Goods Issue | On the Change Outbound Delivery (VL02N) app screen, enter <your outbound delivery document number> and select Post Goods Issue. | Goods issue is successful. Inventory stock is reduced from the supplying plant. |  |

#### Post Goods Receipt for Outbound Delivery

|  |
| --- |
| Note You have to perform [My Store Assignment](#unique_12) [page ] 18 before performing the Post Goods Receipt for Outbound Delivery. |

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
| 2 | Access the Application | Open Receive Products (F1248) app. | Receive Products screen is displayed. |  |
| 3 | Enter Outbound Delivery Number | Select Enter ID.In the Find a Document pop-up <Enter Outbound Delivery Number Created earlier>Select OK. | The selected outbound delivery details are displayed. |  |
| 4 | Check and Post the Goods Receipt for Outbound Delivery | In the Product section, toggle Checked on the bottom right of the screen. Select Post. | Document item was posted successfully message is displayed. |  |

#### Analyze Stock Overview (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the stock overview is displayed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Inventory Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Stock - Single Material (F1076) . | The Stock Single Material screen is displayed. |  |
| 3 | Enter Material | Enter the following entry in the Material field.Select the material from the interactive value help.Material: R_2010 | The Stock Overview for the Material is shown. |  |
| 4 | Change View | You need to choose the icon Chart View in order to change to a graphical view. | A Bar Chart for the stock by Plant / Storage Location is displayed. |  |
| 5 | Back to SAP Fiori Launchpad | Choose Home to go back to the SAP Fiori launchpad. | The SAP Fiori launchpad is displayed. |  |

#### Analyze Stock Overview for Empties

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, the tied and untied stock of empties are displayed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk (Retail). |  |  |
| 2 | Access the Application | Open Display Empties Stock (WBF1) app. | Stock Overview for Empties screen displays. |  |
| 3 | Enter the Parameters | Enter the following data under Select. Criteria:“Empties“ material: R_2011 and R_2012Plant: 3340Choose Execute. | Stock Overview for Empties screen displays with the details of empties material entered. |  |
| 4 | Verify the Stock Details | Stock details of the empties material displays. | Stock details of empties material is displayed. |  |

### Transfer Data to Point-of-Sale (POS)

Point-of-sale (POS) systems in the stores must be provided with the data necessary to enable selling articles to consumers, such as sales prices and article master data (including article description, tax information, and Global Trade Item Number (GTIN) for scanning).

Supply the POS with all needed master data via an initial load, for example when a new store is opened.

Automatically update the POS with the changed article data in regular intervals.

In exceptional cases, you can manually start an immediate supply of the POS, such as for short-term sales price changes.

|  |
| --- |
| Note Refer to scope item Store Connectivity – Outbound (3I2) for more details. |

### Process Point-of-Sale (POS) Transactions

Business transactions originating from point-of-sale (POS) solutions in the stores are regularly transferred and trigger the posting of relevant documents.

Relevant transactions include sales, returns, customer order payments, and pure financial transactions. Based on this, documents for goods movements and billing are created, as well as the respective financial postings.

The processed sales data are the basis for follow-on processes like replenishment.

|  |
| --- |
| Note Refer to scope item Store Connectivity – Inbound (3HV) for more details. |

### Returns from Store (Untied Empties)

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
| 3 | Enter Parameters | Select Order Type as UD2 STO Del Return from dropdown list.Enter the following details:Supplying Plant: 3350Doc.Date: <Current Date>Select Org.Data tabEnter below detailsPurch. Org: 3310Purch. Group: 001Company Code: 3310 | Required parameters are defined. |  |
| 4 | Enter Parameters | Expand Item Overview sectionEnter below details:Material: R_2011 and R_2012PO Quantity: 2Deliv. Date: < Provide any future date>Plant: 3340 |  |  |
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
| 4 | Parameter that Get Determined Automatically | In Item Overview section, enter the following detail:Putaway Qty: <2>Storage Location: 995A | Parameters entered. |  |
| 5 | Post Goods Receipt | Choose Post Goods Receipt. | Goods Receipt for inbound delivery XXXXXXXX posted (Material Document xxxxxxxxxx) message is displayed. |  |

#### Analyze Stock Overview for Empties

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, the tied and untied stock of empties are displayed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk (Retail). |  |  |
| 2 | Access the Application | Open Display Empties Stock (WBF1) app. | Stock Overview for Empties screen displays. |  |
| 3 | Enter the Parameters | Enter the following data under Select. Criteria:“Empties“ material: R_2011 and R_2012Plant: 3340Choose Execute. | Stock Overview for Empties screen displays with the details of empties material entered. |  |
| 4 | Verify the Stock Details | Stock details of the empties material displays. | Stock details of empties material is displayed. |  |

### Returns to Supplier (Untied Empties)

#### Create Returns Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process returns purchase order to supplier is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Purchaser (Retail). |  |  |
| 2 | Access the App | Open Create Purchase Order - Advanced (ME21N) app | Create Purchase Order - Advanced (ME21N) screen is displayed. |  |
| 3 | Enter Parameters | Select Order type: Enh.Ret.to Supplier from dropdown listEnter the following details:Supplier: 33213002Doc.Date: <Current Date>Select Org.Data tabEnter below detailsPurch. Org: 3310Purch. Group: 001Company Code: 3310 |  |  |
| 4 | Enter Parameters | Expand Item Overview sectionEnter below details:Material: R_2011 and R_2012PO Quantity: 2Deliv. Date: <Provide any future date>Plant: 3350 |  |  |
| 5 | Enter Parameters | Select Returns tab in the Header sectionFrom the Return Reason drop down list, select Product damagedFrom the Follow-Up-Activity drop down list, select Ship to SupplierChoose Copy to Items. | Item level the Returns Item flag is set. |  |
| 6 | Save Returns Purchase Order | Choose Save. | Return Purchase order is created.Make a note of return purchase order. |  |

#### Monitor Returns Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process returns purchase order is monitored.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Purchaser (Retail). |  |  |
| 2 | Access the App | Open Display Purchase Order - Advanced (ME23N) app. | Display Purchase Order - Advanced (ME23N) screen is displayed. |  |
| 3 | Access Return Purchase Order | Choose Document Overview OnFrom the Selection Variants dropdown list, select Purchase Orders | Purchasing Document screen is displayed |  |
| 4 | Access Returns Purchase Order | In the Program Selections section, enter below details:Purchasing Document : <Returns Purchase Order>Choose Execute. | Purchase order is displayed in the Document overview section. |  |
| 5 | Select Return Purchase Order | Select Return Purchase orderChoose Adopt. | Return purchase order is displayed. |  |
| 6 | Check Returns Overview | Choose Returns Tab,Choose Returns Overview. | Returns Overview for Returns Purchase Order xxxxxxxxxx screen is displayed. |  |
| 7 | Check Processing Status | Check Processing Status. | Processing Status is displayed as Process Incomplete. |  |
| 8 | Check Return Steps | In the Detail Tree sectionCheck Return Purchase Order status in Return Steps Column. | Processing status is green. |  |

#### Create Outbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process outbound delivery for the returns purchase order is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Shipping Specialist. |  |  |
| 2 | Access the App | Open My Purchase Orders - Due for Delivery (VL10B) app. | Purchase Order s, Fast Display screen is displayed. |  |
| 3 | Enter Parameters | Enter below detail,CalcRuleDefltDlvCrDt: <blank>Choose Purchase Orders and enter below detail,Purchasing Document: <Returns Purchase Order>Choose Execute. | Activities Due for Shipping "Purchase Orders, Fast Display" screen is displayed. |  |
| 4 | Create Outbound Delivery | Select Return Purchase OrderChoose Background. | See Log for information about creating deliveries message is displayed. |  |
| 5 | Check the Outbound Delivery Number | Choose the newly created line item with the same Return Purchase Order entryFrom the <!-- image omitted: unnamed -->(More) icon drop down list, select Show/Hide Delivery. | Outbound Delivery number xxxxxxxx is displayed in the Document coloumn.Make a note of outbound delivery number. |  |

#### Pick and Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process post goods issue for the returns purchase order is initiated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Shipping Specialist |  |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N) app. | Change Outbound Delivery (VL02N) screen is displayed. |  |
| 3 | Enter Parameters | Enter the Outbound Delivery : <Outbound Delivery number>Choose Continue. | RTS Outbound Dlv. XXXXXXXX Change: Overview screen is displayed. |  |
| 4 | Enter the Picked Quantity | Choose PickingIn the All Items section,Enter the below field as value in Deliv.Qty ,Picked Qty : <Deliv.Qty>Press Enter. | OvrllPickStatus is displayed as C (Fully Picked). |  |
| 5 | Post Goods Issue | Choose Post Goods Issue. | RTS Outbound Dlv. XXXXXXXX saved, material document XXXXXXXXXX created message is displayed. |  |

#### Analyze Stock Overview for Empties

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, the tied and untied stock of empties are displayed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk (Retail). |  |  |
| 2 | Access the Application | Open Display Empties Stock (WBF1) app. | Stock Overview for Empties screen displays. |  |
| 3 | Enter the Parameters | Enter the following data under Select. Criteria:“Empties“ material: R_2011 and R_2012Plant: 3350Choose Execute. | Stock Overview for Empties screen displays with the details of empties material entered. |  |
| 4 | Verify the Stock Details | Stock details of the empties material displays. | Stock details of empties material is displayed. |  |

### Returns from Store (Full Article)

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. |  |  |
| 2 | Access the App | Open Create Purchase Order - Advanced (ME21N) app. | The Create Purchase Order - Advanced (ME21N) screen is displayed. |  |
| 3 | Enter Parameters | Select Order Type as UD2 STO Del Return from dropdown list.Enter the following details:Supplying Plant: 3350Doc.Date: <Current Date>Select Org.Data tabEnter below detailsPurch. Org: 3310Purch. Group: 001Company Code: 3310 | Required parameters are defined. |  |
| 4 | Enter Parameters | Expand Item Overview sectionEnter below details:Material: R_2010PO Quantity: 2Deliv. Date: < Provide any future date>Plant: 3340 |  |  |
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
| 4 | Parameter that Get Determined Automatically | In Item Overview section, enter the following detail:Putaway Qty: <2>Storage Location: 995A | Parameters entered. |  |
| 5 | Post Goods Receipt | Choose Post Goods Receipt. | Goods Receipt for inbound delivery XXXXXXXX posted (Material Document xxxxxxxxxx) message is displayed. |  |

#### Analyze Stock Overview for Empties

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, the tied and untied stock of empties are displayed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk (Retail). |  |  |
| 2 | Access the Application | Open Display Empties Stock (WBF1) app. | Stock Overview for Empties screen displays. |  |
| 3 | Enter the Parameters | Enter the following data under Select. Criteria:“Empties“ material: R_2011 and R_2012Plant: 3340Choose Execute. | Stock Overview for Empties screen displays with the details of empties material entered. |  |
| 4 | Verify the Stock Details | Stock details of the empties material displays. | Stock details of empties material is displayed. |  |

### Returns to Supplier (Full Article)

#### Create Returns Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process returns purchase order to supplier is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Purchaser. |  |  |
| 2 | Access the App | Open Create Purchase Order - Advanced (ME21N) app | Create Purchase Order - Advanced (ME21N) screen is displayed. |  |
| 3 | Enter Parameters | Select Order type: Enh.Ret.to Supplier from dropdown listEnter the following details:Supplier: 33213002Doc.Date: <Current Date>Select Org.Data tabEnter below detailsPurch. Org: 3310Purch. Group: 001Company Code: 3310 |  |  |
| 4 | Enter Parameters | Expand Item Overview sectionEnter below details:Material: R_2010PO Quantity: 2Deliv. Date: <Provide any future date>Plant: 3350 |  |  |
| 5 | Enter Parameters | Select Returns tab in the Header sectionFrom the Return Reason drop down list, select Product damagedFrom the Follow-Up-Activity drop down list, select Ship to SupplierChoose Copy to Items. | Item level the Returns Item flag is set. |  |
| 6 | Save Returns Purchase Order | Choose Save. | Return Purchase order is created.Make a note of return purchase order. |  |

#### Monitor Returns Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process returns purchase order is monitored.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Purchaser (Retail). |  |  |
| 2 | Access the App | Open Display Purchase Order - Advanced (ME23N) app. | Display Purchase Order - Advanced (ME23N) screen is displayed. |  |
| 3 | Access Return Purchase Order | Choose Document Overview OnFrom the Selection Variants dropdown list, select Purchase Orders | Purchasing Document screen is displayed |  |
| 4 | Access Returns Purchase Order | In the Program Selections section, enter below details:Purchasing Document : <Returns Purchase Order>Choose Execute. | Purchase order is displayed in the Document overview section. |  |
| 5 | Select Return Purchase Order | Select Return Purchase orderChoose Adopt. | Return purchase order is displayed. |  |
| 6 | Check Returns Overview | Choose Returns Tab,Choose Returns Overview. | Returns Overview for Returns Purchase Order xxxxxxxxxx screen is displayed. |  |
| 7 | Check Processing Status | Check Processing Status. | Processing Status is displayed as Process Incomplete. |  |
| 8 | Check Return Steps | In the Detail Tree sectionCheck Return Purchase Order status in Return Steps Column. | Processing status is green. |  |

#### Create Outbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process outbound delivery for the returns purchase order is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Shipping Specialist. |  |  |
| 2 | Access the App | Open My Purchase Orders - Due for Delivery (VL10B) app. | Purchase Order s, Fast Display screen is displayed. |  |
| 3 | Enter Parameters | Enter below detail,CalcRuleDefltDlvCrDt: <blank>Choose Purchase Orders and enter below detail,Purchasing Document: <Returns Purchase Order>Choose Execute. | Activities Due for Shipping "Purchase Orders, Fast Display" screen is displayed. |  |
| 4 | Create Outbound Delivery | Select Return Purchase OrderChoose Background. | See Log for information about creating deliveries message is displayed. |  |
| 5 | Check the Outbound Delivery Number | Choose the newly created line item with the same Return Purchase Order entryFrom the <!-- image omitted: unnamed -->(More) icon drop down list, select Show/Hide Delivery. | Outbound Delivery number xxxxxxxx is displayed in the Document coloumn.Make a note of outbound delivery number. |  |

#### Pick and Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process post goods issue for the returns purchase order is initiated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Shipping Specialist |  |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N) app. | Change Outbound Delivery (VL02N) screen is displayed. |  |
| 3 | Enter Parameters | Enter the Outbound Delivery : <Outbound Delivery number>Choose Continue. | RTS Outbound Dlv. XXXXXXXX Change: Overview screen is displayed. |  |
| 4 | Enter the Picked Quantity | Choose PickingIn the All Items section,Enter the below field as value in Deliv.Qty ,Picked Qty : <Deliv.Qty>Press Enter. | OvrllPickStatus is displayed as C (Fully Picked). |  |
| 5 | Post Goods Issue | Choose Post Goods Issue. | RTS Outbound Dlv. XXXXXXXX saved, material document XXXXXXXXXX created message is displayed. |  |

#### Analyze Stock Overview for Empties

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, the tied and untied stock of empties are displayed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk (Retail). |  |  |
| 2 | Access the Application | Open Display Empties Stock (WBF1) app. | Stock Overview for Empties screen displays. |  |
| 3 | Enter the Parameters | Enter the following data under Select. Criteria:“Empties“ material: R_2011 and R_2012Plant: 3350Choose Execute. | Stock Overview for Empties screen displays with the details of empties material entered. |  |
| 4 | Verify the Stock Details | Stock details of the empties material displays. | Stock details of empties material is displayed. |  |

### In-Store Inventory Management

#### Perform Physical Inventory

##### Create Physical Inventory Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A Physical Inventory (PI) document is prepared before the actual counting of the stock for the Article. It contains a list of articles which need to be counted in a store.

This process step shows you how you can create a physical inventory document for a store.

|  |
| --- |
| Note You can only have one active PI document for the combination of an article, site, and storage location. Execute preliminary step [Display Physical Inventory Document](#unique_14) [page ] 20 to check if there is an existing PI document for the combination of an article, site, and storage location. If yes, then follow preliminary step [Delete Active Physical Inventory Document (Optional)](#unique_15) [page ] 21 to delete the existing PI document before executing this step. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Inventory Manager (Retail). |  |  |
| 2 | Access app | Open Create Documents - Physical Inventory (WV31) app. | Create Physical Inventory Docs for Unrestricted -Use stock (Retail) app is accessed. |  |
| 3 | Maintain basic information | Maintain the below entries in the selection screen:Under Database Selection section enter:Plant: for example 3340Material Group: R1161002Select the Inc. Inventoried Materials checkbox.Under Data in Phys, Inv, Docmt Header section enter:Planned count date : Today’s DateSelect ON the flag for issue log in control data sectionIssue log: X | The inputs provided are accepted. |  |
| 4 | Create physical inventory document (PID) | Select Execute to create the physical inventory document. | Physical Inventory documents generated |  |
| 5 | Pick the physical inventory document | On the table under Message text column, we can see Physical Inventory Document xxxxxxxxxx is created. Keep note of the physical inventory document number.Note Multiple physical inventory documents can be created depending upon the number of articles available for physical inventory. |  |  |

Result

A physical inventory document has been created and is shown in the count products app.

##### Display Physical Inventory Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

|  |
| --- |
| Note Because the system can only have one open physical inventory document for the same material, it is necessary to check open physical inventory document before any testing procedures. |

Purpose

This process step shows, how you can display the physical inventory document created in the previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Inventory Manager (Retail). |  |  |
| 2 | Access the app | Open Manage Physical Inventory Documents (F0379A) app. |  |  |
| 3 | Enter Data | Make the following entries and choose Go:Plant:Physical Inventory Document: (Enter PI Doc number noted in the previous procedure)Choose Adapt Filters and select the below option:Adjustment Status: Select items Not Posted and Partially Posted. |  |  |
| 4 | Choose an Item | Choose the item displayed in the Physical Inventory Documents List and verify the physical inventory documents detailsNote In case of multiple physical inventory documents, repeat 3 & 4 steps for each physical inventory document.Note down the physical inventory document number and the articles associated with it which needs to be counted in further steps. |  |  |

##### Perform Physical Inventory Count

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how in this application, store associates can perform a physical inventory count of all products in the store, or a cycle count of selected products. The count can be performed region (or zone wise) of the store. This process step can be used to:

- Perform annual inventory count of all products in the store
- Perform periodic inventory counts of selected products in the store
- Respond to recount requests received from head office

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Retail Store Associate. |  |  |
| 2 | Access app | Open Count Stock (F1512) app. | The list of open physical inventory documents for the store are displayed. |  |
| 3 | Start counting | Select a physical inventory document (created in step [Create Physical Inventory Document](#unique_60) [page ] 108) XXXXXXXXX from the list and select Start Count.Note In case of multiple physical inventory documents, select the physical inventory document created for product (article/material) R_2010 by following the preliminary step [Display Physical Inventory Document](#unique_14) [page ] 20. | It pops up the Enter Zone screen. |  |
| 4 | Enter zone | Select Scan and either scan the barcode of the zone or enter it manually if scanner is not available.Bar code: XXXXXXX (Product - R_2010) | Scans or accepts the EAN number of the product. |  |
| 5 | Add product | Select More (…) and Add Product to Count In the Search enter the product (picked from physical inventory document in step [Display Physical Inventory Document](#unique_61) [page ] 109).Search the Product R_2010.Select the Product R_2010 with unit of measure as CRT (Crate) to add it to count list. | The product is added to the count list. |  |
| 6 | Enter quantity | Enter the count of the product 10.Select +, we can increase the count and select – we can decrease the count. | Count of the product gets updated. |  |
| 7 | Add product | Repeat the step 5 to 6 for the Product R_2010 with unit of measure as PC (Pieces). | The product is added to the count list. |  |
| 8 | Submit count | Select More (…) and then on submit and OK in the submit count pop up. | Count submitted. A confirmation message is displayed.Zone count updated. displayed in the screen near to the physical inventory document number. |  |

##### Approve or Reschedule Stock Counts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how as a store manager, you can approve or request for recount, of the count submitted by the store associate. Once the count is approved, the stocks are updated with the count.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Retail Store Manager. |  |  |
| 2 | Access app | Open Manage Stock Counting (F1512) app. | A list of physical inventory documents is displayed. |  |
| 3 | Select physical inventory document | Select the Physical Inventory Document XXXXXXXXXX submitted by store associate in step [Perform Physical Inventory Count](#unique_62) [page ] 110 | Stock counting results are displayed in a product-centric/zone-centric or associate-centric view |  |
| 4 | Request recount | Flag Recount, as the counting difference is too high and select Submit.Select Complete This Inventory Count and select OK to submit selection popup. | A confirmation message is shown Count Submitted.The physical inventory document in the list of documents is labelled as local recount.And the same physical inventory document gets updated into Completed tab, as the Store manager activity is done. |  |
| 5 | Select physical inventory document after recount | Once the store associate recounts the physical inventory document with Local Recount status (as in step [Perform Physical Inventory Count](#unique_62) [page ] 110)Select the recounted physical inventory document | Stock counting results are displayed in a product-centric/zone-centric or associate-centric view |  |
| 6 | Approve count | Flag Count OK and Submit the physical inventory documentCheck Complete this Inventory Count and select OK for submit selection popup. | A confirmation message Count Submitted is displayed.And the physical inventory document gets updated into Completed tab, as the Store manager activity is done. |  |

##### Post Inventory Count Differences

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post the results of the physical inventory. Once the count is reviewed and approved, the store manager can post the inventory count differences.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as an Inventory Manager (Retail) |  |  |
| 2 | Access the app | Open Manage Physical Inventory Documents (F0379A) app. | Manage Physical Inventory Documents: Initial screen is displayed. |  |
| 3 | Enter inventory document data | Make the following entries:Select the arrow on right hand side to view the physical inventory document details.Physical Inventory Document: XXXXXXXXXX (Enter the physical inventory document completed in step [Approve or Reschedule Stock Counts](#unique_63) [page ] 112). | Physical Inventory document is fetched |  |
| 4 | Post Differences | Select the Material and choose Post.Enter the Posting Date: for example < Today's Date>.Choose Post. | Physical inventory is posted successfully. |  |

##### Analyze Stock Overview - Single Material

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the stock overview is displayed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Inventory Manager (Retail). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Stock - Single Material (F1076) . | The Stock Single Material screen is displayed. |  |
| 3 | Enter Material | Enter the following entry in the Material field.Select the material from the interactive value help.Material: R_2010 | The Stock Overview for the Material is shown. |  |
| 4 | Change View | You need to choose the icon Chart View in order to change to a graphical view. | A Bar Chart for the stock by Plant / Storage Location is displayed. |  |
| 5 | Back to SAP Fiori Launchpad | Choose Home to go back to the SAP Fiori launchpad. | The SAP Fiori launchpad is displayed. |  |

##### Analyze Stock Overview for Empties

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, the tied and untied stock of empties are displayed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk (Retail). |  |  |
| 2 | Access the Application | Open Display Empties Stock (WBF1) app. | Stock Overview for Empties screen displays. |  |
| 3 | Enter the Parameters | Enter the following data under Select. Criteria:“Empties“ material: R_2011 and R_2012Plant: 3340Choose Execute. | Stock Overview for Empties screen displays with the details of empties material entered. |  |
| 4 | Verify the Stock Details | Stock details of the empties material displays. | Stock details of empties material is displayed. |  |

#### Count Stock Ad hoc

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Store associates need to keep a track of the stock count for the products on need basis for each storage location available in the store. This process helps to increase the efficiency of the store replenishment process.

You can only have one active PI document for the combination of an article, site, and storage location. Execute preliminary step [Display Physical Inventory Document](#unique_14) [page ] 20 to check if there is an existing PI document for the combination of an article, site, and storage location. If yes, then follow preliminary step [Delete Active Physical Inventory Document (Optional)](#unique_15) [page ] 21 to delete the existing PI document before executing this step.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Retail Store Associate. |  |  |
| 2 | Access app | Open Count Stock Ad hoc - TODAY (F5563) app. | The Count Stock Ad hoc - TODAY (F5563) app is displayed. |  |
| 3 | Create count stock document | Select Create on the upper right corner. | A new stock document is created for the store. The location of the store is displayed in the dropdown list and prefilled with the values selected for the last created stock document.The list of products is empty. |  |
| 4 | Maintain basic information | Change Location: 994A |  |  |
| 5 | Add product by search | Select on 'Search Product' and select the required product R_2010 by searching in the search tab available. Select Add. | Once the product is added "Success" pop up message is displayed and the product is added to in process Tab. |  |
| 6 | Add product by GTIN | Select 'Scan Bar code', enter the EAN/GTIN <xxxxxxxxxxx> of another product in the Bar code field and select OK.Note Repeat step 5 to get the GTIN number for a product (displayed between product description and UOM). | The product is added to the list of products. In case the product was already contained in the list, the number increase by one. |  |
| 7 | Add product by scanning of GTIN (Optional) | Only possible on mobile device:Select scan and scan a barcode with the camera of the mobile device. | The product is added to the list of products. In case the product was already contained in the list, the number increase by one. |  |
| 8 | Add product using hardware scan (Optional) | Only possible on MDE or ruggedized devices with an extension of the Custom SAP Fiori client.Select (hardware) scan of the MDE and scan a barcode. | The product is added to the list of products. In case the product was already contained in the list, the number increase by one. |  |
| 9 | Navigate to product list | Select the product to navigate to product list screen. | The product details are displayed. |  |
| 10 | Change the stock type | Change the stock type as per requirement to Unrestricted useQuality Inspection or Blocked |  |  |
| 11 | Create new placement | Select Add, select the Quantity unit from the dropdown list and select Add. | New placement is created with the selected quantity unit and quantity as 0. |  |
| 12 | Adjust the quantity | Either enter the quantity field directly in the quantity field for the new placement created or select Additional Unit, enter the quantity: 20 and Quantity unit: CRT and select Add. | Quantity updated message is displayed and quantity is successfully updated in the new placement |  |
| 13 | Back to overview | Select Back to Overview. | Navigation to the main screen. |  |
| 14 | Document Posting | Select Submit | The status of the stock document is changed from ‘In Process' to ‘Posted'.Verify if the posting was successful in step [Analyze Stock Overview - Single Material](#unique_65) [page ] 114. |  |
| 15 | Print and submit | Execute steps from 1 to 13 and select Print and Submit. | The status of the stock document is changed from ‘In Process’ to ‘Posted’.Print document is sent to the cloud print manager.Verify if the posting was successful in step [Analyze Stock Overview - Single Material](#unique_65) [page ] 114. |  |

##### Analyze Stock Overview - Single Material

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the stock overview is displayed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Inventory Manager (Retail). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Stock - Single Material (F1076) . | The Stock Single Material screen is displayed. |  |
| 3 | Enter Material | Enter the following entry in the Material field.Select the material from the interactive value help.Material: R_2010 | The Stock Overview for the Material is shown. |  |
| 4 | Change View | You need to choose the icon Chart View in order to change to a graphical view. | A Bar Chart for the stock by Plant / Storage Location is displayed. |  |
| 5 | Back to SAP Fiori Launchpad | Choose Home to go back to the SAP Fiori launchpad. | The SAP Fiori launchpad is displayed. |  |

##### Analyze Stock Overview for Empties

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, the tied and untied stock of empties are displayed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk (Retail). |  |  |
| 2 | Access the Application | Open Display Empties Stock (WBF1) app. | Stock Overview for Empties screen displays. |  |
| 3 | Enter the Parameters | Enter the following data under Select. Criteria:“Empties“ material: R_2011 and R_2012Plant: 3340Choose Execute. | Stock Overview for Empties screen displays with the details of empties material entered. |  |
| 4 | Verify the Stock Details | Stock details of the empties material displays. | Stock details of empties material is displayed. |  |

#### Adjust Mass Stock - Options

##### Adjust Mass Stock (Option 1)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The app Adjust Mass Stock (F4959) can be used to adjust the stock for different reasons such as damaged, stolen, own consumption, etc. “Mass” means scanning and posting the adjustment for several products at once. A typical use case would be: As a store associate, you take a shopping cart in the morning, you walk in the store and collect all products that are for some reason not sellable. Then, you open this app, you scan the products and post the adjustment in the S/4 system. Therewith, you correct the stock quantity. As a result, your store replenishment will be more accurate. And, when you look up the product for customer service, you will have an accurate stock info.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Retail Store Associate . |  |  |
| 2 | Access app | Open Adjust Mass Stock - TODAY (F4959) app. | The Adjust Mass Stock (F4959) app is displayed. |  |
| 3 | Create stock adjustment | Select Create on the upper right corner. | A new stock adjustment in in process status gets created for the store.If the user is new to the app, the reason and the Location of the store adjustment will be blank, which needs to be filled.If the user is not login for first-time, then the Reason and Storage location is prefilled with the values selected for the last created stock adjustment.The list of products is empty. |  |
| 4 | Maintain basic information | Maintain the following entries:Reason : Goods receipt unplanned (3)Location : 994ANote The goods movement type for adjustment posting is linked to the reason.Reason: Goods receipt unplanned (0003) is linked to movement type 501 (Receipt w/o PO) | Values are accepted. |  |
| 5 | Add product by search | Select + and select the required product R_2010 by searching in the search tab available.Select the product available in the list. Selected products will be updated in the product list.Select Add to add the product to the list. | product added message is displayed and the product added. |  |
| 6 | Add product by GTIN | Select Scan Bar Code and enter the EAN/GTIN XXXXXXX of another product in the Bar Code field and select OK. | The product is added to the list of products with message product added.In case the product was already in the list, the quantity should increase by 1 with a message product added. |  |
| 7 | Optional: add product by scanning of GTIN | Only possible on mobile device:Select Scan to scan a barcode with the camera of the mobile device. | The product is added to the list of products with message product added.In case the product was already in the list, the quantity should increase by 1 with a message product added. |  |
| 8 | Optional: Add product using hardware scan | Only possible on MDE or ruggedized devices with an extension of the Custom SAP Fiori clientSelect (hardware) scan of the MDE and scan a barcode | The product is added to the list of products with message product added.In case the product was already in the list, the quantity should increase by 1 with a message product added. |  |
| 9 | Adjust quantity | Enter the required Quantity: 29 to be adjusted either in the Quantity field directly or select + and enter the Quantity and select Quantity Unit from the dropdown list. | The price is updated accordingly to the entered quantity. |  |
| 10 | Submit stock adjustment | Select SubmitMessage Stock Adjustment is Submitted is displayed. | Navigate to Completed tab and refresh the adjustments.Validate the status of the stock adjustment is changed from In Process to Posted. |  |
| 11 | Print and submit | Follow the test steps from 1 to 9 and select Print and submit.It displays message Print and submit request completed. | Navigate to Completed tab and refresh the adjustments.Validate the status of the stock adjustment is changed from In Process to Posted. |  |

##### Adjust Mass Stock with Add Claim (Option 2)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

While performing goods receiving, you notice that a product was arrived damaged. In such case, you adjust the stock because the product is not sellable, and at the same time you file a claim against the shipping company as per your contract. The adjustment including the claim can be printed out for handing to a responsible person or it can be emailed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Retail Store Associate. |  |  |
| 2 | Access app | Open Adjust Mass Stock - TODAY (F4959) app. | The Adjust Mass Stock - TODAY (F4959) app is displayed. |  |
| 3 | Create stock adjustment | Select Create from the top right corner. | A new stock adjustment in in process status gets created for the store.If the user is new to the app, the Reason and the location of the store adjustment will be blank, which needs to be filled.If the user is not login for first-time, then the Reason and Storage location is prefilled with the values selected for the last created stock adjustment.The list of products is empty. |  |
| 4 | Maintain basic information | Change theReason : Breakage/Spoilage of stock Article (1)Location : for example 994ANote The goods movement type for adjustment posting is linked to the reason.Reason: Breakage/spoilage of stock material (0001) is linked to movement type 551 (GI scrapping) | Values are accepted. |  |
| 5 | Add product by search | Select + and select the required product R_2010 by searching in the search tab available.Select ON available near to product “Selected 1” gets updated above the product.Select Add to add the product to list. | product added message is displayed and the product is added. |  |
| 6 | Adjust quantity | Enter the required Quantity: 29 to be adjusted either in the Quantity field directly or by Selecting on the + icon and by entering the Quantity and selecting the Quantity Unit from the dropdown list. | The price is updated accordingly to the entered quantity. |  |
| 7 | Add a claim | Select Add Claim and enter the mandatory field Cost Center: for example 3340Select Add | claim added message is displayed and View claim option visible below the product GTIN |  |
| 8 | Submit stock adjustment | Select SubmitMessage Stock adjustment is submitted is displayed. | Navigate to Completed tab and refresh the adjustments.Validate the status of the stock adjustment is changed from In Process to Posted. |  |
| 9 | Display claim | Select the Posted document and select Claim Info link. | Claim details is displayed. |  |

#### Transfer of Product

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows, how you can process transfers of products from one store to another store or from a store to a distribution centre. All documents relevant for a transfer are created and filled automatically. The SAP Fiori app transfer products covers and simplifies all steps involved in a product transfer and enables store associates to transfer products more efficiently.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Retail Store Associate. |  |  |
| 2 | Access app | Open Transfer Products (F2449) app. | Transfer Product app is displayed. |  |
| 3 | Create transfer | Select create transfer and enter the following fields:Receiving Site Category : StoreReceiving Site : 3341Reason for Transfer : Too much deliveredSelect CreateShows message Your Transfer was created. The detail screen is displayed containing 0 items. | Entry is updated. |  |
| 4 | Add product | Select Add Product (+) , enter the Product: R_2010 CRT in search and select Magnifying Glass icon.Select ON near to the product and select Select .(Optional: add product by Scan Product and enter the GTIN : XXXXXXXXXXX). | 1 Item added to the box message is displayed. |  |
| 5 | Adjust the quantity | Change the Quantity: 2 of the products and ENTER | The quantity is updated accordingly. |  |
| 6 | Add additional product | Select Add Product (+) , Enter the P roduct: R_2010 in search and select magnifying glass icon.Select ON near to the product and select Select.(Optional: add product by Scan Product R_2010 PC and enter the GTIN : XXXXXXXX). | 1 Item added to the box message is displayed. |  |
| 7 | Adjust the quantity | Change the Quantity: 3 of the products | The quantity is updated accordingly. |  |
| 8 | Print shipping and content labels | In More (…) Select Print | The labels will be printed. |  |
| 9 | Submit transfer | Select Submit to submit the transfer and Select OKNote If you haven't set up your printer yet, a notification will appear You have not selected a printer yet. Your documents will not be printed automatically.Submit this transfer? is displayed. | A popup with status Submitting will appear. The system constantly update the status of transfer to following status:In – Transit: Transfer Boxes are In Transit (After the goods issue posting with the movement type 641 - the TF to stock in trans). |  |

### In-Store Customer Order Management

#### Sell from Store: Immediate PickUp

##### Immediate Pickup of General Retail Articles

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
| 2 | Access the App | Open Display Customer (WDA0486) app. | Display Customer (WDA0486) screen is displayed. |  |
| 3 | Enter Parameters | Enter the below detail before selecting Continue:Customer: 33113008 | Display Customer (WDA0486) <xxxxxx> screen is displayed. |  |
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

###### Create Sales Order and Generate Invoice

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
| 4 | Enter Data | In Basic Data section of General Information tab view, enter:Customer: <Enter your customer’s ID>NoteEnter the customer or sold-to-party ID of the respective customer if already registered or newly registered.If one-time customer or sold-to party is used, then after entering your sold-to party, go to Partners , select your Sold-to Party and select Change Address button.Enter or change any field value in the Change Address pop-up and select Change Address button, for instance, enter E-Mail.Customer References: <Order Reference Text>Shipping Conditions: 03In the Products table of the Products tab view, enter the following details:Product : R_2010Requested Quantity: <Order Quantity>Item Category : <Enter Item Category>, for instance TAQ (Standard Item).Note Select Settings icon, on the View Settings pop-up, select Shipping Point checkbox and select OK.Site: <Enter your store>, for instance, 3340.Shipping Point: 33RSChoose Enter | Details are entered successfully. |  |
| 5 | Save the Order | Select Create. | Sales order is saved and Standard Order <order number> has been saved success message is displayed. |  |
| 6 | Generate Invoice | Press Generate Invoice button on the Sales Order screen. | Standard Order xxxxx has been saved message is displayed.Outbound delivery is processed with picked quantity, goods issue is posted and invoice is generated automatically. |  |
| 7 | Print Invoice (Optional) | Navigate back to the Manage In-Store Sales Orders (F7141) screen, enter Sales Order : <the sales order number created previously> and select Go.Select the resulting sales order and go to Process Flow tab and click on the Invoice, then select More Links from the Invoice Number pop-up.Select the Display Billing Documents hyperlink in the Define Link List pop-up.Go to Menu >Goto> Header> OutputSelect the output from the Output table and select Display Document. Select Print . | Invoice is previewed and printed. |  |
| 8 | Validate Follow-On Documents (Optional) | Navigate back to the Sales Orders screen and go to Process Flow tab.Select the <Relevant Follow-On Document> and , then choose More Links from the <Relevant Follow-On Document> number pop-up.Select the Display <Relevant Follow-On Document> Documents hyperlink in the Define Link List pop-up to investigate the details of the subsequent document, for example, outbound delivery, invoice documents and accounting documents. | Generated documents are displayed to investigate the details. |  |

###### Process Customer Order Payment from POS

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

### Sell from Online Store, Delivery from Distribution Center to Customer (Full Article)

#### Create Sales Order

To execute this scope item, you must have sales orders created in the system.

|  |
| --- |
| Note This process step is intended to be executed to simulate sales orders in S/4HANA Cloud Starter System. In real time, sales order creation would be triggered via an inbound service integration arrangement of the Third-Party Web-Shop with the S/4 HANA Cloud system. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Log onto the SAP Fiori Launchpad as an Retail Store Associate. |  |  |
| 2. | Access the App | Open Manage Sales Orders (F1873) app. | Manage Sales Orders (F1873) screen is displayed. |  |
| 3. | Go to App | On the Manage Sales Orders (F1873) screen, select Create > Create Sales Order VA01 option. | Create Sales Documents screen is displayed. |  |
| 4. | Enter data | Enter the following data:Order Type: ORSales Organization:3310Distribution Channel: 60Division: 00Select Continue. | Create Standard Order: Overview screen is displayed |  |
| 5. | Enter Header Data | In the header section, enter Sold-to Party: 33113005 and press EnterNow, in the Address From Master Data for Sold-to Party (Document Header) pop-up, enter <Name> in the Name section and <Telephone number> under the Communication section, then press EnterAlso enter Customer References:<Reference Document ID>, for instance, Customer PO number.Note Leave as blank if no reference needs to be maintained.Select Display header details, navigate to Shipping tab view and enter Shipping Cond.: 01 Standard |  |  |
| 6 | Enter Item Data | Select Back to navigate back to the Create Standard Order: Overview screen. In the All Items table, enter the following details in different rows and press ENTER:Row1:Material: R_2010Order Quantity: <Order Quantity>Item Category: TAQPlant: 3350 |  |  |
| 7 | Save the Order | Select Save.Note the order number for further use. | Sales order is saved and Standard Order <order number> has been saved success message is displayed. |  |

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
| 2 | Access the App | Open Schedule Delivery Creation (F2228) app. | The Application Jobs screen is displayed. The app automatically shows the history of application jobs. |  |
| 3 | Create Delivery Creation Schedule | Choose Create to define a new job. | The New Job: Schedule Delivery Creation for Sales Orders screen is displayed. |  |
| 4 | Enter job details | Enter the application job details in the Template Selection and Scheduling Options sections.Job Template: Schedule Delivery Creation for Sales OrdersJob Name: Schedule Delivery Creation for Sales OrdersChoose Step 2Flag Start ImmediatelyChoose Define Recurrence Pattern if required to change the Recurrence. | The Template Information and scheduling options are defined |  |
| 5 | Enter the Parameters | Choose Step 3In the Parameter section,Make the following entries in Sales Order section (For Testing Purpose)SD Document: <Enter your sales order document number created above in chapter [Create Sales Order](#unique_75) [page ] 129 of this document> | Parameters are entered |  |
| 6 | Check | Choose Check | Message is displayed indicating you can go ahead and schedule job. |  |
| 7 | Schedule | Choose Schedule | Automatic creation of Sales Order has been scheduled message is displayed.The Application Jobs screen displays again, and the new job displays in the Jobs table. |  |
| 8 | Check Delivery Creation Job Log | On the Application Jobs screen, after job item’s status turned to Finish, choose Status symbol in the Log column.Note Choose the Magnifier, and the job list will refresh. | The job log details is displayed. |  |

##### Pick and Post Goods Issue for Outbound Delivery from Distribution Center

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you pick and post the issue of goods in order to remove the stock from the inventory management system of the DC.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access App | Open Change Outbound Delivery (VL02N) app. | Change Outbound Delivery (VL02N) app screen is displayed. |  |
| 3 | Open Outbound Delivery document | On the Change Outbound Delivery (VL02N) app screen, enter <your outbound delivery document number> and choose Continue. |  |  |
| 4 | Specify picked quantity | Go to Picking tab and specify:Picked Qty : <Enter quantity equal to delivery quantity> | Picked quantity is updated. |  |
| 5 | Save the Outbound Delivery document | Select Save. | Outbound Delivery Document is saved. |  |
| 6 | Post Goods Issue | On the Change Outbound Delivery (VL02N) app screen, enter <your outbound delivery document number> and choose Post Goods Issue. | Goods issue is successful. Inventory stock is reduced from the supplying plant. |  |

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

Table 6:

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
| 1 | Log on | Log onto the SAP Fiori Launchpad as an Retail Store Associate. |  |  |
| 2 | Access the App | Open Manage Sales Orders (F1873) app. | Manage Sales Orders (F1873) screen is displayed. |  |
| 3 | Go to App | On the Manage Sales Order screen, enter <your sales order number> in the Sales Order field. Select Go | Sales order line item is displayed in the search result. |  |
| 4 | Open the order details | Select the sales order line item. | Display Standard Order XXXXX: Overview screen is displayed. |  |
| 5 | Navigate to Document Flow | Select Display Document Flow, to investigate the details of the subsequent document, for example, outbound delivery, goods issue, invoice documents, material and accounting documents, select the document and choose Display Document. | Generated documents are displayed on the Document Flow screen. Further, selected documents are displayed to investigate the details. |  |

### Click-and-Reserve (Payment at Store) - Order Fulfillment in Store (Stock is Available in the Store)

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
| Note This process step is intended to be executed to simulate sales orders in S/4HANA Cloud starter system. In real time, sales order creation would be triggered using an inbound service integration arrangement of the Third-Party Web-Shop with the S/4 HANA Cloud system. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Log onto the SAP Fiori Launchpad as an Retail Store Associate. |  |  |
| 2. | Access the App | Open Manage Sales Orders (F1873) app. | Manage Sales Orders (F1873) screen is displayed. |  |
| 3 | Go to App | On the Manage Sales Order screen, select Create > Create Sales Order VA01 option. | Create Sales Documents screen is displayed. |  |
| 4 | Enter data | Enter the following data:Order Type: ORSales Organization:3310Distribution Channel: 60Division: 00Select Continue. | Create Standard Order: Overview screen is displayed |  |
| 5 | Enter Header Data | In the header section, enter Sold-to Party:33113005 and press EnterNow, in the Address From Master Data for Sold-to Party (Document Header) pop-up, enter <Name> in the Name section and <Telephone number> under the Communication section, then press EnterAlso enter Customer References:<Reference Document ID>, for instance, Customer PO number.Note Leave as blank if no reference needs to be maintained.Select Display header details, navigate to Shipping tab view and enterShipping Cond.: 02 Pick-up |  |  |
| 6 | Enter Item Data | Select Back to navigate back to the Create Standard Order: Overview screen.In the All Items table, enter the following details in different rows:Material:R_2010Order Quantity: <Order Quantity>Item Category: TAQPlant: 3340 |  |  |
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

### Click-and-Collect (Pre-Paid Order)- Order Fulfillment in Store (Stock is Available in the Store)

#### Create Sales Order

To execute this scope item, you must have sales orders which in turn creates store pick-up orders and picking requests based on the configurable split criteria.

|  |
| --- |
| Note This process step is intended to be executed to simulate sales orders in S/4HANA Cloud Starter System. In real time, sales order creation would be triggered via an inbound service integration arrangement of the Third-Party Web-Shop with the S/4HANA Cloud system. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Log onto the SAP Fiori Launchpad as an Retail Store Associate. |  |  |
| 2. | Access the App | Open Manage Sales Orders (F1873) app. | Manage Sales Orders (F1873) screen is displayed. |  |
| 3. | Go to App | On the Manage Sales Orders (F1873) screen, select Create > Create Sales Order VA01 option. | Create Sales Documents screen is displayed. |  |
| 4. | Enter data | Enter the following data:Order Type: ORSales Organization:3310Distribution Channel: 60Division: 00Select Continue. | Create Standard Order: Overview screen is displayed |  |
| 5. | Enter Header Data | In the header section, enter Sold-to Party: 33113005 and press EnterNow, in the Address From Master Data for Sold-to Party (Document Header) pop-up, enter <Name> in the Name section and <Telephone number> under the Communication section, then press EnterAlso enter Customer References:<Reference Document ID>, for instance, Customer PO number.Note Leave as blank if no reference needs to be maintained.Select Display header details, navigate to Shipping tab view and enter Shipping Cond.: 02 Pick-up |  |  |
| 6 | Enter Item Data | Select Back to navigate back to the Create Standard Order: Overview screen. In the All Items table, enter the following details in different rows and press ENTER:Row1:Material: R_2010Order Quantity: <Order Quantity>Item Category: TAQPlant: 3340 |  |  |
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

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: Post Inventory Count Differences purpose says the store manager posts differences, but the steps and Overview Table assign posting to the Inventory Manager (Retail) in F0379A.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[15-retail-operations/empties-for-retail-5fk-ae-test-script-sap-s-4hana-cloud-public-edition-part-02]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5FK_S4CLD2608_BPD_EN_AE.docx` — lines 1–3124 of the extracted text · extracted with `mammoth` · 254,719 chars in the whole document
