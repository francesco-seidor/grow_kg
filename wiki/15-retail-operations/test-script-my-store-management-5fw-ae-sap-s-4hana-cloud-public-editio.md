---
id: 15-retail-operations/test-script-my-store-management-5fw-ae-sap-s-4hana-cloud-public-editio
title: "Test Script: My Store Management (5FW_AE) - SAP S/4HANA Cloud Public Edition (5FW_S4CLD2608_BPD_EN_AE)"
description: "SAP test script for scope item 5FW My Store Management (AE): store associate assignment, picking sequence and My Store Overview app, with prerequisites and sample data."
cluster: 15-retail-operations
tags: [kb/retail-operations, topic/my-store-management]
aliases: [5FW_S4CLD2608_BPD_EN_AE]
keywords: [My Store Management, store associate assignment, store assignment change, picking sequence, my store overview, test prerequisites, business roles, sample data, purchase orders, inbound delivery]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5FW_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1091
topic: 15-retail-operations/my-store-management
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: My Store Management (5FW_AE) - SAP S/4HANA Cloud Public Edition (5FW_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5FW_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **My Store Management** in Retail Operations. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | My Store Management (5FW_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232856376)

[2 Prerequisites 4](#_Toc232856377)

[2.1 System Access 4](#_Toc232856378)

[2.2 Roles 4](#_Toc232856379)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232856380)

[2.4 Business Conditions 5](#_Toc232856381)

[2.5 Preliminary Steps 6](#_Toc232856382)

[2.5.1 Create Purchase Order 6](#_Toc232856383)

[2.5.2 Create Inbound Delivery 7](#_Toc232856384)

[2.5.3 Process Aggregated Sales Received from Point-of-Sale (POS) 8](#_Toc232856385)

[2.5.4 Schedule Job for Posting of POS Inbound for Sales 8](#_Toc232856386)

[2.5.5 Setup Retail Promotions 9](#_Toc232856387)

[2.5.5.1 Create Retail Promotions 9](#_Toc232856388)

[2.5.5.2 Determine Supply Sources for Retail Promotions 9](#_Toc232856389)

[2.5.5.3 Activate Retail Pricing for Retail Promotions 10](#_Toc232856390)

[3 Overview Table 11](#_Toc232856391)

[4 Test Procedures 12](#_Toc232856392)

[4.1 Assign Store Associates to a Store 12](#_Toc232856393)

[4.2 Change My Store Assignment 14](#_Toc232856394)

[4.3 Maintain Picking Sequence based on Merchandising Category 15](#_Toc232856395)

[4.4 My Store Overview 16](#_Toc232856396)

## Purpose

Overview

Store associates and managers execute processes differently than employees working in the headquarters. Complex user interfaces aren't an option for in-store processes because of costly training and higher turnover rates of store personnel. The SAP Fiori apps in this scope item are user-friendly, self-explanatory, and streamlined for in-store processes.

A dashboard that contains the most important KPIs for efficient day-to-day operations supports store associates and managers. The dashboard can be configured to exactly meet their needs.

Furthermore, store managers can maintain necessary information required to run and manage processes and people in their store. The SAP Fiori app provides the possibility to:

- Monitor and analyze the most critical KPIs of the store
- Maintain the staff working in the store and thereby control access to the store’s data
- Maintain the picking sequence to support omnichannel order fulfillment (for more information, see the Omnichannel Order Fulfillment for Retail (5FZ) scope item.

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
| Retail Store Associate | [SAP_BR_RFM_STORE_ASSOCIATE](https://qj5-579.wdf.sap.corp/ui) | Retail Store Associate | [SAP_BR_RFM_STORE_ASSOCIATE](https://qj5-579.wdf.sap.corp/ui) |  |
| Retail Store Manager | [SAP_BR_RFM_STORE_MANAGER](https://qj5-579.wdf.sap.corp/ui) | Retail Store Manager | [SAP_BR_RFM_STORE_MANAGER](https://qj5-579.wdf.sap.corp/ui) |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

Use your master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Store (Site) | 3340 | Store 3340 AE |  |
| Merchandise Category | R1111001R1111002R1171001 | FRESH FISHSEAFOODBREAD | Picking sequence is based on merchandise category.Use these merchandise categories to execute Step [Maintain Picking Sequence based on Merchandising Category](#unique_6) [page ] 15 – Maintain picking sequence based on merchandise category |
| Single Article | R_1039 | My Best bread roll - Italian | Use this article to execute the preliminary steps |
| Supplier | 33213001 | Retail Non-Food Supplier AE |  |
| Purchasing Organization | 3310 | Purch. Org. 3310 |  |
| Purchasing Group | 001 | Group 001 |  |
| Company Code | 3310 | Company Code 3310 |  |
| Plant | 3340 | Store 3340 AE |  |
| Storage Location | 994A | St.Loc.Neg.Stock |  |
|  |  |  |  |

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 3HV - Store Connectivity – Inbound | Must be run before this test script. |
| 5FY - In-Store Purchase Order Management | Must be run before this test script. |
| 637 - Retail Promotions | Must be run before this test script. |

### Preliminary Steps

#### Create Purchase Order

Use

You can perform this activity to create purchase orders.

|  |
| --- |
| Note This step is a prerequisite to create inbound delivery. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as Purchaser (Retail) |  |  |
| 2 | Open Manage Purchase Orders app | Open Create Purchase Order – Advanced (F0842A) app |  |  |
| 3 | Navigate to Create Purchase Order screen | On the Create Purchase Order screen, select Create |  |  |
| 4 | Enter Purchase Order data | Enter all the necessary dataOrder type : NB Standard POSupplier : 33213001In Header, on the Org. Data tab:Purch. Org .: 3310Purch. Group : 001Company Code :3310In Item Overview:Material : R_1039Plant : 3340Storage Location : 994APO Quantity : Enter any valueNet Price : Enter any valueDelivery Date : Today’s DateIn Item Detail, on Confirmation's tab:Conf. Control : 0004 (Inbound Delivery) value is defaultedSelect EnterNote Warning message is displayed. |  |  |
| 5 | Save Purchase Order | Select Save and when the purchase order number is displayed, write it down for further use.Note Repeat the steps to create POs with delivery date in the past and future. | A new purchase order is created.Purchase order number is displayed. |  |

Result

Purchase orders are created.

#### Create Inbound Delivery

Use

You can perform this activity to create inbound delivery for the purchase orders created in the previous step.

|  |
| --- |
| Note This step is a prerequisite to display the goods receipt data in My Store Overview (F4674) app. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Receiving Specialist |  |  |
| 2 | Access the SAP Fiori app | Open app |  |  |
| 3 | Create Inbound Delivery | Make the following entries:Supplier: 33213001 (Enter the supplier used in the previous step)Purchase Order: XXX (Enter the purchase order number created in the previous step)Delivery Date: XXX (Delete the default date and enter the delivery date in the purchase order)Select ContinueEnter Put away quantity and select Pack tab.On Pack Material screen, make the following entries:Packaging Materials: R_CARTON and select Enter to get the Handling Unit numberSelect the row for Handling Unit and Material to be packed and select Pack icon to pack the material and select SaveNote A message Material was packed is displayed.When the inbound delivery number displays, write it down for further useNote Repeat the steps to create the inbound deliveries for all the purchase orders created in previous step. | An inbound delivery is created.The inbound delivery number is displayed. |  |

Result

Inbound deliveries are created.

#### Process Aggregated Sales Received from Point-of-Sale (POS)

Use

You can perform this activity to transfer aggregated sales information sent from the POS system to the SAP S/4HANA Cloud Public Edition system.

|  |
| --- |
| Note This step is a prerequisite to display the sales data in My Store Overview (F4674) app. |

Procedure

Refer to the test script for scope item Store Connectivity – Inbound - 3HVstep 4.1.1 – Receive Aggregated Sales To perform this step, you need to perform testing with retail master data and organizational data mentioned in this test script.

Result

Aggregated sales data is received from POS system.

#### Schedule Job for Posting of POS Inbound for Sales

Use

You can perform this activity to schedule the background job to post the aggregated sales information received from the POS system.

|  |
| --- |
| Note This step is a prerequisite to display the sales data in My Store Overview (F4674) app. |

Procedure

Refer to the test script for scope item Store Connectivity – Inbound - 3HV, step 4.1.3 – Schedule Job for Posting of POS Inbound for Sales. To perform this step, you need to perform testing with retail master data and organizational data mentioned in this test script.

Result

POS aggregated sales received from POS system is posted.

|  |
| --- |
| Note To execute steps (2.6.3 and 2.6.4), setup of API client tools is a prerequisite. Refer to the Set Up Instructions Store Connectivity – Inbound - 3HV to complete this setup. |

#### Setup Retail Promotions

##### Create Retail Promotions

Use

You can perform this activity to create the retail promotions for your store.

|  |
| --- |
| Note This step is a prerequisite to display the promotion data in My Store Overview (F4674) app.You can create future promotions by maintaining the validity from date in future (current date + 7 days). |

Procedure

Refer to the test script for scope item Retail Promotions - 637, step 4.1.1. – Create Promotion. To perform this step, you perform testing with retail master data and organizational data mentioned in this test script.

Result

Retail promotions with current validity period and future validity periods are created.

##### Determine Supply Sources for Retail Promotions

Use

You can perform this activity to determine the supply sources for the retail promotions for your store.

|  |
| --- |
| Note This step is a prerequisite to display the promotion data in My Store Overview (F4674) app. |

Procedure

Refer to the test script for scope item Retail Promotions - 637, step 4.1.2 – Determine Suppy Source. To perform this step, you need to perform testing with retail master data and organizational data mentioned in this test script.

Result

Supply source is determined for the Retail promotions.

##### Activate Retail Pricing for Retail Promotions

Use

You can perform this activity to activate the retail pricing for retail promotions for your store.

|  |
| --- |
| Note This step is a prerequisite to display the promotion data in My Store Overview (F4674) app. |

Procedure

Refer to the test script for scope item Retail Promotions - 637, step 4.1.3 – Activate Price. To perform this step, you need to perform testing with retail master data and organizational data mentioned in this test script.

Result

Retail pricing is activated for retail promotions for your store.

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Assign Store Associates to a Store](#unique_16) [page ] 12 | Retail Store Manager | My Store Assignment (F4334) | The store manager can assign the store associates to a particular store so that the associate can view or perform store activities based on his store assignments. |
| [Change My Store Assignment](#unique_17) [page ] 14 | Retail Store Associate | My Store Assignment (F4334) | The store associate can change his store assignment to another store to view or perform activities based on his store assignment. |
| [Maintain Picking Sequence based on Merchandising Category](#unique_6) [page ] 15 | Retail Store Manager | Maintain Picking Sequence (F4711) | The store manager can view, download, and upload the picking sequence for the store based on either merchandise category |
| [My Store Overview](#unique_18) [page ] 16 | Retail Store Manager | My Store Overview (F4674) | The store manager checks the most critical information for the store based in the cards assigned to the app. |

## Test Procedures

This chapter describes the test procedures for each process step that belongs to this scope item.

### Assign Store Associates to a Store

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The store manager assigns store associates to a specific store. The store associates carry out day-to-day activities based on their store assignments. The store associates change their store assignments to another store too.

|  |
| --- |
| Note The store manager can also unassign store associates to a specific store. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Retail Store Manager |  |  |
| 2 | Access app | Open Assign Associates to Store (F8523) app | List of stores are displayed. |  |
| 3 | Search store by street | Enter (parts of) the name of the street in the Search field, which is maintained in the stores’ address: <street name> and select Go | The stores that have the street name is displayed in the search field. |  |
| 4 | Search store by city | Enter (parts of) the name of the city in the Search field, which is maintained in the stores’ address: <city name> and select Go | The stores that have the city name is displayed in the search field. |  |
| 5 | Search store by name | Enter (parts of) the name of the stores in the Search field: <store name> and select Go | The stores that have the store name is displayed in the search field. |  |
| 6 | Search for the store by id | Enter the store 3340 in the Search field and select Go | The stores that have the store ID is displayed in the search field. |  |
| 7 | Show assignments employees | Select the entry of the store in the list of stores | The assigned associate of the store is displayed. |  |
| 8 | Open the assignment page | Select the Assign on the upper right | The Assign Associates popup message is displayed. |  |
| 9 | Search for store manager | Note To assign store associate to the store proceed with step 11Enter (parts of) the first name, the last name, or the username of an employee in the Search field, that you want to assign – Store Manager and select ENTER | The users or employee user ID or full name is displayed in the search field. |  |
| 10 | Select store manager | Check the checkbox in front of the store manager. |  |  |
| 11 | Search for store associate | Enter (parts of) the first, the last or the username of an employee in the Search field, you want to assign and ENTER | The users or employee user ID or full name is displayed.in the search field. |  |
| 12 | Select store associate | Check the checkbox in front of the store associate |  |  |
| 13 | Assign users to store | Select Assign | The pop-up message Associate was assigned to this store. is displayed. The selected users are in the list of assigned associates. |  |
| 14 | Filter list of assigned associates | Enter (parts of) the first, the last or the username of one assigned in step 13, in the Search field and select ENTER | Users or employee user ID or full name is displayed in the search field. |  |
| 15 | Exit screen | Select Close |  |  |

### Change My Store Assignment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The store associates change their store assignment to another store to view or perform activities based on their store assignment.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Retail Store Associate |  |  |
| 2 | Access app | Open My Store Assignment (F4334) app | List of stores are displayed. The store, to which the user is assigned to, is displayed on the header section of the app. |  |
| 3 | Search store by street | Enter (parts of) the name of the street in the Search field, which is maintained in the stores’ address: <street name>and select Go | The stores that have the street name is displayed in the search field. |  |
| 4 | Search store by city | Enter (parts of) the name of the city in the Search field, which is maintained in the stores’ address: <city name>and select Go | The stores that have the city name is displayed in the search field. |  |
| 5 | Search store by name | Enter (parts of) the name of the stores in the Search field, which is maintained in the stores’ name: <store name>and select Go | The stores that have the store name is displayed in the search field. |  |
| 6 | Search for the store by id | Enter the store 3340 in the Search field and select Go | The stores that have the store id is displayed in the search field. |  |
| 7 | Display the store list | Select Reset next to the store id in the Search field and select Go | List of stores is displayed. The store, to which the user is assigned to, is displayed on the header section of the app. |  |
| 8 | Assign associate to another store | Select Store from the list apart from the one already assigned to you and save the new assignment by selecting Assign Me on the top right above the list of storesNote Please ensure to assign store 3340 to yourself before proceeding to the next test procedure. | The pops up message “You were assigned to store xxxx.” is displayed, where xxxx is the store number. The Assigned Store above the list is updated accordingly. |  |
| 9 | Exit screen | Select Back |  |  |

### Maintain Picking Sequence based on Merchandising Category

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The store manager defines the store picking sequence or re-arrange an existing store picking sequence to support omnichannel in-store order fulfilment.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Retail Store Manager |  |  |
| 2 | Open app | Open Maintain Picking Sequence (F4711) app |  |  |
| 3 | Download picking sequence | In the Maintain Picking Sequence app, select Download Picking Sequence | A pop-up information "The file contains merchandise category information of your store. You can rearrange or update the data before uploading it in the system." is displayed. |  |
| 4 | Download excel file | Select Download | The excel is downloaded. |  |
| 5 | Maintain merchandise category sequence in excel | Open the downloaded file in Microsoft Excel. Merchandise Category sequence is rearranged as per user requirement in the excel and saved without any error.For example, exchange the merchandise categories between the first and second rows and select Save . | Changes, allowed and excel is saved. |  |
| 6 | Upload the excel file | In the Maintain Picking Sequence app, select Upload Picking Sequence | Once the excel is uploaded and appears in the app and sequence maintained in step 5. |  |
| 7 | Exit screen | Select Back |  |  |

### My Store Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The store manager gets an overview of the most critical information for their stores. The store managers analyse the information available on My Store Overview (F4674) cards and act accordingly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Retail Store Manager |  |  |
| 2 | Access app | Open My Store Overview (F4674) app | The My Store Overview (F4674) page’s content (cards) is displayed correctly.The layout that responds to screen size adjustment is accurate.The Manage card’s functionality (user settings or manage cards) works correctly. |  |
| 3 | View card - My Store | Have a look at the card - My Store | The store ID and description of the currently assigned store or user combination is displayed. |  |
| 4 | View card - Quick Links | Select each link contained in the card Quick LinksNote Assign Retail Store Associate role in order to view or navigate to links. | You can access all in-store functionality on card using Quick Links. |  |
| 5 | View card - Sales Performance | Have a look at the card - Sales PerformanceNote Sales figures appear only when sales or returns to the customers have been performed at the store. | The gross sales are displayed correctly (sales and returns) for each day of the current month.The sum of all gross sales per day is displayed correctly (sales and returns).The aggregated sales or returns and sales as per receipt or returns as per receipt are considered for calculating the figures. |  |
| 6 | View goods receipt today |  | All (sub)handling units expected and received for the current date are displayed.The diagram shows the expected deliveries for today according to their delivery status correctly (Open/partially/completed).The diagram changes according to the step-by-step posting approach, for example, if the status is ‘Open’, then post a subset of the overall amount of the delivery (status change’s to ‘Partially’ and diagram reacts accordingly). Finally post the whole amount (status should switch to ‘Completed’ and diagram also be updated accordingly).Only the top-level handling unit(s) can be posted when posting in trusted mode.Select the status of the status circle to start the Receive Products (F1248) app. |  |
| 7 | View overdue good receipts |  | All (sub) handling units are displayed correctly:where no goods receipt has been posted so faraccording to the selected time horizonThe information is displayed correctly (carton ID and ‘open since’ date = expected delivery date of corresponding handling unit)Select an item to start the Receive Products (F1248) app. |  |
| 8 | View upcoming goods receipts |  | The card Upcoming Goods Receipts shows all handling units (lowest HU level) within the next 5 days starting tomorrow. |  |

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
- related-to :: [[15-retail-operations/test-script-in-store-merchandise-management-3hq-ae-sap-s-4hana-cloud-p]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5FW_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 28,636 chars in the whole document
