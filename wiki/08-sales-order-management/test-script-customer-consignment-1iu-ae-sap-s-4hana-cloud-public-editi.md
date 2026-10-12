---
id: 08-sales-order-management/test-script-customer-consignment-1iu-ae-sap-s-4hana-cloud-public-editi
title: "Test Script: Customer Consignment (1IU_AE) - SAP S/4HANA Cloud Public Edition 2608 (1IU_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud 2608 test script for Customer Consignment (1IU_AE): fill-up, issue, pick-up, return, with roles, sample data and postings."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/customer-consignment]
aliases: [1IU_S4CLD2608_BPD_EN_AE]
keywords: [Customer Consignment, consignment fill-up, consignment issue, consignment pick-up, consignment return, outbound delivery, delivery scheduling, batch management, serial numbers, stock overview]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1IU_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-727
topic: 08-sales-order-management/customer-consignment
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Customer Consignment (1IU_AE) - SAP S/4HANA Cloud Public Edition 2608 (1IU_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1IU_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Customer Consignment** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Customer Consignment (1IU_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232847219)

[2 Prerequisites 4](#_Toc232847220)

[2.1 System Access 4](#_Toc232847221)

[2.2 Roles 4](#_Toc232847222)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232847223)

[2.4 Business Conditions 7](#_Toc232847224)

[2.5 Preliminary Steps 7](#_Toc232847225)

[2.5.1 Set Initial Stock for Material 7](#_Toc232847226)

[2.5.2 Create Condition Records (Optional) 9](#_Toc232847227)

[3 Overview Table 10](#_Toc232847228)

[4 Test Procedures 13](#_Toc232847229)

[4.1 Consignment Fill-Up 13](#_Toc232847230)

[4.1.1 Create Consignment Fill-Up Order 13](#_Toc232847231)

[4.1.2 Create Outbound Delivery 15](#_Toc232847232)

[4.1.3 Pick Goods 16](#_Toc232847233)

[4.1.4 Check Batches (Optional) 17](#_Toc232847234)

[4.1.5 Maintain Serial Numbers (Optional) 18](#_Toc232847235)

[4.1.6 Post Goods Issue 19](#_Toc232847236)

[4.1.7 Check Stock Overview 21](#_Toc232847237)

[4.2 Consignment Issue 22](#_Toc232847238)

[4.2.1 Create Consignment Issue Order 22](#_Toc232847239)

[4.2.2 Create Delivery 24](#_Toc232847240)

[4.2.2.1 Option 1: Without Scheduling 24](#_Toc232847241)

[4.2.2.2 Option 2: With Scheduling 25](#_Toc232847242)

[4.2.3 Check Batches (Optional) 26](#_Toc232847243)

[4.2.4 Maintain Serial Numbers (Optional) 27](#_Toc232847244)

[4.2.5 Post Goods Issue 28](#_Toc232847245)

[4.2.5.1 Option 1: Without Scheduling 28](#_Toc232847246)

[4.2.5.2 Option 2: With Scheduling 29](#_Toc232847247)

[4.2.6 Check Stock Overview 30](#_Toc232847248)

[4.2.7 Create Customer Invoice (Optional) 31](#_Toc232847249)

[4.3 Consignment Pick-Up 33](#_Toc232847250)

[4.3.1 Create Consignment Pick-Up Order 33](#_Toc232847251)

[4.3.2 Create Return Delivery 35](#_Toc232847252)

[4.3.3 Receive Returned Goods 36](#_Toc232847253)

[4.3.4 Check Batches (Optional) 37](#_Toc232847254)

[4.3.5 Maintain Serial Numbers (Optional) 38](#_Toc232847255)

[4.3.6 Post Goods Receipt 39](#_Toc232847256)

[4.3.7 Check Stock Overview 40](#_Toc232847257)

[4.4 Consignment Return 41](#_Toc232847258)

[4.4.1 Create Consignment Return Order 41](#_Toc232847259)

[4.4.2 Create Return Delivery 43](#_Toc232847260)

[4.4.2.1 Option 1: Without Scheduling 43](#_Toc232847261)

[4.4.2.2 Option 2: With Scheduling 44](#_Toc232847262)

[4.4.3 Check Batches (Optional) 45](#_Toc232847263)

[4.4.4 Maintain Serial Numbers (Optional) 46](#_Toc232847264)

[4.4.5 Post Goods Receipt 47](#_Toc232847265)

[4.4.5.1 Option 1: Without Scheduling 47](#_Toc232847266)

[4.4.5.2 Option 2: With Scheduling 48](#_Toc232847267)

[4.4.6 Check Stock Overview 49](#_Toc232847268)

[4.4.7 Release Consignment Return Order for Billing 50](#_Toc232847269)

[4.4.8 Create Credit Memo 51](#_Toc232847270)

[5 Appendix 54](#_Toc232847271)

[5.1 Process Integration 54](#_Toc232847272)

[5.1.1 Preceding Processes 54](#_Toc232847273)

[5.1.2 Succeeding Processes 54](#_Toc232847274)

[5.2 Limitations 55](#_Toc232847275)

## Purpose

Overview

In this scenario, the goods are initially posted to the customer consignment stock and thus remain the property of the company (consignment fill-up).

At regular intervals, the customer reports how many articles are sold and how many articles are in the current stock (inventory). When the inventory is performed, the batch number may be entered to do a correct material posting. A corresponding sales order is entered that documents the issue from the customer consignment, meaning that the goods are no longer the property of the company (consignment issue).

Goods that are not required can be returned from the consignment stock to the central warehouse. The goods must not be defective. They are posted directly into the free stock (consignment pick-up).

In some cases, goods are returned to the customer consignment stock (by its own customer or based on erroneous consumption posting) after the consignment issue has already taken place. A return order is then created (consignment return).

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
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |
|  |  |  |  |  |
| Credit Controller | SAP_BR_CREDIT_CONTROLLER | Credit Management | SAP_BR_CREDIT_CONTROLLER |  |
| Returns and Refund Clerk | SAP_BR_RETURNS_REFUND_CLERK | Customer Returns | SAP_BR_RETURNS_REFUND_CLERK |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | TG11 | Trading Good for Reg. Trading (MRP planning) | See sections Business Conditions and Preliminary Steps. |
| Material | TG12 | Trad.Good 12,Reorder Point,Reg.Trad. | See sections Business Conditions and Preliminary Steps. |
| Material | TG21 | Trad.Good 21,Reorder Point,Batch-FIFO | Use only if you have activated the building block Batch Management (BLG) (BLH) (BLJ) (BLP).See sections Business Conditions and Preliminary Steps. |
| Material | TG22 | Trad.Good 22,Reorder Point,Batch-ExpD | Use only if you have activated the building block Batch Management (BLG) (BLH) (BLJ) (BLP).See sections Business Conditions and Preliminary Steps. |
| Sold-To Party | Domestic UAE Customer 3/ Domestic UAE Customer 5 | Domestic UAE Customer 3/ Domestic UAE Customer 5 | You can test the scope item using different domestic customers. 33100005 is for credit management. |
| Ship-To Party | 33100003/33100005 | Domestic UAE Customer 3/Domestic UAE Customer 5 |  |
| Payer | 33100003/33100005 | Customer domestic 03/Customer domestic 05 |  |
| Special Stock Partner | 3310000333100005 | Customer domestic 03Customer domestic 05 | Enter the special stock partner in the relevant customer master record on the partner screen using the partner function SB, or enter the partner function SB manually in the document header or in the relevant items if a special stock partner is required. |
| Plant | 3310 |  |  |
| Storage Location | 331A | Std. storage 1 | Outbound |
| Storage Location | 331R |  | Return |
| Shipping Point | 3310 |  | Outbound |
| Shipping Point | 331R |  | Return |
| Shipping Point | 331C |  | Consignment |
| Sales Organization | 3310 |  |  |
| Distribution Channel | 10 |  |  |
| Division | 00 |  |  |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BND | Create Customer Master - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| J45 – Procurement of Direct Materials | To run through this scope item, the materials must be available in stock. If you use trading goods (HAWA) you can either run through the Procurement of Direct Materials process or create stock using FLP tile Post Goods Movement (for details see section Preliminary Steps). |
| BNZ – Create New Open MM Posting Period - MDS | You have completed the step described in the master data script Create New Open MM Posting Period - MDS. Posting period is up to date. |

### Preliminary Steps

#### Set Initial Stock for Material

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to set initial stock to execute this scope item.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk (Retail). | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Goods Receipt Other screen displays. |  |
| 3 | Enter Movement Type | Make the following entry and choose Enter.Executable Action in Transaction MIGO: Goods Receipt & Other |  |  |
| 4 | Edit Material | On the Goods Receipt Other Screen: Material tab, make the following entry, and choose Enter:Material : <Material Number> . |  |  |
| 5 | Edit Quantity Data | On the Goods Receipt Other Screen: Quantity tab, make the following entry, and choose Enter:Qty in Unit of Entry: 1000Unit of Entry: <PC> |  |  |
| 6 | Enter the Goods Receipt Other Screen: Where Tab | On the Goods Receipt Other Screen: Where tab, make the following entries and choose Enter:Movement Type: 561 (Receipt per initial entry of stock balances into unrestricted use)Plant: <Enter a Plant>Storage Location: <Enter a Storage Location> |  |  |
| 7 | Enter the Goods Receipt Other Screen: Batch Tab | On the Goods Receipt Other Screen: Batch tab, make the following entry and choose Enter:Date of Manufacture: <Enter the Current Date or a Date in the Past> | Only relevant for batch relevant materials. |  |
| 8 | Save Your Entries | Choose Post. |  |  |

Financial Postings

| Material | Debited Accounts | Credited Accounts |
| --- | --- | --- |
| Trading Good (HAWA) | 13600000Inventory TradingGd | 39912000Inv Init SF&amp;Fin Bal |

#### Create Condition Records (Optional)

Purpose

In case you have finetuned the access sequence of SAP pre-shipped condition types, the relative condition records should be created accordingly.

You can find general information on how to create your own master data in the following: [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 2: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BEW | Create Free Goods Condition - MDS |

## Overview Table

The Customer Consignment (1IU) scope item consists of several process steps provided in the tables below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Table 3: Consignment Fill-Up

| Process Step | Business Role | App | Expected Results |
| --- | --- | --- | --- |
| [Create Consignment Fill-Up Order](#unique_10) [page ] 13 | Internal Sales Representative | Manage Sales Orders (F1873) | The consignment fill-up order is created.Document type: CCFU/Consignment Fill-Up |
| [Create Outbound Delivery](#unique_11) [page ] 15 | Shipping Specialist | Create Outbound Delivery - With Order Reference (VL01N) | The outbound delivery is created.Document type: LF/Outbound Delivery |
| [Pick Goods](#unique_12) [page ] 16 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | The material is picked. |
| [Check Batches (Optional)](#unique_13) [page ] 17 | Shipping Specialist | Change Outbound Delivery (VL02N) | The batches are checked. |
| [Post Goods Issue](#unique_14) [page ] 19 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | The goods issue is posted. |
| [Check Stock Overview](#unique_15) [page ] 21 | Shipping Specialist | Stock - Multiple Materials (F1595) | The delivered quantity is added to the consignment stock. |

Table 4: Consignment Issue

| Process Step | Business Role | App | Expected Results |
| --- | --- | --- | --- |
| [Create Consignment Issue Order](#unique_16) [page ] 22 | Internal Sales Representative | Manage Sales Orders (F1873) | The consignment issue order is created.Document type: CCIS/Consignment Issue |
| Create Delivery |  |  |  |
| [Option 1: Without Scheduling](#unique_17) [page ] 24 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) | The delivery is created.Document type: CCLF/Consignment Issue Delivery |
| [Option 2: With Scheduling](#unique_18) [page ] 25 | Shipping Specialist | Schedule Delivery Creation (F2228) | The deliveries are created.Document type: CCLF/Consignment Issue Delivery |
| [Check Batches (Optional)](#unique_19) [page ] 26 | Shipping Specialist | Change Outbound Delivery (VL02N) | The batches are checked. |
| Post Goods Issue |  |  |  |
| [Option 1: Without Scheduling](#unique_20) [page ] 28 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | The goods issue is posted. |
| [Option 2: With Scheduling](#unique_21) [page ] 29 | Shipping Specialist | Schedule Goods Issue for Deliveries (F2259) | The goods issue for deliveries is posted. |
| [Check Stock Overview](#unique_22) [page ] 30 | Shipping Specialist | Stock - Multiple Materials (F1595) | The customer consignment stock is reduced by the goods issue. |
| [Create Customer Invoice (Optional)](#unique_23) [page ] 31 | Billing Clerk | Create Billing Documents (F0798) | The customer invoice is created.Document type: F2/Customer Invoice |

Table 5: Consignment Pick-Up

| Process Step | Business Role | App | Expected Results |
| --- | --- | --- | --- |
| [Create Consignment Pick-Up Order](#unique_24) [page ] 33 | Internal Sales Representative | Create Sales Orders - VA01 (VA01) | The consignment pick-up order is created.Document type: CCPU/Consignment Pick-Up |
| [Create Return Delivery](#unique_25) [page ] 35 | Shipping Specialist | Create Outbound Delivery - With Order Reference (VL01N) | The delivery is created.Document type: LR/Return Delivery |
| [Receive Returned Goods](#unique_26) [page ] 36 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | The material is received. |
| [Check Batches (Optional)](#unique_27) [page ] 37 | Shipping Specialist | Change Outbound Delivery (VL02N) | The batch numbers are checked. |
| [Post Goods Receipt](#unique_28) [page ] 39 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | The goods receipt is posted. |
| [Check Stock Overview](#unique_29) [page ] 40 | Shipping Specialist | Stock - Multiple Materials (F1595) | The delivered quantity is posted from the consignment stock into the free available stock. |

Table 6: Consignment Return

| Process Step | Business Role | App | Expected Results |
| --- | --- | --- | --- |
| [Create Consignment Return Order](#unique_30) [page ] 41 | Internal Sales Representative | Create Sales Orders - VA01 (VA01) | The consignment return order is created.Document type: CCRE/Consignment Return |
| Create Return Delivery |  |  |  |
| [Option 1: Without Scheduling](#unique_31) [page ] 43 | Shipping Specialist | Create Outbound Delivery - With Order Reference (VL01N) | The delivery is created.Document type: CCLR/Consignment Return Delivery |
| [Option 2: With Scheduling](#unique_32) [page ] 44 | Shipping Specialist | Schedule Delivery Creation (F2228) | The deliveries are created.Document type: CCLR/Consignment Return Delivery |
| [Check Batches (Optional)](#unique_33) [page ] 45 | Shipping Specialist | Change Outbound Delivery (VL02N) | The batch numbers are checked. |
| Post Goods Receipt |  |  |  |
| [Option 1: Without Scheduling](#unique_34) [page ] 47 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | The goods receipt is posted. |
| [Option 2: With Scheduling](#unique_35) [page ] 48 | Shipping Specialist | Schedule Goods Issue for Deliveries (F2259) | The goods receipt for return for deliveries is posted. |
| [Check Stock Overview](#unique_36) [page ] 49 | Shipping Specialist | Stock - Multiple Materials (F1595) | The received quantity is added to the customer consignment stock. |
| [Release Consignment Return Order for Billing](#unique_37) [page ] 50 | Internal Sales Representative | Manage Customer Returns (F1708) | The billing block is removed. |
| [Create Credit Memo](#unique_38) [page ] 51 | Billing Clerk | Create Billing Documents (F0798) | Billing is carried out.Document type: CBRE/Credit Memo for Returns |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

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

The consignment fill-up order is used to transfer goods from plant stock to customer consignment stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). |  |  |
| 3 | Navigate to Create Sales Order screen | On the Manage Sales Order screen, choose Create and then choose Create Sales Orders - VA01. |  |  |
| 4 | Enter Order Type | On the Create Sales Document screen, make the following entries and choose Continue:Order Type: CCFUSales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 5 | Enter Material Data | On the Create Consignment Fill-Up: Overview screen, make the following entries:Sold-to Party: 33100003Ship-to Party: 33100003Cust. Reference: <customer purchase order number>On the Items tab, make the following entries:Materal: <all material numbers mentioned in master data section>Order Quantity: , for example, 20 PC<the required quantity> |  |  |
| 6 | Save Document | Choose Save. | Make a note of the sales order number _________. |  |

Printing Form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Search for Sales Order | Enter one or more search terms in the filter bar and choose Go.For example, enter a sales order number in the Sales Order field. |  |  |
| 4 | Navigate to Sales Order Screen | Choose a sales order. | The Display Sales Order -VA03 screen displays. |  |
| 5 | Check Output Condition | On the Display Sales Order - VA03 screen, choose Header Output Preview. |  |  |
| 6 | Display Print Preview | On the Display Consignment Fill-Up [number] Output screen, select the line already created for the print output and choose Display Document. |  |  |
| 7 | Print Document | Choose the Print button. Choose your local destination, and choose Print. | The document is printed. |  |

|  |
| --- |
| Note For On-premise, please implement the SAP note [2298826](https://me.sap.com/notes/2298826) - "Switch for enabling NAST condition based output for On-premise for activate the Output Management function" then process the output procedure steps. |

#### Create Outbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create the delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Outbound Deliveries - From Sales Orders (F0869A). |  |  |
| 3 | Search Sales Order | Make the following entries and choose Go:Shipping Point: 3310Planned Creation Date: Enter the delivery selection date.SD Document: Enter the sales order number created previously. |  |  |
| 4 | Create Delivery | Select your sales order items and choose Create Deliveries. | The outbound delivery is created. |  |
| 5 | Check Log | Choose Display Log. Choose Deliveries and note down the delivery ID. | You know which delivery is created. |  |

|  |
| --- |
| Note Without sufficient stock, the created delivery has no confirmed quantities and therefore does not start the warehouse management pick-process. As soon as there is sufficient stock for delivery creation, the system creates a delivery with the start of the picking process in warehouse management.To avoid open deliveries, ensure that there is sufficient inventory quantity at the time of delivery creation. Additionally, you have the following options to restrict the creation of deliveries with no confirmed quantities.You can change the customization settings for the incompleteness procedure for delivery creation, so that only complete deliveries are saved.You can change the customization settings for the used delivery item category. The Check quantity 0 field must be adapted to B = Situation rejected with an error message. |

|  |
| --- |
| Note With the Analyze Outbound Delivery Logs app, you can display an overview of the logs of all the deliveries that have been created in your system. With app Analyze Delivery Logs, you can filter by, for example, Created By and other additional filter criteria. If you select the arrow on the right of each delivery log entry, you can display the exact message type and text and also the related sales document. |

#### Pick Goods

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Open Outbound Delivery Monitor | On the Outbound Delivery Monitor screen, choose For Picking. |  |  |
| 4 | Enter Shipping Point | On the Outbound Deliveries for Picking screen, make the following entry:Shipping Point: 3310 |  |  |
| 5 | Set Only Picking without WM | Choose Only Picking without WM and choose Execute. |  |  |
| 6 | Select Outbound Delivery | On the Day's Workload for Picking screen, select your outbound delivery and choose Change Outbound Deliveries. |  |  |
| 7 | Enter Picked Quantity | On the Delivery [number] Change: Overview screen, choose the Picking tab. Enter the quantity in the Picked Qty field.In case you want to enter picking quantities for items with batches, enter the batch number or choose Batch Split to expand the sub item(s). Please refer to Enter / Check Batches (Optional).The picking status is set to complete if the picked quantity and the delivery quantity is equal. To solve deviations in quantity, choose Menu > Edit > Copy Picked Quantity as Deliv. Quantity . | The picked quantities are entered. |  |
| 8 | Save Document | Choose Save. | The delivery is saved. |  |

#### Check Batches (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you check the batch number assigned to the materials or enter the batch manually.

Prerequisite

You can only perform this activity if batch management is activated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). | The Change Outbound Deliveryscreen displays. |  |
| 3 | Enter Outbound Delivery Number | On the Change Outbound Delivery screen, enter the outbound delivery number and press Enter. |  |  |
| 4 | Check Batch Number Assignment | In the Batch Split Indicator column, expand Batch Split Exists, and check the batch number assignment in the expanded items.If the Batch field is not filled, enter the batch number or choose Batch Split, and enter the batch number and the quantities on the Batch Split screen. |  |  |
| 5 | Save Document | Choose Save. |  |  |

#### Maintain Serial Numbers (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to maintain serial number to the material.

Prerequisites

Run this step if Serial Number is used, such as TG20.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). |  |  |
| 3 | Enter Outbound Delivery Number | In the Outbound Delivery field, enter the outbound delivery number, and choose Enter. |  |  |
| 4 | Navigate to Serial Numbers | On the Delivery XXXXXXXXX Change: Overview screen, choose Menu > Extras > Serial Numbers . |  |  |
| 5 | Maintain Serial Numbers | On the Maintain Serial Numbers screen, choose Create serial number automatically and choose Continue. |  |  |
| 6 | Save Document | Choose Save. |  |  |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Open Outbound Delivery Monitor | Choose For Goods Issue. Make the following entries and choose Execute.Shipping Point: 3310 |  |  |
| 4 | Post Goods Issue | Select the relevant delivery and choose Post Goods Issue in the dialog box, choose today’s date and choose Continue. | The goods issue is posted. |  |

Financial Postings

As transfer from plant stock to consignment stock does not result in a change of stock owner, no accounting document is created.

Printing Form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Outbound Delivery (VL03N). | The Display Outbound Deliveryscreen displays. |  |
| 3 | Issue Delivery Output | On the Display Outbound Deliveryscreen, enter the delivery number and choose Continue.On the Delivery [number] Display: Overview screen, choose Menu > Extras > Delivery Output > Output Control. | The Delivery: Output screen is displayed. |  |
| 4 | Display Print Preview | On the Delivery: Output screen, select the line with the output type Delivery Note and choose Display PDF Document. | The preview of the print document is displayed. |  |
| 5 | Print Delivery Note | In the preview of the document, choose Print. | The delivery note is printed. |  |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Stock - Multiple Materials (F1595). | The Stock - Multiple Materials screen displays. |  |
| 3 | Enter Plant, Material Data, and Customer | On the Stock - Multiple Materials screen, make the following entries:Plant: 3310Material Number: Enter material numbers used in the consignment fill-up order.Customer: Enter the customer used in sales document.Special Stock Type: WChoose Go. | The customer consignment stock is displayed. The delivered quantity is posted into the consignment stock.Note You may need to adapt the following filters:Special Stock TypeCustomer: You may need to adapt column settings. For example, Customer. |  |

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

At regular intervals, the customer reports either how many products have been sold, or consumed, or how many products are in the current stock (inventory).

A corresponding order is entered, documenting the issue from the consignment stock.

A billing document is created for the issue from the external stock at the customer site.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Create Sales Order | On the Manage Sales Orders screen, choose Create and then choose Create Sales Order. |  |  |
| 4 | Enter Order Type | On the Create Sales Document screen, make the following entries and choose Continue:Order Type: CCISSales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 5 | Enter Material Data | On the Create Consignment Issue: Overview screen, make the following entries:Sold-to Party: 33100003Ship-to Party: 33100003Cust. Reference: <the customer purchase order number>On the Items tab, make the following entries:Material: <all material numbers mentioned in master data section>Order Quantity: <the required quantity>, for example, 10PC | Item Category:You can choose correct item category to fit your business caseCIN (By default): Consig IssueCCXN (Manual input): Consig Issue FOC Bil (Consignment Issue with Free of Charge 100% discount).CCIN (Manual input): Consig Issue FOC (Consignment Issue with Free of Charge Not Billing Relevant). |  |
| 6 | Enter Batch Number | If the entered material is batch-managed, please continue with process step Enter Batch Number (Optional).Double-click the item with the batch-managed material.On the Sales A tab, enter the batch number in the Batch field. | A batch number is assigned to the item with batch-managed material. |  |
| 7 | Save Document | Choose Save.Make a note of the sales order number__________. | The consignment issue order is created. |  |

Printing Form (Optional)

The consignment issue is currently excluded from the output form determination.

|  |
| --- |
| Note If you want to print a consignment issue order, you can change the output form determination for sales document type CCIS. To do so, log on to the SAP Fiori launchpad as Administrator and open the app Output Parameter Determination. |

|  |
| --- |
| Note For On-premise, please implement the SAP note [2298826](https://me.sap.com/notes/2298826) - "Switch for enabling NAST condition based output for On-premise for activate the Output Management function" then process the output procedure steps. |

#### Create Delivery

##### Option 1: Without Scheduling

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create the delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Outbound Deliveries - From Sales Orders (F0869A). | The Create Outbound Delivery screen displays. |  |
| 3 | Search Sales Order | Make the following entries and choose Go:Shipping Point: 331CPlanned Creation Date: <the delivery selection date>SD Document: <the sales order number created previousl> |  |  |
| 4 | Create Delivery | Select your sales order items and choose Create Deliveries. | The creation of a delivery is triggered. |  |
| 5 | Check Log | Choose Display Log, go to Deliveries, and note down the delivery ID. | You know which delivery is created. |  |

Printing Form (Optional)

Deliveries for consignment issues are currently excluded from the output form determination.

|  |
| --- |
| Note If you want to print a delivery for a consignment issue order, you can change the output form determination for sales document type CCLF. To do so, log on to the SAP Fiori launchpad as Administrator and open the app Output Parameter Determination.Without sufficient stock, the created delivery has no confirmed quantities and therefore does not start the warehouse management picking process. As soon as there is sufficient stock for delivery creation, the system creates a delivery with the start of the picking process in warehouse management. To avoid open deliveries, ensure that there is sufficient inventory quantity at the time of delivery creation. Additionally, you have the following options to restrict the creation of deliveries with no confirmed quantities:You can change the customization settings for the incompleteness procedure for delivery creation, so that only complete deliveries are saved.You can change the customization settings for the used delivery item category. The check quantity 0 field must be adapted to B = Situation rejected with an error message.With the Analyze Outbound Delivery Logs app, you can display an overview of the logs of all the deliveries that have been created in your system. You can filter by, for example, Created By. If you select the arrow on the right of each delivery log entry, you can display the exact message type and text, and also the related sales document. |

##### Option 2: With Scheduling

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you schedule the delivery creation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Schedule Delivery Creation (F2228). | The Application Jobs screen displays. |  |
| 3 | Create Job for Delivery Creation | Choose Create and at a minimum make the following entries:Step 1 Template SelectionSelect Template Schedule Delivery Creation for Sales Orders, enter Job name and navigate toStep 2 Scheduling OptionsChoose Start Immediately.Select Define Recurrence PatternIn the upcoming popup, select Recurrence Pattern Single Run, click OK and navigate toStep 3 ParametersEnter Shipping Point: XX1C (e.g. 331C)You can also add more Scheduling Options.Choose Schedule. | The New Job screen displays.Depending on the scheduling options, the delivery creation is started immediately or at a specific time, for one or more consignment orders.The Application Jobs screen displays. |  |
| 4 | View Job Log | On the Application Job screen, choose Go to refresh the status. If you scheduled the job for immediate start, the job should start and finish immediately. Once the job status is updated, navigate to the job log via the column Log. | The delivery is created. |  |

#### Check Batches (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you check the batch number assigned to the materials.

Prerequisite

You can only perform this activity if batch management is activated for the material.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). | The Change Outbound Delivery screen displays. |  |
| 3 | Enter Outbound Delivery Number | On the Change Outbound Deliveryscreen, enter the outbound delivery number and press Enter. |  |  |
| 4 | Enter Batch Number | If the Batch field is not filled, enter the batch number or choose Batch Split, and enter the batch number and the quantities on the Batch Split screen. |  |  |
| 5 | Save Document | Choose Save. |  |  |

#### Maintain Serial Numbers (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to maintain serial number to the material.

Prerequisites

Run this step if Serial Number is used, such as TG20.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). |  |  |
| 3 | Enter Outbound Delivery Number | In the Outbound Delivery field, enter the outbound delivery number, and choose Enter. |  |  |
| 4 | Navigate to Serial Numbers | On the Delivery XXXXXXXXX Change: Overview screen, choose Menu > Extras > Serial Numbers . |  |  |
| 5 | Maintain Serial Numbers | On the Maintain Serial Numbers screen, choose Create serial number automatically and choose Continue. |  |  |
| 6 | Save Document | Choose Save. |  |  |

#### Post Goods Issue

##### Option 1: Without Scheduling

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). | The Outbound Delivery Monitor screen displays. |  |
| 3 | Open Outbound Delivery Monitor | Choose For Goods Issue. Make the following entry and choose Execute:Shipping point: 331C |  |  |
| 4 | Post Goods Issue | Select the relevant delivery and choose Post Goods Issue. In the dialog box, choose today’s date and choose Continue. | The goods issue is posted. |  |

Financial Postings

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 54083000Inv Chg COGS w/CE | 13600000Inventory TradingGd | none |

##### Option 2: With Scheduling

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you schedule the posting of goods issue for deliveries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Goods Issue for Deliveries (F2259). | The Application Jobs screen displays. |  |
| 3 | Create Scheduling Job | Choose Create and at minimum make the following entries:Step 1 Template SelectionSelect Template Schedule Goods Issue for Deliveries, enter Job name and navigate toStep 2 Scheduling OptionsChoose Start Immediately.Select Define Recurrence Pattern.In the upcoming popup, select Recurrence Pattern Single Run, click OK and navigate toStep 3 ParametersEnter Shipping Point: xxxx (according to test script)Check and adjust defaulted value for Planned Goods Movement DateYou can also add more Scheduling Options.Choose Schedule. | The New Job screen displays.Depending on the scheduling options, the goods issue posting is started immediately or at a specific time, for one or more consignment deliveries.The Application Jobs screen displays. |  |
| 4 | View Job Log | On the Application Job screen, choose Go to refresh the status. If you scheduled the job for immediate start, the job should start and finish immediately. Once the job status is updated, navigate to the job log via the column Log. | The goods issue is posted. |  |

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

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Stock - Multiple Materials (F1595). | The Stock - Multiple Materials screen displays. |  |
| 3 | Enter Plant, Material Data, and Customer | On the Stock - Multiple Materials screen, make the following entries:Plant: 3310Material Number: Enter material numbers used in the consignment fill-up order.Customer: Enter the customer used in sales document.Special Stock Type: WChoose Go. | The customer consignment stock is displayed. The delivered quantity is posted into the consignment stock.Note You may need to adapt the following filters:Special Stock TypeCustomer: You may need to adapt column settings, for example, Customer. |  |

#### Create Customer Invoice (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you handle the billing.

Invoice Creation is NOT relevant for CCIN: Consig Issue FOC Enh (Consignment Issue with Free of Charge - Not Billing Relevant).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Create Billing Documents (F0798). | The Create Billing Documents screen displays. |  |
| 3 | Search for Billing Due Items | Enter the relevant search criteria, such as sold-to party, sales document ID, or sales document category. In the SD Document Category filter, choose Delivery. | A list of delivery-related billing due list items is displayed. |  |
| 4 | Make Billing Settings | Choose the cog symbol on the bottom right-hand corner of the screen.Make sure that Display Billing Documents After Creation is switched on. If not, switch it on.Check that Automatically Post Billing Documents is switched on. If not, switch it on.Choose OK. | The Billing Settings dialog displays and you make your settings. |  |
| 5 | Select Billing Due List Item | Select a row and set a check mark next to the billing due list item that you want to create a billing document for. | The appropriate billing due list item is selected. |  |
| 6 | Create and Display Invoice | Choose the Create button at the bottom of the screen.Choose OK in the pop-up screen. | The system generates a draft customer invoice with ID Sxxxxxxxx and displays the invoice details in the Manage Billing Documentsapp. |  |
| 7 | Save Billing Document | In the Billing Document screen, click button Save. The draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx, make a note of the billing document number: __________. | The system generates an invoice for billing. |  |
| 8 | Display Print Preview | Choose Preview at the bottom of the screen. | A preview of the invoice document in PDF form is displayed. |  |

Financial Postings

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 33100003 | 41000000Rev Domestic Prod 22000000Output Tax (MWS) 21030000 (optional)Freight Clrg MMOnly posted if you enter freight costs in sales order. | none |

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

The customer can return goods that are not required or sold to the central warehouse. The consignment pick-up triggers the return of goods from the customer’s custody.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Sales Orders - VA01 (VA01). | The Create Sales Document screen displays. |  |
| 3 | Enter Order Type | On the Create Sales Document screen, make the following entries and choose Continue (Enter):Order Type: <CCPU>Sales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 4 | Enter Material Data | On the Create Consignment Pick-Up: Overview screen, make the following entries:Sold-to Party: 33100003Ship-to Party: 33100003Customer Reference: <Enter the Customer Purchase Order Number>On the Items tab, make the following entries:Material: <Enter All Material Numbers Mentioned in Master Data Section>Order Quantity: Enter the Required Quantity(for example, 10 PC) |  |  |
| 5 | Enter Batch Number | If the material entered is batch-managed, continue with the Enter Batch Number (Optional) process step.Double-click the item with the batch-managed material.On the Sales A tab, enter <the Batch Number> in the Batch field. | A batch number is assigned to the item with batch-managed material. |  |
| 6 | Save Document | Choose Save.Make a note of the sales order number__________. |  |  |

Printing Form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Sales Orders - VA03 (VA03). | The Display Sales Document screen displays. |  |
| 3 | Enter Sales Order ID | Enter <the sales order ID>, and press Enter. | The Display Consignment Pick-Up Order (number): Overview screen displays |  |
| 4 | Check Output Condition | On the Display Consignment Pick-Up Order [number]: Overview screen, choose Header Output Preview. |  |  |
| 5 | Display Print Preview | On the Display Consignment Pick-Up Order [number] Output screen, select the line already created for the print output, and choose Display PDF Document. |  |  |
| 6 | Print Document | Choose Print. Choose your local destination, and choose Print. | The document is printed. |  |

|  |
| --- |
| Note For On-premise version, please implement the SAP note [2298826](https://me.sap.com/notes/2298826) - "Switch for enabling NAST condition based output for On-premise for activate the Output Management function", then process the output procedure steps. |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Outbound Delivery - With Order Reference (VL01N). | The Create Outbound Delivery with Order Reference screen displays. |  |
| 3 | Search Sales Order | Make the following entries:Shipping Point: 331RSelection Date: Enter the delivery selection date.Order: Enter the sales order number created previously.Choose Continue. |  |  |
| 4 | Create Delivery | Select your sales order items. | The creation of a return delivery is triggered. |  |
| 5 | Save Document | Choose Save. Make a note of the delivery number. | A delivery is created. |  |

|  |
| --- |
| Note Depending on the scope item settings, the availability is checked at the delivery creation using the available inventory. Without sufficient customer consignment stock, the created delivery has no confirmed quantities. As soon as there is sufficient stock for delivery creation, the system creates a delivery.To avoid open deliveries, ensure that there is sufficient inventory quantity at the time of delivery creation. Additionally, you have the following options to restrict the creation of deliveries with no confirmed quantities:You can change the customization settings for the incompleteness procedure for delivery creation, so that only complete deliveries are saved.You can change the customization settings for the used delivery item category. The Check quantity 0 field must be adapted to B = Situation rejected with an error message. |

|  |
| --- |
| Note With the Analyze Outbound Delivery Logs app, you can display an overview of the logs of all the deliveries that have been created in your system. You can filter by, for example, Created By. If you select the arrow on the right of each delivery log entry, you can display the exact message type and text, and also the related sales document. |

Printing Form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Outbound Delivery (VL03N). | The Display Outbound Delivery screen displays. |  |
| 3 | Issue Delivery Output | On the Display Outbound Deliveryscreen, enter the delivery number and choose Continue.On the Delivery (number) Display: Overview screen, choose Menu → Extras → Delivery Output → Output Control. | The Delivery Overview screen displays. |  |
| 4 | Display Print Preview | On the Delivery: Output screen, select the line with the output type Delivery Note and choose Display PDF Document. | A preview of the print document is displayed. |  |
| 5 | Print Delivery Note | In the preview of the document, choose Print. | The delivery note is printed. |  |

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

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). | The Outbound Delivery Monitor screen displays. |  |
| 3 | Open Outbound Delivery Monitor | On the Outbound Delivery Monitor screen, choose For Picking. |  |  |
| 4 | Enter Shipping Point | On the Outbound Deliveries for Pickingscreen, make the following entry:Shipping Point: 331R |  |  |
| 5 | Set Only Picking Without WM | Choose Only Picking without WM and choose Execute. |  |  |
| 6 | Select Outbound Delivery | On the Day's Workload for Picking screen, select your outbound delivery and choose Change Outbound Deliveries. |  |  |
| 7 | Enter Received Quantity | On the Delivery [number] Change: Overview screen, choose the Picking tab. Enter the quantity in the Picked Qty field. In case you want to enter picking quantities for items with batches, enter the batch number or choose Batch Split to expand the sub item(s). Please refer to Enter / Check Batches (Optional).The picking status is set to complete if the picked quantity and the delivery quantity is equal. To solve deviations in quantity, choose Menu > Edit > Copy Picked Quantity as Deliv. Quantity . |  |  |
| 8 | Save Document | Choose Save. | The delivery is saved. |  |

#### Check Batches (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you check the batch number assigned to the materials or enter batch numbers manually.

Prerequisite

You can only perform this activity if batch management is activated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). | The Change Outbound Deliveryscreen displays. |  |
| 3 | Enter Outbound Delivery | On the Change Outbound Delivery screen, enter the outbound delivery number and press Enter. |  |  |
| 4 | Check Batch Number Assignment | Check the batch number.If the Batch field is not filled, enter the batch number or choose Batch Split, and enter the batch number and the quantities on the Batch Split screen. |  |  |
| 5 | Save Document | Choose Save. |  |  |

#### Maintain Serial Numbers (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to maintain serial number to the material.

Prerequisites

Run this step if Serial Number is used, such as TG20.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). |  |  |
| 3 | Enter Outbound Delivery Number | In the Outbound Delivery field, enter the outbound delivery number, and choose Enter. |  |  |
| 4 | Navigate to Serial Numbers | On the Delivery XXXXXXXXX Change: Overview screen, choose Menu > Extras > Serial Numbers . |  |  |
| 5 | Maintain Serial Numbers | On the Maintain Serial Numbers screen, choose Create serial number automatically and choose Continue. |  |  |
| 6 | Save Document | Choose Save. |  |  |

#### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you post the goods receipt. When the goods receipt is posted, the transfer from the consignment stock is carried out at the same time as the direct posting into the free stock of the return storage location.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). | The Outbound Delivery Monitor screen displays. |  |
| 3 | Make Entries | Choose For Goods Issue. Make the following entry and choose ExecuteShipping Point: 331R |  |  |
| 4 | Post Goods Issue | Select the relevant delivery and choose Post Goods Issue. In the dialog box, choose today’s date and choose Continue. | The goods receipt is posted. |  |

Financial Postings

A transfer from consignment stock to plant stock does not result in an owner change of stock, no accounting document is created.

#### Check Stock Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The goods are transferred again to customer's consignment stock. The stock overview reflects this transfer of products.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Stock - Multiple Materials (F1595). | The Stock - Multiple Materials screen displays. |  |
| 3 | Enter Plant, Material Data, and Customer | On the Stock - Multiple Materials screen, make the following entries:Plant: 3310Material Number: Enter the material numbers used in the consignment pick-up order.Customer: Enter the customer used in sales document.Special Stock Type: WChoose Go. | The customer consignment stock is displayed. The delivered quantity has been posted into the consignment stock.Note You may need to adapt the following filters:Special Stock TypeCustomerYou may need to adapt column settings. For example, Customer. |  |

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

Goods that have been consumed or sold by the customer may be returned to the consignment stock. In this case, the customer communicates the returning quantity together with the corresponding batch number. A return order with the following follow-on documents is generated:

- A returns delivery with subsequent goods receipt
- A credit note for returns

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Sales Orders - VA01 (VA01). | The Create Sales Document screen displays. |  |
| 3 | Enter Order Type | On the Create Sales Document screen, make the following entries:Order Type: CCRESales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 4 | Enter Material Data | On the Create Consignment Return: Overview screen, make the following entries and choose Continue (Enter):Sold-To Party: 33100003Ship-To Party: 33100003Cust. Reference: Enter the customer purchase order number.On the Sales tab, make the following entries:Material: <Enter all material numbers mentioned in master data section>Order Quantity: <Enter the required quantity (for example, 10 PC)>Check that the Billing Block is set. | Item Category:You can choose correct item category to fit your business caseCRN (By default): Consig ReturnCCRN (Manual input): ConsigReturn FOC Bil (Consignment Issue with Free of Charge 100% discount).CRBN (Manual input): Consig Return FOC (Consignment Issue with Free of Charge Not Billing Relevant). |  |
| 5 | Enter Batch Number | If the entered material is batch-managed, please continue with Enter Batch Number (Optional) process step.Double-click the item with the batch-managed material.On the Sales tab, enter <the batch number> in the Batch field. | A batch number is assigned to the item with batch-managed material. |  |
| 6 | Save Document | Choose Save.Make a note of the sales order number___________. | The customer return order is created. |  |

Printing Form (Optional)

Consignment returns are currently excluded from the output form determination.

|  |
| --- |
| Note If you want to print a consignment return order, you can change the output form determination for CCRE sales document type. To do so, log on to the SAP Fiori launchpad as Administrator and open Output Parameter Determination app. |

|  |
| --- |
| Note For On-premise version, please implement the SAP note [2298826](https://me.sap.com/notes/2298826) - "Switch for enabling NAST condition based output for On-premise for activate the Output Management function" then process the output procedure steps. |

#### Create Return Delivery

##### Option 1: Without Scheduling

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Outbound Delivery - With Order Reference (VL01N). | The Create Outbound Delivery with Order Reference screen displays. |  |
| 3 | Search Sales Order | Make the following entries:Shipping Point: 331CSelection Date: < the delivery selection date>Order: <the sales order number created previously>Choose Continue. |  |  |
| 4 | Create Delivery | Select your sales order items. | The creation of a delivery is triggered. |  |
| 5 | Save Document | Choose Save.Make a note of the delivery number:_____________. | A return delivery is created. |  |

|  |
| --- |
| Note With the Analyze Outbound Delivery Logs app, you can display an overview of the logs of all the deliveries that have been created in your system. You can filter by, for example, Created By. If you select the arrow on the right of each delivery log entry, you can display the exact message type and text, and also the related sales document. |

Printing Form (Optional)

Deliveries for consignment returns are currently excluded from the output form determination.

|  |
| --- |
| Note If you want to print a delivery for consignment return order, you can change the output form determination for sales document type CCLR. To do so, log on to the SAP Fiori launchpad as Administrator and open the app Output Parameter Determination. |

##### Option 2: With Scheduling

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you schedule the delivery creation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Delivery Creation (F2228). | The Application Jobsscreen displays. |  |
| 3 | Create Scheduling Job | Choose Create and at a minimum make the following entries:Step 1 Template SelectionSelect Template Schedule Delivery Creation for Sales Orders, enter Job name and navigate toStep 2 Scheduling OptionsChoose Start Immediately.Select Define Recurrence PatternIn the upcoming popup, select Recurrence Pattern Single Run, click OK and navigate toStep 3 ParametersEnter Shipping Point: XXXX (e.g. according to test script)You can also add more Scheduling Options.Choose Schedule. | The New Job screen displays.Depending on the scheduling options, the delivery creation is started immediately or at a specific time, for one or more consignment orders.The Application Jobs screen displays. |  |
| 4 | View Job Log | On the Application Job screen, choose Go to refresh the status. If you scheduled the job for immediate start, the job should start and finish immediately. Once the job status is updated, navigate to the job log via the Log column. | The delivery is created. |  |

#### Check Batches (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you check the batch number assigned to the materials.

Prerequisite

You can only perform this activity if batch management is activated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). | The Change Outbound Delivery (VL02N) screen displays. |  |
| 3 | Enter Outbound Delivery | On the Change Outbound Delivery (VL02N) screen, enter the outbound delivery number and press Enter. |  |  |
| 4 | Check Batch Number Assignment | Check the batch number.If the Batch field is not filled, enter the batch number or choose Batch Split, and enter the batch number and the quantities on the Batch Split screen. |  |  |
| 5 | Save Document | Choose Save. |  |  |

#### Maintain Serial Numbers (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to maintain serial number to the material.

Prerequisites

Run this step if Serial Number is used, such as TG20.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). |  |  |
| 3 | Enter Outbound Delivery Number | In the Outbound Delivery field, enter the outbound delivery number, and choose Enter. |  |  |
| 4 | Navigate to Serial Numbers | On the Delivery XXXXXXXXX Change: Overview screen, choose Menu > Extras > Serial Numbers . |  |  |
| 5 | Maintain Serial Numbers | On the Maintain Serial Numbers screen, choose Create serial number automatically and choose Continue. |  |  |
| 6 | Save Document | Choose Save. |  |  |

#### Post Goods Receipt

##### Option 1: Without Scheduling

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). | The Outbound Delivery Monitor screen displays. |  |
| 3 | Open Outbound Delivery Monitor | Choose For Goods Issue. Make the following entry and choose Execute.Shipping Point: 331C |  |  |
| 4 | Post Goods Issue | Select the relevant delivery and choose Post Goods Issue. In the dialog box, choose today’s date and choose Continue. | The goods receipt is posted. |  |

Post Goods Issue

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 51600000Consptn Trde Gds | 13600000Inventory TradingGd | none |

##### Option 2: With Scheduling

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you schedule the posting of goods receipts for return deliveries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Goods Issue for Deliveries (F2259). | The Application Jobs screen displays. |  |
| 3 | Create Scheduling Job | Choose Create and at minimum make the following entries:Step 1 Template SelectionSelect Template Schedule Goods Issue for Deliveries, enter Job name and navigate toStep 2 Scheduling OptionsChoose Start Immediately.Select Define Recurrence Pattern.In the upcoming popup, select Recurrence Pattern Single Run, click OK and navigate toStep 3 ParametersEnter Shipping Point: xxxx (according to test script)Check and adjust defaulted value for Planned Goods Movement DateYou can also add more Scheduling Options.Choose Schedule.e. | The New Job screen displays.Depending on the scheduling options, the goods issue posting is started immediately or at a specific time, for one or more consignment deliveries.The Application Jobs screen displays. |  |
| 4 | View Job Log | On the Application Job screen, choose Go to refresh the status. If you scheduled the job for immediate start, the job should start and finish immediately. Once the job status is updated, navigate to the job log via the Log column. | The goods issue is posted. |  |

#### Check Stock Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The goods are transferred from the customer's consignment stock and no longer owned by the company. The stock overview reflects this transfer of products.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Stock - Multiple Materials (F1595). | The Stock - Multiple Materials screen displays. |  |
| 3 | Enter Plant, Material Data, and Customer | On the Stock - Multiple Materials screen, make the following entries:Plant: 3310Material Number: Enter the material numbers used in the consignment fill-up order.Customer: Enter the customer used in sales document.Special Stock Type: WChoose Go. | The customer consignment stock is displayed. The delivered quantity is posted into the consignment stock.Note You may need to adapt the following filters:Special Stock TypeCustomerYou may need to adapt column settings. For example, Customer. |  |

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

Invoice Creation is NOT relevant for CCIN: Consig Issue FOC Enh (Consignment Issue with Free of Charge - Not Billing Relevant).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Returns and Refund Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer Returns (F1708). | The Manage Customer Returns screen displays. |  |
| 3 | Navigate to Display Return Order Screen | On the Manage Customer Returns screen, enter the respective order number created in previous step in the Customer Returns field and choose Go.Choose the return order line that displays. |  |  |
| 4 | Navigate to Change Return Order Screen | Choose Change. |  |  |
| 5 | Remove Billing Block | On the Change Consignment Return: Overview screen, remove the billing block. | The billing block is removed. |  |
| 6 | Save Document | Choose Save. | The sales order is saved. |  |

#### Create Credit Memo

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you handle the billing.

Invoice Creation is NOT relevant for CCIN: Consig Issue FOC Enh (Consignment Issue with Free of Charge - Not Billing Relevant).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Documentsscreen displays. |  |
| 3 | Search for Billing Due Items | Enter the relevant search criteria, such as <Sold-to Party>, <Sales Document ID>, or <Sales Document Category>, in the search field.In the SD Document Category filter, choose Returns Delivery for Order. | A list of delivery-related billing due list items is displayed. |  |
| 4 | Make Billing Settings | Choose the cog symbol on the top right-hand corner of the screen.Make sure that Display Billing Documents After Creation is switched on. If not, switch it on.Check that Automatically Post Billing Documents is switched on. If not, switch it on.Choose OK. | The Billing Settings dialog displays, and you can make your settings. |  |
| 5 | Select Billing Due List Item | Select a row and set a check mark next to the billing due list item that you want to create a billing document for. | The appropriate billing due list item is selected. |  |
| 6 | Create and Display Invoice | Choose Create Billing Documents.Choose Credit Memo for Returns (CBRE) billing type, and maintain Billing Date, for example, <Current Date>, then press OK. | The system generates a draft customer invoice with ID TMPxxxxxxx and displays the invoice details in the Manage Billing Documents app. |  |
| 7 | Save Billing Document | On the Billing Document screen, click Save.The draft version billing document with ID TMPxxxxxxx turns into a saved billing document with ID xxxxxxxx.Make a note of the billing document number: __________. | The system generates an invoice for billing. |  |
| 8 | Display Print Preview | Choose Preview at the bottom of the screen. | A preview of the credit memo document in PDF form is displayed. |  |

Financial Postings

| Material | Credited Accounts | Debited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 33100003 | 41000000Rev Domestic Prod 22000000Output Tax (MWS) 21030000 (optional) Freight Clrg MMOnly posted if you enter freight costs in sales order | none |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

You may first have completed the following processes and conditions before you start with the test steps:

| Process | Business Condition |
| --- | --- |
| BD6 – Basic Credit Management – Set Credit Limit (Optional) | In this process, a credit limit is set for the selected customer.Complete all the activities regarding set of credit limit described in the test script of the scope item BD6 – Basic Credit Management. Credit limit can’t be checked for consignment fill-up. Only consignment issue will update credit values, but also won’t check the credit limit of the customer. |

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| J59 –Accounts Receivable | In this activity, you post the incoming payment.Complete all activities described in the test script of scope item J59 –Accounts Receivable (Sections Posting a Customer Invoice in Accounting, Overdue Receivables, Display Customer Balances, Manage Customer Line Items) using the master data from this document. |
| BKK – Sales Order Fulfillment Monitoring and Operations | This scope item describes the collection of periodic activities, such as day ending activities or legal requirements.Using the master data from this document, complete all the activities described in the Business Process Documentation of scope item BKK – Sales Order Fulfillment Monitoring and Operations (Chapters Review Sales Documents blocked for billing, Review Billing Due List, Review Log of collective invoice creation and Review List Blocked (for accounting) Billing Documents). |

### Limitations

3rd version of Sales Kits (CPFH) scenario is only enabled in domestic process but not cross border scenarios.

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
> Flagged while digesting this document, not verified: Internal inconsistency in the Consignment Pick-Up Check Stock Overview step: it says goods are 'transferred again to customer's consignment stock' and expects the quantity 'posted into the consignment stock', while the Overview Table and the Post Goods Receipt step say pick-up posts goods from consignment stock directly into free stock.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Internal inconsistency in the Consignment Return Check Stock Overview step: it says goods are 'transferred from the customer's consignment stock and no longer owned by the company', while the Overview Table and the Post Goods Receipt step say the received quantity is added to the customer consignment stock.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[08-sales-order-management/test-script-sales-scheduling-agreement-with-consignment-4lz-ae-sap-s-4]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1IU_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 88,587 chars in the whole document
