---
id: 14-maintenance-service-and-projects/create-functional-location-mds-5lm-443
title: Create Functional Location - MDS (5LM) (5LM_S4CLD2608_Master_Data_EN_XX)
description: SAP S/4HANA Cloud Public Edition 2608 master data test script (5LM) for creating a functional location hierarchy via the Create Technical Object Fiori app.
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/functional-locations]
aliases: [5LM_S4CLD2608_Master_Data_EN_XX]
keywords: [Functional Locations, functional location, technical object, structure indicator, plant maintenance master data, business roles, organizational units, maintenance work center, cost center, master data scripts]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5LM_S4CLD2608_Master_Data_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-443
topic: 14-maintenance-service-and-projects/functional-locations
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Create Functional Location - MDS (5LM) (5LM_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5LM_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Functional Locations** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Functional Location - MDS (5LM) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233904765)

[2 Prerequisites 3](#_Toc233904766)

[2.1 System Access 3](#_Toc233904767)

[2.2 Roles 3](#_Toc233904768)

[2.3 Required Organizational Units 3](#_Toc233904769)

[2.4 Mandatory and Optional Master Data 4](#_Toc233904770)

[2.5 Main Parameters for Data Creation 4](#_Toc233904771)

[2.5.1 Structure Indicator 4](#_Toc233904772)

[2.5.2 Technical Object Category 5](#_Toc233904773)

[3 Overview Table 6](#_Toc233904774)

[4 Procedure 7](#_Toc233904775)

[4.1 Create Functional Location 7](#_Toc233904776)

## Purpose

In this document, you can find a detailed procedure of how to create functional location master data records for your S/4HANA system. It includes data segments that are relevant for the master data to work in regular system enviroment. This document also provides informaton about which data segments and fields require input values.

The fields that are not relevant for the scope of the S/4HANA content delivery by SAP Best Practices are not described in this document although they may appear on the user interface (UI). A Functional Location that is created as described here can be used for maintenance processes.

## Prerequisites

This section summarizes all the prerequisites that are required for creating a fuctional location.

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

Some segments of master data are dependent on the organizational units of the company. General (Central) Data does not depend on an organizational unit or the company code. The following table gives an overview of different data segments and their relevant organizational units:

| Data Segment | Depends On | Field Examples | Comments | Organizational Unit to be Used |
| --- | --- | --- | --- | --- |
| All data | Plant |  | All the data for functional location depends on plant. | Plant:__________ |

### Mandatory and Optional Master Data

Functional location data records may refer to other master data. The following table gives an overview of optional and mandatory master data objects to be used in a functional location.

| Master Data Object | Used in Data Segment | Mandatory / Optional | Comments |
| --- | --- | --- | --- |
| Maintenance Work Center | In the functional location user interface (UI), Organization Data tab, you find the entry of maintenance work center in responsibilities section. | Optional | The system uses maintenance work center as parameter to determine some values, such as setup, machine or labor. |
| Cost Center | In the functional location user interface (UI), Organization Data tab, you find the entry of cost center in responsibilities section. | Optional | The system uses cost center as parameter for the costing. |

### Main Parameters for Data Creation

In this section, we describe some basic parameters that influence the behavior of a master record and are always required to create a functional location:

#### Structure Indicator

The structure indicator of a functional location determines the structure of the functional location label. It establishes the following factor:

- Number of hierarchy levels of a technical system
- Key length of the levels
- Separators (hyphens)

Table 2:

| Structure Indicator | Description |
| --- | --- |
| YBPM | Structure Indicator for Best Practice |

#### Technical Object Category

This is the key which shows the functional location category.

Table 3:

| Technical Object Category | Description |
| --- | --- |
| M | Technical system- standard |

## Overview Table

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Functional Location](#unique_11) [page ] 7 | SAP_BR_MD_SPECIALIST_EAM | Create Technical Object (EAMS_WDA_TECHOBJ_OIF (EAMS_WDA_TECHOBJ_OIF_CFG_V2)) | Functional location is created. |

## Procedure

### Create Functional Location

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this test step you maintain a functional location structure that consists of one highest level functional location and two subordinate functional locations.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data specialist SAP_BR_MD_SPECIALIST_EAM. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Technical Object (EAMS_WDA_TECHOBJ_OIF (EAMS_WDA_TECHOBJ_OIF_CFG_V2)). | A new window opens, showing the Create Technical object: Initial Screen. |  |
| 3 | Create Functional Location | On the Create Technical Object screen, select the Technical Object Type: Functional Location.On the next screen, enter the following:Technical Object Type: Functional LocationStructure Indicator: YBPM (Structure Indicator for Best Practice)Technical Object: <For example 1711 >Technical Object Category: M (Technical system-standard)Choose Continue. |  |  |
| 4 | Maintain General Data | On the Create Technical Object: 1711 screen, in the General Data section, enter the following:Description: <For example, Air Compressor 1 Plant >Optionally maintain further general data, then navigate to the Location Data section. | The create technical object: general data screen appears. |  |
| 5 | Maintain Location Data | In the Location Data section, enter the following:Maintenance Plant: <For example, 1710 for US>Note Technical objects that belong to the same structure must all have the same plant assigned. As an alternative, you can leave the plant information empty for all technical objects.Optionally maintain further details, such as address information. | The create technical object: location data screen appears. |  |
| 6 | Maintain Organizational Data | In the Organizational Data section, enter the following:Planning Plant: <For example, 1710 for US>Maintenance Work Center: <For example, RES-0100 for US>Cost Center: <For example, 17101701 for US>Optionally you can maintain additional information like, for example, partner information, and so on in the Organizational Data section. | The create technical object: Organizational data screen appears. |  |
| 7 | Save Functional Location | Optionally you can maintain additional information for other sections.Click on Check Entries button.Choose Save.Then navigate back to the Home screen. | Functional location is created. |  |
| 8 | Create Subordinate Functional Location | To maintain a functional location structure, proceed as described in the above steps, and maintain the following functional locations:Technical Object: 1711-001Description: <for example, Compressor # 1 >In the Location Data section, enter the following:Location: <For example, YB_1701>Plant Section: YOHIn the Organizational Data section, maintain the following entries:Planner Group: <For example, 920 for US>Planning plant: <For example, 1710 for US>Maintenance Work Center: <For example, RES-0100 for US>Work Center Plant: <For example, 1710 for US>Catalog Profile: <For example, YB-PM0003 for US >Optionally you can maintain additional information in other sections.Choose Check Entries button.Choose Save.Enter the following:Technical Object: 1711-002Description: <for example, Compressor # 2 >In the Location Data section, enter the following:Location: < for example, YB_1702>Plant Section: <YOH>In the Organizational Data section, maintain the following entries:Planner Group: <for example, 920 for US>Planning Plant: <for example, 1710 for US>Maintenance Work Center:<for example, RES-0100 for US>Work Center Plant: <for example, 1710 for US>Catalog Profile: <for example, YB-PM0003 for US >Optionally you can maintain additional information for other sections.Click on Check Entries button.Choose Save. | Subordinate functional locations are created. |  |
| 9 | Review Technical Object in Asset Viewer | On the Home page, choose the Display Technical Object tile.On the Display Technical Object screen, maintain the relevant technical object, for example, 1711, then choose Continue.To review the functional location structure and the details per technical object, choose You can also: Display Technical Object in Asset Viewer. |  |  |

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
- related-to :: [[14-maintenance-service-and-projects/creacion-de-ubicacion-tecnica-mds-5lm-es-444]]
- related-to :: [[14-maintenance-service-and-projects/mds-5lm-445]]
- related-to :: [[14-maintenance-service-and-projects/mds-5lm-447]]
- related-to :: [[14-maintenance-service-and-projects/script-de-dados-mestre-criar-local-de-instalacao-mds-5lm-446]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5LM_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 12,827 chars in the whole document
