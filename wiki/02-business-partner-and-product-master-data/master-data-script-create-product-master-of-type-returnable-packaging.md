---
id: 02-business-partner-and-product-master-data/master-data-script-create-product-master-of-type-returnable-packaging
title: "Master Data Script: Create Product Master of type \"Returnable Packaging\" - MDS (65B) (65B_S4CLD2608_Master_Data_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for creating a Returnable Packaging (LEIH) product master via MM01 or F1602, across basic, sales, MRP, storage and accounting data."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/product-master-packaging]
aliases: [65B_S4CLD2608_Master_Data_EN_XX]
keywords: ["Product Master: Packaging and Returnable Packaging", product master data, returnable packaging, basic data, sales data, mrp planning data, storage location data, accounting data, material types, number ranges]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/65B_S4CLD2608_Master_Data_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-497
topic: 02-business-partner-and-product-master-data/product-master-packaging
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Master Data Script: Create Product Master of type "Returnable Packaging" - MDS (65B) (65B_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/65B_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Product Master: Packaging and Returnable Packaging** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Product Master of type "Returnable Packaging" - MDS (65B) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233904823)

[2 Prerequisites 3](#_Toc233904824)

[2.1 System Access 3](#_Toc233904825)

[2.2 Roles 3](#_Toc233904826)

[2.3 Required Organizational Units 3](#_Toc233904827)

[2.4 Mandatory and Optional Master Data 4](#_Toc233904828)

[2.5 Main Parameters for Data Creation 5](#_Toc233904829)

[2.5.1 Material Type and Number Ranges 5](#_Toc233904830)

[2.5.2 Industry Sector 5](#_Toc233904831)

[3 Overview Table 6](#_Toc233904832)

[4 Test Procedures 7](#_Toc233904833)

[4.1 Create Material (Product) Master Data - Basic Data 7](#_Toc233904834)

[4.2 Create Material (Product) Master Data - Sales Data (Sales Tax Data) 10](#_Toc233904835)

[4.3 Create Material (Product) Master Data - MRP/Planning Data (Plant Data) 14](#_Toc233904836)

[4.4 Create Material (Product) Master Data - Storage Location Data 16](#_Toc233904837)

[4.5 Create Material (Product) Master Data - Accounting Data 19](#_Toc233904838)

## Purpose

The material or product master contains information about all the physical materials that are stored and sold.

The material master holds information such as unique material number, name, material type, unit of measure, descriptions, weight and dimensions. This material information is used and stored in transactions such as sales orders, deliveries and goods movements.

As all information for one material is stored centrally, material master information is organized into different views. For example, sales, storage and accounting.

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

| Data Segment | Depends On | Field Examples | Comments | Organizational Unit to be Used |
| --- | --- | --- | --- | --- |
| Basic Data | Independent from organizational units | Material description (short text), Material number, Material Group, Base Unit of Measure, and so on. | Basic Data exists only once for a material master data record. | N/A |
| Sales Data | Plant, Sales Org., Distribution Channel | Tax Data, Item Category Group, Transp. Group, Loading Group, and so on. | Sales data can exist for every Sales Org. of your enterprise structure for which the material master record is used. | Plant:____________Sales Organization:__________Distribution Channel:__________ |
| MRP/Planning Data | Plant, Storage Location | MRP Type, MRP Controller, Planned delivery time, and so on. | Plant data can exist for every Plant ID of your enterprise structure for which the material master record is used.Storage location data (planning context) is optional based on the need to do storage location specific planning. | Plant:____________Storage Location:__________ |
| Storage Location Data | Plant, Storage Location | Profit center, and so on. | Plant data can exist for every Plant ID of your enterprise structure for which the material master record is used.Storage location data (planning context) is optional based on the need to do storage location specific planning. | Plant:____________Storage Location:__________ |
| Accounting Data | Valuation area(=Plant) | Per Unit Price, Price Control, and so on. | Valuation area data can exist for every Plant ID of your enterprise structure for which the material master record is used. Every plant represents a valuation area (e.g. different valuation price of a material in different plants). | Plant:____________Valuation type:__________ |

### Mandatory and Optional Master Data

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

This scope item consists of several process steps that are listed in the following table:

If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.

You can find all other apps not included on the homepage using the search bar.

If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder.

| Process Step | Business Role | Transaction / App | Expected Results |
| --- | --- | --- | --- |
| [Create Material (Product) Master Data - Basic Data](#unique_11) [page ] 7 | Master Data Specialist - Product Data | Create Material (MM01) / Manage Product Master Data (F1602) | Material Master Data - Basic Data is created. |
| [Create Material (Product) Master Data - Sales Data (Sales Tax Data)](#unique_12) [page ] 10 | Master Data Specialist - Product Data | Create Material (MM01) / Manage Product Master Data (F1602) | Material Master Data - Sales Data is created. |
| [Create Material (Product) Master Data - MRP/Planning Data (Plant Data)](#unique_13) [page ] 14 | Master Data Specialist - Product Data | Create Material (MM01) / Manage Product Master Data (F1602) | Material Master Data - MRP/Planning Data is created. |
| [Create Material (Product) Master Data - Storage Location Data](#unique_14) [page ] 16 | Master Data Specialist - Product Data | Create Material (MM01) / Manage Product Master Data (F1602) | Material Master Data - Storage Location Data is created. |
| [Create Material (Product) Master Data - Accounting Data](#unique_15) [page ] 19 | Master Data Specialist - Product Data | Create Material (MM01) / Manage Product Master Data (F1602) | Material Master Data - Accounting Data (Valuation Area Data) is created. |

## Test Procedures

This section describes procedures for each segment or process step that is part of this master record.

### Create Material (Product) Master Data - Basic Data

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Material (MM01) . | The Create Material (Initial Screen) is displayed. |  |
| 3 | Enter Material Basic Data | On the Create Material (Initial Screen) screen, enter the following:Material: <Material number>Industry Sector: Mechanical engineeringNote If the Industry Sector input field is hidden, no entry is required. When the industry sector is not offered for entry, the field is grayed out.Material Type: Returnable packagingChoose Select View(s). | The Select View(s) screen is displayed. |  |
| 4 | Choose Views | On the Select View(s) screen, select the following entries and choose Continue:Basic data 1Basic data 2 | The Create Material ... (Returnable packaging) screen is displayed. |  |
| 5 | Enter Basic Data | On the Basic data 1 tab, enter a material description (short text). |  |  |
| 6 | Enter Basic Data | Under the Basic data 1 tab, in the General Data section, enter the descriptions for the following:Base Unit of MeasureMaterial GroupGenItemCatGroup: LEIH |  |  |
| 7 | Enter Basic Data | In the Dimensions/EANs section, enter the following:Gross WeightUnit of WeightNet WeightPress Enter. | The next tab, Basic Data 2is displayed. |  |
| 8 | Complete Basic Data | No entries are required for Basic Data 2. |  |  |
| 9 | Save Your Data | At the bottom right of the screen, choose Save to save your data. | The Create Material (Initial Screen) screen is displayed.The Basic Data is created and saved. |  |

Procedure: Option 2 - Manage Product Master Data

Use the following procedure when your user access presents you with the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Product Master Data (F1602). | The Manage Product Master Data screen is displayed. |  |
| 3 | Choose Create New Product Master | On the Manage Product Master Data screen, in the Products section, choose Create. | The Create Master Data Record screen is displayed. |  |
| 4 | Enter Data for Mandatory Fields | On the Create Master Data Record screen, make the following entries:Product Number: for example, Z …Note You either enter any external alphanumeric ID, and that ID must start with an alphanumeric character, or if you provide no entry, the system automatically assigns a numeric ID.For more information about Product Number, see the previous Material Type and Number Ranges section.Product Type: LEIHProduct Group: for example, L006Base Unit: for example, PCDescription: <any description> |  |  |
| 5 | Choose OK | Choose OK. |  |  |
| 6 | Enter Basic Data | Go to Manage Product Master > General Information > Basic Data , and make the following entry:Division: for example, 00 |  |  |
| 7 | Choose Add (+) | Go to Manage Product Master > General Information > Descriptions , and choose Create. | Description in default language (for example, English) is already populated. |  |
| 8 | Enter Descriptions Data | In the Descriptions view, make the following entries:Language: for example, GermanProduct Description: <your description> |  |  |
| 9 | Enter Weight Date Data | In the Weight section (if not appearing, choose Show More), enter the following:Gross Weight: for example, 2Weight Unit: for example, KGNet Weight: for example, 1Note If Weight section does not appear, choose Show More.When fields Gross Weight, Weight Unit, or Net Weight don't provide an input-field, refresh or reload the web page. After refreshing or reloading, the fields are available for input. |  |  |
| 10 | Save Your Data | Choose Save. | The object is saved. |  |

### Create Material (Product) Master Data - Sales Data (Sales Tax Data)

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

You must complete the previous section, [Create Material (Product) Master Data - Basic Data](#unique_11) [page ] 7, before you proceed with this section.

Begin the procedure after you have saved the Basic Data entries, as described in the previous procedure.

Procedure: Option 1 - Create Material

Use the following procedure when your user access presents you with the Create Material (MM01) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Choose Create Material (MM01). | The Create Material (Initial Screen) is displayed. |  |
| 2 | Enter Material Basic Data | On the Create Material (Initial Screen) screen, make the following entries:Material: <Material number>Industry Sector: Mechanical engineeringNote If the Industry Sector input field is hidden, no entry is required. When the industry sector is not offered for entry, the field is grayed out.Material Type: LEIH Returnable packagingChoose Select View(s). | The Select View(s) screen is displayed. |  |
| 3 | Choose Views | On the Select View(s) screen, select Sales: Sales Org. Data 1, Sales: Sales Org. Data 2, and Sales: General/Plant Data and choose Continue. | The Organizational Levels screen is displayed. |  |
| 4 | Enter Organizational Levels Data | On the Organizational Levels screen, in the Organizational levels section, enter the descriptions for the following:PlantSales Org.Distr. ChannelChoose Continue.Note Information appears at the bottom of the screen: The material already exists and will be extended. | The Create Material ... (Returnable packaging) screen is displayed. |  |
| 5 | Enter Sales Data | On the Create Material ... (Returnable packaging) screen, under the Sales: sales org. 1 tab, in the General data section, make the following entries:Base Unit of MeasureDelivering Plant |  |  |
| 6 | Enter Sales Data | On the Create Material ... (Returnable packaging) screen, under the Sales: sales org. 1 tab, in the Tax Data section, make the following entries:Tax classification: 1Note The entered value indicated that the material is (usually) fully taxable.For Brazil only: in the Tax Data section, make the following entries:Country: BRTax Category: IBRXTax Classification: 1Press Enter. | The next tab, Sales: sales org. 2 is displayed. |  |
| 7 | Enter Sales Data | Under the Sales: sales org. 2 tab, in the Grouping terms section, make the following entries:Matl statistics grpItem Category Group: CB02Gen. item cat. grp: LEIHAcct Assmt Grp Mat.: Y2Press Enter. | The next tab, Sales: General/Plant is displayed. |  |
| 8 | Enter Sales Data | Under the Sales: General/Plant tab, in the General data section, enter the following data:Availability check: SR |  |  |
| 9 | Enter Sales Data | Under the Sales: General/Plant tab, in the Shipping data (times in days) section, enter the following data:Trans. Grp: <0001>Loading Grp: <0001> |  |  |
| 10 | Enter Sales Data | Under the Sales: General/Plant tab, in the General plant parameters section, enter the following data:Profit Center |  |  |
| 11 | Save your data | At the bottom of the screen, choose Save. | Your data is saved. |  |

Procedure: Option 2 - Manage Product Master Data

Use the following procedure when your user access presents you with the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Manage Product Master Data (F1602). | The app opens and various search fields are displayed. |  |
| 2 | Search and open the Product for edit | Search the previously created Product by entering Product Number in the Product search field.Select the Product from the list which will navigate you to the Product screen.Choose Edit. | The Product is displayed in edit mode (fields are ready for your input). |  |
| 3 | Choose Distributions Chains | On the Product screen, choose the Distribution Chains tab. | The Distribution Chains tab is displayed. |  |
| 4 | Choose Add (+) | Under the Distribution Chains tab, choose Create. | Distribution Chains is displayed in edit mode. |  |
| 5 | Enter Distribution Chains Data | On the Distribution Chains screen, make the following entries:Go to General Information > General Data :Sales Organization: <Sales org number>Note The organization unit value is determined by what is offered in the value help.Distribution Channel: for example,10Delivery Plant: <Plant number>In the Grouping Terms section:Item Category Group: for example, CB02Accounting Assignment Group: for example, Y2 Returnable goodsIn the Sales Tax section:Country: <country code>Tax Category: for example, TTX1Tax Classification: for example, either 1 for material or 2 for services. Tax Classification example: 1 Full tax when using UTXJ tax condition for the US.Note Tax classification depends on the specific requirements of the country. Tax classification in the material master and customer master tables determine percentage inputs.For Brazil only: In the Tax Classification section, make the following entries:Country: BRTax Category: IBRXTax Classification: 1 |  |  |
| 6 | Return to Main View | Choose Apply to return to the Product screen. | The Product screen is displayed. |  |
| 7 | Save Your Data | Choose Save. | The object is saved. |  |

### Create Material (Product) Master Data - MRP/Planning Data (Plant Data)

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

You must complete the previous procedure,[Create Material (Product) Master Data - Basic Data](#unique_11) [page ] 7, before you proceed with this section.

Begin the procedure after you have saved the Basic Data entries, as described in the previous procedure.

Procedure: Option 1 - Create Material

Use the following procedure when your user access presents you with the Create Material (MM01) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Create Material (MM01). | The Create Material (Initial Screen) is displayed. |  |
| 2 | Enter Material Basic Data | On the Create Material (Initial Screen) screen, make the following entries:Material: <Material number>Industry Sector: Mechanical engineeringNote If the Industry Sector input field is hidden, no entry is required. When the industry sector is not offered for entry, the field is grayed out.Material Type: Returnable packagingChoose Select View(s). | The Select View(s) screen is displayed. |  |
| 3 | Choose Views | On the Select View(s) screen, select MRP 1, MRP 2, MRP 3, and MRP 4, and choose Continue. | The Organizational Levels screen is displayed. |  |
| 4 | Enter Organizational Levels Data | On the Organizational Levels screen, in the Organizational levels section, make the following entries:Plant: <Plant number>Storage Location: <Storage location number>Choose Continue.Note Information appears at the bottom of the screen: The material already exists and will be extended. | The Create Material ... (Returnable packaging) screen is displayed. |  |
| 5 | Enter MRP/Planning Data | On the Create Material ... (Returnable packaging) screen, under the MRP 1 tab, in the MRP procedure section, make the following entries:MRP Type: NDMRP Controller: <001>Press Enter. | The next tab, MRP 2 is displayed. |  |
| 6 | Enter MRP/Planning Data | On the Create Material ... (Returnable packaging) screen, under the MRP 2 tab, in the Scheduling section, make the following entry:Planned Deliv. Time: for example, 10In the Procurement section, make the following entry:Procurement Type: FPress Enter. | The next tab, MRP 3 is displayed. |  |
| 7 | Enter MRP/Planning Data | On the Create Material ... (Returnable packaging) screen, under the MRP 3 tab, in the Availability check section, make the following entry:Availability check: for example, SRPress Enter. | The next tab, MRP 4 is displayed. |  |
| 8 | Save Your Data | At the bottom of the screen, choose Save. | Your data is saved. |  |

Procedure: Option 2 - Manage Product Master Data

Use the following procedure when your user access presents you with the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Manage Product Master Data (F1602) . | The app opens and various search fields are displayed. |  |
| 2 | Search and Open the Product for Edit | Search the previously created Product by entering Product Number in the Product search field.Select the Product from the list which will navigate you to the Product screen.Choose Edit. | The Product is displayed in edit mode (fields are ready for your input). |  |
| 3 | Choose Plants Data | On the Product screen, choose the Plants tab. | The Plants tab is displayed. |  |
| 4 | Choose Add (+) | Under the Plants tab, choose Create. | The Plant screen is displayed in edit mode. |  |
| 5 | Enter Plants - General Data | Go to General Information > General Data , and make the following entries:Plant: Plant number, for example, 1010Profit Center: for example, YB111In the Sales section, make the following entry:Loading Group: for example, 0001 |  |  |
| 6 | Enter Plants - MRP Data | Go to MRP Data > MRP Data , and make the following entries:Availability Check: for example, SRMRP Type: for example, NDMRP Controller: for example, 001 |  |  |
| 7 | Enter Plants - Procurement Data | Go to MRP Data > Procurement , and make the following entry:Planned Delivery Time: for example, 10 |  |  |
| 8 | Return to Main View | Choose Apply to return to the Product screen. | The Product screen is displayed. |  |
| 9 | Save Your Data | Choose Save. | The object is saved. |  |

### Create Material (Product) Master Data - Storage Location Data

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

You must complete the previous procedure, [Create Material (Product) Master Data - Basic Data](#unique_11) [page ] 7, before you proceed with this section.

Begin the procedure after you have saved the Basic Data entries, as described in the previous procedure.

Procedure: Option 1 - Create Material

Use the following procedure when your user access presents you with the Create Material (MM01) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Create Material (MM01). | The Create Material (Initial Screen) is displayed. |  |
| 2 | Enter Material Basic Data | On the Create Material (Initial Screen) screen, make the following entries:Material: <Material number>Industry sector: Mechanical engineeringNote If the Industry Sector input field is hidden, no entry is required. When the industry sector is not offered for entry, the field is grayed out.Material type: Returnable packagingChoose Select View(s). | The Select View(s) screen is displayed. |  |
| 3 | Choose Views | On the Select View(s) screen, select the following:General Plant Data/Storage 1General Plant Data/Storage 2Choose Continue. | The Organizational Levels screen is displayed. |  |
| 4 | Enter Organizational Levels Data | On the Organizational Levels screen, in the Organizational levels section, make the following entries:Plant: for example, <Plant number>Storage Location: <Storage location number>Choose Continue.Note Information appears at the bottom of the screen: The material already exists and will be extended. | The Create Material ... (Returnable packaging) screen is displayed. |  |
| 5 | Enter Storage Location Data | For the Plant data/stor. 1 tab, no entries are required. |  |  |
| 6 | Confirm Entries | For the Plant data/stor. 2 tab, no entries are required. |  |  |
| 7 | Save Your Data | At the bottom of the screen, choose Save. | Your data is saved. |  |

Procedure: Option 2 - Manage Product Master Data

Use the following procedure when your user access presents you with the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Manage Product Master Data (F1602). | The app opens and various search fields are displayed. |  |
| 2 | Search and Open the Product for Edit | Search the previously created Product by entering Product Number in the Product search field.Select the Product from the list which will navigate you to the Product screen.Choose Edit. | The Product is displayed in edit mode (fields are ready for your input). |  |
| 3 | Choose Plants Data | On the Product screen, choose the Plants tab.Note If there is no plant data record, follow the steps in the previous section, [Create Material (Product) Master Data - MRP/Planning Data (Plant Data)](#unique_13) [page ] 14. | The Plants tab is displayed. |  |
| 4 | Choose Plant Details | Under the Plants tab, use the arrow icon to select the plant data you created in the previous step. | The Plant screen is displayed. |  |
| 5 | Navigate to Plant: Storage Location | On the Plant screen, go to Storage Locations > Storage Locations . |  |  |
| 6 | Choose Add (+) | Under the Storage Locations tab, in the Storage Locations section, choose Create. | The Plant - Storage Locations view is displayed. |  |
| 7 | Enter Plant: Storage Location Data | In the Plant - Storage Locations view, make the following entry:Storage Location: <Storage location number> |  |  |
| 8 | Return to Main Screen | Choose Apply twice to return to the Product screen. | The Product screen is displayed. |  |
| 9 | Save Your Data | Choose Save. | The object is saved. |  |

### Create Material (Product) Master Data - Accounting Data

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

You must complete the previous procedure, [Create Material (Product) Master Data - Basic Data](#unique_11) [page ] 7, before you proceed with this section.

Begin the procedure after you have saved the Basic Data entries, as described in the previous procedure.

Procedure: Option 1 - Create Material

Use the following procedure when your user access presents you with the Create Material (MM01) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Create Material (MM01). | The Create Material (Initial Screen) is displayed. |  |
| 2 | Enter Material Basic Data | On the Create Material (Initial Screen) screen, make the following entries:Material: <Material number>Industry Sector: Mechanical engineeringNote If the Industry Sector input field is hidden, no entry is required. When the industry sector is not offered for entry, the field is grayed out.Material Type: Returnable packagingChoose Select View(s). | The Select View(s) screen is displayed. |  |
| 3 | Choose Views | On the Select View(s) screen, select the following:Accounting 1Accounting 2Choose Continue. | The Organizational Levels screen is displayed. |  |
| 4 | Enter Organizational Levels Data | On the Organizational Levels screen, in the Organizational levels section, make the following entry:Plant: <Plant number>Choose Continue.Note Information appears at the bottom of the screen: The material already exists and will be extended. | The Create Material ... (Returnable packaging) screen is displayed. |  |
| 5 | Enter Accounting Data | On the Create Material ... (Returnable packaging) screen, under the Accounting 1 tab, in the Current valuation section, make the following entries:Valuation Class: for example, 3050Moving price: for example, 5Price Control: for example, VPress Enter.Note Valuation class is not mandotory for LEIH type of product, you can set it as empty via App Change Material (MM02). | The next tab, Accounting 2 is displayed. |  |
| 6 | Confirm Entries | For the Accounting 2 tab, no entries are required. |  |  |
| 7 | Save Your Data | At the bottom of the screen, choose Save. | Your data is saved. |  |

Procedure: Option 2 - Manage Product Master Data

Use the following procedure when your user access presents you with the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Manage Product Master Data (F1602). | The app opens and various search fields are displayed. |  |
| 2 | Search and Open the Product for Edit | Search the previously created Product by entering Product Number in the Product search field.Select the Product from the list which will navigate you to the Product screen.Choose Edit. | The Product is displayed in edit mode (fields are ready for your input). |  |
| 3 | Choose Valuation Area Data | On the Product screen, choose the Valuation Areas tab. | The Valuation Areas tab is displayed. |  |
| 4 | Choose Create | Under the Valuation Areas tab, in the Valuation Areas section, choose Create. | The Valuation Area screen is displayed in edit mode. |  |
| 5 | Enter Current Valuation Area Data | Under the General Information tab, in the General Data section, make the following entries:Valuation Area: for example, 1010Valuation Class: for example, 3050In the Current Period section, make the following entries:Inventory Price: for example, 5Price Control: for example, Moving average price/periodic unit price (V) |  |  |
| 6 | Return to Main Screen | Choose Apply to return to the Product screen. | The Product screen is displayed. |  |
| 7 | Save Your Data | Choose Save. | The object is saved. |  |

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
- related-to :: [[02-business-partner-and-product-master-data/mds-65b-499]]
- related-to :: [[02-business-partner-and-product-master-data/mds-65b-501]]
- related-to :: [[02-business-partner-and-product-master-data/script-de-dados-mestre-criar-mestre-de-produtos-do-tipo-embalagem-reto]]
- related-to :: [[02-business-partner-and-product-master-data/script-de-datos-maestros-crear-maestro-de-productos-de-tipo-embalaje-e]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/65B_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 35,766 chars in the whole document
