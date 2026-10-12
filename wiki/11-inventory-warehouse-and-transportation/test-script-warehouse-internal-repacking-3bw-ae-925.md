---
id: 11-inventory-warehouse-and-transportation/test-script-warehouse-internal-repacking-3bw-ae-925
title: "Test Script: Warehouse Internal Repacking (3BW_AE) (3BW_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script (19-06-26) for warehouse internal repacking (3BW_AE): repack, pack and unpack handling units with Pack Warehouse Stock (F3738)."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/ewm-repacking]
aliases: [3BW_S4CLD2608_BPD_EN_AE]
keywords: [Warehouse Internal Repacking, warehouse repacking, handling units, pack product into handling unit, unpack handling unit, favorite packaging materials, warehouse default values, access codes, business roles, business conditions]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3BW_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-925
topic: 11-inventory-warehouse-and-transportation/ewm-repacking
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Warehouse Internal Repacking (3BW_AE) (3BW_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3BW_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Warehouse Internal Repacking** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Warehouse Internal Repacking (3BW_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232852279)

[2 Prerequisites 3](#_Toc232852280)

[2.1 System Access 3](#_Toc232852281)

[2.2 Roles 3](#_Toc232852282)

[2.3 Master Data, Organizational Data, and Other Data 3](#_Toc232852283)

[2.4 Business Conditions 5](#_Toc232852284)

[2.5 Preliminary Steps 5](#_Toc232852285)

[2.5.1 Define Default Values for Warehouse Operative (WM) 5](#_Toc232852286)

[2.5.2 Define Favorite Packaging Materials 6](#_Toc232852287)

[3 Overview Table 8](#_Toc232852288)

[4 Test Procedures 9](#_Toc232852289)

[4.1 Repacking Handling Unit 9](#_Toc232852290)

[4.2 Pack Product into Handling Unit 10](#_Toc232852291)

[4.3 Unpack Handling Unit 11](#_Toc232852292)

[4.4 Appendix 13](#_Toc232852293)

[4.4.1 Access Code Handling 13](#_Toc232852294)

[4.4.2 Process Integration 13](#_Toc232852295)

[4.4.2.1 Preceding Processes 13](#_Toc232852296)

## Purpose

Overview

With this process, you can repack stock in your warehouse. The repacking process is executed in the clarification zone. Before starting the repacking process, you can create ad hoc warehouse tasks to move the products / handling units to be repacked to the clarification zone. At the end of the process, you move the repacked products / handling units to the final bin. There are different use cases for repacking:

• Pack stock into a handling unit

• Repack stock from one handling unit into another handling unit

• Unpack stock from one handling unit onto the bin

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

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
| Warehouse Clerk (EWM) | SAP_BR_WAREHOUSE_CLERK_EWM | Warehouse Office | SAP_BR_WAREHOUSE_CLERK_EWM |  |
| Warehouse Operative (EWM) | SAP_BR_WAREHOUSE_OPERATIVE_EWM | Warehouse Floor | SAP_BR_WAREHOUSE_OPERATIVE_EWM |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | TG0011 | Trading Good 0011,PD,Regular Proc. | General Storage |
| Material | TG0013 | Trading Good 0013,PD,Regular Proc. | General Storage |
| Packaging Material | PMPALLET | Pallet |  |
| Packaging Material | PMPALLET_GTL | Pallet for GTL |  |
| Plant | 3310 |  |  |
| Storage Location | 335W |  |  |

Organizational Master Data in Warehouse:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Warehouse | 3350 |  |  |
| Custodian | 33413310 |  |  |
| Entitled to Dispose | 33413310 |  |  |

Warehouse-Specific Master Data:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Storage Type | SG01 | General Storage |  |
| Storage Type | S970 | Clarification Zone |  |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

| MDS | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| 3KQ | Maintain Warehouse Products Attributes - MDS |
| 3KR | Maintain Storage Bins and Fixed Bin Assignments - MDS |

### Business Conditions

Before you test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the procedure described in the Create New Open MM Posting Period - MDS (BNZ) master data script. The posting period is up to date. |
| 3BR - Warehouse Inbound Processing | You have completed the procedure described in the Warehouse Inbound Processing (3BR) test script. You have the warehouse stock for internal repack. To have the Handling Unit for repacking, make sure you excute the step Create Handling Unit (Optional) before Post Goods Receipt in the Warehouse Inbound Processing (3BR). |
| 5HN - Warehouse Inbound Processing with Synchronous Goods Receipt | Alternatively to scope item Warehouse Inbound Processing (3BR), you can follow the procedure described in Warehouse Inbound Processing with Synchronous Goods Receipt (5HN) test script.You have the warehouse stock for TG0011 or TG0013 in storage bin SG01-GENERAL for internal repack. To have the Handling Unit for repacking, make sure you excute the step Create Handling Unit (Optional) during the Post Goods Receipt or you execute the step Create HU Putaway Warehouse Tasks (Optional) in the Warehouse Inbound Processing with Synchronous Goods Receipt. |

### Preliminary Steps

#### Define Default Values for Warehouse Operative (WM)

Purpose

In this step, you can define the default warehouse number for the Warehouse Operative (EWM).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Operative (EWM). | The Fiori launchpad is displayed. |  |
| 2 | Choose Avatar | Choose your avatar.Then, choose Settings. |  |  |
| 3 | Enter Default Value | Choose Default Values.In the Material Management section, enter the following data:Warehouse Number: 3350.Choose Save. |  |  |

#### Define Favorite Packaging Materials

Purpose

In this step, you define the favorite packaging material to be used in the app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk (EWM). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Define Favorite Packaging Materials (/SCWM/TWSPACKMAT). | The Define Favorite Packaging Materials (/SCWM/TWSPACKMAT) screen is displayed. |  |
| 3 | Enter Warehouse Number | The first time a dialog box displays Determine Work Area: Entry, enter the following data:Warehouse Number: 3350Choose Continue. |  |  |
| 4 | Switch Mode | Choose Edit in the top right corner. | The screen name changes to Change View “Define Favorite Packaging Materials”: Overview. |  |
| 5 | Choose New Entries | Once you have switched the mode, you are able to see different options.Choose New Entries. | You can now edit the gray fields for your required packaging materials. |  |
| 6 | Enter Data | Enter the following data:Work Center: PackProduct: PMPALLETDefault: XSequence: 1Choose Save. | A system message tells you that the data was saved. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Repacking Handling Unit](#unique_10) [page ] 9 | Warehouse Operative (EWM) | Pack Warehouse Stock (F3738) | You have repacked the handling unit. |
| [Pack Product into Handling Unit](#unique_11) [page ] 10 | Warehouse Operative (EWM) | Pack Warehouse Stock (F3738) | You have packed the product into the handling unit. |
| [Unpack Handling Unit](#unique_12) [page ] 11 | Warehouse Operative (EWM) | Pack Warehouse Stock (F3738) | You have unpacked the handling unit. |

## Test Procedures

### Repacking Handling Unit

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Operative (EWM) repacks the handling unit (HU) to another handling unit.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Operative (EWM). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Pack Warehouse Stock (F3738). |  |  |
| 3 | Enter Data | Make the following entries:Work Center: PACKStorage Bin: SG01-GENERALChoose Enter.Choose Start Packing. |  |  |
| 4 | Enter Data | Make the following entries:Handling Unit/Storage Bin: <enter handling unit in the storage bin>Product /Access Code: <enter the product number in the handling unit>Choose Enter. |  |  |
| 5 | Enter Data to Create HU | Select one of the favorite packaging materials or select other packaging material in the Other Packaging Materials field.Enter the target handling unit number or leave it blank to let the system propose automatically.Choose Create. | The destination HU is created and displayed on the right-hand side of the screen. |  |
| 6 | Choose Items | Choose the product and choose Pack.Note If you want to pack all the items, you can choose Pack All. If you want to pack a partial quantity of the product, you can choose Partially Pack. |  |  |
| 7 | Close HU | The selected products are displayed on the right-hand side.If you want to print the HU, choose Print.Choose Close. |  |  |

### Pack Product into Handling Unit

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Operative (EWM) packs the loose product into a handling unit (HU).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Operative (EWM). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Pack Warehouse Stock (F3738). |  |  |
| 3 | Enter Data | Make the following entries:Work Center: PACKStorage Bin: SG01-GENERALChoose Enter.Choose Start Packing. |  |  |
| 4 | Enter Data | Make the following entries:Handling Unit/Storage Bin: <Enter the Storage Bin where product stock exists>Product/Access Code:Choose Enter. | The products in the HU or the storage bin are displayed. |  |
| 5 | Enter Data to Create HU | Select one of the favorite packaging materials or select other packaging material in the Other Packaging Materials field.Enter the target handling unit number or leave it blank to let the system propose automatically.Choose Create. | The destination HU is created and displayed on the right-hand side of the screen. |  |
| 6 | Choose Items | Choose the product and choose Pack.Note If you want to pack all the items, you can choose Pack All. If you want to pack a partial quantity of the product, you can choose Partially Pack. |  |  |
| 7 | Close HU | The selected products are displayed on the right-hand side.If you want to print the HU, choose Print.Choose Close. |  |  |

### Unpack Handling Unit

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Operative (EWM) unpacks the handling unit (HU). The original HU is deleted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Operative (EWM). |  |  |
| 2 | Access App | Open Pack Warehouse Stock (F3738). |  |  |
| 3 | Enter Data | Make the following entries:Work Center: PACKStorage Bin: SG01-GENERALChoose Enter.Choose Start Packing. |  |  |
| 4 | Enter Data | Make the following entries:Handling Unit: <enter the HU for which you want to do the unpacking>Note The field is on the right-hand side of the screen.Handling Unit/Storage Bin: <enter the Storage Bin where you want the unpacked product to be stored>Choose Enter. | The products in the HU or the storage bin are displayed. |  |
| 5 | Choose Unpack | Select the products and choose Unpack. |  |  |

### Appendix

#### Access Code Handling

You can enter or scan external access codes in field Product/Access code during the packing process via the Pack Warehouse Stock (F3738) app. The system triggers the mapped internal access codes in the back end to perform actions.

The following external access codes are currently supported:

| External Access Code | Function |
| --- | --- |
| S_CLOSE_HU | Close HU |
| S_CREATE_HU | Create HU |
| S_PACK_ALL | Pack all product items |
| S_PACK_ITEM | Pack one product item |

#### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

##### Preceding Processes

You may first have completed the following processes and conditions before you start with the test steps.

| Scope Item ID | Business Condition |
| --- | --- |
| 3BR - Warehouse Inbound Processing | You have completed the procedure described in the Warehouse Inbound Processing (3BR) test script. You have the warehouse stock for TG0011 or TG0013 in storage bin SG01-GENERAL for internal repack. To have the Handling Unit for repacking, make sure you excute the step Create Handling Unit (Optional) before Post Goods Receipt in the Warehouse Inbound Processing (3BR). |
| 5HN - Warehouse Inbound Processing with Synchronous Goods Receipt | Alternatively to scope item 3BR - Warehouse Inbound Processing, you can follow the procedure described in Warehouse Inbound Processing with Synchronous Goods Receipt (5HN) test script.You have the warehouse stock for TG0011 or TG0013 in storage bin SG01-GENERAL for internal repack. To have the Handling Unit for repacking, make sure you excute the step Create Handling Unit (Optional) during the Post Goods Receipt or you execute the step Create HU Putaway Warehouse Tasks (Optional) in the Warehouse Inbound Processing with Synchronous Goods Receipt (5HN). |

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
- see-also :: [[02-business-partner-and-product-master-data/stammdatenskript-produktstamm-vom-typ-verpackung-anlegen-sds-3y1-388]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3BW_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 20,252 chars in the whole document
