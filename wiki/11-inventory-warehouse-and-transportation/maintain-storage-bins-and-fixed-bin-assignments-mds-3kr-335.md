---
id: 11-inventory-warehouse-and-transportation/maintain-storage-bins-and-fixed-bin-assignments-mds-3kr-335
title: Maintain Storage Bins and Fixed Bin Assignments - MDS (3KR) (3KR_S4CLD2608_Master_Data_EN_XX)
description: "SAP S/4HANA Cloud Public Edition master data script (3KR) for creating, changing, displaying, mass-changing storage bins and assigning fixed bins in EWM warehouse management."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/ewm-storage-bins]
aliases: [3KR_S4CLD2608_Master_Data_EN_XX]
keywords: [EWM Storage Bins and Fixed Bin Assignments, storage bins, fixed bin assignment, warehouse management, mass change storage bins, warehouse master data, business roles, party entitled to dispose, test procedures, 3KR]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KR_S4CLD2608_Master_Data_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-335
topic: 11-inventory-warehouse-and-transportation/ewm-storage-bins
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Maintain Storage Bins and Fixed Bin Assignments - MDS (3KR) (3KR_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KR_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **EWM Storage Bins and Fixed Bin Assignments** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Maintain Storage Bins and Fixed Bin Assignments - MDS (3KR) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233904624)

