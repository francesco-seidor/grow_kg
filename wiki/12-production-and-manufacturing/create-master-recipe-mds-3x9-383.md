---
id: 12-production-and-manufacturing/create-master-recipe-mds-3x9-383
title: Create Master Recipe - MDS (3X9) (3X9_S4CLD2608_Master_Data_EN_XX)
description: "SAP S/4HANA Cloud master data script (3X9, EN): creating a master recipe for process manufacturing in the Manage Master Recipes app (F5426)."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/process-resources-and-master-recipes]
aliases: [3X9_S4CLD2608_Master_Data_EN_XX]
keywords: [Process Manufacturing Resources and Master Recipes, master recipe, process manufacturing, master data scripts, test procedures, business roles, organizational units, mandatory master data, task list usage, production version]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3X9_S4CLD2608_Master_Data_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-383
topic: 12-production-and-manufacturing/process-resources-and-master-recipes
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Create Master Recipe - MDS (3X9) (3X9_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3X9_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Process Manufacturing Resources and Master Recipes** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Master Recipe - MDS (3X9) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233904725)

[2 Prerequisites 3](#_Toc233904726)

[2.1 System Access 3](#_Toc233904727)

[2.2 Roles 3](#_Toc233904728)

[2.3 Required Organizational Units 3](#_Toc233904729)

[2.4 Mandatory and Optional Master Data 4](#_Toc233904730)

[2.5 Main Parameters for Data Creation 4](#_Toc233904731)

[2.5.1 Usage 4](#_Toc233904732)

[3 Overview Table 6](#_Toc233904733)

[4 Test Procedures 7](#_Toc233904734)

[4.1 Creating Master Recipe 7](#_Toc233904735)

[5 Appendix 10](#_Toc233904736)

[5.1 Modifying Master Recipe with Change Management Procedure 10](#_Toc233904737)

## Purpose

You can use the master recipe to describe an enterprise-specific process in process industries without relating to a specific order.

Master recipes are mainly used for planning the manufacture of products. However, you can also use them to describe the clean-out or changeover of a production line.

Master recipes are used as a reference for process orders as well as the basis for product costing.

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
| Production Engineer - Process Manufacturing | SAP_BR_PRODN_ENG_PROC | Production Engineering - Process Manufacturing | SAP_BR_PRODN_ENG_PROC |  |

### Required Organizational Units

| Data Segment | Depends On | Field Examples | Comments | Organizational Unit to be Used |
| --- | --- | --- | --- | --- |
| All data | Plant |  | All the data for a Master Recipe depends on plant. | Plant:__________ |

### Mandatory and Optional Master Data

Master Recipe data records may refer to other master data. The following table gives an overview of optional and mandatory master data objects to be used in a Master Recipe.

| Master Data Object | Used in Data Segment | Mandatory / Optional | Comments |
| --- | --- | --- | --- |
| Material |  | Mandatory | Complete the following test script as prerequisite before executing process steps:Create Product Master of type "Raw Material" - MDSCreate Product Master of type "Semi-Finished Good" - MDSCreate Product Master of type "Finished Good" - MDS |
| Resouce | In create Master Recipe: operation overview screen, select a work center for an internal operation | Mandatory, (Optional) | For an external operation the work center is not a mandatory input field.If required, execute the Create Resource - MDS test script. |
| Bill of Material |  | Optional | Execute the Create Material BOM for Production and Sales - MDS test script. |
| Purchasing Info Record |  | (Mandatory) | For an external operation, you could use a purchasing info record to capture all supply relevant data |
| Material Group |  |  |  |
| Cost Element |  |  |  |

### Main Parameters for Data Creation

In this section, we describe some basic parameters that influence the behavior of a master record and are always required to create a Master Recipe.

#### Usage

| Key of task list usage | Description |
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
| [Creating Master Recipe](#unique_10) [page ] 7 | Production Engineer - Process Manufacturing | Manage Master Recipes (F5426) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Creating Master Recipe

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Engineer - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Master Recipes (F5426). |  |  |
| 3 | Choose Create | Choose Create. | The Create Master Recipe: Initial Screen displays. |  |
| 4 | Set up the Create Master Recipe Initial Screen | On the Create Master Recipe Initial Screen, enter the following data:Material: <Finished/Semi-finished material number>Plant: <Your Plant number>Profile: <YPI1>Press Enter. | The Create Master Recipe header detail screen displays. |  |
| 5 | Set up the Create Master Recipe Header Sub-Tab | On the Create Master Recipe: Recipe screen, enter the following data on the Recipe Header sub-tab:Usage: <1 for production>Status: <4 released-general>Planner Group: <1>Press Enter. |  |  |
| 6 | Add an Operation | Enter the following data on the Operations sub-tab:Resouce: <Resouce>Control Key: <YBP4>Description: <Enter a description for the operation>.Press Enter. |  |  |
| 7 | Add a Phase | Start on a new row.Enter the following data on the Operations sub-tab:Phase Indicator: <X>Superior Operation: <Operation ID, for example, 0010>Resouce: <Resouce>Control Key: <YBP4>Description: <Enter a description for the operation>.Double-click the phase you created. | The Create Master Recipe : Operation screen displays. |  |
| 8 | Set Up for Standard Value Section of Phase | Enter the following data on the Standard Values sub-tab, and then go back:Machine: <Machine operation time>Labor: <Labor Time> |  |  |
| 9 | Add More Operations or Phase | Repeat the previous steps for each Operation or Phase.If you want to assign components at this moment, you should proceed following steps; otherwise you can save your entries and exit. |  |  |
| 10 | Choose Material | On the Create Master Recipe: Recipe screen, choose the Materials sub-tab. | The Insert Production Version dialog box displays. |  |
| 11 | Insert Production Version | In the Insert Production Version dialog box, make the following entries:Production Version: <New production version>BOM Data – Alternative BOM: <Your AltBOM>BOM Data – BOM Usage: <Usage>Choose Check. Check the relevant information and make sure no error exists, and then choose Close. | The check indicator displays as green for the BOM Data section. |  |
| 12 | Close Screen and Adopt Changes | In the Insert Production Version dialog box, choose Close Screen and Adopt Changes. | The material list displays under Material Component Assignments on the Materials sub-tab. |  |
| 13 | Create a New Assignment | Choose New assignment. | The New Assignment dialog box displays. |  |
| 14 | Assign to Oper./act. List | Choose Oper./act. List. |  |  |
| 15 | Choose Operation | Select an operation and press Enter. |  |  |
| 16 | Assign Other Components | Repeat the previous steps for other components. |  |  |
| 17 | Save Your Data | Save your entries. | Master Recipe is created. |  |
| 18 | Print Out (Optional) | Within the Manage Master Recipes (F5426) app, find and choose the Master Recipe you just created.On the Display Master Recipe: Recipe screen, choose Menu > Extras > Print Master Recipe . | A PDF file containing the Master Recipe details is downloaded. |  |

## Appendix

### Modifying Master Recipe with Change Management Procedure

If you use Master Recipe which requires approval, you may refer to the test script of scope item 5QC - Product Change Management with Change Records – Process Industries, and follow Chapter Modify Master Recipe for any change.

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
- related-to :: [[12-production-and-manufacturing/criar-receita-mestre-mds-3x9-386]]
- related-to :: [[12-production-and-manufacturing/mds-3x9-385]]
- related-to :: [[12-production-and-manufacturing/mds-3x9-387]]
- related-to :: [[12-production-and-manufacturing/script-de-datos-maestros-creacion-de-receta-de-planificacion-mds-3x9-3]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3X9_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 11,856 chars in the whole document
