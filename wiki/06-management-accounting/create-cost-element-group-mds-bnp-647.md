---
id: 06-management-accounting/create-cost-element-group-mds-bnp-647
title: Create Cost Element Group - MDS (BNP) (BNP_S4CLD2608_Master_Data_EN_XX)
description: SAP S/4HANA Cloud Public Edition master data script (EN) for creating cost element groups via Manage Cost Element Groups (F5373) as Cost Accountant - Overhead.
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/cost-element-groups]
aliases: [BNP_S4CLD2608_Master_Data_EN_XX]
keywords: [Cost Element Groups, master data script, cost accounting roles, controlling area, fiori launchpad access, chart of accounts, BNP]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNP_S4CLD2608_Master_Data_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-647
topic: 06-management-accounting/cost-element-groups
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Create Cost Element Group - MDS (BNP) (BNP_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNP_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Cost Element Groups** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Cost Element Group - MDS (BNP) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233904978)

[2 Prerequisites 3](#_Toc233904979)

[2.1 System Access 3](#_Toc233904980)

[2.2 Roles 3](#_Toc233904981)

[2.3 Required Organizational Units 3](#_Toc233904982)

[2.4 Mandatory and Optional Master Data 4](#_Toc233904983)

[2.5 Main Parameters for Data Creation 4](#_Toc233904984)

[3 Overview Table 5](#_Toc233904985)

[4 Test Procedures 6](#_Toc233904986)

[4.1 Creating Cost Element Group Master Data 6](#_Toc233904987)

## Purpose

Business Context

Cost element groups are typically used to collect cost elements with similar characteristics for purposes of reporting. Cost element groups can be used in the information system, for example. You can use the cost element group structure to define the row structure of your reports. Totals are calculated in the report for each node.

You can also use cost element groups whenever you want to process several cost elements in one transaction. For example, in cost center planning, distribution or assessment.

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
| Cost Accountant - Overhead | SAP_BR_OVERHEAD_ACCOUNTANT | Overhead Accounting | SAP_BR_OVERHEAD_ACCOUNTANT |  |

### Required Organizational Units

The organizational structure and master data of your company was created in your ERP system during implementation. The organizational structure reflects the structure of your company. The master data represents cost element groups, depending on the operational focus of your company.

| Data Object | Used in Data Segment | Mandatory / Optional | Comments |
| --- | --- | --- | --- |
| Controlling Area | General Data | Mandatory |  |

### Mandatory and Optional Master Data

Cost element group master data records may refer to other master data. The following table gives an overview of optional and mandatory master data objects to be used in a cost element group data record.

| Master Data Object | Used in Data Segment | Mandatory / Optional | Comments |
| --- | --- | --- | --- |
| Chart of accounts | Organizational Units | Optional |  |

### Main Parameters for Data Creation

This scope item has no business conditions.

## Overview Table

This scope item consists of several process steps that are listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Creating Cost Element Group Master Data](#unique_9) [page ] 6 | Cost Accountant - Overhead | Manage Cost Element Groups (F5373) | Cost element groups can be created according to new business requirements. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Creating Cost Element Group Master Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

You have entered and saved the basic data for the Material.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Cost Element Groups (F5373). | The app opens. |  |
| 3 | Enter New Cost Element Group | On the Manage Cost Element Groups screen, choose Create. On the Create Cost Element Group: Initial Screen, make the following entry:Cost Element Group: <Cost Element Group>Press Enter.Optionally, you can choose a reference from the existing Cost Center Groups. | The Create Cost Element Group: Structure screen displays. |  |
| 4 | Enter Cost Element and/or Cost Element Group | New master data displays on the Cost Element Group: Structure screen. Make the following entry:Description: <Description>Furthermore, you can make the following entries by placing your cursor on your selection and make use of the following navigation buttons:Lower Level : <Insert a Cost Element Group on the lower level>Cost Element: <(Insert option) - Add Cost Elements or Element Ranges>Same Level: <Insert additional Cost Element Groups on the same lower level> | New master data displays on the Cost Element Group: Structure screen. |  |
| 5 | Save Your Data | Choose Save. | The Cost Element Group is created and saved. |  |

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
- related-to :: [[06-management-accounting/criar-grupo-de-classes-de-custo-mds-bnp-650]]
- related-to :: [[06-management-accounting/kostenartengruppe-anlegen-sds-bnp-646]]
- related-to :: [[06-management-accounting/mds-bnp-649]]
- related-to :: [[06-management-accounting/mds-bnp-651]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNP_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 8,911 chars in the whole document
