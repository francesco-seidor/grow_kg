---
id: 12-production-and-manufacturing/master-data-script-create-routing-mds-bnl-629
title: "Master Data Script: Create Routing - MDS (BNL) (BNL_S4CLD2608_Master_Data_EN_XX)"
description: Master data script BNL for creating a production routing in SAP S/4HANA Cloud Public Edition with Manage Routings (F5425) as Production Engineer.
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/routings-and-reference-operation-sets]
aliases: [BNL_S4CLD2608_Master_Data_EN_XX]
keywords: [Routings and Reference Operation Sets, production routing, master data scripts, work centers, operations control key, component allocation, external operations, business roles, required master data, BNL]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNL_S4CLD2608_Master_Data_EN_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-629
topic: 12-production-and-manufacturing/routings-and-reference-operation-sets
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Master Data Script: Create Routing - MDS (BNL) (BNL_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNL_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Routings and Reference Operation Sets** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Routing - MDS (BNL) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233904960)

[2 Prerequisites 3](#_Toc233904961)

[2.1 System Access 3](#_Toc233904962)

[2.2 Roles 3](#_Toc233904963)

[2.3 Required Organizational Units 3](#_Toc233904964)

[2.4 Mandatory and Optional Master Data 4](#_Toc233904965)

[2.5 Main Parameters for Data Creation 4](#_Toc233904966)

[2.5.1 Usage 4](#_Toc233904967)

[3 Overview Table 6](#_Toc233904968)

[4 Test Procedures 7](#_Toc233904969)

[4.1 Creating Routing 7](#_Toc233904970)

## Purpose

A production routing defines the production process for a material. It contains the operations or work steps to be carried out during production. It defines the use of materials and work centers. It forms a template for a production order and is the basis for product costing.

A routing is defined for a finished product or semi-finished product and is specific to a production site (known as a plant). It applies for a given lot size and consists of a number of operations with each one allocated to a work center.

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
| All data | Plant |  | All the data for a routing depends on plant. | Plant:__________ |

### Mandatory and Optional Master Data

Routing data records may refer to other master data. The following table gives an overview of optional and mandatory master data objects to be used in a routing.

| Master Data Object | Used in Data Segment | Mandatory / Optional | Comments |
| --- | --- | --- | --- |
| Material |  | Mandatory | Complete the following test script as prerequisite before executing process steps:Create Product Master of type "Raw Material" - MDS (BNR)Create Product Master of type "Semi-Finished Good" - MDS (BNS)Create Product Master of type "Finished Good" - MDS (BNT) |
| Work Center | In create routing: operation overview screen, select a work center for an internal operation | Mandatory, (Optional) | For an external operation the work center is not a mandatory input field.If required, execute the Create Routing - MDS (BNL) test script. |
| Bill of Material |  | Optional | Execute the Create Material BOM for Production and Sales - MDS (BNK) test script. |
| Purchasing Info Record |  | (Mandatory) | For an external operation, you could use a purchasing info record to capture all supply relevant data |
| Material Group |  |  |  |
| Cost Element |  |  |  |

### Main Parameters for Data Creation

In this section, we describe some basic parameters that influence the behavior of a master record and are always required to create a routing:

#### Usage

| Work Center category | Description |
| --- | --- |
| 1 | Production |
| 2 | Engineering/Design |
| 3 | Universal |

## Overview Table

This scope item consists of the process step listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction | Expected Results |
| --- | --- | --- | --- |
| [Creating Routing](#unique_10) [page ] 7 | Production Engineer - Discrete Manufacturing | Manage Routings (F5425) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Creating Routing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Engineer - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Routings (F5425). | The app opens. |  |
| 3 | Choose Create | Choose Create. | A new window opens, displaying the Create Routing screen. |  |
| 4 | Set up the Create Routing Screen | Enter the following data on the Create Routing screen:Material : <Finished/Semi-finished material number>Plant: <Your Plant number>Choose Continue. | The Create Routing: Header Details screen displays. |  |
| 5 | Set up the Create Routing: Header Details Screen | Enter the following data on the Create Routing: Header Details screen:Usage: <1 for production>Status: <4 released-general>From lot size - to lot size: <Enter Lot size interval and unit of measure> |  |  |
| 6 | Set up the Create Routing: Operation Overview Screen | Choose Operation and the Create Routing: Operation Overview Screen displays.Enter the following data on the Create Routing: Operation Overview Screen:Work Center: required for internal operations, (blank) for external operationsControl Key: <YBP1/YBP2/YBP3/YBP5>YBP1 for internal operation w/o autom. goods receiptYBP2 for external operation (PP subcontracting)YBP3 for internal operation with autom. goods receiptYBP4 for process manufacturing milestoneDescription: <Enter a description for the operation>And then double-click your entered operation. |  |  |
| 7 | External Operation Set up for the External Processing Section | Enter the following data on the Create Routing: Operation Details screen:Purchasing info record: required for internal operations, (blank)for external operationsMaterial group: L002/L003Cost element: <relevant cost element for your country>Purchasing Organization: <purchasing organization>. |  |  |
| 8 | Internal Operation Set up for Standard Value Section | Enter the following data on the Create Routing operation Details screen:Setup: <setup time>Machine: <Machine operation time>Labor: <labor time> |  |  |
| 9 | Add More Operations | Repeat the previous steps for each operation. |  |  |
| 10 | Choose a Component | Choose Component Allocation from the top of the view, and then select a component. | The Material Component Overview view displays. |  |
| 11 | Create a New Assignment | Choose New assignment. | A New Assignment dialog box displays. |  |
| 12 | Assign to Oper./act. List | Choose Oper./act. List. |  |  |
| 13 | Choose Operation | Select an operation and press Enter. |  |  |
| 14 | Assign Other Components | Repeat the previous steps for other components. |  |  |
| 15 | Save Your Data | Save your entries. | Routing is created. |  |

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
> Flagged while digesting this document, not verified: Step 7 says purchasing info record is 'required for internal operations, blank for external', while prerequisites table says it is used for external operations; internal inconsistency.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[12-production-and-manufacturing/arbeitsplan-anlegen-sds-bnl-628]]
- related-to :: [[12-production-and-manufacturing/creacion-de-hoja-de-ruta-mds-bnl-630]]
- related-to :: [[12-production-and-manufacturing/criar-roteiro-mds-bnl-632]]
- related-to :: [[12-production-and-manufacturing/mds-bnl-631]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNL_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 10,954 chars in the whole document
