---
id: 02-business-partner-and-product-master-data/create-application-group-and-characteristic-display-mds-2ni-269
title: Create Application Group and Characteristic Display - MDS (2NI) (2NI_S4CLD2608_Master_Data_EN_XX)
description: "English SAP S/4HANA Cloud master data script (2NI): create an application group and characteristic display for variant configuration via CU_CHAR_DISPLAY."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/variant-configuration-master-data]
aliases: [2NI_S4CLD2608_Master_Data_EN_XX]
keywords: [Configurable Materials and Characteristic Display, characteristic display, application group, variant configuration, characteristic assignment, transaction types, business roles, 2NI]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2NI_S4CLD2608_Master_Data_EN_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-269
topic: 02-business-partner-and-product-master-data/variant-configuration-master-data
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Create Application Group and Characteristic Display - MDS (2NI) (2NI_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2NI_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Configurable Materials and Characteristic Display** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Application Group and Characteristic Display - MDS (2NI) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233904531)

[2 Prerequisites 3](#_Toc233904532)

[2.1 System Access 3](#_Toc233904533)

[2.2 Roles 3](#_Toc233904534)

[2.3 Mandatory and Operational Master Data 3](#_Toc233904535)

[2.4 Main Parameters for Data Creation 4](#_Toc233904536)

[2.4.1 Transaction 4](#_Toc233904537)

[3 Overview Table 5](#_Toc233904538)

[4 Test Procedures 6](#_Toc233904539)

[4.1 Create Application Group 6](#_Toc233904540)

[4.2 Create Characteristic Display 7](#_Toc233904541)

## Purpose

In this document, you get a description of how to create characteristic display record for your SAP S/4HANA Cloud Public Edition system. The description includes data relevant for the SAP S/4HANA Cloud Public Edition appliance such as Application Group, Characteristic Display, and Characteristic Assignment. Fields that are not relevant for the scope of SAP S/4HANA Cloud Public Edition are not described in this document.

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
| Product Configuration Modeler | SAP_BR_PRODUCT_CONFIG_MODELER | Variant Configuration | SAP_BR_PRODUCT_CONFIG_MODELER |  |

### Mandatory and Operational Master Data

Characteristic Display records may refer to other master data. The following table gives an overview of optional and mandatory master data objects to be used in a material master data record.

| Master Data Object | Used in Data Segment | Mandatory / Optional | Comments |
| --- | --- | --- | --- |
| Characteristics |  | Mandatory | Characteristics are to be assigned to characteristic display record |

### Main Parameters for Data Creation

In this section, we describe some basic parameters that influence the behavior of a master record and are always required to create a characteristic display.

#### Transaction

With the help of Transaction, the system determines in which transaction the characteristic display should be available.

For 1711 edition, only the Sales and Distribution Document is supported.

| Transaction | Comment |
| --- | --- |
| Sales and Distribution Document | For 1711 edition, only Sales and Distribution Document is supported for characteristic display. |
| Production Order |  |
| Trading Contract |  |
| Purchase Order |  |
| Goods Receipt |  |
| Order Confirmation |  |

## Overview Table

In this section, a list of steps a user goes through when creating a master data record is provided. Every logical, meaningful segment of a master data object should lead to a separate step (for example: org.-unit dependent data segments and so on).

The scope item Create Application Group and Characteristic Display - MDS consists of several process steps provided in the following tables:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step, Report or Item | Business Role | Transaction/APP | Expected Results |
| --- | --- | --- | --- |
| [Create Application Group](#unique_9) [page ] 6 | Product Configuration Modeler | Maintain Char. Display for Configuration (CU_CHAR_DISPLAY) | Application Group is created |
| [Create Characteristic Display](#unique_10) [page ] 7 | Product Configuration Modeler | Maintain Char. Display for Configuration (CU_CHAR_DISPLAY) | Application Group is created |

## Test Procedures

This section describes procedures for each process step that belongs to this scope item. You can use these procedures also for testing the master data creation.

### Create Application Group

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Configuration Modeler. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Maintain Char. Display for Configuration (CU_CHAR_DISPLAY). | The Change View ''Application Group'': Overview view displays. |  |
| 3 | Enter Application Group | On the Change View ''Application Group'': Overview screen, choose New Entry. And make the following entries:Transact. : <Select from dropdown list>Appl Grp: <Any code> | The New Entries: Overview of Added Entries screen displays. |  |
| 4 | Save Your Data | Choose Save. |  |  |

### Create Characteristic Display

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Configuration Modeler. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Choose Maintain Char. Display for Configuration (CU_CHAR_DISPLAY). | The Change View ''Application Group'': Overview view displays. |  |
| 3 | Enter Application Group | On the Change View ''Application Group'': Overview screen, choose Characteristic Display.Choose New Entry. Make the following entry and press Enter:Char. Display: <Any code>.Description: <Enter description for the characteristic display>.Appl. Grp: <Select F4 for help>. | The Change View ''Characteristic Display'': Overview screen displays. |  |
| 4 | Assign Characteristic | Choose the characteristic display created in previous step and select Characteristic Assignment.Make the following entries:Seq.: <Enter sequence number to determine the sequence of characteristic>.Characteristic Name: <Search for a characteristic by selecting F4 search help>.Col.: <Enter proper column width in order to show characteristic description and value>. | The Change View ''Characteristic Assignment'': Overview screen displays. |  |
| 5 | Save Your Data | Choose Save. |  |  |

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
> Flagged while digesting this document, not verified: Text says only Sales and Distribution Document is supported (1711 edition) yet lists other transaction types; the overview table gives the same 'Application Group is created' result for both steps

## Connections
- part-of :: [[_cluster]]
- related-to :: [[02-business-partner-and-product-master-data/anwendungsgruppe-und-merkmalsanzeige-anlegen-sds-2ni-268]]
- related-to :: [[02-business-partner-and-product-master-data/crear-grupo-de-aplicaciones-y-visualizacion-de-caracteristicas-mds-2ni]]
- related-to :: [[02-business-partner-and-product-master-data/mds-2ni-271]]
- related-to :: [[02-business-partner-and-product-master-data/mds-2ni-273]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2NI_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 10,537 chars in the whole document
