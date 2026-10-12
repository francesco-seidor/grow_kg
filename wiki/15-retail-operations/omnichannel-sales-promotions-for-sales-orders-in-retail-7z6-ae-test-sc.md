---
id: 15-retail-operations/omnichannel-sales-promotions-for-sales-orders-in-retail-7z6-ae-test-sc
title: Omnichannel Sales Promotions for Sales Orders in Retail (7Z6_AE) - Test Script (7Z6_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 7Z6: applying SAP Omnichannel Promotion Pricing promotions to in-store sales orders and POS payments."
cluster: 15-retail-operations
tags: [kb/retail-operations, topic/omnichannel-promotions]
aliases: [7Z6_S4CLD2608_BPD_EN_AE]
keywords: [Omnichannel Promotion Pricing for Sales Orders, omnichannel promotion pricing, sales promotions, in-store sales orders, pos payment, initial stock, business partner settings, retail terminology, business roles, test scripts]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7Z6_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1240
topic: 15-retail-operations/omnichannel-promotions
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Omnichannel Sales Promotions for Sales Orders in Retail (7Z6_AE) - Test Script (7Z6_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7Z6_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Omnichannel Promotion Pricing for Sales Orders** in Retail Operations. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 04-07-26 |
| --- | --- |
|  | Omnichannel Sales Promotions for Sales Orders in Retail (7Z6_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc234569068)

[2 Prerequisites 3](#_Toc234569069)

[2.1 System Access 3](#_Toc234569070)

[2.2 Roles 3](#_Toc234569071)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc234569072)

[2.4 Additional Manual Configuration 5](#_Toc234569073)

[2.5 Preliminary Steps 5](#_Toc234569074)

[2.5.1 Verify the Business Partner Settings 5](#_Toc234569075)

[2.5.2 Create Initial Stock 6](#_Toc234569076)

[2.5.3 Maintain Promotions in SAP Omnichannel Promotion Pricing 7](#_Toc234569077)

[3 Overview Table 10](#_Toc234569078)

[4 Test Procedure 11](#_Toc234569079)

[4.1 Sell from store 11](#_Toc234569080)

[4.1.1 Create Sales Order and Generate Invoice 11](#_Toc234569081)

[4.1.2 Process Customer Order Payment from POS 13](#_Toc234569082)

## Purpose

Overview

This scope item enables to use of SAP Omnichannel Promotion Pricing features within a sales order in SAP S/4HANA Cloud Public Edition. SAP Omnichannel Promotion Pricing is a cloud-based solution designed to operate seamlessly across multiple sales channels, including the SAP S/4HANA Cloud Public Edition. It empowers rule administrators to create and manage complex promotional rules that define when promotions apply and specify the associated rewards.

These rules can be configured based on criteria such as:

- The promotion’s valid time frame
- Specific sales channels where the promotion is active
- The type of discount offered, such as a percentage off

When a retail store associate creates or modifies a sales order, the system automatically evaluates whether the order meets the conditions set by these promotional rules. If the criteria are satisfied, the calculation service in SAP Omnichannel Promotion Pricing applies the rewards to the sales order automatically.

These rewards may include:

- Free goods: Additional items are automatically added to the order
- Discounts: Price adjustments applied to one or more items or the entire order
- A combination of both

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

|  |
| --- |
| Note In the retail industry, specific terms differ from the standard terms used in other lines of business. Therefore, SAP solutions which provide business processes across multiple lines of businesses may use terms for the corresponding business objects, transactions, and user interfaces that deviate from the retail terminology. For integration and reuse reasons, the SAP S/4HANA Cloud Public Edition, retail, fashion, and vertical business business may thus include different terms that refer to the same concept. SAP intends to harmonize the terminology in the future.The following terms are used synonymously in this document:Table 1:Standard Terms in Lines of BusinessSAP S/4HANA Cloud Public Edition, retail, fashion, and vertical business businessMaterial, productArticleMaterial group, product groupMerchandise categoryPlant, locationSite (as superordinate term) - store and distribution center (DC) |

## Prerequisites

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
| Warehouse Clerk (Retail) | SAP_BR_WAREHOUSE_CLERK_RFM | Retail Inventory Processing | SAP_RFM_SPT_INVTRY_PROCG_PC |  |
| Retail Store Associate | SAP_BR_RFM_STORE_ASSOCIATE | Retail Store Associate | SAP_BR_RFM_STORE_ASSOCIATE |  |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |
| Administrator (Retail) | SAP_BR_ADMINISTRATOR_RFM | Administration - Retail | SAP_BR_ADMINISTRATOR_RFM |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Single Article (Material or Product) | R_1050 | My Best Blond Shampoo |  |
| Single Article (Material or Product) | R_1051 | My Best Blond Conditioner |  |
| Single Article (Material or Product) | R_2004 | Relax Body Lotion, 200 ml |  |
| Sold-to Party | 33113010 | Consumer 2 AE |  |
| Ship-to party | 33113010 | Consumer 2 AE |  |
| Store (Site) | 3340 | Store 3340 AENote Used as delivery plant for creating a sales order. |  |
| Sales Organization | 3310 | Dom. Sales Org |  |
| Distribution Channel | 40 | Store Sales |  |
| Division | 00 | Product Division 00 |  |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/fa2b64101451d11f4484b978720e64a0)

### Preliminary Steps

#### Verify the Business Partner Settings

Use

With this process step, you verify whether the correct SAP Omnichannel Promotion Pricing procedure is assigned to the customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. |  |  |
| 2 | Access the App | Open Manage Customer Master Data (F0850A) app. |  |  |
| 3 | Enter Parameters | On the Selection Screen enter the following data and click on Go.Business Partner: 33113010 |  |  |
| 4 | Check the details | Check the below details:Choose Sales Areas sectionGo to details for:Sales Organization: 3310Distribution Channel: 40Division: 00Go to Sales Area Details > Pricing and Statistics sectionCheck for value in Customer Pricing Procedure. | Customer Pricing Procedure: Standard with OPPS (OC) should be available. |  |

|  |
| --- |
| Note Alternatively, you can choose to verify whether the correct omnichannel promotion pricing procedure is assigned to the new customer.When you are creating a new customer, ensure you set the Customer Pricing Procedure to Standard with OPPS (OC) to determine the omnichannel sales promotion pricing.For detailed instructions on how to create a new customer, please refer to the Business Partners for Retail (5FH). |

#### Create Initial Stock

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

This process step shows you how to create the initial stock and post the material document in the system using the Post Goods Movement (MIGO) app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk (Retail). | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). It only displays this way if it was your last transaction. So, the action for the user should be to select Reference Document for MIGO Transaction > Other. | The Goods Receipt Other screen displays. |  |
| 3 | Enter Movement Type | Make the following entry and choose Enter.Executable Action in Transaction MIGO: Goods Receipt |  |  |
| 4 | Enter Material | On the Goods Receipt Other Screen: Material tab, make the following entry, and choose Enter:Material : R_1050, R_1051, R_2004 |  |  |
| 5 | Enter Quantity Data | On the Goods Receipt Other Screen: Quantity tab, make the following entry, and choose Enter:Qty in Unit of Entry: <Enter your Qty>Unit of Entry: <Enter UoM of material> |  |  |
| 6 | Enter Movement Type | On the Goods Receipt Other Screen: Where tab, make the following entries and choose Enter:Movement Type: 561 (Receipt per initial entry of stock balances into unrestricted use) |  |  |
| 8 | Save Your Entries | Choose Post. | Material document XXXX posted. |  |

#### Maintain Promotions in SAP Omnichannel Promotion Pricing

Use

You use the Maintain Promotions app to create promotions to offer rewards to customers, based on certain eligibility criteria.

These are various scenarios to create omnichannel promotion pricing.

Scenario 1. Maintain Promotion - Simple Discount

1. Access SAP Omnichannel Promotion Pricing in the SAP BTP cockpit.
2. Open the Maintain Promotions app.
3. Click on Create to create a new promotion.
4. Enter Promotion Name -SalesOrderPromotions, Description - SalesOrderPromotions, Start Date -Dec 1, 2030, and End Date - Dec 31, 2030.
5. Click on Create to create a promotion.
6. Go to Promotion Rules section and click on Create.

|  |
| --- |
| Note In the Promotional Rules section, you define what triggers the promotion and what customers get as a reward. |

1. Enter a Rule Name - SalesOrderPromotions, choose value For Sales and Returns for Sales and Returns Type.
2. Click on Create to create a promotion rule.
3. In the promotional rule, configure the Advanced Rule Settings according to your business needs.
4. Click on Edit and in the Eligibility and Reward section, select Product, enter the below details:
    1. Product ID - R_1050
    2. Unit of Measure - PC
5. Go to Add Reward section, choose Single > Sinple Discount and enter the below details:
    1. Price Modification - Percent Discount (RP)
    2. Discount Percentage - 10
6. Click on Save to save your changes.
7. Go back to your promotion screen and select Business Units section, click on Create, enter the below details and choose Add:
    1. Business Unit Type - Customer
    2. Business Unit ID - 33113010
8. Once you are done with your configuration, select Activate to activate the promotion.

Scenario 2. Maintain Promotion - Fixed Price Promotion

1. Access SAP Omnichannel Promotion Pricing in the SAP BTP cockpit.
2. Open the Maintain Promotions app.
3. Click on Create icon to create a new promotion.
4. Enter Promotion Name -SalesOrderPromotions, Description - SalesOrderPromotions, Start Date - Dec 1, 2030, and End Date - Dec 31, 2030.
5. Click on Create to create a promotion.
6. Go to Promotion Rules section and click on Create.

|  |
| --- |
| Note In the Promotional Rules section, you define what triggers the promotion and what customers get as a reward. |

1. Enter a Rule Name- FixedPricePromotions, choose value For Sales and Returns for Sales and Returns Type.
2. Click on Create to create a promotion rule.
3. In the promotional rule, configure the Advanced Rule Settings according to your business needs.
4. Click on Edit and in the Eligibility and Reward section, select Product, enter the below details:
    1. Product ID - R_1051
    2. Unit of Measure - PC
5. Go to Add Reward section, choose Single > Sinple Discount and enter the below details:
    1. Price Modification - Promotion Price (PS)
    2. New Price Amount - 1
6. Click on Save to save your changes.
7. Go back to your promotion screen and select Business Units section, click on Create, enter the below details and choose Add:
    1. Business Unit Type - Customer
    2. Business Unit ID - 33113010
8. Once you are done with your configuration, select Activate to activate the promotion.

Scenario 3. Maintain Promotion - Bonus Buy Scenario

1. Access SAP Omnichannel Promotion Pricing in the SAP BTP cockpit.
2. Open the Maintain Promotions app.
3. Click on Create icon to create a new promotion.
4. Enter Promotion Name -SalesOrderPromotions, Description - SalesOrderPromotions, Start Date -Dec 1, 2030, and End Date - Dec 31, 2030.
5. Click on Create to create a promotion.
6. Go to Promotion Rules section and click on Create.

|  |
| --- |
| Note In the Promotional Rules section, you define what triggers the promotion and what customers get as a reward. |

1. Enter a Rule Name- BonusBuyPromotions, choose value For Sales and Returns for Sales and Returns Type.
2. Click on Create to create a promotion rule.
3. In the promotional rule, configure the Advanced Rule Settings according to your business needs.
4. Click on Edit and in the Eligibility and Reward section, select Product, enter the below details:
    1. Product ID - R_1051
    2. Unit of Measure - PC
5. Go to Add Reward section, choose Additional Bonus > Product and enter the below details:
    1. Product ID - R_2004
    2. Quantity - 1
6. Click on Save to save your changes.
7. Go back to your promotion screen and select Business Units section, click on Create, enter the below details and choose Add:
    1. Business Unit Type - Customer
    2. Business Unit ID -33113010
8. Once you are done with your configuration, select Activate to activate the promotion.

Result

You have created a promotion for SAP omnichannel promotion pricing. It can now be used for omnichannel sales promotions in sales orders. For more information about the app, see [SAP Omnichannel Promotion Pricing](https://help.sap.com/docs/OPP?locale=en-US) > Use > Application Help > [Application Help for Promotion Maintenance](https://help.sap.com/docs/omnichannel-promotion-pricing/application-help-for-promotion-maintenance/promotion-maintenance?version=LATEST&locale=en-US).

## Overview Table

This scope item consists of several process step provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App | Expected Results |
| --- | --- | --- | --- |
| [Create Sales Order and Generate Invoice](#unique_10) [page ] 11 | Retail Store Associate | Manage In-Store Sales Orders (F7141) | Sales order is created, picking of the outbound delivery is triggered, goods issue for the outbound delivery is posted. |
| [Process Customer Order Payment from POS](#unique_11) [page ] 13 | Administrator (Retail) | Schedule POS Inbound Service (F5236) | Customer order payment information from a POS system to SAP S/4HANA Cloud Public Edition is transferred. |

## Test Procedure

### Sell from store

#### Create Sales Order and Generate Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Follow this step to create a sales order using the Manage In-Store Sales Order app. During this process, the system will initiate the picking of the outbound delivery, posting of goods issue for the outbound delivery, and generation of the associated follow-on documents. After the process is completed, you have the option to generate and print invoices.

Additionally, you can validate any updates on the sales order if needed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori launchpad | Log onto the SAP Fiori launchpad using the role Retail Store Associate. | The SAP Fiori launchpad displays. |  |
| 2 | Access Sales order worklist | Open Manage In-Store Sales Orders (F7141) app. | Manage In-Store Sales Orders (F7141) screen is displayed. |  |
| 3 | Go to App | On the Manage In-Store Sales Orders (F7141) screen, press Create button. | Sales Order screen is displayed. |  |
| 4 | Enter Data | In Basic Data section of General Information tab view, enter:Customer: <Enter your customer’s ID>NoteEnter the customer or sold-to-party ID of the respective customer if already registered or newly registered.If one-time customer or sold-to party is used, then after entering your sold-to party, go to Partners , select your Sold-to Party and select Change Address button.Enter or change any field value in the Change Address pop-up and select Change Address button, for instance, enter E-Mail.Customer References: <Order Reference Text>Shipping Conditions: Immediately 03Under Advance Data, make the following entries:Sales Organization: 3310Distribution Channel: 40Division: 00Promotion Pricing Date: <Date> e,g 10.10.2025In the Products table of the Products tab view, enter the following details:Product : R_1050Requested Quantity: <Order Quantity>Choose EnterProduct : R_1051Requested Quantity: <Order Quantity>Choose EnterProduct : R_2004Requested Quantity: <Order Quantity>Choose Enter | Details are entered successfully. |  |
| 5 | Save the order | Select Create. | OK order is saved and Standard Order <order number> has been saved success message is displayed. |  |
| 6 | Check the Omnichannel Promotion Condition Type | In the Sales Order screen, select Products tab:Select the Item and navigate to the Details icon.In the Item screen, go to Prices > Price Elements > Settings and select Promotion Price Rule ID and Promotion ID and choose OK.Check the Condition Type, Promotion Price Rule ID and Promotion ID. (For example: OCT1, OCT2, D100).Note Promotion Price Rule ID and Promotion ID is not applicable D100. | The Item screen is displayed.In the Condition Type column, the condition is displayed.Example For the Condition Type- OCT1 Discount % value is displayed.For the Condition Type- OCT2 Discount Fixed-Price value is displayed.For the Condition Type- D100 Manual Discount 100% value is displayed. |  |
| 7 | Generate Invoice | Press Generate Invoice button on the Sales Order screen. | Standard Order xxxxx has been saved message is displayed. Outbound delivery is processed with picked quantity, goods issue is posted and invoice is generated automatically. |  |
| 8 | Print Invoice (Optional) | Navigate back to the Manage In-Store Sales Orders (F7141) screen, enter Sales Order : <the sales order number created previously> and select Go.Select the resulting sales order and go to Process Flow tab and click on the Invoice, then select More Links from the Invoice Number pop-up.Select the Display Billing Documents hyperlink in the Define Link List pop-up.Go to Menu >Goto> Header> OutputSelect the output from the Output table and select Display Document. Select Print . | Invoice is previewed and printed. |  |
| 9 | Validate Follow-On Documents (Optional) | Navigate back to the Sales Orders screen and go to Process Flow tab.Select the <Relevant Follow-On Document> and , then choose More Links from the <Relevant Follow-On Document> number pop-up.Select the Display <Relevant Follow-On Document> Documents hyperlink in the Define Link List pop-up to investigate the details of the subsequent document, for example, outbound delivery, invoice documents and accounting documents. | Generated documents are displayed to investigate the details. |  |

#### Process Customer Order Payment from POS

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure you can transfer customer order payment information from a POS system to SAP S/4HANA Cloud Public Edition based on the method of payment, such as cash, cheques, payment cards, electronic cash, or electronic wallet using SOAP service.

Procedure

|  |
| --- |
| Note Refer Process Customer Order Payment from POS from Store Connectivity – Inbound (3HV) scope item. Also, customer order payment related payload should be referred to simulate the inbound payload with the aggregated information of payments for the sales took place in the Point-of-sales system. |

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
- related-to :: [[15-retail-operations/test-script-omnichannel-sales-promotion-opps-consumer-products-7t7-ae]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7Z6_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 25,954 chars in the whole document
