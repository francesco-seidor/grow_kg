---
id: 15-retail-operations/test-script-sap-s-4hana-cloud-public-edition-assortments-3i5-ae-945
title: "Test Script: SAP S/4HANA Cloud Public Edition - Assortments (3I5_AE) (3I5_S4CLD2608_BPD_EN_AE)"
description: "Test script for SAP S/4HANA Cloud scope item Assortments (3I5, AE): assortment modules, versions, product/store/DC assignment, plus optional steps."
cluster: 15-retail-operations
tags: [kb/retail-operations, topic/retail-sites-partners-and-assortments]
aliases: [3I5_S4CLD2608_BPD_EN_AE]
keywords: ["Retail Sites, Business Partners and Assortments", assortments, assortment modules, assortment module versions, product assignment, store assignment, distribution center assignment, listing conditions, test scripts, product replacement]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3I5_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-945
topic: 15-retail-operations/retail-sites-partners-and-assortments
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: SAP S/4HANA Cloud Public Edition - Assortments (3I5_AE) (3I5_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3I5_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Retail Sites, Business Partners and Assortments** in Retail Operations. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Assortments (3I5_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232852945)

[2 Prerequisites 3](#_Toc232852946)

[2.1 System Access 3](#_Toc232852947)

[2.2 Roles 3](#_Toc232852948)

[2.3 Master Data, Organizational Data, and Other Data 3](#_Toc232852949)

[2.4 Business Conditions 4](#_Toc232852950)

[3 Overview Table 6](#_Toc232852951)

[4 Test Procedures 7](#_Toc232852952)

[4.1 Create Assortment Module 7](#_Toc232852953)

[4.2 Create Assortment Module Version 8](#_Toc232852954)

[4.3 Assign Product to Assortment Module Version 9](#_Toc232852955)

[4.4 Assign Store to Assortment Module 11](#_Toc232852956)

[4.5 Assign Products to Distribution Center 12](#_Toc232852957)

[4.6 Replace Product in Assortment Module (Optional) 13](#_Toc232852958)

[4.7 Exclude Product from Store (Optional) 15](#_Toc232852959)

[4.8 Copy Store Assortment (Optional) 16](#_Toc232852960)

[4.9 Analyze Listing Overview (Optional) 17](#_Toc232852961)

## Purpose

Overview

Assortments are collections of articles for the purpose of defining which articles are relevant for which sites (stores and DCs). They're required to check whether an article can be procured by a site. In addition, assortments play an important role in other processes like point-of-sale outbound communication.

Assortments can be defined in terms of assortment modules that serve as article containers. Those assortment modules can be assigned to stores later. Furthermore, articles can be assigned to distribution centers directly without visible assortment modules in-between.

As a result of listing, assortment information is made available for operational usage in procurement. As a subtask, this includes generation of article master segments if necessary. The listing process and master data generation is automatically executed once an article-site relationship is defined by the user.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

|  |
| --- |
| Note In the retail industry, specific terms differ from the standard terms used in other lines of business. Therefore, SAP solutions which provide business processes across multiple lines of businesses may use terms for the corresponding business objects, transactions, and user interfaces that deviate from the retail terminology. For integration and reuse reasons, the SAP S/4HANA Cloud Public Edition, retail, fashion, and vertical business business may thus include different terms that refer to the same concept. SAP intends to harmonize the terminology in the future.The following terms are used synonymously in this document:Table 1:Standard Terms in Lines of BusinessSAP S/4HANA Cloud Public Edition, retail, fashion, and vertical business businessMaterial, productArticleMaterial group, product groupMerchandise categoryPlant, locationSite (as superordinate term) - store and distribution center (DC) |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

|  |  |
| --- | --- |
|  | Details |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Assortment Specialist - Retail | SAP_BR_ASSTMT_SPCLST_RFM | Assortments | SAP_RFM_SPT_ASSTMT_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Product | <Product 1> | Single article | Use a product that was created when executing the test script for Products for Retail (3I1). |
| Product | <Product 2> | Single article | Use a product that was created when executing the test script for Products for Retail (3I1). |
| Store | 3340 | Store 3340 AE |  |
| Store | <Store 2> | Retail store | Use a store that was created when executing the test script for Sites for Retail (3I3). |
| Distribution center | 3350 | DC 3350 AE |  |

For more information about creating master data objects, see the following scope items:

- Sites for Retail (3I3)
- Business Partners for Retail (5FH)
- Products for Retail (3I1)
- Product Taxonomies for Retail (5FJ)

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 3I3 - Sites for Retail | Sites must exist as a prerequisite for assigning them to an assortment module and consequently creating listing conditions.Note In the configuration activity Manage General Settings for scope item Assortments (3I5), the following configuration setting exists: Ignore Opening Date of Site. It specifies whether the system ignores or considers the opening date of stores and distribution centers when calculating the respective listing conditions. According to the default configuration setting, the system is supposed to consider the opening date. However, the system ignores the respective date when calculating the listing conditions if the value for the opening date is initial. Therefore, with respect to scope item Sites for Retail (3I3), ensure that you have defined the opening date for the stores and the distribution center, which you use in the test procedures. |
| 3I1 - Products for Retail | Products must exist as a prerequisite for assigning them to an assortment module and consequently creating listing conditions. |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Assortment Module](#unique_8) [page ] 7 | Assortment Specialist - Retail | Manage Assortment Modules (F4892) | Assortment module ASM1 is created along with the first version. |
| [Create Assortment Module Version](#unique_9) [page ] 8 | Assortment Specialist - Retail | Manage Assortment Modules (F4892) | The second version of assortment module ASM1 is created. |
| [Assign Product to Assortment Module Version](#unique_10) [page ] 9 | Assortment Specialist - Retail | Manage Assortment Modules (F4892) | Product <Product 1> is assigned to both versions of assortment module ASM1. |
| [Assign Store to Assortment Module](#unique_11) [page ] 11 | Assortment Specialist - Retail | Manage Assortment Modules (F4892) | Store 3340 is assigned to assortment module ASM1. |
| [Assign Products to Distribution Center](#unique_12) [page ] 12 | Assortment Specialist - Retail | Assign Products to Distribution Centers (F4543) | Products <Product 1> and <Product 2> are assigned to distribution center 3350. |
| [Replace Product in Assortment Module (Optional)](#unique_13) [page ] 13 | Assortment Specialist - Retail | Assign Product to Assortment Modules (F4894) | Product <Product 1> is terminated in assortment module ASM1 one day before the replacement date <Replacement Date> and product <Product 2> is assigned to assortment module ASM1 as of the replacement date <Replacement Date>. |
| [Exclude Product from Store (Optional)](#unique_14) [page ] 15 | Assortment Specialist - Retail | Assign Store to Assortment Modules (F4893) | Product <Product 1> is excluded from store 3340. |
| [Copy Store Assortment (Optional)](#unique_15) [page ] 16 | Assortment Specialist - Retail | Assign Store to Assortment Modules (F4893) | The store assortment of store 3340 is copied to store <Store 2>. |
| [Analyze Listing Overview (Optional)](#unique_16) [page ] 17 | Assortment Specialist - Retail | Listing Overview (F7745) | Listing conditions are displayed hierarchically. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

|  |
| --- |
| Note If you create multiple assortment modules by executing the Create Assortment Module test case, make sure to enter different values in the Assortment Module field and to use the various assortment modules accordingly in the subsequent test cases. |

### Create Assortment Module

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

### Create Assortment Module Version

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

### Assign Product to Assortment Module Version

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

### Assign Store to Assortment Module

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You assign a store to the assortment module created in process step [Create Assortment Module](#unique_8) [page ] 7. Together with the product assignment which you added in process step [Assign Product to Assortment Module Version](#unique_10) [page ] 9, your store assignment entails the first listing condition and initiates the generation of the product master data for the assigned store.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Assortment Specialist - Retail. |  |  |
| 2 | Access App | Open the Manage Assortment Modules (F4892) app. | The app opens and a list report with an empty result table appears. |  |
| 3 | Search for Assortment Module | Set the Assortment Module filter by entering ASM1 and choose Go. | The list report contains one line item with assortment module ASM1. |  |
| 4 | Navigate to Assortment Module | In the list report, click the line item of assortment module ASM1 to trigger the navigation. | The object page of assortment module ASM1 appears. |  |
| 5 | Start Store Assignment | In the table toolbar of the Assortment User s facet, choose Assign. | The Assign Assortment Users to Assortment Module dialog box appears. |  |
| 6 | Enter Required Data and Finish Store Assignment | In the Assign Assortment Users to Assortment Module dialog box, make the following entries and choose Assign:Assortment Users: 3340Assigned From: Leave as is (the default date is the current date)Assigned To: Leave empty for unlimited validity | The dialog box disappears, and the newly assigned assortment user appears in the Assortment Users facet.The line item contains the following data:Assortment User: 3340Assigned From/To: Current date - 31.12.9999. |  |

### Assign Products to Distribution Center

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

### Replace Product in Assortment Module (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You replace a product that reaches the end of its lifetime with a follow-on product in an assortment module. You can use this feature to meet the requirements related to the product lifecycle as well as the requirements related to your assortment.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Assortment Specialist - Retail. |  |  |
| 2 | Access App | Open the Assign Product to Assortment Modules (F4894) app. | The app opens and a list report with an empty result table appears. |  |
| 3 | Search for Product to Be Replaced | Set the Product filter by entering <Product 1>, set the Assigned to Module to Yes, and choose Go. | The list report contains one line item with product <Product 1>. |  |
| 4 | Navigate to Product | In the list report, click the line item of <Product 1> product to trigger the navigation. | The object page of the product appears. |  |
| 5 | Start Replacement | In the Product Assignments facet, select assortment module ASM1 and choose Replace Product in the table toolbar. | The Replace Product dialog box appears. |  |
| 6 | Enter Required Data and Finish Replacement | In the Replace Product dialog box, make the following entries and choose Replace Product:Follow-On Product: <Product 2>Valid From: <Replacement Date>. | The dialog box disappears. In the Product Assignments facet, the valid-to date changes, and the line item of assortment module ASM1 contains the following data:Assigned To: <Replacement Date> - 1 day |  |
| 7 | Check Follow-On Product | Navigate back to the initial list report and repeat test steps 3 and 4 for product <Product 2>. | The object page of product <Product 2> appears.In the Product Assignments facet, the new line item of assortment module ASM1 contains the following data:Assigned From: <Replacement Date>Assigned To: 31.12.9999. |  |

### Exclude Product from Store (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can exclude a product from an assortment module for a certain store. Thus, the product cannot be procured by the store any longer which also implies that the store does not continue selling the product. You can use this feature to react to certain requirements, for example, if a product is not running well in a store or if the store is subject to certain restrictions (for example, this can be the case if the store is not allowed to sell alcoholic beverages).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Assortment Specialist - Retail. |  |  |
| 2 | Access App | Open the Assign Store to Assortment Modules (F4893) app. | The app opens and a list report with an empty result table appears. |  |
| 3 | Search for Store | Set the Store filter by entering 3340 and choose Go. | The list report contains one line item with store 3340. |  |
| 4 | Navigate to Store | In the list report, click the line item of store 3340 to trigger the navigation. | The object page of the store appears. |  |
| 5 | Navigate to Assigned Assortment Module | In the Store Assignments facet, click the line item of assortment module ASM1 to trigger the navigation. | The object page of assortment module ASM1 appears. |  |
| 6 | Exclude Product | In the Assigned Products facet, select the line item of product <Product 1>, and choose Exclude in the table toolbar. | Product <Product 1> is removed from the Assigned Products facet and appears in the Excluded Products facet. |  |

### Copy Store Assortment (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You copy an existing assortment of a store to another store. A typical use case for copying an existing assortment is the opening of a new store. Thus, you can initially equip the new store with the assortment of a similar store.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Assortment Specialist - Retail. |  |  |
| 2 | Access App | Open the Assign Store to Assortment Modules (F4893) app. | The app opens and a list report with an empty result table appears. |  |
| 3 | Search for the Store to Copy From | Set the Store filter by entering 3340 and choose Go. | The list report contains one line item with store 3340. |  |
| 4 | Start Copying Procedure | Select the line item of store 3340 and choose Copy Assortment. | The Copy Assortment dialog box appears. |  |
| 5 | Enter Required Data and Finish Copying Procedure | In the Copy Assortment dialog box, make the following entries and choose Copy Assortment:Target Store: <Store 2>Valid From: <Your Valid-From Date> | The new store <Store 2> is assigned to all assortment modules which match your valid-from date and to which store 3340 has already been assigned. This means that the assortment modules which terminate before the valid-from date are not copied from store 3340. |  |

### Analyze Listing Overview (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process, you can display listing conditions such as validity periods, listing source, assortment module, assortment module version, promotion and allocation table.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Assortment Specialist - Retail. |  |  |
| 2 | Access App | Open Listing Overview (F7745) app. | Listing Overview screen is displayed. |  |
| 3 | Enter the Details | Enter the below data:Product: <Product 1>Site: 3340Choose Go. | Listing conditions are displayed. |  |

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
- related-to :: [[15-retail-operations/sites-for-retail-3i3-ae-test-script-sap-s-4hana-cloud-public-edition-9]]
- related-to :: [[15-retail-operations/test-script-business-partners-for-retail-5fh-ae-sap-s-4hana-cloud-publ]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3I5_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 33,781 chars in the whole document
