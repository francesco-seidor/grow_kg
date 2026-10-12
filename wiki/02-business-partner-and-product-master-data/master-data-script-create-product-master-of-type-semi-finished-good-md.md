---
id: 02-business-partner-and-product-master-data/master-data-script-create-product-master-of-type-semi-finished-good-md
title: "Master Data Script: Create Product Master of type \"Semi-Finished Good\" - MDS (BNS) (BNS_S4CLD2608_Master_Data_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for creating a HALB semi-finished product master via MM01 or F1602, by data view, with prerequisites."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/product-master-raw-semifinished-finished]
aliases: [BNS_S4CLD2608_Master_Data_EN_XX]
keywords: ["Product Master: Raw Materials, Semi-Finished and Finished…", product master data, semi-finished product, basic data, purchasing data, mrp planning data, storage location data, accounting data, configurable products, product attachments]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNS_S4CLD2608_Master_Data_EN_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-665
topic: 02-business-partner-and-product-master-data/product-master-raw-semifinished-finished
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Master Data Script: Create Product Master of type "Semi-Finished Good" - MDS (BNS) (BNS_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNS_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Product Master: Raw Materials, Semi-Finished and Finished Goods** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Product Master of type "Semi-Finished Good" - MDS (BNS) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233905004)

[2 Prerequisites 3](#_Toc233905005)

[2.1 System Access 3](#_Toc233905006)

[2.2 Roles 3](#_Toc233905007)

[2.3 Required Organizational Units 3](#_Toc233905008)

[2.4 Mandatory and Optional Master Data 4](#_Toc233905009)

[2.5 Main Parameters for Data Creation 4](#_Toc233905010)

[2.5.1 Material Type and Number Ranges 5](#_Toc233905011)

[2.5.2 Industry Sector 5](#_Toc233905012)

[3 Overview Table 6](#_Toc233905013)

[4 Test Procedures 7](#_Toc233905014)

[4.1 Create Product Master Data - Basic Data 7](#_Toc233905015)

[4.2 Create Product Master Data - Purchasing Data 9](#_Toc233905016)

[4.3 Create Product Master Data - MRP Planning Data / Plant Data 12](#_Toc233905017)

[4.4 Create Product Master Data - Storage Location Data 16](#_Toc233905018)

[4.5 Create Product Master Data - Accounting Data / Valuation Area Data 18](#_Toc233905019)

[4.6 Create Product Master Data – Configurable Product and Variants 21](#_Toc233905020)

[4.7 Create Product Master Data – Save Attachments 24](#_Toc233905021)

[4.8 Create Product Master Data - Plant Sales / General Data 26](#_Toc233905022)

[4.9 Create Product Master Data - Plant / Repetitive Manufacturing 28](#_Toc233905023)

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
| Basic Data | Independent of organizational units | Material description (short text), Material number, Material Group, Base Unit of Measure etc. | Basic Data exists only once for a material master data record. | n/a |
| Purchasing Data | Plant | Purchasing Group, Material Group, GR processing time etc. | Purchasing Data can exist for every purchasing organization for which the material shall be used in purchasing processes. | Plant:__________ |
| MRP/Planning Data (Plant Data) | Plant, Storage Location | MRP Type, MRP Controller, Lot Size, Planned delivery time etc. | Plant data can exist for every Plant ID of your enterprise structure for which the material master record is used.Storage location data (planning context) is optional based on the need to do storage location specific planning. | Plant:____________Storage Location:__________ |
| Storage Location Data | Plant, Storage Location | Number of GR slips, Max. Storage Period, Min. Rem. Shelf etc. | Plant data can exist for every Plant ID of your enterprise structure for which the material master record is used.Storage location data (planning context) is optional based on the need to do storage location specific planning. | Plant:____________Storage Location:__________ |
| Accounting Data | Valuation area (=Plant), Valuation type | Valuation Class, Per Unit Price, Price Control etc. | Valuation area data can exist for every Plant ID of your enterprise structure for which the material master record is used. Every plant represents a valuation area (for example, different valuation price of a material in different plants) | Plant:____________Valuation type:__________ |

### Mandatory and Optional Master Data

Material master data records may refer to other master data. The following table gives an overview of optional and mandatory master data objects to be used in a material master data record.

|  |
| --- |
| Note Brazil specific fields are required to get a proper tax calculation.Check Nota Fiscal Brazil - JD0 in Define BR Specific Fields for Master Data chapter for material master data. |

| Master Data Object | Used in Data Segment | Mandatory / Optional | Comments |
| --- | --- | --- | --- |
| Profit Center |  | Mandatory | Assigning a Profit Center to a material master is required for correct valuation processes. |

### Main Parameters for Data Creation

In this section, we describe some basic parameters that influence the behavior of a master record and are always required to create a material master data record.

#### Material Type and Number Ranges

With the help of material types, the system determines which data segments (views) can be maintained or which fields are mandatory or optional. Based on material types, the system also determines the number ranges for materials. In the SAP standard content, all material types use the same number range definition.

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

| Process Step | Business Role | Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Product Master Data - Basic Data](#unique_11) [page ] 7 | Master Data Specialist - Product Data | Create Material (MM01)/ Manage Product Master Data (F1602) | Material Master Data – Basic Data is created. |
| [Create Product Master Data - Purchasing Data](#unique_12) [page ] 9 | Master Data Specialist - Product Data | Create Material (MM01)/ Manage Product Master Data (F1602) | Material Master Data – Purchasing Data (Plant Data) is created. |
| [Create Product Master Data - MRP Planning Data / Plant Data](#unique_13) [page ] 12 | Master Data Specialist - Product Data | Create Material (MM01)/ Manage Product Master Data (F1602) | Material Master Data – MRP/Planning Data is created. |
| [Create Product Master Data - Storage Location Data](#unique_14) [page ] 16 | Master Data Specialist - Product Data | Create Material (MM01)/ Manage Product Master Data (F1602) | Material Master Data – Storage Location Data is created. |
| [Create Product Master Data - Accounting Data / Valuation Area Data](#unique_15) [page ] 18 | Master Data Specialist - Product Data | Create Material (MM01)/ Manage Product Master Data (F1602) | Material Master Data – Accounting Data (Valuation Data) is created. |
| [Create Product Master Data – Configurable Product and Variants](#unique_16) [page ] 21 | Master Data Specialist - Product Data | Create Material (MM01)/ Manage Product Master Data (F1602) | Create Configurable Product and Variants. |
| [Create Product Master Data – Save Attachments](#unique_17) [page ] 24 | Master Data Specialist - Product Data | Create Material (MM01)/ Manage Product Master Data (F1602) | Save attachments to the material master record. |
| [Create Product Master Data - Plant Sales / General Data](#unique_18) [page ] 26 | Master Data Specialist - Product Data | Create Material (MM01)/ Manage Product Master Data (F1602) |  |
| [Create Product Master Data - Plant / Repetitive Manufacturing](#unique_19) [page ] 28 | Master Data Specialist - Product Data | Create Material (MM01)/ Manage Product Master Data (F1602) |  |

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

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Material (MM01). | The Create Material (MM01) displays. |  |
| 3 | Enter Material Basic Data | On the Create Material (Initial view), make the following entries:Material: Material numberIndustry sector: MNote If the Industry Sector input field is hidden, no entry is required. When the industry sector is not offered for entry, the field is populated with in the dark.Material type: HALB (Semifinished Product)Click on Select View(s). | The Select View(s) view displays. |  |
| 4 | Choose Views | In the Select View(s) window, select Basic data 1 and Basic data 2 and choose Continue. | The Create Material (Semifinished Product) view displays. |  |
| 5 | Enter Basic Data | In the Material... (Semifinished Product) view, on the Basic data 1 tab, enter the Material Description (short text). |  |  |
| 6 | Enter Basic Data | On the Basic data 1 tab, in the General Data section, make the following entries:Base Unit of MeasureMaterial GroupGenItemCatGroup |  |  |
| 7 | Enter Basic Data | In the Dimensions/EANs section, make the following entries and confirm twice with Enter:Gross WeightWeight UnitNet WeightGo to Basic data 2 tab. | The Basic Data 2 tab displays. |  |
| 8 | Enter Basic Data | On the Basic Data 2 tab, you do not have to make any entries. Confirm with Enter. | A new view Last data view reached opens with the notification You are about to exit. Do you want to save your data for this material first?. |  |
| 9 | Save Your Data | In the Last data view reached choose Yes. | The Master Data - Product view displays.The Basic Data is created and saved. |  |

Procedure: Option 2 - Manage Product Master Data

Use the following procedure when your user access presents you with the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using your user credentials. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Product Master Data (F1602). | The Manage Product Master view opens.. |  |
| 3 | Choose Create New Product Master | In the Manage Product Master view, choose Create Product | The Create Master Data Record window displays. |  |
| 4 | Enter Data for Mandatory Fields | In the Create Master Data Record view, make the following entries:Product Number: for example, Z …either any external alphanumeric ID … (at least this needs to start with a character) or no entry so system assigns a numeric ID automaticallyProduct Type: HALB (Semifinished Product)Product Group : for example, L003Base Unit: for example, PCDescription: <any description> |  |  |
| 5 | Choose OK | In the Manage Product Master view, choose OK. | The Manage Product Master view displays. |  |
| 6 | Enter Basic Data | In the Manage Product Master > BASIC DATA > Basic Data view, make the following entry:Division: for example 00 |  |  |
| 7 | Choose Create | On the Product view go to BASIC DATA > Descriptions facet, choose Create. | Description in default language (for example, English) is already populated |  |
| 8 | Enter Descriptions Data | In the Descriptions view, make the following entries:Language: for example, GermanProduct Description: <your description> | Descriptions can be maintained in different languages. |  |
| 9 | Choose Base Unit of Measure | In the Manage Product Master > BASIC DATA view, choose Base Unit of Measure | The Base Unit of Measure view displays. |  |
| 10 | Save Your Data | ChooseSave. | The system issues a notification indicating the object is saved. |  |

### Create Product Master Data - Purchasing Data

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

Begin the procedure after you have saved the Basic Data entries, as described in the previous section.

Procedure: Option 1 - Create Material

Use the following procedure when your user access presents you with the Create Material (MM01) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Create Material (MM01). | The Create Material (Initial view) displays. |  |
| 2 | Enter Material Basic Data | In the Create Material (Initial view), make the following entries:Material: Material numberIndustry sector:MNote If the Industry Sector input field is hidden, no entry is required. When the industry sector is not offered for entry, the field is populated with in the dark.Material type: HALB (Semifinished Product)Click on Select View(s). | The Select View(s) view displays. |  |
| 3 | Choose Views | In the Select View(s) window, select Purchasing and choose Continue.Note For Poland only: in order to enter PKWiU code, select also Foreign Trade - Import Data before choosing Continue. | The Organizational Levels view displays. |  |
| 4 | Enter Organizational Levels Data | On the Organizational Levels view, in the Organizational levels section, make the following entry and choose Continue:Plant: <Plant number> | The Create Material (Semifinished Product) view displays. |  |
| 5 | Enter Purchasing Data | In the Material (Semifinished Product) view, on the Purchasing tab, in the General Data section, make the following entries:Purchasing Group: for example 001Material Group: for example, L003 |  |  |
| 6 | Enter Purchasing Data | In the Other data/manufacturer data section, make the following entry:GR processing time: for example 1 | A new window Last data view reached opens with the message You are about to exit. Do you want to save your data for this material first?. |  |
| For Poland Only | Enter Foreign Trade - Import Data | For Poland, in the Foreign Trade Data section, enter PKWiU code data:Control code: for example, 24.10.32.0 | PKWiU code for Poland is maintained. |  |
| 7 | Save Your Data | In the Last data view reached window, choose Yes. | The Master Data - Product window displays.Your data is saved. |  |

Procedure: Option 2 - Manage Product Master Data

Use the following procedure when your user access presents you with the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Manage Product Master Data (F1602). | Manage Product Master Data app opens and various search fields are displayed. |  |
| 2 | Search and Open the Product for Edit | Search the previously created Product by entering Product Number in the Product search field.Select the Product from the list which will navigate you to Product view.Click on Edit. | Product is displayed in edit mode (fields are ready for your input). |  |
| 3 | Choose Purchasing Data | In the Product Master view, choose PURCHASING | The PURCHASING view displays. |  |
| 4 | Enter Purchasing Data | On the PURCHASING view, make the following entry:• Purchasing Value Key: for example 1 |  |  |
| 5 | Save Your Data | Choose Save. | System notification indicates that the object is saved. |  |

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

You must complete the previous section, Create Product Master Data - Basic Data, before you proceed with this section.

Begin the procedure after you have saved the Basic Data entries, as described in the previous procedure.

Procedure: Option 1 - Create Material

Use the following procedure when your user access presents you with the Create Material (MM01) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Create Material (MM01). | The Create Material (Initial view) view displays. |  |
| 2 | Enter Material Basic Data | On the Create Material (Initial view), make the following entries:Material: Material numberIndustry sector: MNote If the Industry Sector input field is hidden, no entry is required. When the industry sector is not offered for entry, the field is populated with in the dark.Material type: HALB (Semifinished Product)Click on Select View(s). | The Select View(s) view displays. |  |
| 3 | Choose Views | In the Select View(s) window, select MRP1, MRP2, MRP3 and MRP4 and choose Continue. | The Organizational Levels view displays. |  |
| 4 | Enter Organizational Levels Data | On the Organizational Levels view, in the Organizational level section, make the following entries:PlantStorage Location | The Create Material (Semifinished Product) view displays. |  |
| 5 | Enter MRP/Planning Data | On the Material (Semifinished Product) view, on the MRP 1 tab, in the General Data section, make the following entries:MRP Type: PDPlanning time fenceMRP Controller: 001 | You get the following system message at the bottom of the view: The material already exists and will be extended. | . |
| 6 | Enter MRP/Planning Data | In the Lot Sizing Procedure section, make the following entry:Lot Sizing Procedure: EX | The MRP 2 view displays. |  |
| 7 | Enter MRP/Planning Data | In the Create Material (Semifinished Product) view, on the MRP 2 tab, in the Procurement section, make the following entries:Procurement typeProd. Stor. location |  |  |
| 8 | Enter MRP/Planning Data | In the Scheduling section, make the following entries:In-house productionPlanned delivery timeGR processing timeSchedMargin key | The MRP 3 view displays. |  |
| 9 | Enter MRP/Planning Data | In the Create Material (Semifinished Product) view, on the MRP 3 tab, in the Planning section, make the following entries:Strategy GroupConsumption modeBwd consumption per.Fwd consumption per. |  |  |
| 10 | Enter MRP/Planning Data | In the Availability check section, make the following entries:Availability checkTot. repl. Lead time | The MRP 4 view displays. |  |
| 11 | Enter MRP/Planning Data | Note For scope item Subcontracting - BMY, you need to maintain the Production Versions field to ensure correct functionality.On the Create Material (Semifinished Product) view, on the MRP 4 tab, in the BOM explosion/dependent requirements section, make the following entry:Individual/coll. | A new window Last data view reached opens with the message: You are about to exit. Do you want to save your data for this material first? |  |
| 12 | Save Your Data | In the Last data view reached window, choose Yes. | The Master Data - Product view displays.Your data is saved. |  |

Procedure: Option 2 - Manage Product Master Data

Use the following procedure when your user access presents you with the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Manage Product Master Data (F1602). | The Manage Product Master Data app opens and various search fields are displayed. |  |
| 2 | Search and Open the Product for Edit | Search the previously created Product by entering Product Number in the Product search field.Select the Product from the list which will navigate you to Product view.Click on Edit. | Product is displayed in edit mode (fields are ready for your input). |  |
| 3 | Choose Plants Data | In the Product Master view, choose PLANTS. | The PLANTS view displays. |  |
| 4 | Choose Create | In the PLANTS view, choose Create. | The Plant view opens in Edit Mode. |  |
| 5 | Enter Plants - General Information Data | In the Plant > GENERAL INFORMATION view, make following entries:Plant: <Plant number>Profit Center: for example, YB110 or YB111Loading Grp: for example, 0001 | The Create Material (Semifinished Product) view displays. |  |
| 6 | Enter Plants - MRP Data | Note For scope item Subcontracting - BMY, you need to maintain the Strategy Group field as well.In the Product Master view, choose MRP DATA.In the MRP DATA view, choose MRP Data, and make the following entries:Availability Check: for example, SPPlanned Delivery Time: for example, 3Goods Receipt Processing Time: for example, 1MRP Type : For example, PD MRPMRP Controller : For example, 001 |  |  |
| 7 | Enter Plants - Lot-Size Data | From the MRP DATA view, choose Lot-Sized DataIn the Lot-Sized Data view, entry the following:Lot Sizing Procedure: for example, EX |  |  |
| 8 | Enter Plants – Procurement Data | In the MRP Data > Procurement section, make the following entry:● Planned Delivery Time: for example, 3● Goods Receipt Processing Time: for example, 1 |  |  |
| 9 | Choose Plants - Forecast Data | In the Manage Product Master - PLANTS view, choose FORECASTING | The Plant - FORECASTING view displays. |  |
| 10 | Enter Plants - Forecast Data | In the FORECASTING view, make the following entries:Period Type: for example, M |  |  |
| 11 | Return to Main View | Choose Apply to return to Product view. | Return to the Product Master view . |  |
| 12 | Save Your Data | Choose Save. | The system displays a notification that the object is saved. |  |

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

You must complete the previous section, Create Product Master Data - Basic Data, before you proceed with this section.

Begin the procedure after you have saved the Basic Data entries, as described in the previous section.

Procedure: Option 1 - Create Material

Use the following procedure when your user access presents you with the Create Material (MM01) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Create Material (MM01). | The Create Material (Initial view) displays. |  |
| 2 | Enter Material Basic Data | In the Create Material (Initial view), make the following entries:Material: Material numberIndustry sector: MNote If the Industry Sector input field is hidden, no entry is required. When the industry sector is not offered for entry, the field is populated with in the dark.Material type: HALB (Semifinished Product)Choose Select View(s). | The Select View(s) view displays. |  |
| 3 | Select Views | In the Select View(s) window, select the following views and choose Continue:General Plant Data/Storage 1General Plant Data/Storage 2 | The Organizational Levels view displays. |  |
| 4 | Enter Organizational Levels Data | In the Organizational Levels view, in the Organizational level section, make the following entries:Plant: <Plant number>Storage Location: <Storage location number> | A new window opens, showing the Create Material (Semifinished Product) view.The following system message displays at the bottom of the view: The material already exists and will be extended. |  |
| 5 | Enter Storage Location Data | In the Create Material (Semifinished Product) view, on the Plant data/stor. 1 tab, in the General Data section, make the following entry and confirm with Enter:Number of GR slips: for example, 1 | The Plant data/stor.2 tab displays. |  |
| 6 | Confirm Entries | On the Plant data/stor. 2 tab, in the General Plant parameters section, make the following entries:Profit Center: for example, YB110 or YB111SerialNoProfileChoose a valid serial number profile which has been assigned with the proper equipment category for your business. | A new window Last data view reached displays with the following message You are about to exit. Do you want to save your data for this material first?. |  |
| 7 | Save Your Data | In the Last data view reached window, choose Yes. | The Master Data - Product view displays.Your data is saved. |  |

Procedure: Option 2 - Manage Product Master Data

Use the following procedure when your user access presents you with the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Manage Product Master Data (F1602). | Manage Product Master Data app opens and various search fields are displayed. |  |
| 2 | Search and Open the Product for Edit | Search the previously created Product by entering Product Number in the Product search field.Select the Product from the list which will navigate you to Product view.Choose Edit. | Product is displayed in edit mode (fields are ready for your input). |  |
| 3 | Choose Plants Data | In the Manage Product Master view, choose PLANTSNote If you haven't already added a plant data record, follow the steps in the previous procedure, Create Product Master Data - MRP Planning Data / Plant Data. | The PLANTS view displays. |  |
| 4 | Choose Plant Details | In the PLANTS view, use the right arrow icon to select the Plant Data you have created in the previous procedure. | The Product Master Plant view displays. |  |
| 5 | Navigate to Plant: Storage Location | In the PLANTS view, navigate to PLANTS > STORAGE LOCATION | The PLANTS view opens in Edit Mode. |  |
| 6 | Choose Create | From the PLANTS > STORAGE LOCATIONS > Storage Locations view, choose Create. | TheStorage Location view opens in Edit Mode. |  |
| 7 | Enter Plant: Storage Location Data | In the Storage Location view, make the following entries:Storage Location: <Storage location number | The New Record - Storage Location view displays. |  |
| 8 | Return to Main View | Choose back arrow, twice, to return the Product Master. | Return to the Product Master view. |  |
| 9 | Save Your Data | Choose Save. | The system displays a notification indicating the object is saved. |  |

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

You must complete the previous section, Create Product Master Data - Basic Data, before you proceed with this section.

Begin the procedure after you have saved the Basic Data entries, as described in the previous procedure.

Procedure: Option 1 - Create Material

Use the following procedure when your user access presents you with the Create Material (MM01) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Create Material (MM01). | The Create Material (Initial view) displays. |  |
| 2 | Enter Material Basic Data | In the Create Material (Initial view), make the following entries:Material: Material numberIndustry sector: MNote If the Industry Sector input field is hidden, no entry is required. When the industry sector is not offered for entry, the field is populated with in the dark.Material type: HALB (Semifinished Product)Click on Select View(s). | The Select View(s) view displays. |  |
| 3 | Choose Views | In the Select View(s) window, select the following views and choose Continue:Accounting 1Accounting 2 | The Organizational Levels view displays. |  |
| 4 | Enter Organizational Levels Data | On the Organizational Levels view, in the Organizational level section, make the following entries:Plant | A new window displays, showing the Create Material (Semifinished Product) view.The following system message displays at the bottom of the view: The material already exists and will be extended | . |
| 5 | Enter Accounting Data | In the Create Material (Semifinished Product) view, on the Accounting 1 tab, in the General Valuation Data section, make the following entry:Valuation Class: for example, 7900 |  |  |
| 6 | Enter Accounting Data | In the Prices and values section, make the following entries:Standard PricePer. Unit price: for example, 20Prc. Ctrl: for example, STo confirm your entries, press Enter twice. | The Accounting 2 tab displays. |  |
| 7 | Confirm Entries | In the Accounting 2 tab, you do not have to make any entries. | A new window Last data view reached displays with the message You are about to exit. Do you want to save your data for this material first?. |  |
| 8 | Save Your Data | In the window Last data view reached, choose Yes. | The Master Data - Product window displays.Your data is saved. |  |

Procedure: Option 2 - Manage Product Master Data

Use the following procedure when your user access presents you with the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Manage Product Master Data (F1602). | Manage Product Master Data app opens and various search fields are displayed. |  |
| 2 | Search and Open the Product for Edit | Search the previously created Product by entering Product Number in the Product search field.Select the Product from the list which will navigate you to Product view.Click on Edit. | Product is displayed in edit mode (fields are ready for your input). |  |
| 3 | Choose Valuation Area Data | From the Product Master view, choose VALUATION AREA. | The VALUATION AREA view area displays. |  |
| 4 | Choose Create | In the New Product Master - VALUATION AREA view section, choose Create. | The Product Master - Valuation view opens in edit mode. |  |
| 5 | Enter Valuation Area Data | In the New Product Master - Valuation view make following entries:Valuation Area: <number>Price Control Determination: for example, 2Note For Brazil only: Price Determination for Brazil must be 3, for Brazilian Cost Accounting principles.Valuation Class: <number>, for example, 3100 |  |  |
| 6 | Enter Current Valuation Area Data | In the VALUATION AREAS > VALUATION view, choose Current Period... and make the following entries:Moving Average Price: for example, 20Price Control Indicator: for example, S |  |  |
| 7 | Return to Main View | Choose Apply to return to Product view. | Return to the main Product Master view. |  |
| 8 | Save Your Data | Choose Save. | The system issues a notification indicating the object has been saved. |  |

### Create Product Master Data – Configurable Product and Variants

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

You must complete a previous procedure, Create Product Master Data – Basic Data, before you proceed with this procedure.

Begin the procedure after you have saved the Basic Data entries, as described in the previous procedure.

Procedure: Option 1 – Create Material

Use the following procedure when your user access presents you with the Create Material (MM01) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Create Material (MM01). | A new window opens, showing the Create Material (Initial Screen). |  |
| 2 | Enter Material Basic Data | On the Create Material (Initial Screen), make the following entries:Material: <Material number>Industry sector: MNote If the Industry Sector input field is hidden, no entry is required. When the industry sector is not offered for entry, the field is populated with in the dark.Material type: HALB (Semifinished Product)Choose Select View(s). | A new window opens, showing the Select View(s) view. |  |
| 3 | Choose Views | In the Select View(s) window, select the following views and choose Continue:Basic data 1Basic data 2Classification |  |  |
| 4 | Enter Basic Data | In the Material (Finished Product) view, on the Basic data 1 tab, enter the Material Description (short text) and Base Unit of Measure.Press Enter. | The Basic data 2 tab displays. |  |
| 5 | Enter Basic Data | In the Basic data 2 tab, check the Material is configurable checkbox.Press Enter. | Classification tab displays and Class Type popup opens. |  |
| 6 | Choose Class Type | In the Class Type dialog box, select class type 300 (Variant) and choose Continue. | The Classification view displays. |  |
| 7 | Assign Class | In the Assignment section, assign a class and press Enter. | Corresponding characteristics displays below the Assignment section. |  |
| 8 | Choose Characteristics Values | Choose the required values of the characteristics. |  |  |
| 9 | Save Your Data | Choose Save. | Configurable material is created. Now you need to create variant. |  |
| 10 | Create Variant | For creating Variant, again open Create Material tile and follow the above steps to create a new material with Basic data 1 and Basic data 2. |  |  |
| 11 | Create Variant | In Basic data 2, go to Client-specific configuration and enter the previously created Configurable material in the Cross-plant CM. Choose Configure variant and then choose required characteristics value to configure variants. | Variant is created. |  |

Procedure: Option 2 – Manage Product Master Data

Use the following procedure when your user access presents you with the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Manage Product Master Data (F1602). | Manage Product Master Data app opens and various search fields are displayed. |  |
| 2 | Search and Open the Product for Edit | Search the previously created Product by entering Product Number in the Product search field.Select the Product from the list which will navigate you to the Product view.Choose Edit. | Product is displayed in edit mode (fields are ready for your input). |  |
| 3 | Make Product Configurable | In the Product view, go to Configuration tab and check the Product is Configurable checkbox. |  |  |
| 4 | Assign Variant Class | In the Product view, go to Classification tab and choose Click here to assign a class. Then select a class of type 300 (Variant). | The characteristics of the assigned class is displayed. |  |
| 5 | Choose Characteristics | Choose the required characteristic values for each characteristic. |  |  |
| 6 | Go to the Variants Tab | In the Product view, go to Variants tab and choose Select Product Variants | A tree/table is displayed with the different characteristics. |  |
| 7 | Select Characteristics and Create Variants | Choose the combination of characteristic values and choose Apply. | Variants are created. |  |
| 8 | Save | Choose Save. | The system issues a notification that the object is saved. |  |

### Create Product Master Data – Save Attachments

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

You must complete a previous procedure, Create Product Master Data – Basic Data, before you proceed with this procedure.

Begin the procedure after you have saved the Basic Data entries, as described in the previous procedure.

Procedure: Option 1 – Create Material

Use the following procedure when your user access presents you with the Create Material (MM01) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Create Material (MM01). | A new window opens, showing the Create Material (Initial Screen). |  |
| 2 | Enter Material Basic Data | On the Create Material (Initial Screen), in More menu choose Material > Change > Immediately , and make the following entries:Material: Material numberIndustry sector: MNote If the Industry Sector input field is hidden, no entry is required. When the industry sector is not offered for entry, the field is populated with dark.Material type: HALB (Semifinished Product)Choose Select View(s). | A new window opens, showing the Select View(s) view. |  |
| 3 | Choose Views | In the Select View(s) window, select Basic data 1 and Basic data 2 and choose Continue. | The Create Material (Finished Product) view displays. |  |
| 4 | Choose Services for Object | In the application toolbar click on Services for Object > Create Attachment . | Import file window opens. |  |
| 5 | Choose Upload | Import file window, choose Upload button. | A file upload window opens. |  |
| 6 | Upload Attachment | Select the file and choose Open. | File is uploaded. |  |
| 7 | Save | Select Choose and Save. | The system issues a notification that the object is saved. |  |

Procedure: Option 2 – Manage Product Master Data

Use the following procedure when your user access presents you with the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Manage Product Master Data (F1602). | Manage Product Master Data app opens and various search fields are displayed. |  |
| 2 | Search and Open the Product for Edit | Search the previously created Product by entering Product Number in the Product search field.Select the Product from the list which will navigate you to Product view.Click on Edit. | Product is displayed in edit mode (fields are ready for your input). |  |
| 3 | Choose Attachments | In the Product view, go to Attachments tab. | Attachments view displays. |  |
| 4 | Choose Create | Under the Document Management System section, choose Create. | A file upload window opens. |  |
| 5 | Upload Attachment | Select the file and choose Open. | File is uploaded. |  |
| 6 | Save | Choose Save. | The system issues a notification that the object is saved. |  |

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
| 2 | Enter Material Basic Data | In the Create Material (Initial screen), make the following entries:Material: <Material number>Industry sector: MNote If the Industry Sector input field is hidden, no entry is required. When the industry sector is not offered for entry, the field is populated with in the dark.Material type: HALBChoose Select View(s). | Select View(s) screen opens. |  |
| 3 | Choose Views | In the Select View(s) window select Basic Data and Sales: General/Plant Data and choose continue. | Organizational Levels appears |  |
| 4 | Enter Organizational Levels Data | In the Organizational Levels screen, in the Organizational level section, make following entries:Plant: <Plant number>Storage Location: <Storage location number> | The Create Material…(Trading Goods) screen opens. |  |
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

The following procedure provides instructions for creating material (product) master data. Apps available to you are dependent upon your assigned role, so two options are provided.

Prerequisite

You must complete the previous procedure, Creating Material (Product) Master Data - Basic Data, before you proceed with this section.

Begin the procedure after you have saved the Basic Data entries, as described in the previous procedure.

Procedure: Option 1 - Create Material

Use the following procedure when your user access presents you with the Create Material (MM01) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Create Material (MM01) | Create Material (Initial Screen) opens. |  |
| 2 | Enter Material Basic Data | In the Create Material (Initial screen), make the following entries:Material: <Material number>Industry sector: MNote If the Industry Sector input field is hidden, no entry is required. When the industry sector is not offered for entry, the field is populated with in the dark.Material type: HALBChoose Select View(s). | Select View(s) screen opens. |  |
| 3 | Choose Views | In the Select View(s) window select Basic Data 1, MRP 1 and MRP 4 and choose continue. | Organizational Levels appears |  |
| 4 | Enter Organizational Levels Data | In the Organizational Levels screen, in the Organizational level section, make following entries:Plant: <Plant number>Storage Location: <Storage location number> | The Create Material…(Trading Goods) screen opens. |  |
| 5 | Enter Data in Basic Data 1 | In View Basic Data 1 make the following entries and choose Enter:Description : Maintain description for productBase Unit: Maintain Base Unit "EA" for example 1 |  |  |
| 6 | Enter Data in MRP 1 | In the MRP procedure section make the following entry:MRP Type: Maintain MRP Type “ND” for example |  |  |
| 7 | Enter Data in MRP 4 | In the Repetitive manufacturing/ assembly / deployment strategy section make the following entry:Rpet. Manufacturing : Select the checkboxREM Profile: choose any value from value help |  |  |
| 8 | Save Your Data | At the bottom of the screen, choose Save. | Your data is saved. |  |

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
| 7 | Enter Repetitive Manufacturing Data | In the Repetitive Manufacturing section make following entries:Repetitive Manufacturing Enabled: select the checkbox to enable Repetitive Manufacturing Profile fieldRepetitive Manufacturing Profile: choose any value from value help | On checking Repetitive Manufacturing Enabled checkbox, the Repetitive Manufacturing Profile field should be editable.On unchecking Repetitive Manufacturing Enabled checkbox, the Repetitive Manufacturing Profile field should be display only. |  |
| 8 | Return to Main Screen | Choose Apply to return to Product view. | The Product view displays. |  |
| 9 | Save Your Data | Choose Save. | System message indicates that the object is saved. |  |

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
> Flagged while digesting this document, not verified: Some steps in plant sales and repetitive manufacturing procedures mention 'Trading Goods' screens and the attachment procedure mentions 'Finished Product' although material type is HALB; wording inconsistent inside the script.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[02-business-partner-and-product-master-data/mds-bns-669]]
- related-to :: [[02-business-partner-and-product-master-data/mds-bns-sap-s-4hana-cloud-public-edition-2608-japanese-667]]
- related-to :: [[02-business-partner-and-product-master-data/script-de-dados-mestre-criar-mestre-de-produtos-do-tipo-produto-semiac]]
- related-to :: [[02-business-partner-and-product-master-data/script-de-datos-maestros-creacion-de-maestro-de-productos-de-tipo-prod]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNS_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 54,326 chars in the whole document
