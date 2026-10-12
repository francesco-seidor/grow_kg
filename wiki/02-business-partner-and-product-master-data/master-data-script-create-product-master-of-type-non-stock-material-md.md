---
id: 02-business-partner-and-product-master-data/master-data-script-create-product-master-of-type-non-stock-material-md
title: "Master Data Script: Create Product Master of type \"Non-Stock Material\" - MDS (31Y) (31Y_S4CLD2608_Master_Data_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition 2608 master data script (31Y) for creating a non-stock material (NLAG) product master: basic, sales, purchasing, accounting data."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/product-master-non-stock-and-service]
aliases: [31Y_S4CLD2608_Master_Data_EN_XX]
keywords: ["Product Master: Non-Stock Materials and Service Products", product master, non-stock material, sales data, purchasing data, accounting data, material type, number ranges, organizational units, industry sector]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/31Y_S4CLD2608_Master_Data_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-311
topic: 02-business-partner-and-product-master-data/product-master-non-stock-and-service
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Master Data Script: Create Product Master of type "Non-Stock Material" - MDS (31Y) (31Y_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/31Y_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Product Master: Non-Stock Materials and Service Products** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Product Master of type "Non-Stock Material" - MDS (31Y) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233904597)

[2 Prerequisites 3](#_Toc233904598)

[2.1 System Access 3](#_Toc233904599)

[2.2 Roles 3](#_Toc233904600)

[2.3 Required Organizational Units 3](#_Toc233904601)

[2.4 Mandatory and Operational Master Data 4](#_Toc233904602)

[2.5 Main Parameters for Data Creation 4](#_Toc233904603)

[2.5.1 Material Type and Number Ranges 5](#_Toc233904604)

[2.5.2 Industry Sector 5](#_Toc233904605)

[3 Overview Table 6](#_Toc233904606)

[4 Test Procedures 7](#_Toc233904607)

[4.1 Create Material (Non-Stock Material) Master Data - Basic Data 7](#_Toc233904608)

[4.2 Create Material (Non-Stock Material) Master Data - Sales Data (Sales Tax Data) 9](#_Toc233904609)

[4.3 Create Material (Non-Stock Material) Master Data - Purchasing Data 13](#_Toc233904610)

[4.4 Create Material (Non-Stock Material) Master Data - Accounting Data (Valuation Area Data) 15](#_Toc233904611)

## Purpose

The material or product master contains information about all the physical materials that are procured, produced, stored and sold. It is also used to manage information about services e.g. for buying and selling services in hours.

The material master holds information such as unique material number, name, material type, unit of measure, descriptions, weight and dimensions. This material information is used and stored in transactions such as sales orders, deliveries, purchase orders and goods movements.

As all information for one material is stored centrally, material master information is organized into different views. For example, sales, storage, MRP, costing and accounting.

Some information in each material is specific to particular organizational units. For example, a sales description is specific to a sales unit (known as sales area), a MRP controller is specific to a specific site (known as a plant) or some information might be specific to a storage location.

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
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Products / Product Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |

### Required Organizational Units

Some segments of material master data are dependent on the organizational units of the company, General (Central) Data does not depend on an organizational unit or the company code. The following table gives an overview of these different data segments and their relevant organizational units:

| Data Segment | Depends On | Field Examples | Comments | Organizational Unit to be Used |
| --- | --- | --- | --- | --- |
| Basic Data | Independent from organizational units | Material description (short text), Material number, Material Group, Base Unit of Measure, and so on. | Basic Data exists only once for a material master data record. | n/a |
| Sales Data | Plant, Sales Org., Distribution Channel | Tax Data, Item Category Group, Transp. Group, Loading Group, Setup Time, and so on. | Sales data can exist for every Sales Org. of your enterprise structure for which the material master record is used. | Plant:____________Sales Organization:__________Distribution Channel:__________ |
| Purchasing Data | Plant | Purchasing Group, Material Group, GR processing time, and so on. | Purchasing Data can exist for every purchasing organization for which the material shall be used in purchasing processes. | Plant:__________ |
| Accounting Data | Valuation area (=Plant), Valuation type | Valuation Class, Per Unit Price, Price Control, and so on. | Valuation area data can exist for every Plant ID of your enterprise structure for which the material master record is used. Every plant represents a valuation area (e.g. different valuation price of a material in different plants) | Plant:____________Valuation type:__________ |

### Mandatory and Operational Master Data

Material master data records may refer to other master data. The following table gives an overview of optional and mandatory master data objects to be used in a material master data record.

|  |
| --- |
| Note Brazil specific fields are required to get a proper tax calculation.Check Nota Fiscal Brazil - JD0 in Define BR Specific Fields for Master Data chapter for material master data. |

| Master Data Object | Used in Data Segment | Mandatory / Optional | Comments |
| --- | --- | --- | --- |
| Profit Center |  | Mandatory | Assigning a Profit Center to a material (product) master is required for correct valuation processes. |

### Main Parameters for Data Creation

In this section, we describe some basic parameters that influence the behavior of a master record and are always required to create a material master data record.

#### Material Type and Number Ranges

With the help of material types, the system determines which data segments (views) can be maintained or which fields are mandatory or optional. Based on material types, the system also determines the number ranges for materials. In the SAP standard content, all material types use the same number range definition.

| Number Range | Range / Business Partner ID | Comments |
| --- | --- | --- |
| External alpha-numeric | A – ZZZZZZZZ | This range must start with a character. Overall the ID must not be longer than 40 characters. |
| Internal numeric | 1 – 99999999 | This range is used if the system shall automatically assign a numeric number to a material. |

#### Industry Sector

The standard content only provides one industry sector M. Currently, this is visible in the SAP GUI only.

## Overview Table

In this section, you provide a list of steps a user goes through when creating a master data record. Every logical, meaningful segment of a master data object should lead to a separate step (e.g. org. unit dependent data segments etc.).

This scope item consists of several process steps that are listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction / App | Expected Results |
| --- | --- | --- | --- |
| [Create Material (Non-Stock Material) Master Data - Basic Data](#unique_11) [page ] 7 | Master Data Specialist - Product Data | Create Material (MM01)/ Manage Product Master Data (F1602) | Material Master Data - Basic Data is created. |
| [Create Material (Non-Stock Material) Master Data - Sales Data (Sales Tax Data)](#unique_12) [page ] 9 | Master Data Specialist - Product Data | Create Material (MM01)/ Manage Product Master Data (F1602) | Material Master Data - Sales Data is created. |
| [Create Material (Non-Stock Material) Master Data - Purchasing Data](#unique_13) [page ] 13 | Master Data Specialist - Product Data | Create Material (MM01)/ Manage Product Master Data (F1602) | Material Master Data - Purchasing Data is created. |
| [Create Material (Non-Stock Material) Master Data - Accounting Data (Valuation Area Data)](#unique_14) [page ] 15 | Master Data Specialist - Product Data | Create Material (MM01)/ Manage Product Master Data (F1602) | Material Master Data - Accounting Data (Valuation Area Data) is created. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Material (Non-Stock Material) Master Data - Basic Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating material (product) master data. Apps available to you are dependent upon your assigned role, so two options are provided.

Procedure: Option 1 - Create Material

Use the following procedure when your user access presents you with the Create Material (MM01) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad appears. |  |
| 2 | Access the SAP Fiori App | Choose Create Material (MM01). | The Create Material (MM01) screen displays. |  |
| 3 | Enter Material Basic Data | In the Create Material (Initial screen)Material : Material numberIndustry sector: MNote If the Industry Sector input field is hidden, no entry is required. When the industry sector is not offered for entry, the field is populated with in the dark.Material type: Non-Stock MaterialClick on Select View(s). | A new window appears, Select View(s). |  |
| 4 | Choose Views | In Select View(s), select Basic data 1 and choose continue. | Create Material...(Non-Stock Material) opens. |  |
| 5 | Enter Basic Data | From Material...(Non-Stock Material), on the Basic data 1 tab, enter a Material description (short text). |  |  |
| 6 | Enter Basic Data | From the Basic data 1 tab in the General Data section, enter the descriptions for the following:Base Unit of MeasureMaterial GroupGenItemCatGroup |  |  |
| 7 | Save Your Data | At the bottom right of the display, choose Save to save your data. | The Create Material (Initial Screen) appears.The Basic Data is created and saved. |  |

Procedure: Option 2 - Manage Product Master Data

Use the following procedure when your user access presents you with the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad appears. |  |
| 2 | Access the SAP Fiori App | Open Manage Product Master Data (F1602). |  |  |
| 3 | Choose Create New Product Master | Choose Create. | The Create Master Data Record screen displays. |  |
| 4 | Enter Data for Mandatory Fields | In the Create Master Data Record initial screen, make the following entries:Product Number: for example,Z …You either enter any external alphanumeric ID, and that ID must start with an alphanumeric character, or if you provide no entry, the system automatically assigns a numeric ID.For more information about Product Number, see the previous Material Type and Number Ranges section.Product Type: NLAGProduct Group: for example, YBPM01Base Unit: for example, PCDescription: any description |  |  |
| 5 | Choose OK | In the Manage Product Master view, choose OK. | The Manage Product Master view displays. |  |
| 6 | Enter Basic Data | In the Manage Product Master > BASIC DATA > Basic Data view, make the following entry:Division: for example 00 |  |  |
| 7 | Choose Add (+) | In the Manage Product Master > BASIC DATA > Descriptions view, screen, choose + (Add). | The Product Master- Description view appears.Some fields are already populated with data from previous step. |  |
| 8 | Enter Descriptions Data | In the Descriptions view, make the following entries:Language: for example, GermanProduct Description: <your description> |  |  |
| 9 | Save Your Data | Choose Save. | System message displays that object is saved. |  |

### Create Material (Non-Stock Material) Master Data - Sales Data (Sales Tax Data)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating material (Non-Stock Material) master data. Apps available to you are dependent upon your assigned role, so two options are provided.

Prerequisite

You must complete the previous section, Creating Material (Non-Stock Material) Master Data - Basic Data, before you proceed with this section.

Begin the procedure after you have saved the Basic Data entries, as described in the previous procedure.

Procedure: Option 1 - Create Material

Use the following procedure when your user access presents you with the Create Material (MM01) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad appears. |  |
| 2 | Access the SAP Fiori App | Open Create Material (MM01). | The Create Material (MM01) view displays. |  |
| 3 | Enter Material Basic Data | In the Create Material (Initial view) make the following entries:Material: Material numberIndustry sector: MNote If the Industry Sector input field is hidden, no entry is required. When the industry sector is not offered for entry, the field is populated with in the dark.Material type: NLAG Non-Stock MaterialClick on Select View(s). | After completing entries, a new window opens, Select View(s) |  |
| 4 | Choose Views | In the Select View(s) window select Sales: Sales Org. Data 1, Sales: Sales Org. Data 2 and Sales: General/Plant Data and choose continue.Note For Poland only: also select Foreign Trade - Export Data in order to enter PKWiU classification number. | A window with Organizational Levels displays |  |
| 5 | Enter Organizational Levels Data | In Organizational Levels, in the Organizational level section, enter descriptions for the following:PlantSales Org.Distr. ChannelChoose Continue.Note Information appears at the bottom of the view: The material already exists and will be extended. | Create Material…(Non-Stock Material) view displays.. |  |
| 6 | Enter Sales Data | In Material...(Non-Stock Material), from the Sales: sales org. 1 tab, in the General data section, make the following entry:Base Unit of MeasureDelivering Plant |  |  |
| 7 | Enter Sales Data | In Material…(Non-Stock Material), from the Sales: sales org. 1 tab, in the Tax Data section, make the following entriesTax classification: 1Note The entered value indicated that the material is (usually), fully taxable.For Brazil only: in the Tax Data section make the following entries:Country: BRTax Category: IBRXFiscal Classification: Either 1 for material or 2 for services | Sales: sales org. 2 tab displays |  |
| 8 | Enter Sales Data | On the Sales: sales org 2 tab, in the Grouping terms section, make the following entries:Gen. item cat. grpItem category groupAcct Assmt Grp Mat. | The next tab, Sales: General/Plant displays. |  |
| 9 | Enter Sales Data | On the Sales: General/Plant tab, in the Shipping data section, enter following data:LoadingGrp |  |  |
| 10 | Enter Sales Data | On the Sales: General/Plant tab, in the General plant parameters section, enter following data:Profit Center |  |  |
| For Poland Only | Enter Sales Data | In the International Trade: Export section, enter the following data:Control code: for example, 26.70.13.0 | PKWiU code for Poland is maintained. |  |
| 11 | Save Your Data | At the bottom of the screen, choose Save. | Your data is saved. |  |

Procedure: Option 2 - Manage Product Master Data

Use the following procedure when your user access presents you with the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad appears. |  |
| 2 | Access the SAP Fiori App | Open Manage Product Master Data (F1602). | The Manage Product Master Data (F1602) screen displays. |  |
| 3 | Search and Open the Product for Edit | Search the previously created Product by entering Product Number in the Product search field.Select the Product from the list which will navigate you to Product view.Click on Edit. | Product is displayed in edit mode (fields are ready for your input). |  |
| 4 | Choose Distributions Chains | In the Product view, choose Distribution Chains tab. | The Distribution Chains tab displays. |  |
| 5 | Choose Add (+) | In the Distribution Chains tab, choose + (Add) | Distribution Chains opens in Edit Mode. |  |
| Not Relevant for Brazil | Enter Distribution Chains Data | In Distribution Chains, make following entries:In the GENERAL DATA - General Information section:Sales Organization: Sales org numberNote The organization unit value is determined by what is offered in the value help.Distribution Channel: for example 10Delivery Plant: Plant numberIn the GROUPING TERMS section:Item Category Group: for example, NLAGIn the SALES TAX view section:Country: country codeTax Category: for example, TTX1Tax Classification: for example, either 1 for material or 2 for services. Tax Classification example: 1 Full tax when using UTXJ tax condition for the US.Note Tax classification depends on the specific requirements of the country/region. Tax classification in the material master and customer master tables determine percentage inputs. |  |  |
| 6 | Return to Main View | Choose Apply to return to the Product view. | The Product view appears. |  |
| 7 | Save Your Data | Choose Save. | System message appears that the object is saved. |  |

### Create Material (Non-Stock Material) Master Data - Purchasing Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating material (Non-Stock Material) master data. Apps available to you are dependent upon your assigned role, so two options are provided.

Prerequisite

You must complete the previous procedure, Creating Material (Non-Stock Material) Master Data - Basic Data, before you proceed with this section.

Begin the procedure after you have saved the Basic Data entries, as described in the prior procedure.

Procedure: Option 1 - Create Material

Use the following procedure when your user access presents you with the Create Material (MM01) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad appears. |  |
| 2 | Access the SAP Fiori App | Open Create Material (MM01). | The app opens. |  |
| 3 | Enter Material Basic Data | On the Create Material (Initial screen), make the following entries:Material: Material numberIndustry sector: MNote If the Industry Sector input field is hidden, no entry is required. When the industry sector is not offered for entry, the field is populated with in the dark.Material type: NLAG Non-Stock MaterialChoose Select View(s). | The Select View(s) screen displays. |  |
| 4 | Choose Views | On the Select View(s) screen, select Purchasing and choose Continue. | The Organizational Levels screen displays. |  |
| 5 | Enter Organizational Levels Data | On the Organizational Levels screen, in the Organizational level section, make the following entry:Plant: Plant numberChoose Continue.Note A message displays at the bottom of the screen: The material already exists and will be extended. | The Create Material…(Non-Stock Material) screen displays. |  |
| 6 | Enter Purchasing Data | On the Material…(Non-Stock Material) screen, on the Purchasing tab, in the General Data section, make the following entries:Base Unit of Measure: for example, HMaterial Group: for example, YBPM02Purchase Group: for example, 001Tax ind. f. material: for example, 1 |  |  |
| Not Relevant for Brazil | Enter Purchasing Data | On the Material…(Non-Stock Material) screen, on the Purchasing tab, in the Other data / manufacturer data section, make the following entry:GR Processing Time: for example, 1 |  |  |
| 7 | Save Your Data | At the bottom of the screen, choose Save. | Your data is saved. |  |

Procedure: Option 2 - Manage Product Master Data

Use the following procedure when your user access presents you with the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad appears. |  |
| 2 | Access the SAP Fiori App | Open Manage Product Master Data (F1602). | The app opens. |  |
| 3 | Search and Open the Product for Edit | Search the previously created product by entering Product Number in the Product search field.Select the product from the list which will navigate you to the Product view.Choose Edit. | Product is displayed in edit mode (fields are ready for your input). |  |
| 4 | Choose Edit Header | In the Edit Header view, choose Maintain Product Group.Choose OK. |  |  |
| 5 | Enter Purchasing Data | In the Purchasing view, make the following entry:Purchasing Value Key: for example, 1 |  |  |
| 6 | Save Your Data | Choose Save. | System message indicates that the object is saved. |  |

### Create Material (Non-Stock Material) Master Data - Accounting Data (Valuation Area Data)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating material (Non-Stock Material) master data. Apps available to you are dependent upon your assigned role, so two options are provided.

Prerequisite

You must complete the previous procedure, Create Material (Non-Stock Material) Master Data - Basic Data, before you proceed with this section.

Begin the procedure after you have saved the Basic Data entries, as described in the previous procedure.

Procedure: Option 1 - Create Material

Use the following procedure when your user access presents you with the Create Material (MM01) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad appears. |  |
| 2 | Access the SAP Fiori App | Open Create Material (MM01). | The Create Material (MM01) view displays. |  |
| 3 | Enter Material Basic Data | In the Create Material (Initial screen) make the following entries:Material : Material numberIndustry sector: MNote If the Industry Sector input field is hidden, no entry is required. When the industry sector is not offered for entry, the field is populated with in the dark.Material type: NLAG Non-Stock MaterialClick on Select View(s). | Select View(s) opens. |  |
| 4 | Choose Views | In Select View(s), select the following views:Accounting 1Accounting 2Choose Continue. | Organizational Levels opens. |  |
| 5 | Enter Organizational Levels Data | In the Organizational Levels screen, in the Organizational level section, make following entries:PlantNote Information appears at the bottom of the screen: The material already exists and will be extended. | Create Material…(Non-Stock Material) opens. |  |
| 6 | Enter Accounting Data | In the Create Material…(Non-Stock Material) screen, on the Accounting 1 tab, in the Current valuation Data section, make the following entry:Valuation Class: for example, YB01Price Control: for example, SMoving price: for example, 1Price Unit: for example, 1 |  |  |
| Not Relevant for Brazil | Confirm Entries | You are not required to make entries in Accounting 2 tab. |  |  |
| 7 | Save Your Data | From the bottom of the display, choose Save. | The Master Data-Product window appears.Your data is saved. |  |

Procedure: Option 2 - Manage Product Master Data

Use the following procedure when your user access presents you with the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad appears. |  |
| 2 | Access the SAP Fiori App | Open Manage Product Master Data (F1602). | The Manage Product Master Data (F1602) screen displays. |  |
| 3 | Search and Open the Product for Edit | Search the previously created Product by entering Product Number in the Product search field.Select the Product from the list which will navigate you to Product view.Click on Edit. | Product is displayed in edit mode (fields are ready for your input). |  |
| 4 | Choose Valuation Area Data | In the Product view, choose Valuation Areas tab. | The Valuation Areas tab displays. |  |
| 5 | Choose Add (+) | In the Valuation Areas section, choose + (Add). | Valuation opens in Edit Mode. |  |
| 6 | Enter Valuation Area Data | In Valuation view, make following entries:Valuation Area: valuation area numberValuation Class: for example, YB01 |  |  |
| Not Relevant for Brazil | Enter Current Valuation Area Data | In VALUATION AREAS > Valuation > Current Period , make the following entries:Inventory PricePrice Control: for example, S |  |  |
| 7 | Return to Main Screen | Choose Apply to return to Product view. | Manage Product Master view displays. |  |
| 8 | Save Your Data | Choose Save. | System message indicates that the object is saved. |  |

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
- related-to :: [[02-business-partner-and-product-master-data/master-data-script-creating-non-stock-material-product-master-data-31y]]
- related-to :: [[02-business-partner-and-product-master-data/mds-31y-313]]
- related-to :: [[02-business-partner-and-product-master-data/script-de-dados-mestre-criar-mestre-de-produtos-do-tipo-material-nao-e]]
- related-to :: [[02-business-partner-and-product-master-data/script-de-datos-maestros-creacion-de-maestro-de-productos-de-tipo-mate]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/31Y_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 29,880 chars in the whole document
