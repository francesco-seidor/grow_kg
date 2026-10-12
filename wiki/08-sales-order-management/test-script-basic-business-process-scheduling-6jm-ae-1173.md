---
id: 08-sales-order-management/test-script-basic-business-process-scheduling-6jm-ae-1173
title: "Test Script: Basic Business Process Scheduling (6JM_AE) (6JM_S4CLD2608_BPD_EN_AE)"
description: "Test script (UAE/AE) for scope item 6JM, Basic Business Process Scheduling in SAP S/4HANA Cloud Public Edition 2608: activation config and sales order scheduling with days granularity."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/sales-order-scheduling-bps]
aliases: [6JM_S4CLD2608_BPD_EN_AE]
keywords: [Sales Order Scheduling with Business Process Scheduling, business process scheduling, sales order scheduling, bps activation, business roles, test master data, demo data, delivery scheduling, sell from stock, 6JM]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6JM_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1173
topic: 08-sales-order-management/sales-order-scheduling-bps
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Basic Business Process Scheduling (6JM_AE) (6JM_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6JM_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Sales Order Scheduling with Business Process Scheduling** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Basic Business Process Scheduling (6JM_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232858790)

[2 Prerequisites 3](#_Toc232858791)

[2.1 System Access 3](#_Toc232858792)

[2.2 Roles 3](#_Toc232858793)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232858794)

[2.4 Business Conditions 5](#_Toc232858795)

[2.5 Preliminary Steps 5](#_Toc232858796)

[2.5.1 Self-Service Configuration to Activate Business Process Scheduling 5](#_Toc232858797)

[3 Overview Table 8](#_Toc232858798)

[4 Test Procedures 9](#_Toc232858799)

[4.1 Business Process Scheduling 9](#_Toc232858800)

[4.1.1 Create/Change Sales Order with Business Process Scheduling (Days Granularity) 9](#_Toc232858801)

[5 Appendix 12](#_Toc232858802)

[5.1 Process Integration 12](#_Toc232858803)

## Purpose

Overview

Before you can execute business process scheduling, you must perform configuration to activate business process scheduling.

First, you create or change a business document, such as a sales order, with the business process scheduling functionality activated. You can schedule logistically relevant date types that are available at the schedule line level in the sales order (for example, material availability date, delivery date) with the new Business Process Scheduling (BPS) solution using days as the time granularity. BPS is used through the creation or change of a sales document (for example, a sales order).

|  |
| --- |
| Note With the Configure Activity Attributes (F6439) app, you can even more granularly maintain durations and working times for logistical activities for certain characteristic combinations based on the document attributes. This is an addition to Basic Business Process Scheduling (6JM) and is available as part of Advanced Available-to-Promise Processing (1JW). |

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
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Order Fulfillment Manager - Scheduling | SAP_BR_ORD_FLFMT_MNGR_SCHDG | Business Process Scheduling | SAP_SCM_SPT_BUS_PROC_SCHDG_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Material | TG11 | Trading Good for Reg. Trading (MRP planning)No serial number, no batch |  |
| Material | TG12 | Trad.Good 12,Reorder Point,Reg.Trad. |  |
| Sold-to Party | 33100003 | Domestic UAE Customer 3 |  |
| Ship-to Party | 33100003 | Domestic UAE Customer 3 |  |
| Plant | 3310 | Plant 1 AE |  |
| Shipping Point | 3310 | Shipping Point 3310 |  |
| Sales Organization | 3310 | Dom. Sales Org |  |
| Distribution Channel | 10 | Direct Sales |  |
| Division | 00 | Product Division 00 |  |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BND | Create Customer Master - MDS |
| 2YX | Create Supplier Master - MDS |

### Business Conditions

The business process described in this test script is part of a bigger chain of integrated business processes or scope items. As a consequence, you must have completed the following processes and fulfilled the following business conditions before you can go through this scope item:

| Scope Item | Business Condition |
| --- | --- |
| BD9 - Sell from Stock | Create sales orders to find the Business Process Scheduling setup applied.Create Sales OrderCreate Delivery |

### Preliminary Steps

#### Self-Service Configuration to Activate Business Process Scheduling

Purpose

This process step shows you how to enable scheduling with Business Process Scheduling for sales orders.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241).Go to Configure Your Solution and search for Business Process Scheduling. Go to configuration step Activate BPS for Sales Documents. | The Activate BPS for Sales Documents screen displays. |  |
| 3 | Check Data | On the Activate BPS for Sales Documents screen, make the following entries if not available and choose Save:Sales Document Type: ORItem Category: TANShipping Point: 3310Schema: SALES_DAYS |  |  |
| 4 | Access the App | Open Manage Your Solution (F1241).Go to Configure Your Solution and search for Delivery and Transportation Scheduling. Go to configuration step Define Scheduling By Sales Document Type. | The Define Scheduling By Sales Document Type screen displays |  |
| 5 | Check Data | Check if the following entries are made. If not, make the following entries and choose Save:Sales Document Type: ORDelivery Scheduling: X (selected)Transportation Scheduling: X (selected) |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the BPS Configuration Activity | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Activate BPS for Sales Documents.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Check Data | On the Activate BPS for Sales Documents screen, make the following entries if not available and choose Save:Sales Document Type: ORItem Category: TANShipping Point: 3310Schema: SALES_DAYS |  |  |
| 4 | Access the Scheduling Configuration Activity | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Scheduling By Sales Document Type.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 5 | Check Data | Check if the following entries are made. If not, make the following entries and choose Save:Sales Document Type: ORDelivery Scheduling: X (selected)Transportation Scheduling: X (selected) |  |  |

## Overview Table

This scope item consists of several process steps that are listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| Business Process Scheduling |  |  |  |
| [Create/Change Sales Order with Business Process Scheduling (Days Granularity)](#unique_9) [page ] 9 | Internal Sales Representative | Create Sales Orders - VA01 (VA01) | A sales order is created. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

|  |
| --- |
| Note The Enterprise Search function provides a central entry point for finding business objects in your company from different sources using a single search request. You can search for objects such as: apps, fact sheets for business objects. From the data found, you can go directly to the respective apps and fact sheets to display, edit the data or find related objects. |

### Business Process Scheduling

#### Create/Change Sales Order with Business Process Scheduling (Days Granularity)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to schedule logistically relevant date types available at schedule line level in the sales order (for example, material availability date, delivery date) with the new scheduling solution Business Process Scheduling (BPS) with the time granularity ‘Days’. BPS is used through the creation or change of a sales document (here: sales order).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Sales Orders - VA01 (VA01) from SAP Fiori launchpad. | The Create Sales Orders screen displays. |  |
| 3 | Create a Sales Order | Make the following entries:Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00Press Enter. |  |  |
| 4 | Create Order Data | On the Create Standard Order: Overview screen, make the following entries:Sold-to Party: 33100003Ship-to Party: 33100003Cust.Reference: <Customer Reference>Material: TG11, Order Quantity: <50>Material: TG12, Order Quantity: <100>Note The system proposes the current date as the requested delivery date at header level (which is derived for all items automatically). |  |  |
| 5 | Maintain Order Shipping Data | On the overview screen, go to the tab Shipping and make the following entries:Route for item 10: TR0102Route for item 20: TR0101Press Enter. |  |  |
| 6 | Check Results | Select item 10 and choose Schedules Lines for Item.Select the confirmed schedule line and click on the tab Shipping. | The scheduled date types (delivery date, goods issue date, etcetera) are displayed. |  |
| 7 | Verify Results (Optional) | To verify and understand the retrieved scheduling result, you can compare the duration of activities maintained in the Delivery and Transportation Scheduling configuration as described below.Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration, and open Manage Your Solution (F1241). Go to Configure Your Solution and search for Delivery and Transportation Scheduling. Select configuration step Maintain Duration.Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |  |  |
| 8 | Check Results | Return to the overview screen. Select item 20 and choose Schedules Lines for Item.Select the confirmed schedule line and click on the tab Shipping. | The scheduled date types (delivery date, goods issue date, etcetera) are displayed. |  |
| 9 | Verify Results (Optional) | See step 7. |  |  |
| 10 | Save Sales Order | Save the sales order. |  |  |
| 11 | Reopen Sales Order | Open the app Change Sales Orders - VA02 (VA02). Reopen your sales order. | The Change Standard Order: Overview screen displays. |  |
| 12 | Change Sales Order | Change the quantity of both items and choose Availability Check afterwards. |  |  |
| 13 | Check Results | Select each item and choose Schedules Lines for Item.Select the confirmed schedule line and click on the tab Shipping.If the changed quantity could be confirmed by the availability check, verify that the scheduling results remain the same as before (as in steps 6 and 8). | The date types are scheduled for the same dates as before. |  |
| 14 | Reopen Sales Order | Reopen sales order as in step 11. | The Change Standard Order: Overview screen displays. |  |
| 15 | Change Sales Order | Change the delivery date of both items to a weekday approximately two weeks ahead into the future. Then choose Availability Check. |  |  |
| 16 | Check Results | Select each item and choose Schedules Lines for Item.Select the confirmed schedule line and click on the tab Shipping. | Only one schedule line per item is displayed (as the delivery date is set further into the future than the initial date, which was set to the current date by the system).All date types are rescheduled correctly, considering durations and factory calendars for each logistical activity (see step 9). |  |
| 17 | Save Sales Order | Save the sales order. |  |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

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

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6JM_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 19,882 chars in the whole document
