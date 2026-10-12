---
id: 08-sales-order-management/test-script-customer-returns-involving-supplier-by-message-exchange-3q
title: "Test Script: Customer Returns Involving Supplier by Message Exchange (3QD_AE) - SAP S/4HANA Cloud Public Edition (3QD_S4CLD2608_BPD_EN_AE)"
description: "S/4HANA Cloud 2608 test script for scope item 3QD (AE): seller-supplier returns via EDI RMA, refund by credit memo or replacement, with test steps."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/customer-returns-and-refunds]
aliases: [3QD_S4CLD2608_BPD_EN_AE]
keywords: [Customer Returns and Refunds, customer returns, returns order, rma request, edi message exchange, returns purchase order, refund determination, credit memo, replacement delivery, material inspection]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3QD_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-967
topic: 08-sales-order-management/customer-returns-and-refunds
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Customer Returns Involving Supplier by Message Exchange (3QD_AE) - SAP S/4HANA Cloud Public Edition (3QD_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3QD_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Customer Returns and Refunds** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Customer Returns Involving Supplier by Message Exchange (3QD_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232853535)

[2 Prerequisites 4](#_Toc232853536)

[2.1 System Access 4](#_Toc232853537)

[2.2 Roles 4](#_Toc232853538)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232853539)

[2.4 Business Conditions 7](#_Toc232853540)

[2.5 Preliminary Steps 8](#_Toc232853541)

[2.5.1 Create Info Records 8](#_Toc232853542)

[2.5.2 Initialize Material Stock 10](#_Toc232853543)

[2.5.3 Create Condition Rercords (Optional) 11](#_Toc232853544)

[3 Overview Table 12](#_Toc232853545)

[4 Test Procedures 14](#_Toc232853546)

[4.1 Scenario 1: Returned Goods Processing in Seller System 14](#_Toc232853547)

[4.1.1 Create Returns Order 15](#_Toc232853548)

[4.1.2 Perform Picking and Post Goods Receipt 17](#_Toc232853549)

[4.1.3 Perform Material Inspection 18](#_Toc232853550)

[4.1.4 Review Returns Purchase Order 19](#_Toc232853551)

[4.1.5 Send RMA Request via EDI 20](#_Toc232853552)

[4.1.6 Review Returns Order Confirmation 21](#_Toc232853553)

[4.1.7 Return Goods to Supplier via Seller 22](#_Toc232853554)

[4.1.7.1 Create Outbound Delivery 22](#_Toc232853555)

[4.1.7.2 Execute Picking and Post Goods Issue 23](#_Toc232853556)

[4.1.7.3 Display Supplier Invoice 24](#_Toc232853557)

[4.1.8 Determine Refund 26](#_Toc232853558)

[4.1.9 Display Returns Overview 27](#_Toc232853559)

[4.1.10 Refund Customer with Credit Memo (Option A) 28](#_Toc232853560)

[4.1.10.1 Create Credit Memo 28](#_Toc232853561)

[4.1.11 Refund Customer with Replacement Material (Option B) 31](#_Toc232853562)

[4.1.11.1 Create Free-of-Charge Delivery 31](#_Toc232853563)

[4.1.11.2 Execute Picking 32](#_Toc232853564)

[4.1.11.3 Post Goods Issue 33](#_Toc232853565)

[4.1.11.4 Create Pro-forma Invoice 35](#_Toc232853566)

[4.1.11.5 Create Customer Invoice 36](#_Toc232853567)

[4.2 Scenario 2: Returned Goods Processing in Supplier System 38](#_Toc232853568)

[4.2.1 Display and Release Returns Order 38](#_Toc232853569)

[4.2.2 Review Returns Order 40](#_Toc232853570)

[4.2.3 Send Returns Order Confirmation via EDI 41](#_Toc232853571)

[4.2.4 Perform Picking and Post Goods Receipt 41](#_Toc232853572)

[4.2.5 Perform Material Inspection 42](#_Toc232853573)

[4.2.6 Determine Refund 44](#_Toc232853574)

[4.2.7 Display Returns Overview 45](#_Toc232853575)

[4.2.8 Refund Seller with Credit Memo 46](#_Toc232853576)

[4.2.8.1 Create Credit Memo 46](#_Toc232853577)

[4.2.8.2 Send Credit Memo via EDI 48](#_Toc232853578)

[5 Appendix 49](#_Toc232853579)

[5.1 Process Integration 49](#_Toc232853580)

[5.2 Scheduling Job (Alternative) 49](#_Toc232853581)

[5.2.1 Job Scheduling for Delivery Creation (Alternative) 49](#_Toc232853582)

[5.2.2 Job Scheduling for Goods Issue Deliveries (Alternative) 50](#_Toc232853583)

[5.2.3 Job Scheduling for Billing Creation (Alternative) 51](#_Toc232853584)

[5.2.4 Job Scheduling for Billing Release (Alternative) 52](#_Toc232853585)

[5.2.5 Job Scheduling for Billing Output (Alternative) 53](#_Toc232853586)

[5.3 Succeeding Processes 54](#_Toc232853587)

## Purpose

Overview

1.) Seller returning to supplier:

After lean inspection at seller side, a returns purchase order is created to ask for authorization to return goods back to supplier. A return material authorization (RMA) is sent via message exchange to supplier.

If the supplier rejects the RMA, the seller's receiving specialist decides on alternative follow-up actions. Further processing options are according to the customer returns scope item.

If the supplier approves the RMA, the goods are returned to the supplier.

2.) Supplier receiving return request by seller:

The supplier, using message exchange, asks for authorization to return goods to the plant for credit. The RMA request creates a returns order with seller being customer.

The return and refund specialist approves or rejects the RMA and notifies the seller via message exchange.

If approved, the return delivery is automatically created. The goods are inspected after they are received in return stock. Further processing options are according to the customer returns scope item.

If the return and refund specialist decides on paying a credit memo, a corresponding EDI message is sent to the seller.

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
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Returns and Refund Clerk | SAP_BR_RETURNS_REFUND_CLERK | Customer Returns | SAP_BR_RETURNS_REFUND_CLERK |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Receiving Specialist | SAP_BR_RECEIVING_SPECIALIST | Receiving | SAP_BR_RECEIVING_SPECIALIST |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

Seller System

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | TG11 | Trading Good for Reg. Trading (MRP planning)No Serial no.; no batch. |  |
| Material | TG10 | Trad.Good 10,PD,Third PartyTrading Good for regular Trading (MRP planning) with item category group CBORNo Serial no.; no batch. |  |
| Material | TG13 | Trad.Good 13,Reorder Point,Thrd PartyTrading Good for Regular Trading (reorder point planning) with item category group CBNANo batch. |  |
| Sold-to party | 33100003 | Domestic UAE Customer 3 |  |
| Supplier | 33300084 | Inlandslieferant DE (EDI) |  |
| Plant | 3310 |  |  |
| Storage Location | 331A331R |  |  |
| Shipping Point | 3310331R |  |  |
| Sales Organization | 3310 |  |  |
| Distribution Channel | 10 |  |  |
| Division | 00 |  |  |

Supplier System

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | TG11 | Trading Good for Reg. Trading (MRP planning)No Serial no.; no batch. |  |
| Material | TG10 | Trad.Good 10,PD,Third PartyTrading Good for regular Trading (MRP planning) with item category group CBORNo Serial no.; no batch. |  |
| Material | TG13 | Trad.Good 13,Reorder Point,Thrd PartyTrading Good for Regular Trading (reorder point planning) with item category group CBNANo batch. |  |
| Sold-to party | 33100080 | Inlandskunde DE 80 |  |
| Plant | 3310 |  |  |
| Storage Location | 331R |  |  |
| Shipping Point | 331R |  |  |
| Sales Organization | 3310 |  |  |
| Distribution Channel | 10 |  |  |
| Division | 00 |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BND | Create Customer Master - MDS |

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| 2EJ - Integration of Procurement with External Suppliers | To enable EDI data exchange between seller and supplier systems, you have to activate scope item 2EJ and complete all manual configuration steps mentioned in Additional Manual Configuration and Preliminary Steps chapters. |
| 2EL - Integration of Sales with External Buyers | To enable EDI data exchange between seller and supplier systems, you have to activate scope item 2EL and complete all manual configuration steps mentioned in Additional Manual Configuration chapter. |
| To ensure sales process is finished before this scope item is run, choose one from the following test scripts and complete the whole process. |  |
| BD9 - Sell from Stock | Before running this test script, complete all activities in Sell from Stock (BD9) test script in seller system using master data, which is listed in the previous section Master Data, Organization Data and Other Data. Also note down the created document numbers of sales order and billing document for further use. |
| BD3 - Sales Processing using Third-Party with Shipping Notification | Before running this test script, complete all activities in Sales Processing using Third-Party with Shipping Notification (BD3) test script in seller system using master data, which is listed in the previous section Master Data, Organization Data and Other Data. Also note down the created document numbers of sales order and billing document for further use. |
| BDK - Sales Processing Using Third-Party Without Shipping Notification | Before running this test script, complete all activities in Sales Processing using Third-Party without Shipping Notification (BDK) test script in seller system using master data, which is listed in the previous section Master Data, Organization Data and Other Data. Also note down the created document numbers of sales order and billing document for further use. |

### Preliminary Steps

#### Create Info Records

Purpose

This process step shows you how to create info records.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Purchasing Info Records (F1982). | The Manage Purchasing Info Records screen displays. |  |
| 3 | Open New Purchasing Info Records | Choose + on the right corner of the screen, where the mouseover says Create Purchasing Info Record. | The New Purchasing Info Record screen displays. |  |
| 4 | Enter Header Data | Go to Header tab, make the following entries:Info Record Description: <Enter Short Text>Purchasing Organization: 3310Supplier: 33300084Material: TG10Plant: 3310Purchasing Group:001 | Header data is added. |  |
| 5 | Enter General Data | Go to General Information tab, make the following entries:Supplier Material Number: TG11 |  |  |
| 6 | Enter Delivery and Quantity Data | Go to Delivery and Quantity tab, and make the following entries:Delivery Time in Days: <Delivery Time, for example, 1>Under Delivery Tolerance in %: <Under Delivery Tolerance, for example, 10>Over Delivery Tolerance in %: <Over Delivery Tolerance, for example, 10>Tax Code: <Input Tax Code>Order Unit: <Order Unit, for example, PC>Standard Order Quantity: <Standard Order Quantity, for example, 1>On the lower right, and lower left sides of the screen, check the following entry boxes if applicable:Unlimited Delivery: <Checked>Goods-Receipt-Based Invoice Verification: <Unchecked>No Evaluated Receipt Settlement: <Checked>Order Acknowledgment Requirement: <Checked> | Delivery and Quantity data is added. |  |
| 7 | Enter Condition Data | Go to Conditons tab, choose + (Add). Enter the following data:Valid From: <Valid from Date>Amount: 12Pricing Unit: <Pricing Unit, for example,1>Valid to: <Valid to Date>Currency: AEDChoose Apply. | Condition data is added. |  |
| 8 | Save | Choose Save. |  |  |
| 9 | Repeat the Same Steps and Create Two New Info Records | Repeat the same steps and create two new info records with below two sets of master data:Supplier: 33300084, Material: TG11Supplier: 33300084, Material: TG13 |  |  |

Result

The Purchasing info records are created.

#### Initialize Material Stock

Purpose

To run through this scope item, material must be available in stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Stock (F1062). | The Manage Stock screen displays. |  |
| 3 | Enter Movement Type | Make the following entry and choose Enter:Material:TG10,TG11 and TG13Plant: <Plant> | The Stock overview for the material displays. |  |
| 4 | Select Stock | Select the icon beside the stock that you want to add initial stock, for example:Storage Location : Std. storage 1 (331A ) Unrestricted-Use Stock | A dialog box opens. The Storage Location, Stock Type, and Current Quantity are displayed according to your entries in the previous steps. |  |
| 5 | Add Initial Entry | Make the following entries and choose Post:Document Date: <Today>Posting Date: <Today>Stock Change: <Initial Entry>Quantity: <Enter a Number> | The system displays a message: Material document XXX created. The stock has been added. |  |

Financial Postings

| Material | Debited Accounts | Credited Accounts |
| --- | --- | --- |
| Trading Good (HAWA) | 13600000Inventory TradingGd | 39912000Inv Init SF& Fin Bal. |

#### Create Condition Rercords (Optional)

Purpose

In case you have finetuned the access sequence of SAP pre-shipped condition types, the relative condition records should be created accordingly.

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 2: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BET | Create Sales Pricing Condition - MDS |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| Scenario 1: Returned Goods Processing in Seller System |  |  |  |
| [Create Returns Order](#unique_11) [page ] 15 | Returns and Refund Clerk |  |  |
| [Perform Picking and Post Goods Receipt](#unique_12) [page ] 17 | Shipping Specialist | Change Outbound Delivery (VL02N) |  |
| [Perform Material Inspection](#unique_13) [page ] 18 | Receiving Specialist | Enter Inspection Results - From Warehouse (MSR_INSPWH) |  |
| [Review Returns Purchase Order](#unique_14) [page ] 19 | Purchaser | Manage Purchase Orders (F0842A) |  |
| [Send RMA Request via EDI](#unique_15) [page ] 20 |  |  |  |
| [Review Returns Order Confirmation](#unique_16) [page ] 21 | Purchaser | Manage Purchase Orders (F0842A) |  |
| [Return Goods to Supplier via Seller](#unique_17) [page ] 22 |  |  |  |
| [Create Outbound Delivery](#unique_18) [page ] 22 | Shipping Specialist | My Purchase Orders - Due for Delivery (VL10B) |  |
| [Execute Picking and Post Goods Issue](#unique_19) [page ] 23 | Shipping Specialist | Change Outbound Delivery (VL02N) |  |
| [Display Supplier Invoice](#unique_20) [page ] 24 | Accounts Payable Accountant | Supplier Invoices List (F1060A) |  |
| [Determine Refund](#unique_21) [page ] 26 | Returns and Refund Clerk |  |  |
| [Display Returns Overview](#unique_22) [page ] 27 | Returns and Refund Clerk |  |  |
| Refund Customer with Credit Memo (Option A) |  |  |  |
| [Create Credit Memo](#unique_23) [page ] 28 | Billing Clerk | Create Billing Documents (F0798) |  |
| Refund Customer with Replacement Product (Option B) |  |  |  |
| [Create Free-of-Charge Delivery](#unique_24) [page ] 31 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) |  |
| [Execute Picking](#unique_25) [page ] 32 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) |  |
| [Post Goods Issue](#unique_26) [page ] 33 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) |  |
| [Create Pro-forma Invoice](#unique_27) [page ] 35 | Billing Clerk | Create Billing Documents (F0798) |  |
| [Create Customer Invoice](#unique_28) [page ] 36 | Billing Clerk | Create Billing Documents (F0798) |  |
| Scenario 2: Returned Goods Processing in Supplier System |  |  |  |
| [Display and Release Returns Order](#unique_29) [page ] 38 | Returns and Refund Clerk |  |  |
| [Review Returns Order](#unique_30) [page ] 40 | Returns and Refund Clerk |  |  |
| [Send Returns Order Confirmation via EDI](#unique_31) [page ] 41 |  |  |  |
| [Perform Picking and Post Goods Receipt](#unique_32) [page ] 41 | Shipping Specialist | Change Outbound Delivery (VL02N) |  |
| [Perform Material Inspection](#unique_33) [page ] 42 | Receiving Specialist | Enter Inspection Results - From Warehouse (MSR_INSPWH) |  |
| [Determine Refund](#unique_34) [page ] 44 | Returns and Refund Clerk |  |  |
| [Display Returns Overview](#unique_35) [page ] 45 | Returns and Refund Clerk |  |  |
| Refund Seller with Credit Memo |  |  |  |
| [Create Credit Memo](#unique_36) [page ] 46 | Billing Clerk | Create Billing Documents (F0798) |  |
| [Send Credit Memo via EDI](#unique_37) [page ] 48 |  |  |  |

## Test Procedures

The test should take around, for example, 60 minutes. The Enterprise Search function provides a central entry point for finding business objects in your company from different sources using a single search request, such as: apps, fact sheets for business objects. From the data found, you can go directly to the respective apps and fact sheets to display, edit the data or find related objects.

How to access and check a fact sheet:

- Log on to the SAP Fiori launchpad using the respective user, for example, Internal Sales Representative.
- Access the Enterprise Search bar and choose the magnifying glass button in the upper right corner.
- The Enterprise Search bar displays, two filter fields appear left to the search button. Enter your search criteria and choose the business object type, example: Customer Returns from dropdown menu in first field, enter customer returns order number in second field and choose Search, The sales order is listed.
- Choose the sales order number link, the system navigates to fact sheet screen and returns order-related information is integrated and summarized in one Fiori page. You can get detailed data via choosing the corresponding links.

There are fact sheets available for the following objects (visible depending on the assigned role):

- Sales (Return) Order
- Quotation
- Billing Document
- Credit Memo
- Debit Memo
- Customer 360 Fact sheet

This section describes test procedures for each process step that belongs to this scope item.

### Scenario 1: Returned Goods Processing in Seller System

|  |
| --- |
| Note To ensure supplier return is carried out using shipping processing, below data need to be maintained correctly before creating returns order. |

| Business Role ID | App | Instructions | Expected Result |
| --- | --- | --- | --- |
| SAP_BR_BUPA_MASTER_SPECIALIST | Maintain Business Partner (BP) | Open BP 33300084 with BP role FLVN01 Supplier (defined), switch to Purchasing > Purchasing Data tab, in Additional Purchasing Data sub-area, set flag in checkbox Returns supplier. For details, please refer to Enabling Supplier Master Data for Return and Shipping Processing in test script 2EJ - Integration of Procurement with External Suppliers. | Set flag Returns supplier in supplier master data. |
| SAP_BR_BPC_EXPERT | Manage Your Solution (F1241) | Maintain correct relationship between plant and sales organization / distribution channel via SSCUI 101926 or activity Define Shipping Data for Plants as below:Plant: 3310Sales Organization: 3310Distribution Channel: 10 | Sales organization and distribution channel are assigned to the plant. |

#### Create Returns Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a returns order.

Prerequisites

You must have billing document or sales order as reference (refer to Business Conditions chapter).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Returns and Refund Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer Returns - Version 2 (F4832). |  |  |
| 3 | Create Returns Order with Reference to Billing | Choose Create with Reference then choose Create from Invoice. | The Create from Invoice dialog box displays. |  |
| 4 | Reference Document Data | Enter the following data and choose Select Items:Returns Order Type:Standard Return (CBAR)Invoice: <Billing document number created previously> |  |  |
| 5 | Maintain Returned Quantity | Select the item(s) to be returned and enter your quantity, then choose Continue. | New: Returns Order screen displays. |  |
| 6 | Enter Data | On General Information tab, enter the following data:Return Order Reason: for example, Standard Return (009)Under the Items tab, choose the arrow button at the end of the item, and enter the following data:Return Reason: for example, product damaged (003)Follow-up Activity: Ship to Supplier (0005)Supplier: <enter Supplier>, for example, 33300084 |  |  |

The user can influence the point in time when the refunding document is created: either immediately when the returns order is saved and released, or at a later point of time. Combination of the refund setting determines follow-up document creation. System provides four options for your reference. Choose one of the following options to continue:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 1 | Option 1: Execute Refund with Credit Memo Request Immediately | On Refund sub-area, enter the following data or action then choose Apply:Refund Type: <Credit Memo>Refund Code: <select one from down-drop list>, for example, 100%.Refund Control: Create Credit Memo RequestChoose Save and Release. | Returns order is released.Returns delivery and credit memo request are generated automatically. |  |
| 2 | Option 2: Execute Refund with Replacement Order Immediately | On Refund sub-area, enter the following data or action then choose Apply:Refund Type: <Replacement Product>Refund Control: Create Replacement OrderChoose Save and Release. | Returns order is released.Returns delivery and replacement order are generated automatically. |  |
| 3 | Option 3: Refund on Hold, Choose Credit Memo as Temporary Refund Type | On Refund sub-area, enter the following data or action then choose Apply:Refund Type: Credit MemoRefund Code: <Select one from down-drop list>, for example, 10%.Refund Control: Decide LaterChoose Save and Release. | Returns order is released.Returns delivery is generated automatically. |  |
| 4 | Option 4: Refund on Hold, Choose Replacement Product as Temporary Refund Type | On Refund sub-area, enter the following data or action then choose Apply:Refund Type: Replacement ProductRefund Control: Decide LaterChoose Save and Release. | Returns order is released.Returns delivery is generated automatically. |  |
| 5 | Check Process Flow | On the Manage Customer Returns (F1708) screen, choose arrow at end of the item.In the Process Flow tab, check dependent documents in process flow. Make a note of the follow-up document numbers for further use. | The Display Returns Order screen displays. |  |

If freight was maintained in previous delivery document header, and material was partly returned regarding billing document, kindly check (or change if necessary) freight amount for YBHD condition type in the headers of returns order (and credit memo request document if it is generated automatically) using the role of Sales Representative (SAP_BR_INTERNAL_SALES_REP) and the Change Sales Order tile. If requested delivery date is reached and delivery document has not been created, warning information delivery issue shows in the process flow as a reminder. Once delivery document is generated later, such alert disappears.

#### Perform Picking and Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to perform picking and post goods receipt in stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). | The Change Outbound Delivery (VL02N) screen displays. |  |
| 3 | Enter Delivery Number | On the Change Outbound Delivery (VL02N) screen, make the following entry and choose Enter.Outbound Delivery: Enter the outbound delivery number that created in last chapter [Create Returns Order](#unique_11) [page ] 15. | The Std Returns Delivery XXXXXXXX Change: Overview screen displays. |  |
| 4 | Enter Picking Data | On the Std. Returns Delivery XXXXXXXX Change: Overview screen, choose the Picking tab, make the following entries:Picked quantity: <Equal to Delivery quantity> | C (Fully Picked) displays in theOvrllPickStatus field. |  |
| 5 | Post Goods Receipt | Choose Post Goods Receipt. | Std.Returns Delivery 8XXXXXXX has been saved. |  |

#### Perform Material Inspection

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to perform material inspection after the warehouse received the returned goods, while the further handling of the returned goods is decided.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Receiving Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Enter Inspection Results - From Warehouse (MSR_INSPWH). | The Worklist Selection of Deliveries screen displays. |  |
| 3 | Maintain Selection Criteria | Enter the following entries and choose Execute:Delivery Items Waiting for Inspection: <select>Delivery: <enter returns delivery number> | The Change: Material Inspection in Warehouse for Delivery screen displays. |  |
| 4 | Item | Choose Item. |  |  |
| 5 | Maintain Inspection Result | In the Inspection Result subarea, enter the following data and press Enter:Inspection Code: <enter inspection code>Inspected Quantity: <enter inspected quantity>If the Confirmation of Redetermination dialog box appears, choose Yes to confirm. |  |  |
| 6 | Check Follow-up Activity | In the Logistical Follow-Up subarea, make sure the following data is entered:Follow-Up Activity: 0005 Ship to SupplierSupplier : <enter Supplier>, for example, 33300084 |  |  |
| 7 | Check Inspection Status | On the Header tab, in the Basic Data subarea, Inspection Status shows Inspected, which means all received materials are inspected completely. | All received materials are inspected completely. |  |
| 8 | Save and Confirm | Choose Save and Confirm on the top menu bar. | Inspection result is recorded, returns purchase order is created, RMA request is sent to supplier system automatically. |  |
| 9 | Record Returns Purchase Order Number | Choose Returns Overview. | In Returns Steps section, returns purchase order 45XXXXXXXX displays in Document Number column. |  |

#### Review Returns Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to preview returns purchase order and check EDI relevant output entry.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Purchase Orders (F0842A). | The Manage Purchase Orders screen displays.A list of already created purchase orders displays. |  |
| 3 | Select Returns purchase order | Enter the following selection criteria in filter bar and choose Go:Purchase Order: <returns purchase order number created previously>Choose the arrow at the end of returns purchase order entry. | Display Purchase Order screen displays. |  |
| 4 | Choose Message | Choose Messages on top menu bar. | Display Pur. Order: Ouput screen displays. |  |
| 5 | Check EDI Output Entry | In Output section, the entry with the following fields displays:Status: CompletedOutput Type: PURCHASE_ORDERChannel: EDI |  |  |

#### Send RMA Request via EDI

Purpose

A RMA request is automatically sent to the supplier system via EDI message.

Prerequisites

Returns purchase order is generated.

Procedure

This step is automatically generated.

#### Review Returns Order Confirmation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to review returns order confirmation.

|  |
| --- |
| Note The following test steps can be processed only after the corresponding supplier system has sent an order confirmation. For details, kindly refer to chapter [Display and Release Returns Order](#unique_29) [page ] 38 and [Send Returns Order Confirmation via EDI](#unique_31) [page ] 41. |

Prerequisite

Supplier approved or rejected the RMA request from the seller side. For details, refer to [Display and Release Returns Order](#unique_29) [page ] 38 chapter.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Purchase Orders (F0842A). | The Manage Purchase Orders screen displays. |  |
| 3 | Select Returns Purchase Order | Enter returns purchase order number in the Purchase Order search box, and choose Go. Select the row for the Purchase Order you want to preview and use the little arrow on the right side to enter the PO detail. | The Display Purchase Order screen displays. |  |
| 4 | Check Returns Purchase Order details | Expand Item Detail, check data on Confirmations tab and Returns tab. | The returns purchase order details are checked. |  |
| 5 | Choose One of the Following Options | After supplier releases returns order, choose one of the following options to check updated fields in returns purchase order. |  |  |
| 5a | Option 1: Supplier Approved RMA Request | In the Item Detail section, check the following updated fields:Confirmations tabOrder Ack.: 6XXXXXXX (Returns order generated in supplier system)Returns tabSupplier RMA Number: 6XXXXXXX-000010 (RMA number generated in supplier system) | Key fields are updated in returns purchase order according to the supplier’s decision.If RMA request is rejected by the supplier, execute the following chapters in Scenario 1:Returned Goods Processing in Seller System:[Perform Material Inspection](#unique_13) [page ] 18[Determine Refund](#unique_21) [page ] 26Refund Customer with Credit Memo orRefund Customer with Replacement MaterialElse, complete all subsequent chapters. |  |
| 5b | Option 2: Supplier Rejected RMA Request | In the Item Overview section, Deletion icon is marked in the item.In the Item Detail section, Check the following updated fields:Confirmations tabOrder Ack.: 6XXXXXXX (Returns order generated in supplier system)Returns tabSupplier Rejection Reason: Same to the one chosen in chapter [Display and Release Returns Order](#unique_29) [page ] 38 in supplier system | Key fields are updated in returns purchase order according to the supplier’s decision.If RMA request is rejected by the supplier, execute the following chapters in Scenario 1:Returned Goods Processing in Seller System:[Perform Material Inspection](#unique_13) [page ] 18[Determine Refund](#unique_21) [page ] 26Refund Customer with Credit Memo orRefund Customer with Replacement MaterialElse, complete all subsequent chapters. |  |

#### Return Goods to Supplier via Seller

This section can be processed only after supplier approves the return request.

##### Create Outbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

Reurn request is approved by the supplier.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open My Purchase Orders - Due for Delivery (VL10B). | The Purchase Orders, Fast Display screen displays. |  |
| 3 | Enter Data | In the head area:Shipping Point: 3310Delivery Creation Dates (From): <delivery creation From date> Delete the default dateDelivery Creation Dates (To) <delivery creation To date> Delete the default dateCalc Rule: <calculation rule>, for example, 2.Go to the Purchase Orders tab and make the following entries then choose Execute:Purchasing Document: Enter the returned purchase order that created in chapter Perform Material Inspection. | Activities Due for Shipping "Purchase Orders, Fast Display" screen displays. PO due for delivery is listed. |  |
| 4 | Create A Delivery | Select the line of purchase order from the list.Choose Background to create delivery in Background. | Activities Due for Shipping "Purchase Orders, Fast Display" screen displays. |  |
| 5 | Check Delivery Number | Choose More > Show/Hide Delivery, and note down the returns delivery number shown in the Document field. | A returns delivery is created. |  |

##### Execute Picking and Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to perform picking, to ship retuned material back to the supplier, and to post a goods issue.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). | The Change Outbound Delivery (VL02N) screen displays. |  |
| 3 | Enter Delivery Number | On the Change Outbound Delivery (VL02N) screen, make the following entry and choose Enter.Outbound Delivery: Enter the Outbound Delivery number that created in last chapter: Create Outbound Delivery. | The RTS Outbound Dlv. XXXXXXXX Change: Overview screen displays. |  |
| 4 | Enter Picking Data | On the RTS Outbound Dlv. XXXXXXXX Change: Overview screen, choose the Picking tab, make the following entries:Picked quantity: <picked quantity>Choose Save . | The system shows the message: Returns Delivery xxxxxxxx has been saved. The screen return to Change Outbound Delivery (VL02N) screen. |  |
| 5 | Post Goods Issue | On the Change Outbound Delivery (VL02N) screen, choose Post Goods Issue. | Returns (Pur.Ord.) 8XXXXXXX is saved. |  |

##### Display Supplier Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, the supplier credit memo displays.

Prerequisites

Credit memo is created in supplier system, EDI message is sent accordingly. For details, refer to chapter Create Credit Memo in Scenario 2: Returned Goods Processing in Supplier System.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Supplier Invoices List (F1060A). | The Supplier Invoices List screen displays. |  |
| 3 | Search for Supplier Credit Memo | Enter selection criteria in the Filter Bar and choose Go. For example:Reference: <SD credit memo number created in chapter Create Credit Memo in Scenario 2: Returned Goods Processing in Supplier System>. | The supplier credit memo created automatically via EDI displays in Invoice section. |  |
| 4 | Navigate to Supplier Details | Choose the arrow at the end of credit memo row. | If the returned material is refunded fully by supplier, supplier invoice is posted auto-matically, Supplier Invoice screen displays.Else, post supplier invoice manually with the following steps. |  |
| 5 | Display Supplier Invoice | Open Display Supplier Invoice - Advanced (MIR4), enter the created invoice document number and fiscal year, and choose Display Document.Choose Menu > Edit > Display/Change (F7) on top of the menu bar. | Change Invoice Document displays. |  |
| 6 | Post Invoice Manually | On PO Reference tab, maintain the following data and choose Post:Amount: <Net value>Quantity: <Refund quantity>Correctn ID: No error | Supplier invoice is posted manually. |  |

#### Determine Refund

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to make or check a refund decision. You can either refund the customer with a credit memo or compensate the customer with replacement product.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Returns and Refund Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer Returns - Version 2 (F4832). | The Manage Customer Returns - Version 2 screen displays. |  |
| 3 | Search for Returns Order | Choose Show Filter Bar if it is hidden. Enter the following data and choose Go:Returns Order : <returns order number 6XXXXXXX> | Returns order is found and displayed. |  |
| 4 | Navigate to Determine Refund Screen | Select returns order entry and choose Determine Refund. | The Determine Refund screen displays. |  |
| 5 | Check Refund Progress | In the upper area, check percentage number in the field Refund Progress and then take next action accordingly:<100%: Refund determination is not completed. Go to Section A and then Section B.100%: Refund determination is completed. Skip Section A and go to Section B. |  |  |
| Section A: Refund is Determined with Reference to Material Inspection Results | Option 1: Credit Memo | On the Items to Be Refunded tab, choose Change Refund in the Refund Details column for the return item.Enter the following data:Refund Type: Credit MemoRefund Code: <a percentage number>, for example, 10% RefundChoose OK.Select the item and choose Release Selected Items. | Refund setting is maintained, and credit memo request document is created in background. |  |
| Section A: Refund is Determined with Reference to Material Inspection Results | Option 2: Product Replacement | On the Items to Be Refunded tab, choose Change Refund in Refund Details column for the return item.Enter the following data:Refund Type: Replacement productReplacement Product: <Material>Supplying Plant: 3310Replacement Quantity: <Quantity> / PCChoose OK.Select the item and choose Release Selected Items.Note If supplier directly sends replacement product to customer as compensation, choose No Refund in the Refund Type field, then perform Sales Processing Using Third-Party Without Shipping Notification (BDK) test script. | Refund setting is maintained, and replacement order document is created in background. |  |
| Section B: Check Refund Determination Result | Check Refund Results | On the Completed Items tab, refund result is displayed. The follow-up document number is shown in the Refund Details column.Make a note of document number for further use. You can choose the created document number to check detailed information. | The refund result displays. |  |

#### Display Returns Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check the progress of return process. You may check all dependent documents are available in process flow.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Returns and Refund Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer Returns - Version 2 (F4832). | The Manage Customer Returns - Version 2 screen displays. |  |
| 3 | Search for Returns Order | Choose Show Filter Bar if it is hidden. Enter the following data and choose Go:Returns Order: <returns order number 6XXXXXXX> | Returns order is found and displayed. |  |
| 4 | Navigate to Order Overview Screen | Click the created return sales order number 6XXXXXXX and choose Display Returns Order. | The Display Standard Return 6XXXXXXX: Overview screen displays. |  |
| 5 | Navigate to Document Flow Screen | On Returns tab, choose Returns Overview in Returns Control area. | The Returns Overview for Returns Order 6XXXXXXX - 10 screen displays. |  |
| 6 | Check Document Flow | In Document Number column, make a note of follow-up document number for further use:Credit memo request or replacement order (subsequent delivery free of charge) :<number> |  |  |

After you have completed this activity, choose option A or option B:

Option A: If credit memo request is generated, go to the Refund Customer with Credit Memo chapter.

Option B: If replacement order is generated, go to the Refund Customer with Replacement Material chapter.

#### Refund Customer with Credit Memo (Option A)

##### Create Credit Memo

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a credit memo.

Procedure

Create Billing Document.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Document screen displays. |  |
| 3 | Define Billing Setting | Choose Billing Settings in the bottom bar, keep the settings as below:Set Billing Date and type before billing: ONCreate Separate billing document for each item of billing due list: ONAutomatically Post Billing Documents: ONDisplay Billing Document after creation: ONChoose delivery items to be billed and select quantities: OFF |  |  |
| 4 | Search for Billing List | In the search condition, enter criteria if necessary. | SD documents display in the result. |  |
| 5 | Choose SD Document | Select the row of credit memo request document recorded previously and choose Create. | The Create Billing Documents (F0798) screen displays. |  |
| 6 | Maintain Billing Type and Billing Date | Choose billing type Credit Memo (G2) and maintain billing date, such as the current date, and then choose OK. | The draft billing document with ID Sxxxxxxxx displays. |  |
| 7 | Save Billing Document | On the Billing Document screen, choose Save. The draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx. Make a note of the billing document number: __________. | Final credit memo is generated. |  |

Financial Postings

| Material | Debited Accounts | Credited Accounts |
| --- | --- | --- |
| Trading Good (HAWA) | 44002000Sales Disc Domestic | 41000000Rev Domestic Prod |

Manage Billing Documents

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access the App | Open Manage Billing Documents (F0797). | The Manage Billing Documents (F0797) screen displays. |  |
| 2 | Search for the Billing Document | Enter the billing document number recorded previously in the Billing Document field, and press Enter. | The billing document which is created previously displays. |  |
| 3 | Display the Billing Document | Select the billing document item, and choose Display. | The billing document displays. |  |
| 4 | Check Output Condition | On the Billing Document screen, go to the last assignment block, Output Items. | There is one entry in the item and the output type is BILLING_DOCUMENT. |  |
| 5 | Display Print Preview | On the Billing Document screen, choose Preview. | Preview for PDF document displays. |  |
| 6 | Cancel Billing Document (Optional) | On the Billing Document screen, select a certain billing document and choose Cancel Billing Document. | A log displays the following message: Billing Document Canceled. |  |
| 7 | Update New Attachment (Optional) | In the Edit mode, you can add, delete, and update the attachments. Save your changes by choosing Save in the footer bar. |  |  |
| 8 | Update New Text (Optional) | In the Edit mode, you can add, delete, and update the texts. Save your changes by choosing Save in the footer bar. |  |  |

#### Refund Customer with Replacement Material (Option B)

##### Create Free-of-Charge Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a free-of-charge replacement delivery with reference to replacement order.

Prerequisite

Replacement order is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open the Create Outbound Deliveries - From Sales Orders (F0869A) . | The Create Outbound Deliveries-From Sales Orders screen displays. |  |
| 3 | Search Sales Order | Make the following entries and choose Continue:Shipping point:3310Planned Creation Date: <Delivery selection date>Order: <Replacement order number created previously> |  |  |
| 4 | Create Delivery | Select your items and choose Create Deliveries. | Delivery is created with a number ______________ |  |
| 5 | Check Details | Choose Display Log. | The Analyze Delivery Log screen displays. Delivery is created successfully with delivery number shown on the Deliveries tab. |  |

##### Execute Picking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The picking process involves taking goods from a storage location and staging the right quantity in a picking area where the goods are prepared for shipping. This process step shows you how to perform picking.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). | The Manage Outbound Deliveries screen displays. |  |
| 3 | Choose Picking | Choose For Picking. |  |  |
| 4 | Enter Shipping Point | Make the following entries and choose Execute:Shipping Point: for example, 331ROnly Picking without WM: <select the checkbox> |  |  |
| 5 | Change Outbound Deliveries | On the Day's Workload for Picking screen, select your delivery number and choose Change Outbound Deliveries. |  |  |
| 6 | Enter Picked Quantity | On the Picking tab, input quantity equal to delivery quantity in the Picked Qty field. |  |  |
| 7 | Choose Enter | Choose Enter. |  |  |
| 8 | Save | Choose Save. | The delivery has been picked. |  |

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
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Shipping Specialist. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). | The Manage Outbound Deliveries screen displays. |  |
| 3 | Choose Good Issue | Choose For Goods Issue. |  |  |
| 4 | Enter Shipping Point | Make the following entries and choose Execute:Shipping Point: 3310 |  |  |
| 5 | Post Goods Issue | Mark the relevant delivery and choose Post Goods Issue. Select today’s date and choose Continue in the dialog box. | The goods issue is posted |  |

Financial Postings

| Material | Debited Account | Credited Account | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 54083000Inv Chg COGS w/CE | 13600000Inventory TradingGd | none |

Printing Form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Outbound Delivery (VL03N). | The Display Outbound Delivery (VL03N) screen displays. |  |
| 3 | Issue Delivery Output | On the Display Outbound Delivery (VL03N) screen, enter the Delivery number and choose Continue. From the Delivery xxxxxxxx Display: Overview screen, choose Menu > Extras > Delivery Output > Output Control | The Delivery: Output screen displays. |  |
| 4 | Print Preview | On the Delivery: Output screen, select the line with the Output Type Delivery Note and choose Display PDF Document. | A preview of the print document displays. |  |
| 5 | Print Delivery Note | From the preview of the document, choose Print. | The delivery note is posted. |  |

##### Create Pro-forma Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a pro-forma invoice with reference to delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Documents (F0798) screen displays. |  |
| 3 | Define Billing Setting | Choose Billing Settings in the bottom bar, keep the settings as below:Set Billing Date and type before billing: ONCreate Separate billing document for each item of billing due list: ONAutomatically Post Billing Documents: ONDisplay Billing Document after creation: ONChoose delivery items to be billed and select quantities: OFF |  |  |
| 4 | Search for Billing List | In the search condition, use criteria if necessary. | Sales documents displays in the result. |  |
| 5 | Choose Individual Billing Document | Select the row of delivery document created previously and choose Create. |  |  |
| 6 | Maintain Billing Type and Billing Date | Choose the billing type Invoice (F8) and billing date, such as the current date, then choose OK. | The draft billing document with ID Sxxxxxxxx displays. |  |
| 7 | Save Billing Document | In the Billing Document screen, choose Save. The draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx. Make a note of the billing document number: __________. | Pro-forma invoice is generated. |  |

Alternatively, it is supported to create pro-forma (type F5) with reference to replacement order.

Manage Billing Documents

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the App | Open Manage Billing Documents (F0797). | The Manage Billing Document screen displays. |  |
| 2 | Search the Billing DocumentCreated in Previous Step | Input the pro-forma invoice number recorded in the previous step.Press Enter. | The billing document created in the previous step displays. |  |
| 3 | Display the Billing Document | Select the billing document item and choose Display. | The billing document displays. |  |
| 4 | Check Output Condition | On the Billing Document screen, choose the last assignment block, Output Items. | There is one entry in the item and the output type is BILLING_DOCUMENT. |  |
| 5 | Display Print Preview | On the Billing Document screen, choose Preview. | Preview for PDF document displays. |  |
| 6 | Update New Attachment (Optional) | In the Edit mode, you can add, delete, and update the attachments. Choose Save to save your changes in the footer bar. |  |  |
| 7 | Update New Text (optional) | In the Edit mode, you can add, delete, and update these texts. Choose Save to save your changes in the footer bar. |  |  |

##### Create Customer Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, ‘F2’ type of invoice is created, and costs are transferred to accounting accordingly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Documents (F0798) screen displays. |  |
| 3 | Define Billing Setting | Choose Billing Settings in the bottom bar, keep the settings as below:Set Billing Date and type before billing: ONCreate Separate billing document for each item of billing due list: ONAutomatically Post Billing Documents: ONDisplay Billing Document after creation: ONChoose delivery items to be billed and select quantities: OFF |  |  |
| 4 | Search for Billing List | In the search condition, use criteria if necessary. | Sales documents displays in the result. |  |
| 5 | Choose Individual Billing Document | Select the row of delivery document created previously and choose Create. |  |  |
| 6 | Maintain Billing Type and Billing Date | Choose billing type Invoice (F2) and maintain Billing date, such as the current date, and then choose OK. | The draft billing document with ID Sxxxxxxxx displays. |  |
| 7 | Save Billing Document | On the Billing Document screen, choose Save. The draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx. Make a note of the billing document number: __________. | Customer invoice is generated. |  |

Financial Postings

| Material | Debited Accounts | Credited Accounts |
| --- | --- | --- |
| Trading Good (HAWA) | 44002000Sales Disc Domestic | 41000000Rev Domestic Prod |

Manage Billing Documents

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the App | Open Manage Billing Documents (F0797). | The Manage Billing Document screen displays. |  |
| 2 | Search the Billing Document Created in Previous Step | Input the pro-forma invoice number recorded in the previous step.Press Enter. | The billing document created in the previous step displays. |  |
| 3 | Display the Billing Document | Select the billing document item and choose Display. | The billing document displays. |  |
| 4 | Check Output Condition | On the Billing Document screen, choose the last assignment block, Output Items. | There is one entry in the item and the output type is BILLING_DOCUMENT. |  |
| 5 | Display Print Preview | On the Billing Document screen, choose Preview. | Preview for PDF document displays. |  |
| 6 | Cancel Billing Document (Optional) | Select certain billing document and choose Cancel Billing Docs. | Log displayed: Billing Document Canceled. |  |
| 7 | Update New Attachment (optional) | In the Edit mode, you can add, delete, and update the attachments. Choose Save to save your changes in the footer bar. |  |  |
| 8 | Update New Text (optional) | In the Edit mode, you can add, delete, and update these texts. Choose Save to save your changes in the footer bar. |  |  |

### Scenario 2: Returned Goods Processing in Supplier System

#### Display and Release Returns Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display returns order generated via EDI in supplier system.

Prerequisite

Returns purchase order is created and RMA request via EDI message is sent successfully in seller system. For details, refer to Perform Material Inspection chapter in Scenario 1: Returned Goods Processing in Seller System.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Returns and Refund Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer Returns - Version 2 (F4832). | The Manage Customer Returns - Version 2 screen displays. |  |
| 3 | Search for Returns Order | Enter the following data and choose Go:Customer Reference: <returns purchase order number 45XXXXXX noted down in Perform Material Inspection chapter> | Returns order is found and displayed. |  |
| 4 | Order Overview | Choose the arrow at the end of returns order row. | The Display Returns Order screen displays. |  |
| 5 | Edit Returns Order | Choose Edit. | The Edit Returns Order screen displays. |  |
| 6 | Choose One of the Following Options | You can approve or reject the returns order. |  |  |
| 6a | Option 1: Approve Returns Order, Refund Immediately | Under the Item tab, choose the arrow at the end of item. In Refund section, enter the following data and choose Apply:Refund Type: Credit MemoRefund Code: <select one from down-drop list>, for example, 100%.Refund Control: Create Credit Memo RequestChoose Save and Release. | Returns order is released and approved.Returns delivery and credit memo request are generated automatically. |  |
| 6b | Option 2: Approve Returns Order, Refund Later | Under the Item tab, choose the arrow at the end of item. In Refund section, enter the following data and choose Apply:Refund Control: Decide LaterChoose Save and Release. | Returns order is released and approved. |  |
| 6c | Option 3: Reject Returns Order | Under Items tab, select the item(s) and choose Rejection Reason, then choose Set Rejection Reason.Choose one from dropdown list and choose Set Rejection Reason, for example:Reason for Rejection: Other Compensation (58)Choose Save and Release. | Reurns order is released and rejected. |  |

#### Review Returns Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to preview returns order and check EDI relevant output entry.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Returns and Refund Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer Returns - Version 2 (F4832). | The Manage Customer Returns - Version 2 screen displays. |  |
| 3 | Search for Returns Order | Enter the following data and choose Go:Customer Reference: <returns purchase order number 45XXXXXX noted down in chapter Perform Material Inspection in Scenario 1:Returned Goods Processing in Seller System >Choose returns order number and click Display Customer Return in dialog box. | Display Standard Return XXXX: Overview screen displays. |  |
| 4 | Choose Header Output Preview | Choose Header Output Preview on top menu bar. | Display Standard Return XXXX: Output screen displays. |  |
| 5 | Check EDI Output Entry | In Output section, the entry with the following fields displays:Status: CompletedOutput Type: CUSTOMER_RETURNChannel: EDI |  |  |

#### Send Returns Order Confirmation via EDI

Purpose

A returns order confirmation is automatically sent to the seller system via EDI message.

Prerequisites

Returns order must have been released in supplier system.

Procedure

This step is automatically generated.

#### Perform Picking and Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After returned goods physically arrive in warehouse, execute picking for returns delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). | The Change Outbound Delivery (VL02N) screen displays. |  |
| 3 | Enter Delivery Number | On the Change Outbound Delivery (VL02N) screen, make the following entry and choose Enter.Outbound Delivery: Enter the outbound delivery number that you created in chapter [Display and Release Returns Order](#unique_29) [page ] 38. | The Returns (Pur. Ord.) XXXXXXXX Change: Overview screen displays. |  |
| 4 | Enter Picking Data | On the Std. Returns Delivery XXXXXXXX Change: Overview screen, choose the Picking tab, make the following entries:Picked quantity: <Equal to Delivery quantity> | C (Fully Picked) displays in theOvrllPickStatus field. |  |
| 5 | Post Goods Receipt | Choose Post Goods Receipt. | Picking and goods receipt are post for returns delivery 8XXXXXXX. |  |

#### Perform Material Inspection

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The material inspection takes place after the returned goods have been received in the warehouse. The further handling of the returned goods is decided. This process step shows you how to perform material inspection.

Prerequisite

The returned goods are received.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Receiving Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Enter Inspection Results - From Warehouse (MSR_INSPWH). | The Worklist Selection of Deliveries screen displays. |  |
| 3 | Maintain Selection Criteria | Enter the following entries and choose Execute:Delivery Items Waiting for Inspection: <select>Delivery: <enter returns delivery number> | The Change: Material Inspection in Warehouse for Delivery screen displays. |  |
| 4 | Choose Item tab | Choose Item tab. |  |  |
| 5 | Maintain Inspection Result | In the Inspection Result subarea, enter the following data, and press Enter:Inspection Code: <enter inspection code>Inspected Quantity: <enter inspected quantity>If the Confirmation of Redetermination dialog box appears, choose Yes to confirm. |  |  |
| 6 | Maintain Follow-up Activity | In the Logistical Follow-up subarea, enter the following data and press Enter:Follow-up Activity: <enter follow-up activity>Note Choose appropriate follow-up activity according to inspection code. For example, choose follow-up activity Transfer to Free Available Stock responding to inspection code 0001. |  |  |
| 7 | Check Inspection Status | On the Header tab, in the Basic Data subarea, Inspection Status shows Inspected, which means all received materials are inspected completely. | All received materials are inspected completely. |  |
| 8 | Save and Confirm | Choose Save and Confirm. | Inspection result is recorded, and goods movement is posted accordingly. |  |

#### Determine Refund

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, refund decision is made or checked: either refund the customer with a credit memo or compensate with a replacement product . For Repair business, you may choose No Refund if there is no refund for customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Returns and Refund Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer Returns - Version 2 (F4832). | The Manage Customer Returns - Version 2 screen displays. |  |
| 3 | Search for Returns Order | Choose Show Filter Bar if it is hidden. Enter the following data and choose Go:Returns Order : <returns order number 6XXXXXXX> | Returns order is found and displayed. |  |
| 4 | Navigate to Determine Refund Screen | Select the returns order entry and choose Determine Refund. | The Determine Refund screen displays. |  |
| 5 | Check Refund Progress | In the upper area, check percentage number in the Refund Progress field and then take next action accordingly:<100%: Refund determination is not completed. Go to Section A and then Section B.100%: Refund determination is completed. Skip Section A and go to Section B. |  |  |
| Section A: Refund is determined with reference to material inspection results | Refund Seller with Credit Memo | On the Items to Be Refunded tab, choose Change Refund in the Refund Details column for the return item.Enter the following data:Refund Type: Credit MemoRefund Code: <a percentage number>, for example, 100% RefundChoose OK.Select the item and choose Release Selected Items. | Refund setting is maintained, and credit memo request document is created in background. |  |
| Section B: Check Refund Determination Result | Check Refund Results | On the Completed Items tab, refund result is displayed. Follow-up document number is shown in Refund Details column. Make a note of document number for further use. You can choose the created document number to check detailed information. | The refund result displays. |  |

#### Display Returns Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check the progress of return process. All dependent documents are available in process flow.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Returns and Refund Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer Returns - Version 2 (F4832). | The Manage Customer Returns - Version 2 screen displays. |  |
| 3 | Search for Returns Order | Choose Show Filter Bar if it is hidden. Enter the following data and choose Go:Returns Order: <returns order number 6XXXXXXX> | Returns order is found and displayed. |  |
| 4 | Order Overview | Choose the created returns order number 6XXXXXXX and choose Display Customer Return. | The Display Standard Return 6XXXXXXX: Overview screen displays. |  |
| 5 | Document Flow | On Returns tab, choose Returns Overview in Returns Control area. | The Returns Overview for Returns Order 6XXXXXXX - 10 screen displays. |  |
| 6 | Check Document Flow | In Document Number column, make a note of follow-up credit memo request number for further use. |  |  |

#### Refund Seller with Credit Memo

##### Create Credit Memo

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a credit memo.

Procedure

Create Billing Document

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Document screen displays. |  |
| 3 | Define Billing Setting | Choose Billing Settings in the bottom bar, keep the settings as below:Set Billing Date and type before billing: ONCreate Separate billing document for each item of billing due list: ONAutomatically Post Billing Documents: ONDisplay Billing Document after creation: ONChoose delivery items to be billed and select quantities: OFF |  |  |
| 4 | Search for Billing List | In the search condition, enter criteria if necessary. | SD documents display in the result. |  |
| 5 | Choose SD Document | Select the row of credit memo request document recorded previously and choose Create. | The Create Billing Documents (F0798) screen displays. |  |
| 6 | Maintain Billing Type and Date | Choose billing type Credit Memo (G2) and maintain billing date, such as the current date, and then choose OK. | The draft billing document with ID Sxxxxxxxx displays. |  |
| 7 | Save Billing Document | On the screen, choose Save. The draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx. Make a note of the billing document number: __________. | Final credit memo is generated. |  |

Manage Billing Documents

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access the App | Open Manage Billing Documents (F0797). | The Manage Billing Documents screen displays. |  |
| 2 | Search Billing Document | Enter the billing document number recorded previously in the Billing Document field, and press Enter. | The billing document which is created previously displays. |  |
| 3 | Display Billing Document | Select the billing document item, and choose Display. | The billing document displays. |  |
| 4 | Check Output Condition | On the Billing Document screen, go to the last assignment block, Output Items. | There are two entries with output type BILLING_DOCUMENT: one is for channel EDI, the other is for channel PRINT. |  |
| 5 | Display Print Preview | On the Billing Document screen, choose Preview. | Preview for PDF document displays. |  |
| 6 | Update New Attachment (Optional) | In the Edit mode, you can add, delete, and update the attachments. Save your changes by choosing Save in the footer bar. |  |  |
| 7 | Update New Text (Optional) | In the Edit mode, you can add, delete, and update the texts. Save your changes by choosing Save in the footer bar. |  |  |

##### Send Credit Memo via EDI

Purpose

Credit Memo is sent to the seller system.

Prerequisites

Billing Document must have been created in the supplier system.

Procedure

This step is automatically generated.

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

### Scheduling Job (Alternative)

#### Job Scheduling for Delivery Creation (Alternative)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to schedule a background job for creating outbound deliveries.

This app can be used as an alternative instead of the manual creation of outbound deliveries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Delivery Creation. | The Application Jobs screen is displayed. The app automatically shows the history of application jobs. |  |
| 3 | Create Delivery Creation Schedule | Choose New to define a new job. | The New Job screen is displayed. Job Template should default as Schedule Delivery Creation. |  |
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary, then choose Check. | The system displays the message: Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A delivery creation job is scheduled. Screen goes back to Application Jobs. |  |
| 6 | Check Delivery Creation Job Log | On the Application Jobs screen, after the status of the job item turns to Finish, choose Job Log.Note Choose the Magnifier, and the job list refreshes. | The job log details displays. |  |

#### Job Scheduling for Goods Issue Deliveries (Alternative)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to schedule a background job for goods issue posting with reference to outbound deliveries.

This app can be used as an alternative instead of the manual goods issue posting for outbound deliveries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Goods Issue For Deliveries. | The Application Jobs screen displays. The app automatically shows the history of application jobs. |  |
| 3 | Create Goods Issue Deliveries Schedule | Choose New to define a new job. | The New Job screen displays. The Job Template should default as Schedule goods issue for Deliveries. |  |
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary, then choose Check. | The system displays the message: Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A schedule goods issue for deliveries job is scheduled. Screen goes back to Application Jobs. |  |
| 6 | Check Goods Issue Deliveries Job Log | On the Application Jobs screen, after the status of the job item turns to Finish, choose Job Log.Note Choose the Magnifier, and the job list refreshes. | The job log details displays. |  |

#### Job Scheduling for Billing Creation (Alternative)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to schedule a background job for creation billing documents.

This app can be used as an alternative instead of the manual creation of billing documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Billing Creation. | The Application Jobs screen is displayed. The app automatically shows the history of application jobs. |  |
| 3 | Create Billing Creation Schedule | Choose New to define a new job for billing creation. | The New Job screen is displayed. Job Template should default as Schedule Billing Creation. |  |
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary.Choose Check. | The system displays the message Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A billing creation job is scheduled. Screen goes back to Application Jobs. |  |
| 6 | Check Billing Creation Job Log | On the Application Jobs screen, after the status of the job item turns to Finish, choose Job Log.Note Choose the Magnifier, and the job list refreshes. | The log details displays. |  |

#### Job Scheduling for Billing Release (Alternative)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to schedule a background job for release billing documents to accounting.

This app can be used as an alternative instead of the manual release to accounting for billing documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Billing Release. | The Application Jobs screen displays. The app automatically shows the history of application jobs. |  |
| 3 | Create Billing Release Schedule | Choose New to define a new job for billing creation. | The New Job screen displays. Job Template defaultly should be Schedule Billing Release. |  |
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary.Choose Check. | The system displays the message: Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A billing release job is scheduled. Return to Application Jobs. |  |
| 6 | Check Billing Release Job Log | On the Application Jobs screen, after the status of the job item turns to Finish, choose Job Log.Note Choose the Magnifier, and the job list refreshes. | The log details displays. |  |

#### Job Scheduling for Billing Output (Alternative)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to schedule a background job for when and how billing documents are sent to customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Billing Output. | The Application Jobs screen is displayed. The app automatically shows the history of application jobs. |  |
| 3 | Create Billing Output Schedule | Choose New to define a new job for billing creation. | The New Job screen displays. Job Template should default as Schedule Billing Output. |  |
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary.Choose Check. | The system displays the message Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A billing release job is scheduled. Return to Application Jobs. |  |
| 6 | Check Billing Output Job Log | On the Application Jobs screen, after the status of the job item turns to Finish, choose Job Log.Note Choose the Magnifier, and the job list refreshes. | The log details displays. |  |

### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| BKK-Sales Order Fulfillment Monitoring and Operations (Optional) | Using the master data from this document, complete the following activities described in the test script:Review sections: Incomplete SD Documents (deliveries) and Review Outbound Deliveries for Goods Issue |

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
- related-to :: [[08-sales-order-management/customer-returns-bkp-ae-test-script-sap-s-4hana-cloud-public-edition-1]]
- related-to :: [[08-sales-order-management/customer-returns-for-non-stock-and-service-materials-3te-ae-test-scrip]]
- related-to :: [[08-sales-order-management/customer-returns-management-consumer-products-61v-ae-test-script-sap-s]]
- related-to :: [[08-sales-order-management/test-script-customer-returns-with-direct-shipment-from-customer-to-sup]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3QD_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 90,848 chars in the whole document
