---
id: 14-maintenance-service-and-projects/create-equipment-mds-5mf-455
title: Create Equipment - MDS (5MF) (5MF_S4CLD2608_Master_Data_EN_XX)
description: "English master data script (5MF) for SAP S/4HANA Cloud Public Edition: creating equipment master records and installing them in a functional location via Create Technical Object."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/equipment]
aliases: [5MF_S4CLD2608_Master_Data_EN_XX]
keywords: [Equipment Master Records, equipment master data, technical objects, functional locations, maintenance work center, cost center, business roles, master data scripts, plant dependency, 5MF]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5MF_S4CLD2608_Master_Data_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-455
topic: 14-maintenance-service-and-projects/equipment
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Create Equipment - MDS (5MF) (5MF_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5MF_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Equipment Master Records** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Equipment - MDS (5MF) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233904801)

[2 Prerequisites 3](#_Toc233904802)

[2.1 System Access 3](#_Toc233904803)

[2.2 Roles 3](#_Toc233904804)

[2.3 Required Organizational Units 3](#_Toc233904805)

[2.4 Mandatory and Optional Master Data 4](#_Toc233904806)

[3 Overview Table 5](#_Toc233904807)

[4 Main Parameters for Data Creation 6](#_Toc233904808)

[4.1 Technical Object Category 6](#_Toc233904809)

[5 Procedure 7](#_Toc233904810)

[5.1 Create Equipment 7](#_Toc233904811)

## Purpose

In this document, you can find a detailed procedure of how to create equipment master data records for your S/4HANA system. It includes data segments that are relevant for the master data to work in regular system enviroment. This document also provides informaton about which data segments and fields require input values.

The fields that are not relevant for the scope of the S/4HANA content delivery by SAP Best Practices are not described in this document although they may appear on the user interface (UI).

## Prerequisites

This section summarizes all prerequisites for creating an equipment.

### System Access

The test should be conducted with the following system:

Table 1:

| System | Details |
| --- | --- |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Space) | ID (Space) |
| --- | --- | --- | --- |
| Maintenance Planner | SAP_BR_MD_SPECIALIST_EAM | Maintenance Planner | SAP_EAM_SPT_MD_SPECIALIST_PC |

### Required Organizational Units

Some segments of master data are dependent on the organizational units of the company. General (central) data does not depend on an organizational unit or the company code. The following table gives an overview of different data segments and their relevant organizational units:

| Data Segment | Depends On | Field Examples | Comments | Organizational Unit to be Used |
| --- | --- | --- | --- | --- |
| All data | Plant |  | All the data for equipment depends on plant. | Plant:__________ |

### Mandatory and Optional Master Data

Equipment data records may refer to other master data. The following table gives an overview of optional and mandatory master data objects to be used in an equipment.

| Master Data Object | Used in Data Segment | Mandatory / Optional | Comments |
| --- | --- | --- | --- |
| Maintenance Work Center | In the equipment master user interface (UI), Organization Data tab, you find the entry of maintenance work center in responsibilities section. | Optional | The system uses maintenance work center as parameter to determine some values, such as setup, machine or labor. |
| Cost Center | In the equipment master user interface (UI), Organization Data tab, you find the entry of cost center in responsibilities section. | Optional | The system uses cost center as parameter for the costing. |

## Overview Table

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Equipment](#unique_8) [page ] 7 | SAP_BR_MD_SPECIALIST_EAM | Create Technical Object (EAMS_WDA_TECHOBJ_OIF (EAMS_WDA_TECHOBJ_OIF_CFG_V2)) | Equipment is created. |

## Main Parameters for Data Creation

In this section, we describe some basic parameters that influence the behavior of a master record and are always required to create an equipment.

### Technical Object Category

The possible uses may be:

- Machinery
- Device
- Production resource/tool
- Customer equipment

Table 2:

| Technical Object Category | Description |
| --- | --- |
| M | Machines |

## Procedure

### Create Equipment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this test step you maintain a record for a piece of equipment that is installed in a functional location.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a SAP_BR_MD_SPECIALIST_EAM. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Technical Object (EAMS_WDA_TECHOBJ_OIF (EAMS_WDA_TECHOBJ_OIF_CFG_V2)). | A new window opens, showing the Create Technical object: Initial Screen. |  |
| 3 | Create Equipment | On the Create Technical Object screen, select the Technical Object Type: Equipment.On the next screen, enter the following:Technical Object Type: EquipmentTechnical Object: leave emptyValid From: today's dateTechnical Object Category: M (Technical system-standard)Choose Continue. |  |  |
| 4 | Maintain General Data | On the Create Technical Object: <Equipment ID> screen, in the General Data section, enter the following:Description: For example, Manual Isolation Valve>Object Type: For example, 9400>Start-Up Date: For example, today’s date>Country/Region of Manufacture: For example, US>Month/Year of Construction: For example, 04/2011>Manufacturer Part Number: For example, HZZ-TD B4>Manufacturer Serial Number: For example, HZZ-TD B4/66>Acquisition Value/Currency: For example,10,000.00/ USD >Acquisition Date: For example, 04/10/2011 >Optionally maintain further general data, then navigate to the Location Data section. | The create technical object: general data screen appears. |  |
| 5 | Maintain Location Data | In the Location Data section, enter the following:Maintenance Plant: For example, 1710 for US>Location: For example, YB_1701 for US>Plant Section: For example, YOH for US>Note Technical objects that belong to the same structure must all have the same plant assigned. As an alternative, you can leave the plant information empty for all technical objects.Optionally maintain further details, such as address information. | The create technical object: location data screen appears. |  |
| 6 | Maintain Organizational Data | In the Organizational Data section, enter the following:Planner Group: For example, 920 for US>Planning Plant: For example, 1710 for US>Maintenance Work Center: For example, RES-0100 for US>Work Center Plant: For example, 1710 for US>Cost Center: For example, 17101701 for US>Optionally, you can maintain additional information like, for example, partner information and so on in the Organizational Data section. | The create technical object: Organizational data screen appears. |  |
| 7 | Save Equipment | Optionally, you can maintain additional information for other sections.Choose Check Entries button.Choose Save. | Equipment is created. |  |
| 8 | Install Equipment in Functional Location | On the Change Technical Object: <equipment ID> screen, navigate to the Structure section.Choose Change Structure: Install.On the Change Installation Location screen, enter the following:Superior Technical Object: for example< 1710>Position: <leave empty>Installation Date/Time: <keep system proposal>Choose OK.Choose Save. |  |  |

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
- related-to :: [[14-maintenance-service-and-projects/crear-equipo-mds-5mf-456]]
- related-to :: [[14-maintenance-service-and-projects/criar-equipamento-mds-5mf-458]]
- related-to :: [[14-maintenance-service-and-projects/equipment-anlegen-sds-5mf-454]]
- related-to :: [[14-maintenance-service-and-projects/mds-5mf-457]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5MF_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 11,085 chars in the whole document
