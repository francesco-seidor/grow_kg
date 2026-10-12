---
id: 15-retail-operations/test-script-retail-promotions-637-ae-sap-s-4hana-cloud-public-edition
title: "Test Script: Retail Promotions (637_AE) - SAP S/4HANA Cloud Public Edition (637_S4CLD2608_BPD_EN_AE)"
description: "Test script for SAP S/4HANA Cloud Public Edition scope item Retail Promotions (637_AE): create promotion, supply source, prices, listing, allocation, jobs."
cluster: 15-retail-operations
tags: [kb/retail-operations, topic/retail-sales-pricing-and-promotions]
aliases: [637_S4CLD2608_BPD_EN_AE]
keywords: [Retail Sales Pricing and Promotions, retail promotions, promotion creation, supply source determination, promotion price activation, promotion sales price, article listing, allocation tables, allocation distribution, follow-on documents]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/637_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1142
topic: 15-retail-operations/retail-sales-pricing-and-promotions
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Retail Promotions (637_AE) - SAP S/4HANA Cloud Public Edition (637_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/637_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Retail Sales Pricing and Promotions** in Retail Operations. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Retail Promotions (637_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232857344)

[2 Prerequisites 4](#_Toc232857345)

[2.1 System Access 4](#_Toc232857346)

[2.2 Roles 4](#_Toc232857347)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232857348)

[3 Overview Table 6](#_Toc232857349)

[4 Test Procedures 8](#_Toc232857350)

[4.1 Manual Procedure 8](#_Toc232857351)

[4.1.1 Create Promotion 8](#_Toc232857352)

[4.1.2 Determine Supply Source 10](#_Toc232857353)

[4.1.3 Activate Prices 11](#_Toc232857354)

[4.1.4 Check Promotion Sales Price 12](#_Toc232857355)

[4.1.5 Perform Listing 13](#_Toc232857356)

[4.1.6 Allocate Distribution 14](#_Toc232857357)

[4.1.7 Allocate Table Generation 15](#_Toc232857358)

[4.1.8 Generate Follow-on Document 16](#_Toc232857359)

[4.1.9 Display Follow-On Document 17](#_Toc232857360)

[4.1.10 Retail Promotion Factsheet 18](#_Toc232857361)

[4.2 Periodic Background Job 19](#_Toc232857362)

[4.2.1 Schedule Promotion Supply Source Determination 19](#_Toc232857363)

[4.2.2 Schedule Promotion Price Activation 20](#_Toc232857364)

[4.2.3 Schedule Promotion Allocation Table Generation 22](#_Toc232857365)

[5 Appendix 25](#_Toc232857366)

[5.1 Process Integration 25](#_Toc232857367)

[5.1.1 Succeeding Processes 25](#_Toc232857368)

## Purpose

Overview

When planning a promotion, you need to define relevant factors, such as time periods, participating stores (a group of stores or all stores in a distribution chain), and included products. For these factors, among others, the planned promotional sales prices, sales and logistical units of measure, and procurement quantities must be specified. All this information is maintained via the object promotion. When operational follow-on activities are due, those can be triggered from the promotion object, including:

- Activating promotional sales prices
- Determining supply sources for the procurement
- Creating an allocation table that plans the procurement and distribution of merchandise between suppliers, distribution centers and stores
- Creating operational documents with reference to the allocation table, such as purchase orders for suppliers and stock transport orders for the procurement for the stores from the distribution centers (various process variants are supported)

For ease of maintenance, promotions can be created with reference to an existing promotion, and for a specific promotion type, which defaults in parameters like currency, price activation type, and various lead times.

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

| System | Details |
| --- | --- |
| System | Accessible through SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Promotion Specialist (Retail) | SAP_BR_PROMOTION_SPCLST_RFM | Retail Promotions | SAP_BR_PROMOTION_SPCLST_RFM |  |
| Allocator (Retail) | SAP_BR_ALLOCATOR_RETAIL | Allocation and Merchandise Distribution | SAP_BR_ALLOCATOR_RETAIL |  |
| Purchaser (Retail) | SAP_BR_PURCHASER_RFM | Purchasing | SAP_BR_PURCHASER_RFM |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | R_1006 | My Best Frozen Strawberries |  |
| Purchasing Organization | 3310 | Purch. Org. 3310 |  |
| Purchasing Group | 001 | Group 001 |  |
| Sales Organization | 3310 | Dom. Sales Org |  |
| Distribution Channel | 40 | Store Sales |  |
| Planned Currency | AED | UAE Dirham |  |
| Store | 3340, 3341 | Store 3340 AE, Store 3341 AE |  |
| Distribution Center | 3350 | DC 3350 AE |  |
| General Article | R_1003 | ChocolateVariants:R_1003001R_1003002R_1003003R_1003004R_1003005R_1003006R_1003007R_1003008R_1003009R_1003010R_1003011R_1003012R_1003013R_1003014 |  |
| Sales Set | R_1052 | My Best Blond Shampoo & ConditionerComponents: R_1051 and R_1050 |  |
| Promotion Type | R331 | Promotion Store |  |

## Overview Table

This scope item consists of several process steps that are listed in the following table:

If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.

You can find all other apps not included on the homepage using the search bar.

If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose Settings > App Finder .

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Promotion](#unique_7) [page ] 8 | Promotion Specialist (Retail) | Create Promotion (WAK1) | Promotion is created. |
| [Determine Supply Source](#unique_8) [page ] 10 | Promotion Specialist (Retail) | Execute Subsequ. Processing - Promotions (WAK5) | Supply source is determined. |
| [Activate Prices](#unique_9) [page ] 11 | Promotion Specialist (Retail) | Execute Subsequ. Processing - Promotions (WAK5) | Promotion price is activated. |
| [Check Promotion Sales Price](#unique_10) [page ] 12 | Promotion Specialist (Retail) | Determine Sales Prices (VKP2) | Promotion sales price are displayed. |
| [Perform Listing](#unique_11) [page ] 13 | Promotion Specialist (Retail) | Execute Subsequ. Processing - Promotions (WAK5) | Articles are listed for promotion. |
| [Allocate Distribution](#unique_12) [page ] 14 | Promotion Specialist (Retail) | Execute Subsequ. Processing - Promotions (WAK5) | Allocation distribution to stores. |
| [Allocate Table Generation](#unique_13) [page ] 15 | Promotion Specialist (Retail) | Execute Subsequ. Processing - Promotions (WAK5) | Allocation table is generated. |
| [Generate Follow-on Document](#unique_14) [page ] 16 | Allocator (Retail) | Maintain Allocation Table (WA02) | Follow-on document is generated. |
| [Display Follow-On Document](#unique_15) [page ] 17 | Purchaser (Retail) | Display Purchase Order - Advanced (ME23N) | Follow-on document is displayed. |
| [Retail Promotion Factsheet](#unique_16) [page ] 18 | Promotion Specialist (Retail) | Retail Promotion (S/4HANA) (F0336A) | Promotion details are displayed. |
| [Schedule Promotion Supply Source Determination](#unique_17) [page ] 19 | Promotion Specialist (Retail) | Schedule Promotion Supply Source Determination (F6443) | The supply source is determined for given Item/Promotion through application Job. |
| [Schedule Promotion Price Activation](#unique_18) [page ] 20 | Promotion Specialist (Retail) | Schedule Promotion Price Activation (F6441) | The Price is activated for a given Item/promotion through application Job. |
| [Schedule Promotion Allocation Table Generation](#unique_19) [page ] 22 | Promotion Specialist (Retail) | Schedule Promotion Allocation Table Generation (F6442) | The Price is activated for a given Item/promotion through application Job. |

## Test Procedures

This chapter describes procedures for each process step that belongs to this scope item.

### Manual Procedure

#### Create Promotion

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

#### Determine Supply Source

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process supply source is determined for the promotion.

|  |
| --- |
| Note Article should have been listed for DC 3350 and should have stock in DC 3350. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Promotion Specialist (Retail) |  |  |
| 2 | Access the App | Open Execute Subsequ. Processing - Promotions (WAK5) app. | Promo . Subsequent processing: Initial Screen is displayed. |  |
| 3 | Enter Parameter | Enter below details:Promotion : <Provide Promotion number>Choose Supply source determination . | Promo. subsequent processing: Supply Source Determin.screen is displayed. |  |
| 4 | Select Material | Select Material and Choose SS in column Chge SS | Promo. Subsequent processing: Supply Source Determin.screen is displayed. |  |
| 5 | Select Stores | Select all Stores and Choose SS Proposal. | Supplier and External Supplier are determined. |  |
| 6 | Save | Choose Save. | Promotion xxxxxxxxx saved message displayed. |  |

#### Activate Prices

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process price is activated for the promotion .

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Promotion Specialist (Retail) |  |  |
| 2 | Access the App | Open Execute Subsequ. Processing - Promotions (WAK5) app. | Promo. Subsequent processing: Initial Screen is displayed. |  |
| 3 | Enter Parameter | Enter below details:Promotion : <Provide Promotion number>Choose Price Activation | Promo. Subsequent processing: Price Activation screen is displayed. |  |
| 4 | Select Material | Select Material and Choose Activate. | Selection of Periods for Price Activations dialog box is displayed. |  |
| 5 | Choose Display Price Calculation | Choose Display price calculation. | Change Price Calculation screen is displayed. |  |
| 6 | Navigate back | Choose Back. | Promo. Subsequent processing: Price Activation screen is displayed |  |
| 7 | Save | Choose Save. | Promotion xxxxxxxxx saved message displayed. |  |

#### Check Promotion Sales Price

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process you can check promotion sales price.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Promotion Specialist (Retail) |  |  |
| 2 | Access the App | Open Determine Sales Prices (VKP2) app. | Price Overview : Initial screen is displayed. |  |
| 3 | Enter Parameter | Enter below details in Selection criteria section:Material : R_1006Sales Organization : 3310Distribution Channel: 40Plant..to: 3340, 3341Validity Period ..to : <Provide validity period given in created promotion>Check below flag in Organizational Level Selection section:Display distribution chain and plant/price list prices separatelyEnter below detail in Display section:List Group : BChoose Execute. | Sales Price Conditions from < Validity Period > to <Validity Period> screen is displayed. |  |
| 4 | Choose view | Choose Standard <-> Promotion. | The promotion and standard price is listed.The promotion sales price (ESP0) of material is displayed. |  |
| 5 | Change Layout | Choose Change Layout to change the display of Prices. | Prices is displayed as per changed layout. |  |
| 6 | Navigate to Home screen | Choose back till reaches Home screen | Home screen is displayed. |  |

Note:

|  |
| --- |
| Note If you work with generic materials you must enter * (star) after the material number to get the price changes on variant level. |

#### Perform Listing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process listing is performed and the stores will be listed for promotion.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Promotion Specialist (Retail). |  |  |
| 2 | Access the App | Open Execute Subsequ. Processing - Promotions (WAK5) app. | Promo. Subsequent processing: Initial Screen is displayed. |  |
| 3 | Enter Parameter | Enter below details:Promotion : <Provide Promotion number>Choose Listing. | Promo. Subsequent processing: Listing screen is displayed. |  |
| 4 | Perform Listing | Choose Listing button. | Information pop-up appears with message Listing successfully generated. |  |
| 5 | Verify Listing Status | Choose Continue and verify the Listing Status. | The Listing status is displayed as ‘ Y’. |  |
| 6 | Save | Choose Save. | Promotion xxxxxxxxx saved message is displayed. |  |

#### Allocate Distribution

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process a proposal for merchandise distribution to the stores are determined.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Promotion Specialist (Retail) |  |  |
| 2 | Access the App | Open Execute Subsequ. Processing - Promotions (WAK5) app. | Promo. Subsequent processing: Initial Screen is displayed. |  |
| 3 | Enter Parameter | Enter below details:Promotion : <Provide Promotion number>Choose Allocation Table | Promo. Subsequent processing: Active Allocation Table screen is displayed. |  |
| 4 | Select Material | Select Material and Choose Plant Data. | Promo. Subsequent processing: Site Quantities Overview screen is displayed. |  |
| 5 | Distribute quantity | Select Plant quantities tab.Choose Distribute qty evenly against Pld sales qty and plnd alloc. Q ty in Item section | Pl.sls qty and PlndAllQty columns is displayed the allocated quantities. |  |
| 6 | Save | Choose Save. | Promotion xxxxxxxxx saved message displayed. |  |

#### Allocate Table Generation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process allocation table is generated for the promotion.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Promotion Specialist (Retail). |  |  |
| 2 | Access the App | Open Execute Subsequ. Processing - Promotions (WAK5) app. | Promo. Subsequent processing: Initial Screen is displayed. |  |
| 3 | Enter Parameter | Enter below details:Promotion : <Provide Promotion number>Choose Allocation Table | Promo. Subsequent processing: Active Allocation Table screen is displayed. |  |
| 4 | Select Material | Select Material and Choose Plant qty. | Goods Receipt , Lead Time for Distribution Center dialog box is displayed. |  |
| 5 | Enter Parameter | Enter below details:GR lead time in distribution center: 2Press Enter | Document lines: Display messages dialog box is displayed.Allocation table generated.Make note of allocation table. |  |
| 6 | Choose Continue | Choose Continue in pop up. | Allocation table number is displayed in Alloc.Tab. column |  |
| 7 | Save | Choose Save. | Promotion xxxxxxxxx saved message displayed. |  |

#### Generate Follow-on Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process follow-on document is generated for the promotion.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as Allocator (Retail). |  |  |
| 2 | Access the App | Open Maintain Allocation Table (WA02) app. | Change Allocation Table : Initial Screen is displayed. |  |
| 3 | Enter Parameter | Enter below details:Allocation Table : <Provide Allocation Table>Navigate Menu > Allocation Table > Create follow-on docs > All Follow-On Documents . | Allocation Table Generation Follow - On Documents screen is displayed. |  |
| 4 | Select line items | Select all line items and Choose Generate Documents. | Follow-on document generated .Column Wrhs Order displays follow on documents.Column Expectation status displays in green.Make note of follow-on documents. |  |

#### Display Follow-On Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process follow-on document is displayed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Purchaser (Retail) |  |  |
| 2 | Access the App | Open Display Purchase Order - Advanced (ME23N) app. | Display Purchase Order - Advanced (ME23N) screen is displayed. |  |
| 3 | Access Return Purchase Order | Choose Other Purchase Order from Menu bar.Enter Pur. Order number and choose Other Document. | Purchase order document is displayed. |  |

#### Retail Promotion Factsheet

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process the retail promotion factsheet app is displayed all relevant information about your promotion in one place and enables you to navigate directly to related business objects.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Promotion Specialist (Retail) |  |  |
| 2 | Access the App | Open Retail Promotion (S/4HANA) (F0336A) app. | Retail Promotion (S/4HANA) (F0336A) screen is displayed. |  |
| 3 | Choose Go | Choose GoYou can select more filters through Adapt Filters beside Go | Details are displayed. |  |
| 4 | Select Promotion | Select Promotion and choose left arrow against Promotion. | Retail Promotion (S/4HANA) (F0336A) screen displayed with Promotion details. |  |
| 5 | Check details | Check details in General Information, Items, Store Groups, Participating Stores, Allocation Tables, Purchase Orders sections. | Details displayed. |  |
| 6 | Change Settings | Choose Settings in right corner of each section to adjust visible columns.For examble , choose Created By column in Items section | Columns settings are adjusted. |  |
| 7 | Check details | Choose left arrow in each section to check more details. | Details displayed. |  |
| 8 | Check details | Choose Blue highlighted text in any section and choose More Links to view accessible apps. | Details displayed. |  |

### Periodic Background Job

To perform below application jobs supply source determination, price activation and allocation table genaration you have to create a new promotion through chapter [Create Promotion](#unique_7) [page ] 8.

#### Schedule Promotion Supply Source Determination

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process the supply source is determined for given item/promotion.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Promotion Specialist (Retail) |  |  |
| 2 | Access the App | Open Schedule Promotion Supply Source Determination (F6443) app. | Application Jobs screen is displayed. |  |
| 3 | Create new job | Choose Create to create a new application job. | New Job: Promotion Supply Source Determination Job Templatescreen is displayed. |  |
| 4 | Enter job details | Enter the application job details in the Template Information and Scheduling Options sections.(Step 1)Job Template: Promotion Supply Source Determination Job TemplateJob Name: Promotion Supply Source Determination Job Template XXChoose Step 2Choose Define Recurrence Pattern to schedule periodic jobFor testing purpose - Flag Start Immediately [optional] | Template Information and Scheduling Options of Promotion Supply Source Determination Job Template are defined. |  |
| 5 | Enter Parameters | Choose Step 3In the Parameter section, make the following entries:Promotion: <Provide Promotion number>Provide Material Restrictions if requiredIf you use Generic Article in Promotion ,Flag Select All Variants of Selected Generic MaterialsIn the Other Parameters section, make the following entries:Enter Max. No. of Items per Process: <1> | The parameters of promotion supply source determination job template are defined. |  |
| 6 | Check | Choose Check | You can go ahead and schedule job message is displayed. |  |
| 7 | Schedule Job | Choose Schedule | Job Promotion Supply Source Determination Job Template XX has been scheduled message is displayed.Application Jobs screen displays again, and the new job displays in the Jobs table. |  |
| 8 | Check Job Status | On the Application Jobs screen, the job item status turned to Finished. | Job status turn to Finished. |  |
| 9 | Check Job Details | Choose right arrow against Job Navigate to Job details. | Job details displayed. |  |
| 10 | Execute Subsequent Processing | See chapter [Determine Supply Source](#unique_8) [page ] 10 with Promotion number. | Srce colum for all materials included in the application Job is determined to B. |  |

#### Schedule Promotion Price Activation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process promotion price is activated for a given item/promotion.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Promotion Specialist (Retail) |  |  |
| 2 | Access the App | Open Schedule Promotion Price Activation (F6441) app. | Application Jobs screen is displayed. |  |
| 3 | Create new job | Choose Create to create a new application job. | New Job: Promotion Price Activation Job Templatescreen is displayed. |  |
| 4 | Enter job details | Enter the application job details in the Template Information and Scheduling Options sections.(Step 1)Job Template: Promotion Price Activation Job TemplateJob Name: Promotion Price Activation Job Template XXChoose Step 2Choose Define Recurrence Pattern to schedule periodic jobFor testing purpose - Flag Start Immediately [optional] | Template Information and Scheduling Options of promotion price activation job template are defined. |  |
| 5 | Enter Parameters | Choose Step 3In the Parameter section, make the following entries:Promotion: <Provide Promotion number>Provide Material Restrictions if requiredFlag Activation in Option sectionIf you use Generic Article in Promotion ,Flag Select All Variants of Selected Generic MaterialsIf you have to Deactivate the already Activated PriceFlag Deactivation in Option sectionIn the Other Parameters section, make the following entries:Enter Max. No. of Items per Process: <1> | The parameters of promotion price activation job template are defined. |  |
| 6 | Check | Choose Check | You can go ahead and schedule job message is displayed. |  |
| 7 | Schedule Job | Choose Schedule | Job Promotion Price Activation Job Template XX has been scheduled message is displayed.Application Jobs screen displays again, and the new job displays in the Jobs table. |  |
| 8 | Check Job Status | On the Application Jobs screen, the job item status turned to Finished. | Job status turn to Finished. |  |
| 9 | Check Job Details | Choose right arrow against Job Navigate to Job details | Job details displayed. |  |
| 10 | Execute Subsequent Processing | See chapter [Activate Prices](#unique_9) [page ] 11 with Promotion number | Sales pr. colum for all materials included in the application Job is determined to B . |  |

#### Schedule Promotion Allocation Table Generation

|  |
| --- |
| Note You have to see chapter [Allocate Distribution](#unique_12) [page ] 14 and follow the steps to distribute allocation for all materials involved in promotion , before performing below application job to generate allocation table. |

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process allocation table generated for given item/promotion.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Promotion Specialist (Retail). |  |  |
| 2 | Access the App | Open Schedule Promotion Allocation Table Generation (F6442) app. | Application Jobs screen is displayed. |  |
| 3 | Create new job | Choose Create to create a new application job. | New Job: Promotion Price Activation Job Templatescreen is displayed. |  |
| 4 | Enter job details | Enter the application job details in the Template Information and Scheduling Options sections (Step 1)Job Template: Promotion Allocation Table Generation Job TemplateJob Name: Promotion Allocation Table Generation Job Template XXChoose Step 2Choose Define Recurrence Pattern to schedule periodic jobFor testing purpose - Flag Start Immediately [optional] | Template Information and Scheduling Options of promotion price activation job template are defined. |  |
| 5 | Enter Parameters | Choose Step 3In the Parameter section, make the following entries:Promotion: <Provide Promotion number>Provide Material Restrictions if requiredFlag Allocation table generation using entered plant quantities | The parameters of promotion allocation table generation job template are defined. |  |
| 6 | Check | Choose Check | You can go ahead and schedule job message is displayed. |  |
| 7 | Schedule Job | Choose Schedule | Job Promotion Allocation Table Generation Job Template XX has been scheduled message is displayed.Application Jobs screen displays again, and the new job displays in the Jobs table. |  |
| 8 | Check Job Status | On the Application Jobs screen, the job item status turned to Finished. | Job Status turn to Finished. |  |
| 9 | Check Job Details | Choose right arrow against Job Navigate to Job details | Job details displayed. |  |
| 10 | Check Allocation Table Number | Open Execute Subsequ. Processing - Promotions (WAK5) app, enter below detail:Promotion: <Provide Promotion Number>Choose Allocation Table. | Alloc.Tab. colum populates with allocation table number.Make a note of allocation table number. |  |
| 11 | Generate Follow-On Document | See chapter [Generate Follow-on Document](#unique_14) [page ] 16. | Follow-on document generated .Column Wrhs Order displays follow on documents.Column Expectation status displays in green.Make note of follow-on documents. |  |
| 12 | Display Follow-On Document | See chapter [Display Follow-On Document](#unique_15) [page ] 17. | Stock transport order is displayed. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| 5FV - Outbound Logistics for Distribution Centers | This scope item perform creation of Outbound Delivery, Goods Issue and Goods Receipt against Outbound Delivery. |

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
- related-to :: [[15-retail-operations/test-script-sales-pricing-for-retail-3i4-ae-sap-s-4hana-cloud-public-e]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/637_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 37,421 chars in the whole document
