---
id: 15-retail-operations/sales-from-distribution-center-3hs-ae-test-script-sap-s-4hana-cloud-pu
title: "Sales from Distribution Center (3HS_AE) - Test Script, SAP S/4HANA Cloud Public Edition (3HS_S4CLD2608_BPD_EN_AE)"
description: "Test script for scope item 3HS_AE (UAE): sales from distribution center, debit memos, consignment, advanced intercompany sales; roles, apps, sample data, postings."
cluster: 15-retail-operations
tags: [kb/retail-operations, topic/sales-from-distribution-center]
aliases: [3HS_S4CLD2608_BPD_EN_AE]
keywords: [Sales from Distribution Centers, sales from distribution center, sales order processing, outbound delivery, picking and goods issue, billing documents, debit memos, consignment processing, consignment returns, advanced intercompany sales]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3HS_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-938
topic: 15-retail-operations/sales-from-distribution-center
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Sales from Distribution Center (3HS_AE) - Test Script, SAP S/4HANA Cloud Public Edition (3HS_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3HS_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Sales from Distribution Centers** in Retail Operations. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Sales from Distribution Center (3HS_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Sales from Distribution Center (3HS_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 4](#_Toc232852669)

[2 Prerequisites 5](#_Toc232852670)

[2.1 System Access 5](#_Toc232852671)

[2.2 Roles 5](#_Toc232852672)

[2.3 Master Data, Organizational Data, and Other Data 6](#_Toc232852673)

[2.4 Additional Manual Configuration 8](#_Toc232852674)

[2.5 Business Conditions 8](#_Toc232852675)

[2.6 Preliminary Steps 9](#_Toc232852676)

[2.6.1 Set Initial Stock for Material 9](#_Toc232852677)

[2.6.2 Preliminary Steps BRF+ Settings for Delivery Documents 10](#_Toc232852678)

[2.6.2.1 BRF+ Settings for Delivery Documents (Optional) 10](#_Toc232852679)

[3 Overview Table 11](#_Toc232852680)

[4 Test Procedures 15](#_Toc232852681)

[4.1 Create Sales Quotation 15](#_Toc232852682)

[4.2 Change Quotation Document (Optional) 16](#_Toc232852683)

[4.3 Create Sales Orders 17](#_Toc232852684)

[4.4 Create an Outbound Delivery 18](#_Toc232852685)

[4.5 Create Attachment for Delivery (Optional) 20](#_Toc232852686)

[4.6 Process Picking for Outbound Delivery 21](#_Toc232852687)

[4.7 Post Goods Issue for Outbound Delivery 22](#_Toc232852688)

[4.8 Create Billing Document 23](#_Toc232852689)

[4.9 Create Attachment for Billing Document (Optional) 24](#_Toc232852690)

[4.10 Create Debit Memo Request 25](#_Toc232852691)

[4.11 Create Attachment for Debit Memo Request (Optional) 27](#_Toc232852692)

[4.12 Remove Billing Block 28](#_Toc232852693)

[4.13 Create Debit Memo 29](#_Toc232852694)

[4.14 Consignment Fill-Up 30](#_Toc232852695)

[4.14.1 Create Consignment Fill-Up Order 30](#_Toc232852696)

[4.14.2 Create Outbound Delivery 31](#_Toc232852697)

[4.14.3 Process Picking for Outbound Delivery 32](#_Toc232852698)

[4.14.4 Post Goods Issue 33](#_Toc232852699)

[4.14.5 Check Stock Overview 34](#_Toc232852700)

[4.15 Consignment Issue 35](#_Toc232852701)

[4.15.1 Create Consignment Issue Order 35](#_Toc232852702)

[4.15.2 Create Outbound Delivery 36](#_Toc232852703)

[4.15.3 Post Goods Issue 37](#_Toc232852704)

[4.15.4 Check Stock Overview 38](#_Toc232852705)

[4.15.5 Create Customer Invoice 39](#_Toc232852706)

[4.16 Consignment Pick-Up 40](#_Toc232852707)

[4.16.1 Create Consignment Pick-Up Order 40](#_Toc232852708)

[4.16.2 Create Return Delivery 42](#_Toc232852709)

[4.16.3 Receive Returned Goods 42](#_Toc232852710)

[4.16.4 Post Goods Receipt 44](#_Toc232852711)

[4.16.5 Check Stock Overview 44](#_Toc232852712)

[4.17 Consignment Return 45](#_Toc232852713)

[4.17.1 Create Consignment Return Order 45](#_Toc232852714)

[4.17.2 Create Return Delivery 47](#_Toc232852715)

[4.17.3 Post Goods Receipt 47](#_Toc232852716)

[4.17.4 Check Stock Overview 48](#_Toc232852717)

[4.17.5 Release Consignment Return Order for Billing 49](#_Toc232852718)

[4.17.6 Create Credit Memo 50](#_Toc232852719)

[4.18 Advanced Intercompany Sales 52](#_Toc232852720)

[4.18.1 Create Sales Order 52](#_Toc232852721)

[4.18.2 Process Sales Order Approval (Optional) 56](#_Toc232852722)

[4.18.3 Create Pro Forma F5 Invoice (Optional) 56](#_Toc232852723)

[4.18.4 Create Delivery 57](#_Toc232852724)

[4.18.5 Perform Picking 58](#_Toc232852725)

[4.18.6 Post Goods Issue 59](#_Toc232852726)

[4.18.7 Confirm Transfer of Control Dates 61](#_Toc232852727)

[4.18.8 Create Pro Forma F8 Invoice (Optional) 63](#_Toc232852728)

[4.18.9 Create Intercompany Invoice 65](#_Toc232852729)

[4.18.10 Display Intercompany Supplier Invoice 66](#_Toc232852730)

[4.18.11 Create F2 Invoice 67](#_Toc232852731)

[4.18.12 Update Text in Billing Document (Optional) 69](#_Toc232852732)

[4.18.13 Monitor Intercompany Sales Value Chain 70](#_Toc232852733)

[4.18.13.1 Display Intercompany Sales Value Chain 70](#_Toc232852734)

[4.18.13.2 Display Intercompany Purchase Order 72](#_Toc232852735)

[4.18.13.3 Display Intercompany Sales Order 73](#_Toc232852736)

[4.18.13.4 Display Intercompany Supplier Invoice 74](#_Toc232852737)

[4.18.14 Schedule Resolution of Value Chain Issues (Optional) 75](#_Toc232852738)

[5 Appendix 78](#_Toc232852739)

[5.1 Scheduling Job (Alternative) 78](#_Toc232852740)

[5.1.1 Schedule Job for Creation of Outbound Delivery (Alternative) 78](#_Toc232852741)

[5.1.2 Schedule Job for Goods Issue Deliveries (Alternative) 79](#_Toc232852742)

[5.1.3 Schedule Job for Creation of Billing Documents (Alternative) 80](#_Toc232852743)

## Purpose

Overview

The process starts with the creation of a customer's standard sales order, or optionally with creation of a sales quotation. Depending on the customer and the article, various special activities are executed during the order entry, such as customer/article pricing, insertion of applicable discounts, or checking the availability of the articles. For fulfillment, an outbound delivery is created when the sales order is due. The shipping specialist picks the articles and enters the quantities in the outbound delivery. After picking is complete, the shipping specialist can post the goods issue and, as a result, inventory accounts are posted to in financial. Now, the delivery can be invoiced and the revenue posted to financial accounting. This step completes the sales from a logistic perspective. Finance covers the process of customer account clearing through payment. The debit/credit memo process is triggered if the customer is undercharged or overcharged (for example, because of a pricing or sales tax rate error).

This scope item also describes the process for standard customer consignment processing. The articles shipped to the customer are still owned by the retailer until they're sold by the customer to a third party. The articles, which are usually stored in the customer store or warehouse, are posted in a stock (consignment stock) that is assigned to the corresponding customer. This allows the current customer stock to be viewed at any time.

The process of intercompany sales is also supported. In this case, the sales originate in a sales area assigned to one company code. It's fulfilled from a distribution center belonging to a different company code. The supported process includes the respective intercompany billing.

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
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Warehouse Clerk (Retail) | SAP_BR_WAREHOUSE_CLERK_RFM | Retail Inventory Processing | SAP_BR_WAREHOUSE_CLERK_RFM |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |
| Pricing Specialist (Retail) | SAP_BR_PRICING_SPCLST_RFM | Retail PricingRetail Markups | SAP_BR_PRICING_SPCLST_RFM |  |
| Master Data Specialist - Location Data (Retail) | SAP_BR_MD_SPCLST_SITE_RFM | Retail Site Master | SAP_BR_MD_SPCLST_SITE_RFM |  |
| Master Data Specialist - Product Data (MDG) | SAP_BR_HOME_PRODHRY_SPECIALIST |  |  |  |
| Configuration Expert | SAP_BR_CONFIGURATION_EXPERT |  |  |  |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | General Ledger | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Returns and Refund Clerk | SAP_BR_RETURNS_REFUND_CLERK | Customer Returns | SAP_BR_RETURNS_REFUND_CLERK |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

Use your own master data or the following sample data to go through the test procedure.

|  |
| --- |
| Note In our example for advanced intercompany sales process, the Sales Organization 3310 is selling the product R_3018 to the domestic Customer 33113007 in United Arab Emirates. The goods are directly shipped to the customer from the plant 1750 in US (which is owned by the US Delivering Company 1710). Meanwhile, Stock in Transit that is owned by the Selling Company 3310 is assigned to the plant 3350 of the Selling Company 3310. The Delivering Sales Organization 1710 will create an intercompany invoice towards the Selling Company 3310, while the Customer’s Company 3310 will receive a supplier invoice from the Delivering Company 1710. |

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Intercompany Payer | 33403310 | In the US Delivering Company 1710’s view, this ID represents the Customer Company 3310 as a customer. It acts as the payer in both the sales order and the intercompany invoice in the US Delivering Company1710. |  |
| Intercompany Supplier | 17401710 | In the Customer Company 3310’s view, this ID represents the US Delivering Company 1710 as a vendor. It acts as the invoicing party in both the purchase order and the supplier invoice in the Customer Company 3310. |  |
| Intercompany Plant Customer | 3350 | DC 3350 AE |  |
| Intercompany Plant Supplier | 1750 | DC Newtown Square |  |
| Selling Company's Sales Organization | 3310 | Sales organization in selling company 3310 and is responsible for creating invoice to customer. |  |
| Delivering Company's Sales Organization | 1710 | Dom. Sales Org US |  |
| Customer | 33100002 | Domestic UAE Customer 2 |  |
| Article | R_3018 | Gas Grill 3-Burner Black |  |
| Single Article (Material or Product) | R_1006 | My Best Frozen Strawberries |  |
| Generic Article & Variant (Material or Product) | R_1003 & R_1003001 | Chocolate & Chocolate, Whole-Milk, Diet |  |
| Display Article (Material or Product) | R_2007 | Chocolate Bar Display |  |
| Sales set Article (Material or Product) | R_1052 | My Best Blond Shampoo & Conditioner |  |
| Sold-to Party/ Ship-to party/Payer | 3311300633113007 | Wholesale Food AEWholesale non-Food AE |  |
| Distribution Center (Site) | 3350 | DC 3350 AE |  |
| Storage Location | 995A | Storage Loc. DC |  |
| Storage Location | 995R | St.Loc.Return |  |
| Shipping Point | 1750 | SP DC 1750 |  |
| Shipping Point | 335C | SP DC 3350 Consignment |  |
| Shipping Point | 335R | SP DC 3350 Return |  |
| Sales Organization | 3310 | Dom. Sales Org |  |
| Distribution Channel | 10 | Direct Sales |  |
| Division | 00 | Product Division 00 |  |
| Product Group (Material Group or Merchandise Category) | R1193001 | Frozen Fruit |  |
| Product Group (Material Group or Merchandise Category) | R1202001 | Sweets |  |
| Product Group (Material Group or Merchandise Category) | R2121002 | Hair Care |  |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/1cfbf2a6e2c2a7b0612d1ec67ec6c4f7)

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 5FU - Inbound Logistics for Distribution Centers | To run through the scope of this scope, the material must be available in stock. If you use trading goods (HAWA) you can either:Run through the Inbound Logistics for Distribution Centers (5FU) test processes.or,Create stock using Post Goods Movement (MIGO) app. For more information, see Preliminary Steps. |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the process step described in the Create New Open MM Posting Period - MDS (BNZ) master data script. Posting period is up to date.Open new posting period in company codes 1710 and 3310 respectively. |
| 7DM - Advanced Intercompany Sales – Make-to-Order and Variant Config | You must activate this scope item if you use standalone variant article in advanced intercompany sales process. |

### Preliminary Steps

#### Set Initial Stock for Material

Use

To execute this scope item, the materials must be available in stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk (Retail). |  |  |
| 2 | Access the App | Open Post Goods Movement (MIGO) app.It only displays if it was your last transaction. So, the action for the user is to select Reference Document for MIGO Transaction > Other . | The Goods Receipt Other screen is displayed. |  |
| 3 | Input Movement Type | Make the following entries and select Enter.Executable Action in Transaction MIGO: Goods ReceiptReference Document for MIGO Transaction: Other |  |  |
| 4 | Enter Material | On the Goods Receipt Other Screen: Material tab, make the following entry and select Enter:Material: R_3018. |  |  |
| 5 | Enter Quantity Data | On the Goods Receipt Other screen: Quantity tab, make the following entry and select Enter:Qty in Unit of Entry: <Quantity in UOM>Unit of Entry: <UoM of material> |  |  |
| 6 | Input on the Goods Receipt Other screen: Where tab | On the Goods Receipt Other screen: Where tab, make the following entries and select Enter:Movement Type: 561Receipt per initial entry of stock balances into unrestricted usePlant: 3350Storage Location: 995A |  |  |
| 7 | Save Your Entries | Select Post. | Material document <document number> posted success message is displayed. |  |

|  |
| --- |
| Note For above procedure, if you use a material (article) of type:"Generic article" - enter quantity in the variant matrix grid which appears on expanding Tree display for the material after entering the required details. Generic articles are logical entities which are not entitled for physical stocks creation."Variant article" - enter variant article directly in the Material field.For various types of articles you can use in this scope item, refer to the list of retail articles mentioned in [Master Data, Organizational Data, and Other Data](#unique_5) [page ] 6. |

Result

You have created stock for the materials.

#### Preliminary Steps BRF+ Settings for Delivery Documents

##### BRF+ Settings for Delivery Documents (Optional)

Purpose

This process step shows you how to define the system determination of output parameters for printing a delivery document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Output Parameter Determination (APOC_WD_BRF_DEC_TAB_MAINTAIN). | The Output Parameter Determination screen displays. |  |
| 3 | Output Type | In the Select Business Rule section, make the following entries:Show Rules for: Outbound DeliveryDetermination Step: Form Template | Details are displayed in the Maintain Business Rules section. |  |
| 4 | Add Rules | Expand the Maintain Business Rules section. Choose Edit. In the Table Contents, choose Insert New Row and enter the following entries:Output Type: DELIVERY_NOTE | The relevant form is added.Insert after the line the last Sender Country mentioned in the list and insert before the lines with no Sender Country mentioned. |  |
| 5 | Activate | Choose Activate. | Rules are activated. |  |

## Overview Table

This scope item consists of several process step provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App | Expected Results |
| --- | --- | --- | --- |
| [Create Sales Quotation](#unique_11) [page ] 15 | Internal Sales Representative | Manage Sales Quotations (F1852) | Sales quotation is created |
| [Change Quotation Document (Optional)](#unique_12) [page ] 16 | Internal Sales Representative | Manage Sales Quotations (F1852) | Sales quotation is changed. |
| [Create Sales Orders](#unique_13) [page ] 17 | Internal Sales Representative | Create Sales Orders - VA01 (VA01) | Sales order is created. |
| [Create an Outbound Delivery](#unique_14) [page ] 18 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) | Delivery from sales order is created. |
| [Create Attachment for Delivery (Optional)](#unique_15) [page ] 20 | Shipping Specialist | Display Outbound Delivery (VL03N) | Attachment for delivery is created. |
| [Process Picking for Outbound Delivery](#unique_16) [page ] 21 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Picking for delivery is complete. |
| [Post Goods Issue for Outbound Delivery](#unique_17) [page ] 22 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Issue of goods against the delivery is posted. |
| [Create Billing Document](#unique_18) [page ] 23 | Billing Clerk | Create Billing Documents (F0798) | Billing document is created. |
| [Create Attachment for Billing Document (Optional)](#unique_19) [page ] 24 | Billing Clerk | Manage Billing Documents (F0797) | Attachment for billing document is created. |
| [Create Debit Memo Request](#unique_20) [page ] 25 | Internal Sales Representative | Manage Debit Memo Requests (F1988) | Debit memo request is created |
| [Create Attachment for Debit Memo Request (Optional)](#unique_21) [page ] 27 | Internal Sales Representative | Manage Debit Memo Requests (F1988) | Attachment for debit memo request is created. |
| [Remove Billing Block](#unique_22) [page ] 28 | Internal Sales Representative | Manage Debit Memo Requests (F1988) | Billing block is removed. |
| [Create Debit Memo](#unique_23) [page ] 29 | Billing Clerk | Create Billing Documents (F0798) | Debit memo is created |

Consignment Fill-Up

| Process Step | Business Role | App | Expected Results |
| --- | --- | --- | --- |
| [Create Consignment Fill-Up Order](#unique_24) [page ] 30 | Internal Sales Representative | Create Sales Orders - VA01 (VA01) | Consignment fill-up order is created. |
| [Create Outbound Delivery](#unique_25) [page ] 31 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) | Outbound delivery is created. |
| [Process Picking for Outbound Delivery](#unique_26) [page ] 32 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Material is picked. |
| [Post Goods Issue](#unique_27) [page ] 33 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Issue of goods against the delivery is posted. |
| [Check Stock Overview](#unique_28) [page ] 34 | Shipping Specialist | Stock - Multiple Materials (F1595) | The delivered quantity is added to the consignment stock. |

Consignment Issue

| Process Step | Business Role | App | Expected Results |
| --- | --- | --- | --- |
| [Create Consignment Issue Order](#unique_29) [page ] 35 | Internal Sales Representative | Create Sales Orders - VA01 (VA01) | Consignment issue order is created. |
| [Create Outbound Delivery](#unique_30) [page ] 36 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) | The delivery is created. |
| [Post Goods Issue](#unique_31) [page ] 37 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Issue of goods against the delivery is posted. |
| [Check Stock Overview](#unique_32) [page ] 38 | Shipping Specialist | Stock - Multiple Materials (F1595) | The customer consignment stock is reduced by the goods issue. |
| [Create Customer Invoice](#unique_33) [page ] 39 | Billing Clerk | Create Billing Documents (F0798) | Customer invoice is created. |

Consignment Pick-Up

| Process Step | Business Role | App | Expected Results |
| --- | --- | --- | --- |
| [Create Consignment Pick-Up Order](#unique_34) [page ] 40 | Internal Sales Representative | Create Sales Orders - VA01 (VA01) | Consignment pickup order is created. |
| [Create Return Delivery](#unique_35) [page ] 42 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) | Delivery is created. |
| [Receive Returned Goods](#unique_36) [page ] 42 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Material is received. |
| [Post Goods Receipt](#unique_37) [page ] 44 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Goods receipt is posted. |
| [Check Stock Overview](#unique_38) [page ] 44 | Shipping Specialist | Stock - Multiple Materials (F1595) | The delivered quantity is posted from the consignment stock into the free available stock. |

Consignment Return

| Process Step | Business Role | App | Expected Results |
| --- | --- | --- | --- |
| [Create Consignment Return Order](#unique_39) [page ] 45 | Internal Sales Representative | Create Sales Orders - VA01 (VA01) | Consignment return order is created. |
| [Create Return Delivery](#unique_40) [page ] 47 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) | Delivery is created. |
| [Post Goods Receipt](#unique_41) [page ] 47 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Goods receipt is posted. |
| [Check Stock Overview](#unique_42) [page ] 48 | Shipping Specialist | Stock - Multiple Materials (F1595) | The received quantity is added to the customer consignment stock. |
| [Release Consignment Return Order for Billing](#unique_43) [page ] 49 | Internal Sales Representative | Manage Customer Returns (F1708) | Billing block is removed. |
| [Create Credit Memo](#unique_44) [page ] 50 | Billing Clerk | Create Billing Documents (F0798) | Billing is carried out. |

Table 2: Advanced Intercompany Sales

| [Create Sales Order](#unique_45) [page ] 52 | Internal Sales Representative | Manage Sales Orders (F1873) | Sales order is created |
| --- | --- | --- | --- |
| [Process Sales Order Approval (Optional)](#unique_46) [page ] 56 |  |  | Sales order is approved |
| [Create Pro Forma F5 Invoice (Optional)](#unique_47) [page ] 56 | Billing Clerk | Create Billing Documents - VF01 (VF01) | Billing with F5 type is created |
| [Create Delivery](#unique_48) [page ] 57 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) | Delivery is created |
| [Perform Picking](#unique_49) [page ] 58 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Material is picked |
| [Post Goods Issue](#unique_50) [page ] 59 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | The goods issue is posted |
| [Confirm Transfer of Control Dates](#unique_51) [page ] 61 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Transfer of Control Dates are confirmed |
| [Create Pro Forma F8 Invoice (Optional)](#unique_52) [page ] 63 | Billing Clerk | Create Billing Documents - VF01 (VF01) | Billing with F8 type is created |
| [Create Intercompany Invoice](#unique_53) [page ] 65 | Billing Clerk | Create Billing Documents (F0798) | Billing with IV2 type is created. Intercompany Supplier Invoice is created automatically. |
| [Display Intercompany Supplier Invoice](#unique_54) [page ] 66 | Accounts Payable Accountant | Supplier Invoices List (F1060A) | Intercompany Supplier Invoice displays |
| [Create F2 Invoice](#unique_55) [page ] 67 | Billing Clerk | Create Billing Documents (F0798) | Billing with F2 type is created |
| [Update Text in Billing Document (Optional)](#unique_56) [page ] 69 | Billing Clerk | Change Billing Documents (VF02) |  |
| [Display Intercompany Sales Value Chain](#unique_57) [page ] 70 | Internal Sales Representative | Monitor Value Chains (F4854) | Advanced Intercompany Sales Value Chain would be displayed |
| [Display Intercompany Purchase Order](#unique_58) [page ] 72 | Internal Sales Representative | Monitor Value Chains (F4854) | Purchase Order document created as part of Advanced Intercompany Sales Value Chain Process can be displayed or checked |
| [Display Intercompany Sales Order](#unique_59) [page ] 73 | Internal Sales Representative | Monitor Value Chains (F4854) | Sales Order document created as part of Advanced Intercompany Sales Value Chain Process can be displayed or checked |
| [Display Intercompany Supplier Invoice](#unique_60) [page ] 74 | Internal Sales Representative | Monitor Value Chains (F4854) | Supplier Invoice document created as part of Advanced Intercompany Sales Value Chain Process can be displayed or checked |
| [Schedule Resolution of Value Chain Issues (Optional)](#unique_61) [page ] 75 | Internal Sales Representative | Schedule Resolution of Value Chain Issues (F6868) | Application Jobs displays |

## Test Procedures

This chapter describes the test procedures for each process step that belongs to this scope item.

### Create Sales Quotation

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
| 5 | Enter Quotation Details | Make the following entries and select Enter.Sold-to Party: 33113006Ship-to Party: 33113006Valid to: <Enter a Date>. For example, one year from todayIn the All Items table, enter the following details:Material: R_3018Order Quantity: <Quantity>Plant: 3350Enter a <quantity> for the relevant variant article in the grid and select Next Screen. |  |  |
| 6 | Select Save | Select Save. | The quotation document is created. |  |

### Change Quotation Document (Optional)

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

### Create Sales Orders

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
| 4. | Enter Data | In the header section, enter:Sold-to Party:33113006Ship-to Party: 33113006Customer References: <Reference Document ID>, for instance, sales quotation document number.In the All Items table, enter the following details:Material: R_3018Order Quantity: <Order Quantity>Plant: 3350Select EnterEnter a <quantity> for the relevant variant article in the grid and select Next Screen. | Details are copied from the reference document if sales order is selected to create with reference else if selected to create without reference then details are entered successfully.Note In case quotation exists for the given customer and material combination and you still select to create the sales order without its reference then Open quotations for item pop-up appears after you enter the customer and material details. You can select to proceed in one of the following ways:Select Continue or Cancel on the Open quotations for item pop-up to continue and complete sales order creation without the quotation reference. Or,Select List on the Open quotations for item pop-up, select the relevant SD document (quotation document) which you want to use as reference and select Copy. |  |
| 5 | Save the Order | Select Save. | A success message on save of a sales order is displayed. |  |

### Create an Outbound Delivery

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

### Create Attachment for Delivery (Optional)

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

### Process Picking for Outbound Delivery

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

### Post Goods Issue for Outbound Delivery

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

### Create Billing Document

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

### Create Attachment for Billing Document (Optional)

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

### Create Debit Memo Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step explains how to generate a billing document and debit the customer's account.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. |  |  |
| 2 | Access the App | Open Manage Debit Memo Requests (F1988) app. | The Manage Debit Memo Requests (F1988) screen is displayed. |  |
| 3 | Navigate to Create Debit Memo Request | Select Create Debit Memo Requests. | The Create Sales Document screen is displayed. |  |
| 4 | Enter Sales Document Type | Make the following entries and select Continue:Order Type: DRNote Regarding an existing order or billing document: Select Create with Reference. Enter the billing document number in Billing Document field under BillDoc tab view or sales order number in Order field under Order tab view and select Copy. | The Create Debit Memo Requests Overview screen is displayed. |  |
| 5 | Input Order Quantity | Make the following entries and select Enter:Sold-to Party: 33113006Ship-to Party: 33113006Customer Reference : <Reference Document ID>, for instance, Sales Order document number or Billing Document number.In the All Items table, enter the following details:Material: R_3018Target Quantity: <Quantity>Plant: 3350Enter the <quantity> for the relevant variant article in the grid and select Next Screen.Note If you create the debit memo request regarding an existing order or billing document, input the quantity, for example, 1 PCE (piece). | The input order quantities are entered. |  |
| 6 | Enter Order Reason | On the Sales tab, enter an order reason, for example, Damaged in Transit, | The order reason is recorded. |  |
| 7 | Save | Save your entries. | The order is saved, and a billing block is assigned to the debit memo. |  |

### Create Attachment for Debit Memo Request (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step explains how to create attachment for a sales order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. |  |  |
| 2 | Access the App | Open Manage Debit Memo Requests (F1988) app. |  |  |
| 3 | Navigate to Display Debit Memo Request Screen | On the Manage Debit Memo Requests (F1988) screen, enter the respective order number created in previous step in the Debit Memo Requests and select Go.Select the debit memo request line that is displayed. |  |  |
| 4 | Debit Memo Request | Select Change then select Services for Object in the upper right corner of the Change Debit Memo Request xxxxxxxx: Overview screen, select Create Attachment. | The File Upload dialog box is displayed. |  |
| 5 | Import File | Select OK in the File Upload dialog box.In the Open view, select local path and file, and select Open. | The attachment was successfully created message is displayed. |  |
| 6 | Check Attachment (Optional) | Select Services for Object in the upper right corner of screen, select Attachment list. Select the attachment and select Display, if you want to open the document | An attachment is displayed on the Service: Attachment list screen. |  |
| 7 | Save | On the Change Debit Memo Request xxxxxxxx: Overview screen, select Save | The debit memo request is saved. |  |

### Remove Billing Block

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step explains how to remove the billing block assigned to the debit memo by the sales order entry procedure.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. |  |  |
| 2 | Access the App | Open Manage Debit Memo Requests (F1988) app. |  |  |
| 3 | Find Document | Make the following entry, and select Go:Debit Memo Request: <Debit Memo Request Number> | Debit Memo Request number is accessed. |  |
| 4 | Remove Billing Block | Select the row of your Debit Memo Request and select Remove Billing Block. | The billing block is removed. |  |

### Create Debit Memo

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step explains how to generate a debit memo and debit the customer's account.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Billing Clerk. |  |  |
| 2 | Access the App | Open Create Billing Documents (F0798) app. |  |  |
| 3 | Define Billing Setting | Select Billing Settings at the bottom bar, you can make the following settings as below:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: OFFAutomatically post billing documents: ONDisplay billing documents after creation: ONSelect delivery items to be billed and select quantities: OFF |  |  |
| 4 | Search Billing Due Items | In the search condition, use criteria if necessary. | Sales document(s) is displayed. |  |
| 5 | Select Billing Item(s) | Select row(s) of a sales document created previously and select button Create Billing Documents. | The pop-up Create Billing Documents is displayed. |  |
| 6 | Maintain Billing Date | Select billing type Debit Memo (L2) and maintain billing date, for example, <current date>, then select OK.Note The pop-up Messages will display the following messages:Document TMPxxxxxxxx: Document TMPxxxxxxx has been saved.Document xxxxxxxx, Item xx: Item category L2 TAG cannot be invoiced with billing type L2. (This message will be displayed only if generic article (TAG) exists in the debit memo request )Select OK on the Messages pop-up. | The draft billing document or invoice with ID <TMPxxxxxx> is displayed. |  |
| 7 | Save Billing Document | On the Manage Billing Documents screen, select Save. Make a note of the billing document number.Note The draft version billing document or invoice with ID TMPxxxxxx is converted into a saved billing document with ID xxxxxxxx. | The system generates a billing invoice. |  |

### Consignment Fill-Up

#### Create Consignment Fill-Up Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The consignment fill-up order is used to transfer goods from plant stock to customer consignment stock. This process step explains how to create a consignment fill-up order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. |  |  |
| 2 | Access the App | Open Create Sales Orders - VA01 (VA01) app. |  |  |
| 3 | Enter Order Type | Enter the following data:Order Type: CCFUSales Organization: 3310Distribution Channel: 10Division: 00Select Continue. | Create Consignment Fill-Up: Overview screen is displayed. |  |
| 4 | Enter Material Data | On the Create Consignment Fill-Up: Overview screen, make the following entries:Sold-to Party: 33113007Ship-to Party: 33113007Cust. Reference : <Reference Document ID>, for instance, Customer PO number. In the All Items table, enter the following details:Material: R_3018Order Quantity: <Order Quantity>Plant: 3350Select Enter enter the <quantity> for the relevant variant article in the grid and select Next Screen |  |  |
| 5 | Save Document | Select Save. Make a note of the sales order number. |  |  |

#### Create Outbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step explains how to create the outbound delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Create Outbound Deliveries - From Sales Orders (F0869A) app. |  |  |
| 3 | Search Sales Order | Make the following entries and select Go:Shipping Point: 3350Planned Creation Date: <Enter the delivery selection date>.SD Document: <Enter the sales order number created previously>. |  |  |
| 4 | Create Delivery | Select your sales order items and select Create Deliveries. | The outbound delivery is created. |  |
| 5 | Check Log | Select Display Log. Select Deliveries and note down the delivery ID. | You know which delivery is created. |  |

#### Process Picking for Outbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The picking process involves taking goods from a storage location and providing the right quantity in a picking area where the goods are prepared for shipping.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD) app. |  |  |
| 3 | Enter value in the selection screen | On the Manage Outbound Deliveries - VL06O (VL06O_CLOUD) screen, select For Picking. |  |  |
| 4 | Enter Shipping Point | On the Outbound Deliveries for Picking screen, make the following entry:Shipping Point: 3350 |  |  |
| 5 | Set Only Picking without WM | Select Only Picking without WM and select Execute. |  |  |
| 6 | Select Outbound Delivery | On the Day's Workload for Picking screen, select your outbound delivery and select Change Outbound Deliveries. |  |  |
| 7 | Enter Picked Quantity | On the Outbound Delivery xxxxxxxx Change: Overview screen, select the Picking tab. Enter the quantity in the Picked Qty field.The picking status is set to complete if the picked quantity and the delivery quantity is equal. To solve deviations in quantity, select Menu > Edit > Copy Picked Quantity as Deliv. Quantity. | The picked quantities are entered. |  |
| 8 | Save Document | Select Save. | The delivery is saved. |  |

#### Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you post the goods issue.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD) app. |  |  |
| 3 | Enter value in the selection screen | Select For Goods Issue. Make the following entries and select Execute:Shipping Point: 3350 |  |  |
| 4 | Post Goods Issue | Select the relevant delivery and select Post Goods Issue in the dialog box, select today’s date and select Continue. | The goods issue is posted. |  |

#### Check Stock Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The goods are now in the customer's consignment stock. The stock overview reflects this transfer of products. This process step shows you how to check the stock overview.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Stock - Multiple Materials (F1595) app. |  |  |
| 3 | Enter Plant, Material Data, and Customer | On the Stock - Multiple Materials (F1595) screen, select Adapt Filters then select the Customer and Special Stock Type checkboxes in the Adapt Filters pop-up, select OK and then make the following entries:Plant: 3350Material Number: R_3018Customer: <Enter the customer used in sales document>Special Stock Type: WSelect Go.Note You may need to adapt column view settings to view Customer. Select Settings, select Customer checkbox on the View Settings pop-up and select OK. | The customer consignment stock is displayed. The delivered quantity is posted into the consignment stock. |  |

### Consignment Issue

#### Create Consignment Issue Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

At regular intervals, the customer reports either how many products have been sold, or consumed, or how many products are in the current stock (inventory). A corresponding order is entered, documenting the issue from the consignment stock. A billing document is created for issue from the external stock at the customer site.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Internal Sales Representative. |  |  |
| 2 | Access the App | Open Create Sales Orders - VA01 (VA01) app. | Create Sales Documents screen is displayed. |  |
| 3 | Enter Order Type | On the Create Sales Document screen, make the following entries and select Continue:Order Type: CCISSales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 4 | Enter Material Data | On the Create Consignment Issue: Overview screen, make the following entries:Sold-to Party: 33113007Ship-to Party: 33113007Cust. Reference: <Reference Document ID>, for instance, Customer PO number.In the All Items table, enter the following details:Material: R_3018.Order Quantity: <Order Quantity>Plant: 3350Select EnterEnter the <quantity> for the relevant variant article in the grid and select Next Screen. |  |  |
| 7 | Save Document | Select Save.Make a note of the sales order number. | The consignment issue order is created. |  |

#### Create Outbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step explains how to create the outbound delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Create Outbound Deliveries - From Sales Orders (F0869A) app. |  |  |
| 3 | Search Sales Order | Make the following entries and select Go:Shipping Point: 335CPlanned Creation Date: <the delivery selection date>SD Document: <the sales order number created previously> |  |  |
| 4 | Create Delivery | Select your sales order items and select Create Deliveries. | The creation of a delivery is triggered. |  |
| 5 | Check Log | Select Display Log, go to Deliveries, and note down the delivery ID. | The outbound delivery is created. |  |

#### Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step explains how to, you post the goods issue.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD) app. |  |  |
| 3 | Enter value in the selection screen | Select For Goods Issue. Make the following entry and select Execute:Shipping Point: 335C |  |  |
| 4 | Post Goods Issue | Select the relevant delivery and select Post Goods Issue. In the dialog box, select today’s date and select Continue. | The goods issue is posted. |  |

#### Check Stock Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The goods are transferred from the customer's consignment stock and are no longer owned by the company. The stock overview reflects this transfer of products.

This process step shows you how to check the stock overview.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Stock - Multiple Materials (F1595) app. |  |  |
| 3 | Enter Plant, Material Data, and Customer | On the Stock - Multiple Materials (F1595) screen, select Adapt Filters then select the Customer and Special Stock Type checkboxes in the Adapt Filters pop-up, select OK and then make the following entries:Plant: 3350Material Number: R_3018Customer: <Enter the customer used in sales document>Special Stock Type: WSelect GoNote You may need to adapt column view settings to view Customer. Select Settings, select Customer checkbox on the View Settings pop-up and select OK. | The customer consignment stock is displayed. The customer consignment stock is reduced by the goods issue. |  |

#### Create Customer Invoice

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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. |  |  |
| 2 | Access App | Open Create Billing Documents (F0798) app. |  |  |
| 3 | Search for Billing Due Items | Enter the relevant search criteria, such as <Sold-to Party>, <Sales Document ID>, or <Sales Document Category>. In the SD Document Category filter, select Delivery. | A list of delivery-related billing due list items is displayed. |  |
| 4 | Make Billing Settings | Select Billing Settings at the bottom bar, you can make the following settings as below:Set billing date and type before billing : ON Create separate billing document for each item of billing due list: OFFAutomatically Post Billing Documents : ON .Display Billing Documents After Creation: ON.Select delivery items to be billed and select quantities: OFFSelect OK. |  |  |
| 5 | Select item(s) for billing | Select row(s) of SD Document created previously and select button Create Billing Documents. | The Create Billing Document s pop-up is displayed. |  |
| 6 | Maintain Billing Date | Select billing type Invoice (F2) and maintain Billing Date, for example <currentdate>, then select button OK. | The draft billing document or invoice with ID <TMPxxxxxx> is displayed. |  |
| 7 | Save Billing Document | On the Manage Billing Documents screen, select button Save. Make a note of the billing document number.Note The draft version billing document or invoice with ID TMPxxxxxx is converted into a saved billing document with ID xxxxxxxx. | The system generates an invoice for billing. |  |
| 8 | Display Print Preview | Select Preview at the top right side of the screen. | A preview of the invoice document in PDF form is displayed. |  |

### Consignment Pick-Up

#### Create Consignment Pick-Up Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The customer can return goods that are not required or sold to the central warehouse. The consignment pickup triggers the return of goods from the customer’s custody.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Internal Sales Representative. |  |  |
| 2 | Access the App | Open Create Sales Orders - VA01 (VA01) app. |  |  |
| 3 | Enter Order Type | On the Create Sales Document screen, make the following entries and select Continue (Enter):Order Type: CCPUSales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 4 | Enter Material Data | On the Create Consignment Pick-Up: Overview screen, make the following entries:Sold-to Party: 33113007Ship-to Party: 33113007Customer Reference: <the customer purchase order number>In the All Items table, enter the following details:Material: R_3018.Order Quantity: <Order Quantity>Plant: 3350Press Enter.Enter the <quantity> for the relevant variant article in the grid and select Next Screen. |  |  |
| 5 | Save Document | Select Save.Make a note of the sales order number. |  |  |

#### Create Return Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step explains how to create return delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Create Outbound Delivery - With Order Reference (VL01N) app. |  |  |
| 3 | Search Sales Order | Make the following entries:Shipping Point: 335RSelection Date: <Enter the delivery selection date>.Order: <Enter the sales order number created previously>.Select Continue. |  |  |
| 4 | Save Document | Select Save. Make a note of the delivery number. | A delivery is created. |  |

#### Receive Returned Goods

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The picking process involves taking goods from a storage location and providing the right quantity in a picking area where the goods are prepared for shipping.

This process step explains how to manage the returned goods.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD) app. |  |  |
| 3 | Enter value in the selection screen | On the Manage Outbound Deliveries - VL06O (VL06O_CLOUD) screen, select For Picking. |  |  |
| 4 | Enter Shipping Point | On the Outbound Deliveries for Picking screen, make the following entry:Shipping Point: 335R |  |  |
| 5 | Set Only Picking Without WM | Select Only Picking without WM and select Execute. |  |  |
| 6 | Select Outbound Delivery | On the Day's Workload for Picking screen, select your outbound delivery and select Change Outbound Deliveries. |  |  |
| 7 | Enter Received Quantity | On the ... <Delivery Number> Change: Overview screen, select the Picking tab. Enter the quantity in the Picked Qty field.The picking status is set to complete if the picked quantity and the delivery quantity is equal. To solve deviations in quantity, select M enu > Edit > Copy Picked Quantity as Deliv. Quantity. |  |  |
| 8 | Save Document | Select Save. | The delivery is saved. |  |

#### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step explains how to post the goods receipt. When the goods receipt is posted, the transfer from the consignment stock is carried out at the same time as the direct posting into the free stock of the return storage location.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD) app. |  |  |
| 3 | Make Entries | Select For Goods Issue. Make the following entry and select Execute :Shipping Point: 335R |  |  |
| 4 | Post Goods Issue | Select the relevant delivery and select Post Goods Issue. In the dialog box, select today’s date and select Continue. | The goods receipt is posted. |  |

#### Check Stock Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The goods are transferred again to customer's consignment stock. This process step shows you how to check the stock overview.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Stock - Multiple Materials (F1595) app. | The Stock - Multiple Materials (F1595) screen is displayed. |  |
| 3 | Enter Plant, Material Data, and Customer | On the Stock - Multiple Materials (F1595) screen, make the following entries:Plant: 3350Material Number: R_3018Storage Location : 995RSelect Go. | The customer consignment stock is displayed. The delivered quantity is posted from the consignment stock into the free available stock. |  |

### Consignment Return

#### Create Consignment Return Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Goods that have not been consumed or sold by the customer may be returned to the consignment stock. In this case, the customer communicates the returning quantity together with the corresponding batch number. A return order with the following follow-on documents is generated:

- A returns delivery with subsequent goods receipt
- A credit notes for returns

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Internal Sales Representative. |  |  |
| 2 | Access the App | Open Create Sales Orders - VA01 (VA01) app. | The Create Sales Orders - VA01 (VA01) screen is displayed. |  |
| 3 | Enter Order Type | On the Create Sales Orders - VA01 (VA01) screen, make the following entries:Order Type: CCRESales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 4 | Enter Material Data | On the Create Consignment Return: Overview screen, make the following entries and Select Continue (Enter):Sold-To Party: 33113007Ship-To Party: 33113007Cust. Reference: <Reference Document ID>, for instance, Customer PO number. In the All Items table, enter the following details:Material: R_3018Order Quantity: <Order Quantity>Plant: 3350Select EnterEnter the <quantity> for the relevant variant article in the grid and select Next ScreenCheck that the Billing Block is set. |  |  |
| 5 | Save Document | Select Save.Make a note of the sales order number. | The customer return order is created. |  |

#### Create Return Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create the return delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Create Outbound Delivery - With Order Reference (VL01N) app. | The Create Outbound Delivery - With Order Reference (VL01N) screen is displayed. |  |
| 3 | Search Sales Order | Make the following entries:Shipping Point: 335CSelection Date: <the delivery selection date>Order: <the sales order number created previously>Storage Location: 995ASelect Continue. |  |  |
| 4 | Save Document | Select Save.Make a note of the delivery number. | A return delivery is created. |  |

#### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you post the goods receipt. When the goods receipt is posted, the consignment stock is consequently increased.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD) app. | The Manage Outbound Deliveries - VL06O (VL06O_CLOUD) screen is displayed. |  |
| 3 | Enter value in the selection screen | Select For Goods Issue. Make the following entry and select Execute:Shipping Point: 335C |  |  |
| 4 | Post Goods Issue | Select the relevant delivery and select Post Goods Issue. In the dialog box, select today’s date and select Continue. | The goods receipt is posted. |  |

#### Check Stock Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The goods are transferred to the customer consignment stock. This process step shows you how to check the stock overview.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Stock - Multiple Materials (F1595) app. | The Stock - Multiple Materials (F1595) screen is displayed. |  |
| 3 | Enter Plant, Material Data, and Customer | On the Stock - Multiple Materials (F1595) screen, select Adapt Filters then select the Customer and Special Stock Type checkboxes in the Adapt Filters pop-up, select OK and then make the following entries:Plant: 3350Material Number: R_3018Customer: <Enter the customer used in sales document>Special Stock Type: WSelect Go.Note You may need to adapt column view settings to view Customer. Select Settings , select Customer checkbox on the View Settings pop-up and select OK. | The customer consignment stock is displayed. The received quantity is added to the customer consignment stock. |  |

#### Release Consignment Return Order for Billing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The consignment return order has been created with a billing block to be removed manually. This is done to add a check of the credit memo to ensure that the entries are correct.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Returns and Refund Clerk. |  |  |
| 2 | Access the App | Open Manage Customer Returns (F1708) app. | The Manage Customer Returns (F1708) screen is displayed. |  |
| 3 | Navigate to Display Return Order Screen | On the Manage Customer Returns (F1708) screen, enter the respective order number created in previous step in the Returns Order field and select Go.Select the return order line that is displayed. |  |  |
| 4 | Navigate to Change Return Order Screen | Select Change. |  |  |
| 5 | Remove Billing Block | On the Change Consignment Return xxxxxxxx : Overview screen, remove the billing block. | The billing block is removed. |  |
| 6 | Save Document | Select Save. | The sales order is saved. |  |

#### Create Credit Memo

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step explains how to create the billing document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk |  |  |
| 2 | Access the App | Open Create Billing Documents (F0798) app. | The Create Billing Documents (F0798) screen is displayed. |  |
| 3 | Search for Billing Due Items | Enter the relevant search criteria, such as <Sold-to Party>, <Sales Document ID>, or <Sales Document Category>, in the search field.In the SD Document Category filter, select Returns Delivery for Order. | A list of delivery-related billing due list items is displayed. |  |
| 4 | Make Billing Settings | Select Billing Settings at the bottom bar, you can make the following settings as below:Set billing date and type before billing : ONCreate separate billing document for each item of billing due list: OFFAutomatically post billing documents: ONDisplay Billing Documents After Creation : ON .Select delivery items to be billed and select quantities: OFFSelect OK. |  |  |
| 5 | Select item(s) for billing | Select row(s) of SD Document created previously and select button Create Billing Documents. | The Create Billing Documents pop-up is displayed. |  |
| 6 | Maintain Billing Date | Select Credit Memo for Returns (CBRE) billing type, and maintain Billing Date, for example, <Current Date>, then select OK. | The draft billing document or invoice with ID <TMPxxxxxx> is displayed. |  |
| 7 | Save Billing Document | On the Manage Billing Documents screen, select Save. Make a note of the billing document number.Note The draft version billing document or invoice with ID TMPxxxxxx is converted into a saved billing document with ID xxxxxxxx. | The system generates an invoice for billing. |  |
| 8 | Display Print Preview | Select Preview at the top right side of the screen. | A preview of the credit memo document in PDF form is displayed. |  |

### Advanced Intercompany Sales

#### Create Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create sales order in the selling company, then goods will be directly delivered to the customer from the affiliate company/plant.

Part 1: Create Sales Order with General Trading Material

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Navigate to Create Sales Order Screen | On the Manage Sales Orders screen, choose Create > Create Sales Order VA01 . | The Sales Order screen displays. |  |
| 4 | Enter Sales Document Type | Make the following entries:Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00Sales Office: 330Choose Continue. | The Create Sales Order: Overview screen displays. |  |
| 5 | Enter Order Details | Sold-to Party: 33113007Cust. Reference: PO numberDeliver.Plant: <Delivery Plant in another company code>, for example, 1750Plant: <Delivery Plant in another company code>, for example, 1750Material: <material number>, for example, R_3018.Order Quantity: <quantity>, for example, 10. |  |  |
| 6 | Enter Tax Departure Country | On the top menu, choose Menu > Goto > Header > Billing . |  |  |
| 7 | Tax Country/Region | In the Billing section, input country abbreviation that is consistent to Sales Organization.For example, if Sales Organization is 3310, then make the following entry:Tax Departure C / R: AE |  |  |
| 8 | Go Back | Choose Back. | The Create Standard Order: Overview screen displays. |  |
| 9 | Check Transit Plant | Choose the line item and choose Display Item Details. Choose Shipping tab, check the value of the field Transit Plant, for example, 3350. | The right Transit Plant displays. |  |
| 10 | Save | Choose Save. | A sales order is created.Make a note of the sales order number. |  |
| 11 | Check Intercompany Purchase Order | Execute the step [Display Intercompany Purchase Order](#unique_58) [page ] 72 to check the Intercompany Purchase Order automatically created by the above sales order. | Intercompany Purchase Order is automatically created successfully. |  |
| 12 | Check Intercompany Sales Order | Execute the step [Display Intercompany Sales Order](#unique_59) [page ] 73 to check the intercompany sales order automatically created by the above sales order. | Intercompany Sales Order is automatically created successfully. |  |

Part 2: Create Sales Order with Sales Kits Material

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Create Sales Order | On the Manage Sales Orders screen, choose Create, then select Create Sales Orders - VA01(VA01). |  |  |
| 4 | Enter the Order Data | On the Create Standard Order: Initial screen, make the following entries and choose Enter:Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 5 | Enter Order Details | On the Create Sales Orders: Overview screen, make the following entries:Sold to party: 33100002Ship to party: 33100002Customer Reference: <Customer Reference>Customer Reference Date: <Date>Material Number: <SDBOMERLAHD> or <SDBOMLUMFHD>Deliver.Plant: <Delivery Plant in another company code>, for example, 1710Plant: <Delivery Plant in another company code>, for example, 1710Order Quantity: <Quantity>Enter the item category TAQF or TAPF manually before BOM explosion if the item is free of charge during order creation.Note If you are using SDBOMERLAHD, SDBOMLUMFHD, or SDBOMCPFHHD, SDBOMDISHHD (for Cloud only) in testing, the sales BOM will explode and subitems will appear. However, the BOM expansion and material presentation on Sales to Customer documents and Internal Sales documents are different.In Sales to Customer documents (Sales Order, Outbound Delivery, Customer Invoice), main item and subitems are shown both.In Internal Sales documents (Purchase Order, Intercompany Order, Intercompany Invoice, Supplier Invoice, and Stock in Transit postings) only items with Inventory Management are shown.Consequently, these items must carry (internal) prices, regardless of whether the external price is charged on them or not.BOM TypePricing inInventory inThe section for Sales to Customer documents displaysThe section for Internal Sales document displaysSDBOMERLAHDMain itemMain itemMain item and subitems bothMain item onlySDBOMLUMFHDSubitemsSubitemsMain item and subitems bothSubitems onlySDBOMCPFHHDMain itemSubitemsMain item and subitems bothSubitems onlySDBOMDISHHDSubitemsMain itemMain item and subitems bothMain item only |  |  |
| 6 | Enter Tax Departure Country | On the top menu, choose Menu > Goto > Header > Billing . |  |  |
| 7 | Tax Country/Region | In the Billing section, input country abbreviation that is consistent to Sales Organization.For example, if Sales Organization is 1010, then make the following entry:Tax Departure C / R: DE |  |  |
| 8 | Go Back | Choose Back. | The Create Standard Order: Overview screen displays. |  |
| 9 | Check Transit Plant | Choose the line item and choose Display Item Details. Choose Shipping tab, check the value of the field Transit Plant, for example, 1010. | The right Transit Plant displays. |  |
| 10 | Save | Choose Save. | A sales order is created.Make a note of the sales order number. |  |
| 11 | Check Intercompany Purchase Order | Execute the step [Display Intercompany Purchase Order](#unique_58) [page ] 72 to check the Intercompany Purchase Order automatically created by the above sales order. | Intercompany Purchase Order is automatically created successfully. |  |
| 12 | Check Intercompany Sales Order | Execute the step [Display Intercompany Sales Order](#unique_59) [page ] 73 to check the intercompany sales order automatically created by the above sales order. | Intercompany Sales Order is automatically created successfully. |  |

#### Process Sales Order Approval (Optional)

Follow the procedure in Process Sales Order Approval steps in the scope item Sell from Stock (BD9).

Purpose

This process step shows you how to review the sales orders that might be approved.

Procedure

Complete the activities of Process Sales Order Approval step described in the scope item Sell from Stock (BD9).

#### Create Pro Forma F5 Invoice (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create Pro Forma F5 Invoice by referring the intercompany sales order created in the previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents - VF01 (VF01). | The Create Billing Document screen displays. |  |
| 3 | Maintain Billing Date | Select billing type Pro Forma for Order (F5) and maintain billing date, for example, current date.Enter Intercompany Sales Order number in the input field Document which is created in the previous step.Press Enter. |  |  |
| 4 | Save | Choose Save. | The F5 billing document is created. |  |
| 5 | Search Billing Document | Open Display Billing Documents (VF03). | The Display Billing Document screen displays. |  |
| 6 | Display Billing Document | On the Display Billing Documents (VF03) screen, enter the Billing Number and choose Continue. | The Billing Document screen displays. |  |
| 7 | Check Output Condition | On the Pro Forma Invoicexxxxxxxx (F5) Display: Overview screen, choose Change Bill. Doc. and then choose Menu > Goto > Header > Output . | The Pro Forma for Order xxxxxxxx ( F5) Change: Output screen displays. |  |
| 8 | Display Print Preview | On the Invoice Change: Output screen, select the output entry and choose Display PDF Document. | Preview for PDF document displays. |  |
| 9 | Print Billing Document | From the preview of the document, choose Print. |  |  |

#### Create Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create the delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Outbound Deliveries - From Sales Orders (F0869A). | The Create Outbound Deliveries-From Sales Orders screen displays. |  |
| 3 | Search Sales Order | Make the following entries and choose Go:Shipping Point: 1750Planned Creation Date: <delivery selection date>Order: <sales order number created previously> | The Create Delivery: Overview screen displays. |  |
| 4 | Create Delivery | Select your sales order items and choose Create Deliveries. | Creation of a delivery is triggered. |  |
| 5 | Check Details | Choose Display Log. | The Analyze Delivery Log screen displays. Delivery is created successfully with delivery number shown on the Deliveries tab. |  |

#### Perform Picking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to take goods from a storage location and staging the right quantity in a picking area where the goods are prepared for shipping.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). | The Manage Outbound Deliveries screen displays. |  |
| 3 | Open Outbound Delivery Monitor | On the Outbound Delivery Monitor screen, choose For Picking. |  |  |
| 4 | Enter Shipping Point | On the Manage Outbound Deliveries screen, make the following entry:1750 |  |  |
| 5 | Select the Only Picking without WM Checkbox and Choose Execute | Choose Only Picking without WM.Choose Execute. |  |  |
| 6 | Select the Outbound Delivery | On the Day's Workload for Picking screen, select your outbound delivery and choose Change Outbound Deliveries. |  |  |
| 7 | Enter Picked Quantity | On the Outbound Delivery xxx Change: Overview screen, choose Picking and enter quantity in the Picked Qty field.Picking status is set to Completely processed if picked quantity and delivery quantity are equal.Deviations in quantity can be solved by the Copy Picked Quantity as Delivery Quantity function. |  |  |
| 8 | Save Document | Choose Save. |  |  |

#### Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post the goods issue.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). | The Manage Outbound Deliveries screen displays. |  |
| 3 | Open Outbound Delivery Monitor | Choose For Goods Issue.Make the following entry and choose Execute.Shipping Point: 1750 |  |  |
| 4 | Post Good Issue | Mark the relevant delivery and choose Post Goods Issue.Select today’s date in the dialog box.Choose Continue. | The goods issue is posted to Stock in Transit of delivering company, for example, 3310. The other follow-on good movements are posted or scheduled for later posting according to the Transfer of Control Dates. |  |
| 5 | Check Status of Advanced Intercompany Sales Value Chain | Execute the step Display Intercompany Sales Value Chain to check the status of the Advanced Intercompany Sales Value Chain. | The status of the Advanced Intercompany Sales Value Chain is correct. The other follow-on good movements are posted or scheduled for later posting successfully according to the Transfer of Control Dates. |  |

Printing Form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Outbound Delivery (VL03N). | The Display Outbound Delivery screen is displayed. |  |
| 3 | Issue Delivery Output | Choose For Goods Issue.Make the following entries and choose Execute.Shipping Point: 1750On the Display Outbound Delivery, enter the Delivery number, and choose Continue.On the Delivery xxxxxxxxxxx Display: Overview:choose More > Extras > Delivery > Output > Output Control . | The Delivery: Output screen displays. |  |
| 4 | Print Preview | On the Delivery: Output screen, select the line with the Output Type DELIVERY_NOTE, and choose Display PDF Document. | A preview of the print document displays. |  |
| 5 | Print Delivery Note | From the preview of the document, choose Print. | The delivery note is printed. |  |

Financial Posting

| Material | Debited Account | Credited Account | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 13600000 Inventory - Trading Goods | 13600000 Inventory - Trading Goods | none |

#### Confirm Transfer of Control Dates

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to confirm transfer of control dates. Normally the transfer of control dates is confirmed by API or TM integration based on Incoterms.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). | The Manage Outbound Deliveries screen displays. |  |
| 3 | Open Outbound Delivery Monitor | Choose List Outbound Deliveries.Make the following entries and choose Execute.Shipping Point/Receiving Pt: 1750 | List of Outbound Deliveries screen displays. |  |
| 4 | Change Outbound Deliveries | Mark the relevant delivery and choose Change Outbound Deliveries. | Outbound Delivery <Outbound Delivery> Change: Overview screen displays. |  |
| 5 | Confirm Internal Transfer of Control Dates and Times | On the top menu, choose Menu > Goto > Header > Shipment , check the field Planned Dates and Time at the screen block Internal Transfer of Control Dates, input new actual date and time in the field Actual Date and Time to reflect the actual case, for example, current System Date and Time.Note This field controls when the goods movement will be posted from Stock in Transit of the delivering company to the selling company. If the Planned Date and Time or Actual Planned Date and Time is earlier than the System Date and Time, system will post the goods movement immediately when Goods Issue is posted on the Outbound Delivery. If the Planned Date and Time or Actual Planned Date and Time is in the future, system will post the goods movement one day later than this date and time. | Internal Transfer of Control Dates are confirmed. |  |
| 6 | Confirm External Transfer of Control Dates | At the screen block External Transfer of Control Dates, check the field Planned Dates and Time, input new actual date and time in the field Actual Date and Time to reflect the actual case, for example, current System Date and Time.Note This field controls when the goods movement will be posted from Stock in Transit of the selling company to customer. If the Planned Date and Time or Actual Planned Date and Time is earlier than the System Date and Time, system will post the goods movement immediately when Goods Issue is posted on the Outbound Delivery. If the Planned Date and Time or Actual Planned Date and Time is in the future, system will post the goods movement one day later than this date and time. | External Transfer of Control Dates are confirmed. |  |
| 7 | Save | Choose Save. | Outbound delivery is confirmed with transfer of control dates. |  |

Financial Posting

Post Goods Issue from Issuing SiT in delivering company

| Material | Debited Account | Credited Account | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 54083000 Inventory Change - Cost of own Goods sold w/C.Elem | 13600000 Inventory - Trading Goods | 54083000 Inventory Change - Cost of own Goods sold w/C.Elem |

Post Goods Receipt to storage location in selling company 3310

| Material | Debited Account | Credited Account | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 13600000 Inventory - Trading Good | 21120000 Goods Received/Invoice Received | none |

Post Goods Issue from storage location in selling company 3310

| Material | Debited Account | Credited Account | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 13600000 Inventory - Trading | 13600000 Inventory - Trading Goods | none |

Post Goods Issue from SiT to Customer in selling company 3310

| Material | Debited Account | Credited Account | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 54083000 Inventory Change - Cost of own Goods sold w/C.Elem | 13600000 Inventory - Trading Goods | 54083000 Inventory Change - Cost of own Goods sold w/C.Elem |

#### Create Pro Forma F8 Invoice (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create Pro Forma invoice in the selling company.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents - VF01 (VF01). | The Create Billing Documents screen displays. |  |
| 3 | Maintain Billing Date | Choose billing type Pro Forma Invoice for Delivery (F8) and maintain billing date, for example, current date.Enter Delivery Number.Choose Enter. |  |  |
| 4 | Save | Choose Save. | The F8 billing document is created. |  |
| 5 | Search Billing Document | Open Display Billing Documents (VF03). | The Display Billing Document screen displays. |  |
| 6 | Display Billing Document | On the Display Billing Documents (VF03) screen, enter the Billing Number, and choose Continue. | The Billing Document screen displays. |  |
| 7 | Check Output Condition | On the Pro Forma Invoicexxxxxxxx Display: Overview screen, choose Change Bill. Doc. and then choose Menu > Goto > Header > Output . | The Invoice xxxxxxxx Change: Output screen displays. |  |
| 8 | Display Print Preview | On the Invoice Change: Output screen, select the output entry and choose Display PDF Document. | Preview for PDF document displays. |  |
| 9 | Print Billing Document | From the preview of the document, choose Print. |  |  |

#### Create Intercompany Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create intercompany invoice in delivering company code. In background, intercompany supplier invoice is created automatically in the selling company code by Value Chain Management.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Documents screen displays. |  |
| 3 | Define Billing Settings | Choose Billing Settings on the bottom bar and make the following entries:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: ONAutomatically post billing documents: ONDisplay billing documents after creation: ONChoose delivery items to be billed and select quantities: OFF |  |  |
| 4 | Search for billing due list | In the search condition, use criteria if necessary, for example, the Delivery Number, press Enter. | Sales document(s) display in the result. |  |
| 5 | Select item(s) for billing | Select row(s) of SD Document created previously with intercompany sold-to party and choose the button Create Billing Documents. | The Create Billing Document screen displays. |  |
| 6 | Maintain Billing Date | Choose billing type Intercompany Invoice (IV2) and maintain billing date, for example current date, then choose button OK. | The draft billing document with ID TMPxxxxxxx displays. |  |
| 7 | Save Billing Document | On the Billing Document screen, choose Save.The draft version billing document with ID TMPxxxxxxx turns into a saved billing document with ID xxxxxxxx. Make a note of the billing document number: __________.Note The intercompany supplier invoice is only created automatically by VCM when the intercompany customer invoice has been transferred and released to FI. | The system generates an invoice for billing. |  |
| 8 | Check Intercompany Supplier Invoice | Execute the step Display Intercompany Supplier Invoice to know the number of the intercompany supplier invoice. |  |  |

Financial Posting

In all the scenarios related to a sales flow, whatever billing document is created (customer invoice, debit note, credit note, intercompany invoice, etc.) the journal entry type is determined according to the following rule:

- If the Dest. Country/Region is Italy, the FI document type is W1 IT Local Cust. Sales.
- If the Dest. Country/Region is within European Union, the FI document type is W2 IT EU Cust. Sales.
- If the Dest. Country/Region is outside European Union, the FI document type is W3 IT EXEU Cust. Sales.

Financial Posting

| Material | Debited Account | Credited Account | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 12300000 Receivables affiliated Companies | 41001500 Revenue Affiliate - Product | 41001500 Revenue Affiliate - Product |

#### Display Intercompany Supplier Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display the intercompany supplier invoice automatically created by the IV2 invoice.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Accounts Payable Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Supplier Invoices List (F1060A). | The Supplier Invoices List screen displays. |  |
| 3 | Search Intercompany Supplier Invoice | Enter the intercompany supplier invoice number in the field Invoice Document No. or enter the intercompany invoice number in the field Reference, which is noted down in the previous step. Choose Go. | The supplier invoice is listed out. |  |
| 4 | Display Intercompany Supplier Invoice | Choose the line item of the intercompany supplier invoice. | The Supplier Invoice screen displays. |  |
| 5 | Display Journal Entry | Choose Journal Entries, and the Display Process Flow – Accounts Payable screen displays.Choose the node Journey Entry, and the Journal Entry dialog box displays.Expand Related Applications, and choose Display Journal Entries. | The Display Document: Data Entry View screen displays. |  |

Financial Posting

| Material | Debited Account | Credited Account | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 21120000 Goods Received/Invoice Received | 21300000 Company Code 1710 as Business Partner | none |

#### Create F2 Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create customer invoice.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Documents screen displays. |  |
| 3 | Define Billing Settings | Choose Billing Settings on the bottom bar and make the following entries:Set the billing date and type in before billing: ONCreate a separate billing document for each item of billing due list: ONAutomatically post billing documents: ONDisplay billing documents after the creation: ONChoose delivery items to be billed and select quantities: OFF |  |  |
| 4 | Search for billing due list | In the search condition, use criteria if necessary, for example, the Delivery Number. Then press Enter. | Sales document(s) display in the result. |  |
| 5 | Select item(s) for billing | Select the row(s) of the SD document created previously with customer sold-to party and choose Create Billing Documents. | The Create Billing Document screen displays. |  |
| 6 | Maintain Billing Date | Choose billing type Invoice (F2) and maintain the billing date, for example the current date. Then choose OK. | The draft billing document with ID TMPxxxxxxx displays. |  |
| 7 | Save Billing Document | On the Billing Document screen, choose Save.The draft version billing document with ID TMPxxxxxxx turns into a saved billing document with ID xxxxxxxx. Make a note of the billing document number: __________. | The system generates an invoice for billing. |  |

Financial Posting

| Material | Debited Account | Credited Account | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 12100000 Rcvbls Domestic | 41000000 Revenue Domestic – Product22000000 Output Tax (MWS) | none |

#### Update Text in Billing Document (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to update text in a billing document.

Procedure

Update Text in Billing Document

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Billing Documents (VF02). | The Change Billing Documents screen displays. |  |
| 3 | Enter the Billing Number | On the Change Billing Documents screen, enter the respective billing document number created in the previous step.Choose Enter. | The billing document displays. |  |
| 4 | Update Text (Optional) | In the Edit mode, you can add, delete, and update these texts. | The relevant text is added, deleted, or updated. |  |
| 5 | Save your Changes | Save your changes by choosing Save in the footer bar. | The billing document is saved. |  |

Display Billing Document

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Display Billing Documents (VF03). | The Display Billing Documents screen displays. |  |
| 3 | Enter the Billing Number | On the Display Billing Documents screen, enter the respective billing document number and choose Continue. | The billing document displays. |  |
| 4 | Check Output Condition | On the Invoice xxxxxxxx (F2) Display: Overview of Billing Items screen, choose More > Goto > Header > Output . |  |  |
| 5 | Display PDF Document | On the Invoice xxxxxxxx (F2) Display: Output screen, select output item with output type BILLING_DOCUMENT and form template SDBIL_INVOICE_RU. Choose Display PDF Document. | Preview for PDF document displays. |  |

#### Monitor Intercompany Sales Value Chain

##### Display Intercompany Sales Value Chain

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display advanced intercompany sales value chain.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Value Chains (F4854). | The Monitor Value Chains screen displays. |  |
| 3 | Adapt Searching Filter | Choose Adapt Filters, and the Adapt Filters dialog box pops up. Select Initiating Document, Processing Stage and Process Type, and choose OK. | Searching field Process Type displays. |  |
| 4 | Search Value Chain Process | Make the following entries and choose Go:Initiating Document: * + Sales Order number.Process Type: <Advanced Intercompany Sales>Note You can also enter other document number to search the Advanced Intercompany Process Chain, for example, Outbound Delivery number, Intercompany Invoice number and so on. | Business Processes that match the search criteria are listed out. |  |
| 5 | Display the Advanced Intercompany Value Chain Process | Click the line item from the Business Processes list. | The Business Process screen displays. |  |
| 6 | Check the Status of the Advanced Intercompany Sales Value Chain Process | Check the value of the field Status on the screen, possible values could be from the list:Open: Value Chain is triggeredIn Process: Value Chain is in processingPending: Value Chain is pending for external processingProcessed with Errors: Error occurred when executing a process step by Value Chain ManagementReprocessing: Value Chain is under reprocessingCompleted: Value Chain is completed | The status of the intercompany sales value chain displays. |  |
| 7 | Display the Process Flow of the Advanced Intercompany Sales Value Chain Process | Choose Process Flow tab in Business Process screen, detailed process steps of Advanced Intercompany Sales value chain are displayed in a flow chart. Each process step is displayed as a node with the following data:Step Name, for example, Sales Order (SOSC)Business Document Number, for example, Sales Order (1234)Document Type, for example, Sales OrderDocument ID, for example, 1234Document Status, for example, CompletedNote Legend of the color of process node:Green: process step is CompletedRed: process step is in an ErrorGrey: process step is OpenOrange: process step is PendingBlue: process step is Scheduled | The Process Flow of the Advanced Intercompany Sales value chain process displays. |  |

##### Display Intercompany Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display or check intercompany purchase order of the advanced inter-company sales value chain.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Value Chains (F4854). | The Monitor Value Chains screen displays. |  |
| 3 | Adapt Searching Filter | Choose Adapt Filters, and the Adapt Filters dialog box pops up. Select Initiating Document, Processing Stage and Process Type, and choose OK. | Searching field Process Type displays. |  |
| 4 | Search Value Chain Process | Make the following entries and choose Go:Initiating Document: * + Sales Order number.Process Type : <Advanced Intercompany Sales> | Business Processes that match the search criteria are listed out. |  |
| 5 | Display the Advanced Intercompany Value Chain Process | Click the line item from the Business Processes list. | The Business Process screen displays. |  |
| 6 | Display Intercompany Purchase Order | Locate the line item for the step “IC Purchase Order (POIC)” from the Documents list, click the line item. | The Document screen displays. |  |
| 7 | Note Down the Purchase Order Number | Note down the Purchase Order number on the top of the screen. |  |  |

##### Display Intercompany Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display or check intercompany sales order of the advanced intercompany sales value chain.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Value Chains (F4854). | The Monitor Value Chains screen displays. |  |
| 3 | Adapt Searching Filter | Choose Adapt Filters, and the Adapt Filters dialog box pops up. Select Initiating Document, Processing Stage and Process Type, and choose OK. | Searching field Process Type displays. |  |
| 4 | Search Value Chain Process | Make the following entries and choose Go:Initiating Document: * + Sales Order number.Process Type: <Advanced Intercompany Sales> | Business Processes that match the search criteria are listed out. |  |
| 5 | Display the Advanced Intercompany Value Chain Process | Click the line item from the Business Processes list. | The Business Process screen displays. |  |
| 6 | Display Intercompany Sales Order | Locate the line item for the step “IC Sales Order (SOIC)” from the Documents list, click the line item. | The Document screen displays. |  |
| 7 | Note Down the Sales Order Number | Note down the Sales Order number on the top of the screen. |  |  |

##### Display Intercompany Supplier Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display or check supplier invoice of the advanced intercompany sales value chain.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Value Chains (F4854). | The Monitor Value Chains screen displays. |  |
| 3 | Adapt Searching Filter | Choose Adapt Filters, and the Adapt Filters dialog box pops up. Select Initiating Document, Processing Stage and Process Type, and choose OK. | Searching field Process Type displays. |  |
| 4 | Search Value Chain Process | Make the following entries and choose Go:Initiating Document: * + Sales Order number.Process Type: <Advanced Intercompany Sales> | Business Processes that match the search criteria are listed out. |  |
| 5 | Display the Advanced Intercompany Value Chain Process | Click the line item from the Business Processes list. | The Business Process screen displays. |  |
| 6 | Display Intercompany Sales Order | Locate the line item for the step “IC Supplier Invoice (SIIC)” from the Documents list, click the line item. | The Document screen displays. |  |
| 7 | Note Down the Supplier Invoice Number | Note down the Supplier Invoice number on the top of the screen. |  |  |

#### Schedule Resolution of Value Chain Issues (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to schedule a background job to resolve the value chain issues massively.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Resolution of Value Chain Issues (F6868). | The Application Jobs screen displays. |  |
| 3 | Create a New Application Job | Choose Create. | The New Job: Schedule Resolution of Value Chain Issues screen displays. |  |
| 4 | Select a Template | Make the following entries and choose Step 2:Job Template: Schedule Resolution of Value Chain IssuesJob Name: for example, Schedule Resolution of Value Chain Issues | The Scheduling Options screen displays. |  |
| 5 | Define One-time Scheduling Settings | Option 1:Start Immediately: SelectedOption 2:Start Immediately: UnselectedStart: Choose a date and time when this job is startedTime Zone: Choose the preferred time zone, for example, UTC+08 | One-time Scheduling Option is defined. |  |
| 6 | Define Recurrence Schedule Option | Choose Define Recurrence Pattern, make the following entries and choose OK:Job Start: A date and time when the job is started for the first timeTime Zone: for example, UTC+08Recurrence Pattern: WeeklyEvery: 1 Week(s)On: for example, FridayEnd: for example, AfterOccurrence(s): for example, 52On Non-Working Day: for example, No restrictionCalendar: Germany (Standard) | Recurrence Scheduling Option is defined. |  |
| 7 | Define Parameters | Choose Step 3, make the following entries and choose Check:Process Type: for example, IC_SALES and ICO_STOCKTRANSFERSystem runtime errors: SelectedBlocked event queues: SelectedBusiness process errors: SelectedChoose Schedule. | Resolution of Value Chain Issues job is scheduled. |  |
| 8 | Check Resolution of Value Chain Issues Job Log | Return to the Application Jobs screen.On the Application Jobs screen, after job item’s status turns to Finished, choose the status icon in the Log column.Note Choose Magnifier, and the job list is refreshed. | The Log Details list displays. |  |

## Appendix

### Scheduling Job (Alternative)

#### Schedule Job for Creation of Outbound Delivery (Alternative)

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist |  |  |
| 2 | Access the App | Open Schedule Delivery Creation (F2228) app. | The Application Jobs screen is displayed. The app automatically shows the history of application jobs. |  |
| 3 | Create Delivery Creation Schedule | Select Create to define a new job. | The New Job screen is displayed. The Job Template is defaulted as Schedule Delivery Creation. |  |
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary, then select Check. | The system message is displayed as You can go ahead and schedule the job. |  |
| 5 | Schedule | Select Schedule. | A delivery creation job is scheduled. Screen goes back to Application Jobs. |  |
| 6 | Check Delivery Creation Job Log | On the Application Jobs screen, after job item’s status turned to Finish, select Status symbol in the Log column.Note Select the Magnifier, and the job list will refresh. | The job log details display. |  |

#### Schedule Job for Goods Issue Deliveries (Alternative)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step explains you how to schedule a background job for goods issue posting with reference to outbound deliveries.

This app can be used as an alternative instead of the manual goods issue posting for outbound deliveries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Schedule Goods Issue For Deliveries (F2259) app. | The Application Jobs screen is displayed. The app automatically shows the history of application jobs. |  |
| 3 | Create Goods Issue Deliveries Schedule | Select Create to define a new job. | The New Job screen is displayed. The Job Template is defaulted as Schedule goods issue for Deliveries. |  |
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary, then select Check. | The system message is displayed as You can go ahead and schedule the job. |  |
| 5 | Schedule | Select Schedule. | A schedule goods issue for deliveries job is scheduled. The screen goes back to Application Jobs. |  |
| 6 | Check Goods Issue Deliveries Job Log | On the Application Jobs screen, after job item’s status turned to Finish, select Status symbol in the Log column.Note Select the Magnifier, and the job list will refresh. | The job log details are displayed. |  |

#### Schedule Job for Creation of Billing Documents (Alternative)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step explains you how to schedule a background job for creation of billing documents. Schedule Billing Creation (F1519) app can be used as an alternative instead of the manual creation of billing documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. |  |  |
| 2 | Access the App | Open Schedule Billing Creation (F1519) app. | The Application Jobs screen is displayed. The app automatically shows the history of application jobs. |  |
| 3 | Create Billing Creation Schedule | Select Create to define a new job for billing creation. | The New Job screen is displayed. Job Template is default as Schedule Billing Creation. |  |
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary.Select Check. | The system message is displayed You can go ahead and schedule the job. |  |
| 5 | Schedule | Select Schedule. | A billing creation job is scheduled. You are navigated to Application Jobs screen. |  |
| 6 | Check Billing Creation Job Log | On the Application Jobs screen, after job item’s status turned to Finish, select Job Log.Note Select the Magnifier, and the job list will refresh. | The log details display. |  |

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
> Flagged while digesting this document, not verified: Advanced intercompany Part 2 example mentions Sales Organization 1010, Tax Departure DE, transit plant 1010 and plant 1710, inconsistent with the 3310/AE/3350 sample data; and the Financial Posting rule cites Italian FI types (W1/W2/W3) and an invoice form template SDBIL_INVOICE_RU, inconsistent with the UAE scope.

## Connections
- part-of :: [[_cluster]]
- see-also :: [[15-retail-operations/outbound-logistics-for-distribution-centers-5fv-ae-test-script-1090]]
- see-also :: [[08-sales-order-management/test-script-advanced-intercompany-sales-5d2-ae-sap-s-4hana-cloud-publi]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3HS_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 133,281 chars in the whole document
