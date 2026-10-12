---
id: 08-sales-order-management/create-object-and-value-determination-mds-5nh-479
title: Create Object and Value Determination - MDS (5NH) (5NH_S4CLD2608_Master_Data_EN_XX)
description: "Master data test script (5NH) for substitution controls, characteristic combinations and access sequences used for product/plant/storage location substitution with AATP ABC in S/4HANA Cloud 2608."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/product-and-location-substitution]
aliases: [5NH_S4CLD2608_Master_Data_EN_XX]
keywords: ["Product, Plant and Storage Location Substitution", object and value determination, substitution controls, characteristic combination, access sequences, product substitution, plant substitution, storage location substitution, alternative based confirmation, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5NH_S4CLD2608_Master_Data_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-479
topic: 08-sales-order-management/product-and-location-substitution
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Create Object and Value Determination - MDS (5NH) (5NH_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5NH_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Product, Plant and Storage Location Substitution** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Object and Value Determination - MDS (5NH) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233904802)

[2 Prerequisites 3](#_Toc233904803)

[2.1 System Access 3](#_Toc233904804)

[2.2 Roles 3](#_Toc233904805)

[2.3 Required Organizational Units 3](#_Toc233904806)

[2.4 Mandatory Master Data 3](#_Toc233904807)

[2.5 Preliminary Steps 4](#_Toc233904808)

[2.5.1 Create Control for Product Substitution (Optional) 4](#_Toc233904809)

[2.5.2 Create Control for Plant Substitution (Optional) 6](#_Toc233904810)

[2.5.3 Create Control for Storage Location Substitution (Optional) 7](#_Toc233904811)

[3 Overview Table 10](#_Toc233904812)

[4 Test Procedures 11](#_Toc233904813)

[4.1 Create Characteristic Combination 11](#_Toc233904814)

[4.2 Create Access 12](#_Toc233904815)

## Purpose

In this document, you will find how to create a Combination and the Access with Characteristic Values for the combination master data for your SAP S/4HANA Cloud Public Edition system.

Object and Value determination allows an user to configure the characteristics to determine a Control that would be used to Substitute a Product/Plant/Storage Location in Sales Order during the availability check.

This enables the Integration of master Data Substitution with the Alternative Based Confirmation (ABC) of AATP functionality.

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

| System | Details |
| --- | --- |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Order Fulfillment Manager | SAP_BR_ORDER_FULFILLMNT_MNGR | Order Fulfillment Management | SAP_BR_ORDER_FULFILLMNT_MNGR |  |
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Products / Product Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |

### Required Organizational Units

No specific Organizational data required.

| Data Segment | Depends On | Field Examples | Comments | Organizational Unit to be Used |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

### Mandatory Master Data

No Specific Master Data required.

| Master Data Object | Used in Data Segment | Mandatory/Optional | Comments |
| --- | --- | --- | --- |
|  |  |  |  |

For more information on creating master data objects, see Table 1: Master Data Script Reference:

| MDS | Description |
| --- | --- |
|  |  |

### Preliminary Steps

#### Create Control for Product Substitution (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions on creating control for product substitution/exclusion groups. Apps available to you are dependent upon your assigned role.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Substitution Controls - Products (F4787). | The app opens. |  |
| 3 | Choose Create | On the Manage Substitution Controls - Products screen, choose Create. | The Manage Substitution Controls-Products Create screen displays. |  |
| 4 | Enter Control | In the Header section, make the following entry:Control: <Enter the new Control for substitution, for example, SALE> |  |  |
| 5 | Choose Create | Choose Create. | System message displays that Control created. |  |
| 6 | Create Description | In the Description section, choose Create. | The Control Description Create screen displays. |  |
| 7 | Enter Description Data | In the Description section, make the following entries:Language Key: <Enter Language applicable for the Control, for example, EN for English>Control Description: <Enter text to describe the Control, for example, For Sale> |  |  |
| 8 | Choose Create | Choose Create. | System message displays that Control Description created. |  |
| 9 | Choose Back | In the Title section, choose < (Back). | The Manage Substitution Controls-Products screen displays. |  |
| 10 | Assign Groups | In the Assigned Groups section, Choose Assign. | The Assign Groups to Control dialog box displays. |  |
| 11 | Choose Group | In the Assign Groups to Control dialog box, search and choose Group.For example, choose the STANDARD_DISPLAY Group.Note If no existing available Group displays, you can first go through the process step Create Group for Substitution (Optional) in Master Data Script Create Product Substitution - MDS - 4VO.Choose Assign. | System message displays that Object is assigned. |  |

#### Create Control for Plant Substitution (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions on creating control for Plant substitution/exclusion controls. Apps available to you are dependent upon your assigned role.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Order Fulfillment Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Substitution Controls - Locations (F5312). | The app opens. |  |
| 3 | Choose Create | On the Manage Substitution Controls - Locations screen, choose Create. | The Manage Substitution Controls - Locations Create screen displays. |  |
| 4 | Enter Control | In the Header section, make the following entries:Location Type: <Plant>Control: <Enter the new control for substitution, for example, REGION> |  |  |
| 5 | Save Your Data | Choose Save. | System message displays that Control Created. |  |
| 6 | Choose Create | In the Description section, choose Create. | The Control Description Create screen displays. |  |
| 7 | Enter Description Data | In the Description section, make the following entries:Language Key: <Enter the language key applicable for the Control, for example, EN for English>Control Description: <Enter text to describe the Control, for example, Control for a Region> |  |  |
| 8 | Save Your Data | Choose Create. | System message displays that Control Description Created. |  |
| 9 | Choose Back | In the Title section, Choose < (Back). | The Manage Substitution Controls - Locations screen displays. |  |
| 10 | Assign Groups | In the Assigned Groups section, choose Assign. | The Assign Groups to Control dialog box displays. |  |
| 11 | Choose Group | In the Assign Groups to Control dialog box, search and choose Group.For example, choose the <SOUTH_REGION> Group.Note If no existing available Group displays, you can first go through the process step Create Group for Plant Substitution (Optional) in Master Data Script Create Location Substitution and Exclusion - MDS - 5NG.Choose Assign. | System message displays that Group(s) have been assigned. |  |

#### Create Control for Storage Location Substitution (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions on creating control for Storage Location substitution/exclusion controls. Apps available to you are dependent upon your assigned role.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Order Fulfillment Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Substitution Controls - Locations (F5312). | The app opens. |  |
| 3 | Choose Create | On the Manage Substitution Controls - Locations screen, choose Create. | The Manage Substitution Controls - Locations Create screen displays. |  |
| 4 | Enter Control | In the Header section, make the following entries:Location Type: <Storage location>Control: <Enter the new Control for substitution, for example, STORAGE_TYPE> |  |  |
| 5 | Choose Create | Choose Create. | System message displays that Control Created. |  |
| 6 | Choose Create | In the Description section, choose Create. | The Control Description Create screen displays. |  |
| 7 | Enter Description Data | In the Description section, make the following entries:Language Key: <Enter the language key applicable for the Control, for example, EN for English>Control Description: <Enter text to describe the Control, for example, Control for Type of Storage> |  |  |
| 8 | Save Your Data | Choose Create. | System message displays that Control Description Created. |  |
| 9 | Choose Back | In the Title section, choose < (Back). | The Manage Substitution Controls - Locations screen displays. |  |
| 10 | Assign Groups | In the Assigned Groups section, choose Assign. | The Assign Groups to Control dialog box displays. |  |
| 11 | Choose Group | In the Assign Groups to Control dialog box, search and choose Group.For example, choose the <COLD_STORAGE> Group.Note If no existing available Group displays, you can first go through the process step Create Group for Storage Location Substitution (Optional) in Master Data Script Create Location Substitution and Exclusion - MDS - 5NG.Choose Assign. | System message displays that Group(s) have been assigned. |  |

## Overview Table

This scope item consist of the process segments provided in the below table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Segment | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Characteristic Combination](#unique_11) [page ] 11 | Order Fulfillment Manager | Manage Characteristic Combinations (F5303). | Characteristic Combination is created. |
| [Create Access](#unique_12) [page ] 12 | Order Fulfillment Manager | Manage Access Sequences - Substitutions (F5302) | Access is created for the combination created in the above Segments and Characteristic values are defined for the Accesses. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Characteristic Combination

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions on creating Characteristic Combination. Apps available to you are dependent upon your assigned role.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Order Fulfillment Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Characteristic Combinations (F5303). | The app opens. |  |
| 3 | Choose Create | On the Manage Characteristic Combination screen, choose Create. | The Manage Characteristic Combination Create screen displays. |  |
| 4 | Enter Header Data | In the Header section, make the following entries:Combination: <Enter the Combination name>Combination Description : <Enter the description of the Combination>Usage: <Substitution>Catalog Type: <Base (Sales Document) with Usage SUBSTN>Combination, Usage, and Catalog Type are mandatory to create a Substitution. |  |  |
| 5 | Assign Characteristics | In the Characteristics section, make the following entries to assign the Characteristics:Choose AssignChoose the Characteristics on the screenChoose Assign on the screenSet the order of the Characteristics by using the Up or Down arrow |  |  |
| 6 | Choose Create | Choose Create. | System message displays that Combination is Created. |  |

### Create Access

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating the Access for the combination and defining the CVC values to the Access. Apps available to you are dependent upon your assigned role.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Order Fulfillment Manager. | The SAP Fiori launchpad appears. |  |
| 2 | Access the SAP Fiori App | Open Manage Access Sequences - Substitutions (F5302) | The Manage Access Sequences - Substitution screen is displayed. |  |
| 3 | Choose Create | In the Manage Access Sequences - Substitution view, under the Products tab, choose Create ( 3 tabs Products, Plant and Storage Location are available). | The Manage Access Sequences - Substitution Create screen is displayed. |  |
| 4 | Enter the details | In the Pop up window, make the following entries:Combination: <Select the Combination from value help>Status : <Select the required status from the drop down> Status field is defaulted with In Active status.Choose CreateCombination is mandatory to create an Access. | System message shows that the Access is created. |  |
| 5 | Enter Assigned Controls details | In the Assigned Controls section, add the Characterisitcs and the Control Details:Choose AddCharacteristics: <Enter the Characteristics values or choose from the Value help>Status: <Status is Active by default>Execute Substitution: <Enabled by default>Control : <Optional - Enter the Product Substitution Control>Add multiple values as required. | The characterisitcs Columns shown in the Assigned Controls section are the ones assigned to the Combination chosen while creating the access. |  |
| 6 | Create Access | Choose Create. | System message shows that Access created. |  |

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
- related-to :: [[08-sales-order-management/5nh-483]]
- related-to :: [[08-sales-order-management/crear-determinacion-de-objeto-y-valor-mds-5nh-480]]
- related-to :: [[08-sales-order-management/criar-determinacao-de-objeto-e-valor-mds-5nh-482]]
- related-to :: [[08-sales-order-management/mds-5nh-481]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5NH_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 18,160 chars in the whole document
