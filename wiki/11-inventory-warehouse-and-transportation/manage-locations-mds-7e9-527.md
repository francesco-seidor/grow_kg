---
id: 11-inventory-warehouse-and-transportation/manage-locations-mds-7e9-527
title: Manage Locations - MDS (7E9) (7E9_S4CLD2608_Master_Data_EN_XX)
description: SAP S/4HANA Cloud Public Edition master data script (7E9) for creating transportation location master records in Manage Locations (F6225).
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/transportation-locations]
aliases: [7E9_S4CLD2608_Master_Data_EN_XX]
keywords: [Transportation Locations, location master data, location types, un/locode, airport codes, business roles, transportation management, geocoordinates, 7E9]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/7E9_S4CLD2608_Master_Data_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-527
topic: 11-inventory-warehouse-and-transportation/transportation-locations
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Manage Locations - MDS (7E9) (7E9_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/7E9_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Transportation Locations** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Manage Locations - MDS (7E9) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233904882)

[2 Prerequisites 3](#_Toc233904883)

[2.1 System Access 3](#_Toc233904884)

[2.2 Roles 3](#_Toc233904885)

[2.3 Main Parameters for Data Creation 3](#_Toc233904886)

[2.3.1 Location Types 3](#_Toc233904887)

[2.3.2 Define UN/LOCODE 4](#_Toc233904888)

[2.3.3 Define Airport Codes 4](#_Toc233904889)

[3 Overview Table 5](#_Toc233904890)

[4 Test Procedures 6](#_Toc233904891)

[4.1 Manage Locations 6](#_Toc233904892)

## Purpose

In this document you find a description of how to create a location master data record for your SAP S/4HANA Cloud Public Edition system. The description includes those data segments that are relevant for the master data to work in a "usual" system environment. You mainly learn which data segments and fields usually need to be filled with input values. Fields that are not relevant for the scope of the SAP S/4HANA Cloud Public Edition content delivery by SAP Best Practices are not described in this document although they may appear on the screen.

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
| Master Data Specialist - Transportation Management | SAP_BR_TRANSP_MDSPEC | Transportation Master Data | SAP_BR_TRANSP_MDSPEC |

### Main Parameters for Data Creation

In this section, some basic parameters that influence the behavior of a master record and that are always required to create a <type> master data record are described.

#### Location Types

The following options for assigning the location types are available:

| Name | ID |
| --- | --- |
| Port | 1100 |
| Airport | 1110 |
| Railway Station | 1120 |
| Rail Junction | 1190 |
| Loading Point | 1200 |

#### Define UN/LOCODE

You can define United Nations Codes for Trade and Transport Locations (UN/LOCODES).

In your configuration environment, use the search function to find each activity. For more information, see [Configuration Environment of SAP S/4HANA Cloud Public Edition.](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/0b3f87579f345c08e10000000a441470.html)

#### Define Airport Codes

You can define airport codes.

In your configuration environment, use the search function to find each activity. For more information, see [Configuration Environment of SAP S/4HANA Cloud Public Edition](https://help.sap.com/docs/SAP_S4HANA_CLOUD/61e246f4b34c4e1790d8b7651c0b40a8/0b3f87579f345c08e10000000a441470.html?state=DRAFT).

## Overview Table

This master record consists of several segments provided in the table below.

| Segment | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Manage Locations](#unique_10) [page ] 6 | Master Data Specialist - Transportation Management | Manage Locations (F6225) |  |

## Test Procedures

This section describes procedures for each segment or process step that is part of this master record.

### Manage Locations

Purpose

The following steps show how to create locations.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Transportation Management. | The SAP Fiori launchpad appears. |  |
| 2 | Access App | Open Manage Locations (F6225). | The Manage Location Master (F6225) screen appears. |  |
| 3 | Choose Create | Choose Create. | The Create dialog box appears. |  |
| 4 | Enter details | In the Create dialog box, make the following entries:Location: <your location>Location Type: <your location type> |  |  |
| 5 | Choose Continue | Choose Continue. | The Location screen appears. |  |
| 6 | Enter General Information | On the General Information tab, make the following entry:Loc. Description: <your location description> |  |  |
| 7 | Enter Address data | On the Address tab, make the following entries:Street: <street>Postal Code: <postal code>Country/Region: <country/region>House Number: <house number>City: <city>Region: <region>Time Zone: <time zone>Search Term 1: <search term> |  |  |
| 8 | Enter Identification data | On the Identification tab, make the following entry:UN/LOCODE: <UN/LOCODE>Airport Code: <airport code> |  |  |
| 9 | Choose Calculate Geocoordinates | Choose Calculate Geocoordinates. | The geocoordinates were automatically determined and filled in the Geocoordinates tab. |  |
| 10 | Choose Create | Choose Create. | The following system message appears:Location <your location> created successfully |  |

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
- related-to :: [[11-inventory-warehouse-and-transportation/administrar-localizacoes-mds-7e9-530]]
- related-to :: [[11-inventory-warehouse-and-transportation/gestion-de-ubicaciones-mds-7e9-528]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-7e9-529]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-7e9-531]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/7E9_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 8,194 chars in the whole document
