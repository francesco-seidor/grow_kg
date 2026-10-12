---
id: 15-retail-operations/test-script-value-added-services-for-retail-6nm-ae-sap-s-4hana-cloud-p
title: "Test Script: Value-Added Services for Retail (6NM_AE), SAP S/4HANA Cloud Public Edition (6NM_S4CLD2608_BPD_EN_AE)"
description: "SAP test script for scope item 6NM_AE: configuring and testing retail value-added services (VAS) across sales, purchasing and stock transfer, with sample data and roles."
cluster: 15-retail-operations
tags: [kb/retail-operations, topic/value-added-services-retail]
aliases: [6NM_S4CLD2608_BPD_EN_AE]
keywords: [Value-Added Services for Retail, value-added services, vas service types, charge codes, pricing procedures, vas characteristic combinations, sales order processing, purchase order processing, stock transfer orders, vas quantity correlation]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6NM_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1186
topic: 15-retail-operations/value-added-services-retail
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Value-Added Services for Retail (6NM_AE), SAP S/4HANA Cloud Public Edition (6NM_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6NM_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Value-Added Services for Retail** in Retail Operations. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Value-Added Services for Retail (6NM_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232859132)

[2 Prerequisites 4](#_Toc232859133)

[2.1 System Access 4](#_Toc232859134)

[2.2 Roles 4](#_Toc232859135)

[2.3 Master Data, Organizational Data, and Other Data 6](#_Toc232859136)

[2.4 Additional Manual Configuration (Optional) 7](#_Toc232859137)

[2.5 Business Conditions 7](#_Toc232859138)

[2.6 Preliminary Steps 8](#_Toc232859139)

[2.6.1 Maintain Service Types and Subservice Types 8](#_Toc232859140)

[2.6.2 Set Initial Stock for Material 8](#_Toc232859141)

[2.6.3 VAS Quantity Correlation (Optional) 10](#_Toc232859142)

[2.6.3.1 Maintain VAS Controls for Delivery Types 10](#_Toc232859143)

[2.6.3.2 Update VAS Article with MRP Parameters 10](#_Toc232859144)

[2.6.4 Charge Code (Optional) 12](#_Toc232859145)

[2.6.4.1 Define Charge Code 13](#_Toc232859146)

[2.6.4.2 Maintain Sales Pricing Condition Records for Charge Code 14](#_Toc232859147)

[2.6.4.3 Maintain Purchase Pricing Condition Records for Charge Code 14](#_Toc232859148)

[2.6.4.4 Maintain Pricing Procedure for Sales Process 15](#_Toc232859149)

[2.6.4.5 Assign Condition Type to Pricing Procedure for Sales 16](#_Toc232859150)

[2.6.4.6 Assign Condition Type to Pricing Procedure for Purchasing 19](#_Toc232859151)

[2.6.4.7 Maintain Pricing Procedure for Purchasing 21](#_Toc232859152)

[2.6.5 Identify Characteristics Using Manage Characteristic Catalog App 22](#_Toc232859153)

[2.6.6 Configure VAS Characteristic Combinations 23](#_Toc232859154)

[2.6.7 Display VAS Characteristic Combination (Optional) 26](#_Toc232859155)

[3 Overview Table 27](#_Toc232859156)

[4 Test Procedures 29](#_Toc232859157)

[4.1 Sales Document Processing 29](#_Toc232859158)

[4.1.1 Sales Order Processing 29](#_Toc232859159)

[4.1.1.1 Create Sales Order 29](#_Toc232859160)

[4.1.1.2 Create an Outbound Delivery 31](#_Toc232859161)

[4.1.1.3 Display Delivery Document using Display Outbound Delivery Application (Optional) 33](#_Toc232859162)

[4.1.1.4 Process Picking for Outbound Delivery 34](#_Toc232859163)

[4.1.1.5 Post Goods Issue for Outbound Delivery 35](#_Toc232859164)

[4.1.1.6 Create Billing Document with Reference to Outbound Delivery 36](#_Toc232859165)

[4.1.1.7 Display Billing Document (Optional) 38](#_Toc232859166)

[4.2 Purchase Document Processing 39](#_Toc232859167)

[4.2.1 Purchase Order Processing 39](#_Toc232859168)

[4.2.1.1 Create Purchase Order 39](#_Toc232859169)

[4.2.1.2 Display Purchase Order (Optional) 41](#_Toc232859170)

[4.2.1.3 Create Inbound Delivery 43](#_Toc232859171)

[4.2.1.4 Display Inbound Delivery Document (Optional) 44](#_Toc232859172)

[4.2.1.5 Confirm Quantities for Putaway 46](#_Toc232859173)

[4.2.1.6 Post Goods Receipt for Inbound Delivery 47](#_Toc232859174)

[4.2.1.7 Create Supplier Invoice using Purchase Order 48](#_Toc232859175)

[4.2.1.8 Display Supplier Invoice 50](#_Toc232859176)

[4.2.2 Stock Transfer Order Processing 50](#_Toc232859177)

[4.2.2.1 Create Stock Transfer Order 50](#_Toc232859178)

[4.2.2.2 Display Stock Transfer Order (Optional) 52](#_Toc232859179)

[4.2.2.3 Create Replenishment Delivery for Stock Transfer Order 53](#_Toc232859180)

[4.2.2.4 Display Outbound Delivery Document (Optional) 54](#_Toc232859181)

[4.2.2.5 Pick, Pack, and Post Goods Issue for Delivery 55](#_Toc232859182)

[5 Appendix 57](#_Toc232859183)

[5.1 Optional Scenarios 57](#_Toc232859184)

[5.1.1 Monitor EDI Message Summary for the Purchase Order 57](#_Toc232859185)

[5.1.2 Create Value-Added Service Articles 58](#_Toc232859186)

## Purpose

Overview

Customers often request price labels, custom packaging, or other special services for their orders, which must be completed before delivery. These value-added services (VAS) are essential in retail, especially to meet specific customer expectations. Fulfilling VAS typically requires additional products (materials), expertise, or personnel, and may therefore incur a surcharge.

For example, a customer may order slacks and skirts and request that they be packed separately. Due to the delicate nature of the skirts, the customer specifies that no more than ten be packed per carton. In the system, this packing requirement can be defined as a service type, along with the maximum quantity per carton. A surcharge may be applied to cover the additional handling effort.

This business process covers the configuration and processing of VAS types and subservice types in the order-to-cash, procure-to-pay, and stock transfer processes.

VAS-related costs can be managed using charge codes, which are maintained independently of material pricing and applied as pricing conditions in sales or purchase orders. These codes specify surcharges based on the service’s complexity or resource requirements.

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
| Configuration Expert - Business Network Integration (Optional) | SAP_BR_CONF_EXPERT_BUS_NET_INT | Business Network Integration / Business Network Integration - Concur Integration / Business Network Integration - Output Control / Business Network Integration - Data Replication / Configuration Expert - Business Network Integration Cross Applications | SAP_CORE_SPT_INT_PC / SAP_CON_SPT_CONCUR_INT_PC / SAP_OC_SPT_INT_PC / SAP_CA_SPT_DATA_REP_PC / SAP_CA_SPT_BUS_NETWORK_INT_PC |  |
| Master Data Specialist - Business Partner Data (Optional) | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |
| Administrator (Optional) | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |
| Order Fulfillment Manager (Retail) | SAP_BR_ORDER_FLFMT_MGR_RFM | Order Fulfillment Manager (Retail) | SAP_BR_ORDER_FLFMT_MGR_RFM |  |

|  |
| --- |
| Note The optional roles need to be assigned to the test users only if they need to implement the additional setup instructions mentioned in [Additional Manual Configuration (Optional)](#unique_5) [page ] 7. |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Customer | 33113007 | Wholesale non-Food AE |  |
| Generic Product | R_1080 | Cycling Jersey Longsleeve |  |
| Product Variants | R_1080001 | Cycling Jersey Longsleeve, S, BLACK |  |
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
| VAS Article | R_8000 | Hanger |  |
| Condition Type for Sales | EPV1 | VAS - Costs |  |
| Condition Type for Purchasing | EPV2 | VAS - Costs |  |

|  |
| --- |
| Note To create your own VAS article, refer [Create Value-Added Service Articles](#unique_7) [page ] 58. |

### Additional Manual Configuration (Optional)

You must complete certain additional setup instructions for the communication scenario SAP_COM_0224 for sourcing and procurement with suppliers integration to perform the steps described in [Monitor EDI Message Summary for the Purchase Order](#unique_8) [page ] 57. These setup instructions are specific to your implementation and contain mandatory settings that are not delivered by SAP and must be created by you.

The following setup instructions described in [Setting Up Integration of Procurement with External Suppliers (2EJ)](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/Setup/2EJ_Set-Up_EN_XX.pdf) must be completed if you want to use the SAP Application Interface Framework to monitor XML messages and perform related troubleshooting activities using the Message Dashboard (/AIFX/WDA_MSG_MONITOR) Fiori application:

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 3I1 - Products for Retail | Products must be created before assigning value-added services. |
| 3I4 - Sales Pricing for Retail | Sales price must be created for generic articles and variant articles if they do not already exist. |

### Preliminary Steps

#### Maintain Service Types and Subservice Types

Purpose

Use this configuration activity to create or define value-added service types and subservice types, which in turn are used in sales documents, purchasing documents, and stock transfer documents to assign the services and subservices frequently requested by the customers.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Project Experience in SAP Central Business Configuration. |  |  |
| 2 | Open Business Processes Configuration | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Maintain Service Types and Subservice Types (106837).Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Maintain Service Types and Subservice Types screen is displayed. |  |
| 3 | Maintain Service and Subservice Types | Choose New Entries.Enter values for Service and Subservice.For example:Service Type: 10 – Gift WrappingSubservice Type: 10-1 - Birthday |  |  |
| 4 | Save the Configuration | Choose Save. | The configuration is saved. |  |

Result

You have defined the value-added service and subservice types.

#### Set Initial Stock for Material

Use

To execute this scope item, the materials must be available in stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk (Retail). |  |  |
| 2 | Access the App | Open Post Goods Movement (MIGO) app.It only displays if it was your last transaction. So, the action for the user is to select Reference Document for MIGO Transaction > Other . | The Goods Receipt Other screen is displayed. |  |
| 3 | Input Movement Type | Make the following entries and select Enter.Executable Action in Transaction MIGO: Goods ReceiptReference Document for MIGO Transaction: Other |  |  |
| 4 | Enter Material | On the Goods Receipt Other Screen: Material tab, make the following entry and select Enter:Material: R_1080 or R_1080001 and R_8000. |  |  |
| 5 | Enter Quantity Data | On the Goods Receipt Other screen: Quantity tab, make the following entry and select Enter:Qty in Unit of Entry: <Quantity in UOM>Unit of Entry: <UoM of material> |  |  |
| 6 | Input on the Goods Receipt Other screen: Where tab | On the Goods Receipt Other screen: Where tab, make the following entries and select Enter:Movement Type: 561Receipt per initial entry of stock balances into unrestricted usePlant: 3350Storage Location: 995ANote If generic article is entered as the material then you should enter quantity in the variant matrix grid which appears on expanding the tree display for the material.Else, enter the variant article as the material for which stock needs to be created as generic articles are logical entities which are not entitled for physical stocks creation. |  |  |
| 7 | Save Entries | Select Post. | Material document <document number> posted success message is displayed. |  |

Result

You have created stock for the materials.

#### VAS Quantity Correlation (Optional)

##### Maintain VAS Controls for Delivery Types

Purpose

Use this configuration activity to enable VAS quantity correlation in deliveries, that is, whether the delivery quantity of the main item and its corresponding VAS items must be correlated in delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Project Experience in SAP Central Business Configuration. |  |  |
| 2 | Open Business Processes Configuration | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define VAS Controls for Delivery Types (ID: 107016).Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define VAS Controls for Delivery Types screen is displayed. |  |
| 3 | Maintain VAS Controls for Delivery Types | Choose and double- click on delivery type LF.Enable VAS Correlation. |  |  |
| 4 | Save the Configuration | Choose Save. | The configuration is saved. |  |

Result

You have enabled VAS quantity correlation.

##### Update VAS Article with MRP Parameters

Purpose

With this process step, you can update value-added service (VAS) articles with MRP parameters using the Maintain Article (MM42) app or the Manage Product Master Data (F1602) Fiori app.

This is essential when using the VAS quantity correlation functionality.

Procedure

Using Maintain Article (MM42) Application

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data (Retail). |  |  |
| 2 | Access the SAP Fiori App | Open Maintain Article (MM42) app. | The Maintain Material (Initial Screen) is displayed. |  |
| 3 | Enter Article | In the Maintain Material (Initial screen), enter the following details:Material: R_8000Purchasing Org.: 3310Supplier: 33213004Sales Org.: 3310Distr. Channel: 10 |  |  |
| 4 | Choose Views | Select view Logistics: Distribution Center.Choose Continue. | Change Material R_8000(Logistics Distribution Center) screen is displayed. |  |
| 5 | Maintain MRP Parameters | Choose Switch Validity Area.Under Areas of Validity section, enter Distr. Center: 3350Maintain the following details under MRP Parameters:MRP Type: R1 (Time-Phased Planning)Lot Sizing Proc.: EX (Lot-for-lot order quantityMaintain the following details under MRP Controller/Replenishment Data:MRP Controller: 001 (MRP Controller 001)Planning Cycle: P01 (Order Day Monday) |  |  |
| 6 | Save Article | Choose Save. | The VAS article with MRP parameters is saved. | You can view the article created above using the Display Article (MM43) app. |

Using Manage Product Master Data (F1602) Application

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data (Retail). |  |  |
| 2 | Access the SAP Fiori App | Open Manage Product Master Data (F1602). | The Manage Product Master Data (F1602) screen is displayed. |  |
| 3 | Enter Article | In the Manage Product Master Data screen, enter the following details:Product: R_8000Choose Go. |  |  |
| 4 | Maintain MRP Parameters | Choose > to navigate to the product object page.Choose Distribution Centers tab.Choose > next to the distribution center 3350 to navigate to the distribution center object page.Choose MRP Data tab.Choose Edit.Maintain the following details under MRP Data:MRP Type: Time-Phased Planning (R1)MRP Controller: MRP Controller 001 (001)Planning Cycle: Order Day Monday (P01)Maintain the following details under Lot-Size Data:Lot Sizing Procedure: Lot-for-lot order quantity (EX) |  |  |
| 5 | Return to Main Screen | Choose Apply to return to Product screen. | The Product screen displays. |  |
| 6 | Save Your Data | Choose Save. | The VAS article with MRP parameters is saved. |  |

Result

You have maintained MRP parameters for the VAS article. These parameters ensure that VAS quantity correlation is respected in the delivery documents.

#### Charge Code (Optional)

Purpose

Customers or suppliers may be required to pay an additional surcharge for any requested value-added service. This payment varies depending on the effort required to carry out the value-added service, how much time is needed, and which materials you must provide and use. You can define such payments using the charge codes to which you can assign the corresponding pricing conditions.

|  |
| --- |
| Note All the steps pertaining to charge code are optional. If charge code is maintained, then the item pricing condition in the sales document and the purchase document is supplemented by the additional charge code pricing conditions maintained in the corresponding configuration activities. |

##### Define Charge Code

Purpose

Use this configuration activity to maintain charge codes which in turn are used in sales documents and purchasing documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Project Experience in SAP Central Business Configuration. |  |  |
| 2 | Open Business Processes Configuration | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Charge Code (ID: 107060).Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Charge Code : Display screen is displayed. |  |
| 3 | Maintain Charge Code | Choose New Entries.Enter values for Charge Code and Charge Code Description.For example:Charge Code: C01Charge Code Description: Charge code 01 |  |  |
| 4 | Save the Configuration | Choose Save. | The configuration is saved. |  |

Result

You have maintained the charge code.

##### Maintain Sales Pricing Condition Records for Charge Code

Purpose

With this process step, you maintain pricing condition records for charge code in sales documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Pricing Specialist (Retail). | The SAP Fiori launchpad appears. |  |
| 2 | Access the App | Open Manage Prices - Sales (F4111). | The Manage Prices - Sales screen is displayed. |  |
| 3 | Enter Condition Records | Choose Create.Enter the following details:Condition Type: EPV1Condition Table: 4ACVAS Charge Code: C01 or <any charge code created earlier>Sales Organization: 3310Distribution Channel: 10Valid From: <Enter in DD.MM.YYYY Format>Valid To: <Enter in DD.MM.YYYY Format>Condition Amount or Ratio : <Enter amount>Pricing Unit: <User Specific>Calculation Type: Quantity(C) |  |  |
| 4 | Save Your Entries | Choose Save. | Sales pricing condition record is maintained. |  |

Result

You have maintained the sales pricing condition records.

##### Maintain Purchase Pricing Condition Records for Charge Code

Purpose

With this process step, you maintain pricing condition records for charge code in purchasing documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data (Retail). | The SAP Fiori launchpad appears. |  |
| 2 | Access the App | Open Create Price Conditions - Purchasing (MEK1). | The Create Condition Records screen is displayed. |  |
| 3 | Enter Condition Records | Enter Condition Type:EPV2Press EnterOn the Create VAS - Costs Condition (EPV2) : Fast Entry screen, enter the following details:Purch. Organization: 3310Charge Code: C01 or <any charge code created earlier>Amount: <Enter amount>Valid From: <Enter in DD.MM.YYYY Format>Valid To: <Enter in DD.MM.YYYY Format> |  |  |
| 4 | Save Your Entries | Choose Save. | Purchase pricing condition record is maintained. |  |

Result

You have maintained the purchase pricing condition records.

##### Maintain Pricing Procedure for Sales Process

Purpose

With this process step, you maintain the pricing procedure value which is used in pricing calculations of sales documents

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Project Experience in SAP Central Business Configuration. |  |  |
| 2 | Open Business Processes Configuration | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Set Pricing Procedure Determination (ID: 101118).Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Set Pricing Procedure Determination : Change screen is displayed. |  |
| 3 | Maintain Pricing Procedure Value | Search the pricing procedure for the following combination of values:Sales Organization: 3310Distribution Channel: 10Division: 00Doc. Pricing Proc.: <As identified earlier> (See 1. Identify Document Pricing Procedure of [Assign Condition Type to Pricing Procedure for Sales](#unique_19) [page ] 16)Cust. Pricing procedure: <As identified earlier> (See 2. Identify Customer Pricing Procedure (Optional) of [Assign Condition Type to Pricing Procedure for Sales](#unique_19) [page ] 16)Replace the existing value in Pricing Procedure field for the above combination with the following value:Pricing Procedure: Z* <created earlier> (See 3. Identify Pricing Procedure of [Assign Condition Type to Pricing Procedure for Sales](#unique_19) [page ] 16) |  |  |
| 4 | Save the Configuration | Choose Save. | The configuration is saved. |  |

Result

You have maintained the pricing procedure for sales.

##### Assign Condition Type to Pricing Procedure for Sales

Purpose

With this process step, you assign condition type to pricing procedure which is used in pricing calculations of sales documents.

Procedure

1. Identify Document Pricing Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Project Experience in SAP Central Business Configuration. |  |  |
| 2 | Open Business Processes Configuration | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Configure Sales Document Types (ID: 102495).Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Sales Document Types : Change screen is displayed. |  |
| 3 | Identify Document Pricing Procedure | Select sales document type OR and choose Details.Under General Settings, check the value for Doc. Pricing. Proc..Note down this value for future use. |  |  |

2. Identify Customer Pricing Procedure (Optional)

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Project Experience in SAP Central Business Configuration. |  |  |
| 2 | Open Business Processes Configuration | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Set Customer Pricing Procedures (ID: 101202).Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Set Customer Pricing Procedures : Change screen is displayed. |  |
| 3 | Identify Customer Pricing Procedure | Note down the defined customer pricing procedure value under Cust.Pric.Procedure. |  |  |

3. Identify Pricing Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Project Experience in SAP Central Business Configuration. |  |  |
| 2 | Open Business Processes Configuration | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Set Pricing Procedure Determination (ID: 101118).Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Set Pricing Procedure Determination : Change screen is displayed. |  |
| 3 | Identify Pricing Procedure | Note down the pricing procedure for the following combination of values:Sales Organization: 3310Distribution Channel: 10Division: 00Doc. Pricing Proc.: <As identified above in 1. Identify Document Pricing Procedure>Cust. Pricing procedure: <As identified above in 2. Identify Customer Pricing Procedure (Optional)> (optional) | The pricing procedure is identified. |  |

4. Assign Condition Type to Pricing Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Project Experience in SAP Central Business Configuration. |  |  |
| 2 | Open Business Processes Configuration | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Set Pricing Procedures (ID: 101117).Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Set Pricing Procedures : Change screen is displayed. |  |
| 3 | Assign Condition Type to Pricing Procedure | Select pricing procedure as identified from subsection 2.Choose Copy As and provide any Z* name under the Procedure field.Choose Copy.Specify object to be copied pop-up is displayed.Choose copy all.A message pop up is displayed.Choose continue.Select the procedure Z*.Double-click Procedure - Control Data on the left side panel.In the Procedure- Control Data table, maintain the following values:Step Number: any number between 700 and 800, for example, 761Counter: 0Condition Type: EPV1Print Type: a (at item: General)Requirement: 440 (VAS Price)Account Key: ERL (Revenue) |  |  |
| 4 | Save the Configuration | Choose Save. | The configuration is saved. |  |

Result

You have assigned the condition type EPV1 for the sales pricing procedure.

##### Assign Condition Type to Pricing Procedure for Purchasing

Purpose

With this process step, you assign condition type to pricing procedure which is used in pricing calculations of purchase documents.

Procedure

1. Identify the Pricing Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Project Experience in SAP Central Business Configuration. |  |  |
| 2 | Open Business Processes Configuration | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Determination of Calculation Schema in Purchasing (ID: 102144)..Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Determination of Calculation Schema in Purchasing: Change screen is displayed. |  |
| 3 | Identify Pricing Procedure | Note down the pricing procedure for the following combination of values:Schema GrpPOrg: 3310Sch. Grp Supp: GP | The pricing procedure/schema is identified. |  |

2. Assign Condition Type to Pricing Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Project Experience in SAP Central Business Configuration. |  |  |
| 2 | Open Business Processes Configuration | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Set Calculation Schema – Purchasing (ID: 101095).Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Set Calculation Schema – Purchasing : Change screen is displayed. |  |
| 3 | Assign Condition Type to Pricing Procedure/Schema | Select pricing procedure as identified from subsection 1.Choose Copy As and provide any Z* name under the Procedure field.Choose Copy.Specify object to be copied pop-up is displayed.Choose copy all.A message pop up is displayed.Choose continue.Select the procedure Z*.Double-click Control Data on the left side panel.On the Control Data screen, maintain the following values:Step Number: any number between 700 and 800, for example, 761Counter: 0Condition Type: EPV2Print Type: a (at item: General)Requirement: 440 (VAS Price) |  |  |
| 4 | Save the Configuration | Choose Save. | The configuration is saved. |  |

Result

You have assigned the condition type EPV2 for the purchasing pricing procedure.

##### Maintain Pricing Procedure for Purchasing

Purpose

With this process step, you maintain the pricing procedure value which is used in pricing calculations of purchasing documents

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Project Experience in SAP Central Business Configuration. |  |  |
| 2 | Open Business Processes Configuration | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Determination of Calculation Schema in Purchasing (ID: 102144)..Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Determination of Calculation Schema in Purchasing: Change screen is displayed. |  |
| 3 | Maintain Pricing Procedure Value | Search the pricing procedure for the following combination of values:Schema GrpPOrg: 3310Sch. Grp Supp: GPReplace the existing value in Proc. field for the above combination with the following value:Proc.: Z* <created earlier> (See point 2 of [Assign Condition Type to Pricing Procedure for Purchasing](#unique_20) [page ] 19) |  |  |
| 4 | Save the Configuration | Choose Save. | The configuration is saved. |  |

Result

You have maintained the pricing procedure for purchasing.

#### Identify Characteristics Using Manage Characteristic Catalog App

Purpose

With this process, you can identify characteristics using the Manage Characteristic Catalogs (F3829) app. These characteristics are then used in the Configure VAS Characteristic Combinations (F8623) app to create VAS characteristic combinations.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Order Fulfillment Manager (Retail). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access app | Open Manage Characteristic Catalogs (F3829). | The Manage Characteristic Catalogs (F3829)screen is displayed. |  |
| 3 | Open Catalog Type Base (Purchasing Document) belonging to Retail Fashion Management | Open Catalog Type Base (purchasing document) for Catalog Use Type Retail Fashion Management.Choose Edit if you want to change the listed characteristics.Choose Add to add characteristics.Select the required characteristics from Select Characteristics pop-up.Choose OK.Choose Save.NoteTo remove any characteristic, select the characteristic and choose Remove.Characteristics in a catalog can only be removed when it is not used in VAS characteristic combination.If the Value Existence Check Type is set to Check with Error, an error message should be displayed when deleting the characteristic.If the Value Existence Check Type is set to Check with Warning, a warning message should be displayed when deleting the characteristic.Choose Save. | The newly added characteristics are available for the selected catalog type. |  |

Result

The newly added characteristics are available for selected catalog type to be used in the Configure VAS Characteristic Combinations (F8623) app.

#### Configure VAS Characteristic Combinations

Purpose

With this procedure, you can create VAS characteristic combinations using the Configure VAS Characteristic Combinations (F8623) app. These characteristic value combinations are necessary for the automatic VAS determination in purchase orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Order Fulfillment Manager (Retail). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access app | Open Configure VAS Characteristic Combinations (F8623). | The Configure VAS Characteristic Combinations (F8623) screen is displayed. |  |
| 3 | Add General Information | Select Create.In the Characteristic Combination section, enter the below details in General Information section:VAS Characteristics Combination: SupplierDescription: Supplier |  |  |
| 4 | Assign Characteristics | In the Assigned Characteristics section.Select Add.Select the Select button in the Characteristics field.Select for example, Supplier.NoteThe characteristics listed in the Characteristics field are based on the characteristics added using the Manage Characteristic Catalogs (F3829) mentioned in [Identify Characteristics Using Manage Characteristic Catalog App](#unique_22) [page ] 22.Select Manage Characteristic Catalogs (F3829) to navigate to the app home page.A maximum of 5 characteristics can be added.The Sequence field is updated automatically.Characteristics cannot be added or removed if characteristic value combinations are maintained.Characteristics cannot be added or removed if the VAS characteristic combinations is in use. | The selected characteristics are available in the Assigned Characteristics section.The chosen characteristic Supplier is available as a column in the table under section Characteristics Value Combinations. |  |
| 5 | Create VAS Characteristic Combination: Add Characteristics Value Combinations | Select Add in the Characteristic Value Combinations section .Follow the below steps in the Characteristics Value Combinations screen.In the Characteristic Value Combinations section, make the following entries:Select Select button in Supplier field and select the required value, for example, 33213004Select Default if you want to make this characteristics value combination as a default combination.Enter Valid From and Valid To date fields if you want to set a specific date range. |  |  |
| 6 | Create VAS Characteristic Combination: Add Service Details | In the Service Details section, select Add.In the following screen, enter the following details:Service: 10 Gift wrappingSubservice: 10-1 BirthdayCharge Code: C01 or <any defined charge code> (optional)Supplementary Product: <VAS Material>(optional)Round Down Indicator: <Unchecked by default>(optional)Order Quantity Multiplier: <Multiplier Value>(For example: 1,2 and so on) (optional)NoteFor each characteristic value combination, one or more VAS Service/Subservice can be maintained but one VAS Service and Subservice is mandatory.The fields Order Quantity Multiplier and Round Down Indicator are optional and only relevant when a Supplementary Product is provided.By default, the value of Order Qty Multiplier is 1.In the Service Text section,Select Add.In the pop-up, enter language: <User- specific language> (optional).Select Continue.In the subsequent screen, enter Instruction: <User- specific instruction> or <long description>(optional).Select Apply.In the Service Details screen, Select Apply. |  |  |
| 7 | Change Status | Select Change Status button available on the top of the screen.Note To change the status of an existing VAS characteristic combination,1.Select the VAS characteristic combination.2. Select Change Status button available on the top of the screen.. | The status of VAS characteristic combination Supplier is set to ActiveNoteVAS characteristic combination can be active only when characteristic value combinations have been maintained.By default, the created VAS characteristic combination is in status Inactive. |  |
| 8 | Create VAS Characteristic Combination: Create | Once all entries are in place, Select Create. | The VAS characteristic combination is created. |  |
| 9 | Change Priority (Optional) | The priority for a VAS characteristic combination is set automatically in the sequence that it was created.To change the priority, select a VAS characteristic combination.Select the down arrow next to Create to decrease the priority of the combination.Select the up arrow next to Create to increase the priority of the combination.NoteFor combination with priority 1, only the down arrow is enabled.For combinations with other priority, both the up and down arrows are enabled. |  |  |

Result

The VAS characteristic combination is created. The created VAS characteristic combination can now be used during VAS determination in purchase documents.

#### Display VAS Characteristic Combination (Optional)

Purpose

With this process, you can display the VAS characteristic combinations created earlier.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Order Fulfillment Manager (Retail). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access app | Open Configure VAS Characteristic Combinations (F8623). | The Configure VAS Characteristic Combinations (F8623) initial screen is displayed. |  |
| 3 | Display VAS Characteristic Combination | Search for the VAS combination Supplier in the Search field.Choose >. | Details of VAS characteristic combination Supplier are displayed.Status: ActiveAssigned Characteristics section has the characteristics Supplier.Characteristic Value Combinations section has the below details:VAS Status: GreenSupplier: 33213004Default: YesValid From: <DD.MM.YYYY>, (for example, 06.10.2025)Valid To: <DD.MM.YYYY>, (for example, 06.10.2025) |  |

Result

The VAS characteristic combination values are validated.

## Overview Table

This scope item consists of several process steps that are listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Sales Document Processing

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Sales Order](#unique_26) [page ] 29 | Internal Sales Representative | Create Sales Orders - VA01 (VA01) | Sales order is created with value-added service items. |
| [Create an Outbound Delivery](#unique_27) [page ] 31 | Shipping Specialist | Create Outbound Deliveries (F0869A) | Outbound delivery is created with value-added service items. |
| [Display Delivery Document using Display Outbound Delivery Application (Optional)](#unique_28) [page ] 33 | Shipping Specialist | Display Outbound Delivery (VL03N) | Outbound delivery is displayed with value-added service items copied from sales order. |
| [Process Picking for Outbound Delivery](#unique_29) [page ] 34 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Picking is performed on the outbound delivery. |
| [Post Goods Issue for Outbound Delivery](#unique_30) [page ] 35 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Goods issue is performed on the outbound delivery. |
| [Create Billing Document with Reference to Outbound Delivery](#unique_31) [page ] 36 | Billing Clerk | Create Billing Documents (F0798) | Billing document is created with value-added service items copied from outbound delivery. |
| [Display Billing Document (Optional)](#unique_32) [page ] 38 | Billing Clerk | Manage Billing Document (F2250) | Billing document is displayed with value-added service items copied from outbound delivery. |

Purchase Document Processing

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Purchase Order](#unique_33) [page ] 39 | Purchaser | Create Purchase Order - Advanced (ME21N) | Purchase order is created with value-added service items. |
| [Display Purchase Order (Optional)](#unique_34) [page ] 41 | Purchaser | Display Purchase Order - Advanced (ME23N) | Purchase order is displayed with value-added service items. |
| [Create Inbound Delivery](#unique_35) [page ] 43 | Receiving Specialist | Create Inbound Delivery (VL31N) | Inbound delivery is created with value-added service items copied from purchase order. |
| [Display Inbound Delivery Document (Optional)](#unique_36) [page ] 44 | Receiving Specialist | Display Inbound Delivery (VL33N) | Inbound delivery is displayed with value-added service items copied from purchase order. |
| [Confirm Quantities for Putaway](#unique_37) [page ] 46 | Receiving Specialist | Change Inbound Delivery (VL32N) | Inbound delivery document is updated with confirmed putaway quantities. |
| [Post Goods Receipt for Inbound Delivery](#unique_38) [page ] 47 | Warehouse Clerk | Post Goods Movement (MIGO) | Goods receipt is posted for the inbound delivery when goods arrive at the disribution centre. |
| [Create Supplier Invoice using Purchase Order](#unique_39) [page ] 48 | Accounts Payable Accountant | Create Supplier Invoice - Advanced (MIRO) | Invoice is generated. |
| [Display Supplier Invoice](#unique_40) [page ] 50 | Accounts Payable Accountant | Display Supplier Invoice - Advanced (MIR4) | Invoice and follow-on documents are displayed. |

Stock Transfer Order Document Processing

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Stock Transfer Order](#unique_41) [page ] 50 | Purchaser | Create Purchase Order - Advanced (ME21N) | Stock transfer order is created with value-added service items. |
| [Display Stock Transfer Order (Optional)](#unique_42) [page ] 52 | Purchaser | Display Purchase Order - Advanced (ME23N) | Stock transfer order is displayed with the value-added service items. |
| [Create Replenishment Delivery for Stock Transfer Order](#unique_43) [page ] 53 | Shipping Specialist | My Purchase Orders - Due for Delivery (VL10B) | Outbound delivery document with reference to stock transfer order is created. |
| [Display Outbound Delivery Document (Optional)](#unique_44) [page ] 54 | Shipping Specialist | Change Outbound Delivery (VL02N) | Outbound delivery is displayed with the value-added service items copied from stock transfer order. |
| [Pick, Pack, and Post Goods Issue for Delivery](#unique_45) [page ] 55 | Shipping Specialist | Change Outbound Delivery (VL02N) | Material is picked then packed. Handling units are generated. Goods issue is posted for the outbound delivery. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

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
| 4 | Enter Data | In the header section, enter:Sold-to Party: 33113007Ship-to Party: 33113007In the All Items table, enter the following details:Material: R_1080 or R_1080001Order Quantity: <Order quantity in piece (PC)>Plant: 3350Press ENTER.Note If you only enter the generic product, the order quantity must be filled in the variant matrix for the required variants. |  |  |
| 5 | Enter VAS Details | Select an item and choose the Value-Added Services button or choose Menu > Goto > Value-Added Service > VAS Details.On the Value-Added Services dialog, choose the Append Row button.Enter the following mandatory fields:VAS Service Types: 10VAS Sub Services : 10-1The following fields are optional:Supplementary Product : R_8000Order Quantity Multiplier: <Multiplier Value> (For example: 1,2, and so on )VAS Charge Code: C01 or <any defined charge code>Round Down Quantity: <Not selected by default>Instruction: <User-specific Instruction>Long Text : <User-specific Long Text>VAS Item number: <Item Number> (populated automatically when dialog is reopened)Choose Continue | The VAS details are included for the selected item.NoteIf the Round Down Quantity checkbox is selected, the VAS item quantity is rounded to the lower value if the calculated VAS item quantity is in decimals. By default (checkbox not selected), this quantity is always rounded to the higher value.If a supplementary product is maintained in the VAS dialog box, the Net Value field on the Create Standard Order: Overview screen is updated according to the sales price maintained for the supplementary product.If a charge code is maintained for the VAS data or VAS instruction in the VAS dialog box, the Net Value field on the Create Standard Order: Overview screen is updated according to the sales pricing configuration maintained in preliminary steps.The combination of supplementary product and the VAS charge code is not allowed in VAS dialog box. |  |
| 6 | Save Order | Choose Save. | Sales order is saved, and a standard order has been saved success message is displayed. |  |

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
| 3 | Display Delivery | In the Outbound Delivery field, enter Delivery and choose Continue. | Overview of delivery document is displayed.Note If the VAS Correlation checkbox is enabled as mentioned in [Maintain VAS Controls for Delivery Types](#unique_12) [page ] 10, the outbound delivery has the confirmed quantity of the main item and the VAS item in an appropriate ratio.If the confirmation of the main item is less than the ordered quantity and the VAS item confirmation corresponds to the ordered quantity in the sales order, the VAS item in the outbound delivery gets adjusted accordingly to the confirmed main item quantity. The same applies the other way around. |  |
| 4 | Display VAS Details | Select an item.Choose the Value-Added Services button or choose Menu > Goto > Value-Added Service > VAS Details. | The following VAS details are displayed on the Value-Added Services dialog and the same are validated:VAS Service Types: 10VAS Sub Services : 10-1Supplementary Product : R_8000 (if entered earlier)Order Quantity Multiplier: <Multiplier Value> (For example: 1,2, and so on ) (if entered earlier)VAS Charge Code: C01 or <any defined charge code> (if entered earlier)Round Down Quantity: <Not selected by default> (if not selected earlier)Instruction: <User-specific Instruction> (if entered earlier)Long Text : <User-specific Long Text> (if entered earlier) |  |

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
| 5 | Change Outbound Deliveries | On the Day’s Workload for Picking, select <your delivery number> and choose Change Outbound Deliveries. | The Outbound Delivery xxx Change: Overview screen is displayed.Note If the VAS Correlation checkbox is enabled as mentioned in [Maintain VAS Controls for Delivery Types](#unique_12) [page ] 10, the outbound delivery has the confirmed quantity of the main item and the VAS item in an appropriate ratio.If the confirmation of the main item is less than the ordered quantity and the VAS item confirmation corresponds to the ordered quantity in the sales order, the VAS item in the outbound delivery gets adjusted accordingly to the confirmed main item quantity. The same applies the other way around. |  |
| 6 | Check VAS Details (Optional) | Select an item.Choose the Value-Added Services button or choose Menu > Goto > Value-Added Service > VAS Details. | The following VAS details are displayed on the Value-Added Services dialog and the same are validated:VAS Service Types: 10VAS Sub Services : 10-1Supplementary Product : R_8000 (if entered earlier)Order Quantity Multiplier: <Multiplier Value> (For example: 1,2, and so on ) (if entered earlier)VAS Charge Code: C01 or <any defined charge code> (if entered earlier)Round Down Quantity: <Not selected by default> (if not selected earlier)Instruction: <User-specific Instruction> (if entered earlier)Long Text : <User-specific Long Text> (if entered earlier) |  |
| 7 | Enter Picked Quantity | Enter <quantity equal to delivery Qty> in Picked Qty field for picking related item(s). |  |  |
| 8 | Press Enter | Press Enter. |  |  |
| 9 | Choose Save | Choose Save. | A message confirms that the outbound delivery is saved. |  |

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
| 6 | Maintain Billing Date | Select billing type Invoice (F2) ,maintain Billing Date for example, <Current Date> and inform the sales document created previously.Choose OK. | The draft billing document or invoice with ID <TMPXXXXXX> is displayed in the Manage Billing Documents screen. |  |
| 7 | Save Billing Document | On the Create Billing Documents screen, validate the details and choose Save.Note the billing document number.Note The draft version billing document or invoice with ID <TMPXXXXXX> is converted into a saved billing document with ID <XXXXXX>. | The system generates an invoice for billing.Billing document is created with value-added service details copied from outbound delivery. |  |

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
| 3 | Display Billing Document | Enter the Billing Document .Choose Continue. | Billing document is displayed. |  |
| 4 | Display VAS Details | Select an item.Choose the Value-Added Services button. | The following VAS details are displayed on the Value-Added Services dialog and the same are validated:VAS Service Types: 10VAS Sub Services: 10-1Supplementary Product : R_8000 (if entered earlier)Order Quantity Multiplier: <Multiplier Value> (For example: 1,2, and so on ) (if entered earlier)VAS Charge Code: C01 or <any defined charge code> (if entered earlier)Round Down Quantity: <Not selected by default> (if not selected earlier)Instruction: <User-specific Instruction> (if entered earlier)Long Text: <User-specific Long Text> (if entered earlier) |  |

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

With this process step, you can create a purchase order with VAS details.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Purchaser (Retail). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Create Purchase Order - Advanced (ME21N) app. | The Create Purchase Order - Advanced (ME21N) screen is displayed.Standard filters and buttons are displayed. |  |
| 3 | Enter Purchase Order Data | Enter the following data and press Enter:Order type: Standard PO or NB Standard POSupplier: 33213004In Header section, on the Org. Data tab:Purch. Org.: 3310Purch. Group: 001Company Code: 3310In Item Overview section:Material: R_1080 or R_1080001Plant: 3350Storage Location: 995AQuantity: <Enter a quantity>Net Price: xxxNoteThe VAS details maintained for Supplier: 33213004 in the Configure VAS Characteristic Combinations (F8623) app is automatically determined and proposed as default.You can choose to retain the details of the automatically proposed VAS or make changes to it if needed.Additionally, you can add another VAS by following the steps mentioned in step 4.Price of the product will include any costs associated to the VAS charge codes.If you only enter the generic product, the order quantity must be filled in the variant matrix for the required variants from the Variants tab of the Item Detail section.Under the Item Detail section, select Confirmations:Conf. Control: Inbound Delivery. |  |  |
| 4 | Enter VAS Details - Additional VAS (Optional) | Select an item and choose the Value-Added Services button or choose Menu > Environment > Value-Added Service > VAS Details.On the Value-Added Services dialog, choose the Append Row button.Enter the following mandatory fields:VAS Service Types: 10 Gift wrappingVAS Subservice : 10-2 AnniversaryThe following fields are optional:Supplementary Product : R_8000 (optional)Order Quantity Multiplier: <Multiplier Value> (For example: 1,2, and so on )(optional)VAS Charge Code: C01 or <any defined charge code>(optional)Round Down Quantity: <Unchecked by default>(optional)Instruction: <User-specific Instruction>(optional)Long Text : <User-specific Long Text>(optional)VAS Item number: <Item Number> (populated automatically when dialog is reopened) (optional)Choose Continue | The VAS details are included for the selected item.If the Round Down Quantity checkbox is selected, the VAS item quantity is rounded to the lower value if the calculated VAS item quantity is in decimals. By default (checkbox not selected), this quantity is always rounded to the higher value.If a Supplementary Product is maintained, a new purchase order line item is created.If a Charge Code is maintained for a VAS service, the purchase price of the order item is updated considering the costs maintained for the charge code. |  |
| 5 | Save Order | Choose Save. | A new purchase order is created, and the order number is displayed.Note down the order number for future use. |  |

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
| 3 | Display Purchase Order | Choose Other Purchase Order.Enter the purchase order number and choose Other Document. | The purchase order is displayed. |  |
| 4 | Display VAS Details | Select an item.Choose the Value-Added Services button or choose Menu > Environment > Value-Added Service > VAS Details. | Automatically determined VAS :VAS Service Types: 10 Gift wrappingVAS Subservices : 10-1 BirthdaySupplementary Product : VAS material (if entered earlier)Order Quantity Multiplier: <Multiplier Value> (if entered earlier)VAS Charge Code: C01 or <any defined charge code> (if entered earlier)Round Down Quantity: <Unchecked> (if not selected earlier)Instruction: <User-specific Instruction> (if entered earlier)Long Text : <User-specific Long Text> (if entered earlier)VAS Item number: <Item Number> (populated automatically)Manually maintained VAS :VAS Service Types: 10 Gift wrappingVAS Subservices : 10-2 AnniversarySupplementary Product : VAS material (if entered earlier)Order Quantity Multiplier: <Multiplier Value> (if entered earlier)VAS Charge Code: C01 or <any defined charge code> (if entered earlier)Round Down Quantity: <Unchecked> (if not selected earlier)Instruction: <User-specific Instruction> (if entered earlier)Long Text : <User-specific Long Text> (if entered earlier)VAS Item number: <Item Number> (populated automatically) |  |

|  |
| --- |
| Note When you enter a supplementary logistics services (SLS)-relevant collective purchase order number, the Value-Added Services dialog displays the following recipient details:Recipient of the Packed ItemsQuantity of the Packed ItemsUnit of Measure of the Packed ItemsFor more information, see scope item 71O - Merchandise Distribution and Collective Purchase Order. |

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
| 3 | Start Selection for Inbound Delivery Creation | On the Create Inbound Delivery (VL31N) app screen, enter the following:Supplier: 33213004Purchase Order: <your Purchase Order document number>Choose Continue. | The Inbound Delivery Create: Overview screen is displayed. |  |
| 4 | Validate VAS Details | On the Inbound Delivery Create: Overview screen, select an item from under All Items in the Item Overview tab.Choose the Value-Added Services button or choose Menu > Environment > Value-Added Services > VAS Details.Validate the below details on the Value-Added Services dialog:VAS Service Types: 10 Gift wrappingVAS Subservices : 10-1 BirthdaySupplementary Product : <VAS Material> (if entered earlier)Order Quantity Multiplier: <Multiplier Value> (if entered earlier)VAS Charge Code: C01 or <any defined charge code> (if entered earlier)Round Down Quantity: <Unchecked> (if entered earlier)Instruction: <User-specific Instruction> (if entered earlier)Long Text : <User-specific Long Text> (if entered earlier)VAS Item number: <populated automatically>AndVAS Service Types: 10 Gift wrappingVAS Subservices : 10-2 AnniversarySupplementary Product : <VAS Material> (if entered earlier)Order Quantity Multiplier: <Multiplier Value> (if entered earlier)VAS Charge Code: C01 or <any defined charge code> (if entered earlier)Round Down Quantity: <Unchecked> (if entered earlier)Instruction: <User-specific Instruction> (if entered earlier)Long Text : <User-specific Long Text> (if entered earlier)VAS Item number: <populated automatically> | VAS details are displayed as expected. |  |
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
| 3 | Display Delivery | In the Inbound Delivery field, enter the recently created inbound delivery document number and choose Continue. | Overview of delivery document is displayed. |  |
| 4 | Display VAS Details | On the Inbound Delivery Display: Overview, select an item from under All Items in the Item Overview tab.Choose the Value-Added Services button or choose Menu > Environment > Value-Added Services > VAS Details. | The following VAS details are displayed on the Value-Added Services dialog and the same are validated:VAS Service Types: 10 Gift wrappingVAS Subservices : 10-1 BirthdaySupplementary Product : VAS material (if entered earlier)Order Quantity Multiplier: <Multiplier Value> (if entered earlier)VAS Charge Code: C01 or <any defined charge code> (if entered earlier)Round Down Quantity: <Not selected by default> (if not selected earlier)Instruction: <User-specific Instruction> (if entered earlier)Long Text : <User-specific Long Text> (if entered earlier)VAS Item number:<populated automatically>VAS Service Types: 10VAS Subservices : 10-2Supplementary Product : <VAS Material (if entered earlier)Order Quantity Multiplier: <Multiplier Value>(if entered earlier)VAS Charge Code: C01 or <any defined charge code> (if entered earlier)Round Down Quantity: <Not selected by default> (if not selected earlier)Instruction: <User-specific Instruction> (if entered earlier)Long Text : <User-specific Long Text> (if entered earlier)VAS Item number:<populated automatically> |  |

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
| 4 | Check and Post the Goods Receipt for Inbound Delivery | In the Detail data section, select the Item OK checkbox for the main article.If a VAS article is available, select the Item OK checkbox for the VAS article also.Choose Check to validate the entries.Choose Post. | The goods receipt is posted.Message Material Document <Document number> posted.is displayed. |  |

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
| 3 | Navigate to Create Supplier Invoice - Advanced Screen | In the pop-up, enter Company Code as 3310Choose Continue. | The Enter Incoming Invoice: Company Code 3310 screen is displayed. |  |
| 4 | Provide Invoice Details | Navigate to Basic Data tab and enter the values for the following fields:Invoice Date: <enter date>Reference: <enter reference>Amount: <enter amount> (Total value you had noted down while creating purchase order. You can check this value under Header > Conditions > Total Value )Tax Code: <enter tax code> (Tax code you have noted down in purchase order. You can check this value under Item Detail > Invoice > Tax Code )Tax Amount: <enter tax amount> (Tax amount you had noted down while creating purchase order. You can check this value under Header > Conditions > TTX1 > Tax )Under the Details tab, select the corresponding document type in the Doc. Types field.Navigate to PO Reference tab and enter values for the following fields:Ref Document category: Purchase Order/Scheduling AgreementPurchasing Document: <enter purchase order number>Item type: Goods/service itemsPress Enter. | The purchase order reference details are displayed. |  |
| 5 | Check Balance | Check the document balance amount in the Balance field. | Balance in green indicates there is no issue between the purchase order and respective invoice. |  |
| 6 | Post Supplier Invoice | Choose Post.Supplier invoice number is displayed. Note down this number for future use. | The message "Document number XXXXXXX created" is displayed.Invoice verification is completed. |  |

|  |
| --- |
| Note If there are more than one items in the purchase order and the supplier sends an invoice for all items with complete quantity, the total value and tax details can be retrieved by navigating to Purchase Order > Header > Conditions > Total Value and Purchase Order > Header > Conditions > TTX1 . |

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
| 4 | Check Follow- On Document | Select Follow-On Documents. | You can view the accounting document. |  |

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

With this process step, you can create a stock transfer order (STO) with value-added service details.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser (Retail). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Create Purchase Order (ME21N) app. | Create Purchase Order (ME21N) app screen is displayed. |  |
| 3 | Enter Stock Transfer Order Data | Enter the following data, then press Enter:Order Type: StockTranspOrderDel or UD StockTranspOrderDelSupplying Plant: 3350In the Org. Data tab of the Header section:Company Code: 3310Purchasing Org.: 3310Purchasing Group: 001In the Item Overview section:Material:R_1080 or R_1080001Plant:3340Storage Location:994APO Quantity:xNote If you only enter the generic product, the order quantity must be filled in the variant matrix for the required variants from the Variants tab of the Item Detail section. |  |  |
| 4 | Enter VAS Details | Select an item and choose the Value-Added Services button or choose Menu > Environment > Value-Added Service > VAS Details.On the Value-Added Services dialog, choose the Append Row button.Enter the following mandatory fields:VAS Service Types: 10VAS Sub Services : 10-1The following fields are optional:Supplementary Product: R_8000Order Quantity Multiplier: <Multiplier Value> (For example: 1,2, and so on )VAS Charge Code: <Not Applicable>Round Down Quantity: <Not selected by default>Instruction: <User-specific Instruction>Long Text : <User-specific Long Text>VAS Item number: <Item Number> (populated automatically when dialog is reopened)Choose Continue | The VAS details are included for the selected item.NoteIf the Round Down Quantity checkbox is selected, the VAS item quantity is rounded to the lower value if the calculated VAS item quantity is in decimals. By default (checkbox not selected), this quantity is always rounded to the higher value.Charge code is not supported in stock transfer order process. |  |
| 5 | Save Stock Transfer Order | Choose Save. | A new stock transfer order is created, and the order number is displayed.Note down the order number for future use. |  |

Result

The stock transfer order is created, and a stock transfer order number is generated.

##### Display Stock Transfer Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this process step, you can display the created stock transfer order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Purchaser (Retail). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Display Purchase Order - Advanced (ME23N). | The Display Purchase Order screen is displayed. |  |
| 3 | Display Stock Transfer Order | Choose Other Purchase Order.Enter the stock transfer order number and choose Other Document. | The stock transfer order is displayed. |  |
| 4 | Display VAS Details | Select an item.Choose the Value-Added Services button or choose Menu > Environment > Value-Added Service > VAS Details. | The following VAS details are displayed on the Value-Added Services dialog and the same are validated:VAS Service Types: 10VAS Sub Services : 10-1Supplementary Product : R_8000 (if entered earlier)Order Quantity Multiplier: <Multiplier Value> (For example: 1,2, and so on ) (if entered earlier)Round Down Quantity: <Not selected by default> (if not selected earlier)Instruction: <User-specific Instruction> (if entered earlier)Long Text : <User-specific Long Text> (if entered earlier)VAS Item number: <Item Number> (populated automatically) |  |

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
| 4 | Display VAS Details | Select an item.Choose the Value-Added Services button or choose Menu > Goto > Value-Added Service > VAS Details. | The following VAS details are displayed on the Value-Added Services dialog and the same are validated:VAS Service Types: 10VAS Sub Services : 10-1Supplementary Product : R_8000 (if entered earlier)Order Quantity Multiplier: <Multiplier Value> (For example: 1,2, and so on ) (if entered earlier)Round Down Quantity: <Not selected by default> (if not selected earlier)Instruction: <User-specific Instruction> (if entered earlier)Long Text : <User-specific Long Text> (if entered earlier) |  |

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

#### Monitor EDI Message Summary for the Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this step, you can use the Message Dashboard (/AIFX/WDA_MSG_MONITOR) app to verify the electronic data interchange (EDI) message sent to the supplier.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Configuration Expert - Business Network Integration |  |  |
| 2 | Access the App | Open Message Dashboard (/AIFX/WDA_MSG_MONITOR) app. | The Message Dashboard screen is displayed. |  |
| 3 | Select the Dates | Execute the following:Select From(Date/Time) and To(Date/Time)Choose Search. | The replication log for the selected dates is displayed. |  |
| 4 | Expand the Result List and Select the Messages Link | Execute the following:Expand the Namespace/Interface, for example, Procurement EDI scenario - /MMEDI to view Interface for purchase order out - ORDREQOUT/0001Select the messages link text under All Messages | Monitor and Error Handling screen is displayed. |  |
| 5 | Select Node to Check its Content | Select the ORDREQOUT/0001 Interface for purchase order out from the panel on the left.Select the latest message from the Log Messages section from the panel on the right.Select the node ORDER from the Data Structure section to view the purchase order or the collective purchase order details.Select the node RFMVALUE_ADDED_SERVICE from the Data Structure section to view the VAS details of the purchase order or the collective purchase order.Select the node PACKED_ITEM_QUANTITY from the Data Structure section to view the quantity and the unit of measure of the packed item. | The corresponding details are displayed in the Data Content section.ExampleVAS (without charge code)<RFMVALUE_ADDED_SERVICE> <EDI_RFMVALUE_ADDED_SERVICE> <CONTROLLER/> <VALUE_ADDED_SERVICE_TYPE>10</VALUE_ADDED_SERVICE_TYPE> <VALUE_ADDED_SUB_SERVICE_TYPE>10-1</VALUE_ADDED_SUB_SERVICE_TYPE> <VALUE_ADDED_SERVICE_PRODUCT>R_8000</VALUE_ADDED_SERVICE_PRODUCT> <VALUE_ADDED_SRVC_ITEM_NUMBER>85001</VALUE_ADDED_SRVC_ITEM_NUMBER> <VALUE_ADDED_SERVICE_INSTRUCTIO>Test1</VALUE_ADDED_SERVICE_INSTRUCTIO> <VALUE_ADDED_SERVICE_LONG_TEXT>Test PO 2</VALUE_ADDED_SERVICE_LONG_TEXT> <PACKED_ITEM_RECIPIENT/> <PACKED_ITEM_QUANTITY> <CONTROLLER/> <UNIT_CODE/> <CONTENT>0.0</CONTENT> </PACKED_ITEM_QUANTITY> <VALUE_ADDED_SERVICE_CHARGE_COD/> </EDI_RFMVALUE_ADDED_SERVICE> </RFMVALUE_ADDED_SERVICE>VAS (with charge code)<RFMVALUE_ADDED_SERVICE> <EDI_RFMVALUE_ADDED_SERVICE> <CONTROLLER/> <VALUE_ADDED_SERVICE_TYPE>10</VALUE_ADDED_SERVICE_TYPE> <VALUE_ADDED_SUB_SERVICE_TYPE>10-1</VALUE_ADDED_SUB_SERVICE_TYPE> <VALUE_ADDED_SERVICE_PRODUCT/> <VALUE_ADDED_SRVC_ITEM_NUMBER>00000</VALUE_ADDED_SRVC_ITEM_NUMBER> <VALUE_ADDED_SERVICE_INSTRUCTIO>Test1</VALUE_ADDED_SERVICE_INSTRUCTIO> <VALUE_ADDED_SERVICE_LONG_TEXT>Test PO 2</VALUE_ADDED_SERVICE_LONG_TEXT> <PACKED_ITEM_RECIPIENT/> <PACKED_ITEM_QUANTITY> <CONTROLLER/> <UNIT_CODE/> <CONTENT>0.0</CONTENT> </PACKED_ITEM_QUANTITY> <VALUE_ADDED_SERVICE_CHARGE_COD>C01</VALUE_ADDED_SERVICE_CHARGE_COD> </EDI_RFMVALUE_ADDED_SERVICE> </RFMVALUE_ADDED_SERVICE> |  |

#### Create Value-Added Service Articles

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this process step, you can create a value-added service (VAS) article using the Create Article (MM41) app or the Manage Product Master Data (F1602) Fiori app.

Procedure

Using Create Article (MM41) Application

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data (Retail). |  |  |
| 2 | Access the SAP Fiori App | Open Create Article (MM41) app. | The Create Material (Initial Screen) is displayed. |  |
| 3 | Enter Article Basic Data | In the Create Material (Initial screen), enter the following details:Material: Article number (<R_YYYYY>)Material Type: Value-Added ServicesMaterial Group: (R7113002/Value Added Services)Material Category: Single Material/00 |  |  |
| 4 | Choose Views | Select views Basic Data, Basic Data 2, Sales, Logistics: Distribution Center, Logistics: Store and POS.Choose Continue. | Create Material … (Basic Data) screen is displayed. |  |
| 5 | Enter Basic Data | On the Basic data tab, enter a Article description (short text). |  |  |
| 6 | Enter Basic Data | In the Units of measure/EANs/dimensions section, enter the following: (All the below should ideally get filled automatically (only except EAN Category) from the Reference Article, but if you need to maintain any deviation then you can go ahead and maintain)Base Unit of Measure (PC)Gross Weight (<value>)Unit of Weight (KG)Net Weight (<value>)EAN Category (IE - Instore EAN (int. assignment possible))Volume (<value>)Volume Unit (L) |  |  |
| 7 | Enter Basic Data | In the Internal logistics data section, enter the following:Purchasing Group (002/Group 002)Supply Source (4 - Stock Transfer Before Standard)GenItemCatGroup VAS / Value Added ServicesLoading Group (0001/Crane)Transportation Group (0001/On pallets)Variable Order Unit (1/Active)In General Data section, enter the following:Tax Class (1- Full tax)Valuation Class (3100 – Trading goods)In Validity section, enter the following:Valid from: <date>Valid to: <date> (default 31.12.9999, cannot be maintained)In Shelf Life Data section, enter the following:Remaining Shelf Life: (0)Total Shelf Life: (0)Period Indicator: (D)Storage %: (0) |  | The system message “The EAN will be determined internally on the basis of the EAN category displays” |
| 8 | Navigate to Goto Additional Data in Basic Data View | In Short Text tab, enter/check the description and language:Language ArabicMaterial Description <Value>Choose Goto Main Data. | Basic Data screen appears. |  |
| 9 | Choose Views | Navigate to Basic Data 2 view and enter the descriptions for the following:Allowed Packaging Weight: <Value>Allowed Packaging Volume: <Value>Excess Weight Tolerance: <Value>Excess Volume Tolerance: <Value> |  |  |
| 10 | Enter Sales Period | If necessary, adjust sales period for stores and distribution center.Sales Period: storeFor sales from: <date>For sales till: <date>Sales Period: distribution centerFor sales from: <date>For sales till: <date> |  |  |
| 11 | Choose Views | Navigate to Sales view. | Create Material …(Sales) view displays. |  |
| 12 | Enter Organizational Levels Data | Choose Switch Validity Area.In the Areas of Validity pop-up, enter descriptions for the following:Sales Unit (PC)Sales Org. (3310/ Dom. Sales Org)Distr. Channel (10 - Direct Sales)Choose Continue. |  |  |
| 13 | Enter Sales Data | On the Create Material: Sales screen, make the following entries:(All the below should ideally get filled automatically from the Reference Article, but if you need to maintain any deviation then you can go ahead and maintain)For Sales from <date>For Sales to <date>Item Category Group VASPP det. Seq. (Purchase Price determination Sequence) (01/ Standard with price determination)SP det Seq. (Sales price Determination Sequence) (01/ Calculate SP from planned markup)Save Calculated Price (Uncheck the box) |  | Repeat the same steps 11 and 12 for maintaining Sales Area – 3310/50 (For DC) for Sales unit PC.Repeat the same steps 11 and 12 for maintaining Sales Area – 3310/60 (For DC) for Sales unit PC. |
| 14 | Choose Views | Navigate to the Logistics: DC view.Check for the below entries:In MRP Parameters:MRP Type: ND (No Planning)In Forecast Parameters:Forecast model – 0Period Indicator : WIn MRP Controller/Replenishment Data:Supply Source: 1 (Standard)In General control parameters:Purchasing Group: 002/Group 002Tax Indicator: 1 (Full tax)Availability Check: ST/Consider Only StockIn Physical inventory/ goods issue/ picking/ shipping section:Loading Group: 0001/CraneIn Storage data:Storage Location: 995A | On the Create Material: Logistics DC screen, check the available entries. These are proposed based on the reference article. Only changes must be maintained. |  |
| 15 | Navigate to MRP/Forecast Data inside Logistics: DC View | Choose MRP/Forecast Data.Maintain or check for the below entries:In Procurement section:Procurement Type: F (External Procurement)In Control data section:Select checkbox Autom.resetChoose Back button. |  |  |
| 16 | Choose Views | Navigate to the Logistics: Store view.Check for the below entries:In MRP Parameters:MRP Type: ND/ No PlanningIn Forecast Parameters:Forecast Model: K/Constant with smoothing factor adjustmentIn MRP Controller/Replenishment Data:Supply Source: 4 (Stock Transfer Before Standard)In General control parameters:Purchasing Group: 002/Group 002Tax Indicator: 1(Full tax)Availability Check: ST / Consider Only StockNegative Stock: XIn Storage data:Storage Location: 994A |  | On the Create Material: Logistics Store screen, Check the available entries and do adjustments if necessary (e.g., supply source) |
| 17 | Navigate to MRP/Forecast Data inside Logistics: Store View | Choose MRP/Forecast Data.Maintain or check for the below entries:In Procurement section :Procurement Type : F (External Procurement)In the Number of periods required section:History Periods: 60Forecast Periods: 12In Control data section:Initialization: XTrack Limit: 4(Value that specifies the amount by which the forcast value may deviate from the actual value.)Select checkbox Autom.resetModel Selection Procedure: 2 (Analytical model selection procedure)Choose Back. |  |  |
| 18 | Choose Views | Navigate to POS view.In Till receipt texts section, enter the following:Language Key: ENAlternate Unit: PCTill receipt text for Unit: <value> |  | Maintain POS Text for distribution chain: 3310/40Maintain, if necessary, the text in different languages. Press the button: additional data |
| 19 | Save Your Data | At the bottom right of the display, choose Create to save your data. | The Create Material (Initial Screen) appears.The VAS article is created and saved. | You can change or maintain or update the article created above, via Maintain Article (MM42) app. |

Using Manage Product Master Data (F1602) Application

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data (Retail). |  |  |
| 2 | Access the SAP Fiori App | Open Manage Product Master Data (F1602). | The Manage Product Master Data (F1602) screen is displayed. |  |
| 3 | Choose Create New Product Master | In the Manage Product Master Data (F1602) screen, choose Create button and select Single Article from the list. | The Create Master Data Record pop-up displays. |  |
| 4 | Enter Data for Mandatory Fields | Enter the following details:Product Number: for example, <R_ZZZZZ>Note You either enter any external alphanumeric ID, and that ID must start with an alphanumeric character, or if you provide no entry, the system automatically assigns a numeric ID.Product Type: Value-Added Services (VAS)Product Group: Value Added Services (R7113002)Base Unit: for example, PCValuation Class: Trading goods (3100)Tax Classification: 1 (Full Tax)Loading Group: 0001/CraneDescription: <any description>Choose OK. | The Product screen is displayed with the entered values. |  |
| 5 | Enter Basic Data | Under General Information > Basic Data , enter the following details:Division: 00 |  |  |
| 6 | Create Descriptions | Under General Information > Descriptions , choose Create. |  |  |
| 7 | Enter Descriptions Data | In the Descriptions subsection, make the following entries:Language: for example, ArabicProduct : <your description> |  |  |
| 8 | Enter Base Unit of Measure | Under General Information > Base Unit of Measure , choose Show More and enter the following details:GTINGTIN Category: IEGross Weight: <value>Net Weight: <value>Volume: <value> L |  |  |
| 9 | Choose Unit of Measure | Under General Information > Unit of Measure , choose the Unit of Measure (e.g. PC) and navigate to the details. | The Unit of Measure screen is displayed. |  |
| 10 | Enter Receipt Texts | Under Receipt Texts, choose Create.Enter Language and Text. |  |  |
| 11 | Enter Dimensions Data | Under Dimensions > Weight section, enter the following:Gross Weight: for example, 0.200Net Weight: for example, 0.200Weight Unit: for example, KGChoose Apply. |  |  |
| 12 | Choose Distributions Chains | In the Product screen, choose Distribution Chains tab. | The Distribution Chains tab displays. |  |
| 13 | Choose Create | In the Distribution Chains tab, choose Create | The Distribution Chains screen is displayed. |  |
| 14 | Enter Distribution Chains Data | Under General Information > General Data enter the following details:Sales Organization: <Sales org number> (3310/ Dom. Sales Org)Note The organization unit value is determined by what is offered in the value help.Distribution Channel: for example, 10 - Direct SalesIn the Grouping Terms section, enter Item Category Group: for example, VAS |  |  |
| 15 | Return to Main View | Choose Apply to return to Product screen. | The Product screen appears. | Repeat steps 12 to 14 to maintain other distribution chains e.g.,3310/50.Repeat the same steps 12 to 14 for maintaining Sales Area – 3310/60 for Sales unit PC. |
| 16 | Choose Distribution Center Data | In the Product screen, choose Distribution Centers tab. | The Distribution Centers tab displays. |  |
| 17 | Create Distribution Center | Under Distribution Centers, choose Create. | The Distribution Center screen is displayed. |  |
| 18 | Enter Distribution Center - General Information | In the General Information section, make the following entries:Distribution Center: Distribution center number for example, 3391 (Reference DC comes by default, no need to enter explicitly and remain Non Editable) |  | Similarly, Administrator can maintain for different DC. |
| 19 | Enter Distribution Center - Sales Data | In the Sales section, make the following entry:Loading Group: for example, Crane |  |  |
| 20 | Enter Distribution Center - MRP Data | Navigate to MRP Data > MRP Data and make following entries:Availability Check: for example, NC(No ATP Check)MRP Type: For example, ND (No MRP) |  |  |
| 21 | Enter Distribution Center - Storage Location | Navigate to Storage > Storage Locations and choose Create.Enter Storage Location: 994A. |  |  |
| 22 | Return to Main Screen | Choose Apply to return to Product screen. | The Product screen displays. |  |
| 23 | Create Stores | In the Product screen, navigate to Stores > Stores .Choose Create. | The Store screen is displayed. |  |
| 24 | Enter Store - General Information | In the General Information section, make following entries if not maintained:Store: Store number for example, 3392 (Reference Store comes by default, no need to enter explicitly and remain Non Editable)Negative Stock Allowed in Plant: X |  | Similarly, Administrator can maintain for different Stores |
| 25 | Enter Store - Sales Data | In the Sales Data section, make the following entry:Loading Grp: for example, Crane |  |  |
| 26 | Enter Store - MRP Data | Navigate to MRP Data > MRP Data section and make following entries:Availability Check: for example, No ATP Check (NC)MRP Type: For example, No planning (ND) |  |  |
| 27 | Enter Store - Storage Location | Navigate to Storage > Storage Locations and choose Create.Enter Storage Location: 994A. |  |  |
| 28 | Return to Main Screen | Choose Apply to return to Product screen. | The Product screen displays. |  |
| 29 | Save Your Data | Choose Create. | The VAS article is created. |  |

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
- see-also :: [[15-retail-operations/product-taxonomies-for-retail-5fj-ae-test-script-1079]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6NM_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 114,295 chars in the whole document
