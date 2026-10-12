---
id: 02-business-partner-and-product-master-data/master-data-script-create-product-master-of-type-trading-good-mds-bnf
title: "Master Data Script: Create Product Master of type \"Trading Good\" - MDS (BNF), SAP S/4HANA Cloud Public Edition (BNF_S4CLD2608_Master_Data_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for creating Trading Goods product master data per view, via Create Material (MM01) or Manage Product Master Data (F1602)."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/product-master-trading-goods]
aliases: [BNF_S4CLD2608_Master_Data_EN_XX]
keywords: ["Product Master: Trading Goods", product master data, trading goods, sales data, purchasing data, mrp planning data, storage location data, accounting data, configurable products, material type]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNF_S4CLD2608_Master_Data_EN_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-593
topic: 02-business-partner-and-product-master-data/product-master-trading-goods
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Master Data Script: Create Product Master of type "Trading Good" - MDS (BNF), SAP S/4HANA Cloud Public Edition (BNF_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNF_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Product Master: Trading Goods** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Product Master of type "Trading Good" - MDS (BNF) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc233904911)

[2 Prerequisites 4](#_Toc233904912)

[2.1 System Access 4](#_Toc233904913)

[2.2 Roles 4](#_Toc233904914)

[2.3 Required Organizational Units 4](#_Toc233904915)

[2.4 Mandatory and Operational Master Data 5](#_Toc233904916)

[2.5 Main Parameters for Data Creation 6](#_Toc233904917)

[2.5.1 Material Type and Number Ranges 6](#_Toc233904918)

[2.5.2 Industry Sector 6](#_Toc233904919)

[3 Overview Table 7](#_Toc233904920)

[4 Test Procedures 8](#_Toc233904921)

[4.1 Create Material (Product) Master Data - Basic Data 8](#_Toc233904922)

[4.2 Create Material (Product) Master Data - Sales Data (Sales Tax Data) 11](#_Toc233904923)

[4.3 Create Material (Product) Master Data - Purchasing Data 15](#_Toc233904924)

[4.4 Create Material (Product) Master Data - MRP/Planning Data (Plant Data) 17](#_Toc233904925)

[4.5 Create Material (Product) Master Data - Storage Location Data 20](#_Toc233904926)

[4.6 Create Material (Product) Master Data - Accounting Data (Valuation Area Data) 23](#_Toc233904927)

[4.7 Create Product Master Data - Configurable Product and Variants 25](#_Toc233904928)

[4.8 Create Product Master Data - Save Attachments 28](#_Toc233904929)

[4.9 Create Product Master Data - Plant Sales / General Data 30](#_Toc233904930)

[4.10 Create Product Master Data - Plant / Repetitive Manufacturing 32](#_Toc233904931)

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
| MRP/Planning Data | Plant, Storage Location | MRP Type, MRP Controller, Lot Size, Planned delivery time, and so on. | Plant data can exist for every Plant ID of your enterprise structure for which the material master record is used.Storage location data (planning context) is optional based on the need to do storage location specific planning | Plant:____________Storage Location:__________ |
| Storage Location Data | Plant, Storage Location | Number of GR slips, Max. Storage Period, Min. Rem. Shelf, and so on. | Plant data can exist for every Plant ID of your enterprise structure for which the material master record is used.Storage location data (planning context) is optional based on the need to do storage location specific planning. | Plant:____________Storage Location:__________ |
| Accounting Data | Valuation area (=Plant), Valuation type | Valuation Class, Per Unit Price, Price Control,and so on. | Valuation area data can exist for every Plant ID of your enterprise structure for which the material master record is used. Every plant represents a valuation area (e.g. different valuation price of a material in different plants) | Plant:____________Valuation type:__________ |

### Mandatory and Operational Master Data

Material master data records may refer to other master data. The following table gives an overview of optional and mandatory master data objects to be used in a material master data record.

|  |
| --- |
| Note Brazil specific fields are required to get a proper tax calculation.Check Nota Fiscal Brazil - JD0 in Define BR Specific Fields for Master Data chapter for material master data. |

| Master Data Object | Used in Data Segment | Mandatory / Optional | Comments |
| --- | --- | --- | --- |
| Profit Center |  | Mandatory | Assigning a Profit Center to a material (product) master is required for correct valuation processes. |

### Main Parameters for Data Creation

In this section, we describe some basic parameters that influence the behavior of a master record and are always required to create a material master data record:

#### Material Type and Number Ranges

With the help of material types, the system determines which data segments (views) can be maintained or which fields are mandatory or optional. Based on material types, the system also determines the number ranges for materials. In the SAP standard content, all material types use the same number range definition

| Number Range | Range / Business Partner ID | Comments |
| --- | --- | --- |
| External alpha-numeric | A – ZZZZZZZZ | This range must start with a character. Overall the ID must not be longer than 40 characters. |
| Internal numeric | 1 – 99999999 | This range is used if the system shall automatically assign a numeric number to a material. |

#### Industry Sector

The standard content only provides one industry sector M. Currently, this is visible in the SAP GUI only.

## Overview Table

This scope item consists of several process steps that are listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction / App | Expected Results |
| --- | --- | --- | --- |
| [Create Material (Product) Master Data - Basic Data](#unique_11) [page ] 8 | Master Data Specialist - Product Data | Create Material (MM01)/ Manage Product Master Data (F1602) | Material Master Data - Basic Data is created. |
| [Create Material (Product) Master Data - Sales Data (Sales Tax Data)](#unique_12) [page ] 11 | Master Data Specialist - Product Data | Create Material (MM01)/ Manage Product Master Data (F1602) | Material Master Data - Sales Data is created. |
| [Create Material (Product) Master Data - Purchasing Data](#unique_13) [page ] 15 | Master Data Specialist - Product Data | Create Material (MM01)/ Manage Product Master Data (F1602) | Material Master Data - Purchasing Data is created. |
| [Create Material (Product) Master Data - MRP/Planning Data (Plant Data)](#unique_14) [page ] 17 | Master Data Specialist - Product Data | Create Material (MM01)/ Manage Product Master Data (F1602) | Material Master Data - MRP/Planning Data is created. |
| [Create Material (Product) Master Data - Storage Location Data](#unique_15) [page ] 20 | Master Data Specialist - Product Data | Create Material (MM01)/ Manage Product Master Data (F1602) | Material Master Data - Storage Location Data is created. |
| [Create Material (Product) Master Data - Accounting Data (Valuation Area Data)](#unique_16) [page ] 23 | Master Data Specialist - Product Data | Create Material (MM01)/ Manage Product Master Data (F1602) | Material Master Data - Accounting Data (Valuation Area Data) is created. |
| [Create Product Master Data - Configurable Product and Variants](#unique_17) [page ] 25 | Master Data Specialist - Product Data | Create Material (MM01)/ Manage Product Master Data (F1602) | Create Configurable Product and Variants. |
| [Create Product Master Data - Save Attachments](#unique_18) [page ] 28 | Master Data Specialist - Product Data | Create Material (MM01)/ Manage Product Master Data (F1602) | Save attachments to the material master record. |
| [Create Product Master Data - Plant Sales / General Data](#unique_19) [page ] 30 | Master Data Specialist - Product Data | Create Material (MM01)/ Manage Product Master Data (F1602) |  |
| [Create Product Master Data - Plant / Repetitive Manufacturing](#unique_20) [page ] 32 | Master Data Specialist - Product Data | Create Material (MM01)/ Manage Product Master Data (F1602) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Material (Product) Master Data - Basic Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions on how to create Material (Product) master data. Apps available to you are dependent upon your assigned role, so two options are provided.

Procedure: Option 1 - Create Material

Follow this procedure when your user access presents you with the Create Material (MM01) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Material (MM01). | The app opens. |  |
| 3 | Enter Material Basic Data | On the Create Material (Initial view) screen, make the following entries:Material: <Material number>Industry Sector: MNote If the Industry Sector input field is hidden, no entry is required. When the Industry Sector is not offered for entry, the field is grayed out.Material type: Trading GoodsChoose Select View(s). | The Select View(s) screen displays. |  |
| 4 | Select Views | On the Select View(s) screen, select Basic data 1 and Basic data 2.Choose Continue. | The Create Material...(Trading Goods) screen displays. |  |
| 5 | Enter Basic Data | On the Material...(Trading Goods) screen, on the Basic data 1 tab, enter the Material description (short text). |  |  |
| 6 | Enter Basic Data | On the Basic data 1 tab, in the General Data section, make the following entries:Base Unit of Measure: <Base unit of measure>Material Group: <Material group>GenItemCatGroup: <GenItemCatGroup> |  |  |
| 7 | Enter Basic Data | In the Dimensions/EANs section, make the following entries:Gross Weight: <Gross weight>Unit of Weight: <Unit of weight>Net Weight: <Net weight>Press Enter. | The Basic data 2 tab displays. |  |
| 8 | Complete Basic Data | On the Basic data 2 tab, you do not need to make any entries. |  |  |
| 9 | Save Your Data | Choose Save to save your data. | The Create Material (Initial Screen) screen displays.The Basic Data is created and saved. |  |

Procedure: Option 2 - Manage Product Master Data

Follow this procedure when your user access presents you with the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Product Master Data (F1602). | The app opens. |  |
| 3 | Choose Create Product | On the Manage Product Master Data screen, choose Create Product. | The Create Master Data Record screen displays. |  |
| 4 | Enter Data for Mandatory Fields | On the Create Master Data screen, make the following entries:Product Number: For example, Z … or any external alphanumeric ID. It must start with a character or no entry, and then the system will assign a numeric ID automatically.Note For more information about Product Number, see the previous [Material Type and Number Ranges](#unique_8) [page ] 6 chapter.Product Type: Trading GoodsProduct Group: For example, L001.Base Unit: For example, PC.Description: <Any description> |  |  |
| 5 | Choose OK | On the Manage Product Master screen, choose OK. | The Manage Product Master screen displays. |  |
| 6 | Enter Basic Data | Go to the Manage Product Master > BASIC DATA > Basic Data screen, and make the following entry:Division: For example 00. |  |  |
| 7 | Choose Create | Go to the Manage Product Master > BASIC DATA > Descriptions screen, and choose Create. | Description in default language (for example, English) displays. |  |
| 8 | Enter Descriptions Data | On the Descriptions screen, make the following entries:Language: For example, German.Product Description: <Product description> |  |  |
| 9 | Return to Main Screen | Choose the back arrow to return to the main screen. | The Product Master screen displays. |  |
| 10 | Choose Base Unit of Measure | Go to Manage Product Master > BASIC DATA , and choose Base Unit of Measure. |  |  |
| 11 | Return to Main Screen | Choose the back arrow to return to the main screen. | The Product Master screen displays. |  |
| 12 | Save Your Data | Choose Save. | The system displays a notification indicating that the object is saved. |  |

### Create Material (Product) Master Data - Sales Data (Sales Tax Data)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions on how to create Material (Product) master data. Apps available to you are dependent upon your assigned role, so two options are provided.

Prerequisite

You must complete the previous chapter, [Create Material (Product) Master Data - Basic Data](#unique_11) [page ] 8, before you proceed with this chapter.

Follow the procedure after you have saved the Basic Data entries, as described in the previous chapter.

Procedure: Option 1 - Create Material

Follow this procedure when your user access presents you with the Create Material (MM01) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Create Material (MM01). | The app opens. |  |
| 2 | Enter Material Basic Data | On the Create Material (Initial screen) screen, make the following entries:Material: <Material number>Industry Sector: MNote If the Industry Sector input field is hidden, no entry is required. When the Industry Sector is not offered for entry, the field is grayed out.Material type: Trading GoodsChoose Select View(s). | The Select View(s) screen displays. |  |
| 3 | Select Views | On the Select View(s) screen, select Sales: Sales Org. Data 1, Sales: Sales Org. Data 2, and Sales: General/Plant Data.Choose Continue.Note For Poland Only: also select Foreign Trade - Export Data in order to enter PKWiU classification number. | The Organizational Levels screen displays. |  |
| 4 | Enter Organizational Levels Data | On the Organizational Levels screen, in the Organizational level section, make the following entries:PlantSales Org.Distr. ChannelChoose Continue.Note The system message displays that The material already exists and will be extended. | The Create Material…(Trading Goods) screen displays. |  |
| 5 | Enter Sales Data | On the Material…(Trading Goods) screen, on the Sales: sales org. 1 tab, in the General data section, make the following entries:Base Unit of MeasureDelivering Plant |  |  |
| 6 | Enter Sales Data | On the Material…(Trading Goods) screen, on the Sales: sales org. 1 tab, in the Tax Data section, make the following entry:Tax classification: 1Note The entered value indicates that the Material is (usually) fully taxable.For Brazil Only:In the Tax Data section, make the following entries:Country: BRTax Category: IBRXFiscal Classification: Either 1 for Material or 2 for Services. | The Sales: sales org. 2 tab displays. |  |
| 7 | Enter Sales Data | On the Sales: sales org 2 tab, in the Grouping terms section, make the following entries:Matl statistics grpItem category groupAcct Assmt Grp Mat.: 01 | The Sales: General/Plant tab displays. |  |
| 8 | Enter Sales Data | On the Sales: General/Plant tab, in the General data section, make the following entry:Availability check: SP |  |  |
| 9 | Enter Sales Data | On the Sales: General/Plant tab, in the Shipping data (times in days) section, make the following entries:Transp. Grp: <0001>Loading Grp: <0001> |  |  |
| 10 | Enter Sales Data | In the General Plant parameters section, make the following entry:Profit Center: <Profit center>Note For the SerialNoProfile, select a valid serial number profile which has been assigned with the proper equipment category for your business. |  |  |
| For Poland Only | Enter Sales Data | For Poland Only:In the International Trade: Export section, make the following entry:Control code: For example, 26.70.13.0. | PKWiU code for Poland is maintained. |  |
| 11 | Save Your Data | Choose Save. | Your data is saved. |  |

Procedure: Option 2 - Manage Product Master Data

Follow this procedure when your user access presents you with the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Manage Product Master Data (F1602). | The app opens. |  |
| 2 | Search and Open the Product for Edit | Search the previously created Product by entering the Product Number in the Product search field.Select the Product from the list which navigates you to the Product screen.Choose Edit. | The Product displays in edit mode (fields are ready for your input). |  |
| 3 | Choose Distributions Chains | On the Product screen, choose the Distribution Chains tab. | The Distribution Chains tab displays. |  |
| 4 | Choose + (Add) | On the Distribution Chains tab, choose + (Add). | The Distribution Chains screen displays in edit mode. |  |
| 5 | Enter Distribution Chains Data | On the Distribution Chains screen, make the following entries:In the GENERAL DATA - General Information section:Sales Organization: <Sales organization number>Note The Organization Unit value is determined by what is offered in the value help.Distribution Channel: For example 10.Delivery Plant: <Plant number>In the GROUPING TERMS section:Item Category Group: For example, NORM.Accounting Assignment Group: For example, 01 Trading Goods.In the SALES TAX section:Country: <Country code>Tax Category: For example, TTX1.Tax Classification: For example, either 1 for Material or 2 for Services.Tax Classification: For example, 1 Full tax when using UTXJ tax condition for US.Note Tax classification depends on the specific requirements of the country/region. Tax classification in the Material Master and Customer Master tables determines the percentage inputs.For Brazil Only:In the Tax Classificationsection, make the following entries:Country: BRTax Category: IBRXTax Classification: Either 1 for Material or 2 for Services. |  |  |
| 6 | Return to Main Screen | Choose Apply to return to the Productscreen. | The Product screen displays. |  |
| 7 | Save Your Data | Choose Save. | The system displays a notification indicating that the object is saved. |  |

### Create Material (Product) Master Data - Purchasing Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions on how to create Material (Product) master data. Apps available to you are dependent upon your assigned role, so two options are provided.

Prerequisite

You must complete the previous chapter, [Create Material (Product) Master Data - Basic Data](#unique_11) [page ] 8, before you proceed with this chapter.

Follow the procedure after you have saved the Basic Data entries, as described in the previous chapter.

Procedure: Option 1 - Create Material

Follow this procedure when your user access presents you with the Create Material (MM01) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Create Material (MM01). | The app opens. |  |
| 2 | Enter Material Basic Data | On the Create Material (Initial screen) screen, make the following entries:Material: <Material number>Industry Sector: MNote If the Industry Sector input field is hidden, no entry is required. When the Industry Sector is not offered for entry, the field is grayed out.Material type: Trading GoodsChoose Select View(s). | The Select View(s) screen displays. |  |
| 3 | Select Views | On the Select View(s) screen, select Purchasing and choose Continue. | The Organizational Levels screen displays. |  |
| 4 | Enter Organizational Levels Data | On the Organizational Levels screen, in the Organizational level section, make the following entry:Plant: <Plant number>Choose Continue.Note The system message displays that The material already exists and will be extended. | The Create Material…(Trading Goods) screen displays. |  |
| 5 | Enter Purchasing Data | On the Material…(Trading Goods) screen, on the Purchasing tab, in the General Data section, make the following entries:Base Unit of Measure: For example KG.Purchasing Group: For example, 001 .Material Group: For example, L001 . |  |  |
| 6 | Enter Purchasing Data | In the Other data/manufacturer data section, make the following entry:GR processing time: For example, 1 . |  |  |
| 7 | Save Your Data | Choose Save. | Your data is saved. |  |

Procedure: Option 2 - Manage Product Master Data

Follow this procedure when your user access presents you with the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Manage Product Master Data (F1602). | The app opens. |  |
| 2 | Search and Open the Product for Edit | Search the previously created Product by entering the Product Number in the Product search field.Select the Product from the list which navigates you to the Product screen.Choose Edit. | Product displays in edit mode (fields are ready for your input). |  |
| 3 | Choose Purchasing Data | On the Product screen, choose Purchasing. | The Purchasing screen displays. |  |
| 4 | Enter Purchasing Data | On the Purchasing screen, make the following entries:Purchasing Value Key: For example, 1.State of Variable Purchase Order Unit: ActiveIn the header data section, choose Edit Header and make the following entry:Product Group: For example, L001. |  |  |
| 5 | Save Your Data | Choose Save. | The system displays a notification indicating that the object is saved. |  |

### Create Material (Product) Master Data - MRP/Planning Data (Plant Data)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions on how to create Material (Product) master data. Apps available to you are dependent upon your assigned role, so two options are provided.

Prerequisite

You must complete the previous chapter, [Create Material (Product) Master Data - Basic Data](#unique_11) [page ] 8, before you proceed with this chapter.

Follow the procedure after you have saved the Basic Data entries, as described in the previous chapter.

Procedure: Option 1 - Create Material

Follow this procedure when your user access presents you with the Create Material (MM01) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Create Material (MM01). | The app opens. |  |
| 2 | Enter Material Basic Data | On the Create Material (Initial screen) screen, make the following entries:Material: <Material number>Industry Sector: MNote If the Industry Sector input field is hidden, no entry is required. When the Industry Sector is not offered for entry, the field is grayed out.Material type: Trading GoodsChoose Select View(s). | The Select View(s) screen displays. |  |
| 3 | Select Views | On the Select View(s) screen, select MRP1, MRP2, MRP3, and MRP4.Choose Continue. | The Organizational Levels screen displays. |  |
| 4 | Enter Organizational Levels Data | On the Organizational Levels screen, in the Organizational level section, make the following entries:Plant: <Plant number>Storage Location: <Storage location number> | The Create Material…(Trading Goods) screen displays. |  |
| 5 | Enter MRP/Planning Data | On the Create Material…(Trading Goods) screen, on the MRP1 tab, in the General Data section, make the following entries:MRP Type: PDMRP Controller: <001>Note The system message displays that The material already exists and will be extended. |  |  |
| 6 | Enter MRP/Planning Data | In the Lot size data section, make the following entry:Lot Sizing Procedure: <EX> | The MRP 2 tab displays. |  |
| 7 | Enter MRP/Planning Data | On the Create Material…(Trading Goods) screen, on the MRP 2 tab, in the Scheduling section, make the following entries:Planned Delivery Time: For example, 3.Goods Rec. Proc. Time: For example, 1.Scheduling Margin Key: For example, 000. | The MRP 3 tab displays. |  |
| 8 | Enter MRP/Planning Data | On the Create Material…(Trading Goods) screen, on the MRP 3 tab, in the Planning section, make the following entry:Strategy Group: For example, 40. |  |  |
| 9 | Enter MRP/Planning Data | In the Availability check section, make the following entries:Availability check: For example, SP.Tot. repl. Lead time: For example, 3. | The MRP 4 tab displays. |  |
| 10 | Enter MRP/Planning Data | On the Create Material…(Trading Goods) screen, on the MRP 4 tab, in the BOM explosion/dependent requirements section, make the following entry:Individual/Coll. Req.: 1 |  |  |
| 11 | Save Your Data | Choose Save. | Your data is saved. |  |

Procedure: Option 2 - Manage Product Master Data

Follow this procedure when your user access presents you with the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Manage Product Master Data (F1602). | The app opens. |  |
| 2 | Search and Open the Product for Edit | Search the previously created Product by entering the Product Number in the Product search field.Select the Product from the list which navigates you to the Product screen.Choose Edit. | Product displays in edit mode (fields are ready for your input). |  |
| 3 | Choose Plants Data | On the Product screen, choose Plants. | The Plants tab displays. |  |
| 4 | Choose Create | On the Plants tab, choose Create. | The Plant screen displays in edit mode. |  |
| 5 | Enter General Data | In the General Data section, make the following entries:Plant: <Plant number>, for example, 1710Profit Center : For example, YB700.Loading Grp: For example, 0001. |  |  |
| 6 | Enter MRP Data | Go to the MRP Data > MRP Data section, and make the following entries:Availability Check: For example, SP.MRP Type: For example, PD.MRP Controller: For example, 001. |  |  |
| 7 | Enter Lot-Size Data | In the MRP Data > Lot-Size Data section, make the following entry:Lot Sizing Procedure: For example EX. |  |  |
| 8 | Enter Procurement Data | Go to the MRP Data > Procurement section, and make the following entries:Planned Delivery Time: For example, 3.Goods Receipt Processing Time: For example, 1. |  |  |
| 9 | Choose Forecast Data | On the Plant screen, choose the Forecasting tab. | The Forecasting tab displays. |  |
| 10 | Enter Forecast Data | On the Forecasting tab, make the following entry:Period Type: For example, Monthly. |  |  |
| 11 | Return to Main Screen | Choose Apply to return to the Product screen. | The Product screen displays. |  |
| 12 | Save Your Data | Choose Save. | The system displays a notification indicating that the object is saved. |  |

### Create Material (Product) Master Data - Storage Location Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions on how to create Material (Product) master data. Apps available to you are dependent upon your assigned role, so two options are provided.

Prerequisite

You must complete the previous chapter, [Create Material (Product) Master Data - Basic Data](#unique_11) [page ] 8, before you proceed with this chapter.

Follow the procedure after you have saved the Basic Data entries, as described in the previous chapter.

Procedure: Option 1 - Create Material

Follow this procedure when your user access presents you with the Create Material (MM01) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Create Material (MM01). | The app opens. |  |
| 2 | Enter Material Basic Data | On the Create Material (Initial screen) screen, make the following entries:Material: <Material number>Industry Sector: MNote If the Industry Sector input field is hidden, no entry is required. When the Industry Sector is not offered for entry, the field is grayed out.Material type: Trading GoodsChoose Select View(s). | The Select View(s) screen displays. |  |
| 3 | Select Views | On the Select View(s) screen, select the following views:General Plant Data/Storage 1General Plant Data/Storage 2Choose Continue. | The Organizational Levels screen displays. |  |
| 4 | Enter Organizational Levels Data | On the Organizational Levels screen, in the Organizational level section, make following entries:Plant: <Plant number>Storage Location: <Storage location number>Note The system message displays that The material already exists and will be extended. | The Create Material…(Trading Goods) screen displays. |  |
| 5 | Enter Storage Location Data | On the Create Material…(Trading Goods) screen, on the Plant data/stor. 1 tab, in the General Data section, make the following entry:Number of GR slips: For example, 1. | The Plant data/stor.2 tab displays. |  |
| 6 | Confirm Entries | On the Plant data/stor. 2 tab, you do not need to make any entries.Note For the Serial No. Profile field, choose a valid serial number profile which has been assigned with the proper equipment category for your business. |  |  |
| 7 | Save Your Data | Choose Save. | The Master Data-Product screen displays.Your data is saved. |  |

Procedure: Option 2 - Manage Product Master Data

Follow this procedure when your user access presents you with the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Manage Product Master Data (F1602). | The app opens. |  |
| 2 | Search and Open the Product for Edit | Search the previously created Product by entering the Product Number in the Product search field.Select the Product from the list which navigates you to the Product screen.Choose Edit. | Product displays in edit mode (fields are ready for your input). |  |
| 3 | Choose Plants Data | On the Product screen, choose the Plants tab.Note If there is no plant data record, follow the steps in the previous chapter, [Create Material (Product) Master Data - MRP/Planning Data (Plant Data)](#unique_14) [page ] 17. | The Plants tab displays. |  |
| 4 | Choose Plant Details | On the Plants tab, use the arrow icon to select the plant data you created in the previous step. | The Plant screen displays. |  |
| 5 | Navigate to Plant: Storage Locations | On the Plant screen, go to Storage Locations > Storage Locations . |  |  |
| 6 | Choose Create | Go to Storage Locations > Storage Locations , and choose Create. | The Plant - Storage Location screen displays in edit mode. |  |
| 7 | Enter Plant: Storage Location Data | On the Storage Locations screen, make following entry:Storage Location: <Storage location number> |  |  |
| 8 | Return to Main Screen | Choose Apply twice to return to the Product screen. | The Productscreen displays. |  |
| 9 | Save Your Data | Choose Save. | The system displays a notification indicating that the object is saved. |  |

### Create Material (Product) Master Data - Accounting Data (Valuation Area Data)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions on how to create Material (Product) master data. Apps available to you are dependent upon your assigned role, so two options are provided.

Prerequisite

You must complete the previous chapter, [Create Material (Product) Master Data - Basic Data](#unique_11) [page ] 8, before you proceed with this chapter.

Follow the procedure after you have saved the Basic Data entries, as described in the previous chapter.

Procedure: Option 1 - Create Material

Follow this procedure when your user access presents you with the Create Material (MM01) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Create Material (MM01). | The app opens. |  |
| 2 | Enter Material Basic Data | On the Create Material (Initial screen), make the following entries:Material: <Material number>Industry sector: MNote If the Industry Sector input field is hidden, no entry is required. When the Industry Sector is not offered for entry, the field is grayed out.Material type: Trading GoodsChoose Select View(s). | The Select View(s) screen displays. |  |
| 3 | Choose Views | On the Select View(s) screen, select the following views:Accounting 1Accounting 2Choose Continue. | The Organizational Levels screen displays. |  |
| 4 | Enter Organizational Levels Data | On the Organizational Levels screen, in the Organizational level section, make the following entry:Plant: <Plant>Note Information displays at the bottom of the screen: The material already exists and will be extended. | The Create Material…(Trading Goods) screen displays. |  |
| 5 | Enter Accounting Data | On the Create Material…(Trading Goods) screen, on the Accounting 1 tab, in the General Valuation Data section, make the following entry:Valuation Class: <number> |  |  |
| 6 | Enter Data | In the Prices and values section, make the following entries:Per. Unit price: for example, 20Price Control: for example, V | The Accounting 2 tab displays. |  |
| 7 | Confirm Entries | You are not required to make any entries on the Accounting 2 tab. |  |  |
| 8 | Save Your Data | From the bottom of the screen, choose Save. | The Master Data - Product screen displays.Your data is saved. |  |

Procedure: Option 2 - Manage Product Master Data

Follow this procedure when your user access presents you with the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Choose Manage Product Master Data (F1602). | The app opens and various search fields display. |  |
| 2 | Search and Open the Product for Edit | Search the previously created Product by entring Product Number in the Product search field.Select the Product from the list which will navigate you to Product view.Choose Edit. | Product is displayed in edit mode (fields are ready for your input). |  |
| 3 | Choose Valuation Area Data | In the Product view, choose the Valuation Areas tab. | The Valuation Areas tab displays. |  |
| 4 | Choose Create | In the Valuation Areas section, choose Create. | Valuation opens in edit mode. |  |
| 5 | Enter Valuation Area Data | In the Valuation view, make the following entries:Valuation Area: <valuation area number>Price Control Determination: 2Valuation Class: for example, 3100 |  |  |
| 6 | Enter Current Valuation Area Data | Go to VALUATION AREAS > Valuation and make the following entries:Inventory Price: for example, 20Price Control Indicator: for example, VNote When you input V as the Price Control Indicator, the value added in Inventory Price becomes Moving Average Price. When you input S as the Price Control Indicator, the value added in Inventory Price becomes Standard Price. |  |  |
| 7 | Return to Main Screen | Choose Apply to return to the Product view. | The Manage Product Master view displays. |  |
| 8 | Save Your Data | Choose Save. | System message indicates that the object is saved. |  |

### Create Product Master Data - Configurable Product and Variants

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

You must complete the previous chapter, [Create Material (Product) Master Data - Basic Data](#unique_11) [page ] 8, before you proceed with this chapter.

Follow the procedure after you have saved the Basic Data entries, as described in the previous chapter.

Procedure: Option 1 - Create Material

Follow this procedure when your user access presents you with the Create Material (MM01) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Create Material (MM01). | The app opens. |  |
| 2 | Enter Material Basic Data | On the Create Material (Initial screen) screen, make the following entries:Material: <Material number>Industry Sector: MNote If the Industry Sector input field is hidden, no entry is required. When the Industry Sector is not offered for entry, the field is grayed out.Material type: Trading GoodsChoose Select View(s). | The Select View(s) screen displays. |  |
| 3 | Select Views | On the Select View(s) screen, select the following views and choose Continue:Basic data 1Basic data 2Classification |  |  |
| 4 | Enter Basic Data | On the Material (Finished Product) screen, on the Basic data 1 tab, enter the Material Description (short text) and Base Unit of Measure.Press Enter. | The Basic data 2 tab displays. |  |
| 5 | Enter Basic Data | On the Basic data 2 tab, check the Material is configurable checkbox.Press Enter. | The Classification tab displays and the Class Type dialog box displays. |  |
| 6 | Select Class Type | In the Class Type dialog box, select Class Type 300 (Variant) and choose Continue. | The Classification screen displays. |  |
| 7 | Assign Class | In the Assignment section, assign a Class and press Enter. | The corresponding Characteristics display under the Assignment section. |  |
| 8 | Choose Characteristics Values | Choose the required values for the Characteristics. |  |  |
| 9 | Save Your Data | Choose Save. | The Configurable Material is created. |  |
| 10 | Create Variant | To create a Variant, open the Create Material (MM01) tile again and follow the above steps to create a new Material with Basic data 1 and Basic data 2. |  |  |
| 11 | Create Variant | On the Basic data 2 tab, go to Client-specific configuration and enter the previously created Configurable Material in the Cross-plant CM field, choose Configure variant, and then choose the required Characteristics value to configure the variants. | The Variant is created. |  |

Procedure: Option 2 - Manage Product Master Data

Follow this procedure when your user access presents you with the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Manage Product Master Data (F1602). | The app opens. |  |
| 2 | Search and Open the Product for Edit | Search the previously created Product by entering the Product Number in the Product search field.Select the Product from the list which navigates you to the Product screen.Choose Edit. | Product displays in edit mode (fields are ready for your input). |  |
| 3 | Make Product Configurable | On the Product screen, go to the Configuration tab and check the Product is Configurable checkbox. |  |  |
| 4 | Assign Variant Class | On the Product screen, go to the Classification tab, choose Click here to assign a class, and then select a Class of Type 300 (Variant). | The Characteristics of the assigned Class display. |  |
| 5 | Choose Characteristics | Choose the required Characteristic values for each of the Characteristics. |  |  |
| 6 | Go to Variants Tab | On the Product screen, go to the Variants tab and choose Select Product Variants. | A tree/table displays with the different Characteristics. |  |
| 7 | Select Characteristics and Create Variants | Choose the combination of Characteristic values and choose Apply. | Variants are created. |  |
| 8 | Save | Choose Save. | The system displays a notification indicating that the object is saved. |  |

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

You must complete the previous chapter, [Create Material (Product) Master Data - Basic Data](#unique_11) [page ] 8, before you proceed with this chapter.

Follow the procedure after you have saved the Basic Data entries, as described in the previous chapter.

Procedure: Option 1 - Create Material

Follow this procedure when your user access presents you with the Create Material (MM01) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Create Material (MM01). | The app opens. |  |
| 2 | Enter Material Basic Data | On the Create Material (Initial screen) screen, make the following entries:Material: <Material number>Industry Sector: MNote If the Industry Sector input field is hidden, no entry is required. When the Industry Sector is not offered for entry, the field is grayed out.Material type: Trading GoodsChoose Select View(s). | The Select View(s) screen displays. |  |
| 3 | Select Views | On the Select View(s) screen, select Basic data 1 and Basic data 2.Choose Continue. | The Create Material (Finished Product) screen displays. |  |
| 4 | Choose Services for Object | In the application toolbar, go to Services for Object > Create Attachment . | The Import file screen displays. |  |
| 5 | Choose Upload | On the Import file screen, choose Upload. | A file upload screen displays. |  |
| 6 | Upload Attachment | Select the file and choose Open. | The file is uploaded. |  |
| 7 | Save | Select Choose and Save. | The system displays a notification indicating that the object is saved. |  |

Procedure: Option 2 - Manage Product Master Data

Follow this procedure when your user access presents you with the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Choose Manage Product Master Data (F1602). | The app opens. |  |
| 2 | Search and Open the Product for Edit | Search the previously created Product by entering the Product Number in the Product search field.Select the Product from the list which navigates you to the Product screen.Choose Edit. | Product displays in edit mode (fields are ready for your input). |  |
| 3 | Choose Attachments | On the Product screen, go to the Attachments tab. | The Attachments tab displays. |  |
| 4 | Choose Create | Under the Document Management System section, choose Create. | A file upload screen displays. |  |
| 5 | Upload Attachment | Select the file and choose Open. | The file is uploaded. |  |
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

The following procedure provides instructions on how to create Material (Product) master data. Apps available to you are dependent upon your assigned role, so two options are provided.

Prerequisite

You must complete the previous chapter, [Create Material (Product) Master Data - Basic Data](#unique_11) [page ] 8, before you proceed with this chapter.

Follow the procedure after you have saved the Basic Data entries, as described in the previous chapter.

Procedure: Option 1 - Create Material

Follow this procedure when your user access presents you with the Create Material (MM01) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Create Material (MM01) | The app opens. |  |
| 2 | Enter Material Basic Data | On the Create Material (Initial screen) screen, make the following entries:Material: <Material number>Industry Sector: MNote If the Industry Sector input field is hidden, no entry is required. When the Industry Sector is not offered for entry, the field is grayed out.Material type: Trading GoodsChoose Select View(s). | The Select View(s) screen displays. |  |
| 3 | Select Views | On the Select View(s) screen, select Basic Data and Sales: General/Plant Data.Choose Continue. | The Organizational Levels screen displays. |  |
| 4 | Enter Organizational Levels Data | On the Organizational Levels screen, in the Organizational level section, make the following entries:Plant: <Plant number>Storage Location: <Storage location number> | The Create Material…(Trading Goods) screen displays. |  |
| 5 | Enter Data in Basic Data 1 | On the Basic Data 1 screen, make the following entries and press Enter:Description: <Description of the Product>Base Unit: Maintain Base Unit EA, for example, 1. |  |  |
| 6 | Enter Data | In the Shipping data (times in days) section, make the following entry:LoadingGrp: <Choose any value from the value help> |  |  |
| 7 | Save Your Data | Choose Save. | Your data is saved. |  |

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
| 7 | Enter Plant- Sales | In the Sales section, make the following entry:Loading Group: <Choose from the value help> |  |  |
| 8 | Return to Main Screen | Choose Apply to return to the Product screen. | The Product screen displays. |  |
| 9 | Save Your Data | Choose Save. | The system displays a notification indicating that the object is saved. |  |

### Create Product Master Data - Plant / Repetitive Manufacturing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions on how to create Material (Product) master data. Apps available to you are dependent upon your assigned role, so two options are provided.

Prerequisite

You must complete the previous chapter, [Create Material (Product) Master Data - Basic Data](#unique_11) [page ] 8, before you proceed with this chapter.

Follow the procedure after you have saved the Basic Data entries, as described in the previous chapter.

Procedure: Option 1 - Create Material

Follow this procedure when your user access presents you with the Create Material (MM01) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Create Material (MM01) | The app opens. |  |
| 2 | Enter Material Basic Data | On the Create Material (Initial screen) screen, make the following entries:Material: <Material number>Industry Sector: MNote If the Industry Sector input field is hidden, no entry is required. When the Industry Sector is not offered for entry, the field is grayed out.Material type: Trading GoodsChoose Select View(s). | The Select View(s) screen displays. |  |
| 3 | Select Views | On the Select View(s) screen, select Basic Data 1, MRP 1, and MRP 4.Choose Continue. | The Organizational Levels screen displays. |  |
| 4 | Enter Organizational Levels Data | On the Organizational Levels screen, in the Organizational level section, make the following entries:Plant: <Plant number>Storage Location: <Storage location number> | The Create Material…(Trading Goods) screen displays. |  |
| 5 | Enter Data in Basic Data 1 | On the Basic Data 1 screen, make the following entries and press Enter:Description: <Description of the Product>Base Unit: Maintain Base Unit EA, for example, 1. |  |  |
| 6 | Enter Data MRP 1 | In the MRP procedure section, make the following entry:MRP Type: For example, ND. |  |  |
| 7 | Enter Data in MRP 4 | In the Repetitive manufacturing/ assembly / deployment strategy section, make the following entries:Repet. Manufacturing: Select the checkbox.REM Profile: <Choose any value from the value help> |  |  |
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
> Flagged while digesting this document, not verified: Sales Data row in the organizational units table lists Plant, Sales Org., Distribution Channel, while Option 2 steps use Distribution Chains tab without plant; minor wording inconsistency only

## Connections
- part-of :: [[_cluster]]
- related-to :: [[02-business-partner-and-product-master-data/mds-bnf-597]]
- related-to :: [[02-business-partner-and-product-master-data/sap-s-4hana-cloud-public-edition-bnf-595]]
- related-to :: [[02-business-partner-and-product-master-data/script-de-dados-mestre-criar-mestre-de-produtos-do-tipo-produto-comerc]]
- related-to :: [[02-business-partner-and-product-master-data/script-de-datos-maestros-crear-maestro-de-productos-de-tipo-mercaderia]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNF_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 59,154 chars in the whole document
