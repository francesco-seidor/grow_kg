---
id: 14-maintenance-service-and-projects/master-data-script-create-service-product-for-project-5to-485
title: "Master Data Script: Create Service Product for Project (5TO) (5TO_S4CLD2608_Master_Data_EN_XX)"
description: "SAP S/4HANA Cloud master data script for creating service product PROJECT via Create Material (MM01), with sales org data for solution orders."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/solution-orders-and-cpq]
aliases: [5TO_S4CLD2608_Master_Data_EN_XX]
keywords: [Solution Orders and SAP CPQ Quotations, service product, material master, sales organization data, business roles, profit center, master data script, 5TO]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5TO_S4CLD2608_Master_Data_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-485
topic: 14-maintenance-service-and-projects/solution-orders-and-cpq
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Master Data Script: Create Service Product for Project (5TO) (5TO_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5TO_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Solution Orders and SAP CPQ Quotations** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Service Product for Project - MDS (5TO) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233904790)

[2 Prerequisites 3](#_Toc233904791)

[2.1 System Access 3](#_Toc233904792)

[2.2 Roles 3](#_Toc233904793)

[2.3 Required Organizational Units 3](#_Toc233904794)

[2.4 Mandatory and Operational Master Data 4](#_Toc233904795)

[3 Overview Table 5](#_Toc233904796)

[4 Test Procedures 6](#_Toc233904797)

[4.1 Create Service Product - PROJECT 6](#_Toc233904798)

## Purpose

In this document you find a description of how to create service productmaster data records including prices. The description includes those data segments that are relevant for the master data to work in a "usual" system environment. The reader mainly learns which data segments and fields usually need to be filled with input values. Fields that are not relevant for the scope are not described in this document although they may appear on the UI.

Service product master record that is created as described here can be used for solution order.

| Service product ID | Description | Usage |
| --- | --- | --- |
| PROJECT | Project | represents the project |

## Prerequisites

### System Access

| System | Details |
| --- | --- |
| System | Accessible via SAP Fiori Launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) |
| --- | --- | --- | --- |
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Product | SAP_CMD_SP_PR_MAINT |

### Required Organizational Units

Some segments of master data are dependent on the organizational units of the company, General (Central) Data does not depend on an organizational unit or the company code. The following table gives an overview of these different data segments and their relevant organizational units:

| Data Segment | Depends On | Organizational Unit to be Used for US | Organizational Unit to be Used for DE |
| --- | --- | --- | --- |
| Create Material | Sales Organization | 1710 (Dom. Sales Org US) | 1010 (Dom. Sales Org DE) |
| Create Material | Distribution Channel | 10 (Direct Sales) | 10 (Direct Sales) |

### Mandatory and Operational Master Data

Material master data records may refer to other master data. The following table gives an overview of optional and mandatory master data objects to be used in a material master data record.

|  |
| --- |
| Note Brazil specific fields are required to get a proper tax calculation.Check Nota Fiscal Brazil - JD0 in Define BR Specific Fields for Master Data chapter for material master data. |

| Master Data Object | Used in Data Segment | Mandatory / Optional | Comments |
| --- | --- | --- | --- |
| Profit Center |  | Mandatory | Assigning a Profit Center to a material (product) master is required for correct valuation processes. |

## Overview Table

This master record consists of several segments provided in the table below.

If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.

You can find all other apps not included on the homepage using the search bar.

If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose Settings > App Finder .

| ID (Role Template) | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Create Service Product | SAP_BR_PRODMASTER_SPECIALIST | Create Material (MM01) | Service products are created. |

## Test Procedures

This section describes procedures for each segment or process step that is part of this master record.

### Create Service Product - PROJECT

Purpose

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Product Data (MDG). |  |  |
| 2 | Access the SAP Fiori app | Choose the Create Material (MM01) tile. | The Create Material (Initial Screen) is displayed. |  |
| 3 | Maintain Material Basic Data (for Service Product ) | On the Create Material (Initial Screen) make the following entries:Material:PROJECTMaterial Type:Service ProductThen choose Continue (Enter). | You have maintained basic information for the new service product.The Select View(s) dialog window is displayed. |  |
| 4 | Choose Views | On the Select View(s)Basic Data 1 view, then choose Continue (Enter). | The Create Material PROJECT view is displayed. |  |
| 5 | Maintain Basic Data | On the Basic data 1 view, maintain the following values:Descr.:Project ItemBase Unit of Measure:AU (ACTIVITY UNIT)Material Group:P001 (Services)GenItemGroup:SPRJ (Project)Then choose Save. | Basic data is maintained and the service product is saved.After saving, the Create Material (Initial Screen) view is displayed.For every different language used in your company the corresponding description for the product has to be maintained per language code! |  |
| 6 | Extend Product Details | On the Create Material (Initial Screen) view, enter material PROJECT, then choose Continue (Enter). | The Select View(s) dialog window is displayed. |  |
| 7 | Choose Views | On the Select View(s) dialog window, select the following views:Sales: Sales Org. Data 1Sales: Sales Org. Data 2Then choose Continue (Enter). | The Organizational Levels dialog window is displayed. |  |
| 8 | Choose Organizational Levels | On the Organizational Levels window, maintain the following values:Sales Org.:1710 (Dom. Sales Org US)Distr. Channel:10 (Direct Sales)Then choose Continue (Enter). | Organizational data has been selected.The Create Material PROJECT view is displayed. |  |
| 9 | Maintain Sales Organization Data (1) | On the Sales: sales org. 1 view, maintain the following values:General dataCash Discount:X <selected>Tax dataTax classification:1 (Full tax)Then choose Enter. | Sales organizational data is maintained. The Sales: sales org. 2 tab page is displayed. |  |
| 10 | Maintain Sales Organization Data (2) | On the Sales: sales org. 2 view, maintain the following entry:Item category group:SPRJ (Project)Then choose Enter.Then choose Save. | Sales organizational data is maintained. The Sales: General/Plant tab page is displayed. |  |

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
- related-to :: [[14-maintenance-service-and-projects/creacion-de-producto-de-servicio-para-proyecto-mds-5to-486]]
- related-to :: [[14-maintenance-service-and-projects/criar-produto-de-servico-para-projeto-mds-5to-488]]
- related-to :: [[14-maintenance-service-and-projects/mds-5to-487]]
- related-to :: [[14-maintenance-service-and-projects/mds-5to-489]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5TO_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 9,796 chars in the whole document
