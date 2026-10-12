---
id: 08-sales-order-management/test-script-sales-order-processing-for-sales-kits-31q-ae-896
title: "Test Script: Sales Order Processing for Sales Kits (31Q_AE) (31Q_S4CLD2608_BPD_EN_AE)"
description: "S/4HANA Cloud test script (scope item 31Q_AE, UAE): sales kit BOMs ERLA, LUMF, CPFH, DISH from sales order through delivery, picking, goods issue and billing."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/sales-kits-with-variant-configuration]
aliases: [31Q_S4CLD2608_BPD_EN_AE]
keywords: [Sales Kits with Variant Configuration and Their Returns, sales kits, sales bill of material, sales order processing, outbound delivery, picking, goods issue, billing documents, item categories, material master data]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/31Q_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-896
topic: 08-sales-order-management/sales-kits-with-variant-configuration
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Sales Order Processing for Sales Kits (31Q_AE) (31Q_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/31Q_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Sales Kits with Variant Configuration and Their Returns** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Sales Order Processing for Sales Kits (31Q_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232851375)

[2 Prerequisites 4](#_Toc232851376)

[2.1 System Access 4](#_Toc232851377)

[2.2 Roles 4](#_Toc232851378)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232851379)

[2.4 Preliminary Steps 7](#_Toc232851380)

[2.4.1 Manually Create Material Master Data for CPFH and DISH Scenario 7](#_Toc232851381)

[2.4.2 Manually Create Condition Records and BOM Definition 8](#_Toc232851382)

[2.4.3 Set Initial Stock for Material 10](#_Toc232851383)

[2.4.4 Create Condition Records 11](#_Toc232851384)

[3 Overview Table 12](#_Toc232851385)

[4 Test Procedures 13](#_Toc232851386)

[4.1 Create Sales Order 13](#_Toc232851387)

[4.2 Create Delivery 15](#_Toc232851388)

[4.3 Execute Picking 16](#_Toc232851389)

[4.4 Post Goods Issue 18](#_Toc232851390)

[4.5 Create Billing Document 18](#_Toc232851391)

[5 Appendix 21](#_Toc232851392)

[5.1 Process Integration 21](#_Toc232851393)

[5.1.1 Succeeding Processes 21](#_Toc232851394)

[5.2 Relevant Processes 21](#_Toc232851395)

[5.3 Statistical Price on Header for LUMF Use Case 22](#_Toc232851396)

[5.4 Scheduling Job Creation (Optional) 23](#_Toc232851397)

[5.4.1 Scheduling Job for Delivery Creation (Optional) 23](#_Toc232851398)

[5.4.2 Scheduling Job for Goods Issue Deliveries (Optional) 24](#_Toc232851399)

[5.4.3 Scheduling Job for Billing Creation (Optional) 24](#_Toc232851400)

[5.4.4 Scheduling Job for Billing Release (Optional) 25](#_Toc232851401)

[5.4.5 Scheduling Job for Billing Output (Optional) 26](#_Toc232851402)

[5.5 Overview on Possible Item Categories for BOM Main Item 27](#_Toc232851403)

[5.6 Supported Item Categories for Sales Kits 28](#_Toc232851404)

## Purpose

Overview

Companies often want to sell single products bundled into a sales kit (such as selling a PC together with monitor, keyboard, computer mouse, and so on). Sales kits are commonly used when the products that are part of the sales kit can also be sold independently as single products.

Customers want to have an easy way to use sales kits during order taking and follow up processes without a need to use production BOMs, variant configuration, or other functions that don't fit or are too complex for this use case.

There are multiple ways to process a bill of material in sales. Once you've entered a bill of material in a sales order, the system runs pricing and execution at the following levels:

- Header level (ERLA): usually used when product is assembled
- Item level (LUMF): usually used when product isn't assembled
- Pricing on header level, logistics on item level (CPFH): usually used when product isn't assembled, but the header should carry the total price
- Logistics on header level, pricing on item level (DISH): usually used for displays if the main item is inventory managed and the components carry the price

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all prerequisites to conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

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
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Master / Org. Data | Value | Master / Org. Data Details | Comments |
| --- | --- | --- | --- |
| Material | SDBOMERLAHDSDBOMLUMFHDSDBOMCPFHHDSDBOMDISHHD | SD BOM Header ERLA (with Pricing, inventory management)SD BOM Header LUMF(No pricing, no inventory)SD BOM Header CPFH(with pricing, subitems with inventory)SD BOM Header DISH (Inventory on header, subitems with pricing) |  |
| Sold-to party | 33100003 | Domestic UAE Customer 3 | You can test the scope item using another domestic customer. |
| Ship-to party | 33100003 | Domestic UAE Customer 3 |  |
| Payer | 33100003 | Customer domestic 03 |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Shipping Point | 3310 | Shipping Point 3310 |  |
| Sales organization | 3310 | Dom. Sales Org |  |
| Distribution channel | 10 | Direct Sales |  |
| Division | 00 | Product Division 00 |  |

Sales Bill of Material Structure

This overview shows the sales bill of material structure.

| Material | Level | Material Type | Quantity | Unit | Description |
| --- | --- | --- | --- | --- | --- |
| SDBOMERLAHD | BOM Header | HAWA | 1 | PC | SD BOM Header ERLA |
| SDBOMERLAIT01 | BOM Item | HAWA | 3 | PC | SD BOM ERLA Item01 |
| SDBOMERLAIT02 | BOM Item | HAWA | 5 | PC | SD BOM ERLA Item02 |

| Material | Level | Material Type | Quantity | Unit | Description |
| --- | --- | --- | --- | --- | --- |
| SDBOMLUMFHD | BOM Header | HAWA | 1 | PC | SD BOM Header LUMF |
| SDBOMLUMFIT01 | BOM Item | HAWA | 3 | PC | SD BOM LUMF Item01 |
| SDBOMLUMFIT02 | BOM Item | HAWA | 5 | PC | SD BOM LUMF Item02 |

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| BND | Create Customer Master - MDS |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BNK | Create Material BOM for Production and Sales - MDS |

### Preliminary Steps

#### Manually Create Material Master Data for CPFH and DISH Scenario

Purpose

To execute this scope item for CPFH and DISH (for cloud version) scenario, the materials must be created manually, only for ERLA & LUMF the best practice masterdata is pre-shipped by SAP. You can find general information on how to create material master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| BNF | Create Product Master of Type "Trading Good" |

|  |
| --- |
| Note The customer have to create their own material masterdata for sales kits of Type CPFH and DISH (for cloud version). In our test script we assume that they maintain it as shown in belowtable – as we refere to these descriptions throughout the script, you can also refer below comments and sample during your material master creation. |

Header level material “SDBOMCPFHHD” : all the parameters you can copy from material SDBOMLUMFHD, but please note that the only difference is the item category Group which need to be used “CPFH” in “basic” view and “Sales:General/Plant”view, also need to change the material description.

Item level material SDBOMCPFHIT01/ SDBOMCPFHIT02: create subitem material and you can refer the MDS document BNF regarding how to create Product Master of Type "Trading Good".

A special characteristic of CPFH is – that from a Financial reporting point of view cost & revenue is collected on main item level(accounting view).

Sample :

| Material | Level | Material Type | Quantity | Unit | Description |
| --- | --- | --- | --- | --- | --- |
| SDBOMCPFHHD | BOM Header | HAWA | 1 | PC | SD BOM Header CPFH |
| SDBOMCPFHIT01 | BOM Item | HAWA | 3 | PC | SD BOM CPFH Item01 |
| SDBOMCPFHIT02 | BOM Item | HAWA | 5 | PC | SD BOM CPFH Item02 |

Header level material “SDBOMDISHHD” : all the parameters you can copy from material SDBOMLUMFHD, but please note that the only difference is the item category Group which need to be used “DISH” in “basic” view and “Sales:General/Plant”view, also need to change the material description.

Item level material SDBOMDISHIT01/ SDBOMDISHIT02: create subitem material and you can refer the MDS document BNF regarding how to create Product Master of Type "Trading Good".

A special characteristic of DISH is – that from a Financial reporting point of view cost & revenue is collected on main item level(accounting view).

Sample :

| Material | Level | Material Type | Quantity | Unit | Description |
| --- | --- | --- | --- | --- | --- |
| SDBOMDISHHD | BOM Header | HAWA | 1 | PC | SD BOM Header DISH |
| SDBOMDISHIT01 | BOM Item | HAWA | 3 | PC | SD BOM DISH Item01 |
| SDBOMDISHIT02 | BOM Item | HAWA | 5 | PC | SD BOM DISH Item02 |

#### Manually Create Condition Records and BOM Definition

Purpose

In case you have finetuned the access sequence of SAP pre-shipped condition types, the relative condition records should be created accordingly. And to execute this scope item for CPFH scenario, the relevant condition records and BOM definition must be created manually, only for ERLA & LUMF the best practice pricing and BOM definition relevant masterdata is pre-shipped by SAP.

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) &(BNK):

Table 2: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BET | Create Sales Pricing Condition |
| BNK | Create Material BOM for Production and Sales |

|  |
| --- |
| Note The customer have to create their own condition records and BOM for sales kits of Type CPFH and DISH (for Cloud). In our test script we assume that they maintain it as shown in below table – as we refere to these descriptions throughout the script, you can also refer below comments and sample during your master creation. |

Regaridng the sales pricing for material SDBOMCPFHHD: in the condition type PPR0, you can directly copy the condition records from material SDBOMLUMFHD as below:

Sample:

| Material | Description | Amount | Unit | Per | UoM | Calculat.Type | ScalBseTyp |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SDBOMCPFHHD | SD BOM Header CPFH | 200 | EUR | 1 | PC | C | C |

| Material | Description | Amount | Unit | Per | UoM | Calculat.Type | ScalBseTyp |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SDBOMDISHIT01 | SD BOM DISH Item01 | 100 | EUR | 1 | PC | C | C |
| SDBOMDISHIT02 | SD BOM DISH Item02 | 100 | EUR | 1 | PC | C | C |

Regaridng the BOM definition for material SDBOMCPFHHD and SDBOMDISHIT01& SDBOMDISHIT02 (for Cloud): the BOM usage should be maintained as number #5, you can directly copy the material BOM from material SDBOMLUMFHD and add one more compent “NS0002” for non-stock scenario as below:

Sample:

| Item | ICt | Component | Component desctiption | Quantity | UoM |
| --- | --- | --- | --- | --- | --- |
| 0010 | L | SDBOMCPFHIT01 | SD BOM CPFH Item 01 | 3 | PC |
| 0020 | L | SDBOMCPFHIT02 | SD BOM CPFH Item 02 | 5 | PC |
| 0030 | N | NS002 | Non-Stock Material 02 | 3 | PC |

Regaridng the BOM definition for material SDBOMDISHHD : the BOM usage should be maintained as number #5, you can directly copy the material BOM from material SDBOMLUMFHD as below:

Sample:

| Item | ICt | Component | Component desctiption | Quantity | UoM |
| --- | --- | --- | --- | --- | --- |
| 0010 | L | SDBOMDISHIT01 | SD BOM DISH Item 01 | 3 | PC |
| 0020 | L | SDBOMDISHIT02 | SD BOM DISH Item 02 | 5 | PC |

#### Set Initial Stock for Material

Purpose

To execute this scope item, the materials must be available in stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). |  |  |
| 3 | Enter Reference Document for MIGO Transaction | At the top left of the screen, you see two drop down lists.For the first one, select Goods Receipt.For the seond one, select Other. |  |  |
| 4 | Edit Material Tab | Scroll down, and on the Material tab, make the following entry and choose Enter:Material : <Material Number> |  |  |
| 5 | Edit Quantity Tab | On the Quantity tab, make the following entry, and choose Enter:Qty in Unit of Entry: <Qty in UOM>Unit of Entry: <PC> |  |  |
| 6 | Edit Where Tab | On the Where tab, make the following entries and choose Enter:Movement Type: 561 (Receipt per initial entry of stock balances into unrestricted use)Plant: <Enter a Plant>Storage Location: <Enter a Storage Location> |  |  |
| 7 | Edit Batch Tab | On the Batch tab, make the following entry and choose Enter:Date of Manufacture: <Enter the Current Date or a Date in the Past> | Only relevant for batch relevant materials. |  |
| 8 | Save Your Entries | Click Post. |  |  |

Financial Postings

| Material | Debited Accounts | Credited Accounts |
| --- | --- | --- |
| Trading Good (HAWA) | 13600000Inventory TradingGd | 39912000Inv Init SF&amp;Fin Bal |

#### Create Condition Records

Purpose

In case you have finetuned the access sequence of SAP pre-shipped condition types, the relative condition records should be created accordingly.

You can find general information on how to create master data objects in the following MDS:

Table 2: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BET | Create Sales Pricing Condition - MDS |

## Overview Table

This scope item consists of several process steps, provided in the table below:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Sales Order](#unique_11) [page ] 13 | Internal Sales Representative | Manage Sales Orders (F1873) | The Manage Sales Orders screen displays. |
| [Create Delivery](#unique_12) [page ] 15 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) | Delivery is created. |
| [Execute Picking](#unique_13) [page ] 16 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | The delivery is picked. |
| [Post Goods Issue](#unique_14) [page ] 18 | Shipping Specialist | Change Outbound Delivery (VL02N) | The goods issue is posted. |
| [Create Billing Document](#unique_15) [page ] 18 | Billing Clerk | Create Billing Documents (F0798) | Billing is carried out. |

## Test Procedures

This section describes procedures for each process step that belongs to this scope item.

The Enterprise search function provides a central entry point for finding business objects in your company from different sources using a single search request, You can search for objects such as: Apps, fact sheets for business objects. From the data found, you can go directly to the respective apps and fact sheets to display, edit the data, or find related objects.

How to access and check a fact sheet:

● Log on to the SAP Fiori launchpad as a respective user. For example, Internal Sales Representative.

● Access the Enterprise Search Bar and choose the magnifying glass button in the upper right corner.

● The Enterprise Search bar is displayed, two filter fields appear left to the search button. Enter your Search Criteria and choose the business object type, example,: Sales or-ders from dropdown menu in 1st field, enter sales order number in 2nd field and choose Search, The sales order is listed.

● Choose the sales order number link. The system navigates to the fact sheet screen and sales order related information is integrated and summarized in one SAP Fiori page. You can get detailed data via choosing the corresponding links.

There are fact sheets available for the following objects (visible depending on the assigned role):

● Sales order

● Billing document

### Create Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a sales order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Create Sales Order | On the Manage Sales Orders screen, choose Create, then select Create Sales Orders - VA01 (VA01). |  |  |
| 4 | Enter the Order Data | On the Create Standard Order: Initial screen, make the following entries and choose Enter:Order Type: ORSales Organization: 3310Distribution Channel: 10Division:00 |  |  |
| 5 | Enter Order Details | On the Create Sales Orders: Overview screen, make the following entries:Sold to party: 33100003Ship to party: 33100003Customer Reference: <Customer Reference>Customer Reference Date: <Date>Material Number: <SDBOMERLAHD> or <SDBOMLUMFHD>Order Quantity: <Quantity>Enter the item category TAQF or TAPF manually before BOM explosion if the item is free of charge during order creation.Note If you are using SDBOMERLAHD ， SDBOMLUMFHD， or SDBOMCPFHHD,SDBOMDISHHD (for Cloud only)in testing, the sales BOM will explode and subitems will appear. Here is the difference between them:For SDBOMERLAHD, pricing and inventory managed on the main item.For SDBOMLUMFHD, pricing and inventory managed on the subitems.For SDBOMCPFHHD, pricing managed on the main item and inventory managed on the subitems.For SDBOMDISHHD, Pricing on subitems, inventory managed on main item". |  |  |
| 6 | Save Document | Choose Save. Make a note of the sales order number: __________.If you have installed Free Goods Processing in your system and you use material TG11 and customer 33100001 , the following warning may appear:Minimum quantity 1.000 PC of free goods has not been reached.To skip this warning, choose Enter. | The order is saved and the order confirmation is printed out. |  |

Printing Forms

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Search for Sales Order | Enter search terms in filter bar and choose GoExample: Enter <Sales Order Number> in the Sales Order field. | Sales order is displayed in result list. |  |
| 4 | Navigate to Sales Order Screen | Choose > on the right of the Sales Oder item and navigate to Display Standard Oders xxx: Overview screen. | The Display Standard Orders XXX: Overview screen displays. |  |
| 5 | Check Output Condition | On the Display Standard Orders xxx: Overview screen, choose Extras > Output > Header > Edit. |  |  |
| 6 | Display Print Preview | On the Display Standard Orders XXX: Output screen: select the line already created for the print output, and choose Display Document | Preview for PDF document displays. |  |

|  |
| --- |
| Note It can also be navigated to a factsheet screen in app Manage Sales Orders (F1873):On the Manage Sales Orders (Original) screen, enter search terms in filter bar and choose Go.In search result, choose your Sales Order Number and choose More Links. |

### Create Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Create Outbound Deliveries - From Sales Orders (F0869A). | The Create Outbound Deliveries - From Sales Orders (F0869A) screen displays. |  |
| 3 | Search Sales Order | Make the following entries and choose Go:Shipping point: 3310Planned Creation Date: <Delivery selection date>Sales Document: <Sales order number created previously> |  |  |
| 4 | Create Delivery | Select your sales order, and choose Create Deliveries. | Creation of a delivery is triggered |  |
| 5 | Check Details | Choose Display Log. | The Analyze Delivery Log screen displays, a delivery is created successfully with delivery number shown on tab Deliveries. |  |

With the Analyze Outbound Delivery Logs app, you can display an overview about the logs of all the deliveries, which have been created in your system. You can filter by, for example, Created By and Additional Settings. If you select the arrow on the right of each delivery log entry, you can display the exact message type, text, and also the related sales document.

### Execute Picking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The picking process involves taking goods from a storage location and staging the right quantity in a picking area where the goods are prepared for shipping. This process step shows you how to execute picking.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). | The Outbound Delivery Monitor screen displays. |  |
| 3 | Choose Picking | Choose For Picking. |  |  |
| 4 | Enter Shipping Point | Make the following entries and choose Execute.Shipping Point: 3310Only Picking without WM: X |  |  |
| 5 | Change Outbound Delivery | From Day’s Workload for Picking , select your delivery number, and choose Change Outbound Deliveries. |  |  |
| 6 | Enter Picked Quantity | Enter quantity equal to delivery Qty in field Picked Qty for picking related item(s).For SDBOMERLAHD, enter picked quantity on the main item.For SDBOMLUMFHD, enter picked quantity on the subitems.For SDBOMCPFHHD, enter picked quantity on the subitems.For SDBOMDISHHD, enter picked quantity on the main item.. |  |  |
| 7 | Enter | Choose Enter. |  |  |
| 8 | Save | Choose Save. | The delivery has been picked. |  |

### Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post a goods issue.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). | The Change Outbound Delivery (VL02N) screen displays. |  |
| 3 | Change Outbound Delivery | Make the following entries and Choose Continue.Outbound Delivery: <Delivery Number Created Previously> | The Delivery XXX Change: Overviewscreen displays. |  |
| 4 | Post Goods Issue | Choose Post Goods Issue | The goods issue is posted. |  |

### Create Billing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create and manage a billing document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Documents screen displays. |  |
| 3 | Define Billing Setting | Choose Billing Settings in the bottom bar, you can make the following settings:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: OFFAutomatically post billing documents: ONDisplay billing documents after creation: ONChoose delivery items to be billed and select quantities: OFF |  |  |
| 4 | Search for Billing Due List | In the search condition, use criteria if necessary. | Sales document displays in the result. |  |
| 5 | Select Item for Billing | Select row of SD document created previously, and choose Create Billing Documents. | The Create Billing Documents screen displays. |  |
| 6 | Maintain Billing Date | Choose billing type Invoice (F2) and maintain billing date, for example, <Current Date>, then choose OK. | The system generates an invoice for billing. |  |
| 7 | Save Billing Document | Save your entries.Make a note of the billing document number: __________. | The system generates an invoice for billing.Material: Sales Kits (HAWA)Debited Accounts: 33100003Rcvbls Domestic UAE Customer 3Credited Accounts:41910000 Billed Rev Domestic Prod22000000 Output tax (MWS)52590000 (optional) Freight Revenue/Rec.Cost Element/CO Object: None |  |
| 8 | Access the App | Open Manage Billing Documents (F2250). | The Manage Billing Documents (F2250) screen displays. |  |
| 9 | Enter Billing Number | In the Billing Document (F1901) field, enter the respective invoice number, and choose Enter. | The Invoice XXX Display: Overview of Billing Items screen displays. |  |
| 10 | Check Output Condition | On the Invoice XXX Display: Overview of Billing Items screen, choose Menu→ More→ Goto→ Header > Output . | The The Invoice XXX Display: Output screen displays. |  |
| 11 | Display Print Preview | On the Invoice xxx Display: Output view, select the line already created for the print output, and choose Display Document. | Preview for PDF document displays. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Succeeding Processes

After completing the activities in this test script, you can continue to test the following business processes:

| Process | Business Condition |
| --- | --- |
| Accounts Receivable (J59) | Posting a Customer Invoice in Accounting, and so on.Using the master data from this document, complete the following activities described in the test script:Posting a Customer Invoice in AccountingOverdue Receivables, Display Customer BalancesManage Customer Line Items |
| Sales Period End Closing Operations (BKK) (optional) | This scope item describes the collection of periodic activities such as day ending activities, or reporting.Using the master data from this document, complete all the activities described in the Test Script of the scope item:Review Incomplete SAP Digital Documents (deliveries),Review Sales Documents blocked for billingReview Log of collective invoice creation |

### Relevant Processes

If the following process are enabled in your system, you can also test these business processes for the Sales Kits material described in this test script.

| Process |
| --- |
| BD9 -Sell from Stock |
| BDA -Free of Charge Delivery |
| BDG -Sales Quotation |
| BDH-Sales Order Entry with One-Time Customer |
| BDQ-Invoice Correction Process with Debit Memo |
| BDW-Returnables Processing |
| BKJ-Sales Order Processing with Customer Down Payment |
| BKK-Sales Order Processing – SEPA Direct Debit Handling |
| BKL-Invoice Correction Process with Credit Memo |
| BKP-Customer Returns |
| BKZ-Sales Order Processing with Invoice List and Collective Billing |
| 1B6-Sales Rebate Processing |
| 1EZ-Credit Memo Processing |
| 1F1-Debit Memo Processing |
| 1IQ-Sales Inquiry |
| 1Z1-Digital Payments – Sales |
| I9I-Sales Contract Management |

### Statistical Price on Header for LUMF Use Case

From 1902 release, PCUM (Cumulation Condition) condition type can be added as statistical price on header level of a sales BOM of type LUMF in customer pricing procedures. For further information regarding Cumulated Conditions, please refer to SAP Note [844141](https://me.sap.com/notes/844141).

In order to print a billing document with the statistical price shown on the header position, of which the function is enabled by Sales Kits Variant LUMF, refer to this KBA [https://launchpad.support.sap.com/#/notes/2721635](https://launchpad.support.sap.com/#/notes/2721635).

### Scheduling Job Creation (Optional)

#### Scheduling Job for Delivery Creation (Optional)

Context

In this process step, you can define the schedule background job for creation outbound deliveries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Delivery Creation. | The Application Jobs displays.The app starts with the history of application jobs. |  |
| 3 | Create Delivery Creation Schedule | Choose New to define a new job. | The New Job view displays.Job Template should be defaulted as Schedule Delivery Creation. |  |
| 4 | Job Parameters | Define scheduling options and parameter section for batch job if necessary, then choose Check. | The system displays the notification Go Ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A delivery creation job is scheduled.The view backs to Application Jobs. |  |
| 6 | Check Delivery Creation Job Log | In the view Application Jobs, after job item status turn to Finish, choose Status symbol in column Log.Choose Magnifier, the job list refreshes. | The view goes to job log details. |  |

#### Scheduling Job for Goods Issue Deliveries (Optional)

Context

In this process step, you can define the schedule background job for goods issue for deliveries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Goods Issue For Deliveries. | The Application Jobs displays.The app starts with the history of application jobs. |  |
| 3 | Create Goods Issue Deliveries Schedule | Choose New to define a new job. | The New Job view displays.Job Template should be defaulted as Schedule goods issue for Deliveries. |  |
| 4 | Job Parameters | Define scheduling options and parameter section for batch job if necessary, then choose Check. | The system displays the notification Go Ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A schedule goods issue for deliveries job is scheduled. The view goes back to Application Jobs. |  |
| 6 | Check Goods Issue Deliveries Job Log | In the view Application Jobs, after job item status turn to Finish, choose Status Symbol in column Log.Click Magnifier, the job list refreshes. | The view goes to job log details. |  |

#### Scheduling Job for Billing Creation (Optional)

Context

In this process step, you can define the schedule background job for creation billing documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open the Schedule Billing Creation. | The Application Jobs displays.The app starts with the history of application jobs. |  |
| 3 | Create Billing Creation Schedule | Choose New to define a new job for billing creation. | The New Job view displays.Job Template should be defaulted as Schedule Billing Creation. |  |
| 4 | Job Parameters | Define scheduling options and parameter section for batch job if necessary, then choose the Check. | The system displays the notification Go Ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A billing creation job is scheduled.The view goes back to Application Jobs. |  |
| 6 | Check Billing Creation Job Log | In the view Application Jobs, after job item status turn to Finish, choose Job Log.Choose the Magnifier, the job list refreshes. | The view goes to log details. |  |

#### Scheduling Job for Billing Release (Optional)

Context

In this process step, you can define the schedule background job for release billing documents to accounting.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open the Schedule Billing Release. | The Application Jobs displays.The app starts with the history of application jobs. |  |
| 3 | Create Billing Release Schedule | Choose New to define a new job for billing creation. | The New Job view displays.Job Template should be defaulted as Schedule Billing Release. |  |
| 4 | Job Parameters | Define scheduling options and parameter section for batch job if necessary, then choose Check. | The system displays the notification Go Ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A billing release job is scheduled.The view goes back to Application Jobs. |  |
| 6 | Check Billing Release Job Log | In the view Application Jobs, after job item status turn to Finish, choose Job Log.Choose the Magnifier, the job list refreshes. | The view goes to log details. |  |

#### Scheduling Job for Billing Output (Optional)

Context

In this process step, you can define the schedule background job for when and how billing documents are sent to customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Billing Output. | The Application Jobs displays.The app starts with the history of application jobs. |  |
| 3 | Create Billing Output Schedule | Choose New to define a new job for billing creation. | The New Job view displays.Job Template should be defaulted as Schedule Billing Output. |  |
| 4 | Job Parameters | Define scheduling options and parameter section for batch job if necessary, then choose Check. | The system displays the notification Go Ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A billing output job is scheduled.The view back to Application Jobs. |  |
| 6 | Check Billing Output Job Log | In the view Application Jobs, after job item status turns to Finish, choose Job Log.Choose the Magnifier, the job list refreshes. | The view goes to log details. |  |

### Overview on Possible Item Categories for BOM Main Item

For the 3 BOM variants which are mentioned in the test script we offer also 'subvariants' which include Free of charge delivery with/without invoice and we also support Milestonebilling as described in scope item BKJ. Below you find an overview of the related item categories in the Sales order.

BOM Type CPFH

Main item variant in Sales order

1. CPHD. This is the default main item. With this main item the BOM determines a price on main item and will be relevant for invoicing based on the delivery
2. CFHD. This is an optional main item variant which can be choosen manually. With this variant the main item will have an automatically applied 100% rebate and is free of charge. The Bom is invoiced based on delivery with value 0
3. CNHD. This is an optional main item variant which can be choosen manually. With this variant the main item will have no pricing at all and is free of charge. No invoice is created- process does end with the creation of a delivery.
4. CMHD. This is an optional main item variant which can be choosen manually. With this variant you can invoice the sales BOM with a down payment and milestone billing according to scope item BKJ

BOM Type LUMF

Main item variant in Sales order

1. TAP. This is the default main item. With this main item the BOM determines a price on main item and will be relevant for invoicing based on the delivery
2. TAPF. This is an optional main item variant which can be choosen manually. With this variant the main item will have an automatically applied 100% rebate and is free of charge. The Bom is invoiced based on delivery with value 0
3. TAPN. This is an optional main item variant which can be choosen manually. With this variant the main item will have no pricing at all and is free of charge. No invoice is created- process does end with the creation of a delivery.
4. CBTP. This is an optional main item variant which can be choosen manually. With this variant you can invoice the sales BOM with a down payment and milestone billing according to scope item BKJ

BOM Type ERLA

Main item variant in Sales order

1. TAQ. This is the default main item. With this main item the BOM determines a price on main item and will be relevant for invoicing based on the delivery
2. TAQF. This is an optional main item variant which can be choosen manually. With this variant the main item will have an automatically applied 100% rebate and is free of charge. The Bom is invoiced based on delivery with value 0
3. CBTQ. This is an optional main item variant which can be choosen manually. With this variant you can invoice the sales BOM with a down payment and milestone billing according to scope item BKJ

For the 4th BOM variants which are mentioned in the test below you find an overview of the related item categories in the Sales order.

BOM Type DISH

|  |  |
| --- | --- |
| FPHD | This is the default main item. The main item is relevant for logistics and the automatically exploded subitems carry the Sales price. The Profitability analysis will be done on main item level as cost and revenue are collected on the main item level for the Profitability reporting |
| FBHD | This is an optional main item variant which can be choosen manually. This item will in addition determine a 100% rebate so the item can be send free of charge with an invoice |
| FFOC | This is an optional main item variant which can be choosen manually. With this variant the main item will have no pricing at all and is free of charge. No invoice is created- process does end with the creation of a delivery. |

### Supported Item Categories for Sales Kits

Only item category CPFH is supported in consignment processes. For the detailed steps, see the test script of scope item 1IU_US (Customer Consignment).

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
> Flagged while digesting this document, not verified: Process code BKK is used for two different scope items in the same document: 'Sales Period End Closing Operations (BKK)' under Succeeding Processes and 'BKK-Sales Order Processing - SEPA Direct Debit Handling' under Relevant Processes.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[08-sales-order-management/customer-returns-for-sales-kits-5cx-ae-test-script-sap-s-4hana-cloud-p]]
- related-to :: [[08-sales-order-management/test-script-make-to-order-production-for-sales-kits-with-variant-confi]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/31Q_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 45,297 chars in the whole document
