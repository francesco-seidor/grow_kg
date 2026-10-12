---
id: 13-quality-ehs-and-compliance/create-quality-info-record-mds-bf5-551
title: Create Quality Info Record - MDS (BF5) (BF5_S4CLD2608_Master_Data_EN_XX)
description: "SAP S/4HANA Cloud Public Edition 2608 master data script (BF5): creating quality info records, QM control keys and PPAP settings in procurement."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/quality-info-records]
aliases: [BF5_S4CLD2608_Master_Data_EN_XX]
keywords: [Quality Info Records in Procurement, quality info record, qm control keys, production part approval, first article inspection, quality planner role, master data prerequisites, goods receipt inspection, supplier release, BF5]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BF5_S4CLD2608_Master_Data_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-551
topic: 13-quality-ehs-and-compliance/quality-info-records
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Create Quality Info Record - MDS (BF5) (BF5_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BF5_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Quality Info Records in Procurement** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Quality Info Record - MDS (BF5) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233904892)

[2 Prerequisites 3](#_Toc233904893)

[2.1 System Access 3](#_Toc233904894)

[2.2 Roles 3](#_Toc233904895)

[2.3 Required Organizational Units 3](#_Toc233904896)

[2.4 Mandatory and Optional Master Data 4](#_Toc233904897)

[3 Overview Table 5](#_Toc233904898)

[4 Test Procedures 6](#_Toc233904899)

[4.1 Create Quality Info Record in Procurement 6](#_Toc233904900)

[4.2 Create Quality Info Record for Materials Without Quality Info Record (Optional) 7](#_Toc233904901)

[4.3 Assign QM Control Keys for Procurement 8](#_Toc233904902)

[4.4 Create settings for PPAP 9](#_Toc233904903)

## Purpose

If a quality assurance agreement or a supplier release is required for a material, a quality planner must create a quality information record (quality info record). The quality info record determines how the material can be processed further.

When a purchase order is created, the system checks whether a quality info record is required and available for the combination of material and supplier.

The system also checks whether the supplier and material-supplier combination is blocked or released for quotations, purchase orders and/or goods receipt. The execution of this check depends on the settings of the QM in procurement control key in the material master.

Additionally, you can assign QM systems and trigger a possible inspection accordingly. It can also determine, of a goods receipt inspection and/or a source inspection is triggered. You can also indicate that a production part approval process (PPAP) is required for which you can plan first article inspections (FAI) in the quality info record. You can manage PPAP here by updating the PPAP Status and Valuation Code (based on the usage decision made). Also, you can assign multiple purchase oders/items at a time for PPAP to perform First Article Inspection (FAI).

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
| Quality Planner | SAP_BR_QUALITY_PLANNER | Quality Planning | SAP_BR_QUALITY_PLANNER |  |

For more information about business roles, refer to Assigning Business Roles to a User in the Administration Guide for the Implementation of SAP S/4HANA Cloud Public Edition.

### Required Organizational Units

Some segments of customer master data are dependent on the organizational units of the company, General (Central) Data does not depend on an organizational unit or the company code. The following table gives an overview of these different data segments and their relevant organizational units:

| Data Segment | Depends On | Field Examples | Comments | Organizational Unit to be Used |
| --- | --- | --- | --- | --- |
| Quality Info Record | Plant |  | Plant data can exist for every Plant ID of your enterprise structure for which the material master record is used. | Plant: |

### Mandatory and Optional Master Data

Quality management data records may refer to other master data. The following table gives an overview of optional and mandatory master data objects to be used in a quality info record.

| Master Data Object | Used in Data Segment | Mandatory / Optional | Comments |
| --- | --- | --- | --- |
| Material Master |  | Mandatory | With quality management view. For more information, the master data script, Create Quality Management Attributes for Material/Product Master - MDS (BNY). |
| Supplier Master |  | Mandatory |  |

|  |
| --- |
| Note A Quality Info Record is necessarily needed, if the QM procurement key requires a supplier release. In this case, for each supplier-material combination, a Quality Info Record needs to be created. |

## Overview Table

This scope item consists of several process steps that are listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Quality Info Record in Procurement](#unique_8) [page ] 6 | Quality Planner | Create Quality Info Record - Procurement (QI01) | A Quality Info Record is created. |
| [Create Quality Info Record for Materials Without Quality Info Record (Optional)](#unique_9) [page ] 7 | Quality Planner | Manage Quality Info Records (F2256A) | A Quality Info Record is created. |
| [Assign QM Control Keys for Procurement](#unique_10) [page ] 8 | Quality Planner | Assign QM Control Keys for Procurement - Process Manually (QI05) | A Quality Info Record is created. |
| [Create settings for PPAP](#unique_11) [page ] 9 | Quality Planner | Manage Quality Info Records (F2256A) | A Quality Info Record is created. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Quality Info Record in Procurement

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Quality Info Record - Procurement (QI01). | The Create Q-Info Record view displays. |  |
| 3 | Enter General Data | Make the following entries:Material: <material number>Supplier: <supplier code>Plant: <plant code>Choose Continue. |  |  |
| 4 | Enter Release Data | In the Release section, enter the following data:Release Until: date in the future, for example, in one yearOptional:Release Qty is Active: flaggedRelease Quantity: for example, 15 |  |  |
| 5 | Save Your Data | Choose Save. | Your data is saved. |  |

|  |
| --- |
| Note In the Quality Info Record, you can also decide whether you want to deactivate the goods receipt inspection or perform a goods receipt inspection and/or source inspection. For this purpose, choose the Inspection Control tab, and enter the following data:If you want to perform a source inspection in addition to a goods receipt inspection, enter an inspection type for the source inspection and a lead time in days.If you do not want to perform a goods receipt inspection even though the settings in the material master specify such an inspection, set the No Inspection indicator.If you want to perform a source inspection instead of a goods receipt inspection, set the relevant indicator.If this indicator is set, the system does not create an inspection lot for a goods receipt if a source inspection is performed. If no source inspection is performed, an inspection lot is generated for goods receipt.Under the Inspection Control tab, you can also enter the following:Supplier’s QM systemIf the supplier has a QM system, you can store the description of the QM system for this specific material here.Production part approvalYou can specify that a production part approval process is required. You must make further settings for this in the Manage Quality Info Records (F2256A) app (see chapter [Assign QM Control Keys for Procurement](#unique_10) [page ] 8). |

### Create Quality Info Record for Materials Without Quality Info Record (Optional)

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Quality Info Records (F2256A). |  |  |
| 3 | Create Quality Info Record (Optional) | Choose Create in the upper right corner of the results table and maintain the following data in the Header level:Material: material numberSupplier: supplier codePlant: plant codeFor the Release section, refer to the previous chapter, step 4. |  |  |
| 4 | Save Your Data | Choose Create. | Your data is saved and a new quality info record was created. |  |

### Assign QM Control Keys for Procurement

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Assign QM Control Keys for Procurement - Process Manually (QI05). |  |  |
| 3 | Assign QM Control Key | You can run this selection on plant and/or material level. Choose the QM control key to be assigned.Material: material numberPlant: plant codeQM Control Key: QM Control KeyImplement Database Change: active (if this indicator is not set, only a test run is executed)Note Only those materials, where the QM in Procur. Active indicator is set in the material master data, are selected. |  |  |

### Create settings for PPAP

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

A first article inspection is achieved by using the dedicated inspection plan usage GR Model Inspection, which is assigned to the following Control Keys for QM in Procurement:

- 0001 Supplier Release
- 9001 Supplier Release (with Error Message)

In detail, the following conditions must be met so that a first article inspection is executed:

- An inspection plan with usage GR Model Inspection (51) exists for first article inspection.
- One of the QM control keys listed above is assigned to the material.
- For this material, a quality info record exists with the following settings under Production Part Approval:
    - Production part approval is enabled and the PPAP level and the PPAP status are set.
    - At least one purchase order and purchase order item is entered.

At goods receipt for the purchase order item, an inspection lot is created for first article inspection. For this inspection lot, the FAI Plan Usage of the QM control key is taken and the usage maintained for the inspection type.

Procedure

You enable PPAP in the Manage Quality Info Records (F2256A) app. There you can specify for a material that a first article inspection should take place at goods receipt for one or several purchase order items.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Quality Info Records (F2256A). |  |  |
| 3 | Create Quality Info Record | Choose Create in the upper right corner of the results table and maintain the following data in the Header level:Material: material numberSupplier: supplier codePlant: plant codeFor the Release section, refer to Step 4 in the previous chapter.Alternatively , select an existing Quality Info Record you want to enable the PPAP. |  |  |
| 4 | Enter Production Part Approval Data | Got to the Production Part Approval section. Choose Enable.Assign corresponding PPAP Level in the PPAP Level field. |  |  |
| 5 | Save Your Data | Choose Create. | Your data is saved and a new quality info record was created. |  |

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
- related-to :: [[13-quality-ehs-and-compliance/crear-registro-info-de-calidad-mds-bf5-552]]
- related-to :: [[13-quality-ehs-and-compliance/criar-registro-info-de-qualidade-mds-bf5-554]]
- related-to :: [[13-quality-ehs-and-compliance/mds-bf5-553]]
- related-to :: [[13-quality-ehs-and-compliance/mds-bf5-555]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BF5_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 16,395 chars in the whole document
