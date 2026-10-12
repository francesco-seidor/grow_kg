---
id: 12-production-and-manufacturing/create-production-supply-area-mds-40d-401
title: Create Production Supply Area - MDS (40D) (40D_S4CLD2608_Master_Data_EN_XX)
description: "English master data script 40D: create a production supply area via PK05S or Manage Production Supply Areas (F6935) as Production Planner - Lean Manufacturing,"
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/production-supply-areas]
aliases: [40D_S4CLD2608_Master_Data_EN_XX]
keywords: [Production Supply Areas, production supply area, lean manufacturing, mrp controller, plant and storage location, business roles, test procedures, 40D]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/40D_S4CLD2608_Master_Data_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-401
topic: 12-production-and-manufacturing/production-supply-areas
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Create Production Supply Area - MDS (40D) (40D_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/40D_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Production Supply Areas** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Production Supply Area - MDS (40D) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233904743)

[2 Prerequisites 3](#_Toc233904744)

[2.1 System Access 3](#_Toc233904745)

[2.2 Roles 3](#_Toc233904746)

[2.3 Required Organizational Units 3](#_Toc233904747)

[2.4 Mandatory and Optional Parameters for Data Creation 4](#_Toc233904748)

[3 Overview Table 5](#_Toc233904749)

[4 Test Procedures 6](#_Toc233904750)

[4.1 Create Production Supply Area 6](#_Toc233904751)

## Purpose

In this document you find a description of how to create a production supply area for your SAP S/4HANA Cloud Public Edition system. The description includes those data segments that are relevant for the SAP S/4HANA Cloud Public Edition appliance. Fields that are not relevant for the scope of the SAP S/4HANA Cloud Public Edition content are not described in this document.

A production supply area that is created as described here can be used for production processes.

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
| Production Planner - Lean Manufacturing | SAP_BR_PRODN_PLNR_LEAN_MFG | Production Planning - Lean Manufacturing | SAP_BR_PRODN_PLNR_LEAN_MFG |  |

### Required Organizational Units

| Data Segment | Depends On | Field Examples | Comments | Organizational Unit to be Used |
| --- | --- | --- | --- | --- |
| All data | Plant |  | All the data for production supply area depends on plant. | Plant:__________ |
| All data | Storage Location |  | All the data for production supply area depends on storage location. | Storage Location:__________ |

### Mandatory and Optional Parameters for Data Creation

Production supply area records may refer to other input parameters. The following table gives an overview of optional and mandatory enter parameters to be used for creating a Production Supply Area.

| Data Object | Mandatory / Optional | Comments |
| --- | --- | --- |
| Responsible / MRP controller | Optional | Person responsible for one or more supply areas |

## Overview Table

This scope item consists of the process step listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Production Supply Area](#unique_8) [page ] 6 | Production Planner - Lean Manufacturing | Production Supply Area - Fast Entry (PK05S) or Manage Production Supply Areas (F6935) | Production Supply Area is created. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Production Supply Area

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

Option 1:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner - Lean Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Production Supply Area - Fast Entry (PK05S). | The Edit Table Views: Initial Screen displays. |  |
| 3 | Enter Plant Code | On the Determine Work Area: Entry subscreen, enter the Plant code and choose Continue. |  |  |
| 4 | Navigate to Create Supply Area Screen | Choose New Entries. |  |  |
| 5 | Supply Area | Enter Supply Area details and press Enter.Supply Area: <Supply Area>SLoc: <Storage Location>Res: <A MRP Controller>Unloading Point: <"Unloading point A">Production Supply Area Name: <Description of the Production Supply Area> |  |  |
| 6 | Save Your Data | Choose Save. |  |  |
| 7 | Maintain Other Parameters (Optional) | You can enter other necessary parameters according to specific requirement. For example:Maintain the Production Supply Area address via More > Goto > Address.Save the changes. |  |  |

Option 2:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner - Lean Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Production Supply Areas (F6935). | The app opens. |  |
| 3 | Create | In the Production Supply Areas section, choose Create. |  |  |
| 4 | Enter Data | In the dialog box, make the following entries and choose Continue:Production Supply Area: <Supply Area>Plant: <Plant>Storage Location: <Storage Location> |  |  |
| 5 | Enter Basic Data | In the Basic Data section, make the following entries:Person Responsible: <An MRP Controller>Unloading Point: <"Unloading point A"> |  |  |
| 6 | Enter Description | In the Language-Dependent Description section, make the following entries:Language: <Choose a language code, for example, EN for English>Description: <Description of the Production Supply Area> |  |  |
| 7 | Save Your Data | Choose Create. |  |  |
| 8 | Maintain Other Parameters (Optional) | You can enter other necessary parameters according to specific requirement. For example:Maintain the Production Supply Area address via Create Address.Save the changes. |  |  |

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
- related-to :: [[12-production-and-manufacturing/creacion-de-area-de-suministro-de-produccion-mds-40d-402]]
- related-to :: [[12-production-and-manufacturing/criar-area-de-abastecimento-da-producao-mds-40d-404]]
- related-to :: [[12-production-and-manufacturing/mds-40d-403]]
- related-to :: [[12-production-and-manufacturing/mds-40d-405]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/40D_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 9,645 chars in the whole document
