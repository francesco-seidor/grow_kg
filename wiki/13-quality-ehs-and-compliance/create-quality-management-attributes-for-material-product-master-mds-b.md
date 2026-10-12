---
id: 13-quality-ehs-and-compliance/create-quality-management-attributes-for-material-product-master-mds-b
title: Create Quality Management Attributes for Material/Product Master - MDS (BNY) (BNY_S4CLD2608_Master_Data_EN_XX)
description: SAP S/4HANA Cloud Public Edition master data script (BNY) for maintaining the Quality Management view of a material via Create Material (MM01).
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/qm-material-master-attributes]
aliases: [BNY_S4CLD2608_Master_Data_EN_XX]
keywords: [Quality Management View of the Material Master, quality management view, material master, inspection setup, master data scripts, business roles, automatic usage decision, qm procurement data, BNY]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNY_S4CLD2608_Master_Data_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-689
topic: 13-quality-ehs-and-compliance/qm-material-master-attributes
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Create Quality Management Attributes for Material/Product Master - MDS (BNY) (BNY_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNY_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Quality Management View of the Material Master** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Quality Management Attributes for Material/Product Master - MDS (BNY) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233905248)

[2 Prerequisites 3](#_Toc233905249)

[2.1 System Access 3](#_Toc233905250)

[2.2 Roles 3](#_Toc233905251)

[2.3 Required Organizational Units 3](#_Toc233905252)

[3 Overview Table 4](#_Toc233905253)

[4 Test Procedures 5](#_Toc233905254)

[4.1 Quality Management Attributes for Material 5](#_Toc233905255)

## Purpose

If material quality is supposed to be inspected, the prerequisite is that the quality management view in the material master is maintained for the respective plant.

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
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Products / Product Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |

### Required Organizational Units

In this section, you describe and explain all organizational units that are relevant to create the master data records.

Some segments of customer master data are dependent on the organizational units of the company, General (Central) Data does not depend on an organizational unit or the company code. The following table gives an overview of these different data segments and their relevant organizational units:

| Data Segment | Depends On | Field Examples | Comments | Organizational Unit to be Used |
| --- | --- | --- | --- | --- |
| Quality Management | Plant |  | Plant data can exist for every Plant ID of your enterprise structure for which the material master record is used. | Plant: |

## Overview Table

This scope item consists of several process steps that are listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Quality Management Attributes for Material](#unique_7) [page ] 5 | Master Data Specialist - Product Data | Create Material (MM01) | Material Master Data – Quality Management Data is created. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Quality Management Attributes for Material

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Material (MM01). | The app opens. |  |
| 3 | Enter Material Data | On the Create Material (Initial screen) screen, make the following entries:Material: <Material number>Material Type: Trading GoodsPress Enter. | The Select View(s) screen displays. |  |
| 4 | Select Quality Management View | On the Select View(s) screen, select the Quality Management view and choose Org Levels. | A new screen displays for organizational data input. |  |
| 5 | Enter Organizational Levels Data | On the Organizational Levels screen, in the Organizational levels section, make the following entry and choose Continue:Plant: <Plant code> | The Create Material… (Trading Goods) screen displays. |  |
| 6 | Enter Quality Management Data | On the Create Material <XXX> (Trading Goods) screen, on the Quality management tab, enter the description for the material:Descr.: <Enter the description>In the General Data section, on the Quality management tab, make the following entry:Base Unit of Measure: <Unit of measure>Choose Insp. Setup. In the dialog box that diaplays, choose Create Inspection Types and make the following entries:Insp Type: For example, 01.Preferred Insp. Type: XActive: XSelect Insp. Type Det. to see details.Ensure that the following fields are flagged with X:Post to Insp. StockInsp. with Task ListAutomatic AssignmentInspect CharcsChoose Continue. |  |  |
| 7 | Enable/Disable Automated Usage Decision (Optional) | Select or deselect Automatic UD to enable or disable the automated usage decision for this material and inspection type combination.Note An automatic usage decision after results recording can be made for inspection lots with positive inspection results. To enable this process, your system must be set up accordingly in the Manage Your Solution (F1241) app. Please check[SAP Help](https://help.sap.com/viewer/DRAFT/84dbf30eedb4450983dc3d1c81b71996/1811.500/en-US/746b66d98e504e238eca043bae05ecb8.html) for further technical information and prerequisites. |  |  |
| 8 | Enter Procurement Data (Optional) | If you want to optionally use a quality information record for material, on the Quality Management tab, in the Procurement Data section, make the following entries:QM Procuremnt Active: XQM Control Key: For example, 0001. |  |  |
| 9 | Save Your Data | Choose Save. | Your data is saved. |  |

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
- related-to :: [[13-quality-ehs-and-compliance/criar-atributos-de-administracao-de-qualidade-para-mestre-de-materiais]]
- related-to :: [[13-quality-ehs-and-compliance/mds-bny-691]]
- related-to :: [[13-quality-ehs-and-compliance/mds-bny-693]]
- related-to :: [[13-quality-ehs-and-compliance/script-de-datos-maestros-crear-atributos-de-gestion-de-calidad-para-ma]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNY_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 9,453 chars in the whole document
