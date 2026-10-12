---
id: 09-subscription-billing-and-contract-accounting/master-data-script-create-product-master-for-consumption-based-billing
title: "Master Data Script: Create Product Master for Consumption Based Billing - MDS (3JA) (3JA_S4CLD2608_Master_Data_EN_XX)"
description: SAP S/4HANA Cloud Public Edition 2608 master data script (3JA) for creating a configurable product master with variant pricing for consumption-based billing.
cluster: 09-subscription-billing-and-contract-accounting
tags: [kb/subscription-billing-and-contract-accounting, topic/variant-configured-products-in-provider-contracts]
aliases: [3JA_S4CLD2608_Master_Data_EN_XX]
keywords: [Variant-Configured Products in Provider Contracts, product master, consumption based billing, variant pricing, configurable material, characteristics and classes, configuration profile, material classification, sales data, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3JA_S4CLD2608_Master_Data_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-323
topic: 09-subscription-billing-and-contract-accounting/variant-configured-products-in-provider-contracts
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Master Data Script: Create Product Master for Consumption Based Billing - MDS (3JA) (3JA_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3JA_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Variant-Configured Products in Provider Contracts** in Subscription Billing and Contract Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Product Master for Consumption Based Billing - MDS (3JA) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233904600)

[2 Prerequisites 3](#_Toc233904601)

[2.1 System Access 3](#_Toc233904602)

[2.2 Roles 3](#_Toc233904603)

[2.3 Required Organizational Units 3](#_Toc233904604)

[2.4 Mandatory and Optional Master Data 4](#_Toc233904605)

[2.5 Main Parameters for Data Creation 4](#_Toc233904606)

[2.5.1 Groupings and Number Ranges 4](#_Toc233904607)

[2.5.2 Industry Sector 5](#_Toc233904608)

[3 Overview Table 6](#_Toc233904609)

[4 Test Procedures 7](#_Toc233904610)

[4.1 Create Configurable Material Master - Basic Data 7](#_Toc233904611)

[4.2 Create Characteristic 8](#_Toc233904612)

[4.3 Create Class 10](#_Toc233904613)

[4.4 Create Configuration Profile 11](#_Toc233904614)

[4.5 Create Material Master - Classification 12](#_Toc233904615)

[4.6 Create Variant Pricing 14](#_Toc233904616)

[4.7 Create Product Master Data - Sales Data/Sales Tax Data 15](#_Toc233904617)

## Purpose

In this document you find a description of how to create a material master data record for your SAP S/4HANA Cloud Public Edition system. The description includes those data segments that are relevant for the master data to work in a "usual" system environment. The reader mainly learns which data segments and fields usually need to be filled with input values. Fields that are not relevant for the scope of the SAP S/4HANA Cloud Public Edition content are not described in this document although they may appear on the UI.

A product master record with variant pricing that is created as described here can be used for consumption-based billing.

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

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Product Configuration Modeler | SAP_BR_PRODUCT_CONFIG_MODELER | Variant Configuration | SAP_BR_PRODUCT_CONFIG_MODELER |  |
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Products / Product Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |

### Required Organizational Units

Some segments of master data are dependent on the organizational units of the company, General (Central) Data does not depend on an organizational unit or the company code. The following table gives an overview of these different data segments and their relevant organizational units:

| Data Segment | Depends On | Field Examples | Comments | Organizational Unit to be Used |
| --- | --- | --- | --- | --- |
| Basic Data | Independent of organizational units | Material description (short text), Material number, Material Group, Base Unit of Measure and so on. | Basic Data exists only once for a material master data record. | n/a |
| Sales Data | Plant, Sales Org., Distribution Channel | Tax Data, Item Category Group, and so on. | Plant data can exist for every Plant ID of your enterprise structure for which the material master record is used. | Plant: ____________ Sales Organization: __________ Distribution Channel: __________ |

### Mandatory and Optional Master Data

Master data records may refer to other master data. The following table gives an overview of optional and mandatory master data objects to be used in a master data record.

|  |
| --- |
| Note Brazil specific fields are required to get a proper tax calculation.Check Nota Fiscal Brazil - JD0 in Define BR Specific Fields for Master Data chapter for material master data. |

| Master Data Object | Used in Data Segment | Mandatory / Optional | Comments |
| --- | --- | --- | --- |
|  |  |  |  |
|  |  |  |  |

### Main Parameters for Data Creation

In this section, we describe some basic parameters that influence the behavior of a master record and are always required to create a material master data record:

#### Groupings and Number Ranges

With the help of material types, the system determines which data segments (views) can be maintained or which fields are mandatory or optional. Based on material types, the system also determines the number ranges for materials. In the SAP standard content, all material types use the same number range definition

#### Industry Sector

The standard content only provides one industry sector M. Currently this is visible in the SAP GUI only

## Overview Table

This master record consists of several segments provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Segment | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Configurable Material Master - Basic Data](#unique_11) [page ] 7 | Master Data Specialist - Product Data | Create Material (MM01) | Material Master Data – Basic Data is created. |
| [Create Characteristic](#unique_12) [page ] 8 | Product Configuration Modeler | Manage Characteristics (CT04) | Characteristic is created. |
| [Create Class](#unique_13) [page ] 10 | Product Configuration Modeler | Manage Classes (CL02) | Class is created. |
| [Create Configuration Profile](#unique_14) [page ] 11 | Product Configuration Modeler | VC Modeling Environment (PMEVC) | Configuration profile is created. |
| [Create Material Master - Classification](#unique_15) [page ] 12 | Master Data Specialist - Product Data | Create Material (MM01) | Material Master Data – Classification is created. |
| [Create Variant Pricing](#unique_16) [page ] 14 | Product Configuration Modeler | VC Modeling Environment (PMEVC) | Variant condition is mapped to a characteristic value. |
| [Create Product Master Data - Sales Data/Sales Tax Data](#unique_17) [page ] 15 | Master Data Specialist - Product Data | Create Material (MM01) | Material Master Data – Sales Data (Sales Tax Data) is created. |

## Test Procedures

This section describes procedures for each segment or process step that is part of this master record.

### Create Configurable Material Master - Basic Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create basic data view for the material master.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Material (MM01). | The app opens. |  |
| 3 | Enter Material Basic Data | On the Create Material (Initial Screen) screen, make the following entries:Material: <CBPTS001>Industry sector: MNote If the Industry Sector input field is hidden, no entry is required. When the industry sector is not offered for entry, the field is populated with in the dark.Material Type: KMAT - Configurable materials | The Select View(s) screen displays. |  |
| 4 | Select Views | On the Select View(s) screen, select Basic data 1 and Basic data 2, and choose Continue. | The Create Material (Configurable Materials) screen displays. |  |
| 5 | Enter Basic Data | On the Create Material CBPTS001 (Configurable materials) screen, on the Basic data 1 tab, enter the material description (short text).For example, enter <Consumption-Based Power Tools>. |  |  |
| 6 | Enter Basic Data | On the Basic data 1 tab, in the General Data section, make the following entries:Base Unit of Measure: <PC>GenItemCatGroup: <0003> |  |  |
| 7 | Enter Basic Data | In the Dimensions/EANs section, make the following entry:Unit of Weight: KGChoose the Basic Data 2 tab. |  |  |
| 8 | Enter Basic Data | On the Basic Data 2 tab, you do not have to make any entry.Press Enter. | The Last data view reached screen displays with the message: You are about to exit. Do you want to save your data for this material first?. |  |
| 9 | Save Your Data | On the Last data view reached screen, choose Yes. | The Create Material (Initial Screen) screen displays.The basic data is created and saved. |  |

### Create Characteristic

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create a characteristic.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Configuration Modeler. | The SAP Fiori launchpad displays. |  |
| 2 | Open Manage Customer Master Data | Open Manage Characteristics (CT04). | The app opens. | Common screen for create, change, and display mode. |
| 3 | Enter the Characteristic Name | Make the following entry and choose Create:Characteristic: <CATEGORY> | The Create Characteristic screen displays. | The value in the Valid from field is auto-populated.If the characteristic <CATEGORY> already exists, then create the characteristic <CATEGORY>_Vnn, where nn is the running number. |
| 4 | Enter Basic Data | On the Basic data tab, make the following entries:The Basic data section:Description: <Category>Status: Released (default)The Format section:Data Type: Character FormatNumber of Chars: <15>Case Sensitive: <de-selected>The Value assignment section:Select the Single-value radio button.De-select the Restrictable checkbox. |  |  |
| 5 | Enter Values | On the Values tab, in the Allowed Values section, make the following entries.Char. Value:<STANDARD><HIGH_END>Description:<Standard Power Tools><High End Power Tools>Select the Default Value check box for the <STANDARD> value. |  |  |
| 6 | Save the Characteristic | Choose Save. | The characteristic is created. |  |
| 7 | Create Another Characteristic | Make the following entry and choose Create:Characteristic: <CATEGORY_VARCOND> |  |  |
| 8 | Enter Basic Data | On the Basic data tab, make the following entries:The Basic data section:Description: <Variant Condition Key>Status: Released (default)The Format section:Data Type: Character FormatNumber of Chars: <26>Case Sensitive: <selected>The Value assignment section:Select the Multiple Values radio button.De-select the Restrictable checkbox. |  |  |
| 9 | Enter Addnl Data | On the Addnl data tab, make the following entries:The Reference to Table Field section:Table Name: SDCOMField Name: VKONDThe Behavior for Value Assignment section:Not Ready for Input: <de-selected> |  |  |
| 10 | Save the Characteristic | Choose Save. |  |  |

### Create Class

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create a class with the class type - 300.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Configuration Modeler. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Classes (CL02). | The app opens. | Common screen for create, change, and display mode. |
| 3 | Enter Class Name | Make the following entries and choose Create:Class: <CATEGORY>Class Type: 300 | The Create Class screen displays. | The value in the Valid from field is auto-populated.If the class <CATEGORY> already exists, then create the class <CATEGORY>_Vnn, where nn is the running number. |
| 4 | Enter Basic Data | On the Basic data tab, make the following entries:In the Basic data section:Description: <Power Tools Category>Status: Released (default)In the Same classification section:Select the Do not check radio button (default). |  | If you use the same classification, then you can choose the way of checking (warning message, error, none). |
| 5 | Enter Char. | On the Char. tab, make the following entries:Char.: <CATEGORY>Char.: <CATEGORY_VARCOND> |  |  |
| 6 | Save the Class | Choose Save. | The class is created. |  |

### Create Configuration Profile

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create a configuration profile.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Configuration Modeler. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open VC Modeling Environment (PMEVC). | The app opens. |  |
| 3 | Enter Configuration Model Data | On the initial screen, make the following entries and choose Enter Model:Material: <CBPTS001>Class Type: 300 (Default) | The configuration screen displays. |  |
| 4 | Create Configuration Profile | In the Object section, right-click <CBPTS001> and choose Create Configuration Profile.In the Create Configuration Profile dialog box, make the following entry:Configuration Profile: <CBPT_CP_V01>Choose Continue. | The Configuration Profile screen displays in the right panel and the Basic Data tab is selected. |  |
| 5 | Save the Configuration Profile | Choose Save. | The configuration profile is created. |  |

### Create Material Master - Classification

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create classification view for the material master.

Prerequisite

You must complete the steps in the previous section, [Create Configurable Material Master - Basic Data](#unique_11) [page ] 7, before you proceed with this section. Begin the procedure after you have saved the Basic Data entries, as described in the previous procedure.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Material (MM01). | The app opens. |  |
| 3 | Enter Material Basic Data | On the Create Material (Initial Screen), make the following entries:Material: <CBPTS001>Industry sector: MNote If the Industry Sector input field is hidden, no entry is required. When the industry sector is not offered for entry, the field is populated within the dark.Material Type: KMAT – Configurable materials | The Select View(s) screen displays. |  |
| 4 | Select Views | On the Select View(s) screen, select Classification and choose Continue. | The Class Type (1) screen displays. |  |
| 5 | Enter Class Type | In the Restrictions level section, make the following entries and choose Continue:Class type description: VariantsType: 300 | The Classification screen displays. |  |
| 6 | Enter Classification Data | On the Classification screen, under the Assignments tab, enter the following data in the Class column and choose Save:<CATEGORY>Under the Values for Class CATEGORY - object <CBPTS001> tab, enter the following data in the Value column and choose Save:<STANDARD><HIGH_END> | Your data is saved. |  |

### Create Variant Pricing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The variant condition is mapped to a characteristic value.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Configuration Modeler. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open VC Modeling Environment (PMEVC). | The app opens. |  |
| 3 | Enter Configuration Model Data | On the initial screen, make the following entries and choose Enter Model Maintenance:Material: <CBPTS001>Class Type: 300 (Default) | The configuration screen displays. |  |
| 4 | Create Variant Pricing | In the Object section, double-click <CBPTS001> and choose the Variant Pricing tab in the right panel.Choose Change and make the following entries:Characteristic: <CATEGORY>Char. Value: <HIGH_END>Variant Cond: <HIGH_END> |  |  |
| 5 | Save the Configuration | Choose Save. | The variant pricing is created. |  |

### Create Product Master Data - Sales Data/Sales Tax Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create sales data view for the material master.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Material (MM01). | The app opens. |  |
| 3 | Enter Material Basic Data | On the Create Material (Initial Screen), make the following entries:Material: <CBPTS001>Industry sector: MNote If the Industry Sector input field is hidden, no entry is required. When the industry sector is not offered for entry, the field is populated with in the dark.Material Type: KMAT - Configurable materials | The Select View(s) screen displays. |  |
| 4 | Choose Views | On the Select View(s) screen, select Sales: Sales Org. Data 1, Sales: Sales Org. Data 2, and Sales: General/Plant Data, and then choose Continue. | The Organizational Levels screen displays. |  |
| 5 | Enter Organizational Levels Data | On the Organizational Levels screen, in the Organizational levels section, make following entries and choose Continue:Plant: For example, <1010>.Sales Org.: For example, <1010 for plant 1010>.Distr. Channel: For example, <10>. | The Create Material (Configurable Materials) screen displays.You get the following system message at the bottom of the screen: The material already exists and will be extended. |  |
| 6 | Enter Sales Data | On the Create Material CBPTS001 (Configurable materials) screen, under the Sales: sales org. 1 tab, enter an appropriate value for Tax classification.Usually, this is value 1 for fully taxable.Press Enter. | The Sales: sales org. 2 tab displays.The entered value indicates that the material is (usually) fully taxable. |  |
| 7 | Enter Sales Data | On the Sales: sales org 2 tab, in the Grouping terms section, make the following entry and press Enter:Item category group: <0003> | The Sales: General/ Plant tab displays. |  |
| 8 | Enter Sales Data | On the Sales: General/Plant tab, in the General data section, make the following entry and press Enter:Availability check: For example, <NC>. | The Last data view reached screen displays with the message: You are about to exit. Do you want to save your data for this material first?. |  |
| 9 | Save Your Data | Choose Yes on the Last data view reached screen. | The Master Data - Product screen displays.Your data is saved. |  |

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
- related-to :: [[09-subscription-billing-and-contract-accounting/mds-3ja-325]]
- related-to :: [[09-subscription-billing-and-contract-accounting/mds-3ja-327]]
- related-to :: [[09-subscription-billing-and-contract-accounting/script-de-dados-mestre-criar-dados-mestre-do-produto-para-faturamento]]
- related-to :: [[09-subscription-billing-and-contract-accounting/script-de-datos-maestros-creacion-de-maestro-de-productos-para-factura]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3JA_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 24,339 chars in the whole document
