---
id: 02-business-partner-and-product-master-data/master-data-script-create-product-master-of-type-spare-parts-mds-2j7-2
title: "Master Data Script: Create Product Master of type Spare Parts - MDS (2J7) (2J7_S4CLD2608_Master_Data_EN_XX)"
description: "SAP master data script (2J7) for creating a Spare Parts (ERSA) material master across basic, purchasing, MRP, storage, accounting views, plus optional document linking."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/product-master-spare-parts]
aliases: [2J7_S4CLD2608_Master_Data_EN_XX]
keywords: ["Product Master: Spare Parts", spare parts material, material master data, basic data, purchasing data, mrp planning data, storage location data, accounting data, document info record, document linking]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2J7_S4CLD2608_Master_Data_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-263
topic: 02-business-partner-and-product-master-data/product-master-spare-parts
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Master Data Script: Create Product Master of type Spare Parts - MDS (2J7) (2J7_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2J7_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Product Master: Spare Parts** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Product Master of type "Spare Parts" - MDS (2J7) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233904533)

[2 Prerequisites 3](#_Toc233904534)

[2.1 Roles 3](#_Toc233904535)

[2.2 Required Organizational Units 3](#_Toc233904536)

[2.3 Mandatory and Optional Master Data 4](#_Toc233904537)

[2.4 Main Parameters for Data Creation 4](#_Toc233904538)

[2.4.1 Material Type and Number Ranges 5](#_Toc233904539)

[2.4.2 Industry Sector 5](#_Toc233904540)

[3 Overview Table 6](#_Toc233904541)

[4 Test Procedures 7](#_Toc233904542)

[4.1 Create Material Master Data - Basic Data 7](#_Toc233904543)

[4.2 Create Material Master Data - Purchasing Data 8](#_Toc233904544)

[4.3 Create Material Master Data - MRP/Planning Data (Plant Data) 10](#_Toc233904545)

[4.4 Create Material Master Data - Storage Location Data 12](#_Toc233904546)

[4.5 Create Material Master Data - Accounting Data (Valuation Area Data) 14](#_Toc233904547)

[4.6 Create Document (Optional) 15](#_Toc233904548)

[4.7 Change Material Master Data - Link Document to Material Master Data (Optional) 16](#_Toc233904549)

## Purpose

This building block creates a product master data record for Spare Parts.

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Products / Product Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |
| Design Engineer | SAP_BR_DESIGN_ENGINEER | Document Management | SAP_BR_DESIGN_ENGINEER |  |

### Required Organizational Units

Some segments of material master data are dependent on the organizational units of the company, General (Central) Data does not depend on an organizational unit or the company code. The following table gives an overview of these different data segments and their relevant organizational units:

| Data Segment | Depends On | Field Examples | Comments | Organizational Unit to be Used |
| --- | --- | --- | --- | --- |
| Basic Data | Independent from organizational units | Material description (short text), Material number, Material Group, Base Unit of Measure, and so on. | Basic Data exists only once for a material master data record. | n/a |
| Purchasing Data | Plant | Purchasing Group, Material Group, GR processing time, and so on. | Purchasing Data can exist for every purchasing organization for which the material shall be used in purchasing processes. | Plant:__________ |
| MRP/Planning Data | Plant, Storage Location | MRP Type, MRP Controller, Lot Size, Planned delivery time, and so on. | Plant data can exist for every Plant ID of your enterprise structure for which the material master record is used.Storage location data (planning context) is optional based on the need to do storage location specific planning | Plant:____________Storage Location:__________ |
| Storage Location Data | Plant, Storage Location | Number of GR slips, Max. Storage Period, Min. Rem. Shelf, and so on. |  | Plant:____________Storage Location:__________ |
| Accounting Data | Valuation area (=Plant), Valuation type | Valuation Class, Per Unit Price, Price Control, and so on. | Valuation area data can exist for every Plant ID of your enterprise structure for which the material master record is used. Every plant represents a valuation area (for example, different valuation price of a material in different plants) | Plant:____________Valuation type:__________ |

### Mandatory and Optional Master Data

Material master data records may refer to other master data. The following table gives an overview of optional and mandatory master data objects to be used in a material master data record.

|  |
| --- |
| Note Brazil specific fields are required to get a proper tax calculation.Check Nota Fiscal Brazil - JD0 in Define BR Specific Fields for Master Data chapter for material master data. |

| Master Data Object | Used in Data Segment | Mandatory / Optional | Comments |
| --- | --- | --- | --- |
|  |  | Optional |  |
|  |  | Mandatory |  |

### Main Parameters for Data Creation

In the following topics under this section, some basic parameters are described that influence the behavior of a master record and are always required to create a material master data record.

#### Material Type and Number Ranges

With the help of material types, the system determines which data segments (views) can be maintained or which fields are mandatory or optional. Based on material types, the system also determines the number ranges for materials. In the SAP standard content, all material types use the same number range definition

| Number Range | Range / Business Partner ID | Comments |
| --- | --- | --- |
| External alpha-numeric | A – ZZZZZZZZ | This range must start with a character. Overall the ID must not be longer than 8 digits. |
| Internal numeric | 1 – 99999999 | This range is used if the system shall automatically assign a numeric number to a material. |

#### Industry Sector

The standard content only provides one industry sector M.

|  |
| --- |
| Note Currently, this is only visible in SAP GUI. |

## Overview Table

This scope item consists of several process steps that are listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Material Master Data - Basic Data](#unique_10) [page ] 7 | Master Data Specialist - Product Data | Create Material (MM01) | Basic Material Master Data is created. |
| [Create Material Master Data - Purchasing Data](#unique_11) [page ] 8 | Master Data Specialist - Product Data | Create Material (MM01) | Purchasing Master Data is created. |
| [Create Material Master Data - MRP/Planning Data (Plant Data)](#unique_12) [page ] 10 | Master Data Specialist - Product Data | Create Material (MM01) | MRP Planning Master Data is created |
| [Create Material Master Data - Storage Location Data](#unique_13) [page ] 12 | Master Data Specialist - Product Data | Create Material (MM01) | Storage Location Master Data is created |
| [Create Material Master Data - Accounting Data (Valuation Area Data)](#unique_14) [page ] 14 | Master Data Specialist - Product Data | Create Material (MM01) | Accounting Master Data is created |
| [Create Document (Optional)](#unique_15) [page ] 15 | Design Engineer | Manage Documents (F2733) | A new Document Info Record is created and Meta data are added. Attachments are added to the Document. |
| [Change Material Master Data - Link Document to Material Master Data (Optional)](#unique_16) [page ] 16 | Master Data Specialist - Product Data | Change Material (MM02) | The Document created in previous step is linked to the Material Master Data. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Material Master Data - Basic Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating material master data.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The Start page is displayed.Note Logging on using the SAP Fiori launchpad is only relevant for Web GUI use. |  |
| 2 | Access the SAP Fiori app | Open Create Material (MM01). | A new screen opens, Create Material (Initial screen). |  |
| 3 | Enter Material Basic Data | On the Create Material (Initial screen), make the following entries:Material: <Material number>Industry sector: MNote If the Industry Sector input field is hidden, no entry is required. When the industry sector is not offered for entry, the field is populated with in the dark.Material type: for example, ERSA Spare Parts | A new screen opens, showing the Select View(s). |  |
| 4 | Choose Views | In the Select Views screen, select Basic data 1 and Basic data 2 and choose Continue. | A new screen opens, showing the Create Material (Spare Parts) view. |  |
| 5 | Enter Basic Data | In the Create Material … (Spare Parts) view, on the Basic data 1 tab, enter the Description (short text). |  |  |
| 6 | Enter Basic Data | On the Basic data 1 tab, in the General Data section, make the following entries:Base Unit of Measure: for example, PCMaterial Group: for example, YBPM01 |  |  |
| 7 | Save Your Data | Choose Save | Material number is created. |  |

### Create Material Master Data - Purchasing Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating material master data.

Prerequisite

You have completed and saved the basic data for the material as described in the previous section, Create Material Master Data - Basic Data.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The Start page is displayed.Note Logging on using the SAP Fiori launchpad is only relevant for Web GUI use. |  |
| 2 | Open Create Material Tile | In the Product Master section, choose Create Material (MM01). | A new screen opens, showing the Create Material (Initial Screen). |  |
| 3 | Enter Material Basic Data | On the Create Material (Initial screen), make the following entries:Material: Material number created in the previous step.Industry sector: MNote If the Industry Sector input field is hidden, no entry is required. When the industry sector is not offered for entry, the field is populated with in the dark.Material type: for example, ERSA Spare Parts | A new screen opens, showing the Select View(s) screen. |  |
| 4 | Choose Views | In the Select View(s) screen, select Purchasing and choose Continue.Note For Poland only: in order to enter PKWiU code select also International Trade: Import. | A new screen opens, showing the Organizational Levels. |  |
| 5 | Enter Organizational Levels Data | On the Organizational Levels screen, in the Organizational levels section, make the following entry :Plant: <Plant code>Choose Continue. | A new screen opens, showing the Create Material (Spare Parts) screen.Note The following system message displays at the bottom of the screen: The material already exists and will be extended. |  |
| 6 | Enter Purchasing Data | In the Create Material (Spare Parts) screen, on the Purchasing tab, in the General Data section, make the following entries:Purchasing Group: Purchasing Group number |  |  |
| 7 | Enter Purchasing Data | In the Other data/manufacturer data section, make the following entry:GR processing time: for example, 1 |  |  |
| For Poland Only | Enter Sales Data | In the International Trade: Import section, enter the following data:Control code: for example, 41.00.30.0Then choose Save. | PKWiU code for Poland is maintained. |  |
| 8 | Save Your Data | Choose Save. | Material number is created. |  |

### Create Material Master Data - MRP/Planning Data (Plant Data)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating material master data..

Prerequisite

You have completed the previous sections, Create Material Master Data - Basic Data and have saved the purchasing master data.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The Start page is displayed.Note Logging on using the SAP Fiori launchpad is only relevant for Web GUI use. |  |
| 2 | Access the SAP Fiori App | Open Create Material (MM01). | A new view opens, showing the Create Material (Initial Screen). |  |
| 3 | Enter Material Basic Data | On the Create Material (Initial view), make the following entries:Material: Material number created in previous stepIndustry sector: MNote If the Industry Sector input field is hidden, no entry is required. When the industry sector is not offered for entry, the field is populated with in the dark.Material type: for example, ERSA Spare Parts | A new view opens, showing the Select View(s) view. |  |
| 4 | Choose Views | In the Select View(s) view, select MRP1, MRP2, MRP3 and MRP4 and choose Continue. | A new view opens, showing the Organizational Levels. |  |
| 5 | Enter Organizational Levels Data | On the Organizational Levels view, in the Organizational level section, make the following entries:Plant: <Plant number>Storage Location: <storage location> | A new view opens, showing the Create Material (Spare Parts) view. |  |
| 6 | Enter MRP/Planning Data | On the Create Material (Spare Parts) view, on the MRP 1 tab, in the MRP procedure section, make the following entries:MRP Type: for example, PDMRP Controller: for example, 001 | You get the following system message at the bottom of the view: The material already exists and will be extended. |  |
| 7 | Enter MRP/Planning Data | In the Lot size data section, make the following entry:Lot Sizing Procedure: for example, EX | You are navigated to the next tab MRP 2. |  |
| 8 | Enter MRP/Planning Data | On the Create Material (Spare Parts) view, on the MRP 2 tab, in the Procurement section, make the following entries:Procurement type: for example, FProd. Stor. Location: <Location>Storage loc. For EP <Location> |  |  |
| 9 | Enter MRP/Planning Data | In the Scheduling section, make the following entries:Planned delivery time: For example, 3GR processing time: for example, 1SchedMargin key: for example, 000 | You are navigated to the next tab MRP 3. |  |
| 10 | Enter MRP/Planning Data | In the Create Material (Spare Parts) view, on the MRP 3 tab, in the Availability check section, make the following entries:Availability check: for example, SPTot. repl. Lead time: for example, 3 | You are navigated to the next tab MRP 4. |  |
| 11 | Enter MRP/Planning Data | In the Create Material (Spare Parts) view, on the MRP 4 tab, in the BOM explosion/dependent requirements section, make the following entries:Individual/coll.: 2 |  |  |
| 12 | Save Your Data | Choose Save | The Material number is created. |  |

### Create Material Master Data - Storage Location Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating material master data..

Prerequisite

You have filled out the data for the material as described in the previous Create Material Master Data - Basic Data procedure and have completed and saved the MRP/planning data.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The Start page is displayed.Note Logging on using the SAP Fiori launchpad is only relevant for Web GUI use. |  |
| 2 | Access the SAP Fiori App | Open Create Material (MM01). | A new view opens, showing the Create Material (Initial view). |  |
| 3 | Enter Material Basic Data | On the Create Material (Initial view), make the following entries:Material: Material number created in previous step.Industry sector: MNote If the Industry Sector input field is hidden, no entry is required. When the industry sector is not offered for entry, the field is populated with in the dark.Material type: for example, ERSA Spare Parts | A new view opens, showing the Select View(s) view. |  |
| 4 | Choose Views | In the Select View(s) view, select the following views and choose Continue:General Plant Data/Storage 1General Plant Data/Storage 2 | A new view opens, showing the Organizational Levels. |  |
| 5 | Enter Organizational Levels Data | On the Organizational Levels view, in the Organizational level section, make the following entries:Plant: <Plant code>Storage Location: <Storage Location number> | A new view opens, showing the Create Material (Spare Parts) view.Note A system message displays at the bottom of the view : The material already exists and will be extended. |  |
| 6 | Enter Storage Location Data | On the Create Material (Spare Parts) view, on the Plant data/stor. 1 tab, in the General Data section, make the following entries:Number of GR slips: for example, 1 | You are navigated to the next tab, Plant data/stor.2. |  |
| 7 | Confirm Entries | On the Plant data/stor. 2 tab, in the General plant parameters section, make the following entry:Profit Center. |  |  |
| 8 | Save Your Data | Choose Save. | Material number is created. |  |

### Create Material Master Data - Accounting Data (Valuation Area Data)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating material master data.

Prerequisite

You created the data for the material described in the previous procedure, Create Material Master Data - Basic Data and have completed and saved the storage location data.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The Start page is displayed.Note Logging on using the SAP Fiori launchpad is only relevant for Web GUI use. |  |
| 2 | Access the SAP Fiori App | Open Create Material (MM01). | Create Material (Initial Screen) displays. |  |
| 3 | Enter Material Basic Data | On the Create Material (Initial Screen), make the following entries:Material: <The material number you created in the previous step>Industry sector: MNote If the Industry Sector input field is hidden, no entry is required. When the industry sector is not offered for entry, the field is populated with in the dark.Material type: for example, ERSA Spare Parts | The Select View(s) view displays. |  |
| 4 | Choose Views | In Select View(s), select the following and choose Continue:Accounting 1Accounting 2 | The Organizational Levels view displays. |  |
| 5 | Enter Organizational Levels Data | On the Organizational Levels view, in the Organizational level section, make the following entries:Plant | The Create Material (Spare Parts) view displays.This system message appears: The material already exists and will be extended. |  |
| 6 | Enter Accounting Data | From the Create Material (Spare Parts) view, on the Accounting 1 tab, in the General Valuation Data section, make the following entry:Valuation Class: 3040 |  |  |
| 7 | Enter Accounting Data | In the Prices and values section, make the following entries:Standard Price for example, 100Price Unit: 1Prc. Ctrl: keep it as standard | The next tab, Accounting 2 opens. |  |
| 8 | Confirm Entries | On the Accounting 2 tab, you do not make any entries. |  |  |
| 9 | Save Your Data | Choose Save. | Material number is created. |  |

### Create Document (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using your user credentials Design Engineer. | The Start page is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Documents (F2733). | The Manage Documents (F2733) screen displays. |  |
| 3 | Create New Document | On the Manage Document view, choose Create to create a new document. | The Document view appears. |  |
| 4 | Enter Metadata | On the General Information tab of the Document view, make the following entries:Document Type: for example, YBODocument Part: for example, 000On the Document Data tab of the Document view, make the following entries:Description: for example, <SparePartsDoc001> | Metadata is maintained on the Document view with default values. |  |
| 5 | Upload Attachments to the Document | On the Document view, go to the Originals tab and choose Upload to browse and upload the appropriate documents:File Name: for example, <test001.jpg> | The document attachments appear checked in. |  |
| 6 | Save the Document | Choose Create to save the document. | A new document of type YBO is created and saved.Write down the Document Number. |  |
| 7 | Change Status | On the Document view, choose Edit and from the Document Data section, set Document Status to Re(Released) |  |  |
| 8 | Save the Document | Choose Save to save the document. |  |  |

### Change Material Master Data - Link Document to Material Master Data (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for linking a document to the material master data.

Prerequisite

You created the data for the material described in the previous procedure, Create Material Master Data - Basic Data and have completed the optional Create Document procedure.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Change Material (MM02). | A new window opens, showing the Change Material (Initial Screen). |  |
| 3 | Enter Material Basic Data | On the Change Material (Initial Screen), make the following entries:Material: <Material number created in previous step>Industry Sector: MNote If the Industry Sector input field is hidden, no entry is required. When the industry sector is not offered for entry, the field is populated with in the dark. |  |  |
| 4 | Choose Views | On the Change Material (Initial Screen), choose Select View(s) on the top bar. | A new view opens, showing the Select View(s) view. |  |
| 5 | Choose Views | In the Select View(s) window, select the following views and choose Continue:Basic Data 1 | A new window opens, showing the Change Material … (Spare Parts) screen. |  |
| 6 | Open Additional Data | On the Change Material … (Spare Parts) screen, choose Additional Data on the top bar. |  |  |
| 7 | Enter Document Data | Choose the Document data tab and from Linked Documents, choose All versions. Choose the plus sign (+) to insert a new row. Search for the document you created in the previous procedure. |  |  |
| 8 | Copy Document Data | Select the document created in the previous step and then choose Copy to insert the document to the row. |  |  |
| 9 | Save your Data | Choose Save. | Material number is changed. |  |

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
- related-to :: [[02-business-partner-and-product-master-data/mds-2j7-265]]
- related-to :: [[02-business-partner-and-product-master-data/mds-2j7-267]]
- related-to :: [[02-business-partner-and-product-master-data/script-de-dados-mestre-criar-mestre-de-produtos-do-tipo-pecas-de-repos]]
- related-to :: [[02-business-partner-and-product-master-data/script-de-datos-maestros-creacion-de-maestro-de-productos-de-tipo-piez]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2J7_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 28,590 chars in the whole document
