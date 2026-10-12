---
id: 02-business-partner-and-product-master-data/master-data-script-create-product-master-of-type-finished-good-sap-s-4
title: "Master Data Script - Create Product Master of type \"Finished Good\" (SAP S/4HANA Cloud Public Edition) (BNT_S4CLD2608_Master_Data_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for creating a Finished Good (FERT) product master via MM01 or Manage Product Master Data (F1602), by data segment."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/product-master-raw-semifinished-finished]
aliases: [BNT_S4CLD2608_Master_Data_EN_XX]
keywords: ["Product Master: Raw Materials, Semi-Finished and Finished…", product master data, material types, basic data, sales data, mrp planning data, storage location data, accounting valuation data, configurable products, repetitive manufacturing]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNT_S4CLD2608_Master_Data_EN_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-671
topic: 02-business-partner-and-product-master-data/product-master-raw-semifinished-finished
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Master Data Script - Create Product Master of type "Finished Good" (SAP S/4HANA Cloud Public Edition) (BNT_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNT_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Product Master: Raw Materials, Semi-Finished and Finished Goods** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Product Master of type "Finished Good" - MDS (BNT) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233905058)

[2 Prerequisites 3](#_Toc233905059)

[2.1 System Access 3](#_Toc233905060)

[2.2 Roles 3](#_Toc233905061)

[2.3 Required Organizational Units 3](#_Toc233905062)

[2.4 Mandatory and Optional Master Data 4](#_Toc233905063)

[2.5 Main Parameters for Data Creation 5](#_Toc233905064)

[2.5.1 Material Type and Number Ranges 5](#_Toc233905065)

[2.5.2 Industry Sector 5](#_Toc233905066)

[3 Overview Table 6](#_Toc233905067)

[4 Test Procedures 7](#_Toc233905068)

[4.1 Create Product Master Data - Basic Data 7](#_Toc233905069)

[4.2 Create Product Master Data - Sales Data / Sales Tax Data 10](#_Toc233905070)

[4.3 Create Product Master Data - MRP Planning Data / Plant Data 13](#_Toc233905071)

[4.4 Create Product Master Data - Storage Location Data 17](#_Toc233905072)

[4.5 Create Product Master Data - Accounting Data / Valuation Area Data 19](#_Toc233905073)

[4.6 Create Product Master Data - Configurable Product and Variants 22](#_Toc233905074)

[4.7 Create Product Master Data - Save Attachments 25](#_Toc233905075)

[4.8 Create Product Master Data - Plant Sales / General Data 26](#_Toc233905076)

[4.9 Create Product Master Data - Plant / Repetitive Manufacturing 29](#_Toc233905077)

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
| Basic Data | Independent of organizational units | Material description (short text), Material number, Material Group, Base Unit of Measure and so on. | Basic Data exists only once for a material master data record. | n/a |
| Sales Data | Plant, Sales Org., Distribution Channel | Tax Data, Item Category Group, Transp. Group, Loading Group, Setup Time and so on. | Sales data can exist for every Sales Org. of your enterprise structure for which the material master record is used. | Plant:____________Sales Organization:__________Distribution Channel:__________ |
| MRP/Planning Data (Plant Data) | Plant, Storage Location | MRP Type, MRP Controller, Lot Size, Planned delivery time and so on. | Plant data can exist for every Plant ID of your enterprise structure for which the material master record is used.Storage location data (planning context) is optional based on the need to do storage location specific planning. | Plant:____________Storage Location:__________ |
| Storage Location Data | Plant, Storage Location | Number of GR slips, Max. Storage Period, Min. Rem. Shelf and so on. |  | Plant:____________Storage Location:__________ |
| Accounting Data (Valuation Data) | Valuation area (=Plant), Valuation type | Valuation Class, Per Unit Price, Price Control and so on. | Valuation area data can exist for every Plant ID of your enterprise structure for which the material master record is used. Every plant represents a valuation area (for example, different valuation price of a material in different plants) | Plant:____________Valuation type:__________ |

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
| External alpha-numeric | A – ZZZZZZZZ | This range must start with a character. Overall the ID must not be longer than 40 characters. |
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
| [Create Product Master Data - Basic Data](#unique_11) [page ] 7 | Master Data Specialist - Product Data | Create Material (MM01)/ Manage Product Master Data (F1602) | Material Master Data - Basic Data is created. |
| [Create Product Master Data - Sales Data / Sales Tax Data](#unique_12) [page ] 10 | Master Data Specialist - Product Data | Create Material (MM01)/ Manage Product Master Data (F1602) | Material Master Data - Sales Data (Sales Tax Data) is created. |
| [Create Product Master Data - MRP Planning Data / Plant Data](#unique_13) [page ] 13 | Master Data Specialist - Product Data | Create Material (MM01)/ Manage Product Master Data (F1602) | Material Master Data - MRP/Planning Data Data (Plant Data) is created. |
| [Create Product Master Data - Storage Location Data](#unique_14) [page ] 17 | Master Data Specialist - Product Data | Create Material (MM01)/ Manage Product Master Data (F1602) | Material Master Data - Storage Location Data is created. |
| [Create Product Master Data - Accounting Data / Valuation Area Data](#unique_15) [page ] 19 | Master Data Specialist - Product Data | Create Material (MM01)/ Manage Product Master Data (F1602) | Material Master Data - Accounting Data (Valuation Data) is created. |
| [Create Product Master Data - Configurable Product and Variants](#unique_16) [page ] 22 | Master Data Specialist - Product Data | Create Material (MM01)/ Manage Product Master Data (F1602) | Create Configurable Product and Variants. |
| [Create Product Master Data - Save Attachments](#unique_17) [page ] 25 | Master Data Specialist - Product Data | Change Material (MM02)/ Manage Product Master Data (F1602) | Save attachments to the material master record. |
| [Create Product Master Data - Plant Sales / General Data](#unique_18) [page ] 26 | Master Data Specialist - Product Data | Create Material (MM01)/ Manage Product Master Data (F1602) |  |
| [Create Product Master Data - Plant / Repetitive Manufacturing](#unique_19) [page ] 29 | Master Data Specialist - Product Data | Create Material (MM01)/ Manage Product Master Data (F1602) |  |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Material (MM01). | The app opens. |  |
| 3 | Enter Material Basic Data | On the Create Material (Initial view) screen, make the following entries and choose Select View(s):Material: <Material Number>Industry Sector: MNote If the Industry Sector input field is hidden, no entry is required. When the industry sector is not offered for entry, the field is filled with in the dark.Material Type: FERT | The Select View(s) view displays. |  |
| 4 | Choose Views | In the Select View(s) view, select Basic data 1 and Basic data 2 and choose Continue. | The Create Material (Finished Product) view displays. |  |
| 5 | Enter Basic Data | In the Material (Finished Product) view, on the Basic data 1 tab, enter the material description (short text). |  |  |
| 6 | Enter Basic Data | On the Basic data 1 tab, in the General Data section, make the following entries:Base Unit of Measure: <Base Unit of Measure>Material Group: <Material Group>GenItemCatGroup: <GenItemCatGroup> |  |  |
| 7 | Enter Basic Data | In the Dimensions/EANs section, make the following entries and press Enter:Gross Weight: <Gross Weight>Weight Unit: <Weight Unit>Net Weight: <Net Weight> | The Basic Data 2 tab displays. |  |
| 8 | Enter Basic Data | On the Basic Data 2 tab, you do not have to make any entries. | A new window Last data view reached opens with the message You are about to exit. Do you want to save your data for this material first?. |  |
| 9 | Save Your Data | In the Last data view reached window, choose Yes. | The Master Data - Product view displays.The Basic Data is created and saved. |  |

Procedure: Option 2 - Manage Product Master Data

Use the following procedure when your user access presents you with the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Product Master Data (F1602). | The app opens. |  |
| 3 | Choose Create New Product Master | Choose Create Product. | The Create Master Data Record view displays. |  |
| 4 | Enter Data for Mandatory Fields | In the Create Master Data Record view, make the following entries:Product Number: for example, Z …Note Here you can enter any external alphanumeric ID … (at least this needs to start with a character). If you do not make any entry here, the system will assign a numeric ID automatically.For more information about Product Number, see the Material Type and Number Ranges section in Main Parameters for Data Creation.Product Type: FERTProduct Group: for example, L004Base Unit: for example, PCDescription: <Description> |  |  |
| 5 | Choose OK | In the Manage Product Master view, choose OK. | The Manage Product Master view displays. |  |
| 6 | Enter Basic Data | Go to Manage Product Master > BASIC DATA > Basic Data view and make the following entry:Division: for example, 00 |  |  |
| 7 | Go to the Descriptions View | Go to the Descriptions view. | Description in default language (English, for example) is already filled. |  |
| 8 | Choose Create | In the DESCRIPTIONS view, choose Create. | The Product Master - Description view displays.Some fields are already filled. |  |
| 9 | Enter Descriptions Data | In the Product Master - Description view, make the following entries:Language: for example, GermanProduct Description: <Product Description> | Descriptions can be maintained in different languages. |  |
| 10 | Return to Product Master | Choose the back arrow to return to the Product Master view. | The Product Master view displays. |  |
| 11 | Choose Base Unit of Measure | In the Product Master view, go to BASIC DATA and choose Base Unit of Measure. | The Base Unit of Measure view displays. |  |
| 12 | Enter Base Unit of Measure Data | Choose Show More and make the following entries for the Weight-related fields:Weight Unit: for example, KGGross Weight: for example, 2Net Weight: for example, 1Note If the Gross Weight, Weight Unit, or Net Weight fields do not display as input fields, refresh/reload the view. After refreshing/reloading, you are able to make the entries indicated to those fields. |  |  |
| 13 | Return to Main Screen | Choose the back arrow to return to the Product Master view. | The Product Master view displays. |  |
| 14 | Save Your Data | Choose Save. | The object is saved. |  |

### Create Product Master Data - Sales Data / Sales Tax Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions on how to create Product master data. Apps available to you are dependent upon your assigned role, so two options are provided.

Prerequisite

You must complete the previous chapter, [Create Product Master Data - Basic Data](#unique_11) [page ] 7, before you proceed with this chapter.

Follow the procedure after you have saved the Basic Data entries, as described in the previous chapter.

Procedure: Option 1 - Create Material

Follow this procedure when your user access presents you with the Create Material (MM01) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Create Material (MM01). | The app opens. |  |
| 2 | Enter Material Basic Data | On the Create Material (Initial view) screen, make the following entries:Material: <Material number>Industry Sector: MNote If the Industry Sector input field is hidden, no entry is required. When the Industry Sector is not offered for entry, the field is grayed out.Material type: FERTChoose Select View(s). | The Select View(s) screen displays. |  |
| 3 | Select Views | On the Select View(s) screen, select Sales: Sales Org. Data 1, Sales: Sales Org. Data 2, and Sales: General/Plant Data.Choose Continue.Note For Poland Only: in order to enter PKWiU classification number, you need to also select International Trade: Export. | The Organizational Levels screen displays. |  |
| 4 | Enter Organizational Levels Data | On the Organizational Levels screen, in the Organizational level section, make the following entries and choose Continue:Plant: For example, 1710.Sales Org.: For example, 1710.Distr. Channel: For example, 10. | The Create Material (Finished Product) screen displays.The system message displays that The material already exists and will be extended. |  |
| 5 | Enter Sales Data | On the Material (Finished Product) screen, on the Sales: sales org. 1 tab, enter an appropriate value for the Tax classification field. For example, 1 for fully taxable. | The Sales: sales org. 2 tab displays.The entered value indicates that the Material is (usually) fully taxable. |  |
| 6 | Enter Sales Data | On the Sales: sales org 2 tab, in the Grouping terms section, make the following entry:Item category group: <Item category group> | The Sales: General/Plant tab displays. |  |
| 7 | Enter Sales Data | On the Sales: General/Plant tab, in the General data section, make the following entry:Availability check: For example,SP. |  |  |
| 8 | Enter Sales Data | In the Shipping data (times in days) section, make the following entries:Transp. Grp: For example, 0001.Loading Grp: For example, 0001. |  |  |
| 9 | Enter Sales Data | In the General Plant parameters section, make the following entries:Profit Center: For example, YB110 or YB111.SerialNoProfile: Choose a valid serial number profile which has been assigned with the proper equipment category for your business. | The Last data view reached screen displays with the message: You are about to exit. Do you want to save your data for this material first?. |  |
| For Poland Only | Enter Sales Data - for Poland Only | In the International Trade: Export section, make the following entry:Control code: For example, 26.70.13.0. | PKWiU code for Poland is maintained. |  |
| 10 | Save Your Data | On the Last data view reached screen, choose Yes. | The Master Data - Product screen displays.Your data is saved. |  |

Procedure: Option 2 - Manage Product Master Data

Follow this procedure when your user access presents you with the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Manage Product Master Data (F1602). | The app opens. |  |
| 2 | Search and Open the Product for Edit | Search the previously created Product by entering the Product Number in the Product search field.Select the Product from the list which navigates you to the Product screen.Choose Edit. | Product displays in edit mode (fields are ready for your input). |  |
| 3 | Choose Distributions Chains | On the Product Master screen, choose DISTRIBUTION CHAINS. | The DISTRIBUTIONS CHAINS screen displays. |  |
| 4 | Choose Create | Go to DISTRIBUTION CHAINS > Distribution Chains , and choose Create. | The Distribution Chain screen displays in edit mode. |  |
| 5 | Enter Distribution Chains Data | On the Distribution Chain screen, make the following entries:GENERAL DATA - General InformationSales Organization: <Sales organization number>, for example, 1710Distribution Channel: For example, 10.Delivery Plant: <Plant number>, for example, 1710GROUPING TERMSItem Category Group: For example, NORM.Accounting Assignment Group: For example, 03 Finished Products.SALES TAXCountry: <Country code>, for example, DETax Category: TTX1Tax Classification: Either 1 for Material or 2 for Services.Tax Classification: For example, 1 Full tax when using UTXJ tax condition for US.Note Tax classification depends on the specific country/region requirements. Tax classification in the Material master and Customer master tables determines tax percentage inputs.For Brazil Only:In the Tax Classification section, make the following entries:Country: BRTax Category: IBRXTax Classification: Either 1 for Material or 2 for Services. |  |  |
| 6 | Save Your Data | Choose Save. | The system displays a notification indicating that the object is saved. |  |

### Create Product Master Data - MRP Planning Data / Plant Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions on how to create Product master data. Apps available to you are dependent upon your assigned role, so two options are provided.

Prerequisite

You must complete the previous chapter, [Create Product Master Data - Basic Data](#unique_11) [page ] 7, before you proceed with this chapter.

Follow the procedure after you have saved the Basic Data entries, as described in the previous chapter.

Procedure: Option 1 - Create Material

Follow this procedure when your user access presents you with the Create Material (MM01) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Create Material (MM01). | The app opens. |  |
| 2 | Enter Material Basic Data | On the Create Material (Initial view) screen, make the following entries:Material: <Material number>Industry Sector: MNote If the Industry Sector input field is hidden, no entry is required. When the Industry Sector is not offered for entry, the field is grayed out.Material type: FERTChoose Select View(s). | The Select View(s) screen displays. |  |
| 3 | Select Views | On the Select View(s) screen, select MRP1, MRP2, MRP3, and MRP4.Choose Continue. | The Organizational Levels screen displays. |  |
| 4 | Enter Organizational Levels Data | On the Organizational Levels screen, in the Organizational level section, make the following entries:Plant: <Plant code>, for example, 1710Storage Location: For example, 171A. | The Create Material (Finished Product) screen displays.The system message displays that The material already exists and will be extended. |  |
| 5 | Enter MRP/Planning Data | On the Material (Finished Product) screen, on the MRP 1 tab, in the General Data section, make the following entry:Purchasing Group: <Purchasing Group> |  |  |
| 6 | Enter MRP/Planning Data | In the MRP procedure section, make the following entries:MRP Type: For example, PD.MRP Controller: For example, 001. |  |  |
| 7 | Enter MRP/Planning Data | In the Lot Sizing Procedure section, make the following entry:Lot Sizing Procedure: EX | The MRP 2 tab displays. |  |
| 8 | Enter MRP/Planning Data | On the Create Material (Finished Product) screen, on the MRP 2 tab, make entries based on your requirements or at least enter values for the mandatory fields. For example, the In-house production time in days. | The MRP 3 tab displays. |  |
| 9 | Enter MRP/Planning Data | On the Create Material (Finished Product) screen, on the MRP 3 tab, in the Planning section, make the following entries:Strategy Group: For example, 40.Consumption mode: For example,2.Bwd consumption per.: <Bwd consumption per.>Fwd consumption per.: <Fwd consumption per.> |  |  |
| 10 | Enter MRP/Planning Data | In the Availability check section, make the following entries:Availability check: For example, SP.Tot. repl. Lead time: For example, 3. | The MRP 4 tab displays. |  |
| 11 | Enter MRP/Planning Data | On the Create Material (Finished Product) screen, on the MRP 4 tab, you do not need to make any entries. | The Last data view reached screen displays with the message You are about to exit. Do you want to save your data for this material first?. |  |
| 12 | Save | On the Last data view reached screen, choose Yes. | The Master Data - Product screen displays.Your data is saved. |  |

Procedure: Option 2 - Manage Product Master Data

Follow this procedure when your user access presents you with the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Manage Product Master Data (F1602). | The app opens. |  |
| 2 | Search and Open the Product for Edit | Search the previously created Product by entering the Product Number in the Product search field.Select the Product from the list which navigates you to the Product screen.Choose Edit. | Product displays in edit mode (fields are ready for your input). |  |
| 3 | Choose Plants Data | On the Product Master screen, choose PLANTS. | The PLANTS screen displays. |  |
| 4 | Choose Create | On the PLANTS screen, choose Create. | The Plant screen displays in edit mode. |  |
| 5 | Enter Plants - General Information Data | Go to Plant > GENERAL INFORMATION , and make the following entries:Plant: <Plant number>, for example, 1710Profit Center: For example, YB110 or YB111. |  |  |
| 6 | Enter Plants - MRP Data | On the Product Master screen, choose MRP DATA.In the MRP DATA > MRP Data section, make the following entries:Availability Check: For example, SP.MRP Type: For example, PD.MRP Controller: For example, 001. |  |  |
| 7 | Enter Plants - Lot-Size Data | On the MRP DATA screen, choose Lot-Size Data.On the Lot-Size Data screen, make the following entry:Lot Sizing Procedure: For example, EX. |  |  |
| 8 | Enter Plants - Procurement Data | Go to MRP Data > Procurement , and make the following entries:Planned Delivery Time: For example, 3.Goods Receipt Processing Time: For example, 1. |  |  |
| 9 | Choose Plants - Forecast Data | Go to Manage Product Master > PLANTS , and choose FORECASTING. | The FORECASTING screen displays. |  |
| 10 | Enter Plants - Forecast Data | On the FORECASTING screen, make the following entry:Period Type: For example, M. |  |  |
| 11 | Return to Main Screen | Choose Apply to return to the Productscreen. | The Product Master screen displays. |  |
| 12 | Save Your Data | Choose Save. | The object is saved. |  |

### Create Product Master Data - Storage Location Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions on how to create Product master data. Apps available to you are dependent upon your assigned role, so two options are provided.

Prerequisite

You must complete the previous chapter, [Create Product Master Data - Basic Data](#unique_11) [page ] 7, before you proceed with this chapter.

Follow the procedure after you have saved the Basic Data entries, as described in the previous chapter.

Procedure: Option 1 - Create Material

Follow this procedure when your user access presents you with the Create Material (MM01) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Create Material (MM01). | The app opens. |  |
| 2 | Enter Material Basic Data | On the Create Material (Initial view) screen, make the following entries:Material: <Material number>Industry Sector: MNote If the Industry Sector input field is hidden, no entry is required. When the Industry Sector is not offered for entry, the field is grayed out.Material type: FERTChoose Select View(s). | The Select View(s) screen displays. |  |
| 3 | Select Views | On the Select View(s) screen, select the following views and choose Continue:General Plant Data/Storage 1General Plant Data/Storage 2 | The Organizational Levels screen displays. |  |
| 4 | Enter Organizational Levels Data | On the Organizational Levels screen, in the Organizational level section, make the following entries:Plant: For example, 1710.Storage Location: For example, 171A. | The Create Material (Finished Product) screen displays.The system message displays that The material already exists and will be extended. |  |
| 5 | Enter Storage Location Data | On the Create Material (Finished Product) screen, on the Plant data/stor. 1 tab, in the General Data section, make the following entry:Number of GR slips: For example, 1. | The Plant data/stor.2 tab displays. |  |
| 6 | Confirm Entries | On the Plant data/stor. 2 tab, you do not need to make any entries.Note For the SerialNoProfile field, choose a valid serial number profile which has been assigned with the proper equipment category for your business. | The Last data view reached screen displays with the message: You are about to exit. Do you want to save your data for this material first?. |  |
| 7 | Save | On the Last data view reached screen, choose Yes. | The Master Data - Product screen displays.Your data is saved. |  |

Procedure: Option 2 - Manage Product Master Data

Follow this procedure when your user access presents you with the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Manage Product Master Data (F1602). | The app opens. |  |
| 2 | Search and Open the Product for Edit | Search the previously created Product by entering the Product Number in the Product search field.Select the Product from the list which navigates you to the Product screen.Choose Edit. | Product displays in edit mode (fields are ready for your input). |  |
| 3 | Choose Plants Data | On the Manage Product Master screen, choose PLANTS.Note If there is no plant data record, follow the steps in the previous chapter: [Create Product Master Data - MRP Planning Data / Plant Data](#unique_13) [page ] 13. | The PLANTS screen displays. |  |
| 4 | Choose Plant Details | On the PLANTS screen, use the arrow icon to select the Plant data you created in the previous step. | The Product Master - Plant screen displays. |  |
| 5 | Navigate to Plant: Storage Location | On the Product Master - Plant screen, go to PLANTS > STORAGE LOCATIONS . | The Product Master - PLANTS screen displays in edit mode. |  |
| 6 | Choose Create | Go to STORAGE LOCATIONS > Storage Locations , and choose Create. | The Plant - Storage Location screen displays in edit mode. |  |
| 7 | Enter Plant: Storage Location Data | On the Storage Locations screen, make the following entry:Storage Location: <Storage location number>, for example, 171A |  |  |
| 8 | Return to Main Screen | Choose Apply twice to return to the Productscreen. | The Product Master screen displays. |  |
| 9 | Save | Choose Save. | The system displays a notification indicating that the object is saved. |  |

### Create Product Master Data - Accounting Data / Valuation Area Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions on how to create Product master data. Apps available to you are dependent upon your assigned role, so two options are provided.

Prerequisite

You must complete the previous chapter, [Create Product Master Data - Basic Data](#unique_11) [page ] 7, before you proceed with this chapter.

Follow the procedure after you have saved the Basic Data entries, as described in the previous chapter.

Procedure: Option 1 - Create Material

Follow this procedure when your user access presents you with the Create Material (MM01) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Create Material (MM01). | The app opens. |  |
| 2 | Enter Material Basic Data | On the Create Material (Initial view) screen, make the following entries:Material: <Material number>Industry Sector: MNote If the Industry Sector input field is hidden, no entry is required. When the Industry Sector is not offered for entry, the field is grayed out.Material type: FERTChoose Select View(s). | The Select View(s) screen displays. |  |
| 3 | Select Views | On the Select View(s) screen, select the following views and choose Continue:Accounting 1Accounting 2 | The Organizational Levels screen displays. |  |
| 4 | Enter Organizational Levels Data | On the Organizational Levels screen, in the Organizational level section, make the following entries:Plant: <Plant code> | The Create Material (Finished Product) screen displays.The system message displays that The material already exists and will be extended. |  |
| 5 | Enter Accounting Data | On the Create Material (Finished Product) screen, on the Accounting 1 tab, in the General Valuation Data section, make the following entry:Valuation Class: 7920 |  |  |
| 6 | Enter Accounting Data | In the Prices and values section, make the following entries:Standard Price: <Standard price>Per. Unit price: For example, 20.Price Control: For example, S. | The Accounting 2 tab displays. |  |
| 7 | Confirm Entries | On the Accounting 2 tab, you do not need to make any entries. | The Last data view reached screen displays with the message You are about to exit. Do you want to save your data for this material first?. |  |
| 8 | Save Your Data | On the Last data view reached screen, choose Yes. | The Master Data - Product screen displays.Your data is saved. |  |

Procedure: Option 2 - Manage Product Master Data

Follow this procedure when your user access presents you with the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Manage Product Master Data (F1602). | The app opens. |  |
| 2 | Search and Open the Product for Edit | Search the previously created Product by entering the Product Number in the Product search field.Select the Product from the list which navigates you to the Product screen.Choose Edit. | Product displays in edit mode (fields are ready for your input). |  |
| 3 | Choose Valuation Area Data | On the Manager Product Master screen, choose VALUATION AREAS. | The VALUATION AREAS screen displays. |  |
| 4 | Choose Create | On the VALUATION AREAS screen, choose Create. | The VALUATION AREAS screen displays in edit mode. |  |
| 5 | Enter Valuation Area Data | Go to VALUATION AREAS > Valuation Area , and make the following entries:Valuation Area: <Valuation Area>, for example, 1710Price Control Determination: 2Valuation Class: For example, 7920. |  |  |
| 6 | Enter Current Valuation Area Data | On the Valuation screen, choose Current Period, and make the following entries:Moving average price: For example, 20.Price Control: For example,S. |  |  |
| 7 | Return to Main Screen | Choose Apply to return to the Productscreen. | The Product Master screen displays. |  |
| 8 | Save Your Data | Choose Save. | The system displays a notification indicating that the object is saved. |  |

### Create Product Master Data - Configurable Product and Variants

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
| 1 | Access the SAP Fiori App | Open Create Material (MM01). | A new window opens, showing the Create Material (Initial Screen). |  |
| 2 | Enter Material Basic Data | On the Create Material (Initial Screen), make the following entries:Material : Material numberIndustry sector: MNote If the Industry Sector input field is hidden, no entry is required. When the industry sector is not offered for entry, the field is populated with in the dark.Material type: FERTClick on Select View(s). | A new window opens, showing the Select View(s) view. |  |
| 3 | Choose Views | In the Select View(s) window, select the following views and choose Continue:Basic data 1Basic data 2Classification |  |  |
| 4 | Enter Basic Data | On the Material (Finished Product) view, on the Basic data 1 tab, enter the Material Description (short text) and Base Unit of Measure.Press Enter. | Basic data 2 tab displays. |  |
| 5 | Enter Basic Data | In the Basic data 2 tab, check the Material is configurable checkbox.Press Enter. | Classification tab displays and Class Type popup opens. |  |
| 6 | Choose Class Type | In the Class Type popup, select class type 300 (Variant) and choose Continue. | Classification view displays. |  |
| 7 | Assign Class | In the Assignment section, assign a class and press enter. | Corresponding characteristics displays below the Assignment section. |  |
| 8 | Choose Characteristics Values | Choose the required values of the characteristics. |  |  |
| 9 | Save Your Data | Choose Save. | Configurable material is created. Now you have to create variant. |  |
| 10 | Create Variant | For creating Variant, again open Create Material (MM01) tile and follow the above steps to create a new material with Basic data 1 and Basic data 2. |  |  |
| 11 | Create Variant | In Basic data 2 go to Client-specific configuration and enter the previously created Configurable material in the Cross-plant CM and click on Configure variant and then choose required characteristics value to configure variants. | Variant gets created. |  |

Procedure: Option 2 - Manage Product Master Data

Use the following procedure when your user access presents you with the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Manage Product Master Data (F1602). |  |  |
| 2 | Search and Open the Product for Edit | Search the previously created Product by entering Product Number in the Product search field.Select the Product from the list which will navigate you to Product view.Click on Edit. | Product is displayed in edit mode (fields are ready for your input). |  |
| 3 | Make Product Configurable | In the Product view, go to Configuration tab and check the Product is Configurable checkbox. |  |  |
| 4 | Assign Variant Class | In the Product view, go to Classification tab and choose Click here to assign a class and then select a class of type 300 (Variant). | The characteristics of the assigned class will be displayed. |  |
| 5 | Choose Characteristics | Choose the required characteristic values for each of the characteristic. |  |  |
| 6 | Go to Variants Tab | In the Product view, go to Variants tab and choose Select Product Variants. | A tree/table will be displayed with the different characteristics. |  |
| 7 | Select Characteristics and Create Variants | Choose the combination of characteristic values and click Apply. | Variants will get created. |  |
| 8 | Save | Choose Save. | The system issues a notification that the object is saved. |  |

### Create Product Master Data - Save Attachments

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions on how to create Product master data. Apps available to you are dependent upon your assigned role, so two options are provided.

Prerequisite

You must complete the previous chapter, [Create Product Master Data - Basic Data](#unique_11) [page ] 7, before you proceed with this chapter.

Follow the procedure after you have saved the Basic Data entries, as described in the previous chapter.

Procedure: Option 1 - Change Material

Follow this procedure when your user access presents you with the Change Material (MM02) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Change Material (MM02). | The Change Material (Initial Screen) screen displays. |  |
| 2 | Enter Material Number | Make the following entry and Choose Select View(s):Material Number: <Material Number> | The Select View(s) screen displays. |  |
| 3 | Select Views | On the Select View(s) screen, select Basic data 1 and Basic data 2.Choose Continue. | The Change Material (Finished Product) screen displays. |  |
| 4 | Choose Services for Object | In the application toolbar, go to Services for Object > Create Attachment . | The Import file screen displays. |  |
| 5 | Choose Upload | On the Import file screen, choose Upload. | A file upload screen displays. |  |
| 6 | Upload Attachment | Select the file and choose Open. | The file gets uploaded. |  |
| 7 | Save | Select Choose and then Save. | The system displays a notification indicating that the object is saved. |  |

Procedure: Option 2 - Manage Product Master Data

Follow this procedure when your user access presents you with the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Choose Manage Product Master Data (F1602). | The app opens. |  |
| 2 | Search and Open the Product for Edit | Search the previously created Product by entering the Product Number in the Product search field.Select the Product from the list which navigates you to the Product screen.Choose Edit. | Product displays in edit mode (fields are ready for your input). |  |
| 3 | Choose Attachments | On the Product screen, go to the Attachments tab. | The Attachments tab displays. |  |
| 4 | Choose Upload | Under the Document Management System section, choose Upload. | A file upload screen displays. |  |
| 5 | Upload Attachment | Select the file and choose Open. | The file gets uploaded. |  |
| 6 | Save | Choose Save. | The system displays a notification indicating that the object is saved. |  |

### Create Product Master Data - Plant Sales / General Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating material (product) master data. Apps available to you are dependent upon your assigned role, so two options are provided.

Prerequisite

You must complete the previous procedure, Creating Material (Product) Master Data - Basic Data, before you proceed with this section.

Begin the procedure after you have saved the Basic Data entries, as described in the previous procedure.

Procedure: Option 1 - Create Material

Use the following procedure when your user access presents you with the Create Material (MM01) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Create Material (MM01) | Create Material (Initial Screen) opens. |  |
| 2 | Enter Material Basic Data | In the Create Material (Initial screen), make the following entries:Material: <Material number>Industry sector: MNote If the Industry Sector input field is hidden, no entry is required. When the industry sector is not offered for entry, the field is populated with in the dark.Material type: FERTChoose Select View(s). | Select View(s) screen opens. |  |
| 3 | Choose Views | In the Select View(s) window select Basic Data and Sales: General/Plant Data and choose continue. | Organizational Levels appears |  |
| 4 | Enter Organizational Levels Data | In the Organizational Levels screen, in the Organizational level section, make following entries:Plant: <Plant number>Storage Location: <Storage location number> | The Create Material…(Finished Product) screen opens. |  |
| 5 | Enter Data in Basic Data 1 | In View Basic Data 1 make the following entries and choose Enter:Description : Maintain description for productBase Unit: Maintain Base Unit "EA" for example 1 |  |  |
| 6 | Enter Data in Sales:General/plant | In the Shipping data (times in days) section make the following entry:LoadingGrp: choose any value from value help |  |  |
| 7 | Save Your Data | At the bottom of the screen, choose Save. | Your data is saved. |  |

Procedure: Option 2 - Manage Product Master Data

Use the following procedure when your user access presents you with the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Choose Manage Product Master Data (F1602) | The Manage Product Master Data (F1602) app opens and various search fields are displayed. |  |
| 2 | Search and Open the Product for Edit | Search the previously created Product by entering Product Number in the Product search field.Select the Product from the list which will navigate you to Product view.Choose Edit. | Product is displayed in edit mode (fields are ready for your input). |  |
| 3 | Choose Plants Data | In the Product view, choose Plants | The Plants tab displays. |  |
| 4 | Choose Create | In the Plants view, choose Create. |  |  |
| 5 | Enter Plants - General Data | In the General Data section, make following entries:Plant: Plant number for example, 1710 |  |  |
| 6 | Enter MRP Data | In the MRP section, make following entries:MRP Type: example ND |  |  |
| 7 | Enter Plant- Sales | In the Sales section make following entries:Loading Group: choose from value help |  |  |
| 8 | Return to Main Screen | Choose Apply to return to Product view. | The Product view displays. |  |
| 9 | Save Your Data | Choose Save. | System message indicates that the object is saved. |  |

### Create Product Master Data - Plant / Repetitive Manufacturing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions on how to create Product master data. Apps available to you are dependent upon your assigned role, so two options are provided.

Prerequisite

You must complete the previous chapter, [Create Product Master Data - Basic Data](#unique_11) [page ] 7, before you proceed with this chapter.

Follow the procedure after you have saved the Basic Data entries, as described in the previous chapter.

Procedure: Option 1 - Create Material

Follow this procedure when your user access presents you with the Create Material (MM01) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Create Material (MM01) | The app opens. |  |
| 2 | Enter Material Basic Data | On the Create Material (Initial view) screen, make the following entries:Material: <Material number>Industry Sector: MNote If the Industry Sector input field is hidden, no entry is required. When the Industry Sector is not offered for entry, the field is grayed out.Material type: FERTChoose Select View(s). | The Select View(s) screen displays. |  |
| 3 | Select Views | On the Select View(s) screen, select Basic Data 1, MRP 1, and MRP 4.Choose Continue. | The Organizational Levels screen displays. |  |
| 4 | Enter Organizational Levels Data | On the Organizational Levels screen, in the Organizational level section, make the following entries:Plant: <Plant number>Storage Location: <Storage location number> | The Create Material…(Trading Goods) screen displays. |  |
| 5 | Enter Data in Basic Data 1 | On the Basic Data 1 screen, make the following entries and press Enter:Description: <Description of the Product>Base Unit: Maintain Base Unit EA, for example, 1. |  |  |
| 6 | Enter Data in MRP 1 | In the MRP procedure section, make the following entry:MRP Type: For example, ND. |  |  |
| 7 | Enter Data in MRP 4 | In the Repetitive manufacturing/ assembly / deployment strategy section, make the following entries:Rpet. Manufacturing: Select the checkbox.REM Profile: <Choose any value from the value help> |  |  |
| 8 | Save Your Data | Choose Save. | Your data is saved. |  |

Procedure: Option 2 - Manage Product Master Data

Follow this procedure when your user access presents you with the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Choose Manage Product Master Data (F1602) | The app opens. |  |
| 2 | Search and Open the Product for Edit | Search the previously created Product by entering the Product Number in the Product search field.Select the Product from the list which navigates you to the Product screen.Choose Edit. | Product displays in edit mode (fields are ready for your input). |  |
| 3 | Choose Plants Data | On the Product screen, choose Plants. | The Plants tab displays. |  |
| 4 | Choose Create | On the Plants tab, choose Create. |  |  |
| 5 | Enter Plants - General Data | In the General Data section, make the following entry:Plant: <Plant number>, for example, 1710 |  |  |
| 6 | Enter MRP Data | In the MRP section, make the following entry:MRP Type: For example, ND. |  |  |
| 7 | Enter Repetitive Manufacturing Data | In the Repetitive Manufacturing section, make the following entries:Repetitive Manufacturing Enabled: Select the checkbox to enable the Repetitive Manufacturing Profile field.Repetitive Manufacturing Profile: <Choose any value from the value help> | If you check the Repetitive Manufacturing Enabled checkbox, the Repetitive Manufacturing Profile field should be editable.If you uncheck the Repetitive Manufacturing Enabled checkbox, the Repetitive Manufacturing Profile field should be read only. |  |
| 8 | Return to Main Screen | Choose Apply to return to the Product screen. | The Product screen displays. |  |
| 9 | Save Your Data | Choose Save. | The system displays a notification indicating that the object is saved. |  |

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
> Flagged while digesting this document, not verified: Repetitive manufacturing Option 1 step 4 expects a 'Trading Goods' screen although the script is for Finished Good (FERT)

> [!warning] Conflict
> Flagged while digesting this document, not verified: Create Product Master Data - Basic Data step 3 text differs slightly from other chapters on hidden Industry Sector field (greyed out vs garbled wording)

## Connections
- part-of :: [[_cluster]]
- related-to :: [[02-business-partner-and-product-master-data/sap-s-4hana-cloud-public-edition-bnt-675]]
- related-to :: [[02-business-partner-and-product-master-data/sap-s-4hana-cloud-public-edition-mds-bnt-673]]
- related-to :: [[02-business-partner-and-product-master-data/script-de-dados-mestre-criar-mestre-de-produtos-do-tipo-produto-acabad]]
- related-to :: [[02-business-partner-and-product-master-data/script-de-datos-maestros-creacion-de-maestro-de-productos-de-tipo-prod-2]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNT_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 55,664 chars in the whole document
