---
id: 08-sales-order-management/statistical-sales-conditions-34b-ae-test-script-906
title: Statistical Sales Conditions (34B_AE) - Test Script (34B_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 34B (AE): statistical sales conditions such as cash discount posted to extension ledger 0C."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/sales-pricing-conditions]
aliases: [34B_S4CLD2608_BPD_EN_AE]
keywords: [Sales Price Conditions and Statistical Conditions, statistical sales conditions, margin analysis, extension ledger 0C, cash discount, sales order creation, sales order actuals report, outbound delivery, picking, goods issue posting]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/34B_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-906
topic: 08-sales-order-management/sales-pricing-conditions
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Statistical Sales Conditions (34B_AE) - Test Script (34B_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/34B_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Sales Price Conditions and Statistical Conditions** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Statistical Sales Conditions (34B_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232851696)

[2 Prerequisites 3](#_Toc232851697)

[2.1 System Access 3](#_Toc232851698)

[2.2 Roles 3](#_Toc232851699)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232851700)

[2.4 Preliminary Steps 6](#_Toc232851701)

[2.4.1 Set Initial Stock for Material 6](#_Toc232851702)

[3 Overview Table 8](#_Toc232851703)

[4 Test Procedures 9](#_Toc232851704)

[4.1 Create Sales Order 9](#_Toc232851705)

[4.2 Create Delivery 11](#_Toc232851706)

[4.3 Execute Picking 12](#_Toc232851707)

[4.4 Post Goods Issue 13](#_Toc232851708)

[4.5 Create Billing Document 14](#_Toc232851709)

[4.6 Sales Order Actual Report 16](#_Toc232851710)

## Purpose

Overview

If you want to see statistical values such as warranties and cash discounts in Margin Analysis reports, align with your Sales and Distribution colleagues so that they include such statistical SD conditions in the pricing procedure. The scope item 34B has to be activated. Don’t forget to select extension ledger 0C as well when executing Margin Analysis reports.

After activation of this scope item, the system will calculate and transfer the values of statistical sales conditions from SD Sales and Distribution to Margin Analysis. The values are written to extension ledger 0C using General Ledger accounts. The account key is assigned to a statistical condition, posted to the G/L, and set as relevant for account determination in the SD pricing procedure. For example, a statistical cash discount is posted to the extension ledger during billing.

To use the functionality for other statistical SD condition use cases such as warranties and cash discounts, you make the following settings for the price condition: the price condition has been set for statistics only, that is, you have selected the Statistics indicator; an Account key that defines two accounts (the Accruals key is not considered).

Various self-service configuration steps are also available for your convenience.

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
| Cost Accountant - Sales | SAP_BR_SALES_ACCOUNTANT | Sales Accounting | SAP_BR_SALES_ACCOUNTANT |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |

### Master Data, Organizational Data, and Other Data

SAP Best Practices Standard Values based on new global template will be used once available. In the table you still see the master data used for the current baseline.

Essential master and organizational data was created in your SAP S/4HANA system in the implementation phase, such as the data that reflects the organizational structure of your company and master data that suits its operational focus, for example, master data for materials, vendors, and customers.

This master data usually consists of standardized SAP Best Practices default values, and enables you to go through the process steps of this scope item.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

|  |
| --- |
| Note Additional Master Data (Default Values)You can test the scope item with other SAP Best Practices default values that have the same characteristics.Check your SAP system to find out which other material master data exists. |

|  |
| --- |
| Note Using Your Own Master DataYou can also use customized values for any material or organizational data for which you have created master data.Note The condition type DCD1 or DCD2 for cash discount is filled only if in the material master the indicator for cash discount is set: (View - Sales Order, Field - Cash discount) - for example, as marked in material master TG11. |

Use the following master data in the process steps described in this document:

| Master / Org. Data | Value | Master / Org. Data Details | Comments |
| --- | --- | --- | --- |
| Material | TG11 | Trading Good for Reg. Trading (MRP planning)No serial number, no batch | See sections Business Conditions and Preliminary Steps.Use TG11 to test customer material, recorded with customer 33100009. |
| Material | TG12 | Trad.Good 12,Reorder Point,Reg.Trad.No serial number, no batch | See sections Business Conditions and Preliminary Steps. |
| Sold-to Party | 33100001 | Domestic UAE Customer 1 |  |
| Ship-to Party | 33100001 | Domestic UAE Customer 1 |  |
| Payer | 33100001 | Domestic UAE Customer 1 |  |
| Plant | 3310 |  |  |
| Storage Location | 331A |  |  |
| Shipping Point | 3310 |  |  |
| Sales Organization | 3310 |  |  |
| Distribution Channel | 10 |  |  |
| Division | 00 |  |  |
| SD Condition Type | DCD2DCD1 | Cash Discount NetCash Discount Gross | These are marked as statistical conditions and relevant for Account Determination (demo data) |
| Account Key | YSC |  |  |
| G/L Account | 7105500021775000 | Accrual statistical conditionStatistical condition cash discount | Posting to extension ledger 0C |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BND | Create Customer Master - MDS |
| 2YX | Create Customer-Material Info Record - MDS |

### Preliminary Steps

#### Set Initial Stock for Material

Purpose

To execute this scope item, the materials must be available in stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO) | The Goods Issue Other - <warehouse_clerk USER ID> screen displays. |  |
| 3 | Input Movement Type | Make the following entry and choose Enter.Executable Action in Transaction MIGO: Goods ReceiptReference Document for MIGO Transaction: Other | The Goods Receipt Other screen displays. |  |
| 4 | Input on the Goods Receipt Other screen: Material tab | On the Goods Receipt Other screen: Material tab, make the following entry and choose Enter:Material: Material Number, for example TG11 |  |  |
| 5 | Enter Quantity Data | On the Goods Receipt Other screen: Quantity tab, make the following entry and choose Enter:Qty in Unit of Entry: Qty in UOM, for example 5Unit of Entry: PC |  |  |
| 6 | Input on the Goods Receipt Other screen: Where tab | On the Goods Receipt Other screen: Where tab, make the following entries and choose Enter:Movement Type: 561 - Receipt per initial entry of stock balances into unr.-usePlant: <Enter a Plant>, for example 3310Storage Location: <Enter a Storage Location>, for example 331A |  |  |
| 7 | Input on the Goods Receipt Other screen: Batch tab | On the Goods Receipt Other screen: Batch tab, make the following entry and choose Enter:Date of manufacture: <Enter the current date or a date in the past>Note Only applicable for batch relevant materials. |  |  |
| 8 | Save your entries. | Click Post. |  |  |

Financial postings:

| Material | Debited Accounts | Credited Accounts |
| --- | --- | --- |
| Trading Good (HAWA) | 13600000Inventory TradingGd | 39912000Inv Init SF&amp;Fin Bal |

## Overview Table

This scope item consists of several process steps that are listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Create Sales Order](#unique_8) [page ] 9 | Internal Sales Representative | Manage Sales Orders (F1873) | The Manage Sales Orders screen displays. |
| [Create Delivery](#unique_9) [page ] 11 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) | The Create Outbound Deliveries screen displays. |
| [Execute Picking](#unique_10) [page ] 12 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | The Manage Sales Orders screen displays. |
| [Post Goods Issue](#unique_11) [page ] 13 | Shipping Specialist | Manage Outbound Deliveries (F0867A) | The goods issue is posted. |
| [Create Billing Document](#unique_12) [page ] 14 | Billing Clerk | Create Billing Documents (F0798) | Billing is handled in this activity. |
| [Sales Order Actual Report](#unique_13) [page ] 16 | Cost Accountant - Sales | Sales Orders - Actuals (F1582A) | The actual figures for sales orders displays. You can see that the cash discount is posted in ledger 0C. |

## Test Procedures

This section describes procedures for each process step that belongs to this scope item.

The Enterprise search function provides a central entry point for finding business objects in your company from different sources using a single search request, You can search for objects such as: Apps, factsheets for business objects. From the data found, you can go directly to the respective apps and factsheets to display, edit the data or find related objects.

How to access and check a factsheet:

1. Log onto the SAP Fiori Launchpad using the respective user, for example, Internal Sales Representative.
2. Access the Enterprise Search Bar and choose the magnifying glass button in the upper right corner.
3. The Enterprise Search bar is displayed, two filter fields appear left to the search button. Enter your Search Criteria and choose the business object type, for example, Sales orders from drop-down menu in 1st field, enter sales order number in 2nd field and choose Search, The sales order is listed.
4. Choose the sales order number link: the system navigates to the factsheet screen and sales order related information is integrated and summarized in one Fiori page, You can get detailed data via choosing the corresponding links.

There are factsheets available for the following objects: (Visible depending on the assigned role)

- Sales order
- Quotation
- Create Nota Fiscal
- Billing document
- Credit Memo
- Debit Memo
- Customer 360 Fact sheet

### Create Sales Order

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
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Navigate to Create Order Screen | Choose Create > Create Sales Orders - VA01 . |  |  |
| 4 | Enter the Order type OR (Standard Order) | On the Create Sales Documents screen, make the following entries and choose the Continue button:Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 5 | Enter Order Details | On the Create Standard Order: Overview screen, make the following entries and press Enter:Sold-To Party: 33100002Ship-To Party: 33100002Cust. Reference: <Enter a customer purchase order number as reference>Cust. Ref. Date: <Enter a date>Pyt Terms: 0002Material: <Material number>, for example TG11Order Quantity: <Enter a quantity> | Customer master data 33100002 is defaulted with payment terms 0004, so you can assign payment terms 0002 in the customer order.This ensures the cash discount in this sales order, and therefore condition type DCD1 or DCD2 for cash discount is filled. This statistical condition value will be posted to Extension Ledger 0C. |  |
| 6 | Save Document | Choose the Save button. Make a note of the sales order number. | The order is saved and the order confirmation is printed out. |  |

|  |
| --- |
| Note You can also navigate to a fact sheet screen in the Manage Sales Orders app:On Manage Sales Orders screen, enter search terms in filter bar and choose Go.In search result, choose your sales order number. |

### Create Delivery

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

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2. | Access the SAP Fiori App | Open Create Outbound Deliveries - From Sales Orders (F0869A). | The Create Outbound Deliveries screen displays. |  |
| 3. | Search Sales Order | Make the following entries and choose Go:Shipping Point: 3310Planned Creation Date: <Delivery selection date>Sales Document: Sales order number created previously |  |  |
| 4. | Create Delivery | Select your sales order items and choose Create Deliveries. | Creation of a delivery is triggered. |  |
| 5. | Check Details | Choose Display Log | The Analyze Delivery Log screen displays, delivery is created successfully with delivery number shown on tab Deliveries. |  |

To avoid open deliveries, ensure that there is sufficient inventory quantity at the time of delivery creation. Additionally, you have the following options to restrict the creation of deliveries with no confirmed quantities:

- You can increase the replenishment lead time which is used during the availability check (has to be larger than the selection period used for delivery creation).
- You can change the customization settings for the incompleteness procedure for delivery creation, so that only complete deliveries are saved.
- You can change the customization settings for the used delivery-item-category. The Check quantity 0 field must be adapted to B = Situation rejected with an error message.

|  |
| --- |
| Note With the Analyze Delivery Logs app, you can display an overview about the logs of all the deliveries which have been created in your system. You can filter by Created by and other additional settings. If you select the arrow on the right of each delivery log entry, you can display the exact message type and text and also the related sales document. |

### Execute Picking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The picking process involves taking goods from a storage location and staging the right quantity in a picking area where the goods are prepared for shipping.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad screen displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). | The Manage Outbound Deliveries screen displays. |  |
| 3 | Choose Picking | Choose For Picking. |  |  |
| 4 | Enter Shipping Point | Make the following entries, and choose Execute.Shipping point: 3310Only Picking without WM: X |  |  |
| 5 | Change Outbound Delivery (Original) | From Day’s Workload for Picking , select your delivery number and choose Change Outbound Deliveries. |  |  |
| 6 | Check if Batch Split Exists | Navigate to the Picking tab, check if batch split exists in Batch Split Indicator column:Yes: go to 7 a.No: go to 7 b. |  |  |
| 7 | Enter Picked Quantity | 7a: Choose Batch Split Exists to expand subitems, enter quantity equal to delivery Qty in the Picked Qty field for subitem.7b: Enter quantity equal to delivery Qty in the Picked Qty field for picking related items. |  |  |
| 8 | Choose Enter | Choose Enter. |  |  |
| 9 | Save | Choose Save. | The delivery has been picked. |  |

### Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you post the goods issues for the delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2. | Access the SAP Fiori App | Open Manage Outbound Deliveries (F0867A). | The Manage Outbound Deliveries screen displays. |  |
| 3. | Open Outbound Delivery Monitor | Choose For Goods Issue. Make the following entry and choose Go.Shipping point: 3310 | A list of relevant deliveries is displayed. |  |
| 4. | Post Goods Issue | Mark the relevant delivery and choose Post GI. Select today’s date from the dialog box and choose Post GI. | The goods issues are posted for the delivery. |  |

Financial Postings:

| Material (Original) | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 51600000Consptn Trde Gds | 13600000Inventory TradingGd | none |

### Create Billing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Billing is handled in this activity.

Create Billing Document

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Billing Documents (F0798). | The Create Billing Documents (F0798) screen displays. |  |
| 3 | Define Billing Setting | Choose Billing Settings in the bottom bar, and make the following settings:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: OFFAutomatically post billing documents: ONDisplay billing documents after creation: ONChoose delivery items to be billed and select quantities: OFF |  |  |
| 4 | Search for Billing Due List | In the search condition, use criteria if necessary. | The sales documents display. |  |
| 5 | Select Items for Billing | Select rows of sales document created previously and choose the Create button. | The Create Billing Documents displays. |  |
| 6 | Maintain Billing Date | Choose billing type Invoice (F2) and maintain billing date, for example current date, then press button OK. | The draft billing document with ID Sxxxxxxxx displays. |  |
| 7 | Save Billing Document | In the Billing Document screen, choose the Save button. The draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx, make a note of the billing document number: __________.. | The system generates an invoice for billing. |  |

Financial Postings:

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) |  | 41000000Rev Domestic Prod | none |

### Sales Order Actual Report

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the sales order report is generated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Sales Orders - Actuals (F1582A). | The Sales Orders - Actuals screen displays. |  |
| 3 | Enter Data | Make the following entries :Ledger: 0CFiscal Year of Ledger: <Enter the current year>Key Date: <Enter the current date>Fiscal Period: <Enter the current period>Company Code: 3310G/L Account Hierarchy: YPS2Sales Order: <Created in the previous step>Choose Go. | The actual figures for sales orders displays. You can see that the cash discount is posted in ledger 0C. |  |
| 4 | Set Dimensions | To set dimensions for reporting, drag and drop items from section Dimensions into sections Columns or Rows. | The selected dimensions are presented as rows and columns on the report. |  |

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
> Flagged while digesting this document, not verified: Master data table lists sold-to/ship-to/payer 33100001 but the sales order test step uses customer 33100002 (and mentions 33100009 for customer material).

## Connections
- part-of :: [[_cluster]]
- related-to :: [[08-sales-order-management/create-sales-pricing-condition-mds-bet-539]]
- related-to :: [[08-sales-order-management/mds-bet-541]]
- related-to :: [[08-sales-order-management/mds-bet-543]]
- related-to :: [[08-sales-order-management/script-de-dados-mestre-criar-condicao-de-determinacao-de-preco-de-vend]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/34B_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 27,396 chars in the whole document
