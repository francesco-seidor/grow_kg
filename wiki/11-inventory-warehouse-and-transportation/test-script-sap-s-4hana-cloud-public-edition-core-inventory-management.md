---
id: 11-inventory-warehouse-and-transportation/test-script-sap-s-4hana-cloud-public-edition-core-inventory-management
title: Test Script SAP S/4HANA Cloud Public Edition - Core Inventory Management (BMC_AE) (BMC_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition 2608 (AE) test script for core inventory management: goods receipt, scrapping, stock transfers, stock analytics, reservations."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/core-inventory-management]
aliases: [BMC_S4CLD2608_BPD_EN_AE]
keywords: [Core Inventory Management, inventory management, test prerequisites, goods receipt, stock scrapping, stock blocking, stock transfers, stock overview, slow moving materials, dead stock analysis]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BMC_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1285
topic: 11-inventory-warehouse-and-transportation/core-inventory-management
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script SAP S/4HANA Cloud Public Edition - Core Inventory Management (BMC_AE) (BMC_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BMC_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Core Inventory Management** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Core Inventory Management (BMC_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232862163)

[2 Prerequisites 4](#_Toc232862164)

[2.1 System Access 4](#_Toc232862165)

[2.2 Roles 4](#_Toc232862166)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232862167)

[2.4 Business Conditions 6](#_Toc232862168)

[2.5 Preliminary Steps 6](#_Toc232862169)

[2.5.1 Open New MM Period 6](#_Toc232862170)

[2.5.2 Initialize Material Stock 6](#_Toc232862171)

[3 Overview Table 9](#_Toc232862172)

[4 Test Procedures 11](#_Toc232862173)

[4.1 Post Goods Receipt Without Reference 11](#_Toc232862174)

[4.2 Customer Returns Scrapping: Goods Issue to CO-PA 12](#_Toc232862175)

[4.3 General Stock Scrapping: Goods Issue to Cost Center 14](#_Toc232862176)

[4.4 Block Material – Stock Transfer Unrestricted to Blocked 15](#_Toc232862177)

[4.5 Unblock Material – Stock Transfer Blocked to Unrestricted 16](#_Toc232862178)

[4.6 Unblock Material – Stock Transfer Blocked to Quality Inspection Stock 17](#_Toc232862179)

[4.7 One Step Stock Transfer 18](#_Toc232862180)

[4.8 Two Steps Stock Transfer (Remove from Storage Location) 19](#_Toc232862181)

[4.9 Two Steps Stock Transfer (Place to Storage Location) 20](#_Toc232862182)

[4.10 Stock Overview - Single Material 21](#_Toc232862183)

[4.11 Stock Overview - Multiple Materials 22](#_Toc232862184)

[4.12 Material Documents Overview 23](#_Toc232862185)

[4.13 Slow or Non-Moving Materials 24](#_Toc232862186)

[4.14 Dead Stock Analysis 25](#_Toc232862187)

[4.15 Manage Manual Reservations 26](#_Toc232862188)

[4.16 Manage Reservation Items 28](#_Toc232862189)

[4.17 Goods Movement Analysis (Optional) 29](#_Toc232862190)

[4.18 Analyze Stock in Date Range (Optional) 31](#_Toc232862191)

[4.19 Overview Inventory Processing (Optional) 33](#_Toc232862192)

[4.20 Overview Inventory Management (Optional) 34](#_Toc232862193)

## Purpose

Overview

This scope item covers core inventory management processes, including the following processes: Post Goods Receipt without Reference, scrapping, block stock, unblock stock, one step stock transfer, two steps stock transfer, stock overview, Slow or Non-Moving Materials, Dead Stock Analysis, Goods Movement Analysis, and Material Document Overview.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

|  |
| --- |
| Caution Testing in a 3-System LandscapeIn a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version (see the following [link](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/TestScripts/BMC_S4CLD2602_BPD_EN_AE.docx) ). |

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
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure. If you have installed an SAP Best Practices baseline package, you can use the following baseline package sample data:

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Storage Location | 331B | Std. storage 2 |  |
| Storage Location | 331C | Raw mat. stoloc. |  |
| Storage Location | 331R | Storage Location Returns |  |
| Company Code | 3310 | Company Code 3310 |  |
| Material | TG11 | Trading Good for Reg. Trading (MRP planning) | See sections [Business Conditions](#unique_6) [page ] 6 and Preliminary Steps. |
| Material | TG21 | Trad.Good 21,Reorder Point,Batch-FIFO | For managing manual reservation. |

For more information on creating these master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Business Condition | Comment |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | The material TG11 and TG21 are available in stock in considerable quantity.Recommended Quantity: 100You have completed the step described in BNZ master data script. Posting Period is up to date. |

|  |
| --- |
| Note To run through this scope item, the materials must be available in stock. You can create stock using either Manage Stock (F1062) or Transfer Stock (F1061) app.For details about how to build up stock, refer to [Initialize Material Stock](#unique_7) [page ] 6. |

### Preliminary Steps

#### Open New MM Period

External Process

For this activity, run the following step from the Create New Open MM Posting Period - MDS (BNZ) to close MM period and open new posting period:

Closing MM Period and Opening New Posting Period

#### Initialize Material Stock

Purpose

In a real business case, the materials are usually purchased from external suppliers. This process step shows you how to post initial stock directly to the storage locations.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Stock (F1062). | The Manage Stock screen displays. |  |
| 3 | Input Material | Make the following entry and press Enter:Material: TG11Plant: Plant 1 AE (3310) |  |  |
| 4 | Select Stock | Choose the icon beside the stock that you want to add initial stock, for example:Storage Location: 331RUnrestricted-Use Stock | The Manage Stock dialog box opens. The Storage Location, Stock Type and Current Quantity display according to your entries in previous steps. |  |
| 5 | Add Initial Stock | Make the following entries and choose Post:Stock Change: Initial EntryQuantity: Enter a number, for example, 100Document Date: <Today>Posting Date: <Today> | The system displays Material document XXX created. The stock has been added. |  |
| 6 | Input Material | Make the following entries and press Enter:Material: TG21Batch: Choose any existing batch number, for example 0000000010Plant: Plant 1 AE (3310) |  |  |
| 7 | Select Stock | Choose the icon beside the stock that you want to add initial stock, for example:Storage Location: 331AUnrestricted-Use StockNote If there is no stock existing in the Storage Location where you want to add stock, you may choose Add Storage Location, for example:Storage Location: 331BAnd then choose the icon beside the stock that you want to add initial stock:Unrestricted-Use Stock | The Manage Stock dialog box opens. The Storage Location, Stock Type and Current Quantity display according to your entries in previous steps. |  |
| 8 | Add Initial Stock | Make the following entries and choose Post:Stock Change: Initial EntryQuantity: Enter a number, for example, 100Document Date: <Today>Posting Date: <Today> | The system displays the following message. The stock has been added.1 document has been created: Material Document XXXXXXXXXX/20XX |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Post Goods Receipt Without Reference](#unique_10) [page ] 11 | Warehouse Clerk | Post Goods Receipt without Reference (F3244) | The Post Goods Receipt Without Reference screen displays. |
| [Customer Returns Scrapping: Goods Issue to CO-PA](#unique_11) [page ] 12 | Inventory Manager | Post Goods Movement (MIGO) | The Goods Movement screen displays. |
| [General Stock Scrapping: Goods Issue to Cost Center](#unique_12) [page ] 14 | Inventory Manager | Manage Stock (F1062) | The Manage Stocks screen displays. |
| [Block Material – Stock Transfer Unrestricted to Blocked](#unique_13) [page ] 15 | Warehouse Clerk | Transfer Stock - In-Plant (F1061) | The Transfer stock screen displays. |
| [Unblock Material – Stock Transfer Blocked to Unrestricted](#unique_14) [page ] 16 | Warehouse Clerk | Transfer Stock - In-Plant (F1061) | The Transfer stock screen displays. |
| [Unblock Material – Stock Transfer Blocked to Quality Inspection Stock](#unique_15) [page ] 17 | Warehouse Clerk | Transfer Stock - In-Plant (F1061) | The Transfer Stock – In-Plant screen displays. |
| [One Step Stock Transfer](#unique_16) [page ] 18 | Warehouse Clerk | Transfer Stock - In-Plant (F1061) | The Transfer Stock screen displays. |
| [Two Steps Stock Transfer (Remove from Storage Location)](#unique_17) [page ] 19 | Warehouse Clerk | Transfer Stock - In-Plant (F1061) | The Transfer Stock screen displays. |
| [Two Steps Stock Transfer (Place to Storage Location)](#unique_18) [page ] 20 | Warehouse Clerk | Transfer Stock - In-Plant (F1061) | The Transfer Stock screen displays. |
| [Stock Overview - Single Material](#unique_19) [page ] 21 | Warehouse Clerk | Stock - Single Material (F1076) | The Stock – Single Material screen appears. |
| [Stock Overview - Multiple Materials](#unique_20) [page ] 22 | Inventory Manager | Stock - Multiple Materials (F1595) | The Stock - Multiple Materials screen displays. |
| [Material Documents Overview](#unique_21) [page ] 23 | Warehouse Clerk | Material Documents Overview (F1077) | The Material Documents Overview displays. |
| [Slow or Non-Moving Materials](#unique_22) [page ] 24 | Inventory Manager | Slow or Non-Moving Materials (F2137) | The Slow or Non-Moving Materials screen displays. |
| [Dead Stock Analysis](#unique_23) [page ] 25 | Inventory Manager | Dead Stock Analysis (F2899) | The Dead Stock Analysis screen displays. |
| [Manage Manual Reservations](#unique_24) [page ] 26 | Warehouse Clerk | Manage Manual Reservations (F4839) | The Manage Manual Reservations screen displays. |
| [Manage Reservation Items](#unique_25) [page ] 28 | Warehouse Clerk | Manage Reservation Items (F5601) | The Manage Reservation Items screen displays. |
| [Goods Movement Analysis (Optional)](#unique_26) [page ] 29 | Inventory Manager | Goods Movement Analysis - (Obsolete) (F2912) | The Prompts screen displays. |
| [Analyze Stock in Date Range (Optional)](#unique_27) [page ] 31 | Inventory Manager | Analyze Stock in Date Range (F6185) | The Analyze Stock in Date Range screen displays. |
| [Overview Inventory Processing (Optional)](#unique_28) [page ] 33 | Warehouse Clerk | Overview Inventory Processing (F2416) | The Overview Inventory Processing screen displays. |
| [Overview Inventory Management (Optional)](#unique_29) [page ] 34 | Inventory Manager | Overview Inventory Management (F2769) | The Overview Inventory Management screen displays. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Post Goods Receipt Without Reference

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post goods receipt without reference.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Receipt without Reference (F3244). | The Post Goods Receipt Without Reference screen displays. |  |
| 3 | Enter Material | Enter the following data and choose Enter.Material: TG11 |  |  |
| 4 | Enter Quantity | Enter the quantity you want to deliver:Quantity / Unit: <x PC> |  |  |
| 5 | Enter Plant | Enter the plant.Plant: Plant 1 AE3310 |  |  |
| 6 | Enter Storage Location | Enter the storage location where you want to receive the material.Storage Location:Std. storage 1 331A |  |  |
| 7 | Enter Stock Type | Enter the stock type from dropdown list.Stock Type: Unrestricted-Use |  |  |
| 8 | Enter Supplier | Choose the line of item you are editing, on the next screen enter the Supplier you want to use.Supplier: 33300001Choose Apply. | The Item Details screen displays. |  |
| 9 | Post Goods Receipt | Choose Post. | The system displays a message 1 material document(s) posted: xxx.You can check the material document using the link provided in the message. |  |

### Customer Returns Scrapping: Goods Issue to CO-PA

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Materials must be scrapped as part of production or for other reasons. Therefore, the goods movement financial posting is done via COPA. This process step shows you how to post goods issue.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Goods Movement screen displays. |  |
| 3 | Screen Settings | In the upper area, enter the following data and choose Enter:First Box: Goods IssueSecond Box: OtherMovement Type: 551In the General tab of Header Data section, enter the following:Material Slip: material slip | Entries are made. |  |
| 4 | Enter Material Data | Enter the following data and choose Enter:Material: TG11 | Entries are made. |  |
| 5 | Enter Quantity | Enter the following data on the Quantity tab and choose Enter:Quantity: Qty in Unit of Entry |  |  |
| 6 | Enter Organization Data | Enter the following data on the Where tab and choose Enter:Movement Type: 551Plant: 3310Storage Location: 331RReason for Movement: 0001Checkbox Item OK: select |  |  |
| 7 | Maintain Profitability Segment | Enter the following data on the Account Assignment tab and choose Enter:Cost Center: 33101202To enter the assignment to a profitability segment, on the Account Assignment tab, choose Profit. Segment.Note To ensure the consistency of the profit center derivation and posting, the cost center and the profitability segment should be assigned to the same profit center.On the Assignment to a Profitability Segment screen , choose Derivation and Continue. |  |  |
| 8 | Post Goods Issue | Choose Post.Note Stock needs to be available on storage location 331R (returns). For details about how to post stock to 331R, refer to [Initialize Material Stock](#unique_7) [page ] 6. | The goods are removed from stock with quantity and value. The goods value is posted to the account and to CO-PA. |  |

### General Stock Scrapping: Goods Issue to Cost Center

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Materials are consumed to the cost center as part of the production or for MRO. Therefore, the goods movement financial posting is done via the cost center. This process step shows you how to post goods movement via cost center.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Stock (F1062). | The Manage Stock screen displays. |  |
| 3 | Open Stock Overview | Make the following entries:Plant: 3310Material: TG11 | Entries are made. |  |
| 4 | Select stock | Select the icon beside the stock that you want to scrap. | A dialog box opens. The Storage Location, Stock Type, and Quantity display according to your entries in the previous steps. |  |
| 5 | Scrap Items | Make the following entries:Stock Change: ScrappingQuantity: x PCCost Center: Such as R&DReason Code: Material Damage | Entries are made. |  |
| 6 | Goods Issue | Choose Post. | The system displays Material document XXX created. The stock has been scrapped. |  |

### Block Material – Stock Transfer Unrestricted to Blocked

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Materials must be blocked from further usage. This means that the stock couldn’t be used for logistic purposes and it’s excluded in MRP calculations. For example, the material needs to be reworked. This process step shows you how to exclude the goods stock from MRP calculations.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Transfer Stock - In-Plant (F1061). | The Transfer Stock - In-Plant screen displays. |  |
| 3 | Open Stock Overview | Enter the following data in the appropriate fields:Plant: 3310Material: TG11 | Entries are made. |  |
| 4 | Select Transfer from Stock | Choose the icon beside the Unrestricted-Use Stock that you want to transfer from. | The icons change. |  |
| 5 | Select Transfer to Stock | Choose the icon beside the Blocked Stock that you want to transfer to. | A dialog box opens. Storage Locations and Stock Types are selected according to your entries in the previous steps. |  |
| 6 | Transfer Stock | Enter the quantity that you want to transfer:Quantity: x PC |  |  |
| 7 | Post | Choose Post. | The system displays a message Material document xxx posted.The goods stock status is switched from Unrestricted to Blocked. Goods stock is excluded from MRP calculations. |  |

### Unblock Material – Stock Transfer Blocked to Unrestricted

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Materials must be unblocked for upcoming usage. This means that the stock could be used for any logistic purpose and it is included in MRP calculations again. This process step shows you how to include goods stock in MRP calculations.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Transfer Stock - In-Plant (F1061). | The Transfer Stock - In-Plant screen displays. |  |
| 3 | Open Stock Overview | Enter the following data in the appropriate fields:Plant: 3310Material: TG11 |  |  |
| 4 | Select Transfer from Stock | Choose the icon beside the Blocked Stock that you want to transfer from. | The icons change. |  |
| 5 | Select Transfer to Stock | Choose the icon beside the Unrestricted-Use Stock that you want to transfer to. | A dialog box opens. Storage Locations and Stock Types are selected according to your entries in the previous steps. |  |
| 6 | Transfer Stock | Enter the quantity that you want to transfer:Quantity: x PC |  |  |
| 7 | Post | Choose Post. | The system displays a message Material document xxx posted.The goods stock status is switched from Blocked to Unrestricted. Goods stock is included in MRP calculations. |  |

### Unblock Material – Stock Transfer Blocked to Quality Inspection Stock

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Materials must be unblocked for upcoming usage, for example, for a return delivery. This process step shows you how to unblock materials for upcoming usage.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. |  |  |
| 2 | Access the App | Open Transfer Stock - In-Plant (F1061). | The Transfer Stock - In-Plant screen displays. |  |
| 3 | Open Stock Overview | Enter the following data in the appropriate fields:Plant: 3310Material: TG11 |  |  |
| 4 | Select Transfer from Stock | Choose the icon beside the Blocked Stock that you want to transfer from. | The icons change. |  |
| 5 | Select Transfer to Stock | Choose the icon beside the Stock in Quality Inspection that you want to transfer to. | A dialog box opens. Storage Locations and Stock Types are selected according to your entries in the previous steps. |  |
| 6 | Transfer Stock | Enter the quantity that you want to transfer:Quantity: x PC |  |  |
| 7 | Post | Choose Post. | The system displays a message Material document xxx posted.The goods stock status is switched from Blocked to Quality Inspection Stock. Goods stock is included in MRP calculations. |  |

### One Step Stock Transfer

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to transfer stock from one storage location to another.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Transfer Stock - In-Plant (F1061). | The Transfer Stock - In-Plant screen displays. |  |
| 3 | Open Stock Overview | Enter the following data in the appropriate fields:Plant: 3310Material: TG11 | Entries are made. |  |
| 4 | Select Transfer from Stock | Choose the icon beside the Unrestricted-Use Stock in the storage location that you want to transfer from, for example, 331A. | The icons change. |  |
| 5 | Select Transfer to Stock | Choose the icon beside the Unrestricted-Use Stock in the storage location that you want to transfer to, for example, 331R. | A dialog box opens. Storage Locations and Stock Types are selected according to your entries in the previous steps. |  |
| 6 | Transfer Stock | Enter the quantity that you want to transfer:Quantity: x PC |  |  |
| 7 | Post | Choose Post. | The system displays a message Material document xxx posted.The stock is transferred from one storage location to another. |  |

### Two Steps Stock Transfer (Remove from Storage Location)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to transfer stock from Unrestricted-Use Stock to Stock Transfer (Storage Location).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Transfer Stock - In-Plant (F1061). | The Transfer Stock - In-Plant screen displays. |  |
| 3 | Open Stock Overview | Enter the following data in the appropriate fields:Plant: 3310Material: TG11 | Entries are made. |  |
| 4 | Select Transfer from Stock | Choose the icon beside the column Unrestricted-Use Stock in the storage location that you want to transfer from, for example, 331A. | The icons change. |  |
| 5 | Select Transfer to Stock | Choose the icon beside the column Stock Transfer (Storage Location) in the storage location that you want to transfer to, for example, 331R. | A dialog box opens. Storage Locations and Stock Types are selected according to your entries in the previous steps. |  |
| 6 | Transfer Stock | Enter the quantity that you want to transfer:Quantity: x PC |  |  |
| 7 | Post | Choose Post. | The system displays a message: Material document xxx posted.The stock is transferred from Unrestricted-Use Stock in 331A to Stock Transfer (Storage Location) in 331R. |  |

### Two Steps Stock Transfer (Place to Storage Location)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to transfer stock from Stock Transfer (Storage Location) to Unrestricted-Use Stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Transfer Stock - In-Plant (F1061). | The Transfer Stock - In-Plant screen displays. |  |
| 3 | Open Stock Overview | Enter the following data in the appropriate fields:Plant: 3310Material: TG11 | Entries are made. |  |
| 4 | Select Transfer from Stock | Choose the icon beside the column Stock Transfer (Storage Location) in the storage location that you want to transfer from, for example 331R. | The icons change. |  |
| 5 | Select Transfer to Stock | Choose the icon beside the column Unrestricted-Use Stock in the storage location that you want to transfer to, for example 331R. | A dialog box opens. Storage Locations and Stock Types are selected according to your entries in the previous steps. |  |
| 6 | Transfer Stock | Enter the quantity that you want to transfer:Quantity: x PC |  |  |
| 7 | Post | Choose Post. | The system displays a message: Material document xxx posted.The stock is transferred from Stock Transfer (Storage Location) to Unrestricted-Use Stock. |  |

### Stock Overview - Single Material

Purpose

This process step shows you how to display material stock in the storage locations of a plant.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. |  |  |
| 2 | Access the App | Open Stock - Single Material (F1076). | The Stock Single Material screen displays. |  |
| 3 | Enter Material | Make the following entries:Material: TG11Press Enter. | The stock overview for the material shows. |  |

### Stock Overview - Multiple Materials

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to get an overview of your material stocks. You can review your stocks by the plants and storage locations for which you are responsible.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Stock - Multiple Materials (F1595). | The Stock - Multiple Materials screen displays. |  |
| 3 | Set Filters for Background Job | You can schedule a background job to export inventory analysis results. The exported result will be based on the following filters and settings.Make the following entries, and choose Go:Plant: 3310You can also choose Adapt Filters to show more filter options. | The necessary filters are set. |  |
| 4 | Schedule Report | From the upper-right corner of the main page, choose Schedule Export, and then make the following entries in the pop-up dialog:Job Name: <job name> for example: Test for Stock Multiple MaterialsColumns: keep default valuesChoose Schedule. | Export of inventory analytics was successfully initiated. |  |
| 5 | Check Job Details | Choose the link Display application job results in the Success dialog box. | On the Job Results screen, the job which is created in the previous step has Job Status as Finished. |  |
| 6 | Download Export Job Results (Optional) | Once the export job is completed, the job details are displayed and available to be downloaded in Microsoft Excel format.In the Attachments section, you can choose the file link Material Stock.xlsx to download the result as an Excel file.Note If you have scheduled more than one export job and want to view job results altogether, go to the app Display Inventory Analytics Job Results (F7504).Then set filters, for example, Job Created At: Today. Choose Go. Then click into each line of job to export Excel files. | The result of Stock-Multiple Materials can be downloaded to local disk for your further analysis. |  |

### Material Documents Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows how to find material documents by using Material Documents Overview.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Material Documents Overview (F1077). | The Material Documents Overview screen displays. |  |
| 3 | Search for Material Document | Search material documents using different criteria. Choose Adapt Filters and all basic filters display. Enter the entries accordingly, and then choose Go.For example:Stock Change: AllMaterial: TG11Choose the row of a certain material document to view details. | The relevant Material Document items show.Note If you want to reverse goods movement, you can choose Reverse at the top of the screen. You can view the corresponding movement type and quantity in the Items section. You can also view the Material Document and Accounting Document in the Process Flow section. The Process Flow section shows the goods movement process in a flow chart. |  |

### Slow or Non-Moving Materials

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to offer a quick overview of materials that have not seen any consumption posting in a specified number of days.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Slow or Non-Moving Materials (F2137). | The Slow or Non-Moving Materials screen displays. |  |
| 3 | Search Slow or Non-Moving Materials | All basic filters display.Make the following entries:Days with low consumption: 90 daysNote If you cannot get the filtered result, try to lower number of the days from the default 90 to 30 days. The app only shows the stocks that exist at the beginning of the analysis time period (reference date - Days with low Consumption).Reference date: For example, TodayDisplay currency: AEDInventory consumption Group: 000 (standard consumption group)Enter any other entries needed accordingly, and then choose Go. | The search results show the details with the respective filter criteria. It lists the material stocks and values per plant and storage location on a specified reference day. It also states the last posting date and the last consumption date before the reference date along with the number of days passed between the last posting and the reference date.Any postings made after the reference date are not considered in the app. Any materials with zero stock (per plant/storage location) on the reference date are excluded from the list.You can choose Adapt Filters to select filters. |  |

### Dead Stock Analysis

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to offer a quick overview of materials that have not seen any consumption or posting in a specified number of days.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Dead Stock Analysis (F2899). | The Dead Stock Analysis screen displays. |  |
| 3 | Search for Dead Stock Materials | All basic filters are displayed.Analytics Start Date, Analytics End Date, and Display Currency are mandatory search fields.Enter Analytics Start Date, Analytics End Date, and any other entries needed accordingly. Then choose Go. | The search results show the details with the respective filter criteria. It lists the material stocks and values per plant and storage location as well as the stock value and quantity on the start and end date of the period according to the search criteria. It also states the Date of Last Consumption/Posting as well as the Days without Consumption/Posting.Any postings made after the reference date are not considered in the app. Any materials with zero stock (per plant/storage location) on the reference date are excluded from the list.You can choose Adapt Filters to select filters. |  |

### Manage Manual Reservations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create reservation manually. You may also review, copy and delete the documents with the Manage Manual Reservations (F4839) app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Manual Reservations (F4839). | The Manage Manual Reservations screen displays. |  |
| 3 | Create Reservation | Choose Create Reservation, and make the following entries in the Create dialog box:Movement Type: 201Plant: 3310Base Date: keep default value, for example, <Today>Choose Create. | The draft Reservation XXXXX displays. |  |
| 4 | Input General Information | Make the following entries in the appropriate fields on the General Information tab:Cost Center: 33101101Note You may also choose Discard Draft if you don’t want to keep the information you just input. | Entries are made. |  |
| 5 | Input Items | Make the following entries in the appropriate fields on the Reservation Item tab:Material: TG11Quantity: 10 PCPlant: 3310Storage Location: 331AMovement Allowed: keep default valueChoose Create. | Reservation XXXX is created.Please note down the document number. |  |
| 6 | Search Reservation | Choose Back and make the following entry on the Manage Manual Reservations screen:Reservation: Enter the reservation number you just createdChoose Go. | Reservation XXXX displays. |  |
| 7 | Copy Reservation | Select the checkbox of the reservation created in step 5.Then choose Copy Reservation.In the Copy dialog box, keep all the default information and choose Copy. | The draft Reservation XXXXX displays. |  |
| 8 | Add Reservation Item | Enter the following data in the appropriate fields on the Reservation Item tab:Material: TG21Quantity: 10 PCPlant: 3310Storage Location: 331ABatch: Choose an existing batchMovement Allowed: keep default valueChoose Create. | Reservation XXXX is created.Please note down the document number. |  |
| 9 | Delete Reservation | Choose Back and make the following entry on the Manage Manual Reservations screen:Reservation: Enter the first reservation number you created in step 5Choose Go.Select the checkbox of the reservation and choose Delete Reservation.In the Delete dialog box, choose Delete Reservation. | Reservation XXXX is deleted. |  |

### Manage Reservation Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post reservation manually.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Reservation Items (F5601). | The Manage Reservation Items screen displays. |  |
| 3 | Search Reservation | On the Manage Reservation Items screen, make the following entry:Reservation: The reservation number in step 8 in [Manage Manual Reservations](#unique_24) [page ] 26Choose Go. | Reservation XXXX displays. |  |
| 4 | Create Goods Movement | Select all the items in the reservation, and choose Create Goods Movement | The draft screen displays. |  |
| 5 | Post Goods Movements | Verify the data in each of the reservation items, and choose Post Goods Issue. | Material document item XXXX for material document XXXXXXXXXX is created. |  |
| 6 | Check Reservation Status | Choose Back and on the Manage Reservation Items screen and make the following entry:Reservation: The reservation number you just posted in step 5Choose Go.Check the Completed Items column. | Completed Items status is Yes. |  |

### Goods Movement Analysis (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to analyze goods movement in your company to identify opportunities for process improvement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Goods Movement Analysis (MMIM_FPM_OVP_GDSMVT (MMIM_FPM_OVP_GDSMVT)). | The Goods Movement Analysis screen displays. |  |
| 3 | Set Search Parameter | Make the following settings and choose Go.Posting Date: Set your own posting date or keep default valueNote Please choose fiscal year according to the material documents created in the previous steps. | Data Analysis tab displays values of the physical inventory documents. |  |
| 4 | Select Measures | In the left Navigation Panel, go to the Dimensions section, then choose arrow beside Measures to expand the options.Click the + button beside the field you want to add to display, for example: Movement Count.Note To avoid updating the analysis results lively, in the Navigation Panel, choose the Settings arrow besides Dimensions and select Defer Layout Update from the dropdown list. This is useful when processing large amount of data. | The Column Movement Count is added to the right-side data analysis result. |  |
| 5 | Remove Measures | Click the - button beside the field that already selected as measures and need to be removed, for example, Issue Amount. | The Issue Amount column is removed from the right-side data analysis result. |  |
| 6 | Add Rows | In the left Navigation Panel, drag the dimension field that needs to be added and drop it in Rows section, or click the button <!-- image omitted: unnamed -->(Add Field to Row Axis) beside the dimension field.For example, drag Company Code and drop it in the section of Rows. | The Company Code row is added to the right-side data analysis result. |  |
| 7 | Switch the Sequence of Dimension in Row | In the Rows section, drag and drop dimension field to adjust the sequence.For example, drag and drop Company Code above Plant. | The sequence of row dimension is adjusted. |  |
| 8 | Remove Rows | Drag the dimension field, for example, Company Code, from the Rows section and drop it back to the dimension section, or click the button <!-- image omitted: unnamed -->(Remove Field from Row Axis) beside the dimension field. | The Company Code row is removed from the right-side data analysis display. |  |
| 9 | Change Layout to Bar Chart | On the right side, choose the tab Graphical Display beside Data Analysis. | The layout of analysis result is changed to bar chart. |  |
| 10 | Personalize Chart Settings | Choose the Settings button on the upper-right corner of the Graphical Display screen. | You can change the chart type to, for example a line chart or stacked bar chart and determine whether to show Legend or Tooltip or not. |  |

### Analyze Stock in Date Range (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to analyze and monitor goods movement postings for one or more materials in a defined date range.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Analyze Stock in Date Range (F6185). | The Analyze Stock in Date Range screen displays. |  |
| 3 | Set Search Criteria | Display stock using different criteria. Make the following entries, and choose Go.For example:Display Currency: AEDAnalytics Date Range: for example, <Last 30 Days>Plant: 3310You can also choose Adapt Filters to show more filter options. | Stock values and quantities of the filtered-out materials display on the main page with detailed information referring to the analytical start and end date respectively. |  |
| 4 | Check Analytical Chart | In the middle of the screen, a bar chart displays values by start and end date.From the upper right corner of the chart, select View By and choose dimensions according to your needs. You can change the chart type as well. | Stock values (start period and end period) per plant are displayed and can be further adapted by using filters or settings according to your analytical needs. |  |
| 5 | Adjust Materials Table Settings | From the upper right corner of the Materials table, choose the Settings button.Select additional columns to display if needed, for example, Batch, Stock Type and Special Stock Type. | The table is adapted according to the newly selected field. |  |
| 6 | Show Posting Details | By selecting a line item on the main page and clicking the rightmost Details button, you can navigate directly to the detail page to see further information regarding the material posting history.Note In the Documents section of the detailed page, the stock value aggregates values from each accounting document, not considering stock identifying details. Therefore, the total value can be different from the logistics calculations on the main page, especially when stock identifying fields (except material and plant) are enabled or filtered on the main page.For more information, see [Details for Calculating and Displaying Values](https://help.sap.com/docs/SAP_S4HANA_CLOUD/32da8359c8ee4e8b8e8c5e15cacba5aa/d5980b96e6f84d58b1124c4c81f7952d.html). | A detailed page containing material postings displays on the right side. |  |
| 7 | Schedule Export of Material Stock and Postings (Optional) | You can schedule a background job to export inventory analysis results. The exported result will be based on the filters and settings set above, for example, Currency, Analytic Date Range, Plant, and so on.From the upper right corner of the App's main page, click the button Schedule Export, and then make the following entries in the pop-up:Job Name: <enter a job name>Export Selection Type: Material Stock and PostingsClick on Schedule button, then choose Display application job results. | Export job has been scheduled. Job status is In Process. |  |
| 8 | Download Export Job Results (Optional) | Once the export job is completed, the job details are displayed and available to be downloaded in Microsoft Excel format.Note The Attachments section can contain three types of Microsoft Excels:Material postings with stock (based on the Export Selection Type setting)Material postings without stockMaterial stock (based on the Export Selection Type setting)Note If you have scheduled more than one export job and want to view job results altogether, go to the App Display Inventory Analytics Job Results (F7504).Then set filters, for example, Job Created At: Today. Choose Go. Then click into each line of job to export Excel files. | Material Posting with Stock and Material Stock can be downloaded from the Attachments section. |  |

### Overview Inventory Processing (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

By following the steps below, you can test if the Overview Inventory Processing (F2416) app is running correctly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open the Overview Inventory Processing (F2416) app. | The Overview Inventory Processing screen displays. |  |
| 3 | Set Search Criteria | Make the following entries, and choose Go.For example:Plant: 3310You can also choose Adapt Filters to show more filter options.Check the following cards are shown including content (exact names may vary):Recent Inventory CountsWarehouse Throughput HistoryRecent Material DocumentsOverdue Materials - Stock in TransitMonitor Purchase Order ItemsOverdue Materials-GR Blocked StockInbound Delivery ListOutbound Delivery List | The filtered values from the Overview Inventory Processing (F2416) app have been applied in the corresponding card. |  |
| 4 | Hide Cards | Choose the icon at the top right of the page and select Manage Cards.Disable various cards via the checkboxes in the dialog box and choose OK.In the same way, you can add the cards again to the overview page (or simply choose Reset in the Manage Cards dialog box).In addition, you can drag and drop the cards in the Overview Inventory Processing (F2416) app. | The cards can be rearranged, hidden, and shown again. |  |
| 5 | Header Navigation to Apps | Choose the headers of these cards. | The corresponding app starts, for example: Manage Physical Inventory Documents (F0379A), Goods Movement Analysis (MMIM_FPM_OVP_GDSMVT (MMIM_FPM_OVP_GDSMVT)), Material Documents Overview (F1077), Overdue Materials (F2139), Monitor Purchase Order Items (F2358), Overdue Materials (F2347), List of Inbound Deliveries, General Delivery List. |  |
| 6 | Item Navigation to Apps | Select items from these cards. | The lines navigate to the corresponding Object Page / Display Transaction. |  |

### Overview Inventory Management (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

By following the steps below, you can test if the Overview Inventory Management (F2769) app is running correctly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open the Overview Inventory Management (F2769) app. | The Overview Inventory Management screen displays. |  |
| 3 | Set Search Criteria | Make the following entries, and choose Go.For example:Plant: 3310You can also choose Adapt Filters to show more filter options.Check that the following cards are shown including content (exact names may vary):Recent Material DocumentsWarehouse Throughput HistoryOverdue Materials- Stock in TransitOverdue Materials- GR Blocked StockMonitor Purchase Order ItemsStock Value by Stock TypeStock Value by Special Stock Type | Check if the filtered values from Overview Inventory Management have been applied in the corresponding card. |  |
| 4 | Hide Cards | Choose the user icon at the top right of the page and select Manage Cards.Disable various cards via the checkboxes in the dialog box and choose OK.In the same way, you can add the cards again to the overview page (or simply choose Reset in the Manage Cards dialog box).In addition, you can drag and drop the cards in the Overview Inventory Management (F2769) app. | The cards can be rearranged, hidden, and shown again. |  |
| 5 | Header Navigation to Apps | Choose the headers of these cards which are populated with data. | The corresponding app starts, for example: Goods Movement Analysis (MMIM_FPM_OVP_GDSMVT (MMIM_FPM_OVP_GDSMVT)), Overdue Materials - GR Blocked Stock (F2347), Overdue Materials - Stock in Transit (F2139), Monitor Purchase Order Items (F2358), Stock - Multiple Materials (F1595). |  |
| 6 | Item Navigation to Apps | Choose the items of these cards. | The lines navigate you to the corresponding Object Page / Display Transaction. |  |

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
> Flagged while digesting this document, not verified: Goods Movement Analysis is marked Obsolete in the overview table but has a test procedure with a different app ID (MMIM_FPM_OVP_GDSMVT)

> [!warning] Conflict
> Flagged while digesting this document, not verified: Customer returns scrapping uses MIGO while other scrapping uses Manage Stock; may differ from other inventory documents

## Connections
- part-of :: [[_cluster]]
- see-also :: [[11-inventory-warehouse-and-transportation/test-script-stock-transfer-with-delivery-bme-ae-sap-s-4hana-cloud-publ]]
- see-also :: [[11-inventory-warehouse-and-transportation/physical-inventory-cycle-counting-4lu-ae-test-script-sap-s-4hana-cloud]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BMC_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 59,735 chars in the whole document
