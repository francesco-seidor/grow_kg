---
id: 12-production-and-manufacturing/create-material-bom-for-production-and-sales-mds-bnk-623
title: Create Material BOM for Production and Sales - MDS (BNK) (BNK_S4CLD2608_Master_Data_EN_XX)
description: "SAP S/4HANA Cloud Public Edition 2608 master data script (BNK): create change number, production BOM (usage 1) and sales BOM (usage 5) with item categories."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/material-boms]
aliases: [BNK_S4CLD2608_Master_Data_EN_XX]
keywords: [Material BOMs for Production and Sales, material bom, sales bill of material, change master, bom usage, bom item categories, business roles, routing, master data scripts, product master]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNK_S4CLD2608_Master_Data_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-623
topic: 12-production-and-manufacturing/material-boms
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Create Material BOM for Production and Sales - MDS (BNK) (BNK_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNK_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Material BOMs for Production and Sales** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Material BOM for Production and Sales - MDS (BNK) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233904968)

[2 Prerequisites 3](#_Toc233904969)

[2.1 System Access 3](#_Toc233904970)

[2.2 Roles 3](#_Toc233904971)

[2.3 Required Organizational Units 3](#_Toc233904972)

[2.4 Mandatory and Optional Master Data 4](#_Toc233904973)

[2.5 Main Parameters for Data Creation 4](#_Toc233904974)

[2.5.1 BOM Usage 4](#_Toc233904975)

[3 Overview Table 5](#_Toc233904976)

[4 Test Procedures 6](#_Toc233904977)

[4.1 Create Change Number 6](#_Toc233904978)

[4.2 Create Production Bill of Material 7](#_Toc233904979)

[4.3 Create Sales Bill of Material 9](#_Toc233904980)

[5 Appendix 11](#_Toc233904981)

[5.1 Follow-up Processes: Create Routing 11](#_Toc233904982)

## Purpose

A production bill of material is a formally structured list of the components that make up a product or assembly (part of a product). The list contains the object number of each component, together with the quantity and unit of measure. A component might be a raw material or a semi-finished material representing an assembly.

It is used in an MRP run to calculate material requirements and in transactions such as a production order. Information is specific to a production site (known as a plant).

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
| BOM Engineer | SAP_BR_BOM_ENGINEER | Bills Of Material | SAP_BR_BOM_ENGINEER |  |

### Required Organizational Units

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers and vendors, for example, depending on the operational focus of your company.

Use your own master data or the following sample data to go through the test procedure.

### Mandatory and Optional Master Data

BOM data records may refer to other master data. The following table gives an overview of optional and mandatory master data objects to be used in a BOM

| Master Data Object | Used in Data Segment | Mandatory / Optional | Comments |
| --- | --- | --- | --- |
| Material | In the create material BOM: Initial Screen and Create material BOM: general Item View, enter Material Number in Material and Component. | Mandatory | Complete the following Master Data Scripts as a prerequisite before beginning process steps:Create Product Master of type "Raw Material" - MDS (BNR)Create Product Master of type "Semi-Finished Good" - MDS (BNS)Create Product Master of type "Finished Good" - MDS (BNT)Create Product Master of type "Trading Good" - MDS (BNF) |

### Main Parameters for Data Creation

In this section, we describe some basic parameters that influence the behavior of a master record and are always required to create a bill of material:

#### BOM Usage

Bill of Materials (BOM) usage defines the area (such as Sales or Production) where a Material BOM can be used.

| BOM usage | Description |
| --- | --- |
| 1 | Production |
| 5 | Sales and Distribution |

## Overview Table

This scope item consists of several process steps that are listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Change Number](#unique_10) [page ] 6 | BOM Engineer | Create Change Master (CC01) |  |
| [Create Production Bill of Material](#unique_11) [page ] 7 | Production Engineer - Discrete Manufacturing | Maintain Bill Of Material (Version 2) - Create, change & display BOMs (F1813A) |  |
| [Create Sales Bill of Material](#unique_12) [page ] 9 | Production Engineer - Discrete Manufacturing | Maintain Bill Of Material - Create, change & display BOMs (F1813) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Change Number

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Creation of the Change Master that will be used for the Bill of Material creation in the next steps of Production and Bill of Material.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a BOM Engineer. |  |  |
| 2 | Access the SAP Fiori App | Open Create Change Master (CC01). |  |  |
| 3 | Enter Change Number | On the Create Change Master: Initial Screen screen, enter the following data and press Enter.Change Number: <Enter your change number, for Example:CN001>Leave default values in other fields. |  |  |
| 4 | Enter Change Master data | On the Create Change Master: Change Header screen, enter data as provided in the following example and press Enter:Field beside Change Number: Change Master for MBOMValid From: TodayChange no. status: 01 Active |  |  |
| 5 | Select Checkboxes for Bill of Material | On the Create Change Master: Object Types screen, Object types table, Bill of Material row, select the following checkboxes:Actv.ObjectMgtRec |  |  |
| 6 | Choose Save | Choose Save. | The Change Master is created. |  |

### Create Production Bill of Material

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
| 2 | Access the SAP Fiori App | Open Maintain Bill Of Material (Version 2) - Create, change & display BOMs (F1813A). |  |  |
| 3 | Create BOM | Choose Create BOM. On the Create BOM screen, enter following data and choose OK.Material : <Finished/Semi-finished material number>Change Number: <your change number created in perious step>Plant: <Your Plant>BOM usage: 1 (for production only) |  |  |
| 4 | Add Components Data | In the Components section, choose Add icon to add one or more components.Item Category ICt: <L for stock item>Component: <Material Number, Raw/semi product>Quantity: <Quantity>Component UoM: PC | Components data are added. |  |
| 5 | Enter BOM Item Category Non Stock (‘N’) | In the Components section, choose the Add icon to add one or more components.Item Category ICt: <N for Non stock item>Component: <Material Number, Raw/semi product>Component quantity: <Quantity>Component UoM: PCPress Enter to enable Component and Component Quantity fields.Note This item category is used for components which are not kept in stock, Non-stock items can be entered in the BOM with or without a master record. | Components data for non stock items are added. |  |
| 6 | Enter BOM Item Category Variable Size (‘R’) | In the Components section, choose the Add icon to add one or more components.Item Category ICt: <R for variable size item>Component: <Material Number, Raw/semi product>Select the arrow to open the Details page.On the Variable size item data make the required entries.Size 1: <Enter your dimensions of variable size items>Size 2: <Enter your dimensions of variable size items>Size3: <Enter your dimensions of variable size items>Size Unit: <Enter your unit of measure for the quantity of a variable-size item>Formula Key: <Enter the formula to calculate variable size item>No of Variable size items: <Quantity>Qty of variable size item: <A quantity calculated for the variable size items>Choose Apply.Note This item category enables you to specify different sized sections of a component with one material, such as the size of a steel sheet required to repair some planking. | Components data for Variable Items are added/calculated. |  |
| 7 | Enter BOM Item Category Text Item (‘T’) | For the new BOM Item Number line, make entries similar to the following example:Item Category: Text itemIn the BOM Item Number line,Select the arrow to open the Details page.On the Maintain Bill of Material-Basic Details screen,Component quantity: 1Component UoM: PCSelect the Status/Long Text tab to display the Item Text.Item Text: Documentation | Text documents data for text Items are added. |  |
| 8 | Check Header | In the Header Attributes section, you can check the data and change if needed. |  |  |
| 9 | Save Your Data | Save your entries. | Message Material BOM saved displays. |  |

### Create Sales Bill of Material

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
| 2 | Access the SAP Fiori App | Choose Maintain Bill Of Material - Create, change & display BOMs (F1813). |  |  |
| 3 | Create BOM | Choose Create BOM. On the Create BOM screen, enter following data and choose OK.Material:<BOM header material number>, for example, SDBOMERLAHD, or SDBOMLUMFHDPlant: <enter your Plant>Change Number: <your change number created in the previous step>BOM usage: 5 |  |  |
| 4 | Add Components Data | In the Components section, choose the Add icon to add one or more components.Item Category ICt: <L for stock item>Component: <Material Number, Trading Goods>Quantity: <quantity> | Components data are added. |  |
| 5 | Check Header | In the Header Attributes section, you can check the data and change if needed. |  |  |
| 6 | Save Your Data | Save your entries. | Message Material BOM saved displays. |  |

## Appendix

### Follow-up Processes: Create Routing

| Master Data Object | Used in Data Segment | Mandatory / Optional | Comments |
| --- | --- | --- | --- |
| Routing |  |  | To execute this activity, complete the Create Routing - MDS (BNL) test script. |

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
- related-to :: [[12-production-and-manufacturing/bom-mds-bnk-625]]
- related-to :: [[12-production-and-manufacturing/crear-lista-de-materiales-para-material-para-produccion-y-ventas-mds-b]]
- related-to :: [[12-production-and-manufacturing/mds-bnk-627]]
- related-to :: [[12-production-and-manufacturing/script-de-dados-mestre-criar-lista-tecnica-de-materiais-para-producao]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNK_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 15,013 chars in the whole document
