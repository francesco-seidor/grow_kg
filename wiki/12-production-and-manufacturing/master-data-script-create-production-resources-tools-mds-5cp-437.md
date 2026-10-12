---
id: 12-production-and-manufacturing/master-data-script-create-production-resources-tools-mds-5cp-437
title: "Master Data Script: Create Production Resources/Tools - MDS (5CP) (5CP_S4CLD2608_Master_Data_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition master data script (5CP, 02-07-26) for creating material, miscellaneous, document and equipment PRTs and assigning them to routings and production orders."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/production-resources-tools]
aliases: [5CP_S4CLD2608_Master_Data_EN_XX]
keywords: [Production Resources/Tools (PRTs), production resources tools, material prt, miscellaneous prt, document prt, equipment prt, prt assignment in routing, prt assignment in production order, prt status, prt control key]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5CP_S4CLD2608_Master_Data_EN_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-437
topic: 12-production-and-manufacturing/production-resources-tools
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Master Data Script: Create Production Resources/Tools - MDS (5CP) (5CP_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5CP_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Production Resources/Tools (PRTs)** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Production Resources/Tools - MDS (5CP) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233904782)

[2 Prerequisites 3](#_Toc233904783)

[2.1 System Access 3](#_Toc233904784)

[2.2 Roles 3](#_Toc233904785)

[2.3 Required Organizational Units 4](#_Toc233904786)

[2.4 Mandatory and Optional Master Data 4](#_Toc233904787)

[2.5 Main Parameters for Data Creation 4](#_Toc233904788)

[2.5.1 PRT Status 4](#_Toc233904789)

[2.5.2 PRT Control Key 5](#_Toc233904790)

[3 Overview Table 6](#_Toc233904791)

[4 Procedures 7](#_Toc233904792)

[4.1 Create Production Resources/Tools 7](#_Toc233904793)

[4.1.1 Create Material PRT 7](#_Toc233904794)

[4.1.2 Create Miscellaneous PRT 8](#_Toc233904795)

[4.1.3 Create Document PRT 9](#_Toc233904796)

[4.1.4 Create Equipment PRT 10](#_Toc233904797)

[4.2 Assign PRT in Routing (Optional) 11](#_Toc233904798)

[4.3 Assign PRT in Production Order (Optional) 13](#_Toc233904799)

[5 Appendix 16](#_Toc233904800)

## Purpose

In this document you find a description of how to create a Production Resources/Tools master data record for your SAP S/4HANA Cloud Private Edition system. Unlike machines and fixed assets, PRTs (Production Resources/Tools) are movable (not stationary) operating resources that are required to perform an activity and can be used repeatedly.

There are several categories of Production Resources/Tools available. The category determines the characteristics and business functions that a PRT can have.

You can create your own PRT under the instruction of this Master Data Script.

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
| Production Supervisor - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC | Production Management - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC |  |
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Products / Product Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |
| Design Engineer | SAP_BR_DESIGN_ENGINEER | Document Management | SAP_BR_DESIGN_ENGINEER |  |
| Maintenance Planner | SAP_BR_MAINTENANCE_PLANNER | Maintenance Planning | SAP_BR_MAINTENANCE_PLANNER |  |

### Required Organizational Units

Some segments of material master data are dependent on the organizational units of the company, General (Central) Data does not depend on an organizational unit or the company code. The following table gives an overview of these different data segments and their relevant organizational units:

| Data Segment | Depends On | Field Examples | Comments | Organizational Unit to be Used |
| --- | --- | --- | --- | --- |
| All Data | Plant |  | All the data depends on plant.. | Plant:____________ |

### Mandatory and Optional Master Data

Reference Routing data records may refer to other master data. The following table gives an overview of optional and mandatory master data objects to be used in a Reference routing.

| Master Data Object | Used in Data Segment | Mandatory / Optional | Comments |
| --- | --- | --- | --- |
| Routing | Assign PRT in Routing | Optional | We suppose you have a routing and you want to assign PRT to it. |

### Main Parameters for Data Creation

In this section, we describe some basic parameters that influence the behavior of a master record and are always required to create a PRT master data record:

#### PRT Status

The PRT status controls the usage of production resources/tools. Depending on its status, a production resource/tool can be released for various tasks in PRT maintenance.

| PRT Status | Description |
| --- | --- |
| 01 | Created on |
| 02 | Released for PRT usage planning |
| 03 | Released for production |

#### PRT Control Key

The PRT control key determines whether the PRTs are allocated to a task list or an order are included in the following business functions:

| PRT Control Profile | Description |
| --- | --- |
| 1 | All functions |
| 2 | Print |

## Overview Table

This scope item consists of several process steps that are listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction / App | Expected Results |
| --- | --- | --- | --- |
| [Create Material PRT](#unique_11) [page ] 7 | Master Data Specialist - Product Data | Create Material (MM01) |  |
| [Create Miscellaneous PRT](#unique_12) [page ] 8 | Production Engineer - Discrete Manufacturing | Manage Production Resources And Tools (F7653) |  |
| [Create Document PRT](#unique_13) [page ] 9 | Design Engineer | Manage Documents (F2733) |  |
| [Create Equipment PRT](#unique_14) [page ] 10 | Maintenance Planner | Create Technical Object (W0029) |  |
| [Assign PRT in Routing (Optional)](#unique_15) [page ] 11 | Production Engineer - Discrete Manufacturing | Change Routing (CA02) |  |
| [Assign PRT in Production Order (Optional)](#unique_16) [page ] 13 | Production Supervisor - Discrete Manufacturing | Change Production Order (CO02) |  |

## Procedures

This section describes procedures for each segment or process step that is part of this master record.

### Create Production Resources/Tools

#### Create Material PRT

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This chapter shows you how to create a material PRT.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The Start page appears. |  |
| 2 | Open the SAP Fiori App | Open Create Material (MM01). | A new window opens, showing Create Material (Initial Screen). |  |
| 3 | Enter Material Basic Data | On the Create Material (Initial Screen), make the following entries:Material: <Material number>, for example, PRT_01Material Type: Production Resources/ToolsChoose Select View(s). | The Select View(s) view displays. |  |
| 4 | Choose Views | On the Select View(s) screen, select view:Basic ViewProduction Resources/ToolsOther necessary viewsChoose Continue. |  |  |
| 5 | Enter Organizational Levels Data | On the Organizational Levels view, in the Organizational level section, make the following entries:Plant: <Plant code>, for example, 1010Press Enter. |  |  |
| 6 | Enter Basic View Data | On the Basic data 1 tab, enter the following data:Description: <Finished assembly PRT>Base Unit of Measure: <EA>Choose the Production Resources/Tools tab. | Basic Data is saved. |  |
| 7 | Enter Production Resources/Tools Data | On the Production Resources/Tools tab, enter the following data:PRT Usage: <009>PRT Control Profile: <1>Choose Save. | The screen goes back to initial screen.Material PRT_01 is created. |  |

#### Create Miscellaneous PRT

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This chapter shows you how to create a miscellaneous PRT.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Engineer - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Production Resources And Tools (F7653). | The app opens. |  |
| 3 | Choose Create | Choose Create. | A new window opens, displaying the Create PRT screen. |  |
| 4 | Enter Name | Make the following entries:Production Resource/Tool: <Name>, for example, PRT_02Choose Basic data. | The Create Production Resource/Tool: Basic Data screen displays. |  |
| 5 | Enter Basic Data | Provide a description for your created PRT:Find the Description of the Production Resource/Tool tooltip and enter: <Miscellaneous PRT 02>In the Basic Data section, make the following entries:Status: <03>PRT Usage: <009>Base unit of measure: <EA>Choose Save. | The screen goes back to the initial screen.Production Resource/Tool is created. |  |

#### Create Document PRT

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This chapter shows you how to create a Document PRT.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Design Engineer. | The Start page appears. |  |
| 2 | Open the SAP Fiori App | Open Manage Documents (F2733). | A new window opens, showing Manage Documents. |  |
| 3 | Create the Document | Choose Create.On the Document screen, make the following entries:Document Type: <SPP>Document Description: <PRT_03>Choose Create. | The document is created.Note down the Document Number. |  |
| 4 | Edit the Document | Choose Edit at the top right corner.In the Document Data section, change the Document Status into In Work.In the Originals section, choose Upload, and then attach a PRT Document from your PC.Choose Save. | The document is saved. |  |
| 5 | Release the Document | Choose Edit at the top right corner.In the Document Data section, change the Document Status int Released.Choose Save. | The document is saved. |  |

#### Create Equipment PRT

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This chapter shows you how to create Equipment PRT.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Maintenance Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Technical Object (W0029). | The app opens. |  |
| 3 | Create Equipment | On the Create Technical Object screen, select the Technical Object Type: Equipment.On the next screen, enter the following:Technical Object Type: EquipmentTechnical Object: leave emptyValid From: today's dateTechnical Object Category: P (Production resources/tools)Choose Continue. |  |  |
| 4 | Maintain General Data | On the Create Technical Object: <Equipment ID> screen, in the General Data section, enter the following:Description: <For example, PRT equipment>Optionally, maintain further general data, then navigate to the PRT Data section. | The Create technical object: general data screen appears. |  |
| 5 | Maintain PRT Data | In the PRT Data section, enter the following:Task List usage: 009 (All task list types)Control Key: 1 (All functions)Optionally, maintain further details. For example, you can create a Measuring Point assigned with some Characteristics, and then attach the Measuring Point in field Measuring Point, and select checkbox for field Load Records. | The Create technical object: location data screen appears. |  |
| 6 | Save Equipment | Optionally, you can maintain additional information for other sections.Choose Save. | Equipment is created. Note down the equipment number. |  |

### Assign PRT in Routing (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This chapter shows you how to assign Material PRT, Miscellaneous PRT, Document PRT, or Equipment PRT in routing. You can assign different types of production resources and tools to the task lists and production orders for which they are required. PRTs assigned to the task list will be automatically copied to the production order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Engineer - Discrete Manufacturing. | The Start page appears. |  |
| 2 | Open the SAP Fiori App | Open Change Routing (CA02). | A new window opens, showing Change Routing: Initial Screen. |  |
| 3 | Enter Material | Make following entries and choose Continue:Material: <Material number>Plant: <Plant code>, for example, 1010 | The Change Routing: Operation Overview screen appears. |  |
| 4 | Select Operation | Select an item and choose Operations.Choose an operation which you want to assign PRT. Then choose PRT. | The Change Routing: PRT Overview screen appears. |  |
| 5 | Assign Material PRT | When there’s no PRT existing in the operation, make following entries in the dialog: Change Routing: New PRTs.If there already have any, choose Material, make following entries and press the green check mark:PRT Item Number: <0010>Material: <Material number>, for example, PRT_01Plant: <Plant code>, for example, 1010 | Material PRT is assigned to operation. |  |
| 6 | Assign Miscellaneous PRT | Choose Other, make following entries and press the green check mark:PRT Item Number: <0020>Production Resources/Tools: <Name>, for example, PRT_02 | Miscellaneous PRT is assigned to operation. |  |
| 7 | Assign Document PRT | Choose Document, make following entries and press the green check mark:PRT Item Number: <0030>Document: <Document number created in pervious step>Document Type: <SPP>Document Part: <000>Document version: <00>Quantity: <1 EA>Ctrl Prof.: <1> | Document PRT is assigned to operation. |  |
| 8 | Assign Equipment PRT | Choose Equipment, make following entries and choose the green check mark:Equipment: <Equipment number created in pervious step> |  |  |
| 9 | Save the Changes | Choose Save. | Routing is saved. |  |

### Assign PRT in Production Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This chapter shows you how to assign Material PRT, Miscellaneous PRT, Document PRT or Equipment PRT for an operation in a production order. Make sure you have a production order created upfront. You can also assign PRTs in the operation overview tab during order creation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The Start page appears. |  |
| 2 | Access the SAP Fiori App | Open Change Production Order (CO02). | A new window opens, showing Production Order Change: Initial Screen. |  |
| 3 | Enter Order Information | Make the following entries and choose Continue:Order: <Order number> | The Production Order Create: Change screen appears. |  |
| 4 | Choose an Operation | Choose Operations.In the Operation Overview table, choose the check box for one operation, for example, Operation 0010, and choose PRT. | A new dialog Production Order Change: PRT New Entries appears if there’s no PRT existing in the operation.If there is already any, the Production Resources/Tools Overview table will display. |  |
| 5 | Assign Material PRT | When there’s no PRT existing in the operation, make following entries in the dialog Production Order Change: PRT New Entries:If there already have one, choose the + at the bottom of Production Resources/Tools Overview and make following entries:Item Number: for example, 0010Material: for example, PRT_01Plant: for example, 1010Choose the green check mark. | Material PRT is assigned to operation. |  |
| 6 | Assign Miscellaneous PRT | Choose the + at the bottom of Production Resources/Tools Overview and choose Other. Then make following entries:Item Number: for example, 0020PRT: for example, PRT_02Choose the green check mark. | Miscellaneous PRT is assigned to operation. |  |
| 7 | Assign Document PRT | Choose the + at the bottom of Production Resources/Tools Overview and choose Document. Then make following entries:Item Number: <0030>Document: <Document number created in pervious step>Document Type: <SPP>Document Part: <000>Document Version: <00>Quantity: <1 EA>Control Key: <1>Choose the green check mark. | Document PRT is assigned to operation. |  |
| 8 | Assign Equipment PRT | Choose the + at the bottom of Production Resources/Tools Overview and choose Equipment. Then make following entries:Equipment:<Equipment number created in pervious step>Control Profile: 1 (All functions)Choose the green check mark. |  |  |

## Appendix

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
> Flagged while digesting this document, not verified: Purpose text says 'SAP S/4HANA Cloud Private Edition system' while the document is for Public Edition

## Connections
- part-of :: [[_cluster]]
- related-to :: [[12-production-and-manufacturing/master-data-script-mds-5cp-japanese-439]]
- related-to :: [[12-production-and-manufacturing/mds-5cp-441]]
- related-to :: [[12-production-and-manufacturing/script-de-dados-mestre-criar-meio-auxiliar-de-producao-mds-5cp-440]]
- related-to :: [[12-production-and-manufacturing/script-de-datos-maestros-creacion-de-medios-auxiliares-de-fabricacion]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5CP_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 21,768 chars in the whole document
