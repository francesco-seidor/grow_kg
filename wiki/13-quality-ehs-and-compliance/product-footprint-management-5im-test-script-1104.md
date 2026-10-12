---
id: 13-quality-ehs-and-compliance/product-footprint-management-5im-test-script-1104
title: Product Footprint Management (5IM) Test Script (5IM_S4CLD2608_BPD_EN_XX)
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 5IM: viewing product footprints from SAP Sustainability Footprint Management, incl. purchase requisition CO2e."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/product-footprint-and-carbon-emissions]
aliases: [5IM_S4CLD2608_BPD_EN_XX]
keywords: [Product Footprints and Carbon Emission Quantities, product footprint management, view product footprints, smart link navigation, purchase requisition footprint, sustainability footprint management, business roles, test procedures, 5IM]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5IM_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1104
topic: 13-quality-ehs-and-compliance/product-footprint-and-carbon-emissions
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Product Footprint Management (5IM) Test Script (5IM_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5IM_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Product Footprints and Carbon Emission Quantities** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Product Footprint Management (5IM) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232824768)

[2 Prerequisites 3](#_Toc232824769)

[2.1 System Access 3](#_Toc232824770)

[2.2 Roles 3](#_Toc232824771)

[2.3 Additional Manual Configuration 3](#_Toc232824772)

[2.4 Business Conditions 4](#_Toc232824773)

[3 Overview Table 5](#_Toc232824774)

[4 Test Procedures 6](#_Toc232824775)

[4.1 Search and View Product Footprints 6](#_Toc232824776)

[4.2 Navigate to View Product Footprints app via Smart Link Navigation 7](#_Toc232824777)

[4.3 View Product Footprint of Purchase Requisition Item 9](#_Toc232824778)

## Purpose

Overview

This scope item enables you to integrate product footprints calculated in SAP Sustainability Footprint Management on SAP Business Technology Platform. Product footprints can be either viewed or integrated into end-to-end processes of SAP S/4HANA Cloud Public Edition.

This scope item enables you to integrate product footprints calculated in SAP Sustainability Footprint Management on SAP Business Technology Platform. Product footprints can be either viewed or integrated into end-to-end processes of SAP S/4HANA Cloud Public Edition.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

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
| Administrator - Product Footprint Management | SAP_BR_ADMIN_SUS_PFM | Product Footprint Management | SAP_BR_ADMIN_SUS_PFM |  |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_BR_PURCHASER |  |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/4336245147f00f87eba0a178b3aa0082)

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 5IM – Product Footprint Management | The integration with SAP Sustainability Footprint Management is set up according to the set-up instructions of this scope item, as well as the connectivity information provided for [SAP Sustainability Footprint Management](https://help.sap.com/viewer/b3e39aed098c41a2b0d49db0caf80711/LATEST/en-US/3ac9633b2f724eab9e2ac126cea7288c.html). Product Footprints are published from SAP Sustainability Footprint Management to SAP S/4HANA Cloud Public Edition. |

## Overview Table

This scope item consists of several process steps provided in the table below.

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Search and View Product Footprints | Administrator - Product Footprint Management | View Product Footprints | The app is available and can be accessed. It is possible to search for product footprints by different filter criteria. Footprints are displayed and can be viewed in the app. |
| Navigate to View Product Footprints app via Smart Link Navigation | PurchaserAdministrator - Product Footprint Management | Manage Purchase Requisition - Professional | It is possible to navigate to the View Product Footprints app and display the Product Footprint of a Product via Smart Link of a Product. |
| View Product Footprint of Purchase Requisition Item | Purchaser | Manage Purchase Requisition - Professional | The absolute CO2e footprint of a Purchase Requisition Item is calculated and displayed on the Purchase Requisition Item screen. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Search and View Product Footprints

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to search and view product footprints for a plant and product, or plant, product, and supplier.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Administrator - Product Footprint Management. |  |  |
| 2 | Access App | Open View Product Footprints (F5783). | The View Product Footprints (F5783) app opens. |  |
| 3 | View Product Footprints by Product | On the entry screen of the View Product Footprints app, select a Product for which a product footprint has been published to SAP S/4HANA Cloud Public Edition for at least one plant.Choose Go. | A list showing one or multiple product footprints for the selected product is displayed. |  |
| 4 | View Product Footprints by Plants | On the entry screen of the View Product Footprints app, select a Plant that has products assigned for which a product footprint has been published to SAP S/4HANA Cloud Public Edition.Choose Go. | A list showing one or multiple product footprints for the selected plant is displayed. |  |
| 5 | View Product Footprints by different filter criteria | On the entry screen of the View Product Footprints app, select different filter criteria as well as combinations of the following filter criteria (some of the filters can be added to the filter bar via Adapt Filters):ProductProduct GroupPlantSupplierCompany CodeQuantityReference BasisCalculated ByChoose Go. | A list showing one or multiple product footprints according to the filter criteria is displayed. |  |
| 6 | View Product Footprints by Key Date | Product footprints have a validity period that is defined by Valid From Date and Valid To Date of a product footprint. Use the Key Date filter to display all product footprints that are valid for the selected Key Date. Also use the filter in combination with other filters that have been applied in the previous step.Choose Go.Note: The Key Date is a mandatory filter. By default, the current date is applied as filter.By default, only the Valid From Date is displayed in the Footprints table. The Valid To Date can be added as additional table column via the View Settings. | A list is displayed showing one or multiple product footprints that are valid on the selected key date. |  |

### Navigate to View Product Footprints app via Smart Link Navigation

|  |
| --- |
| Note For this test you need a user with both roles Administrator - Product Footprint Management and Purchaser. |

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to navigate to the View Product Footprints app and view a Product Footprint via Smart Link Navigation.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Purchaser. |  |  |
| 2 | Access App | Open Manage Purchase Requisitions - Professional. | The Manage Purchase Requisitions – Professional (F2229) app opens. |  |
| 3 | Create Purchase Requisition | In the Manage Purchase Requisitions – Professional app, choose Create. | The screen to create a new Purchase Requisition is displayed. |  |
| 4 | Create Purchase Requisition Item | On the new Purchase Requisition, in the Purchase Requisition Items table, choose Create. On the selection menu, select Material. | The screen to create a new Purchase Requisition Item is displayed. |  |
| 5 | Provide details of the Purchase Requisition Item | On the Purchase Requisition Item screen, provide at least the following details:PlantMaterialQuantityDelivery DatePurchasing GroupDo not enter a Desired Supplier yet. Note: For the provided Material and Plant, a Product Footprint must be published to SAP S/4HANA Cloud Public Edition.Choose Apply. | The Purchase Requisition Item is created with the provided details.The screen to create a new Purchase Requisition is displayed. |  |
| 6 | Save Purchase Requisition | On the Purchase Requisition screen, select Create. | The Purchase Requisition is created. The Purchase Requisition screen is displayed. |  |
| 7 | Add View Product Footprints app to the Smart Link menu of the Material. | On the Purchase Requisition screen, in the Purchase Requisition Items table, select the Material. In the Smart Link menu for the Material, choose More Links. On the Define Link List screen, select the check box for View Product Footprints. Choose OK.Note: This step is only required in case the Smart Link for the View Product Footprints app has not been added before. | The View Product Footprints app is added to the Smart Link menu. |  |
| 8 | Display Product-Plant Footprint of the Material of the Purchase Requisition Item. | On the Purchase Requisition screen, in the Purchase Requisition Items table, select the Material. In the Smart Link menu for the Material, select View Product Footprints. | The View Product Footprints (F5783) app opens and displays the Product Footprint of the selected Material and Plant. |  |
| 9 | Navigate back to the Purchase Requisition | On the View Product Footprints app, use the SAP Fioriback navigation button in the upper left corner of the shell bar. | The Purchase Requisition screen is displayed. |  |
| 10 | Add a Desired Supplier to the Purchase Requisition Item | On the Purchase Requisition screen, choose Edit. On the Purchase Requisition Item table, enter a Desired Supplier and choose Save.Note: For the provided Material, Plant, and Supplier, a Product Footprint must be published to SAP S/4HANA Cloud Public Edition. | The Purchase Requisition is saved. The Purchase Requisition screen is displayed. |  |
| 11 | Display Product-Plant-Supplier Footprint of the Material of the Purchase Requisition Item. | On the Purchase Requisition screen, in the Purchase Requisition Items table, select the Material. In the Smart Link menu for the Material, select View Product Footprints. | The View Product Footprints (F5783) app opens and displays the Product Footprint of the selected Material, Plant, and Supplier. |  |

### View Product Footprint of Purchase Requisition Item

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to view the absolute Product Footprint of a Purchase Requisition Item.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Purchaser. |  |  |
| 2 | Access App | Open Manage Purchase Requisitions – Professional. | The Manage Purchase Requisitions – Professional (F2229) app opens. |  |
| 3 | Display Purchase Requisition | In the Manage Purchase Requisitions – Professional app, search for the Purchase Requisition created in the previous step. Select the Purchase Requisition. | The Purchase Requisition screen is displayed. |  |
| 4 | Display Purchase Requisition Item | On the Purchase Requisition screen, select a Purchase Requisition Item. | The Purchase Requisition Item screen is displayed. The absolute CO2e Footprint of the Purchase Requisition Item is displayed on the header area of the screen. |  |

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
- related-to :: [[13-quality-ehs-and-compliance/product-related-carbon-emission-quantities-6vn-ae-test-script-1192]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5IM_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 16,390 chars in the whole document
