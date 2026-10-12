---
id: 14-maintenance-service-and-projects/master-data-script-create-material-and-equipment-bom-for-service-mds-6
title: "Master Data Script: Create Material and Equipment BOM for Service - MDS (63J) (63J_S4CLD2608_Master_Data_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition 2608 master data script: create service products, a material BOM and an equipment with equipment BOM for service (scope item 63J)."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/service-technical-objects-and-boms]
aliases: [63J_S4CLD2608_Master_Data_EN_XX]
keywords: [Technical Objects and BOMs for Service, service products, material bom, equipment bom, equipment master data, business roles, organizational units, master data prerequisites, service contracts, sap fiori apps]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/63J_S4CLD2608_Master_Data_EN_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-491
topic: 14-maintenance-service-and-projects/service-technical-objects-and-boms
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Master Data Script: Create Material and Equipment BOM for Service - MDS (63J) (63J_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/63J_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Technical Objects and BOMs for Service** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Material and Equipment BOM for Service - MDS (63J) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233904847)

[2 Prerequisites 3](#_Toc233904848)

[2.1 System Access 3](#_Toc233904849)

[2.2 Roles 3](#_Toc233904850)

[2.3 Required Organizational Units 3](#_Toc233904851)

[2.4 Mandatory and Operational Master Data 4](#_Toc233904852)

[3 Overview Table 5](#_Toc233904853)

[4 Procedures 6](#_Toc233904854)

[4.1 Create Material BOM 6](#_Toc233904855)

[4.1.1 Create Service Products 6](#_Toc233904856)

[4.1.1.1 Create Service Product - SRV_BOM_01_01 6](#_Toc233904857)

[4.1.1.2 Create Service Product - SRV_BOM_02_01 7](#_Toc233904858)

[4.1.1.3 Create Service Product - SRV_BOM_02_02 9](#_Toc233904859)

[4.1.2 Create New Bill of Materials 10](#_Toc233904860)

[4.2 Create Equipment BOM 12](#_Toc233904861)

[4.2.1 Create Equipment 12](#_Toc233904862)

[4.2.2 Create Equipment BOM 14](#_Toc233904863)

## Purpose

In this document you find a description of how to create service productmaster data records and creating the bill of materials with the service products created The description includes those data segments that are relevant for the master data to work in a "usual" system environment. The reader mainly learns which data segments and fields usually need to be filled with input values. Fields that are not relevant for the scope are not described in this document although they may appear on the UI.

Service product master record that is created as described here can be used for Service Contracts.

| Product Type | Service product ID | Description |
| --- | --- | --- |
| Material Master | SRV_BOM_01_01 | Service product with BOM 01_01 |
|  | SRV_BOM_02_01 | Service product with BOM 02_01 |
|  | SRV_BOM_02_02 | Service product with BOM 02_02 |
| Material BOM | SRV_BOM_01_01 | Service product with BOM 01_01 |
| Equipment | <Equipment ID> | Create Equipment |
| Equipment BOM | <Equipment BOM> | Equipment BOM |

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
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Product | SAP_CMD_SP_PR_MAINT |
| BOM Engineer | SAP_BR_BOM_ENGINEER | Bills Of Material | SAP_BR_BOM_ENGINEER |
| Maintenance Planner | SAP_BR_MAINTENANCE_PLANNER | Maintenance Planning | SAP_BR_MAINTENANCE_PLANNER |

### Required Organizational Units

Some segments of master data are dependent on the organizational units of the company, General (Central) Data does not depend on an organizational unit or the company code. The following table gives an overview of these different data segments and their relevant organizational units:

| Data Segment | Depends On | Organizational Unit to be Used for US | Organizational Unit to be Used for DE |
| --- | --- | --- | --- |
| Create Material | Sales Organization | 1710 (Dom. Sales Org US) | 1010 (Dom. Sales Org DE) |
| Create Material | Distribution Channel | 10 (Direct Sales) | 10 (Direct Sales) |

### Mandatory and Operational Master Data

Material master data records may refer to other master data. The following table gives an overview of optional and mandatory master data objects to be used in a material master data record.

|  |
| --- |
| Note Brazil specific fields are required to get a proper tax calculation.Check Nota Fiscal Brazil - JD0 in Define BR Specific Fields for Master Data chapter for material master data. |

| Master Data Object | Used in Data Segment | Mandatory / Optional | Comments |
| --- | --- | --- | --- |
| Profit Center |  | Mandatory | Assigning a Profit Center to a material (product) master is required for correct valuation processes. |

## Overview Table

This master record consists of several segments provided in the table below.

If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.

You can find all other apps not included on the homepage using the search bar.

If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose Settings > App Finder .

| ID (Role Template) | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Create Material BOM | SAP_BR_PRODMASTER_SPECIALIST | Create Material (MM01) | Service products are created. |
| SAP_BR_BOM_ENGINEER | Maintain Bill Of Material - Create, change & display BOMs | Material BOM is created |  |
| Create Equipment BOM | SAP_BR_MAINTENANCE_PLANNER | Create Technical Object | Equipment is created |
| Create Equipment BOM | Equipment BOM is created |  |  |

## Procedures

This section describes procedures for each segment or process step that is part of this master record.

### Create Material BOM

#### Create Service Products

##### Create Service Product - SRV_BOM_01_01

Purpose

This material is relevant for cloud edition only.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Product Data (MDG). | The Home page appears. |  |
| 2 | Access the SAP Fiori app | Choose the Create Material tile. | The Create Material (Initial Screen) is displayed. |  |
| 3 | Maintain Material Basic Data (for Service Product ) | On the Create Material (Initial Screen) make the following entries: dialog window, select theMaterial: SRV_BOM_01_01Material Type: Service ProductThen choose Continue (Enter). | You have maintained basic information for the new service product.The Select View(s) dialog window is displayed. |  |
| 4 | Choose Views | On the Select View(s) dialog window, select the following views:Basic Data 1Sales: Sales Org. Data 1Sales: Sales Org. Data 2Then choose Continue (Enter). | The Organizational Levels dialog window is displayed. |  |
| 5 | Choose Organizational Levels | On the Organizational Levels window, maintain the following values:Sales Org.: 1710 (Dom. Sales Org US)Distr. Channel: 10 (Direct Sales)Then choose Continue (Enter). | Organizational data has been selected.The Create Material SRV_BOM_01_01 view is displayed. |  |
| 6 | Maintain Basic Data | On the Basic data 1 view, maintain the following values:Descr.: Service product with BOM 01_01Base Unit of Measure: HR (Hour)Material Group: P001 (Services)GenItemCatGroup: SRVP (Service Product)Then choose Save. | Basic data is maintained and the service product is saved.After saving, the Create Material (Initial Screen) view is displayed.For every different language used in your company the corresponding description for the product has to be maintained per language code! |  |
| 7 | Maintain Sales Organization Data (1) | On the Sales: sales org. 1 view, maintain the following values:General dataCash Discount: X <selected>Tax dataTax classification: 1 (Full tax)Then choose Enter. | Sales organizational data is maintained. The Sales: sales org. 2 tab page is displayed. |  |
| 8 | Maintain Sales Organization Data (2) | On the Sales: sales org. 2 view, maintain the following entry:Item Category Group : SRVP (Service Product)Then choose Save. | Sales organizational data is maintained. The Sales: General/Plant tab page is displayed. |  |

##### Create Service Product - SRV_BOM_02_01

Purpose

This material is relevant for cloud edition only.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Product Data (MDG). | The Home page appears. |  |
| 2 | Access the SAP Fiori app | Choose the Create Material tile. | The Create Material (Initial Screen) is displayed. |  |
| 3 | Maintain Material Basic Data (for Service Product ) | On the Create Material (Initial Screen) make the following entries: dialog window, select theMaterial: SRV_BOM_02_01Material Type: Service ProductThen choose Continue (Enter). | You have maintained basic information for the new service product.The Select View(s) dialog window is displayed. |  |
| 4 | Choose Views | On the Select View(s) dialog window, select the following views:Basic Data 1Sales: Sales Org. Data 1Sales: Sales Org. Data 2Then choose Continue (Enter). | The Organizational Levels dialog window is displayed. |  |
| 5 | Choose Organizational Levels | On the Organizational Levels window, maintain the following values:Sales Org.: 1710 (Dom. Sales Org US)Distr. Channel: 10 (Direct Sales)Then choose Continue (Enter). | Organizational data has been selected.The Create Material SRV_BOM_ 02_01 view is displayed. |  |
| 6 | Maintain Basic Data | On the Basic data 1 view, maintain the following values:Descr.: Service product with BOM 02_01Base Unit of Measure: HR (Hour)Material Group: P001 (Services)GenItemCatGroup: SRVP (Service Product)Then choose Enter. | Basic data is maintained and the service product is saved.After saving, the Create Material (Initial Screen) view is displayed.For every different language used in your company the corresponding description for the product has to be maintained per language code! |  |
| 7 | Maintain Sales Organization Data (1) | On the Sales: sales org. 1 view, maintain the following values:General dataCash Discount: X <selected>Tax dataTax classification: 1 (Full tax)Then choose Enter. | Sales organizational data is maintained. The Sales: sales org. 2 tab page is displayed. |  |
| 8 | Maintain Sales Organization Data (2) | On the Sales: sales org. 2 view, maintain the following entry:Item Category Group : SRVP (Service Product)Then choose Save. | Sales organizational data is maintained. The Sales: General/Plant tab page is displayed. |  |

##### Create Service Product - SRV_BOM_02_02

Purpose

This material is relevant for cloud edition only.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Product Data (MDG). | The Home page appears. |  |
| 2 | Access the SAP Fiori app | Choose the Create Material tile. | The Create Material (Initial Screen) is displayed. |  |
| 3 | Maintain Material Basic Data (for Service Product ) | On the Create Material (Initial Screen) make the following entries: dialog window, select theMaterial: SRV_BOM_02_02Material Type: Service ProductThen choose Continue (Enter). | You have maintained basic information for the new service product.The Select View(s) dialog window is displayed. |  |
| 4 | Choose Views | On the Select View(s) dialog window, select the following views:Basic Data 1Sales: Sales Org. Data 1Sales: Sales Org. Data 2Then choose Continue (Enter). | The Organizational Levels dialog window is displayed. |  |
| 5 | Choose Organizational Levels | On the Organizational Levels window, maintain the following values:Sales Org.: 1710 (Dom. Sales Org US)Distr. Channel: 10 (Direct Sales)Then choose Continue (Enter). | Organizational data has been selected.The Create Material SRV_BOM_02_02 view is displayed. |  |
| 6 | Maintain Basic Data | On the Basic data 1 view, maintain the following values:Descr.: Service product with BOM 02_02Base Unit of Measure: HR (Hour)Material Group: P001 (Services)GenItemCatGroup: SRVP (Service Product)Then choose Enter. | Basic data is maintained and the service product is saved.After saving, the Create Material (Initial Screen) view is displayed.For every different language used in your company the corresponding description for the product has to be maintained per language code! |  |
| 7 | Maintain Sales Organization Data (1) | On the Sales: sales org. 1 view, maintain the following values:General dataCash Discount: X <selected>Tax dataTax classification: 1 (Full tax)Then choose Enter. | Sales organizational data is maintained. The Sales: sales org. 2 tab page is displayed. |  |
| 8 | Maintain Sales Organization Data (2) | On the Sales: sales org. 2 view, maintain the following entry:Item Category Group : SRVP (Project)Then choose Save. | Sales organizational data is maintained. The Sales: General/Plant tab page is displayed. |  |

#### Create New Bill of Materials

Purpose

This material is relevant for cloud edition only. In this step, you can create a new Bill of Material.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a BOM Engineer. | The SAP Fiori launchpad is displayed.. |  |
| 2 | Access the SAP Fiori app | Open Maintain Bill Of Material (Version 2) - Create, change & display BOMs (F1813A) app. |  |  |
| 3 | Choose Create BOM | On the Maintain Bill of Material screen, choose Create BOM. | The Create BOM dialog box appears. |  |
| 4 | Maintain BOM Header data | On the Create BOM window, enter data similar to the following example and choose OK:ExampleMaterial: SRV_BOM_01_01BOM usage: S (Service Management)Valid From: Today | The Maintain Bill of Material screen is displayed and by default, the Components tab will be open. |  |
| 5 | Maintain BOM Component data | In the BOM Item Number 0010 line, make entries similar to the following example:ExampleComponent: SRV_BOM_02_01Component quantity:10 HR(Press Enter to enable Component and Component Quantity fields)Note Item Category value is N (Non Stock Item) | BOM Item Number 0010, Component, Component Description and Component quantity is displayed in the first table line. |  |
| 6 | Maintain additional BOM Components data | Repeat above step for BOM Item Number 0020 with the following entries:Component: SRV_BOM_02_02Component quantity: 20 HR(Press Enter to enable Component and Component Quantity fields)Note Item Category value is N (Non Stock Item) | BOM Item Number 0020, Component, Component Description and Component quantity is displayed in the table lines. |  |
| 8 | Navigate to Item Detail | In the BOM Item Number 0010 line, click the details arrow on extreme right side of tableOn the Maintain Bill of Material screen, make entries similar to the following example under the Basic Details tab:ExampleComponent quantity: 10Component UoM: HR | The Maintain Bill of Material screen with the details section for the entered item appears. |  |
| 9 | Navigate to Item Detail | In the BOM Item Number 0020 line, click the details arrow on extreme right side of tableOn the Maintain Bill of Material screen, make entries similar to the following example under the Basic Details tab:ExampleComponent quantity: 20Component UoM: HR | The Maintain Bill of Material screen with the details section for the entered item appears. |  |
| 10 | Choose Save | On the Maintain Bill of Material screen, choose Create. | The Bill of Material is saved.Note After saving, BOM status will be automatically set to 1 (Active).If BOM Status 2 (Inactive) is needed for the BOM, on the Maintain Bill of Material screen, choose Show Header Details, choose Administrative Data and set appropriately the BOM Status before saving again.Change Number is added under Timeline tab. |  |

### Create Equipment BOM

#### Create Equipment

Purpose

In this test step you maintain a record for a piece of equipment that is installed in a functional location.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Maintenance Planner.. | The SAP Fiori launchpad is displayed.. |  |
| 3 | Access the SAP Fiori App | Open Create Technical Object | A new window opens, showing the Create Technical object: Initial Screen. |  |
| 4 | Create Equipment | On the Create Technical Object screen, select the Technical Object Type: Equipment.On the next screen, enter the following:Technical Object Type: EquipmentTechnical Object: leave emptyValid From: today's dateTechnical Object Category: M (Machines)Choose Continue (Enter). |  |  |
| 5 | Maintain General Data | On the Create Technical Object: <Equipment ID> screen, in the General Data section, enter the following:Description: For example, Equipment of BOM header for serviceObject Type: For example, 9400Start-Up Date: For example, today’s dateCountry/Region of Manufacture: For example, USMonth/Year of Construction: For example, 04/2011Manufacturer Part Number: For example, HZZ-TD B4Manufacturer Serial Number: For example, HZZ-TD B4/66Acquisition Value/Currency: For example,10,000.00/ USDAcquisition Date: For example, 04/10/2011Note Optionally maintain further general data, then navigate to the Location Data section. | The create technical object: general data screen appears. |  |
| 6 | Maintain Location Data | In the Location Data section, enter the following:Maintenance Plant: For example, 1710 for USLocation: For example, YB_1701 for USPlant Section: For example, YOH for USNote Technical objects that belong to the same structure must all have the same plant assigned. As an alternative, you can leave the plant information empty for all technical objects.Optionally maintain further details, such as address information. | The create technical object: location data screen appears. |  |
| 8 | Maintain Organizational Data | In the Organizational Data section, enter the following:Planner Group: For example, 920 for USPlanning Plant: For example, 1710 for USMaintenance Work Center: For example, RES-0100 for USWork Center Plant: For example, 1710 for USCost Center: For example, 17101701 for USOptionally, you can maintain additional information like, for example, partner information and so on in the Organizational Data section. | The create technical object: Organizational data screen appears. |  |
| 9 | Save Equipment | Optionally, you can maintain additional information for other sections.Choose Check Entries button.Choose Save. | Equipment is created.Note down the equipment ID created. |  |

#### Create Equipment BOM

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Maintenance Planner.. | The SAP Fiori launchpad is displayed.. |  |
| 2 | Access the SAP Fiori App | Open Create Equipment BOM | A new window opens, showing the Create Equipment BOM: Initial Screen. |  |
| 3 | Create Equipment | On the Create Equipment BOM: Initial Screen.screen, enter the following:Equipment: Equipment ID generated in previous chapterBOM Usage: SChoose Continue. |  |  |
| 4 | Maintain Material Data | On the Create equipment BOM: General Item Overview screen, in the Material section, enter the following:Component: Material ID For Example SRV_BOM_02_02Item Category: N (Non Stock Item)Quantity: For example, 10Unit of Measure: For example, HRChoose Enter | The Create equipment BOM: General Item Overview screen appears. |  |
| 5 | Save Equipment | Choose Save | Equipment BOM is created |  |

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
> Flagged while digesting this document, not verified: Step 8 of SRV_BOM_02_02 gives Item Category Group SRVP labelled (Project) whereas the other two products label SRVP as (Service Product)

## Connections
- part-of :: [[_cluster]]
- related-to :: [[14-maintenance-service-and-projects/bom-mds-63j-493]]
- related-to :: [[14-maintenance-service-and-projects/material-und-equipmentstuckliste-fur-service-anlegen-sds-63j-490]]
- related-to :: [[14-maintenance-service-and-projects/mds-63j-495]]
- related-to :: [[14-maintenance-service-and-projects/script-de-dados-mestre-criar-lista-tecnica-de-material-e-equipamento-p]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/63J_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 22,502 chars in the whole document
