---
id: 02-business-partner-and-product-master-data/create-product-master-of-type-packaging-mds-3y1-389
title: "Create Product Master of Type \"Packaging\" - MDS (3Y1) (3Y1_S4CLD2608_Master_Data_EN_XX)"
description: "Master data script (3Y1) for SAP S/4HANA Cloud Public Edition: create packaging material/product master (basic, sales, WM views) for Warehouse Management scope items."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/product-master-packaging]
aliases: [3Y1_S4CLD2608_Master_Data_EN_XX]
keywords: ["Product Master: Packaging and Returnable Packaging", packaging material master, material master basic data, material master sales data, warehouse management data, material types, number ranges, business roles, master data scripts, industry sector]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3Y1_S4CLD2608_Master_Data_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-389
topic: 02-business-partner-and-product-master-data/product-master-packaging
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Create Product Master of Type "Packaging" - MDS (3Y1) (3Y1_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3Y1_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Product Master: Packaging and Returnable Packaging** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Product Master of Type "Packaging" - MDS (3Y1) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233904693)

[2 Prerequisites 3](#_Toc233904694)

[2.1 System Access 3](#_Toc233904695)

[2.2 Roles 3](#_Toc233904696)

[2.3 Required Organizational Units 3](#_Toc233904697)

[2.4 Mandatory and Optional Master Data 4](#_Toc233904698)

[2.5 Main Parameters for Data Creation 4](#_Toc233904699)

[2.5.1 Material Type and Number Ranges 4](#_Toc233904700)

[2.5.2 Industry Sector 5](#_Toc233904701)

[3 Overview Table 6](#_Toc233904702)

[4 Procedures 7](#_Toc233904703)

[4.1 Create Material Master Data - Basic View 7](#_Toc233904704)

[4.2 Create Material Master Data - Sales View 9](#_Toc233904705)

[4.3 Update Material Master Data - WM View 11](#_Toc233904706)

[5 Appendix 14](#_Toc233904707)

## Purpose

This master data script provides procedures to create packaging material/product master used by the Warehouse Management scope items.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

### System Access

| System | Details |
| --- | --- |
| System | Accessible via SAP Fiori Launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) |
| --- | --- | --- | --- |
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Products / Product Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |

### Required Organizational Units

Some segments of master data are dependent on the organizational units of the company, General (Central) Data does not depend on an organizational unit or the company code. The following table gives an overview of these different data segments and their relevant organizational units:

| Data Segment | Depends On | Field Examples | Comments | Organizational Unit to be Used |
| --- | --- | --- | --- | --- |
| Basic Data | Independent from organizational units | Base Unit of MeasureMaterial Group and so on. |  | n/a |
| Sales Data | Independent from organizational units | Transp. Group, Packaging Mat. Type,Allowed pkg weight,Allowed pkg volume, and so on. |  | n/a |
| WM Data | Independent from organizational units | Handling Unit TypeStandard HU Type |  | n/a |

### Mandatory and Optional Master Data

Master data records may refer to other master data. The following table gives an overview of optional and mandatory master data objects to be used in a Packagingmaster data record.

| Master Data Object | Used in Data Segment | Mandatory / Optional | Comments |
| --- | --- | --- | --- |
| Base Unit of Measure | Basic Data | Mandatory |  |

|  |
| --- |
| Note Brazil-specific fields are required to get a proper tax calculation. Check the Define BR Specific Fields for Master Data chapter for Material Master Data chapter in the Create Master Data for Brazil (JD0_BR) document. |

### Main Parameters for Data Creation

In this section, we describe some basic parameters that influence the behavior of a master record and are always required to create a packaging master data record:

#### Material Type and Number Ranges

With the help of material types, the system determines which data segments (views) can be maintained or which fields are mandatory or optional. Based on material types, the system also determines the number ranges for materials. In the SAP standard content, all material types use the same number range definition.

| Number Range | Range / Business Partner ID | Comments |
| --- | --- | --- |
| External alpha-numeric | A - ZZZZZZZZ | This range must start with a character. Overall the ID must not be longer than 40 characters. |
| Internal numeric | 1–99999999 | This range is used if the system shall automatically assign a numeric number to a material. |

#### Industry Sector

The standard content only provides one industry sector M.

## Overview Table

This master record consists of several segments provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction / App | Expected Results |
| --- | --- | --- | --- |
| Create Material Master Data - Basic View | Master Data Specialist - Product Data | Create Material (MM01)/ Manage Product Master Data (F1602) | Material Master Data - Basic Data is created. |
| Create Material Master Data - Sales View | Master Data Specialist - Product Data | Create Material (MM01)/ Manage Product Master Data (F1602) | Material Master Data - Sales Data is created. |
| Update Material Master Data - WM View | Master Data Specialist - Product Data | Change Material (MM02)/ Manage Product Master Data (F1602) | Material Master Data - WM Data is created. |

## Procedures

This section describes procedures for each segment or process step that is part of this master record.

### Create Material Master Data - Basic View

Purpose

The following procedure provides instructions for creating material master data. Apps available to you are dependent upon your assigned role, so two options are provided.

Procedure: Option 1 - Create Material

Use the following procedure when your user access presents you with the Create Material app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad appears. |  |
| 2 | Access the SAP Fiori App | Open Create Material (MM01). | The Create Material (Initial Screen) appears. |  |
| 3 | Enter Material Basic Data | On the Create Material (Initial screen), make the following entries:Material: <Material number>Material type: Packaging | The Select View(s) screen appears. |  |
| 4 | Choose Select View(s) | Choose Select View(s). | The Select View(s) dialog box appears. |  |
| 5 | Choose Views | In Select View(s) dialog box, select the Basic Data 1 checkbox and the Basic Data 2 checkbox. Choose Continue (Enter). | The Create Material <your material number> (Packaging), screen appears |  |
| 6 | Enter Basic Data | On the Create Material > your material number > (Packaging) screen, make the following entries:Descr.: <your material description> |  |  |
| 7 | Enter Basic Data | On the Basic data 1 tab in the General Data section, make the following entries:Base Unit of Measure: <UoM>for example, PCGenItemCatGroup: VERP |  |  |
| 7 | Enter Basic Data | In the Dimensions/EANs section, make the following entries:Gross Weight: for example, 20Unit of Weight: for example, KGNet Weight: for example, 15Volume: for example, 138Volume Unit: for example, CD3Choose Enter. | Once the entry is completed, move to the next tab, Basic Data 2. |  |
| 8 | Complete Basic Data | No entries are required for the Basic Data 2 view. |  |  |
| 9 | Save Your Data | Choose Save. | The basic data is created and saved. |  |

Procedure: Option 2 - Manage Product Master Data

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad appears. |  |
| 2 | Access the SAP Fiori App | Open Manage Product Master Data (F1602). | The Manage Product Master Data (F1602) screen displays. |  |
| 3 | Choose Create New Product Master | On the Manage Product Master Data (F1602) screen, choose Create and choose Product. | The Create Master Data Record screen is displayed. |  |
| 4 | Enter Data for Mandatory Fields | On the Create Master Data Record screen, make the following entries:Product Number: for example, Z …You either enter any external alphanumeric ID, and that ID must start with an alphanumeric character. If you provide no entry, the system automatically assigns a numeric ID.For more information about the product number, see the previous Material Type and Number Ranges section.Product Type: VERPBase Unit: for example, PCDescription: <any description>Choose OK. |  |  |
| 5 | Enter Basic Data | On the General Information tab page, make the following entry:In Basic Data section:Division: for example, 00Choose Show More and make the following entry:General Item Category Group: VERP |  |  |
| 6 | Enter Descriptions Data | In the Descriptions section, choose Create and make the following entries:Language: for example, DEProduct Description: <your description> |  |  |
| 7 | Choose Base Unit of Measure | In the Base Units of Measure section, choose Show More to enter the additional data. |  |  |
| 8 | Enter other Measure Data | In the Weight section, make the following entries:Gross Weight: for example, 20 KGNet Weight: for example, 15 KGIn the Volume section, make the following entry:Volume: for example,138 CD3 |  |  |
| 9 | Save Your Data | Choose Create. | A system message displays that the object is saved. |  |

### Create Material Master Data - Sales View

Purpose

The following procedure provides instructions for creating material master data. Apps available to you are dependent upon your assigned role, so two options are provided.

Prerequisite

You must complete the previous section, Creating Material Master Data - Basic Data, before you proceed with this section.

Begin the procedure after you have saved the Basic Data entries, as described in the previous procedure.

|  |
| --- |
| Note Due to performance restriction in App Manage Product Master Data, not all the fields can be seen and edited. If you find any field missing, choose option 1 to create material or you can add these fields in App Manage Product Master Data via the guideline in Adapting SAP Fiori UIs at Runtime - Key User Adaptation \| SAP Help Portal |

Procedure: Option 1 - Create Material

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Choose Create Material (MM01). | Create Material (Initial view) displays. |  |
| 2 | Enter Material Basic Data | On the Create Material (Initial view) screen make the following entries:Material: <Material number> Industry sector: MNote If the Industry Sector input field is hidden, no entry is required. When the industry sector is not offered for entry, the field is populated with in the dark.Material type: PackagingChoose Select View(s). | After completing the entries, a new screen opens, Select View(s). |  |
| 3 | Choose Views | On the Select View(s) screen, select Sales: General/Plant Data and choose Continue.Note For Poland only: Select also Foreign Trade - Export Data in order to enter the PKWiU classification number. | A screen with Organizational Levels displays. |  |
| 4 | Choose Continue | On the Organizational Levels screen, in the Organizational level section, do not enter data for plant, sales organization and distribution channelChoose Continue.The following information appears at the bottom of the view: The material already exists and will be extended.pFor Poland only: If you have selected Foreign Trade - Export Data, select Plant. |  |  |
| 5 | Enter Sales Data | On the Sales: General/Plant tab, in the Shipping data (times in days) section, make the following entry:Transp. Grp: 0001 |  |  |
| 6 | Enter Packaging material data | In the Packaging material data section, make the following entries:Packaging Mat. TypeAllowed pkg weightExcess wt toleranceAllowed pkg volumeExcess volume tol.Closed |  |  |
| 7 | For Poland only Enter Sales Data | In the International Trade: Export section, enter the following data:• Control code: for example, 26.40.20.0 | The PKWiU code for Poland is maintained. |  |
| 8 | Save your data | Choose Save. | Your data is saved. |  |

Procedure: Option 2 - Manage Product Master Data

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Manage Product Master Data (F1602). | The Manage Product Master Data (F1602) app opens and various search fields are displayed. |  |
| 2 | Search and open the Product for edit | Search the previously created Product by entering the Product Number in the Product search field.Select the Product from the list that guides you to the Product view.Choose Edit. | The product is displayed in edit mode (fields are ready for your input). |  |
| 3 | Choose Sales | On the Product screen, choose Sales .make following entries:Transportation Group: 0001Allowed Packing Weight:Allowed Packing Volume: |  |  |
| 4 | Save Your Data | Choose Save. | A system message appears that the object is saved. |  |

### Update Material Master Data - WM View

Purpose

The following procedure provides instructions for creating material master data. Apps available to you are dependent upon your assigned role, so two options are provided.

Prerequisite

You must complete the previous procedure, Creating Material (Product) Master Data - Basic Data, before you proceed with this section.

Begin the procedure after you have saved the basic data entries, as described in the previous procedure.

Procedure: Option 1 - Create Material

Use the following procedure when your user access presents you with the Change Material (MM02) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Change Material (MM02). | Create Material (Initial Screen) opens. |  |
| 2 | Enter Material Basic Data | On the Change Material(Initial Screen) screen, make the following entries:Material: <Material number>Click on Select View(s). | Select View(s) opens. |  |
| 3 | Choose Views | On the Select View(s) screen, select the following views:WM ExecutionWM PackagingChoose Continue. |  |  |
| 4 | Enter WM Execution Data | On the WM Execution tab, make the following entries:Standard HU Type: for example, SP1 |  |  |
| 5 | Enter WM Packaging Data | On the WM Packaging tab, make the following entries:Handling Unit Type: for example, SP1 |  |  |
| 6 | Save Your Data | Choose Save. |  |  |

Procedure: Option 2 - Manage Product Master Data

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Manage Product Master Data (F1602). | The Manage Product Master Data (F1602) app opens and various search fields are displayed. |  |
| 2 | Search and Open the Product for Edit | Search the previously created Product by entering the Product Number in the Product search field.Select the Product from the list that guides you to the Product view.Choose Edit. | The product is displayed in edit mode (fields are ready for your input). |  |
| 3 | Choose Execution | In the Product view, choose the Warehouse Management tab. |  |  |
| 4 | Enter Execution Data | In the Execution section, make the following entries:Standard Handling Unit Type: for example, SP1 |  |  |
| 5 | Enter Packaging Data | In the Packaging section, make following entries:Handling Unit Type: for example, SP1 |  |  |
| 6 | Save Your Data | Choose Save. | The system message indicates that the object is saved. |  |

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

## Connections
- part-of :: [[_cluster]]
- related-to :: [[02-business-partner-and-product-master-data/criar-mestre-de-produtos-do-tipo-embalagem-mds-3y1-392]]
- related-to :: [[02-business-partner-and-product-master-data/mds-3y1-391]]
- related-to :: [[02-business-partner-and-product-master-data/mds-3y1-393]]
- related-to :: [[02-business-partner-and-product-master-data/script-de-datos-maestros-creacion-de-maestro-de-productos-de-tipo-emba]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3Y1_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 19,547 chars in the whole document
