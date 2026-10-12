---
id: 08-sales-order-management/test-script-sell-from-stock-with-valuated-stock-in-transit-5mq-ae-1109
title: "Test Script: Sell from Stock with Valuated Stock in Transit (5MQ_AE) (5MQ_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 (UAE) test script for scope item 5MQ: sell from stock with valuated stock in transit, from sales order to billing, with job alternatives."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/sell-from-stock-with-stock-in-transit]
aliases: [5MQ_S4CLD2608_BPD_EN_AE]
keywords: [Sell from Stock with Valuated Stock in Transit, valuated stock in transit, sell from stock, sales order creation, outbound delivery, goods issue posting, value chain monitoring, billing documents, proof of delivery, scheduled jobs]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5MQ_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1109
topic: 08-sales-order-management/sell-from-stock-with-stock-in-transit
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Sell from Stock with Valuated Stock in Transit (5MQ_AE) (5MQ_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5MQ_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Sell from Stock with Valuated Stock in Transit** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Sell from Stock with Valuated Stock in Transit (5MQ_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232856733)

[2 Prerequisites 4](#_Toc232856734)

[2.1 System Access 4](#_Toc232856735)

[2.2 Roles 4](#_Toc232856736)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232856737)

[2.4 Additional Manual Configuration 6](#_Toc232856738)

[2.5 Business Conditions 6](#_Toc232856739)

[2.6 Preliminary Steps 7](#_Toc232856740)

[2.6.1 Set Initial Stock for Material 7](#_Toc232856741)

[2.6.2 Set Relevance for Sell from Stock with VSiT 8](#_Toc232856742)

[3 Overview Table 10](#_Toc232856743)

[4 Test Procedures 12](#_Toc232856744)

[4.1 Create Sales Order 12](#_Toc232856745)

[4.2 Process Sales Order Approval (Optional) 14](#_Toc232856746)

[4.3 Review Blocked Sales Orders (Optional) 14](#_Toc232856747)

[4.4 Create Attachment for Sales Order (Optional) 15](#_Toc232856748)

[4.5 Monitor Value Chains for Sales Order 16](#_Toc232856749)

[4.6 Create Delivery 17](#_Toc232856750)

[4.7 Create Attachment for Delivery (Optional) 19](#_Toc232856751)

[4.8 Monitor Value Chains 19](#_Toc232856752)

[4.9 Execute Picking 20](#_Toc232856753)

[4.10 Post Goods Issue 21](#_Toc232856754)

[4.11 Check Material Document Number of Goods Movements 23](#_Toc232856755)

[4.12 Monitor Value Chains 24](#_Toc232856756)

[4.13 Proof of Delivery (Optional) 25](#_Toc232856757)

[4.14 Create Billing Document 27](#_Toc232856758)

[4.15 Create Attachment for Billing (Optional) 29](#_Toc232856759)

[4.16 Monitor Value Chains 30](#_Toc232856760)

[5 Appendix 32](#_Toc232856761)

[5.1 Process Integration 32](#_Toc232856762)

[5.1.1 Succeeding Processes 32](#_Toc232856763)

[5.2 Scheduling Job (alternative) 32](#_Toc232856764)

[5.2.1 Job Scheduling for Delivery Creation (Alternative) 32](#_Toc232856765)

[5.2.2 Job Scheduling for Goods Issue Deliveries (Alternative) 33](#_Toc232856766)

[5.2.3 Job Scheduling for Preliminary Billing Documents Creation (Alternative) 34](#_Toc232856767)

[5.2.4 Job Scheduling for Billing Creation (Alternative) 35](#_Toc232856768)

[5.2.5 Job Scheduling for Billing Release (Alternative) 36](#_Toc232856769)

[5.2.6 Job Scheduling for Billing Output (Alternative) 37](#_Toc232856770)

[5.2.7 Schedule Resolution of Value Chain Issues (Optional) 38](#_Toc232856771)

## Purpose

Overview

This scope item allows you to use valuated stock in transit (VSIT). After the goods issue is posted to an outbound delivery, the stock is transferred into VSIT. With the transfer of control of the delivered goods to the customer (for example, based on incoterms and transportation management), the goods issue from VSIT to the customer is posted. At this point in time, revenue and COGS can be recognized.

The material movements are done based on configuration settings and are posted automatically through a process orchestration framework, called Value Change Management (VCM).

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
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Master / Org. Data | Value | Master / Org. Data Details | Comments |
| --- | --- | --- | --- |
| Material | TG12 | Trading Good for Reg. Trading (MRP planning)No serial number, no batch. | See Business Conditions and Preliminary Steps sections. |
| Sold-to Party | 33100003 | Domestic UAE Customer 3 | You can test the scope item using another domestic customer. |
| Ship-to Party | 33100003 | Domestic UAE Customer 3 |  |
| Payer | 33100003 | Customer domestic 03 |  |
| Plant | 3310 |  |  |
| Storage Location | 331A |  |  |
| Shipping Point | 3310 |  |  |
| Sales Organization | 3310 |  |  |
| Distribution Channel | 10 |  |  |
| Division | 00 |  |  |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BND | Create Customer Master - MDS |
| 2YX | Create Customer-Material Info Record - MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/5d791e9003101666c7a7622951ce4651)

### Business Conditions

The business process described in this test script is part of a bigger chain of integrated business processes or scope items. As a consequence, you must have completed the following processes and fulfilled the following business conditions before you can go through this scope item:

| Scope Item | Business Condition |
| --- | --- |
| J45 - Procurement of Direct Materials | To run through this scope item, the materials must be available in stock. If you use trading goods (HAWA), you can either:Run through the Procurement of Direct Materials (J45) test script process.Or create stock using Post Goods Movement (MIGO) app (refer to Preliminary Steps section for details). |
| BNZ - Create New Open MM Posting Period - MDS | You've completed the step described in the Create New Open MM Posting Period - MDS (BNZ) master data script. Posting Period is up to date. |

### Preliminary Steps

#### Set Initial Stock for Material

Purpose

To execute this scope item, the materials must be available in stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO).It only displays in that way if it was your last transaction. So the action for the user should be to select Reference Document for MIGO Transaction > Other . | The Goods Receipt Other screen displays. |  |
| 3 | Enter Movement Type | Make the following entries and choose Enter.Executable Action in Transaction MIGO: Goods ReceiptReference Document for MIGO Transaction: Other |  |  |
| 4 | Enter Material | On the Goods Receipt Other screen: Material tab, make the following entry and choose Enter:Material : <Material Number> |  |  |
| 5 | Enter Quantity Data | On the Goods Receipt Other screen: Quantity tab, make the following entries and choose Enter:Qty in Unit of Entry: 1000Unit of Entry: <PC> |  |  |
| 6 | Input on the Goods Receipt Other Screen: Where Tab | On the Goods Receipt Other screen: Where tab, make the following entries and choose Enter:Movement Type: 561 (Receipt per initial entry of stock balances into unr. use)Plant: <Plant>Storage Location: <Storage Location> |  |  |
| 7 | Input on the Goods Receipt Other Screen: Batch Tab | On the Goods Receipt Other screen: Batch tab, make the following entry and choose Enter:Date of Manufacture: <Current Date or a Past Date>Only relevant for batch-relevant material. |  |  |
| 8 | Enter the Goods Receipt Other Screen: Serial Number Tab | On the Goods Receipt Other screen: Serial Numbers tab, enter the serial number of your received material.Only relevant for material TG20. |  |  |
| 9 | Save Your Entries | Choose Post. |  |  |

Financial Postings

Table 2:

| Material | Debited Accounts | Credited Accounts |
| --- | --- | --- |
| Trading Good (HAWA) | 13600000Inventory TradingGd | 39912000Inv Init SF&amp; Fin Bal |

#### Set Relevance for Sell from Stock with VSiT

Purpose

You need to set relevance for item category, sales org, plant and incoterm with VSiT.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Set Version | Choose Set Local Version in the end of the screen.In the pop-up window, choose Local Country Version and Set Local Version. |  |  |
| 4 | Configure Your Solution | Choose Configure Your Solution. |  |  |
| 5 | Choose SSCUI | On the Configure Your Solution: Realize Phase screen, search for SSCUI named Set Relevance for Sell-from-Stock with VSiT Process (105504) under Sales Application Area. |  |  |
| 6 | Access SSCUI | Click the line of the SSCUI, and choose Configure. |  |  |
| 7 | Set Relevance for Sell-from-Stock with VSiT | On the Change View "Set Relevance for Sell from Stock with VSiT": Overview screen, choose New Entries and make the following entries:Item Category: TANSOrg: 3310Plant: 3310Incoterm: DAPRelevance for SFS VSiT Process: Relevant for SFS VSiT ProcessChoose Save. | The relevant entries have been set for SFS VSiT Process. |  |

## Overview Table

This scope item consists of several process steps that are listed in the following table:

If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.

You can find all other apps not included on the homepage using the search bar.

If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder.

| Process Step | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Create Sales Order](#unique_11) [page ] 12 | Internal Sales Representative | Manage Sales Orders (F1873) | The Manage Sales Orders screen displays. |
| [Process Sales Order Approval (Optional)](#unique_12) [page ] 14 |  |  |  |
| [Review Blocked Sales Orders (Optional)](#unique_13) [page ] 14 |  |  |  |
| [Create Attachment for Sales Order (Optional)](#unique_14) [page ] 15 | Internal Sales Representative | Manage Sales Orders (F1873) |  |
| [Monitor Value Chains for Sales Order](#unique_15) [page ] 16 | Internal Sales Representative | Monitor Value Chains (F4854) |  |
| [Create Delivery](#unique_16) [page ] 17 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) |  |
| [Create Attachment for Delivery (Optional)](#unique_17) [page ] 19 | Shipping Specialist | Change Outbound Delivery (VL02N) |  |
| [Monitor Value Chains](#unique_18) [page ] 19 | Internal Sales Representative | Monitor Value Chains (F4854) |  |
| [Execute Picking](#unique_19) [page ] 20 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) |  |
| [Post Goods Issue](#unique_20) [page ] 21 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | The goods issue is posted. |
| [Check Material Document Number of Goods Movements](#unique_21) [page ] 23 | Warehouse Clerk | Display Material Document List - Deprecated (MB51) |  |
| [Monitor Value Chains](#unique_22) [page ] 24 | Internal Sales Representative | Monitor Value Chains (F4854) |  |
| [Proof of Delivery (Optional)](#unique_23) [page ] 25 | Shipping Specialist | Change Outbound Delivery - Proof of Delivery (VLPOD) |  |
| [Create Billing Document](#unique_24) [page ] 27 | Billing Clerk | Create Billing Documents (F0798) | The Create Billing Document screen displays. |
| [Create Attachment for Billing (Optional)](#unique_25) [page ] 29 | Billing Clerk | Manage Billing Documents (F0797) | The Display Billing Document screen displays. |
| [Monitor Value Chains](#unique_26) [page ] 30 | Internal Sales Representative | Monitor Value Chains (F4854) | The Monitor Value Chains screen displays. |

## Test Procedures

This section describes procedures for each process step that belongs to this scope item.

The Enterprise Search function provides a central entry point for finding business objects in your company from different sources using a single search request. You can search for objects, such as apps, fact sheets for business objects. From the data found, you can go directly to the respective apps and fact sheets to display, edit the data or find related objects.

How to access and check a fact sheet:

1. Log on to the SAP Fiori launchpad as a respective user, for example, an Internal Sales Representative.
2. Access the Enterprise Search bar by choosing the magnifying glass icon in the upper right corner.
3. The Enterprise Search bar displays two filter fields next to the search icon: all dropdown list and a search field. Enter your Search Criteria and choose the business object type, for example, select Sales orders from the dropdown list, and enter a sales order number in the search field and choose Search. The sales order lists display.
4. Choose the sales order number link. The system navigates to the fact sheet screen and sales order related information is integrated and summarized in one Fiori page. You can get detailed data by choosing the corresponding links.

There are fact sheets available for the following objects (visible depending on the assigned role):

- Sales order
- Quotation
- Billing document
- Credit Memo
- Debit Memo
- Customer 360 Fact sheet

### Create Sales Order

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
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Order screen displays. |  |
| 3 | Navigate to Create Order Screen | On the Manage Sales Order screen, choose Create, and choose Create Sales Orders - VA01. |  |  |
| 4 | Enter Data | On the Create Sales Order screen, make the following entries and choose Enter:Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 5 | Enter Order Details | If you would like to use listing and exclusion, continue with Enter listed/excluded Material Numbers step.If you would like to use customer material record information, continue with Enter Customer Material Number step.On the Create Standard Order: Overview screen, make the following entries:Sold-to Party: 33100003Ship-to Party: 33100003Cust. Reference: <PO number>Material: TG12Order Quantity: <Quantity>Incoterms: <DAP>Choose Continue to skip Freight is redetermined pop-up window. |  |  |
| 6 | Save Document | Choose Save. Make a note of the sales order number: __________.Choose Enter in case any warning messages. | The order is saved and the order confirmation is printed out. |  |

Printing Form-Output Management

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Order screen displays. |  |
| 3 | Search for Sales Order | Enter search terms in filter bar and choose Go.For example, enter sales order number in Sales Order field. | Sales order is displayed in result list. |  |
| 4 | Navigate to Sales Order Screen | Click sales order number, and choose Display Sales Orders.Note If Display Sales Orders is not displayed, then click More Links. Select Display Sales Orders, and choose OK. | The Display Sales Orders xxx: Overview screen displays. |  |
| 5 | Check Output Condition | On the Display Standard Order xxx: Overview screen, choose Header Output Preview. | The document displays. |  |

It can also be navigated to a fact sheet screen in the Manage Sales Orders app:

1. On Manage Sales Orders screen, enter search terms in filter bar, and choose Go.
2. In search result, select your sales order number, and choose sales order number.

### Process Sales Order Approval (Optional)

Follow the procedure for Process Sales Order Approval steps in the Sell from Stock (BD9) scope item.

Purpose

This process step shows you how to review the sales orders that might need to be approved.

Procedure

Complete the activities of Process Sales Order Approval described in the test script of Sell from Stock (BD9) scope item.

### Review Blocked Sales Orders (Optional)

Follow the procedure for Review Blocked Sales Orders process step in the Basic Credit Management (BD6) scope item.

Purpose

In this process, you can review the sales orders that might have been blocked due to the credit limit check.

Procedure

Complete the activities of Review and Release or Reject a Sales Order described in the test script of Basic Credit Management (BD6) scope item.

### Create Attachment for Sales Order (Optional)

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
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Order screen displays. |  |
| 3 | Navigate to Change Sales Order Screen | On the Manage Sales Orders screen, enter the respective order number created in previous step and choose Go.Click the sales order number and choose Change Sales Order - VA02. |  |  |
| 4 | Create Attachment for Sales Order | Choose Services for Object on the top right corner of screen, and choose Create Attachment. | The File Upload screen displays. |  |
| 5 | Import File | Choose OK in the File Upload dialog box.In the Open view, choose local path and file, and choose Open. | The attachment is successfully created. |  |
| 6 | Check Attachment | Choose Services for Object on top right corner of screen, and choose Attachment List. | Attachment displays on the Service: Attachment list screen. |  |

### Monitor Value Chains for Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display sales value chain.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Value Chains (F4854). | The Monitor Value Chains screen displays. |  |
| 3 | Adapt Searching Filter | Choose Adapt Filters, the Adapt Filters screen displays. Choose Filter Initial Document, Processing Stage and Process Type, and choose OK. | The searching field Process Type is switched on. |  |
| 4 | Search Value Chain Process | Make the following entry and choose Go:Initiating Document: <Sales Order number> | Business processes matching the search criteria are listed out. |  |
| 5 | Display the Value Chain Process | Select the line item from the Business Processes list. | The Business Process screen displays. |  |
| 6 | Check the Status | Check the value of the field Status on the screen, possible values could be from the list:Sales Order: CompletedOutbound Delivery: Pending | The status of the sales order value chain displays. |  |

### Create Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Create Outbound Deliveries - From Sales Orders (F0869A). | The Create Outbound Deliveries - From Sales Orders screen displays. |  |
| 3 | Search Sales Order | Make the following entries and choose Go:Shipping Point: 3310Planned Creation Date: <Delivery selection date>Sales Document: Sales order number created previously |  |  |
| 4 | Create Delivery | Select your sales order items and choose Create Deliveries. | Creation of a delivery is triggered. |  |
| 5 | Check Details | Choose Display Log. | The Analyze Delivery Log screen displays, delivery is created successfully. Delivery number displays on Deliveries tab. |  |

|  |
| --- |
| Note Depending on the scope item settings, the availability is checked at the delivery creation using the available inventory and replenishment lead time. Without sufficient stock, the created delivery has no confirmed quantities, and therefore does not start the warehouse management picking process. As soon as there is sufficient stock for delivery creation, the system creates a delivery with the starting of the picking process in warehouse management. |

To avoid open deliveries, ensure there is sufficient inventory quantity at the time for delivery creation. Additionally, you have the following options to restrict the creation of deliveries with no confirmed quantities.

You may increase the replenishment lead time which is used during the availability check (must be larger than the selection period used for delivery creation).

You may change the customization settings for the incompleteness procedure for delivery creation, so that only complete deliveries may be saved.

You may change the customization settings for the used delivery-item-category. The Check quantity 0 field must be adapted to B = Situation Rejected with An Error Message.

|  |
| --- |
| Note With the Analyze Delivery Logs app, you can display an overview about the logs of all the deliveries which have been created in your system. You can filter by, for example, Created by and other additional settings. If you select the arrow on the right of each delivery log entry, you can display the exact message type and text and also the related sales document. |

Printing Form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). |  |  |
| 3 | Issue Delivery Output | On the Change Outbound Delivery screen, enter the Delivery Number, and choose Continue.From the Delivery xxxxxxxx Change: Overview screen, choose Menu > Extras > Delivery Output > Output Control . | The Delivery: Output screen displays. |  |
| 4 | Print Preview | On the Delivery: Output screen, select the line with the DELIVERY_PICK_LIST Output Type, and choose Display PDF Document. | A preview of the print document is displayed. |  |
| 5 | Print Delivery Pick List | From the preview of the document, choose Print. | The delivery pick list is printed. |  |

### Create Attachment for Delivery (Optional)

Purpose

This process step shows you how to create attachment for delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). | The Change Outbound Delivery screen displays. |  |
| 3 | Enter Outbound Delivery Number | In the Outbound Delivery field, enter <the outbound delivery number created in previous step> and choose Continue. | The Outbound Delivery xxx Change: Overview screen displays. |  |
| 4 | Create Delivery Attachment | Choose Services for Object on the top right corner of the screen, choose Create Attachment. | The File Upload screen displays. |  |
| 5 | Import File | Choose OK in the File Upload dialog box.In the Open view, choose local path and file, and choose Open. | The attachment is successfully created. |  |
| 6 | Check Attachment | Choose Services for Object on the top right corner of the screen, and then choose Attachment List. | Attachment shows up on Service: Attachment List screen. |  |

### Monitor Value Chains

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display sales value chain.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Value Chains (F4854). | The Monitor Value Chains screen displays. |  |
| 3 | Adapt Searching Filter | Choose Adapt Filters, the Adapt Filters screen displays. Choose Filter Initial Document, Processing Stage and Process Type, and choose OK. | The searching field Process Type is switched on. |  |
| 4 | Search Value Chain Process | Make the following entry and choose Go:Initiating Document: <Sales Order number> | Business Processes matching the search criteria are listed out. |  |
| 5 | Display Value Chain Process | Click the line item from the Business Processes list. | The Business Process screen displays. |  |
| 6 | Check the Status | Check the value of the field Status on the screen, possible values could be from the list:Sales Order: CompletedOutbound Delivery: CompletedMaterial Document: PendingBilling Document: Pending | The status of the sales order value chain displays. |  |

### Execute Picking

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
| 3 | Choose Picking | Choose For Picking. |  |  |
| 4 | Enter Shipping Point | Make the following entries, and choose Execute:Shipping Point: 3310Under the Picking Data tab, select Only Picking Without WM. |  |  |
| 5 | Change Outbound Deliveries | From Day’s Workload for Picking, select your delivery number, and choose Change Outbound Deliveries. |  |  |
| 7 | Enter Picked Quantity | Choose the Picking tab, enter <quantity equal to delivery Qty> in Picked Qty field for picking related item(s). |  |  |
| 8 | Choose Enter | Choose Enter. |  |  |
| 9 | Save | Choose Save. | The delivery has been decided. |  |

### Post Goods Issue

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Open Outbound Delivery Monitor | Choose For Goods Issue. Make the following entries and choose Post Goods IssuesExecute.Shipping Point: 3310 |  |  |
| 4 | Post Goods Issue | Select your outbound delivery note, and choose .Select today’s date from the dialog box, and choose Continue. | A message which confirms the goods issue has been posted. |  |

Financial Posting I (GIOD)

| Material | Debited Account | Credited Account | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 13600000Inventory TradingGd | 13600000Inventory TradingGd | none |

|  |
| --- |
| Note The document will only be generated after Post Goods Issue. |

Financial Posting II (GITC)

| Material | Debited Account | Credited Account | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 54083000Inv Chg COGS w/CE | 13600000Inventory TradingGd | none |

When the bundling functionality in context of IFRS15 is tested, the financial document in IFRS ledger (Ledger Group 2L) with the adjusted revenue amount displays.

Note

The Planned Date of the External Transfer of Control Dates in the delivery header shipment tab is used to determine the goods issue date from Valuated Stock in Transit. In case a job is scheduled, deliveries due for goods issue postings will be selected according to this date. To check the date, follow the procedure below.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the App | Open Display Outbound Delivery (VL03N). | The Display Outbound Delivery screen displays. |  |
| 2 | Display Out bound Delivery | In the Outbound Delivery field, enter <Outbound Delivery Number>, and choose Continue. | The Display Outbound Delivery screen displays. |  |
| 3 | Check Dates | On the Display Outbound Delivery screen, choose Menu > Goto > Header > Shipment.Check dates in External Transfer of Control Dates area. |  |  |

Printing Form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Outbound Delivery (VL03N). | The Display Outbound Delivery screen displays. |  |
| 3 | Issue Delivery Output | In the Outbound Delivery field, enter <Outbound Delivery Number>, and choose Continue.On the Delivery xxxxxxxx Display: Overview screen, choose Menu > Extras > Delivery Output > Output Control. | The Delivery: Output screen displays. |  |
| 4 | Print Preview | On the Delivery: Output screen, select the line with the Output Type Delivery Note, and choose Display Document. | A preview of the print document is displayed. |  |
| 5 | Print Delivery Note | From the preview of the document, choose Print. | The delivery note is printed. |  |

### Check Material Document Number of Goods Movements

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step verifies material document number and movement type used to post into Valuated Stock in Transit.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Material Document List - Deprecated (MB51). | The Material Document List screen displays. |  |
| 3 | Choose Document | On the Material Document List screen, enter the following entries and choose Execute.Material: TG12Plant:3310Movement Type:687 |  |  |
| 4 | Check Material Document Number | Check material document number. | The material document number displays. |  |

### Monitor Value Chains

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display sales value chain.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Value Chains (F4854). | The Monitor Value Chains screen displays. |  |
| 3 | Adapt Searching Filter | Choose Adapt Filters, the Adapt Filters screen displays. Choose Filter Initial Document, Processing Stage and Process Type, and choose OK. | The searching field Process Type is switched on. |  |
| 4 | Search Value Chain Process | Make the following entry and choose Go:Initiating Document: <Sales Order number> | Business Processes matching the search criteria are listed out. |  |
| 5 | Display Value Chain Process | Select the line item from the Business Processes list. | The Business Process screen displays. |  |
| 6 | Check the Status | Check the value of the field Status on the screen, possible values could be from the list:Sales Order: CompletedOutbound Delivery: CompletedMaterial Document (with document ID appears in last step): CompletedMaterial Document: ScheduledBilling Document: Pending | The status of the sales order value chain displays. |  |

### Proof of Delivery (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you record the quantities as confirmed by the respective customer after physical arrival of goods delivered. Thus, document the right quantities that should become subject to billing to this customer.

This is only possible for Outbound Deliveries if the customer master data has been maintained in a way that this customer is POD-relevant (on sales area level).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Change Outbound Delivery - Proof of Delivery (VLPOD). |  |  |
| 3 | Enter Outbound Delivery | On the same screen, make the following entry, and choose Continue.Outbound Delivery: <your Outbound Delivery Document Number> | The selected Outbound Delivery Document screen displays, and Overview POD tab becomes active. |  |
| 4 | Quantity Difference | If there is a quantity difference between shipping and receiving, go to steps 5 and 6. |  |  |
| 5 | Enter POD Delivery Reason (Optional) | In the line with the item for which a differing quantity was reported by the customer, make the following entry or select the following value from the list:Reason: <DFG2(Underdelivery, reason unknown)> |  |  |
| 6 | Enter Deviation (Optional) | In the Quantity Difference field, go to Sales Unit (Qty Diffin Sales Un), enter <respective quantity (differs from the expected Delivery Quantity as per the Outbound Delivery Item)>, and choose Enter. | The quantity displayed for the respective item in the POD quantity field has been recalculated (Quantity Difference subtracted from Delivery Quantity).The value for POD Status field has changed to B (Differences Reported). |  |
| 7 | Confirm Delivery Proof | Choose Confirm Proof of Delivery. | The POD Date field has been filled with the current date.The value for the POD Status field has changed to C (Confirmed). |  |
| 8 | Save | Choose Save. | The Outbound Delivery document is saved with confirmation for delivered quantities.These will be used for the consecutive billing step. |  |

### Create Billing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you handle the billing.

Create Billing Document

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Documents screen displays. |  |
| 3 | Define Billing Settings | Choose Billing Settings in the bottom bar and make the following settings:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: OFFAutomatically post billing documents: ONDisplay billing documents after creation: ONChoose delivery items to be billed and select quantities: OFF |  |  |
| 4 | Search for Billing Due List | In the search condition, use criteria if necessary. | Sales document(s) display in the result. |  |
| 5 | Select Item(s) for Billing | Select row(s) of SD Document created previously and choose Create Billing Documents. | The Create Billing Document screen displays. |  |
| 6 | Maintain Billing Date | Choose billing type Invoice (F2) and maintain billing date, for example current date, then choose OK. | The draft billing document with ID Sxxxxxxxx displays. |  |
| 7 | Save Billing Document | On the Billing Document screen, choose Save.The draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx, make a note of the billing document number: __________. | The system generates an invoice for billing. |  |

Financial Postings

| Material | Debited Accounts | Credited Accounts | Cost Element/CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 10100003Rcvbls Domestic DE 3 | 41000000Rev Domestic Prod22000000Output tax (MWS)21730000 (optional)Freight Clrg MM | none |

|  |
| --- |
| Note When the bundling functionality in context of IFRS15 is tested, you can see the financial document created in the IFRS ledger (Ledger Group 2L). |

Manage Billing Documents

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Billing Documents (F0797). | The Manage Billing Document screen displays. |  |
| 3 | Search Billing Document | Enter the Billing document number recorded in previous step. Choose Enter. | The billing document created in previous step displays. |  |
| 4 | Display Billing document | Select the billing document item and choose Display. | The billing document displays. |  |
| 5 | Check Output Condition | Choose the last assignment block - Output Items. | There is one entry in the item and the output type is Billing Document. |  |
| 6 | Display Print Preview | Choose Preview. | Preview for PDF document displays. |  |
| 7 | Cancel Billing Document (Optional) | Select certain billing document and choose Cancel Billing Docs. | Message Billing Document Canceled displays. |  |
| 8 | Update New Attachment (Optional) | In the Edit mode, you can add, delete and update the attachments. Save your changes by choosing Save in the footer bar. |  |  |
| 9 | Update New Text (Optional) | In the Edit mode, you can add, delete and update these texts. Save your changes by choosing Save in the footer bar. |  |  |

### Create Attachment for Billing (Optional)

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
| 6 | Create Billing Attachment | Scroll down and choose Upload in the Attachments section. | The Open File screen displays. |  |
| 7 | Import File | In the Open window, select a local path or file and choose Open.Choose Save. | The attachment is successfully created. |  |
| 8 | Check Attachment | In the Attachments section, you can see the uploaded document. Choose the document you want to open. |  |  |

### Monitor Value Chains

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display sales value chain.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Value Chains (F4854). | The Monitor Value Chains screen displays. |  |
| 3 | Adapt Searching Filter | Choose Adapt Filters, the Adapt Filters screen displays. Choose Filter Initial Document, Processing Stage and Process Type, and choose OK. | The searching field Process Type is switched on. |  |
| 4 | Search Value Chain Process | Make the following entry and choose Go:Initiating Document: <Sales Order number> | Business Processes matching the search criteria are listed out. |  |
| 5 | Display Value Chain Process | Select the line item from the Business Processes list. | The Business Process screen displays. |  |
| 6 | Check the Status | Check the value of the field Status on the screen, possible values could be from the list:Sales Order: CompletedOutbound Delivery: CompletedMaterial Document (with document ID appears in last step): CompletedMaterial Document: ScheduledBilling Document: Completed (it may need some time for system to process the document from Pending to Completed) | The status of the sales order value chain displays. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Scope Item | Business Condition |
| --- | --- |
| J59 - Accounts Receivable | Posting a Customer Invoice in Accounting and so on.Using the master data from this document, complete the following activities described in the test script:Accounts Receivable (Sections Posting a Customer Invoice in Accounting, Overdue Receivables, Display Customer Balances, Manage Customer Line Items) |
| BKK - Sales Order Fulfillment Monitoring and Operations (Optional) | This scope item describes the collection of periodic activities, such as day ending activities or legal requirements.Using the master data from this document, complete all the activities described in the Test Script of the scope item: Sales Order Fulfillment Monitoring and Operations (BKK) (Chapters Review Sales Documents Blocked for Billing, Review Billing Due List, Review Log of Collective Invoice Creation and Review List Blocked (for accounting) Billing Documents). |

### Scheduling Job (alternative)

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
| 3 | Create Delivery Creation Schedule | Choose New to define a new job. | The New Job screen displays. The Job Template should default as Schedule Delivery Creation. |  |
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary, then choose Check. | The system displays the message Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A delivery creation job is scheduled. Screen goes back to Application Jobs. |  |
| 6 | Check Delivery Creation Job Log | On the Application Jobs screen, after job item’s status turned to Finish, choose Status symbol in the Log column.Note Choose Magnifier, and the job list will refresh. | The job log details display. |  |

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
| 3 | Create Goods Issue Deliveries Schedule | Choose New to define a new job. | The New Job screen displays. The Job Template should default as Schedule Goods Issue for Deliveries. |  |
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary, then choose Check. | The system displays the message Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A schedule goods issue for deliveries job is scheduled. The screen goes back to Application Jobs. |  |
| 6 | Check Goods Issue Deliveries Job Log | On the Application Jobs screen, after job item’s status turned to Finish, choose Status symbol in the Log column.Note Choose Magnifier, and the job list will refresh. | The job log details display. |  |

#### Job Scheduling for Preliminary Billing Documents Creation (Alternative)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to schedule a background job for creating preliminary billing documents.

This app can be used as an alternative instead of the manual creation of preliminary billing documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Creation of Preliminary Billing Documents (F4563). | The Application Jobs screen displays. The app automatically shows the history of application jobs. |  |
| 3 | Create Preliminary Billing Creation Schedule | Choose New to define a new job for preliminary billing creation. | The New Job screen displays. Job Template should default as Preliminary Billing Document Creation. |  |
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary.Choose Check. | The system displays the message You can go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A preliminary billing creation job is scheduled. Screen goes back to Application Jobs. |  |
| 6 | Check Preliminary Billing Creation Job Log | On the Application Jobs screen, after job item’s status turned to Finish, choose Job Log.Note Choose Go, and the job list will refresh. | The log details display. |  |

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
| 6 | Check Billing Creation Job Log | On the Application Jobs screen, after job item’s status turned to Finish, choose Job Log.Note Choose Magnifier, and the job list will refresh. | The log details display. |  |

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
| 3 | Create Billing Release Schedule | Choose New to define a new job for billing creation. | The New Job screen displays. Job Template should default as Schedule Billing Release. |  |
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary.Choose Check. | The system displays the message Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A billing release job is scheduled. Return to Application Jobs. |  |
| 6 | Check Billing Release Job Log | On the Application Jobs screen, after job item’s status turned to Finish, choose Job Log.Note Choose Magnifier, and the job list will refresh. | The log details display. |  |

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
| 3 | Create Billing Output Schedule | Choose New to define a new job for billing creation. | The New Job screen displays. Job Template should default as Schedule Billing Output. |  |
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary.Choose Check. | The system displays the message Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A billing release job is scheduled. Return to Application Jobs. |  |
| 6 | Check Billing Output Job Log | On the Application Jobs screen, after job item’s status turned to Finish, choose Job Log.Note Choose Magnifer, and the job list will refresh. | The log details display. |  |

#### Schedule Resolution of Value Chain Issues (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to schedule a background job to resolve the value chain issues massively.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Resolution of Value Chain Issues (F6868). | The Application Jobs screen displays. |  |
| 3 | Create a New Application Job | Choose Create. | The New Job: Schedule Resolution of Value Chain Issues screen displays. |  |
| 4 | Select a Template | Make the following entries and choose Step 2:Job Template: Schedule Resolution of Value Chain IssuesJob Name: for example, Schedule Resolution of Value Chain Issues | The Scheduling Options screen displays. |  |
| 5 | Define One-time Scheduling Settings | Option 1:Start Immediately: SelectedOption 2:Start Immediately: UnselectedStart: Choose a date and time when this job is startedTime Zone: Choose the preferred time zone, for example, UTC+08 | One-time Scheduling Option is defined. |  |
| 6 | Define Recurrence Schedule Option | Choose Define Recurrence Pattern, make the following entries and choose OK:Job Start: A date and time when the job is started for the first timeTime Zone: for example, UTC+08Recurrence Pattern: WeeklyEvery: 1 Week(s)On: for example, FridayEnd: for example, AfterOccurrence(s): for example, 52On Non-Working Day: for example, No restrictionCalendar: Germany (Standard) | Recurrence Scheduling Option is defined. |  |
| 7 | Define Parameters | Choose Step 3, make the following entries and choose Check:Process Type: for example, SFS_W_VSITSystem runtime errors: SelectedBlocked event queues: SelectedBusiness process errors: SelectedChoose Schedule. | Resolution of Value Chain Issues job is scheduled. |  |
| 8 | Check Resolution of Value Chain Issues Job Log | Return to the Application Jobs screen.On the Application Jobs screen, after job item’s status turns to Finished, choose the status icon in the Log column.Note Choose Magnifier, and the job list is refreshed. | The Log Details list displays. |  |

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
- see-also :: [[08-sales-order-management/test-script-advanced-available-to-promise-consumer-products-6n0-ae-117]]
- see-also :: [[06-management-accounting/stammdatenskript-materialstamm-fur-universelle-erlosrealisierung-anleg]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5MQ_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 65,667 chars in the whole document
