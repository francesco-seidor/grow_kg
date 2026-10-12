---
id: 02-business-partner-and-product-master-data/master-data-script-create-product-master-of-type-configurable-material
title: "Master Data Script: Create Product Master of Type \"Configurable Material\" - MDS (2T7) (2T7_S4CLD2608_Master_Data_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script (2T7) for creating a KMAT configurable material master via MM01 or F1602, view by view."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/variant-configuration-master-data]
aliases: [2T7_S4CLD2608_Master_Data_EN_XX]
keywords: [Configurable Materials and Characteristic Display, configurable material, product master data, material type, sales data, purchasing data, classification, mrp planning data, work scheduling, storage location data]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2T7_S4CLD2608_Master_Data_EN_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-281
topic: 02-business-partner-and-product-master-data/variant-configuration-master-data
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Master Data Script: Create Product Master of Type "Configurable Material" - MDS (2T7) (2T7_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2T7_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Configurable Materials and Characteristic Display** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Product Master of Type "Configurable Material" - MDS (2T7) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc233904564)

[2 Prerequisites 4](#_Toc233904565)

[2.1 System Access 4](#_Toc233904566)

[2.2 Roles 4](#_Toc233904567)

[2.3 Business Conditions 4](#_Toc233904568)

[2.4 Required Organizational Units 5](#_Toc233904569)

[2.5 Mandatory and Optional Master Data 6](#_Toc233904570)

[2.6 Main Parameters for Data Creation 6](#_Toc233904571)

[2.6.1 Material Type and Number Ranges 6](#_Toc233904572)

[2.6.2 Industry Sector 7](#_Toc233904573)

[3 Overview Table 8](#_Toc233904574)

[4 Test Procedures 9](#_Toc233904575)

[4.1 Create Product Master Data - Basic Data 9](#_Toc233904576)

[4.2 Create Product Master Data - Sales Data / Sales Tax Data 12](#_Toc233904577)

[4.3 Create Product Master Data - Purchasing Data 15](#_Toc233904578)

[4.4 Create Product Master Data - Classification 17](#_Toc233904579)

[4.5 Create Product Master Data - MRP Planning Data / Plant Data 18](#_Toc233904580)

[4.6 Create Product Master Data – Work Scheduling 22](#_Toc233904581)

[4.7 Create Product Master Data - Storage Location Data 24](#_Toc233904582)

[4.8 Create Product Master Data - Accounting Data / Valuation Area Data 26](#_Toc233904583)

[4.9 Create Product Master Data – Costing 29](#_Toc233904584)

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

### Business Conditions

Before this Master Data Script can be tested, the following business condition must be met.

|  |
| --- |
| Note Scope Item 22T - Set Up Configurable Model Using Variant Configuration is a prerequisite for this Master Data Script. |

### Required Organizational Units

Some segments of material master data are dependent on the organizational units of the company, General (Central) Data does not depend on an organizational unit or the company code. The following table gives an overview of these different data segments and their relevant organizational units:

| Data Segment | Depends On | Field Examples | Comments | Organizational Unit to be Used |
| --- | --- | --- | --- | --- |
| Basic Data | Independent of organizational units | Material description (short text), Material number, Material Group, Base Unit of Measure and so on. | Basic Data exists only once for a material master data record. | n/a |
| Classification | Independent of organizational units | Class Type, Class and Class Values | Classification data exists for the class type for which the classification data is used. | n/a |
| Sales Data | Plant, Sales Org., Distribution Channel | Tax Data, Item Category Group, Transp. Group, Loading Group, Setup Time and so on. | Plant data can exist for every Plant ID of your enterprise structure for which the material master record is used. | Plant:____________Sales Organization:__________Distribution Channel:__________ |
| Purchasing Data | Plant | Base Unit of Measure, Material Group | Plant data can exist for every Plant ID of your enterprise structure for which the material master record is used. | Plant:____________ |
| MRP/Planning Data (Plant Data) | Plant, Storage Location | MRP Type, MRP Controller, Lot Size, Planned delivery time and so on. | Plant data can exist for every Plant ID of your enterprise structure for which the material master record is used.Storage location data (planning context) is optional based on the need to do storage location specific planning. | Plant:____________Storage Location:__________ |
| Work Scheduling | Plant | Production Supervisor and Production Schedule Profile | Plant data can exist for every enterprise structure for which the material master record is used. | Plant:_____________ |
| Storage Location Data | Plant, Storage Location | Number of GR slips, Max. Storage Period, Min. Rem. Shelf and so on. |  | Plant:____________Storage Location:__________ |
| Accounting Data (Valuation Data) | Valuation area (=Plant), Valuation type | Valuation Class, Per Unit Price, Price Control and so on. | Valuation area data can exist for every Plant ID of your enterprise structure for which the material master record is used. Every plant represents a valuation area (for example, different valuation price of a material in different plants) | Plant:____________Valuation type:__________ |
| Costing | Plant | Base unit of Measure, Profit Center, Costing lot size, Valuation class, Price control and Price unit. | Costing area data can exist for every Plant ID of your enterprise structure for which the material master record is used. | Plant:____________ |

### Mandatory and Optional Master Data

Material master data records may refer to other master data. The following table provides an overview of optional and mandatory master data objects to be used in a material master data record.

|  |
| --- |
| Note Brazil specific fields are required to get a proper tax calculation.Check Nota Fiscal Brazil - JD0 in Define BR Specific Fields for Master Data chapter for material master data. |

| Master Data Object | Used in Data Segment | Mandatory / Optional | Comments |
| --- | --- | --- | --- |
| Profit Center |  | Mandatory | Assigning a Profit Center to a material (product) master is required for correct valuation processes. |

### Main Parameters for Data Creation

This section describes some basic parameters that influence the behavior of a master record and are always required to create a material master data record:

#### Material Type and Number Ranges

With the help of material types, the system determines which data segments (views) can be maintained or which fields are mandatory or optional. Based on material types, the system also determines the number ranges for materials. In the SAP standard content, all material types use the same number range definition

| Number Range | Range / Business Partner ID | Comments |
| --- | --- | --- |
| External alpha-numeric | A – ZZZZZZZZ | This range must start with a character. Overall the ID must not be longer than 8 digits. |
| Internal numeric | 1 – 99999999 | This range is used if the system shall automatically assign a numeric number to a material. |

#### Industry Sector

The standard content only provides one industry sector M. Currently this is visible in the SAP GUI only.

## Overview Table

This scope item consists of several process steps that are listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction / App | Expected Results |
| --- | --- | --- | --- |
| [Create Product Master Data - Basic Data](#unique_12) [page ] 9 | Master Data Specialist - Product Data | Create Material (MM01) or Manage Product Master Data (F1602) | Material Master Data – Basic Data is created. |
| [Create Product Master Data - Sales Data / Sales Tax Data](#unique_13) [page ] 12 | Master Data Specialist - Product Data | Create Material (MM01) or Manage Product Master Data (F1602) | Material Master Data – Sales Data (Sales Tax Data) is created. |
| [Create Product Master Data - Purchasing Data](#unique_14) [page ] 15 | Master Data Specialist - Product Data | Create Material (MM01) or Manage Product Master Data (F1602) | Material Master Data – Purchasing Data is created. |
| [Create Product Master Data - Classification](#unique_15) [page ] 17 | Master Data Specialist - Product Data | Create Material (MM01) | Material Master Data – Classification is created. |
| [Create Product Master Data - MRP Planning Data / Plant Data](#unique_16) [page ] 18 | Master Data Specialist - Product Data | Create Material (MM01) or Manage Product Master Data (F1602) | Material Master Data – MRP/Planning Data (Plant Data) is created. |
| [Create Product Master Data – Work Scheduling](#unique_17) [page ] 22 | Master Data Specialist - Product Data | Create Material (MM01) | Material Master Data – Work Scheduling is created. |
| [Create Product Master Data - Storage Location Data](#unique_18) [page ] 24 | Master Data Specialist - Product Data | Create Material (MM01) or Manage Product Master Data (F1602) | Material Master Data – Storage Location Data is created. |
| [Create Product Master Data - Accounting Data / Valuation Area Data](#unique_19) [page ] 26 | Master Data Specialist - Product Data | Create Material (MM01) or Manage Product Master Data (F1602) | Material Master Data – Accounting Data (Valuation Data) is created. |
| [Create Product Master Data – Costing](#unique_20) [page ] 29 | Master Data Specialist - Product Data | Create Material (MM01) | Material Master Data – Costing is created. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Product Master Data - Basic Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating product master data. Apps available to you are dependent upon your assigned role, so two options are provided.

Procedure: Option 1 - Create Material

Use the following procedure when your user access presents you with the Create Material (MM01) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Material (MM01). | The Create Material (MM01) displays. |  |
| 3 | Enter Material Basic Data | On the Create Material (Initial view), make the following entries:Material: CM-FL-V01Industry sector: MNote If the Industry Sector input field is hidden, no entry is required. When the industry sector is not offered for entry, the field is populated with in the dark.Material type: KMAT - Configurable materials | The Select View(s) view displays. |  |
| 4 | Choose Views | In the Select View(s) window, select Basic data 1 and Basic data 2 and choose Continue. | The Create Material (Configurable Materials) view displays. |  |
| 5 | Enter Basic Data | On the Create Material CM-FL-V01 (Configurable materials) view, on the Basic data 1 tab, enter the material description (short text).For example: Forklift |  |  |
| 6 | Enter Basic Data | On the Basic data 1 tab, in the General Data section, make the following entries:Base Unit of Measure: PCMaterial Group: L004GenItemCatGroup: 0002 |  |  |
| 7 | Enter Basic Data | In the Dimensions/EANs section, make the following entries:Gross Weight: 3Unit of Weight: KGNet Weight: 2 | The tab Basic Data 2 displays. |  |
| 8 | Enter Basic Data | On the Basic Data 2 tab, you do not have to make any entries. | A new window Last data view reached opens with the message You are about to exit. Do you want to save your data for this material first? |  |
| 9 | Save Your Data | In the Last data view reached window, choose Yes. | The Create Material (Initial Screen) view displays.The Basic Data is created and saved. |  |

Procedure: Option 2 - Manage Product Master Data

Use the following procedure when your user access presents you with the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Product Master Data (F1602). | The app opens. |  |
| 3 | Choose Create New Product Master | In the Manage Product Master Data view, choose Create | Create Master Data Record displays. |  |
| 4 | Enter Data for Mandatory Fields | In the Create Master Data Record view, make the following entries:Product Number: for example, CM-FL-V01 …either any external alphanumeric ID … (at least this needs to start with a character) or when no entry the system assigns a numeric ID automaticallyFor more information about Product Number, see the Material Type and Number Ranges section in Main Parameters for Data CreationProduct Type: KMATProduct Group: for example, L004Base Unit: for example, PCDescription: Forklift |  |  |
| 5 | Choose OK | In the Create Master Data Record view, choose OK. | Product View displays. |  |
| 6 | Enter Basic Data | In the Product > General Information > Basic Data view, make the following entries:Division: for example, 00 |  |  |
| 7 | Choose Descriptions | Go to Product > General Information > Descriptions . | The Descriptions view displays. |  |
| 8 | Choose Add (+) | In the Descriptions view, choose + (Add). | Some fields are already populated. |  |
| 9 | Enter Descriptions Data | In the Descriptions view make the following entries:Language: for example, EnglishProduct Description: <your description> |  |  |
| 10 | Choose Base Unit of Measure | Go to Product > General Information > Base Unit of Measure . |  |  |
| 11 | Enter Base Unit of Measure Data | In the Weight view, make following entries:Weight Unit: for example, KGGross Weight: for example, 2Net Weight: for example, 1Note If the Gross Weight, Weight Unit, or Net Weight fields do not display as input fields, choose See More in the right corner.. |  |  |
| 12 | Save Your Data | Choose Save. | System issue a notification that the object is saved. |  |

### Create Product Master Data - Sales Data / Sales Tax Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating product master data. Apps available to you are dependent upon your assigned role, so two options are provided.

Prerequisite

You must complete the previous section, Create Product Master Data - Basic Data, before you proceed with this section.

Begin the procedure after you have saved the Basic Data entries, as described in the previous procedure.

Procedure: Option 1 - Create Material

Use the following procedure when your user access presents you with the Create Material app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Material (MM01). | The Create Material (MM01) displays. |  |
| 3 | Enter Material Basic Data | In the Create Material (Initial Screen), make the following entries:Material: : CM-FL-V01Industry sector: MNote If the Industry Sector input field is hidden, no entry is required. When the industry sector is not offered for entry, the field is populated with in the dark.Material type: : KMAT - Configurable materials | A new window displays the Select View(s) view. |  |
| 4 | Choose Views | In the Select View(s) window, select Sales: Sales Org. Data 1, Sales: Sales Org. Data 2 and Sales: General/Plant Data and choose Continue. | A new window displays the Organizational Levels. |  |
| 5 | Enter Organizational Levels Data | In the Organizational Levels view, in the Organizational level section, make following entries and choose Continue:Plant: for example, 1710Sales Org.: for example, 1710Distr. Channel: for example, 10 | A new window displays theCreate Material (Configurable Materials) view.You get the following system message at the bottom of the view: The material already exists and will be extended. |  |
| 6 | Enter Sales Data | In the Create Material CM-FL-V01 (Configurable materials) view, under the Sales: sales org. 1 tab enter an appropriate value for the <Tax classification>Usually this is value 1 for fully taxable. | The Sales: sales org. 2 tab displays.The entered value indicates that the material is (usually) fully taxable. |  |
| 7 | Enter Sales Data | On the Sales: sales org 2 tab, in the Grouping terms section make the following entry:Item category group: 0002Matl statistics grp: 1 | You navigated to the next tab, Sales: General/Plant. |  |
| 8 | Enter Sales Data | On the Sales: General/Plant tab, in the General data section, enter the following data:Availability check: for example,SP |  |  |
| 9 | Enter Sales Data | In the Shipping data (times in days) section, enter the following data:Transp. Grp:for example, 0001Loading Grp: for example, 0001 |  |  |
| 10 | Enter Sales Data | In the General Plant parameters section, enter the following data:Profit Center: for example, YB110 or YB111 | A new window displays: Last data view reached with the message You are about to exit. Do you want to save your data for this material first?. |  |
| 11 | Save Your Data | In the Last data view reached window, choose Yes. | The Master Data - Product window displays.Your data is saved. |  |

Procedure: Option 2 - Manage Product Master Data

Use the following procedure when your user access presents you with the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Product Master Data (F1602). |  |  |
| 3 | Choose Edit | Choose Edit.Note This step assumes you are continuing from the previous step and are already on the Manage Product Master Data tile. After you have saved your data from the previous section, the system is in Display Mode. To proceed, you must be in Edit Mode. | Edit Mode (fields are ready for your input). |  |
| 4 | Choose Distributions Chains | In the Product view, choose Distribution Chains. | The Distribution Chains view displays. |  |
| 5 | Choose Add (+) | In the Distribution Chains > Distribution Chains view, choose + (Add) | The Product Master - Distribution Chains view opens in Edit Mode. |  |
| 6 | Enter Distribution Chains Data | In the Product Master - Distribution Chains view make following entries:GENERAL DATA - General InformationSales Organization: <Sales org number> for example, 1710Distribution Channel: for example, 10Delivery Plant: <Plant number> for example, 1710GROUPING TERMSItem Category Group: for example, 0002Accounting Assignment Group: for example, 03 Finished ProductsSALES TAXCountry: <country code> for example, DETax Category: TTX1Tax Classification: Either 1 for material or 2 servicesTax Classification: for example 1 Full tax when using UTXJ tax condition for US.Tax classification depends on the specific country/region requirements. Tax classification in the material master and customer master tables determine tax percentage inputs.For Brazil only in the Tax Classification section, make the following entries:Country: BRTax Category: IBRXTax Classification: Either 1 for material or 2 for services |  |  |
| 7 | Save Your Data | Choose Save. | The system issues a notification indicating the object is saved. |  |

### Create Product Master Data - Purchasing Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

|  |
| --- |
| Note If you want to run the KMAT material with 3rd party process, then extend the purchasing view. |

Procedure: Option 1 – Create Material

Use the following procedure when your user access presents you with the Create Material (MM01)Create Material (MM01) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Material (MM01) | The Create Material (MM01) displays. |  |
| 3 | Enter Material Basic Data | In the Create Material (Initial Screen), make the following entries:Material: : CM-FL-V01Industry sector: MMaterial type: : KMAT - Configurable materials | A new window displays the Select View(s) view. |  |
| 4 | Choose Views | In the Select View(s) window, select Purchasing and choose Continue. | A new window displays the Organizational Levels. |  |
| 5 | Enter Organizational Levels Data | In the Organizational Levels view, in the Organizational level section, make following entries and choose Continue:Plant: for example, 1010 | A new window displays theCreate Material (Configurable Materials) view.You get the following system message at the bottom of the view: The material already exists and will be extended. |  |
| 6 | Enter Purchasing Data | Make sure the following entries are available.Base Unit of Measure: PCMaterial Group: L004 | The Purchasing tab displays |  |
| 7 | Save Your Data | Choose Save. | Your data is saved. |  |

Procedure: Option 2 – Manage Product Master Data

Use the following procedure when your user access presents you with the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Product Master Data (F1602). |  |  |
| 3 | Choose Edit | Choose Edit | Edit Mode (fields are ready for your input). |  |
| 4 | Choose Purchasing view | In the Product Master view, choose Purchasing. | The Purchasing view displays. |  |
| 5 | Enter Purchasing data | In the Purchasing view, make the following entry and choose Save.Order Unit of Measure: PC | The system issues a notification indicating the object is saved. |  |

### Create Product Master Data - Classification

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating product master data. Apps available to you are dependent upon your assigned role, so two options are provided.

Prerequisite

You must complete the previous section, Create Product Master Data – Basic Data, before you proceed with this section.

Begin the procedure after you have saved the Basic Data entries, as described in the previous procedure.

Procedure: Option 1 – Create Material

Use the following procedure when your user access presents you with the Create Material (MM01) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Material (MM01). | The Create Material (MM01) displays. |  |
| 3 | Enter Material Basic Data | In the Create Material (Initial Screen), make the following entries:Material: CM-FL-V01Industry sector: MNote If the Industry Sector input field is hidden, no entry is required. When the industry sector is not offered for entry, the field is populated with in the dark.Material type: KMAT – Configurable materials | A new window displays the Select View(s) view. |  |
| 4 | Choose Views | In the Select View(s) window, select Classification and choose Continue. | A new window displays the Class Type (1) view |  |
| 5 | Enter Organizational Levels Data | In the Restrictions level section, select the following entries and choose Continue:Class type description: VariantsType: 300 | A new window displays the Classification view. |  |
| 6 | Enter Sales Data | In the Classification view, under the Assignments enter the following values under the Class column and choose Save.AVC_CL_ELECADD_V01AVC_CL_REFCSTC_V01AVC_CL_COMMON_V01 | The Classification view window displays.Your data is saved. |  |

Procedure: Option 2 - Manage Product Master Data

|  |
| --- |
| Note The required fields are currently unavailable for this application. Use Option 1 (above) |

### Create Product Master Data - MRP Planning Data / Plant Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating product master data. Apps available to you are dependent upon your assigned role, so two options are provided.

Prerequisite

You must complete a previous procedure, Create Product Master Data - Basic Data, before you proceed with this section.

Begin the procedure after you have saved the Basic Data entries, as described in the previous procedure.

Procedure: Option 1 - Create Material

Use the following procedure when your user access presents you with the Create Material (MM01) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Material (MM01). | The Create Material (MM01) displays. |  |
| 3 | Enter Material Basic Data | On the Create Material (Initial Screen), make the following entries:Material: CM-FL-V01Industry sector: MNote If the Industry Sector input field is hidden, no entry is required. When the industry sector is not offered for entry, the field is populated with in the dark.Material type: KMAT - Configurable materials | The Select View(s) view displays. |  |
| 4 | Choose Views | In the Select View(s) window, select MRP1, MRP2, MRP3 and MRP4 and choose Continue. | The Organizational Levels view displays. |  |
| 5 | Enter Organizational Levels Data | On the Organizational Levels view, in the Organizational level section, make the following entries:Plant: <Plant code> for example 1710Storage Location: for example 171A | The Create Material (Configurable Materials) view displays.You get the following system message at the bottom of the view: The material already exists and will be extended. |  |
| 6 | Enter MRP/Planning Data | On the Material (Configurable Materials) view, on the MRP 1 tab, in the General Data section, make the following entry:Base Unit of Measure: PC |  |  |
| 7 | Enter MRP/Planning Data | In the MRP procedure section, make the following entries:MRP Type: for example, PDMRP Controller: for example, 001 |  |  |
| 8 | Enter MRP/Planning Data | In the Lot Sizing Procedure section, make the following entry:Lot Sizing Procedure: EX | The next tab MRP 2 displays. |  |
| 9 | Enter MRP/Planning Data | In the Create Material CM-FL-V01 (Configurable Material) view, on the MRP 2 tab, make entries based on your needs or at least populate mandatory fields with values, for example, In-house production time in days. | The next tab MRP 3 displays. |  |
| 10 | Enter MRP/Planning Data | In the Create Material (Configurable Materials) view, on the MRP 3 tab, in the Planning section, make the following entries:Strategy Group: for example, 25Consumption mode: for example, 2 |  |  |
| 11 | Enter MRP/Planning Data | In the Availability check section, make the following entries:Availability check: for example, SPTot. repl. Lead time: for example, 3 | The next tab MRP 4 displays. |  |
| 12 | Enter MRP/Planning Data | In the Create Material CM-FL-V01 (Configurable Material) view, on the MRP 4 tab, you do not have to make any entries. | A new window Last data view reached opens with the message You are about to exit. Do you want to save your data for this material first?. |  |
| 13 | Save | In the Last data view reached window, choose Yes. | The Master Data - Product view displays.Your data is saved. |  |

Procedure: Option 2 - Manage Product Master Data

Use the following procedure when your user access presents you with the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Product Master Data (F1602). |  |  |
| 3 | Choose Edit | Choose EditNote This step assumes you are continuing from the previous step and are already on the Manage Product Master Data tile. After you have saved your data from the previous section, the system is in Display Mode. To proceed, you must be in Edit Mode. | Edit Mode (fields are ready for your input). |  |
| 4 | Choose Plants Data | In the Product Master view, choose Plants | The Plants view displays. |  |
| 5 | Choose Add (+) | In the Plants view section, choose + (Add) | The Plant view opens in Edit Mode. |  |
| 6 | Enter Plants – General Information Data | In the Plant > General Data view, make following entries:Plant: <Plant number> for example, 1710Profit Center : for example, YB110 or YB111Loading Grp: for example, 0001 - Forklift |  |  |
| 7 | Choose Plants – MRP Data | In the Plant view, choose MRP Data | The MRP Data view displays. |  |
| 8 | Enter Plants – MRP Data | In the MRP Data view, choose MRP Data and make following entries:Availability Check: for example, SPPlanned Delivery Time: for example, 3Goods Receipt Processing Time: for example, 1MRP Type: For example, PDMRP Controller: For example, 001 |  |  |
| 9 | Choose Plants – Lots-Size Data | In the MRP Data view, choose Lot-Size Data. | The Lot-Size Data view section displays. |  |
| 10 | Enter Plants – Lot-Size Data | In the Lot-Size Data view, make the following entry:Lot Sizing Procedure: for example EX |  |  |
| 11 | Choose Plants – Forecast Data | In the Product > PLANTS view, choose FORECASTING. | FORECASTING displays |  |
| 12 | Enter Plants - Forecast Data | In the FORECASTING view, make the following entry:Period Type: for example, F |  |  |
| 13 | Return to Main View | Choose the back arrow to return to Product Master. | The Product Master view displays. |  |
| 14 | Save Your Data | Choose Save. | System issue a notification that the object is saved. |  |

### Create Product Master Data – Work Scheduling

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating product master data. Apps available to you are dependent upon your assigned role, so two options are provided.

Prerequisite

You must complete the previous section, Create Product Master Data – Basic Data, before you proceed with this section.

Begin the procedure after you have saved the Basic Data entries, as described in the previous procedure.

Procedure: Option 1 – Create Material

Use the following procedure when your user access presents you with the Create Material (MM01) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Material (MM01). | The Create Material (MM01) screen displays. |  |
| 3 | Enter Material Basic Data | In the Create Material (Initial view), make the following entries:Material: CM-FL-V01Industry sector: MNote If the Industry Sector input field is hidden, no entry is required. When the industry sector is not offered for entry, the field is populated with in the dark.Material type: KMAT - Configurable materials | The Select View(s) view displays. |  |
| 4 | Choose Views | In the Select View(s) window, select Work Scheduling, and choose Continue. | The Organizational Levels view displays. |  |
| 5 | Enter Organizational Levels Data | In the Organizational Levels view make the following entry and choose Continue.Plant: 1710 | A new window Change Material CM-FL-V01 (Configurable materials) displays. |  |
| 6 | Enter Work Scheduling Data | In the Change Material CM-FL-V01 (Configurable materials) window, under General Data enter the following entries and choose Save.Base unit of Measurement: PCProdn Supervisor: YB3Prod. Sched. Profile: YB0003 | A new window displays: Last data view reached with the message You are about to exit. Do you want to save your data for this material first? |  |
| 7 | Save Your Data | In the Last data view reached window, choose Yes. | The Master Data – Product window displays.Your data is saved. |  |

Procedure: Option 2 – Manage Product Master Data

|  |
| --- |
| Note The required fields are currently unavailable for this application. Use Option 1 (above) and save your entries. |

### Create Product Master Data - Storage Location Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating product master data. Apps available to you are dependent upon your assigned role, so two options are provided.

Prerequisite

You must complete a previous procedure, Create Product Master Data - Basic Data, before you proceed with this section.

Begin the procedure after you have saved the Basic Data entries, as described in the previous procedure.

Procedure: Option 1 - Create Material

Use the following procedure when your user access presents you with the Create Material (MM01) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Material (MM01). | The Create Material (MM01) displays. |  |
| 3 | Enter Material Basic Data | On the Create Material (Initial view), make the following entries:Material: CM-FL-V01Industry sector: MNote If the Industry Sector input field is hidden, no entry is required. When the industry sector is not offered for entry, the field is populated with in the dark.Material type: KMAT - Configurable materials | The Select View(s) view displays. |  |
| 4 | Choose Views | In the Select View(s) window, select the following views and choose Continue:General Plant Data/Storage 1General Plant Data/Storage 2 | The Organizational Levels view displays. |  |
| 5 | Enter Organizational Levels Data | On the Organizational Levels view, in the Organizational level section, make following entries:Plant: for example, 1710Storage Location: for example, 171A | A new window opens, showing the Create Material (Configurable materials) view.You get the following system message at the bottom of the view: The material already exists and will be extended. |  |
| 6 | Enter Storage Location Data | In the Create Material (Configurable materials) view, on the Plant data/stor. 1 tab, in the General Data section, make the following entry:Number of GR slips: for example, 1 | The next tab displays, Plant data/stor.2. |  |
| 7 | Confirm Entries | On the Plant data/stor. 2 tab, you do not have to make any entries. | A new window Last data view reached opens with the message You are about to exit. Do you want to save your data for this material first?. |  |
| 8 | Save | In the Last data view reached window, choose Yes. | The Master Data - Product window displays.Your data is saved. |  |

Procedure: Option 2 - Manage Product Master Data

Use the following procedure when your user access presents you with the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Product Master Data (F1602). |  |  |
| 3 | Choose Edit | Choose EditNote This step assumes you are continuing from the previous step and are already on the Manage Product Master Data tile. After you have saved your data from the previous section, the system is in Display Mode. To proceed, you must be in Edit Mode. | Edit Mode (fields are ready for your input). |  |
| 4 | Choose Plants Data | In the Product view, choose PLANTS.Note If there is no plant data record, follow the steps in the previous section, Create Product Master Data - MRP Planning Data / Plant Data | The PLANTS view displays. |  |
| 5 | Choose Plant Details | In the PLANTS view, use the arrow icon to select the plant data you created in the previous step. | The Product Master Plant view displays. |  |
| 6 | Navigate to Plant: Storage Location | In the Product Master – Plant view navigate to PLANTS > STORAGE LOCATIONS . | The Product Master – PLANTS view opens in Edit Mode. |  |
| 7 | Choose Add (+) | In the STORAGE LOCATIONS > Storage Locations and choose + (Add). | The Plant – Storage Location view opens in Edit Mode. |  |
| 8 | Enter Plant: Storage Location Data | In the Storage Locations view make following entries:Storage Location: <Storage location number> for example, 171A |  |  |
| 9 | Return to Main View | Choose the back arrow, twice, to return to Product Master . | Return to the Product Master view. |  |
| 10 | Save | Choose Save. | The system issues a notification that the object is saved. |  |

### Create Product Master Data - Accounting Data / Valuation Area Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating product master data. Apps available to you are dependent upon your assigned role, so two options are provided.

Prerequisite

You must complete a previous procedure, Create Product Master Data - Basic Data, before you proceed with this procedure.

Begin the procedure after you have saved the Basic Data entries, as described in the previous procedure.

Procedure: Option 1 - Create Material

Use the following procedure when your user access presents you with the Create Material (MM01) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Material (MM01). | The Create Material (MM01) displays. |  |
| 3 | Enter Material Basic Data | On the Create Material (Initial view), make the following entries:Material: CM-FL-V01Industry sector: MNote If the Industry Sector input field is hidden, no entry is required. When the industry sector is not offered for entry, the field is populated with in the dark.Material type: KMAT - Configurable materials | The Select View(s) displays. |  |
| 4 | Choose Views | In the Select View(s) window, select the following views and choose Continue:Accounting 1Accounting 2 | The Organizational Levels view displays. |  |
| 5 | Enter Organizational Levels Data | In the Organizational Levels view, in the Organizational level section, make the following entries:Plant: 1710 | The Create Material (Configurable materials) view displays.You get the information at the bottom of the view: The material already exists and will be extended. |  |
| 6 | Enter Accounting Data | In the Create Material (Configurable materials) view, on the Accounting 1 tab, in the General Valuation Data section, make the following entry:Valuation Class: 7920 |  |  |
| 7 | Enter Accounting Data | In the Prices and values section, make the following entries:Standard Price: 1Per. Unit price: 1Prc. Ctrl: S | You have navigated to the next tab, Accounting 2. |  |
| 8 | Confirm Entries | In the Accounting 2 tab, you do not have to make any entries. | A new window Last data view reached displays with the message You are about to exit. Do you want to save your data for this material first?. |  |
| 9 | Save Your Data | In the window Last data view reached choose Yes. | The Master Data - Product window displays.Your data is saved. |  |

Procedure: Option 2 - Manage Product Master Data

Use the following procedure when your user access presents you with the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Product Master Data (F1602). |  |  |
| 3 | Choose Edit | Choose EditNote This step assumes you are continuing from the previous step and are already on the Manage Product Master Data tile. After you have saved your data from the previous section, the system is in Display Mode. To proceed, you must be in Edit Mode. | Edit Mode (fields are ready for your input). |  |
| 4 | Choose Valuation Area Data | In the Product view, choose VALUATION AREAS | The VALUATION AREAS view displays. |  |
| 5 | Choose Add (+) | In the VALUATION AREAS view, choose + (Add) | The VALUATION AREAS view opens in Edit Mode. |  |
| 6 | Enter Valuation Area Data | In the VALUATION AREAS > Valuation Area view make following entries:Valuation Area: <number>, for example, 1710Price Control Determination:2Valuation Class: for example, 7920 |  |  |
| 7 | Enter Current Valuation Area Data | In the Valuation view, choose Current Period view, make the following entries:Moving average price: for example, 20Price Control: for example,S |  |  |
| 8 | Return to Main View | Choose the back arrow to return to Product Master | Return to the Product Master view. |  |
| 9 | Save | Choose Save. | The system issues a notification that the object is saved. |  |

### Create Product Master Data – Costing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating product master data. Apps available to you are dependent upon your assigned role, so two options are provided.

Prerequisite

You must complete the previous section, Create Product Master Data – Basic Data, before you proceed with this section.

Begin the procedure after you have saved the Basic Data entries, as described in the previous procedure.

Procedure: Option 1 – Create Material

Use the following procedure when your user access presents you with the Create Material (MM01) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Material (MM01). | The Create Material (MM01) displays. |  |
| 3 | Enter Material Basic Data | In Create Material (Initial view), make the following entries:Material: CM-FL-V01Industry sector: MNote If the Industry Sector input field is hidden, no entry is required. When the industry sector is not offered for entry, the field is populated with in the dark.Material type: KMAT – Configurable materials | The Select View(s) view displays. | Field is not available. |
| 4 | Choose Views | In the Select View(s) window, select Costing 1 and Costing 2 and choose Continue. | The Class Type (1) view displays. |  |
| 5 | Enter Organizational Levels Data | In the Organizational level section, select the following entries and choose Continue:Plant: 1710 | The Costing 1 view displays. |  |
| 6 | Enter Costing 1 Data | In the Costing 1 view, select the following entries and choose the Costing 2 tab.Base unit of Measure: PCProfit Center: YB110Costing lot size: 100 | The Costing 2 view displays.Your data is saved. |  |
| 7 | Enter Costing 2 Data | In the Costing 2 view, select the following entries and choose Continue to save:Valuation class: 7920Price control: SPrice unit: 1 | Your data is saved. |  |

Procedure: Option 2 – Manage Product Master Data

|  |
| --- |
| Note The required fields are currently unavailable for this application. Use Option 1 (above) and save your entries. |

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

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: Costing step 3 carries a stray 'Field is not available.' comment in the result column, which is unclear

> [!warning] Conflict
> Flagged while digesting this document, not verified: Sales/Basic Data steps reference Plant 1010 in purchasing but 1710 elsewhere (example values only)

## Connections
- part-of :: [[_cluster]]
- related-to :: [[02-business-partner-and-product-master-data/mds-2t7-285]]
- related-to :: [[02-business-partner-and-product-master-data/sap-s-4hana-cloud-public-edition-mds-2t7-283]]
- related-to :: [[02-business-partner-and-product-master-data/script-de-dados-mestre-criar-mestre-de-produtos-do-tipo-material-confi]]
- related-to :: [[02-business-partner-and-product-master-data/script-de-datos-maestros-creacion-de-maestro-de-productos-de-tipo-mate-3]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2T7_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 51,319 chars in the whole document
