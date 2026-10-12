---
id: 08-sales-order-management/create-sales-pricing-condition-mds-bet-539
title: Create Sales Pricing Condition - MDS (BET) (BET_S4CLD2608_Master_Data_EN_XX)
description: "English SAP master data script (BET, 2608): create a sales pricing condition (e.g. PPR0) with Set Material Prices - Sales (VK12) as Pricing Specialist."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/sales-pricing-conditions]
aliases: [BET_S4CLD2608_Master_Data_EN_XX]
keywords: [Sales Price Conditions and Statistical Conditions, sales pricing conditions, pricing condition creation, business roles, sales organization, distribution channel, master data scripts, test procedures, fiori launchpad access, BET]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BET_S4CLD2608_Master_Data_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-539
topic: 08-sales-order-management/sales-pricing-conditions
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Create Sales Pricing Condition - MDS (BET) (BET_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BET_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Sales Price Conditions and Statistical Conditions** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Sales Pricing Condition - MDS (BET) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233904854)

[2 Prerequisites 3](#_Toc233904855)

[2.1 System Access 3](#_Toc233904856)

[2.2 Roles 3](#_Toc233904857)

[2.3 Mandatory and Optional Master Data 3](#_Toc233904858)

[3 Overview Table 5](#_Toc233904859)

[4 Test Procedures 6](#_Toc233904860)

[4.1 Create Pricing Condition 6](#_Toc233904861)

## Purpose

Sales pricing conditions are used to store the information required to undertake automatic pricing in a sales order. They include prices, discounts, surcharges and taxes. They may be specific to a particular customer or material or a combination of parameters.

A sales pricing condition holds information such as a price in a specific currency for a material or a customer specific discount as a percentage. This information is used and stored in the sales order and in billing documents such as invoices.

The information is generally specific to a particular sales unit within your organization.

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
| Pricing Specialist | SAP_BR_PRICING_SPECIALIST | Price Management | SAP_BR_PRICING_SPECIALIST |  |

### Mandatory and Optional Master Data

The following table gives an overview of optional and mandatory master data objects to be used when creating pricing conditions.

If you have installed an SAP Best Practices baseline package, you can use the baseline package sample data or add your own master data, as required:

| Master Data Object | Used in Data Segment | Mandatory/Optional | Sample Values | Comments |
| --- | --- | --- | --- | --- |
| Sales Organization | Initial screen | Mandatory | <Sales Organization number> |  |
| Distribution Channel | Initial screen | Mandatory | <Distribution Channel number> |  |
| Material | Initial screen | Mandatory | For example, TG11 |  |

|  |
| --- |
| Remember Sample values for master data values are country/region-specific, the baseline package sample data provides localized values for supported countries/regions. |

## Overview Table

This scope item consists of several process steps that are listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction / App | Expected Results |
| --- | --- | --- | --- |
| [Create Pricing Condition](#unique_7) [page ] 6 | Pricing Specialist | Set Material Prices - Sales (VK12) | Sales pricing conditions are created. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Pricing Condition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes creating sales pricing conditions.

|  |
| --- |
| Remember Sample values for master data values are country/region-specific. Substitute the country/region-specific values provided by the SAP S/4HANA Cloud Public Edition system or use master data values you have created for this purpose. |

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Pricing Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Set Material Prices - Sales (VK12). | The Create Mandate: Initial Screen displays. |  |
| 3 | Pricing Condition Type | In the Change Condition Records view, enter the following information:Condition Type: for example, PPR0Press Enter. | The Key Combination view displays. |  |
| 4 | Key Combination | In the Key combination view, choose Material with release status and click Choose. | The Change Price (PPR0): Selection view displays. |  |
| 5 | Selection | In the Change Price (PPR0): Selection view, enter the following information:Sales organization: <Sales Organization>Distribution Channel: <Distribution Channel>Material: for example, TG11Valid On: for example, <Date>Choose Execute. | The Change Price Condition (PPR0): Overview view displays. |  |
| 6 | Change Price Condition | In the Change Price Condition (PPR0): Overview view, enter the following data:Material: for example, TG11Amount: for example, $17.55$Valid From: for example, <Current date>Valid To: for example, <Current date + one year> | Material pricing condition is maintained. |  |
| 7 | Save | Choose Save. | The pricing condition is saved. |  |

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
- related-to :: [[08-sales-order-management/mds-bet-541]]
- related-to :: [[08-sales-order-management/mds-bet-543]]
- related-to :: [[08-sales-order-management/script-de-dados-mestre-criar-condicao-de-determinacao-de-preco-de-vend]]
- related-to :: [[08-sales-order-management/script-de-datos-maestros-crear-condicion-de-determinacion-de-precio-de]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BET_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 8,940 chars in the whole document
