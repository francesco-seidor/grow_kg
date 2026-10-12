---
id: 11-inventory-warehouse-and-transportation/test-script-intercompany-stock-transfer-returns-2ts-ae-sap-s-4hana-clo
title: "Test Script: Intercompany Stock Transfer Returns (2TS_AE) - SAP S/4HANA Cloud Public Edition 2608 (2TS_S4CLD2608_BPD_EN_AE)"
description: "SAP test script (AE, release 2608) for intercompany stock transfer returns, domestic and international: returns STO through credit memo, with prerequisites."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/stock-transfer-returns]
aliases: [2TS_S4CLD2608_BPD_EN_AE]
keywords: [Stock Transfer Returns, intercompany stock transfer returns, returns stock transport order, outbound delivery, goods issue, inbound delivery, goods receipt, material inspection, internal credit memo, invoice verification]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2TS_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-862
topic: 11-inventory-warehouse-and-transportation/stock-transfer-returns
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Intercompany Stock Transfer Returns (2TS_AE) - SAP S/4HANA Cloud Public Edition 2608 (2TS_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2TS_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Stock Transfer Returns** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Intercompany Stock Transfer Returns (2TS_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232850134)

[2 Prerequisites 4](#_Toc232850135)

[2.1 System Access 4](#_Toc232850136)

[2.2 Roles 4](#_Toc232850137)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232850138)

[2.4 Additional Manual Configuration 8](#_Toc232850139)

[2.5 Business Conditions 8](#_Toc232850140)

[2.6 Preliminary Steps 9](#_Toc232850141)

[2.6.1 Opening New MM Period 9](#_Toc232850142)

[2.6.2 Create Initial Stock in Shipping Plant 9](#_Toc232850143)

[2.6.3 Create Condition Records (Optional) 10](#_Toc232850144)

[2.6.4 Optional: Configure Flexible Workflow for Returns Stock Transport Order 11](#_Toc232850145)

[2.6.4.1 Optional: Check Flexible Workflow for Returns Stock Transport Order Approval 11](#_Toc232850146)

[2.6.4.2 Optional: Configure Flexible Workflow for Return Stock Transport Order 13](#_Toc232850147)

[3 Overview Table 14](#_Toc232850148)

[4 Test Procedures 16](#_Toc232850149)

[4.1 Domestic 16](#_Toc232850150)

[4.1.1 Create Returns Stock Transport Order 16](#_Toc232850151)

[4.1.2 Create Outbound Delivery for Returns Stock Transport Order 18](#_Toc232850152)

[4.1.3 Optional: Create Pro Forma F8 Invoice 19](#_Toc232850153)

[4.1.4 Perform Picking and Post Goods Issue for Outbound Delivery 20](#_Toc232850154)

[4.1.5 Check Batches (Optional) 21](#_Toc232850155)

[4.1.6 Check Stock Status 22](#_Toc232850156)

[4.1.7 Check Inbound Delivery 23](#_Toc232850157)

[4.1.8 Confirm Quantities for Putaway 24](#_Toc232850158)

[4.1.9 Post Goods Receipt for Inbound Delivery 25](#_Toc232850159)

[4.1.10 Perform Material Inspection 26](#_Toc232850160)

[4.1.11 Check Stock Status 27](#_Toc232850161)

[4.1.12 Create Internal Credit Memo with Reference to Inbound Delivery 28](#_Toc232850162)

[4.1.13 Create Credit Memo in Invoice Verification 29](#_Toc232850163)

[4.2 International 31](#_Toc232850164)

[4.2.1 Create Returns Stock Transport Order 31](#_Toc232850165)

[4.2.2 Create Outbound Delivery for Returns Stock Transport Order 33](#_Toc232850166)

[4.2.3 Optional: Create Pro Forma F8 Invoice 34](#_Toc232850167)

[4.2.4 Perform Picking and Post Goods Issue for Outbound Delivery 35](#_Toc232850168)

[4.2.5 Check Stock Status 37](#_Toc232850169)

[4.2.6 Check Inbound Delivery 38](#_Toc232850170)

[4.2.7 Confirm Quantities for Putaway 38](#_Toc232850171)

[4.2.8 Post Goods Receipt for Inbound Delivery 40](#_Toc232850172)

[4.2.9 Perform Material Inspection 40](#_Toc232850173)

[4.2.10 Check Stock Status 42](#_Toc232850174)

[4.2.11 Create Internal Credit Memo with Reference to Inbound Delivery 43](#_Toc232850175)

[4.2.12 Create Credit Memo in Invoice Verification 44](#_Toc232850176)

[5 Appendix 47](#_Toc232850177)

[5.1 Scheduling Job (Alternative) 47](#_Toc232850178)

[5.1.1 Job Scheduling for Delivery Creation (Alternative) 47](#_Toc232850179)

## Purpose

Overview

The Intercompany Stock Transfer Returns process begins with a requirement to return material from one company or plant to another company or plant within the same country.

The buyer creates a stock transfer return order in the system. A shipping specialist at the issuing plant monitors the materials due to be shipped and creates deliveries as required. Once a return delivery is created, a pick list is generated for the materials. A warehouse clerk gathers the materials and confirms the picked quantities. The delivery quantities are issued when the return delivery is complete. Once the delivery quantities are issued, an inbound delivery is automatically created in the receiving plant as a follow-up document. A receiving specialist confirms the putaway, then receives and inspects the goods to stock, referencing the inbound delivery. An internal credit memo is generated that transfers the liability to the received company.

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
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Returns and Refund Clerk | SAP_BR_RETURNS_REFUND_CLERK | Customer Returns | SAP_BR_RETURNS_REFUND_CLERK |  |
| Receiving Specialist | SAP_BR_RECEIVING_SPECIALIST | Receiving | SAP_BR_RECEIVING_SPECIALIST |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure. If you have installed SAP Best Practices Baseline Packages for Germany and US national versions, you can use the following Baseline Package scenario data:

Domestic

Below master data table shows the data of organizational units for returns stock transfers within Germany.

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 | Company Code 3310 |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A331R | Std. storage 1 | Plant 1 AE |
| Shipping Point | 3310331R | Shipping Point 3310 |  |
| Purchase Organization | 3310 | Purch. Org. 3310 |  |
| Purchase Group | 002 | Group 002 |  |
| Company Code | 3320 | Company Code 3320 | Flex.Org App or Set Up Organizational (CBC) extension |
| Plant | 3330 | Plant 3 AE | Flex.Org App or Set Up Organizational (CBC) extension |
| Storage Location | 333A333R | Std. storage 1 | Flex.Org App extension in Plant 2 AE or Set Up Organizational (CBC) extensionShop floor w/o lean WM |
| Shipping Point | 3330333R | Shipping Point 3330 | Flex.Org App or Set Up Organizational (CBC) extension |
| Sales Organization | 3330 | Sales Organization in Company 3320 | Flex.Org App or Set Up Organizational (CBC) extension |
| Material | TG11 | Trading Good 0011,PD,Regular Proc. | See sections Business Conditions and Preliminary Steps. |
| Material | TG21 | Trad.Good 21,Reorder Point,Batch-FIFONo serial number, batch controlled (FIFO strategy) | Only use if you have activated the building block Batch Management (BLG) (BLH)(BLJ)(2EG)(BLP).See sections Business Conditions and Preliminary Steps. |
| Material | TG22 | Trad.Good 22,Reorder Point,Batch-ExpDNo serial number, batch controlled (Exp. Date) | Only use if you have activated the building block Batch Management (BLG) (BLH)(BLJ)(2EG)(BLP).See sections Business Conditions and Preliminary Steps. |
| Supplier | 33413330 | Representing the Supplying Company/Plant (Company Code 3320/ Plant 3330) | Fiori App creation |
| SupplierInvoicing Party | 33403320 | Representing Supplier in Company Code 3310 AE | Fiori App creation |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

International

In below master data table, we take United States as an example as the goods return receiver.

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 | Company Code 3310 |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A331R | Std. storage 1 | Plant 1 AE |
| Shipping Point | 3310331R | Shipping Point 3310 |  |
| Purchase Organization | 3310 | Purch. Org. 3310 |  |
| Purchase Group | 002 | Group 002 |  |
| Company Code | 1710 | Company Code 1710 | US country/region solution activation |
| Plant | 1710 | Plant 1 US | US country/region solution activation |
| Storage Location | 171A171R | Std. storage 1 | US country/region solution activation |
| Shipping Point | 1710171R | Shipping Point 1710 | US country/region solution activation |
| Sales Organization | 1710 | Sales Organization in Company 1710 | US country/region solution activation |
| Material | TG11 | Trading Good 0011,PD,Regular Proc. | See sections Business Conditions and Preliminary Steps. |
| Material | TG21 | Trad.Good 21,Reorder Point,Batch-FIFONo serial number, batch controlled (FIFO strategy) | Only use if you have activated the building block Batch Management (BLG) (BLH)(BLJ)(2EG)(BLP).See sections Business Conditions and Preliminary Steps. |
| Material | TG22 | Trad.Good 22,Reorder Point,Batch-ExpDNo serial number, batch controlled (Exp. Date) | Only use if you have activated the building block Batch Management (BLG) (BLH)(BLJ)(2EG)(BLP).See sections Business Conditions and Preliminary Steps. |
| SupplierInvoicing Party | 1741171017401710 | Supplier in Company Code 3310 AE and it is the Supplying US Company/Plant (Company code 1710/ Plant 1710 )Pur.Org.1710 |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BNE | Create Supplier Master - MDS |
| BND | Create Customer Master - MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/adc449519b5b9cbf640b477a00c6a3ea)

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | Open new posting period in relative company codes, for example, 3310, and 3320. |

### Preliminary Steps

#### Opening New MM Period

Purpose

For this activity, run the following steps from the Create New Open MM Posting Period - MDS (BNZ) to close MM period and open new posting period.

- Closing MM Period and Opening New Posting Period

#### Create Initial Stock in Shipping Plant

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create initial stock in shipping plants.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Goods Receipt Other screen displays. |  |
| 3 | Enter Movement Type | Make the following entries and choose Enter:Executable Action in Transaction MIGO: Goods ReceiptReference Document for MIGO Transaction: Other (The system saves this selection if you have selected this option before.) |  |  |
| 4 | Enter Material | On the Goods Receipt Other Screen: Material tab, make the following entry and choose Enter:Material: <Material Number> |  |  |
| 5 | Enter Quantity Data | On the Goods Receipt Other Screen: Quantity tab, make the following entry and choose Enter:Qty in Unit of Entry: <Qty in UOM>Unit of Entry: <PC> | The system displays Material document XXX created. The stock has been added. |  |
| 6 | Enter on the Goods Receipt Other Screen: Batch Tab | On the Goods Receipt Other Screen: Where tab, make the following entries and choose Enter:Movement Type: 561 (Receipt per initial entry of stock balances into unrestricted use)Plant: 3310Storage Location: 331A |  |  |
| 7 | Enter on the Goods Receipt Other Screen: Batch Tab | If the enter material number is TG21 or TG22, go to the Goods Receipt Other Screen: Batch tab, make the following entry and choose Enter:Date of Manufacture: <the Current Date or a Date in the Past>Note Only relevant for batch relevant materials. |  |  |
| 8 | Save Your Entries | Choose Post. |  |  |

Financial Postings

| Material | Debited Accounts | Credited Accounts |
| --- | --- | --- |
| Trading Good (HAWA) | 13600000Inventory TradingGd | 39912000Inv Init SF&amp;Fin Bal |

#### Create Condition Records (Optional)

Purpose

In case you have finetuned the access sequence of SAP pre-shipped condition types, the relative condition records should be created accordingly.

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 2: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BET | Create Sales Pricing Condition - MDS |

#### Optional: Configure Flexible Workflow for Returns Stock Transport Order

##### Optional: Check Flexible Workflow for Returns Stock Transport Order Approval

Purpose

In this procedure, you check flexible workflow for returns stock transprot order approval.

Make sure flexible workflow for returns stock transprot order with NBF2 document is activated, and flexible workflow for purchase order approval is configured.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.To create country-/region-dependent settings for the intended local version, choose Set Local Version . | The Configure Your Solution screen displays. |  |
| 4 | Open Active Flexible Workflow | On the Configure Your Solution screen, search Activate Flexible Workflow for Purchase Orders, then choose Go.Select the line of the item and go to next screen.On the Configure Your Solution - Purchase Order Processing screen, choose Configure on the line of Activate Flexible Workflow for Purchase Orders the configuration step. | The Document Types Purchase Order Change screen displays. |  |
| 5 | Activate Flexible Workflow for PO Approval | Make sure the following entries are made:Document Type: NBF2Scenario based workflow:XYou may be asked to enter a customizing request number, either choose your own customizing request or create a new one, then choose Continue. | The scenario based workflow is active for purchase orders with Document Type: NBF2. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Activate Flexible Workflow for Purchase Orders.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Document Types Purchase order Change screen displays. |  |
| 3 | Activate Flexible Workflow for PO Approval | Make sure the following entries are made:Document Type: NBF2Scenario based workflow:XYou may be asked to enter a customizing request number, either choose your own customizing request or create a new one, then choose Continue. | The scenario based workflow is active for purchase orders with Document Type: NBF2. |  |

Result

The scenario based workflow is active for Document Type: NBF2.

##### Optional: Configure Flexible Workflow for Return Stock Transport Order

Purpose

In this procedure, you configure your release conditions for return stock transport order approval.

When you start to process this step, please make sure that the flexible workflow for return stock transport order NBGF2 has been activated in your system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Workflows for Purchase Orders (F2872). | The Manage Workflows screen displays. |  |
| 3 | Create Manage Workflow | Choose Add and make following entry:Name: Test Workflow for Return Transport Order NBF2Go to the Preconditions area and choose Document type of purchase order is: STO Adavance Return (NBF2)Choose Add and make the following entry:Purchasing group of purchase order is: 003Go to the Step Sequence area, and choose Add, then make the following entry on the next screen:Type: Release Purchase OrderGo to the Recipients area:User: Select User with Purchasing_manager from F4 help.Step to be completed by：One of the recipients.Choose Add.Choose Save. | The workflow for stock Transport order is configured. |  |
| 4 | Activate Workflow Item | Select the just created Workflow Item and choose Activate. | The workflow item is activated. |  |

## Overview Table

This scope item consists of several process steps provided in the tables below .

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Table 3: Domestic

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Returns Stock Transport Order](#unique_14) [page ] 16 | Purchaser | Create Purchase Order - Advanced (ME21N) | A returns stock transport order is created. |
| [Create Outbound Delivery for Returns Stock Transport Order](#unique_15) [page ] 18 | Shipping Specialist | My Purchase Orders - Due for Delivery (VL10B) | Ourbound delivery for returns stock transport order is created. |
| [Perform Picking and Post Goods Issue for Outbound Delivery](#unique_16) [page ] 20 | Shipping Specialist | Change Outbound Delivery (VL02N) | Goods issue is posted. |
| [Check Stock Status](#unique_17) [page ] 22 | Warehouse Clerk | Stock - Single Material (F1076)Display Stock in Transit (MB5T). |  |
| [Check Batches (Optional)](#unique_18) [page ] 21 | Shipping Specialist | Change Outbound Delivery (VL02N) |  |
| [Check Inbound Delivery](#unique_19) [page ] 23 | Purchaser | Manage Purchase Orders (Version 2) (F0842A) | Check the inbound delivery which is generated automatically. |
| [Confirm Quantities for Putaway](#unique_20) [page ] 24 | Receiving Specialist | Inbound Deliveries for Putaway (VL06IP) | Putaway is done for the inbound delivery. |
| [Post Goods Receipt for Inbound Delivery](#unique_21) [page ] 25 | Receiving Specialist | Change Inbound Delivery (VL32N) | The goods receipt is posted for return delivery. |
| [Perform Material Inspection](#unique_22) [page ] 26 | Receiving Specialist | Enter Inspection Results - From Warehouse (MSR_INSPWH) | Inspection results are recorded. |
| [Check Stock Status](#unique_23) [page ] 27 | Warehouse Clerk | Stock - Single Material (F1076)Display Stock in Transit (MB5T). |  |
| [Create Internal Credit Memo with Reference to Inbound Delivery](#unique_24) [page ] 28 | Billing Clerk | Create Billing Documents (F0798) | Credit memo is created. |
| [Create Credit Memo in Invoice Verification](#unique_25) [page ] 29 | Accounts Payable Accountant | Create Supplier Invoice - Advanced (MIRO) | Credit memo in Invoice Verification is created. |

Table 4: International

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Returns Stock Transport Order](#unique_26) [page ] 31 | Purchaser | Create Purchase Order - Advanced (ME21N) | A returns stock transport order is created. |
| [Create Outbound Delivery for Returns Stock Transport Order](#unique_15) [page ] 18 | Shipping Specialist | My Purchase Orders - Due for Delivery (VL10B) | Outbound delivery for returns stock transport order is created. |
| [Perform Picking and Post Goods Issue for Outbound Delivery](#unique_16) [page ] 20 | Shipping Specialist | Change Outbound Delivery (VL02N) | Goods issue is posted. |
| [Check Stock Status](#unique_17) [page ] 22 | Warehouse Clerk | Stock - Single Material (F1076)Display Stock in Transit (MB5T). |  |
| [Check Inbound Delivery](#unique_19) [page ] 23 | Purchaser | Manage Purchase Orders (Version 2) (F0842A) | Check the inbound delivery which is generated automatically. |
| [Confirm Quantities for Putaway](#unique_20) [page ] 24 | Receiving Specialist | Inbound Deliveries for Putaway (VL06IP) | Putaway is done for the inbound delivery. |
| [Post Goods Receipt for Inbound Delivery](#unique_21) [page ] 25 | Receiving Specialist | Change Inbound Delivery (VL32N) | The goods receipt is posted for inbound delivery. |
| [Perform Material Inspection](#unique_22) [page ] 26 | Receiving Specialist | Enter Inspection Results - From Warehouse (MSR_INSPWH) | Inspection results are recorded. |
| [Check Stock Status](#unique_23) [page ] 27 | Warehouse Clerk | Stock - Single Material (F1076)Display Stock in Transit (MB5T). |  |
| [Create Internal Credit Memo with Reference to Inbound Delivery](#unique_24) [page ] 28 | Billing Clerk | Create Billing Documents (F0798) | Credit memo is created. |
| [Create Credit Memo in Invoice Verification](#unique_27) [page ] 44 | Accounts Payable Accountant | Create Supplier Invoice - Advanced (MIRO) | Credit memo in Invoice Verification is created. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Domestic

#### Create Returns Stock Transport Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a return stock transport order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Purchase Order - Advanced (ME21N). | The Create Purchase Order Advanced screen displays. |  |
| 3 | Enter Return Stock Transport Order Document Type | Make the following entry:Order Type: NBF2 (STO Advanced Return).Then choose Enter. | All data is entered, the item detail screen opens. |  |
| 4 | Enter Return Stock Transport Order Data | Enter the following data:Supplier: 33413330In the Header area, Org. Data tab:Company Code: 3310Purchasing Organization: 3310Purchasing Group: 002Tab Partners:Partner Function: PINumber: 33403320For Item Overview:Material: TG11(without batch management) TG21/TG22 (with batch management)Quantity: <x pc>Delivery Date: <any date in the future>Plant: 3310Storage Location: 331AIn Item Details area, Invoice tab:Tax Code: for example, <V1> (Germany)Note We are using <V1> as an example to show the tax code of a German company. You may enter a differentTax Code value based on which country/region your company belongs to.Then choose Enter.Note Currently the system triggers an availability check. Based on the results of the checks, if requested availability cannot be fulfilled, the Confirmation Proposal screen shows up and the user needs to take a decision based on the result of the checks. | All data is entered, the item detail screen opens. |  |
| 5 | Save Return Stock Transport Order | Choose Save and when the returns stock transport order number displays, write it down for further use. | A new returns stock transport order is created. Returns stock transfport order number displays.Write down the returns stock transport order number for further usage. |  |

#### Create Outbound Delivery for Returns Stock Transport Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create the outbound delivery for the returns stock transport order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Shipping Specialist. | The Fiori launchpad displays. |  |
| 2 | Access the App | Open My Purchase Orders - Due for Delivery (VL10B). | The Purchase Orders, Fast Display screen appears. |  |
| 3 | Enter Data | Make the following entries:Shipping Point/Receiving Pt: 3310Delivery Creation Date (From): <delivery creation From date>Delete the default dateDelivery creation dates (To): <delivery creation To date>Delete the default dateCalcRuleDefltDlvCrDt: <calculation rule> 3 |  |  |
| 4 | Enter Returns Stock Transport Order Number | Choose the Purchasing Order tab and enter the returns stock transport order number which has been created in previous step in the Purchasing document field.Choose Execute. | The Activities Due for Shipping "Purchase Orders, Fast Display" screen appears. |  |
| 5 | Create Delivery | Select returns stock transport order from the list. Choose Background to create outbound delivery in background. |  |  |
| 6 | Check Delivery Number | Choose More > Show/Hide Delivery and note down the outbound delivery number shown in the SD Doc. field | An outbound delivery is created. |  |

#### Optional: Create Pro Forma F8 Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create the Pro Forma invoice in the selling company.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents - VF01 (VF01). | The Create Billing Documents screen displays. |  |
| 3 | Maintain Billing Date | Make the following entries:Billing Type: Pro Forma Invoice for Delivery (F8)Billing Date: For example, <current date>Enter delivery number in the Document field and press Enter. |  |  |
| 4 | Save | Choose Save. | The F8 billing document is created.Note down the document number. |  |
| 5 | Search Billing Document | Open Display Billing Documents (VF03). | The Display Billing Documents screen displays. |  |
| 6 | Display Billing Document | On the Display Billing Documents screen, enter the Billing Document number, and choose Continue. | The Pro Forma Invoice for Delivery xxxxxxxx Display: Overview of Bi screen displays. |  |
| 7 | Check Output Condition | On the Pro Forma Invoice for Delivery xxxxxxxx Display: Overview of Bi screen, choose Change Bill. Doc. and then choose Menu > Goto > Header > Output . | The Pro Forma Invoice for Delivery xxxxxxxx Change: Output screen displays. |  |
| 8 | Display Print Preview | On the Pro Forma Invoice for Delivery xxxxxxxx Change: Output screen, select the output entry and choose Display Document. | A preview for PDF document displays. |  |
| 9 | Print Billing Document | From the preview of the document, choose Print. |  |  |

#### Perform Picking and Post Goods Issue for Outbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to pick and post goods issue for outbound delivery created previously.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). | The Change Outbound Delivery screen displays. |  |
| 3 | Enter Delivery Number | On the Change Outbound Delivery screen, enter the delivery document number from the previous section and choose Continue. | The Adv. Returns Delivery XXXXXXXX Change: Overview screen displays. |  |
| 4 | Check Batch Split | On the Adv. Returns Delivery XXXXXXXX Change: Overview screen, choose the Picking tab. If the material number is TG21 or TG22, navigate to the Picking tab, check batch split exists in the Batch Split Indicator column. |  |  |
| 5 | Enter Picked Quantity | • If the material is TG21/ TG22, the batch split will exist, choose Batch Split Exists to expand sub item(s), enter quantity equal to delivery qty in Picked Qty field for sub item.• If the material is TG11, the batch split doesn't exist, enter quantity equal to delivery qty in Picked Qty field for picking related item(s). |  |  |
| 6 | Post Goods Issue | On the Change Outbound Delivery screen, choose Post Goods Issue. |  |  |

#### Check Batches (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This optional process step shows you how to check batches.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). | The Change Outbound Delivery screen displays. |  |
| 3 | Enter Delivery Number | On the Change Outbound Delivery screen, enter the delivery document number from the earlier section and choose Continue. | The Replen. Cross-Company XXXXXXXX: Overview screen displays. |  |
| 4 | Check Batch Number Assignment | If Expand Batch Spilit exists, select the Batch Split Indicator field, and check the batch number assignment. | Batch numbers are assigned to the materials. The batch numbers are required to be entered during Post Goods Receipt step. |  |
| 5 | Save Document | Choose Save. |  |  |

#### Check Stock Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check stock status.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Option 1: Open Stock - Single Material (F1076).Option 2: Open Display Stock in Transit (MB5T). | The Stock Single Material/ Display Stock in Transit screen displays. |  |
| 3 | Enter Returns Stock Transport Order Data | Option 1: Enter material number and choose Enter.Option 2: Make the following entries:Material Number: <Material Number>Receiving Plant: 3310Then choose Execute. | You receive an overview of the materials and of the returns stock transport orders that are currently in transit. It concerns all materials that have left the issuing plant and have not yet reached the receiving plant. |  |

#### Check Inbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check the inbound delivery which the system generates automatically when you psot the goods issue for the outbound delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Purchase Orders (Version 2) (F0842A). | The Manage Purchase Order screen displays. |  |
| 3 | Search for Returns Stock Transport Order Number | Enter the returns stock transport order number in Search field.Then choose GO. | All data is entered. |  |
| 4 | Display Returns Stock Transport Order | Select the returns stock transport order which is in the purchase orders list. | The Display Purchase Order screen appears. |  |
| 5 | Check Inbound Delivery Number | On the Display Purchase screen, choose Returns in Item Detail tab.Choose Returns Overview on Returns tab. The Returns Overview for Returns STO xxxxxxx-xx screen displays.You can check the inbound delivery number in returns steps list. | Write down the inbound delivery number for further usage. |  |

#### Confirm Quantities for Putaway

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to confirm that all the materials have been put away in the correct quantities.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Receiving Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Inbound Deliveries for Putaway (VL06IP). | The Inbound Deliveries for Putaway screen appears. |  |
| 3 | Enter Inbound Delivery Number | Make the following entries, and choose Execute:Delivery Date: Delete the default dateInbound Delivery: XXX | The selected Inbound Delivery shows up. |  |
| 4 | Change the Inbound Delivery | Check the selected Inbound Deliveries and choose Change Inbound Deliveries. |  |  |
| 5 | Confirm Quantities for Putaway Without Batch Assignment | If the material is TG11, under Stock Placement tab, enter the following data:Putaway Qty: XXXThe put away quantity should be equal to the delivery quantity.Choose Save. | Back to the Inbound Deliveries for Putaway screen and Inbound Delivery XXX has been saved message displays. |  |
| 6 | Confirm Quantities for Putaway with Batch Assignment | If the material is TG21 or TG22, under Stock Placement tab, select the Batch Split Indicator field of the item and expand the batch items of the main item, enter the following data:Putaway Qty: XXXThe put away quantity should be equal to the delivery quantity of the batch item.Choose Save. | Back to the Inbound Deliveries for Putaway screen and Inbound Delivery XXX has been saved message displays. |  |

#### Post Goods Receipt for Inbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post goods receipt for inbound delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Receiving Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Inbound Delivery (VL32N). | The Change Inbound Delivery screen displays. |  |
| 3 | Enter Inbound Delivery Number | Make the following entriesInbound Delivery: XXXSelect the delivery number when the inbound delivery list displays. | The selected inbound deliveries show up. |  |
| 4 | Change the Inbound Delivery | Check the selected inbound deliveries and choose Post Goods Receive.The goods receipt is posted for the inbound delivery XXX. Choose Continue. | Goods receipt is posted.A success message shows up. |  |

#### Perform Material Inspection

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The material inspection takes place after you have posted the goods receipt in the receiving plant. The further logistical handling of the returned materials is decided. This process step shows you how to perform material inspection.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Receiving Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Enter Inspection Results - From Warehouse (MSR_INSPWH). | The Worklist Selection of Deliveries screen displays. |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Execute:Delivery items waiting for inspection: <select>Delivery: <Enter Inbound delivery number> | The Change: Material Inspection in Warehouse for Delivery screen displays. |  |
| 4 | Choose Item Tab | Choose Item. |  |  |
| 5 | Enter Inspection Result | In the Inspection Result subarea, enter the following data and choose Enter:Inspection Code: <Enter inspection code>Inspected quantity: <Enter inspected quantity>If the Confirmation of Redetermination dialog box appears, choose Yes to confirm. |  |  |
| 6 | Enter Follow-Up Activity | In Logistical Follow-Up subarea, enter the following data and choose Enter:Follow-Up Activity: <Enter follow-up activity>Note Choose appropriate logistical follow-up activity according to inspection code. For example, choose follow-up activity 0011--Transfer to Free Available Stock responding to inspection code 0001. |  |  |
| 7 | Check Inspection Status | Under the Header tab, in Basic Data subarea, Inspection status shows Inspected, which means all received material is inspected completely. | All received material is inspected completely. |  |
| 8 | Save and Confirm | Choose Save and Confirm.Note Please do not choose Save Inspection Results. | Inspection result is recorded, logistical follow-up document is posted accordingly. |  |

#### Check Stock Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check stock status.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Stock - Single Material (F1076) | The Stock Single Material screen displays. |  |
| 3 | Enter Transfer Order Data | Enter material and choose Enter. | You receive an overview of the materials. This concerns all materials that have left the supplying plant and have already reached the receiving plant.Unrestricted use stock is increased after confirming the follow-up activity 0011--Transfer to Free Available Stock. |  |

#### Create Internal Credit Memo with Reference to Inbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create internal credit memo with reference to the inbound delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Document screen displays. |  |
| 3 | Define Billing Settings | Choose the Billing Settings in the bottom bar. Switch on the following settings:Set billing data and type before billing.Create separate billing documents for each billing due list item.Automatically post billing documents.Display billing document after creation. |  |  |
| 4 | Search for Billing List | In the search field or in the compact filter area, enter selection criteria if necessary. | SD Billing due list items display in the result. |  |
| 5 | Choose SD Inbound Delivery | Select the row of the inbound delivery document created previously and choose Create. | The Create Billing Documents dialog screen displays. |  |
| 6 | Enter Billing Type and Billing Date | Choose billing type Internal CM STO Return (CIIG) and enter billing date, for example, current date, then choose OK. | The draft billing document with ID Sxxxxxxxx displays. |  |
| 7 | Save Billing Document | On the Billing Document screen, choose Save, the draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx, make a note of the billing document number: __________. | Internal credit memo is generated. |  |

Financial Posting for Internal Credit Memo

| Material | Debited Account | Credited Account | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 41001500 Revenue Affiliate – Product22000000 Output Tax (MWS) | 12300000 company code 3310 as a business partner | none |

#### Create Credit Memo in Invoice Verification

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create the credit memo for the returns stock transport order in invoice verification.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Supplier Invoice - Advanced (MIRO). | The Create Supplier Invoices screen displays. |  |
| 3 | Enter General Data | If the returns stock transport orders have been created with local currency in your system, make the following entries.Transaction: Credit MemoCompany Code: 3310Gross Invoice Amount: XXXCurrency: AEDInvoice Date: TodayPosting Date: TodayReference: xxx (enter 00 + invoice number from invoicing party)Invoice Party: 33403320If the returns stock transport orders have been created with foreign currency in your system, make the following entries.Transaction: Credit MemoCompany Code: 3310Gross Invoice Amount: XXXCurrency: XXX(change the invoice currency, for example from EUR to USD)Invoice Date: TodayPosting Date: TodayReference: xxx (enter 00 + invoice number from invoicing party)Invoice Party: 33403320Select See More at header area, make the following entries.Exchange Rate: XXX | The Create Supplier Invoices screen displays.The exchange rate should be changed from USD in EUR according to the customizing settings. The exchange rate is changeable |  |
| 4 | Enter Returns Stock Transport Order References | Under Purchase Order References tab,make the following entries (use a STO you created previously).References Document Category: Purchase Order/Scheduling AgreementPurchase Order: xxxxxxxx | The Purchase Order References screen displays. |  |
| 5 | Check the Returns Stock Transport Order Items Data | Check the amount, the quantity, the tax code (there may already be a tax code that was copied from the returns stock transport order.). | The Stock Transfer Return Order Item's table displays. |  |
| 6 | Check Tax Code | In the Tax section, check the tax code and enter the tax amount. You can select the check box Calculate Tax and system will calculate the tax amount automatically. | In the tax area, you should see the same tax codes as in the items.Note If there is no tax, specify the tax code V0. |  |
| 7 | Check the Balance | Check the balance (difference between the calculated amount and the gross amount you entered in step 3). | The balance should be zero (or within the defined tolerance). |  |
| 8 | Simulate Supplier Credit Memo and Check Messages | Choose Simulate.If there are no differences (or if the value is within the defined tolerance), a new screen Simulation Results appears. You can check the simulation results in Overview and Details area. | The credit memo is complete to post. |  |
| 9 | Post Credit Memo | Choose Post. | The credit memo is posted. The system displays the message Invoice xxx has been posted. |  |

### International

#### Create Returns Stock Transport Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a returns stock transport order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Purchase Order - Advanced (ME21N). | The Create Purchase Order Advanced screen displays. |  |
| 3 | Enter Returns Stock Transport Order Document Type | Make the following entry:Order Type: NBF2 (STO Advanced Return)Then choose Enter. | All data is entered, the item detail screen opens. |  |
| 4 | Enter Returns Stock Transport Order Data | Enter the following data:Supplier: 17411710 (US)For Header / Org. Data:Company Code: 3310Purchasing Org.: 3310Purchasing Group: 002Header / Partners:Partner Function.: PINumber: 17401710 (US)For Item Overview:Material: TG11(without batch management) TG21/TG22 (with batch management)Quantity: <x pc>Delivery Date: <any date in the future>Plant: 3310Storage Location: 331AUnder Item Details Invoice tab:Tax Code: <Tax Code>Then choose Enter.Note Currently the system triggers an availability check. Based on the results of the checks, if requested availability cannot be fulfilled, the Confirmation Proposal screen shows up and the user needs to take a decision based on the result of the checks. | All data is entered, the item detail screen opens. |  |
| 5 | Save Returns Stock Transport Order | Choose Save and when the returns stock transport order number displays, write it down for further use. | A new returns stock transport order is created. Returns stock transport order number displays.Write down the returns stock transport order number for further usage. |  |

#### Create Outbound Delivery for Returns Stock Transport Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create the outbound delivery for the returns stock transport order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Shipping Specialist. | The Fiori launchpad displays. |  |
| 2 | Access the App | Open My Purchase Orders - Due for Delivery (VL10B). | The Purchase Orders, Fast Display screen appears. |  |
| 3 | Enter Data | Make the following entries:Shipping Point/Receiving Pt: 3310Delivery Creation Date (From): <delivery creation From date>Delete the default dateDelivery creation dates (To): <delivery creation To date>Delete the default dateCalcRuleDefltDlvCrDt: <calculation rule> 3 |  |  |
| 4 | Enter Returns Stock Transport Order Number | Choose the Purchasing Order tab and enter the returns stock transport order number which has been created in previous step in the Purchasing document field.Choose Execute. | The Activities Due for Shipping "Purchase Orders, Fast Display" screen appears. |  |
| 5 | Create Delivery | Select returns stock transport order from the list. Choose Background to create outbound delivery in background. |  |  |
| 6 | Check Delivery Number | Choose More > Show/Hide Delivery and note down the outbound delivery number shown in the SD Doc. field | An outbound delivery is created. |  |

#### Optional: Create Pro Forma F8 Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create the Pro Forma invoice in the selling company.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents - VF01 (VF01). | The Create Billing Documents screen displays. |  |
| 3 | Maintain Billing Date | Make the following entries:Billing Type: Pro Forma Invoice for Delivery (F8)Billing Date: For example, <current date>Enter delivery number in the Document field and press Enter. |  |  |
| 4 | Save | Choose Save. | The F8 billing document is created.Note down the document number. |  |
| 5 | Search Billing Document | Open Display Billing Documents (VF03). | The Display Billing Documents screen displays. |  |
| 6 | Display Billing Document | On the Display Billing Documents screen, enter the Billing Document number, and choose Continue. | The Pro Forma Invoice for Delivery xxxxxxxx Display: Overview of Bi screen displays. |  |
| 7 | Check Output Condition | On the Pro Forma Invoice for Delivery xxxxxxxx Display: Overview of Bi screen, choose Change Bill. Doc. and then choose Menu > Goto > Header > Output . | The Pro Forma Invoice for Delivery xxxxxxxx Change: Output screen displays. |  |
| 8 | Display Print Preview | On the Pro Forma Invoice for Delivery xxxxxxxx Change: Output screen, select the output entry and choose Display Document. | A preview for PDF document displays. |  |
| 9 | Print Billing Document | From the preview of the document, choose Print. |  |  |

#### Perform Picking and Post Goods Issue for Outbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to pick and post goods issue for outbound delivery created previously.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). | The Change Outbound Delivery screen displays. |  |
| 3 | Enter Delivery Number | On the Change Outbound Delivery screen, enter the delivery document number from the earlier section and choose Continue. | The Adv. Returns Delivery XXXXXXXX Change: Overview screen displays. |  |
| 4 | Enter Picking Data | On the Adv. Returns Delivery XXXXXXXX Change: Overview screen, choose the Picking tab, make the following entries:Picked Quantity: <picked quantity>Storage Location: 331AChoose Save. | The system shows the message: Adv. Returns Delivery xxxxxxxx has been saved. The screen returns to Change Outbound Delivery. |  |
| 5 | Check Batch Split | On the Adv. Returns Delivery XXXXXXXX Change: Overview screen, choose Picking. If the material number is TG21 or TG22,navigate to Picking, check batch split exists in the Batch Split Indicator column . |  |  |
| 6 | Enter Picked Quantity | • If the material is TG21/ TG22, the batch split exists, choose Batch Split Exists to expand sub item(s), enter quantity equal the delivery quantity in Picked Qty field for sub item.• If the material is TG11, the batch split doesn't exist, enter quantity equal the delivery quantity in Picked Qty field for picking related item(s). |  |  |
| 7 | Post Goods Issue | On the Change Outbound Delivery screen, choose Post Goods Issue. |  |  |

#### Check Stock Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check stock status.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Option 1: Open Stock - Single Material (F1076).Option 2: Open Display Stock in Transit (MB5T). | The Stock Single Material/ Display Stock in Transit screen displays. |  |
| 3 | Enter Returns Stock Transport Order Data | Option 1: Enter material number and choose Enter.Option 2: Make the following entries:Material Number: <Material Number>Receiving Plant: 3310Then choose Execute. | You receive an overview of the materials and of the returns stock transport orders that are currently in transit. It concerns all materials that have left the issuing plant and have not yet reached the receiving plant. |  |

#### Check Inbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check the inbound delivery which the system generates automatically when you psot the goods issue for the outbound delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Purchase Orders (Version 2) (F0842A). | The Manage Purchase Order screen displays. |  |
| 3 | Search for Returns Stock Transport Order Number | Enter the returns stock transport order number in Search field.Then choose GO. | All data is entered. |  |
| 4 | Display Returns Stock Transport Order | Select the returns stock transport order which is in the purchase orders list. | The Display Purchase Order screen appears. |  |
| 5 | Check Inbound Delivery Number | On the Display Purchase screen, choose Returns in Item Detail tab.Choose Returns Overview on Returns tab. The Returns Overview for Returns STO xxxxxxx-xx screen displays.You can check the inbound delivery number in returns steps list. | Write down the inbound delivery number for further usage. |  |

#### Confirm Quantities for Putaway

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to confirm that all the materials have been put away in the correct quantities.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Receiving Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Inbound Deliveries for Putaway (VL06IP). | The Inbound Deliveries for Putaway screen appears. |  |
| 3 | Enter Inbound Delivery Number | Make the following entries, and choose Execute:Delivery Date: Delete the default dateInbound Delivery: XXX | The selected Inbound Delivery shows up. |  |
| 4 | Change the Inbound Delivery | Check the selected Inbound Deliveries and choose Change Inbound Deliveries. |  |  |
| 5 | Confirm Quantities for Putaway Without Batch Assignment | If the material is TG11, under Stock Placement tab, enter the following data:Putaway Qty: XXXThe put away quantity should be equal to the delivery quantity.Choose Save. | Back to the Inbound Deliveries for Putaway screen and Inbound Delivery XXX has been saved message displays. |  |
| 6 | Confirm Quantities for Putaway with Batch Assignment | If the material is TG21 or TG22, under Stock Placement tab, select the Batch Split Indicator field of the item and expand the batch items of the main item, enter the following data:Putaway Qty: XXXThe put away quantity should be equal to the delivery quantity of the batch item.Choose Save. | Back to the Inbound Deliveries for Putaway screen and Inbound Delivery XXX has been saved message displays. |  |

#### Post Goods Receipt for Inbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post goods receipt for inbound delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Receiving Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Inbound Delivery (VL32N). | The Change Inbound Delivery screen displays. |  |
| 3 | Enter Inbound Delivery Number | Make the following entriesInbound Delivery: XXXSelect the delivery number when the inbound delivery list displays. | The selected inbound deliveries show up. |  |
| 4 | Change the Inbound Delivery | Check the selected inbound deliveries and choose Post Goods Receive.The goods receipt is posted for the inbound delivery XXX. Choose Continue. | Goods receipt is posted.A success message shows up. |  |

#### Perform Material Inspection

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The material inspection takes place after you have posted the goods receipt in the receiving plant. The further logistical handling of the returned materials is decided. This process step shows you how to perform material inspection.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Receiving Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Enter Inspection Results - From Warehouse (MSR_INSPWH). | The Worklist Selection of Deliveries screen displays. |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Execute:Delivery items waiting for inspection: <select>Delivery: <Enter Inbound delivery number> | The Change: Material Inspection in Warehouse for Delivery screen displays. |  |
| 4 | Choose Item Tab | Choose Item. |  |  |
| 5 | Enter Inspection Result | In the Inspection Result subarea, enter the following data and choose Enter:Inspection Code: <Enter inspection code>Inspected quantity: <Enter inspected quantity>If the Confirmation of Redetermination dialog box appears, choose Yes to confirm. |  |  |
| 6 | Enter Follow-Up Activity | In Logistical Follow-Up subarea, enter the following data and choose Enter:Follow-Up Activity: <Enter follow-up activity>Note Choose appropriate logistical follow-up activity according to inspection code. For example, choose follow-up activity 0011--Transfer to Free Available Stock responding to inspection code 0001. |  |  |
| 7 | Check Inspection Status | Under the Header tab, in Basic Data subarea, Inspection status shows Inspected, which means all received material is inspected completely. | All received material is inspected completely. |  |
| 8 | Save and Confirm | Choose Save and Confirm.Note Please do not choose Save Inspection Results. | Inspection result is recorded, logistical follow-up document is posted accordingly. |  |

#### Check Stock Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check stock status.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Stock - Single Material (F1076) | The Stock Single Material screen displays. |  |
| 3 | Enter Transfer Order Data | Enter material and choose Enter. | You receive an overview of the materials. This concerns all materials that have left the supplying plant and have already reached the receiving plant.Unrestricted use stock is increased after confirming the follow-up activity 0011--Transfer to Free Available Stock. |  |

#### Create Internal Credit Memo with Reference to Inbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create internal credit memo with reference to the inbound delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Document screen displays. |  |
| 3 | Define Billing Settings | Choose the Billing Settings in the bottom bar. Switch on the following settings:Set billing data and type before billing.Create separate billing documents for each billing due list item.Automatically post billing documents.Display billing document after creation. |  |  |
| 4 | Search for Billing List | In the search field or in the compact filter area, enter selection criteria if necessary. | SD Billing due list items display in the result. |  |
| 5 | Choose SD Inbound Delivery | Select the row of the inbound delivery document created previously and choose Create. | The Create Billing Documents dialog screen displays. |  |
| 6 | Enter Billing Type and Billing Date | Choose billing type Internal CM STO Return (CIIG) and enter billing date, for example, current date, then choose OK. | The draft billing document with ID Sxxxxxxxx displays. |  |
| 7 | Save Billing Document | On the Billing Document screen, choose Save, the draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx, make a note of the billing document number: __________. | Internal credit memo is generated. |  |

Financial Posting for Internal Credit Memo

| Material | Debited Account | Credited Account | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 41001500 Revenue Affiliate – Product22000000 Output Tax (MWS) | 12300000 company code 3310 as a business partner | none |

#### Create Credit Memo in Invoice Verification

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create the credit memo for the returns stock transport order in invoice verification.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Supplier Invoice - Advanced (MIRO). | The Create Supplier Invoices screen displays. |  |
| 3 | Enter General Data | If the returns stock transport orders have been created with local currency in your system, make the following entries.Transaction: Credit MemoCompany Code: 3310Gross Invoice Amount: XXXCurrency: AEDInvoice Date: TodayPosting Date: TodayReference: xxx (enter 00 + invoice number from invoicing party)Invoice Party: 17401710If the returns stock transport orders have been created with foreign currency in your system, make the following entries.Transaction: Credit MemoCompany Code: 3310Gross Invoice Amount: XXXCurrency: XXX(change the invoice currency, for example from EUR to USD)Invoice Date: TodayPosting Date: TodayReference: xxx (enter 00 + invoice number from invoicing party)Invoice Party: 17401710Select See More at header area, make the following entries.Exchange Rate: XXX | The Create Supplier Invoices screen displays.The exchange rate should be changed from USD in EUR according to the customizing settings. The exchange rate is changeable. |  |
| 4 | Enter Returns Stock Transport Order References | Under the Purchase Order References tab,make the following entries (use a RSTO you created previously).References Document Category: Purchase Order/Scheduling AgreementPurchase Order: xxxxxxxx | The Purchase Order References screen displays. |  |
| 5 | Check the Returns Stock Transport Order Items Data | Check the amount, the quantity, the tax code (there may already be a tax code that was copied from the returns stock transport order.). | The Stock Transfer Return Order Item's table displays. |  |
| 6 | Check Tax Code | In the Tax section, check if there is tax code information and enter the tax amount. You can select the Calculate Tax checkbox and system will calculate the tax amount automatically. | In the Tax area, you should see the same tax codes as in the items.Note If there is no tax, specify the tax code V0. |  |
| 7 | Check the Balance | Check the balance (difference between the calculated amount and the gross amount you entered in step 3). | The balance should be zero (or within the defined tolerance). |  |
| 8 | Simulate Supplier Credit Memo and Check Messages | Choose Simulate.If there are no differences (or if the value is within the defined tolerance), a new screen Simulation Results appears. You can check the simulation results in Overview and Details area. | The credit memo is complete to post. |  |
| 9 | Post Credit Memo | Choose Post. | The credit memo is posted. The system displays the message Invoice xxx has been posted. |  |

## Appendix

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
| 2 | Access App | Open Schedule Delivery Creation (F2228). | The Application Jobs screen displays.The app automatically shows the history of application jobs. |  |
| 3 | Create Delivery Creation Schedule | Choose Create to define a new Job. | The New Job screen displays. The Job Template should be displayed as Schedule Delivery Creation for Purchase Orders by default. |  |
| 4 | Scheduling Options | Choose Step 2 to define scheduling for the batch job if necessary. | Depending on the scheduling options, the delivery creation is started immediately or at a specific time. |  |
| 5 | Job Parameters | Choose Step 3 to define Parameters, and make at least the following entries:Shipping Point: 3320Purchasing Document: Stock Transport Order # created aboveThen choose Check. | The system displays the message You can go ahead and schedule the job. |  |
| 6 | Schedule | Choose Schedule. | A delivery creation job is scheduled.Screen goes back to Application Jobs. |  |
| 7 | Check Delivery Creation Job Log | On the Application Jobs screen, after job item’s status turned to Finished, choose Status symbol in the Log column.Note Choose the Magnifier, and the job list is refreshed. | The Job Details screen displays. |  |

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
> Flagged while digesting this document, not verified: Appendix job scheduling uses Shipping Point 3320, while the main procedure uses Shipping Point 3310 (and the master data lists shipping points 3310331R and 3330333R, none being 3320; 3320 is a company code).

> [!warning] Conflict
> Flagged while digesting this document, not verified: Purpose says the process returns material 'within the same country', yet the document also has an International section (US company code 1710); the Domestic master data is described as 'within Germany' and uses German tax code V1 as an example, while the org units are labelled AE and the currency is AED.

> [!warning] Conflict
> Flagged while digesting this document, not verified: The optional flexible workflow example uses purchasing group 003 as precondition, while the test returns STO is created with purchasing group 002, so the example workflow would not apply to the test order.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[11-inventory-warehouse-and-transportation/intra-company-returns-stock-transfers-5wi-ae-test-script-1129]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2TS_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 78,616 chars in the whole document
