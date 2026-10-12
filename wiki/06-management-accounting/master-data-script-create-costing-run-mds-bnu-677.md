---
id: 06-management-accounting/master-data-script-create-costing-run-mds-bnu-677
title: Master Data Script - Create Costing Run – MDS (BNU) (BNU_S4CLD2608_Master_Data_EN_XX)
description: "English master data script (BNU) for SAP S/4HANA Cloud Public Edition: creating and executing a product costing run with app F1865 as logistics test prerequisite."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/product-costing-and-standard-cost-updates]
aliases: [BNU_S4CLD2608_Master_Data_EN_XX]
keywords: [Product Costing Runs and Standard Cost Updates, costing run, product cost planning, cost estimates, master data scripts, costing variant, business roles, organizational units, price update, BNU]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNU_S4CLD2608_Master_Data_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-677
topic: 06-management-accounting/product-costing-and-standard-cost-updates
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Master Data Script - Create Costing Run – MDS (BNU) (BNU_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNU_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Product Costing Runs and Standard Cost Updates** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Costing Run - MDS (BNU) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233905033)

[2 Prerequisites 3](#_Toc233905034)

[2.1 System Access 3](#_Toc233905035)

[2.2 Roles 3](#_Toc233905036)

[2.3 Required Organizational Units 3](#_Toc233905037)

[2.4 Mandatory and Optional Master Data 4](#_Toc233905038)

[2.5 Main Parameters for Data Creation 4](#_Toc233905039)

[2.5.1 Costing Variant 4](#_Toc233905040)

[3 Overview Table 5](#_Toc233905041)

[4 Test Procedures 6](#_Toc233905042)

[4.1 Create Costing Run 6](#_Toc233905043)

[4.2 Execute Costing Run 7](#_Toc233905044)

## Purpose

This document contains process steps that have to be done as prerequisite before you can start to work through the standard test scripts of selected logistics scenarios.

In this document, you find a description of how to create and execute a product costing run for materials used in your company / plant. The purpose is to plan costs for materials without reference to orders, and set prices for materials and other cost accounting objects.

You can use Product Cost Planning to analyze the costs of your company’s products such as:

- Manufactured materials
- Services
- Other intangible goods

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
| Cost Accountant - Inventory | SAP_BR_INVENTORY_ACCOUNTANT | Inventory Accounting | SAP_BR_INVENTORY_ACCOUNTANT |  |

### Required Organizational Units

To create a costing run, you need to specify the Controlling Area and the Company Code.

|  |
| --- |
| Note In the Organizational Unit to be Used column, enter your value for the data segment which is relevant for your system environment.For company code : for example,10 = Germany ,17 = US |

| Data Segment | Depends On | Field Examples | Comments | Organizational Unit to be Used |
| --- | --- | --- | --- | --- |
| Costing Data | Controlling Area |  |  | Controlling Area:____________ |
|  | Company Code |  |  | Company Code:__________ |
| Selection | Plant |  |  | Plant:__________ |

### Mandatory and Optional Master Data

BOM data records may refer to other master data. The following table gives an overview of optional and mandatory master data objects that are to be used in a BOM.

| Master Data Object | Used in Data Segment | Mandatory / Optional | Comments |
| --- | --- | --- | --- |
| Materials | Create Cost Estimate > Flow Step > Selection | Mandatory | Usually, you specify the material types to indicate for which materials the costing run shall create a product costing. |
| Production Master Data (BOM, Routing, Work Center, and so on). | In the Create Cost Estimate--> Flow Step --> Structure Explosion | Optional (or) Mandatory | In case manufactured products are used in the costing run (for example,products of material type "FERT" (Finished Goods) or "HALB" (Semi-Finished Goods), these products have a bill of material which is "exploded" in the costing run.At the same time the routing(s) is/are selected.Additional data from work centers,assigned cost centers and used activity types, along with cost rates are determined for calculating the final costing data. |

### Main Parameters for Data Creation

In this section, we describe some basic parameters that influence the behavior of a master record and are always required to create a bill of material:

#### Costing Variant

Costing Variant defines a link between the application and Customizing, since all cost estimates are carried out and saved with reference to a costing variant.

| Costing Variant | Description | Comment |
| --- | --- | --- |
| PYC1 | Cost Estimate Standard | This Costing Variant is used to create standard product cost estimates for the selected materials. Based on the result, the material valuation data will be updated. |

## Overview Table

This scope item consists of several process steps that are listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Create Costing Run](#unique_10) [page ] 6 | Cost Accountant - Inventory | Manage Costing Runs - Estimated Costs (F1865) | Header data with costing data tab is displayed. |
| [Execute Costing Run](#unique_11) [page ] 7 | Cost Accountant - Inventory | Manage Costing Runs - Estimated Costs (F1865) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Costing Run

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a costing run.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Cost Accountant - Inventory. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Costing Runs - Estimated Costs (F1865). | The Manage Costing Runs Estimated Costs view displays. |  |
| 3 | Creating Costing Run | Choose Create. | The Create New Costing Run view displays. |  |
| 4 | Enter Parameters for Costing Run | Make the following entries and press Enter.Costing Run: Test1Costing Run Date: <Enter the current date>Description: Costing Run Test1Costing Variant: PYC1Costing Version: 1Controlling Area: A000Company Code: 1010Costing Date From: <Current date>Costing Date To: Adopt default valueQty Structure Date: <Current date>Valuation Date: <Current date> |  |  |
| 5 | Save Costing Run | Choose Save. |  |  |

### Execute Costing Run

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you execute the costing run. Configured materials are not included.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Inventory. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Costing Runs - Estimated Costs (F1865). | The Manage Costing Runs Estimated Costs view displays. |  |
| 3 | Select Costing Run | Search for the costing run created in the previous step and click on the entry and select Edit to access the details of the costing run. |  |  |
| 4 | Open Costing Run | Make the following entry:Costing Run: Enter the costing run created in the previous step and choose Enter.Expand the Processing section. |  |  |
| 5 | Create Cost Estimates | In the Processing table, for each row, there is a Change Parameter button in the Parameters column. Choose the one in the selection row and make the following entries:Material Type : HALB, ROH, FERTPlant: 1010Deselect Background Processingand select option EXPLO.Save your entries and choose Back.Choose Execute, which displays in the Execute column, and the status light for the Selection row turns green. | The selection is executed. |  |
| 6 | Create Cost Estimates | For the Costing row, choose the Change Parameter button. On the Costing Run: Cost Estimate - Change Parameters, deselect Background Processing indicator and then choose Save.Choose BackChoose Execute, which displays in the Execute column and the status light for the Costing row turns green. | Costing Run is executed. |  |
| 7 | Create Cost Estimates | From the menu, choose Edit > Costing Results.If the status light for this row is red, review the Costing levels report. Correct errors in the report. To re-run the costing (if necessary), repeat steps for Struct. Explosion and Costing Rows. | Costing Run is executed. |  |
| 8 | Create Cost Estimates | On the Analysis row, choose the Change Parameter button. Select SAP&11 for the parameter setting. On the Costing Run: Analysis - Change Parameters, deselect Background Processing indicator and then choose Save.Choose Back.Choose Execute, which displays in the Execute column. | Costing Run is executed. |  |
| 9 | Create Cost Estimates | On the Marking row, choose the Lock button.On the Price Update: Organizational Measure screen, select the Company Code: 1010.In the dialog box that appears, enter the costing variant of PYC1 and the costing version of 1, and then choose Enter. The status light of the row turns green.Choose Back.Choose Change Parameter and deselect Background Processing.Choose Save.Choose Back, and choose Execute. | Costing Run is executed. |  |
| 10 | Create Cost Estimates | On the Release row, choose Change Parameter and deselect Test Run and Background Processing.Choose Save.Choose Back, and choose Execute. | The current prices will be updated in the material master data. |  |

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
- related-to :: [[06-management-accounting/crear-ejecucion-del-calculo-del-coste-mds-bnu-678]]
- related-to :: [[06-management-accounting/criar-execucao-de-calculo-de-custos-mds-bnu-680]]
- related-to :: [[06-management-accounting/kalkulationslauf-anlegen-sds-bnu-676]]
- related-to :: [[06-management-accounting/mds-bnu-679]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNU_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 13,415 chars in the whole document
