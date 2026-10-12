---
id: 13-quality-ehs-and-compliance/create-ehs-location-mds-3sr-359
title: Create EHS Location - MDS (3SR) (3SR_S4CLD2608_Master_Data_EN_XX)
description: SAP S/4HANA Cloud Public Edition master data script for creating an EHS Location and assigning it to the location structure in Manage Locations.
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/ehs-locations]
aliases: [3SR_S4CLD2608_Master_Data_EN_XX]
keywords: [EHS Locations, ehs location, location structure, master data scripts, business roles, fiori launchpad access, location activation, 3SR]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3SR_S4CLD2608_Master_Data_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-359
topic: 13-quality-ehs-and-compliance/ehs-locations
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Create EHS Location - MDS (3SR) (3SR_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3SR_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **EHS Locations** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create EHS Location - MDS (3SR) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233904637)

[2 Prerequisites 3](#_Toc233904638)

[2.1 System Access 3](#_Toc233904639)

[2.2 Roles 3](#_Toc233904640)

[3 Overview Table 4](#_Toc233904641)

[4 Procedures 5](#_Toc233904642)

[4.1 Create EHS Location Master Data - General Data 5](#_Toc233904643)

## Purpose

This document helps you to create an EHS Location within the location structure. The EHS Location is a central master data object that is used in Environment, Health, and Safety. The creation of EHS Locations organized into a location structure is part of the initial setup of the solution and locations are used in further processes that are part of the solution.

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
| Industrial Hygienist (Incident Manager) | SAP_BR_INDUSTRIAL_HYGIENIST | Workplace Safety | SAP_BR_INDUSTRIAL_HYGIENIST |  |
| Environmental Manager | SAP_BR_EHS_ENV_MGMT | Environment Management | SAP_BR_EHS_ENV_MGMT |  |
| Change Management Coordinator | SAP_BR_CHG_MGMT_COORDINATOR | Management of Change | SAP_BR_CHG_MGMT_COORDINATOR |  |

## Overview Table

This master record consists of several segments provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Segment | Business Role | Transaction / App | Expected Results |
| --- | --- | --- | --- |
| [Create EHS Location Master Data - General Data](#unique_6) [page ] 5 | Industrial HygienistEnvironmental ManagerChange Management Coordinator | Manage Locations (EHFND_UI_LOC_ENTRY) | An EHS Location is created and assigned to the EHS Location structure. |

## Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create EHS Location Master Data - General Data

Purpose

The following procedure provides instructions for creating an EHS Location and assigning it to the EHS Location structure.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with one of the following roles:Industrial HygienistEnvironmental ManagerChange Management Coordinator | The SAP Fiori launchpad is displayed with the sections and tiles for the respective role. |  |
| 2 | Navigate to Location Structure | Open Manage Locations (EHFND_UI_LOC_ENTRY). | The Locations screen is displayed. The location structure initially has All Locations set as top level. |  |
| 3 | Create a Location | Choose Edit Location Structure.On the Location Structure screen:Select the All Locations row.Choose New.On the Create Location screen:Enter a <Location name> in the Location field.Select a <Location type> via the value help for the Location Type field.Enter date 01.01.2000 in the Revision Start Date field.Choose Save.Choose Return to Location Structure.On the Location Structure screen:Save your entries. | A location with the name <Location name> is created and saved in the location structure. |  |
| 4 | Edit a Location | On the Location Structure screen:In the Name column, choose the <Location name> link. | The Edit Location app is displayed. |  |
| 5 | Add Basic Information | On the Location: <Location name> screen, under the Basic Information tab:Add a <location description> text in the Description field.Choose Translations next to the Location field. Add translated text for different languages.Choose Translations next to the Description field. Add translated text for different languages.Choose Upload Image to add a picture for the location.Save your entries. | The data of the location is saved. |  |
| 6 | Add Address | On the Location: <Location name> screen, under the Address tab:Enter <Name line 1> in the Name Line 1 field.Enter <Name line 2> in the Name Line 2 field.Enter <Street name> in the Street field.Enter <Postal code> in the Postal Code field.Enter <City name> in the City field.Select <Country/Region> in the Country/Region field via the value help.Select <Region> in the Region field via the value help.Leave the default UTC value in the Time Zone field.Enter additional data in the Phone Number, Fax Number, Latitude, Longitude, and Elevation fields.Save your entries. | The data of the location is saved. |  |
| 7 | Add Person Responsible | This step is only relevant for the following roles:SAP_BR_INDUSTRIAL_HYGIENIST (Industrial Hygienist)SAP_BR_EHS_ENV_MGMT (Environmental Manager)On the Location: <Location name> screen, under the Persons Responsible tab:In the Persons Responsible by Roles table, select your <user name> in the Name column via the value help.In the Role column, select Incident Manager or Environmental Manager from the dropdown list.Save your entries. | The data of the location is saved. |  |
| 8 | Add Documents | On the Location: <Location name> screen, under the Documents tab:In the Documents and Links table, choose Add File to add a document for the location.Save your entries. | The selected document is added to the table.The data of the location is saved. |  |
|  | Activate Location | On the Location: <Location name> screen:Choose Set Status in the page header.Select the Active option. | The location is activated.The Status field is set to Active in the page header.The data of the location is saved. |  |

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
- related-to :: [[13-quality-ehs-and-compliance/ehs-lokation-anlegen-sds-3sr-358]]
- related-to :: [[13-quality-ehs-and-compliance/ehs-mds-3sr-361]]
- related-to :: [[13-quality-ehs-and-compliance/ehs-mds-3sr-363]]
- related-to :: [[13-quality-ehs-and-compliance/script-de-dados-mestre-criar-local-ehs-mds-3sr-362]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3SR_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 9,613 chars in the whole document
