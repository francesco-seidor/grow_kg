---
id: 06-management-accounting/create-profit-center-mds-bnh-605
title: Create Profit Center - MDS (BNH) (BNH_S4CLD2608_Master_Data_EN_XX)
description: Master data script (BNH) for creating profit center master data with Manage Profit Centers - Old Version (F3516) in SAP S/4HANA Cloud Public Edition 2608.
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/profit-centers]
aliases: [BNH_S4CLD2608_Master_Data_EN_XX]
keywords: [Profit Centers and Profit Center Reorganization, profit center master data, profit center validity period, profit center group, segment reporting, company code assignment, controlling area, business roles, master data scripts, BNH]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNH_S4CLD2608_Master_Data_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-605
topic: 06-management-accounting/profit-centers
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Create Profit Center - MDS (BNH) (BNH_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNH_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Profit Centers and Profit Center Reorganization** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Profit Center - MDS (BNH) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233904951)

[2 Prerequisites 3](#_Toc233904952)

[2.1 System Access and Roles 3](#_Toc233904953)

[2.2 Required Organizational Units 3](#_Toc233904954)

[2.3 Mandatory and Optional Master Data 4](#_Toc233904955)

[2.4 Main Parameters for Data Creation 5](#_Toc233904956)

[3 Overview Table 6](#_Toc233904957)

[4 Test Procedures 7](#_Toc233904958)

[4.1 Creating Profit Center Master Data 7](#_Toc233904959)

## Purpose

A profit center is an organizational unit in accounting that reflects a management-oriented structure of the organization for the purpose of internal control. Dividing your company up into profit centers allows you to determine profit for internal areas of responsibility and to delegate responsibility to decentralized units.

The master data of a profit center includes the name of the profit center, the controlling area it is assigned to, and the profit center’s period of validity, as well as information about the person responsible for the profit center, the profit center’s assignment to a node of the standard hierarchy, and data required for communication (address, telephone number and so on).

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access and Roles

Conduct the test in the following systems:

| System | Details |
| --- | --- |
| SAP S/4HANA Cloud Public Edition | System ID: ###Client: ### |

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Divisional Accountant | SAP_BR_DIVISION_ACCOUNTANT | Divisional Accounting | SAP_BR_DIVISION_ACCOUNTANT |  |

### Required Organizational Units

Some segments of customer master data are dependent on the organizational units of the company, General (Central) Data does not depend on an organizational unit or the company code. The following table gives an overview of these different data segments and their relevant organizational units:

| Data Segment | Depends On | Field Examples | Comments | Organizational Unit to be Used |
| --- | --- | --- | --- | --- |
| Profit Center Basic Data | Controlling AreaProfit Center GroupSegment | Name, Long Text, Validity period, User Responsible Person, Responsible Person | Profit center groups enable the controller to address profit centers group wise by providing the group name instead of single profit center names e.g. in customizing or reporting. In reporting, this allows an analysis of controlling key figures on an aggregate level.Segment is normally not posted to explicitly. Data is derived from account assignment objects like profit centers. In turn the profit center is normally not posted to explicitly. Data is derived from primary account assignment objects like cost centers, internal orders, etc. | Controlling Area:____________Profit Center Group:____________Segment:____________ |
| Profit Center Company Code Assignment | Company Code | Company Code | Company code data can exist for every company code ID of your enterprise structure for which the profit center master record is used. | Company Code:____________ |

### Mandatory and Optional Master Data

The following table gives an overview of optional and mandatory master data objects to be used in a profit center master data record.

| Master Data Object | Used in Data Segment | Mandatory / Optional | Comments |
| --- | --- | --- | --- |
| Controlling Area | Profit Center Basic Data | Mandatory | A reference controlling area can be used to create a new profit center. |
| Profit Center | Profit Center Basic Data | Mandatory | A reference profit center can be used to create a new profit center. |
| Valid From | Profit Center Basic Data | Mandatory |  |
| Valid To | Profit Center Basic Data | Mandatory |  |
| Name | Profit Center Basic Data | Mandatory |  |
| Long Text | Profit Center Basic Data | Optional |  |
| User Responsible | Profit Center Basic Data | Optional |  |
| Responsible Person | Profit Center Basic Data | Mandatory |  |
| Profit Center Group | Profit Center Basic Data | Mandatory |  |
| Department | Profit Center Basic Data | Optional |  |
| Segment | Profit Center Basic Data | Optional | If profit center is valid for a US company, we recommend to populate the segment field; this way, segment reporting can be executed. |
| Planning Template | Profit Center Basic Data | Optional |  |
| Address and Communication fields | Profit Center Address and Communication Data | All are optional |  |

### Main Parameters for Data Creation

In this section, we describe some basic parameters that influence the behavior of a master record and are always required to create a profit center master data record:

Controlling Area: A000

## Overview Table

This scope item consists of several process steps that are listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/APP | Expected Results |
| --- | --- | --- | --- |
| [Creating Profit Center Master Data](#unique_8) [page ] 7 | Divisional Accountant | Manage Profit Centers - Old Version (F3516) | A new window opens, displaying the Master Data for Profit Center screen. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Creating Profit Center Master Data

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Divisional Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Profit Centers - Old Version (F3516). | The Master Data for Profit Center screen displays. |  |
| 3 | Search for Profit Center | Search for the profit center.Choose Go. | A list of profit centers displays on the screen. |  |
| 4 | Add Profit Center | Choose Create. | The Profit Center: New screen displays. |  |
| 5 | Enter New Profit Center Data | In the New Profit Center section, enter the following data:Profit Center: <Name>, for example, YBXXXNote The maximum length is 10 characters. Do not use special characters like %, !, $, &, @, and so on. They will cause app crash and cannot be deleted.Valid From: <Valid from date>Valid To: <Valid to date>Name: <Any description>Responsible Person: <Name of the responsible person> |  |  |
| 6 | Enter Basic Data | On the Organizational Unit tab, enter the following data:Standard Hierarchy Node: <Profit center group>Segment: <Segment> |  |  |
| 7 | Company Code Assignment | Select or deselect the checkbox to assign company code(s) to the new profit center. |  |  |
| 8 | Save Your Data | Save your entries. |  |  |
| 9 | Set New Validity Period (Optional) | Choose Edit.In the profit center you have created, choose Validity Period > New Validity Period .Make entries for the Valid From and Valid To fields, and select a source data period.Choose Create.Note If the new validity period overlaps with the existing one, the overlapping time will be excluded from the current period.If there is a gap between the new validity period and other periods, the system will prevent this action. |  |  |
| 10 | Change Time-dependent Fields (Optional) | You could change the following time-dependent fields in the newly-created validity period.DepartmentPerson Resp. for PCUser ResponsibleTitleNameName 2Name 3Name 4Lock IndicatorChoose Save.Note If you modify fields that are not time-dependent, the changes will be applied across all validity periods.If there is no difference between the new period and the preceding or following period, the new period will be merged with the existing one. | A new validity period is created.The change records are displayed in the Change Log section. |  |

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
- related-to :: [[06-management-accounting/mds-bnh-607]]
- related-to :: [[06-management-accounting/mds-bnh-609]]
- related-to :: [[06-management-accounting/profitcenter-anlegen-sds-bnh-604]]
- related-to :: [[06-management-accounting/script-de-dados-mestre-criar-centro-de-lucro-mds-bnh-608]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNH_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 12,069 chars in the whole document
