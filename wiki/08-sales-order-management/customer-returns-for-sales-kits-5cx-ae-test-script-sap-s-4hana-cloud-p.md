---
id: 08-sales-order-management/customer-returns-for-sales-kits-5cx-ae-test-script-sap-s-4hana-cloud-p
title: "Customer Returns for Sales Kits (5CX_AE) - Test Script, SAP S/4HANA Cloud Public Edition (5CX_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script (5CX_AE, UAE) for customer returns of sales kits: returns order, goods receipt, inspection, refund by credit memo or replacement."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/sales-kits-with-variant-configuration]
aliases: [5CX_S4CLD2608_BPD_EN_AE]
keywords: [Sales Kits with Variant Configuration and Their Returns, customer returns, sales kits, bill of materials, returns order, refund determination, credit memo, replacement material, material inspection, goods receipt]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5CX_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1073
topic: 08-sales-order-management/sales-kits-with-variant-configuration
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Customer Returns for Sales Kits (5CX_AE) - Test Script, SAP S/4HANA Cloud Public Edition (5CX_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5CX_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Sales Kits with Variant Configuration and Their Returns** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Customer Returns for Sales Kits (5CX_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232856285)

[2 Prerequisites 4](#_Toc232856286)

[2.1 System Access 4](#_Toc232856287)

[2.2 Roles 4](#_Toc232856288)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232856289)

[2.4 Business Conditions 6](#_Toc232856290)

[2.5 Preliminary Steps 7](#_Toc232856291)

[2.5.1 Create Condition Records (Optional) 7](#_Toc232856292)

[2.5.2 Extend Material Master Data 7](#_Toc232856293)

[2.5.3 Set Initial Stock for Material 8](#_Toc232856294)

[3 Overview Table 10](#_Toc232856295)

[4 Test Procedures 12](#_Toc232856296)

[4.1 Create Returns Order 12](#_Toc232856297)

[4.2 Post Goods Receipt 19](#_Toc232856298)

[4.3 Perform Material Inspection 20](#_Toc232856299)

[4.4 Determine Refund 21](#_Toc232856300)

[4.5 Display Returns Overview 23](#_Toc232856301)

[4.6 Refund Customer with Credit Memo 24](#_Toc232856302)

[4.6.1 Create Credit Memo 24](#_Toc232856303)

[4.7 Refund Customer with Replacement Material (Optional) 26](#_Toc232856304)

[4.7.1 Create Free-of-Charge Delivery 26](#_Toc232856305)

[4.7.2 Execute Picking 27](#_Toc232856306)

[4.7.3 Post Goods Issue 28](#_Toc232856307)

[4.7.4 Create Pro-forma Invoice 30](#_Toc232856308)

[4.7.5 Create Customer Invoice 31](#_Toc232856309)

[5 Appendix 33](#_Toc232856310)

[5.1 Process Integration 33](#_Toc232856311)

[5.2 Scheduling Job (Alternative) 33](#_Toc232856312)

[5.2.1 Job Scheduling for Delivery Creation (Alternative) 33](#_Toc232856313)

[5.2.2 Job Scheduling for Goods Issue Deliveries (Alternative) 34](#_Toc232856314)

[5.2.3 Job Scheduling for Billing Creation (Alternative) 35](#_Toc232856315)

[5.2.4 Job Scheduling for Billing Release (Alternative) 36](#_Toc232856316)

[5.2.5 Job Scheduling for Billing Output (Alternative) 37](#_Toc232856317)

[5.3 Succeeding Processes 38](#_Toc232856318)

## Purpose

Overview

Companies often want to return individual products that are bundled into a sales kit (for example selling a PC together with monitor, keyboard, mouse, license, and so on). In such cases, sales kits are commonly used to sell and return individual products independently from the bundled product. Bills of materials (BOMs) are used to bundle sales kits.

The process of customer returns in returns management supports BOMs. The process starts with customer returns order creation. The sales kit material is then logistically received into the plant. Subsequently, a credit memo or replacement material is provided to customer as compensation.

Once you enter a bill of material in a customer returns order, the system runs pricing and logistics execution at the following levels:

- Header level (ERLA): usually used when product is assembled

- Item level (LUMF): usually used when product is not assembled

- Both levels (CPFH): pricing is run on header level and logistics (goods movements) on item level

- Both levels (DISH): pricing is run on item level and logistics (goods movement) on header level

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
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_SD_SP_INTERNAL_SALES |  |
| Returns and Refund Clerk | SAP_BR_RETURNS_REFUND_CLERK | Customer Returns | SAP_SD_SP_RETURNS_REFUND |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_LE_SP_OUTBD |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_SD_SP_BILLING |  |
| Receiving Specialist | SAP_BR_RECEIVING_SPECIALIST | Receiving | SAP_LE_SP_INBOD |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | SDBOMERLAHD | SD BOM Header ERLA (with pricing, inventory management) | ERLA BOM components:SDBOMERLAIT01SDBOMERLAIT02 |
| Material | SDBOMLUMFHD | SD BOM Header LUMF(no pricing, no inventory) | LUMF BOM components:SDBOMLUMFIT01SDBOMLUMFIT02 |
| Material | SDBOMCPFHHD | SD BOM Header CPFH (with pricing, no inventory) | CPFH BOM components:SDBOMCPFHIT01SDBOMCPFHIT02 |
| Material | SDBOMDISHHD | SD BOM Header DISH (no pricing, with inventory) | DISH BOM components:SDBOMDISHIT01SDBOMDISHIT02 |
| Sold-to Party | 33100003 | Domestic UAE Customer 3 |  |
| Ship-to Party | 33100003 | Domestic UAE Customer 3 |  |
| Payer | 33100003 | Customer domestic 03 |  |
| Plant | 3310 |  |  |
| Storage Location | 331A331R |  |  |
| Shipping Point | 331A331R |  |  |
| Sales Organization | 3310 |  |  |
| Distribution Channel | 10 |  |  |
| Division | 00 |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNF | Create Product Master of Type "Trading Good" |
| BET | Create Sales Pricing Condition |

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| 31Q- Sales Order Processing for Sales Kits | Complete all activities described in test script 31Q using master data, which is listed in the previous section Master Data, Organizational Data, and Other Data and note down the created document numbers of sales order and billing document for further use. |

### Preliminary Steps

#### Create Condition Records (Optional)

Purpose

In case you have finetuned the access sequence of SAP pre-shipped condition types, the relative condition records should be created accordingly.

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 2: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BET | Create Sales Pricing Condition |

#### Extend Material Master Data

Prerequisite

The following material master data exists in system, details refer to the Prerequisite part of test script item 31Q – Sales Order Processing for Sales Kits:

- SDBOMCPFHIT01
- SDBOMCPFHIT02
- SDBOMDISHHD

Purpose

In this step, the storage location data in 331R is created for materials SDBOMCPFHIT01, SDBOMCPFHIT02 and SDBOMDISHHD.

Procedure

Complete the chapter Create Material (Product) Master Data - Storage Location Data in the master data script BNF - Create Product Master of type "Trading Good" - MDS using the following data:

| Material | Plant | Storage Location |
| --- | --- | --- |
| SDBOMCPFHIT01 | 3310 | 331R |
| SDBOMCPFHIT02 | 3310 | 331R |
| SDBOMDISHHD | 3310 | 331R |

#### Set Initial Stock for Material

Purpose

This process step shows you how to set initial stock to execute this scope item.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk . | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Post Goods Movement (MIGO) . It only displays this way if it was your last transaction. So the action for the user should be to select Reference Document for MIGO Transaction > Other . | The Goods Receipt Other screen displays. |  |
| 3 | Input Movement Type | Make the following entry and choose Enter .Executable Action in Transaction MIGO : Goods ReceiptReference Document for MIGO Transaction : Other |  |  |
| 4 | Edit Material | On the Goods Receipt Other Screen: Material tab, make the following entry, and choose Enter :Material : SDBOMLUMFIT01, SDBOMLUMFIT02,SDBOMDISHHD |  |  |
| 5 | Edit Quantity Data | On the Goods Receipt Other Screen: Quantity tab, make the following entry, and choose Enter :Qty in Unit of Entry : 100Unit of Entry : <PC> |  |  |
| 6 | Enter the Goods Receipt Other Screen: Where Tab | On the Goods Receipt Other Screen: Where tab, make the following entries and choose Enter :Movement Type : 561 (Receipt per initial entry of stock balances into unrestricted use)Plant : 3310Storage Location : 331A |  |  |
| 7 | Enter the Goods Receipt Other Screen: Batch Tab | On the Goods Receipt Other Screen: Batch tab, make the following entry and choose Enter :Date of Manufacture : <Enter the Current Date or a Date in the Past> | Only relevant for batch relevant materials. |  |
| 8 | Save Your Entries | Choose Post . |  |  |

Financial Postings

| Material | Debited Accounts | Credited Accounts |
| --- | --- | --- |
| Trading Good (HAWA) | 13600000Inventory TradingGd | 39912000Inv Init SF&Fin Bal |

## Overview Table

This scope item consists of several process steps provided in the table below.

If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.

You can find all other apps not included on the homepage using the search bar.

If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose Settings > App Finder .

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Returns Order](#unique_12) [page ] 12 | Returns and Refund Clerk | Manage Customer Returns (F1708) | Returns order is created, returns delivery is generated in the background. |
| [Post Goods Receipt](#unique_13) [page ] 19 | Shipping Specialist | Change Outbound Delivery (VL02N) | The goods receipt is posted for returns delivery. |
| [Perform Material Inspection](#unique_14) [page ] 20 | Receiving Specialist | Enter Inspection Results - From Warehouse (MSR_INSPWH) | Inspection results are recorded. |
| [Determine Refund](#unique_15) [page ] 21 | Returns and Refund Clerk | Manage Customer Returns (F1708) | Refund determination is checked or triggered. |
| [Display Returns Overview](#unique_16) [page ] 23 | Returns and Refund Clerk | Manage Customer Returns (F1708) | Document flow is displayed. |
| Refund Customer with Credit Memo |  |  |  |
| [Create Credit Memo](#unique_17) [page ] 24 | Billing Clerk | Create Billing Documents (F0798) | Credit memo is created. |
| Refund Customer with Replacement Material |  |  |  |
| [Create Free-of-Charge Delivery](#unique_18) [page ] 26 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) | Outbound delivery is created. |
| [Execute Picking](#unique_19) [page ] 27 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Picking is done for outbound delivery. |
| [Post Goods Issue](#unique_20) [page ] 28 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | The goods issue is posted for outbound delivery. |
| [Create Pro-forma Invoice](#unique_21) [page ] 30 | Billing Clerk | Create Billing Documents (F0798) | Pro-forma invoice is created. |
| [Create Customer Invoice](#unique_22) [page ] 31 | Billing Clerk | Create Billing Documents (F0798) | Customer invoice is created. |

The following table provides the general return process for different kit types:

| Kit Types | Returns Order (Main item category) | Delivery | Picking/Goods Receipt | Inspection/LFU | Credit Memo | Material Replacement |
| --- | --- | --- | --- | --- | --- | --- |
| ERLA header | REQ | yes | yes | yes | yes | not supported |
| ERLAComponent | REE | yes | not relevant | not relevant | not relevant | not relevant |
| LUMF header | REP | yes | not relevant | not relevant | not relevant | not relevant |
| LUMFComponent | RENV | yes | yes | yes | yes | yes |
| LUMF Component | RLAN | yes | yes | yes | not relevant | not relevant |
| CPFH header | REHD | yes | not relevant | not relevant | yes | not relevant |
| CPFHComponent | RENI | yes | yes | yes | not relevant | not supported |
| DISH header | RBHD | yes | yes | yes | not relevant | not relevant |
| DISH component | RBNI | yes | not relevant | not relevant | yes | not supported |

|  |
| --- |
| Note If you want to return LUMF with returnable material (e.g RP001) as component, ensure below activities are completed as prerequisites:Activate scope item BDW - Returnables ProcessingEmpty field Valuation Class in view Accounting 1 for RP001 material master data with reference to Master Data Script 65B. |

## Test Procedures

The test should take around 60 minutes. The Enterprise Search function provides a central entry point for finding business objects in your company from different sources using a single search request, such as Apps and fact sheets, for business objects. From the data found, you can go directly to the respective apps and fact sheets to display, edit the data or find related objects.

How to access and check a fact sheet:

- Log on to the SAP Fiori launchpad using the respective user example, Internal Sales Representative.
- Access the Enterprise Search bar and choose the magnifying glass button in the upper right corner.
- The Enterprise Search bar is displayed, two filter fields appear left to the search button. Enter your search criteria and choose the business object type. For example, select Customer Returns from dropdown menu in the first field, enter customer returns order number in the second field and choose Search. The sales order is listed.
- Choose the sales order number link, the system navigates to fact sheet screen and returns order related information is integrated and summarized on one Fiori page. You can get detailed data via choosing the corresponding links.

There are fact sheets available for the following objects (Visible depending on the assigned role):

- Sales (return) order
- Quotation
- Billing document
- Credit Memo
- Debit Memo
- Customer 360 Fact sheet

This section describes test procedures for each process step that belongs to this scope item.

### Create Returns Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a returns order.

Prerequisite

You must have billing document or sales order as reference (refer to section Business Conditions).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Returns and Refund Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer Returns (F1708).Note Alternatively, SAP system supports creating returns order without reference using app Manage Customer Returns - Version 2 (F4832). On the Manage Customer Returns – Version 2 screen, choose Create > Create Returns Order – VA01 . After manually entering order type CBAR and other necessary data, choose Save to create returns order without reference. | The Manage Customer Returns screen displays. |  |
| 3 | Create Customer Return | Choose Create. | The Create Returns Order from Reference Document screen displays. |  |
| 4 | Enter Data | Use Adapt Filters to add Reference Document field if it is hidden.Enter the following selection criteria in the filter bar and choose Go:Reference Document: <sales order number or billing document number created previously> | Billing (sales) documents are displayed in the Reference Documents table. |  |
| 5 | Choose Create | Choose Create in the billing (sales) document entry. | The dialog box Create Returns Order from Invoice (Order) displays. |  |
| 6 | Enter Data | Enter the following data and choose Create:Return Reason: <customer ordered too much>In the Items area:Quantity: <quantity to be returned> | Returns order is created.System navigates to Edit Returns Order screen. |  |

|  |
| --- |
| Note Next part mainly introduces follow-up activity 0001 - Receive into Plant after which material inspection needs to be performed for further inventory movement of retuned materials. If you can specify the final destination of the returned materials when creating returns order and expect to skip subsequent material insepection chapter, just choose one alternatively from below:* 0002- Immediately Move to Free Available Stock* 0003- Immediately Move to ScrapWith above follow-up activities 0002 or 0003, it is mandatory to maintain inspection result in returns order. Once returns order is saved and released, returns delivery, picking and goods receipt will be generated automatically in background, next run the refund relevant steps:[Determine Refund](#unique_15) [page ] 21[Display Returns Overview](#unique_16) [page ] 23[Refund Customer with Credit Memo](#unique_24) [page ] 24 or [Refund Customer with Replacement Material (Optional)](#unique_25) [page ] 26The user can influence the point in time when the subsequent refund document is created: either immediately when the returns order is saved and released, or at a later point of time. Combination of the refund setting determines follow-up refund document creation. Choose one from the following tables to determine refund details according to different Kit types:, enter the following data: |

ERLA (logistics and pricing/billing on Header Level)

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Option 1: Execute Refund with Credit Memo Request Immediately | On the top right corner of the screen, choose Follow-up Activities, check Receive into Plant (0001) is maintained in the Follow-Up Activity column, choose Back.On the Edit Returns Order screen, in the Item area, in the Refund Details column, enter the following data or action:Refund Type: Credit MemoRefund Code: 10%(select from dropdown list)Refund Control: Create Credit Memo RequestChoose Save and Release. | Returns order is released.Returns delivery and credit memo request are generated automatically.If returns order workflow is activated, next need to perform returns order approval process, details refer to the chapter Process Returns Order Approval in test script BKP.Next please complete the following chapters:[Post Goods Receipt](#unique_13) [page ] 19[Perform Material Inspection](#unique_14) [page ] 20 (for component materials)[Refund Customer with Credit Memo](#unique_24) [page ] 24 |  |
|  | Option 2: Execute Refund with Credit Memo Immediately | On the top right corner of the screen, choose Follow-up Activities, maintain the following data and choose Back.Follow-Up Activity: Receive into Plant (0001)Product Received: XOn the Edit Returns Order screen, in the Item area, in the Refund Details column, enter the following data or action:Refund Type: Credit MemoRefund Code: 10%(select from dropdown list)Refund Control: Create Credit MemoChoose Save and Release. | Returns order is released.Subsequent documents are generated in background including:Returns deliveryGoods receipt of returns deliveryCredit memoNext please complete the following chapters:[Perform Material Inspection](#unique_14) [page ] 20 (for component materials) |  |
|  | Option 3: Decide Refund Later | On the top right corner of the screen, choose Follow-up Activities , check Receive into Plant (0001) is maintained in the Follow-Up Activity column, choose Back.On the Edit Returns Order screen, in the Items area, enter the following data or action:Refund Type: Credit MemoRefund Code: 10%(select from dropdown list)Refund Control: Decide LaterChoose Save and Release. | Returns order is released.Returns delivery is generated automatically.Next please complete the following chapters:[Post Goods Receipt](#unique_13) [page ] 19[Perform Material Inspection](#unique_14) [page ] 20 (for component materials)[Determine Refund](#unique_15) [page ] 21[Refund Customer with Credit Memo](#unique_24) [page ] 24 |  |
| 2 | Check Process Flow | On the Manage Customer Returns screen, choose arrow at end of the item. | The Display Returns Order screen displays. |  |
|  |  | In the Process Flow area, check dependent documents in process flow.Make a note of the follow-up document numbers for further use:__________. | The dependent documents display. |  |

LUMF (logistics and pricing/billing on Item Level)

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Option 1: Execute Refund with Credit Memo Request Immediately | On the top right corner of the screen, choose Follow-up Activities, check Receive into Plant (0001) is maintained in the Follow-Up Activity column, choose Back.On the Edit Returns Order screen, in the Item area, in the Refund Details column, enter the following data or action:Refund Type: Credit MemoRefund Code: 10%(select from dropdown list)Refund Control: Create Credit Memo RequestChoose Save and Release. | Returns order is released.Returns delivery and credit memo request are generated automatically.If returns order workflow is activated, next need to perform returns order approval process, details refer to the chapter Process Returns Order Approval in test script BKP.Next please complete the following chapters:[Post Goods Receipt](#unique_13) [page ] 19[Perform Material Inspection](#unique_14) [page ] 20 (for header material)[Refund Customer with Credit Memo](#unique_24) [page ] 24 |  |
|  | Option 2: Execute Refund with Credit Memo Immediately | On the top right corner of the screen, choose Follow-up Activities, maintain the following data and choose Back:Follow-Up Activity: Receive into Plant (0001)Product Received: XOn the Edit Returns Order screen, in the Item area, in the Refund Details column, enter the following data or action:Refund Type: Credit MemoRefund Code: 10%(select from dropdown list)Refund Control: Create Credit MemoChoose Save and Release. | Returns order is released.Subsequent documents are generated in background including:Returns deliveryGoods receipt of returns deliveryCredit memoNext please complete the following chapter:[Perform Material Inspection](#unique_14) [page ] 20 (for header material) |  |
|  | Option 3: Execute Refund with Replacement Order Immediately | On the top right corner of the screen, choose Follow-up Activities, check Receive into Plant (0001) is maintained in the Follow-Up Activity column, choose Back.On the Edit Returns Order screen, in the Item area, in the Refund Details column, enter the following data or action:Refund Type: Replacement ProductRefund Control: Create Replacement OrderChoose Save and Release. | Returns order is released.Subsequent documents are generated in background including:Returns deliveryReplacement order (SDF)Next please complete the following chapter:[Post Goods Receipt](#unique_13) [page ] 19[Perform Material Inspection](#unique_14) [page ] 20 (for header material)[Refund Customer with Replacement Material (Optional)](#unique_25) [page ] 26 |  |
|  | Option 4: Execute Refund with Immediate Delivery | On the top right corner of the screen, choose Follow-up Activities, maintain the following data and choose Back.Follow-Up Activity: Receive into Plant (0001)Product Received: XOn the Edit Returns Order screen, in the Item area, in the Refund Details column, enter the following data or action:Refund Type: Replacement ProductRefund Control: Immediate DeliveryChoose Save and Release. | Returns order is released.Subsequent documents are generated in background including:Returns deliveryGoods receipt of returns deliveryReplacement order (SDF)Outbound delivery for replacement order (SDF)Goods Issue for SDFNext please complete the following chapters:Perform Material Inspection (for component materials)Refund Customer with Replacement Material – Create Pro-forma InvoiceRefund Customer with Replacement Material – Create Customer Invoice |  |
|  | Option 5: Decide Refund Later, choose Credit Memo as Temporary Refund Type | On the top right corner of the screen, choose Follow-up Activities, check Receive into Plant (0001) is maintained in the Follow-Up Activity column, choose Back.On the Edit Returns Order screen, in the Items area, enter the following data or action:Refund Type: Credit MemoRefund Code: 10%(select from dropdown list)Refund Control: Decide LaterChoose Save and Release. | Returns order is released.Returns delivery is generated automatically. |  |
|  | Option 6: Decide Refund Later, Choose Replacement Product as Temporary Refund Type | On the top right corner of the screen, choose Follow-up Activities, check Receive into Plant (0001) is maintained in the Follow-Up Activity column, choose Back.In the Items area, enter the following data or action:Refund Type: Replacement ProductRefund Control: Decide LaterChoose Save and Release. | Returns order is released.Returns delivery is generated automatically. |  |
| 2 | Check Process Flow | On the Manage Customer Returns screen, choose arrow at end of the item. | The Display Returns Order screen displays. |  |
|  |  | In the Process Flow area, check dependent documents in process flow.Make a note of the follow-up document numbers for further use:__________. | The dependent documents display. |  |

CPFH (logistics on Item Level and pricing/billing on Header Level)

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Option 1: Execute Refund with Credit Memo Request Immediately | On the top right corner of the screen, choose Follow-up Activities, check Receive into Plant (0001) is maintained in the Follow-Up Activity column, choose Back.On the Edit Returns Order screen, in the Item area, in the Refund Details column, enter the following data or action:Refund Type: Credit MemoRefund Code: 10%(select from dropdown list)Refund Control: Create Credit Memo RequestChoose Save and Release. | Returns order is released.Returns delivery and credit memo request are generated automatically.If returns order workflow is activated, next need to perform returns order approval process, details refer to the chapter Process Returns Order Approval in test script BKP.Next please complete the following chapters:[Post Goods Receipt](#unique_13) [page ] 19[Perform Material Inspection](#unique_14) [page ] 20 (for component materials)[Refund Customer with Credit Memo](#unique_24) [page ] 24 |  |
|  | Option 2: Execute Refund with Credit Memo Immediately | On the top right corner of the screen, choose Follow-up Activities, maintain the following data and choose Back.Follow-Up Activity: Receive into Plant (0001)Product Received: XOn the Edit Returns Order screen, in the Item area, in the Refund Details column, enter the following data or action:Refund Type: Credit MemoRefund Code: 10%(select from dropdown list)Refund Control: Create Credit MemoChoose Save and Release. | Returns order is released.Subsequent documents are generated in background including:Returns deliveryGoods receipt of returns deliveryCredit memoNext please complete the following chapters:[Perform Material Inspection](#unique_14) [page ] 20 (for component materials) |  |
|  | Option 3: Decide Refund Later | On the top right corner of the screen, choose Follow-up Activities , check Receive into Plant (0001) is maintained in the Follow-Up Activity column, choose Back.On the Edit Returns Order screen, in the Items area, enter the following data or action:Refund Type: Credit MemoRefund Code: 10%(select from dropdown list)Refund Control: Decide LaterChoose Save and Release. | Returns order is released.Returns delivery is generated automatically. |  |
| 2 | Check Process Flow | On the Manage Customer Returns screen, choose arrow at end of the item. | The Display Returns Order screen displays. |  |
|  |  | In the Process Flow area, check dependent documents in process flow.Make a note of the follow-up document numbers for further use:__________. | The dependent documents display. |  |

DISH (Logistics on Header Level and Pricing/Billing on Item Level)

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Option 1: Execute Refund with Credit Memo Request Immediately | On the top right corner of the screen, choose Follow-up Activities, check Receive into Plant (0001) is maintained in the Follow-Up Activity column, choose Back.On the Edit Returns Order screen, in the Item area, in the Refund Details column, enter the following data or action:Refund Type: Credit MemoRefund Code: 10%(select from dropdown list)Refund Control: Create Credit Memo RequestChoose Save and Release. | Returns order is released.Returns delivery and credit memo request are generated automatically.If returns order workflow is activated, next need to perform returns order approval process, details refer to the chapter Process Returns Order Approval in test script BKP.Next please complete the following chapters:[Post Goods Receipt](#unique_13) [page ] 19[Perform Material Inspection](#unique_14) [page ] 20 (for component materials)[Refund Customer with Credit Memo](#unique_24) [page ] 24 |  |
|  | Option 2: Execute Refund with Credit Memo Immediately | On the top right corner of the screen, choose Follow-up Activities, maintain the following data and choose Back.Follow-Up Activity: Receive into Plant (0001)Product Received: XOn the Edit Returns Order screen, in the Item area, in the Refund Details column, enter the following data or action:Refund Type: Credit MemoRefund Code: 10%(select from dropdown list)Refund Control: Create Credit MemoChoose Save and Release. | Returns order is released.Subsequent documents are generated in background including:Returns deliveryGoods receipt of returns deliveryCredit memoNext please complete the following chapters:[Perform Material Inspection](#unique_14) [page ] 20 (for component materials) |  |
|  | Option 3: Decide Refund Later | On the top right corner of the screen, choose Follow-up Activities, check Receive into Plant (0001) is maintained in the Follow-Up Activity column, choose Back.On the Edit Returns Order screen, in the Items area, enter the following data or action:Refund Type: Credit MemoRefund Code: 10%(select from dropdown list)Refund Control: Decide LaterChoose Save and Release. | Returns order is released.Returns delivery is generated automatically. |  |
| 2 | Check Process Flow | On the Manage Customer Returns screen, choose arrow at end of the item. | The Display Returns Order screen displays. |  |
|  |  | In the Process Flow area, check dependent documents in process flow.Make a note of the follow-up document numbers for further use:__________. | The dependent documents display. |  |

### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When the returned material is received physically, goods receipt is posted for returns delivery. This process step shows you how to post a goods receipt.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). | The Change Outbound Delivery screen displays. |  |
| 3 | Enter Outbound Delivery Number | Make the following entry and choose Enter .Outbound Delivery: <delivery number created previously> |  |  |
| 4 | Post Good Receipt | Choose Post Goods Receipt. | The goods receipt is posted, statistical confirmation is generated. |  |

### Perform Material Inspection

The material inspection takes place after the returned goods have been received in the warehouse. The further handling of the returned goods is decided.

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

Goods receipt is done for returns delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Receiving Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Enter Inspection Results - From Warehouse (MSR_INSPWH). | The Worklist Selection of Deliveries screen displays. |  |
| 3 | Maintain Selection Criteria | Enter the following entries and choose Execute:Delivery Items Waiting for Inspection: <select>Delivery: <enter returns delivery number> | The Change: Material Inspection in Warehouse for Delivery screen displays. |  |
| 4 | Choose Item Tab | Choose Item tab. |  |  |
| 5 | Maintain Inspection Result | In the Inspection Result subarea, enter the following data, and press Enter:Inspection Code: <enter inspection code>Inspected Quantity: <enter inspected quantity>If the Confirmation of Redetermination dialog box appears, choose Yes to confirm. |  |  |
| 6 | Maintain Follow-up Activity | In the Logistical Follow-up subarea, enter the following data and press Enter:Follow-up Activity: <enter follow-up activity>Note Choose appropriate follow-up activity according to inspection code. For example, choose follow-up activity Transfer to Free Available Stock responding to inspection code 0001. |  |  |
| 7 | Check Inspection Status | On the Header tab, in the Basic Data subarea, Inspection Status shows Inspected, which means all received materials are inspected completely. | All received materials are inspected completely. |  |
| 8 | Save and Confirm | Choose Save and Confirm. | Inspection result is recorded, and goods movement is posted accordingly. |  |

### Determine Refund

Purpose

In this activity, refund decision is made or checked: either refund the customer with a credit memo or compensate with a replacement product.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Returns and Refund Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer Returns (F1708). | The Manage Customer Returns screen displays. |  |
| 3 | Search for Returns Order | Choose Show Filter Bar if it is hidden. Enter the following data and choose Go:Returns Order: <returns order number 6XXXXXXX> | Returns order is found and displayed. |  |
| 4 | Navigate to Determine Refund Screen | Select the returns order entry and choose Determine Refund. | The Determine Refund screen displays. |  |
| 5 | Check Refund Progress | In the upper area, check percentage number in the Refund Progressfield and then take next action accordingly:If <100%: Refund determination is not completed. Go to Section A and then Section B.If 100%: Refund determination is completed. Skip Section A and go to Section B. |  |  |
| Section A: Refund Determined with Reference to Material Inspection Results | Option 1: Credit Memo | On the Items to Be Refunded tab, choose Change Refund in the Refund Details column for the return item.Enter the following data:Refund Type: Credit MemoExtent of Refund: <10% Refund>Note Currently, only refund type 100% refund (100) is supported for Brazil.Choose OK.Select the item and choose Release Selected Items. | Refund setting is maintained, and credit memo request document is created in background. |  |
|  | Option 2: Product Replacement (only possible for LUMF component) | On the Items to Be Refunded tab, choose Change Refund in Refund Details column for the return item.Enter the following data:Refund Type: Replacement ProductReplacement Product: <Material>Supplying Plant:Replacement UoM: <Quantity> / PCChoose OK.Select the item and choose Release Selected Items. | Refund setting is maintained, and replacement order document is created in background. |  |
| Section B: Check Refund Determination Result | Check Refund Results | On the Completed Items tab, refund result is displayed. Follow-up document number is shown in Refund Details column. Make a note of document number for further use. You can click the created document number to check detailed information. | The refund result displays. |  |

### Display Returns Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check the progress of returns process. All dependent documents are available in process flow.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Returns and Refund Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer Returns (F1708). | The Manage Customer Returns screen displays. |  |
| 3 | Search for Returns Order | Choose Show Filter Bar if it is hidden. Enter the following data and choose Go:Returns Order: <returns order number 6XXXXXXX> | Returns order is found and displayed. |  |
| 4 | Order Overview | Choose the created returns order number 6XXXXXXX and choose Display Customer Return. | The Display Standard Return 6XXXXXXX: Overview screen displays. |  |
| 5 | Document Flow | On the Returns tab, choose Returns Overview in the Returns Control area. | The Returns Overview for Returns Order 6XXXXXXX - 10 screen displays. |  |
| 6 | Check Document Flow | In Document Number column, make a note of follow-up document number(s) of credit memo request or replacement order (subsequent delivery free of charge) for further use. |  |  |

|  |
| --- |
| Note After you have completed this activity:Option A: If credit memo request is generated, go to the Refund Customer with Credit Memo chapter.Option B: If replacement order is generated, go to the Refund Customer with Replacement Material chapter. |

### Refund Customer with Credit Memo

#### Create Credit Memo

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

Table 3: Create Billing Document

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Document screen displays. |  |
| 3 | Define Billing Setting | Choose Billing Settings.Switch on the following settings:Set billing date and type before billingCreate separate billing document for each item of billing due listAutomatically post billing documentsDisplay billing document after creation |  |  |
| 4 | Search for Billing List | In the search condition, enter criteria if necessary. | SD document(s) display(s) in the result. |  |
| 5 | Choose SD Document | Select the row of credit memo request document recorded previously and choose Create Billing Documents. | The Create Billing Documents screen displays. |  |
| 6 | Maintain Billing Type and Date | Choose billing type Credit Memo (G2) and maintain billing date, such as the current date, and then choose OK. | The draft billing document with ID Sxxxxxxxx displays. |  |
| 7 | Save Billing Document | On the Manage Billing Documents screen, choose Save. The draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx. Make a note of the billing document number: __________. | Final credit memo is generated. |  |

Manage Billing Documents

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access the App | Open Manage Billing Documents(F0797). | The Manage Billing Documents screen displays. |  |
| 2 | Search Billing Document | Enter the billing document number recorded previously in the Billing Document field, and press Enter. | The billing document which is created previously displays. |  |
| 3 | Display Billing Document | Select the billing document item, and choose Display. | The billing document displays. |  |
| 4 | Check Output Condition | On the Billing Document screen, go to the last assignment block, Output Items. | There is one entry in the item and the output type is BILLING_DOCUMENT. |  |
| 5 | Display Print Preview | On the Billing Document screen, choose Preview. | Preview for PDF document displays. |  |
| 6 | Cancel Billing Document (Optional) | On the Billing Document screen, select a certain billing document and choose Cancel Billing Document. | A log displays the following message: Billing Document Canceled. |  |
| 7 | Update New Attachment (Optional) | In the Edit mode, you can add, delete, and update the attachments. Save your changes by choosing Save in the footer bar. |  |  |
| 8 | Update New Text (Optional) | In the Edit mode, you can add, delete and update the texts. Save your changes by choosing Save in the footer bar. |  |  |

### Refund Customer with Replacement Material (Optional)

Note

This chapter is only relevant for LUMF component.

#### Create Free-of-Charge Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a free-of-charge delivery with reference to SDF (replacement order) document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Outbound Deliveries - From Sales Orders (F0869A). | The Create Outbound Deliveries - From Sales Orders screen displays. |  |
| 3 | Search Sales Order | Make the following entries and choose Go:Shipping Point: 1010Planned Creation Date: <delivery selection date>Order: <replacement order number created previously> |  |  |
| 4 | Create Delivery | Select your replacement order item(s) and choose Create Deliveries. |  |  |
| 5 | Check Details | Choose Display Log. | The Analyze Delivery Log screen displays. Delivery is created successfully with delivery number shown on the Deliveries tab. |  |

#### Execute Picking

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
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Choose Picking | Choose For Picking. |  |  |
| 4 | Enter Shipping Point | Make the following entries, and choose Execute:Shipping Point: 1010Only Picking without WM: <Check the checkbox> |  |  |
| 5 | Change Outbound Deliveries | On the Day’s Workload for Picking screen, select your delivery note and choose Change Outbound Deliveries. |  |  |
| 6 | Enter Picked Quantity | On the Picking tab, enter the following data:Picked Qty: <Equal to delivery Qty> |  |  |
| 7 | Enter | Press Enter. |  |  |
| 8 | Save | Choose Save. | The delivery is picked. |  |

#### Post Goods Issue

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
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Choose Good Issue | Choose For Goods Issue. |  |  |
| 4 | Enter Shipping point | Make the following entries and choose Execute:Shipping Point: 331A |  |  |
| 5 | Post Goods Issue | Mark the relevant delivery and choose Post Goods Issue. Select today’s date and choose Continue in the dialog box. | The goods issue is posted |  |

Financial Postings

| Material | Debited Account | Credited Account | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 54083000Inv Chg COGS w/CE | 13600000Inventory TradingGd | none |

Printing Form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Outbound Delivery(VL03N). | The Display Outbound Delivery(VL03N) screen displays. |  |
| 3 | Issue Delivery Output | On the Display Outbound Delivery(VL03N) screen, enter the Delivery number and choose Continue. From the Delivery xxxxxxxx Display: Overview screen, choose Menu > Extras > Delivery Output > Output Control . | The Delivery: Output screen is displayed. |  |
| 4 | Print Preview | On the Delivery: Output screen, select the line with the Output Type Delivery Note and choose Display PDF Document. | A preview of the print document is displayed. |  |
| 5 | Print Delivery Note | From the preview of the document, choose Print. | The delivery note is posted. |  |

#### Create Pro-forma Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a pro-forma invoice with reference to delivery.

|  |
| --- |
| Note Pro-forma invoice is not applicable for Brazil. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Documents(F0798) screen displays. |  |
| 3 | Define Billing Setting | Choose Billing Settings. Turn all of these settings into ON and choose OK:Enter billing data before billingSeparate billing documents for each billing due list itemAutomatically post billing documentsDisplay billing document after creation |  |  |
| 4 | Search for Billing List | In the search condition, use criteria if necessary. | Sales document(s) displays in the result. |  |
| 5 | Choose Individual Billing Document | Select the row of delivery document created previously and choose Create Billing Documents. |  |  |
| 6 | Maintain Billing Type and Billing Date | Choose the billing type Pro Forma Invoice for Delivery (F8) and billing date, such as the current date, then choose OK. | The draft billing document with ID Sxxxxxxxx displays. |  |
| 7 | Save Billing Document | On the Manage Billing Documents screen, choose Save. The draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx. Make a note of the billing document number: __________. | Pro-forma invoice is generated. |  |

Alternatively, it is supported to create pro-forma (type F5) with reference to replacement order.

#### Create Customer Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create ‘F2’ type of invoice, and costs are transferred to accounting accordingly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Documents(F0798) screen displays. |  |
| 3 | Define Billing Setting | Choose Billing Settings. Turn all of these settings into ON and choose OK:Enter billing data before billingSeparate billing documents for each billing due list itemAutomatically post billing documentsDisplay billing document after creation |  |  |
| 4 | Search for Billing List | In the search condition, use criteria if necessary. | Sales document(s) displays in the result. |  |
| 5 | Choose Individual Billing Document | Select the row of delivery document created previously and choose Create Billing Documents. |  |  |
| 6 | Maintain Billing Type and Billing Date | Choose billing type Invoice (F2) and maintain Billing date, such as the current date, and then choose OK. | The draft billing document with ID Sxxxxxxxx displays. |  |
| 7 | Save Billing Document | In the Manage Billing Documents screen, choose Save. The draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx. Make a note of the billing document number: __________. | Customer invoice is generated. |  |

Financial Postings

| Material | Debited Accounts | Credited Accounts |
| --- | --- | --- |
| Trading Good (HAWA) | 44002000Sales Disc Domestic | 41000000Rev Domestic Prod |

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

In this process step, you can schedule a background job for creating outbound deliveries.

This app can be used as an alternative instead of the manual creation of outbound deliveries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Delivery Creation (F2228). | The Application Jobs screen displays. The app automatically shows the history of application jobs. |  |
| 3 | Create Delivery Creation Schedule | Choose New to define a new job. | The New Job screen is displayed. Job Template should default as Schedule Delivery Creation. |  |
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary, then choose Check. | The system displays the message: Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A delivery creation job is scheduled. Screen goes back to Application Jobs. |  |
| 6 | Check Delivery Creation Job Log | On the Application Jobs screen, after job item’s status turned to Finish, choose Status symbol in the Log column.Note Choose the Magnifier, and the job list will refresh. | Screen goes to job log details. |  |

#### Job Scheduling for Goods Issue Deliveries (Alternative)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you can schedule a background job for goods issue posting with reference to outbound deliveries.

This app can be used as an alternative instead of the manual goods issue posting for outbound deliveries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Schedule Goods Issue for Deliveries (F2259). | The Application Jobs screen displays. The app automatically shows the history of application jobs. |  |
| 3 | Create Goods Issue Deliveries Schedule | Choose New to define a new job. | The New Job screen displays. The Job Template should be defaulted as Schedule goods issue for Deliveries. |  |
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary, then choose Check. | The system displays the message: Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A schedule goods issue for deliveries job is scheduled. Screen goes back to Application Jobs. |  |
| 6 | Check Goods Issue Deliveries Job Log | On the Application Jobs screen, after job item’s status turned to Finish, choose Status symbol in the Log column.Note Choose the Magnifier, and the job list will refresh. | The job log details display. |  |

#### Job Scheduling for Billing Creation (Alternative)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you can schedule a background job for creation billing documents.

This app can be used as an alternative instead of the manual creation of billing documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Billing Creation (F1519). | The Application Jobs screen displays. The app automatically shows the history of application jobs. |  |
| 3 | Create Billing Creation Schedule | Choose New to define a new job for billing creation. | The New Job screen displays. The Job Template should be defaulted as Schedule Billing Creation. |  |
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary.Choose Check. | The system displays the message Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A billing creation job is scheduled. Screen goes back to Application Jobs. |  |
| 6 | Check Billing Creation Job Log | On the Application Jobs screen, after job item’s status turned to Finish, choose Job Log.Note Choose the Magnifier, and the job list will refresh. | The log details display. |  |

#### Job Scheduling for Billing Release (Alternative)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you can schedule a background job for release billing documents to accounting.

This app can be used as an alternative instead of the manual release to accounting for billing documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Billing Release (F1518). | The Application Jobs screen displays. The app automatically shows the history of application jobs. |  |
| 3 | Create Billing Release Schedule | Choose New to define a new job for billing creation. | The New Job screen displays. The Job Template should be defaulted as Schedule Billing Release. |  |
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary.Choose Check. | The system displays the message: Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A billing release job is scheduled. Return to Application Jobs. |  |
| 6 | Check Billing Release Job Log | On the Application Jobs screen, after job item’s status turned to Finish, choose Job Log.Note Choose the Magnifier, and the job list will refresh. | The log details display. |  |

#### Job Scheduling for Billing Output (Alternative)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you can schedule a background job for when and how billing documents are sent to customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Billing Output (F1510) | The Application Jobs screen displays. The app automatically shows the history of application jobs. |  |
| 3 | Create Billing Output Schedule | Choose New to define a new job for billing creation. | The New Job screen displays. The Job Template should be defaulted as Schedule Billing Output. |  |
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary.Choose Check. | The system displays the message: Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A billing release job is scheduled. Return to Application Jobs. |  |
| 6 | Check Billing Output Job Log | On the Application Jobs screen, after job item’s status turned to Finish, choose Job Log.Note Choose Magnifier, and the job list will refresh. | The log details display. |  |

### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| BKK-Sales Order Fulfillment Monitoring and Operations(Optional) | Using the master data from this document, complete the following activities described in the test script:Review sections: Incomplete SD Documents (Deliveries) and Review Outbound Deliveries for Goods Issue |

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
- related-to :: [[08-sales-order-management/test-script-make-to-order-production-for-sales-kits-with-variant-confi]]
- related-to :: [[08-sales-order-management/test-script-sales-order-processing-for-sales-kits-31q-ae-896]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5CX_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 66,482 chars in the whole document
