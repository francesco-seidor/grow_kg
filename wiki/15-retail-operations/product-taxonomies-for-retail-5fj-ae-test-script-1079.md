---
id: 15-retail-operations/product-taxonomies-for-retail-5fj-ae-test-script-1079
title: Product Taxonomies for Retail (5FJ_AE) - Test Script (5FJ_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition test script (AE, 19-06-26) for scope item 5FJ: merchandise categories, hierarchies, reclassification, with article, assortment, PO and allocation prerequisites."
cluster: 15-retail-operations
tags: [kb/retail-operations, topic/retail-articles-and-merchandise-categories]
aliases: [5FJ_S4CLD2608_BPD_EN_AE]
keywords: ["Retail Articles, Merchandise Categories and Seasons", merchandise categories, merchandise category hierarchy, article reclassification, reclassification versions, single article creation, generic articles variants, characteristics, assortment modules, purchasing info records]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5FJ_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1079
topic: 15-retail-operations/retail-articles-and-merchandise-categories
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Product Taxonomies for Retail (5FJ_AE) - Test Script (5FJ_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5FJ_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Retail Articles, Merchandise Categories and Seasons** in Retail Operations. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Product Taxonomies for Retail (5FJ_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232856446)

[2 Prerequisites 4](#_Toc232856447)

[2.1 System Access 4](#_Toc232856448)

[2.2 Roles 4](#_Toc232856449)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232856450)

[2.4 Preliminary Steps 6](#_Toc232856451)

[2.4.1 Create Characteristics (Optional) 7](#_Toc232856452)

[2.4.2 Create Characteristic Values (Optional) 8](#_Toc232856453)

[2.4.3 Create Configuration Class for Variants (Optional) 9](#_Toc232856454)

[2.4.4 Create Merchandise Category Hierarchy Level 10](#_Toc232856455)

[2.4.5 Create Article Master Data via App 11](#_Toc232856456)

[2.4.5.1 Create Single Article 11](#_Toc232856457)

[2.4.5.2 Create Generic Article with Variants 24](#_Toc232856458)

[2.4.6 Create Assortments 38](#_Toc232856459)

[2.4.6.1 Create Assortment Module 38](#_Toc232856460)

[2.4.6.2 Create Assortment Module Version 39](#_Toc232856461)

[2.4.6.3 Assign Product to Assortment Module Version 40](#_Toc232856462)

[2.4.6.4 Assign Store to Assortment Module 42](#_Toc232856463)

[2.4.6.5 Assign Products to Distribution Center 43](#_Toc232856464)

[2.4.7 Create Purchasing Info Record 44](#_Toc232856465)

[2.4.8 Create Purchase Order 46](#_Toc232856466)

[2.4.8.1 Create Purchase Order Directly 46](#_Toc232856467)

[2.4.9 Create Allocation Table 48](#_Toc232856468)

[2.4.9.1 Create Allocation Table Manually 48](#_Toc232856469)

[3 Overview Table 50](#_Toc232856470)

[4 Test Procedures 52](#_Toc232856471)

[4.1 Create Merchandise Category 52](#_Toc232856472)

[4.2 Maintain Merchandise Category 56](#_Toc232856473)

[4.3 Display Merchandise Category 57](#_Toc232856474)

[4.4 Change Merchandise Category Hierarchy Level 58](#_Toc232856475)

[4.5 Assign Merchandise Category Hierarchy Level (Optional) 59](#_Toc232856476)

[4.6 Display Merchandise Category Hierarchy Level 60](#_Toc232856477)

[4.7 Display Merchandise Category Hierarchy 61](#_Toc232856478)

[4.8 Delete Merchandise Category Hierarchy Level (Optional) 61](#_Toc232856479)

[4.9 Reclassification of Retail Material (Optional) 62](#_Toc232856480)

[4.10 Create Reclassification Version for Merchandise Category or Merchandise Category Hierarchy Node 64](#_Toc232856481)

[4.11 Update Reclassification Version for Merchandise Category or Merchandise Category Hierarchy Node 65](#_Toc232856482)

[4.12 Maintain Reclassification Version for Merchandise Category or Merchandise Category Hierarchy Node 66](#_Toc232856483)

[4.13 Display Reclassification Version for Merchandise Category or Merchandise Category Hierarchy Node 67](#_Toc232856484)

[4.14 Delete Reclassification Version for Merchandise Category or Merchandise Category Hierarchy Node 68](#_Toc232856485)

## Purpose

Overview

A merchandise category comprises articles that are similar from a process perspective. Those merchandise categories can then be organized in merchandise category hierarchies to ease the classification of the article master. The huge number of different articles causes several challenges for efficient process execution. To meet these requirements, you can select all articles of one or more merchandise categories for process steps, and furthermore specify controlling parameters at the merchandise category or merchandise hierarchy level (for example, sales price strategies or default distribution centers). This higher data retention level above the article enables a more efficient management of all items that a company procures or produces, stores, and sells. Furthermore, reporting at the article cluster level is typically more tangible and easier to comprehend, including reports on procurement, inventory management and master data.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

|  |
| --- |
| Note In the retail industry, specific terms differ from the standard terms used in other lines of business. Therefore, SAP solutions which provide business processes across multiple lines of businesses may use terms for the corresponding business objects, transactions, and user interfaces that deviate from the retail terminology. For integration and reuse reasons, the SAP S/4HANA Cloud Public Edition, retail, fashion, and vertical business business may thus include different terms that refer to the same concept. SAP intends to harmonize the terminology in the future.The following terms are used synonymously in this document:Table 1:Standard Terms in Lines of BusinessSAP S/4HANA Cloud Public Edition, retail, fashion, and vertical business businessMaterial, productArticleMaterial group, product groupMerchandise categoryPlant, locationSite (as superordinate term) - store and distribution center (DC) |

## Prerequisites

This chapter summarizes all prerequisites needed to conduct the test in terms of system, user, master data, organizational data, other test data, and business conditions.

### System Access

|  |  |
| --- | --- |
|  | Details |
| System | Accessible through SAP Fiori Launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) |
| --- | --- | --- | --- |
| Master Data Specialist - Product Data (Retail) | SAP_BR_MD_SPCLST_ITEM_RFM | Retail Product Master Data | SAP_BR_MD_SPCLST_ITEM_RFM |
| Purchaser (Retail) | SAP_BR_PURCHASER_RFM | Retail Purchasing / Retail Sourcing and Contracting | SAP_RFM_SPT_PURCHASING_PC / SAP_RFM_SPT_SOURCING_PC |
| Allocator (Retail) | SAP_BR_ALLOCATOR_RETAIL | Allocation and Merchandise Distribution | SAP_BR_ALLOCATOR_RETAIL |
| Assortment Specialist - Retail | SAP_BR_ASSTMT_SPCLST_RFM | Assortments | SAP_RFM_SPT_ASSTMT_PC |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Article | R_REF01 | Ref article trading goods half tax | You can create only one merchandise category reference article for each merchandise category. However, you can use the same merchandise category reference article for more than one merchandise category.Merchandise category reference article helps to maintain the article master data more easily. When you create an article master record, you must assign it to a merchandise category. If a merchandise category reference article exists for the merchandise category that you have specified, the data for the merchandise category reference article is proposed in the new article master record. |
| Configuration Class | R_FLAVOR | Mandatory | You can use the configuration class to create variants for a generic article. The characteristics that are relevant for the variants of a generic article are assigned to this class. |
| Company Code | 3310 | Company Code 3310 |  |
| Sales Organization | 3310 | Dom. Sales Org |  |
| Purchasing Organization | 3310 | Purchase Organization 3310 |  |
| Distribution Channel | 10 | Direct Sales |  |
| Distribution Channel | 40 | Store Sales |  |
| Distribution Channel | 50 | Distribution |  |
| Distribution Center | 3350 | DC 3350 AE |  |
| MRP Controller | 001 | MRP Controller 001 |  |
| Purchasing Group | 002 | Group 002 |  |
| Storage Location | 994A | St.Loc.Neg.Stock |  |
| Storage Location | 995A | Storage Loc. DC |  |
| Plant Group | R_SITEGROUP_AE_01 | R_SITEGROUP_AE_01 | 3340/3341/3342/3343 and 3344 are the sites part of the plant group R_SITEGROUP_AE_01. Refer 3I3 - Sites for Retail Scope Item for more details. |
| Plant | 3340 | Store 3340 AE |  |
| Supplier | 33213001/33213002 | Retail Non-Food Supplier AE/Retail Food Supplier AE |  |
| Material Group | R1193001/R1182001 | Frozen Fruit/Yoghurt |  |

### Preliminary Steps

The best practice content for the SAP S/4HANA Cloud Public Edition, retail, fashion, and vertical business solution system is already the merchandise categories and merchandise category hierarchy created however you can create your merchandise category hierarchy with several merchandise category hierarchy levels and merchandise categories. You can also create your characteristics and characteristic values by following the steps mentioned in this chapter.

|  |
| --- |
| Note To check the [Reclassification of Retail Material (Optional)](#unique_7) [page ] 62 test procedure, a new set of articles must be created and listed.With this article master, an allocation table and a Purchase Order are created to see if the retail and article reclassification is successful for open Purchase Orders and Allocation table. |

#### Create Characteristics (Optional)

Use

This process step shows you how you can define characteristics separately before assigning them to the merchandise category or the configuration class for variant.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1. | Log on | Log onto the SAP Fiori Launchpad as Master Data Specialist - Product Data (Retail) |  |  |
| 2. | Access the app | Open Manage Characteristics (CT04) app. | The Manage Characteristics (CT04) initial screen is displayed. |  |
| 3. | Provide input values | On the initial screen, make the following entries and select Create :Characteristic: <XXXXXXX>Note Enter the unique characteristic name that needs to be created. | The Create Characteristic screen is displayed. |  |
| 4. | Fill the required field values | Maintain the following Basic Data details for the characteristic:Description: Test Size CharacteristicStatus: 1 ReleasedData type: CHAR Character FormatNumber of chars: 3 |  |  |
| 5. | Add function | Maintain the following values for the characteristic in Values tabUse Other Value Check button Function module and select CopyFunction: WRF_CHECK_CHAR_VAL | A popup window Value Check Strategy is displayed. |  |
| 6. | Save your entries | Confirm your entries and select ENTERSelect Save.Make a note of the characteristic you have created. | A Characteristic is created and a message is displayed. |  |

Result

Characteristic is created.

#### Create Characteristic Values (Optional)

Use

This process step shows you how you define characteristic values for a characteristic. This method of managing characteristic values is particularly useful for characteristics with numerous characteristic values.

In SAP S/4HANA Cloud Public Edition solution for retail, fashion, and vertical business, we support four characteristic types that are Characteristic 1, Characteristic 2, Characteristic 3, and Not typed (for characteristic types other than color and size). There is a control (Check Option) that checks the system response when you try to assign a characteristic value to an article or delete a characteristic value.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad asMaster Data Specialist - Product Data (Retail) |  |  |
| 2 | Access the app | Open Maintain Characteristic Values (WRFCHVAL) app. | The Edit Characteristic Values Initial screen is displayed. |  |
| 3 | Provide input values | On the initial screen, make the following entries and selectENTER:Characteristic: <XXXXXXXX> (Enter the characteristic created in Chapter [Create Characteristics (Optional)](#unique_8) [page ] 7)Char. Type: 1 characteristic 2Check Option: E Check Characteristic Values in Material Maint. w/Error | A popup window Edit Characteristic Value is displayed. |  |
| 4 | Select continue | Select Continue in pop up window. |  |  |
| 5 | Maintain value table | In Value table, make the following entries and select ENTER:Char. Value: S, M, LDescription: Small, Medium, Large |  |  |
| 6 | Save your entries | Select Save. | A Characteristic values are created and a message is displayed. |  |

Result

Characteristic values are updated.

#### Create Configuration Class for Variants (Optional)

Use

This process step shows you how to create the configuration class for variants. You can use the configuration class to create variants for a generic article. The characteristics that are relevant for the variants of a generic article are assigned to this class.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1. | Log on | Log onto the SAP Fiori launchpad as Master Data Specialist - Product Data (Retail) |  |  |
| 2. | Access the app | Open Manage Classes (CL02) app. | The Manage Classes (CL02)Initial screen is displayed. |  |
| 3. | Provide input values | On the initial screen, make the following entries and select Create :Class: <XXXXXXXX>Note Enter the unique class name that needs to be created.Class Type: 300(Variants) |  |  |
| 4. | Fill the required field values | Maintain the following Basic Data details for the class:Description: <XXXXXXXX>Status: 1 Released |  |  |
| 5. | Add function | Maintain the following in Char. tabChar . : <XXXXXXXX> (Enter the characteristic created in chapter [Create Characteristics (Optional)](#unique_8) [page ] 7) |  |  |
| 6. | Save your entries | Confirm your entries and select ENTERSelect Save. | A pop-up message is displayed. |  |

Result

Configuration class is created.

#### Create Merchandise Category Hierarchy Level

Use

Merchandise category hierarchy level in SAP S/4HANA Cloud Public Edition solution system helps to define the hierarchical representation of an article. In this step, you can create a merchandise category hierarchy level which will be assigned to the higher merchandise category hierarchy level to form the hierarchy. A successfully implemented merchandise category hierarchy is an essential tool for efficient merchandise category management. The focus for the management of the merchandise then shifts from individual articles to merchandise groupings. The aim of merchandise category management is better coordination of various customer considerations at each business location (for example, store), including elements such as variety, price structures, and advertising.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as Master Data Specialist - Product Data (Retail) |  |  |
| 2 | Access the app | Open Create Hierarchy Level - Merchand. Cat. Hier. (CLWM) app. | The Create Hierarchy Level - Merchand. Cat. Hier. (CLWM)Initial screen is displayed. |  |
| 3 | Provide input values | On the initial screen, make the following entries and select ENTER:Hierarchy Level: <XXXXXXXXX>Note Enter the hierarchy name that needs to be created | The Create Hierarchy Level: screen is displayed. |  |
| 4 | Fill all mandatory fields | In Basic Data tab, make the following entry and select ENTER:Description: Test Hierarchy |  |  |
| 5 | To maintain a description in an additional language | Select Change language.In the dialog box, enter language, for example, EN and select ENTER:On the Basic Data tab, enter description for second language |  |  |
| 6 | Save your entries | Select Save. | A pop-up message is displayed. |  |

Result

Merchandise category Hierarchy level is created.

#### Create Article Master Data via App

##### Create Single Article

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The single article is the standard product that is sold to the customer also known as material.

This article cannot be changed into a generic article and a generic article cannot be changed into a single article.

The following procedure provides instructions for creating single article master data. The SAP Fiori apps available to you are dependent on your assigned role. There are two options to create single article - using create article application and using Manage product master data app.

|  |
| --- |
| Note It is recommended to use the procedure using Manage Product Master Data (F1602) app.Please note that most of the attributes/fields of article gets referenced from the reference article which is assigned to product group. User needs to input data for only for few fields in below procedures. |

Procedure: Option 1 - Manage Product Master Data

In this procedure you can create product master data using the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data (Retail). |  |  |
| 2 | Access the SAP Fiori App | Open Manage Product Master Data (F1602) app. | The Manage Product Master Data (F1602) screen is displayed. |  |
| 3 | Choose Create New Product Master | In the Manage Product Master Data (F1602) view, select Create button and select Single Article from the list.Note Do not choose Create Product option but chose the appropriate article category for creating product for retail. | The Create Master Data Record screen is displayed. |  |
| 4 | Enter Data for Mandatory Fields | In the Master Data Record sub-screen make the following entries:Product Number: for example, R_<XXXXX>You either enter any external alphanumeric ID, and that ID must start with an alphanumeric character, or if you provide no entry, the system automatically assigns a numeric ID.Product Type: Trading Goods(HAWA)Product Group: for example, Frozen Fruits (R1193001)Note On entering product group the reference product field is auto populated from the reference article maintained for the Product group.Base Unit: for example, PCValuation Class: 3100/Trading GoodsTax Classification: 1/(Full Tax)Loading Group: 0001(Crane)Description: <any description> |  |  |
| 5 | Choose OK | In the Manage Product Master view, select OK. | The Manage Product Master view is displayed. |  |
| 6 | In General Information | In the Manage Product Master > General Information, press Show more and enter the following details in the Content/Design section.Net Contents <value>(KG)Gross Contents <value>(KG)Comparison Price Unit (1)(KG) |  |  |
| 7 | In General Information Descriptions | In the Manage Product Master > General Information > Descriptions view, choose Create. | Description in default language (for example, English) is already populated. |  |
| 8 | Enter Descriptions Data | In the Descriptions view, make the following entries:Language: for example, ArabicProduct Description: <your description> |  |  |
| 9 | In General Information | In the Manage Product Master > General Information > Base Unit of Measure view (Show more), make the following entry:GTINGTIN Category: IEWeightsGross Weight: for example, 2Net Weight: for example, 1.8Weight Unit: for example, KG |  |  |
| 10 | Enter Unit of Measure | In the Manage Product Master > General Information > Unit of Measure view and navigate to the details. |  |  |
| 11 | Enter Receipt Texts | In the Receipt Texts section under Unit of Measure Texts. Select CreateEnter Language and Text.This text is relevant for the POS communication. |  |  |
| 12 | Press Apply button | Press Apply button to navigate back to main screen. |  |  |
| 13 | Add an alternate Unit of Measure | In the Manage Product Master > General Information > Unit of Measure view, and choose Create . | New Record – Unit of Measure screen opens. |  |
| 14 | Enter Unit of Measure | In the General Information section, enter Unit of measure as CRT. |  |  |
| 15 | Enter Conversion factor | In the Conversion Factor section:Enter Units/Quantity – Alternate Unit of Measure <value>, for example, 1Enter Units/Quantity – Base Unit of Measure <value>, for example,10 |  |  |
| 16 | Enter Weight Data | In the Weight section, enter the following:Gross Weight: for example, 20Net Weight: Ideally this should get auto-filled by defaultWeight Unit: for example, KG |  |  |
| 17 | Enter GTIN for the alternate UOM | In the GTINs section GTINs -unit of Measure press create button and assign GTIN category IE and press Enter. |  |  |
| 18 | Press Apply buton | Press Apply button to navigate back to main screen. | The Product Master screen is displayed. |  |
| 19 | Enter Delivery Unit of measure | In the Manage Product Master > General Information > Reference Values maintain Delivery Unit of Measure (CRT). |  |  |
| 20 | Choose Distributions Chains | In the Product screen, choose Distribution Chains tab. | The Distribution Chains tab is displayed. |  |
| 21 | Choose Create | In the Distribution Chains tab, choose Create. | Distribution Chains is displayed in edit mode. |  |
| 22 | Enter Distribution Chains Data | In Distribution Chains, make the following entries:In the GENERAL DATA - General Information sectionSales Organization: <Sales org number> 3310/Dom. Sales OrgNote The organization unit value is determined by what is offered in the value help.Distribution Channel: for example 40/Store SalesCash Discount: XIn the GROUPING TERMS section:Item Category Group: for example, NORM |  |  |
| 23 | Return to Main View | Choose Apply to return to Product screen. | The Product screen is displayed.Repeat step 18-19 to maintain the other distribution chains for example,3310/50 and 3310/10 . |  |
| 24 | Choose Purchasing Data | In the Product screen, choose Purchasing. | The Purchasing view is displayed. |  |
| 25 | Enter Purchasing Data | In the Purchasing section, enter Order Unit of Measure as CRT. |  |  |
| 26 | Choose Distribution Center Data | In the Product screen, choose Distribution centers. | The Distribution Center tab is displayed. |  |
| 27 | Create Distribution Center relevant data | In the Distribution centers view, choose Create. | The Distribution Center view is displayed. |  |
| 28 | Enter Distribution Center - General Information | In the General Information section, make the following entries if not maintained:General DataDistribution Center: DC for example, 3391 (Reference DC comes by default, no need to enter explicitly and remain Non Editable) | The DC 3391 represents the reference distribution center for logistic data maintenance. DC 3391 is not an operational DC. Data maintained at reference DC level are inherited to all operational DCs and only exceptions for individual DCs must be maintained explicitly. |  |
| 29 | Enter Distribution Center - Sales Data | In the Sales section, make the following entry:Loading Grp: for example, 0001(Crane) |  |  |
| 30 | Enter Distribution Center - Purchasing data | In the Purchasing section, make the following entries:Purchasing Group: 002/Group 002Tax Indicator: 2 – Material 50% exemptSupply Source: 1 (Standard)Automatic Purchase Order allowed : X |  |  |
| 31 | Enter Distribution Center - MRP Data | In the MRP Data > MRP Data section, make following entries:MRP Type: For example, R1 – Time Phased PlanningMRP Controller: For example, 001/MRP Controller 001Planning Cycle: P01(Order Day Monday)Availability Check: for example, ST (Consider only Stock)In the MRP Data > Lot-Size Data section, make the following entry:Lot Sizing Procedure: for example EX/ Lot-for-lot order quantityIn the MRP Data > Procurement section, make the following entry:Planned Delivery Time: for example, 3Goods Receipt Processing Time: for example, 1Default Storage Location for external procurement: 995A |  |  |
| 32 | Return to Main Screen | Choose Apply to return to Product screen. | The Product screen is displayed.. |  |
| 33 | Choose Stores Data | In the Product screen, choose Stores. | The Store tab is displayed.. |  |
| 34 | Create Stores | In the Stores view, choose Create. | The Store view is displayed. |  |
| 35 | Enter Stores - General Information | In the General Information section, make following entries if not maintained:General DataStore: Store for example, 3392 (Reference Store comes by default, no need to enter explicitly and remain Non Editable)Negative Stock Allowed in Plant: X | The store 3392 represents the reference store for logistic data maintenance. Store 3392 is not an operational store. Data maintained at reference store level are inherited to all operational stores and and only exceptions for individual stores must be maintained explicitely. |  |
| 36 | Enter Stores - Sales Data | In the Sales section make following entry:Loading Grp: for example, 0001(Crane) |  |  |
| 37 | Enter Stores – Purchasing Data | In Purchasing:Purchasing Group: 002/Group 002Tax Indicator: 2 Material 50% exemptSupply Source: 4 (Stock Transfer Before Standard)Automatic Purchase Order allowed : X |  |  |
| 38 | Enter Stores - MRP Data | In the MRP Data > MRP Data section, make following entries:MRP Type: For example, RF/Replenish with dyn.TargetStock.(Dynamic Target Stock gets calculated at runtime during the planning run from forecast sales value )Availability Check: for example, ST/ Consider only stockIn the MRP Data > Procurement section, make the following entry:Planned Delivery Time: for example, 3Goods Receipt Processing Time: for example, 1Default Storage Location for external procurement: 994A |  |  |
| 39 | Return to Main Screen | Choose Apply to return to Product screen. | The Product screen is displayed.. |  |
| 40 | Save Your Data | Choose Create. | As a next step, you need to:Maintain purchasing Info record. For more information, see chapter Maintain Purchasing Info Record in scope item Products for Retail (3I1).Maintain retail pricing . For more information, refer chapter Succeeding Processes in scope item Sales Pricing for Retail (3I4).You can change or maintain or update the article created above, using Maintain Article (MM42) app. |  |

Procedure: Option 2 - Create Single Article using Create Article Application

In the procedure you create article using Create Article (MM41) app.

There are different views to maintain an article:

Basic Data

Global article data are defined. These are not specific to a supplier, plant, or distribution chain, example:

- Possible units of measurements, weights and dimensions
- EAN code
- Description
- Product group assignment

Purchasing

Supplier or purchasing organization specific data are maintained for the article. This is for example a purchasing price and a confirmation control key or purchasing group. When maintaining the purchasing price a purchasing info record is generated. The data can be maintained for exceptions, even at plant level.

Sales

Distribution chain-specific data are maintained for the article. This is for example a sales price for a defined distribution chain and sales unit of measurement. The data can be maintained for exceptions, even at plant or price list level.

Logistic Distribution Center

Plant-specific article data for distribution centers are maintained. Below are the following options:

- Defining data for all distribution centers
    - The data is maintained for the reference distribution center and valid for all distribution centers.
- Defining data for one distribution center
    - Exceptions can be maintained individually for relevant distribution center.

Logistic relevant data like storage location and replenishment data are maintained at this level.

Logistic Store Data

Plant-specific article data for stores are maintained. There are the following options:

- Defining data for all stores or for all stores from one distribution chain
    - The data is maintained for the reference stores and valid for all relevant stores.
- Defining data for one store
    - Exceptions can be maintained individually for relevant stores.

Logistic relevant data like storage location and replenishment data are maintained at this level.

POS Data

Article data which are required for communicating with point-of-sale (POS) systems are maintained. The data always relates to a single distribution chain for the Article. The data can be maintained for exceptions even at Plant level. Data such as receipt text for each sales unit is maintained.

There is the possibility to use a dedicated article as reference for the creation and field values are proposed from the reference.

If there is no specific reference article specified – data from the merchandise category reference article are proposed.

The proposed field values can always be adjusted if necessary for the new article.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data (Retail) |  |  |
| 2 | Access the SAP Fiori App | Open Create Article (MM41) app. | The Create Article (MM41) (Initial Screen) is displayed. |  |
| 3 | Enter Article Basic Data | In the Create Article (MM41) (Initial screen):Material: Article number (R_<XXXXX>)Material type: Trading Goods/HAWA Trading GoodsMaterial Group: Frozen Fruit/R1193001)Material Category: Single material/00 Single materialSelect Enter. | If there is no particular reference article on the input screen, data from the merchandise category reference article is proposed on the various screens. It's possible to overwrite the data. |  |
| 4 | Choose Views | Select Basic data, Basic data 2, Sales, Logistics Dc, Logistics Store & POS views and choose continue. |  |  |
| 5 | Enter Basic Data | From Create Article ...(Basic Data), on the Basic data tab, enter a Article description (short text). | Create Article … (Basic Data) is displayed. |  |
| 6 | Enter Basic Data | In the Unit of measure/EANs/dimensions section, enter the following:Base Base Unit of Measure (PC)Alternate Unit of Measure (CAR)Number of Lower-level <value>Unit of Measure <value>Gross Weight (<value>)Unit of Weight (KG)Net Weight (<value>)EAN Category (IE - Instore EAN (int. assignment possible))Select Order Unit and Delivery Unit for the Alternate UOM that is, CAR in this case. | Subscreen: Units of Measure/EAN’s/Dimensions.Enter the measurements and dimensions of the Article.Note EAN category and weight These data you should not maintain at reference article.The system message “The EAN will be determined internally on the basis of the EAN category is displayed”. |  |
| 7 | Navigate to Go to Additional data in Basic Data View: | In Short Text View enter the description in second language:Language ENMaterial Description <Value>In the Unit of Measure View maintain/check the following (for Alternate UOM):Length <value>Width <value>Height <value>Unit Of Dimension (CM)Volume <value>Volume Unit (M3)Gross Weight <value>Unit of Weight (KG)EAN Category (IE)In the Additional EANs view maintain the additional EANs for the unit of measures (optional):EAN category (IE)Alt unitIn the Requirement Group view maintain the following (optional):Requirement Group (e.g. 02 -Large) Target Stock <value>Reorder point <value>Safety stock <value>Min. Target stock <value>Max. Target stock <value>Note When you are managing a large number of sites or a large number of articles, you can reduce the effort required to maintain the large amount of data by defining requirement groups. This will prevent you from maintaining all the data for every combination of site and article.This should be used with the MRP Type RP (RP - Replenish with static Target Stock) at Logistics Store tab in Step 15.Then select Go to Main Data | Basic Data screen is displayed.User can maintain multiple EANs for each unit of measure. |  |
| 8 | Enter further Basic Data | In Groupings section:Division 00In General Data:Tax Class (2 – Reduced tax)Valuation Class (3100- Trading goods)Country of Origin AEIn Internal logistics data:Supply Source (4 - Stock Transfer Before Standard)GenItemCatGroup (NORM)Loading Group (0001- Crane)Transportation Group (0001- On pallets )Variable Order Unit: 1/ActiveIn Content section:Net Contents <value>Gross Contents <value>Content Unit (KG)Comparison Price Unit (1)In Validity section (Optional):Valid from: <date>Valid to: <date>(default 31.12.9999, cannot be maintained)In Shelf Life Data section (Optional):Remaining Shelf LifeTotal Shelf LifePeriod indicatorStorage % | Shelf Life Data section: This section is only maintained if really applicable for the article.Note the date of production must be entered in the goods receipt. |  |
| 9 | Choose Views | Select Basic Data 2 View and choose continue/enter. | Create Article …(Basic data 2) view is displayed. |  |
| 10 | Enter Sales Period | In Sales period for Stores and Distribution CenterSales Period: storeFor sale fromFor sale tillSales Period: distribution centerFor sale fromFor sale till |  |  |
| 11 | Choose Views | Choose Purchasing tab. | Area of Validity pop up screen is displayed. |  |
| 12 | Enter Organizational Levels Data | In Switch Validity Area, in the Area of Validity section, enter data for the following:P urchasing Org . 3310/Purch. Org. 3310Supplier (33213002/Retail Food Supplier)Choose Continue. |  |  |
| 13 | Enter Purchasing Data | On the Create Article : Purchasing screen, make the following entries:(All the below data can be proposed from the business partner (supplier) (only except Net Price), but if you need to maintain any deviation then you can go ahead and maintain)Purchasing Group 002/Group 002Var. Order Unit (1/Active)Regular Supplier (X)Net Price (<value>) | As a next step, you need to maintain purchasing Info record. For more information, see chapter Maintain Purchasing Info Record in scope item 3I1Note Regular Supplier value is required only if the customer is operating in one country and has several suppliers for this article and one should be the preferred supplier. |  |
| 14 | Choose Views | Choose Sales tab. | Create Article …(Sales) view is displayed. |  |
| 15 | Enter Organizational Levels Data | In Switch Validity Area, in the Area of Validity section, enter values for the following:Sales Unit (PC)Sales Org. 3310/Dom. Sales OrgDistr. Channel (40/Store Sales)Select Continue. |  |  |
| 16 | Enter Sales Data | On the Create Article :Sales screen, make the following entries:(Few of the below ideally get filled automatically from the Reference Article for example item category group, cash discount,.):Sales Unit ( e.g. PC in case of Sales area 3310/40 )For Sale from <date>For Sale to <date>Item Category Group (NORM)Cash Discount (X)PP det. Seq.(Purchase Price determination Sequence) (01/ Standard with price determination)SP det Seq. (Sales price Determination Sequence) (01/ Calculate SP from planned markup)Final Price (<value>)Save Calculated Price (X) | Repeat the same step 12 and 13 for maintaining sales area – 3310/50 (For DC) – Pass Sales Unit as CARAdministrator can also maintain sales organization 3310 and distribution channel 10 for wholesale process. |  |
| 17 | Choose Views | Choose Logistics DC tab.Check for the below entries:In MRP Parameters:MRP Type: R1/Time-Phased Planning)Lot Size: EX/Lot-for-lot order quantity)Safety Stock: <value> By default it is 0Rounding profile: RDYP/ Retail Dynamic Rounding ProfileIn MRP Controller/Replenishment Data:MRP Controller: 001/MRP Controller 001Planning Cycle: P01/Order Day MondayPlanned Delivery Time: 5Supply Source: 1/StandardIn General ControlP arameters:Purchasing Group: 002/Group 002Tax Indicator: 2/Reduced taxAutomatic PO: XAvailability Check: ST/Consider only StockIn Physical Inventory/Goods Issue/ Picking/ Shipping section:Loading Group: 0001/CraneIn Storage Data:Storage Location: 995A | Create Article …(Logistics DC) view is displayed.On the Create Article : Logistics DC screen, check the available entries. These are proposed based on the reference Article . Only changes must be maintainedRounding profile is a key that the system uses to adjust the order proposal quantity to deliverable units. |  |
| 18 | Navigate to MRP/Forecast Data inside Logistics DC View | In the MRP/Forecast View maintain or check for the below entries:In Procurement section:Procurement Type: F/External procurement (display only)In Control data section:Auto reset: XPress Back button to navigate back to Logistics DC view. |  |  |
| 19 | Choose Views | Choose Logistics Store tab.Check for the below entries:In MRP Parameters:MRP Type: RF/Replenish with dyn.Target StockSafety Stock: <value> By default it is 0In Replenishment section:Target Coverage: 5In the Forecast Parameters:Forecast Model: K/Constant with smoothing factor adjustmentIn MRP Controller/Replenishment Data:Planned Delivery Time: 3Supply Source: 4/Stock Transfer Before StandardIn General Control Parameters:Purchasing Group: 002/Group 002Tax Indicator: 2/Reduced TaxAutomatic PO: XAvailability Check: ST(ST – Consider only stock)Negative Stock: XIn Storage Data:Storage Location: 994A | Create Article …(Logistics Store) view is displayed.On the Create Article : Logistics Store screen, These are proposed based on the reference Article . Check the available entries and do adjustments if necessary (for example supply source).Dynamic Target Stock is calculated at runtime during the planning run from forecast sales value. |  |
| 20 | Navigate to MRP/Forecast Data inside Logistics Store View | In the MRP/Forecast View maintain or check for the below entries:In Procurement section:Procurement Type: : F (External procurement)(display only)In the Number of P eriods Required section:History Periods: 60Forecast Periods: 12In Control D ata section:Initialization: XTrack Limit: 4(Value that specifies the amount by which the may deviate from the actual value.)Auto reset: XModel Selection Procedure: 2 (Analytical model selection procedure)Press Back button. | Administrator is navigated back to the Logistics Store view. |  |
| 21 | Choose Views | Choose POS tab.Enter Till receipt Text as mentioned below:Language Key: ENAlternate Unit: PCTill receipt text for Unit: <value> | Create Article …( POS) view is displayed.Maintain POS Text for distribution chain: 3310/40 (that is the relevant distribution chain for stores - in the case a different is proposed - the user should switch to this distribution chain)Maintain if necessary the text in different languages. Press the Insert Row (+) to add a new entry. |  |
| 22 | Save Your Data | At the bottom right of the display, choose Create to save your data. | The Create Article (Initial Screen) is displayed.The single article is created and saved.You can change or maintain or update the article created above, using Maintain Article (MM42) app. |  |

##### Create Generic Article with Variants

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Generic Article

Variants are articles that differ only in certain characteristics such as color, size, or flavor. They are grouped together as a generic article. Defining a generic article simplifies the maintenance of variants since you need to enter data that is same for all variants only once for the generic article.

You can use variant-creating characteristics (for example, flavor, variety) . By creating variants, the administrative header article becomes in fact an article (by means of the clearly identifiable variants). If a generic article is entered in a purchase order item, the system immediately starts grid processing of the individual variants.

By differentiating between the variants using single characteristic/several characteristics, the common data can be specified, created and stored centrally in the generic article.

Create Characteristic

This process allows you to define characteristic values for a characteristic separately. The method of managing characteristic values is particularly useful for characteristics with numerous characteristic values, such as colors or flavors. The system groups the characteristic values into clear partial quantities, to make it easier for you to access required characteristic values.

There are 4 different characteristic types available:

- Characteristic 1
- Characteristic 2
- Characteristic 3
- Not typed

If you use the categorized characteristic to define variants of a generic article, the system stores the characteristic valuation of the variant in the classification system and at the basic article data level. This improves the search for variants of a certain characteristics.

Maintain Characteristic Values

You use this function to enter characteristic values for a characteristic. At characteristic value level, there are up to ten customer-specific fields that you can use for customer-specific data. The system does not save the characteristic values with the characteristic, rather in a separate characteristic value table. This allows you to monitor characteristics with many characteristic values.

Create Variant Class

Groups characteristics created above and act as a variant creator for the generic article.

|  |
| --- |
| Note For more information, see the test script of scope items ID Product Taxonomies for Retail (5FJ). |

Create a Generic Article with Variants

Defining a generic article/product simplifies the maintenance of variants since you need to enter data that is the same for all variants only once for the generic article.

The following procedure provides instructions for creating generic article master data. The apps available to you depend on your assigned role. You can use any of the following two options.

Procedure: Manage Product Master Data (Option 1)

In this procedure you can create product master data using the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data (Retail) |  |  |
| 2 | Access the SAP Fiori App | Open Manage Product Master Data (F1602) app. | The Manage Product Master Data (F1602) screen is displayed. |  |
| 3 | Choose Create New Product Master | In the Manage Product Master Data (F1602) view, select Create and select Generic Article from the list. | The Create Master Data Record screen is displayed. |  |
| 4 | Enter Data for Mandatory Fields | In the Master Data Record sub-screen make the following entries:Product Number: for example: R_<XXXXX>Note You either enter any external alphanumeric ID, and that ID must start with an alphanumeric character, or if you provide no entry, the system automatically assigns a numeric ID.Product Type: Trading Goods(HAWA)Product Group: for example, Yoghurt (R1182001)Note On entering product group the reference product field is auto populated from the reference article maintained for the Product group.Description: <any description> | Note Automatically the field reference product is filled with the merchandise category reference article and master data are proposed based on this setting.There is as well the possibility to specify a dedicated reference product. |  |
| 5 | Choose OK | In the Manage Product Master view, choose OK. | The Manage Product Master view is displayed. |  |
| 6 | In General Information | In the Manage Product Master > General Information press Show more and enter Net Contents, Gross Contents and Comparison Price Unit in Content/Design section.Net Contents <value>(KG)Gross Contents <value>(KG)Comparison Price Unit (1)(KG) |  |  |
| 7 | Choose Create Description | In the Manage Product Master > General Information > Descriptions view, screen, choose Create. | Description in default language (for example, English) is already populated. |  |
| 8 | Enter Descriptions Data | In the Descriptions view, make the following entries:Language: for example, ArabicProduct Description: <your description> |  |  |
| 9 | Return to Main Screen | Choose Apply to return to Product screen. | The Product Master view is displayed. |  |
| 10 | Choose Base Unit of Measure | In the Manage Product Master > General Information > Base Unit of Measure view, and select Show More. |  |  |
| 11 | Enter Weight Data | In the Weight section, enter the following:Gross Weight: for example, 0.150Net Weight: for example, 0.140Weight Unit: for example, KG |  |  |
| 12 | Enter Unit of Measure | In the Manage Product Master > General Information > Unit of Measure view to navigate for further details. |  |  |
| 13 | Enter Receipt Texts | In the Receipt Texts section under Unit of Measure Texts. Select CreateEnter Language and Text. |  |  |
| 14 | Press Back button | Press Back to navigate back to main screen. |  |  |
| 15 | Create Alternate Unit of Measure | In the Manage Product Master > General Information > Units of Measure view, and select Create. | Unit of Measure screen is displayed. |  |
| 16 | Enter Unit of Measure | Enter Alternate Unit of Measure CAR |  |  |
| 17 | Enter Conversion factor | Enter <value> for example. 1 in Units / Quantity - Alternate Unit of MeasureEnter <value> for example. 10 in Units / Quantity - Base Unit of Measure |  |  |
| 18 | Enter Weight in Dimension Section | In the DimensionsWeight section, enter the following:Gross Weight: for example, 1.5Net Weight: for example, 1.4 (Default value proposed by the system)Weight Unit: for example, KGSelect Apply. | Return to the main screen Product Master is displayed. |  |
| 19 | Choose Reference values | In the Manage Product Master > General Information > Reference Values view and enter Purchasing Group 002/Group 002Delivery Unit of Measure (CAR) |  |  |
| 20 | Assign Class in Classification | In the Classification section click on Assign Class button (Using any class type) and search for R_FLAVOR in Search field and select Go. | Select Class sub-screen is displayed. |  |
| 21 | Select Filtered Entries | Select the filtered entry. | After selection of the filtered entry user will be navigated back to Classification section.Administrator can notice Variants (300) , Class – R_FLAVOR in the Classification Section. Along with them Administrator can also notice few characteristics assigned to the Class R_FLAVOR which in this case is FLAVOR and VARIETY in the Classification section. |  |
| 22 | Maintain Variant Creating Characteristics | Select FLAVOR or F4 on FLAVOR and all or few predefined values.Similarly, Click VARIETY or F4 on VARIETY and select all or few of the predefined values. | Flavor search help open where admin need to select few or all predefined values.Variety search help open where admin need to select few or all predefined values. |  |
| 23 | Select Product Variant | In the Variant section, choose Select Product Variants | Variants screen appears with possible combination of variant with empty check boxes along with them. |  |
| 24 | Select Possible Variant | Select all or few of the possible variant check boxes and press on Apply | Now the variants are shown |  |
| 25 | Choose Distributions Chains | In the Product screen, choose Distribution Chains tab. | The Distribution Chains tab is displayed. |  |
| 26 | Choose Create | In the Distribution Chains tab, choose Create | Distribution Chains opens in edit mode. |  |
| 27 | Enter Distribution Chains Data | In Distribution Chains, make following entries:In the GENERAL DATA - General Information section:Sales Organization: <Sales org number> 3310/Dom. Sales OrgNote The organization unit value is determined by what is offered in the value help.Distribution Channel: for example 40/Store SalesIn the Listing Parameters section:Remove the dates present (if any) . For example sales store or sales distribution center sales period start/end date.In the GROUPING TERMS section:Item Category Group: for example, SAMM | In Generic Article the field “General item category group” get defaulted to the value “SAMM” and for variants it is defaulted to “NORM”. |  |
| 28 | Return to Main View | Choose Apply to return to Product screen. | The Product screen is displayed. |  |
| 29 | Choose Purchasing | In the Product screen, choose Purchasing. | The Purchasing view is displayed. |  |
| 30 | Enter Purchasing Details | In the Purchasing section, enter Order Unit of Measure(CAR) |  |  |
| 31 | Choose Distribution Center | In the Product screen, choose Distribution center. | The Distribution Center tab is displayed. |  |
| 32 | Create Distribution Center | In the Distribution Center view, choose Create. | The Distribution Center view is displayed. |  |
| 33 | Enter Distribution Center - General Information Details | In the General Information section, make following entries:Distribution Center: Plant number for example, 3391 (Reference DC comes by default, no need to enter explicitly and remain non-editable)Loading Grp: for example, 0001 (Sales Data) | Similarly, Administrator can maintain for different DCs. |  |
| 34 | Enter Distribution Center - MRP Data | In the MRP Data > MRP Data section, make following entries:Availability Check: for example, ST(Consider only stock )MRP Type: For example, R1 (Time-Phased Planning)MRP Controller: For example, 001/MRP Controller 001 |  |  |
| 35 | Enter Distribution Center - Lot-Size Data | In the MRP Data > Lot-Size Data section, make the following entry:Lot Sizing Procedure: for example EX/ Lot-for-lot order quantity |  |  |
| 36 | Enter Distribution Center - Procurement Details | In the MRP Data > Procurement section, make the following entry:Planned Delivery Time: for example, 3Goods Receipt Processing Time: for example, 1 |  |  |
| 37 | Return to Main Screen | Choose Apply to return to Product screen. | The Product screen is displayed. |  |
| 38 | Choose Stores | In the Product screen, choose Stores. | The Stores tab is displayed. |  |
| 39 | Create Store | In the Stores section, choose Create. | The Store screen is displayed.Note This section is not related to store replenishment. |  |
| 40 | Enter Store - General Information Details | In the General Information section, make following entries:Stores: for example, 3392 (Reference Store comes by default, no need to enter explicitly and remain non-editable)Loading Grp: for example, 0001 (Crane) |  |  |
| 41 | Enter Store - MRP Data | In the MRP Data > MRP Data section, make following entries:Availability Check: for example, ST(Consider only stock)MRP Type: For example, RF (Replenish with dyn.Target Stock) |  |  |
| 42 | Enter Store - Procurement Details | In the MRP Data > Procurement section, make the following entry:Planned Delivery Time: for example, 3Goods Receipt Processing Time: for example, 1 |  |  |
| 43 | Return to Main Screen | Choose Apply to return to Product screen. | The Product screen is displayed. |  |
| 44 | Save Your Data | Choose Create. | System message is displayed. that object is saved. As a next step:You need to maintain purchasing Info record. For more information, see chapter Maintain Purchasing Info Record in scope item Products for Retail (3I1).You can change or maintain or update the article created above, using Maintain Article (MM42) app. |  |

Procedure: Create Article (Option 2)

In the procedure you can create article using Create Article (MM41) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data (Retail). |  |  |
| 2 | Access the SAP Fiori App | Open Create Article (MM41) app. | The Create Article (MM41) (Initial Screen) is displayed. |  |
| 3 | Enter Article Basic Data | In the Create Article (Initial screen) make the following entries:Material: Article number (R_<XXXXX>)Material type: Trading Goods/HAWA Trading GoodsMaterial Group: Yoghurt (R1182001)Material Category: Generic material/01 : Generic materialSelect Enter | Once the Administrator select Enter , you will notice Configuration class Type and Configuration Class fields are displayed on the Create Article screen. |  |
| 4 | Enter Configuration Class type and Configuration Class | Enter Configuration class type and configuration class:Configuration Class Type: 300Configuration Class: R_FLAVOR |  |  |
| 5 | Choose Views | Select Basic data view and choose continue. | Characteristics Value Assignment screen is displayed. |  |
| 6 | Characteristics Value Assignment screen | In the Characteristics Value Assignment screen, you can notice characteristics description and value fields where you need press F4 key for each of the Characteristics and select the values out of them. | Following values are displayed:Configuration Class Type – 300 (By Default)Configuration Class – R_FLAVOR (By Default)Generic Article – R_<XXXXX> (By Default)Below these value you will notice Characteristics Description and Values fields.The Characteristics Descriptions (Flavour and Variety) and Values (01 till 13 for Flavor and 01-02 for Variety) you see here belong to the Configuration Class (R_FLAVOR)Characteristics - Flavour:01 – Whole Milk02 – Nuts03 – Rasin-Nut04 – Christmas Flavour05 – Cherry Yoghurt06 – Summer-Feeling07 – Cinnamon08 – Orange-Punch09 – Strawberry10 – Raspberry11 – Blueberry12 – Blackberry13 – RedcurrantCharacteristics - Variety:01 - Diet02 - Normal |  |
| 7 | Press F4 on the Characteristics and select the variant creating characteristics | Press F4 on FLAVOR and select all or few values.Similarly press F4 on VARIETY and Select all of few values.Press Enter | Restrict value Range screen is displayed where you need to select the check boxes of the desired Characteristic Values |  |
| 8 | Press Back button on the Characteristics Value Assignment screen | Press Back button on the Characteristics Value Assignment screen | Variants for Generic Material Screen is displayed |  |
| 9 | Select Variants for Generic Article | Select Variants for Generic Article on the Variants for Generic Material Screen.Press Generate all missing nodes button or manually select the desired variants check boxes.Select Back or Next. | Create Material/Article R_<XXXXX> (Basic data) screen is displayed |  |
| 10 | Enter Basic Data | From Create Article ...(Basic Data), on the Basic data tab, enter a Article description (short text). |  |  |
| 11 | Enter Basic Data | In the Unit of measure/EANs/dimensions section, enter the following: (All the below should ideally get filled automatically (only except EAN Category) from the Reference Article, but if you need to maintain any deviation then you can go ahead and maintain)Base Unit of Measure (PC)Alternate Unit of Measure (CAR)Gross Weight (<value>)Unit of Weight (KG)Net Weight (<value>)Select Order Unit and Delivery Unit radio button for the Alternate UOM that is,. CAR in this case. |  |  |
| 12 | Enter Variant EANs | In the Basic Data tab under Standard Values For Entering Variant EANs , enter the following:AlternativeUnit (PC)EAN category (IE)Assign EANs int. (X)And press Variant EANs button ( a warning pop up might appear saying “EANs for all variants + unit of measure PC will be determined internally” press enter again. | You are navigated to the Standard Values For Entering Variant EANs screen where EANs are filled with system generated GTIN/EAN numbers. Select Back.The EAN generation for the variants can be done as well for UoM CAR if desired. |  |
| 13 | Enter Basic Data | From the Basic data tab enter the descriptions for the following: (All the below should ideally get filled automatically from the Reference Article, but if you need to maintain any deviation then you can go ahead and maintain)In Grouping Section:Division 00Pricing Profile (2/All variants have the sales price of the generic material)Variant Pricing Allowed (X)In Internal Logistics Data:Purchasing Group 002/Group 002Supply Source (4 - Stock Transfer Before Standard)GenItemCatGroup (SAMM)Loading Group (0001 - Crane)Transportation Group (0001/ On Pallets )Variable Order Unit (1/Active)In General Data:Tax Class (2-Reduced tax)Valuation Class (3100- Trading goods)Country of Origin AEIn Content Section:Net Contents (150)Gross Contents (150)Content Unit (G)Comparison Price Unit (100)In Validity Section:Valid from: <date>Valid to: <date>(default 31.12.9999, cannot be maintained)In Shelf Life Data section:Remaining Shelf Life(0)Total Shelf Life(0)Period indicator(D)Storage %(0) | Generic article you will see the general item category as SAMM. NORM is the item category for the variants which you can see by double clicking on the field general item category group.Note Double-click on most of the fields the variant matrix appears and deviations at variant level is maintained. Another option to maintain different data at variant level would be the possibility to choose the button: Switch validity area and specify a variant number. |  |
| 14 | Navigate to Go to Additional data in Basic Data View: | In Short Text View enter/check the description and language:Language ArabicMaterial Description <Value>In the Unit of Measure View maintain/check the following (for Alternate UOM):Gross Weight <value>Unit of Weight (KG)Select Go to Main Data. | Basic Data screen is displayed. |  |
| 15 | Choose Views | Choose Basic data 2 tab. | Create Article …(Basic data 2) view is displayed. |  |
| 16 | Enter Sales Period | Enter Sales period for Stores and Distribution Center.Sales Period: storeFor sales fromFor sales tillSales Period: distribution centerFor sales fromFor sales till |  |  |
| 17 | Choose Views | Choose Purchasing tab. | Create Article …(Purchasing) view is displayed. |  |
| 18 | Enter Organizational Levels Data | In Switch Validity Area, in the Area of Validity section, enter descriptions for the following:Purchasing Org. 3310/Purch. Org. 3310Supplier (33213002/Retail Food Supplier AE)Choose Continue. |  |  |
| 19 | Enter Purchasing Data | On the Create Article : Purchasing screen, make the following entries:(All the below data can be proposed from the business partner (supplier) (only except Net Price), but if you need to maintain any deviation then you can go ahead and maintain)Purchasing Group 002/Group 002Var. Order Unit (1/Active)Regular Supplier (X)Net Price (<value>) | As a next step, you need to maintain purchasing Info record. For more information, see chapter Maintain Purchasing Info Record in scope item Products for Retail (3I1).Note Regular Supplier value makes sense, only if the customer is operating in one country and has several suppliers for this article and one should be the preferred supplier. |  |
| 20 | Choose Views | Choose Sales tab. | Create Article …(Sales) view is displayed.. |  |
| 21 | Enter Organizational Levels Data | In Switch Validity Area, in the Area of Validity section, enter descriptions for the following:Sales Org. 3310/Dom. Sales OrgDistr. Channel (40 –Store Sales)Choose Continue. | Repeat the same step 13 and 14 for maintaining Sales Area – 3310/50 (For DC) – Pass Sales Unit as CARUser can also maintain Sales Organization 3310 & Distribution Channel 10 for wholesale process.In generic article, the item category as SAMM. NORM is the item category for the variants which you can see by double clicking on the field item category group. |  |
| 22 | Enter Sales Data | On the Create Article :Sales screen, make the following entries:(Few of the below should ideally get filled automatically from the Reference Article e.g. item category group, cash discount,.))Sales Unit ( e.g. PC in case of Sales Org/ Channel 3310/40 )For Sales from <date>For Sales to <date>Item Category Group (SAMM)Cash Discount (X)PP det. Seq.(Purchase Price determination Sequence) (01/ Standard with price determination)SP det Seq. (Sales price Determination Sequence) (01/ Calculate SP from planned markup)Final Price (<value>)Save Calculated Price (X) |  |  |
| 23 | Choose Views | Choose Logistics DC tab.Check for the below entries:In MRP Parameters:MRP Type: R1 (Time-Phased Planning)Lot Size: EX (Lot-for-lot order quantity)Safety Stock: <value> By default it is 0Rounding profile: RDYP/ Retail Dynamic Rounding ProfileIn MRP Controller/Replenishment Data:MRP Controller: 001/ MRP Controller 001Planning Cycle: P01(Order Day Monday)Planned Delivery Time: 1Supply Source: 1 (Standard)In General Control Parameters:Purchasing Group: 002/Group 002Tax Indicator: 2( Reduced tax)Automatic PO: XAvailability Check: ST(Consider only stock)In Physical Inventory/Goods Issue/ Picking/ Shipping:Loading Group: 0001/ CraneIn Storage Data:Storage Location: 995A | Create Article …(Logistics DC) view is displayed. | On the Create Article : Logistics DC screen, check the available entries. These are proposed based on the reference article. Only changes must be maintained.Rounding profile is a key that the system uses to adjust the order proposal quantity to deliverable units. |
| 24 | Navigate to MRP/Forecast Data inside Logistics DC View | In the MRP/Forecast View maintain or check for the below entries:In Procurement section:Procurement Type: : F (External procurement)In Scheduling section:Schedule Margin key: 001In Control Data section:Auto reset: XSelect Back . | Administrator is navigated back to the Logistics DC view. |  |
| 25 | Navigate to Other logistics Data inside Logistics DC View | In the Other logistics Data View maintain or check for the below entries:In General Plant parameter:Unit of Issue: CARIn Foreign Trade data:Country/Region of Origin: AESelect Back. | Administrator is navigated back to the Logistics DC view. |  |
| 26 | Choose Views | Select Logistics Store tab and choose continue or Enter.Check for the below entries:In MRP Parameters:MRP Type: RF (RF – Replenish with dynamic.Target Stock.Dynamic Target Stock gets calculated at runtime during the planning run from forecast sales value)Safety Stock: <value> By default it is 0In Replenishment parameters section:Target Coverage: 5In the Forecast Parameters:Forecast Model: DIn MRP Controller/Replenishment Data:Planned Delivery Time: 1Supply Source: 4 ( Stock Transfer Before Standard)In General Control Parameters:Purchasing Group: 002/Group 002Tax Indicator: 2 ( Reduced tax)Automatic PO: XAvailability Check: ST(Consider only Stock)Negative Stock: XIn Procurement Data:Storage Location: 994A | Create Article …(Logistics Store) view is displayed. On the Create Article : Logistics Store screen, Check the available entries and do adjustments if necessary (For example. supply source) |  |
| 27 | Navigate to MRP/Forecast Data inside Logistics Store View | In the MRP/Forecast View maintain or check for the below entries:In Procurement section:Procurement Type: : F (External procurement)(Display Only)In the Number of periods required section:History Periods: 60Forecast Periods: 12In Control data Section:Initialization: XTrack Limit: 4(Value that specifies the amount by which the forecast value may deviate from the actual value.)Auto reset: XModel Selection Procedure: 2 (Analytical model selection procedure)Select Back. | Administrator is navigated back to the Logistics Store view. |  |
| 28 | Navigate to Other logistics Data inside Logistics Store View | In the Other logistics Data View maintain or check for the below entries:In General Plant parameter:Unit of Issue: PCIn Foreign trade data:Country/Region of Origin: AESelect Back. | Administrator is navigated back to the Logistics DC view. |  |
| 29 | Choose Views | Select POS tab.Enter Till receipt Text as mentioned below:Language Key: ENAlternate Unit: PCTill receipt text for Unit: <value> | Create Article …(POS) view is displayed.Maintain POS Text for distribution chain: 3310/40 (that is the relevant distribution chain for stores - in the case a different is proposed - the user should switch to this distribution chain) Maintain if necessary the text in different languages. Select Additional Data. |  |
| 30 | Save Your Data | At the bottom right of the display, choose Create to save your data. | The Create Article (Initial Screen) appears.The generic article is created and saved.You can change or maintain or update the article created above, using Maintain Article (MM42) app. |  |

#### Create Assortments

##### Create Assortment Module

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To initiate the listing process for defining an assortment, you have to create an assortment module along with an assortment module version first.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Assortment Specialist - Retail. |  |  |
| 2 | Access App | Open the Manage Assortment Modules (F4892) app. | The app opens and a list report with an empty result table appears. |  |
| 3 | Start Assortment Module Creation | In the table toolbar, choose Create. | The Create Assortment Module dialog box appears. |  |
| 4 | Enter Required Data and Finish Assortment Module Creation | Tip If you execute this test case multiple times, make sure to enter different values in the Assortment Module field.In the Create Assortment Module dialog box, make the following entries and choose Create:Assortment Module: ASM1Description: <Your Description for the Assortment Module>First Version Valid From: <Your Start Date of the First Version>First Version Valid To: Leave empty for unlimited validityFirst Version Description: <Your Description for the First Version> | Assortment module ASM1 is created along with the first version according to your entries.The object page of the newly created assortment module appears. |  |

##### Create Assortment Module Version

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Time dependency is a major aspect when defining assortments. To leverage the time dependency features provided by the assortment module management solution, you create a second assortment module version. You can use multiple assortment module versions to map how the store assortment changes over time.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Assortment Specialist - Retail. |  |  |
| 2 | Access App | Open the Manage Assortment Modules (F4892) app. | The app opens and the list report with an empty result table appears. |  |
| 3 | Search for Assortment Module | Set the Assortment Module filter by entering ASM1 and choose Go. | The list report contains one line item with assortment module ASM1. |  |
| 4 | Navigate to Assortment Module | In the list report, click the line item of assortment module ASM1 to trigger the navigation. | The object page of assortment module ASM1 appears. |  |
| 5 | Start Version Creation | In the table toolbar of the Versions facet, choose Create. | The Create Assortment Module Version dialog box appears. |  |
| 6 | Enter Required Data and Finish Version Creation | In the Create Assortment Module Version dialog box, make the following entries and choose Create:Description: <Your Description for the Second Version>Valid From: <Your Start Date of the Second Version> (The validity start date of the second version must be later than the validity start date of the first version.)Valid To: Leave empty for unlimited validity | The dialog box disappears, and the newly created version appears in the Versions facet. The validity periods are as follows:Valid From/To of first version: <Your Start Date of the First Version> - (<Your Start Date of the Second Version> - 1 day)Valid From/To of second version: <Your Start Date of the Second Version> - 31.12.9999 |  |

##### Assign Product to Assortment Module Version

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You assign the first product to the assortment module version created in the previous process steps. An assortment definition can be described as a relationship between products and stores. Therefore, the product assignment to the assortment module version is a vital step toward listing the product in a store and a distribution center.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Assortment Specialist - Retail. |  |  |
| 2 | Access App | Open the Manage Assortment Modules (F4892) app. | The app opens and a list report with an empty result table appears. |  |
| 3 | Search for Assortment Module | Set the Assortment Module filter by entering ASM1 and choose Go. | The list report contains one line item with assortment module ASM1. |  |
| 4 | Navigate to Assortment Module | In the list report, click the line item of assortment module ASM1 to trigger the navigation. | The object page of assortment module ASM1 appears. |  |
| 5 | Navigate to First Version | In the Versions facet, click the line item of the version which has the earliest valid-from date (that is, the lowest line item). | The object page of the first assortment module version appears. |  |
| 6 | Start Product Assignment | In the toolbar of the table that displays the assigned products, choose Assign. | The Assign Products to Version dialog appears. |  |
| 7 | Enter Required Data and Finish Product Assignment | In the Assign Products to Version dialog, make the following entries and choose Assign:Products: <Product 1>Under Additional Settings, select the Assign to Existing Follow-On Versions checkbox. | The dialog disappears, and the newly assigned product appears in the table that displays the assigned products.The line item contains the following data:Product: <Product 1>Assigned From/To: <Your Start Date of the First Version> - <End Date of the First Version>.You can navigate to the second version by choosing the up-arrow icon (Previous) in the header toolbar next to the Share button.If you navigate to the second version, there is a new line item in the table that displays the assigned products. The new line item contains the following data:Product: <Product 1>Assigned From/To: <Your Start Date of the Second Version> - 31.12.9999. |  |

|  |
| --- |
| Note If you do not use a single article in the above-mentioned process, but any other product category, you must consider the following:You cannot directly assign generic articles to an assortment module version. Instead, you can filter for a specific generic article and assign its variants or a selection of them to the assortment module version.If you assign a structured article to an assortment module version, the system automatically generates the required product master data for the components. Listing conditions are only generated for the structured article itself, not for the individual components. If listing conditions are also required for the components, you must assign them individually to the assortment module version.If you assign a full product, the system automatically generates listing conditions and product master data for the empties, without assigning them to an assortment module version or a distribution center. It is not required to assign empties individually to assortment module versions or distribution centers. |

##### Assign Store to Assortment Module

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You assign a store to the assortment module created in process step [Create Assortment Module](#unique_14) [page ] 38. Together with the product assignment which you added in process step [Assign Product to Assortment Module Version](#unique_16) [page ] 40, your store assignment entails the first listing condition and initiates the generation of the product master data for the assigned store.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Assortment Specialist - Retail. |  |  |
| 2 | Access App | Open the Manage Assortment Modules (F4892) app. | The app opens and a list report with an empty result table appears. |  |
| 3 | Search for Assortment Module | Set the Assortment Module filter by entering ASM1 and choose Go. | The list report contains one line item with assortment module ASM1. |  |
| 4 | Navigate to Assortment Module | In the list report, click the line item of assortment module ASM1 to trigger the navigation. | The object page of assortment module ASM1 appears. |  |
| 5 | Start Store Assignment | In the table toolbar of the Assortment User s facet, choose Assign. | The Assign Assortment Users to Assortment Module dialog box appears. |  |
| 6 | Enter Required Data and Finish Store Assignment | In the Assign Assortment Users to Assortment Module dialog box, make the following entries and choose Assign:Assortment Users: 3340Assigned From: Leave as is (the default date is the current date)Assigned To: Leave empty for unlimited validity | The dialog box disappears, and the newly assigned assortment user appears in the Assortment Users facet.The line item contains the following data:Assortment User: 3340Assigned From/To: Current date - 31.12.9999. |  |

##### Assign Products to Distribution Center

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You have already defined the relationship between the product and the store in the previous steps, that is, you have defined which product can be procured by which store. Subsequently, you have to assign the relevant products to the appropriate distribution center so that they are orderable.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Assortment Specialist - Retail. |  |  |
| 2 | Access App | Open the Assign Products to Distribution Centers (F4543) app. | The app opens and a list report with an empty result table appears. |  |
| 3 | Search for Products to Be Assigned | Set the Assigned to DC filter to No, set the Product filter by entering both products, <Product 1> and <Product 2>, and choose Go. | The list report contains two line items with products <Product 1> and <Product 2>. |  |
| 4 | Start Product Assignment to Distribution Center | Select both products by selecting the checkbox of each line item and choose Add Assignments. | The Assign Products to Distribution Centers dialog box appears. |  |
| 5 | Select Distribution Center and Finish Product Assignment to Distribution Center | In the Assign Products to Distribution Centers dialog box, search for distribution center 3350, select the corresponding checkbox, and choose Assign. | After the products have been assigned, the list report displays an empty result table.This is due to the fact that the Assigned to DC filter is set to No. Therefore, both products do not match the filter criteria anymore because they have already been assigned to a distribution center. |  |
| 6 | Search for Assigned Products | Set the Assigned to DC filter to Yes and choose Go. | Both products appear as line items in the result table of the list report. |  |
| 7 | Check for Correctness of Product Assignment | In the list report, click the line item of one of the products to trigger the navigation. | The object page of the product appears. Check whether the Product Assignments facet contains a line item with the following data:Distribution Center: 3350Assigned From: Current dateAssigned To: 31.12.9999 |  |
| 8 | Repeat Step 7 for Other Product |  |  |  |

#### Create Purchasing Info Record

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Purchaser (Retail). | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Purchasing Info Records (F1982). | The Manage Purchasing Info Records (F1982) screen displays. |  |
| 3 | Open New Purchasing Info Record | Choose Create. | The Purchasing Info Record Screen displays. |  |
| 4 | Enter Header Data | Make the following entries:Purchasing Info Record Category: <Standard>Purchasing Organization: 3310Supplier: 33213001Material: <Material>Note Please use Material created in test procedure step Create Single Article.Plant: 3350Purchasing Group: 001/002Material Group: R1193001 | Header data is added. |  |
| 5 | Enter General Information | Make the following entries:Available From: MM/DD/YYYYAvailable To: MM/DD/YYYY | General Information is added. |  |
| 6 | Enter Purchasing Data | Make the following entries:Incoterm: <Incoterm>Incoterm Location 1: <Incoterm location1> | Purchasing Data is added. |  |
| 7 | Enter Delivery and Quantity Data | Make the following entries:Delivery Time in Days: <XX Days>Under Delivery Tolerance in %: <XX>Over Delivery Tolerance in %: <XX>Order Unit: <Order Unit>Standard Order Quantity: <Standard Order Quantity>Select the following entries if required:Unlimited DeliveryGoods-Receipt-Based Invoice VerificationNo Evaluated Receipt SettlementOrder Acknowledgment RequirementConfirmation Control | Delivery and Quantity Data is added. |  |
| 8 | Enter Condition Data | In the Condition section, choose the Create icon. Enter the following data:Valid From: <Valid from Date>Amount: <Amount>Pricing Unit: <Pricing Unit>Valid To: <Valid to Date>Currency: AEDChoose Apply. | Condition Data is added. |  |
| 9 | Enter Reference Data (Optional) | Optionally, you can enter reference data. | Reference data is added. |  |
| 10 | Save Your Data | Choose Create. | A purchasing info record is saved. |  |

#### Create Purchase Order

##### Create Purchase Order Directly

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process, purchase order is created directly.

|  |
| --- |
| Note Use this process for delisting and discontinuation scenarios. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser (Retail). |  |  |
| 2 | Access the App | Open Create Purchase Order (ME21N) app. | Create Purchase Order intial screen is displayed. |  |
| 3 | Enter Purchase Order Data | Enter all of the necessary data:Order type: NB Standard POSupplier: <use your own Supplier>In Header section, on the Org. Data tab, make the following entries:Purchasing Org.: 3310Purchasing Group: 002Company Code: 3310In Items section,selectMaterial: <XXXXX>Note Use the article created in test procedures [Create Single Article](#unique_12) [page ] 11 / [Create Generic Article with Variants](#unique_13) [page ] 24.Plant: 3350Storage Location: 995A(Automatically determines)Quantity: 100Net Price: XX(Automatically determines) | Purchase order details provided. |  |
| 4 | Save the Purchase Order | Choose Save. | Purchase order is created.Make a note of the purchase order number. |  |

#### Create Allocation Table

|  |
| --- |
| Note In this process step, shows you the creation of allocation table manually for the [Create Single Article](#unique_12) [page ] 11 or [Create Generic Article with Variants](#unique_13) [page ] 24 created in the previous steps.Use the same article (created in [Create Single Article](#unique_12) [page ] 11 or [Create Generic Article with Variants](#unique_13) [page ] 24) to create allocation table manually. |

##### Create Allocation Table Manually

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create an allocation table in SAP S/4HANA Cloud Public Edition, retail, fashion, and vertical business to allocate a specific quantity of merchandise among the stores. The allocation table contains all the important information on how the merchandise is to be distributed, such as the articles to be allocated, the source of supply, the recipients, the quantity each recipient is to receive, and the delivery dates.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as Allocator (Retail) |  |  |
| 2 | Access the app | Open Create Allocation Table (WA01) app |  |  |
| 3 | Make entries | On the Create allocation table screen, make the following entries:Allocation Table Type : 0002(1-step Alloc int)Purchasing Organization : for example 3310Purchasing Group : 001Select Continue | Values entered in the initial screen of allocation is accepted. |  |
| 4 | Fill the fields | On the Create allocation table screen, make the following entries:Allocation Table Description : <Description>Plant Delivery Date : today’s date + 4 (Days)DC Delivery Date : today’s date + 3 (Days)Enter dates in future and DC delivery date one day less than plant delivery date.Material: for example R_1006Plan Quantity: 10Select ENTERNote All the dates must be working days in future. | Field values are accepted. |  |
| 5 | Site group assignment | Select the line item and select Item button, on the Create allocation table: Fast Change Item Data (For Selected Items) screen, make the following entries:Plant group: for example R_SITEGROUP_AE_01Select ENTERSelect Check then select ExecuteIf a message ‘…Change item nonetheless?’ is displayed, select ContinueThe message “Fast entry results: ... item(s) selected; ... item(s) changed; errors: 0” is displayed, select ContinueNote Item category: F Proposed |  |  |
| 6 | Save | Select Save to save your entriesMake a note of the Allocation Table number. | An allocation table is created. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Merchandise Category](#unique_25) [page ] 52 | Master Data Specialist - Product Data (Retail) | Create Merchandise Category (WG21) | Merchandise Category is created. |
| [Maintain Merchandise Category](#unique_26) [page ] 56 | Master Data Specialist - Product Data (Retail) | Maintain Merchandise Category (WG22) | Merchandise Category is maintained. |
| [Display Merchandise Category](#unique_27) [page ] 57 | Master Data Specialist - Product Data (Retail) | Display Merchandise Category (WG24) | Merchandise Category is displayed. |
| [Change Merchandise Category Hierarchy Level](#unique_28) [page ] 58 | Master Data Specialist - Product Data (Retail) | Maintain Hierarchy Level - Merchand. Cat. Hier. (CLWN) | Merchandise Category Hierarchy Level is maintained. |
| [Assign Merchandise Category Hierarchy Level (Optional)](#unique_29) [page ] 59 | Master Data Specialist - Product Data (Retail) | Assign Hierarchy Level - Merchand. Cat. Hier. (CLW1) | Merchandise Category Hierarchy Level is assigned. |
| [Display Merchandise Category Hierarchy Level](#unique_30) [page ] 60 | Master Data Specialist - Product Data (Retail) | Display Hierarchy Level - Merchand. Cat. Hier. (CLWO) | Merchandise Category Hierarchy Level is displayed. |
| [Display Merchandise Category Hierarchy](#unique_31) [page ] 61 | Master Data Specialist - Product Data (Retail) | Display Merchandise Cat. Hierarchy (WGUS) | Merchandise Category Hierarchy is displayed. |
| [Delete Merchandise Category Hierarchy Level (Optional)](#unique_32) [page ] 61 | Master Data Specialist - Product Data (Retail) | Delete Hierarchy Level - Merchand. Cat. Hier. (CLWP) | Merchandise Category Hierarchy Level is deleted. |
| [Reclassification of Retail Material (Optional)](#unique_7) [page ] 62 | Master Data Specialist - Product Data (Retail) | Reclassify Article - Merchandise Category (WRCR) |  |
| [Create Reclassification Version for Merchandise Category or Merchandise Category Hierarchy Node](#unique_33) [page ] 64 | Master Data Specialist - Product Data (Retail) | Create Reclassific. Version - Merchandise Category (WRC4) |  |
| [Update Reclassification Version for Merchandise Category or Merchandise Category Hierarchy Node](#unique_34) [page ] 65 | Master Data Specialist - Product Data (Retail) | Update Reclassific. Version - Merchandise Category (WRCV) |  |
| [Maintain Reclassification Version for Merchandise Category or Merchandise Category Hierarchy Node](#unique_35) [page ] 66 | Master Data Specialist - Product Data (Retail) | Maintain Reclassific. Version - Merchandise Category (WRC3) |  |
| [Display Reclassification Version for Merchandise Category or Merchandise Category Hierarchy Node](#unique_36) [page ] 67 | Master Data Specialist - Product Data (Retail) | Display Reclassific. Version - Merchandise Category (WRC2) |  |
| [Delete Reclassification Version for Merchandise Category or Merchandise Category Hierarchy Node](#unique_37) [page ] 68 | Master Data Specialist - Product Data (Retail) | Delete Reclassific. Version - Merchandise Category (WRC1) |  |

## Test Procedures

This chapter describes procedures for each segment or process step that is part of this master data test script.

### Create Merchandise Category

Purpose

This process step shows you how to create merchandise category and assign it to last node (Leaf node) of merchandise category hierarchy.

|  |
| --- |
| Note Merchandise category is prerequisite to create article master data. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Log onto the SAP Fiori launchpad as Master Data Specialist - Product Data (Retail) |  |  |
| 2. | Access the app | Open Create Merchandise Category (WG21) app. | The Material group Create: screen is displayed. |  |
| 3. | Provide input values | On the initial screen, make the following entries and select ENTER:Material Group: <XXXXXX>Note Enter the merchandise category name, that needs to be created. |  |  |
| 4. | Fill all required fields in basic data | In Basic Data screen, make the following entry and select ENTER:Material Group Desc.: <XXXXXXX> (Enter the description accordingly)MG Hierarchy Level: <XXXXXXX>Note Enter the Merchandise category hierarchy level created in preliminary step [Create Merchandise Category Hierarchy Level](#unique_11) [page ] 10.(Optional entry) - In Assignment, enter theMG Ref. Material:R_REF01Division: 00Note If you want to create a new Merchandise Category Reference Article, do not assign merchandise category reference article here and follow step 7, to create a Merchandise Category Reference Article. |  |  |
| 5. | Save your entries | Select Save | A message “Material group < XXXXX > created” is displayed. |  |
| 6. | Assign characteristics/keyword (Optional) | Select Go to Characteristics/Keyword. Provide characteristic value.Char.: R_ORGANIC (The characteristics assigned directly to the merchandise category are usually informative characteristics. The informative characteristic, for example, R_ORGANIC in the system, has the values assigned directly in CT04 and not through the Function Module. WRF_CHECK_CHAR_VAL)And select Save | A pop-up message is displayed. |  |
| 7. | Create MG reference material (Optional - only applicable if No Ref Article assigned in step 4) | Select Go to MG ref. material to create MG reference material:Material: <XXXXXXX>Note Enter a material name or number that needs to be createdMaterial Type: HAWA Trading GoodsSales Org.: 3310Distr. Channel: 10Select following views:Basic DataBasic Data 2SalesLogistics: Distribution CenterLogistics: StorePOSSelect ENTERUnder Basic Data View, enter the below entries:Description: <XXXXX> (Enter a material description)Alternative Unit of Measure: PCIn Groupings:Division: 00Pricing profile: 2Var.Pr. All: XIn General Data:Tax class: 1Valuation Class: 3100 (value is defaulted)In Internal Logistics Data:Supply Source: 4Trans. Group: 0001Loading Group: 0001GenItemCatGroup: NORM (value is defaulted)Var. Order Unit: 1In Shelf-Life Data:Period Ind: D (value is defaulted)Select ENTERNavigate to Basic Data 2 ViewIn Sales Period: StoreFor sale from: DD.MM.YYYY (Defaulted with system date)For sale till: DD.MM.YYYY (Defaulted with 31.12.9999)In Sales Period: Distribution center:For sale from: DD.MM.YYYY (Defaulted with system date)For sale till: DD.MM.YYYY (Defaulted with 31.12.9999)Select ENTERSelect Sales view and enter the below entries:In Validities for Each Distribution Chain:Item Cat. Group: NORM (Standard item) (value is defaulted)Cash Discount: X (value is defaulted)In Calculation Procedure/Planning Data:PP Det. Seq.: 01 (value is defaulted)SP Determ. Seq.: 01 (value is defaulted)Select Switch Validity Area and select ENTERSales Org.: 3310Distr. Channel: 40 and select continueRepeat the previous step for Distr. Channel: 50 and select ENTERSelect Logistics DC view and enter the below entries:In MRP Parameters:MRP Type: R1 (Time-Phased Planning)Lot Sizing Proc : EX (Lot-for-lot order quantity)Safety Stock: <value> By default it is 0Rnding Profile: RDYPIn MRP Controller/Replenishment Data:MRP Controller 001/001Planning Cycle: P01(Order Day Monday)Pl. Deliv. Time: 5Supply Source: 1 (Standard)In General Control Parameters:Purch. Group : 002Tax Indicator: 1 – Material 100%Autom . PO: XAvail check: ST (Consider only Stock)In Physical Inventory/Goods Issue/ Picking/ Shipping section:Loading Group: 0001 – Crane (value is defaulted)In Storage Data section:Stor . Location : 995A and select ENTERSelect Logistics Store view and enter the below entries:In MRP Parameters:MRP Type: RF (Replenish with dyn.Target Stock)Safety Stock: <value> By default it is 0In Replenishment parameters section:Target Coverage: 5In MRP Controller/ReplenishmentData:Pl. Deliv. Time : 3Supply Source: 4 (Stock Transfer before Standard) (value is defaulted)In General Control Parameters:Purch. Group : 002Tax Indicator: 1 – Material 100%Autom . PO: XAvail check: ST (Consider only Stock)Neg .stocks : XIn the Storage Data:Stor . Location: 994A and select ENTERSelect POS view, enter the below entries:Select Switch Validity Area and select ENTERSales Org.: 3310Distr. Channel: 10and select continueIn Till receipt texts:Enter the two-line items as below in the table.L: DE and ENAUn: PCTill rcpt texts for unit: <XXXXXXXXXXX>And repeat the previous step for Distr. Channel: 40 and 50. |  |  |
| 8. | Save your entries | Select SaveMake a note of the merchandise group referencematerial you have created. | A merchandise category is created and a message is displayed. |  |

Result

Material is created for merchandise category (material group).

### Maintain Merchandise Category

Purpose

This process step shows you how you change the existing merchandise category details of merchandise category and assignment of merchandise category hierarchy level to merchandise category.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Log onto the SAP Fiori launchpad as Master Data Specialist - Product Data (Retail) |  |  |
| 2. | Access the app | Open Maintain Merchandise Category (WG22) app. |  |  |
| 3. | Provide input values | On the initial screen, make the following entry and change Basic Data :Material Group: <XXXXXXXXX> (Enter the material group created in step [Create Merchandise Category](#unique_25) [page ] 52) | A message Material group Change: basic data screen is displayed. |  |
| 4. | Change or fill the required field values and save your entries | In Basic Data screen, you can change the following entries as per requirement and select ENTER. and select SaveMaterial Group Desc.: <XXXXXXX>Material Grp Desc. 2: <XXXXXXXXX>MG Ref. Material: <XXXXXXXXX>Division: 00 and so on. | A message Material group < XXXXXX > changed is displayed. |  |
| 5 | Change merchandise category hierarchy level already assigned (optional) | Go back to Basic Data screen In Basic Data screen, you can change the following entries as per requirement and select ENTER. and select SaveAssign merchandise hierarchy level as belowMG Hierarchy Level: <XXXXXXX>Note If the hierarchy level needs to be changed, follow the steps to create a new merchandise category hierarchy level in preliminary step [Create Merchandise Category Hierarchy Level](#unique_11) [page ] 10 | Merchandise Category <XXXXXXXXX> is changed |  |

Result

Merchandise category values are updated.

### Display Merchandise Category

Purpose

This process step shows you how you display the details of an existing merchandise category.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Log onto the SAP Fiori launchpad as Master Data Specialist - Product Data (Retail) |  |  |
| 2. | Access the app | Open Display Merchandise Category (WG24) app. | The Material group Display: screen is displayed. |  |
| 3. | Provide Input values | On the initial screen, make the following entry and select ENTER:Material Group: <XXXXXX> (Enter the material group created in step [Create Merchandise Category](#unique_25) [page ] 52)or select any from Display basic data, Display characteristics/keyword, Display material overview and Display MG ref. material | If you select ENTER, only basic data details are displayed.A message Display basic data, Display characteristics/keyword, Display material overview, Display MG ref. material is displayed. |  |
| 4. | Exit Screen | Select Exit |  |  |

Result

Merchandise Category (material group) details are displayed.

### Change Merchandise Category Hierarchy Level

Purpose

This process step shows you how you change the details of existing merchandise category hierarchy level.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Log onto the SAP Fiori launchpad Master Data Specialist - Product Data (Retail) |  |  |
| 2. | Access the app | Open Maintain Hierarchy Level - Merchand. Cat. Hier. (CLWN) app. |  |  |
| 3. | Provide input values | On the initial screen, make the following entries and select ENTER:Hierarchy Level: <XXXXXXXXX> (Enter the merchandise category hierarchy level created in preliminary step [Create Merchandise Category Hierarchy Level](#unique_11) [page ] 10). |  |  |
| 4. | Change or fill the required field values | In Basic Data tab, make the following entry and selectENTER:Description: <XXXXXXX> (Change the description of the merchandise category hierarchy level if required). |  |  |
| 5. | To maintain a description in an additional language | Select Change languageIn the dialog box, enter language, for example, Arabic and select Continue.On the Basic Data tab, enter description for second language. |  |  |
| 6. | Save your entries | Select Save. | A message Class type 026: Hierarchy level < XXXXXX > changed” is displayed. |  |

Result

Merchandise category hierarchy level is changed.

### Assign Merchandise Category Hierarchy Level (Optional)

Purpose

This process step shows you how you can assign merchandise category hierarchy levels. You execute this optional step by creating multiple merchandise category hierarchy levels (Refer preliminary step [Create Merchandise Category Hierarchy Level](#unique_11) [page ] 10).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Log onto the SAP Fiori launchpad Master Data Specialist - Product Data (Retail) |  |  |
| 2. | Access the app | Open Assign Hierarchy Level - Merchand. Cat. Hier. (CLW1) app. | The Maintain Material Group Hierarchy Level: screen is displayed. |  |
| 3. | Provide input values | On the initial screen, make the following entries and select ENTER:Superior MatlGrp Hierarchy Level: <XXXXXXXXX> (Enter a new merchandise category hierarchy level created by following preliminary step [Create Merchandise Category Hierarchy Level](#unique_11) [page ] 10). |  |  |
| 4. | Fill all mandatory field | In Assignments table, make the following entries and select ENTER:Hierarchy Level: <XXXXXXXXX> (create a new merchandise category hierarchy level by following the steps in preliminary step [Create Merchandise Category Hierarchy Level](#unique_11) [page ] 10. Use hierarchy level other than the one entered in step 3). |  |  |
| 5. | Save your entries | Select Save |  |  |

### Display Merchandise Category Hierarchy Level

Purpose

This step shows you how you display the existing merchandise category hierarchy level.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Log onto the SAP Fiori launchpad as Master Data Specialist - Product Data (Retail) |  |  |
| 2. | Access the app | Open Display Hierarchy Level - Merchand. Cat. Hier. (CLWO) app. | The Display Hierarchy Level: screen is displayed. |  |
| 3. | Provide input values | On the initial screen, make the following entries and select ENTER:Hierarchy Level: <XXXXXXXXX> (Enter the material group hierarchy level created in preliminary step [Create Merchandise Category Hierarchy Level](#unique_11) [page ] 10) |  |  |
| 4. | Display details | In Basic Data tabDescription: <XXXXXX> | Hierarchy level details are displayed. |  |
| 5. | Exit Screen | Select Exit |  |  |

### Display Merchandise Category Hierarchy

Purpose

This step shows you how you display the existing merchandise category hierarchy level based on the merchandise category. You can display the details of material and plant assigned to the respective merchandise category of the hierarchy level.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Log onto the SAP Fiori launchpad as Master Data Specialist - Product Data (Retail) |  |  |
| 2. | Access the app | Open Display Merchandise Cat. Hierarchy (WGUS) app. | The Use of Material Groups screen is displayed. |  |
| 3. | Provide input values | On the initial screen, make the following entries and select execute.In Select material group objects section:Material group object: <XXXXXXXXX> (Enter the material group hierarchy level created in preliminary step [Create Merchandise Category Hierarchy Level](#unique_11) [page ] 10) |  |  |
| 4. | Display details | Detail page open with tree structure. select Expand All to see the details. |  |  |
| 5. | Exit screen | Select Exit. | The Display Merchandise Category Hierarchy screen is displayed. |  |

### Delete Merchandise Category Hierarchy Level (Optional)

Purpose

This process step shows you how you delete the existing merchandise category hierarchy level. Before deleting merchandise category hierarchy level, you must delete merchandise category/hierarchy levels assignments by using tiles Maintain Merchandise Category (WG22) (for deleting Merchandise Category assignment to a Hierarchy Level) and Delete Hierarchy Level - Merchand. Cat. Hier. (CLWP) (for deleting Merchandise Category Hierarchy level assignments).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Log onto the SAP Fiori launchpad as Master Data Specialist - Product Data (Retail) |  |  |
| 2. | Access the app | Open Delete Hierarchy Level - Merchand. Cat. Hier. (CLWP) app. | The Delete Hierarchy Level - Merchand. Cat. Hier. (CLWP)Initial screen is displayed. |  |
| 3. | Provide input values | On the initial screen, make the following entries and select ENTER:Hierarchy Level: <XXXXXXXXX> (Enter the material group hierarchy created in preliminary step [Create Merchandise Category Hierarchy Level](#unique_11) [page ] 10. |  |  |
| 4. | Delete | Select Delete and select Yes. | Class type 026: Hierarchy level < XXXXXX > deleted message is displayed. |  |

Result

Merchandise category hierarchy deleted.

### Reclassification of Retail Material (Optional)

Purpose

This process step shows you how you Change existing article and merchandise category assignments within merchandise. The reclassification function allows you to change your merchandise category hierarchy, including the objects assigned to the hierarchy (articles and variants). Changes are necessary for the following reasons,

Articles were accidentally assigned to incorrect merchandise categories when they were created.

Articles identified as being 'specialties' in a merchandise category should be assigned to a suitable merchandise category. For example, high-quality cheeses in the Dairy products merchandise category might be reassigned to a new Specialties merchandise category.

A merchandise category or merchandise category hierarchy level that is too large and no longer manageable is to be split in two. Some articles or merchandise categories in the old hierarchy level are reassigned to the new one.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Log onto the SAP Fiori launchpad as Master Data Specialist - Product Data (Retail) |  |  |
| 2. | Access the app | Open Reclassify Article - Merchandise Category (WRCR) app. | The Reclassification of a Retail material screen is displayed. |  |
| 3. | Test run without updates | On the initial screen, make the following entries and select Execute:Material Number: <XXXXXXXXX>Note Select material used in step [Create Single Article](#unique_12) [page ] 11 or/and [Create Generic Article with Variants](#unique_13) [page ] 24New Material Group: <XXXXXXXXX>Note Use material group created in step [Create Merchandise Category](#unique_25) [page ] 52Under Select Check options select check box for below entryChange purchase order itemsChange allocation table itemsUnder Update select check box for below entry (Checkbox are selected by default)Test run without updateLog | WW651 can be reclassified from <old Material Group> to level <New Material Group> message is displayed at the end of the tree structure.Note If the Material reclassification is not possible, message WW701 The assignment of object <Material> to level <New Material Group> could not be created.Select Back and message This material category cannot be reclassified is displayed |  |
| 4. | Reclassify Material | Uncheck the below entry and select Executeand select Yes in the performance queryTest run without update: | Under tree structure The following objects were checked and reclassified:Success message WW641 <Material> was reclassified from <old Material Group> to level <New Material Group> is displayedNote Any open Purchase orders or Allocation tables, the Material group gets updated with message WW647 Purchasing document <XXXXXXXXXX> in item 00010 will be changed |  |

### Create Reclassification Version for Merchandise Category or Merchandise Category Hierarchy Node

Purpose

This process step shows you how you can create a reclassification version for selected objects and a defined date. This means that the changes are not actually written to the database; the reclassification is merely simulated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Log onto the SAP Fiori launchpad as Master Data Specialist - Product Data (Retail) |  |  |
| 2. | Access the app | Open Create Reclassific. Version - Merchandise Category (WRC4) app. | The Create MG reclassification version: Initial screen is displayed. |  |
| 3. | Make entries | On the initial screen, make the following entries and select Execute:Change identification: <XXXXXXXXX>Description : <XXXXXXXXX>Material Group Objects From : <XXXXXXXX>To : <XXXXXXXX>Note Create Multiple Merchandise Category Hierarchy Levels by following step number [Assign Merchandise Category Hierarchy Level (Optional)](#unique_29) [page ] 59 to be used here.Material: <XXXXXXXXX>Immediately (today) : X(if the reclassification needs required from current date)Reclassicifiction planned for : <XXXXXXXXX>(Date from when the reclassification is required)Select Yes in performance query dialog box if any. |  |  |
| 4. | Select an object | Select Expand AllSelect an object to be moved, by positioning the cursor on the corresponding line and choose Objects.Note: You can select all the articles in a block in a single step by choosing Block | Hierarchical list of the merchandise categories and articles or merchandise category hierarchy node selected is displayed.The object gets selected and highlighted. |  |
| 5 | Reassign object | Reassign the selected objects by positioning the cursor on the node (target) and choose Reassign | The reassign is successful to the target node |  |
| 6 | Display consequences | Display the consequences of the reclassification on the planned date, by choosing Consequences.Select the first node and select Expand All. | Consequences of the reclassification is displayed.In case of any error, make the necessary changes in the Merchandise category or Merchandise Category Hierarchy Node and proceed further. |  |
| 7 | Display changes | Select Back.Choose Changes to get an overview of the changes that have resulted so far in this reclassification version. | The current assignment and planned assignment details are shown. |  |
| 8 | Save reclassification | Select Back.Select Save. | The reclassification tree has been saved message is displayed.The reclassification can now be changed or deleted or activated for a specific date. |  |

### Update Reclassification Version for Merchandise Category or Merchandise Category Hierarchy Node

Purpose

This process step shows you how you can update/activate the reclassification version already created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Log onto the SAP Fiori launchpad as Master Data Specialist - Product Data (Retail) |  |  |
| 2. | Access the app | Open Update Reclassific. Version - Merchandise Category (WRCV) app. | The Activate MG Reclassification Version Initial screen is displayed. |  |
| 3. | Make entries | On the initial screen, make the following entries and select Execute:Change Identification: <XXXXXXXXX>Enter the change identification created in step [Create Reclassification Version for Merchandise Category or Merchandise Category Hierarchy Node](#unique_33) [page ] 64Select Check options:Change purchase order items: XChange Allocation table items: XProcessing ParameterTest run without updates: XSelect Yes in performance query dialog box if any. |  |  |
| 4. | Consequences displayed | Select the first node and select Expand AllSelect Back and uncheck the Test run without update and select execute.Select Yes in query. | Hierarchical list/ Consequences of the merchandise categories and articles or merchandise category hierarchy node selected is displayed. |  |
| 5 | Update reclassification | Reclassification is updated successfully. | WW641 XXXXX was reclassified fromXXXXXXX to level XXXXXXX |  |

### Maintain Reclassification Version for Merchandise Category or Merchandise Category Hierarchy Node

Purpose

This process step shows you how you can update the reclassification version already created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Log onto the SAP Fiori launchpad as Master Data Specialist - Product Data (Retail) |  |  |
| 2. | Access the app | Open Maintain Reclassific. Version - Merchandise Category (WRC3) app. | The Change M G Reclassification Version Initial screen is displayed. |  |
| 3. | Make entries | On the initial screen, make the following entries and select Execute:Change Identification: <XXXXXXXXX>Enter the change identification created in step [Create Reclassification Version for Merchandise Category or Merchandise Category Hierarchy Node](#unique_33) [page ] 64To become valid from: <XXXXXXXXX> Enter the date from when the reclassification needs to be validSelect Yes in the Warning pop up | Hierarchical list of the merchandise categories and articles or merchandise category hierarchy nodes selected is displayed. |  |
| 4 | Make necessary changes | In case of any changes other than validity, follow the same steps (from 4 – 8) as in test procedure [Create Reclassification Version for Merchandise Category or Merchandise Category Hierarchy Node](#unique_33) [page ] 64 and follow [Update Reclassification Version for Merchandise Category or Merchandise Category Hierarchy Node](#unique_34) [page ] 65 step. | The reclassification changes should be successful. |  |

### Display Reclassification Version for Merchandise Category or Merchandise Category Hierarchy Node

Purpose

This process step shows you how you display the reclassification version created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Log onto the SAP Fiori launchpad as Master Data Specialist - Product Data (Retail) |  |  |
| 2. | Access the app | Open Display Reclassific. Version - Merchandise Category (WRC2) app. | The Display MG reclassification Version Initial screen is displayed. |  |
| 3. | Make entries | On the initial screen, make the following entries and select Execute:Change Identification: <XXXXXXXXX>Enter the change identification created in step [Create Reclassification Version for Merchandise Category or Merchandise Category Hierarchy Node](#unique_33) [page ] 64 |  |  |
| 4 | Display reclassification | Select the first node and select Expand All | Hierarchical list of the merchandise categories and articles or merchandise hierarchy nodes selected is displayed. |  |
| 5 | Check Log | Select Log | The status should be changed to already updated |  |

### Delete Reclassification Version for Merchandise Category or Merchandise Category Hierarchy Node

Purpose

This process step shows you how you can delete the version that already exists for a date, to create or activate a new reclassification version (change identification) for a date that has already been booked.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Log onto the SAP Fiori launchpad as Master Data Specialist - Product Data (Retail) |  |  |
| 2. | Access the app | Open Delete Reclassific. Version - Merchandise Category (WRC1) app. | The Delete M G Reclassificat ion Version Initial screen is displayed. |  |
| 3. | Make entries | On the initial screen, make the following entries and select Execute:Change Identification: <XXXXXXXXX>Note Use the Identification created in step no: [Create Reclassification Version for Merchandise Category or Merchandise Category Hierarchy Node](#unique_33) [page ] 64 | Hierarchical list of the merchandise categories and articles or merchandise hierarchy nodes selected is displayed. |  |
| 4. | Delete | Select the first node and select Expand AllChoose Delete treeChoose Yes in the confirmation prompt | Reclassification tree XXXXX deleted message is displayed |  |

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
- related-to :: [[15-retail-operations/products-for-retail-3i1-ae-test-script-sap-s-4hana-cloud-public-editio]]
- related-to :: [[15-retail-operations/test-script-characteristic-value-conversion-for-retail-7dl-ae-sap-s-4h]]
- related-to :: [[15-retail-operations/test-script-seasons-for-retail-6di-ae-sap-s-4hana-cloud-public-edition]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5FJ_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 119,051 chars in the whole document
