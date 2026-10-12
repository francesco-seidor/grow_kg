---
id: 15-retail-operations/test-script-in-store-purchase-order-management-5fy-ae-sap-s-4hana-clou
title: "Test Script: In-Store Purchase Order Management (5FY_AE) - SAP S/4HANA Cloud Public Edition (5FY_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 5FY_AE: store order proposals plus standard, customer-order-based and trusted receiving."
cluster: 15-retail-operations
tags: [kb/retail-operations, topic/store-ordering-from-dc]
aliases: [5FY_S4CLD2608_BPD_EN_AE]
keywords: [Store Ordering from Distribution Centers, in-store purchase order management, order proposals, standard receiving, trusted receiving, customer order-based receiving, inbound delivery, handling units, purchase requisition, purchase order]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5FY_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1093
topic: 15-retail-operations/store-ordering-from-dc
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: In-Store Purchase Order Management (5FY_AE) - SAP S/4HANA Cloud Public Edition (5FY_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5FY_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Store Ordering from Distribution Centers** in Retail Operations. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | In-Store Purchase Order Management (5FY_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232856959)

[2 Prerequisites 4](#_Toc232856960)

[2.1 System Access 4](#_Toc232856961)

[2.2 Roles 4](#_Toc232856962)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232856963)

[2.4 Preliminary Steps 5](#_Toc232856964)

[2.4.1 Assign Store Associate to a Store 5](#_Toc232856965)

[2.4.2 Purchase Requisition 7](#_Toc232856966)

[2.4.2.1 Purchase Requisition for Standard PO 7](#_Toc232856967)

[2.4.2.2 Purchase Requisition for Trusted Purchase Order 7](#_Toc232856968)

[2.4.3 Purchase Order 8](#_Toc232856969)

[2.4.3.1 Create Purchase Order for Standard Receiving 8](#_Toc232856970)

[2.4.3.2 Create Purchase Order for Trusted Receiving 9](#_Toc232856971)

[2.4.4 Create Inbound Delivery 10](#_Toc232856972)

[2.4.4.1 Create Inbound Delivery for Standard Receiving 10](#_Toc232856973)

[2.4.4.2 Create Inbound Delivery for Trusted Receiving 11](#_Toc232856974)

[2.4.5 Create Customer Order for Receive Products 12](#_Toc232856975)

[2.4.5.1 Create Customer Order 12](#_Toc232856976)

[2.4.5.2 Create Purchase Order from Purchase Requisition 12](#_Toc232856977)

[2.4.5.3 Convert Purchase Requisition to Purchase Order 13](#_Toc232856978)

[2.4.5.4 Create Inbound Delivery (Optional) 14](#_Toc232856979)

[2.4.5.5 Create Handling Unit (Optional) 15](#_Toc232856980)

[3 Overview Table 16](#_Toc232856981)

[4 Test Procedures 17](#_Toc232856982)

[4.1 Review Order Proposals 17](#_Toc232856983)

[4.2 Receive Product - Standard 18](#_Toc232856984)

[4.2.1 Receive Product (Standard) 18](#_Toc232856985)

[4.2.2 Receive Products for Customer Account Assigned Purchase Order 20](#_Toc232856986)

[4.2.2.1 Receive Product for Customer Order-Based Purchase Order 20](#_Toc232856987)

[4.2.2.2 Receive Product for Customer Order-Based Purchase Order and Inbound Delivery Without Handling Unit 21](#_Toc232856988)

[4.2.2.3 Receive Product for Customer Order-Based Purchase Order and Inbound Delivery with Handling Unit 22](#_Toc232856989)

[4.2.3 Look Up Retail Products (Optional) 24](#_Toc232856990)

[4.3 Receive Product - Trusted 25](#_Toc232856991)

[4.3.1 Look Up Retail Products (Optional) 26](#_Toc232856992)

[4.4 Schedule Clean Up of Operational Data for Receive Products (Optional) 27](#_Toc232856993)

[5 Appendix 29](#_Toc232856994)

[5.1 Process Integration 29](#_Toc232856995)

[5.1.1 Preceding Processes 29](#_Toc232856996)

[5.1.2 Succeeding Processes 29](#_Toc232856997)

## Purpose

Overview

Having the optimal quantity of merchandise on the sales floor is of major importance. Out-of-stock situations reduce customer satisfaction and decrease revenue, but overstock increases capital binding.

Order Products app: Typically, stores are replenished centrally. Store personnel can be involved in the process by reviewing and adjusting the order proposal. In addition, ad hoc manual ordering is available, allowing mitigation of exceptions. Decision support for both scenarios through information such sales history, current stock, and open order quantity is provided to help store personnel to decide on the right order quantity. Articles are ordered from the distribution center or from an external supplier. The purchase requisition is generated once the order proposal from the app is submitted.

Receive Products app: Once the articles arrive at the store, a store associate triggers receiving to update the inventory (from an inventory and finance perspective). The associate can do trusted receiving (no item level scanning, posting everything at once) or detailed receiving (item level scanning is required). If necessary, labels can be printed ad hoc.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

|  |
| --- |
| Note In the retail industry, specific terms differ from the standard terms used in other lines of business. Therefore, SAP solutions which provide business processes across multiple lines of businesses may use terms for the corresponding business objects, transactions, and user interfaces that deviate from the retail terminology. For integration and reuse reasons, the SAP S/4HANA Cloud Public Edition, retail, fashion, and vertical business business may thus include different terms that refer to the same concept. SAP intends to harmonize the terminology in the future.The following terms are used synonymously in this document:Table 1:Standard Terms in Lines of BusinessSAP S/4HANA Cloud Public Edition, retail, fashion, and vertical business businessMaterial, productArticleMaterial group, product groupMerchandise categoryPlant, locationSite (as superordinate term) - store and distribution center (DC) |

## Prerequisites

This chapter summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, and other test data.

|  |
| --- |
| Caution Testing in a 3-System LandscapeIn a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version (see the following [link](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/TestScripts/5FY_S4CLD2602_BPD_EN_DE.docx)). |

### System Access

|  |  |
| --- | --- |
|  | Details |
| System | Accessible through SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) |
| --- | --- | --- | --- |
| Retail Store Associate | SAP_BR_RFM_STORE_ASSOCIATE | Store Operations | SAP_BR_RFM_STORE_ASSOCIATE |
| Purchaser (Retail) | SAP_BR_PURCHASER_RFM | Retail Purchasing / Retail Sourcing and Contracting | SAP_RFM_SPT_PURCHASING_PC / SAP_RFM_SPT_SOURCING_PC |
| Receiving Specialist | SAP_BR_RECEIVING_SPECIALIST | Receiving | SAP_BR_RECEIVING_SPECIALIST |
| Administrator (Retail) | SAP_BR_ADMINISTRATOR_RFM | Administration - Retail | SAP_BR_ADMINISTRATOR_RFM |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

Use your own master data or the following sample data to go through the test procedure.

|  |
| --- |
| Note In the following table, sample values for master data are provided for the country/region US. You can either use the country-dependent sample master data or create and use your own master data while executing the test procedure. |

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Store (Site) | 3340 | Store 3340 AE |  |
| Product | R_1037 | White bread large, organic | Generic article “Chocolate” added |
| Product | R_1003 | Chocolate |  |
| Supplier | 33213002 | Retail Food Supplier AE |  |
| Purchasing Organization | 3310 | Purch. Org. 3310 |  |
| Purchasing Group | 001 | Group 001 |  |

### Preliminary Steps

#### Assign Store Associate to a Store

Use

To filter the data provided in the SAP Fiori store merchandising apps to the relevant store, the users of store associates need to be assigned to a certain store (site). The store assignment can be changed at any point in time in case a store associate is helping in another store or if this is required for testing purposes.

Procedure

| Step # | Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Retail Store Associate. |  |  |
| 2 | Open my store assignment app | Open the My Store Assignment (F4334) app.Note If you are already assigned to store (for example 3340), you can skip this procedure. | A list of stores is displayed. The store, to which the user is assigned to, is shown on the header section of the app. |  |
| 3 | Search store | Search for the following entries:Store: for example 3340 and select GoStore Name:. <Store Name> and select GoPostal Code: <Postal Code>City: <City>Select Go. |  |  |
| 4 | Select store | Select ON radio button to select the store (for example 3340) you want to assign the user to. | Store is selected. |  |
| 5. | Save assignment | After selecting a store, the Assign Me above the store list is activated. Select Assign Me to assign the store to the respective user.. | The successful message popup “You were assigned to store 3340.” is momentarily shown. The Assigned Store above the list is updated accordingly. |  |
| 6 | Exit screen | Choose Back. |  |  |

Result

The data shown in the different SAP Fiori store merchandising apps is filtered to the assigned store, hence the user only has the access to the relevant information which increases the efficiency of the day-to-day work.

#### Purchase Requisition

##### Purchase Requisition for Standard PO

Use

Create a purchase requisition for standard purchase order to fulfil the checks and changes which is described in the further step of this test script.

Procedure

| Step # | Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser (Retail) |  |  |
| 2 | Open create purchase requisition – advanced app | Open the Create Purchase Requisition (ME51N) app. | The Create Purchase Requisition screen is displayed. |  |
| 3 | Enter the details | Enter the following data:Purchase Requisition type : NBItem Overview : <description>Material : R_1037Plant : for example 3340Quantity: 10 PC | Key values of dropdown list are visible. |  |
| 4 | Save the document | Select SaveMake a note of purchase requisition number. | A message indicating Purchase requisition created is displayed. |  |

##### Purchase Requisition for Trusted Purchase Order

Use

Trusted purchase order is from a supplier for whom you do not need to check the quantity and quality in the shipment. Goods receipt can be posted directly without entering the details.

Create a purchase requisition for trusted purchase order to fulfil the checks and changes which is described in the further step of this test script.

Procedure

| Step # | Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser (Retail) |  |  |
| 2 | Open create purchase requisition – advanced app | Open the Create Purchase Requisition - Advanced (ME51N) app. | The Create Purchase Requisition screen is displayed. |  |
| 3 | Enter the details | All the details should be entered as mentionedPurchase Requisition type : NBItem Overview :Material : R_1003Plant : for example 3340Quantity : 10 PC | Key values of dropdown list are visible. |  |
| 4 | Save the document | Select Save.Make a note of purchase requisition number. | A message indicating Purchase requisition number is created is displayed. |  |

Result

#### Purchase Order

##### Create Purchase Order for Standard Receiving

Use

Create a purchase order for standard receiving.

Procedure

| Step # | Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser (Retail). |  |  |
| 2 | Open create purchase order- advanced app | Open the Create Purchase Order - Advanced (ME21N) app. | The Create Purchase Order screen is displayed |  |
| 3 | Enter the details | Enter the following data:Order Type : NBSupplier : for example 33213002Header Details :Purchase Org : for example 3310Purchasing Group : <Select the purchasing group created in the configuration activity "Create Purchasing Groups" or select the purchasing group from the F4 help. For example: you can either select 001 or 002 >.Item Details:Purchase Req : XXXXXXXX (Use Purchase requisition created in chapter [Purchase Requisition for Standard PO](#unique_7) [page ] 7)Select ENTER.Alternative way to find the purchase requisitionChoose Document overview On, Choose selection variantChoose My Purchase RequisitionsChoose Purchase Requisition number and drop it into the basket PO Quantity : 5 CARUnit of measure changes based on the rounding rule (RDYP) of that material. | Key values of dropdown list are visible. |  |
| 4 | Save the document | Select SaveMake a note of purchase order number | A message indicating standard purchase order is created is displayed. |  |

##### Create Purchase Order for Trusted Receiving

Use

Create a purchase order for standard receiving.

Procedure

| Step # | Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser (Retail). |  |  |
| 2 | Open create purchase order- advanced app | Open the Create Purchase Order - Advanced (ME21N) app. | The Create Purchase Order screen is displayed |  |
| 3 | Enter the details | Ener the following data:Order Type : NBSupplier: for example 33213002Header Details :Purchase Org : for example 3310Purchasing Group : <Select the purchasing group created in the configuration activity "Create Purchasing Groups" or select the purchasing group from the F4 help. For example: you can either select 001 or 002>.Item Details :Purchase Req : XXXXXXXX (Use Purchase requisition created in chapter [Purchase Requisition for Trusted Purchase Order](#unique_8) [page ] 7)Add Variants : for example, R_1003001 and R_1003002Whole-Milk : 2Nuts : 2Choose ENTER | Key values of dropdown list are visible. |  |
| 4 | Save the document | Select Save.Make a note of purchase order number. | A message indicating standard purchase order is created is displayed. |  |

#### Create Inbound Delivery

##### Create Inbound Delivery for Standard Receiving

Use

Create an inbound delivery for standard receiving.

Procedure

| Step # | Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Receiving Specialist. |  |  |
| 2 | Open create inbound delivery app under inbound delivery processing group | Open the app. | The screen is displayed. |  |
| 3 | Enter the details | Enter the following data:Purchase Order number : XXXXXXXX (Please refer to PO which is created in chapter [Create Purchase Order for Standard Receiving](#unique_9) [page ] 8)Supplier: for example 33213002Delivery date: <DD.MM.YYYY> | Key values option list is visible. |  |
| 4 | Continue | Select Continue | Detail screen is displayed |  |
| 5 | Enter the quantity | Enter the Putaway quantity same as delivery quantity. |  |  |
| 6 | Choose save document | Select Save.Make a note of inbound delivery number. | A message indicating an inbound delivery is saved is displayed. |  |

##### Create Inbound Delivery for Trusted Receiving

Use

Create an inbound delivery for standard receiving.

Procedure

| Step # | Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Receiving Specialist. |  |  |
| 2 | Access app | Open the app. | The screen is displayed |  |
| 3 | Enter the details | Enter the following data:Purchase Order number : XXXXXXXX (Please refer to PO which is created in chapter [Create Purchase Order for Trusted Receiving](#unique_10) [page ] 9)Supplier: for example 33213002Delivery date : <DD.MM.YYYY> | Key values option list is visible. |  |
| 4 | Select continue | Select Continue | Detail screen is displayed |  |
| 5 | Enter the quantity | Enter the putaway quantity same as delivery quantity. |  |  |
| 6 | Choose save document | Select Save.Make a note of inbound delivery number. | A message indicating inbound delivery is saved is displayed. |  |

Result

|  |
| --- |
| Note With the creation of outbound delivery for standard and trusted PO, you can review order proposal and receive product as described in the Test Procedure chapter. |

#### Create Customer Order for Receive Products

##### Create Customer Order

Refer to the scope item In-Store Customer Order Management (3HU) step Create Sales Order and make a note of the sales order numbers and the corresponding purchase requisitions created.

|  |
| --- |
| Note Please use the master data specified in - In-Store Customer Order Management (3HU) test script.Create three sales orders to test three scenarios for the Receive Products (F1248) app. |

##### Create Purchase Order from Purchase Requisition

Use

Create a purchase order, with reference to a purchase requisition, without confirmation indicator for customer order-based receiving.

Procedure

| Step # | Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser (Retail) |  |  |
| 2 | Open create purchase order- advanced app | Open the Create Purchase Order - Advanced (ME21N) app. | The Create Purchase Order screen is displayed. |  |
| 3 | Enter the details | Enter the following data:Order Type : NBSupplier: for example 33213001Header Details :Purchase Org : for example 3310Purchasing Group : <Select the purchasing group created in the configuration activity "Create Purchasing Groups" or select the purchasing group from the F4 help. For example: you can either select 001 or 002>Item Details :Purchase Req : XXXXXXXX (Use Purchase requisition picked from sale order created in chapter [Create Customer Order](#unique_13) [page ] 12)Note In case there are more than one line item, enter the Requisn. Item – Item of Requisition.Choose ENTER | Key values of dropdown list are visible. |  |
| 4 | Remove Confirmation Control | In Item Details section, Confirmation tab, remove the confirmation control.Note This step ensures that you are able to run the receive product app with respect to a purchase order, without creating an Inbound delivery. |  |  |
| 5 | Save the document | Select Save.Make a note of purchase order number. | A message indicating standard purchase order created is displayed. |  |

##### Convert Purchase Requisition to Purchase Order

Refer to scope item Procurement for Retail (5FM) step 4.2.2 and make a note of the purchase order number created using purchase requisition from step [Create Customer Order](#unique_13) [page ] 12.

|  |
| --- |
| Note By using the data specified in chapter [Master Data, Organizational Data, and Other Data](#unique_5) [page ] 5 convert two (out of three) purchase requisitions to purchase orders to test Receive Products (F1248) app using inbound delivery with handling unit (HU) and inbound delivery without handling unit (HU) respectively. |

##### Create Inbound Delivery (Optional)

Use

Create an inbound delivery for standard receiving.

Procedure

| Step # | Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Receiving Specialist. |  |  |
| 2 | Access App | Open the app | The screen is displayed |  |
| 3 | Enter the details | All the details enter as mentionedPurchase Order number : XXXXXXXX (Please refer to PO which is created in chapter [Create Purchase Order from Purchase Requisition](#unique_14) [page ] 12)Supplier: for example 33213001Delivery date : <DD.MM.YYYY> | Key values option list is visible. |  |
| 4 | Select continue | Select Continue | Detail screen is displayed |  |
| 5 | Enter the quantity | Enter the putaway quantity for each product equal to the delivery quantity |  |  |
| 6 | Select save document | Select Save.Make a note of inbound delivery number. | A message indicating inbound delivery saved is displayed. |  |

Result

With the creation of inbound delivery for the purchase order, you will be able to do the review order proposal and receive product as described in this business process .

|  |
| --- |
| Note Repeat the above steps to create inbound delivery for the other purchase order as well. |

##### Create Handling Unit (Optional)

Use

Create handling unit for inbound delivery.

Procedure

| Step # | Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Receiving Specialist. |  |  |
| 2 | Access App | Open the Change Inbound Deliveries - Deliveries (F1706) app. | The Change Inbound Delivery screen is displayed. |  |
| 3 | Enter the details | Inbound Delivery : XXXXXXXX (Please refer to Inbound delivery which is created in chapter [Create Inbound Delivery (Optional)](#unique_16) [page ] 14).Note Take one (out of 2) inbound delivery created in step [Create Inbound Delivery (Optional)](#unique_16) [page ] 14 |  |  |
| 4 | Select continue | Select Continue | Detail screen is displayed |  |
| 5 | Pack the Material | Select the material line item and select Pack.Select Pack Material tab. | Processing of handling unit for inbound delivery XXXXXXX screen is displayed |  |
| 6 | Enter Packaging Material | Enter the Packaging material: R_CARTONSelect Enter | Handling unit gets created successfully. |  |
| 7 | Pack the Material | Select both the material (in material to be packed section) and the Handling unit created and select Pack. | A message indicating Material is packed is displayed. |  |

Result

The created HU can be used in the Receive Products (F1248) app.

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Review Order Proposals](#unique_19) [page ] 17 | SAP_BR_RFM_STORE_ASSOCIATE | Order Products (F0752) | The store associate reviews and changes the order proposals |
| [Receive Product (Standard)](#unique_20) [page ] 18 | SAP_BR_RFM_STORE_ASSOCIATE | Receive Products (F1248) | The store associate review and post the good receipt partial, remaining and adjust after posting. |
| [Receive Product for Customer Order-Based Purchase Order](#unique_21) [page ] 20 | SAP_BR_RFM_STORE_ASSOCIATE | Receive Products (F1248) | The store associate review and post the good receipt partial, remaining and adjust after posting. |
| [Receive Product for Customer Order-Based Purchase Order and Inbound Delivery Without Handling Unit](#unique_22) [page ] 21 | SAP_BR_RFM_STORE_ASSOCIATE | Receive Products (F1248) | The store associate review and post the good receipt partial, remaining and adjust after posting. |
| [Receive Product for Customer Order-Based Purchase Order and Inbound Delivery with Handling Unit](#unique_23) [page ] 22 | SAP_BR_RFM_STORE_ASSOCIATE | Receive Products (F1248) |  |
| [Look Up Retail Products (Optional)](#unique_24) [page ] 24 | SAP_BR_RFM_STORE_ASSOCIATE | Look Up Retail Products (F0431) | The store associate can view the stock level of a product as well as general information to inform the consumer. |
| [Receive Product - Trusted](#unique_25) [page ] 25 | SAP_BR_RFM_STORE_ASSOCIATE | Receive Products (F1248) | The store associate posts the good receipt automatically without having the enter quantities or check the product. |
| [Look Up Retail Products (Optional)](#unique_26) [page ] 26 | SAP_BR_RFM_STORE_ASSOCIATE | Look Up Retail Products (F0431) | The store associate can view the stock level of a product as well as general information to inform the consumer. |
| [Schedule Clean Up of Operational Data for Receive Products (Optional)](#unique_27) [page ] 27 | SAP_BR_ADMINISTRATOR_RFM | Receive Products (F1248) |  |

## Test Procedures

This chapter describes the test procedures for each process step that belongs to this scope item.

### Review Order Proposals

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
| 3 | Search product | Search for the product R_1037 or scan the barcode of a specific product or attributes White bread large, organicChoose ENTER. | The list of products is filtered according to the entered filter criteria. |  |
| 4 | Filter | Select No Filter SelectedSelect Merchandise category and search R1171001Choose OK. | The filter helps to work on a small list of products. |  |
| 5 | Show order proposal | No Filter SelectedEnter the product ID R_1037 and Choose ENTER or enter the term in the product search White bread large, organic and Choose ENTER Select a product from the search result list. | The detail view of the order proposal displays the following: the proposed and actual order quantity, whether the product is currently on current, expected, and allocated stock |  |
| 6 | Change order proposal | Adapt the quantity “1" and Choose ENTER on the product details of the line item. | The product detail view of the order product displays as the quantity is changed so the order quantity edit box color is changed to Green. |  |
| 7 | Leave the app | Select the SAP icon to navigate back to home. |  |  |

### Receive Product - Standard

#### Receive Product (Standard)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process describes the standard goods receipt process, that is, products arrive from an external supplier or a distribution centre. Received item quantities are individually checked against expected quantities, confirmed, or adapted, if necessary, and only then posted.

Procedure

In case the app is still open, and an article is still selected from another test, the steps 1 – 3 do not have to be executed again.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Retail Store Associate. |  |  |
| 2 | Access app | Open the Receive Products (F1248) app. | The upcoming deliveries are displayed. |  |
| 3 | Open document | Select Enter ID.Enter the purchase order ID XXXXXXXX (Please refer to PO which is created in chapter [Create Purchase Order for Standard Receiving](#unique_9) [page ] 8)or use the filter to specify documents and Select the document XXXXXXX (Please refer to document ID which is created in chapter [Create Purchase Order for Standard Receiving](#unique_9) [page ] 8) and Select OK to open it. | The details of the delivery are displayed. |  |
| 4 | Post partial goods receipt | Enter at least the quantity “1” for one product and select Post | The status of the goods receipt changes to Partially Posted. |  |
| 5 | Post remaining goods receipt | Post the remaining products enter quantity 4 of the goods receipt and select on Post | The status of the goods receipt changes to Completed. |  |
| 6 | Adjust the goods receipt | Decrease the number of a received product by 1 enter quantity “-1”(Negative stock) | The status of the goods receipt is changed to In Process. |  |
| 7 | Post the goods receipt | Select Post. | The status changes to Partially Posted. |  |
| 8 | Enter the zero quantity for the product | Enter the quantity 0 for the product and choose Checked and Delivery Completed | The status of the goods receipt is changed to In Process. |  |
| 9 | Post the goods receipt | Select Post. | The status of the goods receipt changes to Completed. |  |

#### Receive Products for Customer Account Assigned Purchase Order

##### Receive Product for Customer Order-Based Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process describes the standard goods receipt process, that is, products arrive from an external vendor or a distribution centre. Received item quantities are individually checked against expected quantities, confirmed, or adapted, if necessary, and only then posted.

Procedure

In case the app is still open, and an article is still selected from another test, the steps 1 – 3 do not have to be executed again.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Retail Store Associate. |  |  |
| 2 | Access app | Open the Receive Products (F1248) app. | The upcoming deliveries are displayed. |  |
| 3 | Open document | Select Enter ID.Enter the purchase order ID XXXXXXXX (Please refer to PO which is created in chapter [Create Purchase Order from Purchase Requisition](#unique_14) [page ] 12) | The details of the delivery are displayed. |  |
| 4 | Check the Delivery completed indicator | Check the Delivery completed indicator | The delivery completed indicator can be manually set, in case of partial receive if there is no further shipment expected from the supplier. |  |
| 5 | Check the status in Process picking request app | Select Navigation and select Process Picking Requests (F4643) app | Status is shown as Stock yet to arrive. |  |
| 6 | Navigate back to receive products app | Navigate back to Receive Products (F1248) app. |  |  |
| 7 | Post the goods receipt | Select Post | The status changes to Completed. |  |
| 8 | Navigate to Picking Request App (Optional) | Select Navigation and select Process Picking Requests (F4643) appNote Please refer to Start Picking in Scope Item In-Store Customer Order Management (3HU) to perform the picking (Optional). | Status is shown as Not picked. |  |

##### Receive Product for Customer Order-Based Purchase Order and Inbound Delivery Without Handling Unit

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process describes the standard goods receipt process, that is. products arrive from an external vendor or a distribution centre. Received item quantities are individually checked against expected quantities, confirmed, or adapted, if necessary, and only then posted. Here we use the inbound delivery created without the handling unit.

Procedure

In case the app is still open, and an article is still selected from another test, the steps 1 – 3 do not have to be executed again.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Retail Store Associate. |  |  |
| 2 | Access app | Open the Receive Products (F1248) app. | The upcoming deliveries are displayed. |  |
| 3 | Open document | Select Enter ID.Enter the Inbound delivery XXXXXXXX (Please refer to PO which is created in chapter [Convert Purchase Requisition to Purchase Order](#unique_15) [page ] 13 with Inbound Delivery (without HU) created as part of step [Create Inbound Delivery (Optional)](#unique_16) [page ] 14) | The details of the delivery are shown.Receive Products for Customer Order <XXXXX> |  |
| 4 | Check the Delivery completed indicator | Check the Delivery completed indicator. | The delivery completed indicator can be manually set, in case of partial receive if there is no further shipment expected from the supplier. |  |
| 5 | Check the status in Process picking request app | Select Navigation and select Process Picking Requests (F4643) app. | Status is displayed as Stock yet to arrive |  |
| 6 | Navigate back to receive products app | Navigate back to Receive Products (F1248) app. |  |  |
| 7 | Post the goods receipt | Select Post. | The status changes to Completed. |  |
| 8 | Navigate to Picking Request App (Optional) | Select Navigation and select Process Picking Requests (F4643) appPlease refer to Start Picking in Scope Item In-Store Customer Order Management (3HU) to perform the picking (Optional) | Status is displayed as Not picked |  |

##### Receive Product for Customer Order-Based Purchase Order and Inbound Delivery with Handling Unit

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process describes the standard goods receipt process, that is, products arrive from an external vendor or a distribution centre. Received item quantities are individually checked against expected quantities, confirmed, or adapted, if necessary, and only then posted. Here we use the inbound delivery created with the handling unit as part of.

Procedure

In case the app is still open, and an article is still selected from another test, the steps 1 – 3 do not have to be executed again.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Retail Store Associate |  |  |
| 2 | Access app | Open the Receive Products (F1248) app. | The upcoming deliveries are displayed. |  |
| 3 | Open document | Select Enter ID.Enter the Inbound delivery XXXXXXXX (Please refer to PO which is created in chapter [Convert Purchase Requisition to Purchase Order](#unique_15) [page ] 13 with Inbound Delivery (with handling unit) created as part of step [Create Inbound Delivery (Optional)](#unique_16) [page ] 14). | The details of the delivery are displayed. | Receive Products for Customer Order XXXXX |
| 4 | Check the Delivery completed indicator | Check the Delivery completed indicator. | The delivery completed indicator can be manually set, in case of partial receive if there is no further shipment expected from the supplier. |  |
| 5 | Check the status in Process picking request app | Select Navigation and select Process Picking Requests (F4643) app. | Status is displayed as Stock yet to arrive |  |
| 6 | Navigate back to receive products app | Navigate back to Receive Products (F1248) app. |  |  |
| 7 | Post the goods receipt | Select Post | The status changes to Completed |  |
| 8 | Navigate to Picking Request App (Optional) | Select Navigation and select Process Picking Requests (F4643) appPlease refer to Start Picking in Scope Item In-Store Customer Order Management (3HU) to perform the picking (Optional) | Status is displayed as Not picked |  |

#### Look Up Retail Products (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When approached by consumers, store associates can use the Look Up Retail Products (F0431) app to get details of an article and provide a better service for their customers. For example, this might be the information, if a certain article is still in stock. In case required components have been implemented, store associates are able to provide real-time stock information.

Procedure

In case the app is still open, and an article is still selected from another test, the steps 1 – 3 do not have to be executed again.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Retail Store Associate |  |  |
| 2 | Access app | Open the Look Up Retail Products (F0431) app. | The upcoming deliveries are displayed. |  |
| 3a | Scan a product (on mobile) | Select Scan to scan the barcode using the camera on the device to view the details of the associated product.Note Only possible on mobile device with SAP/ Custom Fiori Client. | The stock is updated after receiving. |  |
| 3b | Search a product (on a web browser) | Enter the material that you have received (for Example: R_1037) in the product search and ENTER. Select a product from the search result list. | The stock should be updated after receiving. |  |

### Receive Product - Trusted

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In the trusted receiving process, store associate assumes that the products and the quantity that was delivered to his store on the pallet are correct, for example because the shipment comes from the own distribution center or from a trusted supplier. Store associates know that their own distribution center or your trusted supplier does not over ship or under ship ordered quantities.

Procedure

In case the app is still open, and an article is still selected from another test, the steps 1 – 3 do not have to be executed again.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Retail Store Associate |  |  |
| 2 | Access app | Open the Receive Products (F1248) app. | The upcoming deliveries are displayed. |  |
| 3 | Switch to mobile mode | Right click the screen and select Inspect for Windows OS and Inspect Element for MAC OS select higher version of mobile device ‘ IPhoneX ’ and refresh the page. | Mobile mode is displayed with Scan option.Note for OS dependency |  |
| 4 | Scan & Post document | Select Scan and enter the Inbound delivery no XXXXXXXX (Please refer to Inbound delivery no which is created in chapter [Create Inbound Delivery for Trusted Receiving](#unique_12) [page ] 11) and select OK | The goods receipt is posted automatically in the background without having to enter quantities or check the products. Once posted status is updated to completed and a scan icon is displayed next to the order indicating it has been received as trusted. |  |

#### Look Up Retail Products (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When approached by consumers, store associates can use the Look Up Retail Products (F0431) app to get details of an article and provide a better service for their customers. For example, this might be the information, if a certain article is still in stock. In case required components have been implemented, store associates are able to provide real-time stock information.

Procedure

In case the app is still open, and an article is still selected from another test, the steps 1 – 3 do not have to be executed again.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Retail Store Associate |  |  |
| 2 | Access app | Open the Look Up Retail Products (F0431) app. | The upcoming deliveries are displayed. |  |
| 3a | Scan a product (on mobile) | Select Scan to scan the barcode using the camera on the device to view the details of the associated product.Note Only possible on mobile device with SAP/ Custom Fiori Client. | The stock is updated after receiving. |  |
| 3b | Search a product (on a web browser) | Enter R_1003 or term Chocolate in the product search and ENTER. Select a product from the search result list. | The stock should be updated after receiving. |  |

### Schedule Clean Up of Operational Data for Receive Products (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to clean up the unused operational data from the Receive Products (F1248) app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as an Administrator (Retail) |  |  |
| 2 | Access app | Open Schedule Clean Up of Operational Data - Receive Products (F5595) app. | Schedule Clean Up of Status Tables: Receive Product screen is displayed. |  |
| 3 | Provide input values | On the initial screen, make the following entry in selection criteria and restriction and select CreateJob Template: Cleanup of Operational Data for Receive ProductsJob Name: Cleanup of Operational Data for Receive ProductsSelect Step2Select Step3Select Parameters for Selection Criteria:Under Delete Unprocessed Documents section:Enter Minimum Number of Days: XX(Any available inbound delivery, purchase order or outbound delivery documents which are unused can be deleted by giving the no of days that are not processed since)the Simulate check box is selectedNote By unchecking simulate, all the available documents will be deleted. | Entry is updated. |  |
| 4 | Check | Select Check for validating | The message is displayed as:You can go ahead and schedule the job |  |
| 5 | Schedule Job | Select Schedule and following message appears Job Cleanup of Operational Data for Receive Products has been scheduled. |  |  |
| 6 | Check Job Results | On the Application Jobs screen, after job item status turned to Finished, choose Navigate to the job results in the Results column. | Document (ID XXXXXX) is displayed with job results.Status of X documents will be deleted (not processed since) |  |

Result

Documents which are available in the given period are deleted.

## Appendix

### Process Integration

Not applicable

#### Preceding Processes

The following processes and conditions can proceed this process.

| Process | Business Condition |
| --- | --- |
| 5FU | Outbound Logistics for Distribution Centers |

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Scope Item | Business Condition |
| --- | --- |
| 5FN | Invoice Verification for Retail |

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
- related-to :: [[15-retail-operations/test-script-store-ordering-from-distribution-center-5fx-ae-1092]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5FY_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 49,177 chars in the whole document
