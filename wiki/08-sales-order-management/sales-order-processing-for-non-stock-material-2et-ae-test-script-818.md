---
id: 08-sales-order-management/sales-order-processing-for-non-stock-material-2et-ae-test-script-818
title: Sales Order Processing for Non-Stock Material (2ET_AE) - Test Script (2ET_S4CLD2608_BPD_EN_AE)
description: "S/4HANA Cloud Public Edition 2608 UAE test script for scope item 2ET: non-stock sales order through delivery, goods issue, POD and billing."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/non-stock-material-sales]
aliases: [2ET_S4CLD2608_BPD_EN_AE]
keywords: [Sales of Non-Stock Materials, non-stock material, sales order processing, test scripts, outbound delivery, goods issue, proof of delivery, billing documents, delivery split, freight costs]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2ET_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-818
topic: 08-sales-order-management/non-stock-material-sales
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Sales Order Processing for Non-Stock Material (2ET_AE) - Test Script (2ET_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2ET_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Sales of Non-Stock Materials** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Sales Order Processing for Non-Stock Material (2ET_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Sales Order Processing for Non-Stock Material (2ET_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232849421)

[2 Prerequisites 4](#_Toc232849422)

[2.1 System Access 4](#_Toc232849423)

[2.2 Roles 4](#_Toc232849424)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232849425)

[2.4 Preliminary Steps 6](#_Toc232849426)

[2.4.1 Set POD Relevance for Delivery Item Category 6](#_Toc232849427)

[2.4.2 Set Relevant for Proof of Delivery in BP Master Data 8](#_Toc232849428)

[2.4.3 Create Condition Records (Optional) 8](#_Toc232849429)

[3 Overview Table 9](#_Toc232849430)

[4 Test Procedures 11](#_Toc232849431)

[4.1 Basic Credit Management (BD6) - Set Credit Limit (Optional) 11](#_Toc232849432)

[4.2 Sales Quotation (BDG) (Optional) 12](#_Toc232849433)

[4.3 Sales Contract (Optional) 12](#_Toc232849434)

[4.4 Create Sales Order 13](#_Toc232849435)

[4.5 Process Sales Order Approval (Optional) 15](#_Toc232849436)

[4.6 Basic Credit Management (BD6) - Review Blocked Sales Orders (Optional) 15](#_Toc232849437)

[4.7 Create Delivery 16](#_Toc232849438)

[4.8 Split Outbound Delivery (Optional) 17](#_Toc232849439)

[4.9 Add Freight Cost (Optional) 18](#_Toc232849440)

[4.10 Post Goods Issue 19](#_Toc232849441)

[4.11 Proof of Delivery (Optional) 20](#_Toc232849442)

[4.12 Create Billing Document 21](#_Toc232849443)

[4.13 Create Pro Forma Invoice (Optional) 23](#_Toc232849444)

[5 Appendix 25](#_Toc232849445)

[5.1 Process Integration 25](#_Toc232849446)

[5.1.1 Succeeding Processes 25](#_Toc232849447)

[5.2 Scheduling Job Creation (Optional) 25](#_Toc232849448)

[5.2.1 Scheduling Job for Delivery Creation (Optional) 25](#_Toc232849449)

[5.2.2 Scheduling Job for Goods Issue Deliveries (Optional) 26](#_Toc232849450)

[5.2.3 Scheduling Job for Billing Creation (Optional) 27](#_Toc232849451)

[5.2.4 Scheduling Job for Billing Release (Optional) 28](#_Toc232849452)

[5.2.5 Scheduling Job for Billing Output (Optional) 28](#_Toc232849453)

## Purpose

Overview

A non-stock material can be used in the Sales Order. Non-stock materials are not included in inventory management. With creation of a delivery, the goods issue is reflected by a confirmation posting. Non-stock items can be handled along with stock items on one sales order.

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
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |
| Credit Controller | SAP_BR_CREDIT_CONTROLLER | Credit Management | SAP_BR_CREDIT_CONTROLLER |  |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Master / Org. Data | Value | Master / Org. Data Details | Comments |
| --- | --- | --- | --- |
| Material | NS0002 | Non-Stock Material 02 (No MRP planning)No serial number, no batch | If you use ANC procedure to extend the new country content, you need to manually extend the materials according to Master Data Script 31Y |
| Sold-to party | 33100003 33100005 33100009 | Domestic UAE Customer 3 Domestic UAE Customer 5 Domestic UAE Customer 9 | You can test the scope item using another domestic customer.33100005 is for credit management.33100009 is for customer material record and POD (Proof-of-Delivery) |
| Ship-to party | 33100003 33100005 33100009 | Domestic UAE Customer 3 Domestic UAE Customer 5 Domestic UAE Customer 9 |  |
| Payer | 33100003 33100005 33100009 | Customer domestic 03 Customer domestic 05 Domestic UAE Customer 9 |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Shipping Point | 3310 | Shipping Point 3310 |  |
| Sales organization | 3310 | Dom. Sales Org |  |
| Distribution channel | 10 | Direct Sales |  |
| Division | 00 | Product Division 00 |  |

For more information about creating master data, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) Script documentation.

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| BND | Create Customer Master - MDS |
| 31Y | Create Product Master of type "Non-Stock Material" - MDS |

### Preliminary Steps

#### Set POD Relevance for Delivery Item Category

Purpose

This process step shows you how to set POD-Relevance for delivery item category.

Prerequisites

To use the optional step Proof of Delivery later on in the process, the delivery item categories need to set as POD-Relevant. Following procedure guide how to set indicator POD-Relevant for delivery item category.

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241) under Implementation Cockpit. | The various configuration sections display. |  |
| 3 | Search for a Solution Configuration | Open the configuration section Configure Your Solution, and in the Search field, enter POD | Various configuration activities for POD display. |  |
| 4 | Select a Solution Configuration | Choose application Deliveries. | The Configure Your Solution-Deliveries screen displays. |  |
| 5 | Start the Configuration Activity | Press Configure beside configuration activity Set POD-Relevance Depending on Delivery Item Category | The Change View "Maintain POD Relevance": Overview screen displays. |  |
| 6 | Set POD-Relevant for Item Category | Choose X (Relevant for POD)for item category TAX and TAXN, and press the Save button. | Target item category has been set POD-Relevant. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Set POD-Relevance Depending on Delivery Item Category | Go to the Business Processes Configuration app. You can search for a configuration activity and navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).Search for Set POD-Relevance Depending on Delivery Item Category. |  |  |
| 3 | Set POD-Relevant for Item Category | Choose X (Relevant for POD)for item category TAX and TAXN, and press the Save button. | Target item category has been set POD-Relevant. |  |

#### Set Relevant for Proof of Delivery in BP Master Data

Prerequisites

To use the optional step Proof of Delivery later on in the process, the customer with indicator POD-Relevant need be used from sales document creation. Customer 33100009 has maintained Pod-Relevant as example for test. Following procedure guide how to set indicator POD-Relevant for other test customer if needed.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the Role Master Data Specialist - Business Partner Data (MDG Cloud). |  |  |
| 2 | Access the App | Open Maintain Business Partner (BP). |  |  |
| 3 | Enter Business Partner | On the entry screen of the Maintain Business Partner App. Make the following entry, and choose Enter.Business Partner: <Customer ID> |  |  |
| 4 | Switch to Change Mode | On the screen Display Organization: XXXXXXXX, choose button Switch Between Display and Change. |  |  |
| 5 | Goto Sales Area – Shipping Tab | On the screen Change Organization : XXXXXXXX, choose Customer (maintained) in field Change in BP role. |  |  |
| 6 | Set POD-Relevant | Select the checkbox of POD-Relevant. |  |  |
| 7 | Save | Choose Save. |  |  |

#### Create Condition Records (Optional)

Purpose

In case you have finetuned the access sequence of SAP pre-shipped condition types, the relative condition records should be created accordingly.

You can find general information on how to create your own master data in the following: [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 2: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BEW | Create Free Goods Condition - MDS |

## Overview Table

This scope item consists of several process steps, provided in the table below:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Basic Credit Management (BD6) - Set Credit Limit (Optional)](#unique_10) [page ] 11 | Credit Controller |  | Credit Limit for Customer 33100005 has been set. |
| [Sales Quotation (BDG) (Optional)](#unique_11) [page ] 12 | Internal Sales Representative |  |  |
| [Create Sales Order](#unique_12) [page ] 13 | Internal Sales Representative | Manage Sales Orders - Version 2 (F3893) | The Manage Sales Orders screen displays. |
| [Process Sales Order Approval (Optional)](#unique_13) [page ] 15 |  |  |  |
| [Basic Credit Management (BD6) - Review Blocked Sales Orders (Optional)](#unique_14) [page ] 15 | Credit Controller |  | Sales order is released. |
| [Create Delivery](#unique_15) [page ] 16 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) | Delivery is created. |
| [Split Outbound Delivery (Optional)](#unique_16) [page ] 17 | Shipping Specialist | Split Outbound Delivery (VLSP) | Single outbound delivery split into two (according to preconfigured split profile) |
| [Add Freight Cost (Optional)](#unique_17) [page ] 18 | Shipping Specialist | Change Outbound Delivery (VL02N) | Freight Costs are added to the Outbound Delivery and will be later copied to the Invoice. |
| [Post Goods Issue](#unique_18) [page ] 19 | Shipping Specialist | Change Outbound Delivery (VL02N) | The goods issue is posted. |
| [Proof of Delivery (Optional)](#unique_19) [page ] 20 | Shipping Specialist | Change Outbound Delivery - Proof of Delivery (VLPOD) |  |
| [Create Billing Document](#unique_20) [page ] 21 | Billing Clerk | Create Billing Documents (F0798) | Billing is carried out. |
| [Create Pro Forma Invoice (Optional)](#unique_21) [page ] 23 | Billing Clerk | Create Billing Documents - VF01 (VF01) |  |

## Test Procedures

This section describes procedures for each process step that belongs to this scope item.

The Enterprise search function provides a central entry point for finding business objects in your company from different sources using a single search request, You can search for objects such as: Apps, fact sheets for business objects. From the data found, you can go directly to the respective apps and fact sheets to display, edit the data, or find related objects.

How to access and check a fact sheet:

- Log onto the SAP Fiori launchpad using the respective user example, Internal Sales Representative.
- Access the Enterprise Search Bar and choose the magnifying glass button in the upper right corner.
- The Enterprise Search bar is displayed, two filter fields appear left to the search button. Enter your Search Criteria and choose the business object type, example,: Sales orders from dropdown menu in 1st field, enter sales order number in 2nd field and choose Search, The sales order is listed.
- Choose the sales order number link: the system navigates to the fact sheet screen and sales order related information is integrated and summarized in one SAP Fiori page, You can get detailed data via choosing the corresponding links.

There are fact sheets available for the following objects: (Visible depending on the assigned role)

- Sales order
- Quotation
- Billing document
- Credit Memo
- Debit Memo

### Basic Credit Management (BD6) - Set Credit Limit (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process, a credit limit is set for the used customer.

Procedure

Complete all the activities described in Basic Credit Management (BD6) scope item's test script.

### Sales Quotation (BDG) (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to generate a standard sales quotation. If you want to generate a sales quotation before creating a sales order, you can implement this optional test script.

Procedure

Complete all the activities described in Sales Quotation (BDG) scope item's test script.

|  |
| --- |
| Note If you want to use the optional link between scope item Sales Quotation (BDG) and Sales Order Processing for Non-Stock Material (2ET), make sure to use consistent master data, such as Business Partner for the customer quotation and for the customer sales order. |

### Sales Contract (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This scope item describes the process for a standard sales Contract.

Procedure

Complete all the activities described in the test script of Sales Contract Management (I9I) scope item.

|  |
| --- |
| Note If you want to use the optional link between Sales Contract Management (I9I) and Sales Order Processing for Non-Stock Material (2ET) scope items, this reference only works if you use consistent master data (such as Business Partner for the customer quotation and the customer sales order). |

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
| 2 | Access the App | Open Manage Sales Orders - Version 2 (F3893). | The Manage Sales Orders - Version 2 screen displays. |  |
| 3 | Create Sales Order | On the Manage Sales Orders - Version 2 screen, choose Create. |  |  |
| 4 | Enter Data | On the Sales Order Screen, Order Type is Standard Order (OR), make the following entries and choose Continue:Sales Organization: 3310Distribution Channel: 10Division:00 |  |  |
| 5 | Enter Order Details | On the New: Sales Order screen, make the following entries:Sold-to Party: 33100003Ship-to Party: 33100003Customer References: E.g. Purchase OrderOrder Reason: <Order Reason>, for example, Excellent priceMaterial Number: <NS0002>Quantity: <Quantity>Note The item category can change to TAXN manually if the item is free of charge for Non-Stock Material Sales Order.Note The item category can change to CTAX manually if the item is Downpayment for Non-Stock Material. |  |  |
| 6 | Save Document | Choose Create. Make a note of the sales order number: __________. | The order is saved and its order confirmation is printed out. |  |

Printing Forms

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders - Version 2 (F3893). | The Manage Sales Orders - Version 2 screen displays. |  |
| 3 | Search for Sales Order | Enter search terms in filter bar and choose GoExample: Enter <sales order number> in the Sales Order field. | Sales order is displayed in the result list. |  |
| 4 | Display Sales Order | Choose sales order number and choose Display Sales Order - VA03. | The Display Sales Orders xxx: Overview screen displays. |  |
| 5 | Check Output Condition | On the Display Standand Orders xxx: Output screen, and choose Header Output Preview. |  |  |
| 6 | Display Print Preview | On the Display Standard Orders xxx: Output screen, select the line already created for the print output and choose Display Document. | Preview for PDF document displays. |  |

|  |
| --- |
| Note It can also be navigated to a fact sheet screen in the Manage Sales Orders - Version 2 (F3893) app:On the Manage Sales Orders screen, enter search terms in filter bar and choose Go.In search result, click your sales order number and choose Display Fact sheet. |

### Process Sales Order Approval (Optional)

Follow the procedure for Process Sales Order Approval steps in the Sell from Stock (BD9) scope item.

Purpose

This process step shows you how to review the sales orders that might need to be approved.

Procedure

Complete the activities of Process Sales Order Approval described in the test script of Sell from Stock (BD9) scope item.

### Basic Credit Management (BD6) - Review Blocked Sales Orders (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to review the sales orders that might have been blocked due to the credit limit check.

Procedure

Complete all the activities described in Basic Credit Management (BD6) scope item's test script.

### Create Delivery

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
| 3 | Search for Sales Order | Make the following entries and choose Go:Shipping point:3310Planned Creation Date: <Delivery selection date>Sales Document: <Sales Order Number Created Previously> |  |  |
| 4 | Create Delivery | Select your sales order, and choose Create Deliveries. | A delivery creation is triggered |  |
| 5 | Check Details | Choose Display Log. | The Analyze Delivery Log screen displays.A delivery is created successfully with delivery number shown on tab Deliveries. |  |

|  |
| --- |
| Note With the Analyze Outbound Delivery Logs app, you can display an overview about the logs of all the deliveries, which have been created in your system. You can filter by example created by and Additional settings. If you select the arrow on the right of each delivery log entry you can see its message type, text, and also related sales document. |

### Split Outbound Delivery (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to split up single or multiple items from an existing, completely picked Outbound Delivery and move them to a new delivery document before posting Goods Issue.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Split Outbound Delivery (VLSP). |  |  |
| 3 | Enter Shipping Point | On the Split Outbound Delivery screen, make the following entry:Shipping point: 3310 |  |  |
| 4 | Enter Outbound Delivery | To speed up selection, make the following entry on the same screen:Outbound Delivery: <Outbound Delivery Document Number> |  |  |
| 5 | Choose Split Profile | In the Split Profile field, make the following entry or select the following value from the list:Split Profile: 0003 (Delivery Split - LE Components) |  |  |
| 6 | Start Selection | Choose Execute. | A list of outbound delivery items for the selected Shipping Point and Outbound Delivery is displayed. |  |
| 7 | Select Items for Split | Select the items that should become part of a new delivery that must be split from the current delivery.Enter <Split Quantity> and choose Save Split. | The selected items are displayed with a new delivery document number. The items not selected for the split still appear with the former document number. |  |

### Add Freight Cost (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to want to add the actual freight costs to the Outbound Delivery after you know the exact weights and freight charges.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). |  |  |
| 3 | Enter Number | On the Change Outbound Delivery screen, enter <outbound delivery number> and choose Enter. |  |  |
| 4 | Open Conditions | From the menu, choose Goto > Header Conditions . |  |  |
| 5 | In the Condition Type Data | In the Condition Type column, enter YBHD. |  |  |
| 6 | Enter Freight Costs | In the Amount column, enter <Freight Costs (such as 100)>. | The system distributes the entered amount across the delivery items. The distribution is executed on the basis of the net weight of each item. |  |
| 7 | Save | Save your outbound delivery. | Freight Costs are added to the Outbound Delivery and later copied to the Invoice. |  |

### Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process shows you how to post the goods issue.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). | The Change Outbound Delivery screen displays. |  |
| 3 | Enter Outbound Delivery Number | Make the following entries and Choose Continue.Outbound Delivery: <delivery number created previously> | The Delivery XXX Change: Overview screen displays. |  |
| 4 | Post Good Issue | Choose Post Goods Issue. | The goods issue is posted. |  |

### Proof of Delivery (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you record the quantities as confirmed by the respective customer after physical arrival of goods delivered. Thus document the right quantities that should become subject to billing to this customer.

This is only possible for Outbound Deliveries if the customer master data have been maintained in a way that this customer is "POD-relevant" (on sales area level).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Change Outbound Delivery - Proof of Delivery (VLPOD). |  |  |
| 3 | Enter Outbound Delivery | On the same screen, make the following entry, and choose Continue:Outbound Delivery: <your Outbound Delivery Document Number> | The selected Outbound Delivery Document screen displays, and Overview POD tab becomes active. |  |
| 4 | Quantity Difference | If there is a quantity difference between shipping and receiving, go to step 5 and 6. |  |  |
| 5 | Enter POD Delivery Reason (Optional) | In the line with the item for which a differing quantity was reported by the customer, make the following entry or select the following value from the list:Reason: <DFG2(Underdelivery, reason unknown)> |  |  |
| 6 | Enter Deviation (Optional) | In the Quantity Difference field, go to Sales Unit (Qty Diffin Sales Un), enter <respective quantity (differs from the expected Delivery Quantity as per the Outbound Delivery Item)>, and choose Enter. | The quantity displayed for the respective item in the POD quantity field has been recalculated (Quantity Difference subtracted from Delivery Quantity).The value for POD Status field has changed to B (Differences Reported). |  |
| 7 | Confirm Delivery Proof | Choose Confirm Proof of Delivery. | The POD Date field has been filled with the current date.The value for the POD Status field has changed to C (Confirmed). |  |
| 8 | Save | Choose Save. | The Outbound Delivery document is saved with confirmation for actually delivered quantities.These will be used for the consecutive billing step. |  |

### Create Billing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

In this activity, you handle the billing.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App |  | The Create Billing Documents screen displays. |  |
| 3 | Define Billing Setting | Choose Billing Settings in the bottom bar, you can make the following settings as below:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: OFFAutomatically post billing documents: ONDisplay billing documents after creation: ONChoose delivery items to be billed and select quantities: OFF |  |  |
| 4 | Search for Billing Due List | In the search condition, use criteria if necessary. | Sales document displays in the result. |  |
| 5 | Select Item for Billing | Select row of SD Document created previously, and choose the Create Billing Documents. | The Create Billing Documents screen displays. |  |
| 6 | Maintain Billing Date | Choose billing type Invoice (F2) and maintain billing date, for example current date, then choose OK. | The system generates an invoice for billing. |  |
| 7 | Save Billing Document | Save you entries.Make a note of the billing document number: __________. | To access the accounting data, navigate to Process Flow and click Journal Entry and navigate to Display Journal EntriesMaterial: Non-Stock Material (NLAG)Debited Accounts: 33100003Rcvbls Domestic UAE Customer 3Credited Accounts:41910000 Billed Rev Domestic Prod22001000 Output tax accrued52590000 (optional) Freight Revenue/Rec.44002000 Sales Disc Domestic (if item category TAXN has been used) |  |
| 8 | Access the App | Open Manage Billing Documents (F2250). | The Display Billing Documents screen displays. |  |
| 9 | Enter Billing Number | In the Billing Document field, enter <respective invoice number> and choose Enter. | The Invoice xxx Display: Overview of Billing Items screen displays. |  |
| 10 | Check Output Condition | On the Invoice xxx Display: Overview of Billing Items screen, choose Menu→ More→ Goto→ Header → Output. | The Invoice XXX Display: Output screen displays. |  |
| 11 | Display Print Preview | On the Invoice xxx Display: Output screen, select the line already created for the print output and choose Display PDF Document. | Preview for PDF document displays. |  |

### Create Pro Forma Invoice (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create Pro Forma invoice with reference to delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpads displays. |  |
| 2 | Access the App | Open Create Billing Documents - VF01 (VF01). | The Create Billing document screen displays. |  |
| 5 | Choose Individual Billing Document | Enter delivery document created previously and choose Create Billing Documents. |  |  |
| 6 | Maintain Billing Type and Billing Date | Choose Pro Forma Invoice for Delivery (F8) billing type and billing date, for example current date, then press OK . | The draft pro forma invoice is created. |  |
| 7 | Save Pro Forma Invoice | In the Billing Document screen, click Save.The draft billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx. Make a note of the billing document number: __________. | Pro forma invoice is generated. |  |

|  |
| --- |
| Note Alternatively, it is supported to create Pro Forma (type F5) with reference to sales order. |

Manage Billing Documents Procedures

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpads displays. |  |
| 2 | Access the App | Open Manage Billing Documents (F0797). | The Manage Billing Document screen displays. |  |
| 3 | Enter Invoice | Input the pro-forma invoice number recorded in previous step. Choose Enter. | The billing document created in previous step displays. |  |
| 4 | Display Billing Document | Select the billing document item, and choose Display. | The billing document displays. |  |
| 5 | Check Output Condition | On the Billing Document screen, choose the last assignment block: Output Items. | There is one entry in the item with the BILLING_DOCUMENT output type. |  |
| 6 | Display Print Preview | On the Billing Document screen, choose Preview. | Preview for PDF document displays. |  |
| 7 | Update New Attachment (Optional) | In the Edit mode, add, delete, and update the attachments.Save your changes by pressing Save in the footer bar. |  |  |
| 8 | Update New Text (optional) | In the Edit mode, you can add, delete, and update these texts.Save your changes by pressing Save in the footer bar. |  |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| Accounts Receivable (J59) | Posting a Customer Invoice in Accounting, and so on.Using the master data from this document, complete the following activities described in the test script:Posting a Customer Invoice in AccountingOverdue Receivables, Display Customer BalancesManage Customer Line Items |
| Sales Period End Closing Operations (BKK) (optional) | This scope item describes the collection of periodic activities such as day ending activities, or reporting.Using the master data from this document, complete all the activities described in the Test Script of the scope item:Review Incomplete SAP Digital Documents (deliveries),Review Sales Documents blocked for billingReview Log of collective invoice creation |

### Scheduling Job Creation (Optional)

#### Scheduling Job for Delivery Creation (Optional)

Purpose

This process step shows you how to define the schedule background job for creation outbound deliveries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Delivery Creation (F2228). | The Application Jobs displays. The app must be started with the history of application jobs. |  |
| 3 | Create Delivery Creation Schedule | Choose New to define a new job. | The New Job view displays. Job Template should default as Schedule Delivery Creation. |  |
| 4 | Job Parameters | Define scheduling options and parameter section for batch job if necessary, then choose Check. | The system displays the notification Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A delivery creation job is scheduled. The view backs to Application Jobs. |  |
| 6 | Check Delivery Creation Job Log | In the Application Jobs view, after job item status turn to Finish, choose Status symbol in Logcolumn.Note Choose Magnifier, the job list refreshes. | The view goes to job log details. |  |

#### Scheduling Job for Goods Issue Deliveries (Optional)

Purpose

This process step shows you how to define the schedule background job for goods issue for deliveries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Goods Issue for Deliveries (F2259). | The Application Jobs displays. The app must be started with the history of application jobs. |  |
| 3 | Create Goods Issue Deliveries Schedule | Choose New to define a new job. | The New Job view displays. Job Template should default as Schedule goods issue for Deliveries. |  |
| 4 | Job Parameters | Define scheduling options and parameter section for batch job if necessary, then choose Check. | The system displays the notification Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A schedule goods issue for deliveries job is scheduled. The view back to Application Jobs. |  |
| 6 | Check Goods Issue Deliveries Job Log | In the Application Jobs view, after job item status turn to Finish, choose Status symbol in Log column.Note Choose Magnifier, the job list refreshes. | The view goes to job log details. |  |

#### Scheduling Job for Billing Creation (Optional)

Purpose

This process step shows you how to define the schedule background job for creation billing documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Billing Creation (F1519). | The Application Jobs displays. The app must be started with the history of application jobs. |  |
| 3 | Create Billing Creation Schedule | Choose New to define a new job for billing creation. | The New Job view displays. Job Template should default as Schedule Billing Creation. |  |
| 4 | Job Parameters | Define scheduling options and parameter section for batch job if necessary, then choose Check. | The system displays the notification Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A billing creation job is scheduled. View backs to Application Jobs. |  |
| 6 | Check Billing Creation Job Log | In the Application Jobs view, after job item status turn to Finish, choose Job Log.Note Choose the Magnifier,the job list refreshes. | The view goes to log details. |  |

#### Scheduling Job for Billing Release (Optional)

Purpose

This process step shows you how to define the schedule background job for release billing documents to accounting.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Billing Release (F1518). | The Application Jobs displays. The app starts with the history of application jobs. |  |
| 3 | Create Billing Release Schedule | Choose New to define a new job for billing creation. | The New Job view displays. Job Template should default as Schedule Billing Release. |  |
| 4 | Job Parameters | Define scheduling options and parameter section for batch job if necessary, then choose Check. | The system displays the notification Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A billing release job is scheduled. The view back to Application Jobs. |  |
| 6 | Check Billing Release Job Log | In the view Application Jobs, after job item status turn to Finish, choose Job Log.Note Choose the Magnifier,the job list refreshes. | The view goes to log details. |  |

#### Scheduling Job for Billing Output (Optional)

Purpose

This process step shows you how to define the schedule background job for when and how billing documents are sent to customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Billing Output (F1510). | The Application Jobs displays. The app shall be started with the history of application jobs. |  |
| 3 | Create Billing Output Schedule | Choose New to define a new job for billing creation. | The New Job view displays. Job Template should default as Schedule Billing Output. |  |
| 4 | Job Parameters | Define scheduling options and parameter section for batch job if necessary, then choose Check. | The system displays the notification Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A billing output job is scheduled. The view back to Application Jobs. |  |
| 6 | Check Billing Output Job Log | In the view Application Jobs, after job item status turns to Finish, choose Job Log.Note Choose the Magnifier,the job list refreshes. | The view goes to log details. |  |

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
- related-to :: [[08-sales-order-management/test-script-sales-of-non-stock-item-with-order-specific-procurement-bd]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2ET_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 47,534 chars in the whole document
