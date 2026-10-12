---
id: 09-subscription-billing-and-contract-accounting/master-data-script-create-service-type-based-pricing-condition-mds-3gd
title: Master Data Script - Create Service Type Based Pricing Condition - MDS (3GD) (3GD_S4CLD2608_Master_Data_EN_XX)
description: "Master data script (3GD) for creating service-type-based pricing conditions PST0, PST1, PST2 via Set Material Prices - Sales (VK12) for Convergent Invoicing rating."
cluster: 09-subscription-billing-and-contract-accounting
tags: [kb/subscription-billing-and-contract-accounting, topic/consumption-items-and-rating]
aliases: [3GD_S4CLD2608_Master_Data_EN_XX]
keywords: [Consumption Items and Service-Type-Based Rating, pricing conditions, service type based pricing, master data scripts, condition types, convergent invoicing, business roles, sales organization, 3GD]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3GD_S4CLD2608_Master_Data_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-317
topic: 09-subscription-billing-and-contract-accounting/consumption-items-and-rating
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Master Data Script - Create Service Type Based Pricing Condition - MDS (3GD) (3GD_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3GD_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Consumption Items and Service-Type-Based Rating** in Subscription Billing and Contract Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Service Type Based Pricing Condition - MDS (3GD) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233904606)

[2 Prerequisites 3](#_Toc233904607)

[2.1 System Access 3](#_Toc233904608)

[2.2 Roles 3](#_Toc233904609)

[2.3 Mandatory and Optional Master Data 3](#_Toc233904610)

[3 Overview Table 4](#_Toc233904611)

[4 Test Procedures 5](#_Toc233904612)

[4.1 Create Pricing Condition of PST0 5](#_Toc233904613)

[4.2 Create Pricing Condition of PST1 6](#_Toc233904614)

[4.3 Create Pricing Condition of PST2 7](#_Toc233904615)

## Purpose

Service-based pricing conditions are used to store the information required to undertake automatic pricing in rating of Convergent Invoicing. They include prices and surcharges based on the different variants. They may be specific to a particular customer or material or a combination of parameters. A service-based pricing condition holds information such as a price in a specific currency for a material. This information is used and stored in the billable items, billing plan items, billing documents and invoicing documents.

The information is generally specific to a particular sales unit within your organization.

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

| System | Details |
| --- | --- |
| System | Accessible via SAP Fiori Launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) |
| --- | --- | --- | --- |
| Pricing Specialist | SAP_BR_PRICING_SPECIALIST | Price Management | SAP_BR_PRICING_SPECIALIST |

### Mandatory and Optional Master Data

Master data records may refer to other master data. The following table gives an overview of optional and mandatory master data objects to be used in a master data record.

| Master Data Object | Used in Data Segment | Mandatory / Optional | Comments |
| --- | --- | --- | --- |
| Sales Organization | Initial Screen | Mandatory | <Sales Organization number> |
| Distribution Channel | Initial Screen | Mandatory | <Distribution Channel number> |

## Overview Table

This master record consists of several segments provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Segment | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Pricing Condition of PST0](#unique_7) [page ] 5 | Pricing Specialist | Set Material Prices - Sales (VK12) | Material pricing condition is maintained. |
| [Create Pricing Condition of PST1](#unique_8) [page ] 6 | Pricing Specialist | Set Material Prices - Sales (VK12) | Material pricing condition is maintained. |
| [Create Pricing Condition of PST2](#unique_9) [page ] 7 | Pricing Specialist | Set Material Prices - Sales (VK12) | Material pricing condition is maintained. |

## Test Procedures

This section describes procedures for each segment or process step that is part of this master record.

### Create Pricing Condition of PST0

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes creating sales pricing condition: PST0

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Pricing Specialist. | The Start page appears. |  |
| 2 | Access the SAP Fiori App | Open Set Material Prices - Sales (VK12). | The Change Condition Records screen displays. |  |
| 3 | Pricing Condition Type | In the Change Condition Records view, make the following entries as below and choose Enter.Condition Type: PST0 |  |  |
| 4 | Selection | In the Change SrvcTyp-Bsd Prc Condition (PST0): Selection view, make the following entries as below and choose Execute.Sales Organization: <Sales Organization>Distribution Channel: <Distribution Channel> |  |  |
| 5 | Change Price Condition | In the Change SrvcTyp-Bsd Prc Condition (PST0): Overview view, make the following entries as below and choose Save.Material: CBPTS002Amount: <amount>UoM: <PC>Valid From: <the current date>Valid To: for example, <the current date + one year > | Material pricing condition is maintained. |  |

### Create Pricing Condition of PST1

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes creating sales pricing condition: PST1

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Pricing Specialist. | The Start page appears. |  |
| 2 | Access the SAP Fiori App | Open Set Material Prices - Sales (VK12). | The Change Condition Records screen displays. |  |
| 3 | Pricing Condition Type | In the Change Condition Records view, make the following entries and choose Enter.Condition Type: PST1 |  |  |
| 4 | Selection | In the Change SrvcTyp-Bsd VarP (PST1): Selection view, make the following entries as below and choose Execute.Sales Organization: Sales OrganizationDistribution Channel: Distribution Channel |  |  |
| 5 | Change Price Condition | In the Change SrvcTyp-Bsd VarP (PST1): Overview view, make the following entries as below and choose Save.Material: CBPTS001Variant: HIGH_ENDAmount: <amount>UoM: PCValid From: <the current date>Valid To: for example, <the current date + one year> | Material pricing condition is maintained. |  |

### Create Pricing Condition of PST2

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes creating sales pricing condition: PST2

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Pricing Specialist. | The Start page appears. |  |
| 2 | Access the SAP Fiori App | Open Set Material Prices - Sales (VK12). | The Change Condition Records screen displays. |  |
| 3 | Pricing Condition Type | In the Change Condition Records view, make the following entries and choose Enter.Condition Type: PST2 |  |  |
| 4 | Selection | In the SrvcTyp-Bsd Var% (PST2): Selection view, make the following entries as below and choose Execute.Sales Organization: Sales OrganizationDistribution Channel: Distribution Channel |  |  |
| 5 | Change Price Condition | In the Change SrvcTyp-Bsd Var% (PST2): Overview view, make the following entries as below and choose Save.Material: CBPTS001Variant: HIGH_ENDAmount: <amount>Valid From: <the current date>Valid To: for example, <the current date + one year> | Material pricing condition is maintained. |  |

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
- related-to :: [[09-subscription-billing-and-contract-accounting/criar-condicao-de-determinacao-de-precos-baseada-em-tipo-de-servico-md]]
- related-to :: [[09-subscription-billing-and-contract-accounting/mds-3gd-319]]
- related-to :: [[09-subscription-billing-and-contract-accounting/mds-3gd-321]]
- related-to :: [[09-subscription-billing-and-contract-accounting/script-de-datos-maestros-crear-condicion-de-determinacion-de-precios-b]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3GD_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 11,362 chars in the whole document
