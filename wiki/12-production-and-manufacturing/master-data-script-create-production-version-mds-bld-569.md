---
id: 12-production-and-manufacturing/master-data-script-create-production-version-mds-bld-569
title: "Master Data Script: Create Production Version - MDS (BLD) (BLD_S4CLD2608_Master_Data_EN_XX)"
description: Master data script BLD for creating and editing production versions in S/4HANA Cloud Public Edition 2608 using Fiori apps F6400 and F2568.
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/production-versions]
aliases: [BLD_S4CLD2608_Master_Data_EN_XX]
keywords: [Production Versions, production version, production version editing, master data prerequisites, business roles, bill of materials, task list, production engineering, production version proposals, BLD]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BLD_S4CLD2608_Master_Data_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-569
topic: 12-production-and-manufacturing/production-versions
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Master Data Script: Create Production Version - MDS (BLD) (BLD_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BLD_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Production Versions** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Production Version - MDS (BLD) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233904909)

[2 Prerequisites 3](#_Toc233904910)

[2.1 System Access 3](#_Toc233904911)

[2.2 Roles 3](#_Toc233904912)

[2.3 Required Organizational Units 3](#_Toc233904913)

[2.4 Mandatory and Optional Master Data 4](#_Toc233904914)

[3 Overview Table 5](#_Toc233904915)

[4 Test Procedures 6](#_Toc233904916)

[4.1 Create Production Version 6](#_Toc233904917)

[4.2 Edit Production Version (Optional) 9](#_Toc233904918)

## Purpose

Create Production Version

In this document you find a description of how to create a production version for your SAP S/4HANA Cloud Public Edition system. The description includes those data segments that are relevant for the SAP S/4HANA Cloud Public Edition appliance. Fields that are not relevant for the scope of SAP S/4HANA Cloud Public Edition are not described in this document.

A production version that is created as described here can be used for processing production processes.

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
| Production Engineer - Process Manufacturing | SAP_BR_PRODN_ENG_PROC | Production Engineering - Process Manufacturing | SAP_BR_PRODN_ENG_PROC |  |

### Required Organizational Units

| Data Segment | Depends On | Field Examples | Comments | Organizational Unit to be Used |
| --- | --- | --- | --- | --- |
| All data | Plant |  | All the data for production version depends on plant. | Plant:__________ |

### Mandatory and Optional Master Data

Production version data records may refer to other master data. The following table gives an overview of optional and mandatory master data objects to be used in a production version.

| Master Data Object | Used in Data Segment | Mandatory / Optional | Comments |
| --- | --- | --- | --- |
| Material | Production version is created for each material and plant. | Mandatory | On the Production Version: Mass processing screen, Material is to be entered.For Material creation, you can follow the steps in Master Data Script: Create Product Master of type "Raw Material" - MDS - BNR, Create Product Master of type "Semi-Finished Good" - MDS - BNS, or Create Product Master of type "Finished Good" - MDS - BNT. |
| Bill of Material | A BOM master data for the material is assigned in a production version | Mandatory | On the Production Version: Mass processing screen, Alternative BOM and BOM usage are to be entered.For BOM creation, you can follow the steps in Master Data Script: Create Material BOM for Production and Sales - MDS - BNK. |
| Task List | A take list for the material is assigned in a production version | Mandatory | On the Production Version: Mass processing screen, Task List type, Group, and Group counter are to be entered.For Task List creation, you can follow the steps in Master Data Script: Create Routing - MDS - BNL or Create Master Recipe - MDS - 3X9. |

## Overview Table

This scope item consists of several process steps that are listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Production Version](#unique_8) [page ] 6 | Production Engineer - Discrete Manufacturing or Production Engineer - Process Manufacturing | Process Production Versions (F6400) or Manage Production Versions (F2568) |  |
| [Edit Production Version (Optional)](#unique_9) [page ] 9 | Production Engineer - Discrete Manufacturing or Production Engineer - Process Manufacturing | Process Production Versions (F6400) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Production Version

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

It is possible to perform this step with different SAP Fiori apps. There are 3 options that you can leverage. You can choose either one of them.

Option 1

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Engineer - Discrete Manufacturing or a Production Engineer - Process Manufacturing. | The Start view displays. |  |
| 2 | Access the SAP Fiori App | Open Process Production Versions (F6400). | The app opens. |  |
| 3 | Enter Selection Fields | Make the following entries and choose Go:Material: <Enter Material number>Plant: <Enter Plant> |  |  |
| 4 | Check Production Version Proposals | On the Production Version Proposals tab, you can find the proposals for creating a new production version if the corresponding BOM/Task list combination does not exist yet.You can go through the proposal details by selecting the proposal and make possible changes. | Note Configuration Step (ID: 105965) has been introduced to configure the rules for the production version proposal. |  |
| 5 | Accept Proposal | Select the production version proposal and choose Accept Proposal. |  |  |
| 6 | Confirmation | In the Confirmation dialog box, choose OK. | A new production version is created based on the proposed parameters. You can find it under the Existing Production Versions tab. |  |

Option 2

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Engineer - Discrete Manufacturing or a Production Engineer - Process Manufacturing. | The Start view displays. |  |
| 2 | Access the SAP Fiori App | Open Process Production Versions (F6400). | The app opens. |  |
| 3 | Enter Selection Fields | Make the following entries and choose Go:Material: <Enter Material number>Plant: <Enter Plant> |  |  |
| 4 | Choose Tab | Choose the Existing Production Versions tab. |  |  |
| 5 | Create | Choose Create. In the Create Production Version dialog box, make the following entries and choose Create:Material: <Enter Material number>Plant: <Enter Plant>Production Version: <A 4 digit number>Production Version Description: <Description> |  |  |
| 6 | Input Parameters | Enter the necessary parameters and choose Create:Validity Start Date: <today>Validity End Date: <12/31/9999>Minimum Lot Size: <1>Maximum Lot Size: <999999999>Task List section:Task List Type: <Select the Task List Type for the material>Task List Group: <Select the Group for the material>Task List Counter: <Select the Group Counter for the material>Bill of Material section:Alternative BOM: <Select the Alternative BOM for the material>BOM Usage: <Select the BOM Usage of the BOM master for the material> | The production version is created. |  |

Option 3

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Engineer - Discrete Manufacturing or a Production Engineer - Process Manufacturing. | The Start view displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Production Versions (F2568). | The Production version: mass processing view displays. |  |
| 3 | Enter Plant Code | Enter Plant code. |  |  |
| 4 | Enter Material | Enter Material.Press Enter. |  |  |
| 5 | Production Version | Enter production version line items and then press Enter.Material: <Enter Material number>Production version: <A 4 digit number>Valid from: <today>Valid to: <12/31/9999>From Lot Size: <1>To Lot Size: <999999999>Alternative BOM: Press F4 to choose Alternative BOM for the materialBOM Usage: Press F4 to choose BOM usage of the BOM master for the materialGroup: <Enter the Group for the material>Group Counter: <Enter the Group Counter for the material>Type: <Select the Task List Type for the material> |  |  |
| 6 | Save Your Data | Choose Save. | The production version is created. |  |

### Edit Production Version (Optional)

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
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Engineer - Discrete Manufacturing or a Production Engineer - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Process Production Versions (F6400). | The app opens. |  |
| 3 | Enter Selection Fields | Make the following entries and choose Go:Material: <Enter Material number>Plant: <Enter Plant> |  |  |
| 4 | Navigate to the Existing Production Versions Tab | Go to the Existing Production Versions tab. |  |  |
| 5 | Edit Production Version | Choose the production version that you want to change and choose Edit on the Production Version screen.Make necessary changes to the fields depending on your requirements.Note If you want to make similar changes to multiple production versions, you can make multi-selection on the Existing Production Versions tab and choose Mass Edit.In the Mass Edit dialog box, you can make required changes to the listed fields. |  |  |
| 6 | Save | Choose Save. | The production version is updated successfully. |  |

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
- related-to :: [[12-production-and-manufacturing/fertigungsversion-anlegen-sds-bld-568]]
- related-to :: [[12-production-and-manufacturing/mds-bld-571]]
- related-to :: [[12-production-and-manufacturing/mds-bld-573]]
- related-to :: [[12-production-and-manufacturing/script-de-dados-mestre-criar-versao-de-producao-mds-bld-572]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BLD_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 14,066 chars in the whole document
