---
id: 15-retail-operations/test-script-sales-pricing-for-retail-3i4-ae-sap-s-4hana-cloud-public-e
title: "Test Script: Sales Pricing for Retail (3I4_AE) - SAP S/4HANA Cloud Public Edition (3I4_S4CLD2608_BPD_EN_AE)"
description: "S/4HANA Cloud Public Edition test script for scope item 3I4_AE Sales Pricing for Retail: prerequisites, configuration and 38 pricing test procedures."
cluster: 15-retail-operations
tags: [kb/retail-operations, topic/retail-sales-pricing-and-promotions]
aliases: [3I4_S4CLD2608_BPD_EN_AE]
keywords: [Retail Sales Pricing and Promotions, sales pricing for retail, sales price calculation, planned markup, pricing documents, pricing worklist, generic articles, price points, purchasing conditions, two-step pricing]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3I4_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-944
topic: 15-retail-operations/retail-sales-pricing-and-promotions
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Sales Pricing for Retail (3I4_AE) - SAP S/4HANA Cloud Public Edition (3I4_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3I4_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Retail Sales Pricing and Promotions** in Retail Operations. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Sales Pricing for Retail (3I4_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232852893)

[2 Prerequisites 4](#_Toc232852894)

[2.1 System Access 4](#_Toc232852895)

[2.2 Roles 4](#_Toc232852896)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232852897)

[2.4 Business Conditions 6](#_Toc232852898)

[2.5 Configuration 6](#_Toc232852899)

[2.5.1 Assign Pricing Type or Reference Plant to Organization Level 7](#_Toc232852900)

[2.5.2 Set Pricing Condition Types – Change Access Sequence for Condition Type 7](#_Toc232852901)

[2.5.3 Define Price Point Group and Assign Price Point Ranges (Optional) 8](#_Toc232852902)

[2.5.4 Assign Price Point Group to Organizational Level (Optional) 9](#_Toc232852903)

[2.5.5 Assign Price Point Group to Organizational Level/Material Group (Optional) 9](#_Toc232852904)

[3 Overview Table 11](#_Toc232852905)

[4 Test Procedures 14](#_Toc232852906)

[4.1 Create Planned Markup for Distribution Chain (Optional) 14](#_Toc232852907)

[4.2 Change Planned Markup for Distribution Chain 15](#_Toc232852908)

[4.3 Display Planned Markup for Distribution Chain 16](#_Toc232852909)

[4.4 Create Planned Markup for Price List 17](#_Toc232852910)

[4.5 Change Planned Markup for Price List (Optional) 18](#_Toc232852911)

[4.6 Display Planned Markup for Price List (Optional) 19](#_Toc232852912)

[4.7 Maintain Price List Type for Site and Merchandise Category 20](#_Toc232852913)

[4.8 Calculate Sales Price for Single Articles 21](#_Toc232852914)

[4.9 Display Price Overview 22](#_Toc232852915)

[4.10 Display Sales Price Values (Optional) 23](#_Toc232852916)

[4.11 View Generic Article (with Pricing Profile ‘2’) 24](#_Toc232852917)

[4.12 Calculate Sales Price for Generic Article (with Pricing Profile ‘2’) 26](#_Toc232852918)

[4.13 Display Pricing Document 27](#_Toc232852919)

[4.14 Create Sales Prices for Structures Articles (Sales Set) 28](#_Toc232852920)

[4.15 Change Purchasing Price for Generic Article 29](#_Toc232852921)

[4.16 Maintain Pricing Reference Article for Generic Articles and Variants 31](#_Toc232852922)

[4.17 Calculate Sales Price for Generic article (with Price Reference Article) 33](#_Toc232852923)

[4.18 Calculate Sales Price with Price Points 34](#_Toc232852924)

[4.19 Create Pricing Document 36](#_Toc232852925)

[4.20 Display Pricing Document by Material 37](#_Toc232852926)

[4.21 Change Price Calculation 38](#_Toc232852927)

[4.22 Two-Step Sales Price Calculation 39](#_Toc232852928)

[4.23 Display Pricing Document by Article (Optional) 40](#_Toc232852929)

[4.24 Display Pricing Document by Organization Structure 41](#_Toc232852930)

[4.25 Calculate Sales Price in Background 42](#_Toc232852931)

[4.26 Create Pricing Document - Single Article (for Pricing Worklist) 44](#_Toc232852932)

[4.27 Change Purchasing Price - Single Article (for Pricing Worklist) 45](#_Toc232852933)

[4.28 Generate Pricing Worklist (Distribution Center Distribution Chain) 46](#_Toc232852934)

[4.29 Release Pricing Worklist (Distribution Center Distribution Chain) 47](#_Toc232852935)

[4.30 Generate Pricing Worklist (Store Distribution Chain) 48](#_Toc232852936)

[4.31 Release Pricing Worklist (Store Distribution Chain) 49](#_Toc232852937)

[4.32 Display Price Overview 50](#_Toc232852938)

[4.33 Generate Pricing Worklist in Background 51](#_Toc232852939)

[4.34 Create Supplier (Vendor) Discount Condition 53](#_Toc232852940)

[4.35 Displaying Purchasing Conditions 54](#_Toc232852941)

[4.36 Create Freight Condition 54](#_Toc232852942)

[4.37 Reset Site-Specific Price and Price List Price 55](#_Toc232852943)

[4.38 Maintain Wholesale Prices 59](#_Toc232852944)

## Purpose

Overview

A key aspect of how retailers address the market is their pricing strategy for sales prices. Depending on the desired strategy, sales prices can be planned based on various factors such as purchasing prices and margin goals. Furthermore, sales prices can be specified for all sales channels at different levels, allowing an easy grouping of related stores. You can implement a price strategy that considers the way the merchandise is procured (directly from the supplier or via a distribution center). Thus, you can reflect distribution costs and support selling merchandise from distribution centers to stores (for example, in a franchise scenario).

Mass changes of sales prices can be executed for sets of articles, and multiple organizational levels, also in an automated manner. Retail price management can reflect the retailer’s requirements through roles and authorization of its employees. Once defined, sales prices must be communicated, for example, by transferring the relevant sales prices available to stores and all other sales channels. For more information, see the Store Connectivity – Outbound (3I2) scope item.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

|  |
| --- |
| Note In the retail industry, specific terms differ from the standard terms used in other lines of business. Therefore, SAP solutions which provide business processes across multiple lines of businesses may use terms for the corresponding business objects, transactions, and user interfaces that deviate from the retail terminology. For integration and reuse reasons, the SAP S/4HANA Cloud Public Edition, retail, fashion, and vertical business business may thus include different terms that refer to the same concept. SAP intends to harmonize the terminology in the future.The following terms are used synonymously in this document:Table 1:Standard Terms in Lines of BusinessSAP S/4HANA Cloud Public Edition, retail, fashion, and vertical business businessMaterial, productArticleMaterial group, product groupMerchandise categoryPlant, locationSite (as superordinate term) - store and distribution center (DC) |

## Prerequisites

This chapter summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data, and business conditions.

s

### System Access

|  |  |
| --- | --- |
|  | Details |
| System | Accessible through SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Pricing Specialist (Retail) | SAP_BR_PRICING_SPCLST_RFM | Retail PricingRetail Markups |  |  |
| Purchaser (Retail) | SAP_BR_PURCHASER_RFM | Retail Purchasing |  |  |
| Master Data Specialist - Product Data (Retail) | SAP_BR_MD_SPCLST_ITEM_RFM | Retail Master Data Product Master |  |  |
| Pricing Specialist | SAP_BR_PRICING_SPECIALIST | Price Management |  |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Configuration Expert - Business Process Configuration |  |  |
| Master Data Specialist - Location Data (Retail) | SAP_BR_MD_SPCLST_SITE_RFM | Retail Site Master |  |  |
| Inventory Manager (Retail) | SAP_BR_INVENTORY_MGR_RFM | Inventory Manager (Retail) |  |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

|  |
| --- |
| Note Combination of sales organization and distribution channel makes a distribution chain. |

Use your own master data or the following sample data to go through the test procedure.

| Master / Org. Data | Value | Master / Org. Data Details | Comments |
| --- | --- | --- | --- |
| Article (material or product) | R_1006 | Trading Good - Single Article |  |
| Article (material or product) | R_1003 | Trading Good - Generic Article |  |
| Article (material or product) | R_1052 | Trading Good – Sales Set Article |  |
| Article (material or product) | R_1005 | Trading Good - Generic Article |  |
| Article (material or product) | R_1051 | Trading Good - Single Article |  |
| Article (material or product) | R_1032 | Trading Good - Single Article |  |
| Supplier | 33213002 | Retail Food Supplier AE |  |
| Merchandise Category (material group or product group) | R1193001R1202001R2121002 |  |  |
| Retail Distribution Center (DC) | 3350 | DC 3350 AE |  |
| Retail Store | 33413342 | Store 3341 AEStore 3342 AE |  |
| Sales Organization | 3310 | Dom. Sales Org |  |
| Distribution Channel | 40, 50, 10 | Store SalesDistributionDirect Sales |  |
| Division | 00 | Product Division 00 |  |
| Storage Location | 995A | Storage Loc. DC |  |
| Purchasing Organization | 3310 | Purch. Org. 3310 |  |
| Purchasing Group | 002 | Group 002 |  |
| Company Code | 3310 | Company Code 3310 |  |
| Price Point Group1 | PPG331 | Price Point Group |  |

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 3I1 - Products for Retail | Articles must be available in the system and the sales view must exist for them.Purchasing info records and purchasing price for articles must exist |
| 5FJ- Product Taxonomies for Retail | Creation of Merchandise categories |

### Configuration

Prerequisites

To carry out the following activities, the business role SAP_BR_BPC_EXPERT must be assigned to the user.

#### Assign Pricing Type or Reference Plant to Organization Level

Use

To execute the scope item, you must assign a reference plant and pricing type to organizational level.

The setting here is used for pricing in retail. Assign one of the pricing types you have defined to the organizational level and enter one of the plants in the distribution chain as the reference plant. The reference plant can either be a dummy plant (not used in any operational process) or an operational plant (store and distribution center). Per store distribution chain a reference store or in the case of a distribution center distribution chain a reference distribution center is assigned to. The site (store or distribution center) for this assignment should belong to the corresponding distribution chain.

Procedure

1. Log on to the Project Experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. You can search for the configuration activity Assign Pricing Type/Reference Plant to Organization Level to locate it in the tree view. Choose Open Documentation for the found line item to see more details. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).
3. The Assign Pricing Type/Reference Plant to Organizational Level screen is displayed.
4. Select New Entries.
5. Enter values for Sales Organization, Distribution Channel, Price List (optional), Currency (optional), Pricing Type and Reference Plant.
6. Select Save.

Result

You have assigned reference plant and pricing type to organizational level.

#### Set Pricing Condition Types – Change Access Sequence for Condition Type

Use

To execute the scope item, you must change the access sequence for condition type PPR0 (Default Gross Price) to 0002 (Gross Price)

The setting here is needed for price maintenance of generic articles.

Procedure

1. Log on to the Project Experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. You can search for the configuration activity Set Pricing Condition Types – Purchasing to locate it in the tree view. Choose Open Documentation for the found line item to see more details. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).
3. The "Create Condition Types for Subsequent Settl..”: Change is displayed.
4. Select “Position” and enter in window for Condition Type: PPR0
5. Select the line with PPR0 and select “Details”
6. Overwrite value for Access Sequence with 0002 (Gross Price)
7. Select Save.

Result

You have assigned access sequence 0002 (Gross Price) to condition type PPR0 (Default Gross Price)

#### Define Price Point Group and Assign Price Point Ranges (Optional)

Use

To execute the scope item, you can define price point group and assign price point ranges.

Price points are used in sales price calculations as proposals for persuasive sales prices. Price points are created with the aid of price point ranges.

All price points in a price point range are generated on the basis of the first price point. The interval (increment) is repeatedly added to the first price point until the last price point is calculated. The price point group controls which price points are used in sales price calculations and how prices are rounded off within the price point group.

Procedure

1. Log on to the Project Experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. You can search for the configuration activity Define Price Point Group and Assign Price Point Ranges to locate it in the tree view. Choose Open Documentation for the found line item to see more details. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori Launchpad as aConfiguration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).
3. The "Define Price Point Group and Assign Price Point Ranges screen is displayed.
4. Select New Entries.
5. Enter values for Price Point Group, Description, Price Point Currency and Rounding.
6. Select the line with new value for price point group and Select Assign price point ranges.
7. Enter values for First Price, Last Price, Increment.
8. Select Save.

Result

You have defined your price point group and assigned price point ranges.

#### Assign Price Point Group to Organizational Level (Optional)

Use

To execute the scope item, you can assign your newly created price point group to sales organization and distribution channel.

Procedure

1. Log on to the Project Experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. You can search for the configuration activity Assign Price Point Group to Organizational Level to locate it in the tree view. Choose Open Documentation for the found line item to see more details. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori Launchpad with a business role as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).
3. The "Assign Price Point Group to Organization " screen is displayed.
4. Select New Entries.
5. Enter values for Sales Organization 3310, Distribution Channel (40), Price Point Currency AED, Price Point Category (01) and Price Point Group (your newly created price point group).
6. Select Save.

|  |
| --- |
| Note Within a starter system - an entry is already available for the distribution chain, so new entry would not work. In this case only the assigned price point group can be adjusted with the newly created price point group. New Entries will only work if no data exists for the distribution chain. |

Result

You have assigned your price point group to organizational level.

#### Assign Price Point Group to Organizational Level/Material Group (Optional)

Use

To execute the scope item, you can assign your newly created price point group to sales organization, distribution channel and material group.

|  |
| --- |
| Note This is only required if there is a different price point group relevant for a dedicated merchandise category and the normal one – assigned to distribution chain is not applicable. |

Procedure

1. Log on to the Project Experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. You can search for the configuration activity Assign Price Point Group to Organizational Level//Merchandise Category to locate it in the tree view. Choose Open Documentation for the found line item to see more details. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).
3. The "Assign Price Point Group to Organization " screen is displayed.
4. Select New Entries.
5. Enter values for Sales Organization 3310, Distribution Channel (40) the merchandise category for which a specific price point group is applicable, Price Point Currency AED, Price Point Category (01) and Price Point Group (your newly created price point group).
6. Select Save.

Result

You have assigned your price point group to organizational level.

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App | Expected Results |
| --- | --- | --- | --- |
| [Create Planned Markup for Distribution Chain (Optional)](#unique_14) [page ] 14 | Pricing Specialist (Retail) | Create Planned Markup (WVA8) | Planned markups are created for distribution chain |
| [Change Planned Markup for Distribution Chain](#unique_15) [page ] 15 | Pricing Specialist (Retail) | Maintain Planned Markup (WVA9) | Planned markups are changed for distribution chain |
| [Display Planned Markup for Distribution Chain](#unique_16) [page ] 16 | Pricing Specialist (Retail) | Display Planned Markup (WVA10) | Planned markups are displayed for distribution chain |
| [Create Planned Markup for Price List](#unique_17) [page ] 17 | Pricing Specialist (Retail) | Create Planned Markup - Price List (WVA11) | Planned markups are created for pricelist |
| [Change Planned Markup for Price List (Optional)](#unique_18) [page ] 18 | Pricing Specialist (Retail) | Maintain Planned Markup - Price List (WVA12) | Planned markups are changed for price list |
| [Display Planned Markup for Price List (Optional)](#unique_19) [page ] 19 | Pricing Specialist (Retail) | Display Planned Markup - Price List (WVA13) | Planned markups are displayed for price list |
| [Maintain Price List Type for Site and Merchandise Category](#unique_20) [page ] 20 | Master Data Specialist - Product Data (Retail) | Assign Merchandise Categories - Sites (WB30N) | Price list type for site is maintained |
| [Calculate Sales Price for Single Articles](#unique_21) [page ] 21 | Pricing Specialist (Retail) | Create Sales Price Calculation (VKP5) | Sales price is calculated for single article |
| [Display Price Overview](#unique_22) [page ] 22 | Pricing Specialist (Retail) | Determine Sales Prices (VKP2) | Price overview is displayed for different Organization levels and selection criteria |
| [Display Sales Price Values (Optional)](#unique_23) [page ] 23 | Inventory Manager (Retail) | Material Inventory Values - Line Items (F1423) | Sales Price value is displayed for the specific Inventory Quantity line |
| [View Generic Article (with Pricing Profile ‘2’)](#unique_24) [page ] 24 | Master Data Specialist - Product Data (Retail) | Maintain Article (MM42) | Article attributes are displayed |
| [Calculate Sales Price for Generic Article (with Pricing Profile ‘2’)](#unique_25) [page ] 26 | Pricing Specialist (Retail) | Create Sales Price Calculation (VKP5) | Sales price is calculated for generic article |
| [Display Pricing Document](#unique_26) [page ] 27 | Pricing Specialist (Retail) | Display Pricing Document (VKP7) | Pricing document for the relevant document number is displayed with the details of sales prices. |
| [Create Sales Prices for Structures Articles (Sales Set)](#unique_27) [page ] 28 | Pricing Specialist (Retail) | Create Sales Price Calculation (VKP5) | Sales price is calculated for Sales set |
| [Change Purchasing Price for Generic Article](#unique_28) [page ] 29 | Purchaser (Retail) | Change Price Conditions, Set Tax Rates – Purchasing ( MEK2 ) | Purchasing price is updated. |
| [Maintain Pricing Reference Article for Generic Articles and Variants](#unique_29) [page ] 31 | Master Data Specialist - Product Data (Retail) | Maintain Article (MM42) | Generic article maintained with Pricing reference article. |
| [Calculate Sales Price for Generic article (with Price Reference Article)](#unique_30) [page ] 33 | Pricing Specialist (Retail) | Create Sales Price Calculation (VKP5) | Sales Price calculation for article with pricing reference article |
| [Calculate Sales Price with Price Points](#unique_31) [page ] 34 | Pricing Specialist (Retail) | Create Sales Price Calculation (VKP5) | Sales price is calculated with price points |
| [Create Pricing Document](#unique_32) [page ] 36 | Pricing Specialist (Retail) | Create Sales Price Calculation (VKP5) | Creating a pricing document with status ‘A’ |
| [Display Pricing Document by Material](#unique_33) [page ] 37 | Pricing Specialist (Retail) | List Pricing Documents - for Articles (VKP3) | Display pricing documents created by article |
| [Change Price Calculation](#unique_34) [page ] 38 | Pricing Specialist (Retail) | Maintain Sales Price Calculation (VKP1) | Existing price calculation is changed |
| [Two-Step Sales Price Calculation](#unique_35) [page ] 39 | Pricing Specialist (Retail) | Create Sales Price Calculation (VKP5) | Sales price is calculated for a two-step pricing scenario |
| [Display Pricing Document by Article (Optional)](#unique_36) [page ] 40 | Pricing Specialist (Retail) | List Pricing Documents - for Articles (VKP3) | Displays list of pricing documents arranged by material |
| [Display Pricing Document by Organization Structure](#unique_37) [page ] 41 | Pricing Specialist (Retail) | List Pricing Documents - for Organizations (VKP4) | Displays lists of pricing documents arranged by organizational level |
| [Calculate Sales Price in Background](#unique_38) [page ] 42 | Pricing Specialist (Retail) | Schedule Sales Price Calculation Run (F5412) | Sales price calculation in background run |
| [Create Pricing Document - Single Article (for Pricing Worklist)](#unique_39) [page ] 44 | Pricing Specialist (Retail) | Create Sales Price Calculation (VKP5) | Sales Price is calculated for the article |
| [Change Purchasing Price - Single Article (for Pricing Worklist)](#unique_40) [page ] 45 | Purchaser (Retail) | Change Price Conditions ( MEK2 ) | Change of purchasing pricing condition |
| [Generate Pricing Worklist (Distribution Center Distribution Chain)](#unique_41) [page ] 46 | Pricing Specialist (Retail) | Generate Sales Price Worklist (WVN0) | Create Pricing Worklist |
| [Release Pricing Worklist (Distribution Center Distribution Chain)](#unique_42) [page ] 47 | Pricing Specialist (Retail) | Release Sales Price Worklist - by Article (WVN1) | Release Pricing Worklist |
| [Generate Pricing Worklist (Store Distribution Chain)](#unique_43) [page ] 48 | Pricing Specialist (Retail) | Generate Sales Price Worklist (WVN0) | Create Pricing Worklist |
| [Release Pricing Worklist (Store Distribution Chain)](#unique_44) [page ] 49 | Pricing Specialist (Retail) | Release Sales Price Worklist - by Article (WVN1) | Release Pricing Worklist |
| [Display Price Overview](#unique_45) [page ] 50 | Pricing Specialist (Retail) | Determine Sales Prices (VKP2) | Price overview is displayed for different Organization levels and selection criteria |
| [Generate Pricing Worklist in Background](#unique_46) [page ] 51 | Pricing Specialist (Retail) | Schedule Generation of Sales Price Worklist (F6127) | Generate Pricing Worklist in Background |
| [Create Supplier (Vendor) Discount Condition](#unique_47) [page ] 53 | Purchaser (Retail) | Create Price Conditions - Purchasing (MEK1) | Creation of pricing conditions |
| [Displaying Purchasing Conditions](#unique_48) [page ] 54 | Purchaser (Retail) | Maintain Purchasing Conditions (MEKA) | Purchasing Conditions are displayed |
| [Create Freight Condition](#unique_49) [page ] 54 | Master Data Specialist - Product Data (Retail) | Maintain Article (MM42) | Addition of condition record for Freight via article master maintenance |
| [Reset Site-Specific Price and Price List Price](#unique_50) [page ] 55 | Pricing Specialist (Retail) | Create Sales Price Calculation (VKP5) | Delete site price and price list price |
| [Maintain Wholesale Prices](#unique_51) [page ] 59 | Pricing Specialist (Retail) |  |  |

## Test Procedures

This chapter describes the test procedures for each process step that belongs to this scope item.

### Create Planned Markup for Distribution Chain (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity to manually create planned markup at distribution chain level.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Pricing Specialist (Retail). |  |  |
| 2 | Access App | Open Create Planned Markup (WVA8) app. | Create SP Markup Planned Condition: Fast Entry screen is displayed. |  |
| 3 | Enter Values for Planned Markup Creation | Make the following entries in the screen and select Save:Sales Organization: 3310Distribution Channel: 40Matl Group: <Provide your new merchandise category>Note To create New Merchandise Category refer to chapter "Create Merchandise Category" of scope item 5FJAmount: 40UoM: %Validity: Today To End Of The Year | Planned markup of 40% is created for distribution chain 3310/40 for material group <merchandise category>. |  |
| 4 | (Optional) Repeat Step-3 (for Distribution Channel 50 / 10, all other parameters being same) | Make the following entries in the screen and select Save:Sales Organization: 3310Distribution Channel: 50Matl Group: < Provide your new merchandise category>Amount: 40UoM: %Validity: Today To End Of The Year | Planned markup of 40% is created for distribution chain 3310/50 for material group <merchandise category>.Planned markup of 40% is created for distribution chain 3310/10 for material group <merchandise category>. |  |

### Change Planned Markup for Distribution Chain

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity to manually change planned markup at distribution chain level.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Pricing Specialist (Retail). |  |  |
| 2 | Access App | Open Maintain Planned Markup (WVA9) app. | Change SP Markup Planned Selection screen is displayed. |  |
| 3 | Enter Selection Criteria Values to Change Planned Markup | Make the following entries in the screen and select Execute:Sales Organization: 3310Distribution Channel: 40Matl Group: R1193001Validity: Today | Planned markup for distribution chain 3310/40 for material group R1193001 is displayed in edit mode. |  |
| 4 | Enter New Value for Planned Markup | Change the planned markup Amount to 50 and select Save. | Planned markup for distribution chain 3310/40 for material group R1193001 is changed to 50% |  |
| 5 | (Optional) Repeat Step-3 (for Distribution Channel 50 / 10, all other parameters being same) | Make the following entries in the screen and select Execute:Sales Organization: 3310Distribution Channel: 50Matl Group: R1193001Validity: Today | Planned markup for distribution chain 3310/50 for material group R1193001 is displayed in edit mode.Planned markup for distribution chain 3310/10 for material group R1193001 is displayed in edit mode. |  |
| 6 | (Optional) Repeat Step-4 (for Distribution Channel 50 / 10, all other parameters being same) | Change the planned markup Amount to a new value and select Save. | Planned markup for distribution chain 3310/50 for material group R1193001 is changed to new percentage value.Planned markup for distribution chain 3310/10 for material group R1193001 is changed to new percentage value. |  |

### Display Planned Markup for Distribution Chain

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity to manually display planned markup at distribution chain level.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Pricing Specialist (Retail). |  |  |
| 2 | Access App | Open Display Planned Markup (WVA10) app. | Display SP Markup Planned: Selection screen is displayed. |  |
| 3 | Enter Selection Criteria Values to Display Planned Markup | Make the following entries in the screen and select Execute:Sales Organization: 3310Distribution Channel: 40Matl Group: R1193001Validity: Today | Planned markup of 50% is displayed for distribution chain 3310/40 for material group R1193001. |  |
| 4 | (Optional) Repeat test step 3 (for Distribution Channel 50 / 10, all other parameters remain same) | Make the following entries in the screen and select Execute:Sales Organization: 3310Distribution Channel: 50Matl Group: R1193001Validity: Today | New percentage value for planned markup is displayed for distribution chain 3310/50 for material group R1193001. |  |

### Create Planned Markup for Price List

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity to manually create planned markup at price list level.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Pricing Specialist (Retail). |  |  |
| 2 | Access App | Open Create Planned Markup - Price List (WVA11) app. | Create SP Markup Planned Condition: Fast Entry screen is displayed. |  |
| 3 | Enter values for Planned Markup creation | Make following entries in the screen and select Save:Sales Organization: 3310Distribution Channel: 40Price List Type: P4Document Currency: AEDMatl Group: R1193001Amount: 40UoM: %Validity: Today To End Of The Year | Planned markup for distribution chain 3310/40 with pricelist type P4 (currency AED) for material group R1193001 is created. |  |

### Change Planned Markup for Price List (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity to change planned markup for price list.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Pricing Specialist (Retail). |  |  |
| 2 | Access App | Open Maintain Planned Markup - Price List (WVA12) app. | Change SP Markup Planned : Selection screen is displayed. |  |
| 3 | Enter selection criteria values to change Planned markup | Make the following entries in the screen and select Execute:Sales Organization: 3310Distribution Channel: 40Price List Type: P4Document Currency: AEDMatl Group: R1193001Valid On: Today | Planned markup for distribution chain 3310/40 with pricelist type P4 (currency AED) for material group R1193001 is displayed in edit mode. |  |
| 4 | Enter new value for Amount | Change the planned markup Amount to 50 and select Save. | Planned markup for distribution chain 3310/40 for material group R1193001, price list type P4 and currency AED is changed to 50%. |  |

### Display Planned Markup for Price List (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity to display planned markup for price list.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Pricing Specialist (Retail). |  |  |
| 2 | Access App | Open Display Planned Markup - Price List (WVA13) app. | Display SP Markup Planned : Selection screen is displayed. |  |
| 3 | Enter selectioncriteria values for Planned Markup display | Make the following entries in the screen and select Execute:Sales Organization: 3310Distribution Channel: 40Price List Type: P4Document Currency: AEDMatl Group: R1193001Valid On: Today | Planned markup of 50% is displayed for distribution chain 3310/40 for material group R1193001 and price list type P4. |  |

### Maintain Price List Type for Site and Merchandise Category

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity to assign a price list type for site and merchandise category.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Location Data (Retail). |  |  |
| 2 | Access App | Open Assign Merchandise Categories - Sites (WB30N) app. | Selection screen with Filters is displayed. |  |
| 3 | Enter selection value for Site | Make following entries on screen and select Execute:Select by Merchandise Category: XMerchandise Category: R1193001Customer Number for Site: 3341, 3342 | Change Merchandise Category / Site assignment is shown in list is displayed. |  |
| 4 | Assign Price List Type | Double-Click on the line which has the Merchandise Category.Select both the lines, selectMass Maintenance and enter value for Price List Type and select Continue and Save.Price List Type : P4 | Price list type P4 is assigned to merchandise category R1193001 in sites 3341 and 3342. |  |

### Calculate Sales Price for Single Articles

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity to create sales price for single articles.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Pricing Specialist (Retail). |  |  |
| 2 | Access App | Open Create Sales Price Calculation (VKP5) app. | Create Sales Price Calculation (VKP5) screen is displayed. |  |
| 3 | Enter values for Price Calculation fields | On the Create Price Calculation: initial screen make the following entries and select Execute:Material: R_1006Sales Organization: 3310Distribution Channel: 40Pricelist: P4Plant: 3341Validity: Today To End Of The YearPurchase price determn.seq: 01Sales price determination seq: 01List group: CList variant: 01 | The price calculation for the entries made is displayed considering the planned markups maintained accordingly. The entries shown are specific to the following levels:Distribution chainPrice listSite |  |
| 4 | Select Save | You can see three specific lines specific to the three levels.You can select line specific to required level and update a new value for final price and select Save.Make a note of the pricing document number. | Pricing document gets created and success message is displayed:“Data saved; pricing document <No. Of Pricing Document> created”. |  |

### Display Price Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity to display and review prices for a number of articles and organizational levels.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Pricing Specialist (Retail). |  |  |
| 2 | Access App | Open Determine Sales Prices (VKP2) app. | Price Overview: initial screen is displayed. |  |
| 3 | Enter values for selection criteria | Make the following entries and select Execute:Material: R_1006 ( Single article)Sales Organization: 3310Distribution Channel: 40Plant: 3341Pricelist: P4Validity: Today To End Of The YearDisplay distribution chain and plant/price list separately: XUse all units of measure of the material: XList Group: ADisplay Price Origin: X | Sales price relevant for the selection criteria is displayed.Note Here observe that sales price calculation done for distribution chain-specific line will be different from that of price list-specific line and site-specific line. |  |

### Display Sales Price Values (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity to display and review prices for a number of articles and organizational levels and further you need to execute sales price valuation step (Chapter 4.1 - Run Automatic Sales Price Revaluation) from scope item Sales Price Valuation for Retail (5FT).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager (Retail) |  |  |
| 2 | Access App | Open Material Inventory Values - Line Items (F1423) app. | Material Inventory Values - Line Items (F1423) screen is displayed. |  |
| 3 | Enter values for selection criteria | Make the following entries and select Go:Start Date: Beginning of YearEnd Date: TodayCompany Code: 3310Ledger: 0LSelect Adapt Filters and enter following:Plant: 3341 (flag check box Shown on filter bar)Material: R_1006 (flag check box Shown on filter bar)Select Go. | Output details are displayed such as Inventory Quantity, Amount in Company Code Currency, Amount in Global Currency and Amount in Freely Defined Currency 1. |  |
| 4 | Enhance the Display with an additional column | Select Navigation Panel.Under Columns expand the node MeasuresThere select Add measure Value SP LocalCrcy to display. | A new column Value SP LocalCrcy is displayed in the output display.It displays the sales price value for the specific inventory quantity line.Sales price value for the article can be computed by dividing the value shown in this column Value SP LocalCrcy by the inventory quantity. |  |

### View Generic Article (with Pricing Profile ‘2’)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity to view attributes of a generic article.

Prerequisites

Before executing this activity, you must execute Create Generic Article with Variants process step by using the scope item Products for Retail (3I1).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data (Retail). |  |  |
| 2 | Access App | Open Maintain Article (MM42) app. | All views screen is displayed. |  |
| 3 | Enter values for selection | On the Change Screen, input the following entries, select check boxes for Basic data and Sales and select Continue:Article: R_1003 (Generic Article)Sales Org: 3310Distr. Channel: 40 | Basic Data View for article is displayed in edit mode. |  |
| 4 | Display pricing attributes for article | On Basic Data screen under sub-screen Groupings, check (or change) the following:Pricing Profile: 2 (All variants have the sales price of the generic material)Double click on fieldPricing Reference MaterialChoose Back | Variant matrix screen is shown.For all variants, the generic article is shown as the pricing reference article. The field is display only and cannot be changed. |  |
| 5 | Select Variant Prices matrix | On Sales View screen, select the following:Variant Prices | Sales Price Calculation screen is displayed.Notice that for one of the variants where pricing reference material was set, the price field is grayed out and cannot be changed. |  |
| 6 | Check pricing reference assignment for the article | PrcRefArt. tabMaintain PR ArtChoose CancelChoose Back | Pricing Reference Material Maintenance screen is displayed.This is display only and you cannot change or enter the pricing reference material manually. |  |
| 7 | Save the article | If you have changed the pricing profile to value ‘2’, thenChoose Save. | Article is saved with pricing profile ‘2’ |  |

### Calculate Sales Price for Generic Article (with Pricing Profile ‘2’)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity to create sales price for generic articles that have Pricing Profile set as ‘2’.

|  |
| --- |
| Note Pricing Profile ‘2’ indicates the sales prices of the variants correspond to that of the generic article and the system does not allow you to maintain the sales prices for the variants individually. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Pricing Specialist (Retail). |  |  |
| 2 | Access App | Open Create Sales Price Calculation (VKP5) app. | Create Sales Price Calculation (VKP5): initial screen is displayed. |  |
| 3 | Enter values for Price Calculation fields | On the Create Price Calculation: initial screen, make the following entries and select Execute:Material: R_1003* ( Generic article , Variants )Sales Organization: 3310Distribution Channel: 40Validity: Today To End Of The YearPurchase price determn.seq: 01Sales price determination seq: 01List group: CList variant: 01 | The price calculation for the entries made is displayed considering the planned markups maintained accordingly.Note Only for generic article lines in the output the fields for Final Price, Gross Sales Price, Markup%, and Gross Margin need to enter.These fields are not editable for all other lines (variant articles). |  |
| 4 | Maintain New Price values | Change the final Price for line corresponding to Distribution Channel level. | Upon changing the price, you will notice that the variant article’s prices are also changed for specific level (Distribution Channel) based on the changed prices for this level for generic article. |  |
| 5 | Save the entries | Select lines for Generic article and select Save.Make a note of the pricing document number. | Pricing document is created, and a success message is displayed. |  |

### Display Pricing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity to display a pricing document using a pricing document number.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Pricing Specialist (Retail). |  |  |
| 2 | Access App | Open Display Pricing Document (VKP7) app. | Pricing Document Display: initial screen is displayed. |  |
| 3 | Enter the pricing document number | Enter a <Pricing document number> from previous step and select Execute. | Pricing document for the relevant document number is displayed with the details of sales prices.Verify that the prices shown on the screen are the values you had maintained in previous test step.You will see the status as ‘C’ meaning the prices are active and condition records created. |  |

### Create Sales Prices for Structures Articles (Sales Set)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity to create sales price for structured articles (sales set).

|  |
| --- |
| Note This use case is relevant when the sales set is procured from external supplier. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Pricing Specialist (Retail). |  |  |
| 2 | Access App | Open Create Sales Price Calculation (VKP5) app. | Create Price Calculation: initial screen is displayed. |  |
| 3 | Enter values for Price Calculation fields | On the Create Price Calculation: Initial Screen, make the following entries and select Execute:Material: R_1052 ( Structured article – Sales Set )Sales Organization: 3310Distribution Channel: 40Validity: Today To End Of The YearPurchase price determn.seq: 01Sales price determination seq: 01List group: CList variant: 01 | The price calculation for the entries made is displayed accordingly. |  |
| 4 | Maintain New Price values | Navigate to the Create Price Calculation overview screen.Change the final price for lines corresponding to distribution channel level. |  |  |
| 5 | Select on Save | Select All and select Save.Make a note of the pricing document number. | Pricing document gets created and message is displayed.. |  |

|  |
| --- |
| Note As we are buying the sales set from an external vendor, it is treated like a normal selling article. In this case, the purchase information. record will be available. there is a need to create the sales set in the DC or store, there will not be a purchase information record in this case, and the purchase price determination sequence "02" could be used to propose the purchase price of the sales set based on components. purchase price of components can then also be viewed choosing line with Sales Set and Goto > Purchasing . |

### Change Purchasing Price for Generic Article

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity to change purchasing price for a generic article.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser (Retail). |  |  |
| 2 | Access App | Open Change Price Conditions - Purchasing (MEK2) app. | Change Condition Records Screen is displayed. |  |
| 3 | Enter values for Condition Type field | On the Change Condition Records Screen, enter the following entries and select Key Combination:Condition Type: PPR0 ( Gross Price )Key Combination screen is displayed.Select Material Info Record.Select Choose. | Gross Price selection screen will be displayed. |  |
| 4 | Enter values for selection | On the Change Screen , input the following entries and select Execute:Supplier: 33213002Article: R_1003 ( Generic Article )Purchasing Organization: 3310Info Record Category: 0Valid On: Today’s date | Existing price amount is displayed. |  |
| 5 | Save Price Conditions | Enter a new value in field Amount.Select Save. | Condition records saved. |  |

### Maintain Pricing Reference Article for Generic Articles and Variants

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity to maintain pricing reference article for generic article and its variants.

|  |
| --- |
| Note If you would like to have separate sales prices for variant articles, the concept of pricing reference article in combination with the pricing profile can be used.In the master data of the generic article, you can use the Pricing profile field to generate default values for the pricing reference article field in the master data of the variants.Sales prices of variants of a generic article can be inherited from the so-called pricing reference material. The pricing reference material can be the generic article or a variant. Pricing reference articles are maintained in the article master data. |

The pricing profile field can have the following entries:

- Pricing Profile is initial: The system leaves the Pricing reference article field for the variants blank. If variants are to inherit sales prices, the user has to make the necessary entries. You choose this profile if you wish the majority or all of the variants to have their own sales prices.
- Pricing Profile is 1: For each variant, the system suggests the generic article number in the Pricing reference article field. If variants are to have different sales prices, however, you can change this default value. You choose this profile if you wish the majority or all of the variants to inherit their sales prices from the generic article.
- Pricing Profile is 2: The Pricing reference article field contains the generic article number for all variants. The default value cannot be changed as the Pricing reference article field is not ready for input.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data (Retail). |  |  |
| 2 | Access App | Open Maintain Article (MM42) app. | All views screen is displayed. |  |
| 3 | Enter values for selection | On the Change Screen, input the following entries, select check boxes for Basic data and Sales and select Continue:Article: R_1005 (Generic Article)Sales Org: 3310Distr. Channel: 40 | Basic Data View for article is displayed in edit mode. |  |
| 4 | Change pricing attributes for article | On Basic Data screen under sub-screen Groupings, change the following:Pricing Profile: 1 (Variants priceable differently; propose GMaterial as ref.Double click on fieldPricing Reference MaterialChoose Back | Variant matrix screen is shown.For all variants, the generic article is shown as the pricing reference article. The field is editable and can be changed (if needed). |  |
| 5 | Select Variant Prices matrix | On Sales View screen, select the following:Variant Prices | Sales Price Calculation screen is displayed.Notice that for one of the variants where pricing reference material was set, the price field is grayed out and cannot be changed. |  |
| 6 | Change pricing reference assignment for the article | PrcRefArt. tabMaintain PR ArtCharacteristicsOn the screen Pricing Reference material Maintenance:Select radio button VarietySelect button Characteristic ValuesPress F4(value) help on field Pr. Ref. Matl, choose article number R_1005001 (one of the variants created for Diet) as pricing reference article for all variants of DietChoose OKPress F4(value) help on field Pr. Ref. Matl, choose article number R_1005005 (one of the variants created for Normal) as pricing reference article for all variants of Normal.Choose OKChoose AdoptOn screen Pricing Reference material Maintenance:Choose AdoptAnd againChoose Adopt | Pricing Reference Material Maintenance screen is displayed.You can enter the pricing reference material manually or choose the possibility via Characteristics. |  |
| 7 | Define Sales Price for Pricing Reference Article | On the Characteristics screen shown,Select tab Fin.PrcIn the editable fields for Diet and Normal set the sales price value for the pricing reference article:Diet <price1> and choose ENTERNormal <price2> and choose ENTER. | Two editable fields are shownObserve that the prices are inherited to other variants |  |
| 8 | Save Sales Prices entered | On the Characteristics screen shown, flag check box Save sales pr. CondsChoose backChoose Save. | Variant prices are now applicable instead of the generic article’s price.And further, different prices are possible for different variants. |  |

### Calculate Sales Price for Generic article (with Price Reference Article)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity to maintain sales price for generic article that uses pricing reference article.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Pricing Specialist (Retail). |  |  |
| 2 | Access App | Open Create Sales Price Calculation (VKP5) app. | Create Price Calculation: initial screen is displayed. |  |
| 3 | Enter values for Price Calculation fields | On the Create Price Calculation: initial screen, make the following entries and select Execute:Material: R_1005* ( Generic article)Sales Organization: 3310Distribution Channel: 40Validity: Today To End Of The YearPurchase price determn.seq: 01Sales price determination seq: 01List group: CList variant: 01 | The price calculation for the entries made is displayed.Change price values for the price reference material variant set you in previous step. |  |
| 4 | Save your entries | Select lines that you have changed the prices and select Save.Make a note of the pricing document number. | Pricing document gets created and success message is displayed. |  |

### Calculate Sales Price with Price Points

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity to maintain price points in sales price calculation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Pricing Specialist (Retail). |  |  |
| 2 | Access App | Open Create Sales Price Calculation (VKP5) app. | Create Price Calculation: initial screen is displayed. |  |
| 3 | Enter values for Price Calculation fields | On the Create Price Calculation: initial screen, enter the following entries and select Execute:Material: R_1052 ( Sales set article )Sales Organization: 3310Distribution Channel: 40Validity: Today To End Of The YearPurchase price determin.seq: 01Sales price determination seq: 01List group: CList variant: 01 | The price calculation for the entries made is displayed. Make a note of the final price. |  |
| 4 | Create (or Display) Price Point Group and Assign Price point ranges.Assign Price point Group to Organizational level | Refer to Appendix > Configuration (Optional). |  |  |
| 5 | Make changes to the field Gross Price | On the Create Price Calculation screen, place the cursor in below field and enter a whole value (without any decimal places) and select ENTERGross Price: <new whole value> for example, 6 AED. | Gross Price value entered is displayed as decimal annotation. This is based on price point group defined and the gross price value entered. |  |
| 6 | Make changes to the field Final Price | On the Create Price Calculation screen, place the cursor in below field and enter the same whole value (without any decimal places) entered in step-4 and select ENTERFinal Price: <new whole value> for example, 6 AED | Final Price entered will be shown like how it was entered. There will be no decimal annotation.Note Price point group value will only be relevant for gross price field. |  |
| 7 | Repeat steps | Repeat steps 3 to 6 with the price point group that you have created. |  |  |
| 8 | Save your entries | Select lines that you have changed the prices and select Save.Make a note of the pricing document number. | Pricing document gets created and success message is displayed. |  |
| 9 | Save your entries | Select lines that you have changed the prices and select Save.Make a note of the pricing document number. | Pricing document gets created and success message is displayed. |  |

### Create Pricing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity to enter pricing information in the system with initial status set as inactive.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Pricing Specialist (Retail). |  |  |
| 2 | Access App | Open Create Sales Price Calculation (VKP5) app. | Create Price Calculation: initial screen is displayed. |  |
| 3 | Enter values for Price Calculation fields | On the Create Price Calculation: initial screen, enter following entries and select Execute:Material: R_1051 ( <enter s ingle article > )Sales Organization: 3310Distribution Channel: 40Validity: Today To End Of The YearPurchase price determine .seq: 01Sales price determination seq: 01List group: CList variant: 01 | The price calculation for the entries made is displayed. |  |
| 4 | Create Pricing Document | View the price shown in column Final Price and remember this value.Select the line and go to Menu > Price Calculation > Create Pricing Document . | Pricing document is created, and success message with the number is displayed. |  |

### Display Pricing Document by Material

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity to view the pricing documents created for an article and change the status of the price.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Pricing Specialist (Retail). |  |  |
| 2 | Access App | Open List Pricing Documents - for Articles (VKP3) app. | Pricing Documents for Material, List Display: initial screen is displayed. |  |
| 3 | Enter values for Price Calculation fields | On the Pricing Documents for Material, List Display: initial screen, input following entries and select Execute:Material: R_1051 ( Single article)Sales Organization: 3310Distribution Channel: 40Radio button List of several lines, arranged in blocks: X | Pricing documents (including one created in previous step) is displayed.Status of the pricing document created in previous step will be displayed in status “A” (New, not saved). |  |
| 4 | Change Pricing Document | Select Change Price Calculations. | The chosen line will be editable, and you can change the price or let it remain as is.You will notice the status to be now in ‘B’ (Changed, not saved). |  |
| 5 | Save the Changes | Select the line and select Save. | Price document number is changed. |  |

### Change Price Calculation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity to change the data in the price calculations suggested by the system on the basis of the various default settings (calculation schemas, planned markups, price points). If you compare the selection screens of app - “Create Price Calculation” and “Change Price Calculation”, you can see that they only differ in two flags:

- Create Price Calculation has flag “Pricing levels without general sales price only”. When selecting this, sales price calculation is carried out for materials for which no sales price currently exists.
- Change Price Calculation has flag “Pricing levels with specific sales prices only”. When selecting this, sales price calculation is carried out for materials and organizational levels for which a valid sales price exists.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Pricing Specialist (Retail). |  |  |
| 2 | Access App | Open Maintain Sales Price Calculation (VKP1) app. | Change Price Calculation: initial screen is displayed. |  |
| 3 | Enter values for Price Calculation fields | Make the following entries and select Execute:Material: R_1006 ( Single article)Sales Organization: 3310Distribution Channel: 40Plant: 3341Validity: TodayPurchase price determin.seq: 01Sales price determination seq: 01List group: CList variant: 01 | The price calculation for the entries made is displayed. |  |
| 4 | Change values for price calculation | Change the final price value to any new value. | Final price is changed to new value. |  |
| 5 | Save document | Select all and Save. | Changes made to existing pricing calculation is saved. |  |

### Two-Step Sales Price Calculation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity to create sales price for an article in a two-step sales price calculation scenario.

Stores are occasionally supplied directly by external suppliers. The supplier, on the other hand, is frequently responsible for delivering the items to a company distribution center, from which the articles are distributed to company stores.

A two-step calculation process exists for calculating sales prices to mirror this two-step logistics process. In this, the purchase price of the stores is the transfer price of the distribution center.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Pricing Specialist (Retail). |  |  |
| 2 | Access App | Open Create Sales Price Calculation (VKP5) app. | Create Price Calculation: initial screen is displayed. |  |
| 3 | Enter values for Price Calculation fields | On the Create Price Calculation: Initial Screen, input following entries and select Execute:Material: R_1006 ( Single article)Sales Organization: 3310Distribution Channel: 40, 50Validity: Today To End Of The YearPurchase price determin.seq: 01Sales price determination seq: 01List group: CList variant: 01 | The price calculation for the entries made is displayed.As it is a two-step pricing scenario, for the store distribution chain, the supplier would be distribution center instead of an external vendor.In this case DC 3350 is the suppling site for store 3341.Hence, the vendor would be 3350, which is the BP number of DC 3350.For the distribution chain, supplier is the external supplier. |  |
| 4 | Change Price values | Change article’s transfer price (line with external supplier) field Final Price. | You can notice that this changes the basic purchase price value for the store distribution chain. This is in line with the conversion factor maintained for Unit of Measure (UoM). |  |
| 5 | Save your entries | Select all and select Save.Make a note of the pricing document number. | Pricing document number is generated successfully. |  |

### Display Pricing Document by Article (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity to display lists of pricing documents, arranged by article number.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Pricing Specialist (Retail). |  |  |
| 2 | Access App | Open List Pricing Documents - for Articles (VKP3) app. | Pricing Document for Material, List Display: initial screen is displayed. |  |
| 3 | Enter the selection criteria to display pricing documents | Enter the following values and select Execute:Material: R_1006Sales organization: 3310 | Displays list of pricing documents arranged by article. |  |

### Display Pricing Document by Organization Structure

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity to display lists of pricing documents, arranged by organizational level.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Pricing Specialist (Retail). |  |  |
| 2 | Access App | Open List Pricing Documents - for Organizations (VKP4) app. | Pricing Docs for Organization, List Display: initial screen is displayed. |  |
| 3 | Enter the selection criteria to display pricing documents | Enter the following values and select Execute:Sales Organization: 3310Distribution Channel: 40 | Displays lists of pricing documents arranged by organizational level 3310/40. |  |

### Calculate Sales Price in Background

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity to calculate sales price of a single/generic articles using background job.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Pricing Specialist (Retail). |  |  |
| 2 | Access App | Open Schedule Sales Price Calculation Run (F5412) app. | Application Jobs screen is displayed. |  |
| 3 | Enter all mandatory and relevant job parameters in the job template | Select Create and make the following entries under “Template Section” and select Step 2:Job Template: Retail Sales Price Calculation templateJob Name: Retail Sales Price Calculation templateIn Step 2, enter below details and select Step 3:Start Immediately: XIn Step 3, enter below details and select Check:Material: R_1006 ( Single article)Sales Organization: 3310Distribution Channel: 40Validity: Today To End Of The YearPurchase price determin.seq: 01Sales price determination seq: 04No restrictions on sales price: XList group: CList variant: 01Price Change in percent: -5.00Issue update log check box: XActivate Prices radio button: X | Sales price relevant job parameters are displayed.Error log is shown if any incorrect data is present in job parameters. You must correct them.In case there are no errors you will get message “You can go ahead and schedule the job”. |  |
| 4 | Schedule Job | Select the Schedule in job template. | Job is scheduled. |  |
| 5 | View results | Select Back to view results and select Results in results column to navigate to job results. | Job results is displayed in a separate tab.Pricing calculation table is displayed. |  |
| 6 | Verify Price Changes | Open app Determine Sales PricesEnter details of Article, Sales Organization and Distribution Channel used in Step-3 and select Execute.Select line and Goto > Pricing Document. | Price Overview: initial screen is displayed.Price details are displayed.Pricing document created in Step-4 is displayed. |  |

### Create Pricing Document - Single Article (for Pricing Worklist)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity to create sales price for single articles.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Pricing Specialist (Retail). |  |  |
| 2 | Access App | Open Create Sales Price Calculation (VKP5) app. | Create Price Calculation initial screen is displayed. |  |
| 3 | Enter values for Price Calculation fields | On the Create Price Calculation: initial screen, make the following entries and select Execute:Material: R_1032 ( Single Article )Sales Organization: 3310Distribution Channel: 50, 40Validity: Today To End Of The YearSuppl. (External Procurement): 33213002Purchase price determn.seq: 01Sales price determination seq: 01List group: CList variant: 01 |  |  |
| 4 | Create Pricing Document | Select both lines (corresponding to distribution channel 50 and 40) and select Save.Make a note of the pricing document number.Note The pricing document number created is to be used for entering in the subsequent step to generate the pricing worklist. This is to make the execution of the test steps easier. | Pricing document number is created. |  |

### Change Purchasing Price - Single Article (for Pricing Worklist)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity to change purchasing price for a single article. Sales prices are generally calculated on the basis of the purchase price, which is in turn calculated using the purchase price calculation schema on the basis of condition types affecting pricing (for example, the basic purchase price, supplier discount). Other pricing-relevant parameters including the regular supplier indicator in the purchase info record and the source of supply indicator in the article master data are evaluated in supply source determination.

If the purchase price or the above parameters for source determination change, we recommended to check the existing sales prices with respect to the new margin.

The pricing worklist function allows you to determine all calculations affected by parameter changes.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser (Retail). |  |  |
| 2 | Access App | Open Change Price Conditions - Purchasing (MEK2) app. | Change Condition Records screen is displayed. |  |
| 3 | Enter values for Condition Type field | On the Change Condition Records Screen , enter the following entries and select Key Combination :Condition Type: PPR0 ( Gross Price )Key Combination screen is displayed.Select Material Info Record.Select Choose. | Gross Price selection screen will be displayed. |  |
| 4 | Enter values for selection | On the Change Screen, input the following entries and select Execute:Supplier: 33213002Article:R_1032( Single Article )Purchasing Organization: 3310Info Record Category: 0Valid On: Today’s date | Existing price amount is displayed. |  |
| 5 | Save Price Conditions | Enter a new value in field Amount.Select Save. | Condition records saved. |  |

### Generate Pricing Worklist (Distribution Center Distribution Chain)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity to create pricing worklists.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Pricing Specialist (Retail) |  |  |
| 2 | Access App | Open Generate Sales Price Worklist (WVN0) app. | Pricing Worklist: Generate screen is displayed. |  |
| 3 | Enter values on selection screen for change | On the Pricing Worklist: Generate Screen, input the following entries and select Execute:Document Number: <enter pricing document> number from chapter [Create Pricing Document - Single Article (for Pricing Worklist)](#unique_39) [page ] 44.Pricing Type: Redetermine changed price components, update scalesManual selection of worklist (documents) to be processed: XDelete worklist after processing: X | On the output screen Changeable Documents per Condition: Select Documents, it will display entries for channel 50 (Distribution) and channel 40 (Store Sales).Screen Automatic Document Adjustment: Log (Created on <date>) is displayed. |  |
|  |  | Here select the line with channel 50 (Distribution) and select Update Document. | Screen Automatic Document Adjustment: Log (Created on <date>) is displayed.Here new pricing documents generated is displayed. |  |

### Release Pricing Worklist (Distribution Center Distribution Chain)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity to release the Pricing Worklist.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Pricing Specialist (Retail). |  |  |
| 2 | Access App | Open Release Sales Price Worklist - by Article (WVN1) app. | Release Worklist for Material Screen is displayed. |  |
| 3 | Enter selection screen values | On the Release Worklist for Material Screen, input the following entries and select Execute:Material: R_1032 | In Release Worklist for Material screen, it displays relevant entries. |  |
| 4 | Change new calculated price | On the Release Worklist for Material screen, select the lines and select Change Price Calculations. | Pop-up Display of Price Calculation is displayed. |  |
|  |  | In pop up window Display of Price Calculation enter below fields and select Copy :List Group: CList variant: 01 | In Change Price Calculation screen the new price proposed by the system is displayed. |  |
|  |  | On Change Price Calculation screen, data for relevant channels will be display. These will be in status ‘B’.Here select the line items and select Save. | Pricing document is created. |  |

### Generate Pricing Worklist (Store Distribution Chain)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity to create a pricing worklist record.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Pricing Specialist (Retail). |  |  |
| 2 | Access App | Open Generate Sales Price Worklist (WVN0) app. | Pricing Worklist: Generate screen is displayed. |  |
| 3 | Enter values on selection screen for change | On the Pricing Worklist: Generate Screen, input the following entries and select Execute:Document Number: <enter pricing document number> from chapter [Create Pricing Document - Single Article (for Pricing Worklist)](#unique_39) [page ] 44.Pricing Type: Redetermine changed price components, update scalesManual selection of worklist (documents) to be processed: XDelete w/list after processing: X | On the output screen Changeable Documents per Condition: Select Documents, it will display entries for channel 40 (Store Sales).Here select the line with channel 40 (Store Sales) and select Update Document.Screen Automatic Document Adjustment: Log (Created on <date>) is displayed.Here new pricing documents generated will be displayed. |  |

### Release Pricing Worklist (Store Distribution Chain)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity to release the pricing worklist.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Pricing Specialist (Retail) |  |  |
| 2 | Access App | Open Release Sales Price Worklist - by Article (WVN1) app. | Release Worklist for Material screen is displayed. |  |
| 3 | Enter selection screen values | On the Release Worklist for Material Screen, input the following entries and select Execute:Material: R_1032 | In Release Worklist for Material screen, it shows relevant entries. |  |
| 4 | Change new calculated price | On the Release Worklist for Material screen, select the lines and chose Change Price Calculations. | Pop-up Display of Price Calculation is displayed. |  |
|  |  | In Pop up window Display of Price Calculation enter the below fields and select Copy:List Group: CList variant: 01 | In Change Price Calculation screen the new price proposed by the system is displayed. |  |
|  |  | On Change Price Calculation screen, data for relevant channels will be shown. These will be in status ‘B’.Here select the line items and select Save. | Message is displayed as “Data saved; pricing document <pricing document number> created”. |  |

### Display Price Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity to display and review prices for a number of articles and organizational levels.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Pricing Specialist (Retail). |  |  |
| 2 | Access App | Open Determine Sales Prices (VKP2) app. | Price Overview : initial screen is displayed. |  |
| 3 | Enter values for selection criteria | Make the following entries and select Execute:Article: R_1032 ( Single article)Sales Organization: 3310Distribution Channel: 40, 50, 10Validity: <Date in the past> To End Of The YearList Group: BDisplay Price Origin: X | Sales price condition values is displayed. You see the lines in the output. And lines that have column “Procedure in SP Calculations” value ‘11’ suggests that these price changes were done by the pricing worklist steps. |  |

### Generate Pricing Worklist in Background

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity to create a pricing work list record in background through scheduled application jobs. In case the prerequisites are met (for example change in purchase price), then this background run generates the pricing worklist.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Pricing Specialist (Retail) |  |  |
| 2 | Create Sales Price | Repeat the step described in chapter [Create Pricing Document - Single Article (for Pricing Worklist)](#unique_39) [page ] 44. | Pricing document number will be created. Make a note of this number. |  |
| 2a | Change Purchasing Price | Repeat the step described in chapter [Change Purchasing Price - Single Article (for Pricing Worklist)](#unique_40) [page ] 45. |  |  |
| 3 | Access App | Open Schedule Generation of Sales Price Worklist | Application Jobs screen is displayed. |  |
| 4 | Enter all mandatory and relevant job parameters in the job template | Select Create and make the following entries under “Template Section” and select Step 2:Job Template: Pricing Worklist Generate job TemplateJob Name: <Enter your job name>In Step 2, enter below details and select Step 3Start Immediately: XIn Step 3, enter below details and select CheckDocument Number: <Enter Pricing Document Number from step-2>.Delete worklist after processing: X | Generate pricing worklist relevant job parameters will be displayed.Error log is displayed, if any incorrect data in Job parameters. You must correct them.In case there are no errors you will get message “You can go ahead and schedule the job”. |  |
| 4 | Schedule Job | Select Schedule in the job template. | Job is scheduled. |  |
| 5 | View results | select Back to view results and select the Results in results column to navigate to job results. | Job results will be displayed in separate tab.Pricing calculation table will be displayed. |  |

|  |
| --- |
| Note You can proceed to release the pricing worklist as described in chapter [Release Pricing Worklist (Distribution Center Distribution Chain)](#unique_42) [page ] 47 or chapter [Release Pricing Worklist (Store Distribution Chain)](#unique_44) [page ] 49. |

### Create Supplier (Vendor) Discount Condition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity to create supplier discount condition at purchasing organization and supplier level.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser (Retail) |  |  |
| 2 | Access App | Open Create Price Conditions-Purchasingapp. | Create Condition Records screen is displayed. |  |
| 3 | Enter values for Condition Type field | On the Create Condition Records Screen , input the following entries and select Key Combination:Condition Type: DL01 ( Vendor Discount ) | Select Vendor. |  |
| 4 | Enter values for creation | On the Create Screen, enter the following entries:Purchasing Organization: 3310Supplier: 33213002Amount: 10Unit: %Valid From: Today’s dateValid From: <End of Year> |  |  |
| 5 | Press Save | Select Save. | Condition records are saved. |  |

### Displaying Purchasing Conditions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity to display pricing condition record created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser (Retail). |  |  |
| 2 | Access App | Open Maintain Purchasing Conditions (MEKA) app. | Purchasing Conditions screen is displayed. |  |
| 3 | Enter values for Condition Type field | On the Purchasing Conditions Screen , input the following entries and select Execute:Purchasing Organization: 3310Supplier: 33213002Scope of List: 0001 | Value entered for vendor discount from previous step is displayed. |  |

### Create Freight Condition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity to create freight value condition for the article.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data (Retail) |  |  |
| 2 | Access App | Open Maintain Article (MM42) app. | Change Material (Initial Screen) is displayed. |  |
| 3 | Enter values for selection | On the Change Material (Initial Screen) , input the following entries and select Continue:Material: R_1006 ( Single Article )Purchasing Org. 3310Supplier 33213002Select Purchasing | Change Material (Purchasing) screen is displayed. |  |
| 4 | Traverse to Condition screen | On the Change Material (Purchasing) screen, select Conditions. | If there are more than one validity periods maintained for the article, then a pop-up Validity Period: Conditions is displayed.Select the latest validity period. |  |
| 5 | Enter new condition type | In Change Default Price Condition screen, enter following values and select Save:Condition Type: FVA1 ( Freight value )Amount. <any amount>Unit: AED | A message indicating Material R_1006 changed is displayed. |  |

### Reset Site-Specific Price and Price List Price

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity to delete site-specific prices and price list prices for an article.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Pricing Specialist (Retail) |  |  |
| 2 | Access App | Open Determine Sales Prices (VKP2) app. | Price Overview: Initial Screen is displayed. |  |
| 3 | Enter values for selection (to review prices for article existing at site specific and price list specific pre-deletion) | Make the following entries and select Execute:Material: R_1006 <or enter your test article that has site specific and/or price list price maintained>Sales Organization: 3310Distribution Channel: 40Plant: 3341Pricelist: P4Validity: Today To End Of The YearDisplay distribution chain and plant/price list separately: XUse all units of measure of the material: XList Group: A | Sales price relevant for the selection criteria is displayed.Note Here observe that sales price calculation done for distribution chain specific line will be different from that of price list specific line and site-specific line.Make a note of these prices and also the pricing levels. |  |
| 4 | Access App | Open Create Sales Price Calculation . | Create Price Calculation screen is displayed. |  |
| 5 | Enter values for selection (to delete prices for article existing at site specific and price list specific) | On the Create Price Calculation: Initial Screen , input the following entries and select Execute :Material: R_1006 <or enter your test article that has site specific and/or price list price maintained>Sales Organization 3310Distribution Channel 40Validity: Today+1 To End of the YearPurchase Price Determ. Seq.: 01Sales price determination seq.: 02List Group: CList Variant: 01Note if you want to delete all site specific and/or price list specific prices, do not enter any site and/or price list on selection screen.If you want to retain site specific price for this site, you have to enter this site on the selection screen.If you want to retain price list specific price for this price list, you have to enter this price list on selection screen. |  |  |
| 6 | Select line | On the Create Price Calculation screen, select the Distribution chain line and flag the following:D (Delete Plant Prices): Xand select Save.Note For site ID and price list ID potentially visible on screen, the prices for these are not reset. | The system deletes all site-specific prices for site IDs that are not shown on the screen.Pricing document is created. |  |
| 7 | Access App | Open Determine Sales Prices. | Price Overview: Initial Screen is displayed. |  |
| 8 | Enter values for selection (to review prices for article existing at site specific and price list specific post-deletion) | Make the following entries and select Execute:Material: R_1006 <or enter your test article that has site specific and/or price list price maintained>Sales Organization: 3310Distribution Channel: 40Plant: 3341Pricelist: P4Validity: Today To End Of The YearDisplay distribution chain and plant/price list separately: XUse all units of measure of the material: XList Group: A | You will see adjusted price levels and validity periods for site 3341.In this example, since price list price exists, this price is valid for site 3341. |  |
| 9 | Access App | Open Create Sales Price Calculation. | Create Price Calculation screen is displayed. |  |
| 10 | Enter values for selection (to delete prices for article existing at site specific and price list specific) | On the Create Price Calculation: Initial Screen , input the following entries and select Execute:Material: R_1006 <or enter your test article that has site specific and/or price list price maintained>Sales Organization 3310Distribution Channel 40Validity: Today+1 To End of the YearPurchase Price Determ. Seq.: 01Sales price determination seq.: 02List Group: CList Variant: 01Note if you want to delete all site specific and/or price list specific prices, do not enter any site and/or price list on selection screenIf you want to retain site specific price for this site, you have to enter this site on the selection screen.If you want to retain price list specific price for this price list, you have to enter this price list on selection screen. |  |  |
| 11 | Select line | On the Create Price Calculation screen, select the distribution chain line flag the following:P (Delete SitePrList Prices): Xand select SaveAnd select Enter in the pop-up window.Note For site ID and price list ID potentially visible on screen, the prices for these are not reset. | The system deletes all price list-specific prices for price list IDs that are not displayed on the screen.Pricing document is created. |  |
| 12 | Access App | Open Determine Sales Prices. | Price Overview: Initial Screen is displayed. |  |
| 13 | Enter values for selection (to review prices for article existing at site specific and price list specific post-deletion) | Make the following entries and select Execute:Material: R_1006 ( Single article)Sales Organization: 3310Distribution Channel: 40Plant: 3341Pricelist: P4Validity: Today To End Of The YearDisplay distribution chain and plant/price list separately: XUse all units of measure of the material: XList Group: A | You will see adjusted price levels and validity periods for price list P4.In this example, since distribution chain price exists, this price will be valid for site 3341. |  |

### Maintain Wholesale Prices

|  |
| --- |
| Note In general, all steps mentioned above are relevant for distribution channel 10.However, test procedure step "two-step sales price calculation" is not relevant for wholesale. |

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
> Flagged while digesting this document, not verified: Business role mismatch: the Overview Table lists 'Master Data Specialist - Product Data (Retail)' for Maintain Price List Type for Site and Merchandise Category (WB30N), but the test procedure's log-on step uses 'Master Data Specialist - Location Data (Retail)'.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[15-retail-operations/test-script-retail-promotions-637-ae-sap-s-4hana-cloud-public-edition]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3I4_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 101,534 chars in the whole document
