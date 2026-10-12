---
id: 08-sales-order-management/test-script-sap-returnable-packaging-management-7ho-ae-1215
title: "Test Script: SAP Returnable Packaging Management (7HO_AE) (7HO_S4CLD2608_BPD_EN_AE)"
description: "Test script for SAP S/4HANA Cloud scope item 7HO (SAP Returnable Packaging Management, AE): customer and supplier returnable packaging prerequisites and steps."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/returnable-packaging]
aliases: [7HO_S4CLD2608_BPD_EN_AE]
keywords: [Returnable Packaging and Pallets, returnable packaging management, returnable packaging accounts, customer returnable packaging, supplier returnable packaging, packaging replenishment, outbound delivery, manual packing, goods issue, goods receipt]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7HO_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1215
topic: 08-sales-order-management/returnable-packaging
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: SAP Returnable Packaging Management (7HO_AE) (7HO_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7HO_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Returnable Packaging and Pallets** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | SAP Returnable Packaging Management (7HO_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232860358)

[2 Prerequisites 4](#_Toc232860359)

[2.1 System Access 4](#_Toc232860360)

[2.2 Roles 4](#_Toc232860361)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232860362)

[2.4 Preliminary Steps 6](#_Toc232860363)

[2.4.1 Extend Customer Master Data 6](#_Toc232860364)

[2.4.2 Extend Supplier Master Data 7](#_Toc232860365)

[2.4.3 Create Purchasing Contract 8](#_Toc232860366)

[2.4.4 Set Initial Stock of Finished Material 9](#_Toc232860367)

[2.5 SAP Returnable Packaging Management Setup 10](#_Toc232860368)

[2.5.1 Returnable Packaging Account with Customer 11](#_Toc232860369)

[2.5.2 Returnable Packaging Account with Supplier 13](#_Toc232860370)

[3 Overview Table 15](#_Toc232860371)

[4 Test Procedures 17](#_Toc232860372)

[4.1 Process with Customer 17](#_Toc232860373)

[4.1.1 Create Sales Order 17](#_Toc232860374)

[4.1.2 Create Outbound Delivery 18](#_Toc232860375)

[4.1.3 Execute Manual Packing 19](#_Toc232860376)

[4.1.4 Post Goods Issue 20](#_Toc232860377)

[4.1.5 Steps in SAP RPM 21](#_Toc232860378)

[4.1.5.1 Check Posting Document 21](#_Toc232860379)

[4.1.5.2 Check Packaging Account 22](#_Toc232860380)

[4.1.5.3 Check Stock Overview 23](#_Toc232860381)

[4.1.6 Create Replenishment in SAP RPM 24](#_Toc232860382)

[4.1.7 Post Goods Receipt 25](#_Toc232860383)

[4.1.8 One Step Stock Transfer 26](#_Toc232860384)

[4.2 Process with Supplier 27](#_Toc232860385)

[4.2.1 Post Goods Receipt 27](#_Toc232860386)

[4.2.2 Create Outbound Delivery without Order Reference 29](#_Toc232860387)

[4.2.3 Post Goods Issue 30](#_Toc232860388)

## Purpose

Scenarios mentioned in this document cover how returnable packaging materials can be exchanged between your company and suppliers, as well as between your company and customers.

Overview

SAP Returnable Packaging Management is a product on SAP Business Technology Platform for managing reusable returnable packaging materials in a supply chain. Reusable packaging materials such as containers, pallets, tanks, and load carriers are used to move products safely and efficiently between business partners.

Scenarios mentioned in this document cover how returnable packaging materials can be exchanged between your company and suppliers, as well as between your company and customers.

In the scope item SAP Returnable Packaging Management (7HO), two processes are documented as best practices:

- Closed loop customer returnable packaging - Customer orders packaged products from the plant. Customers return empty packaging material back to the plant after consumption of the products.
- Closed loop supplier returnable packaging - Supplier receives empty packaging material from customer-plant. These packaging materials are delivered by supplier to the plant together with the ordered products. Packaging materials are sent back by the plant after products have been consumed.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

| System | Details |
| --- | --- |
| System | Accessible through SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

You can also use the following space templates that determine the SAP Fiori launchpad layout for a business role. With the space template, you create a space with pages containing predefined apps and assign it to the business role. You then assign this business role to your individual users. For more information, refer to [How to Create a Business Role for a Key User](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/8fa28e0107984d42a99b9eea67856cea.html?version=2408.500) in the product assistance for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) |
| --- | --- | --- | --- |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |

|  |
| --- |
| Note The SAP RPM roles are maintained in SAP BTP cockpit. For more information, refer to the 7HO Setup Guide. |

### Master Data, Organizational Data, and Other Data

Relevant Master Data and Organizational Data Object Types can be uploaded to the SAP RPM system through the applications.

Material Masters mentioned in this document are to be created for both US (1710) and DE (1010) plants.

| Data | Sample Value | Description |
| --- | --- | --- |
| Material | TG11 | Trading Good for Reg. Trading (MRP planning) |
| Material | RPM_PAL_001 | RPM Packaging Material |
| Plant | 3310 | Plant 1 AE |
| Ship-To Party | 33104091 | Domestic AE Customer 3 |
| Storage Location | 331A | Std. storage 1 |
| Storage Location | 331B | Std. storage 2 |
| Company Code | 3310 | Company Code 3310 |
| Sales Organization | 3310 | Dom. Sales Org |
| Distribution Channel | 10 | Direct Sales |
| Division | 00 | Product Division 00 |
| Purchasing Organization | Purchasing Organization AE 3310 | Organizational Unit |
| Purchasing Group | 001/002 | Group 001/Group 002 |
| Vendor | 33304093 | Domestic 33 Supplier 1 |

### Preliminary Steps

#### Extend Customer Master Data

The following procedure provides instructions for extending customer to act as supplier.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log on. | Log onto the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. |  |
| 2 | Access the SAP Fiori application. | Choose the Maintain Business Partner (BP) app. | The Maintain Business Partner (BP) screen is displayed. |
| 3 | Display business partner. | Choose Open BP and enter Business partner: 33104091 | Display Organization: <Business Partner> screen is displayed. |
| 4 | Switch to change mode. | Choose Switch Between Display and Change (F6) button to switch to change mode. | Change Organization: <Business Partner> screen is displayed. |
| 5 | Change BP role. | In the Change in BP role field, choose the following value:SupplierNote The technical key of this BP role is FLVN01. | Supplier role is displayed |
| 6 | Open Purchasing. | Choose Purchasing at the top of the screen. | The Purchasing screen is displayed. |
| 7 | Enter purchasing organization data. | Enter the following data and hit enter:Purchasing Organization AE 3310Note In case a different purchasing organization is already entered, choose Switch Organization and enter the purchasing organization. | Details provided. |
| 8 | Enter sales area data. | In the Purchasing Data tab in the Conditions section, enter the following data:Order Currency: EURPayment Terms: 0001Note In case of a different region, enter the respective currency and payment terms.In the Control Data section, enterShipping Conditions: 01 - Standard | Details provided. |
| 9 | Save your data. | Save your entries.Note A warning Customer ##1 is from an EU country/region; enter a VAT registration number (CMD_API007). Display this message for this business partner again? is displayed. Choose No. | The entry in the Change in BP role field switches from Supplier (New) to Supplier (defined). |

#### Extend Supplier Master Data

The entry in the Change in BP role field switches from Supplier (New) to Supplier (defined).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log on. | Log onto the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. |  |
| 2 | Access the SAP Fiori application. | Choose the Maintain Business Partner (BP) app. | Maintain Business Partner (BP) screen is displayed. |
| 3 | Display business partner. | Choose Open BP and enter Business Partner: 33304093. | Display Organization: <Business Partner> screen is displayed. |
| 4 | Switch to change mode. | Choose Switch Between Display and Change (F6) button to switch to change mode. | Change Organization: <Business Partner> screen is displayed. |
| 5 | Change BP role. | In the Change in BP role field, choose the following value:CustomerNote The technical key of this BP role is FLCU01. | Customer role is displayed. |
| 6 | Open Sales and Distribution Data. | Choose Sales and Distribution at the top of the screen. | The Sales Area screen appears. |
| 7 | Enter sales area data. | Enter the following data:Sales Org: 3310Distribution Channel: 10Division: 00 | Details provided. |
| 8 | Verify tax details. | Go to the Billing tab, provide the details in Output Tax section, and enter the following data for country: DETax Classification: <1> | Tax classification entered. |
| 9 | Save your data. | Save your entries.Note A warning Customer ##1 is from an EU country/region; enter a VAT registration number (CMD_API007). Display this message for this business partner again? is displayed. Choose No. | The entry in the Change in BP role field switches from Customer (New) to Customer (defined). |

#### Create Purchasing Contract

In this activity you create the contract for the packaging material. The purchase contract is needed in order to create the replenishment via SAP RPM towards the supplier.

Make sure that you enter a price of 0 EUR since you don’t buy but rent the returnables from the supplier.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log on. | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori Launchpad opens. |
| 2 | Access the SAP Fiori application. | Choose the Manage Purchase Contracts (F1600A) app. | The Manage Purchase Contracts (F1600A) screen is displayed. |
| 3 | Enter contract header details. | On the Manage Purchase Contracts screen, choose Create and make the following entries:Contract Type: Quantity Contract (MK)Supplier: 33304093Purchasing Organization AE 3310Valid From: Start date of the contract, for example, todayValid To: End date of the contract, for example, the end of this yearPurchasing Group: 001Target value: For example, 0 EURNote In order to enter a price of 0, you need to take out the Invoice Receipt flag in the item line.Currency: EURCompany Code: 3310 | Details on header level provided. |
| 4 | Enter contract item details. | In the Items tab, choose Create and make the following entries:Material: RPM_PAL_001Select the arrow on the end of the item.Plant: 3310.In the Quantity and Price sectionNet price: Enter a net order price, 0 EUR per PC.Target Quantity: For example, 5000.Take out the Invoice Receipt flag.Choose Apply. | Details on item level provided. |
| 5 | Save the purchase contract. | Choose Create and when the purchase contract number is displayed, write it down for further use. | A new purchase contract is created. The Purchase Contract Number is displayed. |

#### Set Initial Stock of Finished Material

In a real business case, the materials are usually purchased from external suppliers. This process step shows you how to post initial stock directly to the storage locations. This material later on will be packed and sent to the customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log on. | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori Launchpad opens. |
| 2 | Access the SAP Fiori application | Choose the Manage Stock (F1062) app. | The Manage Stock (F1062) screen is displayed. |
| 3 | Input material. | Make the following entries and choose Enter.Material: TG11Plant: 3310 |  |
| 4 | Select stock. | Select the icon beside the stock that you want to add initial stock.Storage Location: 331AUnrestricted-Use Stock | The Manage Stock dialog box opens. The Storage Location, Stock Type, and Current Quantity display according to your entries in previous steps. |
| 5 | Add initial stock. | Make the following entries and choose Post.Stock Change: Initial EntryQuantity: Enter a number, for example, 100Document Date: <Today>Posting Date: <Today> | The system displays Material document XXX created message. The stock has been added. |
| 6 | Repeat all steps from above. | Use Material: RPM_PAL_001 |  |

### SAP Returnable Packaging Management Setup

Follow the steps below to set up packaging accounts in your tenant.

#### Returnable Packaging Account with Customer

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log on. | Log on to the SAP RPM launchpad as a Configuration Expert. | The SAP RPM launchpad opens. |
| 2 | Access the application. | Open the Manage Returnable Packaging Accounts (F5126 ) app. | TheManage Returnable Packaging Accounts screen is displayed. |
| 3 | Create the packaging account. | Create Create and fill out the following fields.Note In case the Create button can’t be seen, choose the three dots on the right and side and select Create from the dropdown menu.Example In the Main Relationship sectionExchange Partner: CustomerExchange Partner: 33104091Location Partner: 3310Description: Such as RPM BP Scenario with CustomerIn the General Information sectionMaterial Description: RPM_PAL_001Processor: The name that is maintainedCompany Code: 3310Matching Relevance: noIn the Replenishment sectionPlanning Type: Manual Reorder Point PlanningPlanning Relevance: Manual Replenishment CreationIn the Purchase Order sectionMinimum Reorder Point Quantity : -1Note Based on the reorder point quantity, the system calculates whether or not the actual account balance and open purchase orders (minus open sales orders) fall below the minimum reorder point quantity. Accordingly, a replenishment order is created.Rounding Value: 5Enable Purchase Order: XPurchase Agreement Number: enter the purchase contract number that you have created in the preliminary stepsPurchase Outline Agreement Number: 10In the Partner Relationship sectionExchange Partner Type: VendorExchange Partner: 33104091Location Partner Type: PlantLocation Partner: 3310Company Code: 3310Note The Exchange Partner Relationship with the Customer role will be maintained automatically when creating the packaging account.Choose Create. | The returnable packaging account for the customer is created.Make a note of the number. |
| 4 | Activate account. | Choose Activate. | The returnable packaging account is activated. |

#### Returnable Packaging Account with Supplier

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log on. | Log on to the SAP RPM launchpad as a Configuration Expert. | The SAP RPM launchpad opens. |
| 2 | Access the application. | Open the Manage Returnable Packaging Accounts (F5126 ) app. | TheManage Returnable Packaging Accounts screen is displayed. |
| 3 | Create the packaging account. | Create Create and fill out the following fields.Note In case the Create button can’t be seen, choose the three dots on the right and side and select Create from the dropdown menu.Example In the Main Relationship sectionExchange Partner Type: VendorExchange Partner: 33304093Location Partner: 3310Description: Such as RPM BP Scenario with SupplierIn the General Information sectionMaterial Description: RPM_PAL_001Processor: The name that is maintainedCompany Code: 3310Matching Relevance: noIn the Replenishment sectionPlanning Type: Not Active for PlanningIn the Partner Relationship sectionExchange Partner Type: CustomerExchange Partner: 33304093Location Partner Type: PlantLocation Partner: 3310Company Code: 3310Note The Exchange Partner Relationship with the Vendor role will be maintained automatically when creating the packaging account.Choose Create. | The returnable packaging account for the customer is created.Make a note of the number. |
| 4 | Activate account. | Choose Activate. | The returnable packaging account is activated. |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Output |
| --- | --- | --- | --- |
| Process with Customer |  |  |  |
| [Create Sales Order](#unique_15) [page ] 17 | Internal Sales Representative | Manage Sales Orders (F1873) | Sales order created |
| [Create Outbound Delivery](#unique_16) [page ] 18 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) | Outbound delivery created |
| [Execute Manual Packing](#unique_17) [page ] 19 | Shipping Specialist | Change Outbound Delivery (VL02N) | Material is packed and extra packaging item line is created |
| [Post Goods Issue](#unique_18) [page ] 20 | Shipping Specialist | Change Outbound Delivery (VL02N) | Goods issue posted for outbound delivery |
| Steps in SAP RPM |  |  |  |
| [Check Posting Document](#unique_19) [page ] 21 | Packaging Manager | Manage Posting Documents (F5125) | Posting document created by material document from step 6.2 found |
| [Check Packaging Account](#unique_20) [page ] 22 | Packaging Manager | Manage Returnable Packaging Account (F5126) | Changed account balance can be seen |
| [Check Stock Overview](#unique_21) [page ] 23 | Packaging Manager | Returnable Stock Overview (F6889) | Stock overview analyzed |
| [Create Replenishment in SAP RPM](#unique_22) [page ] 24 | Packaging Manager | Manage Returnable Packaging Account (F5126) | Replenishment created |
| [Post Goods Receipt](#unique_23) [page ] 25 | Inventory Manager | Post Goods Movement (MIGO) | Goods receipt for PO posted and material document created |
| [One Step Stock Transfer](#unique_24) [page ] 26 | Warehouse Clerk | Transfer Stock - In-Plant (F1061) | Stock transferred from "empty" to "full" |
| Process with Supplier |  |  |  |
| [Post Goods Receipt](#unique_25) [page ] 27 | Inventory Manager | Post Goods Movement (MIGO) | Goods receipt for PO posted and material document created |
| [Create Outbound Delivery without Order Reference](#unique_26) [page ] 29 | Shipping Specialist | Create Outbound Delivery - Without Order Reference (VL01NO) | Outbound delivery created |
| [Post Goods Issue](#unique_27) [page ] 30 | Shipping Specialist | Change Outbound Delivery (VL02N) | Goods issue posted for outbound delivery |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Process with Customer

#### Create Sales Order

This process step shows you how to create a sales order.

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log on. | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori Launchpad opens. |
| 2 | Access the SAP Fiori application | Choose the Manage Sales Orders (F1873) app. | The Manage Sales Orders (F1873) screen is displayed. |
| 3 | Go to Create Order screen. | In the Manage Sales Orders screen, choose Create > Create Sales Orders - VA01 . |  |
| 4 | Enter data. | In the Create Sales Order screen, make the following entries and choose Enter.Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00 |  |
| 5 | Enter order details. | In the Create Standard Order: Overview screen, make the following entries.Sold-to Party: 33104091Ship-to Party: 33104091Customer References: <PO number>Material Number: TG11Quantity: 10 PC |  |
| 6 | Save document. | Choose Save. Make a note of the sales order number. | The order is saved. |

#### Create Outbound Delivery

This process step shows you how to create delivery.

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log on. | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori Launchpad opens. |
| 2 | Access the SAP Fiori application. | Choose the Create Outbound Deliveries - From Sales Orders (F0869A) app. | The Create Outbound Deliveries (F0869A) screen is displayed. |
| 3 | Search sales order. | Make the following entries and choose Go.Shipping Point: 3310Planned Creation Date: <Delivery selection date>Sales Document: Sales order number created previously |  |
| 4 | Create delivery. | Select your sales order items and choose Create Deliveries. | Creation of a delivery is triggered. |
| 5 | Check details. | Choose Display Log. | Delivery is created. Delivery number displays in the Deliveries tab. |

Note down the delivery number for later use.

#### Execute Manual Packing

You can execute packing for delivery items right in a outbound delivery.

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log on. | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |
| 2 | Access the SAP Fiori application | Choose the Change Outbound Delivery (VL02N) app. | The Change Outbound Delivery (VL02N) screen is displayed. |
| 3 | Enter the outbound delivery number. | In the Change Outbound Delivery, enter the outbound delivery number, and choose Enter. |  |
| 4 | Choose packing. | In the header section, choose Pack. |  |
| 5 | Select packaging materials. | In the All Existing HUs (Available for Packing) section of the screen, enter a value for Packaging Material and choose Enter. A Handling Unit No. will be automatically generated. Select both line items of Material and Handling Unit, then choose Pack.Note Make sure that you send out several handling units (for example, 5 handling units) to the customer so that the packaging account balance will be less than -1. Otherwise a replenishment will not be created.To create additional handling units, repeat step 5 and enter the same packaging materials in the next item lines. | Creation of a delivery is triggered. |
| 6 | Maintain packed quantities. | In Total Content tab, you can maintain the Packed Quantity for each handling unit. |  |
| 7 | Check general overview. | Choose General Overview in the header section to have a visualized hierarchy of all handling units. |  |
| 8 | Save your outbound delivery. | Choose Save to save packing results and your outbound delivery. | Packing results together with the outbound delivery is saved. |

#### Post Goods Issue

This process step shows you how to post goods issues for delivery.

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log on. | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori Launchpad opens. |
| 2 | Access the SAP Fiori application | Choose the Change Outbound Delivery (VL02N) app. | The Change Outbound Delivery (VL02N) screen is displayed. |
| 3 | Open outbound delivery monitor. | Make the following entries and choose Continue.Outbound Delivery: delivery number created previously | The Delivery XXX Change: Overview screen is displayed. |
| 4 | Execute picking. | Select the Picking tab.Picked Qty (TG11 and RPM_PAL_001): Copy qty from the Delivery Quantity field.SLoc: 331B (empty returnables) |  |
| 5 | Post good issue. | Choose Post Goods Issues. | The goods issue is posted.Note The created material document is replicated to SAP RPM and a posting document is created which triggers the postings in the packaging accounts. |

Note down the material document number for later use.

#### Steps in SAP RPM

##### Check Posting Document

With the creation of the material document in SAP S/4HANA a posting document in SAP RPM is created. This process step shows how to find posting documents by using Manage Posting Documents. The posting document automatically updates the packaging account.

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log on. | Log on to the SAP RPM launchpad as a Packaging Manager. | The SAP Fiori Launchpad opens. |
| 2 | Access the SAP Fiori application. | Choose the Manage Posting Documents (F5125) app. | The Manage Posting Documents app opens. |
| 3 | Search for posting document. | Search posting documents using different criteria. Choose Adapt Filters and all filter possibilities display. Enter the entries accordingly, then choose Go.ExampleMaterial: RPM_PAL_001Choose the row of a certain posting document to view detail. | The relevant Posting Documents / Posting Document items show.The colored bar on the left states if the posting was successful (green) or not (red). |
| 4 | Analyze the posting document. | In the posting document, go to the Reference section and compare the delivery number with the delivery number from the previous step. | The inventory document number and the material document are the same. |

##### Check Packaging Account

This process step shows how to see the account balance of the packaging account and find further information in Manage Returnable Packaging Accounts.

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log on. | Log on to the SAP RPM launchpad as a Packaging Manager. | The SAP Fiori Launchpad opens. |
| 2 | Access the SAP Fiori application. | Choose the Manage Returnable Packaging Accounts (F5126) app. | The Manage Returnable Packaging Accounts screen is displayed. |
| 3 | Search for packaging account | Search packaging accounts using different criteria. Choose Adapt Filters and all filter possibilities display. Enter the entries accordingly, then choose Go.ExampleMaterial: RPM_PAL_001Exchange Partner: 33104091Choose the row of a certain posting document to view detail. | The relevant packaging accounts show. |
| 4 | Analyze the posting document. | Check the account balance. | On top you can see the actual account balance. |

##### Check Stock Overview

This process step shows how to see stock overview in the Returnable Stock Overview.

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log on. | Log on to the SAP RPM launchpad as a Packaging Manager. | The SAP Fiori Launchpad opens. |
| 2 | Access the SAP Fiori application. | Choose the Manage Scheduled Jobs app. | All the jobs relevant for SAP RPM are displayed. |
| 3 | Search for job. | Choose the job Retrieve Stock Data and choose Activate. | The job is activated to update the stock information in SAP RPM. |
| 4 | Access the SAP Fiori application. | Choose the Returnable Stock Overview (F6889) app. | The Returnable Stock Overview app is displayed.Note The information about the Full Returnables, Empty Returnables, Plant Stock and the stock in transit are replicated by the Retrieve Stock Data job (Manage Scheduled Jobs app) from the S/4HANA backend system. The information about the Total Stock is the sum of the information coming from S/4HANA and SAP RPM. The other information is retrieved from SAP RPM. |
| 5 | Search for material. | Search packaging accounts using different criteria. Choose Adapt Filters and all filter possibilities display. Enter the entries accordingly, then choose Go.ExampleMaterial Code: RPM_PAL_001Plant: 3310 | The relevant material displays.Note After conducting a transfer posting, the effect can be seen in the information about the Full and the Empty Returnables. |
| 6 | Analyze the packaging materials. | Choose the blue numbers in order to check the division of the materials with your partners. | In case one material will be exchanged with several partners you can see the division of the material by choosing the blue numbers. |

#### Create Replenishment in SAP RPM

Based on a lot size and a minimum reorder point quantity you create an order in S/4HANA through SAP RPM. In this case, you will create a replenishment purchase order towards the customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log on. | Log on to the SAP RPM launchpad as a Packaging Manager. | The SAP Fiori Launchpad opens. |
| 2 | Access the SAP Fiori application. | Choose the Manage Returnable Packaging Accounts (F5126) app. | The Manage Returnable Packaging Accounts app is displayed. |
| 3 | Search for packaging account | Search packaging accounts using different criteria. Choose Adapt Filters and all filter possibilities display. Enter the entries accordingly, then choose Go.ExampleMaterial: RPM_PAL_001Exchange Partner: 33104091Choose the row of the required posting document to view its details. | The relevant packaging account shows. |
| 4 | Check the replenishment conditions for the purchase order. | In the packaging account, go to the Replenishment section. Make sure you have maintained the minimum reorder point quantity and a rounding value.Note Make sure the reorder quantity is higher than the account balance of the packaging account. If this is not the case the replenishment is not required for the packaging account. | Replenishment conditions are set up in the way, the replenishment can be executed. |
| 5 | Create replenishment. | Choose Create Replenishment. | In the Replenishment section under Last Replenishment, find the created PO and note it down. |

#### Post Goods Receipt

Based on the replenishment, an order is created in SAP S/4HANA. The GR posting will be conducted through Post Goods Movement app.

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log on. | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori Launchpad opens. |
| 2 | Access the SAP Fiori application | Choose the Post Goods Movement (MIGO) app. | The Post Goods Movement (MIGO) screen is displayed. |
| 3 | Screen settings. | In the upper area, enter the following data and choose Enter.First Box: Goods ReceiptSecond Box: Purchase OrderEnter: PO Number that was created in previous stepMovement Type: 101Choose Execute. | The purchase order with the material, the customer and the lot size of the packaging account appears. |
| 4 | Post goods receipt. | Choose Post. | The packaging is posted on stock.Note The created material document is replicated to SAP RPM and create a posting document which triggers the postings in the packaging accounts. |

Note down the material document number for later use.

#### One Step Stock Transfer

This process step shows you how to transfer stock from one storage location to another. Once an empty is used for packaging it should be reflected as being used. This can be done by distinguishing between two storage locations. One showing empty returnable packaging and one showing full returnable packaging.

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log on. | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori Launchpad opens. |
| 2 | Access the SAP Fiori application | Choose the Transfer Stock - In-Plant (F1061) app. | The Transfer Stock (F1061) screen is displayed. |
| 3 | Open stock overview. | Enter the following data in the appropriate fields:Plant: 3310Material: RPM_PAL_001 | Entries are made. |
| 4 | Select transfer from stock. | Select the icon beside the unrestricted stock in storage location that you want to transfer from, for example, 331A. | The icons change. |
| 5 | Select transfer to stock. | Select the icon beside the unrestricted stock in storage location that you want to transfer to, for example, 331B. | A dialog box opens. Storage Locations and Stock Types are selected according to your entries in the previous steps. |
| 6 | Transfer stock. | Enter the quantity that you want to transfer:Quantity: x PC |  |
| 7 | Post | Choose Post. | The system displays the Material document xxx created message.The stock is transferred from one storage location to another. |

### Process with Supplier

#### Post Goods Receipt

Based on the replenishment an order was created in SAP S/4HANA. The GR posting will be conducted through Post Goods Movement app.

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log on. | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori Launchpad opens. |
| 2 | Access the SAP Fiori application | Choose the Post Goods Movement (MIGO) app. | The Post Goods Movement (MIGO) screen is displayed. |
| 3 | Screen settings. | In the upper area, enter the following data and choose Enter.First Box: Goods ReceiptSecond Box: OtherMovement Type: 501Choose Execute. | Entries are made. |
| 4 | Enter material data. | Enter the following data and choose Enter.Material: RPM_PAL_001 | Entries are made. |
| 5 | Enter quantity. |  |  |
| 6 | Enter organization data. | Enter the following data on the Where tab and choose Enter.Movement Type: 501Plant: 3310Storage Location: 331ACheckbox Item OK: select |  |
| 7 | Post goods issue. | Choose Post. | The goods are posted to stock and available for use.Note The created material document is replicated to SAP RPM and create a posting document which triggers the postings in the packaging accounts. |

Note down the material document number for later use.

#### Create Outbound Delivery without Order Reference

This step can be used if the supplier orders returnables back through email.

Prerequisites

You can only return pallets if the customer owns enough of them.

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log on. | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori Launchpad opens. |
| 2 | Access the SAP Fiori application. | Choose the Create Outbound Delivery - Without Order Reference (VL01NO) app. | The Create Outbound Delivery - Without Order Reference (VL01NO) screen opens. |
| 3 | Enter shipping point. | Make the following entries and choose Enter.Shipping Point: <Shipping Point>, for example, 3310Delivery Type: LOSales Organization: <Sales Organization>, for example, 3310Distribution channel: <Distribution Channel>, for example, 10Division: <Division>, for example, 00 | The Delivery without Reference Create: Overview screen is displayed. |
| 4 | Enter delivery details. | Make the following entries and choose Enter.Ship-to party: <Ship-to party>, for example, 33104091Planned GI: <today's date>Material : <Material Number>, for example, RPM_PAL_001Delivery Quantity: <Quantity to be returned>, for example, 1Plant: 3310SLoc: 331B | Choose Enter for the warning that might come up: Division for material RPM_PAL_001 is different from specified division 00Choose Continue for the message: Result of item scheduling is goods issue date. |
| 5 | Post goods receipt. | Choose Save to save the outbound delivery. | Delivery is created. Delivery number displays in the Deliveries tab. |

|  |
| --- |
| Note Note down the delivery number for later use. |

#### Post Goods Issue

This process step shows you how to post goods issues for delivery.

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log on. | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori Launchpad opens. |
| 2 | Access the SAP Fiori application | Choose the Change Outbound Delivery (VL02N) app. | The Change Outbound Delivery (VL02N) screen is displayed. |
| 3 | Change outbound delivery | Make the following entry and choose Continue.Outbound Delivery: delivery number created previously | The Delivery XXX Change: Overview screen displays. |
| 4 | Execute picking | Select the Picking tab.Picked Qty (TG11 and RPM_PAL_001): Copy qty from the Delivery Quantity field.SLoc: 331B (empty returnables) |  |
| 5 | Post good issue. | Choose Post Goods Issues. | The goods issue is posted.Note The created material document is replicated to SAP RPM and the system creates a posting document, which triggers the postings in the packaging accounts. |

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
> Flagged while digesting this document, not verified: The prerequisites state material masters are to be created for both US (1710) and DE (1010) plants, while all sample data and steps in the script use plant 3310 (Plant 1 AE).

## Connections
- part-of :: [[_cluster]]
- related-to :: [[08-sales-order-management/test-script-returnables-processing-bdw-ae-sap-s-4hana-cloud-public-edi]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7HO_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 44,322 chars in the whole document
