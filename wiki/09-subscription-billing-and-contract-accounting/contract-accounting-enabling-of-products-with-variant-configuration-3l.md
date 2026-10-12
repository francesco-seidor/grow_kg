---
id: 09-subscription-billing-and-contract-accounting/contract-accounting-enabling-of-products-with-variant-configuration-3l
title: Contract Accounting – Enabling of Products with Variant Configuration (3L8_AE) – Test Script (3L8_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition test script for scope item 3L8_AE: variant configuration products in provider contracts, with rating, billing and invoicing."
cluster: 09-subscription-billing-and-contract-accounting
tags: [kb/subscription-billing-and-contract-accounting, topic/variant-configured-products-in-provider-contracts]
aliases: [3L8_S4CLD2608_BPD_EN_AE]
keywords: [Variant-Configured Products in Provider Contracts, variant configuration, provider contracts, contract accounting, variant pricing, billing and invoicing, test scripts, business roles, business conditions, demo data]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3L8_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-955
topic: 09-subscription-billing-and-contract-accounting/variant-configured-products-in-provider-contracts
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Contract Accounting – Enabling of Products with Variant Configuration (3L8_AE) – Test Script (3L8_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3L8_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Variant-Configured Products in Provider Contracts** in Subscription Billing and Contract Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Contract Accounting – Enabling of Products with Variant Configuration (3L8_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232853182)

[2 Prerequisites 3](#_Toc232853183)

[2.1 System Access 3](#_Toc232853184)

[2.2 Roles 3](#_Toc232853185)

[2.3 Master Data, Organizational Data, and Other Data 3](#_Toc232853186)

[2.4 Business Conditions 4](#_Toc232853187)

[2.5 Additional Manual Configuration 5](#_Toc232853188)

[3 Overview Table 6](#_Toc232853189)

[4 Test Procedures 8](#_Toc232853190)

[4.1 Create Provider Contract of Product with Variant Configuration 8](#_Toc232853191)

[4.2 Create Subsequent Rating, Billing and Invoicing for Provider Contract with VC Product 8](#_Toc232853192)

## Purpose

Overview

Based on the Contract Accounting – Master Data and Basic Functions (2AR) scope item, you can enable variant configuration material in provider contract with variant pricing for the subsequent Convergent Invoicing – Recurring and One-Off Items (2T3) scope item. Rating, billing, and invoicing takes variant configuration materials into consideration. As a result, contract accounting can cover variant pricing for variant configuration products.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all prerequisites for conducting the test in terms of systems, users, master data, organizational data, and other test data and business conditions.

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
| Product Configuration Modeler | SAP_BR_PRODUCT_CONFIG_MODELER | Variant Configuration | SAP_BR_PRODUCT_CONFIG_MODELER |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material Master | CBPTS001 |  |  |

Table 1: Other Data

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Business Partner | BP_AE_99 |  |  |
| Contract Account | CA_AE_99 |  |  |

You can find general information on how to create master data objects in the following Master Data Scripts (MDS):

Table 2: Master Data Script Reference

| Master Data Script ID | Description |
| --- | --- |
| 3JA | Create Product Master for Consumption Based Billing - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| 2AR - Contract Accounting – Master Data and Basic Functions | Must be run before this test script. Contract partner and contract account have been created for posting. |
| 2AR - Setting Up Contract Accounting - Master Data and Basic Functions | Make sure Communication Arrangement -Create Communication Arrangement for Finance - Contract Accounting Integration has been done before this test script. |

### Additional Manual Configuration

Before you use the VC material- CBPTS001, please make sure the below steps also been done in the system:

1. Log on to the SAP Fiori Launchpad with your user credentials as SAP_BR_PRODUCT_CONFIG_MODELER role assigned.

2. Choose VC Modeling Environment APP, material: CBPTS001. Choose Enter Model, double click the material and select variant pricing tab. Add Characteristic –Category, Char. Value – HIGH_END and Variant Condition = HIGH_END, choose save.

## Overview Table

This enabling of variable configuration of prodcut in provider contract scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Create a Contract Account[2AR] | Accounts Payable and Receivable Accountant (FI-CA) | Maintain Business Partner (BP) | Business partner can be created with BP role MKK (contract partner). |
| Create a Contract Account[2AR] | Accounts Payable and Receivable Accountant (FI-CA) | Maintain Contract Account (CAA3) | Contract account can be created. |
| Create Provider Contract of Product with Variant Configuration |  |  | Provider Contract can be created. |
| Option1: Request Billing Plan Items (Mass Run) [2T3] | Invoicing Specialist (Convergent Invoicing) | Request Billing Plan Items (F3530) | Billable item is created |
| Option2: Request Billing Plan Items (Individual Run) [2T3] | Invoicing Specialist (Convergent Invoicing) | Request Billing Plan Items - Business Partner (FKKBIXBIP_S) | Billable item is created |
| Option1: Perform Billing Process (Mass Run) [2T3] | Invoicing Specialist (Convergent Invoicing) | Execute Billing - Mass Run (F3525) | Billing Document is created |
| Option 2: Perform Billing Process (Individual Run) [2T3] | Invoicing Specialist (Convergent Invoicing) | Request Billing Plan Items - Business Partner (FKKBIXBIP_S) | Billing Document is created |
| Display Billing Document (Optional) [2T3] | Invoicing Specialist (Convergent Invoicing) | Manage Billing Document (F2250) | Billing Document is displayed |
| Option 1: Perform Invoicing Process (Mass Run) [2T3] | Invoicing Specialist (Convergent Invoicing) | Execute Invoicing - Business Partner (FKKINV_S) | Invoicing Document is created. |
| Option 2: Perform Invoicing Process (Individual Run) [2T3] | Invoicing Specialist (Convergent Invoicing) | Execute Invoicing - Business Partner (FKKINV_S) | Invoicing Document is created |
| Display Invoicing Document (Optional) [2T3] | Invoicing Specialist (Convergent Invoicing) | Manage Invoicing Documents (F2048) | Invoicing Document is displayed |
| Option 1: Request Billing Plan Items (Mass Run) [2T3] | Invoicing Specialist (Convergent Invoicing) | Execute Billing - Mass Run (F3525) | Billable item is created |
| Option 2: Request Billing Plan Items (Individual Run) [2T3] | Invoicing Specialist (Convergent Invoicing) | Request Billing Plan Items - Mass Run (FKKBIXBIP_MA) | Billable item is created |

## Test Procedures

Prerequisite Step

In order to create variant pricing, you need refer to 3JA initialize variant configuration modeling environment for material CBPTS001.

### Create Provider Contract of Product with Variant Configuration

Context

In this activity, you can create provider contract of product with variable configurations.

Procedure

Please refer to scope item Contract Accounting – Master Data and Basic Functions (2AR), step Creation of Provider Contract and use specific variable configuration material CBPTS001 as the demo data in start system.

### Create Subsequent Rating, Billing and Invoicing for Provider Contract with VC Product

Context

In this activity, you can do rating, billing and invoicing based on the provider contract with variable configuration products.

Procedure

Refer to scope item Convergent Invoicing – Recurring and One-Off Items (2T3), from step Request Billing Plan Items to step Perform Invoicing Process for the recurring and one-off items and consequent billing and invoicing.

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
- related-to :: [[09-subscription-billing-and-contract-accounting/master-data-script-create-product-master-for-consumption-based-billing]]
- related-to :: [[09-subscription-billing-and-contract-accounting/mds-3ja-325]]
- related-to :: [[09-subscription-billing-and-contract-accounting/mds-3ja-327]]
- related-to :: [[09-subscription-billing-and-contract-accounting/script-de-dados-mestre-criar-dados-mestre-do-produto-para-faturamento]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3L8_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 13,049 chars in the whole document
