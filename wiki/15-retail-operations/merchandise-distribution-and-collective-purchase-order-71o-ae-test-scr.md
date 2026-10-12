---
id: 15-retail-operations/merchandise-distribution-and-collective-purchase-order-71o-ae-test-scr
title: "Merchandise Distribution and Collective Purchase Order (71O_AE) - Test Script, SAP S/4HANA Cloud Public Edition 2608 (71O_S4CLD2608_BPD_EN_AE)"
description: "SAP test script for scope item 71O_AE: collective purchase orders and merchandise distribution by cross-docking, flow-through and put-away, with prerequisites."
cluster: 15-retail-operations
tags: [kb/retail-operations, topic/merchandise-distribution-and-allocation]
aliases: [71O_S4CLD2608_BPD_EN_AE]
keywords: [Merchandise Distribution and Allocation, merchandise distribution, collective purchase order, cross docking, flow-through process, put away process, distribution profiles, stock transfer orders, inbound delivery, goods receipt]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/71O_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1200
topic: 15-retail-operations/merchandise-distribution-and-allocation
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Merchandise Distribution and Collective Purchase Order (71O_AE) - Test Script, SAP S/4HANA Cloud Public Edition 2608 (71O_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/71O_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Merchandise Distribution and Allocation** in Retail Operations. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Merchandise Distribution and Collective Purchase Order (71O_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Merchandise Distribution and Collective Purchase Order (71O_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232859721)

[2 Prerequisites 4](#_Toc232859722)

[2.1 System Access 4](#_Toc232859723)

[2.2 Roles 4](#_Toc232859724)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232859725)

[2.4 Additional Manual Configuration 6](#_Toc232859726)

[2.5 Preliminary Steps 7](#_Toc232859727)

[2.5.1 Determine Storage Location with Situation 7](#_Toc232859728)

[2.5.2 Define Rules for Picking Location Determination 8](#_Toc232859729)

[2.5.3 Maintain Controlling Parameters 9](#_Toc232859730)

[2.5.4 Maintain Retail Site Parameters 10](#_Toc232859731)

[2.5.5 Maintain Distribution Profiles in the Reference Articles for the Reference Distribution Center 11](#_Toc232859732)

[2.5.6 Maintain Distribution Profile for Articles in Distribution Center 12](#_Toc232859733)

[2.5.7 Create Stock Transfer Order 13](#_Toc232859734)

[2.5.8 Assign Store Associate (User) to a Store 14](#_Toc232859735)

[3 Overview Table 16](#_Toc232859736)

[4 Test Procedures 18](#_Toc232859737)

[4.1 Merchandise Distribution using Cross Docking 18](#_Toc232859738)

[4.1.1 Create Collective Purchase Order 18](#_Toc232859739)

[4.1.2 Verify Collective Purchase Order 21](#_Toc232859740)

[4.1.3 Monitor EDI Message Summary for the Purchase Order 22](#_Toc232859741)

[4.1.4 Create Inbound Delivery 24](#_Toc232859742)

[4.1.5 Post Goods Receipt for Inbound Delivery 24](#_Toc232859743)

[4.1.6 Monitor Merchandise Distribution Manually 25](#_Toc232859744)

[4.1.7 Monitor Merchandise Distribution Automatically 27](#_Toc232859745)

[4.1.8 Perform Picking and Post Goods Issue for Outbound Delivery 28](#_Toc232859746)

[4.1.9 Receive Product in Store 29](#_Toc232859747)

[4.2 Merchandise Distribution using Flow-Through Process 30](#_Toc232859748)

[4.2.1 Create Collective Purchase Order 31](#_Toc232859749)

[4.2.2 Verify Collective Purchase Order 33](#_Toc232859750)

[4.2.3 Create Inbound Delivery 34](#_Toc232859751)

[4.2.4 Post Goods Receipt for Inbound Delivery 35](#_Toc232859752)

[4.2.5 Monitor Merchandise Distribution Manually 36](#_Toc232859753)

[4.2.6 Monitor Merchandise Distribution Automatically 38](#_Toc232859754)

[4.2.7 Perform Picking and Post Goods Issue for Outbound Delivery 39](#_Toc232859755)

[4.2.8 Receive Product in Store 40](#_Toc232859756)

[4.3 Merchandise Distribution using Put Away Process 41](#_Toc232859757)

[4.3.1 Create Collective Purchase Order 42](#_Toc232859758)

[4.3.2 Update Quantity in Collective Purchase Order 44](#_Toc232859759)

[4.3.3 Create Inbound Delivery 45](#_Toc232859760)

[4.3.4 Post Goods Receipt for Inbound Delivery 46](#_Toc232859761)

[4.3.5 Monitor Merchandise Distribution Manually 47](#_Toc232859762)

[4.3.6 Transfer Stocks Between Storage Location 49](#_Toc232859763)

## Purpose

Overview

Through collective purchase order processing, you can consolidate procurement for stores for efficient processing by an external supplier. Merchandise distribution manages the planned quantities for the stores, makes necessary adjustments, and efficiently executes logistics processes in the distribution center.

This scope item describes merchandise procurement through a pull process. First, you determine the demand for the stores and create the resulting documents as described in the scope item Replenishment Planning for Stores (3I7). If the supply source is a distribution center, you can combine the demand from stores into a collective purchase order for the distribution center at the external supplier.

You can create collective purchase orders either online or by scheduling a batch job run in the background. At the same time, the information for the merchandise distribution is created, and the quantities for the stores along with further data are being recorded.

After receiving the goods in the distribution center, you can adjust the quantities for the stores if the received quantities differ from those in the purchase order. You can adjust the merchandise distribution quantities either through a merchandise distribution monitor or in the background through a batch run. After the adjustment, the system creates and processes outbound deliveries for pickup and posts the goods issue. Finally, the stores receive the merchandise.

In case of automatic adjustment, the quantities are distributed to the stores and outbound deliveries are generated automatically at the time of goods receipt at distribution center.

The distribution center uses putaway, flow-through, and cross-docking methods (using Supplementary Logistics Services (SLS)) to process merchandise distribution.

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

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) |
| --- | --- | --- | --- |
| Allocator (Retail) | SAP_BR_ALLOCATOR_RETAIL | Allocation and Merchandise Distribution | SAP_BR_ALLOCATOR_RETAIL |
| Receiving Specialist | SAP_BR_RECEIVING_SPECIALIST | Receiving | SAP_BR_RECEIVING_SPECIALIST |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |
| Retail Store Associate | SAP_BR_RFM_STORE_ASSOCIATE | Store Operations | SAP_BR_RFM_STORE_ASSOCIATE |
| Purchaser (Retail) | SAP_BR_PURCHASER_RFM | Retail Purchasing / Retail Sourcing and Contracting | SAP_RFM_SPT_PURCHASING_PC / SAP_RFM_SPT_SOURCING_PC |
| Warehouse Clerk (Retail) | SAP_BR_WAREHOUSE_CLERK_RFM | Retail Inventory Processing | SAP_RFM_SPT_INVTRY_PROCG_PC |
| Master Data Specialist - Product Data (Retail) | SAP_BR_MD_SPCLST_ITEM_RFM | Retail Product Master Data | SAP_BR_MD_SPCLST_ITEM_RFM |
| Configuration Expert - Business Network Integration | SAP_BR_CONF_EXPERT_BUS_NET_INT | Business Network Integration / Business Network Integration - Concur Integration / Business Network Integration - Output Control / Business Network Integration - Data Replication / Configuration Expert - Business Network Integration Cross Applications | SAP_CORE_SPT_INT_PC / SAP_CON_SPT_CONCUR_INT_PC / SAP_OC_SPT_INT_PC / SAP_CA_SPT_DATA_REP_PC / SAP_CA_SPT_BUS_NETWORK_INT_PC |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Single Article | R_5000 | Hoodies Sticker | This article is relevant for cross docking process |
| Single Article | R_5002 | Paint Oil | This article is relevant for flow-through process |
| Single Article | R_5004 | PC Joystick | This article is relevant for flow -hrough process |
| Company Code | 3310 | Company Code 3310 |  |
| Merchandise Category | R5131002 | Sweatshirts & Hoodie |  |
| Purchasing Organization | 3310 | Purch. Org. 3310 |  |
| Purchasing Group | 001 | Group 001 |  |
| Sales Organization | 3310 | Dom. Sales Org |  |
| Distribution Center | 3350 | DC 3350 AE |  |
| Store | 3340 | Store 3340 AE |  |
| Store | 3341 | Store 3341 AE |  |
| Store | 3342 | Store 3342 AE |  |
| Store Storage Location | 994A | St.Loc.Neg.Stock |  |
| WH Storage Location for Putaway | 995A | Storage Loc. DC |  |
| WH Storage Location for Flow Through | 995B | Stor. Loc. DC FT |  |
| WH Storage Location for Cross Docking | 995C | Stor. Loc. DC CD |  |
| Supplier | 33213001 | Retail Non-Food Supplier AE |  |
| Reference Article | R_REF_FT | Ref article for Flow Through |  |
| Reference Article | R_REF_CD | Ref article for Cross Docking |  |

### Additional Manual Configuration

Before you can test this scope item for value added services (VAS), you must have completed the additional configuration steps for setting up the communication scenario SAP_COM_0224 for sourcing and procurement with suppliers integration.

These steps are described in Setup instruction of Integration of Procurement with External Suppliers (2EJ) under the following sections:

- Create Communication User
- Create Communication System
- Set Up Sourcing and Procurement with Suppliers Integration (SAP_COM_0224)
- Output Parameter Determination
- Assign Recipients.

The above mentioned configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/b20a5b9688168baeb48b973b8fef7457)

### Preliminary Steps

#### Determine Storage Location with Situation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Project Experience in SAP Central Business Configuration |  |  |
| 2 | Access the node | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Storage Location Determination with Situation. |  |  |
| 3 | Enter Plant | Enter Plant: 3350 in the popup window Determine Work Area: Entry and Choose Continue | Storage Location Determination: Overview screen is displayed |  |
| 4 | Create New Entry | Choose New Entries in the change view. Enter data in the below fields,For Flow through:Situation: for example <04, 14, 24>Location: 995BFor Putaway:Situation: for example <01, 11, 21>Location: 995AFor Cross Docking:Situation: for example <03, 13, 23>Location: 995CChoose Save | New entry created |  |

#### Define Rules for Picking Location Determination

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Project Experience in SAP Central Business Configuration |  |  |
| 2 | Access the node | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Rules for Picking Location Determination (101107). |  |  |
| 3 | Choose Configure | Choose the line item displayed. Choose Configure in the step Define Rules for Picking Location Determination | Screen Define Rules for Picking Location Determination: Change displays with the list of Delivery Types |  |
| 4 | Update the Rule | Select the line item with below Delivery Type and update the rule:Dlv Ty : NL – Replenishment Dlv.Rule Determ.StLoc.: RETAChoose Save | Data saved message is displayed |  |

#### Maintain Controlling Parameters

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Project Experience in SAP Central Business Configuration |  |  |
| 2 | Access the node | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Maintain Controlling Parameters (105508). |  |  |
| 3 | Choose Configure | Choose the Line item displayed.Choose Configure in the step Maintain Controlling Parameters | Screen is displayed with the reference distribution center. |  |
| 4 | Verify Reference Distribution Center | Verify the reference distribution center in the below fields and make a note.Maintain control parameters for retail material masterReference Distribution Center:Note down the reference distribution center number. |  |  |

#### Maintain Retail Site Parameters

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Project Experience in SAP Central Business Configuration |  |  |
| 2 | Access the node | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Maintain Retail Site Parameters (104671). |  |  |
| 3 | Choose Configure | Choose the Line item displayed. Choose Configure in the step Maintain Retail Site Parameters | Screen is displayed with the list of retail sites. |  |
| 4 | Maintain Distribution Profile | Select the line items with plant as below and enter the Distribution Profile:Plant 3350, 3391 and <Reference DC noted in process[Maintain Controlling Parameters](#unique_9) [page ] 9>Distribution Profile : <For example: R01 or R02>Choose SaveNote Select R01 for automatic adjustment and R02 for manual adjustment. | Distribution profile is maintained. |  |

|  |
| --- |
| Note Maintain distribution profile in both reference distribution center and distribution center. For more information, refer to SAP Accelerator: Set-Up Instructions for SAP S/4HANA Cloud Public Edition, retail, fashion, and vertical business, retail in the SAP Note [3313681](https://me.sap.com/notes/33136813313681). |

#### Maintain Distribution Profiles in the Reference Articles for the Reference Distribution Center

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Fiori Launchpad as a Master Data Specialist - Product Data (Retail). |  |  |
| 2 | Access the app | Open Maintain Article (MM42) app | Change Material (Initial Screen) screen is displayed |  |
| 3 | Enter Parameters | On the Change Material (Initial Screen) screen enter the following data:Material: R_REF_FT or R_REF_CDDistribution Center: 3391 and select Logistics: Distribution Center in the Views section.Choose Continue. | Change Material (Logistics: Distribution Center) screen is displayed |  |
| 4 | Maintain Distribution Profile | Under General Control Parameters,Distribution Profile: For Example: <R03> or <R02>Note For flow through relevant article, enter the R03 as distribution profile.For cross docking relevant article, enter the R02 as distribution profile. | Distribution profile maintained |  |
| 5 | Verify Storage Location | Under Storage Data section, verify the storage location data.Storage Location: 995BNote For flow through relevant article validate that 995B is assigned.For cross docking relevant article validate if 995C is assigned. | Flow through or Cross docking storage location 995B or 995C is maintained respectively. |  |
| 6 | Save | Choose Save. | Changes are saved in the article master. |  |

|  |
| --- |
| Note If a distribution center is missing in retail site parameters, an error message will be displayed as Error determining plant distribution profile for plant XXXXTo resolve this, you need to ensure that the distribution center is maintained with the distribution profile for retail site parameters specified in the step [Maintain Retail Site Parameters](#unique_10) [page ] 10. |

#### Maintain Distribution Profile for Articles in Distribution Center

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Fiori Launchpad as a Master Data Specialist - Product Data (Retail). |  |  |
| 2 | Access the app | Open Maintain Article (MM42) app. | Change Material (Initial Screen) screen is displayed |  |
| 3 | Enter Parameters | On the Change Material (Initial Screen) screen enter the following data:Material : For example: R_5002 or R_5000Distribution Center: 3350and select Logistics: Distribution Center in the Views section.Choose Continue. | Change Material (Logistics: Distribution Center) screen is displayed |  |
| 4 | Maintain Distribution Profile | Under General Control Parameters:Distribution Profile: For example:<R03> or <R02>Note For flow through relevant article give R03 as distribution profile.For cross docking relevant article give R02 as distribution profile. | Distribution Profile maintained |  |
| 5 | Verify Storage Location | Under Storage Data section, verify the storage location data.Storage Location: 995B or 995CNote For flow through relevant article validate if 995B is assigned.For cross docking relevant article validate if 995C is assigned. | Flow through storage location 995B or 995C is maintained. |  |
| 6 | Save | Choose Save | Changes are saved in the article master. |  |

|  |
| --- |
| Note Repeat the complete steps for R_5004.In case if any distribution center is missing with the retail site parameters, an error message will appear as Error determining plant distribution profile for plant XXXXTo resolve this, you need to ensure that the retail site parameters for the distribution center is maintained with the distribution profile specified in the step [Maintain Retail Site Parameters](#unique_10) [page ] 10. |

#### Create Stock Transfer Order

Use

To execute this scope item,open stock transfer order (STO) must be created by the the stores for the distribution center.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser (Retail). |  |  |
| 2 | Access the App | Open Create Purchase Order - Advanced (ME21N) app. |  |  |
| 3 | Enter Order Document Type and other data | Enter the following data, then choose Enter:Order Type: StockTranspOrderDel or UD StockTranspOrderDelSupplying Plant: 3350On the Header / Org. Data tab:Company Code: 3310Purchasing Group: 001Purchasing Org: 3310In Item Overview section:Material: R_5000, R_5002 and R_5004Plant: 3342Storage Location: 994AQuantity: xChoose Enter | All data are entered, the item detail screen is displayed. |  |
| 4 | Confirmation Proposal (Optional) | In the Confirmation Proposal screen, select Continue.Note Confirmation proposal will be asked only when there is no stock.In case of multiple line items, this popup may appear multiple times. |  |  |
| 5 | Save Stock Transfer Order | Choose Save, when the stock transfer order number is displayed, write it down for further use.Note Repeat the above step for other stores like 3340,3341 etc as well. | A new stock transfer order is created. Order number is displayed. |  |

#### Assign Store Associate (User) to a Store

Use

To filter the data provided in the SAP Fiori in-store merchandising apps, the store associate needs to be assigned to a certain store (site).

|  |
| --- |
| Note The store assignment can be changed at any point in time in case a store associate is helping in another store or if this is required for testing purposes. |

Procedure

| Step # | Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Retail Store Associate. |  |  |
| 2 | Open my Store Assignment app | Open My Store Assignment (F4334) app.Note If you are already assigned to store for which stock transfer order's are created in the previous steps (for example 3340), you can skip the entire procedure. |  |  |
| 3 | Search Store | Search for the stores ID:Store ID : for example 3340Select the magnifying glass or select GoNote Since there are multiple stock transfer orders created for different stores like 3341 and 3342 this process needs to be repeated once the stock is received in [Receive Product in Store](#unique_15) [page ] 29. |  |  |
| 4 | Select Store | Select the store you want the user to be assigned. | Store is selected. |  |
| 5. | Assign Store | Save the new assignment by selecting Assign Me on the top right above the list of stores. | The message pops up “You were assigned to store <Store created by you>.” is momentarily displayed. The assigned store above the list is updated accordingly. |  |
| 6. | Exit Screen | Select Back | The SAP Fiori Launchpad is displayed containing all relevant apps for the Retail Store Associates |  |

Result

When assigned to a store, store associate has access to relevant information of the assigned store, increasing the efficiency of the day-to-day work.

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Merchandise Distribution using Cross Docking

| ID (Role Template) | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Collective Purchase Order](#unique_17) [page ] 18 | Allocator (Retail) | Create Collective Purchase Orders (WF10) | Collective purchase order is created for stock transfer order |
| [Verify Collective Purchase Order](#unique_18) [page ] 21 | Purchaser (Retail) | Display Purchase Order - Advanced (ME23N) | Collective purchase order is displayed |
| [Monitor EDI Message Summary for the Purchase Order](#unique_19) [page ] 22 | Configuration Expert - Business Network Integration | Message Dashboard (/AIFX/WDA_MSG_MONITOR) |  |
| [Create Inbound Delivery](#unique_20) [page ] 34 | Receiving Specialist |  | Inbound delivery is created for collective purchase order |
| [Post Goods Receipt for Inbound Delivery](#unique_21) [page ] 46 | Warehouse Clerk | Post Goods Movement (MIGO) | Goods receipt is posted for inbound delivery |
| [Monitor Merchandise Distribution Manually](#unique_22) [page ] 25 | Allocator (Retail) | Monitor Merchandise Distribution (WF30) | Quantity is adjusted manually and Outbound delivery is created |
| [Monitor Merchandise Distribution Automatically](#unique_23) [page ] 27 | Allocator (Retail) | Monitor Merchandise Distribution (WF30) | Quantity is adjusted automatically and Outbound deliveries are created automatically |
| [Perform Picking and Post Goods Issue for Outbound Delivery](#unique_24) [page ] 39 | Shipping Specialist | Change Outbound Delivery (VL02N) | Picking and Goods issue is posted for outbound delivery |
| [Receive Product in Store](#unique_15) [page ] 29 | Retail Store Associate | Receive Products (F1248) | Goods receipt is created for received products |

Merchandise Distribution using Flow Through

| ID (Role Template) | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Collective Purchase Order](#unique_25) [page ] 42 | Allocator (Retail) | Create Collective Purchase Orders (WF10) | Collective purchase order is created for stock transfer order |
| [Verify Collective Purchase Order](#unique_26) [page ] 33 | Purchaser (Retail) | Display Purchase Order - Advanced (ME23N) | Collective purchase order is displayed |
| [Create Inbound Delivery](#unique_20) [page ] 34 | Receiving Specialist |  | Inbound delivery is created for collective purchase order |
| [Post Goods Receipt for Inbound Delivery](#unique_21) [page ] 46 | Warehouse Clerk | Post Goods Movement (MIGO) | Goods receipt is posted for inbound delivery |
| [Monitor Merchandise Distribution Manually](#unique_27) [page ] 36 | Allocator (Retail) | Monitor Merchandise Distribution (WF30) | Quantity is adjusted manually and Outbound delivery is created |
| [Monitor Merchandise Distribution Automatically](#unique_23) [page ] 27 | Allocator (Retail) | Monitor Merchandise Distribution (WF30) | Quantity is adjusted automatically and Outbound deliveries are created automatically |
| [Perform Picking and Post Goods Issue for Outbound Delivery](#unique_24) [page ] 39 | Shipping Specialist | Change Outbound Delivery (VL02N) | Picking and Goods issue is posted for outbound delivery |
| [Receive Product in Store](#unique_15) [page ] 29 | Retail Store Associate | Receive Products (F1248) | Goods receipt is created for received products |

Merchandise Distribution using Put Away

| ID (Role Template) | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Collective Purchase Order](#unique_25) [page ] 42 | Allocator (Retail) | Create Collective Purchase Orders (WF10) | Collective purchase order is created for stock transfer order |
| [Update Quantity in Collective Purchase Order](#unique_28) [page ] 44 | Purchaser (Retail) | Change Purchase Order - Advanced (ME22N) | Collective purchase order is displayed |
| [Create Inbound Delivery](#unique_29) [page ] 45 | Receiving Specialist |  | Inbound delivery is created for collective purchase order |
| [Post Goods Receipt for Inbound Delivery](#unique_21) [page ] 46 | Warehouse Clerk | Post Goods Movement (MIGO) | Goods receipt is posted for inbound delivery |
| [Monitor Merchandise Distribution Manually](#unique_30) [page ] 47 | Allocator (Retail) | Monitor Merchandise Distribution (WF30) | Quantity is adjusted manually and Outbound delivery is created |
| [Transfer Stocks Between Storage Location](#unique_31) [page ] 49 | Warehouse Clerk (Retail) | Transfer Stock (F1061) | Quantity is adjusted manually and Outbound delivery is created |

## Test Procedures

### Merchandise Distribution using Cross Docking

Purpose

The collective purchase orders are used for planning of the distribution of merchandise on short delivery basis. This business process can be used to accumulate requirements for merchandise distribution using the pull process and to generate collective purchase order, which combine the requirements of the unique end recipients (stores) into one common purchase order, which can be transferred to the supplier.

The process variant for collective purchase order with the Supplementary Logistics Services (SLS) allows the company to build up a scenario of cross docking with pre-packing. In a collective purchase order, the materials can be ordered for which the supplier performs special services (for example, pre-packing). If a collective purchase order is generated for a material for which SLS data is defined, the SLS data is automatically included in the collective purchase order. If pre-packing is required, the system generates sub-items for every collective purchase order item. A sub-item is created for each recipient and the quantity allocated to that recipient. This is used for cross-docking scenarios with the prepacking, where the pre-picked merchandise is packed appropriately by the supplier based on a purchase order.

In this case, all the process steps are the same, however the outcome of the process is a purchase order containing the sub-items for the pre-packing.

|  |
| --- |
| Note Before executing the followed topics, implement the BAdI Activate SLS Sub-items Generation in Collective Purchase Orders. You can use this BAdI to activate prepacking merchandise (SLS function) for a specific group of articles (merchandise category for example).To increase the efficiency of the supply chain, goods that pass through distribution centers are handled using fast track process like cross-docking.Example You can implement the merchandise category R5131002 as relevant for sub-items generation in collective purchase order to execute the test steps mentioned within this document.. |

|  |
| --- |
| Note Prerequisite for a collective purchase order creation is to have stock transfer orders are created (in preliminary step [Create Stock Transfer Order](#unique_13) [page ] 13) for the multiple Stores (for example 3340, 3341, 3342 etc) from a particular distribution center (for example 3350).Articles chosen for cross-docking method must have distribution profile as cross-docking for the distribution center. |

#### Create Collective Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can create collective purchase order either manually or by scheduling an application job.

In order to satisfy all of the demands made by the stores in the form of Stock Transfer Orders (STOs), a single collective purchase order will be created for each supplier under the collective purchase order. As soon as stock arrives at the distribution center, it goes through a distribution process because issue documents in the form of stock transfer orders have already been created against these collective purchase order.

|  |
| --- |
| Note If collective purchase orders are already created for a particular distribution center using Option 1, then to execute Option 2 STOs need to be re-created in the step [Create Stock Transfer Order](#unique_13) [page ] 13. |

Procedure

Option 1: Create Collective Purchase Order Manually

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Allocator (Retail). |  |  |
| 2 | Access the SAP Fiori App | Open Create Collective Purchase Orders (WF10) app. | The Create Collective Purchase Order: Selection and Control Parameters (WF10) screen is displayed. |  |
| 3 | Enter the Selection Parameters | Enter the following data and then choose Run:Under Organizational data:Distribution Center: 3350Purchasing Organization: 3310Under Scheduling:Procurement period – date: <From date> and <To date>Schedule - line interval: <no.of days> for example 1Note Kindly ensure that the delivery dates of the STOs created in preliminary steps must fall with in the date range of the procurement period-date provided in the selection screen. | The Worklist screen is displayed.Note In case if there are no STOs available that satisfies above selection criteria then a message popup will appear as No documents selected. |  |
| 4 | Validate Processing Method | Verify the processing method for each material. | Processing Method 2 will be displayed for cross-docking articles. |  |
| 5 | Validate Stock Transport Order | Select each line-item material to see the applicable STO number. | STO number will be listed under Issue Document number. You can also navigate to the STO number to see the details. |  |
| 6 | Choose Worklist | Select the entry displayed under Worklist for ordered merchandise and then choose Worklist. | Document number gets updated in the entry and the below message is displayed.1 collective purchase orders were generated. Check application log generated. |  |

Option 2: Schedule a Job for Generating Collective Purchase Order

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Allocator (Retail). |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Collective Purchase Order Generation (F7821) app. | The Schedule Collective Purchase Order Creation screen is displayed. |  |
| 3 | Provide input values | On the initial screen choose CreateJob Template: Create collective purchase order schedulerJob Name: Create collective purchase order schedulerSelect Step 2Select Step 3Select Parameters for selection criteria:Under Organizational data:Distribution Center: 3350Purchasing Organization: 3310Under Scheduling:Procurement period – date: <From date> and <To date>Schedule - line interval: for example 1 <no.of days>Note Kindly ensure that the delivery dates of the STOs created in preliminary steps must fall with in the date range of the procurement period-date provided in the selection screen. | The Worklist screen is displayed.Note In case if there are no STOs available that satisfies above selection criteria then a message popup will appear as No documents selected. |  |
| 4 | Check Job Parameters | Select Check for validating. | A message is displayed as You can go ahead and schedule the job. |  |
| 5 | Schedule job | Choose Schedule | Job Create collective purchase order scheduler has been scheduled message is displayed. |  |
| 6 | Check Job Results | On the Application Jobs screen, after job item status turned to finished, choose navigate to job results in the Results column.Note down the collective purchase order number created. | Document (ID XXXXXXX) screen is displayed with job results. |  |

#### Verify Collective Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Use this process step to verify the collective purchase order created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Purchaser (Retail) |  |  |
| 2 | Access the App | Open Display Purchase Order - Advanced (ME23N) app. |  |  |
| 3 | Display Collective Purchase Order | Choose Other Purchase Order, enter below details in Select Document popup window. Choose Other DocumentPurchase Order : <Enter Doc number noted in previous process> | Document details will be displayed |  |
| 4 | Verify the Value Added Service | Seletc the line item and choose Value-Added-Service button in Item Overview. | Validate the recipient of the packed item details, which must be equal to the stores for which initially stock transport orders were created.Also, validate value-added-service Item No, UOM of the packed items and SLS field. |  |
| 5 | Verify the Details | Verify the details of Quantity, storage location for cross-docking (995C) and Delivery date in the document | Details of the collective PO is verified |  |

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

#### Create Inbound Delivery

Use

Use this step to create an inbound delivery against Collective Purchase Order (CPO) created in previous steps.

Procedure

| Step # | Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Receiving Specialist. |  |  |
| 2 | Access the App | Open the app | The screen is displayed |  |
| 3 | Enter the Details | Enter all the details as mentioned:Purchase Order number : XXXXXXXX (Please refer to purchase order which is created in chapter [Create Collective Purchase Order](#unique_25) [page ] 42)Supplier: for example 33213001Delivery date : <DD.MM.YYYY> | Key values option list is visible. |  |
| 4 | Select Continue | Select Continue | Detail screen is displayed |  |
| 5 | Validate the Delivery Quantity and Storage Location | Validate the Delivery Quantity for each product and storage location. |  |  |
| 6 | Select Save Document | Select Save.Make a note of inbound delivery number. | A message is displayed as Inbound delivery xxxxxxxxx has been saved. |  |

|  |
| --- |
| Note Access the saved Inbound delivery in Display Inbound Delivery (VL33N) app and verify the details in value added services popup by choosing VAS. |

#### Post Goods Receipt for Inbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Use this step to post the good receipt for the inbound delivery created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Warehouse Clerk |  |  |
| 2 | Access the app | Open Post Goods Movement (MIGO) app. | The Goods Receipt screen is displayed. |  |
| 3 | Enter Inbound Delivery Number | Provide the values for the following entries:Select Goods Receipt and Inbound Delivery from the dropdown and enter the following:Inbound Delivery Number: XXXGoods Movement Type: 101Select ENTER. | The data with in the selected inbound delivery like article, quantities are displayed. |  |
| 4 | Check and Post the Goods Receipt for Inbound Delivery | Scroll to the bottom of the Goods Receipt Inbound Delivery xxxxxxxxxx screen, select the Item OK checkbox to check. Select Check on the bottom right of the screen.Select Post. | The goods receipt is posted.Message Material Document <Document number> posted. is displayed. |  |

#### Monitor Merchandise Distribution Manually

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Use this step to do manual adjustments and generate the outbound deliveries, hence this will allow all the functions with the user interaction for merchandise distribution.

|  |
| --- |
| Note To execute this process, you must select Distribution Profile as R02 in [Maintain Retail Site Parameters](#unique_10) [page ] 10 for the distribution center 3350.If the distribution Profile for distribution center is altered in step - [Maintain Retail Site Parameters](#unique_10) [page ] 10, you must execute whole process again starting with the creation of stock transport order. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Allocator (Retail) |  |  |
| 2 | Access the App | Open Monitor Merchandise Distribution (WF30) app. | The Merchandise Distribution: Monitor screen is displayed |  |
| 3 | Display Options | Under display options, you will have below two options:As List (selected by default)As Table | If As List view is choosen, you can expand and see stock transport order numbersIf As Table view option is choosen than collective purchase order and stock transport order will appear in tabular format. |  |
| 3 | Enter the details | Enter the below details and choose Execute.Under Parameter section,Distribution Center: 3350Under Supplier Purchase Orders:Purchase Order Number: <Enter the Collective Purchase Order number created in [Create Collective Purchase Order](#unique_25) [page ] 42> | The Merchandise Distribution: Monitor screen is displayed with the list of collective purchase orders and corresponding stock transport orders. |  |
| 4 | Choose Adjust | Select Collective Purchase Order Document and Choose Adjust displaying on the bottom right corner of the screenNote In case of multiple entries, repeat the steps for each entry. | The Adjust Distribution screen is displayed with stock transport order document details |  |
| 5 | Adjust the Quantity | Adjust the quantity in the below field - if required.Cross-docking Quantity (CD Qty): <quantity>Note The system will suggest cross-docking quantity which is equal to plan quantity.Choose Save | Distribution adjusted. Follow-on documents created in line with settings message is displayed. |  |
| 6 | Validate Adjustment | Navigate back to Merchandise Distribution: Monitor screen.Refresh the screen.Check the status of the Procurement Status for Collective Purchase Order. | Procurement status for collective purchase order must be Green. |  |
| 7 | Create Deliveries | Select the document line items and choose Deliveries option displaying on the bottom right corner of the screen | Deliveries were/are being posted message is displayed. |  |
| 8 | Validate the General Status of Distribution | Refresh the screen.Check the Status of Distribution for stock transport order number. | General status of distribution for stock transport order must be Green as deliveries are created. |  |
| 9 | Check Delivery Number | Choose stock transfer order numberNote If there are multiple stock transfer orders involved, please repeat the steps to note down all the outbound deliveries created.Make a note of delivery number. | Delivery number will Display against the stock transport order. Make a note of Delivery number. |  |

#### Monitor Merchandise Distribution Automatically

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Use this process step to validate the quantity is automatically adjusted during goods receipt and outbound deliveries are automatically generated. You can validate the procurment status and general status of distribution to confirm if adjustment and delivery generation is completed or not.

In general, the merchandise distribution is done automatically. For example, if there are no differences between the purchased quantity and the delivered quantity there is no user interaction necessary to create the outbound deliveries.

|  |
| --- |
| Note To execute this process, you must select Distribution Profile as R01 in [Maintain Retail Site Parameters](#unique_10) [page ] 10 for distribution center 3350.If the distribution profile for distribution center is changed in step - [Maintain Retail Site Parameters](#unique_10) [page ] 10, you have to execute whole process again starting with the step - [Create Stock Transfer Order](#unique_13) [page ] 13. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Allocator (Retail) |  |  |
| 2 | Access the App | Open Monitor Merchandise Distribution (WF30) app. | The Merchandise Distribution: Monitor screen is displayed |  |
| 3 | Enter the details | Enter the below details and Choose Execute.Under Parameter section,Distribution Center: 3350Under Supplier Purchase Orders:Purchase Order Number: <Mention the purchase order created in [Create Collective Purchase Order](#unique_25) [page ] 42> | The Merchandise Distribution: Monitor screen is displayed with the list of collective purchase order and corresponding stock transfer orders. |  |
| 4 | Validate Adjustment | Check the status of the Procurement Status for Collective Purchase Order. | Procurement status for collective purchase order must be Green. |  |
| 5 | Validate the General Status of Distribution | Check the Status of Distribution for stock transfer order number. | General status of distribution for stock transfer order must be Green as deliveries are auto-created. |  |
| 6 | Validate Outbound Delivery | Choose stock transfer order numberNote If there are multiple stock transfer orders involved, please repeat the steps to note down all the outbound deliveries created.Make a note of delivery number. | Purchase Order History tab in the stock transfer order will have an entry created for outbound delivery. |  |

#### Perform Picking and Post Goods Issue for Outbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Use this process step to pick and post goods issue for outbound delivery created previously.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Shipping Specialist. |  |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N) app. | Change Outbound Delivery (VL02N) screen is displayed. |  |
| 3 | Enter Parameters | Enter the Outbound Delivery :<Provide Outbound Delivery number>Choose Continue. | RST Outbound Dlv. xxxxxx Change: Overview screen is displayed. |  |
| 4 | Validate the Delivery Quantity | Validate the Delivery Quantity. |  |  |
| 5 | Post Goods Issue | Choose Post Goods Issue. | Message is displayed as Replenishment Dlv.xxxxxxxx saved, material document xxxxxxxxxx created. |  |

#### Receive Product in Store

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Use this process step to perform the goods receipt against the outbound delivery as a store associate, created in previous steps for the Stock Transfer Order (STO) created in preliminary steps.

|  |
| --- |
| Note To perform this step, validate the assigned store and assign the desire store as specified in the step [Assign Store Associate (User) to a Store](#unique_14) [page ] 14. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Retail Store Associate |  |  |
| 2 | Access the App | Open Receive Products (F1248) app. | The Receive Products screen is displayed. |  |
| 3 | Open Document | Select EnterID.Outbound Delivery: <created in previous step>and select OK to open it. | The details of the delivery are displayed |  |
| 4 | Post the goods receipt | Verify the quantity and Choose Post displaying on the bottom right corner of the screen. | A popup with message Document items will be posted in the background displayed and Status changes to Completed.This Step will post goods receipt in the store. |  |

|  |
| --- |
| Note Since there are multiple stock transport orders created for different stores like 3341 and 3342 once the stock is received in the assigned store you need to change the assigment in [Assign Store Associate (User) to a Store](#unique_14) [page ] 14 and repeat the above step to receive the product for each store. |

### Merchandise Distribution using Flow-Through Process

Purpose

This process step can be used to create a Collective Purchase Order (CPO) with external supplier based on the demands (STOs) raised by stores.

In the Merchandise Distribution process merchandise can passed through the distribution center using the flow-through method without placing it into the stock for storage. Flow-through enables you to process merchandise quickly and cost-effectively in just a few steps.

The distribution data is adjusted to match the quantities that are effectively available at goods receipt. The merchandise is then distributed to recipients using flow-through processing method. The merchandise is then moved to the goods issue area where the goods issue is then booked.

|  |
| --- |
| Note Prerequisite for a collective purchase order creation is to have stock transfer orders are created (in preliminary step [Create Stock Transfer Order](#unique_13) [page ] 13) for the multiple Stores (for example 3340, 3341, 3342 etc) from a particular DC (for eg 3350).Articles chosen for flow-through method must have distribution profile as flow through for the DC. |

#### Create Collective Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can create collective purchase order either manually or by scheduling an application job.

In order to satisfy all of the demands made by the stores in the form of Stock Transfer Orders (STOs), a single collective purchase order will be created for each supplier under the collective purchase order. As soon as stock arrives at the distribution center, it goes through a distribution process because issue documents in the form of stock transfer orders have already been created against these collective purchase order.

|  |
| --- |
| Note If collective purchase orders are already created for a particular distribution center using Option 1 then to execute Option 2 STOs need to be re-created in the step [Create Stock Transfer Order](#unique_13) [page ] 13. |

Procedure

Option 1: Create Collective Purchase Order Manually

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Allocator (Retail). |  |  |
| 2 | Access the SAP Fiori App | Open Create Collective Purchase Orders (WF10) app. | The Create Collective Purchase Order: Selection and Control Parameters (WF10) screen is displayed. |  |
| 3 | Enter the Selection Parameters | Enter the following data and then choose Execute:Under Organizational data:Distribution Center: 3350Purchasing Organization: 3310Under Scheduling:Procurement period – date: <From date> and <To date>Schedule - line interval: <no.of days> for example 1Note Kindly ensure that the delivery dates of the STOs created in preliminary steps must fall with in the date range of the procurement period-date provided in the selection screen. | The Worklist screen is displayed.Note In case if there are no STOs available that satisfies above selection criteria then a message popup will appear as No documents selected. |  |
| 4 | Validate Processing Method | Verify the processing method for each material. | Processing Method 3 will be displayed for flow through articles. |  |
| 5 | Validate Stock Transport Order | Select each line-item material to see the applicable STO number. | STO number will be listed under Issue Document number. You can also navigate to the STO number to see the details. |  |
| 6 | Choose Worklist | Select the entry displayed under Worklist for ordered merchandise and then choose Worklist. | Document number gets updated in the entry and the below message is displayed.1 collective purchase orders were generated. Check application log generated. |  |

Option 2: Schedule a Job for Generating Collective Purchase Order

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Allocator (Retail). |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Collective Purchase Order Generation (F7821) app. | The Schedule Collective Purchase Order Creation screen is displayed. |  |
| 3 | Provide input values | On the initial screen choose CreateJob Template: Create collective purchase order schedulerJob Name: Create collective purchase order schedulerSelect Step 2Select Step 3Select Parameters for selection criteria:Under Organizational data:Distribution Center: 3350Purchasing Organization: 3310Under Scheduling:Procurement period – date: <From date> and <To date>Schedule - line interval: for example 1 <no.of days>Note Kindly ensure that the delivery dates of the STOs created in preliminary steps must fall with in the date range of the procurement period-date provided in the selection screen. | The Worklist screen is displayed.Note In case if there are no STOs available that satisfies above selection criteria then a message popup will appear as No documents selected. |  |
| 4 | Check Job Parameters | Select Check for validating. | A message is displayed as You can go ahead and schedule the job. |  |
| 5 | Schedule job | Choose Schedule | Job Create collective purchase order scheduler has been scheduled message is displayed. |  |
| 6 | Check Job Results | On the Application Jobs screen, after job item status turned to finished, Choose Navigate to job results in the Results column.Note down the CPO number created. | Document (ID XXXXXXX) screen is displayed with job results. |  |

#### Verify Collective Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Use this process step to verify the collective purchase order created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Purchaser (Retail) |  |  |
| 2 | Access the App | Open Display Purchase Order - Advanced (ME23N) app. |  |  |
| 3 | Display Collective Purchase Order | Choose Other Purchase Order, enter below details in Select Document popup window. Choose Other DocumentPurchase Order : <Enter Doc number noted in previous process> | Document details will be displayed |  |
| 4 | Verify the details | Verify the details of quantity, storage location for flow through (995B) and delivery date in the document | Details of the collective purchase orfder is verified |  |

#### Create Inbound Delivery

Use

Use this step to create an inbound delivery against Collective Purchase Order (CPO) created in previous steps.

Procedure

| Step # | Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Receiving Specialist. |  |  |
| 2 | Access the App | Open the app | The screen is displayed |  |
| 3 | Enter the details | Enter all the details as mentioned:Purchase Order number : XXXXXXXX (Please refer to purchase order which is created in chapter [Create Collective Purchase Order](#unique_25) [page ] 42)Supplier: for example 33213001Delivery date : <DD.MM.YYYY> | Key values option list is visible. |  |
| 4 | Select continue | Select Continue | Detail screen is displayed |  |
| 5 | Enter the quantity | Enter the Putaway Quantity for each product equal to the Delivery Quantity. |  |  |
| 6 | Select save document | Select Save.Make a note of inbound delivery number. | A message is displayed as Inbound delivery xxxxxxxxx has been saved. |  |

#### Post Goods Receipt for Inbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Use this step to post the good receipt for the inbound delivery created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Warehouse Clerk |  |  |
| 2 | Access the app | Open Post Goods Movement (MIGO) app. | The Goods Receipt screen is displayed. |  |
| 3 | Enter Inbound Delivery Number | Provide the values for the following entries:Select Goods Receipt and Inbound Delivery from the dropdown and enter the following:Inbound Delivery Number: XXXGoods Movement Type: 101Select ENTER. | The data with in the selected inbound delivery like article, quantities are displayed. |  |
| 4 | Check and Post the Goods Receipt for Inbound Delivery | Scroll to the bottom of the Goods Receipt Inbound Delivery xxxxxxxxxx screen, select the Item OK checkbox to check. Select Check on the bottom right of the screen.Select Post. | The goods receipt is posted.Message Material Document <Document number> posted. is displayed. |  |

#### Monitor Merchandise Distribution Manually

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Use this step to do manual adjustments and generate the outbound deliveries, hence this will allow all the functions with the user interaction for merchandise distribution.

|  |
| --- |
| Note To execute this process, you must select Distribution Profile as R02 in [Maintain Retail Site Parameters](#unique_10) [page ] 10 for the distribution center 3350.If the distribution profile for distribution center is altered in step - [Maintain Retail Site Parameters](#unique_10) [page ] 10, you must execute whole process again starting with the creation of Stock Transport Order (STO). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Allocator (Retail). |  |  |
| 2 | Access the App | Open Monitor Merchandise Distribution (WF30) app. | The Merchandise Distribution: Monitor screen is displayed |  |
| 3 | Display Options | Under Display Options, you will have below two options:As List (selected by default)As Table | If As List view is choosen, you can expand and see STO numbersIf As Table view option is choosen than collective purchase order and STO will appear in tabular format. |  |
| 4 | Enter the details | Enter the below details and choose Execute.Under Parameter section,Distribution Center: 3350Under Supplier Purchase Orders:Purchase Order Number: <Enter the Collective Purchase Order number created in [Create Collective Purchase Order](#unique_25) [page ] 42> | The Merchandise Distribution: Monitor screen is displayed with the list of collective purchase orders and corresponding STOs. |  |
| 5 | Choose Adjust | Select Collective Purchase Order Document and choose Adjust displaying on the bottom right corner of the screenNote In case of multiple entries, repeat the steps for each entry. | The Adjust Distribution screen is displayed with STO document details |  |
| 6 | Adjust the Quantity | Adjust the quantity in the below field - if required.Flow Through Quantity (FT Qty): <quantity>Note The system will suggest FT quantity which is equal to plan quantity.Choose Save | Distribution adjusted. Follow-on documents created in line with settings message is displayed. |  |
| 7 | Validate Adjustment | Navigate back to Merchandise Distribution: Monitor screen.Refresh the screen.Check the status of the Procurement Status for Collective Purchase Order. | Procurement status for collective purchase order must be green. |  |
| 8 | Create Deliveries | Select the document line items and choose Deliveries option displaying on the bottom right corner of the screen | Deliveries were/are being posted message is displayed. |  |
| 9 | Validate the General Status of Distribution | Refresh the screen.Check the Status of Distribution for STO number. | General status of distribution for STO must be green as deliveries are created. |  |
| 10 | Check Delivery Number | Choose stock transfer order numberNote If there are multiple stock transfer orders involved, please repeat the steps to note down all the outbound deliveries created.Make a note of delivery number. | Delivery number will display against the STO. Make a note of delivery number. |  |

#### Monitor Merchandise Distribution Automatically

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Use this process step to validate the quantity is automatically adjusted during goods receipt and outbound deliveries are automatically generated. You can validate the procurment status and general status of distribution to confirm if adjustment and delivery generation is completed or not.

In general, the merchandise distribution is done automatically. For example, if there are no differences between the purchased quantity and the delivered quantity there is no user interaction necessary to create the outbound deliveries.

|  |
| --- |
| Note To execute this process, you must select Distribution Profile as R01 in [Maintain Retail Site Parameters](#unique_10) [page ] 10 for distribution center 3350.If the distribution profile for distribution center is changed in step - [Maintain Retail Site Parameters](#unique_10) [page ] 10, you have to execute whole process again starting with the step - [Create Stock Transfer Order](#unique_13) [page ] 13. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Allocator (Retail) |  |  |
| 2 | Access the App | Open Monitor Merchandise Distribution (WF30) app. | The Merchandise Distribution: Monitor screen is displayed |  |
| 3 | Enter the details | Enter the below details and Choose Execute.Under Parameter section,Distribution Center: 3350Under Supplier Purchase Orders:Purchase Order Number: <Mention the purchase order created in [Create Collective Purchase Order](#unique_25) [page ] 42> | The Merchandise Distribution: Monitor screen is displayed with the list of collective purchase order and corresponding stock transfer orders. |  |
| 4 | Validate Adjustment | Check the status of the Procurement Status for Collective Purchase Order. | Procurement status for collective purchase order must be Green. |  |
| 5 | Validate the General Status of Distribution | Check the Status of Distribution for stock transfer order number. | General status of distribution for stock transfer order must be Green as deliveries are auto-created. |  |
| 6 | Validate Outbound Delivery | Choose stock transfer order numberNote If there are multiple stock transfer orders involved, please repeat the steps to note down all the outbound deliveries created.Make a note of delivery number. | Purchase Order History tab in the stock transfer order will have an entry created for outbound delivery. |  |

#### Perform Picking and Post Goods Issue for Outbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Use this process step to pick and post goods issue for outbound delivery created previously.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Shipping Specialist. |  |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N) app. | Change Outbound Delivery (VL02N) screen is displayed. |  |
| 3 | Enter Parameters | Enter the Outbound Delivery :<Provide Outbound Delivery number>Choose Continue. | RST Outbound Dlv. xxxxxx Change: Overview screen is displayed. |  |
| 4 | Enter the Picked Quantity | Go to Picking tab:In the All Items section,Enter the Picked Qty equal to Delivery QtyPicked Qty: <equal to Deliv.Qty>Choose Enter. | OvrllPickStatus is displayed as C (Fully Picked). |  |
| 5 | Post Goods Issue | Choose Post Goods Issue. | Message is displayed as Replenishment Dlv.xxxxxxxx saved, material document xxxxxxxxxx created. |  |

#### Receive Product in Store

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Use this process step to perform the goods receipt against the outbound delivery as a store associate, created in previous steps for the Stock Transfer Order (STO) created in preliminary steps.

|  |
| --- |
| Note To perform this step, validate the assigned store and assign the desire store as specified in the step [Assign Store Associate (User) to a Store](#unique_14) [page ] 14. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Retail Store Associate |  |  |
| 2 | Access the App | Open Receive Products (F1248) app. | The Receive Products screen is displayed. |  |
| 3 | Open Document | Select EnterID.Outbound Delivery: <created in previous step>and select OK to open it. | The details of the delivery are displayed |  |
| 4 | Post the goods receipt | Verify the quantity and Choose Post displaying on the bottom right corner of the screen. | A popup with message Document items will be posted in the background displayed and Status changes to Completed.This Step will post goods receipt in the store. |  |

|  |
| --- |
| Note Since there are multiple stock transport orders created for different stores like 3341 and 3342 once the stock is received in the assigned store you need to change the assigment in [Assign Store Associate (User) to a Store](#unique_14) [page ] 14 and repeat the above step to receive the product for each store. |

### Merchandise Distribution using Put Away Process

Purpose

This test procedure describes how to keep a put away quantity from the collective purchase order into the distribution center storage location without distributing for the stores.

|  |
| --- |
| Note Prerequisite for a collective purchase order creation is to have stock transfer orders are created (in preliminary step [Create Stock Transfer Order](#unique_13) [page ] 13) for the multiple stores (for example: 3340, 3341 etc) from a particular distribution center (for example: 3350). |

#### Create Collective Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can create collective purchase order either manually or by scheduling an application job.

In order to satisfy all of the demands made by the stores in the form of Stock Transfer Orders (STOs), a single collective purchase order will be created for each supplier under the collective purchase order. As soon as stock arrives at the distribution center, it goes through a distribution process because issue documents in the form of stock transfer orders have already been created against these collective purchase order.

|  |
| --- |
| Note If collective purchase orders are already created for a particular distribution center using Option 1 then to execute Option 2 STOs need to be re-created in the step [Create Stock Transfer Order](#unique_13) [page ] 13. |

Procedure

Option 1: Create Collective Purchase Order Manually

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Allocator (Retail). |  |  |
| 2 | Access the SAP Fiori App | Open Create Collective Purchase Orders (WF10) app. | The Create Collective Purchase Order: Selection and Control Parameters (WF10) screen is displayed. |  |
| 3 | Enter the Selection Parameters | Enter the following data and then choose Execute:Under Organizational data:Distribution Center: 3350Purchasing Organization: 3310Under Scheduling:Procurement period – date: <From date> and <To date>Schedule - line interval: <no.of days> for example 1Note Kindly ensure that the delivery dates of the STOs created in preliminary steps must fall with in the date range of the procurement period-date provided in the selection screen. | The Worklist screen is displayed.Note In case if there are no STOs available that satisfies above selection criteria then a message popup will appear as No documents selected. |  |
| 4 | Validate Processing Method | Verify the processing method for each material. | Processing Method 3 will be displayed for flow through articles. |  |
| 5 | Validate Stock Transport Order | Select each line-item material to see the applicable STO number. | STO number will be listed under Issue Document number. You can also navigate to the STO number to see the details. |  |
| 6 | Choose Worklist | Select the entry displayed under Worklist for ordered merchandise and then choose Worklist. | Document number gets updated in the entry and the below message is displayed.1 collective purchase orders were generated. Check application log generated. |  |

Option 2: Schedule a Job for Generating Collective Purchase Order

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Allocator (Retail). |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Collective Purchase Order Generation (F7821) app. | The Schedule Collective Purchase Order Creation screen is displayed. |  |
| 3 | Provide input values | On the initial screen choose CreateJob Template: Create collective purchase order schedulerJob Name: Create collective purchase order schedulerSelect Step 2Select Step 3Select Parameters for selection criteria:Under Organizational data:Distribution Center: 3350Purchasing Organization: 3310Under Scheduling:Procurement period – date: <From date> and <To date>Schedule - line interval: for example 1 <no.of days>Note Kindly ensure that the delivery dates of the STOs created in preliminary steps must fall with in the date range of the procurement period-date provided in the selection screen. | The Worklist screen is displayed.Note In case if there are no STOs available that satisfies above selection criteria then a message popup will appear as No documents selected. |  |
| 4 | Check Job Parameters | Select Check for validating. | A message is displayed as You can go ahead and schedule the job. |  |
| 5 | Schedule job | Choose Schedule | Job Create collective purchase order scheduler has been scheduled message is displayed. |  |
| 6 | Check Job Results | On the Application Jobs screen, after job item status turned to finished, Choose Navigate to job results in the Results column.Note down the CPO number created. | Document (ID XXXXXXX) screen is displayed with job results. |  |

#### Update Quantity in Collective Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Use this process step to update the quantity in collective purchase order which already exist.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Purchaser (Retail). |  |  |
| 2 | Access the App | Open Change Purchase Order - Advanced (ME22N) app. |  |  |
| 3 | Access Collective Purchase Order | Choose Other Purchase Order, enter below details in Selected Document popup window. Choose Other Document.Purchase. Order: <Enter Doc number noted in previous process>. | Document details are displayed |  |
| 4 | Update the quantity | Increase the quantity and verify storage location and delivery date in the document. | Additional quantity is added to the collective purchase order. |  |
| 5 | Select Save | Choose Save to save the changes. | Changes are saved. |  |

#### Create Inbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Use this step to create an inbound delivery against Collective Purchase Order (CPO) created in previous step - [Create Collective Purchase Order](#unique_25) [page ] 42.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Receiving Specialist. |  |  |
| 2 | Access the App | Open app. | The screen is displayed. |  |
| 3 | Enter the details | Enter all the details as mentioned below:Purchase Order number : XXXXXXXX (Please refer to PO which is created in above step - [Create Collective Purchase Order](#unique_25) [page ] 42)Supplier: for example, 33213001Delivery date: <DD.MM.YYYY>. | Key values option list is visible. |  |
| 4 | Select Continue | Select Continue. | Detail screen is displayed. |  |
| 5 | Enter the quantity | Enter the Putaway Quantity for each product equal to the Delivery Quantity. |  |  |
| 6 | Select save document. | Select Save.Make a note of inbound delivery number. | A message indicating inbound delivery saved is displayed. |  |

#### Post Goods Receipt for Inbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Use this step to post the good receipt for the inbound delivery created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Warehouse Clerk |  |  |
| 2 | Access the app | Open Post Goods Movement (MIGO) app. | The Goods Receipt screen is displayed. |  |
| 3 | Enter Inbound Delivery Number | Provide the values for the following entries:Select Goods Receipt and Inbound Delivery from the dropdown and enter the following:Inbound Delivery Number: XXXGoods Movement Type: 101Select ENTER. | The data with in the selected inbound delivery like article, quantities are displayed. |  |
| 4 | Check and Post the Goods Receipt for Inbound Delivery | Scroll to the bottom of the Goods Receipt Inbound Delivery xxxxxxxxxx screen, select the Item OK checkbox to check. Select Check on the bottom right of the screen.Select Post. | The goods receipt is posted.Message Material Document <Document number> posted. is displayed. |  |

#### Monitor Merchandise Distribution Manually

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Use this step to do manual adjustments and generate the outbound deliveries, hence this will allow all the functions with the user interaction for merchandise distribution.

|  |
| --- |
| Note To execute this process, you must select Distribution Profile as R02 in [Maintain Retail Site Parameters](#unique_10) [page ] 10 for the DC 3350.If the distribution Profile for DC is altered in step - [Maintain Retail Site Parameters](#unique_10) [page ] 10, you must execute whole process again starting with the creation of Stock Transport Order. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Allocator (Retail) |  |  |
| 2 | Access the App | Open Monitor Merchandise Distribution (WF30) app. | The Merchandise Distribution: Monitor screen is displayed |  |
| 3 | Display Options | Under display options, you will have below two options:As List (selected by default)As Table | If As List view is choosen, you can expand and see STO numbersIf As Table view option is choosen than CPO and STO will appear in tabular format. |  |
| 3 | Enter the details | Enter the below details and choose Execute.Under Parameter section,Distribution Center: 3350Under Supplier Purchase Orders:Purchase Order Number: <Enter the Collective Purchase Order number created in [Create Collective Purchase Order](#unique_25) [page ] 42> | The Merchandise Distribution: Monitor screen is displayed with the list of collective purchase orders and corresponding STOs. |  |
| 4 | Choose Adjust | Select Collective PO Document and Choose Adjust displaying on the bottom right corner of the screenNote In case of multiple entries, repeat the steps for each entry. | The Adjust Distribution screen is displayed with STO document details |  |
| 5 | Adjust the Quantity | Adjust the quantity in the below fields:Flow-Through Quantity (FT Qty) or Cross-Docking Quantity (CD Qty): <equal to plan quantity>Putaway Qty: <equal to the increased quantity in step [Update Quantity in Collective Purchase Order](#unique_28) [page ] 44Unit Putaway Quantity: <equal to unit FT Quantity or CD Quantity>Note The system will suggest FT or CD quantity based upon the distribution profile assigned to the material for distribution center.Choose Save | Distribution adjusted. Follow-on documents created in line with settings message is displayed. |  |
| 6 | Validate Adjustment | Navigate back to Merchandise Distribution: Monitor screen.Refresh the screen.Check the status of the Procurement Status for Collective Purchase Order. | Procurement status for collective purchase order must be Green. |  |
| 7 | Create Deliveries | Select the document line items and Edit > Deliveries > Generate FT or Edit > Deliveries > Generate CD .Note Selection of Generate FT or Generate CD depends on the distribution profile assigned to the material for distribution center. | Deliveries were/are being posted message is displayed.Here the outbound delivery will be created only for the FT qty or CD qty. |  |
| 8 | Validate the General Status of Distribution | Refresh the screen.Check the Status of Distribution for STO number. | General status of distribution for STO is not yet completed and hence it will not be Green as deliveries are created only for FT or CD qty. |  |
| 9 | Check Delivery Number | Choose Delivery Log tab. | Delivery number will Display against the STO. Make a note of Delivery number. |  |
| 10 | Mark the Distribution as Completed for Putaway Quantity | Select the line-item for stock transfer order having putaway qty Edit > Merchandise Distribution > Close . | General status of distribution for stock transfer order will now be marked as completed. |  |

#### Transfer Stocks Between Storage Location

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Use this process step to transfer stock from flow-through or cross docking storage location to putaway storage location.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Warehouse Clerk (Retail) |  |  |
| 2 | Access the App | Open Transfer Stock - In-Plant (F1061) app. | The Transfer Stock screen is displayed. |  |
| 3 | Open Stock Overview | Enter the following data in the appropriate fields:Plant: 3350Material: R_5002 or R_5004 or R_5000 |  |  |
| 4 | Select Transfer from Stock | Select the icon beside the unrestricted stock in storage location that you want to transfer from, for example, 995B (Stor. Loc. DC FT) or 995C (Stor. Loc. DC CD). |  |  |
| 5 | Select Transfer to Stock | Select the icon beside the unrestricted stock in storage location that you want to transfer to, for example, 995A (Storage Loc. DC). | A dialog box appears. Storage Locations and Stock Types are selected according to your entries in the previous steps. |  |
| 6 | Transfer Stock | Enter the quantity that you want to transfer:Quantity: <equal to putaway quantity mentioned in [Monitor Merchandise Distribution Manually](#unique_30) [page ] 47 PCChoose POST | The system displays a message Material document xxx created.The stock is transferred from flow through or cross docking storage location to putaway storage location 995A. |  |

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
- related-to :: [[15-retail-operations/test-script-merchandise-allocation-5fl-ae-sap-s-4hana-cloud-public-edi]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/71O_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 92,352 chars in the whole document
