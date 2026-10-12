---
id: 04-tax-and-statutory-reporting/master-data-script-create-tax-condition-2sw-275
title: "Master Data Script: Create Tax Condition (2SW) (2SW_S4CLD2608_Master_Data_EN_XX)"
description: "SAP S/4HANA Cloud 2608 master data script 2SW: creating purchasing tax condition records (MEK2) and creating/changing price conditions (MEK1/MEK2)."
cluster: 04-tax-and-statutory-reporting
tags: [kb/tax-and-statutory-reporting, topic/purchasing-tax-condition-records]
aliases: [2SW_S4CLD2608_Master_Data_EN_XX]
keywords: [Tax Condition Records and Purchasing Price Conditions, tax conditions, purchasing price conditions, change price conditions, tax codes, condition types, business roles, master data, 2SW]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2SW_S4CLD2608_Master_Data_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-275
topic: 04-tax-and-statutory-reporting/purchasing-tax-condition-records
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Master Data Script: Create Tax Condition (2SW) (2SW_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2SW_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Tax Condition Records and Purchasing Price Conditions** in Tax and Statutory Reporting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Tax Condition - MDS (2SW) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233904560)

[2 Prerequisites 3](#_Toc233904561)

[2.1 System Access 3](#_Toc233904562)

[2.2 Roles 3](#_Toc233904563)

[2.3 Mandatory and Optional Master Data 3](#_Toc233904564)

[3 Overview Table 5](#_Toc233904565)

[4 Test Procedures 6](#_Toc233904566)

[4.1 Create Tax Condition Records 6](#_Toc233904567)

[4.2 Create Price Conditions 7](#_Toc233904568)

[4.3 Change Price Conditions 9](#_Toc233904569)

## Purpose

A tax condition record contains information specific to one country/region and the different tax code for different combinations of Tax indicator for material/Tax indicator for Plant/ Tax indicator of Import.

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
| Tax Specialist | SAP_BR_TAX_SPECIALIST | Tax Rates | SAP_BR_TAX_SPECIALIST |  |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |

### Mandatory and Optional Master Data

Material master data records may refer to other master data. The following table provides an overview of optional and mandatory master data objects to be used in a material master data record.

In this section, we describe some basic parameters that influence the behavior of a master record and are always required to create a pricing condition:

Destination Country: for example, DE

| Master Data Object | Used in Data Segment | Mandatory / Optional | Comments |
| --- | --- | --- | --- |
| Destination Country | Initial Screen | Mandatory |  |

## Overview Table

This scope item consists of several process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | SAP Fiori App / Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Tax Condition Records](#unique_7) [page ] 6 | Tax Specialist | Set Tax Rates - Purchasing (MEK2) | Tax condition is set. |
| [Create Price Conditions](#unique_8) [page ] 7 | Purchaser | Create Price Conditions - Purchasing (MEK1) | Price Conditions are created. |
| [Change Price Conditions](#unique_9) [page ] 9 | Purchaser | Change Price Conditions - Purchasing (MEK2) | Price Conditions are changed. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Tax Condition Records

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Tax Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Set Tax Rates - Purchasing (MEK2). | The app opens. |  |
| 3 | Pricing Condition Type | On the Change Condition Records screen, make the following entry and press Enter:Condition Type: for example, TTX1 | The Key Combination screen displays. |  |
| 4 | Key Combination | On the Key Combination screen, choose the Taxes: Material, Plant and Origin check box and choose Choose. | The Change Non-Deductible T(TTX1): Selection screen displays. |  |
| 5 | Destination Country | On the Change Non-Deductible T(TTX1): Selection screen, make the following entry and choose Execute:Destination Country: <Country/region code> | The Change Non-Deductible Tax Condition (TTX1): Overview screen displays. |  |
| 6 | Change Tax Condition | On the Change Non-Deductible Tax Condition (TTX1): Overview screen, make the following entries:Tax ind.f.material: <Tax indicator for material>TaxIndPlnt: <Tax indicator: Plant>Import: <Import>Valid From: <Valid from>Valid To: <Valid to>Tax Code: <Tax code> | The tax condition record is maintained. |  |
| 7 | Save | Choose Save. | The tax condition record is saved. |  |
| 8 | Choose Back | Choose Back twice. |  |  |
| 9 | Pricing Condition Type | On the Change Condition Records screen, make the following entry and press Enter:Condition Type: for example, TTX1 | The Key Combination dialog box displays. |  |
| 10 | Key Combination | In the Key Combination dialog box, choose the Tax: Plant and Account Assignment Origin and Region check box and choose Choose. | The Change Non-Deductible T(TTX1) : Selection screen displays. |  |
| 11 | Destination Country | On the Change Non-Deductible T(TTX1): Selection screen, make the following entry and choose Execute:Destination Country: <Country/region code> | The Change Non-Deductible Tax Condition (TTX1): Overview screen displays. |  |
| 12 | Change Tax Condition | On the Change Non-Deductible Tax Condition (TTX1): Overview screen, make the following entries:TaxIndPlnt: <Tax indicator: Plant>Tax Ind. Acct Assgt: <Tax indicator account assignment>Import: <Import>Tax Indicator Region: <Region>Valid From: <Valid from>Valid To: <Valid to>Tax Code: <Tax code> | The tax condition record is maintained. |  |
| 13 | Save | Choose Save. | The tax condition record is saved. |  |

### Create Price Conditions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Price Conditions - Purchasing (MEK1). | The app opens. |  |
| 3 | Pricing Condition Type | Make the following entry and press Enter:Condition Type: for example, PPR0 | The Key Combination dialog box displays. |  |
| 4 | Key Combination | On the Key Combination screen, choose the Material Info Record (Plant-Specific) check box and choose Choose. | The Create Default Gross Price Condition (PPR0): Fast Entry screen displays. |  |
| 5 | Create Default Gross Condition | On the Create Default Gross Price Condition (PPR0): Fast Entry screen, make the following entries:Supplier: <Supplier>Material: <Material>Purch. Organization: <Purchasing Organization>Plant: <Plant>Infotype: for example, 0 StandardAmount: <Amount>Unit: <Pricing Unit>Per: <Per quantity>Uom: <Unit>Valid from: <Valid from>Vailid to: <Valid to> | The default gross condition record is maintained. |  |
| 6 | Save | Choose Save. | The condition record is saved. |  |

### Change Price Conditions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Change Price Conditions - Purchasing (MEK2). | The app opens. |  |
| 3 | Pricing Condition Type | Make the following entry and press Enter:Condition Type: for example, PPR0 | The Key Combination screen displays. |  |
| 4 | Key Combination | On the Key Combination screen, choose the Material Info Record (Plant-Specific) check box and choose Choose. | The Create Default Gross Price Condition (PPR0): Fast Entry screen displays. |  |
| 5 | Change Default Gross Condition | On the Change Default Gross Price Condition (PPR0): Fast Entry screen, make the following entries:Supplier: <Supplier>Material: <Material>Purch. Organization: <Purchasing Organization>Plant: <Plant>Infotype: for example, 0 StandardChoose Execute.Make the following entry:Amount: <Amount> | The default gross condition record is changed. |  |
| 6 | Save | Choose Save. | The condition record is saved. |  |

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
- related-to :: [[04-tax-and-statutory-reporting/crear-condicion-para-determinacion-de-impuestos-mds-2sw-276]]
- related-to :: [[04-tax-and-statutory-reporting/mds-2sw-277]]
- related-to :: [[04-tax-and-statutory-reporting/mds-2sw-279]]
- related-to :: [[04-tax-and-statutory-reporting/objetivo-script-de-dados-mestre-criar-condicao-de-imposto-mds-2sw-port]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2SW_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 12,585 chars in the whole document
