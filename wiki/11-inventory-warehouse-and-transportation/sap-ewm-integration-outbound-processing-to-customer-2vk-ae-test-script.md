---
id: 11-inventory-warehouse-and-transportation/sap-ewm-integration-outbound-processing-to-customer-2vk-ae-test-script
title: SAP EWM Integration – Outbound Processing to Customer (2VK_AE) Test Script (2VK_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition test script for scope item 2VK: ship goods to customers from sales order through EWM picking and goods issue, with sample data and steps."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/ewm-outbound-to-customer]
aliases: [2VK_S4CLD2608_BPD_EN_AE]
keywords: [EWM Outbound Processing to Customer, ewm outbound processing, sales order creation, outbound delivery, warehouse tasks, warehouse picking, goods issue, initial stock, business roles, test scripts]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2VK_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-880
topic: 11-inventory-warehouse-and-transportation/ewm-outbound-to-customer
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# SAP EWM Integration – Outbound Processing to Customer (2VK_AE) Test Script (2VK_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2VK_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **EWM Outbound Processing to Customer** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | SAP EWM Integration – Outbound Processing to Customer (2VK_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232850856)

[2 Prerequisites 4](#_Toc232850857)

[2.1 Additional Manual Configuration 4](#_Toc232850858)

[2.2 System Access 4](#_Toc232850859)

[2.3 Roles 4](#_Toc232850860)

[2.4 Master Data, Organizational Data, and Other Data 5](#_Toc232850861)

[2.5 Business Conditions 6](#_Toc232850862)

[2.6 Preliminary Steps 7](#_Toc232850863)

[2.6.1 Check/Close Period for Material Master Records 7](#_Toc232850864)

[2.6.2 Set Initial Stock for Material 7](#_Toc232850865)

[2.6.3 Create User Settings for Transaction /SCWM/PRDO 7](#_Toc232850866)

[2.6.4 Check Stock Level for the EWM Products 8](#_Toc232850867)

[3 Overview Table 9](#_Toc232850868)

[4 Test Procedures 10](#_Toc232850869)

[4.1 Create Sales Order 10](#_Toc232850870)

[4.2 Create Delivery 11](#_Toc232850871)

[4.3 Check Outbound Delivery Orders in SAP EWM (Optional) 12](#_Toc232850872)

[4.4 Create Warehouse Tasks Manually in SAP EWM 13](#_Toc232850873)

[4.5 Pick Warehouse Orders in SAP EWM 14](#_Toc232850874)

[4.6 Post Goods Issue for Outbound Delivery Order in SAP EWM 15](#_Toc232850875)

[4.7 Check Outbound Delivery (Optional) 16](#_Toc232850876)

[5 Appendix 18](#_Toc232850877)

[5.1 Process Integration 18](#_Toc232850878)

[5.1.1 Preceding Processes 18](#_Toc232850879)

[5.1.2 Succeeding Processes 18](#_Toc232850880)

## Purpose

Overview

In this process, you ship ordered goods to external customers using SAP S/4HANA Cloud Public Edition integrated to SAP Extended Warehouse Management (EWM). This process starts with the creation of a sales order and an outbound delivery. The outbound delivery is replicated to the SAP EWM, where an outbound delivery order is created. This document serves as the starting point for the outbound processing within the warehouse. Warehouse tasks are created with reference to the outbound delivery order and the physical process for picking is executed. During the creation of warehouse tasks, the system determines the location for picking the stock and allocates the stock to the warehouse task. At the end of the process, the goods issue is posted. The goods issue information is transferred from SAP EWM to the SAP S/4HANA Cloud Public Edition system. Subsequent process steps such as billing can be executed accordingly.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/178d45fe87e9c4b3e3e8850f5c47ab6b)

### System Access

| System | Details |
| --- | --- |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

For nonstandard users, the following roles must be assigned to the system users testing this scenario:

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and supplier's, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | TG11 | Trading Good for Reg. Trading (MRP Planning) |  |
| Company Code | 3310 | 3310 |  |
| Sales Organization | 3310 | Dom. Sales Org |  |
| Plant | 3310 |  |  |
| Supply Chain Unit | YWAREHOUSE-3330 |  |  |
| Storage Location | 333D |  | Decentral EWM received on dock Receiving |
| Storage Location | 333S |  | Decentral EWM available for sales Receiving |
| Warehouse | 333 |  |  |
| EWM Warehouse | 3330 |  |  |
| Division | 00 |  |  |
| Distribution Channel | 00 |  |  |
| Shipping Point | 3310 |  |  |
| Payer | 33100003 | Customer domestic 03 |  |
| Ship-to party | 33100003 | Domestic UAE Customer 3 |  |
| Sold to party | 33100003 | Domestic UAE Customer 3 |  |
| Ent. To Dispose | 33413310 |  |  |

For more information on creating master data objects, see the following:

| MDS | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BND | Create Customer Master - MDS |
| 2YX | Create Customer-Material Info Record - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| 2VJ - SAP EWM Integration – Inbound Processing from Supplier | Run through the inbound processing to make sure you have enough stock for the outbound processing. |
| 2YL - SAP EWM Integration – Warehouse Stock Handling | Alternatively (or in addition to the inbound processing), you complete an initial stock upload as described in the test script. |

### Preliminary Steps

#### Check/Close Period for Material Master Records

External Process

For this activity, run the following steps from the (BNZ) to close MM period and open new posting period.

Closing MM Period and Opening New Posting Period.

#### Set Initial Stock for Material

External Process

For this activity, run the steps described in the Business Conditions to create initial stock in the warehouse for the material used in this process.

#### Create User Settings for Transaction /SCWM/PRDO

Use

In this step, you can set up user settings that are necessary for transaction: /SCWM/PRDO.

Procedure

1. Access the transaction using one of the following navigation options:

| Transaction Code | Easy Access Menu(SAP EWM) |
| --- | --- |
| /SCWM/PRDO | SCM Extended Warehouse Management > Extended Warehouse Management > Delivery Processing > Outbound Delivery > Maintain Outbound Delivery Orders |

1. In the dialog box, make the following entries:

| Field Name | Description | User Action and Values | Comment |
| --- | --- | --- | --- |
| Warehouse Number |  | 3330 |  |
| Shipping Office |  | YWAREHOUSE-3330 |  |
| Ent. To Dispose |  | 33413310 |  |

1. Choose Continue (Enter).

|  |
| --- |
| Note If the dialog box does not appear, you may choose Default Values (F5) |

#### Check Stock Level for the EWM Products

Procedure

1. Access the transaction using one of the following navigation options:

| Transaction Code | Easy Access Menu(SAP EWM) |
| --- | --- |
| /SCWM/MON | SCM Extended Warehouse Management > Extended Warehouse Management > Monitoring > Warehouse Management Monitor |

1. In the Warehouse Management Monitor dialog box, make the following entries:

| Field Name | Description | User Action and Values | Comment |
| --- | --- | --- | --- |
| Warehouse Number |  | 3330 |  |
| Monitor |  | SAP | SAP Cross Industries Warehouse |

1. Choose Execute (F8).
2. On the hierarchy in the left screen area, choose Stock and Bin > Available Stock
3. On the /SCWM/SAPLSTOCK_OVERVIEW_MON screen, make the following entries:

| Field Name | Description | User Action and Values | Comment |
| --- | --- | --- | --- |
| Product Number |  | TG11 |  |

## Overview Table

The scope item 2VK consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction / App | System | Expected Results |
| --- | --- | --- | --- | --- |
| [Create Sales Order](#unique_13) [page ] 10 | Internal Sales Representative | Create Sales Orders (F3893) | SAP S/4HANA | The following system message appears:Sales order entry to create. |
| [Create Delivery](#unique_14) [page ] 11 | Shipping Specialist | Create Outbound Delivery - With Order Reference (VL01N) | SAP S/4HANA | The following system message appears: Outbound Delivery Order created under the number <your number>. |
| [Check Outbound Delivery Orders in SAP EWM (Optional)](#unique_15) [page ] 12 |  | /SCWM/PRDO | SAP Extended Warehouse Management |  |
| [Create Warehouse Tasks Manually in SAP EWM](#unique_16) [page ] 13 |  | /SCWM/PRDO | SAP Extended Warehouse Management |  |
| [Pick Warehouse Orders in SAP EWM](#unique_17) [page ] 14 |  | /SCWM/TO_CONF | SAP Extended Warehouse Management |  |
| [Post Goods Issue for Outbound Delivery Order in SAP EWM](#unique_18) [page ] 15 |  | /SCWM/PRDO | SAP Extended Warehouse Management |  |
| [Check Outbound Delivery (Optional)](#unique_19) [page ] 16 | Shipping Specialist | Display Outbound Delivery (VL03N) | SAP S/4HANA | On the Overall Status - Delivery table, check that the Overall Goods Movement Status is C Completely processed.In the Delivery Item Status (All Items) table, check that the Goods Movement Status for the items is C Completely processed. |

## Test Procedures

This section describes procedures for each process step that belongs to this scope item.

If you want to create Sales Order you need to ensure enough stock via Preliminary steps. If you want to create Pallet quantity you have to ensure that Storage Type Y001 has materials available. If you want to create Sales Orders partial quantity like 1 PC then please ensure to have material in Storage type Y002.

To have materials there, can be ensured via 3 alternative steps.

1. Inbound
2. Initial Stock upload
3. Replenishment

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
| 1 | Log on to SAP Fiori launchpad | Log on to the SAP Fiori launchpad as a Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the Sales Order Worklist | Open Create Sales Orders - VA01 (VA01). | The Create Sales Document screen displays. |  |
| 3 | Enter the Order Type OR (Standard Order) | On the Create Sales Document, make the following entries. Choose Enter.Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00Choose Continue. | Create Standard Order: Overview screen displays. |  |
| 4 | Enter Order Details | On the Create Standard Order: Overview screen, make the following entries:Sold To Party:33100003Ship To Party: 33100003Cust. Reference: <Reference number>. Enter a customer purchase order number as reference.Material Number: TG11Quantity: 1UoM: PALChoose Save. |  |  |
| 5 | Choose Continue | If necessary, choose Continue in the dialog box Open quotations for item. |  |  |
| 6 | Save Document | Make a note of the sales order number: __________. | The order is saved and the order confirmation is displayed. |  |

### Create Delivery

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
| 1. | Log on to SAP Fiori launchpad | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2. | Access the App | Open Create Outbound Delivery - With Order Reference (VL01N) . | The Create Outbound Delivery - With Order Reference screen displays. |  |
| 3. | Search Sales Order | Make the following entries and choose Go:Shipping point: 3310Order: Sales order number created previouslyChoose Continue. | The Delivery Create: Overview screen displays. |  |
| 4. | Choose Another Header | Choose header Picking next to Item Overview. |  |  |
| 5. | Change an Entry | Change on column SLoc the Storage Location to 333S. |  |  |
| 6. | Create Save | Choose your sales order items and choose Save. | Delivery number is visible. |  |

|  |
| --- |
| Note Depending on the scope item settings, the availability is checked at the delivery creation using the available inventory and replenishment lead time. Without sufficient stock, the created delivery has no confirmed quantities, and therefore does not start the warehouse management picking process. As soon as there is sufficient stock for delivery creation, the system creates a delivery with the starting of the picking process in warehouse management. |

To avoid open deliveries, ensure that there is sufficient inventory quantity at the time of delivery creation.

|  |
| --- |
| Note With the Analyze Delivery Logs (F0870A) app, you can display an overview about the logs of all the deliveries, which have been created in your system. You can filter by, for example, Created by and other additional settings. If you choose the arrow on the right of each delivery log entry, you can display the exact message type and text and also the related sales document. |

### Check Outbound Delivery Orders in SAP EWM (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Transaction Code | SAP EWM Menu |
| --- | --- |
| /SCWM/PRDO | SCM Extended Warehouse Management > Extended Warehouse Management > Delivery Processing > Outbound Delivery > Maintain Outbound Delivery Order |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access Transaction | Access the transaction using one of the navigation options above. | The Outbound Delivery Order- Warehouse No.3330screen appears. |  |
| 2 | Search Outbound Delivery Order | Choose Open Advanced SearchMake the following entries:ERP Document: Previous Delivery NumberChoose Advanced Search. |  |  |
| 3 | Choose Button | Choose Close Advanced Search. |  |  |
| 4 | Note the Outbound Delivery | Note down the Document number if you are verified it is your Material. |  |  |

### Create Warehouse Tasks Manually in SAP EWM

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Transaction Code | SAP EWM Menu |
| --- | --- |
| /SCWM/PRDO | SCM Extended Warehouse Management > Extended Warehouse Management > Delivery Processing > Outbound Delivery > Maintain Outbound Delivery Order |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access Transaction | Access the transaction using one of the navigation options above. | The Maintain Outbound Delivery Order screen appears. |  |
| 2 | Search | Choose Open Advanced Search.Make the following entries:ERP Document: Previous Delivery NumberChoose Advanced Search. | Your delivery displays. |  |
| 3 | Navigate to Warehouse Tasks | Choose Outbound Delivery order and use the menu Outbound Delivery Order > Follow-on Functions > Warehouse Task on the upper left screen. | Create Warehouse Task screen displays. |  |
| 4 | Create Warehouse tasks manually | Select all warehouse requests and choose Create + Save Warehouse Task. | The system confirms that warehouse tasks are created. |  |
| 5 | Warehouse Order Verification | The warehouse order creation with a number shows on the left corner.Note this number down. |  |  |

### Pick Warehouse Orders in SAP EWM

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Transaction Code | SAP EWM Menu |
| --- | --- |
| /SCWM/TO_CONF | SCM Extended Warehouse Management > Extended Warehouse Management > Execution > Confirm > Warehouse Task |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access Transaction | Access the transaction using one of the navigation options above. | The Confirm Warehouse Task in Warehouse Number screen is displayed. |  |
| 2 | Choose | Fill in your warehouse order number noted down from previous step.Choose Execute Search. | Your warehouse task displays. |  |
| 3 | Choose | Choose Confirm + Save | The warehouse material document number is created now.Note down the number. |  |

### Post Goods Issue for Outbound Delivery Order in SAP EWM

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Transaction Code | SAP EWM Menu |
| --- | --- |
| /SCWM/PRDO | SCM Extended Warehouse Management > Extended Warehouse Management > Delivery Processing > Outbound Delivery > Maintain Outbound Delivery Order |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access Transaction | Access the transaction using one of the navigation options above. | The Maintain Outbound Delivery Order screen appears. |  |
| 2 | Choose | Choose your ODO created in step Check Outbound Delivery Orders in SAP EWM. |  |  |
| 3 | Check | Check Picking Status. | Status should be completed. |  |
| 4 | Post Goods Issue | Choose Goods Issue. | The Check Goods Issue and the Check Picking Status should be set to Completed. |  |
| 5 | Outbound Delivery Order | A message shows that your Outbound Delivery is completed. |  |  |

### Check Outbound Delivery (Optional)

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
| 1 | Log on to SAP Fiori launchpad | Log on to the SAP Fiori launchpad using the role Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App Display Outbound Delivery | Open Display Outbound Delivery (VL03N). |  |  |
| 3 | Set your Outbound Delivery | Fill in your outbound delivery number you created in step Create Delivery.Continue. | The Delivery Overview displays. | This outbound delivery you have noted down in step Create Delivery. |
| 4 | Go to Status Overview | Check if the Packing Status and Goods Movement reflect the Status C (Green). |  | For partial quantity, no Packing Status is visible. |
| 5 | Check HU | Check if your ODO in EWM with handling unit informations is without handling unit information in SAP S/4HANA. |  | The purpose is to handle HU only in EWM. |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

You may first have completed the following processes and conditions before you start with the test steps:

| Business Condition | Comment |
| --- | --- |
| SAP EWM Integration – Inbound Processing from Supplier(2VJ) | To ensure that there is enough stock for use in the outbound process, you bring stock into the warehouse using inbound processing. |
| SAP EWM Integration – Warehouse Stock Handling(2YL) | Alternatively (or in addition to the inbound processing), you complete an initial stock upload as described in Initial Stock Upload test script. |
| Create New Open MM Posting Period - MDS(BNZ) | You have completed the step described in the Open New MM Period master data script. Posting Period is up to date. |

#### Succeeding Processes

The process to be tested in this test script is part of a chain of integrated processes. After completing the activities in this test script, the billing status in the Outbound Delivery is A - Not yet processed. You can continue testing the following business process BD9 with the business role Billing Clerk to complete the billing step until the billing status is C - Completed.

| Process | Business Condition |
| --- | --- |
| Sell from Stock(BD9) | Complete all activities described in the test script of the scope item (Section Billing) using the master data from this document. |

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
- related-to :: [[11-inventory-warehouse-and-transportation/test-script-warehouse-outbound-processing-3bs-ae-sap-s-4hana-cloud-pub]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2VK_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 27,484 chars in the whole document
