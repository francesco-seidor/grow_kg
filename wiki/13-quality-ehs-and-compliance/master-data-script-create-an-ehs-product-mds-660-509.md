---
id: 13-quality-ehs-and-compliance/master-data-script-create-an-ehs-product-mds-660-509
title: "Master Data Script: Create an EHS Product - MDS (660) (660_S4CLD2608_Master_Data_EN_XX)"
description: English master data script (660) for creating an EHS product master record for waste management in SAP S/4HANA Cloud Public Edition 2608 via Manage Product Master Data (F1602).
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/ehs-waste-management-products]
aliases: [660_S4CLD2608_Master_Data_EN_XX]
keywords: [EHS Products and Chemical Compliance Materials for Waste, ehs product, product master data, master data scripts, waste management, business roles, 660]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/660_S4CLD2608_Master_Data_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-509
topic: 13-quality-ehs-and-compliance/ehs-waste-management-products
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Master Data Script: Create an EHS Product - MDS (660) (660_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/660_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **EHS Products and Chemical Compliance Materials for Waste** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create an EHS Product - MDS (660) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233904865)

[2 Prerequisites 3](#_Toc233904866)

[2.1 System Access 3](#_Toc233904867)

[2.2 Roles 3](#_Toc233904868)

[3 Overview Table 4](#_Toc233904869)

[4 Procedures 5](#_Toc233904870)

[4.1 Create an EHS Product Master Data - General Data 5](#_Toc233904871)

## Purpose

In this document you find a description of how to create an EHS Product master data record for your S/4 HANA system. The description includes those data segments that are relevant for the master data to work in a "usual" system environment. The reader mainly learns which data segments and fields usually need to be filled with input values. Fields that are not relevant for the scope of the S/4 HANA content delivery by SAP Best Practices are not described in this document although they may appear on the UI.

An EHS Product master record that is created as described here can be used to be later employed in Waste Management processes.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

| System | Details |
| --- | --- |
| System | Accessible via SAP Fiori Launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name | ID |
| --- | --- |
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST |

## Overview Table

This master record consists of several segments provided in the table below.

| Segment | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create an EHS Product Master Data - General Data](#unique_6) [page ] 5 | Master Data Specialist - Product Data | Manage Product Master Data (F1602) | An EHS Product is created. |

## Procedures

This section describes procedures for each segment or process step that is part of this master record.

### Create an EHS Product Master Data - General Data

Purpose

The following procedure provides instructions for creating an EHS product that can be later employed for EHS Waste Management processes.

Procedure (using Fiori Launchpad)

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using your user credentials. | The Start page appears. |  |
| 2 | Navigate to Product Master Data | Open the Manage Product Master Data app (F1602) | The Manage Product Master Data app is opened, and a list report is displayed. |  |
| 3 | Create a Product | In the Create dialog box, select Product. | The Create Master Data Record of a product is shown. |  |
| 4 | Select Master Data Records of a Product | On the same screen:Enter a <Product number> in the Product Number field.Choose a <Product type> in the Product Type field.Choose a <Product group> in the Product Groupfield.Enter a <Description> in the Description field.Choose a <Base unit> via the value help for the Base Unit field.Choose OK. | The product contains master data record information. |  |
| 5 | Save Information | Choose Save. | The Product is created. |  |

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
- related-to :: [[13-quality-ehs-and-compliance/crear-un-producto-ehs-mds-660-510]]
- related-to :: [[13-quality-ehs-and-compliance/criar-um-produto-ehs-mds-660-512]]
- related-to :: [[13-quality-ehs-and-compliance/ehs-mds-660-511]]
- related-to :: [[13-quality-ehs-and-compliance/ehs-mds-660-chinese-513]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/660_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 7,262 chars in the whole document
