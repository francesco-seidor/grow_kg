---
id: 13-quality-ehs-and-compliance/create-an-ehs-chemical-compliance-information-material-mds-65z-503
title: Create an EHS Chemical Compliance Information Material - MDS (65Z) (65Z_S4CLD2608_Master_Data_EN_XX)
description: "English master data script (MDS 65Z) for creating an EHS Chemical Compliance Information material via Manage Material Data (F4864), for later Waste Management use."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/ehs-waste-management-products]
aliases: [65Z_S4CLD2608_Master_Data_EN_XX]
keywords: [EHS Products and Chemical Compliance Materials for Waste, chemical compliance material, master data script, ehs waste management, business roles, environmental manager, 65Z]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/65Z_S4CLD2608_Master_Data_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-503
topic: 13-quality-ehs-and-compliance/ehs-waste-management-products
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Create an EHS Chemical Compliance Information Material - MDS (65Z) (65Z_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/65Z_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **EHS Products and Chemical Compliance Materials for Waste** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create an EHS Chemical Compliance Information Material - MDS (65Z) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233904806)

[2 Prerequisites 3](#_Toc233904807)

[2.1 System Access 3](#_Toc233904808)

[2.2 Roles 3](#_Toc233904809)

[3 Overview Table 4](#_Toc233904810)

[4 Procedures 5](#_Toc233904811)

[4.1 Create an EHS Chemical Compliance Information Material Master Data - General Data 5](#_Toc233904812)

## Purpose

In this document you find a description of how to create an EHS Chemical Compliance Information Material master data record for your S/4 HANA system. The description includes those data segments that are relevant for the master data to work in a "usual" system environment. The reader mainly learns which data segments and fields usually need to be filled with input values. Fields that are not relevant for the scope of the S/4 HANA content delivery by SAP Best Practices are not described in this document although they may appear on the UI.

An EHS Chemical Compliance Information Material master record that is created as described here can be used to be later employed in Waste Management processes.

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

| Name (Role Template) | ID (Role Template) |
| --- | --- |
| Environmental Manager | SAP_BR_EHS_ENV_MGMT |

## Overview Table

This master record consists of several segments provided in the table below.

| Segment | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create an EHS Chemical Compliance Information Material Master Data - General Data](#unique_6) [page ] 5 | Environmental Manager | Manage Material Data (F4864) | An EHS Chemical Compliance Information (CCI) Material is created. |

## Procedures

This section describes procedures for each segment or process step that is part of this master record.

### Create an EHS Chemical Compliance Information Material Master Data - General Data

Purpose

The following procedure provides instructions for creating an EHS chemical compliance information material that can be later employed for EHS Waste Management processes.

Procedure (using Fiori Launchpad)

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using your user credentials. | The Start page appears. |  |
| 2 | Open Manage Customer Master Data | Open the Manage Material Data app (F4864). | The Manage Material Data app is opened, and a list report is displayed. |  |
| 3 | Create a New Material | Choose Create.On the screen:Enter in a <Name> in the Internal Name field.Select a <Logistics role> from the Logistics Role dropdown list.Choose Save. | The New Material tab is displayed, and a new material is created. |  |
| 4 | Add a Product | Choose Edit.In the Product section, choose Add and select one product.Choose Save.Note: Only one product can be assigned to a material. | A product is added to the material and the information is saved. |  |

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
- related-to :: [[13-quality-ehs-and-compliance/crear-un-material-de-informacion-de-conformidad-de-producto-quimico-eh]]
- related-to :: [[13-quality-ehs-and-compliance/criar-um-material-de-informacoes-de-conformidade-quimica-ehs-mds-65z-5]]
- related-to :: [[13-quality-ehs-and-compliance/ehs-mds-65z-chinese-507]]
- related-to :: [[13-quality-ehs-and-compliance/ehs-mds-65z-japanese-505]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/65Z_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 6,757 chars in the whole document
