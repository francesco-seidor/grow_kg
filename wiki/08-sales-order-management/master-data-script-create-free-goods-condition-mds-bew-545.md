---
id: 08-sales-order-management/master-data-script-create-free-goods-condition-mds-bew-545
title: Master Data Script - Create Free Goods Condition - MDS (BEW) (BEW_S4CLD2608_Master_Data_EN_XX)
description: "SAP S/4HANA Cloud 2608 master data script BEW: how a Pricing Specialist maintains free goods conditions per customer and material in app VBN2."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/free-goods]
aliases: [BEW_S4CLD2608_Master_Data_EN_XX]
keywords: [Free Goods and Free-of-Charge Delivery, free goods conditions, pricing conditions, key combinations, business roles, master data scripts, sales orders, BEW]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BEW_S4CLD2608_Master_Data_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-545
topic: 08-sales-order-management/free-goods
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Master Data Script - Create Free Goods Condition - MDS (BEW) (BEW_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BEW_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Free Goods and Free-of-Charge Delivery** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Free Goods Condition - MDS (BEW) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233904899)

[2 Prerequisites 3](#_Toc233904900)

[2.1 System Access 3](#_Toc233904901)

[2.2 Roles 3](#_Toc233904902)

[2.3 Mandatory and Optional Master Data 3](#_Toc233904903)

[3 Overview Table 5](#_Toc233904904)

[4 Test Procedures 6](#_Toc233904905)

[4.1 Create Free Goods Condition 6](#_Toc233904906)

## Purpose

Business Context

Some customers may receive goods free of charge when they buy a certain amount. A free goods condition allows this agreement to be maintained for a specific customer and material. It is used in the sales order transaction.

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
| Customer | Initial screen | Mandatory | <Customer number> |  |
| Material | Initial screen | Optional | For example, TG11 |  |

|  |
| --- |
| Remember Sample values for master data values are country/region-specific, the baseline package sample data provides localized values for supported countries/regions. |

## Overview Table

Create Free Goods Condition - MDS consists of the process steps that are listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | SAP Fiori App / Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Free Goods Condition](#unique_7) [page ] 6 | Pricing Specialist | Manage Free Goods - Sales (VBN2) | Free goods condition record is created. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Free Goods Condition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure describes creating pricing conditions.

|  |
| --- |
| Remember Sample values for master data values are country/region-specific. Substitute the country/region-specific values provided by the SAP S/4HANA Cloud Public Edition system or use master data values you have created for this purpose. |

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Pricing Specialist. | The SAP Fiori launchpad displays. | The SAP Fiori launchpad displays. |
| 2 | Access the SAP Fiori App | Open Manage Free Goods - Sales (VBN2). | A new view opens, displaying Change free goods determination. |  |
| 3 | Pricing Condition Type | In the Change free goods determination view, enter the following information:Discount Type: for example, YA00Press Enter. | The Change Free Goods SD (YA00): Selection view opens. |  |
| 4 | Key Combination | Customer / materialAnd choose Choose. |  |  |
| 5 | Selection | In the Change Free Goods SD (YA00): Selection view, enter the following information:Sales organization: <Company Code>Distribution Channel: for example, 10Customer: <Customer number>Valid On: <Date>Choose Execute. | Change Free Goods SD (YA00) view displays. |  |
| 6 | Change Price Condition | In the Change Free Goods SD (YA00) screen, input the data below:Material: for example, TG11Min.qty: for example, 1,000For: for example, 500Unit: for example, PCAdd. Qnty: for example, 10Add Qnty Unit: for example, PCCacul Type: for example, 1FreeGoods: for example, 1 | Free goods condition is maintained. |  |
| 7 | Save | Choose Save. | The free goods condition is saved. |  |

Key Combination: Sales Org / Distribution Channel / Price Group / Material

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Pricing Specialist. | The SAP Fiori launchpad displays. | The SAP Fiori launchpad displays. |
| 2 | Access the SAP Fiori App | Open Manage Free Goods - Sales (VBN2). | A new view opens, displaying Change free goods determination. |  |
| 3 | Pricing Condition Type | In the Change free goods determination view, enter the following information:Discount Type: for example, YA00Press Enter. | The Change Free Goods SD (YA00): Selection view opens. |  |
| 4 | Key Combination | Sales Org. / Distr.Chl / Price Grp / MaterialAnd Choose Choose |  |  |
| 5 | Selection | In the Change Free Goods SD (YA00): Selection view, enter the following information:Sales organization: <Company Code>Distribution Channel: for example, 10Price group: <Price Group>Valid On: <Date>Choose Execute. | Change Free Goods SD (YA00) view displays. |  |
| 6 | Change Price Condition | In the Change Free Goods SD (YA00) screen, input the data below:Material: for example, TG11Min.qty: for example, 1,000For: for example, 500Unit: for example, PCAdd. Qnty: for example, 10Add Qnty Unit: for example, PCCacul Type: for example, 1FreeGoods: for example, 1 | Free goods condition is maintained. |  |
| 7 | Save | Choose Save. | The free goods condition is saved. |  |

Key Combination: Sales Org / Distribution Channel / Material

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Pricing Specialist. | The SAP Fiori launchpad displays. | The SAP Fiori launchpad displays. |
| 2 | Access the SAP Fiori App | Open Manage Free Goods - Sales (VBN2). | A new view opens, displaying Change free goods determination. |  |
| 3 | Pricing Condition Type | In the Change free goods determination view, enter the following information:Discount Type: for example, YA00Press Enter. | The Change Free Goods SD (YA00): Selection view opens. |  |
| 4 | Key Combination | Sales Org. / Distr.Chl / MaterialAnd Choose Choose. |  |  |
| 5 | Selection | In the Change Free Goods SD (YA00): Selection view, enter the following information:Sales organization: <Company Code>Distribution Channel: for example, 10Valid On: <Date>Choose Execute. | Change Free Goods SD (YA00) view displays. |  |
| 6 | Change Price Condition | In the Change Free Goods SD (YA00) screen, input the data below:Material: for example, TG11Min.qty: for example, 1,000For: for example, 500Unit: for example, PCAdd. Qnty: for example, 10Add Qnty Unit: for example, PCCacul Type: for example, 1FreeGoods: for example, 1 | Free goods condition is maintained. |  |
| 7 | Save | Choose Save. | The free goods condition is saved. |  |

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
- related-to :: [[08-sales-order-management/criar-condicao-de-bonificacao-em-mercadoria-mds-bew-548]]
- related-to :: [[08-sales-order-management/mds-bew-547]]
- related-to :: [[08-sales-order-management/mds-bew-549]]
- related-to :: [[08-sales-order-management/naturalrabattkondition-anlegen-sds-bew-544]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BEW_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 11,565 chars in the whole document
