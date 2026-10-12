---
id: 08-sales-order-management/test-script-sales-order-fulfillment-monitoring-and-operations-bkk-ae-1
title: "Test Script: Sales Order Fulfillment Monitoring and Operations (BKK_AE) (BKK_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script (BKK_AE) for sales order fulfillment monitoring: mass change, incomplete/duplicate docs, delivery, billing."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/sales-fulfillment-monitoring-and-analytics]
aliases: [BKK_S4CLD2608_BPD_EN_AE]
keywords: [Sales Order Fulfillment Monitoring and Sales Analytics, sales order fulfillment, mass change of sales documents, incomplete sales documents, duplicate sales documents, sales order tracking, delivery creation, delivery logs, goods issue, billing due list]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BKK_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1279
topic: 08-sales-order-management/sales-fulfillment-monitoring-and-analytics
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Sales Order Fulfillment Monitoring and Operations (BKK_AE) (BKK_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BKK_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Sales Order Fulfillment Monitoring and Sales Analytics** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Sales Order Fulfillment Monitoring and Operations (BKK_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232862045)

[2 Prerequisites 4](#_Toc232862046)

[2.1 System Access 4](#_Toc232862047)

[2.2 Roles 4](#_Toc232862048)

[2.3 Master Data and Organizational Data 5](#_Toc232862049)

[2.4 Business Conditions 6](#_Toc232862050)

[3 Overview Table 7](#_Toc232862051)

[4 Test Procedures 9](#_Toc232862052)

[4.1 Mass Change of Sales Documents 9](#_Toc232862053)

[4.2 List Incomplete Sales Inquiries 10](#_Toc232862054)

[4.3 List Incomplete Sales Quotations 11](#_Toc232862055)

[4.4 List Incomplete Sales Documents 12](#_Toc232862056)

[4.5 List Incomplete Sales Contracts 13](#_Toc232862057)

[4.6 Track Sales Orders 14](#_Toc232862058)

[4.7 Review Duplicate Sales Documents 15](#_Toc232862059)

[4.8 Review Sales Order Fulfillment 16](#_Toc232862060)

[4.9 Review Sales Orders due for Delivery 18](#_Toc232862061)

[4.10 Review Log of Delivery Creation 19](#_Toc232862062)

[4.11 Review Outbound Deliveries for Goods Issue 20](#_Toc232862063)

[4.12 Review Billing Due List 20](#_Toc232862064)

[4.13 Review Log of Collective Invoice Creation 22](#_Toc232862065)

[4.14 Review List of Blocked Billing Documents (for Accounting) 23](#_Toc232862066)

[4.15 Review Schedule Billing Release for Accounting 24](#_Toc232862067)

## Purpose

Overview

As an internal sales representative, you use the Sales Order Fulfillment Monitor to address problems that occur during the sales order fulfillment process. You can then directly execute follow-up steps from the monitor to resolve these issues. Examples of issues are missing documents, missing or unconfirmed information, and various types of blocks as well as product and trade compliance issues. You can use the application to search for specific sales orders. You can also filter the list of issues according to the stage at which they occur (such as in order, supply, delivery, invoice, or accounting).

As an internal sales representative you use the Sales Order Cockpit to manage mass changes of different types of sales documents on the header and item levels. Flexible filter capabilities help to prepare the list of documents and items to be changed. The change jobs can be scheduled for background processing and monitoring.

Further productivity enhancements are provided for managing duplicate sales orders. The Manage Duplicate Sales Document app can be used to analyze and clear your system of duplicate sales documents. After identifying duplicates, the internal sales representative can reject them to avoid the redundant processing of duplicate sales documents.

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

### Master Data and Organizational Data

SAP Best Practices Standard Values

Essential master and organizational data was created in your ERP system in the implementation phase, such as the data that reflects the organizational structure of your company and master data that suits its operational focus, for example, master data for materials, vendors, and customers.

This master data usually consists of standardized SAP Best Practices default values, and enables you to go through the process steps of this scope item.

|  |
| --- |
| Note Additional Master Data (Default Values)You can test the scope item with other SAP Best Practices default values that have the same characteristics. |

Check your SAP ECC system to find out which other material master data exists.

|  |
| --- |
| Note Using Your Own Master DataYou can also use customized values for any material or organizational data for which you have created master data. For more information about creating master data, see the Master Data Procedures documentation. |

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Master / Org. data | Value | Master / Org. data details | Comments |
| --- | --- | --- | --- |
| Material | TG11 | Trading Good for Reg. Trading (MRP planning)No serial number, no batch. | See sections Business Conditions and Preliminary Steps. |
| Material | TG12 | Trad.Good 12,Reorder Point,Reg.Trad.No serial number, no batch. | See sections Business Conditions and Preliminary Steps. |
| Material | TG21 | Trad.Good 21,Reorder Point,Batch-FIFONo serial number, batch controlled (FIFO strategy). | Only use if you have activated the building block Batch Management (BLG) (BLH)(BLJ)(BLP).See sections Business Conditions and Preliminary Steps. |
| Material | TG22 | Trad.Good 22,Reorder Point,Batch-ExpDNo serial number, batch controlled (Exp. Date). | Only use if you have activated the building block Batch Management (BLG) (BLH)(BLJ)(BLP).See sections Business Conditions and Preliminary Steps. |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Shipping Point | 3310 | Shipping Point 3310 |  |
| Sales organization | 3310 | Dom. Sales Org |  |
| Distribution channel | 10 | Direct Sales |  |
| Division | 00 | Product Division 00 |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BND | Create Customer Master - MDS |

### Business Conditions

The business process described in this Test Script is part of a bigger chain of integrated business processes or scope items. As a consequence, you must have completed the following processes and fulfilled the following business conditions before you are able to start going through this scope item:

| Scope item | Business Condition |
| --- | --- |
| J45 - Procurement of Direct Materials | To run through this scope item, the materials must be available in stock. If you use trading goods (HAWA) you can either:Run through the Procurement of Direct Materials(J45) processOr create stock using transaction MIGO (for details see section Preliminary Steps). |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business role | Transaction/App | Expected results |
| --- | --- | --- | --- |
| [Mass Change of Sales Documents](#unique_8) [page ] 9 | Internal Sales Representative | Mass Change of Sales Documents (F5091) | Mass change of sales documents is achieved. |
| [List Incomplete Sales Inquiries](#unique_9) [page ] 10 | Internal Sales Representative | List Incomplete Sales Inquiries (F2430) |  |
| [List Incomplete Sales Quotations](#unique_10) [page ] 11 | Internal Sales Representative | List Incomplete Sales Quotations (F2430) |  |
| [List Incomplete Sales Documents](#unique_11) [page ] 12 | Internal Sales Representative | List Incomplete Sales Documents (F2430) |  |
| [List Incomplete Sales Contracts](#unique_12) [page ] 13 | Internal Sales Representative | List Incomplete Sales Contracts (F2430) |  |
| [Track Sales Orders](#unique_13) [page ] 14 | Internal Sales Representative | Track Sales Orders (F2577) |  |
| [Review Duplicate Sales Documents](#unique_14) [page ] 15 | Internal Sales Representative | Manage Duplicate Sales Documents (F3245) | Get an overview list of the duplicate sales documents, you can reject the ones that are not relevant after check. |
| [Review Sales Order Fulfillment](#unique_15) [page ] 16 | Internal Sales Representative | Sales Order Fulfillment - Analyze and Resolve Issues (F0029A) | Get an overview of issues around the Sales Documents. |
| [Review Sales Orders due for Delivery](#unique_16) [page ] 18 | Shipping Specialist | My Sales Order Items - Due for Delivery (VL10C) | Sales orders that were due for delivery creation are now turned into deliveries. If the creation fails, a log entry will be generated. |
| [Review Log of Delivery Creation](#unique_17) [page ] 19 | Shipping Specialist | Analyze Delivery Logs (F0870A) | Sales orders for which the delivery creation failed are filed in this log. |
| [Review Outbound Deliveries for Goods Issue](#unique_18) [page ] 20 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | The goods issue is posted. |
| [Review Billing Due List](#unique_19) [page ] 20 | Billing Clerk | Create Billing Documents (F0798) | If no errors occurred the billing documents are created and the billing values are forwarded to Financial Accounting. |
| [Review Log of Collective Invoice Creation](#unique_20) [page ] 22 | Billing Clerk | Schedule Billing Creation (F1519) | Sales orders / deliveries for which the billing creation failed are filed in this log. |
| [Review List of Blocked Billing Documents (for Accounting)](#unique_21) [page ] 23 | Billing Clerk | Manage Billing Documents (F0797) | Billing documents that were blocked are now listed respectively. |
| [Review Schedule Billing Release for Accounting](#unique_22) [page ] 24 | Billing Clerk | Schedule Billing Release (F1518) | Billing documents that were blocked are now released respectively the reason why they are still blocked is reported. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Mass Change of Sales Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to schedule changes to sales documents via jobs and how to monitor the jobs.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative role. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Mass Change of Sales Documents (F5091). | The Mass Change of Sales Documents screen displays. |  |
| 3 | Select business object type | On the Mass Change of Sales Documents screen, click on the business object card under the section Create Change Jobs for Sales Documentsfor which you want to make changes. | The business object relevant worklist screen displays e.g. the Mass Change of Sales Orders screen. |  |
| 4 | Search For Sales Orders | Fill in the relevant search criteria and choose Go.For example, enter sold-to party name in the Sold-to party field. | All sales orders for the selected sold-to partiy are displayed on the Sales Orderstab and all sales order items are displayed on the Sales Order Itemstab. |  |
| 5 | Select documents for change | Select the sales orders or sales order items which you want to change. | The selected documents or document items are highlighted. |  |
| 6 | Choose change action | Choose a change option out of the offered options when you click on the button Change on top of the sales orders or sales orders item table. | Dependent on the chosen change option a dialog will guide you to specify the change e.g. set a delivery block or offer you the fields for change on header or item field. |  |
| 7 | Specify the new value | Choose from the drop-down list or from the value help the new value the sales order or sales order item shall be changed to. |  |  |
| 8 | Submit change | When you have specified the change click the Submit button and submit the job. | A Pop-up screen appears where you can specify an individual job name. After clicking Submit, a job will be scheduled to execute the changes. |  |
| 9 | Review the Job | Go back to the Mass changes of Sales Documents screen and review the jobs in the area My Jobs. The jobs are clustered under three status: Failed, In Process and Completed. Search for the job name and navigate to the job details page by pressing on the table line. | The Job Detail screen displays. |  |
| 10 | Retry | If the job failed you can repeat the changes either manually or by creating a new job. In this case you can click on the button Schedule New Jobat the top of the screen. | The current Job will be set to status Completed and a new job with the same name is created to repeat the changes. |  |

### List Incomplete Sales Inquiries

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display a list of sales inquiries that is based on the specified selection criteria.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open List Incomplete Sales Inquiries (F2430). | The Incomplete Sales Documents screen displays. |  |
| 3 | Search For Incomplete Sales Inquiry | On the Incomplete Sales Documents screen, enter the relevant search criteria and choose Go.For example, enter sales inquiry number in the Sales Document field. | Sales Inquiry is displayed in result list. |  |
| 4 | Select a Sales Inquiry to Review | Click item for a sales inquiry to review detailed issue. | The Change Inquiry 10XXXXXX: Incompletion Log screen displays. |  |
| 5 | Check Log | You can see the missing data of detail information on the Change Inquiry 10XXXXXX: Incompletion Log screen. |  |  |

### List Incomplete Sales Quotations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display a list of sales quotations that is based on the specified selection criteria.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open List Incomplete Sales Quotations (F2430). | The Incomplete Sales Documents screen displays. |  |
| 3 | Search For Incomplete Sales Quotation | On the Incomplete Sales Documents screen, enter the relevant search criteria and choose Go.For example, enter sales quotation number in the Sales Document field. | Sales Quotation is displayed in result list. |  |
| 4 | Select a Sales Quotation to Review | Click item for a sales quotation to review detailed issue. | The Change Quotation 20XXXXXX: Incompletion Log screen displays. |  |
| 5 | Check Log | You can see the missing data of detail information on the Change Quotation 20XXXXXX: Incompletion Log screen. |  |  |

### List Incomplete Sales Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display a list of sales inquiries that is based on the specified selection criteria.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open List Incomplete Sales Documents (F2430). | The Incomplete Sales Documents screen displays. |  |
| 3 | Search For Incomplete Sales Documents | On the Incomplete Sales Documents screen, enter the relevant search criteria and choose Go.For example, enter sales order number in the Sales Document field. | Sales Order is displayed in result list. |  |
| 4 | Select a Sales Order to Review | Click item for a sales order to review detailed issue. | The Change Standard Order XXX: Incompletion Log screen displays. |  |
| 5 | Check log | You can see the missing data of detail information on the Change Standard Order XXX: Incompletion Log screen. |  |  |

### List Incomplete Sales Contracts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display a list of contracts that is based on the specified selection criteria.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open List Incomplete Sales Contracts (F2430). | The Incomplete Sales Documents screen displays. |  |
| 3 | Search For Incomplete Sales Documents | On the Incomplete Sales Documents screen, enter the relevant search criteria and choose Go.For example, enter sales order number in the Sales Document field. | Contract is displayed in result list. |  |
| 4 | Select a Sales Quotation to Review | Click item for a contract to review detailed issue. | The Change XXX Contract 40XXXXXX: Incompletion Log screen displays. |  |
| 5 | Check Log | You can see the missing data of detail information on the Change XXX Contract 40XXXXXX: Incompletion Log screen. |  |  |

### Track Sales Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display a list of sales documents that is based on the specified selection criteria.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative role. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Track Sales Orders (F2577). | The Track Sales Orders screen displays. |  |
| 3 | Search For Sales Order | On the Track Sales Orders screen, enter the relevant search criteria and choose Go.For example, enter sales order number in the Sales Documentfield. | Sales order displays in result list. |  |
| 4 | Check Status | Check status under Overall Fulfillment for sales document. Click the blank area of the sales document to check detailed information. | The Track Sales Orders screen displays. |  |
| 5 | Check Detail Information | You can see detailed information on the Track Sales Orders screen, Shipping Status, Invoicing Status, Net Value and Document flow. |  |  |
| 6 | Check Detail Information | You can choose click to select on Standard Order, Delivery or Invoice line to see the Details. |  |  |

### Review Duplicate Sales Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this app, you can search for duplicate sales documents, for example, sales orders, quotations, returns, and reject the ones not required, to avoid duplicate sales documents being processing multiple times. After checking the duplicates, you can reject the ones that are not relevant. As a result, the list of duplicates is refreshed. and the rejected duplicates are not displayed. This process step shows you how to review duplicate sales documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Launchpad displays. |  |
| 2 | Access the App | Open app Manage Duplicate Sales Documents (F3245). | The Manage Duplicate Sales Documents screen displays. |  |
| 3 | Search for Duplicate Sales Documents | On the screen Manage Duplicate Sales Documents, search according to various criteria by choosing Adapt Filters.Duplicates can be detected according to the following criterias:Sales documentSales document categorySales organizationSold-to partyNet value (of the sales document)Transaction currencyCreation dateCustomer referenceThen click Go. | Duplicate sales documents are displayed in the result list. |  |
| 4 | Check Duplicate Entries | Checking the duplicates by reviewing detailed columns information. |  |  |
| 5 | Reject Not Relevant Document | Select a document which is not relevant, click Reject Duplicate.On the pop-up screen Reject All Items, make the following entry and choose OK.Reason of Rejection, for example, Rejected by Approver. | The list of duplicates is refreshed, and the rejected duplicate entry is not displayed any more. |  |
| 6 | Choose Back | Choose Back. |  |  |

### Review Sales Order Fulfillment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to call the Sales Order Fulfillment to check the status of sales documents. You can get an overview sales orders and can navigate to documents related to the process flow of the sales order.

Frequency

Daily

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Sales Order Fulfillment - Analyze and Resolve Issues (F0029A).Please do not use search function to search for the app. The app locates under Insights category. | The Sales Order Fulfillment screen displays. |  |
| 3 | Swich to Compact Filter Mode | Swich to Compact Filter mode by click on Compact Filter in upper screen. |  |  |
| 4 | Set filters of Issue | In the dropdown list of Issue, choose the issue you interested in and choose Go, for example:Credit Block in Sales OrdersImcomplete Data in Sales OrdersDelivery Block in Sales OrdersBilling Block in Sales Orders |  |  |
| 5 | Change View Settings | In order to indentify sales documents with the issues more easily, you can change the view settings.In the chapter of Sales Document with Issues, Choose Settings. In the pop-up window of View Settings, in the tab of Columns, deselect Next Action in DaysAlso You can maximize the table of Sales Documents with Issues by choose Maximize. |  |  |
| 6 | Slove the Sales Order Issues | Choose the relevant sales orders by click the checkbox of the line, and choose Reject All items, or Remove All Delivery Blocks or Remove All Billing Blocks. |  |  |
| 7 | Check Sales Order Details | Choose Details of the Sales orders, you can check detail issue of the sales orders.Click on the Sales orders appear in right screen, you can change the sales orders if neededChoose Back. |  |  |

### Review Sales Orders due for Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Sales orders become due for delivery creation according to their schedule line. The schedule line becomes due for shipping, when the material availability and the transportation scheduling date for a schedule are reached. This process step shows you how to review sales order due for delivery.

Frequency

The frequency depends on the warehouse and shipping organization. The transaction can either be processed repeatedly online or in batch during shipping hours. We recommend processing the delivery due list at a minimum frequency of once a day.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open My Sales Order Items - Due for Delivery (VL10C). | The Sales Order Items screen displays. |  |
| 3 | Search for Sales Order | On the Sales Order Items screen, make the following entries and choose Execute:Shipping Point: 3310Delivery creation dates (From): <enter delivery creation date>Delivery creation dates (To): <enter delivery creation date> | Delivery creation dates (From): The sales order item delivery date must be equal or greater than the delivery creation date (From).Delivery creation dates (To): The sales order item delivery date must be equal or less than the delivery creation date (To). |  |
| 4 | Create Delivery | Select your sales order and choose Create Delivery in the Background. |  |  |
| 5 | Check the Number of Delivery Created | Set the cursor on the line with the green light and choose the Details icon. In the dialog box, you see the number of the delivery that is created. | Sales orders that were due for delivery creation are now turned into deliveries. If the creation fails, a log entry will be generated. |  |

### Review Log of Delivery Creation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This log provides the detailed reasons why a delivery creation has failed. This process step shows you how to identify the reasons and solve the issues.

Frequency

Daily

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Analyze Delivery Logs (F0870A). | The Analyze Delivery Logs (F0870A) screen displays. |  |
| 3 | Search for Delivery Log | On the screen Analyze Delivery Logs (F0870A), input criteria if necessary to filter delivery log, choose Go. |  |  |
| 4 | Select a Delivery Log to Review | Click item for a delivery log to review detail. |  |  |
| 5 | Resolve Any Issues | On the Analyze Delivery Log screen, check issue log in the Messages tab or delivery number created in the Deliveries tab. |  |  |
| 6 | Choose Back | Choose Back. |  |  |

### Review Outbound Deliveries for Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to review deliveries that are due for goods issue.

Frequency

Daily

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Open Outbound Delivery Monitor | Choose For Goods Issue. |  |  |
| 4 | Enter Shipping Point | Make the following entries and choose Execute.Shipping Point: <Shipping Point> |  |  |
| 5 | Post Good Issue | Mark the relevant delivery and choose Post Goods Issue. (Choose today’s date on the dialog box.) | The goods issue is posted. |  |

### Review Billing Due List

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When processing the billing due list, you do not need to enter the individual documents to be invoiced. The system lists the documents to be invoiced on the basis of the selection criteria you enter. It can also combine several deliveries in one invoice. This process step shows you how to review billing due list.

Frequency

Daily

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents - VF04 (VF04). | The Maintain Billing Due List screen displays. |  |
| 3 | Process Billing Due List | On the initial screen, enter the relevant search criteria and in the Documents to Be Selected area. Choose Order-Related, Delivery-Related. |  |  |
| 4 | Display Bill List | Choose Display Billing List. |  |  |
| 5 | Choose Individual Billing Document | Select the row with the sales document, and then choose Individual Billing Document. |  |  |
| 6 | Save Your Entries | Save your entries.Note a) Individual Billing DocumentsAn individual billing document is created for all documents marked in the billing due list. No combination is carried out. You branch to transaction VF01 for every document selected. Any message is displayed during processing of the individual document.b) Collective Billing DocumentsAll documents marked in the billing due list are billed. The system tries to condense them as much as possible. Processing of the selected documents is carried out in the background. After processing of the documents, you return to the billing due list.To display the (Error) log, choose Log Display.On the next screen select the relevant group and choose Notes. Here, icons indicate whether or not a document has been billed successfully.To display the created billing documents, choose Documents.Alternatively check activity Review Log of collective invoice creation.c) Collective Billing Documents / OnlineThe system branches to the Create Billing Document function (transaction VF01 ). The documents are condensed as far as possible according to the usual criteria. Any message is displayed during processing of the individual document. | If no errors occurs, the billing documents are created and the billing values are forwarded to Financial Accounting. |  |

### Review Log of Collective Invoice Creation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This log provides the detailed reasons why an invoice creation has failed. This process step shows you how to identify the reasons and solve the issues.

Frequency

Daily

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Billing Creation (F1519). | The Application Jobs screen displays. |  |
| 3 | Create a new job | Choose Create to create a new job. |  |  |
| 4 | Select Job Template | In the Template Selection section, select Schedule Billing Creation in drop list in the Job Template field. |  |  |
| 5 | Process Billing Due List | Choose Step 2, choose Start Immediately.Select Define Recurrence Pattern.In the upcoming popup, select Single Run for Recurrence Pattern, click Ok and navigate to Step 3 Parameters.Enter Sales Organization.You can also add more Scheduling Options. |  |  |
| 6 | Check Job | Choose Check. | Pop up system message: You can go ahead and schedule the job. |  |
| 7 | Schedule Job | Choose Schedule. | Job scheduled, and screen back to Application Jobs. |  |
| 8 | Check Log | On the Application Jobs screen, after job item’s status turn to Finish, choose Job Log.Note Click magnifier, and the job list will refresh. | Screen goes to log details. |  |

### Review List of Blocked Billing Documents (for Accounting)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This tile provides the list of billing document blocked for accounting. This process step shows you how to identify the reasons and slove the issues.

Frequency

Daily

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Billing Documents (F0797). | The Manage Billing Documents screen displays. |  |
| 3 | Select Billing Documents to Release. | Select To Be Posted in field the Billing Document Status.Make the following entries for filter if necessary.Billing Document: Billing DocumentBilling Type: Billing TypeSold-to Party: CustomerBilling Date: <from date to date> | On the Manage Billing Documents screen, a list of open billing documents shows up. |  |
| 4 | Check Billing Document | Select the row of billing document, and choose Display. | The Billing Document screen displays. |  |

### Review Schedule Billing Release for Accounting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This tile provides the list of billing document blocked for accounting. This process step shows you how to identify the reasons and solve the issues.

Frequency

Daily

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Schedule Billing Release (F1518). | The Application Jobs screen displays. |  |
| 3 | Create a New Job | Choose Create to create a new job. |  |  |
| 4 | Select Job Template | In the Template Selection section, select Schedule Billing Release in drop list in the Job Template field. |  |  |
| 5 | Select Billing Documents to Release | Choose Step 2Choose Start ImmediatelySelect Define Recurrence PatternIn the upcoming popup, select Single Run for Recurrence Pattern, click Ok and navigate to Step 3 Parameters.Make the following entries for filter if necessary:Payer: <Payer>Sales Organization: <Sales Organization>Billing Document: <Billing Document>Billing Type: <Billing Type>Billing Category: <Billing Category>Created By: <blank>Created On: <dd.MM.yyyy>Select the following checkboxes in the Incomplete Due to section and choose Check:Accounting BlockError in Accounting interfaceError in Authorization | Pop up system message: You can go ahead and schedule the job. |  |
| 6 | Schedule Job | Choose Schedule. | Job scheduled, screen turns back to Application Jobs. |  |
| 7 | Check Log | On the Manage Billing Documents (F0797) screen, after job item’s status turn to Finish, choose Job Log. | Screen goes to log details. |  |

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
> Flagged while digesting this document, not verified: Billing due list app is identified as Create Billing Documents (F0798) in the Overview Table but as Create Billing Documents - VF04 (VF04) in the procedure for the same step.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[08-sales-order-management/test-script-sap-fiori-analytical-apps-for-sales-1bs-sap-s-4hana-cloud]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BKK_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 43,504 chars in the whole document
