---
id: 08-sales-order-management/test-script-sales-contract-management-i9i-ae-sap-s-4hana-cloud-public
title: "Test Script: Sales Contract Management (I9I_AE) - SAP S/4HANA Cloud Public Edition (I9I_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script, scope item I9I_AE (UAE): quantity/value sales contracts, contract down payments and price agreements."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/sales-contracts-and-down-payments]
aliases: [I9I_S4CLD2608_BPD_EN_AE]
keywords: [Sales Contracts and Customer Down Payments, sales contract management, sales quantity contracts, sales value contracts, contract down payments, price agreements, product hierarchy assignment, call-off orders, delivery block, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/I9I_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1295
topic: 08-sales-order-management/sales-contracts-and-down-payments
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Sales Contract Management (I9I_AE) - SAP S/4HANA Cloud Public Edition (I9I_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/I9I_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Sales Contracts and Customer Down Payments** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Sales Contract Management (I9I_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232862597)

[2 Prerequisites 4](#_Toc232862598)

[2.1 System Access 4](#_Toc232862599)

[2.2 Roles 4](#_Toc232862600)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232862601)

[2.4 Business Conditions 6](#_Toc232862602)

[2.5 Preliminary Steps 7](#_Toc232862603)

[2.5.1 Post Good Receipt 7](#_Toc232862604)

[2.5.2 Configure Delivery Block on Billing Plan Type for Contract Down Payment 8](#_Toc232862605)

[2.5.3 Manage Situation Types (Optional) 10](#_Toc232862606)

[2.5.4 Define Price Maintenance Scenarios (Optional) 11](#_Toc232862607)

[2.5.5 Manage Product Hierarchy Assignment 13](#_Toc232862608)

[3 Overview Table 15](#_Toc232862609)

[4 Test Procedures 18](#_Toc232862610)

[4.1 Scenario 1: Sales Quantity or Sales Value Contract 18](#_Toc232862611)

[4.1.1 Create Sales Contract (Quantity) 18](#_Toc232862612)

[4.1.2 Create Sales Contract (Value) 20](#_Toc232862613)

[4.1.3 Print Form - Output Management 21](#_Toc232862614)

[4.1.4 List Sales Contracts 22](#_Toc232862615)

[4.2 Scenario 2: Quantity Contract Based Down Payments 23](#_Toc232862616)

[4.2.1 Create Sales Contract (Quantity) 23](#_Toc232862617)

[4.2.2 Remove Billing Block in Sales Contract manually 25](#_Toc232862618)

[4.2.3 Create Sales Order with Delivery Block 26](#_Toc232862619)

[4.2.4 Create Down Payment Request Part I 27](#_Toc232862620)

[4.2.5 Check Sales Contract Status (Optional) 28](#_Toc232862621)

[4.2.6 Remove Billing Block in Sales Contract manually 29](#_Toc232862622)

[4.2.7 Create Down Payment Request Part II 30](#_Toc232862623)

[4.2.8 Post Incoming Payment 31](#_Toc232862624)

[4.2.9 Check Sales Contract Status (Optional) 33](#_Toc232862625)

[4.2.10 Check Sales Order’s Delivery Block (Optional) 34](#_Toc232862626)

[4.2.11 Create Sales Order without Delivery Block 35](#_Toc232862627)

[4.2.12 Create Outbound Delivery 36](#_Toc232862628)

[4.2.13 Execute Picking 37](#_Toc232862629)

[4.2.14 Post Goods Issue 38](#_Toc232862630)

[4.2.15 Billing 39](#_Toc232862631)

[4.2.16 Schedule Automatic Clearing Job (Optional) 40](#_Toc232862632)

[4.3 Scenario 3: Price Agreement for Quantity Contract 41](#_Toc232862633)

[4.3.1 Create Sales Contract (Quantity) 41](#_Toc232862634)

[4.3.2 Create Sales Order with Price Agreements 43](#_Toc232862635)

[4.3.2.1 Option 1 – Create Sales Order with Contract Reference 44](#_Toc232862636)

[4.3.2.2 Option 2 – Create Sales Order and Assign Sales Contract 45](#_Toc232862637)

[4.3.3 Create Outbound Delivery 46](#_Toc232862638)

[4.3.4 Execute Picking 47](#_Toc232862639)

[4.3.5 Post Goods Issue 48](#_Toc232862640)

[4.3.6 Billing 49](#_Toc232862641)

[4.4 Scenario 4: Price Agreement for Value Contract with Products 50](#_Toc232862642)

[4.4.1 Create Sales Contract (Value) 50](#_Toc232862643)

[4.4.2 Create Sales Order with Price Agreements 52](#_Toc232862644)

[4.4.2.1 Option 1 – Create Sales Order with Contract Reference 53](#_Toc232862645)

[4.4.2.2 Option 2 – Create Sales Order and Assign Sales Contract 54](#_Toc232862646)

[4.4.3 Create Outbound Delivery 55](#_Toc232862647)

[4.4.4 Execute Picking 56](#_Toc232862648)

[4.4.5 Post Goods Issue 57](#_Toc232862649)

[4.4.6 Billing 58](#_Toc232862650)

[4.5 Scenario 5: Price Agreement for Value Contract with Product Hierarchy 59](#_Toc232862651)

[4.5.1 Create Sales Contract (Value) 59](#_Toc232862652)

[4.5.2 Create Sales Order with Price Agreements 61](#_Toc232862653)

[4.5.2.1 Option 1 – Create Sales Order with Contract Reference 62](#_Toc232862654)

[4.5.2.2 Option 2 – Create Sales Order and Assign Sales Contract 63](#_Toc232862655)

## Purpose

Overview

This scope item addresses the following scenarios:

Sales quantity or sales value contract: The quantity contract contains basic quantity and price information. A value contract is a legal agreement with a customer that contains the materials and services that the customer receives within a specified time period, and for a value up to a specified target value. In this scope item, the internal sales representative creates a sales quantity or value contract. Following this, a call-off order is created against the contract.

Quantity-contract-based down payments: For the sales quantity contract, down payments can be requested via a billing plan. Upon call-off order creation, a delivery block is assigned to the call-off order schedule lines. Once the down payments are received, the delivery block is removed automatically. In the delivery-related final invoice of the call-off order, the received down payments for the quantity contract is deducted.

Quantity-contract-based price agreements: For the sales quantity contract, the price agreement can be a special pricing condition record which is maintained in sales contract items. Upon call-off order creation, the price agreements is determined on the order items, and the price agreements is applied in the follow-up businesses including invoices.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

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
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT |  |  |  |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |
|  |  |  |  |  |
| Accounts Receivable Accountant | SAP_BR_AR_ACCOUNTANT | Accounts Receivable | SAP_BR_AR_ACCOUNTANT |  |
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | TG12 | Trad.Good 12,Reorder Point,Reg.Trad. | See sections Business Conditions and Preliminary Steps. |
| Material | TG10 | Trad.Good 10,PD,Third PartyTrading Good for regular Trading (MRP planning) with item category group CBORno batch | Be used in Quantity Contracts only (only for I9I). |
| Material | TG13 | Trading Good for Regular Trading (reorder point planning) with item category group CBNAno batch | Be used in Quantity Contracts only (only for I9I). |
| Material | TG14 | Trading material with item category group CUBK (Reorder point planning, bought in item)no batch | Be used in Quantity Contracts only (only for I9I). |
| Material | SDBOMERLAHD | SD BOM Header ERLA (with Pricing, inventory management) |  |
| Material | SDBOMLUMFHD | SD BOM Header LUMF(No pricing, no inventory) |  |
| Sold-to party | 33100001 | Domestic UAE Customer 1 | You can test the scope item using another domestic customer. |
| Ship-to party | 33100001 | Domestic UAE Customer 1 |  |
| Payer | 33100001 | Domestic UAE Customer 1 |  |
| Plant | 3310 |  |  |
| Storage Location | 331A |  |  |
| Shipping Point | 3310 |  |  |
| Sales Organization | 3310 |  |  |
| Distribution Channel | 10 |  |  |
| Division | 00 |  |  |
| Company Code | 3310 | Company Code 3310 |  |

For more information on creating these master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BND | Create Customer Master - MDS |

### Business Conditions

| Scope Item | Business Condition |
| --- | --- |
| 31N - Situation Handling | This scope item must be installed for situation handling steps. |

### Preliminary Steps

#### Post Good Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To run this step, the material must be available in stock. This process step shows you how to post good receipt.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Stock (F1062). | The Manage Stock screen displays. |  |
| 3 | Enter Material | Make the following entry and choose Enter:Material: TG12Plant: Plant 1 AE (3310)Note For the ERLA material, please choose the material for SDBOMERLAIT01 and SDBOMERLAIT02For the LUMF material, please choose the material for SDBOMLUMFIT01 and SDBOMLUMFIT02. | The stock overview for the material displays. |  |
| 4 | Select Stock | Choose the icon beside the stock that you want to add initial stock, for example:Storage Location: Std. storage 1 (331A)Unrestricted-Use Stock | A dialog box opens. The Storage Location, Stock Type, and Current Quantity display according to your entries in the previous steps. |  |
| 5 | Add Initial Entry | Make the following entries and choose Post:Stock Change: Initial EntryQuantity: <enter a number>Document Date: <today>Posting Date: <today> | The system displays Material document XXX created. The stock is added. |  |

#### Configure Delivery Block on Billing Plan Type for Contract Down Payment

Purpose

This step shows how to activate automatic delivery block determination.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration . | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241) . | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Enter Billing Plans in the search box, and choose Search. Choose the line of Make settings for billing plans. Find the step Define Date Categories for Billing Plan Types, then choose Configure. |  |  |
| 4 | Make the setting | Select the following entry and choose Details:Billing Plan Type: S5Date Category: 01Then check and make the change as below if necessary:Delivery Block: 53 Check PrepaymentChoose Save.NoteDon’t change the delivery block reason code to empty, otherwise, the delivery block on call-off orders will not be setKeep the delivery block reason code same on both date categories, otherwise, automatic removing delivery block on call-off order might not work properly |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Maintain Date Categories for Milestone Billing Plans | In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Define Date Categories for Billing Plan Types.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Make the setting | Select the following entry and choose Details:Billing Plan Type: S5Date Category: 01Then check and make the change as below if necessary:Delivery Block: 53 Check PrepaymentChoose Save.NoteDon’t change the delivery block reason code to empty, otherwise, the delivery block on call-off orders will not be setKeep the delivery block reason code same on both date categories, otherwise, automatic removing delivery block on call-off order might not work properly |  |  |

#### Manage Situation Types (Optional)

Purpose

In this procedure, you configure the situation type by using template.

|  |
| --- |
| Note 31N - Situation Handling is required to execute this step. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on on to the SAP Fiori launchpad as Configuration Expert - Business Process Configuration | The SAP Fiori Launch Pad displays. |  |
| 2 | Access the App | Open Manage Situation Types (F2947) . | The Manage Situation Types.screen displays. |  |
| 3 | Select the template to copy | Choose Go.Select the the latest version of SD_CONTRACT_FULFILLMENT, then choose Copy. | The Situation Type screen displays. |  |
| 4 | Maintain the situation | Make the following entries and choose Save:ID: Z_CONTRACTName: Contract SituationIn the Situation Display tab:Resend Notification: ChooseIn the Notification Recipients area, maintain Operational Purchasing in the field Member Function if necessary; Choose the Condition tab, make the attribute value to configure the conditions to use this function.Choose Save. | Then situation type is maintained |  |
| 5 | Enable this situation type | Choose Enable, it will change from NO to YES. |  |  |

#### Define Price Maintenance Scenarios (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step shows how to create price maintenance scenarios to assign to one item category.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Enter Price Maitenance Scenarios in the search box, and choose Search. Choose the line of Configure pricing for customers and materials in sales. Find the step Define Price Maintenance Scenarios, then choose Configure. |  |  |
| 4 | Make the Settings | Choose New Entries and enter:Scenario:ZSC1Description: Test ScenarioChoose this entry, in the Specify Fields area, choose New Entries:Input entry 1:Field: VBELNDescription: SD DocumentmInput entry 2:Field: POSNRDescription: Item (SD)In the Enable Maintenance of Condition Records area, and choose Details:Cnty: DPA1AcSq: PRAGAcNo: 10Tab: 099Description: Ref. Doc./Ref. ItemThen check and make the change as below if necessary:Enable Maintenance: CheckedChoose Save.NoteYou can create the specified fields instead of sales document and sales document item, however, it shall be ensured that if the condition types are related to the pricing unit.The condtion types are generated automatically according to the fields you specify. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Maintain Date Categories for Milestone Billing Plans | In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Define Price Maintenance Scenarios.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Make the Settings | Choose New Entries and enter:Scenario:ZSC1Description: Test ScenarioChoose this entry, in the Specify Fields area, choose New Entries:Input entry 1:Field: VBELNDescription: SD DocumentmInput entry 2:Field: POSNRDescription: Item (SD)In the Enable Maintenance of Condition Records area, and choose Details:Cnty: DPA1AcSq: PRAGAcNo: 10Tab: 099Description: Ref. Doc./Ref. ItemThen check and make the change as below if necessary:Enable Maintenance: CheckedChoose Save.NoteYou can create the specified fields instead of sales document and sales document item, however, it shall be ensured that if the condition types are related to the pricing unit.The condtion types are generated automatically according to the fields you specify. |  |  |

#### Manage Product Hierarchy Assignment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step shows how to create a product hierarchy assignment to Sales purpose.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Manage Product Hierarchy Assignments (F4240). | The Manage Product Hierarchy Assignments screen is displayed. |  |
| 3 | Choose Create Contract | Choose Create. | The Create screen displays. |  |
| 4 | Make Gernal Information | Make the following entries in the second screen:Purpose: Sales(02)Sales Organization: 3310Distribution Channel: 10Valid From: <today’s date>Valid To: <End of this year>Product Hierarchy: Tools(TOOLS) |  |  |
| 5 | Save | Choose Save and record the quantity contract number. | The product hierarchy assignment is saved. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step, Report or Item | Business Role | Transaction/APP Name | Expected Results |
| --- | --- | --- | --- |
| Scenario 1: Sales Quantity or Sales Value Contract |  |  |  |
| [Create Sales Contract (Quantity)](#unique_13) [page ] 18 | Internal Sales Representative | Manage Sales Contracts (F1851) | The Manage Sales Contract Initial Screen displays. |
| [Create Sales Contract (Value)](#unique_14) [page ] 20 | Internal Sales Representative | Manage Sales Contracts (F1851) | The Manage Sales Contract Initial Screen displays. |
| [Print Form - Output Management](#unique_15) [page ] 21 | Internal Sales Representative | Manage Sales Orders (F1873) | The Create Sales Order: Initial screen displays. |
| [List Sales Contracts](#unique_16) [page ] 22 | Internal Sales Representative | List Incomplete Sales Contracts (F2430) | The List Incomplete Sales Contract initial screen display. |
| Scenario 2: Quantity Contract Based Down Payments |  |  |  |
| [Create Sales Contract (Quantity)](#unique_17) [page ] 23 | Internal Sales Representative | Manage Sales Contracts (F1851) | The Manage Sales Contract Initial Screen displays. |
| [Remove Billing Block in Sales Contract manually](#unique_18) [page ] 25 | Internal Sales Representative | Manage Sales Contracts (F1851) |  |
| [Create Sales Order with Delivery Block](#unique_19) [page ] 26 | Internal Sales Representative | Manage Sales Orders (F1873) | The sale order is created. |
| [Create Down Payment Request Part I](#unique_20) [page ] 27 | Billing Clerk | Create Billing Documents (F0798) | This step is to post a down payment. |
| [Check Sales Contract Status (Optional)](#unique_21) [page ] 28 | Internal Sales Representative | Manage Sales Contracts (F1851) |  |
| [Remove Billing Block in Sales Contract manually](#unique_22) [page ] 29 | Internal Sales Representative | Manage Sales Contracts (F1851) |  |
| [Create Down Payment Request Part II](#unique_23) [page ] 30 | Accounts Payable Accountant | Post Incoming Payments (F1345) | This step is to post a down payment. |
| [Post Incoming Payment](#unique_24) [page ] 31 | Billing Clerk | Create Billing Documents (F0798) |  |
| [Check Sales Contract Status (Optional)](#unique_25) [page ] 33 | Internal Sales Representative | Manage Sales Contracts (F1851) |  |
| [Check Sales Order’s Delivery Block (Optional)](#unique_26) [page ] 34 | Internal Sales Representative | Manage Sales Orders (F1873) |  |
| [Create Sales Order without Delivery Block](#unique_27) [page ] 35 | Internal Sales Representative | Manage Sales Orders (F1873) | The sale order is created. |
| [Create Outbound Delivery](#unique_28) [page ] 36 | Shipping Specialist | Create Outbound Deliveries (F0869A) | The delivery is created. |
| [Execute Picking](#unique_29) [page ] 37 | Shipping Specialist | Manage Outbound Deliveries (F0867A) | Picking is done. |
| [Post Goods Issue](#unique_30) [page ] 38 | Shipping Specialist | Manage Outbound Deliveries (F0867A) | The goods issue is posted. |
| [Billing](#unique_31) [page ] 39 |  | Open Create Billing Documents (F0798) | The billing document is created. |
| [Schedule Automatic Clearing Job (Optional)](#unique_32) [page ] 40 | General Ledger Accountant | Schedule General Ledger Accounting Jobs (F1927) | The General Ledger job is created. |
| Scenario 3: Price Agreement for Quantity Contract |  |  |  |
| [Create Sales Contract (Quantity)](#unique_33) [page ] 41 | Internal Sales Representative | Manage Sales Contracts - Version 2 (F5987) |  |
| [Create Sales Order with Price Agreements](#unique_34) [page ] 43 |  |  |  |
| [Option 1 – Create Sales Order with Contract Reference](#unique_35) [page ] 44 | Internal Sales Representative | Manage Sales Orders (F1873) |  |
| [Option 2 – Create Sales Order and Assign Sales Contract](#unique_36) [page ] 45 | Internal Sales Representative | Manage Sales Orders (F1873) |  |
| [Create Outbound Delivery](#unique_37) [page ] 46 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) |  |
| [Execute Picking](#unique_38) [page ] 47 | Shipping Specialist | Manage Outbound Deliveries (F0867A) |  |
| [Post Goods Issue](#unique_39) [page ] 48 | Shipping Specialist | Manage Outbound Deliveries (F0867A) |  |
| [Billing](#unique_40) [page ] 49 | Billing Clerk | Create Billing Documents (F0798) |  |
| Scenario 4: Price Agreement for Value Contract with Products |  |  |  |
| [Create Sales Contract (Value)](#unique_41) [page ] 50 | Internal Sales Representative | Manage Sales Contracts - Version 2 (F5987) |  |
| [Create Sales Order with Price Agreements](#unique_42) [page ] 52 |  |  |  |
| [Option 1 – Create Sales Order with Contract Reference](#unique_43) [page ] 53 | Internal Sales Representative | Manage Sales Orders (F1873) |  |
| [Option 2 – Create Sales Order and Assign Sales Contract](#unique_44) [page ] 54 | Internal Sales Representative | Manage Sales Orders (F1873) |  |
| [Create Outbound Delivery](#unique_45) [page ] 55 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) |  |
| [Execute Picking](#unique_46) [page ] 56 | Shipping Specialist | Manage Outbound Deliveries (F0867A) |  |
| [Post Goods Issue](#unique_47) [page ] 57 | Shipping Specialist | Manage Outbound Deliveries (F0867A) |  |
| [Billing](#unique_48) [page ] 58 | Billing Clerk | Create Billing Documents (F0798) |  |
| Scenario 5: Price Agreement for Value Contract with Product Hierarchy |  |  |  |
| [Create Sales Contract (Value)](#unique_49) [page ] 59 | Internal Sales Representative | Manage Sales Contracts - Version 2 (F5987) |  |
| [Create Sales Order with Price Agreements](#unique_50) [page ] 61 |  |  |  |
| [Option 1 – Create Sales Order with Contract Reference](#unique_51) [page ] 62 | Internal Sales Representative | Manage Sales Orders (F1873) |  |
| [Option 2 – Create Sales Order and Assign Sales Contract](#unique_52) [page ] 63 | Internal Sales Representative | Manage Sales Orders (F1873) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

The Enterprise search function provides a central entry point for finding business objects in your company from different sources using a single search request, you can search for objects, such as, Apps, factsheets for business objects. From the data found, you can go directly to the respective apps and factsheets to display, edit the data or find related objects.

How to access and check a factsheet: Log on to the SAP Fiori launchpad using the respective user, for example, Internal Sales Representative.

Access the Enterprise Search Bar and choose the magnifying glass button in the upper right corner.

The Enterprise Search bar is displayed, two filter fields appear left to the search button. Enter your Search Criteria and choose the business object type, for example, Sales orders from drop down menu in first field, enter sales order number in second field and choose Search. The sales order is listed.

Choose the sales order number link: the system navigates to the factsheet screen and sales order related information is integrated and summarized in one SAP Fiori page; you can get detailed data via choosing the corresponding links.

There are factsheets available for the following objects: (Visible depending on the assigned role):

- Sales order
- Quotation
- Billing document
- Credit Memo
- Debit Memo
- Customer 360 Fact sheet

### Scenario 1: Sales Quantity or Sales Value Contract

#### Create Sales Contract (Quantity)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create sales quantity contract.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Contracts (F1851). | The Manage Sales Contracts screen displays. |  |
| 3 | Choose Create Contract | Choose Create Contract. | The Create Contracts screen displays. |  |
| 4 | Enter Sales Contract Type | Make the following entries and choose Enter:Contract Type: CQSales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 5 | Enter Customer Information | Make the following entries and choose Enter:Sold-to Party: 33100001 |  |  |
| 6 | Maintain Contract Details | Make the following entries:Customer Reference: <PO number>Material: TG12Valid From: <today’s date>Valid To: <today’s date + one year>Target Quantity: for example, 100 PCNote For LUMF material, sub-items of LUMF material are determined from LUMF material automatically. It is not recommended to add sub-item of LUMF material manually. Otherwise, the down payment status and delivery block on subsequent sales orders are not determined properly. | If the material is TG12, the column Customer Material should be taken the value HANACT2. You can open Manage Customer Manterial to edit or display the customer material information. |  |
| 7 | Save | Choose Save.Note Please ignore any pop-up windows. |  |  |

#### Create Sales Contract (Value)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create sales value contract.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Contracts (F1851). | The Manage Sales Contract screen displays. |  |
| 3 | Create Contract | Choose Create Contract. | The Create Contract screen displays. |  |
| 4 | Enter Sales Contract Type | Make the following entries and choose Enter:Contract Type: VC01Sales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 5 | Enter Customer Information | Make the following entries and choose Enter:Sold-to Party: 33100001 |  |  |
| 6 | Maintain Contract Details | Make the following entries:Customer Reference: <PO number>Material: TG12Valid From: <today’s date>Valid To: <today’s date + one year>Target Value: for example, 1000 AEDChoose Display Header Details. Choose the Partner tab. Make the following entries:Partner Function: SP contract rel. ordPartner: 33100001 |  |  |
| 7 | Save | Choose Save.Note Please ignore any pop-up windows. |  |  |

#### Print Form - Output Management

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to generate the output for sales contract.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Contracts (F1851). | The Manage Sales Contracts displays. |  |
| 3 | Search for Sales Contract | Enter search term(s) in the filter bar and choose Go. For example, enter sales contract number and Sold-to Party: 33100001 in the Sales Contract field. | The sales contract displays in result list. |  |
| 4 | Navigate to Sales Contract Screen | Click the line of the sales contract number you want to display and it will navigate to the Sales Contract page. | The Display Contract xxx: Overview screen displays. |  |
| 5 | Check Output Condition | On the Display Contract xxx: Overview screen, choose More > Extras > Output > Header > Edit . | The document prints. |  |
| 6 | Display Print Preview | On the Display Contract xxx: Output screen, select the line already created for the print output and choose Display PDF Document. |  |  |
| 7 | Print | Choose your local destination and choose Print. |  |  |

#### List Sales Contracts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to review all sales contracts created for certain sold-to party.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open List Incomplete Sales Contracts (F2430). | The Incomplete Sales Documents screen displays. |  |
| 3 | Query Incomplete Sales Contract | Enter the necessary criteria.Choose Go. | All Incomplete Sales Contract display. |  |

### Scenario 2: Quantity Contract Based Down Payments

#### Create Sales Contract (Quantity)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create sales quantity contract.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Contracts (F1851). | The Manage Sales Contracts screen displays. |  |
| 3 | Choose Create Contract | Choose Create Contract. | The Create Contracts screen displays. |  |
| 4 | Enter Sales Contract Type | Make the following entries and choose Continue:Contract Type: CQSales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 5 | Enter Customer Information | Make the following entries and choose Enter:Sold-to Party: 33100001Customer Reference:<Test> |  |  |
| 6 | Maintain Contract Details | Make the following entries:Valid From: <today’s date>Valid To: <End of this year>Material: TG11Target Quantity: for example, 10 PCItCa: CKMNNote The default value is KMN. But for this process, item category CKMN needs to be entered manually.Note For the ERLA material: SDBOMERLAHD, the item category is CKMN.For the LUMF material: SDBOMLUMFHD, the item category is CKMB.If dialog box Choose an unloading point appears, select one entry then choose Copy. | If the material is TG12, the column Customer Material should be taken the value HANACT2. You can open Manage Customer Material to edit or display the customer material information. |  |
| 7 | Maintain the billing plan | Select the item 10, then choose Bill plan button.Check the net value of this item, and record it.Then maintian two entries in the Billing Plan tab:First entry: Billing Date: <today>Bill.Value:100 AEDSecond entry: Billing Date: <today+1>Bill.Value: <Net value-100 AED >Choose Back. |  |  |
| 8 | Save | Choose Save and record the quantity contract number.Note Please ignore any pop-up windows. | The quantity contract is saved. |  |

#### Remove Billing Block in Sales Contract manually

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
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Contracts (F1851) . | The Manage Sales Contracts (F1851) screen displays. |  |
| 3 | Remove the block | Choose the sales contract that was created in step Create Sales Contract (Quantity), and choose Change, then double click the item.Choose the Billing Plan tab, and delete the billing block Y2 in the Block field for the first entry, then choose Back. |  |  |
| 4 | Choose Save | Choose Save. |  |  |

#### Create Sales Order with Delivery Block

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to maintain sales order with delivery block.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Navigate to Create Sales Order Screen | Choose Create, then Create Sales Order-VA01. | The Create Sales Documents: Initial screen displays. |  |
| 4 | Enter Sales Document Type | Make the following entries:Order Type: <sales order type> , for example, OR (Standard Order)Sales Organization: 3310Distribution Channel: 10Division: 00Choose Create with Reference.Choose the Contract tab, and input the number of the contract which was created in the last step, then choose the Copy button.If the information dialog box displays, choose Continue. | The Create Standard Order xxx: Overview screen displays. |  |
| 5 | Enter Customer Reference and Order Quantity | Check and maintain the following entries:Customer Reference: <call-off order>Order Quantity：1 |  |  |
| 6 | Save | Choose Save and record the sales order number. |  |  |
| 7 | Check the status | Choose More > Sales Document > Display , double-click the item 10, then choose the Schedule Lines to check the status. You will find that the entries have the delivery block (Check Prepayment) set in the Delivery Block field. |  |  |

#### Create Down Payment Request Part I

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a down payment request.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Document screen displays. |  |
| 3 | Define Billing Setting | Choose Billing Settings in bottom bar.There are four settings. Set the below settings to ON:Create separate billing documents for each item of billing due listAutomatically post billing documentsDisplay billing document after creationThen choose OK. |  |  |
| 4 | Search for Billing List | In the search condition, enter criteria if necessary.SD Document category: <Contract>Billing Date to:<Today> | SD document(s) displays in the result. |  |
| 5 | Choose Sales Contract | Select the item that was created in the step Create Sales Contract (Quantity), and choose Create. | The Create Billing Documents screen displays. |  |
| 6 | Save the Down Payment Request | Choose Save. |  |  |

#### Check Sales Contract Status (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Contracts (F1851). | The Manage Sales Contracts screen displays. |  |
| 3 | Choose Contract item and check the status | Choose the sales contract that was created in step Create Sales Contract (Quantity).Double-click the item, then choose the Billing Plan tab. You can find that the BillSt (Billing Status) field of the first entry was changed to C.Then choose the Status tab to check the Billing status and Down Payment Status. You can see the Ord. Rel. Billg Status is changed to Partially Invoiced, and the Down Payment Status is changed to Not Paid.Note If you are using LUMF materials, perform the above steps for items 20 and 30 instead of item 10. |  |  |
| 4 | Choose Back | Choose Back. |  |  |

#### Remove Billing Block in Sales Contract manually

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to remove billing blocks.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Contracts (F1851) . | The Manage Sales Contracts (F1851) screen displays. |  |
| 3 | Remove the block | Choose the sales contract that was created in step Create Sales Contract (Quantity). Choose Change, then double click the item.Choose the Billing Plan tab, and delete the billing block Y2 in the Block field of the second entry, then choose Back.Note If you are using LUMF materials, perform the above steps for items 20 and 30 instead of item 10. |  |  |
| 4 | Choose Save | Choose Save. |  |  |

#### Create Down Payment Request Part II

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a down payment request.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798) | The Create Billing Document screen displays. |  |
| 3 | Define Billing Setting | Choose Billing Settings in bottom bar.There are four settings. Set the below settings to ON:Create separate billing documents for each item of billing due listAutomatically post billing documentsDisplay billing document after creationThen choose OK. |  |  |
| 4 | Search for Billing List | In the search condition, enter criteria if necessary.SD Document category: <Contract>Billing Date to:<Today +1> | SD document(s) displays in the result. |  |
| 5 | Choose Sales Contract | Select the second item that was created in the step Create Sales Contract (Quantity), and choose Create. | The Create Billing Documents screen displays. |  |
| 6 | Save the Down Payment Request | Choose Save. |  |  |

#### Post Incoming Payment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post a down payment.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Incoming Payments (F1345). | The Post Incoming Payments (F1345) screen displays. |  |
| 3 | Enter Details | Make the following entries and choose Propose Items:In the General Information area:Company Code: 3310Posting Date: Current dateJournal Entry Date: <Current date>Value Date: Current datePeriod: Current periodJournal Entry Type: DZ (Customer Payment)In the Bank Data area:G/L Account (Company Code CoA): 11001060Amount: Down Payment Amount(For example:100+Tax) / AEDNote Enter the amount of the journal entry the customer has been debited with in the previous step (billing value plus value added tax).In the Open Item Selection area, then choose Propose Items:Account Type/Account ID: Customer / 33100001 |  |  |
| 4 | Search for Down Payment Request | Choose Select More.In field Line Item Type, select Special G/L Transactions and enter value F in field Special G/L, then choose OK. | Select More dialog box displays.All down payment request documents which meet the conditions are listed in Open Items table. |  |
| 5 | Select Down Payment Request | In the Open Items section, select the item of the relevant down payment request with value 100+TAX AED, and choose Clear.Note If you want to find the right entry with Journal Entry number, you can check the Display Document Flow in sales contract to find it. | The item is copied to Items to Be Cleared table. |  |
| 6 | Post | Choose Post. | The Success dialog box displays, the information Journal entry 14XXXXXXXX successfully posted displays. |  |
| 7 | Select Down Payment Request | Choose Post Next Payment in the dialog box.Repeat steps 3-6 for another entry in the sales contract.In the Open Items section, select the item of the relevant down payment request with value Down Payment Amount <Net value-100+Tax AED >, and choose Clear.Note If you want to find the right entry with Journal Entry number, you can check the Display Document Flow in sales contract to find it. | The item is copied to Items to Be Cleared table. |  |
| 8 | Display the document | Choose Display in the dialog box. |  |  |

#### Check Sales Contract Status (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Contracts (F1851). | The Manage Sales Contracts screen appears. |  |
| 3 | Choose Contract item and check the status | Choose the sales contract that was created in step Create Sales Contract (Quantity). Double click the item, then choose the Status tab to check the Billing Status and Down Payment Status.The down payment status is changed after down payment is cleared in FI. You can see the Ord. Rel. Billg Status is changed to Fully Invoiced, and the Down Payment Status is changed to Fully Paid.Note If use the LUMF material, please do above steps for item 20 and item 30, not item 10. | The Create Contracts screen displays. |  |
| 4 | Choose Back. | Choose Back. |  |  |

#### Check Sales Order’s Delivery Block (Optional)

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
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Check the status | Choose the sales order that was created in step Create Sales Order with Delivery Block.Double click the item 10, then choose the Schedule Lines tab to check the status, you will find that the Delivery Block for the entry was removed. |  |  |
| 4 | Choose Back | Choose Back. |  |  |

#### Create Sales Order without Delivery Block

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create sale order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Navigate to Create Sales Order Screen | Choose +, then Create Sales Order-VA01. | The Create Sales Documents: Initial screen displays. |  |
| 4 | Enter Sales Document Type | Maintain the entry in the screen:Order Type: <sales order type> , for example, OR (Standard Order)Sales Organization: 3310Distribution Channel: 10Division: 00Choose Create with Reference.Choose the Contract tab, and input the contract number that was created in step Create Sales Contract (Quantity), then choose Copy. | The Create Standard Order xxx: Overview screen displays. |  |
| 5 | Enter Customer Number | Check and maintain the following entries:Sold-To Party: 33100001Customer Reference: <call-off order>Order Quantity：2 |  |  |
| 6 | Save | Choose Save. |  |  |
| 7 | Check the status | Choose More > Sales Document > Display , double click the item 10, then choose the Schedule Lines to check the delivery block, you will find that the delivery block was removed. |  |  |

#### Create Outbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create delivery.

Prerequisite

The goods receipt was posted to the individual customer’s stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Create Outbound Deliveries - From Sales Orders (F0869A). | The Create Outbound Deliveries - From Sales Orders (F0869A) screen displays. |  |
| 3 | Search Sales Order | Make the following entries and choose Go:Shipping Point: <shipping point> for example, 3310Planned Creation Date: <Delivery selection date>Order: <Sales order number created in Create Sales Order with Delivery Block/ Create Sales Order without Delivery Block> |  |  |
| 4 | Create Delivery | Select your sales order and choose Create Deliveries. |  |  |
| 5 | Check Details | Choose Display Log. | The Analyze Delivery Log screen displays. Delivery is created successfully with delivery number shown on tab Deliveries. |  |

#### Execute Picking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The picking process involves taking goods from a storage location and staging the right quantity in a picking area where the goods are prepared for shipping. This process step shows you how to pick deliveries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries (F0867A). |  |  |
| 3 | Set the critea | Make the following entries, and choose Go:Shipping Point: 3310Overall Status: Ready for Picking |  |  |
| 4 | Choose the outbund delivery for picking | Select the outbound delivery that was created in last step, then choose Pick. | Pick Outbound Delivery screen displays. |  |
| 5 | Picking for inbound delivery | On the Pick Outbound Delivery screen, make the following entry and choose Enter:Picking Quantity: The quantity of Sales Order |  |  |
| 6 | Save | Choose Save. | The delivery has been picked. |  |

|  |
| --- |
| Note For the ERLA / LUMF material, please do the following steps. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). |  |  |
| 3 | Input the inbound delivery number | Make the following entries, and choose Continue:Outbound Delivery: the outbound delivery number that was created in step Create Outbound Delivery. |  |  |
| 4 | Picking for inbound delivery | Choose the Picking tab, then make the following entry and choose Enter:For ERLA material, Picking Quantity: The quantity of sale order item 10For LUMF material, Picking Quantity: The quantity of sale order item 20/item 30 |  |  |
| 5 | Save | Choose Save. |  |  |

#### Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post goods issues for delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Manage Outbound Deliveries (F0867A). |  |  |
| 3 | Set the critea | Make the following critera, and choose Go.Shipping Point: 3310Overall Status: Ready to Post GI |  |  |
| 4 | Choose the outbund delivery for picking | Select the outbound delivery that was created in last step, then choose Pick. | The Pick Outbound Delivery screen displays. |  |
| 5 | Post for inbound delivery | On the Pick Outbound Delivery screen, choose Post GI. |  |  |

|  |
| --- |
| Note For the ERLA / LUMF material, please follow below steps. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). |  |  |
| 3 | Input the inbound delivery number | Make the following entries, and choose Continue:Outbound Delivery: the outbound delivery number that was created in step Create Outbound Delivery. |  |  |
| 4 | Post Goods Issue | Choose Post Goods Issue. |  |  |

#### Billing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to bill a customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Document screen displays. |  |
| 3 | Search for Billing List | In the search condition, enter criteria if necessary. |  |  |
| 4 | Choose Sales Document | Select the sales document that was created previously and choose Create. |  |  |
| 5 | Save | Choose Save. |  |  |
| 6 | Display Billing Document | Choose Process Flow tab, and choose the Invoice just created.Choose Display Billing Documents. On the Invoice XXX Display: Overview of Billing Items screen, you can find one special item with Item Description Down Payment Settlement was created. |  |  |

#### Schedule Automatic Clearing Job (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows how to schedule job to clear journal entries automatically.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule General Ledger Accounting Jobs (F1927). | The Application Jobs screen displays. |  |
| 3 | Schedule job for automatic clearing | Choose +.Job Template: Automatic ClearingJob Name: Automatic ClearingStart Immediately: SelectedSelect Customers: SelectedSpecial G/L Indicator-Customer: select AClearing Date:TodayTest Run: DeselectChoose Schedule. | The information Job Automatic Clearing has been scheduled can be displayed in the log. |  |

### Scenario 3: Price Agreement for Quantity Contract

#### Create Sales Contract (Quantity)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create sales quantity contract.

Preliminary Steps

1. You can create your own price maintenance scenarios by SSCUI 106836 Define Price Maintenance Scenarios.
2. You can assign your price maintenance scenarios in item category KMN by SSCUI 103411 Define Item category.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Contracts - Version 2 (F5987). | The Manage Sales Contracts - Version 2 screen displays. |  |
| 3 | Choose Create Contract | Choose Create. | The Create Contracts screen displays. |  |
| 4 | Enter Sales Contract Type | Make the following entries and choose Continue:Contract Type: CQSales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 5 | Enter Customer Information | Make the following entries in the second screen:Sold-to Party: 33100001Customer Reference: <Test> |  |  |
| 6 | Maintain Contract Details | Make the following entries:Valid From: <Today’s date>Valid To: <End of this year>In the Item section, make the following entries:Product: TG11Target Quantity: for example, 10 PCItCa: KMN | If the material is TG12, the column Customer Material should be taken the value HANACT2. You can open Manage Customer Material to edit or display the customer material information. |  |
| 7 | Maintain the Price Agreements | Select the item 10, and go to the object page.Then maintain one entry in the Price Agreement tab:Condition Type: DPA1Valid From:<Today's date>Valid To: <End of this year>Condition Amount or Ratio: -10%In the detailed screen, maintain the following information in the Scale tab:Scale Type: for example, FromScale Quantity or Value: for example, 1000 AEDCondition Amount or Ratio: -10%Choose Apply. |  |  |
| 8 | Save | Choose Save and record the quantity contract number. | The quantity contract is saved. |  |

#### Create Sales Order with Price Agreements

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to maintain sales order with determaination of price agreements from the sales contract.

##### Option 1 – Create Sales Order with Contract Reference

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Navigate to Create Sales Order Screen | Choose Create, then Create Sales Order-VA01. | The Create Sales Documents: Initial screen displays. |  |
| 4 | Enter Sales Document Type | Make the following entries:Order Type: <sales order type> , for example, OR (Standard Order)Sales Organization: 3310Distribution Channel: 10Division: 00Choose Create with Reference.Choose the Contract tab, and input the number of the contract which was created in the last step, then choose the Copy button.If the information dialog box displays, choose Continue. | The Create Standard Order xxx: Overview screen displays. |  |
| 5 | Enter Customer Reference and Order Quantity | Check and maintain the following entries:Customer Reference: <call-off order>Order Quantity：1 |  |  |
| 6 | Check the Pricing Condition | Choose Pricing Conditions tab and check the pricing conditions. | You will find that the entries of price agreements with condition type DAP1 are displayed. |  |
| 7 | Save | Choose Save and record the sales order number. |  |  |

##### Option 2 – Create Sales Order and Assign Sales Contract

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Navigate to Create Sales Order Screen | Choose Create, then Create Sales Order-VA01. | The Create Sales Documents: Initial screen displays. |  |
| 4 | Enter Sales Document Type | Make the following entries choose Continue:Order Type: <sales order type>, for example, OR (Standard Order)Sales Organization: 3310Distribution Channel: 10Division: 00 | The Create Standard Order xxx: Overview screen displays. |  |
| 5 | Enter Customer Information | Make the following entries and choose Enter:Sold-to Party: 33100001Customer Reference: <Test> |  |  |
| 6 | Maintain Contract Details | In the Item section, make the following entries:Product: TG11Order Quantity: for example, 10 PCItCa: TAN |  |  |
| 7 | Assign the Contract | Go to the menu bar, and choose Edit, then Assign Contract.Choose Headers (Items Automaticaly Assigned), and input the number of the contract which was created in step [Create Sales Contract (Quantity)](#unique_33) [page ] 41, then choose the Assign button.If the information dialog box displays, choose Continue.Note If you choose the contract assignment per order item level, you need to choose the orders items and then assign the contract. | You will find the application log to display the contract assignment results. |  |
| 8 | Check the Pricing Condition | Choose Pricing Conditions tab and check the pricing conditions. | You will find that the entries of price agreements with condition type DAP1 are displayed. |  |
| 9 | Save | Choose Save and record the sales order number. |  |  |
| 10 | Check the logs | Choose More > Sales Document > Display , then choose the Log to check the results. | You will find that the entries have the results of contract assignment. |  |

#### Create Outbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create delivery.

Prerequisite

The goods receipt was posted to the individual customer’s stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Create Outbound Deliveries - From Sales Orders (F0869A). | The Create Outbound Deliveries - From Sales Orders (F0869A) screen displays. |  |
| 3 | Search Sales Order | Make the following entries and choose Go:Shipping Point: <shipping point> for example, 3310Planned Creation Date: <Delivery selection date>Order: <Sales order number created in Create Sales Order with Delivery Block/ Create Sales Order without Delivery Block> |  |  |
| 4 | Create Delivery | Select your sales order and choose Create Deliveries. |  |  |
| 5 | Check Details | Choose Display Log. | The Analyze Delivery Log screen displays. Delivery is created successfully with delivery number shown on tab Deliveries. |  |

#### Execute Picking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The picking process involves taking goods from a storage location and staging the right quantity in a picking area where the goods are prepared for shipping. This process step shows you how to pick deliveries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries (F0867A). |  |  |
| 3 | Set the critea | Make the following entries, and choose Go:Shipping Point: 3310Overall Status: Ready for Picking |  |  |
| 4 | Choose the outbound delivery for picking | Select the outbound delivery that was created in last step, then choose Pick. | Pick Outbound Delivery screen displays. |  |
| 5 | Picking for inbound delivery | On the Pick Outbound Delivery screen, make the following entry and choose Enter:Picking Quantity: The quantity of Sales Order |  |  |
| 6 | Save | Choose Save. | The delivery has been picked. |  |

|  |
| --- |
| Note For the ERLA / LUMF material, please do the following steps. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). |  |  |
| 3 | Input the inbound delivery number | Make the following entries, and choose Continue:Outbound Delivery: the outbound delivery number that was created in step Create Outbound Delivery. |  |  |
| 4 | Picking for inbound delivery | Choose the Picking tab, then make the following entry and choose Enter:For ERLA material, Picking Quantity: The quantity of sale order item 10For LUMF material, Picking Quantity: The quantity of sale order item 20/item 30 |  |  |
| 5 | Save | Choose Save. |  |  |

#### Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post goods issues for delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Manage Outbound Deliveries (F0867A). |  |  |
| 3 | Set the Criteria | Make the following criteria, and choose Go.Shipping Point: 3310Overall Status: Ready to Post GI |  |  |
| 4 | Choose Outbound Delivery for Posting Goods Issues | Select the outbound delivery that was created in last step, then choose Pick. | The Pick Outbound Delivery screen displays. |  |
| 5 | Post for Outbound Delivery | On the Post Goods Issues screen, choose Post GI. |  |  |

|  |
| --- |
| Note For the ERLA / LUMF material, please follow below steps. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). |  |  |
| 3 | Input the Outbound Delivery Number | Make the following entries, and choose Continue:Outbound Delivery: the outbound delivery number that was created in step Create Outbound Delivery. |  |  |
| 4 | Post Goods Issue | Choose Post Goods Issue. |  |  |

#### Billing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to bill a customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Document screen displays. |  |
| 3 | Search for Billing List | In the search condition, enter criteria if necessary. |  |  |
| 4 | Choose Sales Document | Select the sales document that was created previously and choose Create. |  |  |
| 5 | Save | Choose Save. |  |  |
| 6 | Display Billing Document | Choose Process Flow tab, and choose the Invoice just created.Choose Display Billing Documents. On the Invoice XXX Display: Overview of Billing Items screen, you can find one special item with condition type DPA1 was created. |  |  |

### Scenario 4: Price Agreement for Value Contract with Products

#### Create Sales Contract (Value)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create sales quantity contract.

Preliminary Steps

1. You can create your own price maintenance scenarios by SSCUI 106836 Define Price Maintenance Scenarios.
2. You can assign your price maintenance scenarios in item category VC02 by SSCUI 103411 Define Item Category.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Contracts - Version 2 (F5987). | The Manage Sales Contracts - Version 2 screen displays. |  |
| 3 | Choose Create Contract | Choose Create. | The Create Contracts screen displays. |  |
| 4 | Enter Sales Contract Type | Make the following entries and choose Continue:Contract Type: VC01Sales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 5 | Enter Customer Information | Make the following entries in the second screen:Sold-to Party: 33100001Customer Reference: <Test> |  |  |
| 6 | Maintain Contract Details | Make the following entries:Valid From: <Today’s date>Valid To: <End of this year>In the Item section, make the following entries:Product: TG11Target Quantity: for example, 1,000 AEDItCa: VC02Note The default value is VC01. But for this process, item cate-gory VC02 needs to be entered manually. | If the material is TG12, the column Customer Material should be taken the value HANACT2. You can open Manage Customer Material to edit or display the customer material information. |  |
| 7 | Maintain the Price Agreements | Select the item 10, and go to the object page.Then maintain one entry in the Price Agreement tab:Condition Type: DPA1Valid From: <Today's date>Valid To: <End of this year>Condition Amount or Ratio: -10%Choose Apply. |  |  |
| 8 | Save | Choose Save and record the value contract number. | The value contract is saved. |  |

#### Create Sales Order with Price Agreements

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to maintain sales order with determaination of price agreements from the sales contract.

##### Option 1 – Create Sales Order with Contract Reference

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Navigate to Create Sales Order Screen | Choose Create, then Create Sales Order-VA01. | The Create Sales Documents: Initial screen displays. |  |
| 4 | Enter Sales Document Type | Make the following entries:Order Type: <sales order type> , for example, OR (Standard Order)Sales Organization: 3310Distribution Channel: 10Division: 00Choose Create with Reference.Choose the Contract tab, and input the number of the contract which was created in the last step, then choose the Copy button.If the information dialog box displays, choose Continue. | The Create Standard Order xxx: Overview screen displays. |  |
| 5 | Enter Customer Reference and Order Quantity | Check and maintain the following entries:Customer Reference: <call-off order>Order Quantity：1 |  |  |
| 6 | Check the Pricing Condition | Choose Pricing Conditions tab and check the pricing conditions. | You will find that the entries of price agreements with condition type DAP1 are displayed. |  |
| 7 | Save | Choose Save and record the sales order number. |  |  |

##### Option 2 – Create Sales Order and Assign Sales Contract

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Navigate to Create Sales Order Screen | Choose Create, then Create Sales Order-VA01. | The Create Sales Documents: Initial screen displays. |  |
| 4 | Enter Sales Document Type | Make the following entries choose Continue:Order Type: <sales order type>, for example, OR (Standard Order)Sales Organization: 3310Distribution Channel: 10Division: 00 | The Create Standard Order xxx: Overview screen displays. |  |
| 5 | Enter Customer Information | Make the following entries and choose Enter:Sold-to Party: 33100001Customer Reference: <Test> |  |  |
| 6 | Maintain Contract Details | In the Item section, make the following entries:Product: TG11Order Quantity: for example, 10 PCItCa: TAN |  |  |
| 7 | Assign the Contract | Go to the menu bar, and choose Edit, then Assign Contract.Choose Headers (Items Automaticaly Assigned), and input the number of the contract which was created in the step [Create Sales Contract (Value)](#unique_41) [page ] 50, then choose the Assign button.If the information dialog box displays, choose Continue.Note If you choose the contract assignment per order item level, you need to choose the orders items and then assign the contract. | You will find the application log to display the contract assignment results. |  |
| 8 | Check the Pricing Condition | Choose Pricing Conditions tab and check the pricing conditions. | You will find that the entries of price agreements with condition type DAP1 are displayed. |  |
| 9 | Save | Choose Save and record the sales order number. |  |  |
| 10 | Check the logs | Choose More > Sales Document > Display , then choose the Log to check the results. | You will find that the entries have the results of contract assignment. |  |

#### Create Outbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create delivery.

Prerequisite

The goods receipt was posted to the individual customer’s stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Create Outbound Deliveries - From Sales Orders (F0869A). | The Create Outbound Deliveries - From Sales Orders (F0869A) screen displays. |  |
| 3 | Search Sales Order | Make the following entries and choose Go:Shipping Point: <shipping point>, for example, 3310Planned Creation Date: <Delivery selection date>Order: <Sales order number created in Create Sales Order with Delivery Block/ Create Sales Order without Delivery Block> |  |  |
| 4 | Create Delivery | Select your sales order and choose Create Deliveries. |  |  |
| 5 | Check Details | Choose Display Log. | The Analyze Delivery Log screen displays. Delivery is created successfully with delivery number shown on tab Deliveries. |  |

#### Execute Picking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The picking process involves taking goods from a storage location and staging the right quantity in a picking area where the goods are prepared for shipping. This process step shows you how to pick deliveries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries (F0867A). |  |  |
| 3 | Set the critea | Make the following entries, and choose Go:Shipping Point: 3310Overall Status: Ready for Picking |  |  |
| 4 | Choose the Outbound Delivery for Picking | Select the outbound delivery that was created in last step, then choose Pick. | The Pick Outbound Delivery screen displays. |  |
| 5 | Picking for Outbound Delivery | On the Pick Outbound Delivery screen, make the following entry and choose Enter:Picking Quantity: The quantity of Sales Order |  |  |
| 6 | Save | Choose Save. | The delivery has been picked. |  |

|  |
| --- |
| Note For the ERLA / LUMF material, please do the following steps. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). |  |  |
| 3 | Input the inbound delivery number | Make the following entries, and choose Continue:Outbound Delivery: the outbound delivery number that was created in step Create Outbound Delivery. |  |  |
| 4 | Picking for inbound delivery | Choose the Picking tab, then make the following entry and choose Enter:For ERLA material, Picking Quantity: The quantity of sale order item 10For LUMF material, Picking Quantity: The quantity of sale order item 20/item 30 |  |  |
| 5 | Save | Choose Save. |  |  |

#### Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post goods issues for delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Manage Outbound Deliveries (F0867A). |  |  |
| 3 | Set the Criteria | Make the following criteria, and choose Go.Shipping Point: 3310Overall Status: Ready to Post GI |  |  |
| 4 | Choose Outbound Delivery for Posting Goods Issues | Select the outbound delivery that was created in last step, then choose Pick. | The Pick Outbound Delivery screen displays. |  |
| 5 | Post for Outbound Delivery | On the Post Goods Issues screen, choose Post GI. |  |  |

|  |
| --- |
| Note For the ERLA / LUMF material, please follow below steps. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). |  |  |
| 3 | Input the Outbound Delivery Number | Make the following entries, and choose Continue:Outbound Delivery: the outbound delivery number that was created in step Create Outbound Delivery. |  |  |
| 4 | Post Goods Issue | Choose Post Goods Issue. |  |  |

#### Billing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to bill a customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Document screen displays. |  |
| 3 | Search for Billing List | In the search condition, enter criteria if necessary. |  |  |
| 4 | Choose Sales Document | Select the sales document that was created previously and choose Create. |  |  |
| 5 | Save | Choose Save. |  |  |
| 6 | Display Billing Document | Choose Process Flow tab, and choose the Invoice just created.Choose Display Billing Documents. On the Invoice XXX Display: Overview of Billing Items screen, you can find one special item with condition type DPA1 was created. |  |  |

### Scenario 5: Price Agreement for Value Contract with Product Hierarchy

#### Create Sales Contract (Value)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create sales quantity contract.

Preliminary Steps

1. You can create your own price maintenance scenarios by SSCUI 106836 Define Price Maintenance Scenarios.
2. You can assign your price maintenance scenarios in item category VC03 by SSCUI 103411 Define Item Category.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Contracts - Version 2 (F5987). | The Manage Sales Contracts - Version 2 screen displays. |  |
| 3 | Choose Create Contract | Choose Create. | The Create Contracts screen displays. |  |
| 4 | Enter Sales Contract Type | Make the following entries and choose Continue:Contract Type: VC01Sales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 5 | Enter Customer Information | Make the following entries in the second screen:Sold-to Party: 33100001Customer Reference: <Test> |  |  |
| 6 | Maintain Contract Details | Make the following entries:Valid From: <Today’s date>Valid To: <End of this year>In the Item section, make the following entries:Product Hierarchy: TOOLSProduct Hierarchy Node: ADJUST_JOINT_PLIERSTarget Quantity: for example, 10,000 AEDItCa: VC03 | If the material is TG12, the column Customer Material should be taken the value HANACT2. You can open Manage Customer Material to edit or display the customer material information. |  |
| 7 | Maintain the Price Agreements | Select the item 10, and go to the object page.Then maintain one entry in the Price Agreement tab:Condition Type: DPA1Valid From:<Today's date>Valid To: <End of this year>Condition Amount or Ratio: -10%Choose Apply. |  |  |
| 8 | Save | Choose Save and record the value contract number. | The value contract is saved. |  |

#### Create Sales Order with Price Agreements

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to maintain sales order with determination of price agreements.

##### Option 1 – Create Sales Order with Contract Reference

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Navigate to Create Sales Order Screen | Choose Create, then Create Sales Order-VA01. | The Create Sales Documents: Initial screen displays. |  |
| 4 | Enter Sales Document Type | Make the following entries:Order Type: <sales order type> , for example, OR (Standard Order)Sales Organization: 3310Distribution Channel: 10Division: 00Choose Create with Reference.Choose the Contract tab, and input the number of the contract which was created in the last step.Select the contract item, and then choose the Enter matl button.In the new screen, make the following entries:Material: <Material in Product Hierarchy Node>, for example, TG11_PH_GP300Order Quantity: 10Sales Unit: PCGo back to the copy screen, and choose the Copy button.If the information dialog box displays, choose Continue. | The Create Standard Order xxx: Overview screen displays. |  |
| 5 | Enter Customer Reference and Order Quantity | Check and maintain the following entries:Customer Reference: <call-off order>Order Quantity：1 |  |  |
| 6 | Check the Pricing Condition | Choose Pricing Conditions tab and check the pricing conditions. | You will find that the entries of price agreements with condition type DAP1 are displayed. |  |
| 7 | Save | Choose Save and record the sales order number. |  |  |

##### Option 2 – Create Sales Order and Assign Sales Contract

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Navigate to Create Sales Order Screen | Choose Create, then Create Sales Order-VA01. | The Create Sales Documents: Initial screen displays. |  |
| 4 | Enter Sales Document Type | Make the following entries choose Continue:Order Type: <sales order type>, for example, OR (Standard Order)Sales Organization: 3310Distribution Channel: 10Division: 00 | The Create Standard Order xxx: Overview screen displays. |  |
| 5 | Enter Customer Information | Make the following entries and choose Enter:Sold-to Party: 33100001Customer Reference: <Test> |  |  |
| 6 | Maintain Contract Details | In the Item section, make the following entries:Product: <Material in Product Hierarchy Node>, for example, TG11_PH_GP300Order Quantity: for example, 10 PCItCa: TAN |  |  |
| 7 | Assign the Contract | Go to the menu bar, and choose Edit, then Assign Contract.Choose Headers (Items Automaticaly Assigned), and input the number of the contract which was created in the step [Create Sales Contract (Value)](#unique_49) [page ] 59, then choose the Assign button.If the information dialog box displays, choose Continue.Note If you choose the contract assignment per order item level, you need to choose the orders items and then assign the contract. | You will find the application log to display the contract assignment results. |  |
| 8 | Check the Pricing Condition | Choose Pricing Conditions tab and check the pricing conditions. | You will find that the entries of price agreements with condition type DAP1 are displayed. |  |
| 9 | Save | Choose Save and record the sales order number. |  |  |
| 10 | Check the logs | Choose More > Sales Document > Display , then choose the Log to check the results. | You will find that the entries have the results of contract assignment. |  |

All the remaining steps — such as creating the outbound delivery, executing picking, posting the goods issue, and billing — remain the same as described in the section Scenario 4: Price Agreement for Value Contract with Products.

Refer to the step [Create Outbound Delivery](#unique_45) [page ] 55 in the section Scenario 4: Price Agreement for Value Contract with Products to continue the remaining test procedure.

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
> Flagged while digesting this document, not verified: Overview Table role/app assignments disagree with the procedures: 'Create Down Payment Request Part II' is listed as Accounts Payable Accountant / Post Incoming Payments (F1345) but the procedure uses Billing Clerk / Create Billing Documents (F0798); 'Post Incoming Payment' is listed as Billing Clerk / F0798 but the procedure uses Accounts Receivable Accountant / F1345 (the Roles table has no Accounts Payable Accountant); 'Print Form - Output Management' is listed under Manage Sales Orders (F1873) but the procedure uses Manage Sales Contracts (F1851).

> [!warning] Conflict
> Flagged while digesting this document, not verified: Material TG11 is entered in the Scenario 2 to 5 contract and order steps, but the sample data table lists TG12, TG10, TG13, TG14 and no TG11 (Scenario 1 enters TG12, while the Customer Material note in Scenarios 2 to 5 refers to TG12).

> [!warning] Conflict
> Flagged while digesting this document, not verified: Price agreement condition type is DPA1 when maintained in the contract and checked at billing, but the sales order checks in Scenarios 3 to 5 expect condition type DAP1.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[08-sales-order-management/test-script-sales-order-processing-with-customer-down-payment-bkj-ae-1]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/I9I_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 98,235 chars in the whole document
