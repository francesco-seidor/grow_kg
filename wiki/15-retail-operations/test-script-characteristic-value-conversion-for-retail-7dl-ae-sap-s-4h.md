---
id: 15-retail-operations/test-script-characteristic-value-conversion-for-retail-7dl-ae-sap-s-4h
title: "Test Script: Characteristic Value Conversion for Retail (7DL_AE) - SAP S/4HANA Cloud Public Edition (7DL_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 7DL_AE: converting article characteristic values across sales, purchase and STO documents."
cluster: 15-retail-operations
tags: [kb/retail-operations, topic/retail-articles-and-merchandise-categories]
aliases: [7DL_S4CLD2608_BPD_EN_AE]
keywords: ["Retail Articles, Merchandise Categories and Seasons", characteristic value conversion, conversion types, conversion values maintenance, sales order processing, outbound delivery, purchase order processing, inbound delivery, stock transfer order, billing documents]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7DL_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1209
topic: 15-retail-operations/retail-articles-and-merchandise-categories
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Characteristic Value Conversion for Retail (7DL_AE) - SAP S/4HANA Cloud Public Edition (7DL_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7DL_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Retail Articles, Merchandise Categories and Seasons** in Retail Operations. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Characteristic Value Conversion for Retail (7DL_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232860012)

[2 Prerequisites 4](#_Toc232860013)

[2.1 System Access 4](#_Toc232860014)

[2.2 Roles 4](#_Toc232860015)

[2.3 Master Data, Organizational Data, and Other Data 6](#_Toc232860016)

[2.4 Business Conditions 7](#_Toc232860017)

[2.5 Preliminary Steps 7](#_Toc232860018)

[2.5.1 Define Conversion Types 7](#_Toc232860019)

[2.5.2 Set Initial Stock for Material (Optional) 8](#_Toc232860020)

[3 Overview Table 10](#_Toc232860021)

[4 Test Procedures 13](#_Toc232860022)

[4.1 Characteristic Value Conversion 13](#_Toc232860023)

[4.1.1 Maintain Conversion Values 13](#_Toc232860024)

[4.2 Sales Document Processing 15](#_Toc232860025)

[4.2.1 Sales Order Processing 15](#_Toc232860026)

[4.2.1.1 Create Sales Order 15](#_Toc232860027)

[4.2.1.2 Create an Outbound Delivery 16](#_Toc232860028)

[4.2.1.3 Display Delivery Document using Display Outbound Delivery Application (Optional) 18](#_Toc232860029)

[4.2.1.4 Process Picking for Outbound Delivery 19](#_Toc232860030)

[4.2.1.5 Post Goods Issue for Outbound Delivery 20](#_Toc232860031)

[4.2.1.6 Create Billing Document with Reference to Outbound Delivery 21](#_Toc232860032)

[4.2.1.7 Display Billing Document (Optional) 22](#_Toc232860033)

[4.3 Purchase Document Processing 23](#_Toc232860034)

[4.3.1 Purchase Order Processing 23](#_Toc232860035)

[4.3.1.1 Create Purchase Order 23](#_Toc232860036)

[4.3.1.2 Display Purchase Order (Optional) 25](#_Toc232860037)

[4.3.1.3 Create Inbound Delivery 26](#_Toc232860038)

[4.3.1.4 Display Inbound Delivery Document (Optional) 27](#_Toc232860039)

[4.3.1.5 Confirm Quantities for Putaway 28](#_Toc232860040)

[4.3.1.6 Post Goods Receipt for Inbound Delivery 29](#_Toc232860041)

[4.3.1.7 Create Supplier Invoice using Purchase Order 30](#_Toc232860042)

[4.3.1.8 Display Supplier Invoice 32](#_Toc232860043)

[4.3.2 Stock Transfer Order Processing 33](#_Toc232860044)

[4.3.2.1 Create Stock Transfer Order 33](#_Toc232860045)

[4.3.2.2 Display Stock Transfer Order (Optional) 35](#_Toc232860046)

[4.3.2.3 Create Replenishment Delivery for Stock Transfer Order 35](#_Toc232860047)

[4.3.2.4 Display Outbound Delivery Document (Optional) 37](#_Toc232860048)

[4.3.2.5 Pick, Pack, and Post Goods Issue for Delivery 37](#_Toc232860049)

[5 Appendix 39](#_Toc232860050)

[5.1 Optional Scenarios 39](#_Toc232860051)

[5.1.1 Validate Conversion Values for Articles in the Stock Overview Application 39](#_Toc232860052)

## Purpose

Overview

In the retail and fashion industries, a characteristic of a product can be measured using different standards or scales in different countries or geographical regions. For example, a shoe that is considered size 9 in the UK may be a size 11 in the US. Hence, the shoe has both the sizes marked on it. To facilitate this, a characteristic conversion mechanism is necessary to ensure that on every product, sizes in all relevant size standards are correctly marked.

Characteristic value conversion only applies to variant-creating characteristics that are attached to the article master.

Characteristic

Characteristics refer to properties of an article such as the color of a shirt or the size of a shirt. The variant-creating characteristics are used to create variants of the generic product. The non-variant-creating characteristics are for information purposes only.

Characteristic Values

Characteristic values are the attributes of a characteristic. For example, if the characteristic is color, the characteristic values can be red, blue, or yellow. Characteristics can be valuated differently for each individual article. For example, an article with the characteristic color can receive the value red and another article can receive the value blue.

The system converts the characteristic values based on the conversion defined for the article. The system converts the characteristic value for selected items in the document or for the entire document.

Characteristic value conversion can be carried out in documents such as sales orders, purchase orders, and so on.

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
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Products / Product Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |
| Purchaser (Retail) | SAP_BR_PURCHASER_RFM | Retail Purchasing / Retail Sourcing and Contracting | SAP_RFM_SPT_PURCHASING_PC / SAP_RFM_SPT_SOURCING_PC |  |
| Receiving Specialist | SAP_BR_RECEIVING_SPECIALIST | Receiving | SAP_BR_RECEIVING_SPECIALIST |  |
| Order Fulfillment Manager | SAP_BR_ORDER_FULFILLMNT_MNGR | Order Fulfillment Management | SAP_BR_ORDER_FULFILLMNT_MNGR |  |
| Retail Store Associate | SAP_BR_RFM_STORE_ASSOCIATE | Store Operations | SAP_BR_RFM_STORE_ASSOCIATE |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Assortment Specialist - Retail | SAP_BR_ASSTMT_SPCLST_RFM | Assortments | SAP_RFM_SPT_ASSTMT_PC |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Customer Master | 33113007 | Wholesale non-Food AE |  |
| Generic Product | R_1080 | Cycling Jersey Longsleeve |  |
| Product Variant | R_1080001 | Cycling Jersey Longsleeve, S, BLACK |  |
| Sales Organization | 3310 | Dom. Sales Org |  |
| Distribution Channel | 10 | Direct Sales |  |
| Division | 00 | Product Division 00 |  |
| Sold-to Party/ Ship-to Party/Payer | 33113007 | Wholesale non-Food AE |  |
| Distribution Center (Site) | 3350 | DC 3350 AE |  |
| Storage Location | 995A | Storage Loc. DC |  |
| Shipping Point | 3350 | SP DC 3350 |  |
| Supplier | 33213004 | Retail Textile Supplier AE |  |
| Supplier | 33213001 | Retail Non-Food Supplier AE |  |
| Plant (Site or Location) for STO | 3340 | Store 3340 AE |  |
| Storage Location | 994A | St.Loc.Neg.Stock |  |
| Characteristic for Conversion | R_SIZE_STANDARD | Size Standard |  |

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 5FJ - Product Taxonomies for Retail | Characteristics and characteristic values must be created before assigning them to articles. |
| 3I1 - Products for Retail | Products must be created using the characteristic values created using 5FJ. |
| 3I4 - Sales Pricing for Retail | Sales price must be created for generic articles and variant articles if they do not already exist. |

### Preliminary Steps

#### Define Conversion Types

Purpose

You use this configuration activity to define the conversion types and then the variant value conversion. You create a connection based on a conversion type, between the variant values and the conversion values when you create the line item and variant entries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Project Experience in SAP Central Business Configuration. |  |  |
| 2 | Open Business Processes Configuration | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Conversion Types (106744).Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Conversion Types screen is displayed. |  |
| 3 | Define Conversion Types | Choose New Entries.Enter Conv. Type and Text. |  |  |
| 4 | Save the Configuration | Choose Save. | The configuration is saved. |  |

Result

You have defined the conversion types.

#### Set Initial Stock for Material (Optional)

Use

To execute this scope item, the materials must be available in stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk (Retail). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Post Goods Movement (MIGO) app. | The Goods Receipt Other screen is displayed. |  |
| 3 | Input Movement Type | Select the following entries:Executable Action in Transaction MIGO: Goods ReceiptReference Document for MIGO Transaction: Other |  |  |
| 4 | Enter Material | On the Material tab, make the following entry and press Enter:Material: R_1080 | The article is displayed in the General section table. |  |
| 5 | Enter Quantity Data | On the Goods Receipt Other screen: Quantity tab, make the following entries and press Enter:Qty in Unit of Entry: <Quantity in UOM>Unit of Entry: <UoM of material> |  |  |
| 6 | Input on the Goods Receipt Other screen: Where tab | On the Goods Receipt Other screen: Where tab, make the following entries and press Enter:Movement Type: 561 Receipt per initial entry of stock balances into unrestricted usePlant: 3350Storage Location: 995ANote If generic article is entered as the material then you should enter quantity in the variant matrix grid which appears on expanding the tree display for the material.Else, enter the variant article as the material for which stock needs to be created as generic articles are logical entities which are not entitled for physical stocks creation. |  |  |
| 7 | Save Entries | Select Post. | Material document <document number> posted success message is displayed. |  |

Result

You have created stock for the materials.

## Overview Table

This scope item consists of several process steps that are listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Characteristic Value Conversion

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Maintain Conversion Values](#unique_10) [page ] 13 | Master Data Specialist - Product Data (Retail) | Maintain Characteristic Values (WRFCHVAL) | Conversion value is created for a characteristic value |

Sales Document Processing

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Sales Order](#unique_11) [page ] 15 | Internal Sales Representative | Create Sales Orders - VA01 (VA01) | Sales order is created with items as per user specified conversion type |
| [Create an Outbound Delivery](#unique_12) [page ] 16 | Shipping Specialist | Create Outbound Deliveries (F0869A) | Outbound delivery is created with items as per user specified conversion type |
| [Display Delivery Document using Display Outbound Delivery Application (Optional)](#unique_13) [page ] 18 | Shipping Specialist | Display Outbound Delivery (VL03N) | Outbound delivery is displayed with items as per user specified conversion type using the Display Outbound Delivery (VL03N) application |
| [Process Picking for Outbound Delivery](#unique_14) [page ] 19 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Picking is performed on the outbound delivery. |
| [Post Goods Issue for Outbound Delivery](#unique_15) [page ] 20 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Goods issue is performed on the outbound delivery. |
| [Create Billing Document with Reference to Outbound Delivery](#unique_16) [page ] 21 | Billing Clerk | Create Billing Documents (F0798) | Billing document is created with items as per user specified conversion type |
| [Display Billing Document (Optional)](#unique_17) [page ] 22 | Billing Clerk | Manage Billing Document (F2250) | Billing document is displayed with items as per user specified conversion type |

Purchase Document Processing

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Purchase Order](#unique_18) [page ] 23 | Purchaser | Create Purchase Order - Advanced (ME21N) | Purchase order is created with items as per user specified conversion type |
| [Display Purchase Order (Optional)](#unique_19) [page ] 25 | Purchaser | Display Purchase Order - Advanced (ME23N) | Purchase order is displayed with items as per user specified conversion type |
| [Create Inbound Delivery](#unique_20) [page ] 26 | Receiving Specialist | Create Inbound Delivery (VL31N) | Inbound delivery is created with items as per user specified conversion type |
| [Display Inbound Delivery Document (Optional)](#unique_21) [page ] 27 | Receiving Specialist | Display Inbound Delivery (VL33N) | Inbound delivery is displayed with items as per user specified conversion type using the Display Inbound Delivery (VL33N) application |
| [Confirm Quantities for Putaway](#unique_22) [page ] 28 | Receiving Specialist | Change Inbound Delivery (VL32N) | Inbound Delivery document is updated with confirmed putaway quantities |
| [Post Goods Receipt for Inbound Delivery](#unique_23) [page ] 29 | Warehouse Clerk | Post Goods Movement (MIGO) | Goods receipt is posted for the inbound delivery when goods arrive at the disribution centre |
| [Create Supplier Invoice using Purchase Order](#unique_24) [page ] 30 | Accounts Payable Accountant | Create Supplier Invoice - Advanced (MIRO) | Invoice is generated. |
| [Display Supplier Invoice](#unique_25) [page ] 32 | Accounts Payable Accountant | Display Supplier Invoice - Advanced (MIR4) | Invoice and follow-on documents are displayed. |

Stock Transfer Order Document Processing

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Stock Transfer Order](#unique_26) [page ] 33 | Purchaser | Create Purchase Order - Advanced (ME21N) | Stock transfer order is created with items as per user specified conversion type |
| [Display Stock Transfer Order (Optional)](#unique_27) [page ] 35 | Purchaser | Display Purchase Order - Advanced (ME23N) | Stock transfer order is displayed with items as per user specified conversion type |
| [Create Replenishment Delivery for Stock Transfer Order](#unique_28) [page ] 35 | Shipping Specialist | My Purchase Orders - Due for Delivery (VL10B) | Outbound delivery document with reference to stock transport order is created |
| [Display Outbound Delivery Document (Optional)](#unique_29) [page ] 37 | Shipping Specialist | Change Outbound Delivery (VL02N) | Outbound delivery is displayed with items as per user specified conversion type |
| [Pick, Pack, and Post Goods Issue for Delivery](#unique_30) [page ] 37 | Shipping Specialist | Change Outbound Delivery (VL02N) | Outbound delivery document is saved with the updated picked quantity. Goods issue is posted for this outbound delivery |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

|  |
| --- |
| Remember For the currently supported document types, the converted characteristic value is not saved or persisted when the base value of a characteristic undergoes conversion process. Only the base values of the characteristics are persisted. |

### Characteristic Value Conversion

#### Maintain Conversion Values

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this process step, you can maintain conversion values for the already created characteristic values (base values) of a characteristic.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Product Data (Retail). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Maintain Characteristic Values (WRFCHVAL) app. | The Edit Characteristic Values screen is displayed. |  |
| 3 | Display Characteristic Values | Enter the characteristic, for example, R_SIZE_STANDARD.Press ENTER. | Characteristic values (base values) for the characteristic are displayed.In addition, the characteristic type and the check option values are also displayed for the characteristic.Note The characteristic type helps to display the characteristic values in the corresponding characteristic columns of the various process- related applications.For example, if the characteristic type is maintained as Characteristic 2 for a characteristic, only the Characteristic 2 and Char Desc. 2 columns display the corresponding characteristic value. |  |
| 4 | Maintain Conversion Values for Characteristic Values | Choose Characteristic Value Conversion.On the Maintain Characteristic Conversion Values screen, choose Insert Row.Enter the following values:Characteristic Value: <Characteristic Value> (Press F4 to select a characteristic (base) value of the characteristic)Conversion Type: <Conversion type> (Press F4 to select a conversion type as created in [Define Conversion Types](#unique_7) [page ] 7)Conversion Value: <Conversion Value>Conversion Value Text: <Conversion Value Text>Choose Save. | Conversion value for the entered characteristic value is created. |  |
| 5 | Save Your Entries | Choose Save. | The characteristic is saved with the conversion value for the entered characteristic value. |  |

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
| 4 | Enter Data | In the header section, enter:Sold-to Party: 33113007Ship-to Party: 33113007In the All Items table, enter the following details:Material: R_1080 or R_1080001Order Quantity: <Order quantity in piece (PC)>Plant: 3350Press ENTER. | For generic product R_1080, a variant matrix screen is displayed where you must enter the order quantity for the required variants. When you navigate back to the Create Standard Order: Overview screen, the corresponding characteristic (base) values of the variants for which the ordered quantities were entered are displayed.For product variant R_1080001, the characteristic (base) values are displayed by default.NoteThe base values are displayed in the Characteristic 1, Char Desc.1 and/or Characteristic 2, Char Desc. 2 and/or Characteristic 3, Char Desc. 3 columns depending on the characteristic type maintained for the characteristic.In case you have entered an order quantity for the generic material in the Create Standard Order: Overview screen, you must maintain the same quantity in the variant matrix. This means that the sum of the order quantities of the variants must correspond to the order quantity entered for the generic product. |  |
| 5 | Display Conversion Values | Choose the Base Values button.Choose a conversion type. | The conversion values are displayed in the corresponding characteristic columns replacing the existing characteristic value (base value).The button text is replaced by the conversion type.Note The converted characteristic values are displayed directly when a variant is entered with the button text which still shows the conversion type.These converted values are for display purposes only and cannot be used during document processing. |  |
| 6 | Save Order | Choose Save. | Sales order is saved. A success message is displayed. |  |

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
| 3 | Display Delivery | In the Outbound Delivery field, enter Delivery and choose Continue. | Overview of delivery document is displayed.The characteristic value (base value) corresponding to the articles are displayed in the Characteristic 1, Char Desc.1 and/or Characteristic 2, Char Desc. 2 and/or Characteristic 3, Char Desc. 3 columns depending on the characteristic type maintained for the characteristic. |  |
| 4 | Display Conversion Value | Choose the Base Values button.Choose a conversion type. | The conversion values are displayed in the corresponding characteristic columns replacing the existing characteristic value (base value). |  |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD) app. | The Manage Outbound Deliveries - VL06O (VL06O_CLOUD) screen is displayed. |  |
| 3 | Select Picking | Select For Picking. |  |  |
| 4 | Enter Shipping Point | Make the following entries and select Execute: Under Organizat. Data section, select:Shipping Point: 3350Under the Picking Data section, selectOnly Picking Without WM: X | The Day’s Workload for Picking screen is displayed. |  |
| 5 | Change Outbound Deliveries | On the Day’s Workload for Picking, select <your delivery number> and select Change Outbound Deliveries. | The Outbound Delivery xxx Change: Overview screen is displayed.Overview of the delivery document is displayed.The characteristic value (base value) corresponding to the articles are displayed in the Characteristic 1, Char Desc.1 and/or Characteristic 2, Char Desc. 2 and/or Characteristic 3, Char Desc. 3 columns depending on the characteristic type maintained for the characteristic. |  |
| 6 | Display Conversion Values | Select Item Overview tab.Choose the Base Values button. | The conversion values are displayed in the corresponding characteristic columns replacing the existing characteristic value (base value). |  |
| 7 | Check Batch Split | Select Picking tab. |  |  |
| 8 | Enter Picked Quantity | Enter <quantity equal to delivery Qty> in Picked Qty field for picking related item(s).Press Enter. |  |  |
| 9 | Select Save | Choose Save. | A message Outbound Delivery xxx has been saved is displayed. |  |

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
| 3 | Display Billing Document | Enter the Billing Document .Choose Continue. | Billing document is displayed.The characteristic value (base value) corresponding to the articles are displayed in the Characteristic 1, Char Desc.1 and/or Characteristic 2, Char Desc. 2 and/or Characteristic 3, Char Desc. 3 columns depending on the characteristic type maintained for the characteristic. |  |
| 4 | Display Conversion Values | Choose the Base Values button.Choose a conversion type. | The conversion values are displayed in the corresponding characteristic columns replacing the existing characteristic value (base value). |  |

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

With this process step, you can create a purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Purchaser (Retail). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Create Purchase Order - Advanced (ME21N) app. | The Create Purchase Order - Advanced (ME21N) screen is displayed.Standard filters and buttons are displayed. |  |
| 3 | Enter Purchase Order Data | Enter the following data and press Enter:Order type: Standard PO or NB Standard POSupplier: 33213004In Header section, on the Org. Data tab:Purch. Org.:3310Purch. Group:001Company Code:3310In Item Overview section:Material:R_1080 or R_1080001Plant:3350Storage Location:995AQuantity:<Enter a quantity>Net Price:xxxNote Price should be determined automatically from purchasing info record.On the Confirmations tab under the Item Detail section:Conf. Control:Inbound Delivery | For generic product R_1080, a variant matrix screen is displayed where you must enter the order quantity for the required variants. The variants for which the quantity is entered is then displayed in the Item Overview section. The corresponding characteristic (base) value of the articles are displayed.For product variant R_1080001, the corresponding characteristic (base) value of the articles are displayed by default.NoteThe base values are displayed in the Characteristic 1, Char Desc.1 and/or Characteristic 2, Char Desc. 2 and/or Characteristic 3, Char Desc. 3 columns depending on the characteristic type maintained for the characteristic.In case you have entered an order quantity for the generic product in the Item Overview section, you must maintain the same quantity in the variant matrix. This means that the sum of the order quantities of the variants must correspond to the order quantity entered for the generic product. |  |
| 4 | Display Conversion Values | Choose the Base Values button from the top.Choose a conversion type. | The conversion values are displayed in the corresponding characteristic columns replacing the existing characteristic value (base value).The button text is replaced by the conversion type.Note The converted characteristic values are displayed directly when a variant is entered with the button text which still shows the conversion type.These converted values are for display purposes only and cannot be used during document processing. |  |
| 5 | Save Purchase Order | Choose Save. | A new purchase order is created.Purchase order number is displayed.Note down the purchase order number for future use. |  |

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
| 1 | Log On | Log on to the SAP Fiori Launchpad using the Purchaser (Retail) role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Display Purchase Order - Advanced (ME23N). | The Display Purchase Order screen is displayed. |  |
| 3 | Display Purchase Order | Choose Other Purchase Order.Enter the purchase order number and choose Other Document. | The purchase order is displayed.The characteristic value (base value) corresponding to the articles are displayed in the Characteristic 1, Char Desc.1 and/or Characteristic 2, Char Desc. 2 and/or Characteristic 3, Char Desc. 3 columns depending on the characteristic type maintained for the characteristic. |  |
| 4 | Display Conversion Value | Choose the Base Values button.Choose a conversion type. | The conversion values are displayed in the corresponding characteristic columns replacing the existing characteristic value (base value). |  |

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
| 3 | Start Selection for Inbound Delivery Creation | On the Create Inbound Delivery (VL31N) app screen, enter the following:Supplier: 33213004Purchase Order:<your Purchase Order document number>Choose Continue. | The purchase order details are displayed.The characteristic value (base value) corresponding to the articles are displayed in the Characteristic 1, Char Desc.1 and/or Characteristic 2, Char Desc. 2 and/or Characteristic 3, Char Desc. 3 columns depending on the characteristic type maintained for the characteristic. |  |
| 4 | Display Conversion Value | Choose the Base Values button.Choose conversion type. | The conversion values are displayed in the corresponding characteristic columns replacing the existing characteristic value (base value).These converted values are for display purposes only and cannot be used during document processing. |  |
| 5 | Save Inbound Delivery Document | Choose Save. | Inbound delivery document is created. |  |

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
| 3 | Display Delivery | In the Inbound Delivery field, enter the recently created inbound delivery document number and choose Continue. | Overview of delivery document is displayed.The characteristic value (base value) corresponding to the articles are displayed in the Characteristic 1, Char Desc.1 and/or Characteristic 2, Char Desc. 2 and/or Characteristic 3, Char Desc. 3 columns depending on the characteristic type maintained for the characteristic. |  |
| 4 | Display Conversion Value | Choose the Base Values button.Choose a conversion type. | The conversion values are displayed in the corresponding characteristic columns replacing the existing characteristic value (base value). |  |

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
| 3 | Enter Inbound Delivery Number | Enter the following values:Select Goods Receipt and Inbound Delivery from the dropdown and enter the following:Inbound Delivery Number: XXXGoods Movement Type: 101Press Enter. | The inbound delivery is displayed.The characteristic value (base value) corresponding to the articles are displayed in the Characteristic 1, Char Desc.1 and/or Characteristic 2, Char Desc. 2 and/or Characteristic 3, Char Desc. 3 columns depending on the characteristic type maintained for the characteristic. |  |
| 4 | Display Conversion Value | Select a line item.Choose the Base Values button.Choose conversion type. | The conversion values are displayed in the corresponding characteristic columns replacing the existing characteristic value (base value).These converted values are for display purposes only and cannot be used during document processing. |  |
| 5 | Check and Post the Goods Receipt for Inbound Delivery | In the Detail data section, select the Item OK checkbox.Choose Check to validate the entries.Choose Post. | The goods receipt is posted.Message Material Document <Document number> posted. is displayed. |  |

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
| 2 | Access App | Open Create Supplier Invoice - Advanced (MIRO) app. |  |  |
| 3 | Navigate to Enter Incoming Invoice Screen | In the pop-up, enter Company Code as 3310Choose Continue. | The Enter Incoming Invoice: Company Code 3310 screen is displayed. |  |
| 4 | Provide Invoice Details | Navigate to Basic Data tab and enter the values for the following fields:Invoice Date: <enter date>Reference: <enter reference>Amount: <enter amount> (Total value you had noted down while creating purchase order. You can check this value under Item Details > Conditions > Total Value )Tax Code: <enter tax code> (Tax code you have noted down in purchase order. You can check this value under Item Details > Invoice > Tax Code )Tax Amount: <enter tax amount> (Tax amount you had noted down while creating purchase order. You can check this value under Item Details > Conditions > TTX1 > Tax )Under the Details tab, select the corresponding document type in the Doc. Types field.Navigate to PO Reference tab and enter values for the following fields:Ref Document category: Purchase Order/Scheduling AgreementPurchasing Document: <enter purchase order number>Item type: Goods/service itemsPress Enter. | The purchase order reference details are displayed.The characteristic value (base value) corresponding to the articles are displayed in the Characteristic 1, Char Desc.1 and/or Characteristic 2, Char Desc. 2 and/or Characteristic 3, Char Desc. 3 columns depending on the characteristic type maintained for the characteristic. |  |
| 5 | Display Conversion Value | From the top, choose the Base Values button.Choose conversion type. | The conversion values are displayed in the corresponding characteristic columns replacing the existing characteristic value (base value).These converted values are for display purposes only and cannot be used during document processing. |  |
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
| 2 | Access App | Open Display Supplier Invoice - Advanced (MIR4) app. | The Display Invoice Document screen is displayed. |  |
| 3 | Provide Invoice Details | Enter the following values:Invoice Document No.:< Enter invoice document number >Fiscal Year:<Enter year>Choose Display Document. | Invoice details are displayed.The characteristic value (base value) corresponding to the articles are displayed in the Characteristic 1, Char Desc.1 and/or Characteristic 2, Char Desc. 2 and/or Characteristic 3, Char Desc. 3 columns depending on the characteristic type maintained for the characteristic. |  |
| 4 | Display Conversion Value | Choose the Base Values button.Choose a conversion type. | The conversion values are displayed in the corresponding characteristic columns replacing the existing characteristic value (base value). |  |
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

With this process step, you can create a stock transfer order (STO).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser (Retail). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Create Purchase Order (ME21N) app. | Create Purchase Order (ME21N) app screen is displayed. |  |
| 3 | Enter Stock Transfer Order Data | Enter the following data, then press Enter:Order Type: StockTranspOrderDel or UD StockTranspOrderDelSupplying Plant: 3350In the Org. Data tab of the Header section:Company Code: 3310Purchasing Org.: 3310Purchasing Group: 001In the Item Overview section:Material: R_1080 or R_1080001Plant: 3340Storage Location: 994APO Quantity: x | For generic product R_1080, a variant matrix screen is displayed where you must enter the order quantity for the required variants. The variants for which the quantity is entered is then displayed in the Item Overview section. The corresponding characteristic (base) value of the articles are displayed.For product variant R_1080001, the corresponding characteristic (base) value of the articles are displayed by default.NoteThe base values are displayed in the Characteristic 1, Char Desc.1 and/or Characteristic 2, Char Desc. 2 and/or Characteristic 3, Char Desc. 3 columns depending on the characteristic type maintained for the characteristic.In case you have entered an order quantity for the generic product in the Item Overview section, you must maintain the same quantity in the variant matrix. This means that the sum of the order quantities of the variants must correspond to the order quantity entered for the generic product. |  |
| 4 | Display Conversion Values | Choose the Base Values button from the top.Choose a conversion type. | The conversion values are displayed in the corresponding characteristic columns replacing the existing characteristic value (base value).The button text is replaced by the conversion type.Note The converted characteristic values are displayed directly when a variant is entered with the button text which still shows the conversion type.These converted values are for display purposes only and cannot be used during document processing. |  |
| 5 | Save Stock Transfer Order | Choose Save. | A new stock transfer order is created.Order number is displayed.Note down the order number for future use. |  |

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
| 1 | Log On | Log on to the SAP Fiori Launchpad using the Purchaser (Retail) role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Display Purchase Order - Advanced (ME23N). | The Display Purchase Order screen is displayed. |  |
| 3 | Display Stock Transfer Order | Choose Other Purchase Order.Enter the stock transport order number and choose Other Document. | The stock transfer order is displayed.The characteristic value (base value) corresponding to the articles are displayed in the Characteristic 1, Char Desc.1 and/or Characteristic 2, Char Desc. 2 and/or Characteristic 3, Char Desc. 3 columns depending on the characteristic type maintained for the characteristic. |  |
| 4 | Display Conversion Value | Choose the Base Values button.Choose a conversion type. | The conversion values are displayed in the corresponding characteristic columns replacing the existing characteristic value (base value). |  |

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
| 3 | Start Selection for Outbound Delivery Creation | On the entry screen of Purchase Orders, Fast Display screen, enter the following details:Remove Deliv. Creation Date (both from and to dates)Shipping point: 3350Go to Purchase Orders tab view and enter Purchasing Document: STO Document Number created in [Create Stock Transfer Order](#unique_26) [page ] 33.Choose Execute. | A list of purchasing documents for the selected shipping point is displayed in the Activities Due for Shipping "Purchase Orders, Fast Display" screen. |  |
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
| 3 | Display Delivery | In the Outbound Delivery field, enter the recently created outbound delivery document number and choose Continue. | Overview of delivery document is displayed.The characteristic value (base value) corresponding to the articles are displayed in the Characteristic 1, Char Desc.1 and/or Characteristic 2, Char Desc. 2 and/or Characteristic 3, Char Desc. 3 columns depending on the characteristic type maintained for the characteristic. |  |
| 4 | Display Conversion Value | Choose the Base Values button.Choose a conversion type. | The conversion values are displayed in the corresponding characteristic columns replacing the existing characteristic value (base value). |  |

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

#### Validate Conversion Values for Articles in the Stock Overview Application

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this process step, you can validate the conversion values for articles in the Display Advanced Stock Overview (RWBE) application.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk (Retail) | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Display Advanced Stock Overview (RWBE) application. | The Stock Overview screen is displayed. |  |
| 3 | Enter Parameters | Enter the following data:Material: R_1080Plant: 3350Choose Execute. | The Stock Overview: Full List screen is displayed. |  |
| 4 | Check Characteristic (Base) Values | Expand the material and navigate to the right. | The characteristic value (base value) corresponding to the articles are displayed in the Characteristic 1, Char Desc.1 and/or Characteristic 2, Char Desc. 2 and/or Characteristic 3, Char Desc. 3 columns depending on the characteristic type maintained for the characteristic. |  |
| 5 | Validate Conversion Values | From the top, choose the Set Conversion Type button.Choose a conversion type. | The conversion values are displayed in the corresponding characteristic columns replacing the existing characteristic value (base value). |  |

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
- related-to :: [[15-retail-operations/product-taxonomies-for-retail-5fj-ae-test-script-1079]]
- related-to :: [[15-retail-operations/products-for-retail-3i1-ae-test-script-sap-s-4hana-cloud-public-editio]]
- related-to :: [[15-retail-operations/test-script-seasons-for-retail-6di-ae-sap-s-4hana-cloud-public-edition]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7DL_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 68,190 chars in the whole document
