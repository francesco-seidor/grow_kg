---
id: 11-inventory-warehouse-and-transportation/create-new-open-mm-posting-period-mds-bnz-695
title: Create New Open MM Posting Period - MDS (BNZ) (BNZ_S4CLD2608_Master_Data_EN_XX)
description: SAP S/4HANA Cloud Public Edition 2608 master data script for closing the MM period and opening a new posting period via Close Periods (MMPV).
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/mm-posting-periods]
aliases: [BNZ_S4CLD2608_Master_Data_EN_XX]
keywords: [MM Posting Periods, mm posting period, period closing, material stock valuation, back posting, business roles, master data scripts, BNZ]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNZ_S4CLD2608_Master_Data_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-695
topic: 11-inventory-warehouse-and-transportation/mm-posting-periods
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Create New Open MM Posting Period - MDS (BNZ) (BNZ_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNZ_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **MM Posting Periods** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create New Open MM Posting Period - MDS (BNZ) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233905050)

[2 Prerequisites 3](#_Toc233905051)

[2.1 System Access 3](#_Toc233905052)

[2.2 Roles 3](#_Toc233905053)

[3 Overview Table 4](#_Toc233905054)

[4 Test Procedures 5](#_Toc233905055)

[4.1 Closing MM Period and Opening New Posting Period 5](#_Toc233905056)

## Purpose

Information on material stock and certain valuation data such as total stock value, total stock, evaluation elements class, price control indicator, and price unit are held by financial posting period. The period must be set up at the beginning of each new posting period to ensure values and goods movement are posted to the correct period. Usually, only the current posting period is open for posting. All other posting periods are closed.

A back posting to a previous period is only possible if the corresponding flag is set in the control record. This flag is automatically set at initialization and after each period change. In certain cases, however, it may be necessary to set the indicator manually.

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

## Overview Table

This scope item consists of several process steps that are listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Closing MM Period and Opening New Posting Period](#unique_6) [page ] 5 | Master Data Specialist - Product Data | Close Periods (MMPV) | The posting period is up to date. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Closing MM Period and Opening New Posting Period

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Close Periods (MMPV).Note If you cannot find the Close Periods tile, from the dropdown list on the upper right part of the Fiori launchpad, choose Tile Catalog. Under the Master Data - Administration group, navigate to the Close Periods tile and add it to the My Home group. | The app opens. |  |
| 3 | Enter Selection Data | On the Close Period for Material Master Records screen, make the following entries:From Company Code: <Your company code>To Company Code: <Your company code>Period: <Period to open>Fiscal year: <Current fiscal year>Check and close period: SelectedNote In the Period field, enter a two-digit number for the month. For example, January equals to 01, October equals to 10, and so on.If you want to open the current period, enter the current month in the next periods. |  |  |
| 4 | Choose Execute | On the Close Period for Material Master Records screen, choose Execute. |  |  |
| 5 | Check Result | If a log displays that The current period (month/year) of the control record is <period/year you have entered>, you can stop here.Note If the posting period is still in the past, repeat the above steps period by period until you reach the correct (current) one. For example, the period displayed is 04 2014, but you want to open the 12 2015 period, you cannot do this directly. Instead, you need to open the 05 2014 period next, and then 06 2014, etc. until you reach the current period. If you want to close inventory periods in the past year, there might be a system message displayed in Step 3 indicating that you are opening / closing a period in the past year. You need to confirm this system message. | The posting period is up to date. |  |

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
- related-to :: [[11-inventory-warehouse-and-transportation/crear-nuevo-periodo-contable-mm-abierto-mds-bnz-696]]
- related-to :: [[11-inventory-warehouse-and-transportation/criar-periodo-contabil-mm-aberto-mds-bnz-698]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-bnz-699]]
- related-to :: [[11-inventory-warehouse-and-transportation/mm-mds-bnz-697]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNZ_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 8,527 chars in the whole document
