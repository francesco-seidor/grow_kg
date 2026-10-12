---
id: 08-sales-order-management/customer-returns-for-material-with-variant-configuration-7kw-ae-test-s
title: Customer Returns for Material with Variant Configuration (7KW_AE) - Test Script (7KW_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition test script for scope item 7KW: customer returns of variant-configured materials, from returns order to credit memo, with job scheduling appendix."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/customer-returns-variant-configuration]
aliases: [7KW_S4CLD2608_BPD_EN_AE]
keywords: [Customer Returns for Variant-Configured Materials, customer returns, variant configuration, returns order creation, returns order without reference, refund determination, material inspection, credit memo, returns picking and goods receipt, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7KW_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1216
topic: 08-sales-order-management/customer-returns-variant-configuration
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Customer Returns for Material with Variant Configuration (7KW_AE) - Test Script (7KW_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7KW_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Customer Returns for Variant-Configured Materials** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Customer Returns for Material with Variant Configuration (7KW_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232860892)

[2 Prerequisites 4](#_Toc232860893)

[2.1 System Access 4](#_Toc232860894)

[2.2 Roles 4](#_Toc232860895)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232860896)

[2.4 Business Conditions 6](#_Toc232860897)

[2.5 Extend Material Master Data 6](#_Toc232860898)

[3 Overview Table 8](#_Toc232860899)

[4 Test Procedures 9](#_Toc232860900)

[4.1 Create Returns Order with Reference 9](#_Toc232860901)

[4.2 Create Returns Order without Reference (Optional) 13](#_Toc232860902)

[4.3 Perform Picking 17](#_Toc232860903)

[4.4 Post Goods Receipt 18](#_Toc232860904)

[4.5 Perform Material Inspection 19](#_Toc232860905)

[4.6 Determine Refund 21](#_Toc232860906)

[4.7 Display Returns Overview 23](#_Toc232860907)

[4.8 Create Credit Memo 24](#_Toc232860908)

[5 Appendix 26](#_Toc232860909)

[5.1 Process Integration 26](#_Toc232860910)

[5.2 Scheduling Job (Alternative) 26](#_Toc232860911)

[5.2.1 Job Scheduling for Delivery Creation (Alternative) 26](#_Toc232860912)

[5.2.2 Job Scheduling for Goods Issue Deliveries (Alternative) 27](#_Toc232860913)

[5.2.3 Job Scheduling for Billing Creation (Alternative) 28](#_Toc232860914)

[5.2.4 Job Scheduling for Billing Release (Alternative) 29](#_Toc232860915)

[5.2.5 Job Scheduling for Billing Output (Alternative) 30](#_Toc232860916)

[5.2.6 Succeeding Processes 31](#_Toc232860917)

## Purpose

Overview

The scope item is dedicated to handle material with variant configuration for a customer returns process.

A configurable material using the Advanced Variant Configuration can be included in returns order. It can be single-level and multi-level configurable material. Configuration can be copied over from a sales order when created with reference or maintained during creation without reference. Sales price is calculated with condition for configurations. A returns delivery is automatically generated once the returns order is released. After goods receipt, the inspection takes place at the warehouse and final logistical follow up is decided. Refund can be determined either directly when releasing the returns order, or after the inspection. Compensation to customer by credit memo is available.

Please refer to KBA [3670579](https://me.sap.com/notes/3670579) - [Overview] 7KW: Customer Returns for Material with Variant Configuration in S/4HANA Cloud Public Edition for the known limitations and issues.

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
| Returns and Refund Clerk | SAP_BR_RETURNS_REFUND_CLERK | Customer Returns | SAP_BR_RETURNS_REFUND_CLERK |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Receiving Specialist | SAP_BR_RECEIVING_SPECIALIST | Receiving | SAP_BR_RECEIVING_SPECIALIST |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |

### Master Data, Organizational Data, and Other Data

SAP Best Practices Standard Values based on new global template will be used once available. In the table you still see the master data used for the current baseline.

Essential master and organizational data were created in your SAP S/4HANA system in the implementation phase, such as the data that reflects the organizational structure of your company and master data that suits its operational focus, for example, master data for materials, vendors, and customers.

This master data consists of standardized SAP Best Practices default values, and enables you to go through the process steps of this scope item.

|  |
| --- |
| Note Additional Master Data (Default Values)You can test the scope item with other SAP Best Practices default values that have the same characteristics. |

Check your SAP system to find out which other material master data exists.

|  |
| --- |
| Note Using Your Own Master DataYou can also use customized values for any material or organizational data for which you have created master data. |

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | CM-FL-V00 | Configurable Forklifter |  |
| Material | CM-MLFL-KM-VXX | Multilevel Forklifter |  |
| Material | CM-FL-V00-3P | Forklift for 3rd Party |  |
| Sold-to Party | 33100001 | Domestic DE Customer 1 |  |
| Ship-to Party | 33100001 | Domestic DE Customer 1 |  |
| Payer | 33100001 | Domestic DE Customer 1 |  |
| Plant | 3310 |  |  |
| Storage Location | 331A331R |  |  |
| Shipping Point | 3310331R |  |  |
| Sales Organization | 3310 |  |  |
| Distribution Channel | 10 |  |  |
| Division | 00 |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| 2T7 | Create Product Master of Type "Configurable Material" - MDS |
| BND | Create Customer Master - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| 1YT - Make-to-Order Production with Variant Configuration | You have completed the steps described in the Test Script 1YT - Make-to-Order Production with Variant Configuration, note down created sales order number and billing number for further use. |
| 4R6 - Sales Processing using Third-Party with Variant Configuration | You have completed the steps described in the Test Script 4R6 - Sales Processing using Third-Party with Variant Configuration, note down created sales order number and billing number for further use. |

### Extend Material Master Data

Purpose

In this step, the storage location data in 331R is created for material CM-MLFL-KM-VXX.

Procedure

Complete the chapter Create Product Master Data - Storage Location Data in the master data script 2T7 - Create Product Master of Type "Configurable Material" using the following data:

| Material | Plant | Storage Location |
| --- | --- | --- |
| CM-MLFL-KM-VXX | 3310 | 331R |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Returns Order with Reference](#unique_9) [page ] 9 | Returns and Refund Clerk | Manage Customer Returns - Version 2 (F4832) | Returns order is created. |
| [Create Returns Order without Reference (Optional)](#unique_10) [page ] 13 | Returns and Refund Clerk | Create Customer Return Without Reference VA01 | Returns order is created. |
| [Perform Picking](#unique_11) [page ] 17 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Picking is done for the returns delivery. |
| [Post Goods Receipt](#unique_12) [page ] 18 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | The goods receipt is posted for returns delivery. |
| [Perform Material Inspection](#unique_13) [page ] 19 | Receiving Specialist | Enter Inspection Results - From Warehouse (MSR_INSPWH) | Inspection results are recorded. |
| [Determine Refund](#unique_14) [page ] 21 | Returns and Refund Clerk | Manage Customer Returns - Version 2 (F4832) | Refund determination is checked or triggered. |
| [Display Returns Overview](#unique_15) [page ] 23 | Returns and Refund Clerk | Manage Customer Returns - Version 2 (F4832) | Document flow is displayed. |
| [Create Credit Memo](#unique_16) [page ] 24 | Billing Clerk | Create Billing Documents (F0798) | Credit memo is created. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

The test should take around example, 60 minutes. The Enterprise search function provides a central entry point for finding business objects in your company from different sources using a single search request, such as: Apps, fact sheets for business objects. From the data found, you can go directly to the respective apps and fact sheets to display, edit the data or find related objects.

How to access and check a fact sheet:

- Log on to the SAP Fiori Launchpad using the respective user example, Internal Sales Representative.
- Access the Enterprise Search Bar and choose the magnifying glass button in the upper right corner.
- The Enterprise Search bar is displayed, two filter fields appear left to the search button. Enter your search criteria and choose the business object type, example: Customer Returns from dropdown menu in first field, enter customer returns order number in second field and choose Search, The sales order is listed.
- Choose the sales order number link, the system navigates to fact sheet screen and returns order-related information is integrated and summarized in one Fiori page. You can get detailed data via choosing the corresponding links.

There are fact sheets available for the following objects (Visible depending on the assigned role):

- Sales (return) order
- Quotation
- Billing document
- Credit Memo
- Debit Memo
- Customer 360 Fact sheet

### Create Returns Order with Reference

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a returns order with reference to sales order or billing document.

Prerequisite

You must have billing document or sales order as reference (refer to Business Conditions chapter).

|  |
| --- |
| Note Please ensure that the following default item categories are maintained for sales order types CBAR and GA2 in SSCUI 102807 - Assign Item Categories before you create returns order:Sales Document TypesItem Category GroupDefault Item CategoryCBAR0002REVCGA20002GAVC |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Returns and Refund Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer Returns - Version 2 (F4832). | The Manage Customer Returns - Version 2 screen displays. |  |
| 3 | Create Returns Order | Choose Create with Reference, then choose Create from Invoice.Note System also supports to create CBAR order for below cases:From sales order: click Create with Reference, then choose Create from Sales Order.From sales order without charge: click Create with Reference, then choose Create from Sales Order Without Charge. | The Create from Invoice pop-up screen displays. |  |
| 4 | Maintain Data | Enter the following data and then choose Select Items.Returns Order Type: Standard Return (CBAR)Invoice: <Billing document number created previously> |  |  |
| 5 | Maintain Returned Quantity | Select the item(s) to be returned and enter the return quantity, then choose Continue. |  |  |
| 6 | Enter Item Data | Under tab General Information, enter the following data:Return Order Reason: for example, Standard Return(009)Under tab Items, enter the following data:Return Reason: for example, Product damaged (003)Follow-Up Activity: for example, Receive into Plant (0001)Note For material CM-FL-V00-3P, you can choose the following follow-up activities:Ship to Supplier (0005):Refer to the chapter Scenario 3: Goods are Returned to Supplier via Seller in test script BKP - Customer Returns and complete all activities.Direct Shipment to Supplier (0007):Refer to test script 1Z3 - Customer Returns with Direct Shipment from Customer to Supplier and complete all activities.Choose the arrow button at the end of the item. | The Returns Order Item screen displays. |  |
| 7 | Choose One of the Following Options to Continue | The user can influence the point in time when the refunding document must be created: Either immediately when the returns order is saved and released or at a later point of time. Combination of the refund setting determines follow-up document creation. |  |  |
| 7a | Option 1: Execute Refund with Credit Memo Request Immediately | In the Refund section, enter the following data:Refund Type: Credit MemoRefund Code: <select one from down-drop list>, for example, 10%Note Refund deduction (condition type DRE1) is determined automatically based on the refund code entered.The following steps guide you how to define more refund codes and related condition records:Define returns refund codes via SSCUI 104235.Maintain condition records for DRE1 using the Set Material Prices – Sales app. For more details, refer to master data script Create Sales Pricing Condition - MDS (BET).Refund Control: Create Credit Memo RequestIf Accept Recommendations dialog box appears, choose Accept and Apply or other button according to your requirements. |  |  |
| 7b | Option 2: Refund on Hold | In the Refund section, enter the following data:Refund Type: Credit MemoRefund Code: <Select one from dropdown list>, for example, 10%Refund Control: Decide LaterIf Accept Recommendations dialog box appears, choose Accept and Apply or other button according to your requirements |  |  |
| 7c | Option 3: Execute Refund with Credit Memo | Enter the following data:In the Follow-Up Activity section:Product Received: XIn the Refund section:Refund Type: Credit MemoRefund Code: 10% (select from dropdown list)Refund Control: Create Credit MemoIf Accept Recommendations dialog box appears, choose Accept and Apply or other button according to your requirements |  |  |
| 8 | Check Pricing | In the Prices section, pricing of variant components displays.Check the condition value of condition type PVA0.Choose Apply. |  |  |
| 9 | Save Returns Order | Choose Save and Release. | Returns order is created.Returns delivery is generated automatically.More subsequent documents are generated automatically according to different refund cases:Option 1: Execute Refund with Credit Memo Request ImmediatelyCreate Credit MemoOption 3: Execute Refund with Credit MemoGoods receipt of returns deliveryCredit memoNext please complete the following chapter: Perform Material Inspection. |  |
| 10 | Check Process Flow | Under the Process Flow tab, check dependent documents in process flow. Make a note of the follow-up document numbers for further use. |  |  |
| 11 | Review Characteristic Value | In Process Flow table, click standard return 6XXXXXXXX, then choose Display Customer Return.On Display Standard Return 6XXXXXXX: Overview screen, select the item and choose Item Details: Configuration, the value for characteristics is displayed. |  |  |

Printing form - Output Management

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Returns and Refund Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer Returns - Version 2 (F4832). | The Manage Customer Returns - Version 2 screen displays. |  |
| 3 | Search for Returns Order | Enter search terms in filter bar and choose Go.For example, enter returns order number in Returns Order field. | Returns order is displayed in result list. |  |
| 4 | Check Output Condition | Choose the arrow at end of returns order item.On Returns Order screen, choose tab Output Items, output entry displays, click Open File in column Display. | The PDF document displays.The variant pricing, and configuration are displayed. |  |

### Create Returns Order without Reference (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a returns order without reference.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Returns and Refund Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Customer Return Without Reference VA01. | The Create Sales Documents screen displays. |  |
| 3 | Enter Organizational Data | Enter the following data and choose Continue:Order Type: CBARSales Organization: 3310Distribution Channel: 10Division: 00 | The Create from Invoice pop-up screen displays. |  |
| 4 | Enter Order Details | Enter the following data and choose Enter.Sold-to Party: for example, 33100001On the Sales tab:Order Reason: for example, Standard Return (009)On the Returns tab:Material: <Material>Order Quantity: <Quantity> |  |  |
| 5 | Enter Characteristic Value | Choose value for characteristics below and choose Done.For material CM-FL-V00:Fork Size: <Small>Power Source: <Combustion, Electrical>Lifter Model: <Heavy, Standard>Wheel Type: <Cushion Tires, Pneumatic Tires>CR_SIZE: <Small, Medium, Large>Counterweight: <5.000 kg>AVC Count: <one, two, three>Battery Capacity(Ah): <50, 80, 140>Net Value: Varies according to characteristic valueFor material CM-MLFL-KM-VXX:On the Default Group tab:Lifter Model: <Heavy, Standard>Power Source: <Combustion>CR_SIZE: <Small, Medium, Large>AVC Count: <one, two, three>On the Technical tab:Fork Size: <Small, Normal, Large>Wheel Type: <Cushion Tires, Pneumatic Tires>The combination of value for characteristic is constrained by Constraint Net. Only the following combinations are acceptable.Combination One:Lifter Model: HeavyPower Source: CombustionCounterweight (KG): <5.000> is filled in automaticallyWheel Type: Cushion Tires or Pneumatic TiresFork Size: Small or Medium or LargeCombination Two:Lifter Model: StandardPower Source: CombustionWheel Type: Cushion Tires is filled in automatical-lyFork Size: Small or Normal or LargeCounterweight (KG): 1.000 or 2.000Combination Three:Lifter Model: StandardPower Source: ElectricalWheel Type: Cushion Tires is filled in automaticallyFork Size: Small or Normal or LargeCounterweight (KG): 1.000 or 2.000Battery Capacity (Ah): 50 or 80 or 140 (140 only available when fork size is L)Choose Toggle Structure Panel icon on the top right corner.Choose product SF-FL-FORKSEAT-VXX in the Configuable item panel.Choose value for the following characteristic and choose Done.Seat Color: Black, White or GreySeat Type: Standard, Heavy Duty, or Air suspensionNote Heavy Duty is only selectable if the fork lifter model is Heavy. |  |  |
| 6 | Check Pricing | Double-click sales order item and select Conditions tab. Pricing of variant components displays.Check the condition value of condition type PVA0.Choose Back. |  |  |
| 7 | Choose One of the Following Options to Continue | The user can influence the point in time when the refunding document must be created: Either immediately when the returns order is saved and released or at a later point of time. Combination of the refund setting determines follow-up document creation. |  |  |
| 7a | Option 1: Execute Refund with Credit Memo Request Immediately | In the Create Standard Return: Overview screen, on the Returns tab, enter the following data:Return Reason: for example, Product damagedFollow-Up Act: for example, 0001 Receive into PlantRefund Type: Credit MemoRefund Code: <select one from dropdown list>, for example, 10%Refund Control: Create Credit Memo Request |  |  |
| 7b | Option 2: Refund on Hold | In the Create Standard Return: Overview screen, on the Returns tab, enter the following data:Return Reason: for example, Product damagedFollow-Up Act: for example, 0001 Receive into PlantRefund Type: Credit MemoRefund Code: <select one from dropdown list>, for example, 10%Refund Control: Decide Later |  |  |
| 7c | Option 3: Execute Refund with Credit Memo | In the Create Standard Return: Overview screen, on the Returns tab, enter the following data:Return Reason: for example, Product damagedFollow-Up Act: for example, 0001 Receive into PlantMaterial Received: XRefund Type: Credit MemoRefund Code: 10% (select from dropdown list)Refund Control: Create Credit Memo |  |  |
| 8 | Save Returns Order | Choose Save. | Returns order is created.Returns delivery is generated automatically.More subsequent documents are generated automatically according to different refund cases:Option 1: Execute Refund with Credit Memo Request ImmediatelyCredit memo requestOption 3: Execute Refund with Credit MemoGoods receipt of returns deliveryCredit memoNext please complete the following chapter: Perform Material Inspection. |  |

Printing form - Output Management

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Returns and Refund Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer Returns - Version 2 (F4832). | The Manage Customer Returns - Version 2 screen displays. |  |
| 3 | Search for Returns Order | Enter search terms in filter bar and choose Go.For example, enter returns order number in Returns Order field. | Returns order is displayed in result list. |  |
| 4 | Check Output Condition | Choose the arrow at end of returns order item.On Returns Order screen, choose tab Output Items, output entry displays, click Open File in column Display. | The PDF document displays.The variant pricing, and configuration are displayed. |  |

### Perform Picking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, picking is done for returns delivery created previously. This process step shows you how to perform picking.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Choose Picking | Choose For Picking. |  |  |
| 4 | Enter Shipping Point | Make the following entries and choose Execute:Shipping Point: 331R |  |  |
| 5 | Change Outbound Deliveries | On the Day’s Workload for Picking screen, select your delivery number and choose Change Outbound Deliveries. |  |  |
| 6 | Enter Picked Quantity | On the Picking tab, input quantity equal to delivery quantity in the Picked Qty field. |  |  |
| 7 | Choose Enter | Press Enter. |  |  |
| 8 | Save | Choose Save. | The delivery is picked. |  |

### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When the returned material is received, goods receipt is posted for returns delivery. This process step shows you how to post a goods receipt.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Choose Goods Issue | Choose For Goods Issue. |  |  |
| 4 | Enter Shipping Point | Make the following entries and choose Execute:Shipping Point: 331R |  |  |
| 5 | Post Goods Receipt | Mark the relevant delivery and choose Post Goods Issue. Choose date of today from the dialog box. | The goods receipt is posted. |  |

### Perform Material Inspection

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
| 4 | Choose Item Tab | Choose Item tab. |  |  |
| 5 | Inspection Split (Optional) | If different inspection results need to be recorded for the same delivery item, perform below actions, otherwise you can directly skip this step.Select the delivery item and choose Create Split Item, then run steps 5-6 for all inspection items. |  |  |
| 6 | Maintain Inspection Result | In the Inspection Result subarea, enter the following data, and press Enter:Inspection Code: <enter inspection code>Inspected Quantity: <enter inspected quantity>If the Confirmation of Redetermination dialog box appears, choose Yes to confirm.For send back to customer scenario, Inspection Code: 0004 Decision not possible. |  |  |
| 7 | Maintain Follow-up Activity | In the Logistical Follow-up subarea, enter the following data and press Enter:Follow-up Activity: <enter follow-up activity>Note Choose appropriate follow-up activity according to inspection code. For example, choose follow-up activity Transfer to Free Available Stock responding to inspection code 0001.Choose suitable Follow-Up Activity from below options according to your subsequent scenarios:0011 Transfer to Free Available Stock0012 Transfer to Scrap0015 Transfer to Specified Stock0018 Transfer to Scrap for Customer0023 goods receipt quantity correction0031 No Further Activities |  |  |
| 8 | Check Inspection Status | On the Header tab, in the Basic Data subarea, Inspection Status shows Inspected, which means all received materials are inspected completely. | All received materials are inspected completely. |  |
| 9 | Save and Confirm | In menu bar at the top of screen, choose Save and Confirm.Note Do not choose Save Inspection Results at the bottom right of the screen, as subsequent material documents will not be automatically generated.Note Inventory management for configurable material in customer returns is improvable. For example, if logistical follow-up activity 0011 - Transfer to Free Available Stock is chosen during performing material inspection, the returned configurable material will be moved to anonymous stock, in such case, it is not achievable to access the variant configuration via returns order for the configurable material. | Inspection result is recorded, and goods movement is posted accordingly. |  |

### Determine Refund

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, refund decision is made or checked.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Returns and Refund Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer Returns - Version 2 (F4832). | The Manage Customer Returns - Version 2 screen displays. |  |
| 3 | Search for Returns Order | Choose Show Filter Bar to add if it is hidden. Enter the following data and choose Go:Returns Order: <returns order number 6XXXXXXX> | Returns order is found and displayed. |  |
| 4 | Navigate to Determine Refund Screen | Select the returns order entry and choose Determine Refund. | The Determine Refund screen displays. |  |
| 5 | Check Refund Progress | In the upper area, check percentage number in the field Refund Progress and then take next action accordingly:<100%: Refund determination is not completed. Go to Section A and then Section B.100%: Refund determination is completed. Skip Section A and go to Section B. |  |  |
| Section A: Refund is determined with reference to product inspection results | Create Credit Memo | On the Items to Be Refunded tab, choose Change Refund in the Refund Details column for the return item.Enter the following data:Refund Type: Credit MemoRefund Code: <a percentage number>, for example, 10% RefundChoose OK.Select the item and choose Release Selected Items. | Refund setting is maintained, and credit memo request document is created in background. |  |
| Section B: Check refund determination result | Check refund results | On the Completed Items tab, refund result is displayed. Follow-up document number is shown in Refund Details column. Make a note of document number for further use. You can click the created document number to check detailed information. | The refund result displays. |  |

|  |
| --- |
| Note 7KW does not support material replacement for configurable material. |

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
| 2 | Access the App | Open Manage Customer Returns - Version 2 (F4832). | The Manage Customer Returns - Version 2 screen displays. |  |
| 3 | Search for Returns Order | Choose Show Filter Bar if it is hidden. Enter the following data and choose Go:Returns Order: <returns order number 6XXXXXXX> | Returns order is found and displayed. |  |
| 4 | Navigate to Order Overview | Choose the arrow at end of returns order item. | The Returns Order screen displays. |  |
| 5 | Check Document Flow | Choose tab Process Flow, make a note of follow-up document number of credit memo request for further use. |  |  |

### Create Credit Memo

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
| 3 | Define Billing Setting | Choose Billing Settings.Maintain settings as below.Set Billing Data and type before billing: ONCreate separate Billing Documents for Each item of Billing Due List: ONAutomatically Post Billing Documents: ONDisplay Billing Document after creation: ONChoose delivery item to be billed and select quantities: OFF |  |  |
| 4 | Search for Billing List | In the search condition, enter criteria if necessary. | SD document(s) display(s) in the result. |  |
| 5 | Choose SD Document | Select the row of credit memo request document recorded previously and choose Create Billing Documents. | The Create Billing Documents(F0798) screen displays. |  |
| 6 | Maintain Billing Type and Date | Choose billing type Credit Memo (G2) and maintain billing date, such as the current date, and then choose OK. | The draft billing document with ID Sxxxxxxxx displays. |  |
| 7 | Save Billing Document | On the Manage Billing Documents screen, choose Save. The draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx. Make a note of the billing document number: __________. | Final credit memo is generated. |  |

Manage Billing Documents

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access the App | Open Manage Billing Documents (F0797). | The Manage Billing Documents screen displays. |  |
| 2 | Search Billing Document | Enter the billing document number recorded previously, and press Enter. | The billing document which is created previously displays. |  |
| 3 | Display Billing Document | Select the billing document item, and choose Display. | The billing document displays. |  |
| 4 | Check Output Condition | On the Billing Document screen, go to the last assignment block, Output Items. | There is one entry in the item and the output type is BILLING_DOCUMENT. |  |
| 5 | Display Print Preview | On the Billing Document screen, choose Preview. | Preview for PDF document displays. |  |
| 6 | Cancel Billing Document (Optional) | On the Billing Document screen, select a certain billing document and choose Cancel Billing Document. | A log displays the following message: Billing Document Canceled. |  |
| 7 | Update New Attachment (Optional) | In the Edit mode, you can add, delete, and update the attachments. Save your changes by choosing Save in the footer bar. |  |  |
| 8 | Update New Text (Optional) | In the Edit mode, you can add, delete, and update the texts. Save your changes by choosing Save in the footer bar. |  |  |

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
| 2 | Access the App | Open Schedule Delivery Creation (F2228). | The Application Jobs screen displays. The app automatically shows the history of application jobs. |  |
| 3 | Create Delivery Creation Schedule | Choose Create to define a new job. | The New Job screen displays. The Job Template should be Schedule Delivery Creation for Sales Orders. |  |
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary, then choose Check. | The system displays the message Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A delivery creation job is scheduled. Screen goes back to Application Jobs. |  |
| 6 | Check Delivery Creation Job Log | On the Application Jobs screen, after job item’s status turned to Finish, choose Status symbol in the Log column.Note Choose the Magnifier, and the job list will refresh. | The job log details displays. |  |

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
| 2 | Access the App | Open Schedule Goods Issue for Deliveries (F2259). | The Application Jobs screen displays. The app automatically shows the history of application jobs. |  |
| 3 | Create Goods Issue Deliveries Schedule | Choose New to define a new job. | The New Job screen displays. The Job Template should be defaulted as Schedule goods issue for Deliveries. |  |
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary, then choose Check. | The system displays the message Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A schedule goods issue for deliveries job is scheduled. The screen goes back to Application Jobs. |  |
| 6 | Check Goods Issue Deliveries Job Log | On the Application Jobs screen, after job item’s status turned to Finish, choose Status symbol in the Log column.Note Choose the Magnifier, and the job list will refresh. | The job log details are displayed. |  |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Billing Creation (F1519). | The Application Jobs screen displays. The app automatically shows the history of application jobs. |  |
| 3 | Create Billing Creation Schedule | Choose Create to define a new job for billing creation. | The New Job screen displays. Job Template should default as Schedule Billing Creation. |  |
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

This process step shows you how to schedule a background job for release billing documents to accounting.

This app can be used as an alternative instead of the manual release to accounting for billing documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Billing Release (F1518). | The Application Jobs screen displays. The app automatically shows the history of application jobs. |  |
| 3 | Create Billing Release Schedule | Choose Create to define a new job for billing creation. | The New Job screen displays. Job Template defaultly should be Schedule Billing Release. |  |
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary.Choose Check. | The system displays the message Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A billing release job is scheduled. Return to Application Jobs. |  |
| 6 | Check Billing Release Job Log | On the Application Jobs screen, after job item’s status turned to Finish, choose Job Log.Note Choose Magnifier, and the job list will refresh. | The log details displays. |  |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Billing Output (F1510). | The Application Jobs screen displays. The app automatically shows the history of application jobs. |  |
| 3 | Create Billing Output Schedule | Choose Create to define a new job for billing creation. | The New Job screen displays. Job Template should default as Schedule Billing Output. |  |
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary.Choose Check. | The system displays the message Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A billing release job is scheduled. Return to Application Jobs. |  |
| 6 | Check Billing Output Job Log | On the Application Jobs screen, after job item’s status turned to Finish, choose Job Log.Note Choose Magnifier, and the job list will refresh. | The log details display. |  |

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| Sales Order Fulfillment Monitoring and Operations (BKK) (optional) | Using the master data from this document, complete the following activities described in the test script:Review sections: Incomplete SD Documents (deliveries) and Review Outbound Deliveries for Goods Issue |

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
- see-also :: [[08-sales-order-management/test-script-make-to-order-production-for-sales-kits-with-variant-confi]]
- see-also :: [[08-sales-order-management/test-script-intercompany-process-for-customer-returns-2f4-ae-820]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7KW_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 50,399 chars in the whole document
