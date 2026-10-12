---
id: 15-retail-operations/products-for-retail-3i1-ae-test-script-sap-s-4hana-cloud-public-editio
title: "Products for Retail (3I1_AE) - Test Script, SAP S/4HANA Cloud Public Edition (3I1_S4CLD2608_BPD_EN_AE)"
description: "Test script for scope item 3I1 Products for Retail (AE): creating retail article master data of all article types, info records, interfaces, discontinuation."
cluster: 15-retail-operations
tags: [kb/retail-operations, topic/retail-articles-and-merchandise-categories]
aliases: [3I1_S4CLD2608_BPD_EN_AE]
keywords: ["Retail Articles, Merchandise Categories and Seasons", retail article master, single article, generic article variants, sales set, display article, product group reference article, packaging article, service article, purchasing info records]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3I1_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-941
topic: 15-retail-operations/retail-articles-and-merchandise-categories
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Products for Retail (3I1_AE) - Test Script, SAP S/4HANA Cloud Public Edition (3I1_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3I1_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Retail Articles, Merchandise Categories and Seasons** in Retail Operations. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Products for Retail (3I1_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Products for Retail (3I1_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 4](#_Toc232852767)

[1.1 Retail Article Master Data 5](#_Toc232852768)

[1.2 Article Types 5](#_Toc232852769)

[2 Prerequisites 7](#_Toc232852770)

[2.1 System Access 7](#_Toc232852771)

[2.2 Roles 7](#_Toc232852772)

[2.3 Master Data, Organizational Data, and Other Data 8](#_Toc232852773)

[2.4 Additional Manual Configuration 9](#_Toc232852774)

[2.4.1 Monitor Message Using Application Interface Framework (AIF) 9](#_Toc232852775)

[2.5 Business Conditions 10](#_Toc232852776)

[2.6 Preliminary Steps 11](#_Toc232852777)

[2.6.1 Create Assortments 11](#_Toc232852778)

[2.6.1.1 Create Assortment Module 11](#_Toc232852779)

[2.6.1.2 Create Assortment Module Version 12](#_Toc232852780)

[2.6.1.3 Assign Product to Assortment Module Version 13](#_Toc232852781)

[2.6.1.4 Assign Store to Assortment Module 15](#_Toc232852782)

[2.6.1.5 Assign Products to Distribution Center 16](#_Toc232852783)

[2.6.2 Create Promotions 17](#_Toc232852784)

[2.6.2.1 Create Promotion 17](#_Toc232852785)

[2.6.3 Create Purchase Order 19](#_Toc232852786)

[2.6.3.1 Create Purchase Order Directly 19](#_Toc232852787)

[2.6.4 Create Allocation Table Manually 21](#_Toc232852788)

[2.6.5 Create Purchasing Info Record 22](#_Toc232852789)

[2.6.6 Manage Source List 24](#_Toc232852790)

[3 Overview Table 26](#_Toc232852791)

[4 Test Procedures 28](#_Toc232852792)

[4.1 Create Individual Articles 28](#_Toc232852793)

[4.1.1 Create Article Master Data 28](#_Toc232852794)

[4.1.1.1 Create Single Article 28](#_Toc232852795)

[4.1.1.2 Create Generic Article with Variants 41](#_Toc232852796)

[4.1.1.2.1 Additional features for Generic Article with Variants 55](#_Toc232852797)

[4.1.1.3 Create Sales Set 58](#_Toc232852798)

[4.1.1.4 Create Display Article 68](#_Toc232852799)

[4.1.1.5 Create Product Group Reference Article 77](#_Toc232852800)

[4.1.1.6 Create Packaging Article 80](#_Toc232852801)

[4.1.1.7 Create Service article 85](#_Toc232852802)

[4.1.1.8 Assign Serial Number Profile to an Article 93](#_Toc232852803)

[4.1.2 Maintain Purchasing Info Record 95](#_Toc232852804)

[4.1.2.1 Maintain Purchase Info Record Using Create Article Master App (MM41) 96](#_Toc232852805)

[4.1.2.2 Manage Purchasing Info Record App 97](#_Toc232852806)

[4.2 Mass Change of Article Master 98](#_Toc232852807)

[4.3 Mass Change of Purchasing Info Records 98](#_Toc232852808)

[4.4 Exchange Article Master Data using Interfaces 99](#_Toc232852809)

[4.4.1 Replicate Article Master Data to External System (Outbound Communication) 99](#_Toc232852810)

[4.4.1.1 Procedure: Define Selection Criteria in Pooled Mode (Option 1) 100](#_Toc232852811)

[4.4.1.2 Define Filter Criteria 101](#_Toc232852812)

[4.4.1.3 Replicate with Global Filter (Optional) 101](#_Toc232852813)

[4.4.1.4 Analyze Replication Logs 103](#_Toc232852814)

[4.4.1.5 Replicate with Manual Selection (Optional) 104](#_Toc232852815)

[4.4.2 Create / Update Article Master Data Using Inbound Interface 105](#_Toc232852816)

[4.4.2.1 Replicate Specific Data using Replication Model (Optional) 107](#_Toc232852817)

[4.4.2.2 Procedure : Direct Mode (Option 2) 108](#_Toc232852818)

[4.5 Delisting and Discontinuation 109](#_Toc232852819)

[4.5.1 Discontinue Article 109](#_Toc232852820)

[4.5.1.1 Client – Wide Article Discontinuation (Optional) 109](#_Toc232852821)

[4.5.1.2 Supplier Article Discontinuation (Optional) 110](#_Toc232852822)

[4.5.1.3 Delete Allocation Tables (Optional) 112](#_Toc232852823)

[4.5.1.4 Delete Purchase Order line item 113](#_Toc232852824)

[4.5.2 Monitor Status - Article Discontinuation (Optional) 114](#_Toc232852825)

[4.5.3 Display Discontinuation Status – Article (Optional) 115](#_Toc232852826)

[5 Appendix 117](#_Toc232852827)

[5.1 Process Integration 117](#_Toc232852828)

[5.1.1 Preceding Processes 117](#_Toc232852829)

[5.1.2 Succeeding Processes 117](#_Toc232852830)

## Purpose

Overview

The article is the central object for a retailer, touching all steps of the supply chain, starting with the procurement from an external supplier, to distribution center handling, through selling in the store to customers. To support all these processes, data at various levels is needed, including basic data (different units of measure with dimensions and Global Trade Item Numbers (GTIN), description in multiple languages, validity periods, and so on), purchasing data for external suppliers, sales data, point-of-sale data, and logistics data for distribution centers and stores. A sophisticated referencing and defaulting mechanism allows for efficient data maintenance for all relevant levels via the integrated article maintenance. Furthermore, mass processing can maintain article master data for sets of articles. Integration scenarios are available that allow the import of article master data and the distribution to satellite solutions. In addition to the single article, there are special article categories, such as:

- Generic article: an abstract header article. Generic articles have variants (sold to the consumer) that only differ from one another in certain characteristics values (such as colors or sizes) but typically are identical in most other data
- Structured article: comprised of several components, structured via a bill of material
- Sales set: a set of several articles that are bought individually by the retailer and sold together to the consumer (for example, a shirt with a matching tie)
- Displays: a set of articles that are bought together and sold individually, including special for presentation in the store

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

|  |
| --- |
| Note In the retail industry, specific terms differ from the standard terms used in other lines of business. Therefore, SAP solutions which provide business processes across multiple lines of businesses may use terms for the corresponding business objects, transactions, and user interfaces that deviate from the retail terminology. For integration and reuse reasons, the SAP S/4HANA Cloud Public Edition, retail, fashion, and vertical business business may thus include different terms that refer to the same concept. SAP intends to harmonize the terminology in the future.The following terms are used synonymously in this document:Table 1:Standard Terms in Lines of BusinessSAP S/4HANA Cloud Public Edition, retail, fashion, and vertical business businessMaterial, productArticleMaterial group, product groupMerchandise categoryPlant, locationSite (as superordinate term) - store and distribution center (DC) |

### Retail Article Master Data

An article is the smallest unit that can be ordered independently and cannot be split into further smaller units. Articles are generally ordered for a plant and sold. However, these are not always sold in the same form in which they are purchased.

The retail article master record contains the data required to manage an article. This data can be categorized as follows:

- Data of a descriptive nature such as flavor
- Data with a control function such as the article type

Besides this data, which can be directly maintained by the user, a retail article master record contains data that is automatically updated by the system, such as stock levels.

For each product, a retail article master record is created. In the retail article master record, the units of measure and dimensions (in which a article is traded) are assigned to the article.

### Article Types

Article types group together articles with the same attributes. During article creation, article type must be specified. The article type determines, for example

whether the article number can be assigned internally by the system or externally by the user.

Number range interval to which the article number belongs. Whether the stocks are managed on a value basis and/or on a quantity basis relevant article views for article.

The following article types are considered:

| Article Type | Description |
| --- | --- |
| HAWA | Trading goods |
| VERP | Packaging article |

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

|  |
| --- |
| Note In the retail industry, specific terms differ from the standard terms used in other lines of business. Therefore, SAP solutions which provide business processes across multiple lines of businesses may use terms for the corresponding business objects, transactions, and user interfaces that deviate from the retail terminology. For integration and reuse reasons, the SAP S/4HANA Cloud Public Edition, retail, fashion, and vertical business business may thus include different terms that refer to the same concept. SAP intends to harmonize the terminology in the future.The following terms are used synonymously in this document:Table 2:Standard Terms in Lines of BusinessSAP S/4HANA Cloud Public Edition, retail, fashion, and vertical business businessMaterial, productArticleMaterial group, product groupMerchandise categoryPlant, locationSite (as superordinate term) - store and distribution center (DC) |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

| System | Details |
| --- | --- |
| System | Accessible through SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | Log On |  |
| Master Data Specialist - Product Data (Retail) | SAP_BR_MD_SPCLST_ITEM_RFM | Master Data Specialist - Product Data (Retail) | SAP_BR_MD_SPCLST_ITEM_RFM |  |
| Configuration Expert - Business Network Integration | SAP_BR_CONF_EXPERT_BUS_NET_INT | Configuration Expert - Business Network Integration | SAP_BR_CONF_EXPERT_BUS_NET_INT |  |
| Assortment Specialist - Retail | SAP_BR_ASSTMT_SPCLST_RFM | Assortments | SAP_RFM_SPT_ASSTMT_PC |  |
| Promotion Specialist (Retail) | SAP_BR_PROMOTION_SPCLST_RFM | Retail Promotions | SAP_RFM_SPT_PROMOTION_PC |  |
| Allocator (Retail) | SAP_BR_ALLOCATOR_RETAIL | Allocation and Merchandise Distribution | SAP_BR_ALLOCATOR_RETAIL |  |
| Purchaser (Retail) | SAP_BR_PURCHASER_RFM | Retail Purchasing / Retail Sourcing and Contracting | SAP_RFM_SPT_PURCHASING_PC / SAP_RFM_SPT_SOURCING_PC |  |

|  |
| --- |
| Note Administrator - Data Replication business role has to be referenced when you use any app related to data replication framework such as Define Filter Criteria, Replication and so on. |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| SUPPLIER1 | 33213001 | Retail Non-Food Supplier AE |  |
| SUPPLIER2 | 33213002 | Retail Food Supplier AE |  |
| Material/Product group - Single Article | R1193001 | Frozen Fruit |  |
| Material/Product group - Generic Article | R1182001 | Yoghurt |  |
| Material/Product group - Display | R1182002 | Milk |  |
| Material/Product group - Sales set | R2121002 | Hair Care |  |
| Material/Product group - Display | R1202001 | Sweets |  |
| Material/Product group - Display | R7113001 | Warranty |  |
| Material/Product group - Display | R7112002 | Packaging |  |
| Reference DC | 3391 | Ref DC 3391 AE |  |
| Reference Store | 3392 | Ref Store 3392 AE |  |
| Sales Organization | 3310 | Dom. Sales Org |  |
| Distribution Channel | 10 | Direct Sales |  |
| Distribution Channel | 40 | Store Sales |  |
| Distribution Channel | 50 | Distribution |  |
| Purchasing Organization | 3310 | Purch. Org. 3310 |  |
| Company Code | 3310 | Company Code 3310 |  |
| Purchasing Group | 002 | Group 002 |  |
| Storage Location | 995A | Storage Loc. DC |  |
| MRP Controller | 001 | MRP Controller 001 |  |
| Store | 3340 | Store 3340 AE |  |
| Plant group | R_SITEGROUP_AE_01 | R_SITEGROUP_AE_01 | 3340/3341/3342/3343 and 3344 are the sites part of the plant group R_SITEGROUP_AE_01. Refer 3I3 - Sites for Retail Scope Item for more details. |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/c53aa9fc93df79eaf54273e773a3dade)

#### Monitor Message Using Application Interface Framework (AIF)

AIF enables you to monitor the inbound and outbound messages in the SAP S/4HANA Cloud Public Edition system. First, you need to assign recipients to the namespace and then users to the recipients.

Prerequisite

You must create a business role by using the template SAP_BR_CONF_EXPERT_BUS_NET_INT (Configuration Expert - Business Network Integration) consisting of the business catalog SAP_CA_BC_COM_CONF_PC (Communication Management - Message Monitoring Configuration) and assign this to the business user in the SAP S/4HANA Cloud Public Edition.

Use

Assign your business users to the recipients that were defined for your communication scenarios. Once the users are assigned, they can use the Message Dashboard (/AIFX/WDA_MSG_MONITOR) to monitor the interfaces and data messages they are responsible for.

Procedure

1. Access the SAP Fiori launchpad and log on with your user.
2. Open the Assign Recipients to Users (F2949) app.
3. Add a user by selecting + on the bottom left of the Users Assigned to Recipients section.
4. Enter name / user ID in the Add User pop-up.
5. In Assign Recipients dialog, enter the Namespace as /CMDPR and Recipient Name as CMD_PRODUCT
6. Select Assign.

|  |
| --- |
| Note If the user is already added, then select the user who will be responsible for monitoring messages from the left panel and choose Assign. |

Result

Business users defined for your communication scenario is assigned to the recipients.

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 3I3 - Sites for Retail | Must be run before this test script. |
| 5FJ - Product Taxonomies for Retail | Must be run before this test script. |

### Preliminary Steps

|  |
| --- |
| Note These preliminary steps are only applicable for test procedure [Delisting and Discontinuation](#unique_12) [page ] 109. This needs to be executed after the execution of all the test procedures till [Exchange Article Master Data using Interfaces](#unique_13) [page ] 99. Please create two separate articles for the following step [Create Single Article](#unique_14) [page ] 28 (for single article)/[Create Generic Article with Variants](#unique_15) [page ] 41 (for generic article with variants), to test two types of discontinuations. Only these articles needs to be used in all the preliminary steps and also for the test procedure [Delisting and Discontinuation](#unique_12) [page ] 109. Use the master data specified in the [Master Data, Organizational Data, and Other Data](#unique_7) [page ] 8.All the preliminary steps are applicable for test procedure [Client – Wide Article Discontinuation (Optional)](#unique_16) [page ] 109Preliminary steps Create Assortment, Create Purchase order and Create purchasing Info record are only applicable for [Supplier Article Discontinuation (Optional)](#unique_17) [page ] 110 |

|  |
| --- |
| Note Listing ([Assign Store to Assortment Module](#unique_18) [page ] 15) must be done for all the sites as per the plant group used in [Master Data, Organizational Data, and Other Data](#unique_7) [page ] 8 section. |

.

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

You assign a store to the assortment module created in process step [Create Assortment Module](#unique_19) [page ] 11. Together with the product assignment which you added in process step [Assign Product to Assortment Module Version](#unique_21) [page ] 13, your store assignment entails the first listing condition and initiates the generation of the product master data for the assigned store.

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

#### Create Promotions

##### Create Promotion

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process a new promotion is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Promotion Specialist (Retail). |  |  |
| 2 | Access the App | Open Create Promotion (WAK1) app. |  |  |
| 3 | Enter Parameters | Enter below details:Promotion type: R331Choose Create Promotion. | Create Promotion: Fast Entry Overview screen is displayed. |  |
| 4 | Enter Parameters | Enter below details:Promotion Description : <Provide description>Planned Currency : AEDEnter below details in Validity : Sales sectionOn sale from : <Provide promotion sale start date>to: <Provide promotion sale end date>Enter below details in Fast Entry tabMaterial : R_1006SUn : PCPl.sls qty : 1000Choose EnterChoose Enter and continue if following warning message occurs-Material R_1006 PC is already included in other promotion(s) during sale periodOptional-You can follow below steps to maintain Promotion Price if requiredChoose Price Planning tab, maintain Sales Price 2,00 |  |  |
| 5 | Enter Parameters | Enter below details in Quantity planning tabAlloc. qty : 1000AUn: PCPl.sls qty: 1000 |  |  |
| 6 | Select Plant Groups | Select Plant groups tab.Choose Create Promo-Int . | Change Promotion :Local Plant Groups screen is displayed. |  |
| 7 | Enter Parameters | Enter below details in Plnt Assignmnt section:Customer: 3340Choose Enter. | Parameters details are provided. |  |
| 8 | Navigate back | Choose Back. | Create Promotion : Plant Groups Overview screen is displayed. |  |
| 9 | Select Header Data | Choose Header Data. | Create Promotion: Promotion Header -Planning screen is displayed. |  |
| 10 | Enter Parameters | Enter below details in Planning tabPurchasing Org : 3310Purch.grp : 001 | Parameters details are provided. |  |
| 11 | Navigate back | Choose Back. | Create Promotion: Plant Groups Overview screen is displayed. |  |
| 12 | Save Promotion | Choose Save. | Promotion xxxxxxxxxx created.Make a note of promotion. |  |

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
| 3 | Enter Purchase Order Data | Enter all of the necessary data:Order type: NB Standard POSupplier: <use your own Supplier>In Header section, on the Org. Data tab, make the following entries:Purchasing Org.: 3310Purchasing Group: 002Company Code: 3310In Items section,selectMaterial: <XXXXX>Note Use the article created in test procedures [Create Single Article](#unique_14) [page ] 28 / [Create Generic Article with Variants](#unique_15) [page ] 41.Plant: 3350Storage Location: 995A(Automatically determines)Quantity: 100Net Price: XX(Automatically determines) | Purchase order details provided. |  |
| 4 | Save the Purchase Order | Choose Save. | Purchase order is created.Make a note of the purchase order number. |  |

#### Create Allocation Table Manually

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

#### Manage Source List

Purpose

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser (Retail). | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Source Lists (F1859). |  |  |
| 3 | Maintain the Filter of Source List | In the filter, make the following entries:Material: <Product 1 / Product 2>Note Product created in step [Create Single Article](#unique_14) [page ] 28 and [Create Generic Article with Variants](#unique_15) [page ] 41Plant: 3350/3340Then choose Go. |  |  |
| 4 | Check the Source List | If there is one item that valid in the period, ignore the following steps, if it doesn’t have one item, then continue. |  |  |
| 5 | Create Source List | Choose Create. | The Source List screen is displayed. |  |
| 6 | Enter Detailed Data | Enter the values in the following fields:Material: <Product 1 / Product 2>Plant: 3350/3340Then choose ENTER. |  |  |
| 7 | Generate Source List | In the new line appeared under Source Lists area, enter following parameters and choose Enter:Valid From: for example, <today>Valid to: for example, <end of next year>Supplier: 33213001Purchase Organization: 3310 |  |  |
| 8 | Save the Source List | Choose Create. | The source list is saved. |  |

## Overview Table

This scope item consists of several process steps that are listed in the following table:

If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.

You can find all other apps not included on the homepage using the search bar.

If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose Settings > App Finder .

| Process Step | Business Role | App | Expected Results |
| --- | --- | --- | --- |
| Create individual articles | Master Data Specialist - Product Data (Retail)l | Create Article (MM41)/ Manage Product Master Data (F1602) | Individual articles is created. |
| Create article master data | Master Data Specialist - Product Data (Retail) | Create Article (MM41)/ Manage Product Master Data (F1602) | Article master data is created |
| [Create Single Article](#unique_14) [page ] 28 | Master Data Specialist - Product Data (Retail) | Create Article (MM41)/ Manage Product Master Data (F1602) | Retail article master data - single article is created. |
| [Create Generic Article with Variants](#unique_15) [page ] 41 | Master Data Specialist - Product Data (Retail) | Create Article (MM41)/ Manage Product Master Data (F1602) | Retail article master data - generic article is created. |
| [Create Sales Set](#unique_29) [page ] 58 | Master Data Specialist - Product Data (Retail) | Manage Product Master Data (F1602) | Retail article master data - sales set article is created. |
| [Create Display Article](#unique_30) [page ] 68 | Master Data Specialist - Product Data (Retail) | Create Article (MM41)/ Manage Product Master Data (F1602) | Retail article master data - display article is created. |
| [Create Product Group Reference Article](#unique_31) [page ] 77 | Master Data Specialist - Product Data (Retail) | Create Article (MM41)/ Manage Product Master Data (F1602) | Retail article master data - product group reference article is created. |
| [Create Packaging Article](#unique_32) [page ] 80 | Master Data Specialist - Product Data (Retail) | Create Article (MM41)/ Manage Product Master Data (F1602) | Retail article master data - packaging article is created. |
| [Create Service article](#unique_33) [page ] 85 | Master Data Specialist - Product Data (Retail) | Create Article (MM41)/ Manage Product Master Data (F1602) |  |
| [Assign Serial Number Profile to an Article](#unique_34) [page ] 93 | Master Data Specialist - Product Data (Retail) | Maintain Article (MM42)/ Manage Product Master Data (F1602) |  |
| [Maintain Purchasing Info Record](#unique_35) [page ] 95 | Master Data Specialist - Product Data (Retail)/Purchaser (Retail) | Create Material (MM01)/ Manage Purchasing Info Records (F1982) | Purchase Info record is created |
| [Maintain Purchase Info Record Using Create Article Master App (MM41)](#unique_36) [page ] 96 | Master Data Specialist - Product Data (Retail) | Create Material (MM01) |  |
| [Manage Purchasing Info Record App](#unique_37) [page ] 97 | Master Data Specialist - Product Data (Retail) | Manage Purchasing Info Records (F1982) |  |
| [Mass Change of Article Master](#unique_38) [page ] 98 |  |  |  |
| [Mass Change of Purchasing Info Records](#unique_39) [page ] 98 | Master Data Specialist - Product Data (Retail) | Mass Changes to Purchasing Info Records (F2667) |  |
| [Exchange Article Master Data using Interfaces](#unique_13) [page ] 99 | Administrator - Data Replication |  |  |
| [Replicate Article Master Data to External System (Outbound Communication)](#unique_40) [page ] 99 | Administrator - Data Replication |  |  |
| [Create / Update Article Master Data Using Inbound Interface](#unique_41) [page ] 105 | Administrator - Data Replication |  |  |
| [Delisting and Discontinuation](#unique_12) [page ] 109 |  |  |  |
| [Client – Wide Article Discontinuation (Optional)](#unique_16) [page ] 109 | Master Data Specialist - Product Data (Retail) | Discontinue Article (WRF_DIS_SEL) |  |
| [Supplier Article Discontinuation (Optional)](#unique_17) [page ] 110 | Master Data Specialist - Product Data (Retail) | Discontinue Article (WRF_DIS_SEL) |  |
| [Delete Allocation Tables (Optional)](#unique_42) [page ] 112 | Allocator (Retail) | Delete Allocation Table (WA09) |  |
| [Delete Purchase Order line item](#unique_43) [page ] 113 | Purchaser (Retail) | Change Purchase Order - Advanced (ME22N) |  |
| [Monitor Status - Article Discontinuation (Optional)](#unique_44) [page ] 114 | Administrator (Retail) | Monitor Status - Article Discontinuation (WRF_DIS_MON) |  |
| [Display Discontinuation Status – Article (Optional)](#unique_45) [page ] 115 | Administrator (Retail) | Display Discontinuation Status - Article (WSE8) |  |

## Test Procedures

This chapter describes procedures for each segment or process step that is part of this master record.

|  |
| --- |
| Note Field jumping through the tab button” still exist when using Fiori tiles to create article master. When user create article via Product Master App you will notice a Check button on the top right corner, which can be used to check for error entries instead of select Enter. |

### Create Individual Articles

#### Create Article Master Data

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

###### Additional features for Generic Article with Variants

Maintenance of Pricing Reference Article for Generic Article and Variants

Generic article and variants can save a lot of work while maintaining identical master data for article that only differ in one or two characteristics such as different sizes or colors; different flavor etc.

This simplified process can also be used for maintaining sales prices. This involves the variants of a generic Article inheriting the sales price of the generic Article or that of another variant. This is defined via pricing reference article in the retail article master data. If a variant inherits a sales price from another variant, you cannot create a separate sales price for it in a sales price calculation. A sales price can only be maintained for the pricing reference Article itself. In this way, it is possible for example to maintain the same sales price for all flavors from one variety.

Pricing Reference Article Maintenance

Whether and how a sales price is to be copied to a variant is controlled by the pricing reference article field in the master record for each variant. First, the pricing profile in the basic data of the generic Article must allow the price maintenance at variant level in general. The pricing reference Article can be specified in the basic data view and proposed to the sales view of the variant’s master data. On the sales view the data are defined at distribution chain level and can vary between the distribution chains.

|  |
| --- |
| Note The maintained data from the basic data view are relevant for the promotion maintenance. |

Change the created generic article.

Table 3: Case A: The pricing reference article specified in the basic data view of the variant’s master data

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data.Master Data Specialist - Product Data |  |  |
| 2 | Access the SAP Fiori App | Open Maintain Article (MM42) app. | The Change Article (Initial Screen) is displayed. |  |
| 3 | Enter Article Basic Data | In the Change Article (Initial screen)Material: Article number (R_<XXXXX>) |  |  |
| 4 | Choose Basic data View | Select Basic data and choose Continue. | Change Article R_<XXXXX> (Basic Data) is displayed. |  |
|  |  | In the Basic Data view, double-click on the field Pricing reference Article (“Pr.Ref.Matl”)The variant matrix is shown.Based on the pricing profile value = 1, the generic Article is proposed as pricing reference Article for each variantGo to the tab strip “Article number” and copy the variant number from the variants within the first rowGo to the tab Pr. Ref.Matl againDelete the entry within the row for the variants you just copiedCopy the variant numbers into the next linesGo back with the arrowChoose Save. | Article is saved with the changes is applied. |  |

Table 4: Case B: The pricing reference Article specified in the Sales view of the variant’s master data

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. |  |  |
| 2 | Access the SAP Fiori App | Open Change Article (MM42). app. | The Change Article (MM42) <XXXXX> (Initial Screen) is displayed. |  |
| 3 | Enter Article Basic Data | In the Change Article (Initial screen)Product: Article number (R_<XXXXX>) |  |  |
| 4 | Choose Sales view | Select Sales View and choose continue. |  |  |
|  |  | Select Switch Validity Area and enter Sales Organization, Distribution Channel and select Continue. |  |  |
|  |  | In the Sales view, choose the Variant Prices button.Go to the PrcRefMat tab.Choose the Maintain PR Mat button.In the first column, you see the pricing reference assignment. - In the case, the field is empty for a variant number, this means the variant is its own pricing Article . - In the case, there is a Article number assigned (1st column), this means, this Article number is the pricing reference Article for the variant number maintained in the 2nd column.Changes of the assignment could be done in general in the following way:Choose the Characteristics buttonChoose the characteristic which is the Variety characteristicChoose the Characteristic Values button.With the F4-help choose for each variety the variant that should be used as pricing reference Article .Choose the Adopt button.Choose the Adopt button again.The field pricing ref article is empty for the variant numbers you have chosen as pricing reference article via the F4 help. All other variants are having an pricing reference article assignmentIn the case, you would like to maintain new sales prices, define under tab strip Fin Prc the new prices. Press enter and you will see that the other flavors of the variety are getting the same price and no individual price maintenance per variant is possible.In the same screen select the checkbox „Save Sales Price Conditions“for saving the new sales price conditions, even no new sales price was definedChoose the Back .Choose save. |  |  |

##### Create Sales Set

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A sales set is a quantity of single article or variants of one or more generic article that can also be sold as separate article. As separate article, they have their own article number, sales price and a sales price condition. Inventory management is carried out at individual component level or grouped together with the header article on header article level. Sales sets are often used to boost sales. The components can belong to different merchandise categories and can have different tax rates. Only one tax rate can be assigned to the sales set.

The following procedure provides instructions for creating article master data. Apps available to you are dependent upon your assigned role, so two options are provided.

Prerequisite

You must complete the previous procedure, [Create Single Article](#unique_14) [page ] 28 / [Create Generic Article with Variants](#unique_15) [page ] 41, before you proceed with these procedures.

Procedure: Manage Product Master Data (Option 1)

In this procedure you can create product master data using the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data (Retail). |  |  |
| 2 | Access the SAP Fiori App | Open Manage Product Master Data (F1602) app. | The Manage Product Master Data (F1602) screen is displayed. |  |
| 3 | Choose Create New Product Master | In the Manage Product Master Data (F1602) view, click Create button and select Sales Set Article from the list. | The Create Master Data Record screen is displayed. |  |
| 4 | Enter Data for Mandatory Fields | In the Master Data Record sub-screen make the following entries:Product Number: for example,Z …Note You either enter any external alphanumeric ID, and that ID must start with an alphanumeric character, or if you provide no entry, the system automatically assigns a numeric ID.For more information about product number, see the previous Article Type and Number Ranges section.Product Type: Trading Goods(HAWA)Product Group: R2121002/Hair CareNote On entering product group the reference product field is auto populated from the reference article maintained for the Product group.Description: <any description> |  |  |
| 5 | Choose OK | In the Manage Product Master view, choose OK. | The Manage Product Master view is displayed. |  |
| 6 | In General Information Descriptions | In the Manage Product Master > General Information > Descriptions view, screen, choose Create. | Description in default language (for example, English) is already populated. |  |
| 7 | Enter Descriptions Data | In the Descriptions view, make the following entries:Language: for example, ArabicProduct Description: <your description> |  |  |
| 8 | In General Information | In the Manage Product Master > General Information > Base Unit of Measure view (Show more), make the following entry:GTINGTIN Category: IEWeightsGross Weight: <value>Net Weight: <value> |  |  |
| 9 | Choose Unit of Measure | In the Manage Product Master > General Information > Unit of Measure view, and select Show More. |  |  |
| 10 | Enter Weight Data | In the Weight section, enter the following:Gross Weight: for example, 0.2Net Weight: for example 0.18Weight Unit: for example, KG |  |  |
| 11 | Add an alternate Unit of Measure | In the Manage Product Master > General Information > Unit of Measure view, and select Create . | New order – Unit of Measure screen is displayed. |  |
| 12 | Enter Unit of Measure | In the General Information section, enter Unit of Measure, CRT |  |  |
| 13 | Enter Conversion factor | In the Conversion Factor section:Enter Units/Quantity – Alternate Unit of Measure <value> (for example 1)Enter Units/Quantity – Base Unit of Measure <value> (for example 10 |  |  |
| 14 | Enter Weight Data | In the Weight section, enter the following:Gross Weight: for example, 20Net Weight: Ideally this should get auto-filled by defaultWeight Unit: for example, KG |  |  |
| 15 | Enter GTIN for the alternate UOM | In the GTINs section, GTINs -unit of Measure press Create and assign GTIN category IE and press Enter |  |  |
| 16 | Return to Main Screen | Choose the back arrow to return to the main screen. | The Product Master screen appears. |  |
| 17 | Add Components | In the Manage Product Master > Components view, select Create. |  |  |
| 18 | Enter Components | In the Components section, enter the following:Product: for example, Single (for example, R_1050 & R_1051) or Variant of a generic article created aboveQuantity: for example, 1 |  |  |
| 19 | Choose Distribution Center Data | In the Product screen, choose Distribution center. | The Distribution Center tab is displayed. |  |
| 20 | Create Distribution Center | In the Distribution center view, choose Create. | The Distribution Center view opens. |  |
| 21 | Enter Distribution Center - General Information | In the General Information section, make following entries:Distribution Center: Distribution center number for example, 3391 (Reference DC comes by default, no need to enter explicitly and remain Non Editable)Loading Grp: for example, 0001 (Sales Data) | Similarly administrator can maintain for different DC. |  |
| 22 | Enter Distribution Center - MRP Data | In the MRP Data > MRP Data section, make following entries:Availability Check: for example, ST(Consider only stock)MRP Type: For example, R1 (Time-Phased Planning)MRP Controller: For example, 001/MRP Controller 001 |  |  |
| 23 | Enter Distribution Center - Lot-Size Data | In the MRP Data > Lot-Size Data section, make the following entry:Lot Sizing Procedure: for example EX/ Lot-for-lot order quantity |  |  |
| 24 | Enter Distribution Center - Procurement Data | In the MRP Data > Procurement section, make the following entry:Planned Delivery Time: for example, 3Goods Receipt Processing Time: for example, 1 |  |  |
| 25 | Return to Main Screen | Choose Apply to return to Product screen. | The Product screen is displayed. |  |
| 26 | Create Stores | In the Stores view, choose Create. | The Store view opens. |  |
| 27 | Enter Stores - General Information | In the General Information section, make following entries if not maintained:Store: Store number for example, 3392 (Reference Store comes by default, no need to enter explicitly and remain Non Editable)Negative Stock Allowed in Plant: X | Similarly administrator can maintain for different stores. |  |
| 28 | Enter Stores - Sales Data | In the Sales Data section make following entry:Loading Grp: for example, 0001(Crane) |  |  |
| 29 | Enter Stores - MRP Data | In the MRP Data > MRP Data section, make following entries:Availability Check: for example, ST/Consider only stockMRP Type: For example, RF/Replenish with dyn.TargetStock(Dynamic Target Stock gets calculated at runtime during the planning run from forecast sales value ) |  |  |
| 30 | Enter Stores - Procurement Data | In the MRP Data > Procurement section, make the following entry:Planned Delivery Time: for example, 3Goods Receipt Processing Time: for example, 1 |  |  |
| 31 | Return to Main Screen | Choose Apply to return to Product screen. | The Product screen is displayed. |  |
| 32 | Save Your Data | Choose Create. | System message is displayed. that object is saved.As a next step,You need to maintain purchasing Info record. For more information, see section [Maintain Purchasing Info Record](#unique_35) [page ] 95.You can change or maintain or update the article created above, via Maintain Article (MM42) app. |  |

Procedure: Create Article (Option 2)

In the procedure you can create article using Create Article (MM41) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data (Retail). |  |  |
| 2 | Access the SAP Fiori App | Open Create Article (MM41) app. | The Create Article (MM41) (Initial Screen) displays. |  |
| 3 | Enter Article Basic Data | In the Create Article (MM41) (Initial screen)Material: Article number (R_<XXXXX>)Material type: Trading Goods/HAWA Trading GoodsMaterial Group: (R2121002/Hair Care)Material Category: Sales Set/10 Sales Set |  |  |
| 4 | Choose Views | Select Basic data, Basic data 2 , Sales, Logistics DC, Logistics Store & POS views and choose Continue. | Create Article … (Basic Data) is displayed. |  |
| 5 | Enter Basic Data | From Create Article ...(Basic Data), on the Basic data tab, enter a Article description (short text). |  |  |
| 6 | Enter Basic Data | In the Unit of measure/EANs/dimensions section, enter the following: (All the below should ideally get filled automatically (only except EAN Category) from the Reference Article, but if you need to maintain any deviation then you can go ahead and maintain)Base Unit of Measure (PC)Gross Weight (<value>)Unit of Weight (KG)Net Weight (<value>)EAN Category (IE - Instore EAN (int. assignment possible))Alternate Unit of Measure (CAR)Maintain conversion factor for the alternate UOM:Number <Value>Lower-level unit (PC)Select Order Unit and Delivery Unit radio button for the Alternate UOM i.e. CAR in this case. |  |  |
| 7 | Enter Basic Data | From the Basic data tab enter the descriptions for the following: (All the below should ideally get filled automatically from the reference article, but if you need to maintain any deviation then you can go ahead and maintain)In Grouping section:Division 00In Internal logistics data:Purchasing Group 002/Group 002Supply Source (4 - Stock Transfer Before Standard)GenItemCatGroup (NORM)Loading Group (0001/Crane)Transportation Group (0001/On pallets)Variable Order Unit (1/Active)In General Data:Tax Class (1- Full tax)Valuation Class (3100 – Trading goods)Country of Origin AEIn Content section:Net Contents <value>Gross Contents <value>Content Unit (KG)Comparison Price Unit (1)In Validity Section:Valid from: <date>Valid to: <date> (default 31.12.9999, cannot be maintained)In Shelf Life Data section:Remaining Shelf Life(0)Total Shelf Life(0)Period indicator(D)Storage %(0) | The system message “The EAN will be determined internally on the basis of the EAN category is displayed.” |  |
| 8 | Navigate to Go to Additional data in Basic Data View: | In Short Text View enter/check the description and language:Language ArabicMaterial Description <Value>In the Unit of Measure View maintain/check the following (for Alternate UOM):Gross Weight <value>Unit of Weight (KG)EAN (IE - Instore EAN (int. assignment possible))Then select Go to Main Data. | Basic Data screen displays. |  |
| 9 | Enter Basic Data | Select Components and navigate to Create Component Assignment to Set Article screen.Enter the Component such as a Single (for example, R_1050 & R_1051 ) or Variant of a generic articledetails with quantity and UOM (for example, PC) and then press Back. | Once the components and description are completed, you move to the next tab, Basic data 2 view. |  |
| 10 | Choose Views | Select Basic Data 2 View and choose Continue or Enter. | Create Article …(Basic data 2) view displayed. |  |
| 11 | Enter Sales Period | Enter Sales period for Stores and Distribution Channel.Sales Period: storeFor sales fromFor sales tillSales Period: distribution centerFor sales fromFor sales till |  |  |
| 12 | Go to Purchasing view | Select Purchasing tab. |  |  |
| 13 | Enter Organizational Levels Data | In Switch Validity Area, in the Area of Validity section, enter descriptions for the following:Purchasing Org. 3310/Purch. Org. 3310Supplier (33213001/Retail Non-Food Supplier AE)Choose Continue. |  |  |
| 14 | Enter Purchasing Data | On the Create Article : Purchasing screen, make the following entries:(All the below should ideally get filled automatically (only except Net Price) from the Reference Article, but if you need to maintain any deviation then you can go ahead and maintain)sPurchasing Group 002/Group 002Var. Order Unit (1/Active)Regular Supplier (X)Net Price (<value>) | As a next step, you need to maintain purchasing Info record. For more information, see chapter [Maintain Purchasing Info Record](#unique_35) [page ] 95.Note The maintenance of the purchasing inforecord / purchasing data is only relevant if the sales set is already purchased as a set and prepackaged by the supplierRegular Supplier value makes sense, only if the customer is operating in one country and has several suppliers for this article and one should be the preferred supplier. |  |
| 15 | Choose Views | Select Sales View and choose C ontinue or Enter. | Create Article …(Sales) view is displayed.. |  |
| 16 | Enter Organizational Levels Data | In Switch Validity Area, in the Area of Validity section, enter descriptions for the following:Sales Org. 3310/Dom. Sales OrgDistr. Channel (40 – Store Sales)Choose Continue. |  |  |
| 17 | Enter Sales Data | On the Create Article : Sales screen, make the following entries:(All the below should ideally get filled automatically (only except Item Category Group) from the Reference Article, but if you need to maintain any deviation then you can go ahead and maintain)F or Sales from <date>F or Sales to <date>Item Category Group (NORM)Cash Discount (X)PP det. Seq.(Purchase Price determination Sequence) (01/ Standard with price determination)SP det Seq. (Sales price Determination Sequence) (01/ Calculate SP from planned markup)Final Price (<value>)Save Calculated Price (X) | Repeat the same step 15 and 16 for maintaining Sales Area – 3310/50 (For DC)Admin can also maintain Sales Organization 3310 & Distribution Channel 10 for wholesale process.Note Purchase price determination sequence 02 is used in the case the sales set is not bought from the external supplier as a set article. That means the sales set is "created" within the distribution center. |  |
| 18 | Choose Views | Select Logistics DC View and choose continue/enter.Check for the below entries:In MRP Parameters:MRP Type: R1 (Time-Phased Planning)Lot Size: EX (Lot-for-lot order quantity)Safety Stock: <value> By default it is 0Rounding profile: RDYP/ Retail Dynamic Rounding ProfileIn MRP Controller/Replenishment Data:MRP Controller: 001/MRP Controller 001Planning Cycle: P01 (Order Day Monday)Planned Delivery Time: 5Supply Source: 1 (Standard)In General Control Parameters:Purchasing Group: 002/Group 002Tax Indicator: 1 (Full tax)Automatic PO: XAvailability Check: ST(Consider only Stock)In Physical Inventory/Goods Issue/ Picking/ Shipping section:Loading Group: 0001/CraneIn Procurement Data:Storage Location: 995A | Create Article …(Logistics DC) view is displayed.On the Create Article : Logistics DC screen, check the available entries. These are proposed based on the reference Article . Only changes must be maintainedRounding profile is a key that the system uses to adjust the order proposal quantity to deliverable units. |  |
| 19 | Navigate to MRP/Forecast Data inside Logistics DC View | In the MRP/Forecast View maintain or check for the below entries:In Procurement section:Procurement Type: F (External procurement)In Scheduling section:Schedule Margin key: 001In BOM explosion/dependent requirements section:In Control Data Section:Auto reset: XSelect Back . | Administrator is navigated back to the Logistics Dc view. |  |
| 20 | Navigate to Other logistics Data inside Logistics DC View | In the Other logistics Data View maintain or check for the below entries:In General Plant Parameter:Unit of Issue: CARIn Foreign trade data:Country/Region of Origin: AESelect Back. | Administrator is navigated back to the Logistics Dc view. |  |
| 21 | Choose Views | Select Logistics Store View and choose continue/enter.Check for the below entries:In MRP Parameters:MRP Type: RF/ Replenish with dyn.TargetStock(Dynamic Target Stock gets calculated at runtime during the planning run from forecast sales value )Safety Stock: <value> By default it is 0In Replenishment parameters section:Target Coverage: 5In the Forecast Parameters:Forecast Model: K/ Constant with smoothing factor adjustmentIn MRP Controller/Replenishment Data:Planned Delivery Time: 3Supply Source: 4 (Stock Transfer Before Standard)In General Control Parameters:Purchasing Group: 002/Group 002Tax Indicator: 1(Full tax)Automatic PO: XAvailability Check: ST/ Consider only stockNegative Stock: XIn Storage Data:Storage Location: 994A | Create Article …(Logistics Store) view is displayed.On the Create Article : Logistics Store screen, Check the available entries and do adjustments if necessary (For example. supply source) |  |
| 22 | Navigate to MRP/Forecast Data inside Logistics Store View | In the MRP/Forecast View maintain or check for the below entries:In Procurement section:Procurement Type: : F (External procurement)In the Number of periods required section:History Periods: 60Forecast Periods: 12In Control data section:Initialization: XTrack Limit: 4 (Value that specifies the amount by which the forcast valve may deviate from the actual value.)Auto reset: XModel Selection Procedure: 2 (Analytical model selection procedure)Select Back . | Administrator is navigated back to the Logistics Store view. |  |
| 23 | Navigate to Other logistics Data inside Logistics Store View | In the Other logistics Data View maintain or check for the below entries:In General Plant Parameter:Unit of Issue: PCIn Foreign trade data:Country/Region of Origin: AESelect Back. | Administrator is navigated back to the Logistics DC view. |  |
| 24 | Choose Views | Select POS View and choose continue or Enter.Enter Till receipt Text as mentioned below:Language Key: ArabicAlternate Unit: -PCTill receipt text for Unit: <value> | Create Article …( POS) view is displayed.Maintain POS Text for distribution chain: 3310 40Maintain if necessary the text in different languages. Select Additional Data . |  |
| 25 | Save Your Data | At the bottom right of the display, choose Create to save your data. | The Create Article (Initial Screen) displayed.The sales set is created and saved.As a next step:You can change or maintain or update the article created above using Maintain Article (MM42) app. |  |

##### Create Display Article

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A display is a quantity of single article or variants of one or more generic article that are generally put together by the manufacturer. Examples of this include a display of chocolate in various flavors. A display is purchased as a single article and therefore has its own Article number, purchasing price and purchasing price conditions.

In the wholesale trade, is displayed. are purchased and sold, whereas in the retail trade, only the components are sold. For this reason, stock is managed at display level at the distribution center, and at component level at the store.

The following procedure provides instructions for creating article master data. Apps available to you are dependent upon your assigned role, so two options are provided.

Prerequisite

You must complete the previous procedure, Creating Single/Generic Article Master Data, before you proceed with this chapter.

Procedure: Manage Product Master Data (Option 1)

In this procedure you can create product master data using the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Product Master Data (F1602). | The Manage Product Master Data (F1602) screen is displayed. |  |
| 3 | Choose Create New Product Master | In the Manage Product Master Data (F1602) view, click Create and select Display Article from the list. | The Create Master Data Record screen is displayed. |  |
| 4 | Enter Data for Mandatory Fields | In the Master Data Record sub-screen make the following entries:Product Number: for example, Z.Note You either enter any external alphanumeric ID, and that ID must start with an alphanumeric character, or if you provide no entry, the system automatically assigns a numeric ID.For more information about Product Number, see the previous Article Type and Number Ranges section.Product Type: Trading Goods(HAWA)Product Group: for example, Sweets (R1202001)Note On entering product group the reference product field is auto populated from the reference article maintained for the Product group.Description: <any description> |  |  |
| 5 | Choose OK | In the Manage Product Master view, choose OK. | The Manage Product Master view is displayed. |  |
| 6 | Enter General Information | In the Manage Product Master > General Information > Unit of Measure view, make the following entry:GTIN Category: IE |  |  |
| 7 | Choose Create Description | In the Manage Product Master > General Information > Descriptions view, screen, choose Create. | Description in default language (for example, English) is already populated. |  |
| 8 | Enter Descriptions Data | In the Descriptions view, make the following entries:Language: for example, ArabicProduct Description: <your description> |  |  |
| 9 | Return to Main Screen | Choose the back arrow to return to the main screen. | The Product Master view is displayed. |  |
| 10 | Choose Base Unit of Measure | In the Manage Product Master > General Information > Unit of Measure view, and click on Show More. |  |  |
| 11 | Enter Weight Data | In the Weight section, enter the following:Gross Weight: for example, 0.5Net Weight: for example 0.48Weight Unit: for example, KG |  |  |
| 12 | Return to Main Screen | Choose the back arrow to return to the main screen. | The Product Master screen displayed. |  |
| 13 | Choose Reference values | In the Manage Product Master > Components view select Create. |  |  |
| 14 | Enter Components | In the Components section, enter the following:Product: for example, Single or Variant of a generic article created aboveQuantity: for example, 1 |  |  |
| 15 | Choose Distributions Chains | In the Product screen, choose Distribution Chains tab. | The Distribution Chains tab is displayed. |  |
| 16 | Choose Create | In the Distribution Chains tab, choose Create | Distribution Chains is displayed in edit mode. |  |
| 17 | Enter Distribution Chains Data | In Distribution Chains, make following entries:In the GENERAL DATA - General Information section:Sales Organization: 3310/Dom. Sales OrgNote The organization unit value is determined by what is offered in the value help.Distribution Channel: for example 40/ Store SalesDelivery Plant: <Plant number> (optional)In the GROUPING TERMS section:Item Category Group: for example, NORM |  |  |
| 18 | Return to Main View | Choose Apply to return to Product screen. | The Product screen is displayed. |  |
| 19 | Choose Purchasing Data | In the Product screen, choose Purchasing. | The Purchasing view is displayed. |  |
| 20 | Enter Purchasing Data | In the Purchasing Section enter Order Unit of Measure (PC). |  |  |
| 21 | Choose Distribution Center Data | In the Product screen, choose Distribution Center tab. | The Distribution Center tab is displayed. |  |
| 22 | Create Distribution Center | In the Distribution Center view, choose Create. | The Distribution Center view is displayed. |  |
| 23 | Enter Distribution Center - General Information | In the General Information section, make following entries:Distribution Center: Plant number for example, 3391 (Reference DC comes by default, no need to enter explicitly and remain non-editable)Loading Grp: for example, 0001/Crane (Sales Data) | Similarly Administrator can maintain for different DC. |  |
| 24 | Enter Distribution Center - MRP Data | In the MRP Data > MRP Data section, make following entries:Availability Check: for example, STMRP Type: For example, R1 (Time-Phased Planning)MRP Controller: For example, 001/MRP Controller 001 |  |  |
| 25 | Enter Distribution Center - Lot-Size Data | In the MRP Data > Lot-Size Data section, make the following entry:Lot Sizing Procedure: for example EX |  |  |
| 26 | Enter Distribution Center - Procurement Data | In the MRP Data > Procurement section, make the following entry:Planned Delivery Time: for example, 3Goods Receipt Processing Time: for example, 1 |  |  |
| 27 | Return to Main Screen | Choose Apply to return to Product screen. | The Product screen is displayed. |  |
| 28 | Create Stores | In the Stores view, choose Create. | The Store view is displayed. |  |
| 29 | Enter Stores - General Information | In the General Information section, make following entries if not maintained:Store: Store number for example, 3392 (Reference Store comes by default, no need to enter explicitly and remain non-editable)Negative Stock Allowed in Plant: X | Similarly Administrator can maintain for different stores. |  |
| 30 | Enter Stores - Sales Data | In the Sales Data section make following entry:Loading Grp: for example, 0001(Crane) |  |  |
| 31 | Enter Stores - MRP Data | In the MRP Data > MRP Data section, make following entries:Availability Check: for example, ST ( Consider only Stock)MRP Type: For example, RF/Replenish with dyn.TargetStock(Dynamic Target Stock gets calculated at runtime during the planning run from forecast sales value ) |  |  |
| 32 | Enter Stores - Procurement Data | In the MRP Data > Procurement section, make the following entry:Planned Delivery Time: for example, 3Goods Receipt Processing Time: for example, 1 |  |  |
| 33 | Return to Main Screen | Choose Apply to return to Product screen. | The Product screen is displayed. |  |
| 34 | Save Your Data | Choose Create. | System message is displayed. that object is saved.As a next step:You need to maintain purchasing Info record. For more information, see section [Maintain Purchasing Info Record](#unique_35) [page ] 95.You can change or maintain or update the article created above using Maintain Article (MM42) app. |  |

Procedure: Create Article (Option 2)

In this procedure you can create article master data using the Create Article (MM41) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data (Retail). |  |  |
| 2 | Access the SAP Fiori App | Open Create Article (MM41) app. | The Create Article (MM41) (Initial Screen) is displayed. |  |
| 3 | Enter Article Basic Data | In the Create Article (MM41) (Initial screen)Material: Article number (R_<XXXXX>)Material type: Trading Goods/HAWA Trading GoodsMaterial Group: Sweets (R1202001)Material Category: Display/12 Display |  |  |
| 4 | Choose Views | Select Basic data, Basic data 2 Logistics DC, Logistics Store & POS views and choose Continue. | Create Article (Basic Data) is displayed. |  |
| 5 | Enter Basic Data | From Create Article (Basic Data), on the Basic data tab, enter an Article description (short text). |  |  |
| 6 | Enter Basic Data | In the Unit of measure/EANs/dimensions section, enter the following: (All the below should ideally get filled automatically (only except EAN Category) from the Reference Article, but if you need to maintain any deviation then you can go ahead and maintain)Base Unit of Measure (PC)Gross Weight (<value>)Unit of Weight (KG)Net Weight (<value>)EAN Category (IE - Instore EAN (int. assignment possible))Alternate Unit of Measure (CAR)Maintain conversion factor for the alternate UOM:Number <Value>Lower-level unit (PC)Select Order Unit and Delivery Unit radio button for the Alternate UOM i.e. CAR in this case. |  |  |
| 7 | Enter Basic Data | From the Basic data tab enter the descriptions for the following: (All the below should ideally get filled automatically from the Reference Article, but if you need to maintain any deviation then you can go ahead and maintain)In Grouping Section:Division 00In Internal logistics data:Purchasing Group 002/Group 002Supply Source (4 - Stock Transfer Before Standard)GenItemCatGroup (NORM)Loading Group (0001 - Crane)Transportation Group (0001 – On Pallets)Variable Order Unit (1/Active)In General Data:Tax Class (2- Reduced tax)Valuation Class (3100 – Trading Goods)Country of Origin AEIn Validity section:Valid from: <date>Valid to: <date> (default 31.12.9999, cannot be maintained)In Shelf Life Data Section:Remaining Shelf Life(0)Total Shelf Life(0)Period indicator(D)Storage %(0) | The system message The EAN will be determined internally on the basis of the EAN category is displayed. |  |
| 8 | Enter Basic Data | Select Components and navigate to Create Component Assignment to Display Article screen.Enter the Component such as Single Article (for example, R_1050 & R_1051 ) or Variant of a Generic article details with quantity and UOM (for example, PC) and press Back. | Once the components and description are completed, you move to the next tab, Purchasing. |  |
| 9 | Choose Views | Select Basic Data 2 View and choose Continue or Enter. | Create Article …(Basic data 2) view is displayed. |  |
| 10 | Enter Sales Period | Enter Sales period for Stores and Distribution Channel.Sales Period: storeFor sales fromFor sales tillSales Period: distribution centerFor sales fromFor sales till |  |  |
| 11 | Choose Views | Select Purchasing View and choose continue/enter. | Create Article …(Purchasing) view displayed. |  |
| 12 | Enter Organizational Levels Data | In Switch Validity Area, in the Area of Validity section, enter descriptions for the following:P urchasing Org. 3310/Purch. Org. 3310Supplier (33213002/Retail Food Supplier AE)Choose Continue. |  |  |
| 13 | Enter Purchasing Data | On the Create Article: Purchasing screen, make the following entries:(All the below should ideally get filled automatically (only except Net Price) from the Reference Article, but if you need to maintain any deviation then you can go ahead and maintain)sPurchasing Group 002/Group 002Var. Order Unit (1/Active)Regular Supplier (X)Net Price (<value>) | As a next step, you need to maintain purchasing Info record. For more information, see chapter [Maintain Purchasing Info Record](#unique_35) [page ] 95.Note The maintenance of the purchasing inforecord / purchasing data is only relevant if the sales set is already purchased as a set and prepackaged by the supplier.Regular Supplier value makes sense, only if the customer is operating in one country and has several vendors for this article and one should be the preferred vendor. |  |
| 14 | Choose Views | Select Logistics DC View and choose continue/enter.Check for the below entries:In MRP Parameters:MRP Type: R1 (Time-Phased Planning)Lot Size: EX (Lot-for-lot order quantity)Safety Stock: <value> By default it is 0In MRP Controller/Replenishment Data:MRP Controller: 001/MRP Controller 001Planning Cycle: P01 (Order Day Monday)Planned Delivery Time: 5Supply Source: 1 (Standard)In General Control parameters:Purchasing Group: 002/Group 002Tax Indicator: 2 – Reduced taxAutomatic PO: XAvailability Check: ST – Consider only stockIn Physical Inventory/Goods Issue/ Picking/ Shipping section:Loading Group: 0001 - CraneIn Procurement Data:Storage Location: 995A | Create Article …(Logistics DC) view is displayed.On the Create Article : Logistics DC screen, check the available entries. These are proposed based on the reference Article . Only changes must be maintained |  |
| 12 a | Navigate to MRP/Forecast Data inside Logistics DC View | In the MRP/Forecast View maintain or check for the below entries:In Procurement Section:Procurement Type: : F (External procurement)In Scheduling Section:Schedule Margin key: 001In Control data Section:Auto reset: XSelect Back. | Administrator is navigated back to the Logistics Dc view. |  |
| 16 | Choose Views | Select Logistics Store View and choose Continue or Enter.Check for the below entries:In MRP Parameters:MRP Type: RF/Replenish with dyn.TargetStock(Dynamic Target Stock gets calculated at runtime during the planning run from forecast sales value )Safety Stock: <value> By default it is 0In ReplenishmentParameters section:Target Coverage: 5In the Forecast parameters:Forecast Model: K/ Constant with smoothing factor adjustmentIn MRP Controller/Replenishment Data:Planned Delivery Time: 1Supply Source: 4 (Stock Transfer Before Standard)In General Control Parameters:Purchasing Group: 002/Group 002Tax Indicator: 2 – Reduced taxAutomatic PO: XAvailability Check: ST – Consider only stockNegative Stock: XIn Procurement Data:Storage Location: 994A | Create Article …(Logistics Store) view is displayed.On the Create Article: Logistics Store screen, Check the available entries and do adjustments if necessary (for example supply source) |  |
| 17 | Choose Views | Select POS View and choose continue/enter.Enter Till receipt Text as mentioned below:Language Key: ENAlternate Unit: PCTill receipt text for Unit: <value> | Create Article …( POS) view is displayed.Maintain POS Text for distribution chain 3310 40Maintain if necessary the text in different language select Additional Data |  |
| 18 | Save Your Data | At the bottom right of the display, choose Create to save your data. | The Create Article (Initial Screen) appears.The is created and saved.As a next step:You can change or maintain or update the article created above using Maintain Article (MM42) app. |  |

##### Create Product Group Reference Article

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When creating a retail article master record, a merchandise category (product group) is assigned. If a product group reference article exists for the merchandise category the data from the Product group reference article is proposed in the new retail article master record (in the case no explicit reference article is specified). The product group reference article cannot be used in logistics processes. That means it is not possible to order this article. The article maintenance is easier with the help of the reference article

The same product group reference article can be used and assigned to several merchandise categories.

The following procedure provides instructions for creating product group reference article. Applications available to you are dependent upon your assigned role.

Prerequisite

Refer to the scope item Product Taxonomies for Retail (5FJ) from step 1 till step 5create merchandise category. In Step 4 there is an optional assignment of MG Ref. Material: R_REF01, which you have to skip and follow the step 5. to create merchandise category.

Procedure: Manage Product Master Data

In this procedure you can create product group reference article using the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data (Retail). |  |  |
| 2 | Access the SAP Fiori App | Open Manage Product Master Data (F1602) app. | The Manage Product Master Data (F1602) screen is displayed. |  |
| 3 | Choose Create New Product Master | In the Manage Product Master Data (F1602) view, select Create and select Product group reference article (30) from the list. | The Create Master Data Record screen is displayed. |  |
| 4 | Enter Data for Mandatory Fields | In the Master Data Record subscreen make the following entries:Product: for example,Z.Note You either enter any external alphanumeric ID, and that ID must start with an alphanumeric character, or if you provide no entry, the system automatically assigns a numeric ID.For more information about product number, see the previous Article Type and Number Ranges section.Product Type: Trading Goods(HAWA)Product Group: for example, <Enter the Mechandise Category created while executing test procedures in the scope item Product Taxonomies for Retail(5FJ)>Note On entering product group the reference product field is auto populated from the reference article maintained for the Product group.Description: <any description> | Note Merchandise category without reference article assignment is used. |  |
| 5 | Choose OK | In the Manage Product Master view, choose OK. | The Manage Product Master view is displayed. |  |
| 6 | Enter Division in Basic Data | In the Manage Product Master > General Information > Basic Data view, enter Division 00 |  |  |
| 7 | Choose Create Description | In the Manage Product Master > General Information > Descriptions view, screen, choose Create. | Description in default language (for example, English) is already populated. |  |
| 8 | Enter Descriptions Data | In the Descriptions view, make the following entries:Language: for example, ArabicProduct Description: <your description> |  |  |
| 9 | Choose Distribution Chain | Navigate to Manage Product Master > Distribution Chain view, select Create. | Distribution Chain screen is displayed |  |
| 10 | Enter Sales Org and Distribution Channel details | In the General Information > General Data section, enter the following:Sales Organization: for example, 3310/Dom. Sales OrgDistribution Channel : for example 40/Store SalesSelect Apply . | Naviagtes back to the Product Group reference Article screen.Repeat the same step 09 and 10 for maintaining Sales Area – 3310/50 and 3310/10. |  |
| 11 | Choose Distribution Centers | Navigate to Manage Product Master > Distribution Centers view, select Create. | Distribution Center screen is displayed |  |
| 12 | Enter Purchasing Data | Navigate to Purchasing view and enter the following:Purchasing Group: 002/Group 002Automatic Purchase Order Allowed: XTax indicator: 1 (Material 100%)Source of supply: 1 (Standard) |  |  |
| 13 | Enter MRP data | Navigate to MRP Data view and enter the following details:MRP type: R1 (Time-Phased Planning)MRP controller: 001/MRP Controller 001Planning Cycle: P01 (Order Day Monday)Availability Check : ST (Consider only Stock)Lot Size data:Lot Sizing Procedure EX/ Lot-for-lot order quantitySelect Apply. | Naviagtes back to the “Product Group reference Article” main screen |  |
| 14 | Choose Stores | Navigate to Manage Product Master > Stores view, and click on Create. | Store screen is displayed |  |
| 15 | Allow Negative Stocks | Navigate to General Information and select the flag for Negative Stock allowed. |  |  |
| 16 | Enter Purchasing Data | Navigate to Purchasing view and enter the followingPurchasing Group: 002/Group 002Automatic Purchase Order Allowed: XTax indicator: 1 (Material 100%)Source of supply: 4 (Stock Transfer Before Standard) |  |  |
| 17 | Enter Store Replenismenat Data | Navigate to Store Replenishment section and enter Target Range of Coverage for example, 5 Day |  |  |
| 18 | Enter MRP data | Navigate to MRP Data view and enter the following details:MRP type: RF (Replenish with dyn.Target Stock)Availability Check : ST (Consider only Stock)Select Apply. |  |  |
| 19 | Return to Main Screen | Choose the back arrow to return to the main screen. | The Product Master screen displayed. |  |
| 20 | Save Your Data | Choose Create. | System message is displayed that object is saved. |  |

##### Create Packaging Article

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Packaging articles are used to enclose or hold together the packaged goods. You can pack the packaged goods into or onto the packaging articles The packaging article can be a load carrier. The most important packaging articles are, for example, crates, boxes, containers, wire baskets, and pallets.

The following procedure provides instructions for creating packaging article.available to you are dependent upon your assigned role, so two options are provided.

Procedure: Manage Product Master Data (Option 1)

In this procedure you can create product master data using the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data (Retail). |  |  |
| 2 | Access the SAP Fiori App | Open Manage Product Master Data (F1602) app. | The Manage Product Master Data (F1602) screen is displayed. |  |
| 3 | Choose Create New Product Master | In the Manage Product Master Data (F1602) view, select Create and select Single Article from the list. | The Create Master Data Record screen is displayed. |  |
| 4 | Enter Data for Mandatory Fields | In the Master Data Record Subscreen make the following entries:Product Number: for example,Z.Note You either enter any external alphanumeric ID, and that ID must start with an alphanumeric character, or if you provide no entry, the system automatically assigns a numeric ID.For more information about Product Number, see the previous Article Type and Number Ranges section.Product Type: VERP (Packaging)Product Group: for example, R7112002/ PackagingNote On entering product group the reference product field is auto populated from the reference article maintained for the Product group.Description: <any description> |  |  |
| 5 | Choose OK | In the Manage Product Master view, choose OK. | The Manage Product Master view is displayed. |  |
| 6 | Enter General Information | In the Manage Product Master → General Information → Unit of Measure view, make the following entry:GTIN Category: IE |  |  |
| 7 | Choose Create Description | In the Manage Product Master → General Information → Descriptions view, screen, choose Create. | Description in default language (for example, English) is already populated. |  |
| 8 | Enter Descriptions Data | In the Descriptions view, make the following entries:Language: for example, ArabicProduct Description: <your description> |  |  |
| 9 | Return to Main Screen | Choose the back arrow to return to the main screen. | The Product Master view is displayed. |  |
| 10 | Choose Base Unit of Measure | In the Manage Product Master → General Information → Unit of Measure view, and click on Detail Button. |  |  |
| 11 | Enter Weight Data | In the Weight section, enter the following:Gross Weight: for example, 2Net Weight: for example 1.8Weight Unit: for example, KG |  |  |
| 12 | Return to Main Screen | Choose Apply button to come back to the main screen. | The Product Master screen appears. |  |
| 13 | Choose Sales | In the Product screen, choose Sales tab. | The Sales tab is displayed. |  |
| 14 | Choose Create | In the Sales tab, enter below entries:Allowed Packing Weight: <value> KGAllowed Packing Volume: <value> L |  |  |
| 15 | Choose Distribution Center Data | In the Product screen, choose Distribution center. | The Distribution Center tab is displayed. |  |
| 16 | Create Distribution Center | In the Distribution center view, choose Create. | The Distribution Center view is displayed. |  |
| 17 | Enter Distribution Center - General Information | In the General Information section, make following entries:Distribution Center: Plant number for example, 3391 (Reference DC comes by default, no need to enter explicitly and remain Non Editable)Loading Grp: for example, 0002 (Sales Data) | Similarly administrator can maintain for different DC. |  |
| 18 | Enter Distribution Center - MRP Data | In the MRP Data → MRP Data section, make following entries:Availability Check: for example, ST (Consider only stock)MRP Type: For example, ND (No planning) |  |  |
| 19 | Return to Main Screen | Choose Apply to return to Product screen. | The Product screen is displayed. |  |
| 20 | Create Stores | In the Stores view, choose Create. | The Store view is displayed. |  |
| 21 | Enter Distribution Center - General Information | In the General Information section, make following entries if not maintained:Store: Store number for example, 3392 (Reference Store comes by default, no need to enter explicitly and remain Non Editable)Negative Stock Allowed in Plant: X | Similarly administrator can maintain for different stores. |  |
| 22 | Enter Loading group under Sales Data | In the Sales Data section make following entry:Loading Grp: for example, 0001(Crane) |  |  |
| 23 | Enter Store - MRP Data | In the MRP Data → MRP Data section, make following entries:Availability Check: for example, ST Consider only stockMRP Type: For example, ND/No Planning |  |  |
| 24 | Return to Main Screen | Choose Apply to return to Product screen. | The Product screen is displayed. |  |
| 25 | Save Your Data | Choose Create. | System message is displayed that object is saved.As a next step, you can change or maintain or update the article created above, using Maintain Article (MM42) app. |  |

Procedure: Create Packaging Article (Option 2)

In the procedure you can create article using Create Article (MM41) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data (Retail). |  |  |
| 2 | Access the SAP Fiori App | Open Create Article (MM41) app. | The Create Article (MM41) (Initial Screen) displayed. |  |
| 3 | Enter Article Basic Data | In the Create Article (MM41) (Initial screen):Material: Article number (R_<XXXXX>)Material type: Packaging/VERP Packag-ingMaterial Group: R7112002/PackagingMaterial Category: Single Article/00 Single Article |  |  |
| 4 | Choose Views | Select Basic data, Basic Data 2, Logistics Dc, Logistics Store and choose Continue. | Create Article (Basic Data) is displayed. |  |
| 5 | Enter Basic Data | From Create Article (Basic Data), on the Basic data tab, enter a Article description (short text). |  |  |
| 6 | Enter Basic Data | In the Unit of measure/EANs/dimensions section, enter the following:(All the below should ideally get filled automatically (only except EAN Category) from the Reference Article, but if you need to maintain any deviation then you can go ahead and maintain)Base Unit of Measure (PC)Gross Weight (<value>)Unit of Weight (KG)Net Weight (<value>)EAN Category (IE - Instore EAN (int. assignment possible)) | Units of Measure/EAN’s/Dimensions subscreen displayed. Enter the measurements and dimensions of the article. |  |
| 7 | Enter Basic Data | From the Basic data tab enter the descriptions for the following: (All the below should ideally get filled automatically from the Reference Article, but if you need to maintain any deviation then you can go ahead and maintain)In Grouping section:Division: 00In Internal Logistics Data:GenItemCatGroup (VERP- Packaging)Transportation Group (0001/ On pallets)Loading Group (0002/Forklift)In General Data:Tax Class (1- Full tax)Valuation Class (3050- Packaging & Empties)In Validity section:Vaid from <date>Valid to <date>(default 31.12.9999, cannot be maintained)Press Enter. | Once you have made the entries, you move to the next tab, Basic Data 2.The system message “The EAN will be determined internally on the basis of the EAN category is displayed |  |
| 8 | Enter Basic Data 2 | In the Basic data 2 tab enter the descriptions for the following:Packaging Mat. Type - SP11(Car int./ext. closed)Allowed Packaging Weight <Value>Allowed Packaging Volume <Value>Excess Weight Tolerance <Value>Excess Volume Tolerance <Value> | Once you have made the entries, you move to the next tab, Logistics DC. |  |
| 9 | Choose Views | Select Logistics DC View and choose continue/enter.Check for the below entries:MRP Type: ND (No planning)Availability Check: ST(consider only stock)Purchasing Group: 002/Group 002Storage Location: 995A | Create Article (Logistics DC) view is displayed.On the Create Article : Logistics DC screen, check the available entries. These are proposed based on the reference article. Only changes must be maintained. |  |
| 10 | Choose Views | Select Logistics Store View and choose continue/enter.Check for the below entries:MRP Type: ND (No planning)Availability Check: ST(consider only stock)Purchasing Group: 002 / Group 002Storage Location: 994A | Create Article (Logistics Store VIew) view is displayed.On the Create Article : Logistics DC screen, check the available entries. These are proposed based on the reference article. Only changes must be maintained. |  |
| 11 | Save Your Data | At the bottom right of the display, choose Create to save your data. | The Create Article (MM41) (Initial Screen) is displayed.The packaging article is created and saved.As a next step, you can change or main-tain or update the article created above using Maintain Article (MM42) app. |  |

##### Create Service article

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You want so to create a service article which is of non-stock managed. For example, warranty.

Procedure: Option 1 - Manage Product Master Data (F1602)

In this procedure you can create product master data using the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data (Retail). |  |  |
| 2 | Access the SAP Fiori App | Open Manage Product Master Data (F1602) app. | Manage Product Master Data (F1602) screen is displayed. |  |
| 3 | Choose Create New Product Master | In the Manage Product Master Data (F1602) view, select Create button and select Single Article from the list. | The Create Master Data Record screen is displayed.. |  |
| 4 | Enter Data for Mandatory Fields | In the Master Data Record Subscreen make the following entries:Product Number: for example, Z …Note You either enter any external alphanumeric ID, and that ID must start with an alphanumeric character, or if you provide no entry, the system automatically assigns a numeric ID.For more information about Product Number, see the previous Article Type and Number Ranges section.Product Type: Non-Stock Material (NLAG)Product Group: for example, Warranty (R7113001)Note On entering product group the reference product field is auto populated from the reference article maintained for the Product group.Description: <any description> |  |  |
| 5 | Choose OK | In the Manage Product Master view, select OK. | The Manage Product Master view is displayed.. |  |
| 6 | In General Information à Descriptions | In the Manage Product Master > General Information > Descriptions view, screen, choose Create. | Description in default language (for example, English) is already populated. |  |
| 7 | Enter Descriptions Data | In the Descriptions view, make the following entries:Language: for example, ArabicProduct Description: <your description> |  |  |
| 8 | Choose Distributions Chains | In the Product screen, choose Distribution Chains tab. | The Distribution Chains tab is displayed. |  |
| 9 | Choose Create | In the Distribution Chains tab, choose Create | Distribution Chains opens in Edit Mode. |  |
| 10 | Enter Distribution Chains Data | In Distribution Chains, make following entries:In the GENERAL DATA - General Information section:Sales Organization: <Sales org number> 3310/Dom. Sales OrgNote The organization unit value is determined by what is offered in the value help.Distribution Channel: for example, 40/Store SalesCash Discount: XIn the GROUPING TERMS section:Item Category Group: for example, Non-stock Material (NLAG) |  |  |
| 11 | Return to Main View | Choose Apply to return to Product screen. | The Product screen is displayed.. | Repeat step 18-19 to maintain the other distribution chains e.g.3310/50 and 3310/10 . |
| 12 | Choose Distribution Center Data | In the Product screen, choose Distribution centers. | The Distribution Center tab is displayed.. |  |
| 13 | Create Distribution Center relevant data | In the Distribution centers view, choose Create. | The Distribution Center view is displayed.. |  |
| 14 | Enter Distribution Center - General Information | In the General Information section, make following entries if not maintained:In General Section:Distribution Center: DC for example, 3391 (Reference DC comes by default, no need to enter explicitly and remain Non-Editable) |  | The DC 3391 represents the reference distribution center for logistic data maintenance. DC 3391 is not an operational DC. Data maintained at reference DC level are inherited to all operational DC´s and only exceptions for individual DC´s must be maintained explicitly. |
| 15 | Enter Distribution Center - Sales Data | In the Sales Data section make following entry:Loading Grp: for example, 0001(Crane) |  |  |
| 16 | Enter Distribution Center - Purchasing data | In Purchasing Data:Purchasing Group: 002/Group 002Tax Indicator: 0 – Material 0% exemptSupply Source: 1 (Standard)Automatic Purchase Order allowed: X |  |  |
| 17 | Return to Main Screen | Choose Apply to return to Product screen. | The Product screen is displayed.. |  |
| 18 | Choose Stores Data | In the Product screen, choose Stores. | The Store tab is displayed.. |  |
| 19 | Create Stores | In the Stores view, choose Create. | The Store view is displayed.. |  |
| 20 | Enter Stores - General Information | In the General Information section, make following entries if not maintained:In General Section:Store: Store for example, 3392 (Reference Store comes by default, no need to enter explicitly and remain Non-Editable)Negative Stock Allowed in Plant: X |  | The store 3392 represents the reference store for logistic data maintenance. Store 3392 is not an operational store. Data maintained at reference store level are inherited to all operational stores and only exceptions for individual stores must be maintained explicitly. |
| 21 | Enter Stores - Sales Data | In the Sales Data section make following entry:Loading Grp: for example, 0001(Crane) |  |  |
| 22 | Enter Stores – Purchasing Data | In Purchasing Data:Purchasing Group: 002/Group 002Tax Indicator: 0 Material 0% exemptSupply Source: 4 (Stock Transfer Before Standard)Automatic Purchase Order allowed: X |  |  |
| 23 | Return to Main Screen | Choose Apply to return to Product screen. | The Product screen is displayed.. |  |
| 24 | Save Your Data | Choose Create. | System message displays that object is saved. | As a next step,You need to maintain purchasing Info record. For more information, see chapter[Maintain Purchasing Info Record](#unique_35) [page ] 95.You need to maintain Retail Pricing. For more information, see chapter [Succeeding Processes](#unique_48) [page ] 117 for scope item 3I4 - Sales Pricing for RetailYou can change or maintain or update the article created above, via Maintain Article (MM42) app. |

Procedure: Option 2 - Create single article via Create Article (MM41) app

In the procedure you can create article using Create Article (MM41) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data (Retail) . |  |  |
| 2 | Access the SAP Fiori App | Open Create Article (MM41) app. | The Create Article (MM41) (Initial Screen) is displayed. |  |
| 3 | Enter Article Basic Data | In the Create Article (MM41) (Initial screen)Material: Article number (R_<XXXXX>)Material type: Non-Stock Material (NLAG)Material Group: Warranty (R7113001)Material Category: Single material/00 Single materialSelect Enter. | If no specific reference article is maintained on the entry screen - data from the merchandise category reference article are proposed on the different screens. The data can be overwritten |  |
| 4 | Choose Views | Select Basic data, Basic data 2, Sales, Logistics Dc, Logistics Store & POS views and choose continue.. |  |  |
| 5 | Choose Characteristics Profile (optional) | If Characteristics profile screen is proposed, select Cancel. |  |  |
| 6 | Enter Basic Data | From Create Article ... (Basic Data), on the Basic data tab, enter an article description (short text). | Create Article … (Basic Data) is displayed. |  |
| 7 | Enter Basic Data | In the Unit of measure/EANs/dimensions section, enter the following:Base Unit of Measure (PC)Number of Lower-level <value>Unit of Weight (KG) | Subscreen: Units of Measure/EAN’s/Dimensions |  |
| 8 | Enter further Basic Data | In Groupings Section:Division 00In General Data:Supply Source (1 - Standard)GenItemCatGroup (NLAG - Non-stock Material)Loading Group (0001- Crane)Transportation Group (0001- On pallets)Tax Class (0 – Exempt, in VAT return)Valuation Class (YB00 - Non-Stock Mat. without ID)In Internal logistics data:Variable Order Unit: 1/ActiveIn Validity Section (Optional):Valid from: <date>Valid to: <date>(default 31.12.9999, cannot be maintained) | Once you have made the entries, Go to Additional data |  |
| 9 | Navigate to Go to Additional data in Basic Data View: | In Short Text View enter the description in second language:Language ArabicMaterial Description <Value>Then select Go to Main Data | Basic Data Screen is displayed |  |
| 10 | Choose Views | Select Basic Data 2 View and choose continue/enter. | Create Article … (Basic data 2) view is displayed. |  |
| 11 | Enter Sales Period | Enter Sales period for Stores and Distribution CenterSales Period: storeFor sale fromFor sale tillSales Period: distribution centerFor sale fromFor sale till |  |  |
| 12 | Choose Views | Select Purchasing View and choose continue/enter. | Create Article …(Purchasing) view is displayed. |  |
| 13 | Enter Organizational Levels Data | In Switch Validity Area, in the Area of Validity section, enter data for the following:Purchasing Org . 3310/Purch. Org. 3310Supplier (33213001/Retail Non-Food Supplier AE)Choose Continue. |  |  |
| 14 | Enter Purchasing Data | On the Create Article: Purchasing screen, make the following entries:(All the below data can be proposed from the business partner (supplier) (only except Net Price), but if you need to maintain any deviation then you can go ahead and maintain)Purchasing Group 002/Group 002Var. Order Unit (1/Active)Regular Supplier (X)Net Price (<value>) | As a next step, you need to maintain purchasing Info record. For more information, see chapter [Maintain Purchasing Info Record](#unique_35) [page ] 95.Disclaimer: Regular Supplier value makes sense, only if the customer is operating in one country and has several vendors for this article and one should be the preferred vendor. |  |
| 15 | Choose Views | Select Sales View and choose continue/enter. | Create Article …(Sales) view is displayed. |  |
| 16 | Enter Organizational Levels Data | In Switch Validity Area, in the Area of Validity section, enter values for the following:Sales Unit (PC)Sales Org. 3310/Dom. Sales OrgDistr. Channel (40/Store Sales)Select Continue. |  |  |
| 17 | Enter Sales Data | On the Create Article: Sales screen, make the following entries:(Few of the below should ideally get filled automatically from the Reference Article for example, item category group, cash discount.)Sales Unit ( e.g., PC in case of Sales area 3310/40 )For Sale from <date>For Sale to <date>Item Category Group (NLAG)Cash Discount (X)PP det. Seq.(Purchase Price determination Sequence) (01/ Standard with price determination)SP det Seq. (Sales price Determination Sequence) (01/ Calculate SP from planned markup)Final Price (<value>) | Repeat the same step 13 and 14 for maintaining Sales Area – 3310/50 (For DC)Administrator can also maintain sales organization 3310 and distribution channel 10 for wholesale process. |  |
| 18 | Choose Views | Select Logistics DC View and choose continue/enter.Check for the below entries:In MRP Controller/Replenishment Data:Supply Source: 1/StandardIn General Control Parameters:Purchasing Group: 002/Group 002Tax Indicator: 0/Material 0%Automatic PO: XIn Physical Inventory/Goods Issue/ Picking/ Shipping section:Loading Group: 0001/Crane | Create Article … (Logistics DC) view is displayed.to deliverable units.On the Create Article: Logistics DC screen, check the available entries. These are proposed based on the reference Article. Only changes must be maintainedRounding Profile is a Key that the system uses to adjust the order proposal quantity |  |
| 19 | Choose Views | Select POS View and choose continue/enter.Enter Till receipt Text as mentioned below:Language Key: ENAlternate Unit: PCTill receipt text for Unit: <value> | Create Article …(POS) view is displayed. | Maintain POS Text for distribution chain: 3310/40 (that is the relevant distribution chain for stores - in the case a different is proposed - the user should switch to this distribution chain)Maintain if necessary, the text in different languages. Press the Insert Row (+) button: to add a new entry. |
| 20 | Save Your Data | At the bottom right of the display, choose Create to save your data. | The Create Article (Initial Screen) is displayed.The Service Article is created and saved. | As a next step,You can change or maintain or update the article created above, via Maintain Article (MM42) app. |

##### Assign Serial Number Profile to an Article

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You want to create an article which is serial number managed.

The following procedure provides instructions for creating article relevant for Serial number master data. The SAP Fiori apps available to you are dependent on your assigned role. You can create single article in one of the following ways

Procedure: Option 1 – Assign Serial Number Profile to an Article (via Manage Product Master Data (F1602) app)

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data (Retail). | . |  |
| 2 | Access the SAP Fiori App | Open Manage Product Master Data (F1602) app. | The Manage Product Master Data (F1602) screen is displayed. |  |
| 3 | Choose Create New Product Master | In the Manage Product Master Data (F1602) view, select Create and select Single Article from the list. | The Create Master Data Record screen is displayed. |  |
| 4 | Search for the Product | Enter Article in the Product search field and choose go. | Search result gets displayed with the filtered article |  |
| 5 | Navigate to the article | Select filtered article to navigate inside | Product master screen appears with the article details and different tabs. |  |
| 6 | Navigate to the Distribution Centers tab | Select Distribution Centers tab to navigate to this section | User gets navigated to the Distribution center section |  |
| 7 | Navigate to the Reference DC details | Select Ref DC 3391 AE – 3391 section to navigate inside | Distribution Center screen appears with Ref DC 3391 AE -3391 details |  |
| 8 | Maintain Serial Number Profile | In the General Information section, enter Serial Number Profile as SRE2 (OBD SRN mandatory) and choose Apply. | User gets navigated to the Product Master screen |  |
| 9 | Navigate to the Stores tab | select Stores tab to navigate to this section | User gets navigated to the Stores section |  |
| 10 | Navigate to the Reference DC details | Select Ref Store 3392 AE – 3392 section to navigate inside. | Store screen appears with Ref Store 3392 AE -3392 details |  |
| 11 | Maintain Serial Number Profile | In the General Information section, enter Serial Number Profile as SRE2 (OBD SRN mandatory) and Choose Apply | User gets navigated to the Product Master screen. |  |
| 12 | Check entry | Select Check to check for the correctness of the article. | Check executes successfully. |  |
| 13 | Save the article | Choose Save. | Article gets saved. |  |

Procedure: Option 2 – Assign Serial Number Profile to an Article (via Maintain Article (MM42)) app

Follow the steps for creation of the article in the previous chapter for example, Refer to [Create Single Article](#unique_14) [page ] 28 to create single. Then follow the below steps to maintain serial number profile in an existing article.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data (Retail). |  |  |
| 2 | Access the SAP Fiori App | Open Maintain Article (MM42)app. | The Change Article (Initial Screen) is displayed.. |  |
| 3 | Enter Article Basic Data | In the Change Article (Initial screen)Material: Article number (R_<XXXXX>) |  |  |
| 4 | Choose Logistics: Distribution Center View | Select Logistics: Distribution Center and choose continue. | Change Article R_<XXXXX> (Logistics: Distribution Center) is displayed.. |  |
| 5 | Navigate to Other Logistics Data view | Select Other Logistics Data button in the Logistics DC screen | Change Article R_<XXXXX> (Other Logistics Data: DC) is displayed.. |  |
| 6 |  | In General Plant parameters section enter Serial No. Profile as SRE2 and press back button. |  |  |
| 7 | Choose Logistics: Store View | Select Logistics: Store and choose continue. | Change Article R_<XXXXX> (Logistics: Store) is displayed. |  |
| 8 | Navigate to Other Logistics Data view | Select Other Logistics Data button in the Logistics DC screen | Change Article R_<XXXXX> (Other Logistics Data: Store) is displayed.. |  |
| 9 |  | In General Plant parameters section enter Serial No. Profile as SRE2 and Select back.. |  |  |
| 10 | Save the changes | Choose save. | Article gets saved. |  |

#### Maintain Purchasing Info Record

Purpose:

There are below possibilities to maintain the purchase info record:

- Directly in the Article master – purchasing view (refer to details mentioned below in chapter [Maintain Purchase Info Record Using Create Article Master App (MM41)](#unique_36) [page ] 96.
- SAP FIORI Launchpad Manage Purchasing Info Records (F1982) mentioned below in the chapter [Manage Purchasing Info Record App](#unique_37) [page ] 97.

The other info records category (for example. consignment) cannot be maintained using article master. This is possible only using the Manage Purchasing Info Records (F1982) app.

The purchasing view is maintained before the listing view; otherwise no moving average price is available within the Article master until the first goods receipt.

##### Maintain Purchase Info Record Using Create Article Master App (MM41)

| Via Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data (Retail) |  |  |
| 2 | Access the SAP Fiori App | Open Create Article (MM41) app. | The Create Article (MM41) (Initial Screen) is displayed. |  |
| 3 | Enter Article Basic Data | In the Create Article (MM41) (Initial screen)Material: Article number (R_<XXXXX>)Material type: Trading Goods/HAWA Trading GoodsMaterial Group: Frozen Fruits (R1193001)Material Category: Single Article/00 Single ArticleSelect Enter. | Repeat the steps mentioned in chapter [Create Single Article](#unique_14) [page ] 28- Procedure: Option 1 - Create single article via Create Article (MM41) app from Step 1 till Step 8. |  |
| 4 | Choose Purchasing View | In the Create Material (Initial Screen), enter the below details:Purchasing Organization 3310Supplier Details (Vendor Details to be filled according to the article and suppliers dealing with the different kind of articles)Choose the Purchasing view and choose Continue. | Purchasing view is displayed |  |
| 5 | Enter details in Purchasing view | Check for the below entries:Order unit: <value>Var Order Unit: (1/Active)Purchasing Group: 002/Group 002Planned Delivery Time: (5)Confirmation Control: (0004/Inbound Delivery)Net Price: <value> |  |  |
| 6 | Choose InfoRecord Button | Create Info Record: General Data screen displays and choose Enter |  |  |
| 7 | Switch to Purchase Organization Data 1 | Create Info Record: Purchase Organization Data 1 Screen is displayedCheck for the below details:Planned Delivery Time: (5)Purchasing Group: 002/Group 002Standard Quantity: (1)Confirmation control: (0004/Inbound Delivery)GR based IV: (X)Net Price: <value> |  |  |
| 8 | Select Back | Select Back. | Article gets updated with the Purchasing Info Record and you navigate back to the Purchasing View.After this repeat the steps from Step 12 of [Create Single Article](#unique_14) [page ] 28 where you need to select the Sales View till Save the data of the Article master. |  |

##### Manage Purchasing Info Record App

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data (Retail). |  |  |
| 2 | Access the SAP Fiori App | Open Manage Purchasing Info Records (F1982) app | The Manage Purchasing Info Records (F1982) (Initial Screen) is displayed. |  |
| 3 | Choose Create button to create Info-record | Choose Create to create purchasing info record. | New Purchasing Info Record screen is displayed.Purchaser can maintain different kind of Inforecord via this app. For example, consignment, standard, sub-contracting and so on. |  |
| 4 | Enter Details in the Purchasing Info Record Screen | In the Purchasing Info Record screen, enter the below details:P urchasing Info Record category : (Standard)Supplier Details (Vendor Details to be filled according to the article and suppliers dealing with the different kind of articles)Material : (Article Master created above)Purchasing Organization 3310/Purch. Org. 3310Purchasing group 002/Group 002Delivery and Quantity:Delivery Time in Days: (5)Order Unit: (PC)Standard Order Quantity: <value>Confirmation Control: (Inbound Delivery)Conditions:Select Create. | Purchasing view is displayed. |  |
| 5 | Enter Conditions | Conditions screen open up with a Condition PPR0. Maintain Validity dates and Amount for the same.Valid From <dates>Valid To <dates>Amount <value>Select Save.Choose the Purchasing view and choose Continue. | Article gets updated with the purchasing info record. |  |

### Mass Change of Article Master

Refer to scope item Mass Load and Mass Maintenance for Product (1RM).

### Mass Change of Purchasing Info Records

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data (Retail). |  |  |
| 2 | Access the SAP Fiori App | Open Mass Changes to Purchasing Info Records (F2667) app. | The Mass Changes to Purchasing Info Records (F2667) (Initial Screen) is displayed. |  |
| 3 | Enter the filter details | Enter Supplier and/or Material and/or Purchasing Organization and/or Plant and/or Info Record Category and press Go button | Purchasing Info Records screen is displayed. |  |
| 4 | Choose checkbox to select the desired Info Record | Choose checkbox to select the desired Purchasing Info Record and choose Mass Edit. | Mass Edit subscreen is displayed.This subscreen displays the number of affected documents. |  |
| 5 | Replace or Clear or Keep Field values in the Mass Edit subscreen | Replace or Clear or Keep the values for the desired fields. | When user select the Replace Field Value then a new cell gets added, where user need to enter the desired value to be changed during mass change.When user select Clear Field Value or Keep existing Value then system should not add a new cell. |  |
| 6 | Select Apply Mass Changes | Select Apply Mass Changes | Apply Mass Changes pop up is displayed, where user need to pass Job Description |  |
| 7 | Enter Job Description | Enter Job Description and select Apply. | You see a success pop up for the job scheduled.You can navigate to view job list for the status of the job scheduled via View Job List. |  |
| 8 | Navigate to View Job List | Select View Job List from the Success Pop-up screen . | You will be navigated to the Application Log Screen with the Job description scheduled above. Here you can track for the completion of the job and its status.Once the status is finished, you can check for the changes in the Purchasing Info Record |  |

### Exchange Article Master Data using Interfaces

Prerequisite

Refer to Set Up Instructions for scope Item Products for Retail (3I1) for integration scenarios.

#### Replicate Article Master Data to External System (Outbound Communication)

Purpose

Product Master Outbound:

The purpose of this test case is to test Data Replication Framework Outbound (DRFOUT) to exchange the product master data from the SAP S/4HANA system to external systems.

The create/change of article master in SAP S/4 HANA system can happen in two modes (depending on the output mode (D – Direct or P – Pooled) set at the communication arrangement for outbound services):

- Pooled Mode
- Direct Mode

##### Procedure: Define Selection Criteria in Pooled Mode (Option 1)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

To execute this scope item, you must define a selection criterion for articles.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Configuration Expert - Business Network Integration |  |  |
| 2 | Access the App | Open Define Filter Criteria (F6519) app. | Define Filter Criteria (F6519) screen is displayed showing the list of defined replication models . |  |
| 3 | Select your replication model | Select your replication model from the Replication Model list and select Create to set a new filter criterion or select Change or Display, to change or display the existing criteria. | Create Filter Criteria or Change Filter Criteria screen is displayed accordingly. |  |
| 4 | Set filter criteria | Set you necessary filter criteria under Filter Criteria to Include Business Objects.Product : <value> Select Save. | The filter criteria is saved.The data to be replicated would be picked based on the set filter criteria. |  |

Result

You have defined the filter criteria.

##### Define Filter Criteria

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

To execute this scope item, you must define a selection criterion for articles.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as an Configuration Expert - Business Network Integration. |  |  |
| 2 | Access the App | Open Define Filter Criteria (F6519) app. | Define Filter Criteria (F6519) screen is displayed showing the list of defined replication models. |  |
| 3 | Select your replication model | Select your replication model from the Replication Model list and select Create to set a new filter criteri-on or select Change or Display, to change or display the existing criteria. | Create Filter Criteria or Change Filter Criteria screen is displayed accordingly. |  |
| 4 | Set filter criteria | Set you necessary filter criteria under Filter Criteria to Include Business Objects.Product : <value>Select Save. | The filter criteria is saved.The data to be replicated would be picked based on the set filter criteria. |  |

Result

You have defined the filter criteria.

##### Replicate with Global Filter (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you manually replicate initial set of data with respect to the global filter criteria defined in the [Define Filter Criteria](#unique_50) [page ] 101 chapter.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as an Configuration Expert - Business Network Integration. |  |  |
| 2 | Access the SAP Fiori App | Open Replicate by Replication Model (DRF_ADHOC_REPLICATION) app. | Replicate by Replication Model (DRF_ADHOC_REPLICATION) screen is displayed. |  |
| 3 | Select Replication Scope | Perform the following:Select the replication model, which was defined in the Create Communication Arrangements chapter of the Set-Up Instructions of Products for Retail (3I1)Select target system in the Select TargetSystem to which data must be replicated.Select Product as the business object under Select Business Objects to be Replicated.Select Initialization under Replication Mode. |  |  |
| 4 | Replicate | Choose Replicate. | Replication begins for the target system.All articles which adhere to the filter criteria defined in the [Define Filter Criteria](#unique_50) [page ] 101 chapter (For example, article starting with R*) are replicated and sent to the target system. |  |

##### Analyze Replication Logs

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you view the replication logs message summary for the initial replication that was supposed to be triggered using scheduled job while setting up the communication arrangement. Optionally the replication logs message summary of prior optional step can also be analyzed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as an Configuration Expert - Business Network Integration. |  |  |
| 2 | Access the App | Open Monitor Replication (DRF_FPM_OIF_MONITORING) app. | Monitor Replication (DRF_FPM_OIF_MONITORING) selection screen is displayed. |  |
| 3 | Select Monitoring Scope | Perform the following:Select your Replication Model, which was defined in the Create Communication Arrangement chapter of the Set-Up Instructions.The system populates default values for the following fields: Business Object: ProductDate From/Time FromDate To/Time ToLog Class: All LogsUser: *Replication Mode: All Modes You can change the values as required.Select Continue. | The replication log for the selection criteria is displayed. Following outcomes are expected based on the status of replication:Replication logs with Green LED will be displayed if replication happened successfully for the selected replication model.Replication logs with Yellow LED will be displayed if replication happened successfully but there are some warnings associated with replication of few or more products for the selected replication model.Replication logs with Red LED will be displayed if replication fails for the selected replication model. |  |

##### Replicate with Manual Selection (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can do manual replication by specifying individual objects only or by including the already defined filters along with specification of the individual objects.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as an Configuration Expert - Business Network Integration. |  |  |
| 2 | Access the SAP Fiori app | Open Replicate by Object Selection (DRF_MANUAL_REPLICATION) app. | Replicate by Object Selection (DRF_MANUAL_REPLICATION) screen is displayed. |  |
| 3 | Enter selection criteria values | Perform the following:Select the Business Object Type as Product.Select the target system to which data must be replicated under Target System Selection.Specify the filter criteria manually. For example, Product: R_1006 |  |  |
| 4 | (Optional) Apply object filter criteria | Select the Apply Object Filter Criteria to filter data based on the corresponding global filters.Apply Object Filter Criteria includes the global filter criteria, defined in the [Define Filter Criteria](#unique_50) [page ] 101 chapter, for the replication model linked with the target system.Note Business system is displayed under Target System Selection for selection. Refer to the Create Communication System section of the Set-Up Instructions to check the Business System specified for the communication system linked to your communication arrangement. | Note Set of the articles pertaining to both the global filter and the specified manual filter gets replicated to the selected target systems. |  |
| 5 | Replicate | Select Replicate. | Data is replicated. |  |

#### Create / Update Article Master Data Using Inbound Interface

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Product Master Inbound:

The Product Master Inbound SOAP service provider enables you to exchange product master records from the external systems to SAP S/4HANA Cloud Public Edition, using service interface.

Prerequisite

Refer to Set Up Instructions Products for Retail (3I1) for details on how to configure AIF message monitoring in SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Open the Postman tool | Download Postman via below link: [https://www.getpostman.com/downloads/](https://www.getpostman.com/downloads/)Install the package. | Choose suitable version based on your operation system, Windows 32-bit or Windows 64-bit.If you already have Postman installed, skip this step. |  |
| 2 | Create Collection | Choose New > Collection at the top left of the screen and enter Name: <Enter the name for your identification>Choose Create. |  |  |
| 3 | Create Request | Find the collection just created on the left side of the screen. Choose View more actions.Choose Add Request from the dropdown list and enter Request Name: <Enter the name for your identification>Choose Save to <collection name defined in previous step>. |  |  |
| 4 | Provide Article Master payload coming from the External System | SAP S/4HANA Cloud Public Edition solueion system gets an inbound payload with the Article Master information created/changed at the external system.This payload received from the external system using the communication arrangements at the SAP S/4HANA Cloud Public Edition system should be posted using POST method in POSTMANTo simulate the above said behaviour follow the steps mentioned below:Administrator (Retail) need to enter below mandatory details before execution of the payload from POSTMAN tool:URL (Please refer to the steps above in the preliminary steps to get the below URL):https://<subdomain>/sap/bc/srt/scs_ext/sap/productmdmbulkreplicaterequestParams – MessageID for e.g. 989C3E3A-4CD9-21CA-A200-12002B4CA1B4Basic Authorization: Provide username and passwordHeaders:KEY: Content-TypeValue: text/xmlBody: Select Raw radio button and paste the payload you wanted to execute for Article Master as XML (Please check Appendix Transmission Example in Set up guide for Payload details) |  |  |
| 5 | Send the transmission | Choose Send on the upper right of the screen. | Whether the transmission has been successfully received will be displayed at the button after choosing Send. |  |
| 6 | Log on | Log on to the SAP Fiori launchpad as an Configuration Expert - Business Network Integration. |  |  |
|  | Access the SAP Fiori App | Open Interface Monitor app. | The Interface Monitor screen is displayed with Result list of existing Application Logs. |  |
|  | Check for the persisted messages | Navigate to Monitor and Error Handling screen by clicking on the logs present for the Product Master and select the log in the CMD:Product Integration - /CMDPR and navigate to Product Replication from Client via Service - PRDREQ_IN/00001 for the article created above. | The Monitor and Error Handling screen is displayed.You will be able to see the details of the article master exchange triggered from the External System to the SAP S/4HANA Cloud Public Edition system. |  |

##### Replicate Specific Data using Replication Model (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you manually replicate initial set of data with respect to the specific filter criteria defined in the [Define Filter Criteria](#unique_50) [page ] 101 chapter.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as an Configuration Expert - Business Network Integration. |  |  |
| 2 | Access the SAP Fiori App | Open Replicate by Replication Model (DRF_ADHOC_REPLICATION) app. | Replicate by Replication Model (DRF_ADHOC_REPLICATION) screen is displayed. |  |
| 3 | Select Replication Scope | Perform the following:Select the replication model, which was defined in the Create Communication Arrangement chapter of the Set-Up Instructions.Select target system in the Select TargetSystem to which data must be replicated.Select Product as the business object under Select Business Objects to be Replicated.Select Initialization under Replication Mode. |  |  |
| 4 | Replicate | Click Replicate. | Replication begins for the target system. An articles which adhere to the filter criteria defined in the [Define Filter Criteria](#unique_50) [page ] 101 chapter (for example. Article R_1006) are replicated and sent to the target system. |  |

##### Procedure : Direct Mode (Option 2)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In direct mode, if an article master is created or changed in SAP S/4HANA Cloud Public Edition system for Retail, system automatically triggers an outbound XML for the creation or changes to an article in an external system.

Prerequisite

Create an article using Option 1 or Option 2 as mentioned in section create single article and then check for the outbound message exchange using the Interface Monitor app.

Please refer to Set Up Instruction of Products for Retail (3I1) for details on how to configure AIF message monitoring in SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator (Retail) in the sender system. |  |  |
| 2 | Access the App | Open the Interface Monitor app. | The Interface Monitor screen is displayed with result list of existing application logs. |  |
| 3 | Check for the persisted messages | Navigate to Monitor and Error Handling screen by clicking on the logs present for the Product Master and select the log in the CMD:Product Integration - /CMDPR and navigate to Product Replication to Client via Service - PRDREQ_OUT/00001 for the article created above. | The Monitor and Error Handling screen is displayed.You can view details of the article master exchange triggered from the SAP S/4HANA Cloud Public Edition system. |  |

### Delisting and Discontinuation

|  |
| --- |
| Note Refer the [Preliminary Steps](#unique_11) [page ] 11 before proceeding with Delist and Discontinuation test procedure. |

You can use this function to select articles that you want to discontinue. Enter the discontinuation type and processing type, and the system creates worklists accordingly.

You can select one of the following types of discontinuations:

- [Client – Wide Article Discontinuation (Optional)](#unique_16) [page ] 109
- [Supplier Article Discontinuation (Optional)](#unique_17) [page ] 110

#### Discontinue Article

##### Client – Wide Article Discontinuation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure You can disallow the procurement of articles. The article may no longer be procured or sold for the specified client. However, these sites may procure the article from other sources of supply. When you discontinue an article, the article is flagged for deletion. As a result, certain functions can no longer be carried out for it.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Master Data Specialist - Product Data (Retail). |  |  |
| 2 | Access the App | Open Discontinue Article (WRF_DIS_SEL) app | The Discontinue Article screen is displayed |  |
| 3 | Select the Area of Validity | Select Client-Wide Material Discontinuation Client-Wide |  |  |
| 4 | Enter required Data | In the Client-Wide Material Discontinuation (Initial screen) in Material Data tab and ExecuteMaterial: <Product 1 or Product 2> created in step [Create Single Article](#unique_14) [page ] 28 / [Create Generic Article with Variants](#unique_15) [page ] 41Discontinuation date: <XXXX> Enter the date from which the article is no longer to be purchased or soldSelect Enter. | Green LED; Go; OK indicator set on the Material Data tab |  |
| 6 | Follow – up Actions | The Material has Red indicator (Incorrect check)Select the Material and select Follow-Up ActionsSelect Yes in the Follow-Up Actions pop upSelect Continue in the information pop up | Follow-up actions carried out. Please check materials again. Message is displayed |  |
| 7 | Check material | Select Check | The selected items are checked, again message is displayed and the material has a yellow indicator (check partially correct) |  |
| 8 | Discontinue | Select DiscontinueSelect Continue in the information pop up | Materials selected are flagged for discontinuation message is displayed.Material has Green indicator (Correct check) |  |
| 9 | Save the Worklist | Select SaveEnter the,Worklist name: <XXXXXX>Select Continue in the Query Worklist Name popup | Worklist XXXXX “Worklist name” saved message is displayedNote down the Worklist number for future reference |  |

##### Supplier Article Discontinuation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can disallow the procurement of articles. The article may no longer be procured from a specific vendor for specific sites. However, these sites may procure the article from other sources of supply. When you discontinue an article, the article is flagged for deletion. As a result, certain functions can no longer be carried out for it.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Master Data Specialist - Product Data (Retail). |  |  |
| 2 | Access the App | Open Discontinue Article (WRF_DIS_SEL) app | The Discontinue Article screen is displayed |  |
| 3 | Select the Area of Validity | Select Supplier Material Discontinuation |  |  |
| 4 | Enter required Data | In the Supplier Material Discontinuation (Initial screen) in Supplier Data tabPurch. Organization: 3310Supplier: 33213001Ordering Blocking date: <XXXX> Enter the date from which the article is no longer to be purchasedSelect Enter. | Green LED; Go; OK indicator set on the Supplier Data tab |  |
| 5 | Enter Material Data | Select Material Data tab and enter the below data and select ExecuteMaterial: <XXXXXXX> created in step [Create Single Article](#unique_14) [page ] 28/[Create Generic Article with Variants](#unique_15) [page ] 41Select Execute. | Green LED; Go; OK indicator set on the Material Data tab |  |
| 6 | Follow – up Actions | The Material has Red indicator (Incorrect check)Select the Material and select Follow-Up ActionsSelect Yes in the Follow-Up Actions pop upSelect Continue in the information pop up. | Follow-up actions carried out. Please check materials again. Message is displayed |  |
| 7 | Check material | Select Check | The selected items are checked, again message is displayed and the material has a yellow indicator (check partially correct) |  |
| 8 | Discontinue | Select DiscontinueSelect Continue in the information pop up | Materials selected are flagged for discontinuation message is displayed.Material has Green indicator (Correct check) |  |
| 9 | Save the Worklist | Select SaveEnter the,Worklist name: <XXXXXX>Select Continue in the Query Worklist Name popup. | Worklist XXXXX “Worklist name” saved message is displayed |  |

|  |
| --- |
| Note For the errors with follow up activities not configured in the system, the user needs to manually do the activity. Follow the steps [Delete Allocation Tables (Optional)](#unique_42) [page ] 112 and [Delete Purchase Order line item](#unique_43) [page ] 113 to get the allocation table and purchase order line item deleted and proceed with discontinuation of article following step Discontinue Article to get the deletion flag set in the display discontinuation status. |

##### Delete Allocation Tables (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to delete the allocation table with activity status “1 - Not Active” or “4 - Done”.

|  |
| --- |
| Note You need to have Follow-On Documents - Purchase Orders/Stock Transfer Orders to be created completely for having Allocation Table in "4-Done" Status.Kindly note for Allocation Table with status as "4-Done" if ILM Object is Active then Allocation Table cannot be deleted using this App. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad asAllocator (Retail) |  |  |
| 2 | Access the app | Open Delete Allocation Table (WA09) app. |  |  |
| 3 | Give the inputs | Make the following entries:In Deletion for section:Alloc tab: 'x' selected by defaultIn organizat. data section:Purchasing organization: for example 3310Purchasing Group : 001In General Data section:Allocation table: Enter a new allocation table without a follow-on document (Create a new table manually through the Step Create Allocation Table Manually)In processing status section:Done: X selected by defaultSelect Execute | An allocation table that needs to be deleted is displayed. |  |
| 4 | Execute | Select the respective allocation table you want to delete. | The allocation table is accepted, and a popup message is displayed. |  |
| 5 | Delete | Select Delete Allocation Table. Pop up will display for confirmation “Do you want to delete the selected allocation table”Select YsXXX Allocation table with a total of XXX items deleted. | An allocation table is deleted. |  |

##### Delete Purchase Order line item

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can delete the purchase order line item.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Purchaser (Retail). |  |  |
| 2 | Access the App | Open Change Purchase Order - Advanced (ME22N) app | The Change Purchase Order screen is displayed |  |
| 3 | Select the Purchase order | Select Purchase Order > Other Purchase OrderPur. Order: <XXXXX>Enter the purchase order number created in step [Create Purchase Order Directly](#unique_24) [page ] 19Select Other Document |  |  |
| 4 | Delete the line item | Select the Material line item and select Delete from the below options.Select Yes in the Delete Items pop up. |  |  |
| 5 | Save the Purchase order | Select Save | Standard PO XXXXX changed |  |

#### Monitor Status - Article Discontinuation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You use this function to display and process worklists that you have created and saved in the Discontinuation Workbench. The worklist also serves as a discontinuation log for controlling discontinuation runs.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Master Data Specialist - Product Data (Retail). |  |  |
| 2 | Access the App | Open Monitor Status - Article Discontinuation (WRF_DIS_MON) app | The Monitor Status - Article Discontinuation screen is displayed |  |
| 3 | Worklist | Note You can enter selection criteria to select the worklists that you want to process. Your username is defaulted as a selection criterion.Enter the,Worklist Number: <XXXX> created in step [Client – Wide Article Discontinuation (Optional)](#unique_16) [page ] 109Select Execute |  |  |
| 4 | Validate the worklist | The system displays general information for the selected worklists and statistics about the items that have been checkedNote You can select and delete worklists, even if you have not yet completely processed these worklists. |  |  |

#### Display Discontinuation Status – Article (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step shows to how you can check the discontinuation status of a material.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Master Data Specialist - Product Data (Retail). |  |  |
| 2 | Access the App | Open Display Discontinuation Status - Article (WSE8) app | The Display discontinuation status of Material screen is displayed |  |
| 3 | Enter the required data | Enter the below data and Execute,Material: <XXXXXXX> created in step number [Create Single Article](#unique_14) [page ] 28 |  |  |
| 4 | Validate the deletion | Check if there is X mark in Deletion Flag Set field. |  |  |
| 5 | Reset status | Select the material line item for which the status needs to be resetSelect Reset StatusSelect Yes in the stop discontinuation pop up. | Order carried out without any difficulty. |  |

|  |
| --- |
| Note To reset the deletion flag for supplier, execute app Delete Purchasing Info Record (ME15) (role: SAP_BR_PURCHASER) |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

The following processes and conditions can proceed this process.

| Process | Business Condition |
| --- | --- |
| 3I3 - Sites for Retail | Create sites |
| 5FJ - Product Taxonomies for Retail | Product group, Characteristic values for Generic Articles |

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| 3I5 - Assortments | Create listing |
| 3I4 - Sales Pricing for Retail | Retail price management |

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
- related-to :: [[15-retail-operations/product-taxonomies-for-retail-5fj-ae-test-script-1079]]
- related-to :: [[15-retail-operations/test-script-characteristic-value-conversion-for-retail-7dl-ae-sap-s-4h]]
- related-to :: [[15-retail-operations/test-script-seasons-for-retail-6di-ae-sap-s-4hana-cloud-public-edition]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3I1_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 207,543 chars in the whole document
