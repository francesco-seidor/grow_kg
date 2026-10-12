---
id: 11-inventory-warehouse-and-transportation/master-data-script-maintain-warehouse-products-attributes-3kq-329
title: "Master Data Script: Maintain Warehouse Products Attributes (3KQ) (3KQ_S4CLD2608_Master_Data_EN_XX)"
description: "SAP S/4HANA Cloud 2608 master data script 3KQ: maintaining warehouse product attributes via Warehouse Monitor (/SCWM/MON) or Manage Product Master Data (F1602)."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/ewm-warehouse-product-attributes]
aliases: [3KQ_S4CLD2608_Master_Data_EN_XX]
keywords: [EWM Warehouse Product Attributes, warehouse product attributes, warehouse monitor mass change, product master data, replenishment storage types, warehouse management, business roles, organizational units, party entitled to dispose, 3KQ]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KQ_S4CLD2608_Master_Data_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-329
topic: 11-inventory-warehouse-and-transportation/ewm-warehouse-product-attributes
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Master Data Script: Maintain Warehouse Products Attributes (3KQ) (3KQ_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KQ_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **EWM Warehouse Product Attributes** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Maintain Warehouse Products Attributes - MDS (3KQ) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233904617)

[2 Prerequisites 3](#_Toc233904618)

[2.1 System Access 3](#_Toc233904619)

[2.2 Roles 3](#_Toc233904620)

[2.3 Required Organizational Units 3](#_Toc233904621)

[2.4 Mandatory and Optional Master Data 4](#_Toc233904622)

[3 Overview Table 5](#_Toc233904623)

[4 Test Procedures 6](#_Toc233904624)

[4.1 Maintain Warehouse Product Attributes – with Warehouse Monitor 6](#_Toc233904625)

[4.2 Maintain Warehouse Product Attributes 7](#_Toc233904626)

## Purpose

In this document, you can learn how to create warehouse-relevant attributes for your Material/Product Master. There are two options to maintain the warehouse attributes:

- You can maintain Warehouse Product Attributes with the Warehouse Monitor (/SCWM/MON) app. This app can be used for single and mass changes.
- You can maintain Warehouse Product Attributes with the Manage Product Master Data (F1602) app. This app can be used for single changes.

This document includes those data segments that are relevant for the master data to work in a regular system environment. The reader mainly learns which data segments and fields usually need to be filled with input values. Fields that are not relevant for the scope of the SAP S/4HANA content delivery by SAP Best Practices are not described in this document even though they may appear on the UI.

You use this master data for all Warehouse Management business processes.

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
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Products / Product Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |

### Required Organizational Units

Some segments of master data are dependent on the organizational units of the company. General (Central) Data does not depend on an organizational unit or the company code. The following table gives an overview of these different data segments and their relevant organizational units:

| Data Segment | Depends On | Field Examples | Comments | Organizational Unit to be Used |
| --- | --- | --- | --- | --- |
| All | Warehouse Number |  |  |  |

### Mandatory and Optional Master Data

Master data records may refer to other master data. The following table gives an overview of optional and mandatory master data objects to be used in a <type> master data record.

| Master Data Object | Used in Data Segment | Mandatory / Optional | Comments |
| --- | --- | --- | --- |
| Business Partner | Maintain Warehouse Product Attributes | Mandatory | Business Partner as the Party Entitled to Dispose for the Warehouse |

## Overview Table

This master record consists of several segments provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Segment | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Maintain Warehouse Product Attributes – with Warehouse Monitor](#unique_7) [page ] 6 | Warehouse Clerk (EWM) | Warehouse Monitor (/SCWM/MON) | A mass change of warehouse products is carried out. |
| [Maintain Warehouse Product Attributes](#unique_8) [page ] 7 | Master Data Specialist - Product Data | Manage Product Master Data (F1602) | Warehouse attributes for material master data are created. |

## Test Procedures

This section describes procedures for each segment or process step that is part of this master record.

### Maintain Warehouse Product Attributes – with Warehouse Monitor

Purpose

In this section, you maintain Warehouse Product Attributes using the Warehouse Monitor (/SCWM/MON) app. This app can be used for single and mass changes.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as the Warehouse Clerk (EWM). |  |  |
| 2 | Access App | Open Warehouse Monitor (/SCWM/MON). | The Warehouse Management Monitor SAP - Warehouse Number XX50 screen is displayed. |  |
| 3 | Choose Menu | In the hierarchy in the left screen area, choose Product Master Data > Warehouse Attribute. |  |  |
| 4 | Enter Product Number | In the /SCWM/SAPLPROD_OVERVIEW dialog box, enter the following data:Basic Attributes section:Product Number: <Product Number> to <Product Number>Additional Options section:Only Prods W/o Whse Data: XChoose Execute. | The system displays the products that haven’t been maintained yet with warehouse data in the right screen area. |  |
| 5 | Select Products | In the Warehouse Attributes area, select the products, and then choose More Methods > Mass Change/Create. |  |  |
| 6 | Select Products | In the /SCWM/SAPLPROD_OVERVIEW dialog box, enter the following data where applicable.In the Warehouse Data section:Putaway Control Ind.Stk Rmvl Ctrl IndicatorBulk Storage Ind.Cycle Counting IndicatorProc.Type Det. Ind.Choose Execute.Note In the Cloud Warehouse Management, the Putaway Control Indicator and the Stk Rmvl Ctrl Indicator are usually maintained with the same value. However, in the replenishment process used in the warehouse, these two fields have to be maintained differently to enable the process. |  |  |
| 7 | Save Your Data | In the dialog box, confirm the changes. | A system message tells you that the products have been saved successfully. |  |

### Maintain Warehouse Product Attributes

Purpose

In this section, you find a description of how to maintain Warehouse Product Attributes with the Manage Product Master Data (F1602) app. This app can be used for single changes.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as the Master Data Specialist - Product Data. |  |  |
| 2 | Access App | Open Manage Product Master Data (F1602) . |  |  |
| 3 | Enter Material Number | On the Manage Product Master Data (F1602) screen, enter the following data:Product: <Material Number>Choose Go. | The material master data is displayed in the Product section. |  |
| 4 | Select Material | Select the row of the material master data. |  |  |
| 5 | Choose Warehouse Management | On the Product screen, choose Warehouse Management tab and go to Warehouse Management > Warehouse . |  |  |
| 6 | Edit Material Master Data | On the Product screen, choose Edit. |  |  |
| 7 | Add Warehouse Data | In the Warehouse section, select the warehouse number for your warehouse.If your warehouse number does not exist, choose Create. |  |  |
| 8 | Enter Values | On the Warehouse screen, enter the following data:In the General Information section:Warehouse: <EWM Warehouse Number>Party Entitled to Dispose: <Business Partner ID for the Party Entitled to Dispose>Process Type Determination IndicatorCycle Counting IndicatorNote Only Warehouse and Party Entitled to Dispose are mandatory for input. The following values are optional.In the Putaway section:Putaway Control IndicatorIn the Stock Removal section:Stock Removal Control IndicatorNote In the Cloud Warehouse Management, the Putaway Control Indicator and the Stk Rmvl Ctrl Indicator are maintained with the same value. However, in the replenishment process used in the warehouse, these two fields have to be maintained differently to enable the process. |  |  |
|  | Create Storage Type Data for Replenishment | In the Storage Types section, choose Create.On the New Record – Storage Type screen, enter the following data:In the General Information section:Storage Type: <Storage Type>Maximum Number of Bins: <Number of Bins>In the Replenishment section:Minimum Replenishment Quantity / Display UoM: <Quantity> / <UoM>Minimum Quantity / Display UoM: <Quantity> / <UoM>Maximum Quantity / Display UoM: <Quantity> / <UoM> |  |  |
| 9 | Save Your Data | Choose Apply. | The warehouse data is saved. |  |
| 10 | Go back to Product Screen | Go back to the Product screen. |  |  |
| 11 | Select Warehouse Management | On the Product screen, select the Plants tab. |  |  |
| 12 | Add Plant Data | In the Plants section, select the plant.If your plant does not exist, choose Create. |  |  |
| 13 | Enter Values | On the Plant screen, enter the following data in the General Information section:Serial Number Profile: <Serial Number Profile> |  |  |
| 14 | Save Your Data | Choose Apply. | The plant data is saved. |  |

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
- related-to :: [[11-inventory-warehouse-and-transportation/actualizar-atributos-de-productos-de-almacen-mds-3kq-es-330]]
- related-to :: [[11-inventory-warehouse-and-transportation/attribute-fur-lagerprodukte-pflegen-sds-3kq-328]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-3kq-331]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-3kq-333]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KQ_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 12,586 chars in the whole document
