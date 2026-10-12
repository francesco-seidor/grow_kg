---
id: 11-inventory-warehouse-and-transportation/test-script-stock-transfer-with-delivery-bme-ae-sap-s-4hana-cloud-publ
title: "Test Script: Stock Transfer with Delivery (BME_AE) - SAP S/4HANA Cloud Public Edition (BME_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 (AE) test script for intracompany stock transfer with delivery (BME): prerequisites, roles, and step-by-step Fiori test procedures."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/intracompany-stock-transfers]
aliases: [BME_S4CLD2608_BPD_EN_AE]
keywords: [Stock Transfers Within a Company Code, stock transfer, stock transport order, mrp run, outbound delivery, goods issue, goods receipt, stock transport order approval, flexible workflow, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BME_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1287
topic: 11-inventory-warehouse-and-transportation/intracompany-stock-transfers
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Stock Transfer with Delivery (BME_AE) - SAP S/4HANA Cloud Public Edition (BME_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BME_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Stock Transfers Within a Company Code** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Stock Transfer with Delivery (BME_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232862256)

[2 Prerequisites 4](#_Toc232862257)

[2.1 System Access 4](#_Toc232862258)

[2.2 Roles 4](#_Toc232862259)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232862260)

[2.4 Additional Manual Configuration 6](#_Toc232862261)

[2.5 Business Conditions 6](#_Toc232862262)

[2.6 Preliminary Steps 7](#_Toc232862263)

[2.6.1 Open New MM Period 7](#_Toc232862264)

[2.6.2 Optional: Creating Planned Independent Requirements 7](#_Toc232862265)

[2.6.3 Creating Stock in Supplying Plant 8](#_Toc232862266)

[2.6.4 Optional: Configure Flexible Workflow for Stock Transport Order 9](#_Toc232862267)

[2.6.4.1 Optional: Check Flexible Workflow for Stock Transport Order Approval 9](#_Toc232862268)

[2.6.4.2 Configure Flexible Workflow for Stock Transport Order 11](#_Toc232862269)

[3 Overview Table 13](#_Toc232862270)

[4 Test Procedures 15](#_Toc232862271)

[4.1 MRP Run for Single Item 15](#_Toc232862272)

[4.2 Evaluate Stock/Requirements Situation 16](#_Toc232862273)

[4.3 Process Stock Transport Requisition (with MRP) 17](#_Toc232862274)

[4.4 Change Stock Transport Order (with MRP) 19](#_Toc232862275)

[4.5 Optional: Create Stock Transport Order (without MRP) 20](#_Toc232862276)

[4.6 Optional: Change Confirmation Control for Inbound Delivery 21](#_Toc232862277)

[4.7 Optional: Approve Stock Transport Order 22](#_Toc232862278)

[4.7.1 Optional: Check Stock Transport Order Approval Details 23](#_Toc232862279)

[4.8 Create Replenishment Delivery for Stock Transport Order 24](#_Toc232862280)

[4.9 Optional: Create Pro Forma F8 Invoice 25](#_Toc232862281)

[4.10 Pick and Post Goods Issue for Stock Transport Order 26](#_Toc232862282)

[4.11 Check Status of Stock Transfer 27](#_Toc232862283)

[4.12 Optional: Confirm Quantities for Putaway 28](#_Toc232862284)

[4.13 Optional: Post Goods Receipt for Inbound Delivery 29](#_Toc232862285)

[4.14 Post Goods Receipt for Stock Transport Order 30](#_Toc232862286)

[5 Appendix 32](#_Toc232862287)

[5.1 Scheduling Job (Alternative) 32](#_Toc232862288)

[5.1.1 Job Scheduling for Delivery Creation (Alternative) 32](#_Toc232862289)

## Purpose

Overview

The stock transfer process begins with a requirement to transfer material from one plant to another within the same company code. This request, in the form of a stock transfer requisition, may be created in the procuring plant automatically by MRP or manually by a buyer.

The material master must exist in both the procuring (receiving) plant and the providing (shipping) plant. Stock transfer purchase orders are not subject to approval like other purchase orders.

A buyer converts the stock transfer purchase requisition to a stock transfer purchase order. A warehouse clerk at the shipping plant monitors the materials due to be shipped and creates deliveries as required.

A warehouse clerk gathers the materials and confirms the picked quantities. Once the delivery is complete, the delivery quantities are issued, and the goods are shipped, ending the process for the shipping plant.

Goods are received at the receiving plant referencing to the stock transfer order.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all prerequisites to conducting the test in terms of systems, users, master data, organizational data, and other test data and business conditions.

### System Access

| System | Details |
| --- | --- |
| System | Accessible via the SAP FIORI Launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Material Planner - External Procurement | SAP_BR_MATL_PLNR_EXT_PROC | Material Planning - External Procurement | SAP_BR_MATL_PLNR_EXT_PROC |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Receiving Specialist | SAP_BR_RECEIVING_SPECIALIST | Receiving | SAP_BR_RECEIVING_SPECIALIST |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |
| Production Planner | SAP_BR_PRODN_PLNR | Production Planning | SAP_BR_PRODN_PLNR |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure.

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Plant | 3310 | Plant 1 AE |  |
| Plant | 3320 | Plant 2 AE | Flex.Org App or Set Up Organizational (SAP Central Business Configuration) extensionNote The second set of organization entity IDs here is an example. In an evaluation project of the SAP Central Business Configuration environment, the ID follows the naming rule described in [Using the Set Up Organizational Structure App](https://help.sap.com/docs/CENTRAL_BUSINESS_CONFIGURATION/55c9333eed324cd284f6c4e5dab8462f/d020ff461d504421bcc55d87cbc0ae57.html). |
| Storage Location | 331A | Std. storage 1 |  |
| Storage Location | 332A | Std. storage 1 | Flex.Org App or Set Up Organizational (SAP Central Business Configuration) extensionShop floor w/o lean WM |
| Company Code | 3310 | Company Code 3310 |  |
| Purchase Organization | 3310 | Purch. Org. 3310 |  |
| Purchasing group | 001 /002 | Group 001 /Group 002 |  |
| Material | TG11 | Trading Good for Reg. Trading (MRP planning) |  |
| Material | TG20 | Trad.Good 20,Reorder Point,SerialNo |  |
| Material | TG21 | Trad.Good 21,Reorder Point,Batch-FIFO |  |

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BNE | Create Supplier Master - MDS |
| BND | Create Customer Master - MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/3bb2160e5dd7b7daa7d77a5a9fd42803)

### Business Conditions

| Scope Item | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | Complete all relevant steps. |

|  |
| --- |
| Note Before you start the testing, please make sure the setup in the scope item specific customer facing document [Intracompany Stock Transfer with Delivery Setup (BME).docx (Public)](https://support.sap.com/content/dam/SAAP/SAP_Activate/S4H_506%20Intracompany%20Stock%20Transfer%20with%20Delivery%20Setup%20(BME).docx) has been completed. |

### Preliminary Steps

#### Open New MM Period

External Process

For this activity, run the following step from the Create New Open MM Posting Period - MDS (BNZ) to close MM period and open new posting period:

Closing MM Period and Opening New Posting Period

#### Optional: Creating Planned Independent Requirements

Purpose

Planned independent requirements are used to perform demand management functions. A planned independent requirement contains one planned quantity and one date, or a number of planned independent requirements schedule lines, such as one planned quantity split over time according to dates.

|  |
| --- |
| Note Instead of creating a single requirement, sometimes a requirements plan that includes one or more planned independent requirements can be maintained for mass processing. In this case, the requirements are grouped and maintained under a requirement plan number. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/ Fail/ Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain PIRs (F3445). | The Maintain PIRs screen displays. |  |
| 3 | Check Default Area of Responsibility | On the Maintain PIRs screen, select your user name and then choose App Settings icon.On MRP Settings screen, choose Area of Responsibility.Check only this entry is displayed there: Plant 1 AE/001 (MRP Controller 001) | If the entry Plant 1 AE/001 is not present on the Area of Responsibility screen does not exist, choose Add and then choose OK.For other plant entries on the Area of Responsibility screen, choose Delete to remove the others and then choose OK. |  |
| 4 | Select | On the Maintain PIRs screen, make the following entries:Plant: 3310Period Indicator: Monthly (M)Version Active: Yes, NoSearch: TG11, TG20 or TG21Note You need to maintain screen field Period Indicator with option M on the view MRP 3 of the material master data before you use app Maintain PIRs (F3445). |  |  |
| 5 | Filter Result | Choose Go to execute. | Material item displays. |  |
| 6 | Select Material Item | Choose the material item, and choose Edit PIRs in the upper right. | The Edit PIRs view displays. |  |
| 7 | Edit PIRs | Enter quantities per period, for example:PIR: 100 PC for next 12 periodsVersion is Active: YES |  |  |
| 8 | Save PIRs Draft | Choose Save (bottom right). | The PIRs Draft is saved. |  |

#### Creating Stock in Supplying Plant

Purpose

In a real business case, the materials are usually purchased from external suppliers; in that case, that process is covered by the standard purchasing or subcontracting processes. For the purpose of this test, we post initial stock directly to the storage locations.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Stock (F1062). | The Manage Stock screen displays. |  |
| 3 | Enter Material | Make the following entry and choose Enter.Material: TG11, TG20 or TG21Plant: 3320 |  |  |
| 4 | Select Stock | Select the icon beside the stock that you want to add initial stock, for example:Storage Location: 332AUnrestricted-Use Stock | The Manage Stock dialog box opens. The Storage Location, Stock Type and Current Quantity are displayed according to your entries in previous steps. |  |
| 5 | Add Initial Stock | Make the following entries and choose Post:Document Date: <Today>Posting Date: <Today>Stock Change: Initial EntryQuantity: Enter a number, for example, <100> | The system displays the following message. The stock has been added.1 document has been created: Material Document XXXXXXXXXX/20XX |  |

#### Optional: Configure Flexible Workflow for Stock Transport Order

##### Optional: Check Flexible Workflow for Stock Transport Order Approval

Purpose

In this procedure, you check flexible workflow for purchase order approval.

Make sure Flexible Workflow for Purchase Order with UD document is activated, and flexible workflow for purchase order approval is configured.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Configure Your Solution screen displays. |  |
| 4 | Open Active Flexible Workflow | On the Configure Your Solution screen, search Activate Flexible Workflow for Purchase Orders, then choose Go.Select the line of the item and go to next screen.On the Configure Your Solution - Purchase Order Processing screen, choose Configure on the line of Activate Flexible Workflow for Purchase Orders the configuration step. | The Document Types Purchase Order Change screen displays. |  |
| 5 | Activate Flexible Workflow for PO Approval | Make sure the following entries are made:Document Type: UDScenario based workflow: XNote You might be asked to enter a customizing request number, either choose your own customizing request or create a new one. Then choose Continue. | The scenario based workflow is active for purchase orders with Document Type: UD. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the Configuration Activity | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Activate Flexible Workflow for Purchase Orders.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Activate Flexible Workflow for Purchase Orders screen displays. |  |
| 3 | Activate Flexible Workflow for PO Approval | Make sure the following entries are made:Document Type: UDScenario based workflow: XNote You might be asked to enter a customizing request number, either choose your own customizing request or create a new one. Then choose Continue. | The scenario based workflow is active for purchase orders with Document Type: UD. |  |

Result

The Scenario based workflow is active for Document Type: UD.

##### Configure Flexible Workflow for Stock Transport Order

Purpose

In this procedure, you configure your release conditions for purchase order approval.

When you start to process this step, please make sure that the flexible workflow for purchase document type NB has been activated in your system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Workflows for Purchase Orders (F2872). | The Manage Workflows screen displays. |  |
| 3 | Create Manage Workflow | Choose Create and make following entry:Name: Test Workflow for Stock Transport Order UDGo to the Start Conditions area and select Document type of purchase order is: Stock Transp. OrderDel (UD)Choose Add and make the following entry:Purchasing group of purchase order is: 002Go to the Steps area, choose Create, and then make the following entry on the next screen:Step Type: Release of Purchase OrderGo to the Recipients area:Assignment By: UserUser: Select a user from value help (with Employee ID PURCHASING_MANAGER).Step to be completed by：One of the recipients.Choose Create.Choose Save. | The workflow for stock Transport order is configured. |  |
| 4 | Activate Workflow Item | Choose the just created Workflow Item and choose Activate. | The workflow item is activated. |  |

## Overview Table

The scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App Name / Transaction | Expected Results |
| --- | --- | --- | --- |
| [MRP Run for Single Item](#unique_14) [page ] 15 | Material Planner - External Procurement | Schedule MRP Runs (F1339) | A purchase requisition will be created. |
| [Evaluate Stock/Requirements Situation](#unique_15) [page ] 16 | Material Planner - External Procurement | Monitor Material Coverage - Net / Individual Segments (F2101A) |  |
| [Process Stock Transport Requisition (with MRP)](#unique_16) [page ] 17 | Purchaser | Assign and Process Purchase Requisitions (ME57) | A Stock Transport Order will be created. |
| [Change Stock Transport Order (with MRP)](#unique_17) [page ] 19 | Purchaser | Change Purchase Order - Advanced (ME22N) | The Stock Transport Order will be changed. |
| [Optional: Create Stock Transport Order (without MRP)](#unique_18) [page ] 20 | Purchaser | Create Purchase Order - Advanced (ME21N) | A Stock Transport Order will be created. |
| [Optional: Change Confirmation Control for Inbound Delivery](#unique_19) [page ] 21 | Purchaser | Change Purchase Order - Advanced (ME22N) | A Stock Transport Order will be changed. |
| [Optional: Approve Stock Transport Order](#unique_20) [page ] 22 | Purchasing Manager | My Inbox - All Items (F0862) | A Stock Transport Order is approved |
| [Optional: Check Stock Transport Order Approval Details](#unique_21) [page ] 23 | Purchaser | Manage Purchase Orders (F0842A). |  |
| [Create Replenishment Delivery for Stock Transport Order](#unique_22) [page ] 24 | Shipping Specialist | My Purchase Orders - Due for Delivery (VL10B) | Outbound Delivery is created. |
| [Optional: Create Pro Forma F8 Invoice](#unique_23) [page ] 25 | Billing Clerk | Create Billing Documents (F0798) | Billing with F8 type is created. |
| [Pick and Post Goods Issue for Stock Transport Order](#unique_24) [page ] 26 | Shipping Specialist | Change Outbound Delivery (VL02N) | Goods Issue is posted. |
| [Check Status of Stock Transfer](#unique_25) [page ] 27 | Warehouse Clerk | Stock - Single Material (F1076) |  |
| [Optional: Confirm Quantities for Putaway](#unique_26) [page ] 28 | Receiving Specialist | Inbound Deliveries for Putaway (VL06IP) | The material of the Inbound Delivery has been Putaway |
| [Optional: Post Goods Receipt for Inbound Delivery](#unique_27) [page ] 29 | Receiving Specialist | Inbound Deliveries for Goods Receipt (VL06IG) | Goods Receipt is posted for the Inbound Delivery |
| [Post Goods Receipt for Stock Transport Order](#unique_28) [page ] 30 | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843) | Goods Receipt is posted |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### MRP Run for Single Item

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The aim of material requirements planning is to tailor available capacities and receipts on time to suit requirements quantities. This process step shows you how to use MRP or consumption-based planning for this purpose. Single-item multi-level requirement planning is performed for plant 3310.

Prerequisite

The trading goods (TG11, TG20 or TG21) is planned at plant level. There is now a requirement for the material TG11, TG20 or TG21 in plant 3310.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule MRP Runs (F1339). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create.On the New Job screen, make the following entries:For 1. Template Selection section:Job Template: Material Requirement Planning (MRP)Job Name: <MRP forTG11, TG20 or TG21>Choose Step 2.For 2. Scheduling Options section:Start Immediately: <select>Choose Define Recurrence Pattern.On the Scheduling Information screen, make the following entries:Start Immediately: XRecurrence Pattern: Single RunChoose OK.Choose Step 3.Choose 4 Parameters and make the following entries:Plant: 3310Material: TG11, TG20 or TG21Changed BOM Components: selectPlanning Mode: 1Choose Check at the bottom right.Choose Schedule. | A message appears: You can go ahead and schedule the job. |  |
| 4 | Refresh Application Jobs List | To check the job’s status, enter TG11, TG20 or TG21 in the search box and choose Go at the top right section of the screen. | The new job is created and is displayed in the Application Jobs table when refreshed. |  |

### Evaluate Stock/Requirements Situation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the requirement planning has been performed, you want to display the stock/requirements situation for the Trading Goods (TG11, TG20 or TG21) in the stock/requirements list.

Prerequisite

Requirement planning has been carried out.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Material Planner - External Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). | The Monitor Material Coverage screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, check if the toggle button of Manage Material Coverage - New Version (F0251A) is on.Turn it on if the toggle button is off. | If the toggle button is on, continue with following steps to navigate to Manage Material Coverage - New Version (F0251A).If the toggle button is off, you will be navigated to Check Material Coverage - Old Version (F0251).The following steps are described with the toggle button on. |  |
| 4 | Select Material and Show Shortages | In the search area, make the following entries and choose Go.Material: TG11, TG20 or TG21Select the filtered rows and choose Manage Materials. | The Manage Material Coverage screen displays. |  |
| 5 | Verify Purchase Requisitions that are Available | In the Stock/Requirements List, find available purchase requisitions. Look for rows with PurRqs items. | The MRP has created purchase requisitions that can be used for the Procurement of Direct Materials (J45) test script. |  |

### Process Stock Transport Requisition (with MRP)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to assign a purchase requisition for stock transfer and create a corresponding purchase order.

If you want to use the Save Draft feature in this app, you have to use a personalized user.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Process Purchase Requisitions - Deprecated (F1048). | The Process Purchase Requisitions screen displays. |  |
| 3 | Search for Purchase Requisition | On the Process Purchase Requisitions screen, make the following entry and choose Go:Material: for example, TG11Note You may need to choose Adapt Filters if some entries are not displayed. | The Purchase Requisitions table with purchase requisition items displays. |  |
| 4 | Select Purchase Requisition | Choose the row of the purchase requisition you want to process. The Display Purchase Req.XXXXX screen displays.Choose Display/Change to convert the assigned purchase requisitions into stock transport orders. The Change Purchase Req.XXXXX screen displays.Expand Item Overview, and make the following entries:Item Category: UStorage Location: 331AExpand Item Detail, choose the Source of Supply tab, and make the following entries:Suppl.Plant：3320Then choose Save. | The supplying plant 3320 is maintained on tab: Source of Supply. |  |
| 5 | Process Assignments | On the Process Purchase Requisitions screen, select the checkbox of the purchase requisition line item and choose Create Purchaser Order. | The New Purchase Order area displays. |  |
| 6 | Adopt the Purchase Requisition and Create Purchase Order | In the New Purchase Order area make the following entry:Purchase Order Type: UD (StockTranspOrderDel)Choose Save. | The system displays a message: Stock StockTranspOrderDel created under the number 45xxxxxxxx. |  |

### Change Stock Transport Order (with MRP)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to perform when changes within the stock transfer purchase order have to be made.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Purchase Order - Advanced (ME22N) . | Selected stock transport order is displayed. |  |
| 3 | Enter Stock Transportation Order | Choose Other Purchase Order and enter the Stock Transport Order Number created in the previous step and then choose Enter. |  |  |
| 4 | Change Data (Text) | Open header details or items details.Choose the Texts tab. Select the type of text to be entered, and enter text. | Selected stock transport order displays. |  |
| 5 | Change Data (Storage Location) | Open items overview:1. Check the storage location and change if different from 331A.2. Change the Delivery Date to tomorrow.Save the changes by choosing Save. | The stock transport order is changed. |  |

### Optional: Create Stock Transport Order (without MRP)

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Create Purchase Order - Advanced (ME21N). | The Create Purchase Order - Advanced (ME21N) screen displays. |  |
| 3 | Enter Purchase Order Document Type | Enter the following data:Order Type: UD (StockTranspOrderDel)Then choose Enter. |  |  |
| 4 | Enter Purchase Order Data | Enter the following data:Supplying Plant: 3320On the Org. Data tab:Purchasing Org.: 3310Purchasing Group: 002Company Code: 3310In the area of Overview Item:Material: TG11, TG20 or TG21Quantity: x pcDelivery Date: any date in the futurePlant: 3310Storage Location: 331AThen choose Enter.Note Currently the system triggers an availability check. Based on the results of the checks, if requested availability cannot be fulfilled, the Confirmation Proposal screen shows up and the user needs to make decision based on the result of the checks. Material master with item category group CB02 and LEIH is supported.Note Account Assignment Category M - Ind. cust. w/o KD-CO and Q - Proj. make-to-order are supported. There is a perquisite that the combination of Account Assignment Category and Item Category: U should be maintained through SSCUI. For details about how to configure this, please refer to the Setup Instruction. | All data is entered, and the item details screen displays. |  |
| 5 | Save Purchase Order | Choose Save and when the purchase order number is displayed, write it down for further use. | A new purchase order is created. Purchase order number is displayed.Write down the stock transport order number for further usage. |  |

### Optional: Change Confirmation Control for Inbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity is performed when an inbound delivery is to be created for the stock transport order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Purchase Order - Advanced (ME22N). | Selected stock transport order is displayed. |  |
| 3 | Enter Stock Transportation Order | Choose Other Document and enter the stock transport order number created in the previous step. Then choose Enter. |  |  |
| 4 | Switch to Change Mode | Choose Display / Change to switch to the Change mode. | The selected stock transport order is in change mode. |  |
| 5 | Change Data (Confirmation Control) | Choose the Confirmation tab. Select the option Inbound Delivery from the dropdown list Conf. Control and choose Enter.Choose Save. | The stock transport order is changed. |  |

### Optional: Approve Stock Transport Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In the activity, the Purchase Manager releases a stock transport order.

A prerequisite is the existence of a stock transport order that can be released. Purchasing group is 003 and all stock transport order in UD require an approval.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchasing Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862). | A list of already created purchase orders displays. |  |
| 3 | Search for Purchase Order Status | Enter the stock transport order number in the search area, then choose Search. | The purchase orders without follow-on documents (w/o status Follow-On Documents) and purchase group is 0003 have the status in approval. |  |
| 4 | Open Approve Purchase Orders | On the My Inbox screen, select the purchase order from the left screen. | The My Inbox screen displays. |  |
| 5 | Approve Purchase Order | On the Release Purchase Order screen confirm your created purchase Order information.Choose Approve.On the Submit Decision screen, add note if necessary and choose Submit. | Stock transport order is approved. |  |

#### Optional: Check Stock Transport Order Approval Details

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to check an existing stock transport order's approval details.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Purchase Orders (F0842A). | The Manage Purchase Orders screen displays. |  |
| 3 | Search for Stock Transport Order | Enter the stock transport order number in the search area, and then choose Go. |  |  |
| 4 | Choose Purchase Order | Choose the row for the purchase order you want to preview, then go to Purchase Order screen. | The Purchase Order screen displays. |  |
| 5 | Check Approval Details | Go to the Approval Details area and check the approval information. | The purchase order's approval details display. |  |

### Create Replenishment Delivery for Stock Transport Order

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
| 1. | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2. | Access the App | Open My Purchase Orders - Due for Delivery (VL10B). | The Goods Movement screen displays |  |
| 3. | Enter data for PO display | Choose the Purchase Orders Tab and make the following entries then choose Execute:Shipping Point/Receiving Pt: 3320Delivery creation dates: (From): delivery creation From date Delete the default dateDelivery creation dates: (To delivery creation To date Delete the default dateCalcRuleDefltDlvCrDt: calculation rulePurchasing Document: Choose a stock transport order that created in Create Stock Transport Order step . | The Activities Due for Shipping Purchase Orders, Fast Display screen appears. PO due to delivery is listed out. |  |
| 4. | Create Delivery | Select stock transport orders from the list. Choose Background to create delivery in background. | Activities due for shipping purchase orders, fast display screen appears. |  |
| 5. | Check Delivery Number | Choose More > Show/Hide Delivery , and note down the delivery number shown in the SD Doc. field. | A delivery is created. |  |

### Optional: Create Pro Forma F8 Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create Pro Forma invoice in the selling company.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents - VF01 (VF01). | The Create Billing Documents screen displays. |  |
| 3 | Maintain Billing Date | Choose billing type Pro Forma Invoice for Delivery (F8) and maintain billing date, for example, current date.Enter Delivery Number.Choose Enter. |  |  |
| 4 | Save | Choose Save. | The F8 billing document is created. |  |
| 5 | Search Billing Document | Open Display Billing Documents (VF03). | The Display Billing Document screen displays. |  |
| 6 | Display Billing Document | On the Display Billing Documents (VF03) screen, enter the Billing Number, and choose Continue. | The Billing Document screen displays. |  |
| 7 | Check Output Condition | On the Pro Forma Invoice for Delivery xxxxxxxx (F8) Display: Overview screen, choose Change Bill. Doc., and then choose Menu > Goto > Header > Output . | The Invoice xxxxxxxx Change: Output screen displays.Note Make sure to maintain a valid output condition record for the billing document using the Fiori app Output Parameter Determination (APOC_WD_BRF_DEC_TAB_MAINTAIN). |  |
| 8 | Display Print Preview | On the Pro Forma Invoice for Delivery xxxxxxxx (F8) Change: Output screen, select the output entry and choose Display Document. | A preview of the PDF document displays. |  |
| 9 | Print Billing Document | From the preview of the document, choose Print. |  |  |

### Pick and Post Goods Issue for Stock Transport Order

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). | The Change Outbound Delivery screen displays. |  |
| 3 | Enter Delivery Number | On the Change Outbound Delivery screen, enter the delivery document number from the earlier section and choose Continue. | The Replenishment Dlv. XXXXXXXX Change: Overview screen displays. |  |
| 4 | Enter Picking Data | Navigate to the Picking tab, and make the following entries:Picked Qty: <picked quantity>Choose Save. | The system shows the message: Replenishment Dlv. XXXXXXXX has been saved. The screen returns to the Change Outbound Delivery screen. |  |
| 5 | Post Goods Issue | On the Change Outbound Delivery screen, choose Post Goods Issue. |  |  |

### Check Status of Stock Transfer

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Stock - Single Material (F1076). | The Stock - Single Material screen displays. |  |
| 3 | Enter Material Number | Enter material TG11, TG20 or TG21 and choose Enter. | You receive an overview of the material. This concerns all material that has left the supplying plant and hasn't yet reached the receiving plant. |  |

### Optional: Confirm Quantities for Putaway

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity is performed to confirm all the materials of the Inbound Delivery have been put away in the correct quantities.

The step [Optional: Change Confirmation Control for Inbound Delivery](#unique_19) [page ] 21 is a prerequisite process step and has to be performed before this activity.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Receiving Specialist. | The Fiori Launchpad displays. |  |
| 2 | Access the App | Open Inbound Deliveries for Putaway (VL06IP). | The Inbound Deliveries for Putaway screen displays. |  |
| 3 | Enter Inbound Delivery Number | Make the following entries then choose Execute:Purchasing document: Enter the stock transport number created in the previous step.Delivery Date: Delete the default date.Choose Change Inbound Deliveries | The selected Inbound Delivery displays. |  |
| 4 | Confirm Quantities for Putaway | On Stock Placement tab, enter the Putaway Qty for the items: XXXNote The putaway quantity should equal to the Delivery Qty.And choose Save. | Back to the Inbound Deliveries for Putaway screen andInbound Delivery XXX has been saved.message displays. |  |

### Optional: Post Goods Receipt for Inbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity is performed to Post Goods Receipt for the Inbound Delivery to receive the materials to stock.

The step Optional: Confirm Quantities for Putaway is a prerequisite process step and has to be performed before this activity.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Receiving Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Inbound Deliveries for Goods Receipt (VL06IG). | The Inbound Deliveries for Goods Receipt screen displays. |  |
| 3 | Enter Inbound Delivery Number | Make the following entries then choose Execute:Purchasing document: Enter stock transport order number created in the previous step.Delivery Date: Delete the default date | The Goods Receipt for Inbound Deliveries to be Posted screen shows up.The selected inbound deliveries are shown. |  |
| 4 | Change the Inbound Delivery | Check the selected inbound deliveries and choose Post Goods Receipt.The Specify Actual Goods Receipt Date dialog box displays and choose Continue. | The goods receipt is posted.A success message is shown. |  |

### Post Goods Receipt for Stock Transport Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity is performed when you want to check the stock transport order and post goods receipt.

This activity is for the case that there is no inbound delivery created.

Procedure

Option 1:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad with Warehouse Clerk role. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Receipt for Purchasing Document (F0843). | The Purchasing Document screen displays. |  |
| 3 | Search for Purchasing Document | Open Purchasing Document Search. | A list of purchasing documents is displayed. |  |
| 4 | Select the Stock Transport Order | Select your purchase order. | The system displays the data for the goods receipt on the Goods Receipt screen. |  |
| 5 | Enter Delivery Note | Make the following entries:Delivery Note: xxxPrinting (Controls output management after posting): Individual slipChoose Enter. |  |  |
| 6 | Select Item and Post Goods Receipt | Select the items for which a goods receipt is to be posted.Enter the following data:Storage Location: for example, 331AChoose Post. | The Post button is activated.The system displays the message Material document xxx posted. |  |

Option 2:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Overdue Materials - Stock in Transit (F2139). | The Overdue Materials – SiT screen displays. |  |
| 3 | Select Criteria | Enter the following data:Material: TG11, TG20 or TG21Choose Go. |  |  |
| 4 | Check the Stock Transport Order | Check the quantity under the Goods issue Quantity for your Stock Transport Order. | You will see the goods issue quantity. |  |
| 5 | Post Goods Receipt for Purchasing Document | Select the purchasing document, choose Post Goods Receipt for Purchase order. | The Goods Receipt screen displays. |  |
| 6 | Post | Choose Select item, enter storage location and choose Post. | A system message Material document 5xxxxxxxxx posted is displayed. |  |

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
> Flagged while digesting this document, not verified: Approval step states purchasing group is 003 (and 0003 in expected result) while the flexible workflow configuration uses purchasing group 002; the script is internally inconsistent.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[11-inventory-warehouse-and-transportation/test-script-cross-plant-transfer-posting-1p7-ae-752]]
- related-to :: [[11-inventory-warehouse-and-transportation/test-script-sap-ewm-integration-stock-transport-orders-2vl-ae-sap-s-4h]]
- related-to :: [[11-inventory-warehouse-and-transportation/test-script-stock-transfer-without-delivery-bmh-ae-sap-s-4hana-cloud-p]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BME_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 52,730 chars in the whole document