[2 Prerequisites 3](#_Toc233904625)

[2.1 System Access 3](#_Toc233904626)

[2.2 Roles 3](#_Toc233904627)

[2.3 Required Organizational Units 3](#_Toc233904628)

[2.4 Mandatory and Optional Master Data 3](#_Toc233904629)

[3 Overview Table 5](#_Toc233904630)

[4 Test Procedures 6](#_Toc233904631)

[4.1 Create Storage Bins 6](#_Toc233904632)

[4.2 Change Storage Bins 7](#_Toc233904633)

[4.3 Display Storage Bins 8](#_Toc233904634)

[4.4 Carry Out Mass Change to Storage Bins 9](#_Toc233904635)

[4.5 Assign Fixed Bins 10](#_Toc233904636)

## Purpose

In this document, you can learn how to carry out the following activities to create Warehouse Storage Bins and Fixed Bin Assignments:

- [Create Storage Bins](#unique_2) [page ] 6
- [Change Storage Bins](#unique_3) [page ] 7
- [Display Storage Bins](#unique_4) [page ] 8
- [Carry Out Mass Change to Storage Bins](#unique_5) [page ] 9
- [Assign Fixed Bins](#unique_6) [page ] 10

The description includes those data segments that are relevant for the master data to work in a regular system environment. You mainly learn which data segments and fields usually need to be filled with input values. Fields that are not relevant for the scope of the SAP S/4HANA content delivery by SAP Best Practices are not described in this document, even though they may appear on the screen.

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

### Required Organizational Units

Some segments of master data are dependent on the organizational units of the company. General (Central) Data does not depend on an organizational unit or the company code. The following table gives an overview of these different data segments and their relevant organizational units:

| Data Segment | Depends On | Field Examples | Comments | Organizational Unit to be Used |
| --- | --- | --- | --- | --- |
| All | Warehouse Number |  |  |  |

### Mandatory and Optional Master Data

Master data records may refer to other master data. The following table gives an overview of optional and mandatory master data objects to be used in a <type> master data record.

| Master Data Object | Used in Data Segment | Mandatory / Optional | Comments |
| --- | --- | --- | --- |
| Business Partner | Assign Fixed Storage Bins | Mandatory | Business Partner as the Party Entitled to Dispose for the Warehouse |

## Overview Table

This master record consists of several segments provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Segment | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Storage Bins](#unique_2) [page ] 6 | Warehouse Clerk (EWM) | Create Storage Bins (/SCWM/LS01) | The storage bins are created. |
| [Change Storage Bins](#unique_3) [page ] 7 | Warehouse Clerk (EWM) | Edit Storage Bins (/SCWM/LS02) | The storage bins are changed. |
| [Display Storage Bins](#unique_4) [page ] 8 | Warehouse Clerk (EWM) | Display Storage Bins (/SCWM/LS03) | The storage bins are displayed. |
| [Carry Out Mass Change to Storage Bins](#unique_5) [page ] 9 | Warehouse Clerk (EWM) | Mass Edit Storage Bins (/SCWM/LS11) | The mass changes to the storage bins are made. |
| [Assign Fixed Bins](#unique_6) [page ] 10 | Warehouse Clerk (EWM) | Assign Fixed Bins (/SCWM/BINMAT) | The fixed bin assignment is created. |

## Test Procedures

This section describes procedures for each segment or process step that is part of this master record.

### Create Storage Bins

Purpose

In this section, you find a description of how to create storage bins in SAP S/4HANA using the SAP Fiori launchpad.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as the Warehouse Clerk (EWM). |  |  |
| 2 | Access App | Open Create Storage Bins (/SCWM/LS01). |  |  |
| 3 | Enter Storage Bin ID | On the Create Storage Bins (/SCWM/LS01) screen, enter the following data:Warehouse Number: <Your Warehouse Number>Storage Bin: <Storage Bin ID>Choose Enter. |  |  |
| 4 | Enter Storage Bin Attributes | On the Storage Bin tab, enter the following data:Storage Type: <Storage Type>Note Only the Storage Type field is mandatory. All of the other fields below are optional:Maximum WeightMax. VolumeBin AisleX CoordinateStackY CoordinateBin LevelZ CoordinateBin Angle |  |  |
| 5 | Save Your Data | Choose Save. | A system message tells you that the storage bin has been saved. |  |

### Change Storage Bins

Purpose

In this section, you change storage bins in SAP S/4HANA using the SAP Fiori launchpad.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as the Warehouse Clerk (EWM). |  |  |
| 2 | Access App | Open Edit Storage Bins (/SCWM/LS02). |  |  |
| 3 | Enter Storage Bin ID | On the Edit Storage Bins (/SCWM/LS02) screen, enter the following data:Warehouse Number: <Your Warehouse Number>Storage Bin: <Storage Bin ID>Choose Enter. |  |  |
| 4 | Change Storage Bin Attributes | On the Storage Bin tab, change the following values if necessary.Note Only the following fields can be changed:Maximum WeightMax. VolumeBin AisleX CoordinateStackY CoordinateBin LevelZ CoordinateBin Angle |  |  |
| 5 | Save Your Data | Choose Save. | A system message tells you that the storage bin has been saved. |  |

### Display Storage Bins

Purpose

In this section, you display the storage bins in SAP S/4HANA using the SAP Fiori launchpad.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as the Warehouse Clerk (EWM). |  |  |
| 2 | Access App | Open Display Storage Bins (/SCWM/LS03). |  |  |
| 3 | Enter Storage Bin ID | On the Display Storage Bins (/SCWM/LS03) screen, enter the following data:Warehouse Number: <Your Warehouse Number>Storage Bin: <Storage Bin ID>Choose Enter. | The storage bin attributes are displayed. |  |

### Carry Out Mass Change to Storage Bins

Purpose

In this section, you make a mass change to storage bins in SAP S/4HANA using the SAP Fiori launchpad.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as the Warehouse Clerk (EWM). |  |  |
| 2 | Access App | Open Mass Edit Storage Bins (/SCWM/LS11). |  |  |
| 3 | Enter Filter Criteria | On the Mass Change of Storage Bins in Warehouse Number XXXX screen, enter the following data:Warehouse Number: <Your Warehouse Number>You can enter the following values as selection/filter criteria:Storage Bin: <Storage Bin ID> to <Storage Bin ID>Storage Type: <Storage Type ID> to <Storage Type ID>Blocked StatusNote If you choose the Dynamic Selections checkbox, you can choose several filters for storage bin selection.Choose Execute. | The list of storage bins that match the selection criteria is displayed. |  |
| 4 | Mass Change to Storage Bins | Select the entries of your choice by selecting the corresponding checkboxes.Choose Delete to delete multiple bins at a time.orChoose Edit to change multiple bins at the same time. You will be able to make changes to the following attributes of the storage bins.Maximum WeightMax. VolumeBin AisleStackBin LevelBin Angle |  |  |
| 5 | Save Your Data | Choose Save. | A system message tells you that the changes to the storage bin have been saved. |  |

### Assign Fixed Bins

Purpose

In this section, you make a fixed bin assignment in SAP S/4HANA using the SAP Fiori launchpad.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as the Warehouse Clerk (EWM). |  |  |
| 2 | Access App | Open Assign Fixed Bins (/SCWM/BINMAT). |  |  |
| 3 | Enter Filter Criteria | On the Maintain Fixed Storage Bins screen, enter the following data:Warehouse Number: <Your Warehouse Number>Product: <Product ID> to <Product ID>Party Entitled to Dispose: <Business Partner ID> to <Business Partner ID>Note The Party Entitled to Dispose is the Business Partner maintained for the Warehouse Number.Storage Bin: <Storage Bin ID> to <Storage Bin ID>Storage Type: <Storage Type ID> to <Storage Type ID>Choose Execute. | The list of assigned fixed bins that match the selection criteria is displayed. |  |
| 4 | Create Fixed Bin Assignment | On the Warehouse Number XXXX: Display Fixed Storage Bin screen, choose Edit.On the Warehouse Number XXXX: Maintain Fixed Storage Bin screen, choose Create.In the newly created row, enter the following values:Disposal: <Business Partner ID for the Party Entitled to Dispose>Storage Bin: <Fixed Storage Bin ID>Ty.: <Fixed Bin Storage Type ID>Product: <Product ID>Max.Qty: <Quantity>DisplayUoM: <UoM for Maxmium Quantity> for example, PCMin.Qty: <Quantity>DisplayUoM: <UoM for Minimium Quantity > for example, PCIf you have maintained in the warehouse product master data the values for following fields:Max. No. BinsMaximum QuantityMinimum QuantityDisplay UoM for the maximium/minimium quantitiesThe Max.Qty and Min.Qty values in the fixed bin assignment will be calculated based on the values of Maximum Quantity, Minimum Quantity and Max. No. Bins in the warehouse product master data. The Display UoM will also be populated from the warehouse product master data. |  |  |
| 5 | Save Your Data | Choose Save. | A system message tells you that the storage bins have been saved. |  |

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
- related-to :: [[11-inventory-warehouse-and-transportation/mds-3kr-337]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-3kr-339]]
- related-to :: [[11-inventory-warehouse-and-transportation/script-de-dados-mestre-atualizar-posicoes-no-deposito-e-atribuicoes-de]]
- related-to :: [[11-inventory-warehouse-and-transportation/script-de-datos-maestros-actualizar-ubicaciones-y-asignaciones-de-ubic]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KR_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 13,983 chars in the whole document
