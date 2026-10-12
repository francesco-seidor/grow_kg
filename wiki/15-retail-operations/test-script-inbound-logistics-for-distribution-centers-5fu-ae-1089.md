---
id: 15-retail-operations/test-script-inbound-logistics-for-distribution-centers-5fu-ae-1089
title: "Test Script: Inbound Logistics for Distribution Centers (5FU_AE) (5FU_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 5FU_AE: inbound delivery, putaway confirmation and goods receipt posting at a distribution center."
cluster: 15-retail-operations
tags: [kb/retail-operations, topic/dc-inbound-logistics]
aliases: [5FU_S4CLD2608_BPD_EN_AE]
keywords: [Inbound Logistics for Distribution Centers, inbound logistics, inbound delivery, inbound delivery mass processing, putaway confirmation, goods receipt, purchase orders, supplier confirmations, business roles, sample master data]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5FU_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1089
topic: 15-retail-operations/dc-inbound-logistics
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Inbound Logistics for Distribution Centers (5FU_AE) (5FU_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5FU_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Inbound Logistics for Distribution Centers** in Retail Operations. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Inbound Logistics for Distribution Centers (5FU_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232856849)

[2 Prerequisites 3](#_Toc232856850)

[2.1 System Access 3](#_Toc232856851)

[2.2 Roles 3](#_Toc232856852)

[2.3 Master Data, Organizational Data, and Other Data 3](#_Toc232856853)

[2.4 Business Conditions 4](#_Toc232856854)

[2.5 Preliminary Steps 5](#_Toc232856855)

[2.5.1 Create Purchase Order (Optional) 5](#_Toc232856856)

[2.5.2 Monitor Supplier Confirmations (Optional) 6](#_Toc232856857)

[3 Overview Table 8](#_Toc232856858)

[4 Test Procedures 9](#_Toc232856859)

[4.1 Create Inbound Delivery 9](#_Toc232856860)

[4.2 Create Inbound Delivery Mass Processing (Optional) 10](#_Toc232856861)

[4.3 Confirm Quantities for Putaway 11](#_Toc232856862)

[4.4 Post Goods Receipt for Inbound Delivery 12](#_Toc232856863)

[5 Appendix 13](#_Toc232856864)

[5.1 Process Integration 13](#_Toc232856865)

[5.1.1 Preceding Processes 13](#_Toc232856866)

[5.1.2 Succeeding Processes 13](#_Toc232856867)

## Purpose

Overview

The purchase order is the basis for all goods receipt processing. The purchase order is communicated to the external supplier. As the goods are shipped, the supplier can optionally send the corresponding shipping documents to the recipient. These Advance Shipping Notices (ASN) can be posted up front in the system as an inbound delivery before the actual arrival of the merchandise in the distribution center (DC). Compared to the purchase order and an optional order confirmation, the ASN gives more accurate information about the expected quantities and dates, thus enhancing supply chain transparency.

Part of the goods receipt articles and their quantities can be prefilled by data from the purchase order or inbound delivery. After counting, the quantities can be adjusted if needed. As a result of posting the good receipt, the inventory is adjusted accordingly and the respective financial accounts are posted.

If differences are discovered later, you can make the necessary corrections, partially cancelling the goods receipt.

A variant of goods receipt handling is the receiving of merchandise returned from a store to the DC.

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
| Purchaser (Retail) | SAP_BR_PURCHASER_RFM | Retail Purchasing | SAP_BR_PURCHASER_RFM |  |
| Receiving Specialist | SAP_BR_RECEIVING_SPECIALIST | Materials Management - Warehouse Execution | SAP_BR_RECEIVING_SPECIALIST |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK_RFM | Materials Management - Warehouse Execution | SAP_BR_WAREHOUSE_CLERK_RFM |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

Use your own master data or the following sample data to go through the test procedure.

| Master / Org. Data | Value | Master / Org. Data Details | Comments |
| --- | --- | --- | --- |
| Single Article | R_1006 | My Best Frozen Strawberries |  |
| Generic Article | R_1003 | Chocolate |  |
| Sales set Article (Material or Product) | R_1052 | My Best Blond Shampoo & Conditioner |  |
| Display Article (Material or Product) | R_2007 | Chocolate Bar Display |  |
| Supplier | 33213002 | Retail Food Supplier AE |  |
| Supplier | 33213001 | Retail Non-Food Supplier AE |  |
| Plant (Site or Location) | 3350 | DC 3350 AE |  |
| Storage Location | 995A | Storage Loc. DC |  |
| Shipping Point | 3350 | SP DC 3350 |  |
| Purchasing Organization | 3310 | Purch. Org. 3310 |  |
| Purchasing Group | 3310 | Group 001 |  |
| Company Code | 3310 | Company Code 3310 |  |

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 3I8 - Replenishment Planning for Distribution Centers | To run through this scope item, purchase order must be created, purchase requisitions are created automatically through replenishment planning. The result of MRP execution is then handed over to operational procurement via so-called purchase requisitions. |
| 5FM - Procurement for Retail | To run through this scope item, purchase order must be created either manually or in reference to purchase requisitions, corresponding to which goods will be received at the DC. |
| 3I4 - Sales Pricing for Retail | Access Sequence for MM Pricing Condition type PPR0 should be switched to 0002 before creating purchase orders in the system, for details please refer to chapter in scope item (). |

### Preliminary Steps

#### Create Purchase Order (Optional)

Use

To execute this scope item, you must create a purchase order.

|  |
| --- |
| Note This process step must be executed if preceding processes mentioned in chapter [Preceding Processes](#unique_8) [page ] 13 of this document have not been executed. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the Purchaser (Retail) role. |  |  |
| 2 | Open Manage Purchase Orders App | Open Create Purchase Order - Advanced (ME21N) app. | The Create Purchase Order - Advanced (ME21N) screen is displayed.Standard filters and buttons are displayed. |  |
| 3 | Navigate to Create Order Screen | On the Create Purchase Order screen, choose Create. |  |  |
| 4 | Enter Purchase Order Data | Enter all the necessary data.Order type: Standard PO or NB Standard POSupplier: 33213002In Header section, on the Org. Data tab:Purch. Org.: 3310Purch. Group: 001Company Code: 3310In Item Overview section:Material: R_1006Plant: 3350Storage Location: 995AQuantity: <Enter a quantity>Net Price: xxxNote Price should be determined automatically from purchasing info record.Under Item Detail, select Confirmations:Conf. Control: Inbound DeliveryThen select Enter. |  |  |
| 5 | Save Purchase Order | Choose Save and when the purchase order number is displayed and note it down for further use. | A new purchase order is created.Purchase order number is displayed. |  |

Result

The purchase order is created, and purchase order number is generated.

#### Monitor Supplier Confirmations (Optional)

Use

This section describes how to monitor purchase order documents awaiting supplier confirmations.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad using the Purchaser (Retail) role. |  |  |
| 2 | Access the App | Open Monitor Supplier Confirmations (F2359) app. | The Monitor Supplier Confirmations (F2359) screen is displayed. |  |
| 3 | Search for Purchase Orders | Make the following filters in top filter bar then choose Go:Display Currency: AEDConfirmation Category: INBOUND DELIVERY(LA) | The purchasing document is displayed mentioning scheduled date, scheduled quantity and committed quantity.Note Purchase orders that are due for delivery at a future date, appear based on the number of days maintained for the confirmation control key in the Set Up Confirmation Control configuration settings. |  |
| 4 | Display Purchase Order Item Details | Choose the individual line item of the purchasing document where you want to display the purchase order details. | The Purchase Order Item screen is displayed. |  |
| 5 | Verify data displayed on the object page | Verify data displayed on the object page. | The data should be logically in sync with purchase order. |  |

Result

The data is in sync with the purchase order.

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App | Expected Results |
| --- | --- | --- | --- |
| [Create Inbound Delivery](#unique_11) [page ] 9 | Receiving Specialist | Create Inbound Delivery (VL31N) | Inbound delivery document with reference to purchase order is created |
| [Create Inbound Delivery Mass Processing (Optional)](#unique_12) [page ] 10 | Receiving Specialist | Inbound Deliveries for Purchase Orders (VL34) | Inbound delivery documents are created in bulk corresponding to their respective purchase orders |
| [Confirm Quantities for Putaway](#unique_13) [page ] 11 | Receiving Specialist | Change Inbound Delivery (VL32N) | Inbound Delivery document is updated with confirmed putaway quantities. |
| [Post Goods Receipt for Inbound Delivery](#unique_14) [page ] 12 | Warehouse Clerk | Post Goods Movement (MIGO) | Goods receipt is posted for the inbound delivery when goods arrive at DC. |

## Test Procedures

This chapter describes the test procedures for each process step that belongs to this scope item.

### Create Inbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you manually create inbound delivery with reference to purchase order (PO).

|  |
| --- |
| Note The supplier gives information on merchandise, quantities, and dates of delivery, which is stored in an inbound delivery document. It can be created manually as described. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Receiving Specialist. |  |  |
| 2 | Access App | Open Create Inbound Delivery (VL31N) app. | Create Inbound Delivery (VL31N) app screen is displayed. |  |
| 3 | Start Selection for Inbound Delivery Creation | On the Create Inbound Delivery (VL31N) app screen, enter the following:Supplier: 33213002Purchase Order:<your Purchase Order document number>Select Continue. |  |  |
| 4 | Save Inbound Delivery Document | Select Save. | Inbound delivery document is created. |  |

### Create Inbound Delivery Mass Processing (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can process purchase orders (PO) in bulk to create corresponding inbound deliveries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Receiving Specialist. |  |  |
| 2 | Access the App | Open Inbound Deliveries for Purchase Orders (VL34) app. | The Generation of Inbound Deliveries screen is displayed. |  |
| 3 | Create Inbound Delivery | Provide the data for the following fields and select Execute:Document Number: <your Purchase Order document numbers>Delivery Date to: <select date> (Delete the default date and enter the delivery date in purchase order)Test Run: uncheckedThe inbound delivery number displays on the screen. Note it down for further use. | A new inbound delivery is created.The inbound delivery number is displayed. |  |

### Confirm Quantities for Putaway

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

### Post Goods Receipt for Inbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you post goods receipt for inbound delivery to update the inventory information in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Warehouse Clerk. |  |  |
| 2 | Access the App | Open Post Goods Movement (MIGO) app. | The Goods Receipt screen is displayed. |  |
| 3 | Enter Inbound Delivery Number | Provide the values for the following entries and select Enter:Select Goods Receipt and Inbound Delivery from the dropdown and enter the following: Inbound Delivery Number: XXX Goods Movement Type: 101Select Enter. | The data with in the selected inbound delivery like article, quantities are displayed. |  |
| 4 | Check and Post the Goods Receipt for Inbound Delivery | Scroll to the bottom of the Goods Receipt Inbound Delivery xxxxxxxxxx screen, select to check the Item OK checkbox. Select Check on the bottom right of the screen. Select Post. | The goods receipt is posted.Message Material Document <Document number> posted. is displayed. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

The following processes and conditions can proceed this process.

| Process | Business Condition |
| --- | --- |
| 3I8 - Replenishment Planning for Distribution Centers | To run through this scope item, purchase order must be created, purchase requisitions are created automatically through replenishment planning. The result of MRP execution is then handed over to operational procurement via so-called purchase requisitions. |
| 5FM - Procurement for Retail | To run through this scope item, purchase order must be created, corresponding to which goods will be received at the DC. |

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| – | At the end of the logistic process of purchasing, receiving and inventory management, invoice verification is done to ensure the receipt invoices is accurate content, prices, and calculations wise. |

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
- see-also :: [[15-retail-operations/outbound-logistics-for-distribution-centers-5fv-ae-test-script-1090]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5FU_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 21,480 chars in the whole document
