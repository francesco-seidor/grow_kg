---
id: 15-retail-operations/test-script-in-store-merchandise-management-3hq-ae-sap-s-4hana-cloud-p
title: "Test Script: In-Store Merchandise Management (3HQ_AE), SAP S/4HANA Cloud Public Edition (3HQ_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 3HQ_AE: store associates look up retail products and print labels; prerequisites and steps."
cluster: 15-retail-operations
tags: [kb/retail-operations, topic/my-store-management]
aliases: [3HQ_S4CLD2608_BPD_EN_AE]
keywords: [My Store Management, in-store merchandise management, look up retail products, print labels, product variants, delivery information, print queue, test procedures, store assignment, initial stock]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3HQ_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-936
topic: 15-retail-operations/my-store-management
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: In-Store Merchandise Management (3HQ_AE), SAP S/4HANA Cloud Public Edition (3HQ_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3HQ_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **My Store Management** in Retail Operations. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | In-Store Merchandise Management (3HQ_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232852567)

[2 Prerequisites 4](#_Toc232852568)

[2.1 System Access 4](#_Toc232852569)

[2.2 Roles 4](#_Toc232852570)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232852571)

[2.4 Additional Manual Configuration 6](#_Toc232852572)

[2.5 Business Conditions 6](#_Toc232852573)

[2.6 Preliminary Steps 6](#_Toc232852574)

[2.6.1 Assign Store Associate (User) to a Store (Optional) 6](#_Toc232852575)

[2.6.2 Set Initial Stock for Material 7](#_Toc232852576)

[2.6.3 Create Stock Transfer Order 8](#_Toc232852577)

[2.6.4 Create Delivery for Stock Transfer Order 9](#_Toc232852578)

[3 Overview Table 11](#_Toc232852579)

[4 Test Procedures 12](#_Toc232852580)

[4.1 Look Up Retail Products 12](#_Toc232852581)

[4.1.1 Look Up General Product Information 12](#_Toc232852582)

[4.1.2 Look Up Product Variants 13](#_Toc232852583)

[4.1.3 Look Up Delivery Information 14](#_Toc232852584)

[4.2 Print Labels 16](#_Toc232852585)

[4.2.1 Start Print Label app and Scan or Search a Product 16](#_Toc232852586)

[4.2.2 Determine the Number of Labels to be Printed 17](#_Toc232852587)

[4.2.3 Select Label Type 17](#_Toc232852588)

[4.2.4 Select Printer and Print the Label 18](#_Toc232852589)

[4.2.5 Maintain Print Queue 19](#_Toc232852590)

## Purpose

Overview

For a retail associate, having all necessary article information at their fingertips using an app is essential for both customer-facing activities and efficient store operations. The Look Up Retail Product app combines crucial data from a variety of sources. This includes article descriptions, units of measurement, sales pricing, available-to-promise stock information, procurement lead times, real-time stock information considering unprocessed POS sales, procurement lead times, and upcoming planned goods receipts. You can identify the article through bar-code scanning of the Global Trade Identification Number (GTIN), using the search function, or through cross-navigation from another application.

The Print Labels app enables retail associates to search or scan the required product and print the product labels. Additionally, you can print labels for lists of articles. Correct labels support on-shelf availability and proper labeling of prices, which is a key requirement for brick-and-mortar stores.

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
| Warehouse Clerk (Retail) | SAP_BR_WAREHOUSE_CLERK_RFM | Warehouse Clerk (Retail) | SAP_BR_WAREHOUSE_CLERK_RFM |  |
| Purchaser (Retail) | SAP_BR_PURCHASER_RFM | Retail Purchasing / Retail Sourcing and Contracting | SAP_BR_PURCHASER_RFM |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Retail Store Associate | SAP_BR_RFM_STORE_ASSOCIATE | Retail Store Associate | SAP_BR_RFM_STORE_ASSOCIATE |  |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

Use your own master data or the following sample data to go through the test procedure.

|  |
| --- |
| Note In the following table, sample values for master data are provided for the country/region US. You can either use the country-dependent sample master data or create and use your own master data while executing the test procedure. |

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Store (Site) | 3340 | Store 3340 AE |  |
| Store (Site) | 3341 | Store 3341 AE |  |
| Store (Site) | 3342 | Store 3342 AE |  |
| Store (Site) | 3343 | Store 3343 AE |  |
| Store (Site) | 3344 | Store 3344 AE |  |
| Distribution Center | 3350 | DC 3350 AE |  |
| Single Article (Material or Product) | R_4004 | Apple, Golden Delicious Cat. I 1kg pack | Article with multiple units of measure (UoM) and multiple GTIN. |
| Single Article (Material or Product) | R_1006 | My Best Frozen Strawberries | Article having inbound or outbound deliveries, the deliveries with current, future or previous validity periods. |
| Generic Article (Material or Product) | R_1003 | Chocolate | Article having variants. |
| Storage Location | 994A | St.Loc.Neg.Stock |  |
| Company Code | 3310 | Company Code 3310 |  |
| Purchasing Group | 001 | Group 001 |  |
| Purchasing Organization | 3310 | Purchase Organization 3310 |  |
| Shipping Point | 3350 | SP DC 3350 |  |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/dae79ca60887046e13a3f2e43aa80fa8)

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 5FV - Outbound Logistics for Distribution Centers | To look for deliveries, run through the Outbound Logistics for Distribution Centers test script process to create stock transfer orders or outbound deliveries. |

### Preliminary Steps

#### Assign Store Associate (User) to a Store (Optional)

Use

To filter the data provided in the SAP Fiori in-store merchandising apps to the relevant store, the users of store associates need to be assigned to a certain store (site). The store assignment can be changed at any point in time in case a store associate is helping in another store. Perform this process step if store associate (user) is not assigned to a store yet or store assignment needs to be changed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Retail Store Associate. |  |  |
| 2 | Access the App | Open the app My Store Assignment (F4334). | The My Store Assignment screen is displayed. |  |
| 3 | Search Your Store | Enter Store ID, Name, Postal Code or City of the store, for example, enter 3340 and select Search. | The store details are displayed. |  |
| 4 | Select Store | Select (for example 3340). |  |  |
| 5 | Assign Store | When selecting a store, the Assign Me above the store list is activated. Press Assign Me to save the assignment. | A success massege You were assigned to store <store ID > is displayed . |  |

Result

With the assignment to a store, the data shown in the different In-store Merchandising Management apps is filtered to the assigned store, hence the user only has access to relevant information increasing the efficiency of the day-to-day work.

#### Set Initial Stock for Material

Use

To execute this scope item, the materials must be available in stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk (Retail). |  |  |
| 2 | Access the App | Open Post Goods Movement (MIGO).It only displays if it is your last transaction. So, the action for the user should be to select Reference Document for MIGO > Other . |  |  |
| 3 | Input Movement Type | Make the following entry and choose Enter:Executable Action in Transaction MIGO: Goods ReceiptReference Document for MIGO Transaction: Other |  |  |
| 4 | Enter Material | On the Goods Receipt Other Screen: Material tab, make the following entry and choose Enter:Material: R_4004 |  |  |
| 5 | Enter Quantity Data | On the Goods Receipt Other screen: Quantity tab, make the following entry and choose Enter:Qty in Unit of Entry: <Qty in UOM>Unit of Entry: <PC> |  |  |
| 6 | Input on the Goods Receipt Other screen: Where tab | On the Goods Receipt Other screen: Where tab, make the following entries and choose Enter:Movement Type: 501Receipt per initial entry of stock balances into unrestricted usePlant: for example 3340Storage Location: for example 994A |  |  |
| 7 | Save Your Entries | Choose Post. | Material document <document number> posted message is displayed. |  |

|  |
| --- |
| Note For above procedure, if you use a material (article) of type "Generic article", enter quantity in the variant matrix grid which appears on expanding Tree display for the material after entering the required details. Generic articles are logical entities which are not entitled for physical stocks creation.For various types of articles you can use in this scope item, refer to the list of retail articles mentioned in [Master Data, Organizational Data, and Other Data](#unique_5) [page ] 5. |

Result

Stock is created for the materials.

#### Create Stock Transfer Order

Use

To execute this scope item, stock transfer order (STO) must be available so that information of the same can be looked up using the Look Up Retail Products (F0431) app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser (Retail). |  |  |
| 2 | Access the App | Open Create Purchase Order - Advanced (ME21N) app. |  |  |
| 3 | Enter Order Document Type and other data | Enter the following data, then choose Enter:Order Type: StockTranspOrderDel or UD StockTranspOrderDelSupplying Plant: for example 3350On the Header / Org. Data tab:Company Code: for example 3310Purchasing Group:: 001Purchasing Org:: for example 3310In Item Overview section:Material: R_1006Plant: for example 3342Storage Location: 994AQuantity: xNet Price: x | All data are entered, the item detail screen is displayed. |  |
| 6 | Save Stock Transfer Order | Choose Save and when the stock transfer order number is displayed, write it down for further use. | A new stock transfer order is created. Order number is displayed. |  |

#### Create Delivery for Stock Transfer Order

Use

To execute this scope item, outbound or replenishment delivery must be available so that information of the same can be looked up using the Look Up Retail Products (F0431) app. This delivery is created with reference to stock transfer order (STO).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access App | Open My Purchase Orders - Due for Delivery (VL10B) app. |  |  |
| 3 | Start Selection for Outbound Delivery Creation | On the entry screen of the Purchase Orders, Fast Display app, make the following entries and select Execute:Shipping point: for example 3350. | A list of purchasing documents for the selected shipping point is displayed. |  |
| 4 | Select Purchasing Document for Outbound Delivery creation | Mark your purchasing documents and select Background. | Outbound delivery document is created. |  |
| 5 | View the Created Outbound Delivery Document number | Select Log for delivery creation, then choose Documents on the Delivery Creation Log screen. | Outbound delivery document number is displayed. |  |

## Overview Table

This scope item consists of several process steps that are listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Look Up Retail Products (F0431)

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Look Up General Product Information](#unique_13) [page ] 12 | Retail Store Associate | Look Up Retail Products (F0431) Look Up Retail Products (F0431) | The store associate can view the stock level of a product as well as general information to inform the consumer. |
| [Look Up Product Variants](#unique_14) [page ] 13 | Retail Store Associate | Look Up Retail Products (F0431) Look Up Retail Products (F0431) | The store associate can check if a product is available in other variants. |
| [Look Up Delivery Information](#unique_15) [page ] 14 | Retail Store Associate | Look Up Retail Products (F0431) Look Up Retail Products (F0431) | The store associate can check when a product out of stock – will be delivered again. |

Print Labels (F1563)

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Start Print Label app and Scan or Search a Product](#unique_16) [page ] 16 | Retail Store Associate | Print Labels (F1563) | The Print Labels screen is displayed. If the product is available in the store assigned to the retail store associate. |
| [Determine the Number of Labels to be Printed](#unique_17) [page ] 17 | Retail Store Associate | Print Labels (F1563) | The count of labels to be printed is displayed and can change if required. |
| [Select Label Type](#unique_18) [page ] 17 | Retail Store Associate | Print Labels (F1563) | Required Label type is selected |
| [Select Printer and Print the Label](#unique_19) [page ] 18 | Retail Store Associate | Print Labels (F1563) | Printer is selected and the store associate able to print the labels |
| [Maintain Print Queue](#unique_20) [page ] 19 | Administrator | Maintain Print Queues (F1260) | Printed documents available in the Maintain print queue |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Look Up Retail Products

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

#### Look Up Product Variants

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When store associates approached by consumers, the store associates can use the Look Up Retail Products (F0431) app to get the information of any variant existing for a certain product. This facilitates store associates to provide a better service for their customers without performing a physical search in the store.

Procedure

In case the Look Up Retail Products (F0431) app is open, and you have selected a product earlier, the steps 1 - 2 need not be executed again.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Retail Store Associate. |  |  |
| 2 | Access App | Open the Look Up Retail Products (F0431) app. |  |  |
| 3a | Scan a Product (on Mobile) | Select the Scan to scan the barcode using the camera on the device to view the details of the associated product.Note Only possible on mobile device with SAP Custom Fiori Client. | Product details on the Information tab are displayed. |  |
| 3b | Search a product (on a web browser) | Enter R_1003 or a search term, for instance, name of the product, product GTIN, etc. in the product search and select the product from the search result list. | Product details on the Information tab are displayed. |  |
| 4 | Display Variants | Select Variants. | The variants of the selected product are shown including the available inventory at the selected store. |  |
| 5 | Display Additional Details | Select the <Description> of one of the variants. | The Look Up Retail Products (F0431) screen is reloaded, and the product variant clicked is now selected. The product information is displayed. |  |

#### Look Up Delivery Information

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When store associates approached by consumers, store associates use the Look Up Retail Products (F0431) app to get the information, if a certain product is still available in the store. Otherwise, the store associates can look up when the product will be available again in the store. They can inform and reserve it so that customer can pick up the product as soon as it’s available in the store again.

Procedure

In case the app is still open, and a product is still selected from another test, the steps 1 to 2 do not have to be executed again.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Retail Store Associate. |  |  |
| 2 | Access App | Open the Look Up Retail Products (F0431) app. | The product search page is displayed. |  |
| 3a | Scan a product (on mobile) | Select the Scan button and scan the barcode using the camera on the device to view the details of the associated product.Note Only possible on mobile device with SAP/ Custom Fiori Client. | Product details on the Information tab are displayed. |  |
| 3b | Search a product (on a web browser) | Enter R_1006 or a search term, for instance, name of the product, product GTIN, etc. in the product search and select the product from the search result list. | Product details on the Information tab are displayed. |  |
| 4 | View Deliveries | Select on the Deliveries tab.Note If no delivery related information exist in the Deliveries tab, then create stock transfer order and outbound delivery documents as described in chapters [Create Stock Transfer Order](#unique_10) [page ] 8 and [Create Delivery for Stock Transfer Order](#unique_11) [page ] 9 of this document. | The deliveries containing the selected product are displayed.Current display the deliveries expected today.Future display the deliveries expected in the future starting tomorrow until the fixed number of days up to which the shipment arrival information is expected. Refer to the Configuration Activities in Set-Up Instructions.Previous shows the deliveries in the past until the fixed number of days up to which past shipment record is supposed to exist. Refer to the Configuration Activities in Set-Up Instructions. |  |

### Print Labels

#### Start Print Label app and Scan or Search a Product

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Print Labels (F1563) enables the retail store associates to print the price label for the products for the assigned stores. This process shows you how to scan or search for a product for the user and to see information such as product name and sales price.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to Fiori launchpad as a Retail Store Associate. |  |  |
| 2 | Access the App | Open the Print Labels (F1563) app. |  |  |
| 3 | Enter Data | Following are the different ways in which a product can be searched using this app:Enter the Product ID R_1006 in the Search at the bottom left corner of the screen.Select the Scan button and scan the barcode using the camera on the device to view the details of the associated product. and select the product from the search result list. | The master list should return a line item of the product searched. |  |

#### Determine the Number of Labels to be Printed

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to select the number of labels to be printed for the selected product.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Logon | Logon to Fiori launchpad as a Retail Store Associate. |  |  |
| 2 | Access the App | Start Print Labels (F1563) app. | The Print Labels screen is displayed |  |
| 3 | Enter the data | Enter the Enter the Product ID R_1006 in the Search at the bottom left corner of the screen. | The master list should return a line item of the product searched. |  |
| 4 | Check the details of the product and Change the count | Navigate to the product details selected for printing, in the count field change the details if required | The count is changed if required |  |

#### Select Label Type

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process shows you how to select the required label type you want to print for the product.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Logon | Logon to Fiori launchpad as a Retail Store Associate. |  |  |
| 2 | Access the App | Start Print Labels (F1563) app. |  |  |
| 3 | Enter the details | Enter the Product ID R_1006 in the Search at the bottom left corner of the screen. | The master list return a line item of the product searched |  |
| 4 | Select the Label Type | Navigate to the label type drop down and select the required label typeFor example, sample Label for Mobile PrintersSample Label for A4 Printers. | The required label type is selected |  |

#### Select Printer and Print the Label

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step shows you how to select the printer and to print the label of the selected product.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Logon | Logon to Fiori launchpad as a Retail Store Associate. |  |  |
| 2 | Access the app | Start Print Labels (F1563) app. |  |  |
| 3 | Enter the details | Enter the Product ID R_1006 in the Search at the bottom left corner of the screen. | The master list return a line item of the product searched |  |
| 4 | Select the Label type | Navigate to the Label Type drop down and select the required label type.For example, sample Label for Mobile PrintersSample Label for A4 Printers | Required label type should be selected. |  |
| 5 | Submit the product for Printing | Select the Print option available in the right bottom of the screen: Print labels, the Printer selection pop up screen is displayed – select the required printer Printer for (for example 3340) Plant and select OK. | A message is displayed on the screen |  |

#### Maintain Print Queue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step shows you how to print the document details you submitted for the print using SAP Cloud Print Manager.

|  |
| --- |
| Note If SAP Cloud Print Manager is not yet installed, refer to Set Up Instructions. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Logon | Logon to Fiori launchpad as an Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control |  |  |
| 2 | Access the App | Start the Maintain Print Queues (F1260) app. | Maintain Print Queues (F1260) app is displayed. |  |
| 3 | (Optional) Validate the Document Sent for Print | Select the printer selected in Print Labels (F1563) app and validate the document sent for printing.Note In case owner of the printer is not avaliable and other associate want to print the same to do so follow the step below,Select the respective printer check box from the list.Choose change .Edit print queue pop will be generated.Select User name form the Print User drop down list.Choose change button | Printer details and the Label details are displayed. |  |
| 4 | Print the Document in the local Printer | Launch the Cloud Print manager from the local system where you install using setup instruction guide and to print the label details for the product, follow the steps below:Launch the Cloud Print MangerUnder the Print Queue , select the printer details assigned in the Print Labels (F1563) app.Select and right click on the required Queue – Select output option.Note If you want to validate the documents select Save to File and save the document in the required folder of the local system and validate the label documents before printing.Select Send to Printer and select the printer name from the Printer Dropdown list.Select OK. | Label printed successfully with the product details. |  |

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
- related-to :: [[15-retail-operations/test-script-my-store-management-5fw-ae-sap-s-4hana-cloud-public-editio]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3HQ_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 34,340 chars in the whole document
