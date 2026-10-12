---
id: 14-maintenance-service-and-projects/master-data-script-create-plant-maintenance-master-data-for-service-md
title: "Master Data Script: Create Plant Maintenance Master Data for Service - MDS (3U3) (3U3_S4CLD2608_Master_Data_EN_XX)"
description: English master data script (3U3) for creating functional location and equipment master data for plant maintenance/service in SAP S/4HANA Cloud Public Edition.
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/service-technical-objects-and-boms]
aliases: [3U3_S4CLD2608_Master_Data_EN_XX]
keywords: [Technical Objects and BOMs for Service, functional location, equipment master data, plant maintenance, master data script, user roles, warranty, in-house repair, test procedure, 3U3]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3U3_S4CLD2608_Master_Data_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-371
topic: 14-maintenance-service-and-projects/service-technical-objects-and-boms
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Master Data Script: Create Plant Maintenance Master Data for Service - MDS (3U3) (3U3_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3U3_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Technical Objects and BOMs for Service** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Plant Maintenance Master Data for Service - MDS (3U3) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233904673)

[2 Prerequisites 3](#_Toc233904674)

[2.1 System Access 3](#_Toc233904675)

[2.2 Roles 3](#_Toc233904676)

[3 Procedures 4](#_Toc233904677)

[3.1 Creating Functional Location Master Data 4](#_Toc233904678)

[3.2 Creating Equipment Master Data 5](#_Toc233904679)

## Purpose

In this document you find a description of how to create functional location and equipment master data records for your S/4 HANA system. The description includes those data segments that are relevant for the master data to work in a "usual" system environment. The reader mainly learns which data segments and fields usually need to be filled with input values. Fields that are not relevant for the scope of the S/4 HANA content delivery by SAP Best Practices are not described in this document although they may appear on the UI.

Functional location and equipment master records that are created as described here can be used in service orders, service confirmations, and service contracts.

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
| Maintenance Planner | SAP_BR_MAINTENANCE_PLANNER | Maintenance Planning | SAP_BR_MAINTENANCE_PLANNER |

## Procedures

### Creating Functional Location Master Data

Purpose

In this test step you maintain a functional location structure that consists of one highest level functional location and two subordinate functional locations.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Maintenance Planner. |  |  |
| 2 | Open App | In the Technical Object section, choose the Create Technical Object tile. |  |  |
| 3 | Create Functional Location | On the Create Technical Object screen, select the Technical Object Type: Functional Location.On the next screen, maintain the following entries:Technical Object Type: Functional LocationStructure Indicator: YBPM (Structure Indicator for Best Practice)Technical Object: <enter an identifier, for example> ZZ01Technical Object Category: S (Customer Location)Choose Continue. |  |  |
| 4 | Maintain General Data | On the Create Technical Object: ZZ01 screen, in the General Data section, maintain the following entries:Description: <for example, Building A>Optionally maintain further general data, then navigate to the Location Data section. |  |  |
| 5 | Maintain Location Data | In the Location Data section, maintain the following entries:Maintenance Plant: <maintain a relevant plant, for example, 1710 for US>Note Technical objects that belong to the same structure must all have the same plant assigned. As an alternative, you can leave the plant information empty for all technical objects.Optionally maintain further details, such as address information. |  |  |
| 6 | Save Functional Location | Optionally you can maintain additional information like, for example, partner information etc. in the Organizational Data section.Choose Save.Then navigate back to the Home screen. |  |  |
| 7 | Create Subordinate Functional Location | To maintain a functional location structure, proceed as described in the above steps, and maintain the following functional locations:Technical Object: ZZ01-001Description: 1st FloorTechnical Object: ZZ01-002Description: 2nd Floor |  |  |
| 8 | Review Technical Object in Asset Viewer | On the Home page, choose the Display Technical Object tile.On the Display Technical Object screen, maintain the relevant Technical Object, for example, ZZ01, then choose Continue.To review the functional location structure and the details per technical object, choose You can also: Display Technical Object in Asset Viewer. |  |  |

### Creating Equipment Master Data

Purpose

In this test step you maintain a record for a piece of equipment that is installed in a functional location.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Maintenance Planner. |  |  |
| 2 | Open App | Open Create Technical Object. |  |  |
| 3 | Create Equipment | On the Create Technical Object screen, select the Technical Object Type: Equipment.On the next screen, maintain the following entries:Teleave chnical Object Type: EquipmentTechnical Object: <empty>Valid From: <today’s date>Technical Object Category: S (Customer Equipment)Choose Continue. |  |  |
| 4 | Maintain General Data | On the Create Technical Object: <Equipment ID> screen, in the General Data section, maintain the following entries:Description: <for example, Printer A1>(Optional) Customer Warranty: Warranty Start/End(Optional) Vendor Warranty: Warranty Start/EndNote The in-house repair process (scope item 3XK) supports and integrates warranties that are based on dates (warranty period). In In-House Repair, you can use the warranty types customer war-ranty and vendor warranty.You need to enter the warranty start date and warranty end date in the equipment master data. If you have entered the end date for the customer and/or vendor warranty of an equipment, the system checks if the warranty end date is prior to the creation date of the in-house repair.An icon indicates whether the creation date of the in-house repair is within the warranty period.Optionally maintain further general data like manufacturer information, model number etc., then navigate to the Location Data section. |  |  |
| 5 | Assign Material and Serial Number | Choose Additional Functions > Show Serial Number Data .Make the following entries and choose Enter:Material: TG20 |  |  |
| 6 | Maintain Location Data | In the Location Data section, maintain the following entries:Maintenance Plant: <maintain a relevant plant, for example, 1710 for US>Note Technical objects that belong to the same structure must all have the same plant assigned. As an alternative, you can leave the plant information empty for all technical objects.Optionally maintain further details, such as address or room information. |  |  |
| 7 | Save Equipment | Optionally you can maintain additional information like, for example, partner information etc. in theOrganizational Data section.Choose Save. |  |  |
| 8 | Install Equipment in Functional Location | On the Change Technical Object: <equipment ID> screen, navigate to the Structure section.Choose Change Structure: Install.On the Change Installation Location dialog box, maintain the following entries:Superior Technical Object: ZZ01-001Position: <leave empty>Installation Date/Time: <keep system proposal>Choose OK.Choose Save. |  |  |

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
- related-to :: [[14-maintenance-service-and-projects/instandhaltungs-stammdaten-fur-service-anlegen-sds-3u3-370]]
- related-to :: [[14-maintenance-service-and-projects/mds-3u3-373]]
- related-to :: [[14-maintenance-service-and-projects/mds-3u3-375]]
- related-to :: [[14-maintenance-service-and-projects/script-de-dados-mestre-criar-dados-mestre-de-manutencao-de-centro-para]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3U3_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 10,379 chars in the whole document
