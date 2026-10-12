---
id: 10-procurement/master-data-script-create-scheduling-agreement-mds-bf6-557
title: "Master Data Script: Create Scheduling Agreement - MDS (BF6) (BF6_S4CLD2608_Master_Data_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition 2608 master data script for creating purchase scheduling agreements (standard, consigned, subcontracting) in Fiori app F2179."
cluster: 10-procurement
tags: [kb/procurement, topic/scheduling-agreements]
aliases: [BF6_S4CLD2608_Master_Data_EN_XX]
keywords: [Purchase Scheduling Agreements, scheduling agreements, standard procurement, consigned procurement, subcontracting procurement, number ranges, business roles, purchasing organization, material and supplier master data, tax code and tax country]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BF6_S4CLD2608_Master_Data_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-557
topic: 10-procurement/scheduling-agreements
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Master Data Script: Create Scheduling Agreement - MDS (BF6) (BF6_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BF6_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Purchase Scheduling Agreements** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Scheduling Agreement - MDS (BF6) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233904866)

[2 Prerequisites 3](#_Toc233904867)

[2.1 System Access 3](#_Toc233904868)

[2.2 Roles 3](#_Toc233904869)

[2.3 Required Organizational Units 3](#_Toc233904870)

[2.4 Mandatory and Optional Master Data 4](#_Toc233904871)

[2.5 Main Parameters for Data Creation 4](#_Toc233904872)

[2.5.1 Number Ranges 4](#_Toc233904873)

[3 Overview Table 5](#_Toc233904874)

[4 Test Procedures 6](#_Toc233904875)

[4.1 Create Scheduling Agreement for Standard Procurement 6](#_Toc233904876)

[4.1.1 Create Scheduling Agreement with Release Document - Standard 6](#_Toc233904877)

[4.1.2 Create Scheduling Agreement Without Release Document - Standard 8](#_Toc233904878)

[4.2 Create Scheduling Agreement for Consigned Procurement 10](#_Toc233904879)

[4.3 Create Scheduling Agreement for Subcontracting Procurement 12](#_Toc233904880)

## Purpose

This document provides a description for creating a scheduling agreement for your SAP S/4HANA Cloud Public Edition system. The description includes those data segments that are relevant for the SAP S/4HANA Cloud Public Edition appliance such as Purchasing Data, Material Data, and Supplier Data. Fields that are not relevant for the scope of SAP S/4HANA Cloud Public Edition as delivered by SAP Best Practices are not described in this document.

A Scheduling Agreement is a long-term agreement with a supplier covering the supply of materials subject to predetermined conditions. The conditions are valid for a predefined period and a predefined total quantity.

Main advantages of Scheduling Agreements are:

- Scheduling Agreements can replace a large amount of Purchase Orders or Contract Releases.
- It is a long-term agreement, which allows you to negotiate better prices with a supplier.

The following item categories exist:

- Standard procurement
- Consigned procurement
- Subcontracting procurement

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

### Required Organizational Units

The organizational structure and master data of your company was created in your ERP system during implementation. The organizational structure reflects the structure of your company. The following table gives an overview of these different data segments and their relevant organizational units:

| Data Segment | Depends On | Field Examples | Comments | Organizational Unit to be Used |
| --- | --- | --- | --- | --- |
| Purchasing Data | Purchasing Organization | Purchasing Group, Material Group, GR processing time, and so on. | Purchasing Data can exist for every purchasing organization for which the material is used in the purchasing processes. | Purchasing Organization:__________ |

### Mandatory and Optional Master Data

Scheduling agreement may refer to other master data. The following table gives an overview of optional and mandatory master data objects to be used in a scheduling agreement.

| Master Data Object | Used in Data Segment | Mandatory / Optional | Comments |
| --- | --- | --- | --- |
| Material |  | Mandatory | To input the material, first create material master data. |
| Supplier |  | Mandatory | To input the supplier, first create supplier master data. |

### Main Parameters for Data Creation

In this section, a description is provided for the basic parameters that influence the behavior of a scheduling agreement and that are always required to create a scheduling agreement.

#### Number Ranges

The following number ranges are defined for scheduling agreement:

| Number Range | Range / Business Partner ID | Comments |
| --- | --- | --- |
| Internal numeric | Internal numeric number range for standard use:5500000000 – 5599999999 | This number range is used when the system automatically assigns a numeric number to a scheduling agreement. |
| External numeric | External numeric number range:5600000000 – 5699999999 | This number range is reserved for external numeric number assignment. |

## Overview Table

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
|  |  |  |  |
| [Create Scheduling Agreement with Release Document - Standard](#unique_10) [page ] 6 | Purchaser | Manage Purchase Scheduling Agreements (F2179) | Scheduling Agreement with Release Document - Standard |
| [Create Scheduling Agreement Without Release Document - Standard](#unique_11) [page ] 8 | Purchaser | Manage Purchase Scheduling Agreements (F2179) | Scheduling Agreement Without Release Document - Standard |
| [Create Scheduling Agreement for Consigned Procurement](#unique_12) [page ] 10 | Purchaser | Manage Purchase Scheduling Agreements (F2179) | Scheduling Agreement for Consigned Procurement is created |
| [Create Scheduling Agreement for Subcontracting Procurement](#unique_13) [page ] 12 | Purchaser | Manage Purchase Scheduling Agreements (F2179) | Scheduling Agreement for Subcontracting Procurement is created |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Scheduling Agreement for Standard Procurement

#### Create Scheduling Agreement with Release Document - Standard

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Create scheduling agreement for standard procurement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Purchase Scheduling Agreements (F2179). | The app opens. |  |
| 3 | Create Scheduling Agreement | Choose Create to create a new scheduling agreement. | The New Purchase Scheduling Agreement screen displays. |  |
| 4 | Enter Header Data | Create a new scheduling agreement with the following data:Supplier: <Supplier>Agreement type: LPA (SA With Release doc.)Validity Start: <MM/DD/YYYY>Valid To: <MM/DD/YYYY>Company Code: <Company Code>Purchasing Organization: <Purchasing Organization>Purchasing Group: <Purchasing Group>Target Value : <Target Value> |  |  |
| 5 | Enter Header Notes | Go to the Notes section and enter some of the following Header Notes:Header textHeader notePricing typesDeadlinesTerms of deliveryShipping instructionsTerms of paymentWarrantiesPenalty for breach of contractGuaranteesContract riders (clauses)AssetOther contractual stipulationInbound DeliveryVendor memo (general)Vendor memo (pur. org.) |  |  |
| 6 | Add Items to Scheduling Agreement | From the New Purchase Scheduling Agreement screen, choose the Items facets and choose Create. | The Purchase Scheduling Agreement Item screen displays. |  |
| 7 | Enter Item Data | On the Items facets screen, make the following entries:Plant: <Plant>Material: <Material>Target Quantity: <Target Quantity>Net Order Price: <Net Order Price>Tax Code: <XX (the Default Value from Info Record)>Tax Date: <Use Today’s Date as the Default Value>In the Output Control section, make the following entry:Creation Profile: <Creation Profile>Choose Apply at the bottom of the screen. |  |  |
| 8 | Create | Return to the New Purchase Scheduling Agreement screen and choose Create at the bottom of the screen.Take a note of the schedule agreement number. | A schedule agreement is created. |  |

#### Create Scheduling Agreement Without Release Document - Standard

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Create scheduling agreement for standard procurement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Purchase Scheduling Agreements (F2179). | The Manage Purchase Scheduling Agreements (F2179) list page displays |  |
| 3 | Create Scheduling Agreement | Select Create to create a new scheduling agreement | The New Purchase Scheduling Agreement header view displays. |  |
| 4 | Enter Header Data | Create a new scheduling agreement with the following data:Supplier: <Supplier>Agreement type: LP (Scheduling Agreement)Validity Start: <MM/DD/YYYY>Valid To: <MM/DD/YYYY>Company Code: <Company Code>Purchasing Organization: <Purchasing Organization>Purchasing Group: <Purchasing Group>Target Value : <Target Value> |  |  |
| 5 | Enter Header Notes | Navigate to the Notes section and enter some of the following Header Notes:Header textHeader notePricing typesDeadlinesTerms of deliveryShipping instructionsTerms of paymentWarrantiesPenalty for breach of contractGuaranteesContract riders (clauses)AssetOther contractual stipulationInbound DeliveryVendor memo (general)Vendor memo (pur. org.) |  |  |
| 6 | Add Items to Scheduling Agreement | From the New Purchase Scheduling Agreement view, choose the Items facets and choose Create. | The Purchase Scheduling Agreement Item view displays. |  |
| 7 | Enter Item Data | On the Items facets screen, make the following entries:Plant: <Plant>Material: <Material>Target Quantity: <Target Quantity>Net Order Price: <Net Order Price>Tax Code: <XX (the Default Value from Info Record)>Tax Date: <Use Today’s Date as the Default Value>Choose Apply at the bottom of the screen. |  |  |
| 8 | Create | Return to the New Purchase Scheduling Agreement header view and choose Create at the bottom of the view.Make a note of the schedule agreement number. | A schedule agreement is created. |  |

### Create Scheduling Agreement for Consigned Procurement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Create scheduling agreement for consigned procurement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Purchase Scheduling Agreements (F2179). | The Manage Scheduling Agreements list page displays. |  |
| 3 | Create Scheduling Agreement | Select Create to create a new scheduling agreement. | The New Scheduling Agreement header view displays. |  |
| 4 | Enter Header Data | Create a new scheduling agreement with the following data:Agreement type: LP (Scheduling Agreement)Supplier: <Supplier>Validity Start: Default TodayValidity End: MM/DD/YYYY e.g. today + 720 daysPurchasing Group: <Purchase Group>Purchasing Organization: <Purchase Organization>Company Code: <Company Code>Target Value: e.g. XXXXX EUR |  |  |
| 5 | Add Items to Scheduling Agreement | From the New Purchase Scheduling Agreement view, choose the Items facets and select Create. | The New Scheduling Agreement Item view displays. |  |
| 6 | Enter Item Data | On the Item facets view, make the following entries:Item category: K (consignment)Plant: <Plant>Material: <Material>Target Quantity: <Target Quantity>Tax Code: XX (Default Value from Info Record)Tax Date: Default TodayNote If the RITA is activated and tax registration countries is maintained for company code in Finance Configuration Step 103464 (Activate RITA and maintain tax registration countries), then the Tax Country can be taken, or you can also choose different Tax Country value from the list.Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration.Choose Apply at the bottom of the view. |  |  |
| 7 | Create | Return to the New Purchase Scheduling Agreement view and choose Create at the bottom of the view.Make a note of the schedule agreement number. | A schedule agreement is created. |  |

### Create Scheduling Agreement for Subcontracting Procurement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Create scheduling agreement for subcontracting procurement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Purchase Scheduling Agreements (F2179). | The Manage Scheduling Agreements list page displays |  |
| 3 | Create Scheduling Agreement | Select Create to create a new scheduling agreement | The New Scheduling Agreement header view displays. |  |
| 4 | Enter Header Data | Create a new scheduling agreement with the following data:Agreement type: LP (Scheduling Agreement)Supplier: <Supplier>Validity Start: Default TodayValidity End: MM/DD/YYYY e.g. today + 720 daysPurchasing Group: <Purchase Group>Purchasing Organization: <Purchase Organization>Company Code: <Company Code>Target Value: e.g. XXXXX EUR |  |  |
| 5 | Add Items to Scheduling Agreement | From the New Purchase Scheduling Agreement view, choose the Items facets and select Create. | The New Scheduling Agreement Item view displays. |  |
| 6 | Enter Item Data | On the Items facets view, make the following entries:Item category: L (Subcontracting)Plant: <Plant>Storage Location: <Storage Location>Material: <Material>Net Order Price: Default Value from Info recordTarget Quantity: <Target Quantity>Tax Code: XX (Default Value from Info Record)Tax Date: Default TodayNote If the RITA is activated and tax registration countries is maintained for company code in Finance Configuration Step 103464 (Activate RITA and maintain tax registration countries), then the Tax Country can be taken, or you can also choose different Tax Country value from the list.Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration.Choose Apply at the bottom of the view. |  |  |
| 7 | Create | Return to the New Purchase Scheduling Agreement view and choose Create at the bottom of the view.Make a note of the schedule agreement number. | A schedule agreement is created. |  |

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
- related-to :: [[10-procurement/mds-bf6-559]]
- related-to :: [[10-procurement/mds-bf6-561]]
- related-to :: [[10-procurement/script-de-dados-mestre-criar-programa-de-remessas-mds-bf6-560]]
- related-to :: [[10-procurement/script-de-datos-maestros-creacion-de-plan-de-entregas-mds-bf6-558]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BF6_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 19,752 chars in the whole document
