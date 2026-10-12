---
id: 11-inventory-warehouse-and-transportation/master-data-script-create-warehouse-master-data-for-resource-mds-3y2-3
title: "Master Data Script: Create Warehouse Master Data for Resource – MDS (3Y2) (3Y2_S4CLD2608_Master_Data_EN_XX)"
description: SAP S/4HANA Cloud 2608 master data script (3Y2) for creating and deleting warehouse resources in the Warehouse Monitor (/SCWM/MON) as Warehouse Clerk (EWM).
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/ewm-warehouse-resources]
aliases: [3Y2_S4CLD2608_Master_Data_EN_XX]
keywords: [EWM Warehouse Resources, warehouse resources, warehouse monitor, resource deletion, warehouse management, business roles, required organizational units, master data scripts, 3Y2]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3Y2_S4CLD2608_Master_Data_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-395
topic: 11-inventory-warehouse-and-transportation/ewm-warehouse-resources
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Master Data Script: Create Warehouse Master Data for Resource – MDS (3Y2) (3Y2_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3Y2_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **EWM Warehouse Resources** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Warehouse Master Data for Resource – MDS (3Y2) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233904680)

[2 Prerequisites 3](#_Toc233904681)

[2.1 System Access 3](#_Toc233904682)

[2.2 Roles 3](#_Toc233904683)

[2.3 Required Organizational Units 3](#_Toc233904684)

[2.4 Mandatory and Optional Master Data 3](#_Toc233904685)

[3 Overview Table 5](#_Toc233904686)

[4 Test Procedures 6](#_Toc233904687)

[4.1 Create Warehouse Resource 6](#_Toc233904688)

[4.2 Delete Warehouse Resource 7](#_Toc233904689)

## Purpose

In this document, you can learn how to create master data for warehouse resources. You can maintain the warehouse resources with the Warehouse Monitor (/SCWM/MON) app. This document includes those data segments, that are relevant for the master data to work in a regular system environment. You mainly learn which data segments and fields usually need to be filled with input values. Fields that are not relevant for the scope of the SAP S/4HANA content delivery by SAP Best Practices are not described in this document, even though they may appear on the screen. You use this master data for all Warehouse Management business processes.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

### System Access

| System | Details |
| --- | --- |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) |
| --- | --- | --- | --- |
| Warehouse Clerk (EWM) | SAP_BR_WAREHOUSE_CLERK_EWM | Warehouse Office | SAP_BR_WAREHOUSE_CLERK_EWM |

### Required Organizational Units

Some segments of master data are dependent on the organizational units of the company. General (Central) Data does not depend on an organizational unit or the company code. The following table gives an overview of these different data segments and their relevant organizational units:

| Data Segment | Depends On | Field Examples | Comments | Organizational Unit to be Used |
| --- | --- | --- | --- | --- |
| All | Warehouse Number |  |  |  |

### Mandatory and Optional Master Data

Master data records may refer to other master data. The following table gives an overview of optional and mandatory master data objects to be used in a <type> master data record.

| Master Data Object | Used in Data Segment | Mandatory / Optional | Comments |
| --- | --- | --- | --- |
|  |  |  |  |

## Overview Table

This master record consists of several segments provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Segment | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Create Warehouse Resource | Warehouse Clerk (EWM) | Warehouse Monitor (/SCWM/MON) | Creation of resource in the warehouse is carried out. |
| Delete Warehouse Resource | Warehouse Clerk (EWM) | Warehouse Monitor (/SCWM/MON) | Deletion of resource in the warehouse is carried out. |

## Test Procedures

This section describes procedures for each segment or process step that is part of this master record.

### Create Warehouse Resource

Purpose

In this section, you create Warehouse Resource using the Warehouse Monitor (/SCWM/MON) app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as the Warehouse Clerk (EWM). |  |  |
| 2 | Access App | Open Warehouse Monitor (/SCWM/MON). | The Warehouse Management Monitor dialog box is displayed. |  |
| 3 | Enter Warehouse Number | If the Warehouse Management Monitor dialog box opens, enter the following data:Warehouse Number: <Your Warehouse Number>Choose Execute. |  |  |
| 4 | Choose Menu | In the hierarchy in the left screen area, choose Resource Management > Resource. |  |  |
| 5 | Display Resource | In the opening dialog box, choose Execute. | The system displays all the resources that have been created for the warehouse. |  |
| 6 | Create Resource | Choose More Methods > Create Resource. |  |  |
| 7 | Enter Values | In the opening dialog box, enter the following data:Resource: <Resource ID>Note The resource ID is limited to 18 characters.Choose Execute. | A resource has been created successfully. |  |

### Delete Warehouse Resource

Purpose

In this section, you delete Warehouse Resource using the Warehouse Monitor (/SCWM/MON) app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as the Warehouse Clerk (EWM). |  |  |
| 2 | Access App | Open Warehouse Monitor (/SCWM/MON). | The Warehouse Management Monitor dialog box is displayed. |  |
| 3 | Enter Warehouse Number | In the openingWarehouse Management Monitor dialog box, enter the following data:Warehouse Number: <Your Warehouse Number>Choose Execute. |  |  |
| 4 | Choose Menu | In the hierarchy in the left screen area, choose Resource Management > Resource . |  |  |
| 5 | Display Resource | In the dialog box, choose Execute. | The system displays all the resources that have been created for the warehouse. |  |
| 6 | Delete Resource | Select the resource to be deleted, then choose More Methods > Delete Resource. |  |  |
| 7 | Confirm Deletion | In the Delete Resource dialog box, choose Yes.Note You cannot delete a particular resource that is still used in the warehouse. This means, when a user is logged on to the resource or if a user has set the resource as default resource. | A resource was deleted successfully. |  |

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
- related-to :: [[11-inventory-warehouse-and-transportation/crear-datos-maestros-de-almacen-para-recurso-mds-3y2-396]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-3y2-397]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-3y2-399]]
- related-to :: [[11-inventory-warehouse-and-transportation/script-de-dados-mestre-criar-dados-mestre-de-deposito-para-recurso-mds]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3Y2_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 10,036 chars in the whole document
