---
id: 12-production-and-manufacturing/create-production-work-center-mds-bnj-617
title: Create Production Work Center - MDS (BNJ) (BNJ_S4CLD2608_Master_Data_EN_XX)
description: "SAP S/4HANA Cloud 2608 master data script BNJ: create a production work center (F6175) and optionally work center groups (F4044), with test steps."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/production-work-centers]
aliases: [BNJ_S4CLD2608_Master_Data_EN_XX]
keywords: [Production Work Centers and Work Center Groups, production work center, work center groups, work center category, capacity planning, work center costing, standard value key, routing, business roles, test procedures]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNJ_S4CLD2608_Master_Data_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-617
topic: 12-production-and-manufacturing/production-work-centers
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Create Production Work Center - MDS (BNJ) (BNJ_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNJ_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Production Work Centers and Work Center Groups** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Production Work Center - MDS (BNJ) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233904983)

[2 Prerequisites 3](#_Toc233904984)

[2.1 System Access 3](#_Toc233904985)

[2.2 Roles 3](#_Toc233904986)

[2.3 Required Organizational Units 3](#_Toc233904987)

[2.4 Mandatory and Optional Master Data 4](#_Toc233904988)

[2.5 Main Parameters for Data Creation 4](#_Toc233904989)

[2.5.1 Work Center Category 4](#_Toc233904990)

[3 Overview Table 5](#_Toc233904991)

[4 Test Procedures 6](#_Toc233904992)

[4.1 Creating Work Center 6](#_Toc233904993)

[4.2 Manage Work Center Groups (Optional) 8](#_Toc233904994)

[4.2.1 Create Work Center Group (Optional) 8](#_Toc233904995)

[4.2.2 Assign Work Center (Optional) 9](#_Toc233904996)

[5 Appendix 11](#_Toc233904997)

[5.1 Create Routing 11](#_Toc233904998)

## Purpose

A work center is where production operations are carried out. For example, a work center may represent a production line, machine, group of machines, employee or group of employees.

A work center holds information used for capacity planning (e.g. available capacity), scheduling (e.g. formula for processing time) and costing (e.g. cost center). This information is used in task lists and in transactions such as production work orders. Information is specific to a production site (known as a plant).

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
| Production Engineer - Discrete Manufacturing | SAP_BR_PRODN_ENG_DISC | Production Engineering - Discrete Manufacturing | SAP_BR_PRODN_ENG_DISC |  |

### Required Organizational Units

| Data Segment | Depends On | Field Examples | Comments | Organizational Unit to be Used |
| --- | --- | --- | --- | --- |
| All data | Plant |  | All the data for work center depends on plant. | Plant:__________ |

### Mandatory and Optional Master Data

Work center data records may refer to other master data. The following table gives an overview of optional and mandatory master data objects to be used in a work center.

| Master Data Object | Used in Data Segment | Mandatory / Optional | Comments |
| --- | --- | --- | --- |
| Standard value key | In the work center UI, basic data tab, you find the entry of standard value key in standard value Maintenance section. | Mandatory | The system uses standard values as parameters with origin standard value in formulas to calculate execution time, capacity requirements and costs.You use the standard value key to assign a parameter ID to standard values. This parameter ID identifies the standard value in a formula. You can use the parameter ID to determine the key word for a standard value, such as setup, machine or labor. |

### Main Parameters for Data Creation

In this section, we describe some basic parameters that influence the behavior of a master record and are always required to create a work center:

#### Work Center Category

The work center category determines which data can be maintained in the master record for the work center. The work centers can be distinguished by their category (for example, production work center, Maintenance work center and service work center etc.)

| Work Center category | Description |
| --- | --- |
| 0001 | Machine |
| 0007 | Production line |

## Overview Table

This scope item consists of several process steps that are listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction | Expected Results |
| --- | --- | --- | --- |
| [Creating Work Center](#unique_10) [page ] 6 | Production Engineer - Discrete Manufacturing | Manage Work Centers (F6175) |  |
| [Create Work Center Group (Optional)](#unique_11) [page ] 8 | Production Engineer - Discrete Manufacturing | Manage Work Center Groups (F4044) |  |
| [Assign Work Center (Optional)](#unique_12) [page ] 9 | Production Engineer - Discrete Manufacturing | Manage Work Center Groups (F4044) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Creating Work Center

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Engineer - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Open the SAP Fiori App | Choose Manage Work Centers (F6175). |  |  |
| 3 | Choose Create | Choose Create. | A new screen displays, showing the Create Work Center: Initial Screen. |  |
| 4 | Enter Plant Code | Enter Plant code. | The Create Organization screen displays. |  |
| 5 | Enter Work Center ID | Enter Work Center ID.Note The field length of work center ID is less than 8. |  |  |
| 6 | Work Center Category | Choose work center category:<0001> Machine<0007> Production Line |  |  |
| 7 | Choose Basic Data | Choose Basic data button on the top left corner of the screen. | The create work center: basic data screen displays. |  |
| 8 | Enter Data | On the Basic data tab, enter the following data:Description: <enter the description>Person responsible: <person responsible or responsible person for the plant>Usage: <009>Standard value key: <SAP1> |  |  |
| 9 | Set up the Capacity and Processing Formulas | On the capacities tab, enter the following data:Capacity category: <001(Machine/002(Person)>set up formula: <SAP005>Processing formula: <SAP006>Press Enter. | The Create Work Center Capacity: Header screen displays. |  |
| 10 | Set up Work Center Capacity | In the work center capacity: Header section, enter the following data:Capacity category description: <add a description>Capacity Responsible: Press F4 to search for responsible person for the plant.Factory calendar ID: <Calendar for your country>Active version: <1>Capacity Base Unit: for example, DStart time: <Start time>End time: <End time>Length of breaks: <Length of breaks>Operation time: <Operation time>Capacity utilization: <100>No. of Indiv. Cap: <10>Relevant for finite scheduling: <X>Long term Planning: <X>Can be used by several operations: <X>Press Enter. | The screen goes back to the capacity overview. |  |
| 11 | Enter Scheduling Data | On the Scheduling tab, enter the following data:Capacity Category: <001(Machine/002(Person)>Duration of Setup: <SAP001>Processing Duration: <SAP002> |  |  |
| 12 | Enter Costing Data | On the Costing tab page, enter the following data:Cost center: <Cost center for your company code>Activity type ( for set up): <3>Formula ( for set up): <SAP005>Activity type (Machine): <1>Formula (Machine): <SAP006>Activity type （Labor）: <11>Formula （Labor）: <SAP007>Activity unit: Choose the UOM required, for example, Min |  |  |
| 13 | Save Your Data | Save your entries. |  |  |

### Manage Work Center Groups (Optional)

Purpose

This chapter shows you how to group the work centers if needed.

#### Create Work Center Group (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create work center group.

You can check the sample work center groups created through the process step Create and Assign Work Center Group in scope item 31L.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as aProduction Engineer - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Work Center Groups (F4044). | The app opens. |  |
| 3 | Create Group | Choose Create above the table.On the Create Group screen, make the following entries:Group: <Enter the group name>Plant: 1010Group Type: <ALTERNATIV> or <SAME LINE> or <RSPONSBLTY>Description: <Enter the description>Choose Create. | The work center group is created. |  |

#### Assign Work Center (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to assign work centers to work center group.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Engineer - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Work Center Groups (F4044). | The app opens. |  |
| 3 | Select the Group | Find the group created in the pervious step, then choose the > icon at the end of the row. | The detailed information list displays on the right panel. |  |
| 4 | Assign Work Center | In the Group Components section, choose Assign Work Center.Select one or a few work centers from the dialog box and choose Ok.Note If a work center is already assigned to another group, there will be an error message: Work Center "XXX" already assigned to this group type. | The work centers assigned to the group display.The work centers are successfully assigned. |  |

## Appendix

### Create Routing

| Master Data Object | Used in Data Segment | Mandatory / Optional | Comments |
| --- | --- | --- | --- |
| Routing |  |  | To execute this activity, run the Create Routing - MDS (BNL) test script. |

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
- related-to :: [[12-production-and-manufacturing/mds-bnj-619]]
- related-to :: [[12-production-and-manufacturing/mds-bnj-621]]
- related-to :: [[12-production-and-manufacturing/script-de-dados-mestre-criar-centro-de-trabalho-da-producao-mds-bnj-62]]
- related-to :: [[12-production-and-manufacturing/script-de-datos-maestros-crear-puesto-de-trabajo-de-produccion-mds-bnj]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNJ_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 14,277 chars in the whole document
