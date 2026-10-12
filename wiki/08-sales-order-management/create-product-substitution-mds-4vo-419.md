---
id: 08-sales-order-management/create-product-substitution-mds-4vo-419
title: Create Product Substitution - MDS (4VO) (4VO_S4CLD2608_Master_Data_EN_XX)
description: "SAP S/4HANA Cloud Public Edition 2608 master data script (4VO): create product substitution and exclusion, with optional reason, group and control setup."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/product-and-location-substitution]
aliases: [4VO_S4CLD2608_Master_Data_EN_XX]
keywords: ["Product, Plant and Storage Location Substitution", product substitution, product exclusion, master data scripts, substitution reasons, substitution groups, substitution controls, product master data, fiori launchpad roles, 4VO]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/4VO_S4CLD2608_Master_Data_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-419
topic: 08-sales-order-management/product-and-location-substitution
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Create Product Substitution - MDS (4VO) (4VO_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/4VO_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Product, Plant and Storage Location Substitution** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Product Substitution - MDS (4VO) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233904761)

[2 Prerequisites 3](#_Toc233904762)

[2.1 System Access 3](#_Toc233904763)

[2.2 Roles 3](#_Toc233904764)

[2.3 Required Organizational Units 3](#_Toc233904765)

[2.4 Mandatory Master Data 4](#_Toc233904766)

[2.5 Preliminary Steps 4](#_Toc233904767)

[2.5.1 Create Reason for Product Substitution (Optional) 4](#_Toc233904768)

[2.5.2 Create Group for Substitution (Optional) 5](#_Toc233904769)

[2.5.3 Create Control for Substitution (Optional) 6](#_Toc233904770)

[3 Overview Table 9](#_Toc233904771)

[4 Test Procedures 10](#_Toc233904772)

[4.1 Create Product Substitution 10](#_Toc233904773)

[4.2 Create Product Exclusion 11](#_Toc233904774)

## Purpose

In this document you will find how to create a Product Substitution and Exclusion master data for your SAP S/4HANA Cloud Public Edition system.

Product Substitution is a technique used to replace one product with another product. A Product Substitution can be created for various reasons. For example:

- Product is no longer in stock
- Product is out of warranty
- Substitute Product is abundant in stock

Product Exclusion enables customers to exclude a product from being a substitue. For example, Exclusion can be created for a discontinued product.

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

| System | Details |
| --- | --- |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Products / Product Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |

### Required Organizational Units

The organizational structure reflects the structure of your company. Product Substitutes can be dependent on the organizational units (plant) of the company. It can also be independent of the organizational unit. The following table gives an overview of the relevant organizational units.

| Data Segment | Depends On | Field Examples | Comments | Organizational Unit to be Used |
| --- | --- | --- | --- | --- |
| Product Substitution and Product Exclusion | Plant |  | Plant is not mandatory in product substitution/exclusion. Product substation/exclusion can happen without plant restriction. | Plant:____________ |

### Mandatory Master Data

Product Substitution data refers to product master data. The mandatory master data for the test script represents Materials/Products. Create your own master data by following the sample master data provided below.

| Master Data Object | Used in Data Segment | Mandatory/Optional | Comments |
| --- | --- | --- | --- |
| Material | Create Product SubstitutionCreate Product Exclusion | Mandatory | To create product substitution or product exclusion, there should be at least 2 material/products master data in your system |

For more information on creating master data objects, see [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) .

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |

### Preliminary Steps

#### Create Reason for Product Substitution (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions on how to create Reason for Product substitution/exclusion. Apps available to you are dependent upon your assigned role.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Substitution Reasons - Products (F4789). | The Manage Substitution Reasons - Products screen displays. |  |
| 3 | Choose Create | On the Manage Substitution Reasons - Products screen, choose Create. | The Reason screen displays. |  |
| 4 | Enter Reason | In the Header section, make the following entry:Reason: <Enter the new Reason code for substitution, for example, Upgrade> |  |  |
| 5 | Save Your Data | Choose Create. | System message displays that Object is saved. |  |
| 6 | Choose Create | In the Description section, choose Create. | The Reason Description screen displays. |  |
| 7 | Enter Description Data | In the Description section, make the following entries:Language Key: <Enter language key applicable for the Reason, for example, EN for English>Reason Description: <Enter text to describe the Reason, for example, Applicable for Products undergoing upgrades> |  |  |
| 8 | Save Your Data | Choose Create. | System message displays that Description created. |  |

#### Create Group for Substitution (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating Group for Product Substitution/Exclusion. Apps available to you are dependent upon your assigned role.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad appears. |  |
| 2 | Access the SAP Fiori App | Open Manage Substitution Groups - Products (F4788). | The Manage Substitution Groups - Products screen is displayed. |  |
| 3 | Choose Create | On the Manage Substitution Groups – Products screen, choose Create. | The Manage Substitutions Groups-Products Create screen is displayed. |  |
| 4 | Enter Group | In the Header section, make the following entry:Group: <Enter the new Group for substitution, for example, STANDARD_DISPLAY> |  |  |
| 5 | Save Your Data | Choose Create. | System message shows that object is saved. |  |
| 6 | Choose Create | In the Description section, choose Create. | The Group Description Create screen is displayed. |  |
| 7 | Enter Description Data | In the Description section, make the following entries:Language Key: <Enter Language applicable for Group, for example, EN English>Group Description: <Enter text to describe the group, for example, All standard computer display> |  |  |
| 8 | Save Your Data | Choose Create. | System message shows that object is saved. |  |
| 9 | Choose Back | In the Title section, Choose < (Back) | The Manage Substitutions Groups-Products screen is displayed. |  |
| 10 | Activate Group Data | Choose Set to Active. | System message shows that object is active. |  |

#### Create Control for Substitution (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating control for product substitution/exclusion groups. Apps available to you are dependent upon your assigned role.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad appears. |  |
| 2 | Access the SAP Fiori App | Open Manage Substitution Controls - Products (F4787). | The Manage Substitution Controls - Products screen is displayed. |  |
| 3 | Choose Create | On the Manage Substitution Controls – Products screen, choose Create. | The Manage Substitution Controls-Products Create screen is displayed. |  |
| 4 | Enter Control | In the Header section, make the following entry.Control: <Enter the new control for substitution, for example, SALE> |  |  |
| 5 | Save Your Data | Choose Create. | System message shows that object is saved. |  |
| 6 | Choose Create | In the Description section, choose Create. | The Control Description Create screen is displayed. |  |
| 7 | Enter Description Data | In the Description section, make the following entries:Language Key: <Enter Language applicable for Control, for example, EN English>Control Description: <Enter text to describe the Control, for example, For Sale> |  |  |
| 8 | Save Your Data | Choose Create. | System message shows that object is saved. |  |
| 9 | Choose Back | In the Title section, Choose < (Back). | The Manage Substitution Controls-Products screen is displayed. |  |
| 10 | Assign Groups | In the Assigned Groups section, Choose Assign. | The Assign Groups to Control dialog is displayed. |  |
| 11 | Choose Group | In the Assign Groups to Control dialog, search and choose Group.For example, choose Group <STANDARD_DISPLAY>Choose Assign. | System message shows that object is assigned. |  |

## Overview Table

This scope item consist of the process segments provided in the below table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Segment | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Product Substitution](#unique_11) [page ] 10 | Master Data Specialist - Product Data | Manage Substitutions - Products (F4785) | Product Substitution record is created. |
| [Create Product Exclusion](#unique_12) [page ] 11 | Master Data Specialist - Product Data | Manage Exclusions - Products (F4786) | Product Exclusion record is created. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Product Substitution

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating Product Substitution. Apps available to you are dependent upon your assigned role.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Substitutions - Products (F4785). | The Manage Substitutions - Products screen displays. |  |
| 3 | Choose Create | In the Manage Substitutions - Products view, choose Create. | The Manage Substitutions - Products flexible column layout with Create screen displays. |  |
| 4 | Enter Header Data | In the Header section, make the following entries:Product: <Enter the product which requires a substitute>Substitute Product: <Enter the substitute>Plant: <Plant number>Product and Substitute Product data is mandatory to create a substitution. |  |  |
| 5 | Enter General Information Data | In the General Information section, make the following entries:Reason: <Enter the reason for creating substitute. For example, Upgrade>Valid From: <Enter the start date and time for validity>Valid To: <Enter the end date and time for validity>Time Zone: <Enter the time zone applicable for validity>The above entries are optional. |  |  |
| 6 | Save Your Data | Choose Create. | System message displays that object is saved. |  |
| 7 | Activate Product Substitution Data | Choose Set to Active. | System message displays that object is active. |  |

### Create Product Exclusion

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating Product Exclusion. Apps available to you are dependent upon your assigned role.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Exclusions - Products (F4786). | The Manage Exclusions - Products screen displays. |  |
| 3 | Choose Create | In the Manage Exclusions - Products view, choose Create. | The Manage Exclusions -Products Create screen displays. |  |
| 4 | Enter Header Data | In the Header section, make the following entries:Product: <Enter the product which needs to be excluded from Substitution>Plant: <Plant number>Product is mandatory to create an exclusion. |  |  |
| 5 | Enter General Information Data | In the General Information section, make the following entries:Reason: <Enter the reason for excluding the Product>Valid From: <Enter the start date and time for validity>Valid To: <Enter the end date and time for validity>Time Zone: <Enter the time zone applicable for validity>The above entries are optional. |  |  |
| 6 | Save Your Data | Choose Create. | System message displays that object is saved. |  |
| 7 | Activate Product Exclusion Data | Choose Set to Active. | System message displays that object is active. |  |

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
- related-to :: [[08-sales-order-management/creacion-de-sustitucion-de-producto-mds-4vo-420]]
- related-to :: [[08-sales-order-management/mds-4vo-421]]
- related-to :: [[08-sales-order-management/mds-4vo-423]]
- related-to :: [[08-sales-order-management/script-de-dados-mestre-criar-substituicao-de-produto-mds-4vo-422]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/4VO_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 17,391 chars in the whole document
