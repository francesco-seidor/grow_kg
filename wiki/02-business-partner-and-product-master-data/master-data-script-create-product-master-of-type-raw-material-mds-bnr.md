---
id: 02-business-partner-and-product-master-data/master-data-script-create-product-master-of-type-raw-material-mds-bnr
title: "Master Data Script: Create Product Master of type \"Raw Material\" - MDS (BNR) (BNR_S4CLD2608_Master_Data_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for creating a Raw Material (ROH) product master across views, via Create Material (MM01) or Manage Product Master Data (F1602)."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/product-master-raw-semifinished-finished]
aliases: [BNR_S4CLD2608_Master_Data_EN_XX]
keywords: ["Product Master: Raw Materials, Semi-Finished and Finished…", product master data, material master creation, basic data, purchasing data, mrp planning data, storage location data, accounting data, configurable products, product attachments]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNR_S4CLD2608_Master_Data_EN_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-659
topic: 02-business-partner-and-product-master-data/product-master-raw-semifinished-finished
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Master Data Script: Create Product Master of type "Raw Material" - MDS (BNR) (BNR_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNR_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Product Master: Raw Materials, Semi-Finished and Finished Goods** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Product Master of type "Raw Material" - MDS (BNR) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233905012)

[2 Prerequisites 3](#_Toc233905013)

[2.1 System Access 3](#_Toc233905014)

[2.2 Roles 3](#_Toc233905015)

[2.3 Required Organizational Units 3](#_Toc233905016)

[2.4 Mandatory and Optional Master Data 4](#_Toc233905017)

[2.5 Main Parameters for Data Creation 5](#_Toc233905018)

[2.5.1 Material Type and Number Ranges 5](#_Toc233905019)

[2.5.2 Industry Sector 5](#_Toc233905020)

[3 Overview Table 6](#_Toc233905021)

[4 Test Procedures 7](#_Toc233905022)

[4.1 Create Material Master Data - Basic Data 7](#_Toc233905023)

[4.2 Create Material Master Data - Purchasing Data 10](#_Toc233905024)

[4.3 Create Material Master Data - MRP/Planning Data (Plant Data) 12](#_Toc233905025)

[4.4 Create Material Master Data - Storage Location Data 15](#_Toc233905026)

[4.5 Create Material Master Data - Accounting Data (Valuation Area Data) 18](#_Toc233905027)

[4.6 Create Product Master Data - Configurable Product and Variants 21](#_Toc233905028)

[4.7 Create Product Master Data - Save Attachments 24](#_Toc233905029)

[4.8 Create Product Master Data - Plant Sales / General Data 26](#_Toc233905030)

[4.9 Create Product Master Data - Plant / Repetitive Manufacturing 28](#_Toc233905031)

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
| Purchasing Data | Plant | Purchasing Group, Material Group, GR processing time, and so on. | Purchasing Data can exist for every purchasing organization for which the material shall be used in purchasing processes. | Plant:__________ |
| MRP/Planning Data | Plant, Storage Location | MRP Type, MRP Controller, Lot Size, Planned delivery time, and so on. | Plant data can exist for every Plant ID of your enterprise structure for which the material master record is used.Storage location data (planning context) is optional based on the need to do storage location specific planning | Plant:____________Storage Location:__________ |
| Storage Location Data | Plant, Storage Location | Number of GR slips, Max. Storage Period, Min. Rem. Shelf, and so on. | Plant data can exist for every Plant ID of your enterprise structure for which the material master record is used.Storage location data (planning context) is optional based on the need to do storage location specific planning | Plant:____________Storage Location:__________ |
| Accounting Data | Valuation area (=Plant), Valuation type | Valuation Class, Per Unit Price, Price Control, and so on. | Valuation area data can exist for every Plant ID of your enterprise structure for which the material master record is used. Every plant represents a valuation area (for example, different valuation price of a material in different plants) | Plant:____________Valuation type:__________ |

### Mandatory and Optional Master Data

Material master data records may refer to other master data. The following table gives an overview of optional and mandatory master data objects to be used in a material master data record.

|  |
| --- |
| Note Brazil specific fields are required to get a proper tax calculation.Check Nota Fiscal Brazil - JD0 in Define BR Specific Fields for Master Data chapter for material master data. |

| Master Data Object | Used in Data Segment | Mandatory / Optional | Comments |
| --- | --- | --- | --- |
|  |  | Optional |  |
|  |  | Mandatory |  |

### Main Parameters for Data Creation

In this section, we describe some basic parameters that influence the behavior of a master record and are always required to create a material master data record:

#### Material Type and Number Ranges

With the help of material types, the system determines which data segments (views) can be maintained or which fields are mandatory or optional. Based on material types, the system also determines the number ranges for materials. In the SAP standard content, all material types use the same number range definition

| Number Range | Range / Business Partner ID | Comments |
| --- | --- | --- |
| External alpha-numeric | A – ZZZZZZZZ | This range must start with a character. Overall the ID must not be longer than 40 characters. |
| Internal numeric | 1 – 99999999 | This range is used if the system shall automatically assign a numeric number to a material. |

#### Industry Sector

The standard content only provides one industry sector M.

|  |
| --- |
| Note Currently, this is only visible in SAP GUI. |

## Overview Table

This scope item consists of several process steps that are listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Material Master Data - Basic Data](#unique_11) [page ] 7 | Master Data Specialist - Product Data | Create Material (MM01)/ Manage Product Master Data (F1602) | Basic Material Master Data is created. |
| [Create Material Master Data - Purchasing Data](#unique_12) [page ] 10 | Master Data Specialist - Product Data | Create Material (MM01)/ Manage Product Master Data (F1602) | Purchasing Master Data is created. |
| [Create Material Master Data - MRP/Planning Data (Plant Data)](#unique_13) [page ] 12 | Master Data Specialist - Product Data | Create Material (MM01)/ Manage Product Master Data (F1602) | MRP Planning Master Data is created. |
| [Create Material Master Data - Storage Location Data](#unique_14) [page ] 15 | Master Data Specialist - Product Data | Create Material (MM01)/ Manage Product Master Data (F1602) | Storage Location Master Data is created. |
| [Create Material Master Data - Accounting Data (Valuation Area Data)](#unique_15) [page ] 18 | Master Data Specialist - Product Data | Create Material (MM01)/ Manage Product Master Data (F1602) | Accounting Master Data is created. |
| [Create Product Master Data - Configurable Product and Variants](#unique_16) [page ] 21 | Master Data Specialist - Product Data | Create Material (MM01)/ Manage Product Master Data (F1602) or Change Material (MM02) if needed | Configurable Product and Variants are created. |
| [Create Product Master Data - Save Attachments](#unique_17) [page ] 24 | Master Data Specialist - Product Data | Create Material (MM01)/ Manage Product Master Data (F1602) | Save attachments to the Material master record. |
| [Create Product Master Data - Plant Sales / General Data](#unique_18) [page ] 26 | Master Data Specialist - Product Data | Create Material (MM01)/ Manage Product Master Data (F1602) |  |
| [Create Product Master Data - Plant / Repetitive Manufacturing](#unique_19) [page ] 28 | Master Data Specialist - Product Data | Create Material (MM01)/ Manage Product Master Data (F1602) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Material Master Data - Basic Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions on how to create Material master data. Apps available to you are dependent upon your assigned role, so two options are provided.

Procedure: Option 1 - Create Material

Follow this procedure when your user access presents you with the Create Material (MM01) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using your user credentials. | The SAP Fiori launchpad displays.Note Logging on via the launchpad is only relevant in case of Web GUI use. |  |
| 2 | Access the SAP Fiori App | Open Create Material (MM01). | The app opens. |  |
| 3 | Enter Material Basic Data | On the Create Material (Initial Screen) screen, make the following entries:Material: <Material number>Industry Sector: MNote If the Industry Sector input field is hidden, no entry is required. When the Industry Sector is not offered for entry, the field is grayed out.Material type: ROH (Raw materials)Choose Select View(s). | The Select View(s) screen displays. |  |
| 4 | Select Views | On the Select View(s) screen, select Basic data 1 and Basic data 2.Choose Continue. | The Create Material (Raw materials) screen displays. |  |
| 5 | Enter Basic Data | On the Material … (Raw materials) screen, on the Basic data 1 tab, enter description for the Descr. field. |  |  |
| 6 | Enter Basic Data | On the Basic data 1 tab, in the General Data section, make the following entries:Base Unit of Measure: <Base unit of measure>Material Group: <Material group>GenItemCatGroup: <GenItemCatGroup> |  |  |
| 7 | Enter Basic Data | In the Dimensions/EANs section, make the following entries:Gross Weight: <Gross weight>Unit of Weight: <Unit of weight>Net Weight: <Net weight>Press Enter. | The Basic data 2 tab displays. |  |
| 8 | Enter Basic Data | On the Basic data 2 tab, you do not need to make any entries. | The Last data screen reached screen displays with the message You are about to exit. Do you want to save your data for this material first?. |  |
| 9 | Save Your Data | On the Last data screen reached screen, choose Yes. | The Master Data - Product screen displays.The Basic Data is created and saved. |  |

Procedure: Option 2 - Manage Product Master Data

Follow this procedure when your user access presents you with the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using your user credentials. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | In the Product Master catalog, choose the Manage Product Master Data (F1602). | The app opens. |  |
| 3 | Choose Create | On the Manage Product Master Data screen, choose Create. | The Create Master Data Record screen displays. |  |
| 4 | Enter Mandatory Fields | On the Create Master Data Record screen, make the following entries and choose OK:Product Number: For example, Z or any external alphanumeric ID. It must start with a character or no entry, and then the system will assign a numeric ID automatically.Note For more information about Product Number creation, see the previous [Material Type and Number Ranges](#unique_8) [page ] 5 chapter.Product Type: ROHProduct Group: For example, L002.Base Unit: For example, PC.Description: <Any description> |  |  |
| 5 | Return to Main Screen | Return to the Manage Product Master screen. | The Manage Product Master screen displays. |  |
| 6 | Enter Basic Data | Go to Manage Product Master > BASIC DATA > Basic Data , and make the following entry:Division: For example, 00. |  |  |
| 7 | Add a Description | Go to Manage Product Master > BASIC DATA > Description , and choose Create. | Description in default language (for example, English) displays. |  |
| 8 | Enter Description Data | On the Description screen, make the following entries:Language: For example, German.Product Description: <Product description> |  |  |
| 9 | Return to Main Screen | Choose the back arrow to return to the main screen. | The Product Master screen displays. |  |
| 10 | Choose Base Unit of Measure | Go to General Information > BASIC DATA , and choose Base Unit of Measure. | The Base Unit of Measure screen displays. |  |
| 11 | Save Your Data | Choose Create. | The system message displays that Master data record created, indicating that the object is saved. |  |

### Create Material Master Data - Purchasing Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions on how to create Material master data. Apps available to you are dependent upon your assigned role, so two options are provided.

Prerequisite

You have completed and saved the basic data for the Material as described in the previous section, [Create Material Master Data - Basic Data](#unique_11) [page ] 7.

Procedure: Option 1 - Create Material

Follow this procedure when your user access presents you with the Create Material (MM01) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Create Material (MM01). | The app opens. |  |
| 2 | Enter Material Basic Data | On the Create Material (Initial Screen) screen, make the following entries:Material: <Material number>Industry Sector: MNote If the Industry Sector input field is hidden, no entry is required. When the Industry Sector is not offered for entry, the field is grayed out.Material type: ROH (Raw materials)Choose Select View(s). | The Select View(s) screen displays. |  |
| 3 | Select Views | On the Select View(s) screen, select Purchasing and choose Continue.Note For Poland only: in order to enter PKWiU code, also select Foreign Trade - Import Data before choosing Continue. | The Organizational Levels screen displays. |  |
| 4 | Enter Organizational Levels Data | On the Organizational Levels screen, in the Organizational level section, make the following entry and choose Continue:Plant: <Plant code> | The Create Material (Raw materials) screen displays.The system message displays that The material already exists and will be extended. |  |
| 5 | Enter Purchasing Data | On the Material (Raw materials) screen, on the Purchasing tab, in the General Data section, make the following entries:Purchasing Group: <Purchasing group number>Material Group: For example, L002. |  |  |
| 6 | Enter Purchasing Data | In the Other data / manufacturer data section, make the following entry:GR processing time: For example, 1. | The Last data screen reached screen displays with the message You are about to exit. Do you want to save your data for this material first?. |  |
| For Poland Only | Enter Foreign Trade - Import Data | For Poland only: in the Foreign Trade Data section, enter PKWiU code data:Control code: For example, 24.10.32.0. | PKWiU code for Poland is maintained. |  |
| 7 | Save Your Data | On the Last data screen reached screen, choose Yes. | The Master Data - Product screen displays.Your data is saved. |  |

Procedure: Option 2 - Manage Product Master Data

Follow this procedure when your user access presents you with the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Manage Product Master Data (F1602). | The app opens. |  |
| 2 | Search and Open the Product for Edit | Search the previously created Product by entering the Product Number in the Product search field.Select Product (Original) from the list which navigates you to the Product screen.Choose Edit. | The Product displays in edit mode (fields are ready for your input). |  |
| 3 | Choose Purchasing Data | On the Product Master screen, choose Purchasing. | The Purchasing screen displays. |  |
| 4 | Edit Header | Choose Edit Header at the top of the screen and make the following entry:Product Group: For example, A001. | The Edit Header screen displays. |  |
| 5 | Enter Purchasing Data | On the Purchasing screen, make the following entry:Purchasing Value Key: For example, 1. |  |  |
| 6 | Save Your Data | Choose Save. | The system message indicates that the object is saved. |  |

### Create Material Master Data - MRP/Planning Data (Plant Data)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions on how to create Material master data. Apps available to you are dependent upon your assigned role, so two options are provided.

Prerequisite

You have filled out the data for the Material as described in the previous section, [Create Material Master Data - Basic Data](#unique_11) [page ] 7 and have completed and saved the Purchasing master data.

Procedure: Option 1 - Create Material

Follow this procedure when your user access presents you with the Create Material (MM01) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Create Material (MM01). | The app opens. |  |
| 2 | Enter Material Basic Data | On the Create Material (Initial Screen) screen, make the following entries:Material: <Material number>Industry Sector: MNote If the Industry Sector input field is hidden, no entry is required. When the Industry Sector is not offered for entry, the field is grayed out.Material type: ROH (Raw materials)Choose Select View(s). | The Select View(s) screen displays. |  |
| 3 | Select Views | On the Select View(s) screen, select MRP1, MRP2, MRP3, and MRP4.Choose Continue. | The Organizational Levels screen displays. |  |
| 4 | Enter Organizational Levels Data | On the Organizational Levels screen, in the Organizational level section, make the following entries:Plant: For example, 1710.Storage Location: For example, 171C. | The Create Material (Raw materials) screen displays. |  |
| 5 | Enter MRP/Planning Data | On the Material (Raw materials) screen, on the MRP 1 tab, in the MRP procedure section, make the following entries:MRP Type: For example, PD.MRP Controller: For example, 001. | The system message displays that The material already exists and will be extended. |  |
| 6 | Enter MRP/Planning Data | In the Lot size data section, make the following entry:Lot Sizing Procedure: For example, EX. | The MRP 2 tab displays. |  |
| 7 | Enter MRP/Planning Data | On the Create Material (Raw materials) screen, on the MRP 2 tab, in the Procurement section, make the following entries:Procurement type: For example, F.Production Storage LocationStor. Location for Ext. Proc. |  |  |
| 8 | Enter MRP/Planning Data | In the Scheduling section, make the following entries:Planned delivery time: For example, 3.Goods Rec. Proc. Time: For example, 1.Scheduling Margin Key: For example, 000. | The MRP 3 tab displays. |  |
| 9 | Enter MRP/Planning Data | On the Create Material (Raw materials) screen, on the MRP 3 tab, in the Availability check section, make the following entries:Availability check: For example, SP.Total Repl. Lead Time: For example, 3. | The MRP 4 tab displays. |  |
| 10 | Enter MRP/Planning Data | On the Create Material (Raw materials) screen, on the MRP 4 tab, in the BOM Explosion / Dependent Requirements section, make the following entry:Individual/Coll. Req.: 2 | The Last data screen reached screen displays with the message You are about to exit. Do you want to save your data for this material first?. |  |
| 11 | Save Your Data | On the Last data screen reached screen, choose Yes. | The Master Data - Product screen displays.Your data is saved. |  |

Procedure: Option 2 - Manage Product Master Data

Follow this procedure when your user access presents you with the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Manage Product Master Data (F1602). | The app opens. |  |
| 2 | Search and Open the Product for Edit | Search the previously created Product by entering the Product Number in the Product search field.Select the Product from the list which navigates you to the Product screen.Choose Edit. | The Product displays in edit mode (fields are ready for your input). |  |
| 3 | Choose Plants | On the Product Master screen, choose PLANTS. | The PLANTS screen displays. |  |
| 4 | Choose Create | In the PLANTS section, choose Create. | The Plants screen displays in edit mode. |  |
| 5 | Enter Plants - General Information Data | On the Plant - General Information screen, make the following entries:Plant: <Plant number>Profit Center: For example, YB110 or YB111.In the Sales section, make the following entry:Loading Group: For example, 0001. |  |  |
| 6 | Enter Plants - MRP Data | On the MRP Data screen, make the following entries:Availability Check: For example, SP.Planned Delivery Time: For example, 3.Goods Receipt Processing Time: For example, 1.MRP Type: For example, PD.MRP Controller: For example, 001. |  |  |
| 7 | Enter Plants - Lot-Size Data | On the MRP DATA screen, choose Lot-Size Data.On the Lot-Size Data screen, make the following entry:Lot Sizing Procedure: For example, EX. |  |  |
| 8 | Enter Plants - Procurement Data | Go to MRP Data > Procurement , and make the following entries:Planned Delivery Time: For example, 3.Goods Receipt Processing Time: For example, 1. |  |  |
| 9 | Choose Plants - Forecasting | On the Product Master - PLANTS screen, choose FORECASTING. | The Plant - FORECASTING screen displays. |  |
| 10 | Enter Forecasting Data | On the FORECASTING screen, make the following entry:Period Type: For example, M. |  |  |
| 11 | Return to the Main Screen | Choose Apply. | The Manage Product Master screen displays. |  |
| 12 | Save Your Data | Choose Save. | The system message indicates that the object is saved. |  |

### Create Material Master Data - Storage Location Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions on how to create Material master data. Apps available to you are dependent upon your assigned role, so two options are provided.

Prerequisite

You have filled out the data for the Material as described in the previous section, [Create Material Master Data - Basic Data](#unique_11) [page ] 7 and have completed and saved the MRP/Planning data.

Procedure: Option 1 - Create Material

Follow this procedure when your user access presents you with the Create Material (MM01) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Create Material (MM01). | The app opens. |  |
| 2 | Enter Material Basic Data | On the Create Material (Initial Screen) screen, make the following entries:Material: <Material number>Industry Sector: MNote If the Industry Sector input field is hidden, no entry is required. When the Industry Sector is not offered for entry, the field is grayed out.Material type: ROH (Raw materials)Choose Select View(s). | The Select View(s) screen displays. |  |
| 3 | Select Views | On the Select View(s) screen, select the following views and choose Continue:General Plant Data/Storage 1General Plant Data/Storage 2 |  |  |
| 4 | Enter Organizational Levels Data | Choose Org. Levels at the top of the screen.On the Organizational Levels screen, in the Organizational level section, make the following entries:Plant: <Plant code>Storage Location: <Storage Location number> | The Create Material (Raw materials) screen displays.The system message displays that The material already exists and will be extended. |  |
| 5 | Enter Storage Location Data | On the Create Material (Raw materials) screen, on the Plant data/stor. 1 tab, in the General Data section, make the following entry:Number of GR slips: For example, 1.Press Enter to navigate to the next screen. | The Plant data/stor.2 tab displays. |  |
| 6 | Confirm Entries | On the Plant data/stor. 2 tab, in the General Plant parameters section, make the following entries:Profit Center: <Profit Center>Serial No. Profile: <Serial number profile>Choose a valid serial number profile which has been assigned with the proper equipment category for your business. | The Last data screen reached displays with the message You are about to exit. Do you want to save your data for this material first?. |  |
| 7 | Save Your Data | On the Last data screen reached screen, choose Yes. | The Master Data - Product screen displays.Your data is saved. |  |

Procedure: Option 2 - Manage Product Master Data

Follow this procedure when your user access presents you with the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Manage Product Master Data (F1602). | The app opens. |  |
| 2 | Search and Open the Product for Edit | Search the previously created Product by entering the Product Number in the Product search field.Select the Product from the list which navigates you to the Product screen.Choose Edit. | The Product displays in edit mode (fields are ready for your input). |  |
| 3 | Choose Plants | On the Manage Product Master screen, choose PLANTS.Note A Plant data record must have already been created. If you do not have an existing plant record, follow the steps in the previous section, [Create Material Master Data - MRP/Planning Data (Plant Data)](#unique_13) [page ] 12. | The PLANTS screen displays. |  |
| 4 | Choose Plant Details | On the Product Master - PLANTS screen, choose the arrow icon for the Plant data you have created in the previous section, [Create Material Master Data - MRP/Planning Data (Plant Data)](#unique_13) [page ] 12. | The Product Master Plant screen displays. |  |
| 5 | Navigate to Plant: Storage Location | On the Manage Product Master - PLANTS screen, go to PLANTS > STORAGE LOCATION . | The Product Master - PLANTS screen displays in edit mode. |  |
| 6 | Choose Create | Go to PLANTS > STORAGE LOCATION > Storage Location , and choose Create. | The Plant - Storage Location screen displays in edit mode. |  |
| 7 | Enter Plant: Storage Location Data | On the Storage Location screen, make the following entry:Storage Location: <Storage location number> | The New Record - Storage Location screen displays. |  |
| 8 | Return to the Main Screen | Choose Apply twice to return to the Product screen. | The Manage Product Master screen displays. |  |
| 9 | Save Your Data | Choose Save. | The system message indicates that the object is saved. |  |

### Create Material Master Data - Accounting Data (Valuation Area Data)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions on how to create Material master data. Apps available to you are dependent upon your assigned role, so two options are provided.

Prerequisite

You have filled out the data for the Material as described in the previous section, [Create Material Master Data - Basic Data](#unique_11) [page ] 7 and have completed and saved the Storage Location data.

Procedure: Option 1 - Create Material

Follow this procedure when your user access presents you with the Create Material (MM01) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Create Material (MM01). | The app opens. |  |
| 2 | Enter Material Basic Data | On the Create Material (Initial Screen) screen, make the following entries:Material: <Material number>Industry Sector: MNote If the Industry Sector input field is hidden, no entry is required. When the Industry Sector is not offered for entry, the field is grayed out.Material type: ROH (Raw materials)Choose Select View(s). | The Select View(s) screen displays. |  |
| 3 | Select Views | On the Select View(s) screen, select the following views and choose Continue:Accounting 1Accounting 2 | The Organizational Levels screen displays. |  |
| 4 | Enter Organizational Levels Data | On the Organizational Levels screen, in the Organizational level section, make the following entry:Plant: <Plant> | The Create Material (Raw materials) screen displays.The system message displays that The material already exists and will be extended. |  |
| 5 | Enter Accounting Data | On the Create Material (Raw materials) screen, on the Accounting 1 tab, in the General Valuation Data section, make the following entry:Valuation Class: 3000 |  |  |
| 6 | Enter Accounting Data | In the Prices and values section, make the following entries:Per. Unit price: For example, 20.Price Control: <V> | The Accounting 2 tab displays. |  |
| 7 | Confirm Entries | On the Accounting 2 tab, you do not have to make any entries. | The Last data screen reached screen displays with the message You are about to exit. Do you want to save your data for this material first?. |  |
| 8 | Save Your Data | On the Last data screen reached screen, choose Yes. | The Master Data - Product screen displays.Your data is saved. |  |

Procedure: Option 2 - Manage Product Master Data

Follow this procedure when your user access presents you with the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Manage Product Master Data (F1602). | The app opens. |  |
| 2 | Search and Open the Product for Edit | Search the previously created Product by entering the Product Number in the Product search field.Select the Product from the list which navigates you to the Product screen.Choose Edit. | The Product displays in edit mode (fields are ready for your input). |  |
| 3 | Choose Valuation Areas | On the Manage Product Master screen, choose VALUATION AREAS. | The VALUATION AREAS screen displays. |  |
| 4 | Choose Create | On the VALUATION AREAS screen, choose Create. | The New Record - Valuation Area screen displays in edit mode. |  |
| 5 | Enter Valuation Area Data | On the VALUATION AREAS screen, make the following entries:Valuation Area: <Valuation area number>Price Control Determination:: 2Note For Brazil only: Price Control Determination is 2 if Price Control is V, and it is 3 if Price Control is S, when addressing Brazilian Cost Accounting principles.Valuation Class: <Valuation class number> |  |  |
| 6 | Enter Current Valuation Area Data | On the Valuation screen, go to Valuation > Current Period , and make the following entries:Standard Price: For example, 20.Price Control: For example, S. |  |  |
| 7 | Return to the Main Screen | Choose Apply to return to the Manage Product Master screen. | The Manage Product Master screen displays. |  |
| 8 | Save Your Data | Choose Save. | The system message indicates that the object is saved. |  |

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

You must complete the previous chapter, [Create Material Master Data - Basic Data](#unique_11) [page ] 7, before you proceed with this chapter.

Follow the procedure after you have saved the Basic Data entries, as described in the previous chapter.

Procedure: Option 1 - Create Material

Follow this procedure when your user access presents you with the Create Material (MM01) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using your user credentials. | The SAP Fiori launchpad displays.Note Logging on via the launchpad is only relevant in case of Web GUI use. |  |
| 2 | Access the SAP Fiori App | Open Create Material (MM01). | The app opens. |  |
| 3 | Enter Material Basic Data | On the Create Material (Initial Screen) screen, make the following entries:Material: <Material number>Industry Sector: MNote If the Industry Sector input field is hidden, no entry is required. When the Industry Sector is not offered for entry, the field is grayed out.Material type: ROH (Raw materials)Choose Select View(s). | The Select View(s) screen displays. |  |
| 4 | Select Views | Note If the Class Type dialog box displays when you perform Step 3, you need to follow Step 7, 8, 9, and 10 first before Step 4, and then open the Material again in the Change Material (MM02) app to execute Step 5 and Step 6.On the Select View(s) screen, select the following views and choose Continue:Basic data 1Basic data 2Classification |  |  |
| 5 | Enter Basic Data | On the Material (Raw materials) screen, on the Basic data 1 tab, make the following entries:Material Description (short text): <Material description>Base Unit of Measure: <Base Unit of Measure>Press Enter. | The Basic data 2 tab displays. |  |
| 6 | Enter Basic Data | On the Basic data 2 tab, check the Configurable Material checkbox.Press Enter. | The Classification tab displays and the Class Type dialog box displays. |  |
| 7 | Choose Class Type | In the Class Type dialog box, select Class Type 300 (Variant) and choose Continue. | The Classification screen displays. |  |
| 8 | Assign Class | In the Assignment section, assign a Class and press Enter. | The corresponding Characteristics display below the Assignment section. |  |
| 9 | Choose Characteristics Values | Choose the required values of the Characteristics. |  |  |
| 10 | Save Data | Choose Save. | The Configurable Material is created. |  |
| 11 | Navigate to CU41 Transaction | Navigate to CU41 transaction and make the following entries:Profile Name: <Profile name>Class Type: 300 |  |  |
| 12 | Save Data | Choose Save. | The Configuration Profile is created. |  |
| 13 | Navigate to CU42 Transaction | Navigate to CU42 transaction.Double click Prof.Name > Config initial screen > Processing Mode: Advanced Variant Configuration .Choose Save. | The Profile is created. |  |
| 14 | Create Variant | To create a Variant, open the Create Material (MM01) tile again and follow the above steps to create a new Material with Basic data 1 and Basic data 2. |  |  |
| 15 | Create Variant | In Basic data 2, go to Client-specific configuration and enter the previously created Configurable Material in the Cross-plant CM. Choose Configure variant and then choose the required Characteristics value(s) to configure Variants. | The Variant is created. |  |

Procedure: Option 2 - Manage Product Master Data

Follow this procedure when your user access presents you with the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using your user credentials. | The SAP Fiori launchpad displays.Note Logging on via the launchpad is only relevant in case of Web GUI use. |  |
| 2 | Access the SAP Fiori App | Open Manage Product Master Data (F1602). | The app opens. |  |
| 3 | Search and Open Product for Edit | Search the previously created Product by entering the Product Number in the Product search field.Select the Product from the list which navigates you to the Product screen.Choose Edit. | Product displays in edit mode (fields are ready for your input). |  |
| 4 | Make Product Configurable | On the Product screen, go to the Configuration tab and check the Product is Configurable checkbox. |  |  |
| 5 | Assign Variant Class | On the Product screen, go to the Classification tab and choose Click here to assign a class.Select a class of type 300 (Variant). | The Characteristics of the assigned class display. |  |
| 6 | Choose Characteristics | Choose the required Characteristic values for each of the Characteristics. |  |  |
| 7 | Go to Variants Tab | On the Product screen, go to the Variants tab and choose Select Product Variants. | A tree/table displays with the different Characteristics. |  |
| 8 | Select Characteristics and Create Variants | Choose the combination of Characteristic values and choose Apply. | The Variants are created. |  |
| 9 | Save | Choose Save. | The system displays a notification indicating that the object is saved. |  |

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

You must complete the previous section, [Create Material Master Data - Basic Data](#unique_11) [page ] 7, before you proceed with this procedure.

Begin the procedure after you have saved the Basic Data entries, as described in the previous section.

Procedure: Option 1 - Create Material

Follow this procedure when your user access presents you with the Create Material (MM01) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Create Material (MM01). | The app opens. |  |
| 2 | Enter Material Basic Data | On the Create Material (Initial Screen) screen, make the following entries:Material: <Material number>Industry Sector: MNote If the Industry Sector input field is hidden, no entry is required. When the Industry Sector is not offered for entry, the field is grayed out.Material type: ROH (Raw materials)Choose Select View(s). | The Select View(s) screen displays. |  |
| 3 | Select Views | On the Select View(s) screen, select Basic data 1 and Basic data 2.Choose Continue. | The Create Material (Raw materials) screen displays. |  |
| 4 | Choose Services for Object | Go to Services for Object > Create Attachment . | The Import file screen displays. |  |
| 5 | Choose Upload | On the Import file screen, choose Upload. | A file upload screen displays. |  |
| 6 | Upload Attachment | Select the file and choose Open. | The file is uploaded. |  |
| 7 | Save | Select Choose and then Save. | The system message indicates that the object is saved. |  |

Procedure: Option 2 - Manage Product Master Data

Follow this procedure when your user access presents you with the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Manage Product Master Data (F1602). | The app opens. |  |
| 2 | Search and Open the Product for Edit | Search the previously created Product by entering the Product Number in the Product search field.Select the Product from the list which navigates you to the Product screen.Choose Edit. | The Product displays in edit mode (fields are ready for your input). |  |
| 3 | Choose Attachments | On the Product screen, go to the Attachments tab. | The Attachments screen displays. |  |
| 4 | Choose Upload | Under the Document Management System section, choose Upload. | A file upload screen displays. |  |
| 5 | Upload Attachment | Select the file and choose Open. | The file is uploaded. |  |
| 6 | Save | Choose Save. | The system message indicates that the object is saved. |  |

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

You must complete the previous section, [Create Material Master Data - Basic Data](#unique_11) [page ] 7, before you proceed with this procedure.

Begin the procedure after you have saved the Basic Data entries, as described in the previous section.

Procedure: Option 1 - Create Material

Follow this procedure when your user access presents you with the Create Material (MM01) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Create Material (MM01). | The app opens. |  |
| 2 | Enter Material Basic Data | On the Create Material (Initial Screen) screen, make the following entries:Material: <Material number>Industry Sector: MNote If the Industry Sector input field is hidden, no entry is required. When the Industry Sector is not offered for entry, the field is grayed out.Material type: ROH (Raw materials)Choose Select View(s). | The Select View(s) screen displays. |  |
| 3 | Select Views | On the Select View(s) screen, select Basic Data 1 and Sales: General/Plant Data.Choose Continue. | The Organizational Levels screen displays. |  |
| 4 | Enter Organizational Levels Data | On the Organizational Levels screen, in the Organizational level section, make the following entries:Plant: <Plant number>Sales Org: <Sales Org number>Distr. Channel: <Distribution Channel> | The Create Material… (Raw materials) screen displays. |  |
| 5 | Enter Data on the Basic Data 1 Screen | On the Basic Data 1 screen, make the following entries and press Enter:Description: Enter a description for the Product.Base Unit: Maintain Base Unit EA, for example, 1. |  |  |
| 6 | Enter Data on the Sales: General/Plant Data Screen | In the Shipping data (times in days) section, make the following entry:LoadingGrp: <Choose value from the value help> |  |  |
| 8 | Save Your Data | Choose Save. | Your data is saved. |  |

Procedure: Option 2 - Manage Product Master Data

Follow this procedure when your user access presents you with the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Manage Product Master Data (F1602). | The app opens. |  |
| 2 | Search and Open the Product for Edit | Search the previously created Product by entering the Product Number in the Product search field.Select the Product from the list which navigates you to the Product screen.Choose Edit. | The Product displays in edit mode (fields are ready for your input). |  |
| 3 | Choose Plants Data | On the Product screen, choose Plants. | The Plants tab displays. |  |
| 4 | Choose Create | On the Plants screen, choose Create. |  |  |
| 5 | Enter Plants - General Data | In the General Data section, make the following entry:Plant: <Plant number>, for example, 1710 |  |  |
| 6 | Enter MRP Data | In the MRP section, make the following entry:MRP Type: For example, ND. |  |  |
| 7 | Enter Plant- Sales | In the Sales section, make the following entry:Loading Group: <Choose value from the value help> |  |  |
| 8 | Return to the Main Screen | Choose Apply to return to the Product screen. | The Product screen displays. |  |
| 9 | Save Your Data | Choose Save. | The system message indicates that the object is saved. |  |

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

You must complete the previous section, [Create Material Master Data - Basic Data](#unique_11) [page ] 7, before you proceed with this procedure.

Begin the procedure after you have saved the Basic Data entries, as described in the previous section.

Procedure: Option 1 - Create Material

Follow this procedure when your user access presents you with the Create Material (MM01) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Create Material (MM01). | The app opens. |  |
| 2 | Enter Material Basic Data | On the Create Material (Initial Screen) screen, make the following entries:Material: <Material number>Industry Sector: MNote If the Industry Sector input field is hidden, no entry is required. When the Industry Sector is not offered for entry, the field is grayed out.Material type: ROH (Raw materials)Choose Select View(s). | The Select View(s) screen displays. |  |
| 3 | Select Views | On the Select View(s) screen, select Basic Data 1, MRP 1, and MRP 4.Choose Continue. | The Organizational Levels screen displays. |  |
| 4 | Enter Organizational Levels Data | On the Organizational Levels screen, in the Organizational level section, make the following entries:Plant: <Plant number>Storage Location: <Storage location number> | The Create Material… (Raw materials) screen displays. |  |
| 5 | Enter Data on the Basic Data 1 Screen | On the Basic Data 1 screen, make the following entries and press Enter:Description: Enter a description for the Product.Base Unit: Maintain Base Unit EA, for example, 1. |  |  |
| 6 | Enter Data on the MRP 1 Screen | In the MRP procedure section, make the following entry:MRP Type: For example, ND. |  |  |
| 7 | Enter Data on the MRP 4 Screen | In the Repetitive manufacturing/ assembly / deployment strategy section, make the following entry:Rpet. Manufacturing: Select the checkbox.REM Profile: <Choose value from the value help> |  |  |
| 8 | Save Your Data | Choose Save. | Your data is saved. |  |

Procedure: Option 2 - Manage Product Master Data

Follow this procedure when your user access presents you with the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Manage Product Master Data (F1602). | The app opens. |  |
| 2 | Search and Open the Product for Edit | Search the previously created Product by entering the Product Number in the Product search field.Select the Product from the list which navigates you to the Product screen.Choose Edit. | The Product displays in edit mode (fields are ready for your input). |  |
| 3 | Choose Plants Data | On the Product screen, choose Plants. | The Plants tab displays. |  |
| 4 | Choose Add (+) | On the Plants screen, choose Add (+). |  |  |
| 5 | Enter Plants - General Data | In the General Data section, make the following entry:Plant: <Plant number>, for example, 1710 |  |  |
| 6 | Enter MRP Data | In the MRP section, make the following entry:MRP Type: For example, ND. |  |  |
| 7 | Enter Repetitive Manufacturing Data | In the Repetitive Manufacturing section, make the following entries:Repetitive Manufacturing Enabled: Select the checkbox to enable the Repetitive Manufacturing Profile field.Repetitive Manufacturing Profile: <Choose value from the value help>Note After checking the Repetitive Manufacturing Enabled checkbox, the Repetitive Manufacturing Profile field should be editable.After unchecking the Repetitive Manufacturing Enabled checkbox, the Repetitive Manufacturing Profile field should be read-only. |  |  |
| 8 | Return to the Main Screen | Choose Apply to return to the Product screen. | The Product screen displays. |  |
| 9 | Save Your Data | Choose Save. | The system message indicates that the object is saved. |  |

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
> Flagged while digesting this document, not verified: Mandatory/optional master data table is empty (placeholder rows only); Plant Sales section step numbering skips step 7; Create Material app step is hidden in some roles (Industry Sector field may be hidden)

## Connections
- part-of :: [[_cluster]]
- related-to :: [[02-business-partner-and-product-master-data/sap-s-4hana-cloud-public-edition-mds-bnr-661]]
- related-to :: [[02-business-partner-and-product-master-data/sap-s-4hana-cloud-public-edition-mds-bnr-663]]
- related-to :: [[02-business-partner-and-product-master-data/script-de-dados-mestre-criar-mestre-de-produtos-do-tipo-materia-prima]]
- related-to :: [[02-business-partner-and-product-master-data/script-de-datos-maestros-creacion-de-maestro-de-productos-de-tipo-mate-2]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNR_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 54,890 chars in the whole document
