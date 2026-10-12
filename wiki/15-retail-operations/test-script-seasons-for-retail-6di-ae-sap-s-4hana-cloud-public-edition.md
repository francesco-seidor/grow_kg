---
id: 15-retail-operations/test-script-seasons-for-retail-6di-ae-sap-s-4hana-cloud-public-edition
title: "Test Script: Seasons for Retail (6DI_AE) - SAP S/4HANA Cloud Public Edition (6DI_S4CLD2608_BPD_EN_AE)"
description: "SAP test script for Seasons for Retail (6DI_AE): create season master data, assign it to products, verify season copy across sales, purchase and STO documents."
cluster: 15-retail-operations
tags: [kb/retail-operations, topic/retail-articles-and-merchandise-categories]
aliases: [6DI_S4CLD2608_BPD_EN_AE]
keywords: ["Retail Articles, Merchandise Categories and Seasons", season management, season master data, season assignment, season determination, sales order processing, purchase order processing, stock transfer orders, outbound delivery, inbound delivery]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6DI_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1165
topic: 15-retail-operations/retail-articles-and-merchandise-categories
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Seasons for Retail (6DI_AE) - SAP S/4HANA Cloud Public Edition (6DI_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6DI_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Retail Articles, Merchandise Categories and Seasons** in Retail Operations. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Seasons for Retail (6DI_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232858838)

[2 Prerequisites 5](#_Toc232858839)

[2.1 System Access 5](#_Toc232858840)

[2.2 Roles 5](#_Toc232858841)

[2.3 Master Data, Organizational Data, and Other Data 6](#_Toc232858842)

[2.4 Business Conditions 7](#_Toc232858843)

[2.5 Preliminary Steps 8](#_Toc232858844)

[2.5.1 Set Initial Stock for Material (Optional) 8](#_Toc232858845)

[3 Overview Table 10](#_Toc232858846)

[4 Test Procedures 13](#_Toc232858847)

[4.1 Season Master Data 13](#_Toc232858848)

[4.1.1 Create Season Master Data 13](#_Toc232858849)

[4.1.2 Display Season Master Data (Optional) 16](#_Toc232858850)

[4.2 Assign Season Details to Products 18](#_Toc232858851)

[4.2.1 Assign Products to a Season, Collection or Theme using Manage Seasons Fiori App 18](#_Toc232858852)

[4.2.2 Assign Season Details using Maintain Article Application 20](#_Toc232858853)

[4.2.3 Assign Season Details using Manage Product Master App 20](#_Toc232858854)

[4.3 Change Season Details 22](#_Toc232858855)

[4.3.1 Change Season Details using Maintain Article Application (Optional) 22](#_Toc232858856)

[4.3.2 Change Season Details using Manage Product Master App (Optional) 23](#_Toc232858857)

[4.4 Display Seasons Assignment 24](#_Toc232858858)

[4.4.1 Display Seasons Assignment using Manage Seasons Application (Optional) 24](#_Toc232858859)

[4.4.2 Display Seasons Assignment using Display Article Application (Optional) 24](#_Toc232858860)

[4.4.3 Display Seasons Assignment using Manage Product Master Application (Optional) 25](#_Toc232858861)

[4.5 Sales Document Processing 26](#_Toc232858862)

[4.5.1 Sales Order Processing 26](#_Toc232858863)

[4.5.1.1 Create Sales Order 26](#_Toc232858864)

[4.5.1.2 Create an Outbound Delivery 28](#_Toc232858865)

[4.5.1.3 Display Delivery Document using Display Outbound Delivery Application (Optional) 29](#_Toc232858866)

[4.5.1.4 Process Picking for Outbound Delivery 30](#_Toc232858867)

[4.5.1.5 Post Goods Issue for Outbound Delivery 31](#_Toc232858868)

[4.5.1.6 Create Billing Document with Reference to Outbound Delivery 32](#_Toc232858869)

[4.5.1.7 Display Billing Document (Optional) 34](#_Toc232858870)

[4.6 Purchase Document Processing 35](#_Toc232858871)

[4.6.1 Purchase Order Processing 35](#_Toc232858872)

[4.6.1.1 Create Purchase Order 35](#_Toc232858873)

[4.6.1.2 Display Purchase Order (Optional) 36](#_Toc232858874)

[4.6.1.3 Create Inbound Delivery 37](#_Toc232858875)

[4.6.1.4 Display Inbound Delivery Document (Optional) 38](#_Toc232858876)

[4.6.1.5 Confirm Quantities for Putaway 39](#_Toc232858877)

[4.6.1.6 Post Goods Receipt for Inbound Delivery 40](#_Toc232858878)

[4.6.1.7 Create Supplier Invoice using Purchase Order 42](#_Toc232858879)

[4.6.1.8 Display Supplier Invoice 43](#_Toc232858880)

[4.6.2 Stock Transfer Order Processing 44](#_Toc232858881)

[4.6.2.1 Create Stock Transfer Order 44](#_Toc232858882)

[4.6.2.2 Display Stock Transfer Order (Optional) 45](#_Toc232858883)

[4.6.2.3 Create Replenishment Delivery for Stock Transfer Order 46](#_Toc232858884)

[4.6.2.4 Display Outbound Delivery Document (Optional) 47](#_Toc232858885)

[4.6.2.5 Pick, Pack, and Post Goods Issue for Delivery 48](#_Toc232858886)

[5 Appendix 50](#_Toc232858887)

[5.1 Optional Scenarios 50](#_Toc232858888)

[5.1.1 Unassign Seasons 50](#_Toc232858889)

[5.1.1.1 Unassign Season Details using Manage Seasons Fiori App (Optional) 50](#_Toc232858890)

[5.1.1.2 Unassign Season Details using Maintain Article Application (Optional) 51](#_Toc232858891)

[5.1.1.3 Unassign Season Details using Manage Product Master Data App (Optional) 52](#_Toc232858892)

[5.1.1.4 Unassign Product Variants using Manage Seasons Application (Optional) 53](#_Toc232858893)

## Purpose

Overview

Season management forms an important aspect in the product lifecycle for the retail and fashion industry. Retail production is either predetermined or varies according to the manufacturing season. To ensure that the production life cycles are aligned with the demand, the concept of seasons as a temporal unit is used as a base for the production schedule.​

This scope item describes how to set up the season data and assign your defined seasons to products. It explains how the season data is processed for various documents individually.

- In the Order-to-Cash process, this scope item starts with a customer order. Season data is assigned to products at a sales order item level. Subsequently, the season data is transferred to the follow-on documents.
- In the Procure-to-Pay process, this scope item starts with a purchase order. Season data is assigned to products at a purchase order item level. Subsequently, the season data is transferred to the follow-on documents.
- In the Stock Transfer distribution process, this scope item starts with a stock transport order. Season data is assigned to products at a stock transport order item level. Subsequently, the season data is transferred to the follow-on documents.
- In the Advanced Intercompany process, season data from the original document is transferred to the follow-on documents. The season information copied to the follow-on documents cannot be changed in those documents.
- In the Returns process, the season information is copied from the original document to the returns document.

Season Details

In retail, a season belongs to a season year and can be associated with collections. Collections can in turn be assigned to themes. Each of these entities (season, collection, theme) has a validity period. The existence of these features helps to further classify the offering for a season, apart from providing a concept for each segment of product offering.

The key attributes in product master for season functionality are season year, season, collection, theme.

The season can be maintained in the following three combinations:

- Season Year and Season
- Season Year, Season and Collection
- Season Year, Season, Collection, and Theme

Season

A season is a reporting period in which a special assortment limited to a specific period is merchandised and maintained in a certain way in the information system (for example, Summer season, Christmas season, Easter season, Winter season).

Seasons are crucial for the fashion planning of product design and merchandising.

Collection

Collections are a selection of outfits that designers assemble for the upcoming season. They reflect trends, colors, cuts, and proportions.

Theme

Themes are based on collections in the season hierarchy, and the designers represent a theme that matches them. For example, a period in history, a foreign place, a range of colors, types of fabrics, and so on.

|  |
| --- |
| Note An entity in the hierarchy is dependent on the higher-level entity. For example, a collection must be associated with a season and, likewise, a theme with a collection. Therefore, a collection or a theme can't be defined as a standalone entity in the above hierarchy. Also, a season can't be created without a season year. The timeframe is defined as an elementary attribute in the entities that indicates its applicability in a year (timeframe). You can view the hierarchy from the user menu and define a time period on one of the three levels. A sales period, purchasing period or stock transfer period defines the timeframe within which this entity (season, collection, or theme) is maintained to be valid for the corresponding application documents. |

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
| Master Data Specialist - Product Data (Retail) | SAP_BR_MD_SPCLST_ITEM_RFM | Retail Product Master Data | SAP_BR_MD_SPCLST_ITEM_RFM |  |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |
| Warehouse Clerk (Retail) | SAP_BR_WAREHOUSE_CLERK_RFM | Retail Inventory Processing | SAP_BR_WAREHOUSE_CLERK_RFM |  |
| Pricing Specialist (Retail) | SAP_BR_PRICING_SPCLST_RFM | Retail PricingRetail Markups | SAP_BR_PRICING_SPCLST_RFM |  |
| Purchaser (Retail) | SAP_BR_PURCHASER_RFM | Retail Purchasing / Retail Sourcing and Contracting | SAP_RFM_SPT_PURCHASING_PC / SAP_RFM_SPT_SOURCING_PC |  |
| Receiving Specialist | SAP_BR_RECEIVING_SPECIALIST | Receiving | SAP_BR_RECEIVING_SPECIALIST |  |
| Order Fulfillment Manager | SAP_BR_ORDER_FULFILLMNT_MNGR | Order Fulfillment Management | SAP_BR_ORDER_FULFILLMNT_MNGR |  |
| Retail Store Associate | SAP_BR_RFM_STORE_ASSOCIATE | Store Operations | SAP_BR_RFM_STORE_ASSOCIATE |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Assortment Specialist - Retail | SAP_BR_ASSTMT_SPCLST_RFM | Assortments | SAP_RFM_SPT_ASSTMT_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Customer Master | 33113007 | Wholesale non-Food AE |  |
| Generic Product | R_1070 | Running Socks Merino |  |
| Product Variants | R_1070001R_1070002 | Running Socks Merino, 35-37, WHITERunning Socks Merino, 38-39, WHITE |  |
| Sales Organization | 3310 | Dom. Sales Org |  |
| Distribution Channel | 10 | Direct Sales |  |
| Division | 00 | Product Division 00 |  |
| Sold-to Party/ Ship-to Party/Payer | 33113007 | Wholesale non-Food AE |  |
| Distribution Center (Site) | 3350 | DC 3350 AE |  |
| Storage Location | 995A | Storage Loc. DC |  |
| Shipping Point | 3350 | SP DC 3350 |  |
| Supplier | 33213004 | Retail Textile Supplier AE |  |
| Plant (Site or Location) | 3340 | Store 3340 AE |  |
| Storage Location | 994A | St.Loc.Neg.Stock |  |

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 3I1 - Products for Retail | Products must be created before assigning seasons. |
| 3I4 - Sales Pricing for Retail | Sales price must be created for generic articles and variant articles if they do not already exist. |

Additional Business Processes

This scope item supports the following business processes:

| Business Process | Scope Item ID | Condition |
| --- | --- | --- |
| Advanced Intercompany Sales | 3HS - Sales from Distribution Center | Season information is first copied from the sales order document of the selling company to the intercompany purchase order and then to the intercompany sales order without any redetermination or validation.For detailed information on the test procedure or test steps, see the Advanced Intercompany Sales test procedure. |
| Advanced Intercompany Stock Transfer | 5FX - Store Ordering from Distribution Center | Season information is copied from the intercompany purchase order of the receiving company to the intercompany sales order without any redetermination or validation.For detailed information on the test procedure or test steps, see the Advanced Intercompany Stock Transfer test procedure. |
| Returns Process for Purchase Order | 5FO - Returns to Supplier for Retail | Season information from the original purchase order can be copied to the returns purchase order.For detailed information on the test procedure or test steps, see the Returns to Supplier for Retail (5FO) test procedures. |
| Returns Process for Stock Transfer Order | 5FR - Returns from Store | Season information from the original stock transfer order can be copied to the returns stock transfer order.For detailed information on the test procedure or test steps, see the Returns from Store (5FR) test procedures. |
| Returns Process for Sales Order | BKP - Customer Returns | Season information from the original sales order can be copied to the returns sales order.For detailed information on the test procedure or test steps, see the Customer Returns (BKP) test procedures. |

|  |
| --- |
| Note In the advanced intercompany process, the season information copied to the subsequent documents cannot be changed in those documents. |

### Preliminary Steps

|  |
| --- |
| Note Steps mentioned in this section are optional. |

#### Set Initial Stock for Material (Optional)

Use

To execute this scope item, the materials must be available in stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk (Retail). |  |  |
| 2 | Access the App | Open Post Goods Movement (MIGO) app.It only displays if it was your last transaction. So, the action for the user is to select Reference Document for MIGO Transaction > Other . | The Goods Receipt Other screen is displayed. |  |
| 3 | Input Movement Type | Make the following entries and select Enter.Executable Action in Transaction MIGO: Goods ReceiptReference Document for MIGO Transaction: Other |  |  |
| 4 | Enter Material | On the Goods Receipt Other Screen: Material tab, make the following entry and select Enter:Material: R_1070 or R_1070001. |  |  |
| 5 | Enter Quantity Data | On the Goods Receipt Other screen: Quantity tab, make the following entry and select Enter:Qty in Unit of Entry: <Quantity in UOM>Unit of Entry: <UoM of material> |  |  |
| 6 | Input on the Goods Receipt Other screen: Where tab | On the Goods Receipt Other screen: Where tab, make the following entries and select Enter:Movement Type: 561Receipt per initial entry of stock balances into unrestricted usePlant: 3350Storage Location: 995ANote If generic article is entered as the material then you should enter quantity in the variant matrix grid which appears on expanding the tree display for the material.Else, enter the variant article as the material for which stock needs to be created as generic articles are logical entities which are not entitled for physical stocks creation. |  |  |
| 7 | Save Entries | Select Post. | Material document <document number> posted success message is displayed. |  |

Result

You have created stock for the materials.

## Overview Table

This scope item consists of several process steps that are listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Seasons Master Data

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Season Master Data](#unique_10) [page ] 13 | Master Data Specialist - Product Data (Retail) | Manage Seasons (F7465) | Season master data is created. |
| [Display Season Master Data (Optional)](#unique_11) [page ] 16 | Master Data Specialist - Product Data (Retail) | Manage Seasons (F7465) | Season master data is displayed. |
| [Assign Products to a Season, Collection or Theme using Manage Seasons Fiori App](#unique_12) [page ] 18 | Master Data Specialist - Product Data (Retail) | Manage Seasons (F7465) | Generic product and variants are assigned with seasons using the Manage Seasons (F7465) app. |
| [Assign Season Details using Maintain Article Application](#unique_13) [page ] 20 | Master Data Specialist - Product Data (Retail) | Maintain Article (MM42) | Generic product and variants are assigned with seasons using the Maintain Article (MM42) app. |
| [Assign Season Details using Manage Product Master App](#unique_14) [page ] 20 | Master Data Specialist - Product Data (Retail) | Manage Product Master Data (F1602) | Generic product and variants are assigned with seasons using the Manage Product Master Data (F1602) app. |
| [Change Season Details using Maintain Article Application (Optional)](#unique_15) [page ] 22 | Master Data Specialist - Product Data (Retail) | Maintain Article (MM42) | Product variants are assigned with the changed season details using the Maintain Article (MM42) app. |
| [Change Season Details using Manage Product Master App (Optional)](#unique_16) [page ] 23 | Master Data Specialist - Product Data (Retail) | Manage Product Master Data (F1602) | Product variants are assigned with the changed season details using the Manage Product Master Data (F1602) app. |
| [Display Seasons Assignment using Display Article Application (Optional)](#unique_17) [page ] 24 | Master Data Specialist - Product Data (Retail) | Display Article (MM43) | Seasons assigned for all the variants under the generic product are displayed using the Display Article (MM43) app. |
| [Display Seasons Assignment using Manage Product Master Application (Optional)](#unique_18) [page ] 25 | Master Data Specialist - Product Data (Retail) | Manage Product Master Data (F1602) | Seasons assigned for all the variants under the generic product are displayed using the Manage Product Master Data (F1602) app. |

Sales Document Processing

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Sales Order](#unique_19) [page ] 26 | Internal Sales Representative | Create Sales Orders - VA01 (VA01) | Sales orders are created with items that contain seasons that are entered manually or by automatic determination based on sales periods. |
| [Create an Outbound Delivery](#unique_20) [page ] 28 | Shipping Specialist | Create Outbound Deliveries (F0869A) | Outbound delivery is created with seasons copied from sales order. |
| [Display Delivery Document using Display Outbound Delivery Application (Optional)](#unique_21) [page ] 29 | Shipping Specialist | Display Outbound Delivery (VL03N) | Outbound delivery is displayed with the season values copied from sales order. |
| [Process Picking for Outbound Delivery](#unique_22) [page ] 30 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Picking is performed on the outbound delivery. |
| [Post Goods Issue for Outbound Delivery](#unique_23) [page ] 31 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Goods issue is performed on the outbound delivery. |
| [Create Billing Document with Reference to Outbound Delivery](#unique_24) [page ] 32 | Billing Clerk | Create Billing Documents (F0798) | Billing document is created with seasons copied from outbound delivery. |
| [Display Billing Document (Optional)](#unique_25) [page ] 34 | Billing Clerk | Manage Billing Document (F2250) | Billing document is displayed with the season values copied from outbound delivery. |

Purchase Document Processing

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Purchase Order](#unique_26) [page ] 35 | Purchaser | Create Purchase Order - Advanced (ME21N) | Purchase orders are created with items that contain seasons that are entered manually or by automatic determination based on purchasing periods. |
| [Display Purchase Order (Optional)](#unique_27) [page ] 36 | Purchaser | Display Purchase Order - Advanced (ME23N) | Purchase order is displayed with the season values. |
| [Create Inbound Delivery](#unique_28) [page ] 37 | Receiving Specialist | Create Inbound Delivery (VL31N) | Inbound delivery is created with the season values copied from purchase order. |
| [Display Inbound Delivery Document (Optional)](#unique_29) [page ] 38 | Receiving Specialist | Display Inbound Delivery (VL33N) | Inbound delivery is displayed with the season values copied from purchase order. |
| [Confirm Quantities for Putaway](#unique_30) [page ] 39 | Receiving Specialist | Change Inbound Delivery (VL32N) | Inbound Delivery document is updated with confirmed putaway quantities. |
| [Post Goods Receipt for Inbound Delivery](#unique_31) [page ] 40 | Warehouse Clerk | Post Goods Movement (MIGO) | Goods receipt is posted for the inbound delivery when goods arrive at the disribution centre. |
| [Create Supplier Invoice using Purchase Order](#unique_32) [page ] 42 | Accounts Payable Accountant | Create Supplier Invoice - Advanced (MIRO) | Invoice is generated. |
| [Display Supplier Invoice](#unique_33) [page ] 43 | Accounts Payable Accountant | Display Supplier Invoice - Advanced (MIR4) | Invoice and follow-on documents are displayed. |

Stock Transfer Order Document Processing

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Stock Transfer Order](#unique_34) [page ] 44 | Purchaser | Create Purchase Order - Advanced (ME21N) | Stock transfer orders are created with items that contain seasons that are entered manually or by automatic determination based on stock transfer periods. |
| [Display Stock Transfer Order (Optional)](#unique_35) [page ] 45 | Purchaser | Display Purchase Order - Advanced (ME23N) | Stock transport order is displayed with the season values. |
| [Create Replenishment Delivery for Stock Transfer Order](#unique_36) [page ] 46 | Shipping Specialist | My Purchase Orders - Due for Delivery (VL10B) | Outbound delivery document with reference to stock transport order is created. |
| [Display Outbound Delivery Document (Optional)](#unique_37) [page ] 47 | Shipping Specialist | Change Outbound Delivery (VL02N) | Outbound delivery is displayed with the season values copied from stock transfer order. |
| [Pick, Pack, and Post Goods Issue for Delivery](#unique_38) [page ] 48 | Shipping Specialist | Change Outbound Delivery (VL02N) | Material is picked then packed. Handling units are generated. Goods issue is posted for the outbound delivery. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Season Master Data

#### Create Season Master Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can create a new season with a season year, and then it can be assigned to collections and themes of that season. A new season can be created using the create option. You create a season by providing new season information.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data (Retail). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Seasons (F7465). | Manage Seasons (F7465) app initial screen is displayed. |  |
| 3 | Create Season and Season Year | Choose Create.On the Create Season pop-up, make the following entries:Year: <Season Year> (for example, 2023)Season: <Season> (for example, S001)Description: <Description> (for example, Summer)Validity: <Start Date-End Date> (DD.MM.YYYY format)Choose Create. | Season S001 for season year 2023 is created. |  |
| 4 | Create Collections for the created Season Year and Season | Select the season year and season combination.Choose Create.On the Create Collection pop-up, Year and Season fields are populated by default for the selected combination.Enter the following details:Collection: <Collection> (for example, C001)Description: <Description> (for example, Sports Women)Validity: <Start Date-End Date> (DD.MM.YYYY format)Choose Create. | Collection C001 for the seasons details is created. |  |
| 5 | Create Theme for the created Seasons Year, Season and Collection | Select the season year, season, and collection combination.Choose Create.On the Create Theme pop-up, Year, Season, and Collection fields are populated by default for the selected combination.Enter the following details:Theme: <Theme> (for example, TH01)Description: <Description> (for example, Running)Validity: <Start Date-End Date> (DD.MM.YYYY format)Choose Create.Note You can also create an additional theme (for example, TH02) as per the requirement. | Theme TH01 for the seasons details is created. |  |
| 6 | Create Language-based Description for Season, Collection, or Theme | Choose the season, collection, or theme created in steps 3, 4 and 5.On the next screen, navigate to the Description section.Choose Create.Enter Language: <Language> and Description: <Description>Choose Create. | The list of language-based descriptions created for the season, collection, or theme is displayed in the Description section.The description you entered is displayed when you switch to the target language. |  |
| 7 | Assign Products to a Season, Collection or Theme | See detailed procedure under [Assign Products to a Season, Collection or Theme using Manage Seasons Fiori App](#unique_12) [page ] 18 |  |  |
| 8 | Maintain Sales Periods for a Season, Collection or Theme | Choose the season, collection, or theme created in steps 3, 4 and 5.On the next screen, navigate to the Sales Period section.Choose Create.Enter the following mandatory details:Delivery Date From: <Current Date>Delivery Date To: <31.12.2024>Order Date From: <Current Date>Order Date To: <31.12.2024>Choose Create.Note You can also create additional sales periods as per your business requirements. | The newly created sales period is displayed in the Sales Period section.You can also create multiple sales periods relevant for different date intervals for multiple combinations of attributes (Sales Organization, Distribution Channel, Country/Region Key, Region, Customer, and Customer Group). |  |
| 9 | Maintain Purchase Periods for a Season, Collection or Theme | Choose the season, collection, or theme created in steps 3, 4 and 5.On the next screen, navigate to the Purchase Period section.Choose Create.Enter the following mandatory details:Delivery Date From: <Current Date>Delivery Date To: <31.12.2024>Order Date From: <Current Date>Order Date To: <31.12.2024>Choose Create.Note You can also create additional purchase periods as per your business requirements. | The newly created purchase period is displayed in the Purchase Period section.You can also create multiple purchase periods relevant for different date intervals for multiple combinations of attributes (Purch. Organization, Supplier, and Purchasing Group). |  |
| 10 | Maintain Stock Transfer Periods for a Season, Collection or Theme | Choose the season, collection, or theme created in steps 3, 4 and 5.On the next screen, navigate to the Stock Transfer Period section.Choose Create.Enter the following mandatory details:Delivery Date From: <Current Date>Delivery Date To: <31.12.2024>Order Date From: <Current Date>Order Date To: <31.12.2024>Choose Create.Note You can also create additional stock transfer periods as per your business requirements. | The newly created stock transfer period is displayed in the Stock Transfer Period section.You can also create multiple stock transfer periods relevant for different date intervals for multiple combinations of attributes (Supplying Plant, Sales Organization, Distribution Channel, and Customer). |  |

#### Display Season Master Data (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this process step, you can view the seasons details using the Manage Seasons (F7465) Fiori application.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data (Retail). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Seasons (F7465). | Manage Seasons (F7465) app initial screen is displayed. |  |
| 3 | Display Seasons Details | Enter the following search criteria as the seasons value that was created earlier:Season Year: 2023Season: S001Collection: C001Theme: TH01Choose Go. | Season details are displayed. |  |
| 4 | Validate Language Description | Navigate to the Language Description section and validate the language descriptions maintained for the season. | The maintained language descriptions are displayed as expected. |  |
| 5 | Validate the Products assigned to the Season, Collection, or Theme | The Product Assignment Status column indicates whether the season, collection, or theme is assigned to a product.Choose the > button next to the season, collection or theme entry to navigate to the details object page.On the object page, navigate to the Product Assignment section.The Product Assignment section displays the list of products to which the selected season, collection or theme is assigned.Choose the > button to expand the product details. The expanded section displays the assigned and unassigned variants.If the product category is Generic material (01), the assigned and unassigned variants are displayed based on the status in the Variant Deviation Status column.For No Deviation variant deviation status, the assigned variants are displayed.For Partial Deviation variant deviation status, both assigned and unassigned variants are displayed. | The product details are validated as expected.The Assigned Variants tab displays the list of products to which the season, collection, or theme is assigned.The Unassigned Variants tab displays the list of products that do not have the season, collection, or theme assigned. |  |
| 6 | Download Product Assignments (Optional) | Choose the Download Product Assignments button at the top of the screen. | The list of products to which the selected season, collection or theme is assigned can be downloaded to an excel sheet. |  |
| 7 | Validate the Sales Periods | Navigate to Sales Period section and validate the details maintained. | Maintained sales periods are validated for the season as expected. |  |
| 8 | Validate the Purchase Periods | Navigate to Purchase Period section and validate the details maintained. | Maintained purchase periods are validated for the season as expected. |  |
| 9 | Validate the Stock Transfer Periods | Navigate to Stock Transfer Period section and validate the details maintained. | Maintained stock transfer periods are validated for the season as expected. |  |

### Assign Season Details to Products

#### Assign Products to a Season, Collection or Theme using Manage Seasons Fiori App

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this process step, you can assign a season, collection, or theme to products (articles) using the Manage Seasons (F7465) Fiori app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data (Retail). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Seasons (F7465). | The Manage Seasons app initial screen is displayed. |  |
| 3 | Display Season Details | Enter the following season details that was created earlier:Season Year 2023Season S001Collection C001Theme TH02Choose Go | A list of seasons, collection and theme based on the search criteria is displayed. |  |
| 4 | Assign Products to a Season, Collection or Theme | Choose an entry to navigate to the details screen.Navigate to Product Assignment section.Choose Assign.Select a product or products to be assigned.Choose OK. | The selected products are assigned to the season, collection, or theme.The list of products assigned to the season, collection or theme is displayed in the Product Assignment section. |  |
| 5 | Assign Product Variants to a Season, Collection or Theme | Navigate to Product Assignment section.For a product with product category Generic material (01) and variant deviation status Partial Deviation, choose the > button to expand the product details. The assigned and unassigned variants are displayed.From the Unassigned Variants section, select a product variant or product variants to be assigned.Choose Assign.Choose OK.Choose Refresh.Note For a product with product category Single material (00) or generic material with variant deviation status No Deviation, assignment of product variants is not possible. | The selected product variant or product variants are assigned to the season, collection or theme.The variant deviation status is updated (if relevant).The product variant or product variants that were recently assigned is displayed in the Assigned Variants section.Note If all the unassigned product variants are assigned, then the variant deviation status is updated to No Deviation upon refresh. |  |

|  |
| --- |
| NoteTo unassign a season, collection, or theme from products (articles) using Manage Seasons (F7465) Fiori app, see [Unassign Season Details using Manage Seasons Fiori App (Optional)](#unique_40) [page ] 50.To unassign a product variant using Manage Seasons (F7465) Fiori app, see [Unassign Product Variants using Manage Seasons Application (Optional)](#unique_41) [page ] 53. |

#### Assign Season Details using Maintain Article Application

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this process step, you can assign seasons to an article (product) using the Maintain Article (MM42) application.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data (Retail). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Maintain Article (MM42). | The Maintain Article screen is displayed. |  |
| 3 | Enter Article Basic Data | Enter Material: R_1070From Views, select Basic Data 2 and choose Continue . | The Basic Data 2 view of R_1070 is displayed. |  |
| 4 | Assign Seasons Details | In the Basic Data 2 view, navigate to section Season Assignment.Press F4 in the field Season Year and choose Season Year 2023, Season S001, Collection C001 and Theme TH01, which was created earlier in section [Create Season Master Data](#unique_10) [page ] 13.Choose Save. | The selected Season Year 2023, Season S001, Collection C001 and Theme TH01 is saved. |  |

|  |
| --- |
| Note To unassign season details from articles using the Maintain Article (MM42) application, see [Unassign Season Details using Maintain Article Application (Optional)](#unique_42) [page ] 51. |

#### Assign Season Details using Manage Product Master App

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this process step, you can assign seasons to a product using Manage Product Master Data (F1602) Fiori application.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data (Retail). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Product Master Data (F1602). | The Manage Product Master Data screen is displayed. |  |
| 3 | Enter Article Basic Data | Enter the Product: R_1070 and choose Go. | The product details appear under the Products section. |  |
| 4 | Change Season Details | Choose an entry from the Products section.On the Product screen, choose Edit.Navigate to Seasons label under the section General Information.Choose Create.Choose the available Season Year 2023 and choose Season S001, Collection C001 and Theme TH01 created earlier in section [Create Season Master Data](#unique_10) [page ] 13.Choose Save. | The selected Season Year 2023, Season S001, Collection C001 and Theme TH01 are changed for the product. |  |

|  |
| --- |
| Note To unassign season details from articles using Manage Product Master Data (F1602) Fiori application, see [Unassign Season Details using Manage Product Master Data App (Optional)](#unique_43) [page ] 52. |

### Change Season Details

#### Change Season Details using Maintain Article Application (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this process step, you can assign seasons to product variants when season details change using the Maintain Article (MM42) Fiori app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data (Retail). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Maintain Article (MM42). | The Maintain Article screen is displayed. |  |
| 3 | Enter Article Basic Data | Enter the Material: R_1070001.From Views, select Basic Data 2 and choose Continue. | The Basic Data 2 view of R_1070001 is displayed. |  |
| 4 | Change Season Details | In the Basic Data 2 view, navigate to section Season Assignment.The current season details for the material (Season Year 2023, Season S001, Collection C001 and Theme TH01) are displayed.Press F4 and enter the seasons details as Season Year 2023, Season S001, Collection C001 and Theme TH02.Choose Save. | The new season detail (Season Year 2023, Season S001, Collection C001 and Theme TH02) is assigned for the product variant. |  |

#### Change Season Details using Manage Product Master App (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this process step, you can assign seasons to product variants when season details change using the Manage Product Master Data (F1602) Fiori app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data (Retail). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Product Master Data (F1602). | The Manage Product Master Data screen is displayed. |  |
| 3 | Search Product | Enter the Product as R_1070001 and choose Go. | The product details are displayed under the Products section. |  |
| 4 | Change Season Details | Choose an entry from the Products section.On the Product screen, choose Edit.Navigate to Seasons label under the section General Information.Choose Create.Choose the available Season Year 2023 and choose Season S001, Collection C001 and Theme TH02 which was created earlier in [Create Season Master Data](#unique_10) [page ] 13.Choose Save. | The selected Season Year 2023, Season S001, Collection C001 and Theme TH02 is saved. |  |

### Display Seasons Assignment

#### Display Seasons Assignment using Manage Seasons Application (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this process step, you can display the products assigned to a season, collection or theme using the Manage Seasons (F7465) Fiori app.

Procedure

Refer to procedure [Display Season Master Data (Optional)](#unique_11) [page ] 16 Step 5 for details to display the products assigned to the season.

#### Display Seasons Assignment using Display Article Application (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this process step, you can display the seasons details using the Display Article (MM43) Fiori app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data (Retail). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Display Article (MM43). | The Display Article screen is displayed. |  |
| 3 | Enter Article Basic Data | Enter Material: R_1070 or R_1070001From Views, select Basic Data 2 and choose Continue. | The Basic Data 2 view of the entered product is displayed. |  |
| 4 | Display Seasons Details | In the Basic Data 2 view, navigate to the section Season Assignment. | For generic product R_1070, the selected Season Year 2023, Season S001, Collection C001 and Theme TH01 are displayed as created earlier in [Create Season Master Data](#unique_10) [page ] 13.For product variant R_1070001, the newly included Season Year 2023, Season S001, Collection C001 and Theme TH02 are displayed as created earlier in [Create Season Master Data](#unique_10) [page ] 13. This newly added season is displayed along with the season previously assigned via the generic article (2023/S001/C001/TH01). |  |

#### Display Seasons Assignment using Manage Product Master Application (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this process step, you can display the seasons details using the Manage Product Master Data (F1602) Fiori app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data (Retail). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Product Master Data (F1602). | The Manage Product Master Data screen is displayed. |  |
| 3 | Search Product | Enter Product: R_1070 or R_1070001Choose Go. | The product details are displayed under the Products section. |  |
| 4 | Display Season Details | Choose an entry from the Products section.Navigate to Seasons label under the section General Information. | For generic product R_1070, the selected Season Year 2023, Season S001, Collection C001 and Theme TH01 are displayed as created earlier in [Create Season Master Data](#unique_10) [page ] 13.For product variant R_1070001, the newly included Season Year 2023, Season S001, Collection C001 and Theme TH02 are displayed as created earlier in [Create Season Master Data](#unique_10) [page ] 13. This newly added season is displayed along with the season previously assigned via the generic article (2023/S001/C001/TH01). |  |

### Sales Document Processing

#### Sales Order Processing

##### Create Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this process step, you can create a sales order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Create Sales Orders - VA01 (VA01). | The Create Sales Documents screen is displayed. |  |
| 3 | Enter Data | Enter the following data:Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00Choose Continue. | The Create Standard Order: Overview screen is displayed. |  |
| 4 | Enter Data | In the header section, enter:Sold-to Party: 33113007Ship-to Party: 33113007In the All Items table, enter the following details:Material: R_1070001Order Quantity: <Order quantity in piece (PC)>Plant: 3350Press ENTER.Note Seasons details are determined based on the entries maintained in the Sales Period section of Manage Seasons Fiori app.Choose Save.NoteIf you only enter the generic product, the order quantity must be filled in the variant matrix for the required variants.You can also enter your own season values even if there are no valid season values available through automatic determination or you can over-write the automatic determination values if needed. You can validate this by checking the season log under Goto > Logs > Season Determination available in the menu bar. | Sales order is saved. A success message is displayed.The below season values are determined automatically in the sales order:Season Year: 2023Season: S001Collection: C001Theme: TH01 |  |

##### Create an Outbound Delivery

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

##### Display Delivery Document using Display Outbound Delivery Application (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this process step, you can display the generated outbound delivery document using the Display Outbound Delivery (VL03N) Fiori application.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Display Outbound Delivery (VL03N). | The Display Outbound Delivery screen is displayed. |  |
| 3 | Display Delivery | In the Outbound Delivery field, enter Delivery and choose Continue.Validate season details in the Item Overview tab. | Overview of delivery document is displayed.The following seasons details are copied from the created sales order and the same are validated:Season Year: 2023Season: S001Collection: C001Theme: TH01 |  |

##### Process Picking for Outbound Delivery

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

##### Post Goods Issue for Outbound Delivery

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

##### Create Billing Document with Reference to Outbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this process step, you can generate billing documents (invoice).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Create Billing Documents (F0798) app. | The Create Billing Documents screen is displayed. |  |
| 3 | Define Billing Settings | Select Billing Settings in the bottom bar.Make the following settings:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: OFFAutomatically post billing documents: ONDisplay billing documents after creation: ONChoose delivery items to be billed and select quantities: OFFChoose OK. |  |  |
| 4 | Search for billing due list (Optional) | In the search condition, use criteria if necessary. | Sales document or documents display in the result. |  |
| 5 | Select item or items for billing | Select row or rows of SD Document created previously and choose Create Billing Documents. | The Create Billing Documents pop-up is displayed. |  |
| 6 | Maintain Billing Date | Select billing type Invoice (F2) , maintain Billing Date for example, <Current Date>and inform the sales document created previously.Choose OK. | The draft billing document or invoice with ID <TMPXXXXXX> is displayed in the Create Billing Documents screen. |  |
| 7 | Save Billing Document | On the Create Billing Documents screen, validate the details and choose Save.Note the billing document number.Note The draft version billing document or invoice with ID <TMPXXXXXX> is converted into a saved billing document with ID <XXXXXX>. | The system generates an invoice for billing.Billing document is created with season details copied from outbound delivery. |  |

##### Display Billing Document (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this process step, you can display the generated billing documents (invoice).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Display Billing Documents (VF03). | The Display Billing Documents screen displays. |  |
| 3 | Display Billing Document | Enter the Billing Document .Choose Continue.In the subsequent screen, validate whether the items have the following season details:Season Year: 2023Season: S001Collection: C001Theme: TH01 | Billing document is displayed with the season values copied from outbound delivery. |  |

### Purchase Document Processing

#### Purchase Order Processing

##### Create Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this process step, you can create a purchase order with season details.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Purchaser (Retail). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Create Purchase Order - Advanced (ME21N) app. | The Create Purchase Order - Advanced (ME21N) screen is displayed.Standard filters and buttons are displayed. |  |
| 3 | Enter Purchase Order Data | Enter the following data and press Enter:Order type: Standard PO or NB Standard POSupplier: 33213004In Header section, on the Org. Data tab:Purch. Org.:3310Purch. Group:001Company Code:3310In Item Overview section:Material:R_1070001Plant:3350Storage Location:995AQuantity:<Enter a quantity>Net Price:xxxNote Price should be determined automatically from purchasing info record.On the Confirmations tab under the Item Detail section:Conf. Control:Inbound DeliveryConfirm the values and choose Save. | A new purchase order is created.The below season values are determined automatically in the purchase order:Season Year: 2023Season: S001Collection: C001Theme: TH01Note down the order number for future use.NoteSeasons details are automatically determined based on the entries maintained in the Purchase Period section of Manage Seasons Fiori app.If you only enter the generic product, the order quantity must be filled in the variant matrix for the required variants from the Variants tab of the Item Detail section.You can also enter your own season values even if there are no valid season values available through automatic determination or you can over-write the automatic determination values if needed. You can validate this by checking the season log under Environment > Logs > Season Determination available in the menu bar. |  |

Result

The purchase order is created, and a purchase order number is generated.

##### Display Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this process step, you can display the created purchase documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Purchaser (Retail). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Display Purchase Order - Advanced (ME23N) app. | The Display Purchase Order screen is displayed. |  |
| 3 | Validate Seasons | Choose Other Purchase Order.Enter the purchase order number and choose Other Document.Validate the season details in the Retail tab of the Item Detail section. | The following season details of the purchase order is validated:Season Year: 2023Season: S001Collection: C001Theme: TH01 |  |

##### Create Inbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this process step, you manually create inbound delivery document with reference to purchase order (PO).

|  |
| --- |
| Note The supplier gives information on merchandise, quantities, and dates of delivery, which is stored in an inbound delivery document. It can be created manually as described. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Receiving Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Create Inbound Delivery (VL31N) app. | Create Inbound Delivery (VL31N) app screen is displayed. |  |
| 3 | Start Selection for Inbound Delivery Creation | On the Create Inbound Delivery (VL31N) app screen, enter the following:Supplier: 33213004Purchase Order:<your Purchase Order document number>Choose Continue.On the Inbound Delivery Create: Overview screen, validate the following season details under All Items in the Item Overview tab:Season Year: 2023Season: S001Collection: C001Theme: TH01 |  |  |
| 4 | Save Inbound Delivery Document | Choose Save. | Inbound delivery document is created. |  |

##### Display Inbound Delivery Document (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this process step, you can display the created inbound delivery document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Receiving Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Display Inbound Delivery (VL33N). | The Display Inbound Delivery screen is displayed. |  |
| 3 | Display Delivery | In the Inbound Delivery field, enter the recently created inbound delivery document number and choose Continue. | Overview of delivery document is displayed. |  |
| 4 | Validate Season Details | Validate season details in the Item Overview tab. | The following seasons details are copied from the created purchase order and the same are validated:Season Year: 2023Season: S001Collection: C001Theme: TH01 |  |

##### Confirm Quantities for Putaway

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

##### Post Goods Receipt for Inbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this process step, you post goods receipt for inbound delivery to update the inventory information in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO) app. | The Goods Receipt screen is displayed. |  |
| 3 | Enter Inbound Delivery Number | Enter the following values:Select Goods Receipt and Inbound Delivery from the dropdown and enter the following:Inbound Delivery Number: XXXGoods Movement Type: 101Press Enter. | The data within the selected inbound delivery like article, quantities, and so on are displayed. |  |
| 4 | Check and Post the Goods Receipt for Inbound Delivery | Validate the following season details in the General tab of Head.data section:Season Year: 2023Season: S001Collection: C001Theme: TH01In the Detail data section, select the Item OK checkbox.Choose Check to validate the entries.Choose Post. | The goods receipt is posted.Message Material Document <Document number> posted.is displayed. |  |
| 5 | Validate Season Details in Material Document | On the Goods Receipt screen, select Display from the Trans./Event drop down.Select the reference document as Material Document from the next drop down.Enter <Material Document Number>.Choose Execute or press Enter.Validate the following season details in the General tab of Head.data section:Season Year: 2023Season: S001Collection: C001Theme: TH01 | The material document has been validated for season details. |  |

##### Create Supplier Invoice using Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this process step, you verify invoice using purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Create Supplier Invoice - Advanced (MIRO) app. | The Create Supplier Invoice - Advanced (MIRO) screen is displayed. |  |
| 3 | Navigate to Create Supplier Invoice - Advanced Screen | In the pop-up, enter Company Code as 3310Choose Continue. | Details pertaining to the PO and its relevant seasons details are displayed. |  |
| 4 | Provide Invoice Details | Navigate to Basic Data tab and enter the values for the following fields:Invoice Date: <enter date>Reference: <enter reference>Amount: <enter amount> (Total value you had noted down while creating purchase order. You can check this value under Item Details > Conditions > Total Value )Tax Code: <enter tax code> (Tax code you have noted down in purchase order. You can check this value under Item Details > Invoice > Tax Code )Tax Amount: <enter tax amount> (Tax amount you had noted down while creating purchase order. You can check this value under Item Details > Conditions > TTX1 > Tax )Under the Details tab, select the corresponding document type in the Doc. Types field.Navigate to PO Reference tab and enter values for the following fields:Ref Document category: Purchase Order/Scheduling AgreementPurchasing Document: <enter purchase order number>Item type: Goods/service itemsPress Enter. |  |  |
| 5 | Validate Season Details | Validate the season details under PO Reference tab. | Season details are validated as expected. |  |
| 6 | Check Balance | Check the document balance amount in the Balance field. | Balance in green indicates there is no issue between the purchase order and respective invoice. |  |
| 7 | Post Supplier Invoice | Choose Post.Supplier invoice number is displayed. Note down this number for future use. | The message "Document number XXXXXXX created" is displayed.Invoice verification is completed. |  |

|  |
| --- |
| Note In this example, only one item is available in the purchase order. If there are more than one items in the purchase order and the supplier sends an invoice for all items with complete quantity, the total value and tax details can be retrieved by navigating to Purchase Order > Header > Conditions > Total Value and Purchase Order > Header > Conditions > TTX1 . |

##### Display Supplier Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this process step, you display supplier invoice and follow-on document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Display Supplier Invoice - Advanced (MIR4) app. | The Display Invoice Document screen is displayed. |  |
| 3 | Provide Invoice Details | Enter the following values:Invoice Document No.:< Enter invoice document number >Fiscal Year:<Enter year>Choose Display Document. | Invoice details are displayed. |  |
| 4 | Validate Season Details | Validate season details under PO Reference tab. | Season details are validated as expected. |  |
| 5 | Check Follow- On Document | Select Follow-On Documents. | You can view the accounting document. |  |

#### Stock Transfer Order Processing

##### Create Stock Transfer Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this process step, you can create a stock transfer order (STO) with season details.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser (Retail). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Create Purchase Order (ME21N) app. | Create Purchase Order (ME21N) app screen is displayed. |  |
| 3 | Enter Stock Transfer Order Data | Enter the following data, then press Enter:Order Type: StockTranspOrderDel or UD StockTranspOrderDelSupplying Plant: 3350In the Org. Data tab of the Header section:Company Code: 3310Purchasing Org.: 3310Purchasing Group: 001In the Item Overview section:Material: R_1070001Plant: 3340Storage Location: 994APO Quantity: xConfirm the values and choose Save. | A new stock transfer order is created.The below season values are determined automatically in the purchase order:Season Year: 2023Season: S001Collection: C001Theme: TH01Note down the order number for future use.NoteSeasons details are automatically determined based on the entries maintained in the Stock Transfer Period section of Manage Seasons Fiori app.If you only enter the generic product, the order quantity must be filled in the variant matrix for the required variants from the Variants tab of the Item Detail section.You can also enter your own season values even if there are no valid season values available through automatic determination or you can over-write the automatic determination values if needed. You can validate this by checking the season log under Environment > Logs > Season Determination available in the menu bar. |  |

Result

The stock transport order is created, and a stock transport order number is generated.

##### Display Stock Transfer Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this process step, you can display the created stock transport order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Purchaser (Retail). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Display Purchase Order - Advanced (ME23N). | The Display Purchase Order screen is displayed. |  |
| 3 | Validate Seasons | Choose Other Purchase Order.Enter the stock transport order number and choose Other Document.Validate the season details in the Retail tab of the Item Detail section. | The following season details of the stock transport order is validated:Season Year: 2023Season: S001Collection: C001Theme: TH01 |  |

##### Create Replenishment Delivery for Stock Transfer Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this process step, you manually create replenishment or outbound delivery with reference to stock transfer order (STO).

|  |
| --- |
| Note You can create outbound deliveries by scheduling background job which is in close alignment with the distribution center and their work shifts there. However, to test this scope outbound deliveries are created manually. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open My Purchase Orders - Due for Delivery (VL10B) app. | Purchase Orders, Fast Display screen is displayed. |  |
| 3 | Start Selection for Outbound Delivery Creation | On the Purchase Orders, Fast Display screen, enter the following details:Remove Deliv. Creation Date (both from and to dates)Shipping point: 3350Go to Purchase Orders tab view and enter Purchasing Document: STO Document Number created earlier.Choose Run. | A list of purchasing documents for the selected shipping point is displayed in the Activities Due for Shipping "Purchase Orders, Fast Display" screen. |  |
| 4 | Select Purchasing Document for Outbound Delivery Creation | Select your purchasing documents and choose Background. | Outbound delivery document is created. |  |
| 5 | View the Created Outbound Delivery Document Number | Choose Log for delivery creation.On the Delivery Creation Log screen, choose Documents. | Outbound delivery document number is displayed. |  |

##### Display Outbound Delivery Document (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this process step, you can display the created outbound delivery document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Display Outbound Delivery (VL03N). | The Display Outbound Delivery screen is displayed. |  |
| 3 | Display Delivery | In the Outbound Delivery field, enter the recently created outbound delivery document number and choose Continue. | Overview of delivery document is displayed. |  |
| 4 | Validate Season Details | Validate season details in the Item Overview tab. | The following seasons details are copied from the created stock transfer order and the same are validated:Season Year: 2023Season: S001Collection: C001Theme:TH01 |  |

##### Pick, Pack, and Post Goods Issue for Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this process step, you pick and pack materials to create handling units and post the goods to remove them from the inventory management system of the distribution center. Match the receipt of goods in the store to the outbound delivery you created earlier.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Change Outbound Delivery (VL02N) app. | The Change Outbound Delivery screen is displayed. |  |
| 3 | Open Outbound Delivery Document | In the Outbound Delivery field, enter the recently created outbound delivery document number and choose Continue. | The selected outbound delivery details are displayed. |  |
| 4 | Specify Picked Quantity | Navigate to Picking tab and enter Picked Qty: <Enter quantity equal to delivery quantity>. | Picked quantity is updated. |  |
| 5 | Save the Outbound Delivery Document | Choose Save. | Outbound delivery document is saved. |  |
| 6 | Post Goods Issue | Navigate back to the Change Outbound Delivery screen.Enter <your outbound delivery document number>.Choose Post Goods Issue. | Goods issue is successful. Inventory stock is reduced from the supplying plant. |  |

## Appendix

### Optional Scenarios

#### Unassign Seasons

It may be necessary to unassign season details from articles if the season is no longer valid inside the article or if you have assigned an incorrect season to the article.

##### Unassign Season Details using Manage Seasons Fiori App (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this process step, you can unassign a season, collection, or theme to products (articles) using the Manage Seasons (F7465) Fiori app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data (Retail). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Seasons (F7465). | The Manage Seasons app initial screen is displayed. |  |
| 3 | Display Season Details | Enter the following season details that was created earlier:Season Year 2023Season S001Collection C001Theme TH02Choose Go | A list of seasons, collection and theme based on the search criteria is displayed. |  |
| 4 | Assign Season, Collection or Theme to Products | Choose an entry to navigate to the details screen.Navigate to Product Assignment section.Select a product or products to be assigned.Choose Unassign.Choose OK. | The season, collection or theme is unassigned from the selected product or products.The list of products from which the season, collection or theme is unassigned are deleted from the Product Assignment section. |  |

##### Unassign Season Details using Maintain Article Application (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this process step, you can unassign season details from articles using the Maintain Article (MM42) application.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data (Retail). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Maintain Article (MM42). | The Maintain Article screen is displayed. |  |
| 3 | Enter Article Basic Data | Enter Material: R_1070From Views, select Basic Data 2 and choose Continue . | The Basic Data 2 view of R_1070 is displayed. |  |
| 4 | Unassign Season Details | In the Basic Data 2 view, navigate to section Season Assignment.Select an entry or entries and choose the Delete Row icon.Choose Save. | The selected season entry is unassigned. |  |

##### Unassign Season Details using Manage Product Master Data App (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this process step, you can unassign season details from articles (products) using the Manage Product Master Data (F1602) Fiori application.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data (Retail). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Product Master Data (F1602). | The Manage Product Master Data screen is displayed. |  |
| 3 | Enter Article Basic Data | Enter the Product: R_1070 and choose Go. | The product details appear under the Products section. |  |
| 4 | Change Season Details | Choose an entry from the Products section.On the Product screen, choose Edit.Navigate to Seasons label under the section General Information.Select an evtry.Choose Delete.On the prompt screen, choose Delete.Choose Save. | The selected season entry is unassigned for the product. |  |

##### Unassign Product Variants using Manage Seasons Application (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this process step, you can unassign product variants from a season, collection, or theme using the Manage Seasons (F7465) Fiori app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data (Retail). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Seasons (F7465). | The Manage Seasons app initial screen is displayed. |  |
| 3 | Display Season Details | Enter the following season details that was created earlier:Season Year 2023Season S001Collection C001Theme TH02Choose Go | A list of seasons, collection and theme based on the search criteria is displayed. |  |
| 4 | Unassign Product Variants from a Season, Collection or Theme | Choose an entry to navigate to the details screen.Navigate to Product Assignment section.From the Assigned Variants section, select a product or products (if applicable) to be unassigned.Choose Unassign.Choose OK.Choose Refresh.Note Unassign action is not applicable for a product with product category Single material (00). | The selected product variant or variants are unassigned from the season, collection or theme.The variant deviation status is updated (if relevant).The product variant or product variants that were recently unassigned are displayed in the Unassigned Variants section. |  |

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
> Flagged while digesting this document, not verified: Test data sets sales, purchase and stock transfer periods from <Current Date> to a fixed 31.12.2024, while the script is dated 19-06-26 and (c) 2026; following the steps literally would give a period ending before the current date.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[15-retail-operations/product-taxonomies-for-retail-5fj-ae-test-script-1079]]
- related-to :: [[15-retail-operations/products-for-retail-3i1-ae-test-script-sap-s-4hana-cloud-public-editio]]
- related-to :: [[15-retail-operations/test-script-characteristic-value-conversion-for-retail-7dl-ae-sap-s-4h]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6DI_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 91,903 chars in the whole document
