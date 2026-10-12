---
id: 11-inventory-warehouse-and-transportation/maintain-production-supply-area-mds-3ks-341
title: Maintain Production Supply Area - MDS (3KS) (3KS_S4CLD2608_Master_Data_EN_XX)
description: "Master data script (3KS) for optionally assigning storage bins to Production Supply Areas in warehouse production integration, SAP S/4HANA Cloud Public Edition."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/ewm-production-integration]
aliases: [3KS_S4CLD2608_Master_Data_EN_XX]
keywords: [EWM Production Supply and Receipt, production supply area, storage bin assignment, warehouse master data, production integration, control cycle, business roles, kanban supply, 3KS]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KS_S4CLD2608_Master_Data_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-341
topic: 11-inventory-warehouse-and-transportation/ewm-production-integration
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Maintain Production Supply Area - MDS (3KS) (3KS_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KS_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **EWM Production Supply and Receipt** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Maintain Production Supply Area - MDS (3KS) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233904620)

[2 Prerequisites 3](#_Toc233904621)

[2.1 System Access 3](#_Toc233904622)

[2.2 Roles 3](#_Toc233904623)

[2.3 Required Organizational Units 3](#_Toc233904624)

[2.4 Mandatory and Optional Master Data 4](#_Toc233904625)

[2.5 Business Conditions 4](#_Toc233904626)

[3 Overview Table 5](#_Toc233904627)

[4 Test Procedures 6](#_Toc233904628)

[4.1 (OPTIONAL) Assign Bin to PSA - Warehouse 6](#_Toc233904629)

[4.2 (OPTIONAL) Assign Bin to PSA 7](#_Toc233904630)

## Purpose

In this document, you can learn how to carry out the following activities to create warehouse master data for production supply:

- [(OPTIONAL) Assign Bin to PSA - Warehouse](#unique_2) [page ] 6
- [(OPTIONAL) Assign Bin to PSA](#unique_3) [page ] 7

The Production Supply Area creation and replication, as well as the Storage Bin Assignment to PSA are supposed to be done by the execution of relevant steps in the master data script or test script documents mentioned in the Business Condition chapter. This master data script is only for customers to check the relevant settings and create settings manually in case the business conditions are not fulfilled.

The description includes those data segments that are relevant for the master data to work in a regular system environment. You mainly learn which data segments and fields usually need to be filled with input values. Fields that are not relevant for the scope of the SAP S/4HANA content delivery by SAP Best Practices are not described in this document even though they may appear on the UI.

You use this master data for the Production Integration business processes in Warehouse Management.

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

Some segments of master data are dependent on the organizational units of the company. General (central) data does not depend on an organizational unit or the company code. The following table gives an overview of these different data segments and their relevant organizational units:

| Data Segment | Depends On | Field Examples | Comments | Organizational Unit to be Used |
| --- | --- | --- | --- | --- |
| All | Warehouse Number |  |  |  |

### Mandatory and Optional Master Data

Master data records may refer to other master data. The following table gives an overview of optional and mandatory master data objects to be used when creating a storage bin assignment to PSA master data record.

| Master Data Object | Used in Data Segment | Mandatory / Optional | Comments |
| --- | --- | --- | --- |
| Business Partner | Assign Bin to PSA - Warehouse | Mandatory | Business Partner as the Party Entitled to Dispose for the Warehouse. |
| Production Supply Area | Assign Bin to PSA - Warehouse | Mandatory | The Production Supply Area that is created in the SAP S/4HANA. See the Business Condition chapter. |
| Product | Assign Bin to PSA - Warehouse | Mandatory |  |
| Storage Bin | Assign Bin to PSA - Warehouse | Mandatory |  |

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 40D - Create Production Supply Area - MDS | This Master Data Script is the prerequisite of this document.When creating the Production Supply Area (PSA), use the Cloud WM Storage Location, e.g. 105W.After you have executed this master data script, you have created the following settings:Production Supply Area is created in the SAP S/4HANA.The relevant Production Supply Area is replicated automatically from the SAP S/4HANA to the Cloud Warehouse. |
| 3DV - Warehouse Production Integration | The prerequisite of this document is the Create Control Cycle step in the Preliminary Steps chapter of 3DV test script.After you have executed the Create Control Cycle step, you have created the following settings:The relevant Production Supply Area is replicated automatically from the SAP S/4HANA to the Cloud Warehouse.The storage bin is assigned to the PSA. |
| 3VT - Warehouse Kanban Supply into Production | The prerequisite for this document is the Control Cycle for Kanban: Stock Transfer step in the Preliminary Steps chapter of the 3VT test script.After you have executed the Control Cycle for Kanban: Stock Transfer step, you have created the following settings:The relevant Production Supply Area is replicated automatically from the SAP S/4HANA to the Cloud Warehouse.The storage bin is assigned to the PSA. |

## Overview Table

This master record consists of several segments provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Segment | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [(OPTIONAL) Assign Bin to PSA - Warehouse](#unique_2) [page ] 6 | Warehouse Clerk (EWM) | Assign Bin to PSA - Warehouse (/SCWM/PSASTAGE) | The assignment of storage bin to PSA is created. |
| [(OPTIONAL) Assign Bin to PSA](#unique_3) [page ] 7 | Warehouse Clerk (EWM) | Assign Bin to PSA (/SCWM/PSASTAGE2) | The assignment of storage bin to PSA is created. |

## Test Procedures

This section describes procedures for each segment or process step that is part of this master record.

### (OPTIONAL) Assign Bin to PSA - Warehouse

Purpose

In this section, you manage the storage bin assignments of all Production Supply Areas of the Warehouse Number in SAP S/4HANA using the SAP Fiori launchpad.

This step is optional and you can skip it if the Storage Bin has been assigned to the PSA as expected. It is only needed if no bin assignments for your PSA have been done yet during the Control Cycle creation step. See the ‘Create Control Cycle’ step in the Business Condition chapter.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as the Warehouse Clerk (EWM). |  |  |
| 2 | Access App | Open Assign Bin to PSA - Warehouse (/SCWM/PSASTAGE). |  |  |
| 3 | Create New Entry | On the Change View “Assign Bin to PSA”: Overview screen, choose New Entries. |  |  |
| 4 | Enter Assignment Values | On the New Entries: Details of Added Entries screen, enter the following data:Disposal: <Business Partner ID for the Party Entitled to Dispose>Supply Area: <Production Supply Area>Product: <Product ID>Storage Bin: <Storage Bin ID> |  |  |
| 5 | Save Your Data | Choose Save. | A system message tells you that the assignment of the storage bin to the PSA has been saved. |  |

### (OPTIONAL) Assign Bin to PSA

Purpose

In this section, you manage all storage bin assignments within a particular Production Supply Area in SAP S/4HANA using the SAP Fiori launchpad.

This step is optional and you can skip it if the Storage Bin has been assigned to the PSA as expected. It is only needed if no bin assignments for your PSA have been done yet during the Control Cycle creation step. See the ‘Create Control Cycle’ step in the Business Condition chapter.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as the Warehouse Clerk (EWM). |  |  |
| 2 | Access App | Open Assign Bin to PSA (/SCWM/PSASTAGE2). |  |  |
| 3 | Determine Work Area | On the Determine Work Area Entry screen, enter the following data:Party Entitled to Dispose: <Business Partner ID for the Party Entitled to Dispose>Supply Area: <Production Supply Area>Choose Continue. |  |  |
| 4 | Create New Entry | On the Change View “Assign Bin to PSA”: Overview screen, choose New Entries. |  |  |
| 5 | Enter Assignment Values | On the New Entries: Details of Added Entries screen, enter the following data:Product: <Product ID>Storage Bin: <Storage Bin ID> |  |  |
| 6 | Save Your Data | Choose Save. | A system message tells you that the assignment of the storage bin to the PSA has been saved. |  |

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
- related-to :: [[11-inventory-warehouse-and-transportation/atualizar-area-de-abastecimento-da-producao-mds-3ks-344]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-3ks-343]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-3ks-345]]
- related-to :: [[11-inventory-warehouse-and-transportation/produktionsversorgungsbereich-pflegen-sds-3ks-340]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KS_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 12,201 chars in the whole document
