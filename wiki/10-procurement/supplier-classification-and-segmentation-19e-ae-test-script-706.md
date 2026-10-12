---
id: 10-procurement/supplier-classification-and-segmentation-19e-ae-test-script-706
title: Supplier Classification and Segmentation (19E_AE) – Test Script (19E_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition test script for scope item 19E_AE: creating and managing purchasing categories in app F0337 as Purchaser."
cluster: 10-procurement
tags: [kb/procurement, topic/purchasing-categories]
aliases: [19E_S4CLD2608_BPD_EN_AE]
keywords: [Supplier Classification and Purchasing Categories, purchasing categories, supplier classification, supplier segmentation, planned spend, material groups, test scripts, business roles, demo data, 19E]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/19E_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-706
topic: 10-procurement/purchasing-categories
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Supplier Classification and Segmentation (19E_AE) – Test Script (19E_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/19E_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Supplier Classification and Purchasing Categories** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Supplier Classification and Segmentation (19E_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232846443)

[2 Prerequisites 3](#_Toc232846444)

[2.1 System Access 3](#_Toc232846445)

[2.2 Roles 3](#_Toc232846446)

[2.3 Master Data, Organizational Data, and Other Data 3](#_Toc232846447)

[3 Overview Table 5](#_Toc232846448)

[4 Test Procedures 6](#_Toc232846449)

[4.1 Create Purchasing Categories 6](#_Toc232846450)

[4.2 Manage Purchasing Categories 7](#_Toc232846451)

## Purpose

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
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Supplier | 33300001 |  |  |
| Material Group | L001 |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNE | Create Supplier Master - MDS |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Create Purchasing Categories](#unique_7) [page ] 6 | Purchaser | Manage Purchasing Categories (F0337) | Purchasing category is created. |
| [Manage Purchasing Categories](#unique_8) [page ] 7 | Purchaser | Manage Purchasing Categories (F0337) | Purchasing category is maintained, including assigning Suppliers, Team Employees and Material Groups to it. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Purchasing Categories

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, a purchasing category is created and a purchaser responsible for the purchasing category is assigned. Suppliers, team employees, and material groups are also assigned to it.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Logon to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Purchasing Categories (F0337) . | The Manage Purchasing Categories screen displays. |  |
| 3 | Create Purchasing Category | Choose Create. | The Purchasing Category: New screen displays. |  |
| 4 | Enter Purchasing Category data | In the General section, make the following entries:Name : <enter a name for the purchasing category, e.g. Test_PurchasingCategory>Purchaser Responsible : <Enter a Purchaser> (leave it as default value)Choose Enter. | All data is entered, no error or warning messages exist. |  |
| 5 | Assign Suppliers | In the Suppliers section, choose Add Line, and enter following data :ID: 33300001.Choose Enter. | The assignment of suppliers to the purchasing category is done. |  |
| 6 | Assign Team Employees | In the Team section, Choose Add Employee,In the search help Add Employee, choose Go.In the search result list, select an employee and choose OK. | The assignment of team members to the purchasing category is done.Check that the Role is Member. |  |
| 7 | Add Purchasing Category Description and Languages | In the Languages for Purchasing Category Description section, make the following entries:Purchasing Category Description : <enter a description of the purchasing category, e.g. Test_PurchasingCategory>Choose Add Language, enter following data:Language: Choose a language for translation from the dropdown listStatus of Translation: To Be TranslatedChoose Enter. | The assignment of description and available languages of the purchasing category is done. |  |
| 8 | Assign Material Groups | In the Material Groups section, choose Add Material Groups and enter following data in the dialogue box :Material Group ID: L001Choose GO button.In the search resulst list select the entry of L001 and choose OK. | The material group is assigned to the purchasing category. |  |
| 9 | Save Purchasing Category | Choose Save. | A new Purchasing Category is created.A messageData saved successfullydisplays. |  |

Result

The system generates a purchasing category.

### Manage Purchasing Categories

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity displays and edits the purchasing category created in the previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Logon to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Purchasing Categories (F0337) . | The Manage Purchasing Categories (Original) screen displays. |  |
| 3 | Search Purchasing Category | In the Search field, enter a part of the purchasing category name entered in test step 4 of [Create Purchasing Categories](#unique_7) [page ] 6.Choose Go. | The search result list is displayed. |  |
| 4 | Display Purchasing Category | Click on e.g. name of the requested Purchasing Category.On the screen Purchasing Category, check the details of the purchasing category. | The Purchasing Category screen displays.The details of the purchasing category is displayed correctly. |  |
| 5 | Edit Purchasing Category | Choose Back.On the search result list, select the requested purchasing category by choosing the radio button.Choose Edit. | The screen Purchasing Category: <name of purchasing category> displays. |  |
| 6 | Add Planned Spend | On section Planned Spend, choose Add Line and enter following data:From: <select a start date>To: <select an end date>Amount: For example, 10Currency: AEDChoose Save. | The purchasing category is changed and saved. |  |

Result

The Purchasing Category displays and changes.

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
- see-also :: [[10-procurement/test-script-vendor-performance-consumer-products-6a6-ae-1154]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/19E_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 12,986 chars in the whole document
