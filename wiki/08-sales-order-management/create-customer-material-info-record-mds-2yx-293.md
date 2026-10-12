---
id: 08-sales-order-management/create-customer-material-info-record-mds-2yx-293
title: Create Customer-Material Info Record - MDS (2YX) (2YX_S4CLD2608_Master_Data_EN_XX)
description: "SAP S/4HANA Cloud Public Edition 2608 master data script for creating a customer-material info record in Manage Customer Materials (F2499), incl. sales unit conversion."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/customer-material-info-records]
aliases: [2YX_S4CLD2608_Master_Data_EN_XX]
keywords: [Customer-Material Info Records, customer-material info, unit conversion, sales master data, business roles, master data scripts, 2YX]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2YX_S4CLD2608_Master_Data_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-293
topic: 08-sales-order-management/customer-material-info-records
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Create Customer-Material Info Record - MDS (2YX) (2YX_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2YX_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Customer-Material Info Records** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Customer-Material Info Record - MDS (2YX) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233904578)

[2 Prerequisites 3](#_Toc233904579)

[2.1 System Access 3](#_Toc233904580)

[2.2 Roles 3](#_Toc233904581)

[2.3 Mandatory and Optional Master Data 3](#_Toc233904582)

[2.4 Mandatory and Optional Master Data 4](#_Toc233904583)

[3 Overview Table 5](#_Toc233904584)

[4 Test Procedures 6](#_Toc233904585)

[4.1 Create Customer-Material Information 6](#_Toc233904586)

## Purpose

In this document you find a description of how to Create Customer-Material Info for your SAP S/4HANA Cloud Public Edition system. The description includes those data segments that are relevant for the SAP S/4HANA Cloud Public Edition appliance. Fields that are not relevant for the scope of the SAP S/4HANA Cloud Public Edition content are not described in this document.

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

### Mandatory and Optional Master Data

| Master Data Object | Used in Data Segment | Mandatory/Optional | Comments |
| --- | --- | --- | --- |
| Customer | Initial screen | Mandatory |  |
| Sales Organization | Initial screen | Mandatory |  |
| Distribution Channel | Initial screen | Mandatory |  |
| Material | Initial screen | Optional |  |

### Mandatory and Optional Master Data

In this section, you can find some basic parameters that influence the behavior of a master record and are always required to create a pricing condition:

Sales Organization: <Sales Organization>

Distribution Channel: <Distribution Channel>

Customer: <Customer>

Material：<Material Number>

## Overview Table

This scope item consists of several process steps that are listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | SAP Fiori App / Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Customer-Material Information](#unique_8) [page ] 6 | Internal Sales Representative | Manage Customer Materials (F2499) | Customer-Material Info record is created. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Customer-Material Information

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Customer Materials (F2499). | The app opens. |  |
| 3 | Access the Creation of Customer Materials | Choose Create. | The Customer Material screen displays. |  |
| 4 | Enter Basic Customer-Material Information | Make the following entries:Customer: <Customer>Product: <Material Number>Sales Organization: <Sales Organization>Distribution Channel: <Distribution Channel>Customer Material Description: provide a description for the customer and material. | The basic customer-material information is maintained. |  |
| 5 | Enter Sales Unit | In the Unit Conversion section, make the following entry:1 PAL (Customer Unit): 2 PC (Basic Unit) | The Sales Unit for the customer-material combination is maintained.NoteTo maintain the Sales Unit and conversion on this screen, the material master data of the Unit of Measure and conversion should be maintained. You may refer to other Master Data Scripts, for example, Create Product Master of type "Trading Good" - MDS - BNF for trading goods.Once the Sales Unit is maintained on this screen, it displays in the sales document. |  |
| 6 | Choose Create | Choose Create. | The Customer Material is successfully created. |  |

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
- related-to :: [[08-sales-order-management/crear-registro-info-para-cliente-y-material-mds-2yx-294]]
- related-to :: [[08-sales-order-management/criar-registro-info-de-material-do-cliente-mds-2yx-296]]
- related-to :: [[08-sales-order-management/kundenmaterial-infosatz-anlegen-sds-2yx-292]]
- related-to :: [[08-sales-order-management/mds-2yx-295]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2YX_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 8,489 chars in the whole document
