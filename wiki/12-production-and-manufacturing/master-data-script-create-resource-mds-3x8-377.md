---
id: 12-production-and-manufacturing/master-data-script-create-resource-mds-3x8-377
title: "Master Data Script: Create Resource - MDS (3X8) (3X8_S4CLD2608_Master_Data_EN_XX)"
description: "English master data test script (3X8): create a process manufacturing resource (processing unit 0008) in Manage Resources (F6176), with capacity and costing."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/process-resources-and-master-recipes]
aliases: [3X8_S4CLD2608_Master_Data_EN_XX]
keywords: [Process Manufacturing Resources and Master Recipes, production resources, resource category, master data scripts, capacity planning, standard value key, process manufacturing, resource costing, scheduling data, master recipe]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3X8_S4CLD2608_Master_Data_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-377
topic: 12-production-and-manufacturing/process-resources-and-master-recipes
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Master Data Script: Create Resource - MDS (3X8) (3X8_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3X8_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Process Manufacturing Resources and Master Recipes** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Resource - MDS (3X8) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233904654)

[2 Prerequisites 3](#_Toc233904655)

[2.1 System Access 3](#_Toc233904656)

[2.2 Roles 3](#_Toc233904657)

[2.3 Required Organizational Units 3](#_Toc233904658)

[2.4 Mandatory and Optional Master Data 3](#_Toc233904659)

[2.5 Main Parameters for Data Creation 4](#_Toc233904660)

[2.5.1 Resource Category 4](#_Toc233904661)

[3 Overview Table 5](#_Toc233904662)

[4 Test Procedures 6](#_Toc233904663)

[4.1 Creating Resource 6](#_Toc233904664)

[5 Appendix 9](#_Toc233904665)

[5.1 Create Master Recipe 9](#_Toc233904666)

## Purpose

A resource means of production and persons involved in a production process that have capacities assigned to them. Resources are divided into resource categories, such as production line, labor, storage.

Using resources, you can:

- Create a resource network structure to define the sequence of the resources used
- Define a resource hierarchy to group resources for evaluation
- Classify the resources to define their suitability for a purpose or use in an operation

## Prerequisites

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
| Production Engineer - Process Manufacturing | SAP_BR_PRODN_ENG_PROC | Production Engineering - Process Manufacturing | SAP_BR_PRODN_ENG_PROC |  |

### Required Organizational Units

| Data Segment | Depends On | Field Examples | Comments | Organizational Unit to be Used |
| --- | --- | --- | --- | --- |
| All data | Plant |  | All the data for resource depends on plant. | Plant:__________ |

### Mandatory and Optional Master Data

Resource data records may refer to other master data. The following table gives an overview of optional and mandatory master data objects to be used in a resource.

| Master Data Object | Used in Data Segment | Mandatory / Optional | Comments |
| --- | --- | --- | --- |
| Standard value key | In the resource UI, basic data tab, you find the entry of standard value key in standard value Maintenance section. | Mandatory | The system uses standard values as parameters with origin standard value in formulas to calculate execution time, capacity requirements and costs.You use the standard value key to assign a parameter ID to standard values. This parameter ID identifies the standard value in a formula. You can use the parameter ID to determine the key word for a standard value, such as setup, machine or labor. |

### Main Parameters for Data Creation

In this section, we describe some basic parameters that influence the behavior of a master record and are always required to create a resource.

#### Resource Category

The resource category determines the type of data to be maintained in the resource master record. Key differentiating resources according to their category (e.g. resource network, process unit).

| Resource Category | Description |
| --- | --- |
| 0008 | Processing Unit |

## Overview Table

This scope item consists of several process steps that are listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Creating Resource | Production Engineer - Process Manufacturing | Manage Resources (F6176) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Creating Resource

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Engineer - Process Manufacturing | The Start page displays. |  |
| 2 | Open the SAP Fiori App | Choose Manage Resources (F6176) . |  |  |
| 3 | Choose Create | Choose Create. | A new screen displays, showing the Create Resource: Initial Screen. |  |
| 4 | Enter Plant Code | Enter Plant code. | The Create Organization screen displays. |  |
| 5 | Enter Resource ID | Enter Resource ID.Note The field length of resource ID is less than 8. |  |  |
| 6 | Resource Category | Choose resource category:<0008> Processing unit |  |  |
| 7 | Choose Basic Data | Choose Basic data button on the top left corner of the screen. | The create resource: basic data screen displays. |  |
| 8 | Enter Data | On the Basic data tab, enter the following data:Description: <enter the description>Person responsible: <person responsible or responsible person for the plant>Usage: <008>Standard value key: <YBP1> |  |  |
| 9 | Input the Default values | On the Default Values tab, enter the following data:Control Key: <YBP4>Standard Value Unit of Machine: <H>Standard Value Unit of Labor: <H> |  |  |
| 10 | Set up the Capacity and Processing Formulas | On the capacities tab, enter the following data:Capacity category: <001(Machine/002(Person)>set up formula: <YBPI01>Processing formula: <YBPI02> | Choose Enter. The Create Resource Capacity: Header screen displays. |  |
| 11 | Set up Resource Capacity | In the resource capacity: Header section, enter the following data:Capacity category description: <add a description>Capacity Responsible: Choose F4 to search for responsible person for the plant.Factory calendar ID: <Calendar for your country>Active version: <1>Capacity Base Unit.: for example, DStart time:End time:Length of breaks:Operation time:Capacity utilization: <100>No. of Indiv. Cap: <10>Relevant for finite scheduling: <X>Long term Planning: <X>Can be used by several operations: <X>Choose Enter. | Choose Enter. The screen goes back to capacity overview. |  |
| 12 | Enter Scheduling Data | On the Scheduling tab, enter the following data:Capacity Category: <001(Machine/002(Person)>Duration of Setup: <YBPI01>Processing Duration: <YBPI02> |  |  |
| 13 | Enter Costing Data | On the Costing tab page, enter the following data:Cost center: <Cost center of Manufacturing for your company code>Activity type (Machine): <3>Formula (Machine): <YBPI01>Activity type （ Labor ）: <11>Formula （ Labor ）: <YBPI02>Activity unit: Choose the UOM required, for example, H |  |  |
| 14 | Save Your Data | Save your entries. |  |  |

## Appendix

### Create Master Recipe

| Master Data Object | Used in Data Segment | Mandatory / Optional | Comments |
| --- | --- | --- | --- |
| Master Recipe |  |  | To execute this activity, run the Create Master Recipe (3X9) test script. |

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
- related-to :: [[12-production-and-manufacturing/crear-recurso-mds-3x8-378]]
- related-to :: [[12-production-and-manufacturing/mds-3x8-379]]
- related-to :: [[12-production-and-manufacturing/mds-3x8-381]]
- related-to :: [[12-production-and-manufacturing/script-de-dados-mestre-criar-recurso-mds-3x8-380]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3X8_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 10,781 chars in the whole document
