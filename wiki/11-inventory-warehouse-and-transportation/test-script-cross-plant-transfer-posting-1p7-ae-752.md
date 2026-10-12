---
id: 11-inventory-warehouse-and-transportation/test-script-cross-plant-transfer-posting-1p7-ae-752
title: "Test Script: Cross-Plant Transfer Posting (1P7_AE) (1P7_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 1P7_AE: one-step and two-step cross-plant stock transfer posting, with prerequisites and test steps."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/intracompany-stock-transfers]
aliases: [1P7_S4CLD2608_BPD_EN_AE]
keywords: [Stock Transfers Within a Company Code, cross-plant stock transfer, one-step stock transfer, two-step stock transfer, stock status check, stock in transit, initial stock posting, business roles, master data, mm posting period]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1P7_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-752
topic: 11-inventory-warehouse-and-transportation/intracompany-stock-transfers
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Cross-Plant Transfer Posting (1P7_AE) (1P7_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1P7_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Stock Transfers Within a Company Code** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Cross-Plant Transfer Posting (1P7_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232847480)

[2 Prerequisites 3](#_Toc232847481)

[2.1 Roles 3](#_Toc232847482)

[2.2 System Access 3](#_Toc232847483)

[2.3 Master Data, Organizational Data, and Other Data 3](#_Toc232847484)

[2.4 Additional Manual Configuration 5](#_Toc232847485)

[2.5 Business Conditions 5](#_Toc232847486)

[2.6 Preliminary Steps 5](#_Toc232847487)

[2.6.1 Opening New MM Period 5](#_Toc232847488)

[2.6.2 Creating Stock in Supplying Plant 6](#_Toc232847489)

[3 Overview Table 7](#_Toc232847490)

[4 Test Procedures 8](#_Toc232847491)

[4.1 Check Stock Status 8](#_Toc232847492)

[4.2 One Step Stock Transfer 9](#_Toc232847493)

[4.3 Two-Step Stock Transfer 10](#_Toc232847494)

[4.3.1 Transfer Posting – Remove from Storage 10](#_Toc232847495)

[4.3.2 Checking Status of Stock Transfer 11](#_Toc232847496)

[4.3.3 Transfer Posting – Place in Storage 12](#_Toc232847497)

[4.4 Check Stock Status 14](#_Toc232847498)

## Purpose

Overview

This scope item includes two processes for stock transfer between two plants in a company code: One-step stock transfer posting and two-step stock transfer posting.

A one-step transfer posting at the issuing plant moves the stock immediately from the issuing plant to the receiving plant. This is useful if the distance between the two plants is short and when there is no need for stock-in-transit stock overview.

A two-step stock transfer posting is needed for goods movement to remove stock from the supply plant and place it into stock in the receiving plant.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |

### System Access

| System | Details |
| --- | --- |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 | Shop floor w/o lean WM |
| Storage Location | 331B | Std. storage 2 | Shop floor w/o lean WM |
| Storage Location | 331C | Raw mat. stoloc. |  |
| Plant | 3320 | Plant 2 AE | Flex.Org App or Set Up Organizational (SAP Central Business Configuration) extensionNote The second set of organization entity IDs here is an example. In an evaluation project of the SAP Central Business Configuration environment, the ID follows the naming rule described in [Using the Set Up Organizational Structure App](https://help.sap.com/docs/CENTRAL_BUSINESS_CONFIGURATION/55c9333eed324cd284f6c4e5dab8462f/d020ff461d504421bcc55d87cbc0ae57.html). |
| Storage Location | 332A | Std. storage 1 | Flex.Org App or Set Up Organizational (SAP Central Business Configuration) extensionShop floor w/o lean WM |
| Storage Location | 332B |  | Flex.Org App or Set Up Organizational (SAP Central Business Configuration) extensionShop floor w/o lean WM |
| Storage Location | 332C |  | Flex.Org App or Set Up Organizational (SAP Central Business Configuration) extensionShop floor w/o lean WM |
| Material | TG11 | Trading Good for Reg. Trading (MRP planning) |  |
| no Serial no.; no batch | See sections [Business Conditions](#unique_6) [page ] 5 and Preliminary Steps. |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/2fc421a3568490218a1c542abe539d55)

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the master data script. Posting Period is up to date. |

### Preliminary Steps

#### Opening New MM Period

External Process

For this activity, run the following step from the Create New Open MM Posting Period - MDS (BNZ) to close MM period and open new posting period.

Closing MM Period and Opening New Posting Period

#### Creating Stock in Supplying Plant

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post initial stock for materials, for example, TG11.

This step is obsolete if enough stock is available. Check stock availability with App Stock Single Material, TG11 Plant 1 AE 3310, and storage location Std. storage 1 331A.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Stock (F1062). | The Manage Stock screen displays. |  |
| 3 | Input Material | Make the following entries and press Enter:Material: TG11Plant: Plant 1 AE 3310 | The stock overview for the material displays. |  |
| 4 | Select Stock | Choose the icon beside the stock that you want to add initial stock, for example:Storage Location: Std. storage 1 331AUnrestricted-Use Stock | A dialog box opens. The Storage Location, Stock Type, and Current Quantity are displayed according to your entries in the previous steps. |  |
| 5 | Add Initial Entry | Make the following entries and choose Post:Document Date: todayPosting Date: todayStock Change: Initial EntryQuantity: X PC | The system displays the following message. The stock has been added.1 document has been created: Material Document XXXXXXXXXX/20XX |  |

## Overview Table

This scope item consists of several process steps that are listed in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/APP | Expected Results |
| --- | --- | --- | --- |
| [One Step Stock Transfer](#unique_11) [page ] 9 | Inventory Manager | Transfer Stock - Cross-Plant (F1957) | Stock is moved physically and logically in the system |
| [Transfer Posting – Remove from Storage](#unique_12) [page ] 10 | Inventory Manager | Transfer Stock - Cross-Plant (F1957) | Stock is moved physically and logically in the system |
| [Checking Status of Stock Transfer](#unique_13) [page ] 11 | Inventory Manager orWarehouse Clerk | Stock - Single Material (F1076) | Stock overview of the material and of the stocks in stock transfer at the receiving point is displayed, |
| [Transfer Posting – Place in Storage](#unique_14) [page ] 12 | Inventory Manager | Transfer Stock - Cross-Plant (F1957) | Stock is moved physically and logically in the system |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Check Stock Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check the stock status for material in plant, storage location, and stock type.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Stock - Single Material (F1076). | The Stock- Single Material screen displays. |  |
| 3 | Enter Material | Enter the following entry in the Material field.Select the material from the interactive value help.Material: TG11 | The Stock Overview for the Material shows. |  |
| 4 | Change View | Option 1: Choose table view icon;Or option 2: Change to a graphical view by the bar chart icon. | You can check stock status in each plant, storage location, stock type. |  |
| 5 | Back to Launch Pad | Select Home to go back to the SAP Fiori launchpad. | The SAP Fiori launchpad displays. |  |

### One Step Stock Transfer

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to transfer stock immediately from the unrestricted-use stock of the issuing plant to the unrestricted-use stock of the receiving plant. The transfer posting is valuated at the valuation price of the material in the issuing plant.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Lon on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Transfer Stock - Cross-Plant (F1957). | The Transfer Stock - Cross-Plant screen displays. |  |
| 3 | Screen Settings | Make the following entries and press Enter.Material: TG11 | The Stock Overview for the material is shown. |  |
| 4 | Enter Material Data | Choose the icon beside the stock that you want to issue stock, for example:Plant: Plant 1 AE 3310Unrestricted-Use StockChoose the icon beside the stock that you want to receive stock, for example:Plant: Plant 2 AE 3320Unrestricted-Use Stock | A dialog box opens. The Issuing Plant, Issuing Storage Location, Stock Type, Current Quantity, Receiving Plant, Receiving Storage Location, Stock Type, and Current Quantity are displayed according to your entries in the previous steps. |  |
| 5 | Post Transfer | Make the following entries:Issuing Storage Location: Std. storage 1 331AReceiving Storage Location: Std. storage 1 332ADocument Date: <today>Posting Date: <today>Quantity: X PCChoose Post. | The system displays Material document XXX created. The stock has been transferred from plant 3310 to plant 3320 in one step. |  |

### Two-Step Stock Transfer

#### Transfer Posting – Remove from Storage

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to use the two-step procedure to monitor stocks while they are in transit. Once you have posted the goods issue form the issuing point, the stock is located in stock transfer at the receiving point, and it is managed as such in the system.

This enables the quantity "on the way" to be monitored.

The transfer posting is valuated at the valuation price of the material in the issuing plant.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Transfer Stock - Cross-Plant (F1957). | The Transfer Stock - Cross-Plant (F1957) screen displays. |  |
| 3 | Screen Settings | Make the following entries and press Enter.Material: TG11 | The Stock Overview for the material shows. |  |
| 4 | Enter Material Data | Choose the icon beside the stock that you want to issue stock, for example:Plant: Plant 1 AE 3310Unrestricted-Use StockChoose the icon beside the stock that you want to receive stock, for example:Plant: Plant 2 AE 3320Stock Transfer (Plant) | A dialog box opens. The Issuing Plant, Issuing Storage Location, Stock Type, Current Quantity; Receiving Plant, Stock Type and Current Quantity display according to your entries in the previous steps. |  |
| 5 | Post Transfer | Make the following entries:Issuing Storage Location: Std. storage 1 331ADocument Date: <today>Posting Date: <today>Quantity: X PCChoose Post. | The system displays Material document XXX created. The stock has been transferred from plant 3310 to Stock transfer at plant 3320. |  |

#### Checking Status of Stock Transfer

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The system displays an overview of the material and the stocks in stock transfer that have left the supplying plant and is located in stock transfer at the receiving plant.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Open Stock Overview | Open Stock - Single Material (F1076). | The Stock Single Material screen displays. |  |
| 3 | Enter Material | Enter the following entry in the Material field.Select the material from the interactive value help.Material: TG11 | The Stock Overview for the material is shown. |  |
| 4 | Change View | Option 1: Choose the table view icon;Or option 2: Change to a graphical view by the bar chart icon. | You can find there is newly added amount in column Transfer Stock (Plant) for Plant 2 AE 3320.A Bar Chart for the stock by Plant/Storage Location is displayed. You can find there is Transfer Stock (Plant) for receiving plant displayed in grey color. |  |
| 5 | Back to Launchpad | Choose the Home button to go back to the SAP Fiori launchpad. | The SAP Fiori launchpad displays. |  |

#### Transfer Posting – Place in Storage

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to use the two-step procedure to monitor stocks while they are in transit. Once you have posted the goods issue form the issuing point, the stock is located in stock transfer at the receiving point, and it is managed as such in the system.

This enables the quantity "on the way" to be monitored.

The transfer posting is valuated at the valuation price of the material in the issuing plant.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Transfer Stock - Cross-Plant (F1957). | The Transfer Stock - Cross-Plant (F1957) screen displays. |  |
| 3 | Screen Settings | Make the following entries and press Enter:Material: TG11 | The Stock Overview for the material shows. |  |
| 4 | Enter Material Data | Choose the icon beside the stock that you want to issue stock, for example:Plant: Plant 2 AE 3320Stock Transfer (Plant)Choose the icon beside the stock that you want to Receive stock, for example:Plant: Plant 2 AE 3320Unrestricted-Use Stock | A dialog box opens. The Issuing Plant, Stock Type, Current Quantity; Receiving Plant, Receiving Storage Location, Stock Type and Current Quantity display according to your entries in the previous steps. |  |
| 5 | Post Transfer | Make the following entries:Receiving Storage Location: Std. storage 1 332ADocument Date: <today>Posting Date: <today>Quantity: X PCChoose Post. | The system displays Material document XXX created. The stock has been transferred from Stock transfer to Unrestricted-Use Stock at Plant 3320. |  |

### Check Stock Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check the stock status for material in plant, storage location, and stock type.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Stock - Single Material (F1076). | The Stock- Single Material screen displays. |  |
| 3 | Enter Material | Enter the following entry in the Material field.Select the material from the interactive value help.Material: TG11 | The Stock Overview for the material shows. |  |
| 4 | Change View | Option 1: Choose the table view icon;Or option 2: Change to a graphical view by the bar chart icon. | You can check stock status in each plant, storage location, stock type |  |
| 5 | Back to Launchpad | Choose Home to go back to the SAP Fiori launchpad. | The SAP Fiori launchpad displays. |  |

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
- related-to :: [[11-inventory-warehouse-and-transportation/test-script-sap-ewm-integration-stock-transport-orders-2vl-ae-sap-s-4h]]
- related-to :: [[11-inventory-warehouse-and-transportation/test-script-stock-transfer-with-delivery-bme-ae-sap-s-4hana-cloud-publ]]
- related-to :: [[11-inventory-warehouse-and-transportation/test-script-stock-transfer-without-delivery-bmh-ae-sap-s-4hana-cloud-p]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1P7_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 24,459 chars in the whole document
