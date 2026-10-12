---
id: 15-retail-operations/test-script-inventory-management-for-distribution-centers-5fq-ae-sap-s
title: "Test Script: Inventory Management for Distribution Centers (5FQ_AE) - SAP S/4HANA Cloud Public Edition (5FQ_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 5FQ_AE: DC inventory goods receipt, scrapping, stock transfers, blocking and stock/material document display."
cluster: 15-retail-operations
tags: [kb/retail-operations, topic/dc-inventory-and-physical-inventory]
aliases: [5FQ_S4CLD2608_BPD_EN_AE]
keywords: [Inventory Management and Physical Inventory for…, inventory management, goods receipt without reference, stock scrapping, stock transfer, two-step stock transfer, blocked stock, quality inspection stock, stock overview, material document overview]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5FQ_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1085
topic: 15-retail-operations/dc-inventory-and-physical-inventory
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Inventory Management for Distribution Centers (5FQ_AE) - SAP S/4HANA Cloud Public Edition (5FQ_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5FQ_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Inventory Management and Physical Inventory for Distribution Centers** in Retail Operations. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Inventory Management for Distribution Centers (5FQ_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232856741)

[2 Prerequisites 4](#_Toc232856742)

[2.1 System Acess 4](#_Toc232856743)

[2.2 Roles 4](#_Toc232856744)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232856745)

[2.4 Business Conditions 6](#_Toc232856746)

[2.5 Preliminary Steps 7](#_Toc232856747)

[2.5.1 Set Initial Stock for Material 7](#_Toc232856748)

[3 Overview Table 9](#_Toc232856749)

[4 Test Procedures 10](#_Toc232856750)

[4.1 Post Goods Receipt Without Reference 10](#_Toc232856751)

[4.2 Scrapping of Goods: Goods Issue to Cost Center and CO-PA 11](#_Toc232856752)

[4.3 Scrapping of General Stock: Goods Issue to Cost Center 13](#_Toc232856753)

[4.4 Unrestricted Stock Transfer to Blocked Material 14](#_Toc232856754)

[4.5 Stock Transfer from Restricted to Unrestricted – Unblock Material 16](#_Toc232856755)

[4.6 Unblock Material – Stock Transfer Blocked to Quality Inspection Stock 17](#_Toc232856756)

[4.7 Stock Transfer 18](#_Toc232856757)

[4.8 Two Steps Stock Transfer (Remove from Storage Location) 19](#_Toc232856758)

[4.9 Two Steps Stock Transfer (Place to Storage Location) 20](#_Toc232856759)

[4.10 Stock Overview - Single Material 21](#_Toc232856760)

[4.11 Material Document Overview 22](#_Toc232856761)

[5 Appendix 24](#_Toc232856762)

[5.1 Process Integration 24](#_Toc232856763)

[5.1.1 Preceding Processes 24](#_Toc232856764)

## Purpose

Overview

Articles held by a retailer are known as inventory. Inventory management comprises analytical (for example, stock overview) and operational processes (for example, moving goods within a site or changing the status of the stock). In inventory management, you can keep information on the quantities and valuation of the article stock. The valuation is kept in financial accounts and is needed for legally required financial closing statements. Typically, a retailer needs both quantity and valuation information.

Two main types of activities are relevant for inventory management: first, processes where articles are physically moved (goods movements), such as goods receipts, goods issues, or transfers from one storage location to another; second, processes where the status of stock is changed, such as from unrestricted use to scrapping, or from blocked quality management to unrestricted use. Both types of activities are recorded in article documents. Posting such an article document results in quantity updates, and in some cases also leads to postings to financial accounts. For example, a movement from one storage location to another leads to a quantity update of the article for the storage location but doesn't need to be reflected in financial accounting, as the value hasn't changed.

Article documents also serve auditing purposes; every change in quantity or value is reported, as well as who executed it (including the link to the resulting financial posting).

The stock overview displays the current stock situation on different levels (for example site group, site, or storage location) and different status (for example unrestricted use, quality inspection, or in transit).

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

|  |
| --- |
| Note In the retail industry, specific terms differ from the standard terms used in other lines of business. Therefore, SAP solutions which provide business processes across multiple lines of businesses may use terms for the corresponding business objects, transactions, and user interfaces that deviate from the retail terminology. For integration and reuse reasons, the SAP S/4HANA Cloud Public Edition, retail, fashion, and vertical business business may thus include different terms that refer to the same concept. SAP intends to harmonize the terminology in the future.The following terms are used synonymously in this document:Table 1:Standard Terms in Lines of BusinessSAP S/4HANA Cloud Public Edition, retail, fashion, and vertical business businessMaterial, productArticleMaterial group, product groupMerchandise categoryPlant, locationSite (as superordinate term) - store and distribution center (DC) |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Acess

|  |  |
| --- | --- |
|  | Details |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Inventory Manager (Retail) | SAP_BR_INVENTORY_MGR_RFM | Retail Inventory Management | SAP_BR_INVENTORY_MGR_RFM |  |
| Warehouse Clerk (Retail) | SAP_BR_WAREHOUSE_CLERK_RFM | Retail Inventory Processing | SAP_BR_WAREHOUSE_CLERK_RFM |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Plant | 3350 | DC 3350 AE |  |
| Storage Location | 995A | Storage Loc. DC | Shop floor w/o lean WM |
| Storage Location | 995R | St.Loc.Return |  |
| Company Code | 3310 | Company Code 3310 |  |
| Material, single article | R_1006, R_1007 | My Best Frozen StrawberriesMy Best Frozen Raspberries | See sections Business Conditions and Preliminary Steps. |
| Material, generic article | R_1003 | ChocolateVariants;R_1003001R_1003002R_1003003R_1003004R_1003005R_1003006R_1003007R_1003008R_1003009R_1003010R_1003011R_1003012R_1003013R_1003014 | See [Business Conditions](#unique_6) [page ] 6 and [Preliminary Steps](#unique_7) [page ] 7. |
| Display | R_2007 | Chocolate Bar DisplayComponents:R_1003001R_1003002R_1003003R_1003004R_1003005R_1003006R_1003007R_1003008R_1003009R_1003010R_1003011R_1003012R_1003013R_1003014 |  |
| Sales Set | R_1052 | My Best Blond Shampoo & ConditionerComponents:R_1051 and R_1052 |  |
| Profit Center | Y3350 | Template DC |  |
| Cost Center | 3340 | Template Store |  |
| Cost Center | 3350 | Template DC |  |
| Cost Center | 3341 | Demo Store 1 |  |
| Cost Center | 3342 | Demo Store 2 |  |
| Cost Center | 3343 | Demo Store 3 |  |
| Cost Center | 3344 | Demo Store 4 |  |

### Business Conditions

Before you can test this scope item, you must have completed the following processes and fulfilled the following business conditions before you can go through this scope item:

| Scope Item ID | Business Condition |
| --- | --- |
| - | You have completed the step described in the Create New Open MM Posting Period - MDS (BNZ) master data script. Posting Period is up to date. |

### Preliminary Steps

#### Set Initial Stock for Material

Purpose

To execute this scope item, the materials must be available in stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk (Retail) |  |  |
| 2 | Access the App | Open Post Goods Movement (MIGO) app. | The action which was chosen last time is displayed. |  |
| 3 | Input Movement Type | Make the following entry and choose Enter.Executable Action in Transaction MIGO: Goods ReceiptReference Document for MIGO Transaction: Other | Goods Receipt Other-<UserName> screen displays |  |
| 4 | Enter Material | Close the header data and expand the detail data area. On the Goods Receipt Other Screen: Material tab, make the following entry and choose Enter:Material: R_1006 | Material details are provided. |  |
| 5 | Enter Quantity Data | On the Goods Receipt Other screen: Quantity tab, make the following entry and choose Enter:Qty in Unit of Entry: 100Unit of Entry: <PC> | Quantity details are provided. |  |
| 6 | Enter details under where tab | On the Goods Receipt Other screen: Where tab, make the following entries and choose Enter:Movement Type: 561 (Receipt per initial entry of stock balances into unr. use)Plant 3350Storage Location: 995A | Movement type, Plant and storage details are provided. |  |
| 7 | Save Your Entries | Choose Post. | Material document 490000XXX posted message is displayed. |  |

|  |
| --- |
| Note In case you are using a generic article R_1003, the procedure steps will be the following: |

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk (Retail). |  |  |
| 2 | Access the App | Open Post Goods Movement (MIGO) app. | The action which was chosen last time is displayed. |  |
| 3 | Input Movement Type | Make the following entry and choose Enter.Executable Action in Transaction MIGO: Goods ReceiptReference Document for MIGO Transaction: Other | Goods Receipt Other-<User Name> screen displays |  |
| 4 | Enter Material | Close the header data and expand the detail data area. On the Goods Receipt Other Screen: Material tab, make the following entry and choose Enter:Material: R_1003 | Material details are provided. |  |
| 5 | Enter details under where tab | On the Goods Receipt Other screen: Where tab, make the following entries and choose Enter:Movement Type: 561 (Receipt per initial entry of stock balances into unr. use)Plant: 3350Storage Location: 995A | Movement type, Plant and storage details are provided. |  |
| 6 | Enter Quantity Data | Between the header and the detail data a table is displayed. In the column tree display a + icon is displayed: click on this icon and the assigned characteristics and their values (in our example flavor/variety) are displayed in a matrix. In this matrix you can enter the quantities per variant:Qty in Unit of Entry: e.g. 10 per variant | Quantity details are provided |  |
| 7 | Save Your Entries | Choose Post. | Material document 490000XXX posted message is displayed |  |

Financial Postings:

| Material | Debited Accounts | G/L Accounts | Profit Center |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 13600000Inventory TradingGd | 39912000Inventory - Initial Entry SF & Finish Gds Balances | Y3350 |

## Overview Table

This scope item consists of several <choose the appropriate entity: process steps, reports, items> provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Post Goods Receipt Without Reference](#unique_10) [page ] 10 | Warehouse Clerk (Retail) | Post Goods Receipt without Reference (F3244) | The post goods receipt without reference screen is displayed. |
| [Scrapping of Goods: Goods Issue to Cost Center and CO-PA](#unique_11) [page ] 11 | Inventory Manager (Retail) | Post Goods Movement (MIGO) | The goods movement screen is displayed. |
| [Scrapping of General Stock: Goods Issue to Cost Center](#unique_12) [page ] 13 | Inventory Manager (Retail) | Manage Stock (F1062) | The manage stock screen is displayed. |
| [Unrestricted Stock Transfer to Blocked Material](#unique_13) [page ] 14 | Warehouse Clerk (Retail) | Transfer Stock - In-Plant (F1061) | The transfer stock screen is displayed. |
| [Stock Transfer from Restricted to Unrestricted – Unblock Material](#unique_14) [page ] 16 | Warehouse Clerk (Retail) | Transfer Stock - In-Plant (F1061) | The transfer stock screen is displayed. |
| [Unblock Material – Stock Transfer Blocked to Quality Inspection Stock](#unique_15) [page ] 17 | Warehouse Clerk (Retail) | Transfer Stock - In-Plant (F1061) | The transfer stock – In-plant screen is displayed. |
| [Stock Transfer](#unique_16) [page ] 18 | Warehouse Clerk (Retail) | Transfer Stock - In-Plant (F1061) | The transfer stock screen is displayed. |
| [Two Steps Stock Transfer (Remove from Storage Location)](#unique_17) [page ] 19 | Warehouse Clerk (Retail) | Transfer Stock - In-Plant (F1061) | The transfer stock screen is displayed. |
| [Two Steps Stock Transfer (Place to Storage Location)](#unique_18) [page ] 20 | Warehouse Clerk (Retail) | Transfer Stock - In-Plant (F1061) | The transfer stock screen is displayed. |
| [Stock Overview - Single Material](#unique_19) [page ] 21 | Warehouse Clerk (Retail) | Stock - Single Material (F1076) | The Stock - Single Material (F1076) screen appears. |
| [Material Document Overview](#unique_20) [page ] 22 | Warehouse Clerk (Retail) | Material Documents Overview (F1077) | The material documents overview screen is displayed, |

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

This process step you can post the receipt of goods without reference to any previous order or document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk (Retail) |  |  |
| 2 | Access the App | Open Post Goods Receipt without Reference (F3244) app. | The Post Goods Receipt without Reference (F3244) screen is displayed. |  |
| 3 | Enter Material | Enter the following data.Material: R_1006Choose Enter | Material details are provided. |  |
| 4 | Enter Parameters | Enter the quantity you want to post:Quantity: <x PC> | Parameters details are provided. |  |
| 5 | Enter Plant | Enter the plant.Plant: 3350 | Plant details are provided. |  |
| 6 | Enter Storage Location | Enter the storage location where you want to receive the material.Storage Location: Storage Loc. DC 995A | Storage location details are provided. |  |
| 7 | Enter Stock Type | Enter the stock type from dropdown list.Stock Type: Unrestricted-Use | Stock type details are provided. |  |
| 8 | Post Goods Receipt | Choose Post. | The system displays a message 1 material document(s) created: xxx.A goods movement with the movement type 501 has been created. You can check the material document using the link provided in the message. |  |

|  |
| --- |
| Note If you want to execute the post goods receipt for a generic article, you have to execute it for each variant separately. In our example (material R_1003) there exist 14 different variants. |

### Scrapping of Goods: Goods Issue to Cost Center and CO-PA

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Article must be scrapped from free available stock because the article is damaged. The relevant financial setting is posted automatically in controlling and profitability analysis (CO-PA). This process step shows you how to post goods issue.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Inventory Manager (Retail) |  |  |
| 2 | Access the App | Open Post Goods Movement (MIGO) app. | The Post Goods Movement (MIGO) screen displays. |  |
| 3 | Define Default Values | Define default values, for example,:Choose Menu→ Settings→ Default ValuesStorage location: 995AIn Plant: 3350Propose the OK Function in Future (X)Goods Issue/OthersChoose More -Movement Type: 551Choose Adopt. | Details provided. |  |
| 4 | Screen Settings | In the upper area of Post Goods Movement App, displays the following data:First Box: <Goods Issue>Second Box: <other>Movement Type: <GI Scrapping>Choose Enter |  |  |
| 5 | Enter Material Data | Choose tab Material, enter the following data:Material: R_1006Choose Enter | Material details are provided. |  |
| 6 | Enter Quantity | Enter the following data on the Quantity tab:Quantity: <Qty in Unit of Entry>Choose Enter | Quantity details are provided. |  |
| 7 | Enter Organization Data | Enter the following data on the Where tab:Movement Type: 551Plant: 3350Storage Location: 995ACheckbox Item OK: <select>Choose Enter | Organization data are provided. |  |
| 8 | Maintain Profitability Segment | Enter the following data on the Account Assignment tab:Cost Center: 3340To enter the assignment to a profitability segment, on the Account Assignment tab, choose Profit. Segment.To ensure the consistency of the profit center derivation and posting, the cost center and the profitability segment should be assigned to the same profit center.On the Assignment to a Profitability Segment screen, choose Derivation and Continue.Choose Enter | Details are provided. |  |
| 9 | Post Goods Issue | Choose Post. | The goods are removed from stock with quantity and value.The goods value is posted to the account and to CO-PA.Make note of material document created. |  |

### Scrapping of General Stock: Goods Issue to Cost Center

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to scrap a material.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager (Retail) |  |  |
| 2 | Access the App | Open Manage Stock (F1062) app. | The Manage Stock (F1062) screen is displayed. |  |
| 3 | Open Stock Overview | Make the following entries:Plant: 3350Material: R_1006 | Stock overview details are provided. |  |
| 4 | Select Stock | Select the icon beside the stock that you want to scrap. | A dialog box opens. The Storage Location, Stock Type, and Quantity display according to your entries in the previous steps. |  |
| 5 | Scrap Items | Make the following entries:Stock Change: <Scrapping>Cost Center: 3340Reason Code: <Material Damage>Quantity: <x PC> | Details provided. |  |
| 6 | Goods Issue | Choose Post. | A goods movement with the movement type 551 has been posted from unrestricted stock, a goods movement with the movement type 555 has been posted from blocked stock. You can check the material document using the link provided in the message. |  |

|  |
| --- |
| Note If you want to execute the scrap posting for a generic article, you have to execute it for each variant separately. In our example (material R_1003) there exist 14 different variants. |

### Unrestricted Stock Transfer to Blocked Material

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Materials must be blocked from further usage. This means that the stock couldn’t be used for logistic purposes, and it’s excluded in MRP calculations and other processes. For example, the material needs to be reworked. This process step shows you how to exclude the goods stock from MRP (Material Requirement Planning) calculations and from other processes.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk (Retail) |  |  |
| 2 | Access the App | Open Transfer Stock - In-Plant (F1061) app. | The Transfer Stock - In-Plant (F1061) screen displays. |  |
| 3 | Open Stock Overview | Enter the following data in the appropriate fields:Plant: 3350Material: R_1006 | Stock overview details are provided. |  |
| 4 | Select Transfer from Stock | Select the icon beside the unrestricted stock that you want to transfer from. | The icon beside the unrestricted stock is highlighted/active. When you press this icon then the other icons change. |  |
| 5 | Select Transfer to Stock | Select the icon beside the blocked stock that you want to transfer to. | A dialog box opens. Storage Locations and Stock Types are selected according to your entries in the previous steps. |  |
| 6 | Transfer Stock | Enter the quantity that you want to transfer:Quantity: x PC | Transfer stock details are provided. |  |
| 7 | Post | Choose Post. | A goods Movement with the movement type 344 has been created. You can check the material document using the link provided in the message.The goods stock status is switched from unrestricted use to blocked. Goods stock is excluded from MRP calculations. |  |

|  |
| --- |
| Note If you want to execute this posting for a generic article, you have to execute it for each variant separately. In our example (material R_1003) there exist 14 different variants. |

### Stock Transfer from Restricted to Unrestricted – Unblock Material

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Materials must be unblocked for upcoming usage. This means that the stock could be used for any logistic purpose, and it is included in MRP calculations again. This process step shows you how to include goods stock in MRP calculations.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk (Retail) |  |  |
| 2 | Access the App | Open Transfer Stock - In-Plant (F1061) app. | The Transfer Stock - In-Plant (F1061) screen displays. |  |
| 3 | Open Stock Overview | Enter the following data in the appropriate fields:Plant: 3350Material: R_1006 | Stock overview details are provided. |  |
| 4 | Select Transfer from Stock | Select the icon beside the blocked stock that you want to transfer from. | The icon beside the blocked stock is highlighted/active. When you press this icon, then the other icons change. |  |
| 5 | Select Transfer to Stock | Select the icon beside the unrestricted stock that you want to transfer to. | A dialog box opens. Storage Locations and Stock Types are selected according to your entries in the previous steps. |  |
| 6 | Transfer Stock | Enter the quantity that you want to transfer:Quantity: x PC | Details provided. |  |
| 7 | Post | Choose Post. | A goods Movement with the movement type 343 has been created. You can check the material document using the link provided in the messageThe goods stock status is switched from Blocked to Unrestricted. Goods stock is included in MRP calculations. |  |

### Unblock Material – Stock Transfer Blocked to Quality Inspection Stock

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is only necessary if you feel the blocked stock should undergo quality checked and can be moved to unrestricted stock if it’s a good stock or can be scrapped from free available stock because the article is damaged. The relevant financial setting is posted automatically in CO-PA. This step shows you how to transfer blocked stock to quality inspection stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launch Pad as a Warehouse Clerk (Retail) |  |  |
| 2 | Access the App | Open Transfer Stock - In-Plant (F1061) app. | The Transfer Stock - In-Plant (F1061) screen displays. |  |
| 3 | Open Stock Overview | Enter the following data in the appropriate fields:Plant: 3350Material: R_1006 | Stock overview details are provided. |  |
| 4 | Select Transfer from Stock | Select the icon beside the blocked stock that you want to transfer from. | The icon beside the blocked stock is highlighted/active. When you press this icon, then the other icons change. |  |
| 5 | Select Transfer to Stock | Select the icon beside the quality inspection stock that you want to transfer to. | A dialog box opens. Storage Locations and Stock Types are selected according to your entries in the previous steps. |  |
| 6 | Transfer Stock | Enter the quantity that you want to transfer:Quantity: x PC | Details provided. |  |
| 7 | Post | Choose Post. | A goods Movement with the movement type 349 has been created. You can check the material document using the link provided in the message.The goods stock status is switched from Blocked to Quality Inspection Stock. Goods stock is included in MRP calculations. |  |

### Stock Transfer

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to transfer stock from one storage location to another. Please use option “Add Storage Location” to add Storage Location 995R if the storage location is not visible.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk (Retail) |  |  |
| 2 | Access the App | Open Transfer Stock - In-Plant (F1061) app. | The Transfer Stock - In-Plant (F1061) screen is displayed. |  |
| 3 | Open Stock Overview | Enter the following data in the appropriate fields:Plant: 3350Material: R_1006Choose Enter | Stock overview details are provided. |  |
| 4 | Select Transfer from Stock | Select the icon beside the unrestricted stock in storage location that you want to transfer from, for example, 995A. | The icon beside the unrestricted stock is highlighted/active. When you press this icon, then the other icons change. |  |
| 5 | Select Transfer to Stock | Select the icon beside the unrestricted stock in storage location that you want to transfer to, for example, 995R. | A dialog box opens. Storage Locations and Stock Types are selected according to your entries in the previous steps. |  |
| 6 | Transfer Stock | Enter the quantity that you want to transfer:Quantity: x PC | Details provided. |  |
| 7 | Post | Choose Post. | A goods Movement with the movement type 311 has been created. You can check the material document using the link provided in the message.The stock is transferred from one storage location to another. |  |

### Two Steps Stock Transfer (Remove from Storage Location)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to transfer stock from unrestricted stock to Stock Transfer (Storage Location). This step can only be executed when the previous step has been executed successful.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk (Retail) |  |  |
| 2 | Access the App | Open Transfer Stock - In-Plant (F1061) app. | The Transfer Stock - In-Plant (F1061) screen is diaplayed. |  |
| 3 | Open Stock Overview | Enter the following data in the appropriate fields:Plant: 3350Material: R_1006 | Stock overview details are provided. |  |
| 4 | Select Transfer from Stock | Select the icon beside the unrestricted stock in storage location that you want to transfer from, for example, 995A. | The icons beside the other stock types of change = are highlighted/active. |  |
| 5 | Select Transfer to Stock | Select the icon right of the column Stock Transfer (Storage Location) in storage location that you want to transfer to, for example 995A. | A dialog box opens. Storage Locations and Stock Types are selected according to your entries in the previous steps. |  |
| 6 | Transfer Stock | Enter the quantity that you want to transfer:Quantity: x PC | Transfer stock details are provided. |  |
| 7 | Post | Choose Post. | A goods Movement with the movement type 313 has been created. You can check the material document using the link provided in the message.The stock is transferred from unrestricted stock in995A to Stock Transfer (Storage Location) in 995A. |  |

### Two Steps Stock Transfer (Place to Storage Location)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to transfer stock from Stock Transfer (Storage Location) to unrestricted stock. This step can only be executed, when the previous step has been executed successful.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Warehouse Clerk (Retail) |  |  |
| 2 | Access the App | Open Transfer Stock - In-Plant (F1061) app. | The Transfer Stock - In-Plant (F1061) screen is displayed. |  |
| 3 | Open Stock Overview | Enter the following data in the appropriate fields:Plant: 3350Material: R_1006 | Stock overview details are provided. |  |
| 4 | Select Transfer from Stock | Select the icon right of the column Stock Transfer (Storage Location) in storage location that you want to transfer from, for example 995A | Details provided. |  |
| 5 | Select Transfer to Stock | Select the icon beside the unrestricted stock in storage location that you want to transfer to storage location, for example 995A. | A dialog box opens. Storage Locations and Stock Types are selected according to your entries in the previous steps. |  |
| 6 | Transfer Stock | Enter the quantity that you want to transfer:Quantity: x PC | Details provided. |  |
| 7 | Post | Choose Post. | A goods Movement with the movement type 315 has been created. You can check the material document using the link provided in the message.The stock is transferred from Stock Transfer (Storage Location) to unrestricted stock. |  |

### Stock Overview - Single Material

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display material stock in the storage locations of a plant.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Warehouse Clerk (Retail) |  |  |
| 2 | Access the App | Open Stock - Single Material (F1076) app. | In tile group Warehouse Stock MonitoringThe Stock - Single Material (F1076) screen is displayed. |  |
| 3 | Enter Material | Make the following entries:Material: R_1006Choose Enter | The Stock Overview for the Material is displayed. |  |

### Material Document Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display a list of material document items and display the material document details of a selected material document item.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Warehouse Clerk (Retail) |  |  |
| 2 | Access the App | Open Material Documents Overview (F1077) app. | The Material Documents Overview (F1077) screen is displayed. |  |
| 3 | Enter Parameters | Make the following entries:Plant: 3350Material: R_1006Posting date: <Date which Posting Performed>Choose Go. | The Material Documents are listed. |  |
| 4 | Select Material Document | Choose Material Document | Material Document screen is displayed. |  |
| 5 | Check the Details | Check the details in sections (General Information, Items, Process Flow, Attachment) as required | Details are displayed. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

The following processes and conditions can proceed this process.

| Process | Business Condition |
| --- | --- |
| 5FU - Inbound Logistics for Distribution Centers | This scope item creates inbound delivery and goods receipt at distribution center. |

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
- related-to :: [[15-retail-operations/test-script-physical-inventory-for-distribution-centers-5fs-ae-sap-s-4]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5FQ_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 38,707 chars in the whole document
