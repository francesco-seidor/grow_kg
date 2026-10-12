---
id: 15-retail-operations/retail-logistics-with-third-party-warehouse-management-69m-ae-test-scr
title: Retail Logistics with Third-Party Warehouse Management (69M_AE) - Test Script (69M_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 69M_AE: retail DC logistics integrated with a third-party WMS via SOAP web services."
cluster: 15-retail-operations
tags: [kb/retail-operations, topic/retail-dc-warehouse-execution]
aliases: [69M_S4CLD2608_BPD_EN_AE]
keywords: [Retail DC Warehouse Execution (Embedded EWM or Third-Party…, third-party wms integration, soap web services, stock transfers, two-step stock transfer, inbound delivery, outbound delivery, purchase orders, sales orders, customer returns]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/69M_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1153
topic: 15-retail-operations/retail-dc-warehouse-execution
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Retail Logistics with Third-Party Warehouse Management (69M_AE) - Test Script (69M_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/69M_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Retail DC Warehouse Execution (Embedded EWM or Third-Party WMS)** in Retail Operations. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Retail Logistics with Third-Party Warehouse Management (69M_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Retail Logistics with Third-Party Warehouse Management (69M_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232858174)

[2 Prerequisites 5](#_Toc232858175)

[2.1 System Access 5](#_Toc232858176)

[2.2 Roles 5](#_Toc232858177)

[2.3 Master Data, Organizational Data, and Other Data 6](#_Toc232858178)

[2.4 Additional Manual Configuration 8](#_Toc232858179)

[2.5 Preliminary Steps 8](#_Toc232858180)

[2.5.1 Create Purchasing Info Record 8](#_Toc232858181)

[2.5.2 Configuration for Automatic Storage Location Creation 10](#_Toc232858182)

[2.5.3 Configuration for Define Default Values for Deliveries 10](#_Toc232858183)

[2.5.4 Configuration for Setting Warehouse Address 11](#_Toc232858184)

[2.5.5 Configuration for Define Warehouse Attributes 12](#_Toc232858185)

[3 Overview Table 13](#_Toc232858186)

[4 Test Procedures 17](#_Toc232858187)

[4.1 Inventory Management Processes 17](#_Toc232858188)

[4.1.1 Create Initial Stock Posting 17](#_Toc232858189)

[4.1.2 Confirm Inbound Delivery in WMS 18](#_Toc232858190)

[4.1.3 Check Stock Information 19](#_Toc232858191)

[4.1.4 Create Stock Transfer from Non 3rd Party WMS Managed Storage Location to 3rd Party WMS Managed Storage Location 20](#_Toc232858192)

[4.1.5 Create Stock Transfer from 3rd Party WMS Managed Storage Location to 3rd Party WMS Managed Storage Location – Different Stock Type 21](#_Toc232858193)

[4.1.6 Create Scrap Posting 22](#_Toc232858194)

[4.1.7 Create Stock Transfer from 3rd Party WMS Managed Storage Location to 3rd Party WMS Managed Storage Location 24](#_Toc232858195)

[4.1.8 Confirm Outbound Delivery in WMS 25](#_Toc232858196)

[4.1.9 Check Stock Information 25](#_Toc232858197)

[4.1.10 Two Step Stock Transfer from Non 3rd Party WMS Managed Storage Location to 3rd Party WMS Managed Storage Location 26](#_Toc232858198)

[4.1.10.1 Remove Stock from Non 3rd Party WMS Managed Storage Location 26](#_Toc232858199)

[4.1.10.2 Place Stock to 3rd Party WMS Managed Storage Location 27](#_Toc232858200)

[4.1.10.3 Confirm Inbound Delivery in WMS 28](#_Toc232858201)

[4.1.10.4 Check Stock Information 29](#_Toc232858202)

[4.1.11 Two Step Stock Transfer from 3rd Party WMS Managed Storage Location to 3rd Party WMS Managed Storage Location 30](#_Toc232858203)

[4.1.11.1 Two Step Stock Transfer from 3rd Party WMS Managed Storage Location to 3rd Party WMS Managed Storage Location 30](#_Toc232858204)

[4.1.11.2 Confirm Outbound Delivery in WMS 31](#_Toc232858205)

[4.1.11.3 Check Inbound Delivery Number in SAP S/4HANA Cloud Public Edition 31](#_Toc232858206)

[4.1.11.4 Confirm Inbound Delivery in WMS 32](#_Toc232858207)

[4.1.11.5 Check Stock Information 33](#_Toc232858208)

[4.2 Procurement Process 34](#_Toc232858209)

[4.2.1 Create Purchase Order 34](#_Toc232858210)

[4.2.2 Create Inbound Delivery 35](#_Toc232858211)

[4.2.3 Goods Receipt in Third-Party WMS 36](#_Toc232858212)

[4.3 Sales Process 36](#_Toc232858213)

[4.3.1 Create Sales Order 36](#_Toc232858214)

[4.3.2 Create Outbound Delivery 38](#_Toc232858215)

[4.3.3 Picking and Goods Issue in Third-Party WMS 39](#_Toc232858216)

[4.3.4 Receive Split Outbound Delivery 39](#_Toc232858217)

[4.3.5 Receive Outbound Delivery Confirmation 40](#_Toc232858218)

[4.4 Customer Returns 41](#_Toc232858219)

[4.4.1 Create Returns Order 41](#_Toc232858220)

[4.4.2 Perform Picking 42](#_Toc232858221)

[4.4.3 Post Goods Receipt 43](#_Toc232858222)

[4.4.4 Perform Material Inspection 44](#_Toc232858223)

[4.4.5 Post Stock Transfer 46](#_Toc232858224)

[4.4.6 Goods Receipt in Third-Party WMS 47](#_Toc232858225)

[4.4.7 Check Stock Information 47](#_Toc232858226)

[4.5 Return to Supplier Process 48](#_Toc232858227)

[4.5.1 Create Return Purchase Order 48](#_Toc232858228)

[4.5.2 Create Return Delivery 49](#_Toc232858229)

[4.5.3 Check Web Services Message and Execute in WMS 50](#_Toc232858230)

[4.5.4 Check Confirmation in SAP S/4HANA Cloud Public Edition 51](#_Toc232858231)

## Purpose

Overview

A distribution center typically is the logistical entry point of a retailer to the supply chain. It connects the procurement process from external suppliers with the distribution process to the stores. The goal of the distribution process is to shorten delivery cycles to the stores, ensuring that there are no out-of-stock situations. To achieve this, a sophisticated warehouse management is key.

The decentralized third-party warehouse management system runs all processes related to inbound and outbound processes originating from procurement, sales, and distribution processes, as well as in-warehouse goods movements. The integration is covered by asynchronous SOAP interfaces compatible with most existing third-party warehouse management systems to reduce the implementation effort.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

|  |
| --- |
| NoteOData and SOAP web services are offered to integrate SAP S/4HANA Cloud Public Edition, retail with third-party on-premise or Cloud solutions.For exceptional cases and based on individual customer requests, SAP admits usage of BAPIs and IDocs temporarily to integrate your solution with SAP S/4HANA Cloud Public Edition wherever the currently available OData and SOAP web services are not sufficient.This admittance is restricted to individual customers and to a well-defined set of BAPIs and IDocs, which have been technically enabled by SAP for this purpose. To get this approval, follow the process described in the [2653671](https://me.sap.com/notes/2653671).These BAPIs and IDocs are available for use; however these will not be functionally extended. They are maintained for a limited period. Maintenance of a BAPI or IDoc will end 12 months after the availability of an equivalent OData or SOAP web service.To integrate SAP S/4HANA Cloud Public Edition, retail with a third-party WMS, SAP provides the following SOAP web services:Distribute Outbound Delivery -Confirm Outbound Delivery -Distribute Inbound Delivery -Confirm Inbound Delivery -Split Outbound Delivery -Split Outbound Delivery Confirmation -These web services might not be one-to-one replacement for the enabled BAPIs and IDocs. However, the new web services are mapped to the old interfaces. |

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

| Name (Role Template) | ID | Description | ID (Role Template) | Log On |
| --- | --- | --- | --- | --- |
| Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP | Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP |  |
| Shipping | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Purchaser (Retail) | SAP_BR_PURCHASER_RFM | Retail Purchasing / Retail Sourcing and Contracting | SAP_RFM_SPT_PURCHASING_PC / SAP_RFM_SPT_SOURCING_PC |  |
| Receiving Specialist | SAP_BR_RECEIVING_SPECIALIST | Receiving | SAP_BR_RECEIVING_SPECIALIST |  |
| Inventory Processing | SAP_BR_WAREHOUSE_CLERK | Retail Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Customer Returns | SAP_BR_RETURNS_REFUND_CLERK | Customer Returns | SAP_BR_RETURNS_REFUND_CLERK |  |
| Inventory Management | SAP_BR_INVENTORY_MANAGER | Retail Inventory Management | SAP_BR_INVENTORY_MANAGER |  |

### Master Data, Organizational Data, and Other Data

SAP Best Practices standard values based on a new global template will be used once available. In the table, you can still see the master data used for the current baseline.

Essential master and organizational data were created in your S/4HANA system in the implementation phase, such as the data that reflects the organizational structure of your company and the master data that suits its operational focus, for example, master data for materials, vendors, and customers.

This master data usually consists of standardized SAP Best Practices default values and enables you to go through the process steps of this scope item.

|  |
| --- |
| Note Additional master data (Default values)You can test the scope item with other SAP Best Practices default values that have the same characteristics. Check your SAP system to find out which other material master data exists.Using your own master dataYou can also use customized values for any material or organizational data for which you have created master data. For more information about creating master data, see the Master Data Procedures documentation. |

The organizational structure and master data of your company are created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Single Article | R_7001 | Memory Cards |  |
| Single Article | R_7002 | Lense |  |
| Supplier | 33213001 | Retail Non-Food Supplier AE |  |
| Sold-to Party | 33113007 | Wholesale non-Food AE |  |
| Ship-to party | 33113007 | Wholesale non-Food AE |  |
| Sales Organization | 3310 | Dom. Sales Org |  |
| Distribution Channel | 10 | Direct Sales |  |
| Division | 00 | Product Division 00 |  |
| Shipping Point | 3350 | SP DC 3350 |  |
| Plant | 3350 | DC 3350 AE |  |
| Storage Location | 991I | 3rd Party WMS DC |  |
| Storage Location | 991K | 3rd Party WMS Return DC |  |
| Purchase Organization | 3310 | Purch. Org. 3310 |  |
| Purchasing group | 001/002 | Group 001/Group 002 |  |
| Vendor | 33213001 | Retail Non-Food Supplier AE |  |
| Warehouse | 3350 | Warehouse Number |  |
| Warehouse | 332 | Third-Party Warehouse |  |
| Cost Centre | 33403350 | Template StoreTemplate DC |  |
| Carrier | 33300001 | Domestic AE Supplier 1 |  |
| Shipping point | 335R | SP DC 3350 Return |  |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/6d624f9c38bf3ba792a2d40a6512dd00)

### Preliminary Steps

|  |
| --- |
| Note The testing is carried out with retail master data and organizational data mentioned above in section (Master Data, Organizational Data, and Other Data). |

#### Create Purchasing Info Record

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Purchaser (Retail). | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Purchasing Info Records (F1982). | The Manage Purchasing Info Records (F1982) screen displays. |  |
| 3 | Open New Purchasing Info Record | Choose Create. | The Purchasing Info Record Screen displays. |  |
| 4 | Enter Header Data | Make the following entries:Purchasing Info Record Category: <Standard>Purchasing Organization: 3310Supplier: 33213001Material: <Material>Note Please use Material created in test procedure step Create Single Article.Plant: 3350Purchasing Group: 001/002Material Group: R1193001 | Header data is added. |  |
| 5 | Enter General Information | Make the following entries:Available From: MM/DD/YYYYAvailable To: MM/DD/YYYY | General Information is added. |  |
| 6 | Enter Purchasing Data | Make the following entries:Incoterm: <Incoterm>Incoterm Location 1: <Incoterm location1> | Purchasing Data is added. |  |
| 7 | Enter Delivery and Quantity Data | Make the following entries:Delivery Time in Days: <XX Days>Under Delivery Tolerance in %: <XX>Over Delivery Tolerance in %: <XX>Order Unit: <Order Unit>Standard Order Quantity: <Standard Order Quantity>Select the following entries if required:Unlimited DeliveryGoods-Receipt-Based Invoice VerificationNo Evaluated Receipt SettlementOrder Acknowledgment RequirementConfirmation Control | Delivery and Quantity Data is added. |  |
| 8 | Enter Condition Data | In the Condition section, choose the Create icon. Enter the following data:Valid From: <Valid from Date>Amount: <Amount>Pricing Unit: <Pricing Unit>Valid To: <Valid to Date>Currency: AEDChoose Apply. | Condition Data is added. |  |
| 9 | Enter Reference Data (Optional) | Optionally, you can enter reference data. | Reference data is added. |  |
| 10 | Save Your Data | Choose Create. | A purchasing info record is saved. |  |

#### Configuration for Automatic Storage Location Creation

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration as Configuration Expert - Business Process Configuration |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Create Storage Location Automatically.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Create Storage Location Automatically screen is displayed. |  |
| 3 | Configuration Create Storage Location Automatically | Create the following settings:For Movement type 657 - GD returns blocked, check ON Create SLoc. Automat. | The configuration is saved successfully |  |

#### Configuration for Define Default Values for Deliveries

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration as Configuration Expert - Business Process Configuration |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define default values for deliveries.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define default values for deliveries screen is displayed. |  |
| 3 | Configuration Define default values for deliveries | Create the following settings:Select the warehouse and select DetailsMaintain the below entries and SaveShip-To-Party: <Ship-To-Party>Supplier: <Supplier>Shipping Point: 3310Sales Organization: 3310Distribution Channel: 10Division: 00 | The configuration is saved successfully |  |

#### Configuration for Setting Warehouse Address

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration as Configuration Expert - Business Process Configuration |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Set Warehouse Address.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Set Warehouse Address screen is displayed. |  |
| 3 | Confiqure Set Warehouse Address | Create the following settings:Select New EntriesWarehouse Number: 3350Default Pty Entitld: |  |  |
| 4 | Save the configuration | Maintain the below address data entries and Save:Name:Street/House number:Postal Code/City:Country/Region:Time Zone:Choose Enter. | The configuration is saved successfully |  |

#### Configuration for Define Warehouse Attributes

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration as Configuration Expert - Business Process Configuration |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Warehouse Attributes.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Warehouse Attributes screen is displayed. |  |
| 3 | Configuration Define Warehouse Attributes | Create the following settings:Select the warehouse and select DetailsMaintain the below entries and SaveWeight Unit: <Weight Unit>Volume Unit: <Volume Unit>Currency: <Currency>Time Unit: <Time Unit>Unit of Length: <Unit of Length>Factory Calend: <Factory Calendar>Note The SSCUI “Define Warehouse Attributes” allows the input of the units for weight, volume, length and time only if no values have been provided yet. As soon as the units are filled (and saved), the fields are closed for input. This ensures that the units are transported to the productive system only once. The currency and factory calendar can be changed anytime. | The configuration is saved successfully |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Inventory Management Processes

| ID (Role Template) | Name (Role Template) | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Initial Stock Posting](#unique_14) [page ] 17 | Warehouse Clerk | Post Goods Movement (MIGO) |  |
| [Confirm Inbound Delivery in WMS](#unique_15) [page ] 18 | External System | Execute Goods Receipt, send out confirmation to S/4HANA Cloud |  |
| [Check Stock Information](#unique_16) [page ] 19 | Warehouse Clerk | Display Warehouse Stock - Deprecated (MB52) |  |
| [Create Stock Transfer from Non 3rd Party WMS Managed Storage Location to 3rd Party WMS Managed Storage Location](#unique_17) [page ] 20 | Warehouse Clerk | Post Goods Movement (MIGO) |  |
| [Create Stock Transfer from 3rd Party WMS Managed Storage Location to 3rd Party WMS Managed Storage Location – Different Stock Type](#unique_18) [page ] 21 | Warehouse Clerk | Transfer Stock - In-Plant (F1061) |  |
| [Create Scrap Posting](#unique_19) [page ] 22 | Inventory Manager | Post Goods Movement (MIGO) |  |
| [Create Stock Transfer from 3rd Party WMS Managed Storage Location to 3rd Party WMS Managed Storage Location](#unique_20) [page ] 24 | Inventory Manager | Post Goods Movement (MIGO) |  |
| [Confirm Outbound Delivery in WMS](#unique_21) [page ] 25 | External System | Post Goods Issue, Send out confirmation to S/4HANA Cloud |  |
| [Check Stock Information](#unique_22) [page ] 25 | Warehouse Clerk | Display Warehouse Stock - Deprecated (MB52) |  |
| Two Step Stock Transfer from Non 3rd Party WMS Managed Storage Location to 3rd Party WMS Managed Storage Location |  |  |  |
| [Remove Stock from Non 3rd Party WMS Managed Storage Location](#unique_23) [page ] 26 | Warehouse Clerk | Transfer Stock - In-Plant (F1061) |  |
| [Place Stock to 3rd Party WMS Managed Storage Location](#unique_24) [page ] 27 | Warehouse Clerk | Transfer Stock - In-Plant (F1061) |  |
| [Confirm Inbound Delivery in WMS](#unique_25) [page ] 28 | External System | Execute Goods Receipt, send out confirmation to S/4HANA Cloud |  |
| [Check Stock Information](#unique_26) [page ] 29 | Inventory Manager | Display Warehouse Stock - Deprecated (MB52) |  |
| Two Step Stock Transfer from 3rd Party WMS Managed Storage Location to 3rd Party WMS Managed Storage Location |  |  |  |
| [Two Step Stock Transfer from 3rd Party WMS Managed Storage Location to 3rd Party WMS Managed Storage Location](#unique_27) [page ] 30 | Warehouse Clerk | Transfer Stock - In-Plant (F1061) |  |
| [Confirm Outbound Delivery in WMS](#unique_28) [page ] 31 | External System | Post Goods Issue, send out confirmation to S/4HANA Cloud |  |
| [Check Inbound Delivery Number in SAP S/4HANA Cloud Public Edition](#unique_29) [page ] 31 | Shipping Specialist | Display Outbound Delivery (VL03N) |  |
| [Confirm Inbound Delivery in WMS](#unique_30) [page ] 32 | External System | Execute Goods Receipt, send out confirmation to S/4HANA Cloud |  |
| [Check Stock Information](#unique_31) [page ] 33 | Warehouse Clerk | Display Warehouse Stock - Deprecated (MB52) |  |

Procurement Process

| ID (Role Template) | Name (Role Template) | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Create Purchase Order](#unique_32) [page ] 34 | Purchaser (Retail) | Create Purchase Order - Advanced (ME21N) |  |
| [Create Inbound Delivery](#unique_33) [page ] 35 | Receiving Specialist | Inbound Deliveries for Purchase Orders (VL34) |  |
| [Goods Receipt in Third-Party WMS](#unique_34) [page ] 36 | External system | Post Goods Receipt, confirmation delivery sent out to S/4HANA Cloud |  |

Sales Process

| ID (Role Template) | Name (Role Template) | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Create Sales Order](#unique_35) [page ] 36 | Internal Sales Representative | Create Sales Orders - VA01 (VA01) | The C reate Sales document is displayed. |
| [Create Outbound Delivery](#unique_36) [page ] 38 | Shipping Specialist | Create Outbound Delivery - With Order Reference (VL01N) |  |
| [Picking and Goods Issue in Third-Party WMS](#unique_37) [page ] 39 | External system | Execute Picking, split of delivery, Goods issue, confirmation delivery sent out to S/4HANA Cloud |  |
| [Receive Split Outbound Delivery](#unique_38) [page ] 39 | Shipping Specialist | Display Outbound Delivery (VL03N) |  |
| [Receive Outbound Delivery Confirmation](#unique_39) [page ] 40 | Shipping Specialist | Display Outbound Delivery (VL03N) |  |

Customer Returns

| ID (Role Template) | Name (Role Template) | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Create Returns Order](#unique_40) [page ] 41 | Returns and Refund Clerk | Manage Customer Returns (F1708) |  |
| [Perform Picking](#unique_41) [page ] 42 | Shipping Specialist | Manage Outbound Deliveries (F0867A) |  |
| [Post Goods Receipt](#unique_42) [page ] 43 | Shipping Specialist | Manage Outbound Deliveries (F0867A) |  |
| [Perform Material Inspection](#unique_43) [page ] 44 | Receiving Specialist | Enter Inspection Results - From Warehouse (MSR_INSPWH) |  |
| [Post Stock Transfer](#unique_44) [page ] 46 | Warehouse Clerk | Transfer Stock - In-Plant (F1061) |  |
| [Goods Receipt in Third-Party WMS](#unique_45) [page ] 47 | External System | Goods receipt, storage, send out confirmation |  |
| [Check Stock Information](#unique_22) [page ] 25 | Warehouse Clerk | Display Warehouse Stock - Deprecated (MB52) |  |

Return to Supplier Process

| ID (Role Template) | Name (Role Template) | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Create Return Purchase Order](#unique_46) [page ] 48 | Purchaser (Retail) | Create Purchase Order - Advanced (ME21N) |  |
| [Create Return Delivery](#unique_47) [page ] 49 | Shipping Specialist | My Purchase Orders - Due for Delivery (VL10B) |  |
| [Check Web Services Message and Execute in WMS](#unique_48) [page ] 50 | External System | Execute Picking, Post Goods Issue, send out confirmation to S/4HANA Cloud |  |
| [Check Confirmation in SAP S/4HANA Cloud Public Edition](#unique_49) [page ] 51 | Shipping Specialist | Display Outbound Delivery (VL03N) |  |

## Test Procedures

This chapter describes test procedures for each process step that belongs to this scope item.

### Inventory Management Processes

#### Create Initial Stock Posting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This section describes how to create a initial stock posting triggered from SAP S/4HANA Cloud Public Edition for a 3rd party WMS managed storage location.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Post Goods Movement (MIGO). | The Goods Receipt Other screen displays. | It only displays it that way if, it was your last transaction. So the action for the User should be to select field Reference Document for MIGO TransactionOther. |
| 3 | Input Movement Type | Make the following entry and press Enter.Executable Action in Transaction MIGO: Goods ReceiptReference Document for MIGO Transaction: Other |  |  |
| 4 | Input on the Goods Receipt Other screen: Material tab | On the Goods Receipt Other screen: Material tab, make the following entry and press Enter:Material : <Material number> |  |  |
| 5 | Input on the Goods Receipt Other screen: Quantity tab | On the Goods Receipt Other screen: Quantity tab, make the following entry and press Enter:Qty in Unit of Entry: Qty in UOMUnit of Entry: PC |  |  |
| 6 | Input on the Goods Receipt Other screen: Where tab | On the Goods Receipt Other screen: Where tab, make the following entries and press Enter:Movement Type: 561 – Receipt per initial entry of stock balances into unr.-usePlant: 3350Storage Location: 991I |  |  |
| 7 | Save your entries | Choose Post. | Delivery XXXX created |  |

#### Confirm Inbound Delivery in WMS

Purpose

In this section the Inbound delivery Web Services message is received in the Third-party WMS. Some follow up processes need to be done there:

- Execute Goods Receipt
- Confirmation transfer sent out to SAP S/4HANA Cloud Public Edition

The steps are not described here in detail because it might be any 3rd Party WMS.

#### Check Stock Information

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this section the updated stock information is checked.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Display Warehouse Stock - Deprecated (MB52). | The Display Warehouse Stocks of Material screen displays. |  |
| 3 | Enter material | Make the following entries:Material: <Material number>Plant: 3350Storage Location: 991IChoose Run. | The Display Warehouse Stocks of Material is shown. |  |
| 4 | Check stock | Check if the stock information is now updated and the stock of the 3rd party WMS managed storage location displays. |  |  |

#### Create Stock Transfer from Non 3rd Party WMS Managed Storage Location to 3rd Party WMS Managed Storage Location

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this section a stock transfer between a non 3rd party WMS managed storage location as the sender and a 3rd party WMS managed storage location as a receiver. This stock transfer leads to the creation of an inbound delivery which will be transferred to WMS.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Transfer Stock - In-Plant (F1061). | The Transfer Stock-In-Plant screen displays. |  |
| 3 | Enter Material | Enter the following information:Material :<Material>Plant 3350 | The stock situation in the different storage locations assigned to the plant is shown. |  |
| 4 | Move stock from a non 3rd party managed storage location to a 3rd party managed storage location | Click on <!-- image omitted: unnamed -->behind the unrestricted-use stock of a Non 3rd Party WMS Managed Storage Location (for example, 995A).Click on <!-- image omitted: unnamed -->behind a 3rd party WMS managed storage location (for example, 991I).When the pop-up opens, enter the quantity you want to transfer.Choose Post.Note down the stock numbers to be able to compare it when the confirmation is posted. | A new windows open: Transfer Stock – in PlantA message is shown: Material document /0000 createdThe numbers are not yet updated – this happens when the confirmation from WMS system comes back |  |
| 5 | Check Creation of Web Services Message | Inbound Delivery Web Services Message is created. |  |  |

Execute both step [Confirm Inbound Delivery in WMS](#unique_15) [page ] 18 and [Check Stock Information](#unique_22) [page ] 25 to follow up in WMS and check the results.

#### Create Stock Transfer from 3rd Party WMS Managed Storage Location to 3rd Party WMS Managed Storage Location – Different Stock Type

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this section a stock transfer between two different stock types in a 3rd party WMS managed storage location as the sender and a receiver.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Transfer Stock - In-Plant (F1061). | The Transfer Stock-In-Plant screen displays. |  |
| 3 | Enter Material | Enter the following information:Material:<Material>Plant 3350 | The stock situation in the different storage locations assigned to the plant is shown. |  |
| 4 | Move stock from one stock type to another stock type in a 3rd party managed storage location | Click on <!-- image omitted: unnamed -->behind the unrestricted-use stock of the 3rd party WMS managed storage location (for example, 991I).Click on <!-- image omitted: unnamed -->behind the stock-in-quality stock of the same storage location (for example, 991I).When the pop-up opens, enter the quantity you want to transfer.Choose Post.Note down the stock numbers to be able to compare it when the confirmation is posted | A new windows open: Transfer Stock – in PlantA message is shown: Material document /0000 createdThe numbers are not yet updated – this happens when the confirmation from WMS system comes back | It should work from any stock type (unrestricted-use, blocked, stock in quality inspection, returns) to any other |
| 5 | Check Creation of Web Services Message | Outbound Delivery Web Services Message is created. |  |  |

Execute both step [Confirm Outbound Delivery in WMS](#unique_21) [page ] 25 and [Check Stock Information](#unique_22) [page ] 25 to follow up in WMS and check the results.

#### Create Scrap Posting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This section describes how to create a initial stock posting triggered from SAP S/4HANA Cloud Public Edition for a 3rd party WMS managed storage location.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Post Goods Movement (MIGO). | The Goods Movement screen displays. |  |
| 3 | Screen Settings | In the upper area, enter the following data and press Enter:First box: Goods IssueSecond box: otherMovement Type: 551 | Entries are made. |  |
| 4 | Enter Material Data | Enter the following data and press Enter:Material: <Material> | Entries are made. |  |
| 5 | Enter Quantity | Enter the following data in TAB Quantity and press Enter:Quantity:<Qty in Unit of Entry> |  |  |
| 6 | Enter Organization Data | Enter the following data in the Where tab and press Enter:Plant: 3350Storage Location: 991IReason for Movement: 0001Checkbox Item OK: <select> |  |  |
| 7 | Maintain Profitability Segment | Enter the following data in the Account Assignment tab and press Enter:Cost Center: 3350 |  |  |
| 8 | Confirm Entries | Choose Continue. |  |  |
| 9 | Post Goods Issue | Choose Post. | The goods are removed from stock with quantity and value. The goods value is posted to the account and to COPA. |  |

Execute step [Confirm Outbound Delivery in WMS](#unique_21) [page ] 25 and [Check Stock Information](#unique_22) [page ] 25 to follow up in WMS and check the results

#### Create Stock Transfer from 3rd Party WMS Managed Storage Location to 3rd Party WMS Managed Storage Location

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this section a stock transfer between a 3rd party WMS managed storage location as the sender and a 3rd party WMS managed storage location as a receiver. This stock transfer leads to the creation of an outbound delivery which will be transferred to WMS.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Post Goods Movement (MIGO). |  | Alternative SAP GUI: should be transaction MIGO or MIGO_TR |
| 3 | Screen Settings | In the upper area, enter the following data and press Enter:First box: Transfer PostingSecond box: otherMovement Type: 311Material: <Material>Plant: 3350From Storage Location: 991ITo Storage Location: 991KQty in Unit:5 PCChoose Post. | Message: Delivery xxx created. |  |
| 5 | Check creation of Web Services Message | Outbound Delivery Web Services Message should be created. |  |  |

#### Confirm Outbound Delivery in WMS

Purpose

In this section the outbound delivery Web Services message is received in the Third-party WMS. Some follow up processes need to be done there:

- Execute Goods Issue
- Confirmation transfer sent out to SAP S/4HANA Cloud Public Edition

The steps are not described here in detail because it might be any 3rd Party WMS.

#### Check Stock Information

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this section the updated stock information is checked.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Display Warehouse Stock - Deprecated (MB52). | The Display Warehouse Stocks of Material screen displays. |  |
| 3 | Enter material | Make the following entries:Material: <Material number>Plant :3350Storage Location: 991K and 991IPress Enter. | The Display Warehouse Stocks of Material shows. |  |
| 4 | Check stock | Check if the stock information is now updated and the decreased stock of the 3rd party WMS managed storage location is displayed |  |  |

#### Two Step Stock Transfer from Non 3rd Party WMS Managed Storage Location to 3rd Party WMS Managed Storage Location

##### Remove Stock from Non 3rd Party WMS Managed Storage Location

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori launchpad | Log on to the SAP Fiori launchpad with the Warehouse Clerk role. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Transfer Stock - In-Plant (F1061). | The Transfer Stock - In-Plant screen displays. |  |
| 3 | Open Stock Overview | Enter the following data in the appropriate fields and Enter:Plant: 3350Material: <Material> | The stock situation in the different storage locations assigned to the plant is shown. |  |
| 4 | Select Transfer from Stock | Select the icon <!-- image omitted: unnamed -->beside the Unrestricted-Use Stock in storage location that you want to transfer from,for example, a non 3rd Party WMS Managed Storage Location 995A. | The icons beside different stock types change. |  |
| 5 | Select Transfer to Stock | Select the icon <!-- image omitted: unnamed -->right of the column Stock Transfer (Storage Location) in the final target storage location that you want to transfer to, for example, a 3rd Party WMS Managed Storage Location 991I. Stock type Stock Transfer (Storage Location) is for stock in transit. | A dialog box opens. Storage Locations and Stock Types are selected according to your entries in the previous steps. |  |
| 6 | Enter Quantity | Enter the quantity that you want to transfer:Quantity: x PC |  |  |
| 7 | Post | Choose Post. | The system displays a message: Material document xxx created.The stock is moved from Unrestricted-Use Stock in 995A to Stock Transfer (Storage Location) in 991I. |  |

##### Place Stock to 3rd Party WMS Managed Storage Location

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Select Transfer from Stock Type - Stock Transfer (Storage Location) | Note In real-world scenarios, this procedure – placing the stock to the target 3rd party WMS managed storage location, might be conducted a certain period of time after the completion of the first removal procedure by the other warehouse clerks (it may take time to transfer the stock from one storage location to another as they're located in different cities). Here for the demo purposes, we use the same user right after the completion of the first removal procedure.Open Transfer Stock - In-Plant (F1061), select the icon <!-- image omitted: unnamed -->right of the column Stock Transfer (Storage Location) in storage location where stock in transit are stored (by previous procedure), for example 991I. | The icons beside different stock types change. |  |
| 2 | Select Transfer to Stock Type - Unrestricted-Use Stock | Select the icon <!-- image omitted: unnamed -->beside the Unrestricted-Use Stock in storage location that you want to transfer to as the final storage location, for example 991I. | A dialog box opens. Storage Locations and Stock Types are selected according to your entries in the previous steps. |  |
| 3 | Enter Quantity | Enter the quantity that you want to transfer:Quantity: x PC |  |  |
| 4 | Post | Choose Post. | The system displays a message: Inbound delivery document xxx created.The stock is transferred from Stock Transfer (Storage Location) to Unrestricted-Use Stock, stock will be updated once the confirmation from WMS received and processed in SAP S/4HANA Cloud Public Edition. |  |
| 5 | Check Creation of Web Services Message | Check an Inbound Delivery Web Services Message is created for the stock transfer. |  |  |

##### Confirm Inbound Delivery in WMS

Purpose

In this section the Inbound delivery Web Services message is received in the Third-party WMS. Some follow up processes need to be done there:

- Execute Goods Receipt
- Confirmation transfer sent out to SAP S/4HANA Cloud Public Edition

The steps are not described here in detail because it might be any 3rd Party WMS.

##### Check Stock Information

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this section the updated stock information is checked.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Warehouse Clerk. |  |  |
| 2 | Access the SAP Fiori App | Open Display Warehouse Stock - Deprecated (MB52). | The Display Warehouse Stocks of Material screen displays. |  |
| 3 | Enter material | Make the following entries:Material: <Material number>Plant: 3350Storage Location: 991I and 995APress Enter. | The Display Warehouse Stocks of Material shows. |  |
| 4 | Check stock | Check if the stock information is now updated and the updated Unrestricted Unit of the 3rd party WMS managed storage location is displayed. |  |  |

#### Two Step Stock Transfer from 3rd Party WMS Managed Storage Location to 3rd Party WMS Managed Storage Location

##### Two Step Stock Transfer from 3rd Party WMS Managed Storage Location to 3rd Party WMS Managed Storage Location

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this section a two-step stock transfer between a third-party Warehouse Management Systems (WMS) managed storage location as a sender and a third-party WMS managed storage location as a receiver is described. In this case, only one manual step - remove stock from the source storage location, is needed in the SAP S/4HANA Cloud Public Edition. Because the SAP S/4HANA Cloud Public Edition system automatically created a new inbound delivery for the second step - place stock to the target storage location.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori launchpad | Log on to the SAP Fiori launchpad with the Warehouse Clerk role. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Transfer Stock - In-Plant (F1061). | The Transfer Stock screen displays. |  |
| 3 | Open Stock Overview | Enter the following data in the appropriate fields and Enter:Plant: 3350Material: <Material> | The stock situation in the different storage locations assigned to the plant is shown. |  |
| 4 | Select Transfer from Stock | Select the icon <!-- image omitted: unnamed -->beside the Unrestricted-Use Stock in storage location that you want to transfer from,for example, a 3rd Party WMS Managed Storage Location 991I. | The icons beside different stock types change. |  |
| 5 | Select Transfer to Stock | Select the icon <!-- image omitted: unnamed -->right of the column Stock Transfer (Storage Location) in storage location that you want to transfer to. for example, a 3rd Party WMS Managed Storage Location for Return - 991K. Stock type Stock Transfer (Storage Location) is for stock in transit. | A dialog box opens. Storage Locations and Stock Types are selected according to your entries in the previous steps. |  |
| 6 | Enter Quantity | Enter the quantity that you want to transfer:Quantity: x PC |  |  |
| 7 | Post | Choose Post. | The system displays a message: Outbound Delivery document xxx created. |  |
| 8 | Check Creation of Web Services Message | Outbound Delivery and its Web Services Message are created. |  |  |

##### Confirm Outbound Delivery in WMS

Purpose

In this section the outbound delivery is replicated in the Third-party WMS. Some follow up processes need to be done in WMS:

- Execute Goods Issue against outbound delivery
- Confirmation message sent out to SAP S/4HANA Cloud Public Edition
- Once the confirmation message received and processed successfully in SAP S/4HANA Cloud Public Edition, the stock will be removed from Unrestricted-Use Stock in 991I to Stock Transfer (Storage Location) in 991K.
- An inbound delivery for placing the stock to the target storage location will then be automatically created and sent to your WMS.

The steps are not described here in detail because it might be any 3rd Party WMS.

##### Check Inbound Delivery Number in SAP S/4HANA Cloud Public Edition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this section you check the delivery number of the Inbound Delivery automatically created with the confirmation of Outbound Delivery in SAP S/4HANA Cloud Public Edition. As Inbound delivery Web Services Message is received in the 3rd Party WMS, once you have the Inbound Delivery number, you can continue to process the document in the 3rd Party WMS.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Display Outbound Delivery (VL03N). | The Display Outbound Delivery screen displays. |  |
| 3 | Open Outbound Delivery | Enter the Outbound Delivery number you noted down in previous steps and choose Continue. | The Outb.Deliv.Gds Mvmnt xxx Display: Overview screen displays. |  |
| 4 | Check Inbound Delivery Number | Choose Document Flow and note down the Inbound Delivery number. |  |  |

##### Confirm Inbound Delivery in WMS

The follow-up processes need to be done in the 3rd Party WMS:

- Execute Goods Receipt against the inbound delivery
- Confirmation message sent out to SAP S/4HANA Cloud Public Edition

The steps are not described here in detail because it might be any 3rd Party WMS.

Once the inbound delivery is confirmed and sent back to the SAP S/4HANA Cloud Public Edition, stock in transit will be placed to the Unrestricted-Use Stock of the target 3rd Party WMS managed storage location.

|  |
| --- |
| Note If you target storage location is non 3rd Party WMS Managed, for example, you have a two-step stock transfer between a third-party WMS managed storage location 991I as a sender and a non third-party WMS managed storage location 995A as a receiver, to place the stock in transit to the Unrestricted-Use Stock of the target storage location, it is recommended to post goods receipt directly with reference to the automatically created inbound delivery in the SAP S/4HANA Cloud Public Edition. For details, kindly refer to[2724138](https://me.sap.com/notes/2724138) |

##### Check Stock Information

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this section the updated stock information is checked.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Warehouse Clerk. |  |  |
| 2 | Access the SAP Fiori App | Open Display Warehouse Stock - Deprecated (MB52). | The Display Warehouse Stocks of Material screen displays. |  |
| 3 | Enter material | Make the following entries:Material: <Material number>Plant: 3350Storage Location: 991I and 991KPress Enter. | The Display Warehouse Stocks of Material shows. |  |
| 4 | Check stock | Check if the stock information is now updated and the updated Unrestricted Unit of the 3rd party WMS managed storage location is displayed. |  |  |

### Procurement Process

#### Create Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you create a purchase order for stock material directly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad as a Purchaser (Retail). | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Purchase Order - Advanced (ME21N). | The Create Purchase Order Advanced screen displays with a list of existing Purchasing Document Items. |  |
| 3 | Start Purchase Order creation | Without making any selection, choose Create. | The Create Purchase Order screen displays. |  |
| 4 | Enter Purchase Order data | Enter all of the necessary data.General Data:Supplier: 33213001Org. Data:Purchasing Org.:3310Purchasing Group:001Company Code: 3310In the Items section:Material: <Material>Quantity: <Quantity>Net Price: xPlant: 3350Storage Location: 991IIn the Items section, choose Delivery Schedule:Delivery date: <date in the future>In the Items section, choose Confirmations:Conf. Control > Inbound Delivery | The Create Purchase Order screen displays. |  |
| 5 | Save Purchase Order | Choose Save to save the Purchase Order. | A new Purchase Order is created. The system displays the message: Purchase order xxx created. |  |

#### Create Inbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create the inbound deliveries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad using the Role Receiving Specialist. | The Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Inbound Deliveries for Purchase Orders (VL34). | The Generation of Inbound Deliveries screen displays. |  |
| 3 | Create Inbound Delivery | Make the following entries then choose Execute:Document Number: XXX (Enter the purchase order number created in previous step)Delivery Date: XXX Delete the default date and enter the delivery date in purchase orderTest Run: uncheckedThe Inbound Delivery Number is displayed, write it down for further use. | A new Inbound Delivery is created.The Inbound Delivery Number is displayed. |  |

#### Goods Receipt in Third-Party WMS

Purpose

WMS receives the inbound delivery web service message. When goods arrive at the warehouse, the goods receipt is booked in WMS and the following processes such as quality checks in goods receipt area and storing goods in storage bins are managed and performed only in WMS according to your WMS-specific settings. Afterwards, the inbound delivery confirmation web service message needs to be created and sent to the SAP S/4HANA Cloud Public Edition system.

### Sales Process

#### Create Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This section describes how to create a sales order.

Prerequisite

Check the stock level of the material before you create the sales order. Make sure the stock is sufficient.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Sales Orders - VA01 (VA01). | The Create Sales Document screen displays. |  |
| 3 | Enter the Order type OR (Standard Order) | On the Create Sales Document screen, make the following entries and press Enter:Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 4 | Enter Order Details | On the Create Standard Order: Overview screen, make the following entries:Sold-to Party: <Customer Number>, for example, 33113005Ship-to Party: <Customer Number>, for example, 33113005Cust. Reference: <reference number>. Enter a customer purchase order number as reference.Material Number: <material number>Quantity: <great than 1>, for example, <10 PC>Plant : <plant> |  |  |
| 5 | Save Document | Choose Save Document.Make a note of the sales order number.Note The created sales order might need to be approved first before you proceed with follow-up activities. For details, refer to chapter Process Sales Order Approval in the Sell from Stock (BD9) test script. | The order is saved and the order confirmation is printed out. |  |

#### Create Outbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This section describes how to create an outbound delivery based on a sales order. The outbound delivery is the vehicle to inform the WMS about the activities which need to happen in the warehouse.

Procedure

The SAP S/4HANA Cloud Public Edition system automatically creates a Web Services message based on the outbound delivery and sends it to the Third-party WMS. This outbound Web Services message can be checked in the SAP S/4HANA Cloud Public Edition system.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Outbound Delivery - With Order Reference (VL01N). |  |  |
| 3 | Enter Order information | Make the following entry and choose Continue:Shipping Point : 3350Order: <order number from the chapter before> |  |  |
| 4 | Save the Outbound delivery | Change Storage Location into 991IDelivery Quantity: <10>Check the data.Choose Save.Make a note of the outbound delivery number.. | Outbound delivery is created. |  |

#### Picking and Goods Issue in Third-Party WMS

Purpose

The outbound delivery Web services message is received in the third-party WMS. Some follow-up processes need to be done there:

- Execute picking
- Update outbound delivery from WMS
- Split of the delivery
- Goods issue
- Confirmation delivery sent out to SAP S/4HANA Cloud Public Edition

The steps are not described here in details because it can be any third-party WMS.

#### Receive Split Outbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In case the sales order cannot get fulfilled in one delivery, a delivery split is performed by third-party WMS. This information is sent back to the SAP S/4HANA Cloud Public Edition system and could be checked there.

|  |
| --- |
| NoteTo split the original outbound delivery into two outbound deliveries in the SAP S/4HANA Cloud Public Edition System, delivery split information is sent to the SAP S/4HANA Cloud Public Edition System from the third-party WMS via either of the following interfaces:Split Outbound Delivery InboundDetermination of the delivery number of the newly split delivery:While using web service interface, delivery number of the newly split delivery is determined during the creation of the new delivery in the SAP S/4HANA Cloud Public Edition system after Split Outbound Delivery Inbound Web Services message is processed. Once the split delivery is created successfully, a confirmation message which includes the number of newly split delivery will be sent to the third-party WMS via the Web Service interface - Split Outbound Delivery Confirmation Outbound. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Outbound Delivery (VL03N). |  |  |
| 3 | Check Created Document | Enter the split outbound delivery number and press Enter. Check the delivery details. |  |  |

#### Receive Outbound Delivery Confirmation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When the delivery is completed in the third-party WMS, this information is send back to SAP S/4HANA Cloud Public Edition. This section describes how to check the related documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Outbound Delivery (VL03N). |  |  |
| 3 | Check Created Document | Enter the outbound delivery number and press Enter.Check the delivery details. |  |  |

### Customer Returns

#### Create Returns Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity you create a return order.

Procedure

You must have billing document or sales order document as reference (refer to [Create Sales Order](#unique_35) [page ] 36).

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Returns and Refund Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Customer Returns (F1708). |  |  |
| 3 | Navigate to Create Returns Order from Reference Document Screen | Choose Create. | The Create Returns Order from Reference Document screen is displayed. |  |
| 4 | Search for billing (sales) document to be referenced | Choose Show Filter Bars if it is hidden.Choose Adapt Filters if your desired filter is not shown.Enter the following selection criteria in the filter bar and choose Go:Reference Document: <sales order number or billing document number, which are created previously> | Billing (sales) documents are displayed in the Reference Documents table. |  |
| 5 | Create Return | Choose Create for the sales order the return should be created. | The Create Return from Order x dialog box displays. |  |
| 6 | Maintain return | Make the following entries:Return Reason: for example, customer ordered too muchQuantity:<Quantity>Choose Create. | The Edit Customer Return sceen displays. |  |
| 7 | Edit Customer Return | Choose Save and Release.Go back to Manage Customer Returns. | The General Information screen displays. |  |
| 8 | Check Adv. Returns Delivery | Find and choose the Customer Return you just created.On the Display Return's Order screen, choose Process Flow: Check dependent documents in process flow. Make a note of the follow-up document numbers for further use.Display Return delivery. | The dependent documents display. |  |

#### Perform Picking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, picking is done for return delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). | The Outbound Delivery Monitor - VL06O screen is displayed. |  |
| 3 | Choose Picking | Choose For Picking. |  |  |
| 4 | Enter Shipping point | Make the following entries and choose Execute:Shipping Point: for example, 335R. |  |  |
| 5 | Change outbound delivery | On the Day's Workload for Picking screen, select your delivery number and choose Change Outbound Deliveries. |  |  |
| 6 | Enter picked quantity | On the Picking tab, input quantity equal to delivery quantity in the Picked Qty field. |  |  |
| 7 | Choose Enter | Choose Enter. |  |  |
| 8 | Save | Choose Save. | The delivery has been picked. |  |

#### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When the returned material is received, goods receipt is posted for return delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |
| 2 | Access the SAP Fiori App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). | The Outbound Delivery Monitor - VL06O screen displays. |
| 3 | Choose Good Issue | Choose For Goods Issue. |  |
| 4 | Enter Shipping point | Make the following entries and choose Execute:Shipping Point: for example, 335R. |  |
| 5 | Post Good Issue | Mark the relevant delivery and choose Post Goods Issue. Choose today’s date from the dialog box. | The goods issue is posted. |

#### Perform Material Inspection

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you save the inspection results.

Prerequisite

The returned goods are received. During goods receipt for returns an inspection lot is created automatically.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Receiving Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Enter Inspection Results - From Warehouse (MSR_INSPWH). | The Worklist Selection of Deliveries screen displays. |  |
| 3 | Maintain selection criteria | Enter the following entries and choose Execute:Delivery items waiting for inspection: <select>Delivery: <Enter return delivery number> | The Change: Material Inspection in Warehouse for Delivery screen displays. |  |
| 4 | Choose Item tab | Choose the Item tab. |  |  |
| 5 | Maintain Inspection Result | In the Inspection Result subarea, enter the following data and press Enter:Inspection Code: <Enter inspection code>Inspected quantity: <Enter inspected quantity>If the Confirmation of Redetermination dialog box appears, choose Yes to confirm. |  |  |
| 6 | Maintain Follow-Up Activity | In the Logistical Follow-Up subarea, enter the following data and press Enter:Follow-Up Activity: <Enter follow-up activity>Note Choose appropriate follow-up activity according to inspection code. For example, choose follow-up activity Transfer to Free Available Stock responding to inspection code 0001. |  |  |
| 7 | Check Inspection Status | On the Header tab, in the Basic Data subarea, Inspection status shows Inspected, which means all received material is inspected completely. | All received material is inspected completely. |  |
| 8 | Save and Confirm | Choose Save and Confirm | Inspection result is recorded. |  |
| 9 | Perform Necessary Goods Movements | Perform all the necessary goods movements according to the Follow-Up Activity you decided in earlier steps. | Expected goods movements are posted correctly. For example, the goods are posted into your own un-restricted stock. |  |

#### Post Stock Transfer

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you move the returned goods to a storage location which is managed by decentralized WMS.

Prerequisite

The inspection is finished and the returned good is available in unrestricted stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Transfer Stock - In-Plant (F1061). | The Transfer Stock-In-Plant screen displays. |  |
| 3 | Enter Material | Enter the following entries and press Enter:Material:<Material>Plant: 3350 | Stock information displays |  |
| 4 | Create stock movement | Click on the arrow (up) for Returns (995R) blocked stock.Click on the arrow (down) for 3rd Party WMS ( 991I ) and blocked stock.Maintain the quantity and choose Post. | The Transfer stock in Plant window displays.Success message appears. |  |

#### Goods Receipt in Third-Party WMS

Context

WMS receives the inbound delivery Web Services message. When the goods arrive at the warehouse, the goods receipt is posted in WMS and the following process like storage of the goods in storage bins is done in WMS. In addition, the inbound delivery confirmation Web Services message needs to be created and sent to SAP S/4HANA Cloud Public Edition system.

#### Check Stock Information

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this section the updated stock information is checked.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Display Warehouse Stock - Deprecated (MB52). | The Display Warehouse Stocks of Material screen displays. |  |
| 3 | Enter material | Make the following entries:Material: <Material number>Plant :3350Storage Location: 991K and 991IPress Enter. | The Display Warehouse Stocks of Material shows. |  |
| 4 | Check stock | Check if the stock information is now updated and the decreased stock of the 3rd party WMS managed storage location is displayed |  |  |

### Return to Supplier Process

#### Create Return Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is to create a return purchase order for the supplier.

Prerequisite

Check the stock level of the material before you create the return purchase order. Make sure the stock is sufficient in the return storage location. To transfer material into the return storage location, go through [Create Stock Transfer from 3rd Party WMS Managed Storage Location to 3rd Party WMS Managed Storage Location](#unique_20) [page ] 24.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Purchaser (Retail). | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Purchase Order - Advanced (ME21N). | The Create Purchase Order screen displays. |  |
| 3 | Initial entry for return order | Make the following entries and press Enter:Order type: Standard POSupplier : 33213001Under the Header section, in the Org. Data tab, make following entries and press Enter:Purchasing Org: 3310Purchasing Group : 001Company Code: 3310On the Item Overview section, make following entries and press Enter:Material : for example,R_7000Quantity : X PCNet. Price :XAEDPlant: <Plant>Storage Location: 991KReturns Item: <Select the checkbox>In the Items section, choose Delivery Schedule:Delivery Date: <date in the future> | All data is entered, the Item Detail screen displays. |  |
| 4 | Save Purchase Order | Choose Save and when the purchase order number is displayed, write it down for further use. | A new Purchase Order is created.Purchase Order Number displays. |  |

#### Create Return Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This section describes how to create an outbound delivery based on a return purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open My Purchase Orders - Due for Delivery (VL10B). | The Purchase Order, Fast Display screen displays. |  |
| 3 | Enter data for PO Display | In the head area:Purchase Document: <enter the purchase order number from the step before>Choose Execute. | The Activities Due for Shipping "Purchase Order, Fast Display" displays. |  |
| 4 | Create delivery | Select the line of Purchase Order from the list. Choose Background to create delivery in the background.Two lines are displayed now. Select the one with the green arrow and choose Log for Delivery Creation. | The Delivery Creation Log screen displays.The number of the delivery displays. |  |
| 5 | Check Delivery number | Choose Documents.Note down the return delivery number shown in the Document field. |  |  |

#### Check Web Services Message and Execute in WMS

Purpose

The outbound delivery Web Services message is received in the third-party WMS. Some follow-up processes need to be done there:

- Execute picking
- Update outbound delivery from WMS
- (Optional) Split of the delivery
- Goods issue
- Confirmation delivery sent out to SAP S/4HANA Cloud Public Edition

#### Check Confirmation in SAP S/4HANA Cloud Public Edition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This section describes how to check the status of the return delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays |  |
| 2 | Access the App | Open Display Outbound Delivery (VL03N). | The Display Outbound Delivery screen displays. |  |
| 3 | Enter Delivery Number | Enter Delivery number in the Outbound Delivery field and press Enter. | The Returns (Pur. Ord.) Display Overview screen displays. |  |
| 4 | Check Status | Choose Status Overview tab.Check Goods Movement status. | Goods Movement Status of the delivery should be C. |  |

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
> Flagged while digesting this document, not verified: Config step 'Define default values for deliveries' sets Shipping Point 3310, while the master data table and later steps use shipping point 3350 for plant 3350 (3310 is the sales and purchasing org); possibly inconsistent with the sample data.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[15-retail-operations/test-script-retail-logistics-with-embedded-warehouse-management-69l-ae]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/69M_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 81,708 chars in the whole document
