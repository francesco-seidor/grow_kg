---
id: 08-sales-order-management/extended-intercompany-processes-for-sales-1wo-ae-test-script-sap-s-4ha
title: "Extended Intercompany Processes for Sales (1WO_AE) - Test Script, SAP S/4HANA Cloud Public Edition (1WO_S4CLD2608_BPD_EN_AE)"
description: "SAP test script for scope item 1WO (AE): intercompany free-of-charge, credit/debit memo, non-stock, sales kits, down payment and consignment, domestic and international."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/intercompany-sales-domestic-and-international]
aliases: [1WO_S4CLD2608_BPD_EN_AE]
keywords: [Intercompany Sales Order Processing (Domestic and…, intercompany sales, free of charge delivery, intercompany credit memo, intercompany debit memo, non-stock material sales, sales kits, down payment, customer consignment, intercompany billing]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1WO_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-771
topic: 08-sales-order-management/intercompany-sales-domestic-and-international
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Extended Intercompany Processes for Sales (1WO_AE) - Test Script, SAP S/4HANA Cloud Public Edition (1WO_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1WO_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Intercompany Sales Order Processing (Domestic and International)** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Extended Intercompany Processes for Sales (1WO_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 5](#_Toc232847818)

[1.1 Free-of-charge 5](#_Toc232847819)

[1.2 Credit Memo and Debit Memo 5](#_Toc232847820)

[1.3 Sales Kits 5](#_Toc232847821)

[1.4 Down Payment 6](#_Toc232847822)

[1.5 Customer Consignment 6](#_Toc232847823)

[2 Prerequisites 7](#_Toc232847824)

[2.1 System Access 7](#_Toc232847825)

[2.2 Roles 7](#_Toc232847826)

[2.3 Master Data, Organizational Data, and Other Data 8](#_Toc232847827)

[2.4 Additional Manual Configuration 10](#_Toc232847828)

[2.5 Business Conditions 11](#_Toc232847829)

[2.6 Preliminary Steps 11](#_Toc232847830)

[2.6.1 Create Initial Stock in the domestic shipping plant 11](#_Toc232847831)

[2.6.2 Create Initial Stock in the international shipping plant 12](#_Toc232847832)

[2.6.3 Create Condition Records (Optional) 13](#_Toc232847833)

[2.6.4 Process Sales Order Approval (Optional) 14](#_Toc232847834)

[2.6.5 Check Advanced Down Payment Processing for Item Category CBAO, CTAD, and CTAX 14](#_Toc232847835)

[3 Overview Table 16](#_Toc232847836)

[4 Test Procedures 23](#_Toc232847837)

[4.1 Domestic 23](#_Toc232847838)

[4.1.1 Free of Charge 23](#_Toc232847839)

[4.1.1.1 Create Free of Charge Sales Order 23](#_Toc232847840)

[4.1.1.2 Create Delivery 24](#_Toc232847841)

[4.1.1.3 Perform Picking 25](#_Toc232847842)

[4.1.1.4 Post Goods Issue 26](#_Toc232847843)

[4.1.1.5 Create F2 Invoice 27](#_Toc232847844)

[4.1.1.6 Create Intercompany IV Invoice 28](#_Toc232847845)

[4.1.1.7 Display AP Accounting Document 29](#_Toc232847846)

[4.1.2 Credit Memo 30](#_Toc232847847)

[4.1.2.1 Create Intercompany Credit Memo 30](#_Toc232847848)

[4.1.2.2 Display AP Accounting Document of Intercompany Credit Memo 32](#_Toc232847849)

[4.1.3 Debit Memo 33](#_Toc232847850)

[4.1.3.1 Create Intercompany Debit Memo 33](#_Toc232847851)

[4.1.3.2 Display AP Accounting Document of Intercompany Debit Memo 34](#_Toc232847852)

[4.1.4 Non-Stock Material Sales 36](#_Toc232847853)

[4.1.4.1 Create Sales Orders 36](#_Toc232847854)

[4.1.4.2 Process Sales Order Approval (Optional) 37](#_Toc232847855)

[4.1.4.3 Create Delivery 37](#_Toc232847856)

[4.1.4.4 Post Goods Issue 38](#_Toc232847857)

[4.1.4.5 Create F2 Invoice 39](#_Toc232847858)

[4.1.4.6 Create Intercompany IV Invoice 40](#_Toc232847859)

[4.1.4.7 Display AP Accounting Document 41](#_Toc232847860)

[4.1.5 Sales Kits 42](#_Toc232847861)

[4.1.5.1 Create Sales Order 42](#_Toc232847862)

[4.1.5.2 Create Delivery 44](#_Toc232847863)

[4.1.5.3 Perform Picking 45](#_Toc232847864)

[4.1.5.4 Post Goods Issue 46](#_Toc232847865)

[4.1.5.5 Create F2 Invoice 47](#_Toc232847866)

[4.1.5.6 Create Intercompany IV Invoice 48](#_Toc232847867)

[4.1.5.7 Display AP Accounting Document 49](#_Toc232847868)

[4.1.6 Down Payment 50](#_Toc232847869)

[4.1.6.1 Create Sales Orders with Billing Plan 50](#_Toc232847870)

[4.1.6.2 Change Sales Orders (Remove Billing Block) 52](#_Toc232847871)

[4.1.6.3 Create Attachment for Sales Order (Optional) 53](#_Toc232847872)

[4.1.6.4 Create Down Payment Request 54](#_Toc232847873)

[4.1.6.5 Post a Down Payment 55](#_Toc232847874)

[4.1.6.6 Create Delivery 57](#_Toc232847875)

[4.1.6.7 Create Attachment for Delivery (Optional) 58](#_Toc232847876)

[4.1.6.8 Perform Picking 59](#_Toc232847877)

[4.1.6.9 Post Goods Issue 60](#_Toc232847878)

[4.1.6.10 Change Sales Orders (Remove Billing Block) 61](#_Toc232847879)

[4.1.6.11 Create F2 Invoice 63](#_Toc232847880)

[4.1.6.12 Create Attachment for Billing (Optional) 64](#_Toc232847881)

[4.1.6.13 Create Intercompany IV Invoice 65](#_Toc232847882)

[4.1.6.14 Display AP Accounting Document 66](#_Toc232847883)

[4.1.7 Customer Consignment 67](#_Toc232847884)

[4.1.7.1 Consignment Fill-up 67](#_Toc232847885)

[4.1.7.2 Consignment Issue 67](#_Toc232847886)

[4.1.7.2.1 Create Consignment Issue Order 67](#_Toc232847887)

[4.1.7.2.2 Create Delivery 69](#_Toc232847888)

[4.1.7.2.3 Post Goods Issue 69](#_Toc232847889)

[4.1.7.2.4 Check Stock Overview 70](#_Toc232847890)

[4.1.7.2.5 Create Customer (F2) Invoice 71](#_Toc232847891)

[4.1.7.2.6 Create Intercompany Invoice 72](#_Toc232847892)

[4.1.7.2.7 Display AP Journal Entry 73](#_Toc232847893)

[4.1.7.3 Consignment Pick-up 74](#_Toc232847894)

[4.1.7.4 Consignment Return 75](#_Toc232847895)

[4.1.7.4.1 Create Consignment Return Order 75](#_Toc232847896)

[4.1.7.4.2 Create Return Delivery 76](#_Toc232847897)

[4.1.7.4.3 Post Goods Receipt 77](#_Toc232847898)

[4.1.7.4.4 Check Stock Overview 78](#_Toc232847899)

[4.1.7.4.5 Release Consignment Return Order for Billing 79](#_Toc232847900)

[4.1.7.4.6 Create Customer Credit Memo 80](#_Toc232847901)

[4.1.7.4.7 Create Internal Credit Memo 81](#_Toc232847902)

[4.1.7.4.8 Display AP Accounting Document 83](#_Toc232847903)

[4.2 International 84](#_Toc232847904)

[4.2.1 Free of Charge 84](#_Toc232847905)

[4.2.1.1 Create Free of Charge Sales Order 84](#_Toc232847906)

[4.2.1.2 Create Delivery 86](#_Toc232847907)

[4.2.1.3 Perform Picking 87](#_Toc232847908)

[4.2.1.4 Post Goods Issue 88](#_Toc232847909)

[4.2.1.5 Create F2 Invoice 89](#_Toc232847910)

[4.2.1.6 Create Intercompany IV Invoice 90](#_Toc232847911)

[4.2.1.7 Display AP Accounting Document 91](#_Toc232847912)

[4.2.2 Credit Memo 92](#_Toc232847913)

[4.2.2.1 Create Intercompany Credit Memo 92](#_Toc232847914)

[4.2.2.2 Display AP Accounting Document of Intercompany Credit Memo 93](#_Toc232847915)

[4.2.3 Debit Memo 94](#_Toc232847916)

[4.2.3.1 Create Intercompany Debit Memo 94](#_Toc232847917)

[4.2.3.2 Display AP Accounting Document of Intercompany Debit Memo 96](#_Toc232847918)

[4.2.4 Non-Stock Material Sales 97](#_Toc232847919)

[4.2.4.1 Create Sales Orders 97](#_Toc232847920)

[4.2.4.2 Process Sales Order Approval (Optional) 99](#_Toc232847921)

[4.2.4.3 Create Delivery 99](#_Toc232847922)

[4.2.4.4 Post Goods Issue 100](#_Toc232847923)

[4.2.4.5 Create F2 Invoice 101](#_Toc232847924)

[4.2.4.6 Create Intercomapny IV Invoice 102](#_Toc232847925)

[4.2.4.7 Display AP Accounting Document 103](#_Toc232847926)

[4.2.5 Sales Kits 104](#_Toc232847927)

[4.2.5.1 Create Sales Order 104](#_Toc232847928)

[4.2.5.2 Create Delivery 105](#_Toc232847929)

[4.2.5.3 Execute Picking 106](#_Toc232847930)

[4.2.5.4 Post Goods Issue 107](#_Toc232847931)

[4.2.5.5 Create F2 Invoice 108](#_Toc232847932)

[4.2.5.6 Create Intercompany IV Invoice 109](#_Toc232847933)

[4.2.5.7 Display AP Accounting Document 110](#_Toc232847934)

[4.2.6 Down Payment 111](#_Toc232847935)

[4.2.6.1 Create Sales Orders with Billing Plan 111](#_Toc232847936)

[4.2.6.2 Change Sales Orders (Remove Billing Block) 114](#_Toc232847937)

[4.2.6.3 Create Attachment for Sales Order (Optional) 115](#_Toc232847938)

[4.2.6.4 Create Down Payment Request 116](#_Toc232847939)

[4.2.6.5 Post a Down Payment 117](#_Toc232847940)

[4.2.6.6 Create Delivery 119](#_Toc232847941)

[4.2.6.7 Create Attachment for Delivery (Optional) 120](#_Toc232847942)

[4.2.6.8 Perform Picking 121](#_Toc232847943)

[4.2.6.9 Post Goods Issue 122](#_Toc232847944)

[4.2.6.10 Change Sales Orders (Remove Billing Block) 123](#_Toc232847945)

[4.2.6.11 Create F2 Invoice 124](#_Toc232847946)

[4.2.6.12 Create Attachment for Billing (Optional) 125](#_Toc232847947)

[4.2.6.13 Create Intercompany IV Invoice 126](#_Toc232847948)

[4.2.6.14 Display AP Accounting Document 128](#_Toc232847949)

[5 Appendix 129](#_Toc232847950)

[5.1 Limitations 129](#_Toc232847951)

[5.2 Statistical Price on Header for LUMF Use Case 130](#_Toc232847952)

## Purpose

Overview

This scope item provides the intercompany settings for the Credit Memo, Debit Memo, and Free of Charge Delivery scope items.

Free-of-charge delivery is a sales order from one business unit in a group company created and confirmed based on the availability of goods. A delivery from another affiliate business unit is created and the goods are picked and delivered to the end customer. A customer invoice (net value = 0) is generated. The internal invoice based on delivery from the delivering business unit to the selling business unit is handled as a full charged internal pricing.

For credit memo and debit memo, a credit memo or debit memo is created by the delivering business unit and sent to the selling affiliate business unit. The journal entries are posted automatically.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

### Free-of-charge

Free-of-charge delivery is a sales order from one business unit in a group company created and confirmed based on the availability of goods. A delivery from another affiliate business unit is created and the goods are picked and delivered to the end customer. A customer invoice (net value = 0) is generated. The internal invoice based on delivery from the delivering business unit to the selling business unit is handled as a full charged internal pricing.

### Credit Memo and Debit Memo

For credit memo and debit memo, a credit memo or debit memo is created by the delivering business unit and sent to the selling affiliate business unit. The journal entries are posted automatically.

### Sales Kits

Companies often want to sell single products bundled into a sales kit (for example, selling a PC together with monitor, keyboard, computer mouse, and so on). Sales kits are commonly used when the products being part of the sales kits can also be sold independently as single products.

Customers want to have an easy way to use sales kits during order taking and follow up processes without a need to use production BOMs, variant configuration, or other functions that do not fit or are too complex for this use case.

There are two ways to process a bill of material in sales. Once a material executing the BOM explosion is entered into the SO, the system runs pricing and logistic execution at:

● Header level: (Item Categery Determination Group "ERLA") usually used when product is assembled

● Item level: (Item Categery Determination Group "LUMF") usually used when product is not assembled

### Down Payment

In this process, you create requests for down payment, record the receipt of the down payment, and create a final invoice after the deduction of the received down payment and a receipt of the final amount due on the invoice. The process uses the billing plan functionality in sales and distribution. The integrated process allows the maintenance of proper document flow between the sales and financial transactions.

### Customer Consignment

In this scenario, the goods are initially posted to the customer consignment stock and thus remain the property of the delivering company (consignment fill-up).

At regular intervals, the customer reports how many articles are sold and how many articles are in the current stock (inventory). When the inventory is performed, the batch number may be entered to do a correct material posting. A corresponding sales order is entered that documents the issue from the customer consignment, meaning that the goods are no longer the property of the delivering company (consignment issue). Consignment issue with free of charge functionaliy is also supportive for Billing Relvant (100% discount).

Goods that are not required any longer can be returned from the consignment stock to the central warehouse.

The goods must not be defective. They are posted directly into the free stock (consignment pick-up).

In some cases, goods are returned to the customer consignment stock (by its own customer or based on erroneous consumption posting) after the consignment issue has already taken place. A return order is then created (consignment return). Consignment return with free of charge functionaliy is also supportive for Billing Relvant (100% discount).

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
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT |  |
| Accounts Receivable Accountant | SAP_BR_AR_ACCOUNTANT | Accounts Receivable | SAP_BR_AR_ACCOUNTANT |  |
| Returns and Refund Clerk | SAP_BR_RETURNS_REFUND_CLERK | Customer Returns | SAP_BR_RETURNS_REFUND_CLERK |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure:

Domestic

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Material | TG12 | Trad.Good 12,Reorder Point,Reg.Trad. | Material which will be used in order to be provided to the customer |
| Material | NS0002 | Non-Stock Material 02 (No MRP planning)No serial number, no batch |  |
| Material | SDBOMERLAHD | SD BOM Header ERLA (with pricing, inventory management) | Item Category Determination Group "ERLA" |
| Material | SDBOMLUMFHD | SD BOM Header LUMF (No pricing, no inventory) | Item Category Determination Group "LUMF" |
| Customer | 33100002 | Domestic UAE Customer 2 |  |
| Customer | 33100013 | Domestic Customer Invoice List |  |
| Intercompany payer | 33403310 | Customer in company code 3320 AE representing the ordering AE company (company code 3310) |  |
| Supplier | 33403320 | Supplier in company code 3310 AE representing the delivering AE company (company code 3320) |  |
| Sales organization | 3310 | Dom. Sales Org |  |
| Sales organization | 3330 | Dom. Sales Org | Flex.Org App or Set Up Organizational (CBC) extension |
| Distribution channel | 10 | Direct Sales |  |
| Division | 00 | Product Division 00 |  |
| Shipping Point | 333C | Shipping Point 333C | Flex.Org App or Set Up Organizational (CBC) extension |

International

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Material | TG12 | Trad.Good 12,Reorder Point,Reg.Trad. | Material which will be used in order to be provided to the customer |
| Material | NS0002 | Non-Stock Material 02 (No MRP planning)No serial number, no batch |  |
| Material | SDBOMERLAHD | SD BOM Header ERLA (with pricing, inventory management) | Item Category Determination Group ERLA |
| Material | SDBOMLUMFHD | SD BOM Header LUMF (No pricing, no inventory) | Item Category Determination Group LUMF |
| Customer | 33100002 | Domestic UAE Customer 2 |  |
| Distribution channel | 10 | Direct Sales |  |
| Division | 00 | Product Division 00 |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BND | Create Customer Master - MDS |
| BNE | Create Supplier Master - MDS |

Sales Bill of Material Structure

This overview shows the sales bill of material structure.

| Material | Level | Material Type | Quantity | Unit | Description |
| --- | --- | --- | --- | --- | --- |
| SDBOMERLAHD | BOM Header | HAWA | 1 | PC | SD BOM Header ERLA |
| SDBOMERLAIT01 | BOM Item | HAWA | 3 | PC | SD BOM ERLA Item01 |
| SDBOMERLAIT02 | BOM Item | HAWA | 5 | PC | SD BOM ERLA Item02 |

| Material | Level | Material Type | Quantity | Unit | Description |
| --- | --- | --- | --- | --- | --- |
| SDBOMLUMFHD | BOM Header | HAWA | 1 | PC | SD BOM Header LUMF |
| SDBOMLUMFIT01 | BOM Item | HAWA | 3 | PC | SD BOM LUMF Item01 |
| SDBOMLUMFIT02 | BOM Item | HAWA | 5 | PC | SD BOM LUMF Item02 |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/50d91d660c12d10efbc535309712aec7)

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | Open new posting period in company codes 1010 ,1020,1710 and 1720 respectively. |

### Preliminary Steps

#### Create Initial Stock in the domestic shipping plant

Purpose

Create Initial Stock for the domestic shipping plants.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad using the role Inventory Manager. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Stock (F1062). | The Manage Stock screen displays. |  |
| 3 | Input Material | Make the following entries and choose Enter:Material: TG12Plant: Plant 1 <Supply Plant in affiliate company>, for example: 3310 | The Stock overview for the material displays. |  |
| 4 | Select Stock | Select an initial stock to add, for example:Storage Location: <Storage Location in the affiliate supply plant>, for example: 331A | A dialog displays. The Storage Location, Stock Type and Current Quantity are displayed according to the previous step entries. |  |
| 5 | Add Initial Entry | Make the following entry and choose Post:Document Date: <today>Posting Date: <today>Stock Change: Initial EntryQuantity: <enter a number>, for example: 100 | The system displays Material document XXX created. The stock has been added. |  |
| 6 | Post initial stock in plant 1030 | Repeat above steps to post initial stock in plant 3330 for material TG12:Material: TG12Plant: <Supply Plant in affiliate company>, for example: 3330Storage Location: <Storage Location in the affiliate supply plant>, for example: 333ADocument Date: <today>Posting Date: <today>Stock Change: Initial EntryQuantity: <enter a number>, for example: 100 | The system displays Material document XXX created. The stock has been added. |  |
| 7 | Post Initial Stock for Other Materials | Repeat above steps to post initial stock in plant 3310 and 3330 for materials as fllowing:SDBOMERLAHDSDBOMLUMFIT01SDBOMLUMFIT02 |  |  |

Result

The stock quantity is posted and increased.

#### Create Initial Stock in the international shipping plant

Context

Create Initial Stock for the international shipping plants.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad using the role Inventory Manager. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Stock. | The Manage Stock screen displays. |  |
| 3 | Input Material | Make the following entries and choose Enter:Material: TG12Plant: Plant 1 <Supply Plant in affiliate/foreign company> | The Stock overview for the material displays. |  |
| 4 | Select Stock | Select an initial stock to add, for example:Storage Location: <Storage Location in the affiliate/foreign supply plant> | A dialog displays. The Storage Location, Stock Type and Current Quantity are displayed according to the previous step entries. |  |
| 5 | Add Initial Entry | Make the following entry and choose Post:Document Date: <today>Posting Date: <today>Stock Change: Initial EntryQuantity: <enter a number>, for example: 100 | The system displays Material document XXX created. The stock has been added. |  |

Result

The stock quantity is posted and increased.

#### Create Condition Records (Optional)

Purpose

In case you have finetuned the access sequence of SAP pre-shipped condition types, the relative condition records should be created accordingly.

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 2: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BET | Create Sales Pricing Condition - MDS |

#### Process Sales Order Approval (Optional)

Follow the procedure for Process Sales Order Approval steps in the scope item Sell from Stock (BD9).

Purpose

This optional process step shows you how to review the sales orders that might need to be approved.

Procedure

Complete the activities of Process Sales Order Approval step described in the Sell from Stock (BD9) scope item.

#### Check Advanced Down Payment Processing for Item Category CBAO, CTAD, and CTAX

Purpose

Once Advanced Down Payment Processing (ADP) is activated for any of these item categories, you can no longer use that item category for the classical down payment process in new sales orders. Ensure that Advanced Down Payment Processing is disabled for item categories CBAO, CTAD, and CTAX if you want to continue using the classical down payment process.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241).Note If required, choose Set Local Version to set the desired local version. | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution screen is displayed. |  |
| 4 | Open Configuration Activity | Search for the configuration activity Configure Item Categories (ID: 103411).In the All Items table, select the line for Sales Documents.In the Configuration Steps section, choose Configure in the line for Configure Item Categories activity. | The Configure Item Categories: Change screen is displayed. |  |
| 5 | Select Item Category CBAO, CTAD, and CTAX | In the Configure Item Categories table, select the checkbox for item category CBAO, CTAD, and CTAX, and choose Details button. | The Configure Item Categories: Change: Details screen is displayed. |  |
| 6 | Check Advanced Down Payment Processing | In the General Control section, ensure that the checkbox Advanced Down Payment Processing is not selected. | Advanced down payment processing is now inactive for items of item category CBAO, CTAD, and CTAX. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the Activity | Go to the Business Processes Configuration app and search for the following activity: Configure Item Categories.Choose the line item in the search result to see more details about this configuration activity.Choose the Go to Activity button to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Item Categories: Change screen is displayed. |  |
| 3 | Select Item Category CBAO, CTAD, and CTAX | In the Configure Item Categories table, select the checkbox for item category CBAO, CTAD, and CTAX, and choose Details button. | The Configure Item Categories: Change: Details screen is displayed. |  |
| 4 | Check Advanced Down Payment Processing | In the General Control section, ensure that the checkbox Advanced Down Payment Processing is not selected. | Advanced down payment processing is now inactive for items of item category CBAO, CTAD, and CTAX. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| Domestic |  |  |  |
| Free of Charge |  |  |  |
| [Create Free of Charge Sales Order](#unique_19) [page ] 23 | Internal Sales Representative | Manage Sales Orders Without Charge (F2305) | Sales order is created. |
| [Create Delivery](#unique_20) [page ] 24 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) | The Create Outbound Deliveries screen displays. |
| [Perform Picking](#unique_21) [page ] 25 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) |  |
| [Post Goods Issue](#unique_22) [page ] 26 | Shipping Specialist | Manage Outbound Deliveries (F0867A) | The goods issue is posted |
| [Create F2 Invoice](#unique_23) [page ] 27 | Billing Clerk | Create Billing Documents - VF01 (VF01) | Billing with F2 type is created |
| [Create Intercompany IV Invoice](#unique_24) [page ] 28 | Billing Clerk | Create Billing Documents - VF01 (VF01) | Billing with IV type is created |
| [Display AP Accounting Document](#unique_25) [page ] 29 | General Ledger Accountant | Manage Journal Entries (F0717A) | The Manage Journal Entries screen displays. |
| Credit Memo |  |  |  |
| [Create Intercompany Credit Memo](#unique_26) [page ] 30 | Billing Clerk | Create Billing Documents - VF01 (VF01) | You have created an intercompany credit memo. |
| [Display AP Accounting Document of Intercompany Credit Memo](#unique_27) [page ] 32 | General Ledger Accountant | Manage Journal Entries (F0717A) | The Manage Journal Entries screen displays posted AR document. |
| Debit Memo |  |  |  |
| [Create Intercompany Debit Memo](#unique_28) [page ] 33 | Billing Clerk | Create Billing Documents - VF01 (VF01) | You have created an intercompany debit memo. |
| [Display AP Accounting Document of Intercompany Debit Memo](#unique_29) [page ] 34 | General Ledger Accountant | Manage Journal Entries (F0717A) | The Manage Journal Entries screen displays posted AR document. |
| Non-Stock Material Sales |  |  |  |
| [Create Sales Orders](#unique_30) [page ] 36 | Internal Sales Representative | Manage Sales Orders (F1873) | Sales order is created |
| [Process Sales Order Approval (Optional)](#unique_31) [page ] 37 |  |  | Sales order is approved. |
| [Create Delivery](#unique_32) [page ] 37 | Shipping Specialist | Create Outbound Deliveries | Outbound delivery is created |
| [Post Goods Issue](#unique_33) [page ] 38 | Shipping Specialist | Change Outbound Delivery | The goods issue is posted |
| [Create F2 Invoice](#unique_34) [page ] 39 | Billing Clerk | Create Billing Documents - VF01 (VF01) | Billing with F2 type is created |
| [Create Intercompany IV Invoice](#unique_35) [page ] 40 | Billing Clerk | Create Billing Documents - VF01 (VF01) | Billing with IV type is created |
| [Display AP Accounting Document](#unique_36) [page ] 41 | General Ledger Accountant | Manage Journal Entries (F0717A) | The Manage Journal Entries screen displays posted AP document |
| Sales Kits |  |  |  |
| [Create Sales Order](#unique_37) [page ] 42 | Internal Sales Representative | Manage Sales Orders (F1873) | Sales order is created. |
| [Create Delivery](#unique_38) [page ] 44 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) | The Create Outbound Deliveries screen displays. |
| [Perform Picking](#unique_39) [page ] 45 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Material is picked. |
| [Post Goods Issue](#unique_40) [page ] 46 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | The goods issue is posted. |
| [Create F2 Invoice](#unique_41) [page ] 47 | Billing Clerk | Create Billing Documents - VF01 (VF01) | Billing with F2 type is created. |
| [Create Intercompany IV Invoice](#unique_42) [page ] 48 | Billing Clerk | Create Billing Documents - VF01 (VF01) | Billing with IV type is created. |
| [Display AP Accounting Document](#unique_43) [page ] 49 | General Ledger Accountant | Manage Journal Entries (F0717A) | The Manage Journal Entries screen displays. |
| Down Payment |  |  |  |
| [Create Sales Orders with Billing Plan](#unique_44) [page ] 50 | Internal Sales Representative | Manage Sales Orders (F1873) | Order Saved and Order Confirmation sent to printer. |
| [Change Sales Orders (Remove Billing Block)](#unique_45) [page ] 52 | Internal Sales Representative | Manage Sales Orders (F1873) | Sales order is changed to allow for creation of down payment request. |
| [Create Attachment for Sales Order (Optional)](#unique_46) [page ] 53 | Internal Sales Representative | Manage Sales Orders (F1873) |  |
| [Create Down Payment Request](#unique_47) [page ] 54 | Billing Clerk | Create Billing Documents (F0798) | Customer account is debited. A down payment request is generated.. |
| [Post a Down Payment](#unique_48) [page ] 55 | Accounts Receivable Accountant | Post Incoming Payments (F1345) | The down payment is posted. |
| [Create Delivery](#unique_49) [page ] 57 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) | The Create Outbound Deliveries screen displays. |
| [Create Attachment for Delivery (Optional)](#unique_50) [page ] 58 | Shipping Specialist | Display Outbound Delivery (VL03N) | The Display Outbound Delivery: Initial screen displays. |
| [Perform Picking](#unique_51) [page ] 59 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Picking is done. |
| [Post Goods Issue](#unique_52) [page ] 60 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) |  |
| [Change Sales Orders (Remove Billing Block)](#unique_53) [page ] 61 | Internal Sales Representative | Manage Sales Orders (F1873) | The goods issue is posted. |
| [Create F2 Invoice](#unique_54) [page ] 63 | Billing Clerk | Create Billing Documents - VF01 (VF01) |  |
| [Create Attachment for Billing (Optional)](#unique_55) [page ] 64 | Billing Clerk | Manage Billing Documents (F0797) |  |
| [Create Intercompany IV Invoice](#unique_56) [page ] 65 | Billing Clerk | Create Billing Documents - VF01 (VF01) | Billing with IV type is created. |
| [Display AP Accounting Document](#unique_57) [page ] 66 | General Ledger Accountant | Manage Journal Entries (F0717A) | The Manage Journal Entriesscreen displays. |
| [Customer Consignment](#unique_58) [page ] 67 |  |  |  |
| [Consignment Fill-up](#unique_59) [page ] 67 |  |  |  |
| Consignment Issue |  |  |  |
| [Create Consignment Issue Order](#unique_60) [page ] 67 | Internal Sales Representative | Manage Sales Orders (F1873) | The order is saved and its order confirmation is printed out. |
| [Create Delivery](#unique_61) [page ] 69 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) | The creation of a delivery is triggered. |
| [Post Goods Issue](#unique_62) [page ] 69 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | The goods issue is posted. |
| [Check Stock Overview](#unique_63) [page ] 70 | Shipping Specialist | Stock - Multiple Materials (F1595) | The customer consignment stock is displayed. |
| [Create Customer (F2) Invoice](#unique_64) [page ] 71 | Billing Clerk | Create Billing Documents - VF01 (VF01) | The F2 billing document is created. |
| [Create Intercompany Invoice](#unique_65) [page ] 72 | Billing Clerk | Create Billing Documents - VF01 (VF01) | IV billing document is created. |
| [Display AP Journal Entry](#unique_66) [page ] 73 | General Ledger Accountant | Manage Journal Entries (F0717A) | AP accounting document displays. |
| [Consignment Pick-up](#unique_67) [page ] 74 |  |  |  |
| Consignment Return |  |  |  |
| [Create Consignment Return Order](#unique_68) [page ] 75 | Internal Sales Representative | Create Sales Orders - VA01 (VA01) | The customer return order is created. |
| [Create Return Delivery](#unique_69) [page ] 76 | Shipping Specialist | Create Outbound Delivery - With Order Reference (VL01N) | A return delivery is created. |
| [Post Goods Receipt](#unique_70) [page ] 77 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | The goods receipt is posted. |
| [Check Stock Overview](#unique_71) [page ] 78 | Shipping Specialist | Stock - Single Material (F1076) | The delivered quantity has been posted into the consignment stock. |
| [Release Consignment Return Order for Billing](#unique_72) [page ] 79 | Returns and Refund Clerk | Manage Customer Returns (F1708) | The sales order is saved. |
| [Create Customer Credit Memo](#unique_73) [page ] 80 | Billing Clerk | Create Billing Documents (F0798) | Final credit memo is generated. |
| [Create Internal Credit Memo](#unique_74) [page ] 81 | Billing Clerk | Create Billing Documents (F0798) | Internal credit memo is generated. |
| [Display AP Accounting Document](#unique_75) [page ] 83 | General Ledger Accountant | Manage Journal Entries (F0717A) | AP accounting document displays. |
| International (Cross country/region between DE and US) |  |  |  |
| Free of Charge |  |  |  |
| [Create Free of Charge Sales Order](#unique_76) [page ] 84 | Internal Sales Representative | Manage Sales Orders Without Charge (F2305) | Sales order is created. |
| [Create Delivery](#unique_77) [page ] 86 | Shipping Specialist | Create Outbound Deliveries | The Create Outbound Deliveries screen displays. |
| [Perform Picking](#unique_78) [page ] 87 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Material is picked. |
| [Post Goods Issue](#unique_79) [page ] 88 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | The goods issue is posted |
| [Create F2 Invoice](#unique_80) [page ] 89 | Billing Clerk | Create Billing Documents - VF01 (VF01) | Billing with F2 type is created |
| [Create Intercompany IV Invoice](#unique_81) [page ] 90 | Billing Clerk | Create Billing Documents - VF01 (VF01) | Billing with IV type is created |
| [Display AP Accounting Document](#unique_82) [page ] 91 | General Ledger Accountant | Manage Journal Entries (F0717A) | The Manage Journal Entries screen displays. |
| Credit Memo |  |  |  |
| [Create Intercompany Credit Memo](#unique_83) [page ] 92 | Billing Clerk | Create Billing Documents - VF01 (VF01) | You have created an intercompany credit memo. |
| [Display AP Accounting Document of Intercompany Credit Memo](#unique_84) [page ] 93 | General Ledger Accountant | Manage Journal Entries (F0717A) | The Manage Journal Entries screen displays posted AR document. |
| Debit Memo |  |  |  |
| [Create Intercompany Debit Memo](#unique_85) [page ] 94 | Billing Clerk | Create Billing Documents - VF01 (VF01) | You have created an intercompany debit memo. |
| [Display AP Accounting Document of Intercompany Debit Memo](#unique_86) [page ] 96 | General Ledger Accountant | Manage Journal Entries (F0717A) | The Manage Journal Entries screen displays posted AR document. |
| Non-Stock Material Sales |  |  |  |
| [Create Sales Orders](#unique_87) [page ] 97 | Internal Sales Representative | Manage Sales Orders Without Charge (F2305) | Sales order is created. |
| [Process Sales Order Approval (Optional)](#unique_88) [page ] 99 |  |  | Sales order is approved. |
| [Create Delivery](#unique_89) [page ] 99 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) | Outbound delivery is created. |
| [Post Goods Issue](#unique_90) [page ] 100 | Shipping Specialist | Change Outbound Delivery (VL02N) | The goods issue is posted. |
| [Create F2 Invoice](#unique_91) [page ] 101 | Billing Clerk | Create Billing Documents - VF01 (VF01) | Billing with F2 type is created. |
| [Create Intercomapny IV Invoice](#unique_92) [page ] 102 | Billing Clerk | Create Billing Documents - VF01 (VF01) | Billing with IV type is created. |
| [Display AP Accounting Document](#unique_93) [page ] 103 | General Ledger Accountant | Manage Journal Entries (F0717A) | The Manage Journal Entries screen displays posted AP document. |
| Sales Kits |  |  |  |
| [Create Sales Order](#unique_94) [page ] 104 | Internal Sales Representative | Manage Sales Orders (F1873) | Sales order is created. |
| [Create Delivery](#unique_95) [page ] 105 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) | The Create Outbound Deliveries screen displays. |
| [Execute Picking](#unique_96) [page ] 106 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Material is picked. |
| [Post Goods Issue](#unique_97) [page ] 107 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | The goods issue is posted. |
| [Create F2 Invoice](#unique_98) [page ] 108 | Billing Clerk | Create Billing Documents - VF01 (VF01) | Billing with F2 type is created. |
| [Create Intercompany IV Invoice](#unique_99) [page ] 109 | Billing Clerk | Create Billing Documents - VF01 (VF01) | Billing with IV type is created. |
| [Display AP Accounting Document](#unique_100) [page ] 110 | General Ledger Accountant | Manage Journal Entries (F0717A) | The Manage Journal Entries screen displays. |
| Down Payment |  |  |  |
| [Create Sales Orders with Billing Plan](#unique_101) [page ] 111 | Internal Sales Representative | Manage Sales Orders (F1873) | Order Saved and Order Confirmation sent to printer. |
| [Change Sales Orders (Remove Billing Block)](#unique_102) [page ] 114 | Internal Sales Representative | Manage Sales Orders (F1873) | Sales order is changed to allow for creation of down payment request. |
| [Create Attachment for Sales Order (Optional)](#unique_103) [page ] 115 | Internal Sales Representative | Manage Sales Orders (F1873) |  |
| [Create Down Payment Request](#unique_104) [page ] 116 | Billing Clerk | Create Billing Documents (F0798) | Customer account is debited. A down payment request is generated.. |
| [Post a Down Payment](#unique_105) [page ] 117 | Accounts Receivable Accountant | Post Incoming Payments (F1345) | The down payment is posted. |
| [Create Delivery](#unique_106) [page ] 119 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) | The Create Outbound Deliveries screen displays. |
| [Create Attachment for Delivery (Optional)](#unique_107) [page ] 120 | Shipping Specialist | Display Outbound Delivery (VL03N) | The Display Outbound Delivery: Initial screen displays. |
| [Perform Picking](#unique_108) [page ] 121 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Picking is done. |
| [Post Goods Issue](#unique_109) [page ] 122 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) |  |
| [Change Sales Orders (Remove Billing Block)](#unique_110) [page ] 123 | Internal Sales Representative | Manage Sales Orders (F1873) | The goods issue is posted. |
| [Create F2 Invoice](#unique_111) [page ] 124 | Billing Clerk | Create Billing Documents - VF01 (VF01) |  |
| [Create Attachment for Billing (Optional)](#unique_112) [page ] 125 | Billing Clerk | Manage Billing Documents (F0797) |  |
| [Create Intercompany IV Invoice](#unique_113) [page ] 126 | Billing Clerk | Create Billing Documents - VF01 (VF01) | Billing with IV type is created. |
| [Display AP Accounting Document](#unique_114) [page ] 128 | General Ledger Accountant | Manage Journal Entries (F0717A) | The Manage Journal Entriesscreen displays. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Domestic

#### Free of Charge

##### Create Free of Charge Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, sales order is created in ordering company, goods will be directly delivered to the customer from affiliate company/plant.

|  |
| --- |
| Note This is just an example of sample goods delivery. Customer is responsible for how to handle the taxation. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders Without Charge (F2305). | The Manage Sales Orders Without Charge screen displays. |  |
| 3 | Navigate to Create Sales Order Screen | From Manage Sales Orders screen, select the Create Sales Order Without Charge. | The Create Sales Documents screen displays. |  |
| 4 | Enter Sales Document Type | Order Type: CBFD Deliv.Free of ChargeSales Organization: 3310Distribution Channel: 10Division: 00Press Continue. | Create Deliv.Free of Charge: Overview screen displays. |  |
| 5 | Enter Order Details | Sold-to-Party: 33100002Cust. Reference: PO numberOrder Reason : <Order Reason> Free of charge sampleDeliver.Plant: <Delivery Plant> in delivering company code, for example3330Material: Material Number, for example TG12Order Quantity: quantity, for example 1Note You can enter sales kits material here to support sales kit process, go to Sales Kits (4.1.5) chapter to check the details. | Item category CBXN is determined automatically supporting transfer of costs to accounting and creation of proforma invoices. |  |
| 6 | Check intercompany pricing condition type | Choose the line item and select Conditions, check intercompany pricing condition type exists, for example PI02 Intercompany. |  |  |
| 7 | Save | Choose Save. | A Free of Charge sales order is created. Make a note of the sales order document number: |  |

##### Create Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create the delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Outbound Deliveries - From Sales Orders (F0869A). | The Create Outbound Deliveries screen displays. |  |
| 3 | Search Sales Order | Make the following entries and choose Go:Shipping point: 3330 <Shipping point of intercompany delivery plant>Planned Creation Date: <Delivery selection date>Sales Document: Sales order number created previously | The Delivery Creation: Overview screen displays. |  |
| 4 | Create Delivery | Select your sales order items and choose Create Deliveries. | Creation of a delivery is triggered. |  |
| 5 | Check Details | Choose Display Log. | The Analyze Delivery Log screen displays, and delivery is created successfully with delivery number shown on tab Deliveries. |  |

##### Perform Picking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The picking process involves taking goods from a storage location and staging the right quantity in a picking area where the goods are prepared for shipping.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Shipping Specialist. |  |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Open Outbound Delivery Monitor | On the Manage Outbound Deliveries screen, choose For Picking. |  |  |
| 4 | Enter shipping point | On the Outbound Deliveries for Picking screen, make the following entry:Shipping point: 3330 |  |  |
| 5 | Select the Only Picking without WM Checkbox and Choose Execute | Select the Only Picking without WM checkbox and choose Execute. |  |  |
| 6 | Select the Outbound Delivery | On the Day’s Workload for Picking screen, select your outbound delivery and choose Change Outbound Deliveries. |  |  |
| 7 | Input Picked Quantity | On the Delivery xxxxxxxx change: Overview screen, choose tab Picking, input quantity in field Picked Qty.Picking status is set to Completely processed if picked quantity and delivery quantity is equal.Deviations in quantity can be solved by the function Copy Picked Quantity as Delivery Quantity. |  |  |
| 8 | Save Document | Choose Save. |  |  |

##### Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you post the goods issue.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Log onto the SAP Fiori Launchpad using the Role Shipping Specialist. |  |  |
| 2. | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). | The Outbound Delivery Monitor screen displays. |  |
| 3. | Open Outbound Delivery Monitor | Choose For Goods Issue. Make the following entries and choose Execute.Shipping point: 3330 |  |  |
| 4. | Post Good Issue | Mark the relevant delivery and choose Post Goods Issue. Select today’s date from the dialog box. | The goods issue is posted. |  |

##### Create F2 Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity you handle the billing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad using the role Billing Clerk. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents VF01. | The Create Billing Document screen displays. |  |
| 3 | Maintain Billing Date | Choose billing type Invoice (F2) and maintain billing date, for example current date, input delivery number, then press Enter. |  |  |
| 4 | Save | Choose Save. | F2 billing document is created |  |

Financial Postings

| Material | Debit Accounts | Credit Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 44002000 Sales Disc Domestic | 41000000 Rev Domestic Prod | None |

##### Create Intercompany IV Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create the intercompany invoice in delivery company code, in background, AP accounting document is generated in ordering company via IDOC.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad using the role Billing Clerk . | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents - VF01 (VF01)under Billing Document | The Create Billing Document screen displays. |  |
| 3 | Maintain Billing Date | Choose billing type Intercompany Billing (IV) and maintain billing date, for example current date, input delivery number, then press Enter. |  |  |
| 4 | Save | Choose Save. | IV billing document is created, note down billing document number for further use.Note To check the details of the iDoc generated by the intercompany billing document, you can refer to the section Message Monitor of the Setup Instructions document [Intercompany Sales Order Processing Setup (1HO 1MX 1WO) (SAP Customer)](https://support.sap.com/content/dam/SAAP/SAP_Activate/S4H_489%20Intercompany%20Sales%20Order%20Processing%20%20Setup%20(1HO%201MX%201WO).docx). |  |

Financial Postings

| Material | Debit Accounts | Credit Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 33403310 Company Code 3310 as Business | 41001500 Rev Affiliate- Prod22000000 Output tax (MWS) | None |

##### Display AP Accounting Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity you display account payable accounting documents generated by IV invoice IDoc.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad using the role General Ledger Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Journal Entries (F0717A) . | The Manage Journal Entries screen displays.Note If app Manage Journal Entries (F0717A) is not there on the Home Page, please search and find it using the magnifier icon. |  |
| 3 | Add Original Reference Document Field as Filter | Choose Adapt Filters, select Original Reference Document option, and choose OK. | The Original Reference Document field is added as a filter. |  |
| 4 | Filter AP Accounting Document by Referencing IV Invoice | Make the following entry:Original Reference Document: <00 + Intercompany invoice number generated in previous step>Choose Go. | AP accounting document number displays. |  |
| 5 | Display AP Accounting Document | Choose AP accounting number in the Journal Entry column.Choose Display Journal Entries - New Version. | AP accounting document displays. |  |

#### Credit Memo

##### Create Intercompany Credit Memo

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you hw to generate a credit memo by referring the intercompany IV billing document. It also supports the IV billing created in free of charge, sales kits and down payment processes.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad using the role Billing Clerk. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents - VF01. | The Create Billing Documents screen displays. |  |
| 3 | Define Billing Setting | Choose billing type CICM from dropdown list.Search for intercompany invoice number in document field.Maintain Entries on Billing Documents tab:Billing Type: IVSold to party: 33403310Sales Organization: 3330ClickFind.Select billing document from the list.Choose Execute. | List with lines for intercompany invoice display and intercompany credit memo editing is displayed. |  |
| 4 | Modify intercompany Credit memo | Double click line with billing type Intercompany Credit MemoNavigate to item conditionsChange item conditions, for example PIC2 | Net value of the document has been changed. |  |
| 5 | Save Intercompany Credit Memo | Choose Save. | Billing document generated, not released to accounting. |  |
| 6 | Display Billing Document after Creation | The billing document displays automatically. Make a note of the billing document number: __________. |  |  |

Financial Postings

| Material | Debit Accounts | Credit Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 41001500 Rev Affiliate- Prod22000000 Output tax (MWS) | 33403310 Company Code 3310 as Business | None |

##### Display AP Accounting Document of Intercompany Credit Memo

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you display account payable accounting documents generated by Intercompany Credit Memo IDoc.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad using the role General Ledger Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Journal Entries (F0717A). | The Manage Journal Entries screen displays.Note If app Manage Journal Entries (F0717A) is not there on the Home Page, please search and find it using the magnifier icon. |  |
| 3 | Add Original Reference Document Field as Filter | Choose Adapt Filters, select Original Reference Document option, and choose OK. | The Original Reference Document field is added as a filter. |  |
| 4 | Filter AP Accounting Document by Referencing Intercompany Credit Memo | Make the following entry:Original Reference Document: <00 + intercompany credit memo number generated in previous step>Choose Go. | AP accounting document number displays. |  |
| 5 | Display AP Accounting Document | Choose AP accounting number in the Journal Entry column.Choose Display Journal Entries - New Version. | AP accounting document displays. |  |

#### Debit Memo

##### Create Intercompany Debit Memo

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to generate a debit memo by referring the intercompany IV billing document. It also supports the IV billing created in free of charge, sales kits and down payment processes.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad using the role Billing Clerk. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents - VF01. | The Create Billing Documents screen displays. |  |
| 3 | Define Billing Setting | Choose billing type CIDM from dropdown list.Search for intercompany invoice number in document field.Maintain Entries on Billing Documents tab:Billing Type: IVSold to party: 33403310Sales Organization: 3330Click Find.Select billing document from the list.Choose Execute. | List with lines for intercompany invoice display and intercompany debit memo editing is displayed. |  |
| 4 | Modify intercompany Debit memo | Double click line with billing type Intercompany Debit MemoNavigate to item conditionsChange item conditions, for example PIC2 | Net value of the document has been changed. |  |
| 5 | Save intercompany Debit Memo | Choose Save. | Billing document generated, not released to accounting. |  |
| 6 | Display Billing Document after Creation | The billing document displays automatically. Make a note of the billing document number: __________. |  |  |

Financial Postings

| Material | Debit Accounts | Credit Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 33403310 Company Code 3310 as Business | 41001500 Rev Affiliate- Prod22000000 Output tax (MWS) | None |

##### Display AP Accounting Document of Intercompany Debit Memo

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display account payable accounting documents generated by Intercompany Debit Memo IDoc.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad using the role General Ledger Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Journal Entries (F0717A). | The Manage Journal Entries screen displays.Note If app Manage Journal Entries (F0717A) is not there on the Home Page, please search and find it using the magnifier icon. |  |
| 3 | Add Original Reference Document Field as Filter | Choose Adapt Filters, select Original Reference Document option, and choose OK. | The Original Reference Document field is added as a filter. |  |
| 4 | Filter AP Accounting Document by Referencing Intercompany Debit Memo | Make the following entry:Original Reference Document: <00 + intercompany debit memo number generated in previous step>Choose Go. | AP accounting document number displays. |  |
| 5 | Display AP Accounting Document | Choose AP accounting number in the Journal Entry column.Choose Display Journal Entries - New Version. | AP accounting document displays. |  |

#### Non-Stock Material Sales

##### Create Sales Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create sales order in ordering company, goods will be directly delivered to the customer from affiliate company/plant.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Internal Sales Representative. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Navigate to Create Sales Order Screen | Choose Create > Create Sales Order - VA01 . | The Create Sales Documents screen displays. |  |
| 4 | Enter Sales Document Type | Make the following entries and choose Continue.Order Type: OR Standard OrderSales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 5 | Enter Order Details | Make the following entries:Sold-to-Party: 33100002Ship-toParty: 33100002Cust. Reference: PO numberDeliver.Plant: Delivery Plant in delivering company code for example, 3330Material: Material Number, for example NS0002Order Quantity: <quantity>, for example 10 |  |  |
| 6 | Check Intercompany Pricing Condition Type | Select the line item and choose the Item Conditions icon. Check intercompany pricing condition type exists, for example PI02 Inter-company % |  |  |
| 7 | Save | Choose Save. | A sales order is created. Make a note of the sales order document number:___________ |  |

##### Process Sales Order Approval (Optional)

Follow the procedure for Process Sales Order Approval steps in the scope item Sell from Stock (BD9).

Purpose

This process step shows you how to review the sales orders that might need to be approved.

Procedure

Complete the activities of Process Sales Order Approval step described in the scope item Sell from Stock (BD9).

##### Create Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, sales order is created in ordering company, goods will be directly delivered to the customer from affiliate company/plant.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Create Outbound Deliveries - From Sales Orders (F0869A). | The Create Outbound Deliveries screen displays. |  |
| 3 | Search Sales Order | Make the following entries and choose Go:Shipping point: 3330 Shipping point of intercompany delivery plantPlanned Creation Date: Delivery selection dateSales Document: Sales order number created previously | The Delivery Creation: Overview screen displays. |  |
| 4 | Create Delivery | Select your sales order items and choose Create Deliveries. | Creation of a delivery is triggered. |  |
| 5 | Check Details | Choose Display Log | The Analyze Delivery Log screen displays; delivery is created successfully with delivery number shown on tab Deliveries. |  |

##### Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you post goods issue.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad using the role Shipping Specialist. |  |  |
| 2 | Access the App | Open Change Outbound Delivery. | The Change Outbound Delivery screen displays. |  |
| 3 | Change Outbound Delivery | Make the following entries and choose Continue.Outbound Delivery: <delivery number created previously> | The Delivery XXX Change: Overview screen displays. |  |
| 4 | Post Goods Issue | Choose the Post Goods Issue. | The goods issue is posted. |  |

##### Create F2 Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to handle the billing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Billing Clerk. |  |  |
| 2 | Access the App | Open Create Billing Documents VF01 under Billing Document. | The Create Billing Document screen displays. |  |
| 3 | Maintain Billing Date | Choose billing type Invoice(F2) and maintain billing date, for example current date, input delivery number, then choose Enter. |  |  |
| 4 | Save | Choose Save. | F2 billing document is created. |  |

Financial Postings

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Non-Stock Material (NLAG) | 33100002 Rcvbls Domestic AE 2 | 41000000 Rev Domestic Prod22000000 Output tax (MWS) | none |

##### Create Intercompany IV Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create the intercompany invoice in delivery company code, in background, AP accounting document is generated in ordering company via IDOC.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Billing Clerk. |  |  |
| 2 | Access the App | Open Create Billing Documents VF01 under Billing Document. | The Create Billing Document screen displays. |  |
| 3 | Maintain Billing Date | Choose billing type Intercompany Billing (IV) and maintain billing date, for example current date, input delivery number, then choose Enter. |  |  |
| 4 | Save | Choose Save. | IV billing document is created, note down billing document number for further use. |  |

Financial Postings

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Non-Stock Material (NLAG) | 33403310 Company Code 3310 as Business | 41001500 Rev Domestic Prod22000000 Output tax (MWS) | none |

##### Display AP Accounting Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display account payable accounting documents generated by IV invoice IDoc.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad using the role General Ledger Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Journal Entries (F0717A). | The Manage Journal Entries screen displays.Note If app Manage Journal Entries (F0717A) is not displayed on the Home Page, please search and find it using the magnifier icon. |  |
| 3 | Add Original Reference Document Filed as Filter | Choose Adapt Filters, select Original Reference Document option, and choose OK. | The Original Reference Document field is added as a filter. |  |
| 4 | Filter AP Accounting Document by Referencing IV Invoice | Make the following entry:Original Reference Document: <00 + Intercompany invoice number generated in previous step>Choose Go. | AP accounting document number displays. |  |
| 5 | Display AP Accounting Document | Choose AP accounting number in the Journal Entry column.Choose Display Journal Entries - New Version. | AP accounting document displays. |  |

#### Sales Kits

##### Create Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a sales order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Navigate to Create Sales Order Screen | On the Manage Sales Orders screen, choose Create > Create Sales Order VA01 . | The Create Sales Documents screen displays. |  |
| 4 | Enter the Order Data | Make the following entries and choose Continue:Order Type:ORSales Organization: 3310Distribution Channel: 10Division: 00Choose the Order Type OR manually if the item is free of charge during order creation. |  |  |
| 5 | Enter Order Details | On the Create Sales Orders: Overview screen, make the following entries:Sold-to Party: 33100002PO Number: <PO number>Material Number: <SDBOMERLAHD> or <SDBOMLUMFHD>Deliver.Plant: <Deliver.Plant>, in delivering company code, for example, 3330Quantity: <Quantity>, for example, 1If you are using SDBOMERLAHD or SDBOMLUMFHD in testing, the sales BOM will explode and subitems will appear. Here is the difference between them:For SDBOMERLAHD, pricing and inventory managed on the main item.For SDBOMLUMFHD, pricing and inventory managed on the subitems. |  |  |
| 6 | Check Intercompany Pricing Condition Type | Select the line item and choose the Item Conditions icon. Check intercompany pricing condition type exists, for example, PI02 Intercompany. |  |  |
| 7 | Save Document | Choose Save. Make a note of the sales order number: __________. | The order is saved and its order confirmation is printed out. |  |

##### Create Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create the delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Create Outbound Deliveries - From Sales Orders (F0869A). | The Create Outbound Deliveries-From Sales Orders screen displays. |  |
| 3 | Search for Sales Order | Make the following entries and choose Go:Shipping Point: 3330Planned Creation Date: <Delivery selection date>Sales Document: <Sales Order Number Created Previously> |  |  |
| 4 | Create Delivery | Select your sales order, and choose Create Deliveries. | A delivery creation is triggered |  |
| 5 | Check Details | Choose Display Log. | The Analyze Delivery Log screen displays.A delivery is created successfully with delivery number shown on tab Deliveries. |  |

|  |
| --- |
| Note With the Analyze Outbound Delivery Logs app, you can display an overview about the logs of all the deliveries, which have been created in your system. You can filter by example created by and Additional settings. If you select the arrow on the right of each delivery log entry you can see its message type, text, and also related sales document. |

##### Perform Picking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The picking process involves taking goods from a storage location and staging the right quantity in a picking area where the goods are prepared for shipping. This process step shows you how to execute picking.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad screen displays. |  |
| 2. | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3. | Choose Picking | Choose For Picking. |  |  |
| 4. | Enter Shipping Point | Make the following entries and choose Execute.Shipping point: 3330Only Picking without WM: X |  |  |
| 5. | Change Outbound Delivery | From Day’s Workload for Picking, select your delivery number and choose Change Outbound Deliveries. |  |  |
| 6. | Check Batch Split | Navigate to the Picking tab, check if batch split exists in Batch Split Indicator column: |  |  |
| 7. | Enter Picked Quantity | If batch split exists, choose Batch Split Exists to expand sub item(s), enter quantity equal to delivery qty in Picked Qty field for subitem.If batch split doesn't exist, enter quantity equal to delivery qty in Picked Qty field for picking related item(s).For SDBOMERLAHD, enter picked quantity on the main item.For SDBOMLUMFHD, enter picked quantity on the subitems. |  |  |
| 8. | Enter | Choose Enter. |  |  |
| 9. | Save | Choose Save. | The delivery have been picked. |  |

##### Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post a goods issue.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). | The Outbound Delivery Monitor screen displays. |  |
| 3 | Open Outbound Delivery Monitor | Choose For Goods Issue.Shipping Point: 3330 |  |  |
| 4 | Post Good Issue | Mark the relevant delivery and choose Post Goods Issue. Select today’s date from the dialog box. Choose Post Goods Issue. | The goods issue is posted. |  |

##### Create F2 Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to handle the billing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents - VF01 (VF01). | The Create Billing Document screen displays. |  |
| 3 | Maintain Billing Date | Choose billing type Invoice(F2) and maintain billing date, for example, <current date>, enter Delivery Number, then choose Enter. |  |  |
| 4 | Save | Choose Save. | F2 billing document is created. |  |

Financial Postings

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 44002000 Sales Disc Domestic | 41000000 Rev Domestic Prod | None |

##### Create Intercompany IV Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create the intercompany invoice in delivery company code, in background, AP accounting document is generated in ordering company via IDOC.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents - VF01 (VF01). | The Create Billing Document screen displays. |  |
| 3 | Maintain Billing Date | Choose billing type Invoice (IV) and maintain billing date, for example,<current date>, enter Delivery Number, then choose Enter. |  |  |
| 4 | Save | Choose Save. | IV billing document is created, note down billing document number for further use.Note To check the details of the iDoc generated by the intercompany billing document, you can refer to the section Message Monitor of the Setup Instructions document [Intercompany Sales Order Processing Setup (1HO 1MX 1WO) (SAP Customer)](https://support.sap.com/content/dam/SAAP/SAP_Activate/S4H_489%20Intercompany%20Sales%20Order%20Processing%20%20Setup%20(1HO%201MX%201WO).docx). |  |

Financial Postings

| Material | Debit Accounts | Credit Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 33403310 Company Code 3310 as Business | 41001500 Rev Affiliate- Prod22000000 Output tax (MWS) | None |

##### Display AP Accounting Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This processs tep shows you how to display account payable accounting documents generated by IV invoice IDoc.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Journal Entries (F0717A). | The Manage Journal Entries screen displays.Note If app Manage Journal Entries (F0717A) is not there on the Home Page, please search and find it using the magnifier icon. |  |
| 3 | Add the Original Reference Document Field as Filter | Choose Adapt Filters, select Original Reference Document option, and choose OK. | The Original Reference Document field is added as a filter. |  |
| 4 | Filter AP Accounting Document by Referencing IV Invoice | Make the following entry:Original Reference Document: <00 + Intercompany invoice number generated in previous step>Choose Go. | AP accounting document number displays. |  |
| 5 | Display AP Accounting Document | Choose AP accounting number in the Journal Entry column.Choose Display Journal Entries - New Version. | AP accounting document displays. |  |

#### Down Payment

##### Create Sales Orders with Billing Plan

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to require a down payment from the customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Navigate to Create Sales Order Screen | Choose Create > Create Sales Order - VA01 . | The Create Sales Documents: Initial screen displays. |  |
| 4 | Enter Sales Document Type | Make the following entries and choose Continue:Order Type: <sales order type> , for example, OR (Standard Order)Sales Organization: 3310Distribution Channel: 10Division: 00 | The Create Standard Order xxx: Overview screen displays. |  |
| 5 | Enter Customer Number | Make the following entries:Sold-to Party: 33100002Customer Reference: <Customer reference>, for example,<customer purchase Order number>Press Enter. |  |  |
| 6 | Enter Order Details | Make the following entries:Deliver.Plant: <Delivery plant> in delivering company code, for example, 3330Material: <Material number>, for example, TG12Order Quantity: <quantity>, for example, 10Item Category:CBAO Milestone-Bill.Plan for Trading goods. |  |  |
| 7 | Choose Billing Plan | Select the item. Choose Menu > Goto > Item > Billing plan .Note Alternatively, you can assign billing plan on header level: Choose Menu > Goto > Header > Billing Plan . The header billing plan will be applied to all items with item category CBAO. Amount is proportionally to the value of the items participating in the down payment process distributed to the items. |  |  |
| 8 | Enter Details | For the first line item (Down Payment), make the following entries for the advance payment:Billing Date: <Billing date>, for example, enter today's date.Bill Value: <Amount of billing>, for example: Down payment amountDate category (DCat): 04 |  |  |
| 9 | Enter Details | For the second line item (Closing Invoice), make the following entries for the advance payment:Billing Date: <Billing date>. For example, enter today's date.Date category (DCat): 02 |  |  |
| 10 | Enter | Press Enter. Confirm system messages with enter if necessary. | Closing invoice related data is determined. For example, in Bill value field, the amount of billing is calculated by the system. |  |
| 11 | Back | Choose Back. |  |  |
| 12 | Save | Choose Save. |  |  |

##### Change Sales Orders (Remove Billing Block)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to remove billing block from a sales order.

Prerequisite

The billing block must be manually removed for the first down payment request to be processed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Change Sales Documents: Initial screen displays. |  |
| 3 | Search For Sales Order | Make the following entries and choose Enter:Order number: Order number from the previous process step. | The Change Standard Order xxx: Overview screen displays. |  |
| 4 | Navigate to Sales Order Screen | Select the sales order number and choose Change Sales Orders - VA02 (VA02). | The Change Sales Order xxx: Overview screen displays. |  |
| 5 | Choose Billing Plan | Select the line item.From the menu, choose More > Goto > Item > Billing plan .Alternatively, If you assign billing plan on header level: choose More > Goto > Header > Billing plan . Removal of billing block on header level also unlocks items automatically. | The Change Standard Order xxx: Item Data screen displays. |  |
| 6 | Delete Billing Block | In the Dates section, in the Block column delete the billing block for the Down payment item (keep the billing block for the Closing invoice item). |  |  |
| 7 | Back | Choose Back. |  |  |
| 8 | Save | Save your entries. | The billing block is removed. |  |

##### Create Attachment for Sales Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create attachment for a sales order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Navigate to Display Sales Order Screen | On the Manage Sales Orders screen, enter the respective order number created in previous step in the Sales Order and choose Go.Click the sales order number and choose Change Sales Order - VA02. |  |  |
| 4 | Create Attachment for Sales Order | Choose Services for Object on the top right corner of screen, choose Create Attachment. | The Import File screen displays. |  |
| 5 | Import File | Choose OK in the File Upload dialog box.In the Open view, choose local path and file, and choose Open. | The attachment was successfully created. |  |
| 6 | Check Attachment | Choose Services for Object on top right corner of screen, choose Attachment List. | Attachment brings up on the Service: Attachment list screen. |  |

##### Create Down Payment Request

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
| 3 | Define Billing Setting | Choose Billing Setting in bottom bar. There are five settings, make all of these settings to ON:Enter Billing Data before billingSeparate Billing Documents for Each Billing Due List ItemAutomatically Post Billing DocumentsDisplay Billing Document After CreationChoose delivery items to be billed and select quantities |  |  |
| 4 | Search for Billing List | In the search condition, enter criteria if necessary. | SD document(s) displays in the result. |  |
| 5 | Choose Sales Document | More than one SD document item appear in Billing Due List Items table, select the row relevant to down payment request, and choose Create Billing Documents. | The Create Billing Documents screen displays. |  |
| 6 | Maintain Billing Type and Billing Date | Choose billing type Down payment request (FAZ) and maintain billing date, for example current date, then choose Create. | The draft billing document is created. |  |
| 7 | Save Billing Document | On the Billing Document screen, choose Save.The draft billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx.Make a note of the billing document number: __________. | Billing document is generated. |  |

Financial Postings

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 21191000 Down payment requests (customers) | none | none |

##### Post a Down Payment

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Accounts Receivable Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Incoming Payments (F1345). | The Post Incoming Payments (F1345) screen displays. |  |
| 3 | Enter Details | Make the following entries and choose Propose Items:General Information area:Company Code: 3310Posting Date: Current dateJournal Entry Date: <Current date>Value Date: Current datePeriod: Current periodJournal Entry Type: DZ (Customer Payment)Bank Data area:G/L Account (Company Code CoA): 11001060House Bank: DEBK1Bank Account: DEAC1Amount: Down Payment Amount / AEDNote Enter the amount of the journal entry the customer has been debited with in the previous step(billing value plus value added tax)Open Item Selection area:Account Type/Account ID: Customer / 33100002 |  |  |
| 4 | Search for Down Payment Request | Choose Select More.In Line Item Type field, select checkbox in Special G/L Transactions and deselect other values from drop-down menu, then choose OK. | Select More dialog box displays.All down payment request documents which meet the conditions are listed in Open Items table. |  |
| 5 | Select Down Payment Request | Choose Clear in the down payment request document entry in Open Items table. | The item is copied to Items to Be Cleared table. |  |
| 6 | Post | Choose Post. | Success dialog box pop ups, the information Journal entry 14XXXXXXXX successfully posted displays. |  |
| 7 | Display Journal Entry | Choose Display. | The Manage Journal Entries screen displays. Detailed information involved in down payment journal entry is shown. |  |

Financial Postings

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 11001060 Bank Account21191500 Tax sett.dwn pmt cus | 21190000 Down Payments - Customers22000000 Output tax (MWS) | none |

##### Create Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a delivery.

Prerequisite

The goods receipt was posted to the individual customer’s stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Create Outbound Deliveries - From Sales Orders (F0869A). | The Create Outbound Deliveries - From Sales Orders (F0869A) screen displays. |  |
| 3 | Search Sales Order | Make the following entries and choose Go:Shipping Point: <shipping point of intercompany delivery plant> for example, 3330Planned Creation Date: <Delivery selection date>Order: <Sales order number created previously> |  |  |
| 4 | Create Delivery | Select your sales order and choose Create Deliveries. | A delivery is triggered to create. |  |
| 5 | Check Details | Choose Display Log. | The Analyze Delivery Log screen displays, delivery is created successfully with delivery number shown on tab Deliveries. |  |

|  |
| --- |
| Note With the Analyze Outbound Delivery Logs app you can display an overview about the logs of all delivery creation in system. You can search for logs according to different filter criteria, for example: created by and additional settings. Detailed log information is listed via selecting the arrow on the right of each delivery log entry:If delivery is created successfully, delivery number is shown on Deliveries tab, or, you can display the exact message type, text and also the related sales document on Messages tab . |

##### Create Attachment for Delivery (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create attachment for delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Outbound Delivery (VL03N). | The Display Outbound Delivery: Initial screen displays. |  |
| 3 | Enter Outbound Delivery Number | In the Outbound Delivery field, enter <the outbound delivery number created in previous step> and choose Continue. | The Display Outbound Delivery xxx: Overview screen displays. |  |
| 4 | Create Delivery Attachment | Choose Display < - > Change.Choose Services for Object on the top right corner of screen, and choose Create Attachment. | The Import File screen displays. |  |
| 5 | Import File | Choose OK in the File Upload dialog box.In the Open view, choose local path and file, and choose Open. | The attachment was successfully created. |  |
| 6 | Check Attachment | Choose Services for Object on the top right corner of screen, then choose Attachment List. | Attachment shows up on Service: Attachment List screen. |  |

##### Perform Picking

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
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Open Outbound Delivery Monitor | On the Manage Outbound Deliveries screen, choose For Picking. |  |  |
| 4 | Enter Shipping Point | On the Outbound Deliveries for Picking screen, make the following entries:Shipping Point: 3330 |  |  |
| 5 | Execute | Select the Only Picking without WM checkbox and choose Execute. |  |  |
| 6 | Select the Outbound Delivery | On the Day’s Workload for Picking screen, select your outbound delivery and choose Change Outbound Deliveries. |  |  |
| 7 | Enter Picked Quantity | On the Delivery xxxxxxxx Change: Overview screen, choose Picking tab , enter quantity in Picked Qty field.Picking status is set to Completely processed if picked quantity and delivery quantity is equal.Deviations in quantity can be solved by the Copy Picked Quantity as Delivery Quantity function. |  |  |
| 8 | Save Document | Choose Save. |  |  |

##### Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post a goods issue.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). | The Outbound Delivery Monitor screen displays. |  |
| 3 | Open Outbound Delivery Monitor | Choose For Goods Issue.Shipping Point: 3330 |  |  |
| 4 | Post Good Issue | Mark the relevant delivery and choose Post Goods Issue. Select today’s date from the dialog box. Choose Post Goods Issue. | The goods issue is posted |  |

Financial Posting

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 54083000Inv Chg COGS w/CE | 13600000Inventory TradingGd | none |

##### Change Sales Orders (Remove Billing Block)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to remove a billing block from a sales order.

Prerequisite

COGS has been recognized. To recognize revenue in the same month to keep FI and PA in synch, the billing block must be removed manually to process the final invoice.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Search For Sales Order | Enter search term(s) in filter bar, and choose Go:Sales Order: <Sales Order Number> |  |  |
| 4 | Navigate to Sales Order Screen | Select sales order number and choose Changes Sales Orders. | Sales order is displayed in result list. |  |
| 5 | Choose Billing Plan | Select the line item. From the menu, choose More > Goto > Item > Billing Plan.Alternatively, If you assign billing plan on header level: choose More > Goto > Item > Billing Plan . Removal of billing block on header level also unlocks items automatically. | The Change Standard Order xxx: Item Data screen displays. |  |
| 6 | Delete Billing Block | In the Dates section, in the Block column, delete the billing block for the Closing Invoice item. |  |  |
| 7 | Back | Choose Back. |  |  |
| 8 | Save | Save your entries. | The billing block is removed. |  |

##### Create F2 Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to handle the billing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents - VF01 (VF01). | The Create Billing Document screen displays. |  |
| 3 | Maintain Billing Date | Choose billing type Invoice(F2) and maintain billing date, for example, <current date>, enter Sales Order Number, then choose Enter. |  |  |
| 4 | Save | Choose Save. | F2 billing document is created. |  |

Financial Postings

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 12100000 Rcvbls Domestic21190000 Down Payments - Customers22000000 Output tax (MWS) | 41000000 Rev Domestic Prod12100000 Rcvbls Domestic21191500 Tax sett.dwn pmt cus22000000 Output tax (MWS) | None |

##### Create Attachment for Billing (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create an attachment for a billing document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Billing Documents (F0797). | The Manage Billing Document screen displays. |  |
| 3 | Search Billing | Make the following entry, and choose Enter:Billing Document: <Billing Document Number Created Previously> |  |  |
| 4 | Choose Billing Number | On the Manage Billing Documents screen, select your billing document created in the previous step, and choose Display. | The Billing Document screen displays. |  |
| 5 | Edit | On the Billing Documents screen, choose Edit. |  |  |
| 6 | Create Billing Attachment | Scroll down and choose Upload in the ATTACHMENTS section. | The Open File screen displays. |  |
| 7 | Import File | In the Open window, select a local path or file and choose Open.Choose Save. | The attachment is successfully created. |  |
| 8 | Check Attachment | In the ATTACHMENTS section, you can see the uploaded document. Choose the document you want to open. |  |  |

##### Create Intercompany IV Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create the intercompany invoice in delivery company code, in background, AP accounting document is generated in ordering company via IDOC.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents - VF01 (VF01). | The Create Billing Document screen displays. |  |
| 3 | Maintain Billing Date | Choose billing type Intercompany Billing (IV) and maintain billing date, for example, <current date>, enter Delivery Number, then choose Enter. |  |  |
| 4 | Save | Choose Save. | IV billing document is created, note down billing document number for further use.Note To check the details of the iDoc generated by the intercompany billing document, you can refer to the section Message Monitor of the Setup Instructions document [Intercompany Sales Order Processing Setup (1HO 1MX 1WO) (SAP Customer)](https://support.sap.com/content/dam/SAAP/SAP_Activate/S4H_489%20Intercompany%20Sales%20Order%20Processing%20%20Setup%20(1HO%201MX%201WO).docx). |  |

Financial Postings

| Material | Debit Accounts | Credit Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 12300000 Company Code 3310 as Business | 41001500 Rev Affiliate- Prod22000000 Output tax (MWS) | None |

##### Display AP Accounting Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display account payable accounting documents generated by IV invoice IDoc.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Journal Entries (F0717A). | The Manage Journal Entries screen displays.Note If app Manage Journal Entries (F0717A) is not there on the Home Page, please search and find it using the magnifier icon. |  |
| 3 | Add the Original Reference Document Field as Filter | Choose Adapt Filters, select Original Reference Document option, and choose OK. | The Original Reference Document field is added as a filter. |  |
| 4 | Filter AP Accounting Document by Referencing IV Invoice | Make the following entry:Original Reference Document: <00 + Intercompany invoice number generated in previous step>Choose Go. | AP accounting document number displays. |  |
| 5 | Display AP Accounting Document | Choose AP accounting number in the Journal Entry column.Choose Display Journal Entries - New Version. | AP accounting document displays. |  |

#### Customer Consignment

Currently, customer and vendor consignment processes and consignment stocks with a border crossing are not supported. Only domestic consignment processes are supported.

##### Consignment Fill-up

The consignment fill-up process is the same as the scope item Customer Consignment (1IU). For details, refer to the test script of the scope item 1IU to perform the sub-process of consignment fill-up. You can find the test script of 1IU on SAP Signavio Process Navigator.

|  |
| --- |
| Note The delivery plant code on sales order item should be entered with a plant which belongs to a different company code, for example, 3330. |

##### Consignment Issue

###### Create Consignment Issue Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

At regular intervals, the customer reports either how many products have been sold, or consumed, or how many products are in the current stock (inventory).

A corresponding order is entered, documenting the issue from the consignment stock.

A billing document is created for the issue from the external stock at the customer site.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). |  |  |
| 3 | Create Sales Order | On the Manage Sales Orders screen, choose Add and then choose Create Sales Order to Create Sales Order- VA01. |  |  |
| 4 | Enter Order Type | On the Create Sales Document screen, make the following entries and choose Continue (Enter):Order Type: CCISSales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 5 | Enter Material Data | On the Create Consignment Issue: Overview Create Consignment Issue BR: Overview screen, make the following entries:Sold-to Party: 33100003Ship-to Party: 33100003Cust. Reference: <the customer purchase order number>On the Items tab, make the following entries:Material: <all material numbers mentioned in master data section>Delivery Plant: <Deliver.Plant>, 3330Order Quantity: <the required quantity>, for example, 10PC | Item Category:You can choose correct item category to fit your business caseCIN: Consig IssueCCXN (Manual input): Consig Issue FOC Enh (Consignment Issue with Free of Charge 100% discount).Please take a note, the following item catego-ry is not applicable for intercompany business.CCIN (Manual input): Consig Issue FOC Enh (Consignment Issue with Free of Charge Not Billing Relevant). |  |
| 6 | Check Intercompany Pricing Condition Type | Choose the line item and select Conditions, check intercompany pricing condition type exists, for example, PI02 Intercompany. |  |  |
| 7 | Save Document | Choose Save.Make a note of the sales order number__________. | The order is saved and its order confirmation is printed out. |  |

###### Create Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create the delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Outbound Deliveries - From Sales Orders (F0869A). | The Create Outbound Delivery screen displays. |  |
| 3 | Search Sales Order | Make the following entries and choose Go:Shipping Point: 333CPlanned Creation Date: <the delivery selection date>Sales Document: <the sales order number created previousl> |  |  |
| 4 | Create Delivery | Select your sales order items and choose Create Deliveries. | The creation of a delivery is triggered. |  |

###### Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you post the goods issue.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). | The Outbound Delivery Monitor screen displays. |  |
| 3 | Open Outbound Delivery Monitor | Choose For Goods Issue. Make the following entry and choose Execute:Shipping Point: 333C |  |  |
| 4 | Post Goods Issue | Select the relevant delivery and choose Post Goods Issue. In the dialog box, choose today’s date and choose Continue. | The goods issue is posted. |  |

Financial Postings

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 51600000Consptn Trde Gds | 13600000Inventory TradingGd | none |

###### Check Stock Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The goods are transferred from the customer's consignment stock and are no longer owned by the company. The stock overview reflects this transfer of products.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Stock - Multiple Materials (F1595). | The Stock - Multiple Materials screen displays. |  |
| 3 | Enter Plant, Material Data, and Customer | On the Stock - Multiple Materials screen, make the following entries:Plant: 3330Material Number: Enter material numbers used in the consignment fill-up order.Customer: Enter the customer used in sales document.Special Stock Type: WChoose Go. | The customer consignment stock is displayed. The delivered quantity is posted into the consignment stock.Note You may need to adapt the following filters:Special Stock TypeCustomer: You may need to adapt column settings, for example, Customer. |  |

###### Create Customer (F2) Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to creater customer invoice.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Create Billing Documents - VF01 (VF01). | The Create Billing Documents screen displays. |  |
| 3 | Maintain Billing Date | Choose billing type Invoice (F2) and maintain billing date, for example, current date.Enter Delivery Number.Choose Enter. |  |  |
| 4 | Save | Choose Save. | The F2 billing document is created. |  |

Financial Postings

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 12100000 Domestic DE Customer 1 | 41000000 Revenue Domestic – Product22000000 Output Tax (MWS) | none |
| Trading Good (HAWA) | 44002000 Sales Disc Domestic | 41000000 Rev Domestic Prod22000000 Output Tax (MWS) | none |

###### Create Intercompany Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create the intercompany invoice in delivery company code, in background, AP accounting document is generated in ordering company via IDOC.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents - VF01 (VF01). | The Create Billing Document screen displays. |  |
| 3 | Maintain Billing Date | Choose billing type Intercompany Billing (IV) and maintain billing date, for example, <current date>, enter Delivery Number, then choose Enter. |  |  |
| 4 | Save | Choose Save. | IV billing document is created, note down billing document number for further use.Note To check the details of the iDoc generated by the intercompany billing document, you can refer to the section Message Monitor of the Setup Instructions document [Intercompany Sales Order Processing Setup (1HO 1MX 1WO) (SAP Customer)](https://support.sap.com/content/dam/SAAP/SAP_Activate/S4H_489%20Intercompany%20Sales%20Order%20Processing%20%20Setup%20(1HO%201MX%201WO).docx). |  |

Financial Postings

| Material | Debit Accounts | Credit Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 12300000 Company Code 3310 as Business | 41001500 Rev Affiliate- Prod22000000 Output tax (MWS) | None |

###### Display AP Journal Entry

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display account payable accounting documents generated by IV invoice IDoc.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Journal Entries (F0717A). | The Manage Journal Entries screen displays. |  |
| 3 | Add the Original Reference Document Field as Filter | Choose Adapt Filters, select Original Reference Document option, and choose OK. | The Original Reference Document field is added as a filter. |  |
| 4 | Filter AP Entry Document by Referencing IV Invoice | Make the following entry and choose Go.Original Reference Document: <00 + Intercompany invoice number generated in previous step> | AP journal entry number displays. |  |
| 5 | Display AP Entry | Choose AP accounting number in the Journal Entry column.Choose Display Journal Entries - New Version. | AP accounting document displays. |  |

|  |
| --- |
| Note Besides the scenario described in the Post Goods Issue section, opposite-direction transactions can be supported: The customer orders goods from company code 3320 . Company code 3310 directly delivers goods to the customer as a supplier of 3320. Two invoices are generated: one is the customer invoice to company code3320, the other is the intercompany invoice that company code 3320 pays to company code 3310 . |

##### Consignment Pick-up

The consignment pick-up process is the same as the scope item Customer Consignment (1IU). For details, refer to the test script of the scope item 1IU to perform the sub-process of consignment pick-up. You can find the test script of 1IU on SAP Signavio Process Navigator.

|  |
| --- |
| Note The delivery plant code on sales order item should be entered with a plant which belongs to a different company code, for example, 3330. |

##### Consignment Return

###### Create Consignment Return Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Goods that have been consumed or sold by the customer may be returned to the consignment stock. In this case, the customer communicates the returning quantity together with the corresponding batch number. A return order with the following follow-on documents is generated:

- A returns delivery with subsequent goods receipt
- A credit note for returns
- A internal credit memo is created for returns

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Sales Orders - VA01 (VA01). | The Create Sales Document screen displays. |  |
| 3 | Enter Order Type | On the Create Sales Document screen, make the following entries:Order Type: CCRESales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 4 | Enter Material Data | On the Create Consignment Return: Overview screen, make the following entries and choose Continue (Enter):Sold-To Party: 33100013Ship-To Party: 33100013Cust. Reference: Enter the customer purchase order number.On the Sales A tab, make the following entries:Deliver.Plant: <Deliver.Plant>, in delivering company code,for example, 3330Material: <Enter all material numbers mentioned in master data section>Order Quantity: <Enter the required quantity (for example, 10 PC)>Check that the Billing Block is set. |  |  |
| 5 | Check Intercompany Pricing Condition Type | Choose the line item and select Conditions, check intercompany pricing condition type exists, for example, PI02 Intercompany. |  |  |
| 6 | Save Document | Choose Save.Make a note of the sales order number___________. | The customer return order is created. |  |

###### Create Return Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create the return delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Outbound Delivery - With Order Reference (VL01N). | The Create Outbound Delivery with Order Reference screen displays. |  |
| 3 | Search Sales Order | Make the following entries:Shipping Point: 333CSelection Date: <the delivery selection date>Sales Document: <the sales order number created previously>Choose Continue. |  |  |
| 4 | Create Delivery | Select your sales order items. | The creation of a delivery is triggered. |  |
| 5 | Save Document | Choose Save.Make a note of the delivery number:_____________. | A return delivery is created. |  |

|  |
| --- |
| Note With the Analyze Outbound Delivery Logs app, you can display an overview of the logs of all the deliveries that have been created in your system. You can filter by, for example, Created By. If you select the arrow on the right of each delivery log entry, you can display the exact message type and text, and also the related sales document. |

###### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you post the goods receipt. When the goods receipt is posted, the transfer from the consignment stock is carried out at the same time as the direct posting into the free stock of the return storage location.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). | The Outbound Delivery Monitor screen displays. |  |
| 3 | Make Entries | Choose For Goods Issue. Make the following entry and choose ExecuteShipping Point: 333C |  |  |
| 4 | Post Goods Issue | Select the relevant delivery and choose Post Goods Issue. In the dialog box, choose today’s date and choose Continue. | The goods receipt is posted. |  |

Financial Postings

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 51600000Consptn Trde Gds | 13600000Inventory TradingGd | none |

###### Check Stock Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The goods are transferred again to customer's consignment stock. The stock overview reflects this transfer of products.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Stock - Single Material (F1076). | The Stock - Multiple Materials screen displays. |  |
| 3 | Enter Plant, Material Data, and Customer | On the Stock - Multiple Materials screen, make the following entries:Plant: 3330Material Number: Enter the material numbers used in the consignment pick-up order.Customer: Enter the customer used in sales document.Special Stock Type: WChoose Go. | The customer consignment stock is displayed. The delivered quantity has been posted into the consignment stock.Note You may need to adapt the following filters:Special Stock TypeCustomerYou may need to adapt column settings. For example, Customer. |  |

###### Release Consignment Return Order for Billing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The consignment return order has been created with a billing block to be removed manually. This is done to add a check of the credit memo to ensure that the entries are correct.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Returns and Refund Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer Returns (F1708). | The Manage Customer Returns screen displays. |  |
| 3 | Navigate to Display Return Order Screen | On the Manage Customer Returns screen, enter the respective order number created in previous step in the Customer Returns field and choose Go.Choose the return order line that displays. |  |  |
| 4 | Navigate to Change Return Order Screen | Choose Change. |  |  |
| 5 | Remove Billing Block | On the Change Consignment Return: Overview screen, remove the billing block. | The billing block is removed. |  |
| 6 | Save Document | Choose Save. | The sales order is saved. |  |

###### Create Customer Credit Memo

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to credit memo is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Documentsscreen displays. |  |
| 3 | Define Billing Setting | Choose the Billing Setting in the bottom bar. Switch on the following settings:Enter Billing Data before billing.Separate Billing Documents for Each Billing Due List Item.Automatically Post Billing Documents.Display Billing Document After Creation. |  |  |
| 4 | Search for Billing List | In the search condition, enter criteria if necessary. | SD document(s) displays in the result. |  |
| 5 | Choose SD Document | Select the row of credit memo request document recorded previously and choose Create Billing Documents. | Create Billing Documents screen displays. |  |
| 6 | Maintain Billing Type and Billing Date | Choose billing type Credit Memo for Returns (CBRE) and maintain billing date, for example, current date, then press the OK button. | The draft billing document with ID Sxxxxxxxx is dis-played. |  |
| 7 | Save Billing Document | On the Billing Document screen, choose Save, The draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx, make a note of the billing document number: __________. | Final credit memo is generated. |  |

Financial Postings

| Material | Debited Accounts | Credited Account | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 41000000Rev Domestic Prod 22000000Output Tax (MWS) 21030000 (optional) Freight Clrg MM | 12100000 Domestic DE Customer 144002000 Sales Discounts – Domestic | none |

###### Create Internal Credit Memo

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how the internal credit memo is created in delivery company code, and how the AP Journal Entry is generated in ordering company via IDOC in background.

Prerequisites

Customer credit memo created previously.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Documents screen displays. |  |
| 3 | Define Billing Setting | Choose the Billing Setting in the bottom bar. Choose ON for the following settings:Enter Billing Data before billing.Separate Billing Documents for Each Billing Due List Item.Automatically Post Billing Documents.Display Billing Document After Creation. |  |  |
| 4 | Search for Billing List | In the search condition, enter criteria if necessary. | SD document(s) displays in the result. |  |
| 5 | Choose SD Document | Select the row of return delivery document created previously and choose Create Billing Documents. | Create Billing Documents screen displays. |  |
| 6 | Maintain Billing Type and Billing Date | Choose billing type Internal Credit memo (IG) and maintain billing date, for example, current date, then choose OK. | The draft billing document with ID Sxxxxxxxx displays. |  |
| 7 | Save Billing Document | On the Billing Document screen, choose Save, the draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx, make a note of the billing document number: __________.To check the details of the IDoc generated by the intercompany billing document, you can refer to the section Message Monitoring of the 1HO Set-up Instructions document [Intercompany Sales Order Processing Set-up instructions](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/Setup/1HO_Set-Up_EN_XX.pdf). | Internal credit memo is generated. |  |

Financial Postings

| Material | Debited Accounts | Credited Account | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 41001500 Revenue Affiliate - Product22000000 Output Tax (MWS) | 12300000 company code 3310 as a business partner | none |

###### Display AP Accounting Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display account payable accounting documents generated by internal credit memo IDoc.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Journal Entries (F0717A). | The Manage Journal Entries screen displays.Note If app Manage Journal Entries (F0717A) is not there on the Home Page, please search and find it using the magnifier icon. |  |
| 3 | Add the Original Reference Document Field as Filter | Choose Adapt Filters, select Original Reference Document option, and choose OK. | The Original Reference Document field is added as a filter. |  |
| 4 | Filter AP Accounting Document by Referencing Internal Credit Memo | Make the following entry:Original Reference Document: <00 + internal credit memo number generated in previous step>Choose Go. | AP accounting document number displays. |  |
| 5 | Display AP Accounting Document | Choose AP accounting number in the Journal Entry column.Choose Display Journal Entries - New Version. | AP accounting document displays. |  |

### International

#### Free of Charge

##### Create Free of Charge Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, sales order is created in ordering company, goods will be directly delivered to the customer from affiliate company/plant.

|  |
| --- |
| Note This is just an example of sample goods delivery. Customer is responsible for how to handle the taxation. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders Without Charge (F2305). | The Manage Sales Orders Without Charge screen displays. |  |
| 3 | Navigate to Create Sales Order Screen | From Manage Sales Orders screen, select the Create Sales Order Without Charge. | The Create Sales Documents screen displays. |  |
| 4 | Enter Sales Document Type | Order Type: CBFD Deliv.Free of ChargeSales Organization: 3310Distribution Channel: 10Division: 00Press Continue. | Create Deliv.Free of Charge: Overview screen displays. |  |
| 5 | Enter Order Details | Sold-to-Party: 33100002Cust. Reference: PO numberOrder Reason : <Order Reason> Free of charge sampleDeliver.Plant: <Delivery Plant> in delivering company code, for example, 1710Material: Material Number, for example TG12Order Quantity: quantity, for example 1 | Item category CBXN is determined automatically supporting transfer of costs to accounting and creation of proforma invoices. |  |
| 6 | Enter Tax Departure Country/Region | On the top menu, choose More > Goto > Header > Billing |  |  |
| 7 | Tax Country/Region Instruction | In the Billing section, input:Tax Departure Ctry/R: AE |  |  |
| 8 | Go Back | Choose Go Back. | The Create Standard Order: Overview screen displays. |  |
| 9 | Check intercompany pricing condition type | Choose the line item and select Conditions, check intercompany pricing condition type exists, for example PI02 Intercompany. |  |  |
| 10 | Save | Choose Save. | A Free of Charge sales order is created. Make a note of the sales order document number: |  |

##### Create Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create the delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Outbound Deliveries - From Sales Orders (F0869A). | The Create Outbound Deliveries screen displays. |  |
| 3 | Search Sales Order | Make the following entries and choose Go:Shipping Point: 1710<Shipping point of intercompany delivery plant>Planned Creation Date: <Delivery selection date>Sales Document: Sales order number created previously | The Delivery Creation: Overview screen displays. |  |
| 4 | Create Delivery | Select your sales order items and choose Create Deliveries. | Creation of a delivery is triggered. |  |
| 5 | Check Details | Choose Display Log. | The Analyze Delivery Log screen displays, and delivery is created successfully with delivery number shown on tab Deliveries. |  |

##### Perform Picking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The picking process involves taking goods from a storage location and staging the right quantity in a picking area where the goods are prepared for shipping.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Open Outbound Delivery Monitor | On the Outbound Delivery Monitor screen, choose For Picking. |  |  |
| 4 | Enter shipping point | On the Outbound Deliveries for Picking screen, make the following entry:Shipping Point: 1710<Shipping point of intercompany delivery plant> |  |  |
| 5 | Select the Only Picking without WM checkbox and choose Execute | Select the Only Picking without WM checkbox and choose Execute. |  |  |
| 6 | Select the Outbound Delivery | On the Day’s Workload for Picking screen, select your outbound delivery and choose Change Outbound Deliveries. |  |  |
| 7 | Input Picked Quantity | On the Delivery xxxxxxxx change: Overview screen, choose tab Picking, input quantity in Picked Qty field.Picking status is set to Completely processed if picked quantity and delivery quantity is equal.Deviations in quantity can be solved by the function Copy Picked Quantity as Delivery Quantity. |  |  |
| 8 | Save Document | Choose Save. |  |  |

##### Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you post the goods issue.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). | The Manage Outbound Deliveries screen displays. |  |
| 3 | Open Outbound Delivery Monitor | Choose For Goods Issue. Make the following entries and Choose Execute.Shipping point: 1710<Shipping point of intercompany delivery plant> |  |  |
| 4 | Post Good Issue | Mark the relevant delivery and choose Post Goods Issue. Select today’s date from the dialog box. | The goods issue is posted. |  |

##### Create F2 Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to handle the billing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the roleBilling Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents VF01 under Billing Document | The Create Billing Document screen displays. |  |
| 3 | Maintain Billing Date | Choose billing type Invoice (F2) and maintain billing date, for example current date, enter delivery number, then press Enter. |  |  |
| 4 | Save | Choose Save. | F2 billing document is created |  |

Financial Postings

| Material | Debit Accounts | Credit Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 44002000 Sales Disc Domestic | 41000000 Rev Domestic Prod | None |

##### Create Intercompany IV Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity you the intercompany invoice is created in delivery company code, in background, AP accounting document is generated in ordering company via IDOC.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad using the roleBilling Clerk. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents VF01 under Billing Document | The Create Billing Document screen displays. |  |
| 3 | Maintain Billing Date | Choose billing type Intercompany Billing (IV) and maintain billing date, for example current date, input delivery number, then press Enter. |  |  |
| 4 | Save | Choose Save. | IV billing document is created, note down billing document number for further use.Note To check the details of the iDoc generated by the intercompany billing document, you can refer to the section Message Monitor of the Setup Instructions document [Intercompany Sales Order Processing Setup (1HO 1MX 1WO) (SAP Customer)](https://support.sap.com/content/dam/SAAP/SAP_Activate/S4H_489%20Intercompany%20Sales%20Order%20Processing%20%20Setup%20(1HO%201MX%201WO).docx). |  |

Financial Postings

| Material | Debit Accounts | Credit Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 33403310 Company Code 3310 as Business | 41001500 Rev Affiliate- Prod22000000 Output tax (MWS) | None |

##### Display AP Accounting Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity you display account payable accounting documents generated by IV invoice IDoc.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad using the role General Ledger Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Journal Entries (F0717A). | The Manage Journal Entries screen displays.Note If app Manage Journal Entries (F0717A) is not there on the Home Page, please search and find it using the magnifier icon. |  |
| 3 | Add the Original Reference Document Field as Filter | Choose Adapt Filters, select Original Reference Document option, and choose OK. | The Original Reference Document field is added as a filter. |  |
| 4 | Filter AP Accounting Document by Referencing IV Invoice | Make the following entry:Original Reference Document: <00 + Intercompany invoice number generated in previous step>Choose Go. | AP accounting document number displays. |  |
| 5 | Display AP Accounting Document | Choose AP accounting number in the Journal Entry column.Choose Display Journal Entries - New Version. | AP accounting document displays. |  |

#### Credit Memo

##### Create Intercompany Credit Memo

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to generate a credit memo by referring the Intercompany IV billing document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents - VF01 (VF01) . | The Create Billing Documents screen displays. |  |
| 3 | Define Billing Setting | Choose billing type CICM from dropdown list.Search for intercompany invoice number in document field.Maintain Entries on Billing Documents tab:Billing Type: IVSold to party: 33403310Sales Organization: 3330Click on Find.Select billing document from the list.Choose Execute. | List with lines for intercompany invoice display and intercompany credit memo editing is displayed. |  |
| 4 | Modify intercompany Credit memo | Double click line with billing type Intercompany Credit MemoNavigate to item conditions, for example, PIC2Change item conditions | Net value of the document has been changed. |  |
| 5 | Save Intercompany Credit Memo | Choose Save. | Billing document generated, not released to accounting. |  |
| 6 | Display Billing Document after Creation | The billing document displays automatically. Make a note of the billing document number: __________. |  |  |

Financial Postings

| Material | Debit Accounts | Credit Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 41001500 Rev Affiliate- Prod | 33403310 Company Code 3310 as Business | None |

##### Display AP Accounting Document of Intercompany Credit Memo

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you display account payable accounting documents generated by Intercompany Credit Memo IDoc.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad using the role General Ledger Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Journal Entries (F0717A). | The Manage Journal Entries screen displays.Note If app Manage Journal Entries (F0717A) is not there on the Home Page, please search and find it using the magnifier icon. |  |
| 3 | Add the Original Reference Document Field as Filter | Choose Adapt Filters, select Original Reference Document option, and choose OK. | The Original Reference Document field is added as a filter. |  |
| 4 | Filter AP Accounting Document by Referencing Intercompany Credit Memo | Make the following entry:Original Reference Document: <00 + intercompany credit memo number generated in previous step>Choose Go. | AP accounting document number displays. |  |
| 5 | Display AP Accounting Document | Choose AP accounting number in the Journal Entry column.Choose Display Journal Entries - New Version. | AP accounting document displays. |  |

#### Debit Memo

##### Create Intercompany Debit Memo

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to generate a debit memo by referring the Intercompany IV billing document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents - VF01 (VF01). | The Create Billing Documents screen displays. |  |
| 3 | Define Billing Setting | Choose billing type CIDM from dropdown list.Search for intercompany invoice number in document field.Maintain Entries on Billing Documents tab:Billing Type: IVSold to party: 33403310Sales Organization: 3330Click on Find.Select billing document from the list.Choose Execute. | List with lines for intercompany invoice is displayed and then intercompany debit memo editing is displayed. |  |
| 4 | Modify intercompany Debit memo | Double click line with billing type Intercompany Debit MemoNavigate to item conditions, for example, PIC2Change item conditions | Net value of the document has been changed. |  |
| 5 | Save intercompany Debit Memo | Choose Save. | Billing document generated, not released to accounting. |  |
| 6 | Display Billing Document after Creation | The billing document displays automatically. Make a note of the billing document number: __________. |  |  |

Financial Postings

| Material | Debit Accounts | Credit Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 33403310 Company Code 3310 as Business | 41001500 Rev Affiliate- Prod | None |

##### Display AP Accounting Document of Intercompany Debit Memo

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you display account payable accounting documents generated by Intercompany Debit Memo IDoc.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad using the role General Ledger Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Journal Entries (F0717A). | The Manage Journal Entries screen displays.Note If app Manage Journal Entries (F0717A) is not there on the Home Page, please search and find it using the magnifier icon. |  |
| 3 | Add the Original Reference Document Field as Filter | Choose Adapt Filters, select Original Reference Document option, and choose OK. | The Original Reference Document field is added as a filter. |  |
| 4 | Filter AP Accounting Document by Referencing Intercompany Debit Memo | Make the following entry:Original Reference Document: <00 + intercompany debit memo number generated in previous step>Choose Go. | AP accounting document number displays. |  |
| 5 | Display AP Accounting Document | Choose AP accounting number in the Journal Entry column.Choose Display Journal Entries - New Version. | AP accounting document displays. |  |

#### Non-Stock Material Sales

##### Create Sales Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, sales order is created in ordering company, goods will be directly delivered to the customer from affiliate company/plant.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Navigate to Create Sales Order Screen | Choose Create > Create Sales Order - VA01 . | The Create Sales Documents screen displays |  |
| 4 | Enter Sales Document Type | Make the following entries:Order Type: OR Standard OrderSales Organization: 3310Distribution Channel: 10Division: 00Choose Continue. |  |  |
| 5 | Enter Order Details | Make the following entries:Sold-to-Party: 33100002Ship-toParty: 33100002Cust. Reference: PO numberDeliver.Plant: <Delivery Plant> in delivering company code, for example, 1710Material: Material Number, for example NS0002Order Quantity: <quantity>, for example 10 |  |  |
| 6 | Enter Tax Departure Country/Region | On the top menu, choose Menu > Goto > Header > Billing . |  |  |
| 7 | Tax Country/Region Instruction | In the Billing section, make following entry:Tax Departure Ctry/R: AE. |  |  |
| 8 | Go Back | Choose Back. | The Create Standard Order: Overview screen displays. |  |
| 9 | Check intercompany pricing condition type | Select the line item and choose the Item Conditions icon. Check intercompany pricing condition type exists, for example PI02 Inter-company % |  |  |
| 10 | Save | Choose Save. | A sales order is created. Make a note of the sales order document number: |  |

##### Process Sales Order Approval (Optional)

Follow the procedure for Process Sales Order Approval steps in the scope item Sell from Stock (BD9).

Purpose

This process step shows you how to review the sales orders that might need to be approved.

Procedure

Complete the activities of Process Sales Order Approval step described in the scope item Sell from Stock (BD9).

##### Create Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create the delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Outbound Deliveries. | The Create Outbound Deliveries screen displays. |  |
| 3 | Search Sales Order | Make the following entries and choose Go:Shipping point: 1710<Shipping point of intercompany delivery plant>Planned Creation Date: <Delivery selection date>Sales Document: Sales order number created previously | The Delivery Creation: Overview screen displays. |  |
| 4 | Create Delivery | Select your sales order items and choose Create Deliveries. | Creation of a delivery is triggered. |  |
| 5 | Check Details | Choose Display Log. | The Analyze Delivery Log screen displays, and delivery is created successfully with delivery number shown on tab Deliveries. |  |

##### Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you post the goods issue.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on the SAP Fiori Launchpad using the role Shipping Specialist . |  |  |
| 2 | Access the App | Open Change Outbound Delivery. | The Change Outbound Delivery screen displays. |  |
| 3 | Change Outbound Delivery | Make the following entries and choose Continue.Outbound Delivery: <delivery number created previously> | The Delivery XXX Change: Overview screen displays. |  |
| 4 | Post Goods Issue | Choose the Post Goods Issue. | The goods issue is posted. |  |

##### Create F2 Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to handle the billing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad using the role Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents VF01 under Billing Document | The Create Billing Document screen displays. |  |
| 3 | Maintain Billing Date | Choose billing type Invoice (F2) and maintain billing date, for example current date, input delivery number, then press Enter. |  |  |
| 4 | Save | Choose Save. | F2 billing document is created |  |

Financial Postings

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Non-Stock Material (NLAG) | 33100002 Rcvbls Domestic AE 2 | 41910000 Billed Rev Dom22000000 Output tax (MWS) | none |

##### Create Intercomapny IV Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the intercompany invoice is created in delivery company code, in background, AP accounting document is generated in ordering company via IDOC.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad using the role Billing Clerk. |  |  |
| 2 | Access the App | Open Create Billing Documents VF01 under Billing Document. | The Create Billing Document screen displays. |  |
| 3 | Maintain Billing Date | Choose billing type Intercompany Billing (IV) and maintain billing date, for example current date, input delivery number, then choose Enter. |  |  |
| 4 | Save | Choose Save. | IV billing document is created, note down billing document number for further use. |  |

Financial Postings

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Non-Stock Material (NLAG) | 33403310 Company Code 3310 as Business | 41970000 Billed Revenue Affiliated | none |

##### Display AP Accounting Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display account payable accounting documents generated by IV invoice IDoc.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad using the role General Ledger Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Journal Entries (F0717A). | The Manage Journal Entries screen displays.Note If app Manage Journal Entries (F0717A) is not displayed on the Home Page, please search and find it using the magnifier icon. |  |
| 3 | Add the Original Reference Document Field as Filter | Choose Adapt Filters, select Original Reference Document option, and choose OK. | The Original Reference Document field is added as a filter. |  |
| 4 | Filter AP Accounting Document by Referencing IV Invoice | Make the following entry:Original Reference Document: <00 + Intercompany invoice number generated in previous step>Choose Go. | AP accounting document number displays. |  |
| 5 | Display AP Accounting Document | Choose AP accounting number in the Journal Entry column.Choose Display Journal Entries - New Version. | AP accounting document displays. |  |

#### Sales Kits

##### Create Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a sales order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Navigate to Create Sales Order Screen | On the Manage Sales Orders screen, choose Create > Create Sales Order - VA01 . |  |  |
| 4 | Enter the Order Data | On the Initial screen, make the following entries and choose Continue:Order Type:ORSales Organization: 3310Distribution Channel: 10Division: 00Choose the Order Type CBFD manually if the item is free of charge during order creation. |  |  |
| 5 | Enter Order Details | On the Create Sales Orders: Overview screen, make the following entries:Sold-to Party: 33100002PO Number: <PO number>Order Reason: <Order Reason>Deliver.Plant: <Deliver.Plant>, for example, 1710Material Number: <SDBOMERLAHD> or <SDBOMLUMFHD>Quantity: <Quantity>, for example, <1>If you are using SDBOMERLAHD or SDBOMLUMFHD in testing, the sales BOM will explode and subitems will appear. Here is the difference between them:For SDBOMERLAHD, pricing and inventory managed on the main item.For SDBOMLUMFHD, pricing and inventory managed on the subitems. |  |  |
| 6 | Enter Tax Departure Country/Region | On the top menu, choose Menu > Goto > Header > Billing . |  |  |
| 7 | Tax Country/Region Instruction | In the Billing section, make following entry:Tax Departure Ctry/R: AE |  |  |
| 8 | Check Intercompany Pricing Condition Type | Select the line item and choose the Item Conditions icon. Check intercompany pricing condition type exists, for example, PI02 Intercompany. |  |  |
| 9 | Save Document | Choose Save. Make a note of the sales order number: __________. | The order is saved and its order confirmation is printed out. |  |

##### Create Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create the delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Create Outbound Deliveries - From Sales Orders (F0869A). | The Create Outbound Deliveries-From Sales Orders screen displays. |  |
| 3 | Search for Sales Order | Make the following entries and choose Go:Shipping Point:1710Planned Creation Date: <Delivery selection date>Sales Document: <Sales Order Number Created Previously> |  |  |
| 4 | Create Delivery | Select your sales order, and choose Create Deliveries. | A delivery creation is triggered |  |
| 5 | Check Details | Choose Display Log. | The Analyze Delivery Log screen displays.A delivery is created successfully with delivery number shown on tab Deliveries. |  |

With the Analyze Outbound Delivery Logs app, you can display an overview about the logs of all the deliveries, which have been created in your system. You can filter by example created by and Additional settings. If you select the arrow on the right of each delivery log entry you can see its message type, text, and also related sales document.

##### Execute Picking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The picking process involves taking goods from a storage location and staging the right quantity in a picking area where the goods are prepared for shipping. This process step shows you how to execute picking.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad screen displays. |  |
| 2. | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3. | Choose Picking | Choose For Picking. |  |  |
| 4. | Enter Shipping Point | Make the following entries and choose Execute.Shipping Point:1710Only Picking without WM: X |  |  |
| 5. | Change Outbound Delivery | From Day’s Workload for Picking, select your delivery number and choose Change Outbound Deliveries. |  |  |
| 6. | Check Batch Split | Navigate to the Picking tab, check if batch split exists in Batch Split Indicator column: |  |  |
| 7. | Enter Picked Quantity | If batch split exists, choose Batch Split Exists to expand sub item(s), enter quantity equal to delivery qty in Picked Qty field for subitem.If batch split doesn't exist, enter quantity equal to delivery qty in Picked Qty field for picking related item(s).For SDBOMERLAHD, enter picked quantity on the main item.For SDBOMLUMFHD, enter picked quantity on the subitems. |  |  |
| 8. | Enter | Choose Enter. |  |  |
| 9. | Save | Choose Save. | The delivery have been picked. |  |

##### Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post a goods issue.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). | The Outbound Delivery Monitor screen displays. |  |
| 3 | Open Outbound Delivery Monitor | Choose For Goods Issue.Shipping Point:1710 |  |  |
| 4 | Post Good Issue | Choose Post Goods Issue. | The goods issue is posted. |  |

##### Create F2 Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to handle the billing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents - VF01 (VF01). | The Create Billing Document screen displays. |  |
| 3 | Maintain Billing Date | Choose billing type Invoice(F2) and maintain billing date, for example, <current date>, enter Delivery Number, then choose Enter. |  |  |
| 4 | Save | Choose Save. | F2 billing document is created. |  |

Financial Postings

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 44002000 Sales Disc Domestic | 41000000 Rev Domestic Prod | None |

##### Create Intercompany IV Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create the intercompany invoice in delivery company code, in background, AP accounting document is generated in ordering company via IDOC.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents - VF01 (VF01). | The Create Billing Document screen displays. |  |
| 3 | Maintain Billing Date | Choose billing type Intercompany Billing (IV) and maintain billing date, for example <current date>, enter Delivery Number, then choose Enter. |  |  |
| 4 | Save | Choose Save. | IV billing document is created, note down billing document number for further use.Note To check the details of the iDoc generated by the intercompany billing document, you can refer to the section Message Monitor of the Setup Instructions document [Intercompany Sales Order Processing Setup (1HO 1MX 1WO) (SAP Customer)](https://support.sap.com/content/dam/SAAP/SAP_Activate/S4H_489%20Intercompany%20Sales%20Order%20Processing%20%20Setup%20(1HO%201MX%201WO).docx). |  |

Fi2cial Postings

| Material | Debit Accounts | Credit Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 33403310 Company Code 3310 as Business | 41001500 Rev Affiliate- Prod22000000 Output tax (MWS) | None |

##### Display AP Accounting Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display account payable accounting documents generated by IV invoice IDoc.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Journal Entries (F0717A). | The Manage Journal Entries screen displays.Note If app Manage Journal Entries (F0717A) is not there on the Home Page, please search and find it using the magnifier icon. |  |
| 3 | Add the Original Reference Document Field as Filter | Choose Adapt Filters, select Original Reference Document option, and choose OK. | The Original Reference Document field is added as a filter. |  |
| 4 | Filter AP Accounting Document by Referencing IV Invoice | Make the following entry:Original Reference Document: <00 + Intercompany invoice number generated in previous step>Choose Go. | AP accounting document number displays. |  |
| 5 | Display AP Accounting Document | Choose AP accounting number in the Journal Entry column.Choose Display Journal Entries - New Version. | AP accounting document displays. |  |

#### Down Payment

##### Create Sales Orders with Billing Plan

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to require a down payment from the customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Navigate to Create Sales Order Screen | Choose Create > Create Sales Order - VA01 . | The Create Sales Documents: Initial screen displays. |  |
| 4 | Enter Sales Document Type | Make the following entries:Sales Document Type: <sales order type> , for example, OR (Standard Order)Sales organization: 3310Distribution channel: 10Division: 00Choose Continue. | The Create Standard Order xxx: Overview screen displays. |  |
| 5 | Enter Customer Number | Make the following entries:Sold-to Party: 33100002Customer Reference: <Customer reference>, for example,<customer purchase Order number>Press Enter. |  |  |
| 6 | Enter Order Details | Make the following entries:Deliver.Plant: <Delivery plant> in delivering company code, for example, 1710Material: <Material number>, for example, TG12Order Quantity: <quantity>, for example, 10Item Category:CBAO Milestone-Bill.Plan for Trading goods. |  |  |
| 6 | Enter Tax Departure CountryRegion | On the top menu, choose Menu > Goto > Header > Billing . |  |  |
| 7 | Tax Country/Region Instruction | In the Billing section, make following entry:Tax Departure Ctry/R: AE |  |  |
| 8 | Check Intercompany Pricing Condition Type | Select the line item and choose the Item Conditions icon. Check intercompany pricing condition type exists, for example, PI02 Intercompany. |  |  |
| 9 | Choose Billing Plan | Select the item. Choose Menu > Goto > Item > Billing plan .Note Alternatively, you can assign billing plan on header level: Choose Menu > Goto > Header > Billing Plan . The header billing plan will be applied to all items with item category CBAO. Amount is proportionally to the value of the items participating in the down payment process distributed to the items. |  |  |
| 10 | Enter Details | For the first line item (Down Payment), make the following entries for the advance payment:Billing Date: <Billing date>. For example, enter today's date.Bill Value: <Amount of billing>. For example: Down payment amountDate category (DCat): 04 |  |  |
| 11 | Enter Details | For the second line item (Closing Invoice), make the following entries for the advance payment:Billing Date: <Billing date>. For example, enter today's date.Date category(DCat): 02 |  |  |
| 12 | Enter | Press Enter. Confirm system messages with enter if necessary. | Closing invoice related data is determined. For example, in Bill value field, the amount of billing is calculated by the system. |  |
| 13 | Back | Choose Back. |  |  |
| 14 | Save | Choose Save. |  |  |

##### Change Sales Orders (Remove Billing Block)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to remove billing block from a sales order.

Prerequisite

The billing block must be manually removed for the first down payment request to be processed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Change Sales Documents: Initial screen displays. |  |
| 3 | Search For Sales Order | Make the following entries and choose Enter:Order number: Order number from the previous process step. | The Change Standard Order xxx: Overview screen displays. |  |
| 4 | Navigate to Sales Order Screen | Select the sales order number and choose Change Sales Orders - VA02 (VA02). | The Change Sales Order xxx: Overview screen displays. |  |
| 5 | Choose Billing Plan | Select the line item.From the menu, choose More > Goto > Item > Billing plan .Alternatively, If you assign billing plan on header level: choose More > Goto > Header > Billing plan . Removal of billing block on header level also unlocks items automatically. | The Change Standard Order xxx: Item Data screen displays. |  |
| 6 | Delete Billing Block | In the Dates section, in the Block column delete the billing block for the Down payment item (keep the billing block for the Closing invoice item). |  |  |
| 7 | Back | Choose Back. |  |  |
| 8 | Save | Save your entries. | The billing block is removed. |  |

##### Create Attachment for Sales Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create attachment for a sales order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Navigate to Display Sales Order Screen | On the Manage Sales Orders screen, enter the respective order number created in previous step in the Sales Order and choose Go.Click the sales order number and choose Change Sales Order - VA02. |  |  |
| 4 | Create Attachment for Sales Order | Choose Services for Object on the top right corner of screen, choose Create Attachment. | The Import File screen displays. |  |
| 5 | Import File | Choose OK in the File Upload dialog box.In the Open view, choose local path and file, and choose Open. | The attachment was successfully created. |  |
| 6 | Check Attachment | Choose Services for Object on top right corner of screen, choose Attachment List. | Attachment brings up on the Service: Attachment list screen. |  |

##### Create Down Payment Request

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
| 2 | Access the App | Open Create Billing Documents (F0798) under Sales > Billing Documents . | The Create Billing Document screen displays. |  |
| 3 | Define Billing Setting | Choose Billing Setting in bottom bar. There are four settings, make all of these settings to ON:Enter Billing Data before billingSeparate Billing Documents for Each Billing Due List ItemAutomatically Post Billing DocumentsDisplay Billing Document After Creation |  |  |
| 4 | Search for Billing List | In the search condition, enter criteria if necessary. | SD document(s) displays in the result. |  |
| 5 | Choose Sales Document | More than one SD document item appear in Billing Due List Items table, select the row relevant to down payment request, and choose Create. | The Create Billing Documents screen displays. |  |
| 6 | Maintain Billing Type and Billing Date | Choose billing type Down payment request (FAZ) and maintain billing date, for example current date, then choose Create. | The draft billing document is created. |  |
| 7 | Save Billing Document | On the Billing Document screen, choose Save.The draft billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx.Make a note of the billing document number: __________. | Billing document is generated. |  |

Financial Postings

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 21191000 Down payment requests (customers) | none | none |

##### Post a Down Payment

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Accounts Receivable Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Incoming Payments (F1345). | The Post Incoming Payments (F1345) screen displays. |  |
| 3 | Enter Details | Make the following entries and choose Propose Items:General Information area:Company Code: 3310Posting Date: Current dateJournal Entry Date: <Current date>Value Date: Current datePeriod: Current periodJournal Entry Type: DZ (Customer Payment)Bank Data areaG/L Account (Company Code CoA): 11001060House Bank: DEBK1Bank Account: DEAC1Amount: Down Payment Amount / AEDNote Enter the amount of the journal entry the customer has been debited with in the previous step(billing value plus value added tax)Open Item Selection areaAccount Type/Account ID: Customer / 33100002 |  |  |
| 4 | Search for Down Payment Request | Choose Select More.In Line Item Type field, select checkbox in Special G/L Transactions and deselect other values from drop-down menu, then choose OK. | Select More dialog box displays.All down payment request documents which meet the conditions are listed in Open Items table. |  |
| 5 | Select Down Payment Request | Choose Clear in the down payment request document entry in Open Items table. | The item is copied to Items to Be Cleared table. |  |
| 6 | Post | Choose Post. | Success dialog box pop ups, the information Journal entry 14XXXXXXXX successfully posted displays. |  |
| 7 | Display Journal Entry | Choose Display. | The Manage Journal Entries screen displays. Detailed information involved in down payment journal entry is shown. |  |

Financial Postings

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 11001060 Bank Account21191500 Tax sett.dwn pmt cus | 21190000 Down Payments - Customers22000000 Output tax (MWS) | none |

##### Create Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a delivery.

Prerequisite

The goods receipt was posted to the individual customer’s stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Create Outbound Deliveries - From Sales Orders (F0869A). | The Create Outbound Deliveries - From Sales Orders (F0869A) screen displays. |  |
| 3 | Search Sales Order | Make the following entries and choose Go:Shipping Point: <shipping point> for example, 1710Planned Creation Date: <Delivery selection date>Sales Document: <Sales order number created previously> |  |  |
| 4 | Create Delivery | Select your sales order and choose Create Deliveries. | A delivery is triggered to create. |  |
| 5 | Check Details | Choose Display Log. | The Analyze Delivery Log screen displays, delivery is created successfully with delivery number shown on tab Deliveries. |  |

|  |
| --- |
| Note With the Analyze Outbound Delivery Logs app you can display an overview about the logs of all delivery creation in system. You can search for logs according to different filter criteria, for example: created by and additional settings. Detailed log information is listed via selecting the arrow on the right of each delivery log entry:If delivery is created successfully, delivery number is shown on Deliveries tab, or, you can display the exact message type, text and also the related sales document on Messages tab . |

##### Create Attachment for Delivery (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create attachment for delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Outbound Delivery (VL03N). | The Display Outbound Delivery: Initial screen displays. |  |
| 3 | Enter Outbound Delivery Number | In the Outbound Delivery field, enter <the outbound delivery number created in previous step> and choose Continue. | The Display Outbound Delivery xxx: Overview screen displays. |  |
| 4 | Create Delivery Attachment | Choose Display < - > Change.Choose Services for Object on the top right corner of screen, and choose Create Attachment. | The Import File screen displays. |  |
| 5 | Import File | Choose OK in the File Upload dialog box.In the Open view, choose local path and file, and choose Open. | The attachment was successfully created. |  |
| 6 | Check Attachment | Choose Services for Object on the top right corner of screen, then choose Attachment List. | Attachment shows up on Service: Attachment List screen. |  |

##### Perform Picking

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
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Open Outbound Delivery Monitor | On the Manage Outbound Deliveries screen, choose For Picking. |  |  |
| 4 | Enter Shipping Point | On the Outbound Deliveries for Picking screen, make the following entries:Shipping Point: <shipping point> for example, 1710 |  |  |
| 5 | Execute | Select the Only Picking without WM checkbox and choose Execute. |  |  |
| 6 | Select the Outbound Delivery | On the Day’s Workload for Picking screen, select your outbound delivery and choose Change Outbound Deliveries. |  |  |
| 7 | Enter Picked Quantity | On the Delivery xxxxxxxx change: Overview screen, choose Picking tab , enter quantity in Picked Qty field.Picking status is set to Completely processed if picked quantity and delivery quantity is equal.Deviations in quantity can be solved by the Copy Picked Quantity as Delivery Quantity function. |  |  |
| 8 | Save Document | Choose Save. |  |  |

##### Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post a goods issue.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). | The Outbound Delivery Monitor screen displays. |  |
| 3 | Open Outbound Delivery Monitor | Choose For Goods Issue.Shipping Point: <shipping point> for example, 1710 |  |  |
| 4 | Post Good Issue | Mark the relevant delivery and choose Post Goods Issue. Select today’s date from the dialog box. Choose Post Goods Issue. | The goods issue is posted |  |

Financial Posting

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 54083000Inv Chg COGS w/CE | 13600000Inventory TradingGd | none |

##### Change Sales Orders (Remove Billing Block)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to remove a billing block from a sales order.

Prerequisite

COGS has been recognized. To recognize revenue in the same month to keep FI and PA in synch, the billing block must be removed manually to process the final invoice.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Search For Sales Order | Enter search term(s) in filter bar, and choose Go:Sales Order: <Sales Order Number> |  |  |
| 4 | Navigate to Sales Order Screen | Select sales order number and choose Changes Sales Orders. | Sales order is displayed in result list. |  |
| 5 | Choose Billing Plan | Select the line item. From the menu, choose More > Goto > Item > Billing Plan.Alternatively, If you assign billing plan on header level: choose More > Goto > Item > Billing Plan . Removal of billing block on header level also unlocks items automatically. | The Change Standard Order xxx: Item Data screen displays. |  |
| 6 | Delete Billing Block | In the Dates section, in the Block column, delete the billing block for the Closing Invoice item. |  |  |
| 7 | Back | Choose Back. |  |  |
| 8 | Save | Save your entries. | The billing block is removed. |  |

##### Create F2 Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to handle the billing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents - VF01 (VF01). | The Create Billing Document screen displays. |  |
| 3 | Maintain Billing Type and Billing Date | Choose billing type Invoice(F2) and maintain billing date, for example, <current date>, enter Sales order Number, then choose Enter. | The draft billing document is created. |  |
| 4 | Save Billing Document | On the Billing Document screen, choose Save.The draft billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx, make a note of the billing document number: __________. | F2 billing document is created. |  |

Financial Postings

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 12100000 Rcvbls Domestic21190000 Down Payments - Customers22000000 Output tax (MWS) | 41000000 Rev Domestic Prod12100000 Rcvbls Domestic21191500 Tax sett.dwn pmt cus22000000 Output tax (MWS) | None |

##### Create Attachment for Billing (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create an attachment for a billing document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Billing Documents (F0797). | The Manage Billing Document screen displays. |  |
| 3 | Search Billing | Make the following entry, and choose Enter:Billing Document: <Billing Document Number Created Previously> |  |  |
| 4 | Choose Billing Number | On the Manage Billing Documents screen, select your billing document created in the previous step, and choose Display. | The Billing Document screen displays. |  |
| 5 | Edit | On the Billing Documents screen, choose Edit. |  |  |
| 6 | Create Billing Attachment | Scroll down and choose Upload in the ATTACHMENTS section. | The Open File screen displays. |  |
| 7 | Import File | In the Open window, select a local path or file and choose Open.Choose Save. | The attachment is successfully created. |  |
| 8 | Check Attachment | In the ATTACHMENTS section, you can see the uploaded document. Choose the document you want to open. |  |  |

##### Create Intercompany IV Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create the intercompany invoice in delivery company code, in background, AP accounting document is generated in ordering company via IDOC.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents - VF01 (VF01). | The Create Billing Document screen displays. |  |
| 3 | Maintain Billing Date | Choose billing type Intercompany Billing (IV) and maintain billing date, for example, <current date>, enter Delivery Number, then choose Enter. |  |  |
| 4 | Save | Choose Save. | IV billing document is created, note down billing document number for further use.Note To check the details of the iDoc generated by the intercompany billing document, you can refer to the section Message Monitor of the Setup Instructions document [Intercompany Sales Order Processing Setup (1HO 1MX 1WO) (SAP Customer)](https://support.sap.com/content/dam/SAAP/SAP_Activate/S4H_489%20Intercompany%20Sales%20Order%20Processing%20%20Setup%20(1HO%201MX%201WO).docx). |  |

Financial Postings

| Material | Debit Accounts | Credit Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 12300000 Company Code 3310 as Business | 41001500 Rev Affiliate- Prod22000000 Output tax (MWS) | None |

##### Display AP Accounting Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display account payable accounting documents generated by IV invoice IDoc.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Journal Entries (F0717A). | The Manage Journal Entries screen displays.Note If app Manage Journal Entries (F0717A) is not there on the Home Page, please search and find it using the magnifier icon. |  |
| 3 | Add the Original Reference Document Field as Filter | Choose Adapt Filters, select Original Reference Document option, and choose OK. | The Original Reference Document field is added as a filter. |  |
| 4 | Filter AP Accounting Document by Referencing IV Invoice | Make the following entry:Original Reference Document: <00 + Intercompany invoice number generated in previous step>Choose Go. | AP accounting document number displays. |  |
| 5 | Display AP Accounting Document | Choose AP accounting number in the Journal Entry column.Choose Display Journal Entries - New Version. | AP accounting document displays. |  |

## Appendix

### Limitations

- Limitations in Foreign Trade
    - ERLA:

Intrastat will be reported on header level. The item categories for subitems should be excluded from Intrastat Reporting This is delivered as set content. An assignment of commodity codes to product on header level is required and an assignment of commodity codes to components is not necessarily required because reporting should happen on header level. If the components in a sales kit have different commodity codes, then the Intrastat Reporting is not correct. Then the customers have to adjust Intrastat Reporting manually in a case like that.

-
    - LUMF:

Intrastat will be reported on component or item level of the sales kit. Therefore item categories for header or mainitem should be excluded from Intrastat Reporting. This is valid for the predelivered content. The assignment of commodity codes to products need to be done for all components, even if all components in a sales kit have the same commodity code and the assignment of commodity codes to product on header level is not necessary. Packaging material in the sales kit from Intrastat Reporting point of view is not supported. In case the customer wants to use packaging material in the BOM, an own item category is needed to be distinguisedh from the Intrastat Perspective. This is how it could be excluded from Intrastat Reporting. Currently this cannot be solved via SSC UIs.

- Limitations in Analytics
    - ERLA:

There is no specific analytics reporting available currently. Header position is relevant for analytics.

-
    - LUMF:

There is no specific analytics reporting available currently. Only subitems are relevant for analytics, no header.

- Limitations in ARM (Acclearated Returns Management) / Returns Management

Sales kits are not supported in customer returns processing because the status handling (update) for the components does not work.

- Limitations for set up of sales kits

Only physical products as part of the sales kits are currently supported (for example, no service products…).

- Limitation in case POD (Proof of Delivery) is used for Sales Kits

There is no automatic quantity correlation done when POD is made via the UI as the pod quantities are entered.

- Limitation in sales inquiry
    - ERLA:

Sales BOM explosion is supported in sales inquiry.

-
    - LUMF:

Sales BOM explosion is supported in sales inquiry.

- Limitation in quantity contract
    - ERLA:

Sales BOM explosion is not supported in quantity contract.

-
    - LUMF:

Sales BOM explosion is supported in quantity contract.

- Limitation in value contract
    - ERLA:

Sales BOM explosion is not supported in value contract.

-
    - LUMF:

Sales BOM explosion is not supported in value contract.

### Statistical Price on Header for LUMF Use Case

From 1902 release, PCUM (Cumulation Condition) condition type can be added as statistical price on header level of a sales BOM of type LUMF in customer pricing procedures. For further information regarding Cumulated Conditions, please refer to SAP Note [844141](https://me.sap.com/notes/844141).

In order to print a billing document with the statistical price shown on the header position, of which the function is enabled by Sales Kits Variant LUMF, refer to this KBA [https://launchpad.support.sap.com/#/notes/2721635](https://launchpad.support.sap.com/#/notes/2721635).

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
> Flagged while digesting this document, not verified: Business condition says to open posting periods in company codes 1010, 1020, 1710 and 1720, while the procedures use company codes 3310/3320/3330 (AE) for domestic and plant 1710 for international.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Domestic 'Create Down Payment Request' says there are five billing settings but lists four; international version says four.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[08-sales-order-management/intercompany-sales-order-processing-domestic-1ho-ae-724]]
- related-to :: [[08-sales-order-management/intercompany-sales-order-processing-international-1mx-ae-741]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1WO_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 207,263 chars in the whole document
