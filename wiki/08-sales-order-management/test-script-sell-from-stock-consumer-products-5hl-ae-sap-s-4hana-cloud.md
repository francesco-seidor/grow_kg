---
id: 08-sales-order-management/test-script-sell-from-stock-consumer-products-5hl-ae-sap-s-4hana-cloud
title: "Test Script: Sell from Stock – Consumer Products (5HL_AE), SAP S/4HANA Cloud Public Edition (5HL_S4CLD2608_BPD_EN_AE)"
description: "SAP test script for scope item 5HL_AE: sell from stock and from valuated stock in transit, order to invoice list, with roles, apps, test data and postings."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/sell-from-stock, topic/end-to-end-produce-and-sell]
aliases: [5HL_S4CLD2608_BPD_EN_AE]
keywords: [Sell from Stock Order-to-Cash, sell from stock, valuated stock in transit, sales order creation, outbound delivery, picking, goods issue, proof of delivery, billing documents, invoice lists]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5HL_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1097
topic: 08-sales-order-management/sell-from-stock
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Sell from Stock – Consumer Products (5HL_AE), SAP S/4HANA Cloud Public Edition (5HL_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5HL_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Sell from Stock Order-to-Cash** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Sell from Stock – Consumer Products (5HL_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232856550)

[2 Prerequisites 4](#_Toc232856551)

[2.1 System Access 4](#_Toc232856552)

[2.2 Roles 4](#_Toc232856553)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232856554)

[2.4 Additional Manual Configuration 7](#_Toc232856555)

[2.5 SSCUI 7](#_Toc232856556)

[2.5.1 Assign Customer Hierarchy Relevance to Sales Document Types – ID “105807” 7](#_Toc232856557)

[2.6 Business Conditions 9](#_Toc232856558)

[2.7 Preliminary Steps 10](#_Toc232856559)

[2.7.1 Set Initial Stock for Material 10](#_Toc232856560)

[2.7.2 Maintain Product Hierarchy to Distribution Chain (Optional) 12](#_Toc232856561)

[2.7.3 Create Customer Hierarchy 13](#_Toc232856562)

[2.7.4 Create Condition Records (Optional) 15](#_Toc232856563)

[2.7.5 Set a Credit Limit (Optional) 17](#_Toc232856564)

[2.7.6 Set Relevance for Sell from Stock with VSiT 18](#_Toc232856565)

[3 Overview Table 20](#_Toc232856566)

[4 Test Procedures 23](#_Toc232856567)

[4.1 Sell from Stock 23](#_Toc232856568)

[4.1.1 Create Sales Order 23](#_Toc232856569)

[4.1.2 Review and Release or Reject a Sales Order (Optional) 26](#_Toc232856570)

[4.1.2.1 Review Sales Order (Optional) 26](#_Toc232856571)

[4.1.2.2 Release Sales Order (Optional) 27](#_Toc232856572)

[4.1.2.3 Reject Sales Order (Optional) 28](#_Toc232856573)

[4.1.3 Advanced Available-to-Promise Processing (Optional) 29](#_Toc232856574)

[4.1.4 Create Delivery 30](#_Toc232856575)

[4.1.5 Execute Picking 32](#_Toc232856576)

[4.1.6 Check Batches (Optional) 33](#_Toc232856577)

[4.1.7 Post Goods Issue 34](#_Toc232856578)

[4.1.8 Confirm Proof of Delivery 35](#_Toc232856579)

[4.1.9 Create Billing Document 36](#_Toc232856580)

[4.1.10 Send Invoice - EDI Relevant 38](#_Toc232856581)

[4.1.11 Check Invoice in AIF (Message Dashboard) - EDI relevant 39](#_Toc232856582)

[4.1.12 Create Invoice List 39](#_Toc232856583)

[4.2 Sell from Valuated Stock in Transit 41](#_Toc232856584)

[4.2.1 Create Sales Order 42](#_Toc232856585)

[4.2.2 Create Delivery 44](#_Toc232856586)

[4.2.3 Execute Picking 46](#_Toc232856587)

[4.2.4 Check Batches (Optional) 47](#_Toc232856588)

[4.2.5 Post Goods Issue 48](#_Toc232856589)

[4.2.6 Confirm Proof of Delivery 50](#_Toc232856590)

[4.2.7 Create Billing Document 51](#_Toc232856591)

[5 Appendix 53](#_Toc232856592)

[5.1 Succeeding Processes 53](#_Toc232856593)

[5.2 Scheduling Job (alternative) 53](#_Toc232856594)

[5.2.1 Job Scheduling for Delivery Creation (Alternative) 53](#_Toc232856595)

[5.2.2 Job Scheduling for Goods Issue Deliveries (Alternative) 54](#_Toc232856596)

[5.2.3 Job Scheduling for Billing Creation (Alternative) 55](#_Toc232856597)

[5.2.4 Job Scheduling for Billing Output (Alternative) 57](#_Toc232856598)

## Purpose

Overview

The process described in this scope item is a sales process for Consumer Products industry flavored products with seamless integration to the production process described in the Quality Management in Discrete Manufacturing – Consumer Products (5HK) scope item.

The process starts with creating customer standard sales orders. A pricing condition may become relevant via the customer hierarchy. When the inventory is decided, the shipping specialist releases the inventory. The inventory is shipped to the customer, and the actual recording of the physical quantity is recorded.

When the goods issue is posted, cost of goods sold is recorded in Financial Accounting.

Once goods are delivered and the proof of delivery (POD) is confirmed by the ship-to-party, you can invoice the delivery. When the invoices are created, an invoice list is created for the central payer for both customers. An EDI invoice message is sent to the buyer when the billing document is saved.

In addition, this scope item allows you to use valuated stock in transit (VSIT) as described in Sell from Stock with Valuated Stock in Transit (5MQ). After the goods issue is posted to an outbound delivery, the stock is transferred into VSIT. With the transfer of control of the delivered goods to the customer (for example, based on incoterms and transportation management), the goods issue from VSIT to the customer is posted. At this point in time, revenue and COGS can be recognized.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

| System | Details |
| --- | --- |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |
| Pricing Specialist | SAP_BR_PRICING_SPECIALIST | Pricing Specialist | SAP_BR_PRICING_SPECIALIST |  |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |
| Credit Controller | SAP_BR_CREDIT_CONTROLLER | Credit Management | SAP_BR_CREDIT_CONTROLLER |  |
| Configuration Expert - Business Network Integration | SAP_BR_CONF_EXPERT_BUS_NET_INT | Business Network Integration / Business Network Integration - Concur Integration / Business Network Integration - Output Control / Business Network Integration - Data Replication / Configuration Expert - Business Network Integration Cross Applications | SAP_CORE_SPT_INT_PC / SAP_CON_SPT_CONCUR_INT_PC / SAP_OC_SPT_INT_PC / SAP_CA_SPT_DATA_REP_PC / SAP_CA_SPT_BUS_NETWORK_INT_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

This scope item requires new master data set to be created and the needed master data objects are mentioned below:

Material Master Data:

Material Masters mentioned in this document are to be created for plant 3310.

| Data | Value | Description | Other Attributes |
| --- | --- | --- | --- |
| Material | FG0502 | Display Med + Dark 48 * 1kg Arabica | Batch administrated, best before date, Sales BOM |
| Material | FG0511 | Carton 12 x 1kg Bags Medium Beans Arabica | Batch administrated, best before date |
| Material | FG0512 | Carton 12 x 1kg Bags Dark Beans Arabica | Batch administrated, best before date |
| Material | TG0501 | Thermo Coffee Cup 0,4l | No serial number, no batch |

Organization Data:

| Data | Sample Value | Description | Other Attributes |
| --- | --- | --- | --- |
| Company Code | 3310 | Company Code 3310 |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Controlling Area | A000 | Controlling Area A000 |  |
| Shipping Point | 3310 | Shipping Point 3310 |  |
| Sales Organization | 3310 | Dom. Sales Org |  |
| Distribution Channel | 10 | Direct Sales |  |
| Division | 00 | Product Division 00 |  |

Customer:

Below mentioned Customers (Business Partners) will be used in this scenario.

| Master data | Value | Master. data details | Comments |
| --- | --- | --- | --- |
| Sold-to Party | 33105001 | Domestic CP Customer 01 | This Business Partner is setup for the VSiT Process (Incoterm DAP) |
| Ship-to Party | 33105001 | Domestic CP Customer 01 | This Business Partner is setup for the VSiT Process (Incoterm DAP) |
| Payer | 33105010 | Domestic CP Payer Customer 10 |  |
| Sold-to Party | 33105002 | Domestic CP Customer 02 |  |
| Ship-to Party | 33105002 | Domestic CP Customer 02 |  |
| Payer | 33105010 | Domestic CP Payer Customer 10 |  |
| Sold-to Party | 33105005 | Domestic CP Customer 05 |  |
| Ship-to Party | 33105005 | Domestic CP Customer 05 |  |
| Payer | 33105005 | Domestic CP Payer Customer 05 |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BET | Create Sales Pricing Condition - MDS |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BNT | Create Product Master of type "Finished Good" - MDS |
| BND | Create Customer Master - MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/3cefe84fe9e6785643e958a1cea37b89)

### SSCUI

#### Assign Customer Hierarchy Relevance to Sales Document Types – ID “105807”

Customer hierarchy needs to be updated for analytics purpose. For this a sales document type needs to be assigned to the “customer hierarchy relevance".

Purpose

In this activity, you assign Customer Hierarchy Relevance to Sales Document Types.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241) | The Manage Your Solution screen displays. |  |
| 3 | Configure your Solution | Choose Configure Your Solution | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Filter Selection Criteria | Choose the following entries in filter bar and press Enter:Application Area: SalesSub Application Area: Sales Master Data Management | All entries display in All Items section. |  |
| 5 | Select Entry | Find the entry with item name Business Partner and choose arrow at the item end. | Configure Your Solution – Business Partner screen displays. |  |
| 6 | Select Configuration | In Configuration Steps section, choose Configure in column Actions for step Assign Customer Hierarchy Relevance to Sales Document Types (ID 105807) | Change View “Assign Customer Hierarchy Relevance to Sales Document Types”: Change screen displays. |  |
| 7 | Maintain Customer Hierarchy Relevance | Update Entries, enter the following data and choose Save.SaTy: For example: ORCustomer Hierarchy Relevance: 01 Basic Hierarchy Determination | Customer Hierarchy Relevance is updated. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  | Perform the following steps to update Customer Hierarchy Relevance to Sales Document Types. |
| 2 | Open Assign Customer Hierarchy Relevance to Sales Document Types | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign Customer Hierarchy Relevance to Sales Document Types.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Display View Assign Customer Hierarchy Relevance to Sales Document Types screen displays. |  |
| 3 | Open Maintain Customer Hierarchy Relevance | Update Entries, make the following data and choose Save.SaTy:For example: ORCustomer Hierarchy Relevance: 01 Basic Hierarchy Determination | Customer Hierarchy Relevance is updated. |  |

### Business Conditions

The business process described in this test script is part of a bigger chain of integrated business processes or scope items. As a consequence, you must have completed the following processes and fulfilled the following business conditions before you can go through this scope item:

| Scope Item | Business Condition |
| --- | --- |
| J45 - Procurement of Direct Materials | To run through this scope item, the materials must be available in stock. If you use trading goods (HAWA) you can either:Run through the Procurement of Direct Materials (J45) test script process.Or create stock using Post Goods Movement (MIGO) app (refer to Preliminary Steps section for details). |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS (BNZ) master data script. Posting Period is up to date. |
| 5HK - Quality Management in Discrete Manufacturing – Consumer Products | You have produced FG0502, FG0511, FG0512 in sufficient quantities and released them from quality inspection. |
| 5MQ - Sell from Stock with Valuated Stock in Transit | You have completed the additional Manual Configuration from 5MQ |

Activate Features

In a software update, SAP delivers certain features that could have an impact on your implemented solution initially in an inactive state. You can choose to already activate these features before they become available by default in a later release.

The test procedures in this document describe the software behavior when all features have been activated. It is a prerequisite for testing that you have activated all of the following features in each of your systems using the configuration activity Activate Features. For more information about this activity, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/3e94fcc37b42433b97d6aef0c830dc52.html) for SAP S/4HANA Cloud Public Edition.

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

- Configure Your Solution:

Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).

Navigate to Manage your Solution > Configure Your Solution. Search for Activate Features. In the search result, select the configuration activity and go to the next screen. Select the configuration step and choose Configure.

- SAP Central Business Configuration:

Log on to the project experience in SAP Central Business Configuration.

Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Activate Features. Choose the link to navigate directly to the target system of SAP S/4HANA Cloud Public Edition. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).

| Feature ID | Feature Title |
| --- | --- |
| FIN_FSCM_REBUILD_DCD | Rebuild DCD functionality |

### Preliminary Steps

#### Set Initial Stock for Material

Purpose

This process step shows you how to set initial stock to execute this scope item.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Goods Receipt Other screen displays.Note It only displays this way if it was your last transaction. So, the action for the user should be to select Reference Document for MIGO Transaction > Other. |  |
| 3 | Enter Movement Type | Make the following entry and choose Enter.Executable Action in Transaction MIGO: Goods ReceiptReference Document for MIGO Transaction: Other |  |  |
| 4 | Edit Material | On the Goods Receipt Other Screen: Material tab, make the following entry, and choose Enter:Material : FG0502 |  |  |
| 5 | Edit Quantity Data | On the Goods Receipt Other Screen: Quantity tab, make the following entry, and choose Enter:Qty in Unit of Entry: 1000Unit of Entry: <PC> |  |  |
| 6 | Enter the Goods Receipt Other Screen: Where Tab | On the Goods Receipt Other Screen: Where tab, make the following entries and choose Enter:Movement Type: 561 (Receipt per initial entry of stock balances into unrestricted use)Plant: 3310Storage Location: 331A |  |  |
| 7 | Enter the Goods Receipt Other Screen: Batch Tab | On the Goods Receipt Other Screen: Batch tab, make the following entry and choose Enter:Date of Manufacture: <Enter the Current Date or a Date in the Past> | Only relevant for batch relevant materials. |  |
| 8 | Save Your Entries | Choose Post. |  |  |
| 9 | Repeat all steps from above | Use Material: FG0512, FG0511, TG0501 |  |  |

Financial Postings:

| Material | Debited Accounts | Credited Accounts |
| --- | --- | --- |
| Trading Good (HAWA) | 13600000Inventory TradingGd | 39912000Inv Init SF&Fin Bal |
| Finished Goods (FERT) | 13400000Inventory FinishedGd | 39912000Inv Init SF&Fin Bal |

#### Maintain Product Hierarchy to Distribution Chain (Optional)

Purpose

This process helps you to maintain Product Hierarchy to Distribution Chain if you are using Product Hierarchy relevant materials.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Internal Sales Representative. |  |  |
| 2 | Access the App | Open Manage Product Hierarchy Assignments (F4240). | The Manage Product Hierarchy Assignments (F4240) screen displays. |  |
| 3 | Create New Object | Choose Create. | The Create Product Hierachy Assignment Screen displays. |  |
| 4 | Enter General Information | On the Create Product Hierachy Assignment screen, in the General Information tab, make the following entries:Purpose: 02 SalesSales Organization: 3310Distribution Channel: 10Valid From: <For example, Current Date>Valid To: <For example, Current Date + 1 Year>Note If there exists an active product hierarchy assignment, then proceed to the next step.And if necessary, the user may change the valid dates.Product Hierachy: HOTDRINKS |  |  |
| 5 | Save the Entry | Choose Create. |  |  |

#### Create Customer Hierarchy

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a customer hierarchy for the existing customers. The customers in this script will belong to the same hierarchy.

|  |
| --- |
| Note In case a customer hierarchy already exists from script 6V0 this step can be skipped. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Customer Hierarchies (F5794) app. | The Manage Customer Hierarchies screen opens. |  |
| 3 | Create new Hierarchy | Choose Create. | The screen to create a new customer hierarchy is displayed. |  |
| 4 | Enter new Hierarchy | Make the following entries:Type: Customer Hierarchy – SalesHierarchy ID: AE05_0001Hierarchy Description: CP Customer CorporationStart Date: <First of current month>Sales Organization: 3310Distribution Channel: 10Division: 00Choose Create. | The Hierarchy List shows the new hierarchy with status Draft. |  |
| 5 | Create Customer Hierarchy Nodes | Click on the details (>) chevron on the right side of the list entry for the newly created customer hierarchy. | The view pane for the Hierarchy AE05_0001 appears on the right side of the screen. |  |
| 6 | Add new Nodes | Choose Edit. | The pane switches to Edit Mode. |  |
| 7 |  | Choose the Fast Entry Icon on the right hand side of the line for the top-node in the Nodes section. | Fast Entry Screen for Nodes appears.. |  |
| 8 | Fast Entry of Nodes | Choose Subnodes and mark them as pricing relevant:ID: RE_WEST_HQ ; Description: Headquarter Region WestID: RE_SOUTH_HQ ; Description: Headquarter Region SouthID: RE_MIDDLE_HQ ; Description: Headquarter Region MiddleChoose OK. | The subnodes are created. |  |
| 9 | Enter the next level nodes | On the line for RE_WEST_HQ choose the Add Icon to create a single subnode. | The screen to create a single subnode appears. |  |
| 10 |  | Enter the following data:ID:Description:Price Relevant: CheckedChoose OK. | Subnode is created. |  |
| 11 | Enter the next level nodes | On the line for RE_SOUTH_HQ choose the Add Icon to create a single subnode. | The screen to create a single subnode appears. |  |
| 12 |  | Enter the following data:ID:Description:Price Relevant: CheckedChoose OK. | Subnode is created. |  |
| 13 | Enter the next level nodes | On the line for RE_MIDDLE_HQ choose the Add Icon to create a single subnode. | The screen to create a single subnode appears. |  |
| 14 |  | Enter the following data:ID:Description:Price Relevant: CheckedChoose OK. | Subnode is created. |  |
| 15 | Enter business partner nodes | On the line for choose the Add Icon to create a single subnode. | The screen to create a single subnode appears. |  |
| 16 |  | Enter the following data:Business Partner: CheckedID: from the value help select business partner 33105005Choose OK. | Business Partner Subnode is created. |  |
| 17 | Enter business partner nodes | On the line for choose the Add Icon to create a single subnode. | The screen to create a single subnode appears. |  |
| 18 |  | Enter the following data:Business Partner: CheckedID: from the value help select business partner 33105001Choose OK. | Business Partner Subnode is created. |  |
| 19 | Enter business partner nodes | On the line for choose the Add Icon to create a single subnode. | The screen to create a single subnode appears. |  |
| 20 |  | Enter the following data:Business Partner: CheckedID: from the value help select business partner 33105002Choose OK. | Business Partner Subnode is created. |  |
| 21 | Save your data | Choose Save. | The hierarchy is saved with status Draft. |  |
| 22 | Activate the Hierarchy | Choose Activate. | The hierarchy status changes from Draft to Active. |  |

#### Create Condition Records (Optional)

Purpose

In case you have finetuned the access sequence of SAP pre-shipped condition types, the relative condition records should be created accordingly.

You can find general information on how to create your own master data in the following: [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 2: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BEW | Create Free Goods Condition - MDS |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Pricing Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Prices - Sales (F4111) app. | The Manage Prices – Sales screen is displayed. |  |
| 3 | Enter Condition Type | Make the following entries and Enter:ConditionType: <Customer Hierarchy>Key Combination: Choose <4BN DCH1 010> from the help list.Sales Organization: 3310Distribution Channel: 10Choose Go. | The list of existing condition records is displayed. If there are no conditions created yet, the list will be empty. |  |
| 4 | Create new condition record | Choose Create. | An entry line on top of the list appears, condition table, Sales Organization, Distribution Channel are pre-filled from the entered filter values. |  |
| 5 |  | Make the following entries:Sales Organization: 3310Distribution Channel: 10Customer Hierarchy Root Node ID: AE05_0001Customer Hierarchy Node ID: RE_SOUTH_HQValid From: enter todays dateCondition Amount or Ratio: <-7,500>Choose Save.Valid To: leave default value | The condition record is created. |  |

#### Set a Credit Limit (Optional)

Purpose

In this activity, you set a credit limit for the customer. The credit limit currency in all company codes is set to use the group currency, which is defined when the solution is activated.

|  |
| --- |
| Note The credit limit currency in all company codes is set to use the group currency that is defined when the solution is activated. |

|  |
| --- |
| Note If you use the Create Credit Segment configuration step, if you want to set the Credit Segment 1000 in the FLEXIBLE_CHECK field to a value of 3 on the Main Segment and Segment levels, you must also enter a credit limit for Credit Segment 0000. |

Prerequisite

Business partner master record 33105005 is already created with credit management profile.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Credit Controller. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Credit Accounts (F4596). | The Manage Credit Accounts (F4596) view is displayed. |  |
| 3 | Select Customer | Make the following entries and choose Go:Business Partner: 33105005For the row in the Worklist, choose Details (>). |  |  |
| 4 | Maintain Credit Profile | Choose the Scoring tab.Choose Edit.Make the following entries:Calculation Rule: Standard rule without Automatic calculationRisk Class: Medium Default RiskCredit Check Rule: 01 Default - All Checks Active |  |  |
| 5 | Maintain Credit Segment | Choose the Credit Segments tab. Review or enter the following values in the Credit Segment field:Credit Segment: 1000 Credit Segment 1000 (Maintained)Credit Limit: 5.00Go to the Credit Segment line and make the following entry and choose Apply:Limit Valid To: <End of Year>Note If the Valid To field is not visible, you can go into View Settings and select it to display it.Note Repeat this step to set a credit limit on Credit Segment 0000 to avoid the sales order being blocked at headquarter credit check. | The amount and validity date are set for the credit limit. |  |
| 6 | Save | Save your entries. | Changes have been saved. |  |

#### Set Relevance for Sell from Stock with VSiT

Purpose

You need to set relevance for item category, sales org, plant and incoterm with VSiT.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Set Version | Choose Set Local Version in the end of the screen.In the pop-up window, choose Local Country Version and Set Local Version. |  |  |
| 4 | Configure Your Solution | Choose Configure Your Solution. |  |  |
| 5 | Choose SSCUI | On the Configure Your Solution: Realize Phase screen, search for SSCUI named Set Relevance for Sell-from-Stock with VSiT Process (105504) under Sales Application Area. |  |  |
| 6 | Access SSCUI | Click the line of the SSCUI, and choose Configure. |  |  |
| 7 | Set Relevance for Sell-from-Stock with VSiT | On the Change View "Set Relevance for Sell from Stock with VSiT": Overview screen, choose New Entries and make the following entries:Item Category: TANSOrg: 3310Plant: 3310Incoterm: DAPRelevance for SFS VSiT Process: Relevant for SFS VSiT ProcessChoose Save. | The relevant entries have been set for SFS VSiT Process. |  |

## Overview Table

The scope item Sell from Stock – Consumer Products consists of several steps choose the appropriate entity: process steps, reports and items provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Sell from Stock

Overview of the process for Sales Order Processing with Invoice Lists:

| Sales Order | Delivery | Invoice (Billing Document) | Invoice List |
| --- | --- | --- | --- |
| Order 1 from Customer 33105001 with Material 1 | Delivery 1 to customer 33105001 | Invoice 1 to customer 33105001 | Invoice List 1 to payer 33105010 |
| Order 2 from Customer 33105002 with Material 1 | Delivery 2 to customer 33105002 | Invoice 2 to customer 33105002 | Invoice List 1 to payer 33105010 |
| Order 3 from Customer 33105005 with Material 1 | Delivery 3 to customer 33105005 | Invoice 3 to customer 33105005 | No invoice list for this customer |

Payer 33105010 is responsible to pay all invoices for goods that are shipped to customers 33105001, 33105002. After sales order, delivery and invoice are created, invoice list including all invoices with same payer is generated, certain factoring discount and discount tax are calculated and posted to accounting.

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Sales Order](#unique_16) [page ] 23 | Internal Sales Representative | Manage Sales Orders (F1873) | Sales order is created. |
| [Review and Release or Reject a Sales Order (Optional)](#unique_17) [page ] 26 |  |  |  |
| [Review Sales Order (Optional)](#unique_18) [page ] 26 | Credit Controller | Manage Documented Credit Decision - New Version (F5587A) | The blocked sales order is reviewed. |
| [Release Sales Order (Optional)](#unique_19) [page ] 27 | Credit Controller | Manage Documented Credit Decision - New Version (F5587A) | The Sales order is released. |
| [Reject Sales Order (Optional)](#unique_20) [page ] 28 | Credit Controller | Manage Documented Credit Decision - New Version (F5587A) | The Sales order is rejected. |
| [Advanced Available-to-Promise Processing (Optional)](#unique_21) [page ] 29 |  |  |  |
| [Create Delivery](#unique_22) [page ] 30 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) | Outbound delivery is created. |
| [Execute Picking](#unique_23) [page ] 32 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) |  |
| [Check Batches (Optional)](#unique_24) [page ] 33 | Shipping Specialist | Change Outbound Delivery (VL02N) | Batch updated for outbound delivery. |
| [Post Goods Issue](#unique_25) [page ] 34 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Goods Issue is posted. |
| [Confirm Proof of Delivery (POD)](#unique_26) | Shipping Specialist | Deliveries Worklist - Proof of Delivery (VLPODL) | POD is confirmed. |
| [Create Billing Document](#unique_27) [page ] 36 | Billing Clerk | Create Billing Documents (F0798) | Invoice is created for billing document - Invoice is created and sent from the SAP S/4HANA system (supplier side) to the Buyer system. |
| [Send Invoice - EDI Relevant](#unique_28) [page ] 38 |  |  | Supplier Invoice is automatically sent to the Buyer system. |
| [Check Invoice in AIF (Message Dashboard) - EDI relevant](#unique_29) [page ] 39 | Configuration Expert - Business Network Integration | Message Dashboard - SAP Application Interface Framework (/AIFX/WDA0005) | The message (invoice) is checked in dashboard. |
| [Create Invoice List](#unique_30) [page ] 39 | Billing Clerk | Manage Invoice Lists (F2740) | Invoice list document number created. |

Sell from Valuated Stock in Transit

Overview of the process for Sales Order Processing with Invoice Lists:

| Sales Order | Delivery | Invoice (Billing Document) | Invoice List |
| --- | --- | --- | --- |
| Order 1 from Customer 33105001 with Material 1 | Delivery 1 to customer 33105001 | Invoice 1 to customer 33105001 | Invoice List 1 to payer 33105010 |

Payer 33105010 is responsible to pay all invoices for goods that are shipped to customers 33105001, 33105002. After sales order, delivery and invoice are created, invoice list including all invoices with same payer is generated, certain factoring discount and discount tax are calculated and posted to accounting.

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Sales Order](#unique_31) [page ] 42 | Internal Sales Representative | Manage Sales Orders (F1873) | Sales order is created. |
| [Create Delivery](#unique_32) [page ] 44 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) | Outbound delivery is created. |
| [Execute Picking](#unique_33) [page ] 46 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) |  |
| [Check Batches (Optional)](#unique_34) [page ] 47 | Shipping Specialist | Change Outbound Delivery (VL02N) | Batch updated for outbound delivery. |
| [Post Goods Issue](#unique_35) [page ] 48 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Goods Issue is posted. |
| [Confirm Proof of Delivery (POD)](#unique_36) | Shipping Specialist | Deliveries Worklist - Proof of Delivery (VLPODL) | POD is confirmed. |
| [Create Billing Document](#unique_37) [page ] 51 | Billing Clerk | Create Billing Documents (F0798) | Invoice is created for billing document - Invoice is created and sent from the SAP S/4HANA system (supplier side) to the Buyer system. |

## Test Procedures

This section describes procedures for each process step that belongs to this scope item.

The Enterprise Search function provides a central entry point for finding business objects in your company from different sources using a single search request. You can search for objects such as: apps, fact sheets for business objects. From the data found, you can go directly to the respective apps and fact sheets to display, edit the data or find related objects.

How to access and check a fact sheet:

1. Log on to the SAP Fiori launchpad as a respective user, for example, Internal Sales Representative.
2. Access the Enterprise Search Bar by choosing the magnifying glass icon in the upper right corner.
3. The Enterprise Search bar displays two filter fields next to the search icon: all dropdown menu and a search field. Enter your Search Criteria and choose the business object type, for example, select Sales orders from the dropdown menu, and enter a sales order number in the search field and choose Search, the sales order lists.
4. Choose the sales order number link. The system navigates to the fact sheet screen and sales order related information is integrated and summarized in one Fiori page. You can get detailed data by choosing the corresponding links.

There are fact sheets available for the following objects (visible depending on the assigned role):

- Sales order
- Quotation
- Billing document
- Credit Memo
- Debit Memo
- Customer 360 Fact sheet

### Sell from Stock

#### Create Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create three sales orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Create Sales Order | On the Manage Sales Orders screen, choose Create, then select Create Sales Order-VA01. |  |  |
| 4 | Enter Order Details | On the Create Standard Order: Initial screen, make the following entries and choose Continue:Order Type: ORSales organization: 3310Distribution channel: 10Division: 00 |  |  |
| 5 | Enter Order Details | On the Create Standard Order: Overview screen, make the following entries and choose Continue:Sold-To Party: 33105001Ship-To Party: 33105001Customer Reference: <Reference number> Enter a customer purchase order number as reference.Customer Reference Date: <today>Incoterms: CFRGo to item Overview TabProduct: FG0502Order Quantity: 2Optional: Create additional line item with trading material TG0501.Optional: Add additional main line items with FG0511 or FG0512 if you want to sell these products individually. | Together with the order line for FG0502 there are two sub items for FG0511 and FG0512. The sub items only serve as explanation for the content of the display. |  |
| 6 | Check Customer Hierarchy (optional) | Go to Menu > Goto > Header > Additional Functions > Customer Hierarchy . | The screen with the Customer Hiererchy Root node and its sub nodes relevant for this customer are displayed. |  |
| 7 | Check Pricing (optional) | In the overview screen select the item containing the material you entered and select button Item Conditions. | The condition DCH1 is part of the pricing calculation with the rate you have entered earlier. |  |
| 8 | Save | Choose Save. Make a note of the sales order number:___________. | Sales order with customer 33105001 is created. |  |
| 9 | Create More Sales Orders | Repeat above steps from 1 to 6 to create 1 more sales orders: with Sold-to party 33105002 & 33105005.Make a note of the sales order numbers:___________. | Sales orders are created respectively for customers 33105002 & 33105005. |  |

Printing Form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders - Version 2 (F3893). | The Manage Sales Orders - Version 2 screen displays. |  |
| 3 | Search For Sales Order | Enter search term(s) in filter bar and choose Go, for example, enter sales order number in field Sales Order. | Sales order displays in result list. |  |
| 4 | Navigate to Sales Order Screen | Choose > on the right of the Sales Order item and navigate to Display Standard Orders xxx: Overview screen. | The Display Standard Orders xxx: Overview screen displays. |  |
| 5 | Check Output Condition | On the Display Standard Order xxx: Overview screen, choose Header Output Preview. |  |  |
| 6 | Display Print Preview | On the Display Standard Order xxx: Output screen, select the line already created for the print output and choose Display Document. | Preview for PDF document displays. |  |

|  |
| --- |
| Note It can also be navigated to a factsheet screen in app Manage Sales Orders - Version 2 (F3893):On the Manage Sales Orders (Original) screen, enter search terms in filter bar and choose Go.In search result, choose your Sales Order Number and choose More Links. |

#### Review and Release or Reject a Sales Order (Optional)

Context

The sales order failed the credit check. In the following procedures, you review blocked sales orders and resolve any credit issues.

Prerequisites

Sales orders exceeding the credit limit settings are blocked due to credit check block.

Credit case has been assigned to a Credit Analyst or Person Responsible.

##### Review Sales Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The sales order failed the credit check. In this activity, you review blocked sales orders.

Prerequisites

Sales orders exceeding the credit limit settings are blocked due to a credit check block.

The Documented credit decision has been assigned to a Credit Analyst.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Credit Controller. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Documented Credit Decision - New Version (F5587A). | The Manage Documented Credit Decision (New Version) view is displayed. |  |
| 3 | Select Documented Credit Decision - Search | Make the following entries and choose Go:Business Partner: 33105005Credit Segment: 1000Note Use appropriate filter to get documents. | A list of documented credit decisions is displayed. |  |
| 4 | Select | Select the row of the documented credit decision you generated in the previous step. | The Document with Credit Block view is displayed. |  |
| 5 | Enable Editing | Choose Edit. | Updates data. |  |
| 6 | Update | Update the DCD fields.Credit Analyst: <Your user with HR Master Record created> | The DCD data is changed. |  |
| 7 | Save | Save your entries. | The changes are saved. |  |
| 8 | Set In Process | Choose Set To In Process | Status changed to In Process. |  |

##### Release Sales Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The sales order failed the credit check. In this activity, you release the sales orders.

Prerequisites

Sales orders exceeding the credit limit settings are blocked due to credit check block.

The Documented credit decision has been assigned to a Credit Analyst.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Credit Controller. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Documented Credit Decision - New Version (F5587A). | The Manage Documented Credit Decision (New Version) view displays. |  |
| 3 | Select Documented Credit Decision - Search | Make the following entries and choose Go:Business Partner: <your business partner>Credit Segment: 1000 | A list of documented credit decisions is displayed. |  |
| 4 | Select | Select the row of the documented credit decision you generated in the previous step. |  |  |
| 5 | Release | Choose Release. On the Release dialog box, enter an approval note and choose Release. | The log is displayed and under the Classification and Changes facet, the Last Action is Release. |  |

##### Reject Sales Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The sales order failed the credit check. In this activity, you reject the sales orders.

Prerequisites

Sales orders exceeding the credit limit settings are blocked due to credit check block.

The documented credit decision is assigned to a Credit Analyst.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Credit Controller. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Documented Credit Decision - New Version (F5587A). | The Manage Documented Credit Decision view displays. |  |
| 3 | Select Documented Credit Decision - Search | Make the following entries and choose Go:Business Partner: 33105005Credit Segment: 1000 | A list of documented credit decisions is displayed. |  |
| 4 | Select Case | Select the row of the documented credit decision you generated in the previous step.Choose Details (>). | The Document with Credit Block view displays. |  |
| 5 | Reject | Choose Reject. | The Reject dialog box displays. |  |
| 6 | Select Rejection Reason | Make the following entry and choose Reject:Rejection Reason: for example, Rejected by ApproverRejection Note: <any note> | The sales order/service order/service contract is rejected and the DCD Status changes to Closed and the Notes are updated with the note of type Rejection Reason. |  |

#### Advanced Available-to-Promise Processing (Optional)

Purpose

Follow the procedures in the Basic Available-to-Promise Processing (2LN) and Advanced Available-to-Promise Processing (1JW) scope item. This scope item describes the optional process for Advanced Available-to-Promise Processing.

1. From 2LN, the user can Trigger / Schedule BOP, execute a BOP Run and Monitor BOP Run.
2. From 1JW, the user can execute Release for Delivery.

Procedure

Complete all the activities described in the test script of Advanced Available-to-Promise Processing (1JW) scope item.

#### Create Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create three deliveries from three sales orders created previously.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Create Outbound Deliveries - From Sales Orders (F0869A). | The Create Outbound Deliveries - From Sales Orders (F0869A) screen displays. |  |
| 3 | Search Sales Order | Make the following entries and choose Go:Shipping Point: 3310Planned Creation Date: <Delivery selection date>Order: Sales order number created previously |  |  |
| 4 | Create Delivery | Select your sales orders and choose Create Deliveries. | Deliveries are triggered to create. |  |
| 5 | Check Details | Choose Display Log. | The Analyze Delivery Log screen displays. The failed entries will display in Messages tab. The delivery number will display in the Deliveries tab.Three deliveries are created, for customer 33105001, 33105002 and 33105005. |  |

|  |
| --- |
| Note At delivery creation, the scope item settings for check availability use available inventory and replenishment lead time. Without sufficient stock, the created delivery has no confirmed quantities and does not start the warehouse management picking process. As soon as there is sufficient stock at delivery creation, the system creates a delivery with further picking process in warehouse management. To avoid open deliveries, ensure that there is sufficient inventory quantity at delivery creation. Additionally, you have the following options to restrict the creation of deliveries with no confirmed quantities.- You may increase replenishment lead time that is used during the availability check (must be larger than the selection period used for delivery creation).- You may change the customizing settings for the incompleteness procedure for delivery creation, so that only complete deliveries may be saved.- You may change the customizing settings for the used delivery item category.The Check quantity 0 field must be adapted to B = Situation rejected with an error message. |

|  |
| --- |
| Note With the Analyze Outbound Delivery Logs app you can display an overview about the logs of all the deliveries which have been created in your system. You can filter by, for example, created by and Additional settings. If you select the arrow on the right of each delivery log entry you can display the exact message type and text and also the related sales document. |

Printing form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). | The Change Outbound Delivery (VL02N) screen displays. |  |
| 3 | Issue Delivery Output | On the Change Outbound Delivery (VL02N) screen, enter the delivery number and choose Continue. From the Delivery xxxxxxxx Change: Overview screen, choose Menu > Extras > Delivery Output > Output Control . | The Delivery: Output screen displays. |  |
| 4 | Print Preview | On the Delivery: Output screen, select the line with the Output Type Delivery_Pick_List and choose Display Document. | A preview of the print document displays. |  |
| 5 | Print Delivery Pick List | From the preview of the document, choose Print. | The delivery pick list is printed. |  |

#### Execute Picking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The picking process involves taking goods from a storage location and staging the right quantity in a picking area where the goods are prepared for shipping. This process step shows you how to pick deliveries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Choose Picking | Choose For Picking. |  |  |
| 4 | Enter Shipping Point | Make the following entries, and choose Execute:Shipping Point: 3310Under the Picking Data tab, selectOnly Picking Without WM: X |  |  |
| 5 | Change Outbound Deliveries | Choose your delivery number, and choose Change Outbound Deliveries. |  |  |
| 6 | Check Batch Split | Choose the Picking tab, check if batch split exists in the Batch Split Indicator column. |  |  |
| 7 | Enter Picked Quantity | If batch spilt exists, choose Batch Split Exists to expand sub item(s), enter <quantity equal to Deliv. Qty> in Picked Qty field for sub item.Note Sales BOM sub item materials are not relevant for the logistics process i.e. batch or picking quantity update.If batch split doesn't exist, enter <quantity equal to Deliv. Qty> in Picked Qty field for picking related item(s). |  |  |
| 8 | Choose Enter | Choose Enter. |  |  |
| 9 | Save | Choose Save. | The delivery has been decided. |  |
| 10 | Repeat | Repeat step 4 to 9 for other deliveries (if any). |  |  |

#### Check Batches (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check the batch number assigned to the material.

Prerequisites

Execute this step for batch managed products like FG0512.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). |  |  |
| 3 | Enter Outbound Delivery Number | In the Outbound Delivery field, enter <outbound delivery number>, and choose Continue. |  |  |
| 4 | Check Batch Number Assignment | If Expand Batch Split exists, go to the Batch field, and check the batch number assignment. | Batch numbers are assigned to the materials. |  |
| 5 | Save Document | Choose Save. |  |  |

#### Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post goods issues for delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Open Outbound Delivery Monitor | Choose For Goods Issue. Make the following entries and choose Execute.Shipping Point: 3310 |  |  |
| 4 | Post Good Issue | Mark the relevant delivery and choose Post Goods Issue. Select today’s date from the dialog box and choose Continue. | The goods issues are posted for three deliveries. |  |

Financial Postings:

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 51600000Consptn Trde Gds | 13600000Inventory TradingGd | none |
| Finished Goods (FERT) | 54083000Inv Chg COGS w/CE | 13400000Inventory FinishedGd | none |

Printing Form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Outbound Delivery (VL03N). |  |  |
| 3 | Issue Delivery Output | On the Display Outbound Delivery screen, enter the delivery number and choose Continue.On the Delivery xxxxxxxx Display: Overview screen, choose Menu > Extras > Delivery Output > Output Control. | The Delivery: Output screen displays. |  |
| 4 | Print Preview | On the Delivery: Output screen, select the line with the Delivery Note Output Type and choose Display Document. | A preview of the print document is displayed. |  |
| 5 | Print Delivery Note | From the preview of the document, choose Print. | The delivery note is printed. |  |

#### Confirm Proof of Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to confirm proof of delivery. Either the customers sends you a confirmation that the goods were actually received or you assume it after a certain period for example two working days after goods issue. Only if you have the proof of delivery confirmed the invoice can be created.

|  |
| --- |
| Tip This step is necessary depending on the business partner data for this customer. In the shipping data you can see if a Proof of Delivery is expected or not. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Deliveries Worklist - Proof of Delivery (VLPODL). | The Deliveries for Proof of Delivery screen displays. |  |
| 3 | Select the Delivery | No entries necessary. Choose Execute. | The list of deliveries relevant for POD-confirmation is displayed. Status for your delivery is red (POD confirmation Status). |  |
| 4 | Confirm Proof of Delivery | Mark the delivery you posted Goods Issue in the previous step.Choose Confirm.On the Confirmation Prompt choose Continue. | The POD Confirmation Log displays with a message that Proof of Delivery for your delivery has been confirmed.If you return to the worklist the status of your delivery is now green. |  |

#### Create Billing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to handle the billing: Create three billing documents referring to the deliveries created in the previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using Role Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Documents (F0798) screen displays. |  |
| 3 | Define Billing Setting | Choose Billing Settings. You can make the following settings as below:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: OFFAutomatically post billing documents: ONDisplay billing documents after creation: ONChoose delivery items to be billed and select quantities：OFF |  |  |
| 4 | Search for Billing Due List | In the search condition, use criteria if necessary. | Sales document(s) will display in the result. |  |
| 5 | Select Item(s) for Billing | Select row(s) of sales document created previously and choose button Create Billing Document. | There is one window Creating Billing Documents displays. |  |
| 6 | Maintain Billing Date | Choose billing type Invoice (F2) and maintain billing date. For example: current date, then choose OK. | The draft billing document with ID TMPxxxxxxxx displays. |  |
| 7 | Save Billing Document | On the Billing Document (F1901) screen, choose Save. The draft version billing document with ID TMPxxxxxxxx turns into a saved billing document with ID xxxxxxxx. Make a note of the billing document number: __________. | The system generates an invoice for billing. |  |

|  |
| --- |
| Note After this step, the Electronic Nota Fiscal must be handled. This is part of scope item 1J5_BR (section Electronic Fiscal Documents). |

Financial Postings

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Finished Good (FERT) | Enter G/L Acc 1210000012100000 Description. | 41000000 Rev Domestic Prod22000000 Output tax (MWS) | none |

Manage Billing Documents

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access the App | Open Manage Billing Documents (F0797). | The Manage Billing Documents screen displays. |  |
| 2 | Search the Billing Document Created in Previous Step | In the billing document number recorded in previous step, choose Enter. | The billing document created in previous step displays. |  |
| 3 | Display the Billing Document | Select the billing document item and choose Display. | The billing document displays. |  |
| 4 | Check Output Condition | On the Billing Document screen, choose the last assignment block - Output Items. | There is one entry in the item and output type is BILLING_DOCUMENT. |  |
| 5 | Display Print Preview | On the Billing Document (F1901) screen, choose Preview. | Preview for PDF document displays. |  |
| 6 | Cancel Billing Document (Optional) | Select certain Billing document and choose Cancel Billing Document. | Billing Document Canceled log displays. |  |
| 7 | Update New Attachment (Optional) | In the Edit mode, add, delete and update the attachments. Save your changes by pressing the button Save in the footer bar. |  |  |
| 8 | Update New Text (Optional) | In the Edit mode, add, delete and update the text. Save your changes by pressing the button Save in the footer bar. |  |  |

#### Send Invoice - EDI Relevant

Purpose

This process step shows you how to send invoice to the Buyer system.

Prerequisites

Billing Document must have been created in the SAP S/4HANA system (supplier side).

Procedure

This step is automatically generated.

#### Check Invoice in AIF (Message Dashboard) - EDI relevant

Purpose

The customer invoice is sent via EDI to the Buyer. They are automatically processed if no error occurs. This process step shows you how to check the message status.

Prerequisites

The billing document has been created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Network Integration. |  |  |
| 2 | Access the App | Open Message Dashboard - SAP Application Interface Framework (/AIFX/WDA0005). |  |  |
| 3 | Choose Date and Namespace/Interface | On the Interface Monitor screen, choose correct time period entries and choose Search. In the Result List, choose the line of /SDEDI, Outbound Invoice Processing and choose All Messages. |  |  |
| 4 | Check Detail Messages | On the Monitoring and Error Handling screen, expend the messages in the left side of the screen, and choose the corresponding billing number created in previous step.Double click the message to see the detail information on the right side of the screen. |  |  |
| 5 | Reprocess Messages | Choose Reprocess if needed. |  |  |

#### Create Invoice List

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create invoice list.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Invoice Lists (F2740). | The Manage Invoice Lists (F2740) screen displays. |  |
| 3 | Navigate to Edit Worklist for Invoice Lists Screen | Choose Create. | The Edit Worklist for Invoice Lists screen displays. |  |
| 4 | Search Billing Documents | Make the following data in section Customer Data and choose Display Worklist for Invoice Lists:Payer: 33105010 | Billing documents displays in the result. |  |
| 5 | Select item(s) for Invoice List | Select the rows of Billing documents created previously and choose Collective Billing Document. | The system generates an invoice list for billing. |  |
| 6 | Check Invoice List Document | On the Edit Worklist for Invoice Lists screen, choose Log Display. And then choose Documents, make a note of the invoice list document number in SD Document column: __________. | Invoice list document number displays. |  |

Financial Postings

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Finished Good (FERT) | 44002000 Sales Disc Domestic22000000 Output tax (MWS) | Enter G/L Acc 1210000012100000 Description. | none |

Printing form

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Invoice Lists (F2740). |  |  |
| 3 | Search for Invoice List | Enter search term(s) in filter bar and choose Go:For example, enter invoice list number in field Invoice List. | The invoice list is displayed in result list. |  |
| 4 | Navigate to Invoice List Overview Screen | Click invoice list number 9XXXXXXX and choose Display Invoice Lists (VF23). | The Invoice List Display: Invoice List Items Overview screen displays. |  |
| 5 | Check Output Condition | Choose Output. | The Invoice List Display: Output screen displays. |  |
| 6 | Display Print Preview | Select the line already created for the print output and choose Display Document. | The printing form is displayed. |  |

|  |
| --- |
| Note The invoice list can consolidate a list of billing documents: Not only standard invoices with type F2 as above, but also debit memos, credit memos, and convergent billing types (CBD1, CBD2 and CBC1). To simulate invoice lists from debit memo，credit memo, or convergent billing, firstly complete all activities till debit memo/credit memo / convergent billing generation in the following scope item(s) using the data listed in chapter Master Data, Organizational Data, and Other Data:1F1 - Debit Memo Processing1IU - Customer ConsignmentBDD - Lean Customer ReturnsBKP - Customer Returns1EZ - Credit Memo Processing1MC - Omnichannel Convergent Billing |

### Sell from Valuated Stock in Transit

Sell from Valuated Stock in Transit is triggered by the attributes, which are set in the configuration (chapter 2.7.6). Based on the Item Category, the Sales Organization, the Plant and the Incoterms used, the process is triggered successfully.

#### Create Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create three sales orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Create Sales Order | On the Manage Sales Orders screen, choose Create, then select Create Sales Order - VA01. |  |  |
| 4 | Enter Order Details | On the Create Sales Document screen, make the following entries and choose Continue:Order Type: ORSales organization: 3310Distribution channel: 10Division: 00 |  |  |
| 5 | Enter Order Details | On the Create Standard Order: Overview screen, make the following entries and choose Continue:Sold-To Party: 33105001Ship-To Party: 33105001Customer Reference: <Reference number> Enter a customer purchase order number as reference.Customer Reference Date: <today>Go to item Overview TabProduct: FG0512Order Quantity: 2Incoterms: DAPOptional: Create additional line item with trading material TG0501.Optional: Add additional main line items with FG0511. |  | The Business Partner used for this scenario needs to be configured for Incoterm = DAP |
| 6 | Check Customer Hierarchy (optional) | Go to Menu > Goto > Header > Additional Functions > Customer Hierarchy . | The screen with the Customer Hiererchy Root node and its sub nodes relevant for this customer are displayed. |  |
| 7 | Check Pricing (optional) | In the overview screen select the item containing the material you entered and select button Item Conditions. | The condition DCH1 is part of the pricing calculation with the rate you have entered earlier. |  |
| 8 | Save | Choose Save. Make a note of the sales order number:___________. | Sales order with customer 33105001 is created. |  |

Printing Form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders (F1873) screen displays. |  |
| 3 | Search For Sales Order | Enter search term(s) in filter bar and choose Go, for example, enter sales order number in field Sales Order. | Sales order displays in result list. |  |
| 4 | Navigate to Sales Order Screen | Choose > on the right of the Sales Order item and navigate to Display Standard Orders xxx: Overview screen. | The Display Standard Orders xxx: Overview screen displays. |  |
| 5 | Check Output Condition | On the Display Standard Order xxx: Overview screen choose Menu > Extras > Output > Header > Edit . |  |  |
| 6 | Display Print Preview | On the Display Standard Order xxx: Output screen, select the line already created for the print output and choose Display Document. | Preview for PDF document displays. |  |

|  |
| --- |
| Note It can also be navigated to a factsheet screen in app Manage Sales Orders (F1873):On the Manage Sales Orders (Original) screen, enter search terms in filter bar and choose Go.In search result, choose your Sales Order Number and choose More Links. |

#### Create Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create three deliveries from three sales orders created previously.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Create Outbound Deliveries - From Sales Orders (F0869A). | The Create Outbound Deliveries - From Sales Orders (F0869A) screen displays. |  |
| 3 | Search Sales Order | Make the following entries and choose Go:Shipping Point: 3310Planned Creation Date: <Delivery selection date>Order: Sales order number created previously |  |  |
| 4 | Create Delivery | Select your sales orders and choose Create Deliveries. | Deliveries are triggered to create. |  |
| 5 | Check Details | Choose Display Log. | The Analyze Delivery Log screen displays. The failed entries will display in Messages tab. The delivery number will display in the Deliveries tab. |  |

|  |
| --- |
| Note At delivery creation, the scope item settings for check availability use available inventory and replenishment lead time. Without sufficient stock, the created delivery has no confirmed quantities and does not start the warehouse management picking process. As soon as there is sufficient stock at delivery creation, the system creates a delivery with further picking process in warehouse management. To avoid open deliveries, ensure that there is sufficient inventory quantity at delivery creation. Additionally, you have the following options to restrict the creation of deliveries with no confirmed quantities.- You may increase replenishment lead time that is used during the availability check (must be larger than the selection period used for delivery creation).- You may change the customizing settings for the incompleteness procedure for delivery creation, so that only complete deliveries may be saved.- You may change the customizing settings for the used delivery item category.The Check quantity 0 field must be adapted to B = Situation rejected with an error message. |

|  |
| --- |
| Note With the Analyze Outbound Delivery Logs app you can display an overview about the logs of all the deliveries which have been created in your system. You can filter by, for example, created by and Additional settings. If you select the arrow on the right of each delivery log entry you can display the exact message type and text and also the related sales document. |

Printing form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). | The Change Outbound Delivery (VL02N) screen displays. |  |
| 3 | Issue Delivery Output | On the Change Outbound Delivery (VL02N) screen, enter the delivery number and choose Continue. From the Delivery xxxxxxxx Change: Overview screen, choose Menu > Extras > Delivery Output > Output Control . | The Delivery: Output screen displays. |  |
| 4 | Print Preview | On the Delivery: Output screen, select the line with the Output Type Delivery_Pick_List and choose Display Document. | A preview of the print document displays. |  |
| 5 | Print Delivery Pick List | From the preview of the document, choose Print. | The delivery pick list is printed. |  |

#### Execute Picking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The picking process involves taking goods from a storage location and staging the right quantity in a picking area where the goods are prepared for shipping. This process step shows you how to pick deliveries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Choose Picking | Choose For Picking. |  |  |
| 4 | Enter Shipping Point | Make the following entries, and choose Execute:Shipping Point: 3310Under the Picking Data tab, selectOnly Picking Without WM: X |  |  |
| 5 | Change Outbound Deliveries | Choose your delivery number, and choose Change Outbound Deliveries. |  |  |
| 6 | Check Batch Split | Choose the Picking tab, check if batch split exists in the Batch Split Indicator column. |  |  |
| 7 | Enter Picked Quantity | If batch spilt exists, choose Batch Split Exists to expand sub item(s), enter <quantity equal to Deliv. Qty> in Picked Qty field for sub item.Note Sales BOM sub item materials are not relevant for the logistics process i.e. batch or picking quantity update.If batch split doesn't exist, enter <quantity equal to Deliv. Qty> in Picked Qty field for picking related item(s). |  |  |
| 8 | Choose Enter | Choose Enter. |  |  |
| 9 | Save | Choose Save. | The delivery has been decided. |  |
| 10 | Repeat | Repeat step 4 to 9 for other deliveries (if any). |  |  |

#### Check Batches (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check the batch number assigned to the material.

Prerequisites

Execute this step for batch managed products like FG0512.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). |  |  |
| 3 | Enter Outbound Delivery Number | In the Outbound Delivery field, enter <outbound delivery number>, and choose Continue. |  |  |
| 4 | Check Batch Number Assignment | If Expand Batch Split exists, go to the Batch field, and check the batch number assignment. | Batch numbers are assigned to the materials. |  |
| 5 | Save Document | Choose Save. |  |  |

#### Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post goods issues for delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Open Outbound Delivery Monitor | Choose For Goods Issue. Make the following entries and choose Execute.Shipping Point: 3310 |  |  |
| 4 | Post Good Issue | Mark the relevant delivery and choose Post Goods Issue. Select today’s date from the dialog box and choose Continue. | 1 successful and 0 incorrect goods movements. |  |

Financial Postings:

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 51600000Consptn Trde Gds | 13600000Inventory TradingGd | none |
| Finished Goods (FERT) | 54083000Inv Chg COGS w/CE | 13400000Inventory FinishedGd | none |

Printing Form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Outbound Delivery (VL03N). |  |  |
| 3 | Issue Delivery Output | On the Display Outbound Delivery screen, enter the delivery number and choose Continue.On the Delivery xxxxxxxx Display: Overview screen, choose Menu > Extras > Delivery Output > Output Control. | The Delivery: Output screen displays. |  |
| 4 | Print Preview | On the Delivery: Output screen, select the line with the Delivery Note Output Type and choose Display Document. | A preview of the print document is displayed. |  |
| 5 | Print Delivery Note | From the preview of the document, choose Print. | The delivery note is printed. |  |

#### Confirm Proof of Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to confirm proof of delivery. Either the customers sends you a confirmation that the goods were actually received or you assume it after a certain period for example two working days after goods issue. Only if you have the proof of delivery confirmed the invoice can be created.

|  |
| --- |
| Tip This step is necessary depending on the business partner data for this customer. In the shipping data you can see if a Proof of Delivery is expected or not. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Deliveries Worklist - Proof of Delivery (VLPODL). | The Deliveries for Proof of Delivery screen displays. |  |
| 3 | Select the Delivery | No entries necessary. Choose Execute. | The list of deliveries relevant for POD-confirmation is displayed. Status for your delivery is red (POD confirmation Status). |  |
| 4 | Confirm Proof of Delivery | Mark the delivery you posted Goods Issue in the previous step.Choose Confirm.On the Confirmation Prompt choose Continue. | The POD Confirmation Log displays with a message that Proof of Delivery for your delivery has been confirmed.If you return to the worklist the status of your delivery is now green. |  |

#### Create Billing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to handle the billing: Create three billing documents referring to the deliveries created in the previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using Role Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Documents (F0798) screen displays. |  |
| 3 | Define Billing Setting | Choose Billing Settings. You can make the following settings as below:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: OFFAutomatically post billing documents: ONDisplay billing documents after creation: ONChoose delivery items to be billed and select quantities：OFF |  |  |
| 4 | Search for Billing Due List | In the search condition, use criteria if necessary. | Sales document(s) will display in the result. |  |
| 5 | Select Item(s) for Billing | Select row(s) of sales document created previously and choose button Create Billing Document. | There is one window Creating Billing Documents displays. |  |
| 6 | Maintain Billing Date | Choose billing type Invoice (F2) and maintain billing date. For example: current date, then choose OK. | The draft billing document with ID TMPxxxxxxxx displays. |  |
| 7 | Save Billing Document | On the Billing Document (F1901) screen, choose Save. The draft version billing document with ID TMPxxxxxxxx turns into a saved billing document with ID xxxxxxxx. Make a note of the billing document number: __________. | The system generates an invoice for billing. |  |

|  |
| --- |
| Note After this step, the Electronic Nota Fiscal must be handled. This is part of scope item 1J5_BR (section Electronic Fiscal Documents). |

Financial Postings

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Finished Good (FERT) | Enter G/L Acc 1210000012100000 Description. | 41000000 Rev Domestic Prod22000000 Output tax (MWS) | none |

Manage Billing Documents

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access the App | Open Manage Billing Documents (F0797). | The Manage Billing Documents screen displays. |  |
| 2 | Search the Billing Document Created in Previous Step | In the billing document number recorded in previous step, choose Enter. | The billing document created in previous step displays. |  |
| 3 | Display the Billing Document | Select the billing document item and choose Display. | The billing document displays. |  |
| 4 | Check Output Condition | On the Billing Document screen, choose the last assignment block - Output Items. | There is one entry in the item and output type is BILLING_DOCUMENT. |  |
| 5 | Display Print Preview | On the Billing Document (F1901) screen, choose Preview. | Preview for PDF document displays. |  |
| 6 | Cancel Billing Document (Optional) | Select certain Billing document and choose Cancel Billing Document. | Billing Document Canceled log displays. |  |
| 7 | Update New Attachment (Optional) | In the Edit mode, add, delete and update the attachments. Save your changes by pressing the button Save in the footer bar. |  |  |
| 8 | Update New Text (Optional) | In the Edit mode, add, delete and update the text. Save your changes by pressing the button Save in the footer bar. |  |  |

## Appendix

### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

Table 3:

| Process | Business Condition |
| --- | --- |
| Accounts Receivable (J59) | Posting a Customer Invoice in Accounting, etc. Using the master data from this document, complete the following activities described in the test script:Posting a Customer Invoice in AccountingOverdue Receivables, Display Customer BalancesManage Customer Line Items |
| Sales Order Fulfillment Monitoring and Operations (BKK) (Optional) | This scope item describes the collection of periodic activities such as day ending activities, or reporting. Using the master data from this document, complete all the activities described in the Test Script of the scope item:Review Incomplete SD Documents (deliveries)Review Sales Documents blocked for billingReview Log of collective invoice creation |

### Scheduling Job (alternative)

#### Job Scheduling for Delivery Creation (Alternative)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to schedule a background job for creating outbound deliveries.

This app can be used as an alternative instead of the manual creation of outbound deliveries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Delivery Creation (F2228). | The Application Jobs screen displays. The app automatically shows the history of application jobs. |  |
| 3 | Create Delivery Creation Schedule | Choose Create to define a new job. | The New Job screen displays. The Job Template should be Schedule Delivery Creation for Sales Orders. |  |
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary, then choose Check. | The system displays the message Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A delivery creation job is scheduled. Screen goes back to Application Jobs. |  |
| 6 | Check Delivery Creation Job Log | On the Application Jobs screen, after job item’s status turned to Finish, choose Status symbol in the Log column.Note Choose the Magnifier, and the job list will refresh. | The job log details displays. |  |

#### Job Scheduling for Goods Issue Deliveries (Alternative)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to schedule a background job for goods issue posting with reference to outbound deliveries.

This app can be used as an alternative instead of the manual goods issue posting for outbound deliveries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Goods Issue for Deliveries (F2259). | The Application Jobs screen displays. The app automatically shows the history of application jobs. |  |
| 3 | Create Goods Issue Deliveries Schedule | Choose Create to define a new job. | The New Job screen displays. The Job Template should be defaulted as Schedule goods issue for Deliveries. |  |
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary, then choose Check. | The system displays the message Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A schedule goods issue for deliveries job is scheduled. The screen goes back to Application Jobs. |  |
| 6 | Check Goods Issue Deliveries Job Log | On the Application Jobs screen, after job item’s status turned to Finish, choose Status symbol in the Log column.Note Choose the Magnifier, and the job list will refresh. | The job log details are displayed. |  |

#### Job Scheduling for Billing Creation (Alternative)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to schedule a background job for creation billing documents.

This app can be used as an alternative instead of the manual creation of billing documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Billing Creation (F1519). | The Application Jobs screen displays. The app automatically shows the history of application jobs. |  |
| 3 | Create Billing Creation Schedule | Choose Create to define a new job for billing creation. | The New Job screen displays. Job Template should default as Schedule Billing Creation. |  |
| 4 | Job Parameters | Make the following entries:For Step 1, in the Template Selection section, from the drop-down box of Job Template, choose Schedule Billing Creation. Maintain a job name.Then choose Step 2, in the Scheduling Options section, make sure that Start Immediately checkbox is checked. Or you can also set the start date and start time.Then choose Step 3. In the Parameters section, make the following entries:Billing Date From: <today – 1 day>To: <today + 1 day>Sales Organization: 3310SD Document: <sales scheduling agreement created above>Sold-to-Party: <Customer from sales scheduling agreement> exampleDocuments to Be Selected: Delivery-RelatedChoose Check. | The system displays the message Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A billing creation job is scheduled. Screen goes back to Application Jobs. |  |
| 6 | Check Billing Creation Job Log | On the Application Jobs screen, after job item’s status turned to Finish, choose Job Log.Note Choose the Magnifier, and the job list will refresh. | The log details display. |  |

#### Job Scheduling for Billing Output (Alternative)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to schedule a background job for when and how billing documents are sent to customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Billing Output (F1510). | The Application Jobs screen displays. The app automatically shows the history of application jobs. |  |
| 3 | Create Billing Output Schedule | Choose Create to define a new job for billing creation. | The New Job screen displays. Job Template should default as Schedule Billing Output. |  |
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary.Choose Check. | The system displays the message Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A billing release job is scheduled. Return to Application Jobs. |  |
| 6 | Check Billing Output Job Log | On the Application Jobs screen, after job item’s status turned to Finish, choose Job Log.Note Choose Magnifier, and the job list will refresh. | The log details display. |  |

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
> Flagged while digesting this document, not verified: The VSIT section (Post Goods Issue) lists COGS/inventory postings (54083000 / 13400000, 51600000 / 13600000) identical to the standard flow, while the Purpose says goods issue to the delivery only moves stock into VSIT and revenue and COGS are recognized at the later goods issue from VSIT.

> [!warning] Conflict
> Flagged while digesting this document, not verified: The VSIT section says 'create three sales orders', 'three deliveries' and 'three billing documents', but its steps and the overview table cover only one order (customer 33105001) and the goods issue expected result is '1 successful and 0 incorrect goods movements'.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[08-sales-order-management/sell-from-stock-with-invoice-creation-before-goods-issue-7ua-ae-test-s]]
- related-to :: [[08-sales-order-management/test-script-sap-s-4hana-cloud-public-edition-sell-from-stock-bd9-ae-12]]
- see-also :: [[08-sales-order-management/customer-returns-management-consumer-products-61v-ae-test-script-sap-s]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5HL_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 98,470 chars in the whole document
