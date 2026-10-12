---
id: 15-retail-operations/test-script-sales-price-valuation-for-retail-5ft-ae-sap-s-4hana-cloud
title: "Test Script: Sales Price Valuation for Retail (5FT_AE) - SAP S/4HANA Cloud Public Edition (5FT_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script (scope item 5FT, AE) for sales price valuation and revaluation in retail, with roles, sample data and step-by-step Fiori test procedures."
cluster: 15-retail-operations
tags: [kb/retail-operations, topic/retail-sales-price-valuation]
aliases: [5FT_S4CLD2608_BPD_EN_AE]
keywords: [Sales Price Valuation for Retail, sales price revaluation, valuation at retail, initialize valuation, sales price calculation, stock overview, business roles, master data, purchase orders, inbound delivery]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5FT_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1088
topic: 15-retail-operations/retail-sales-price-valuation
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Sales Price Valuation for Retail (5FT_AE) - SAP S/4HANA Cloud Public Edition (5FT_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5FT_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Sales Price Valuation for Retail** in Retail Operations. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Sales Price Valuation for Retail (5FT_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232856813)

[2 Prerequisites 4](#_Toc232856814)

[2.1 System Access 4](#_Toc232856815)

[2.2 Roles 4](#_Toc232856816)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232856817)

[2.4 Preliminary Steps 6](#_Toc232856818)

[2.4.1 Check Stock Availability for Article 6](#_Toc232856819)

[2.4.2 Set Initial Stock for Article (Optional – Only if Stock not available) 6](#_Toc232856820)

[2.4.3 Create Sales Price Calculation 7](#_Toc232856821)

[2.4.4 Send Transmission with API Client Tools (Optional) 9](#_Toc232856822)

[2.4.5 Transmission Example: Aggregated Sales – Payload to be used (Optional) 10](#_Toc232856823)

[3 Overview Table 12](#_Toc232856824)

[4 Test Procedures 14](#_Toc232856825)

[4.1 Run Automatic Sales Price Revaluation 14](#_Toc232856826)

[4.1.1 Execute Revaluation Run: Retail Inventory - Option 1 14](#_Toc232856827)

[4.1.2 Schedule Job for Automatic Revaluation at Retail - Option 2 16](#_Toc232856828)

[4.2 Create Sales Price Revaluation (VKU1) 17](#_Toc232856829)

[4.3 Display Sales Price Revaluation Documents (VKU4) 19](#_Toc232856830)

[4.4 Initialize or Correct Valuation at Retail 20](#_Toc232856831)

[4.4.1 Initialize Valuation: Retail Inventory – Option 1 20](#_Toc232856832)

[4.4.2 Schedule Job for Initialization of Valuation at Retail – Option 2 22](#_Toc232856833)

[4.5 Display Stock Overview Including Sales Price Values 23](#_Toc232856834)

[4.6 Create Purchase Order (Optional) 24](#_Toc232856835)

[4.7 Display Stock Overview Including Sales Price Values 26](#_Toc232856836)

[4.8 Create Inbound Delivery (Optional) 27](#_Toc232856837)

[4.9 Display Stock Overview Including Sales Price Values 27](#_Toc232856838)

[4.10 Post Goods Receipt for Inbound Delivery (Optional) 28](#_Toc232856839)

[4.11 Display Stock Overview Including Sales Price Values 29](#_Toc232856840)

[4.12 Create Supplier Invoice Using Purchase Order (Optional) 30](#_Toc232856841)

[4.13 Display Stock Overview Including Sales Price Values 32](#_Toc232856842)

[4.14 Transfer Products (Store to Store - Optional) 33](#_Toc232856843)

[4.15 Display Stock Overview Including Sales Price Values 34](#_Toc232856844)

[4.16 Process Aggregated Sales from POS – Receive Aggregated Sales (Optional) 35](#_Toc232856845)

[4.17 Schedule Job for Posting of POS Inbound for Sales (Optional) 36](#_Toc232856846)

[4.18 Display Stock Overview Including Sales Price Values 38](#_Toc232856847)

[4.19 Display Material Inventory Values Including Sales Price (Optional) 39](#_Toc232856848)

## Purpose

Overview

Stock valuation for all articles carried in stores and distribution centers is mandatory, as it serves as foundation for balance sheet accounting and legally required financial closing statements. This cost-based stock valuation comes in two flavors: moving average cost (determined by averaging purchase cost in goods receipts) or standard prices (which are fixed during a validity period).

In addition to valuation at cost, many retailers require that valuation at expected sales prices is carried in parallel. This allows retailers to always have up-to-date margin information at hand as a basis for crucial merchandising decisions, such as how to build their assortments. Furthermore, having valuation at cost and sales prices in tandem is required for most planning and reporting activities. Valuation at sales prices can be used for both stores and distribution centers. Sales price values are determined for all article movements (for example goods receipts or goods issues), and stored in the respective article documents.

There are two basic reasons for sales price revaluations of stock:

- The adjustment of planned sales prices (for example, as a result of a new sales price calculation). An automatic sales price revaluation can be performed to adjust the inventory valuation.
- Sales price revaluation can be performed manually, due to the changed condition of an article (for example, if the article is outdated, or inventory is damaged).

In both scenarios, sales price revaluation documents are created to support reporting and auditing.

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
| System | Accessible through SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps/visually harmonized transactions assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) |
| --- | --- | --- | --- |
| Pricing Specialist (Retail) | SAP_BR_PRICING_SPCLST_RFM | Retail Sales Price Revaluation | SAP_BR_PRICING_SPCLST_RFM |
| Allocator (Retail) | SAP_BR_ALLOCATOR_RETAIL | Allocation and Merchandise Distribution | SAP_BR_ALLOCATOR_RETAIL |
| Purchaser (Retail) | SAP_BR_PURCHASER_RFM | Retail Purchasing / Retail Sourcing and Contracting | SAP_RFM_SPT_PURCHASING_PC / SAP_RFM_SPT_SOURCING_PC |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT |
| Warehouse Clerk (Retail) | SAP_BR_WAREHOUSE_CLERK_RFM | Articles Management -Warehouse Management | SAP_BR_WAREHOUSE_CLERK_RFM |
| Retail Store Associate | SAP_BR_RFM_STORE_ASSOCIATE | Retail Store Associate | SAP_BR_RFM_STORE_ASSOCIATE |
| Receiving Specialist | SAP_BR_RECEIVING_SPECIALIST | Receiving | SAP_BR_RECEIVING_SPECIALIST |
| Administrator (Retail) | SAP_BR_ADMINISTRATOR_RFM | Administration - Retail | SAP_BR_ADMINISTRATOR_RFM |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents articles, customers, and Sites, for example, depending on the operational focus of your company.

Use your own master data or the following sample data to go through the test procedure.

|  |
| --- |
| Note In the following table, sample values for master data are provided for the country/region US. You can either use the country-dependent sample master data or create and use your own master data while executing the test procedure. |

| Master / Org. Data | Value | Master / Org. Data Details | Comments |
| --- | --- | --- | --- |
| Article | R_1039 | My Best bread roll - italian |  |
| Article | R_1040 | My Best bread roll - classic |  |
| Material Group | R1171001 | Bread |  |
| Plant | 3341 | Store 3341 AE |  |
| Sales Organization | 3310 | Dom. Sales Org |  |
| Distribution Channel | 40 | Store Sales |  |
| Purchasing Organization | 3310 | Purch. Org. 3310 |  |
| Supplier | 33213002 | Retail Food Supplier AE |  |
| Purchasing Group | 001 | Group 001 |  |
| Company Code | 3310 | Company Code 3310 |  |
| Storage Location | 994A | St.Loc.Neg.Stock |  |

### Preliminary Steps

#### Check Stock Availability for Article

Use

To execute this scope item, the article have stock available in unrestricted category.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Warehouse Clerk (Retail) |  |  |
| 2 | Access the app | Open Display Advanced Stock Overview (RWBE) app. |  |  |
| 3 | Enter details | Make the following entry and select Execute :Material: R_1039Under Plant selectionPlant: for example 3341 | The Stock Overview: Full List screen is displayed. |  |
| 4 | Check stock | Select the Plant and select Expand subtree. | For the specified plant and storage location, the unrestricted stock exists. |  |

Result

Unrestricted stock is checked for the articles.

#### Set Initial Stock for Article (Optional – Only if Stock not available)

Use

To execute this scope item, the article must be available in stock. If there is no stock available for the item in question, do the following preliminary procedures.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Warehouse Clerk (Retail) |  |  |
| 2 | Access the app | Open Post Goods Movement (MIGO) app.If it was your most recent transaction. As a result, the user chooses Reference Document for Transaction > Other as their action. | The Goods Receipt Other – XXXX screen is displayed. |  |
| 3 | Input movement type | Make the following entry and select Enter:Executable Action in Transaction: Goods ReceiptReference Document for Transaction: Other |  |  |
| 4 | Enter article | On the Goods Receipt Other screen: Material tab, make the following entry and select Enter:Material : R_1039 | Material details are displayed. |  |
| 5 | Enter quantity data | On the Goods Receipt Other screen: Quantity tab, make the following entry and select Enter :Qty in Unit of Entry: 100Unit of Entry: CAR | Material details are updated with quantity and unit of entry. |  |
| 6 | Input on the goods receipt other screen: where tab | On the Goods Receipt Other screen: Where tab, make the following entries and select Enter:Movement Type: 561 (Receipt per initial entry of stock balances into unr.-use)Plant: for example 3341Storage Location: for example 994A | Material details are updated with goods movement type, plant, and storage location. |  |
| 7 | Save your entries | Select Post. | Material document <XXXX > posted message displayed. |  |

Result

Stock is created for the articles.

#### Create Sales Price Calculation

Use

Price modifications for the corresponding materials of the needed shop are required to proceed with the sales price revaluation. By following the steps below, you can adjust the price of an article through a transaction.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Log on to the SAP Fiori launchpad as a Pricing Specialist (Retail) |  |  |
| 2. | Access app | Open Create Sales Price Calculation (VKP5) app. | Create Price Calculation Initial screen is displayed. |  |
| 3. | Enter values for price calculation fields | On the Create Price Calculation: Initial Screen, Provide following entries.Under Pricing levels section:Material: R_1039 (Single article)Sales Organization: for example 3310Distribution Channel: 40Plant: for example 3341Validity : Today To End Of The YearUnder Pricing Procedure Section:Purchase Price Determ.seq . : 01Sales price determination seq . : 01Under Display options Section:List group : CList variant : 01Select Execute. | The price calculation for the entries made is displayed. |  |
| 4. | Create pricing document | Change the price shown in column Final Price and select SaveNote If Error as a Result of Overlapping Validity Periods pop up message is displayed, select thevalidity period in Overlapping conditions and select Enter in the popup window.If there are more than 1 line items in the output screen, change the final price for all the line items by select all option in Table selection menu. | Pricing document is created, and the system displays the following message: Data saved; pricing document <Pricing_Document_Number>created |  |

Result

With the creation of price calculation, you will be able to do the revaluation as described in this business process.

|  |
| --- |
| Note This step is the prerequisite for execution for each revaluation.For distribution center (Site: for example 3341), there is a possibility to practice the valuation at retail, with retail price by maintaining the sales organization (for example 3310) and the distribution channel (50) |

#### Send Transmission with API Client Tools (Optional)

Purpose

The process is to simulate sending transmission for testing the aggregated POS sales scenario ([Process Aggregated Sales from POS – Receive Aggregated Sales (Optional)](#unique_11) [page ] 35). Here API client tools used as an example.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Results | Comment |
| --- | --- | --- | --- | --- |
| 1 | Get the test tool API client tools | Please refer to Download and Install API client tools in Set Up Instruction Store Connectivity – Inbound (3HV) if API client tools is not already installed. |  |  |
| 2 | Create collection | select New > Collection at the top left of the screen and make the following entry:Name: Enter the name for your identificationSelect Create |  |  |
| 3 | Create request | Find the collection just created on the left side of the screen. select View more actionsSelect Add Request from the drop-down list and make the following entry:Request Name: Enter the name for your identificationSelect Save tocollection name defined in previous step |  |  |
| 4 | Maintain request | Select the request just created on the left side of the screen under the collection and make the following entry for the details display on the right side of the screen:Change the action from GET to POSTEnter request URL:For Sales Transaction Service:HYPERLINK "https://<Subdomain>/sap/bc/srt/scs_ext/sap/possalestransactionscreaterequ"https://<Subdomain>/sap/bc/srt/scs_ext/sap/possalestransactionscreaterequFor Financial Transaction Service:HYPERLINK "https://<Subdomain>/sap/bc/srt/scs_ext/sap/posfinancialtransactionscreatehttps://<Subdomain>/sap/bc/srt/scs_ext/sap/posfinancialtransactionscreateParams – MessageID for e.g. 989C3E3A-4CD9-21CA-A200-12002B4CA1B4Select Authorization tab, select TYPE: Basic Auth, maintain Username and PasswordSelect Headers tab and add one line entry with the followings:KEY: Content-TypeVALUE: text/xmlSelect Body tab, select the radio button of RawFill in transmission details, as described in the chapter [Create Sales Price Calculation](#unique_9) [page ] 7Select Save. |  | <POS Service URL> canget after following setting up instruction guide for 3HV Set Up Instruction chapter Download and Install API client toolsTechnical User maintained for the Basic Auth. Please refer to setting up scope item 3HV for how to create technical user Technical User for Transmission Receiver API. |
| 5 | Send the transmission | Select Send from the upper right of the screen. | After successful posting Administrator checks:Status Accepted in API client tools.The persisted messages in the Interface Monitor (Deprecated) (/AIF/IFMON) app. |  |

#### Transmission Example: Aggregated Sales – Payload to be used (Optional)

|  |
| --- |
| Note Before executing any payload make sure you have the unique service call reference ID value. If you have used an existing value, then you will not get the expected result. |

<?xml version="1.0" encoding="UTF-8"?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<soapenv:Body>
<n0:PosSalesTransactionsCreateRequest xmlns:n0= "http://sap.com/xi/SAPGlobal20/Global">
<MessageHeader>
<CreationDateTime>2021-04-02T12:00:00.1234567Z </CreationDateTime>
<SenderBusinessSystemID><SENDER_SYSID ></SenderBusinessSystemID>
<RecipientBusinessSystemID><RECEIVER_SYSID></RecipientBusinessSystemID>
</MessageHeader>
<PosSalesTransactions>
<ServiceCallReferenceID>2021-04-03-00</ServiceCallReferenceID>
<StoreInternalID>3341</StoreInternalID>
<SalesTransactionsDate>2021-03-07</SalesTransactionsDate>
<AggregatedSalesByProduct>
<SequenceNumber>1</SequenceNumber>
<GlobalTradeItemNumber/>
<ProductInternalID>R_1039</ProductInternalID>
<RetailPromotion/>
<TotalAmount currencyCode="AED">167</TotalAmount>
<TotalQuantity unitCode="PCE">1</TotalQuantity>
<Tax>
<ProductTaxClassification>0</ProductTaxClassification>
</Tax>
</AggregatedSalesByProduct>
</PosSalesTransactions>
</n0:PosSalesTransactionsCreateRequest>
</soapenv:Body>
</soapenv:Envelope>

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Run Automatic Sales Price Revaluation](#unique_14) [page ] 14 | Pricing Specialist (Retail) | Execute Revaluation Run - Retail Inventory (VKU7) |  |
| [Execute Revaluation Run: Retail Inventory - Option 1](#unique_15) [page ] 14 | Pricing Specialist (Retail) | Execute Revaluation Run - Retail Inventory (VKU7) |  |
| [Schedule Job for Automatic Revaluation at Retail - Option 2](#unique_16) [page ] 16 | Pricing Specialist (Retail) | Schedule Automatic Total Revaluation at Retail (F5394) |  |
| [Create Sales Price Revaluation (VKU1)](#unique_17) [page ] 17 | Pricing Specialist (Retail) | Maintain Revaluation - Retail Inventory (VKU1) |  |
| [Display Sales Price Revaluation Documents (VKU4)](#unique_18) [page ] 19 | Pricing Specialist (Retail) | List Revaluation Documents - Retail Inventory (VKU4) |  |
| [Initialize or Correct Valuation at Retail](#unique_19) [page ] 20 | Pricing Specialist (Retail) | Initialize Valuation - Retail Inventory (VKU10) |  |
| [Initialize Valuation: Retail Inventory – Option 1](#unique_20) [page ] 20 | Pricing Specialist (Retail) | Initialize Valuation - Retail Inventory (VKU10) |  |
| [Schedule Job for Initialization of Valuation at Retail – Option 2](#unique_21) [page ] 22 | Pricing Specialist (Retail) | Schedule Initialization of Valuation at Retail (F5393) |  |
| [Display Stock Overview Including Sales Price Values](#unique_22) [page ] 23 | Allocator (Retail) | Display Advanced Stock Overview (RWBE) |  |
| [Create Purchase Order (Optional)](#unique_23) [page ] 24 | Purchaser (Retail) | Create Purchase Order - Advanced (ME21N) |  |
| [Display Stock Overview Including Sales Price Values](#unique_24) [page ] 26 | Allocator (Retail) | Display Advanced Stock Overview (RWBE) |  |
| [Create Inbound Delivery (Optional)](#unique_25) [page ] 27 | Receiving Specialist |  |  |
| [Display Stock Overview Including Sales Price Values](#unique_26) [page ] 27 | Allocator (Retail) | Display Advanced Stock Overview (RWBE) |  |
| [Post Goods Receipt for Inbound Delivery (Optional)](#unique_27) [page ] 28 | Receiving Specialist | Change Inbound Delivery (VL32N) |  |
| [Display Stock Overview Including Sales Price Values](#unique_28) [page ] 29 | Allocator (Retail) | Display Advanced Stock Overview (RWBE) |  |
| [Create Supplier Invoice Using Purchase Order (Optional)](#unique_29) [page ] 30 | Accounts Payable Accountant | Create Supplier Invoice - Advanced (MIRO) |  |
| [Display Stock Overview Including Sales Price Values](#unique_30) [page ] 32 | Allocator (Retail) | Display Advanced Stock Overview (RWBE) |  |
| [Transfer Products (Store to Store - Optional)](#unique_31) [page ] 33 | Retail Store Associate | Transfer Products (F2449) |  |
| [Display Stock Overview Including Sales Price Values](#unique_32) [page ] 34 | Allocator (Retail) | Display Advanced Stock Overview (RWBE) |  |
| [Process Aggregated Sales from POS – Receive Aggregated Sales (Optional)](#unique_11) [page ] 35 | Administrator | simulate using API client tools |  |
| [Schedule Job for Posting of POS Inbound for Sales (Optional)](#unique_33) [page ] 36 | Administrator | Schedule POS Inbound Service (F5236) |  |
| [Display Stock Overview Including Sales Price Values](#unique_34) [page ] 38 | Allocator (Retail) | Display Advanced Stock Overview (RWBE) |  |
| [Display Material Inventory Values Including Sales Price (Optional)](#unique_35) [page ] 39 | Inventory Manager | Material Inventory Values - Balance Summary (F1422) |  |

## Test Procedures

This chapter describes test procedures for each process step that belongs to this scope item.

### Run Automatic Sales Price Revaluation

#### Execute Revaluation Run: Retail Inventory - Option 1

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how you create the revaluation documents for all the articles after a retail sales price change has happened within a specified duration for the selected articles and site.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Pricing Specialist (Retail) |  |  |
| 2 | Access the app | Open Execute Revaluation Run - Retail Inventory (VKU7) app. | The Automatic Total Revaluation at Retail: Selection screen is displayed. |  |
| 3 | Provide input values | On the initial screen, make the following entry under Selection criteria Section and select below radio button and checkboxes:Date of retail price change : <dd/mm/yyyy>Note The date that you enter here is the same one which you have used in the create sales price calculation, as in preliminary step. Do not mention past dates.Plant : for example 3341Sales Organization : for example 3310Distribution Channel : 40Check if the following Radio button is selected:Under Automatic revaluation at retail Section:All materials with qty-based inventory management without countingCheck if the following checkboxes are selected:Under Additional options section:Create log for revaluations at retailCreate error log for revaluations at retailUnder Price fixing section:Ignore suggested retail pricesIgnore fixed pricesCheck if the following Radio button is selected:Under List Display selection:Single – Line List,Select Execute. | All entries are accepted. |  |
| 4 | Check the revaluation result | Check if any retail price changes happened for the period selected.Note If there is retail price change for any materials of the specified Site, there will be line items with the respective material detailsIf no retail price changes happened, it will display “No Items to Display” | Retail sales price revaluation happens for the selected articles. |  |
| 5 | Check log for revaluation at retail for the plant | Select Back which is next to SAP Icon. | Short log for revaluation at retail for the plant is displayed. |  |
| 6 | Save | Select Save to PC file You can save the records in any of the given format | Data is saved. |  |

|  |
| --- |
| Note For distribution centre (Site: for example 3341), there is a possibility to practice the valuation at retail, with retail price by maintaining the sales organization (for example 3310) and the distribution channel (50). |

#### Schedule Job for Automatic Revaluation at Retail - Option 2

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

This process step shows you how you can revaluate the inventory of an article which has undergone price change. This scope items performs the same activity as Option 1, but in the background. A document is created that contains all the information pertaining to the Job. You can only create job if you have the necessary authorization.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Pricing Specialist (Retail). |  |  |
| 2 | Access the app | Open Schedule Automatic Total Revaluation at Retail (F5394) app. |  |  |
| 3 | Provide input values | On the initial screen, select Create and make the following entry in selection criteria:Job Template: Schedule Automatic Total Revaluation at RetailJob Name: Schedule Automatic Total Revaluation at RetailSelect Step-2Check if Start Immediately checkbox is selected,Select Step-3 and make the following entry in Selection Criteria:Select parameters Under Selection Criteria section:Start Date: Retail Price Change: <dd.mm.yyyy>End Date: Retail Price Change: <dd.mm.yyyy>Note The date that you enter here is the same one which you have used in the Create Sales Price Valuation, as in preliminary step. Do not select past date.Plant: for example 3341Sales Organisation: for example 3310Distribution Channel: 40Check if the following checkboxes and Radio buttons are selected:Under Automatic revaluation at retail:All Products w/o counting XUnder Additional options:Log revaluation at retail: XError log, revaluation at rtl:XUnder Price fixing:Ignore fixed prices:XUnder List display:Multiline List: X |  |  |
| 4 | Check | Select Check for validating. | Message is displayed as You can go ahead and schedule the job. |  |
| 5 | Schedule | Select Schedule and following message is displayed Job Application job template for sales price valuation has been scheduled. |  |  |
| 6 | Check Job Results | On the Application Jobs screen, after job item status turned to Finished, select Navigate to the job results in the Results column. | Document (ID XXXXXX) is displayed with revaluation job results. |  |

### Create Sales Price Revaluation (VKU1)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how you create the revaluation documents for all the articles that have undergone a price change within the specified duration and for selected site.

This test step is an alternative for the transaction VKU7 (recommended step).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Pricing Specialist (Retail) |  |  |
| 2 | Access the app | Open Maintain Revaluation - Retail Inventory (VKU1) app. | The Revaluation at Retail for Retail Prices Changes is displayed. |  |
| 3 | Provide input values | On the initial screen, make the following entry in selection criteriaDate of retail price change : mm/dd/yyyy to mm/dd/yyyyNote The date that you enter here is the same one which you have used in the Create Sales Price Valuation, as in preliminary step. Do not select the past date.Plant : for example 3341Sales Organization : for example 3310Distribution Channel : 40Under Scope of list of rtl changes :select radio button All materials with retail price changesUnder Restrictions Check if the following checkbox is selected:Display retail price changes only for materials with stockUnder Additional Options Check if the following checkbox is selected:Create error log for retail price changesUnder Automatic revaluation at retail :Select the following Radio button:All materials with qty based inventory managementUnder Price fixing Check if the following checkbox is selected:Ignore suggssted retail pricesIgnore fixed pricesUnder List Display :Check if the following Radio button is selected:Single – Line ListSelect execute. | All the entries are accepted successfully. |  |
| 4 | Check for the list of materials gets displayed sorted by date of posting | Check for the list of materials gets displayed sorted by date of posting. | List of materials get displayed. |  |
| 5 | Exit | Select Back and Exit. | Back to initial screen. |  |

|  |
| --- |
| Note For distribution centre (Site: for example 3341), there is a possibility to practice the valuation at retail, with retail price by maintaining the sales organization, for example (3310) and the distribution channel (50) . |

### Display Sales Price Revaluation Documents (VKU4)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how you can display the list of revaluation documents created as part of the above process [Run Automatic Sales Price Revaluation](#unique_14) [page ] 14 Run Automatic Sales Price Revaluation and [Create Sales Price Revaluation (VKU1)](#unique_17) [page ] 17 Create Sales Price Revaluation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Pricing Specialist (Retail) |  |  |
| 2 | Access the app | Open List Revaluation Documents - Retail Inventory (VKU4) app. |  |  |
| 3 | Provide input values | On the initial screen, make the following entry in selection criteria and restriction:Revaluation at Retail Year : yyyyRtl Price Change Date : mm/dd/yyyy to mm/dd/yyyyNote The date that you enter here is the same one which you have used in the [Create Sales Price Revaluation (VKU1)](#unique_17) [page ] 17, as in preliminary step. Do not select the past date.Plant : for example 3341Posting date : date of execution of VKU1Select Execute. | All entries are accepted. |  |
| 4 | Check for the list of materials gets displayed sorted by date of posting | Check for the list of materials gets displayed sorted by date of posting. | List of materials is displayed. |  |
| 5 | Save | Select Back and End list display single – line Pop-up box appears with message as Switch to ABAP list display? For detailed view and to save the file and select Yes. | Detailed list is displayed.(Select save to PC file if you want to download it.) |  |

### Initialize or Correct Valuation at Retail

#### Initialize Valuation: Retail Inventory – Option 1

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how you can in addition to generation of revaluation documents, also corrects revaluation at retail for either one or multiple articles for any inconsistencies, for example, revaluation has not occurred at regular intervals for every change in the system's sales price or if we only wish to correct revaluation for specific article.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Pricing Specialist (Retail) |  |  |
| 2 | Access the app | Open Initialize Valuation - Retail Inventory (VKU10) app. |  |  |
| 3 | Provide input values | On the initial screen, make the following entry:Plant : for example 3341Sales Organization : for example 3310Distribution Channel : 40Date of Retail P rice Change : mm/dd/yyyyNote The date that you enter here is the same one which you have used in the [Create Sales Price Revaluation (VKU1)](#unique_17) [page ] 17, as in preliminary step. Do not select the past date.Reason for revaluation : 1Under Scope of ListSelect the following Radio button:Display all revaluated materials without any additional infoUnder Addit. Options, check if below checkbox is selected:Generate success/error logSelect Execute. | Initialization/Correction of Valuation at Retail Revaluation screen is displayed. |  |
| 4 | Check for the list of revaluated materials gets displayed | Check for the list of revaluated materials managed on a quantity and value basis is displayed. | List of revaluated materials managed on a quantity and value basis is displayed. |  |
| 5 | Check old and new retail prices of each material is same or different | Select on each material and check old and new retail prices of the material is same or different. | The old and new retail prices of each material can be same or different will be displayed with a popup screen. |  |
| 6 | Save | Select Back and Select Save. Save the records in any of the given format. | Data is saved. |  |

|  |
| --- |
| Note For Distribution centre (Site: for example 3341), there is a possibility to practice the valuation at retail, with retail price by maintaining the Sales organization (for example 3310) and the Distribution channel (50). |

#### Schedule Job for Initialization of Valuation at Retail – Option 2

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to do the adjustment of planned sales prices, for example, the results of a new price calculation for sales An automatic revaluation of the sales price can be performed here, updating the site inventory valuation correspondingly. This scope items performs the same activity as test procedure [Initialize Valuation: Retail Inventory – Option 1](#unique_20) [page ] 20, but in the background. This test step is an automated alternative of transaction VKU10 (recommended step).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Pricing Specialist (Retail) |  |  |
| 2 | Access the app | Open Schedule Initialization of Valuation at Retail (F5393) app. |  |  |
| 3 | Provide input values | On the initial screen, make the following entry in selection criteria and restrictionSelect CreateJob Template : Schedule Initialization of Valuation at RetailJob Name : Schedule Initialization of Valuation at RetailSelect Step2Select Step3Select parameters for Selection Criteria :Plant : for example 3341Sales Organisation : for example 3310Distribution Channel : 40Product Group : R1171001Product : R_1039Date of Retail Price Change : mm/dd/yyyyNote The date that you enter here is the same one which you have used in the Create Sales Price Valuation, as in preliminary step. Do not select the past date.Select Reason for revaluation : 1Check if the following checkbox is selected:Generate Success/Error Log : XCheck if the following Radio button is selected:Display all Revaluated Products without any Additional Info |  |  |
| 4 | Check | Select Check for validating. | Message is displayed as You can go ahead and schedule the job |  |
| 5 | Schedule | Select Schedule and following message is displayed Job Application job template for sales price valuation has been schedule |  |  |
| 6 | Check Job Results | On the Application Jobs screen, after job item status turned to Finished, select Navigate to the job results in the Results column. | Document (ID XXXXXX) is displayed with revaluation job results |  |

### Display Stock Overview Including Sales Price Values

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows, how you can display the stock overview of a material for a particular plant.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Allocator (Retail) |  |  |
| 2 | Access the app | Open Display Advanced Stock Overview (RWBE) app. |  |  |
| 3 | Provide Input values | On the initial screen, make the following entry in selection criteria and restriction:Material: R_1039Plant: for example 3341Select Execute. | The Stock overview: Full List screen is displayed. |  |
| 4 | Check Stock value at sales price of the article | Check the sales price of the material:Select Plant: for example 3341Select MenuSelect GotoSelect Purchase/Sales Price Stock val u esCheck Value-based stock. | Purchase/Sales Price Stock: Plnt For material screen is displayed. Stock value at sales price of the Article is equal to stock quantity multiplied to the sales price for the article (updated final price in step [Check Stock Availability for Article](#unique_7) [page ] 6) |  |

### Create Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows, how you can create a purchase order. This process step is to confirm that purchase order creation does not have any impact on sales price stock value of articles.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as Purchaser (Retail) |  |  |
| 2 | Open manage purchase orders app | Open Create Purchase Order - Advanced (ME21N) app. |  |  |
| 3 | Navigate to create order screen | On the Create Purchase Order screen, select Create. | New purchase orders screen is displayed. |  |
| 4 | Enter Purchase Order data | Enter all the necessary data:Order type : NB Standard POSupplier : for example 33213002In Header section, on the Org. Data tab:Purch. Org .: for example 3310Purch. Group : for example 001Company Code : for example 3310In Item Overview section:Material : R_1039Plant : for example 3341Storage Location : for example 994AQuantity : Enter any valueNet Price : Enter any valueIn Item Detail section, on Confirmations tab:Conf. Control : Inbound DeliverySelect Enter. |  |  |
| 5 | Save Purchase Order | Select Save and when the Purchase Order number is displayed, write it down for further use. | A new purchase order is created.purchase order number is displayed. |  |

### Display Stock Overview Including Sales Price Values

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows, how You can display the stock overview of a material for a particular plant. This process step is in continuation to the previous step to confirm that Purchase order creation does not have any impact on sales price stock value of articles.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Allocator (Retail) |  |  |
| 2 | Access the app | Open Display Advanced Stock Overview (RWBE) app. |  |  |
| 3 | Provide Input values | On the initial screen, make the following entry in selection criteria and restriction:Material: R_1039Plant: for example 3341Select Execute. | The Stock overview: Full List screen is displayed. |  |
| 4 | Check Stock value at sales price of the article | Check the sales price of the material:Select Plant: for example 3341Select MenuSelect GotoSelect Purchase/Sales Price Stock valesCheck Value-based stock. | Purchase/Sales Price Stock: Plant For material screen is displayed where you could validate the Sales Price stock value which will not have any impact of Purchase Order Creation. |  |

### Create Inbound Delivery (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows, how you can create a inbound delivery fo the purchase order created above. This process step ensures that the generation of inbound deliveries has no effect on the sales price or stock value of products.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Receiving Specialist |  |  |
| 2 | Access the SAP Fiori app | Open app. |  |  |
| 3 | Create inbound delivery | Make the following entries:Document Number: XXX (Enter the purchase order number created in the previous step),Delivery Date: XXX (Delete the default date and enter the delivery date in the purchase order),Select Continue |  |  |
| 4 | Enter Putaway quantity | Enter Putaway quantity and select SaveWhen the inbound delivery number displays, write it down for further use. | A new Inbound Delivery is created.The Inbound Delivery Number is displayed. |  |

### Display Stock Overview Including Sales Price Values

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how You can display the stock overview of a material for a particular plant. This process step is in continuation to the previous step ensures that the generation of inbound deliveries has no effect on the sales price or stock value of products.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Allocator (Retail) | . |  |
| 2 | Access the app | Open Display Advanced Stock Overview (RWBE) app. |  |  |
| 3 | Provide Input values | On the initial screen, make the following entry in selection criteria and restriction:Material: R_1039Plant: for example 3341Select Execute. | The Stock overview: Full List screen is displayed. |  |
| 4 | Check Stock value at sales price of the article | Check the sales price of the material:Select Plant: for example 3341Select MenuSelect GotoSelect Purchase/Sales Price Stock valesCheck Value-based stock | Purchase/sales price stock: Plnt for material screen displayed where you could validate the Sales Price stock value which will not have any impact of inbound delivery creation. |  |

### Post Goods Receipt for Inbound Delivery (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how you can post the good receipt for the inbound delivery created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Receiving Specialist |  |  |
| 2 | Access the app | Open Change Inbound Delivery (VL32N) app. |  |  |
| 3 | Enter Inbound delivery | On the Change Inbound Delivery (VL32N) screen, enter the respective Inbound delivery number created in previous step and select Continue. |  |  |
| 4 | Check delivery quantity | Check the delivery quantity, adjust the delivery quantity in case of any difference. |  |  |
| 5 | Post goods receipt | Select Post Goods Receipt.A success message is generated Goods receipt for inbound delivery XXXXXXX posted (Material document XXXXXX). | Goods Receipt is posted. |  |

### Display Stock Overview Including Sales Price Values

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows, how you can display the stock overview of a material for a particular plant.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Allocator (Retail) |  |  |
| 2 | Access the app | Open Display Advanced Stock Overview (RWBE) app. |  |  |
| 3 | Provide Input values | On the initial screen, make the following entry in selection criteria and restriction:Material: R_1039Plant: for example 3341Select Execute. | The Stock overview: Full List screen is displayed. |  |
| 4 | Check Stock value at sales price of the article | Check the sales price of the material:Select Plant: for example 3341Select MenuSelect GotoSelect Purchase/Sales Price Stock valesCheck Value-based stock | Purchase/sales price stock: Plnt for material screen is displayed, where you could validate the sales price stock value will increase with amount equal to sales price multiplied to goods receipt quantity.New stock value at sales price of the article is equal to the updated stock quantity multiplied to the sales price for the article (updated final price in step [Check Stock Availability for Article](#unique_7) [page ] 6). |  |

### Create Supplier Invoice Using Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how you can post supplier invoice using the purchase order created above. This process step is to confirm that supplier invoice posting does not have any impact on sales price stock value of articles.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant |  |  |
| 2 | Access the app | Open Create Supplier Invoice - Advanced (MIRO) app. | The Create Supplier Invoice - Advanced (MIRO)screen is displayed. |  |
| 3 | Navigate to create supplier invoice -adavcned screen | In the initial screen, enter Company Code and select ContinueCompany Code : for example 3310 |  |  |
| 4 | Provide invoice details | Navigate to Basic Data and enter the values for the following fields:Invoice Date : enter date (Enter Current Date)Reference : enter referencePurchase Order : enter purchase order numberTax code : enter Tax code (same Tax Code from Invoice line item)Calculate Tax : XAmount : enter amount (same amount as appearing in balance)Under the Details tab, select the corresponding document type in the Doc. Types field.Select Enter. |  |  |
| 5 | Check balance | Look at Balance amount. | Balance in green indicates there is no difference between the purchase order and respective invoice. |  |
| 6 | Post supplier invoice | Select PostIgnore any warning message by selecting ENTER.When the supplier invoice number displays, note it for further use. | Message appears: Document number XXXXXXX created.Invoice verification is completed. |  |

### Display Stock Overview Including Sales Price Values

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how you can display the stock overview of a material for a particular plant. This process step is in continuation to the previous step ensures that the supplier invoice posting has no effect on the sales price or stock value of products.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Allocator (Retail) |  |  |
| 2 | Access the app | Open Display Advanced Stock Overview (RWBE) app. |  |  |
| 3 | Provide Input values | On the initial screen, make the following entry in selection criteria and restriction:Material: R_1039Plant: for example 3341Select Execute. | The Stock overview: Full List screen is displayed. |  |
| 4 | Check Stock value at sales price of the article | Check the sales price of the material:Select Plant: for example 3341Select MenuSelect GotoSelect Purchase/Sales Price Stock valesCheck Value-based stock. | Purchase/sales price stock: Plnt for material screen is displayed where you could validate the sales price stock value will not any impact of supplier invoice posting. |  |

### Transfer Products (Store to Store - Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows, how you process transfers of products from one store to another store or from a store to a distribution center. All documents relevant for a transfer are created and filled automatically. The SAP Fiori app transfer products covers and simplifies all steps involved in a product transfer and enables store associates to transfer products more efficiently. This process step is to show how transfer products impacts the sales price stock value of articles.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Retail Store Associate |  |  |
| 2 | Open my store assignment app | Open My Store Assignment (F4334) app. |  |  |
| 3 | Search store | Search using one of the following options to select and assign a store:Store ID : enter a store ID, such as 3340Name: enter the store name, such as Store 3340 AEPostal Code : enter the applicable postal codeCity : enter the applicable citySelect Go to proceed. |  |  |
| 4 | Save assignment | Select the store you want the user to be assigned by, Check the Radio button near to Store.When selecting a store the Assign Me is enabled, Select Assign me to assign the Store and message appear as “ you were assigned to Store XXXX” | Store assigned successfully |  |
| 5 | Access app | Navigate to home screen and open Transfer Products (F2449) |  |  |
| 6 | Create transfer | Enter the following fieldsReceiving Site Category Select StoreReceiving Site : for example 3341Reason for Transfer : Wrong product deliveredSelect Create | “Your Transfer was created” Message is displayed, The detail screen is shown containing 0 items. |  |
| 7 | Add product | Select Add Product “ +” , search for a product, select the product: R_1039 and select select: add product by GTIN: XXXXXX). | “1 Item added to the box” Message is displayed, |  |
| 8 | Adjust the quantity | Change the quantity: 2 of the products. | The quantity is updated accordingly. |  |
| 9 | Add additional product | Select Add Product “ +” , search for a product: R_1040, (optional: add product by GTIN:XXXXXX) select the product and select select | “1 Item added to the box “Message is displayed, |  |
| 10 | Adjust the quantity | Change the quantity: 3 of the products. | The quantity is updated accordingly. |  |
| 11 | Packaging Mat | Check auto assignment. |  |  |
| 12 | Submit transfer | Select Submit to submit the transfer and select OKNote When no printer is selected a pop up message is displayed as” You have not selected a printer yet. Your documents will not be printed automatically. Submit this transfer?” , Select OK button in order to proceed with transfer submission. | “Transfer w as submitted” popup with In Transit status. |  |

### Display Stock Overview Including Sales Price Values

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows, how You can display the stock overview of a material for a particular plant. This process step is in continuation to the previous step ensures that transfer products impacts the sales price or stock value of products.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Allocator (Retail) |  |  |
| 2 | Access the app | Open Display Advanced Stock Overview (RWBE) app |  |  |
| 3 | Provide Input values | On the initial screen, make the following entry in selection criteria and restrictionMaterial: R_1039Plant: for example 3341Select Execute | The Stock overview: Full List screen is displayed. |  |
| 4 | Check Stock value at sales price of the article | Check the sales price of the material:Select Plant: for example 3341Select MenuSelect GotoSelect Purchase/Sales Price Stock valesCheck Value-based stock | Purchase/sales price stock: Plant for material screen displays where you could validate the sales price stock value will decrease with amount equal to sales price multiplied to transfer quantity.New stock value at sales price of the article is equal to the updated Stock quantity multiplied to the Sales Price for the Article (updated final price in step [Check Stock Availability for Article](#unique_7) [page ] 6) |  |

### Process Aggregated Sales from POS – Receive Aggregated Sales (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how you transfer aggregated sales information sent from POS system to SAP S/4HANA Cloud Public Edition  system. This process step is to process the store sales to validate the change in the sales price stock value of articles.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Receive aggregated sales payload | SAP S/4HANA Cloud Public Edition system receives an inbound payload with the aggregated information on the sales took place in a point-of-sales (POS) system.This payload received from the POS system using the communication arrangements at the SAP S/4HANA Cloud Public Edition systemTo simulate using API client tools the above said behavior follows the steps mentioned in Chapter [Send Transmission with API Client Tools (Optional)](#unique_10) [page ] 9 (In preliminary step).Use the below set of master data:Material : R_1039 (Single Article)Store: for example 3341Refer chapter [Transmission Example: Aggregated Sales – Payload to be used (Optional)](#unique_12) [page ] 10 (In preliminary steps) for sample payload à and replace the article in the transmission example to test all the kind of articles listed above. | After successful posting Administrator (Retail) checks:Status is shown as “Accepted” in API client tools.The persisted messages in the Overview Message Monitoring (F4515) app. |  |

### Schedule Job for Posting of POS Inbound for Sales (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as an Administrator (Retail) |  |  |
| 2 | Access the SAP Fiori App | Open Schedule POS Inbound Service (F5236) app. |  |  |
| 3 | Create a Job to Schedule the persisted messages above | Select Create | The New Job: Schedule POS inbound Service appears with three steps of input:Template SelectionScheduling OptionsParameters |  |
| 4 | Input Template | Select the Job Template ‘Schedule POS Inbound Service’ and enter the Job Name (as Step 1) and select Step 2 |  |  |
| 5 | Input Scheduling Options | Enter the Start date and time to schedule the Job with the recurrence patten (For example, Daily, Monthly or Weekly) and select Step 3 |  |  |
| 6 | Input Parameters | Enter the following section as the parameters to schedule the job:Service and Message Status(here Administrator (Retail) need to mention which POS inbound service need to be scheduled, which in this case is Sales).Message Creation Date and Time (here Administrator (Retail) can enter the date & time frame or date function of the persisted messages to be processed).Other attributes (here Administrator (Retail) can specify the service specific attributes. For example, store or service reference ID) along with the processing control, for example, timeout. |  |  |
| 7 | Schedule Job | Select Schedule to schedule the job created. | Schedule Job screen with Status, Log, Results, Step, Description and so on. is displayed.Note Kindly refer to scope item 3HV step no 4.4 - monitor results and handle errors. |  |

### Display Stock Overview Including Sales Price Values

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows, how you can display the stock overview of a material for a particular plant. This process step is in continuation to the previous step to show how store sales impacts the sales price stock value of articles.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Allocator (Retail) |  |  |
| 2 | Access the app | Open Display Advanced Stock Overview (RWBE) app. |  |  |
| 3 | Provide Input values | On the initial screen, make the following entry in selection criteria and restrictionMaterial: R_1039Plant: for example 3341Select Execute |  |  |
| 4 | Check stock value at sales price of the article | Check the sales price of the materialSelect Plant: for example 3341Select MenuSelect GotoSelect Purchase/Sales Price Stock valesCheck Value-based stock | Purchase/sales price stock: Plant for material screen displays where you could validate the Sales Price stock value will decrease with Amount equal to Sales Price multiplied to POS Sale quantity.New Stock value at sales price of the Article is Equal to the updated Stock Quantity multiplied to the Sales Price for the Article (updated final price in step [Check Stock Availability for Article](#unique_7) [page ] 6) |  |

### Display Material Inventory Values Including Sales Price (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how you can display the inventory values of a material for a particular plant. This optional step is to show a inventory value report to display the sales price stock value of articles.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Inventory Manager |  |  |
| 2 | Access the app | Open Material Inventory Values - Balance Summary (F1422) app. |  |  |
| 3 | Provide input values | On the selection screen, make the following entriesLedger: 0LCompany Code: for example 3310Reporting Key Date: Today’s DateNote Selection field for material can be added by selecting the Adopt Filter and then select Product and select OK.Select Navigation Panel, remove all the predefined fields from row axis and add new fields Product and Plant from Available Fields to Rows axis to display the report for the specified Product.Under Columns select Measures and Add field Amount in Global Currency and remove field Amount in Freely Defined Currency.Deselect the Navigation Panel.Select Go. | The Material Inventory Values - Balance Summary is displayed. |  |
| 4 | Check stock value at sales price of the article | Check the sales price of the material in column Amount in Global Currency. | You could validate the sales price stock value will decrease with amount equal to sales price multiplied to pos sale quantity.New Stock value at sales price of the article is equal to the updated stock quantity multiplied to the sales price for the article (updated final price in step [Check Stock Availability for Article](#unique_7) [page ] 6). |  |

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
- see-also :: [[15-retail-operations/test-script-omnichannel-sales-promotion-opps-consumer-products-7t7-ae]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5FT_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 67,452 chars in the whole document
