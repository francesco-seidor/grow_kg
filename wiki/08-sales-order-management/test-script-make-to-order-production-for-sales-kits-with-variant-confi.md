---
id: 08-sales-order-management/test-script-make-to-order-production-for-sales-kits-with-variant-confi
title: "Test Script: Make-to-Order Production for Sales Kits with Variant Configuration (4OC_AE) (4OC_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script (4OC_AE, 19-06-26) for creating a sales order for a configurable robot bundle SET material, with prerequisites and succeeding processes."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/sales-kits-with-variant-configuration]
aliases: [4OC_S4CLD2608_BPD_EN_AE]
keywords: [Sales Kits with Variant Configuration and Their Returns, variant configuration, make-to-order production, sales kits, sales order creation, configurable material, initial stock posting, bill of material, business roles, master data scripts]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4OC_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1039
topic: 08-sales-order-management/sales-kits-with-variant-configuration
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Make-to-Order Production for Sales Kits with Variant Configuration (4OC_AE) (4OC_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4OC_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Sales Kits with Variant Configuration and Their Returns** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Make-to-Order Production for Sales Kits with Variant Configuration (4OC_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232855349)

[2 Prerequisites 3](#_Toc232855350)

[2.1 System Access 3](#_Toc232855351)

[2.2 Roles 3](#_Toc232855352)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232855353)

[2.4 Business Conditions 6](#_Toc232855354)

[2.5 Preliminary Steps 6](#_Toc232855355)

[2.5.1 Initial Stock Posting for the Material in BOM 6](#_Toc232855356)

[2.5.2 Material master data preparation (Optional) 7](#_Toc232855357)

[3 Overview Table 8](#_Toc232855358)

[4 Test Procedures 9](#_Toc232855359)

[4.1 Create Sales Order with Configurable Material 9](#_Toc232855360)

[5 Appendix 11](#_Toc232855361)

[5.1 Succeeding Processes 11](#_Toc232855362)

[5.1.1 Manufacturing Steps Production Order Processing (Optional) 11](#_Toc232855363)

[5.1.2 Delivery and Billing Processing (Optional) 13](#_Toc232855364)

[5.2 Relevant Processes 13](#_Toc232855365)

## Purpose

Overview

Customers want to have a way to use variant configuration and show the component as sales kits (SET) during order taking and follow up processes.

This scope item shows a make-to-order production scenario for sales kits using advanced variant configuration for an efficient state-of-the-art configuration of a material ordered by a customer.

The configurable material is defined as a SET material. In this process, a sales order is created with an individual configuration for a robot bundle. This is captured by defining the different component characteristics desired by the customers and considering the constraints and dependencies of the components. The sales price calculation is then based on the individually chosen characteristics of the components. The sales order is considered for production planning when doing the materials requirements planning. The production execution for the individual robot bundle takes place before delivering it to the customer. The process finishes with the billing to the customer.

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
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |
| Production Engineer - Discrete Manufacturing | SAP_BR_PRODN_ENG_DISC | Production Engineering - Discrete Manufacturing | SAP_BR_PRODN_ENG_DISC |  |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |
| Product Configuration Modeler | SAP_BR_PRODUCT_CONFIG_MODELER | Variant Configuration | SAP_BR_PRODUCT_CONFIG_MODELER |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure. If you have installed an SAP Best Practices baseline package, you can use the following baseline package sample data:

Manufacturing / Trading

Production Plant

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | AVC_RBT_BUNDLE | Robot Bundle |  |
| Material | AVC_RBT_ROBOT | Robot Base Unit |  |
| Material | AVC_RBT_APPL_UNIT | Painting Unit |  |
| Material | AVC_RBT_SEALING | Sealing Unit | Initial stock posting required |
| Material | AVC_RBT_PAINTING | Painting Unit | Initial stock posting required |
| Material | AVC_RBT_CNTRL_UNIT | Control Unit |  |

Bill of Material Structure

This overview shows the bill of material structure and the usage of each component if you have activated all optional enhancements.

This is a super BOM list for configurable materials. Not all components necessarily used in production order.

| Material | Level | Material Type | Unit | Characteristics of Material | Optional Enhancements |
| --- | --- | --- | --- | --- | --- |
| AVC_RBT_BUNDLE | 0 | KMAT | PC | Configurable Robot Arm |  |
| AVC_RBT_ROBOT | 1 | KMAT | PC | Robot Base Unit |  |
| AVC_RBT_APPL_UNIT | 1 | KMAT | PC | Robot Application Unit |  |
| AVC_RBT_SEALING | 1 | HAWA | PC | Sealing Unit |  |
| AVC_RBT_PAINTING | 1 | HAWA | PC | Painting Unit |  |
| AVC_RBT_CNTRL_UNIT | 1 | KMAT | PC | Control Unit |  |

Sales Center

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Sales Organization | 3310 |  | National |
| Distribution Channel | 10 |  | Direct Sales |
| Customer | 33100001 |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| BND | Create Customer Master - MDS |
| 2NI | Create Application Group and Characteristic Display - MDS |
| 2T7 | Create Product Master of Type "Configurable Material" - MDS |
| BNJ | Create Production Work Center - MDS |
| BNK | Create Material BOM for Production and Sales - MDS |
| BNL | Create Routing - MDS |
| BLD | Create Production Version - MDS |

### Business Conditions

Before this scope item can be tested, the following business condition must be met.

| Scope Item | Business Condition |
| --- | --- |
| BEG - Standard Cost Calculation | You have completed the step described in the Test Script Standard Cost Calculation (BEG). |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS (BNZ) master data script. Posting Period is up to date. |
| 22T - Set Up Configurable Model Using Variant Configuration (Optional) | If you are going to execute 1YT with Set Up Configurable Model Using Variant Configuration Sample Master Data, you must have completed the preliminary step in 1YT for CM-FL-V01 material to enable the material for production and sales and distribution process. |

### Preliminary Steps

#### Initial Stock Posting for the Material in BOM

Purpose

In a real business case, the materials are usually purchased from external vendors; in that case, that process is covered by the standard purchasing or subcontracting processes. This process step shows you how to post initial stock directly to the storage locations. Note that you only need to post initial stock in case there is none available or the current stock is insufficient. Ensure that at least as many components for the configurable material, for example, forklifter, are available as you intend to sell in the later step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Stock (F1062). | The Manage Stock (F1062) screen displays. |  |
| 3 | Input Material | Make the following entry and choose Enter:Material: AVC_RBT_PAINTING or AVC_RBT_SEALING, for examplePlant:3310 |  |  |
| 4 | Select Stock | Select the icon beside the stock that you want to add initial stock, for example:Storage Location: 331BUnrestricted - Use Stock | A dialog box opens. The Storage Location, Stock Type, and Current Quantity display according to your entries in the previous steps. |  |
| 5 | Add Initial Entry | Make the following entries and choose Post:Document Date: <today>Posting Date: <today>Stock Change: Intial EntryQuantity: <Enter a number> | The Material document XXX created. message displays. The stock has been added. |  |

#### Material master data preparation (Optional)

If you would like to test the planned / Production order for sales kits with Variant configuration (Pricing and logistics on Header item), pleaser copy BOM of the new material AVC_RBT_ROBOT1 from AVC_RBT_ROBOT usage 1 to usage 3 using FIORI App: Maintain Bill Of Material - Create, change & display BOMs (F1813)

Role: SAP_BR_PRODN_ENG_DISC

- Select components that should appear in sales order and press Item Detail button
- Go to Status/Long Text tab
- Under the Status/Long text mark relevant to sales as X
- Then save

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/APP | Expected Results |
| --- | --- | --- | --- |
| [Create Sales Order with Configurable Material](#unique_10) [page ] 9 | Internal Sales Representative | Manage Sales Orders (F1873) |  |

## Test Procedures

### Create Sales Order with Configurable Material

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Sales order is created with an individual configuration for a robot bundle.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders (F1873) screen displays. |  |
| 3 | Navigate to Create Sales Order Screen | On Manage Sales Orders (F1873) screen, select Create Sales Order - VA01. |  |  |
| 4 | Enter the Order type OR (Standard Order) | On the Create Sales Order: Initial Screen, make the following entries and choose Continue:Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 5 | Enter Order Details | On the Create Standard Order: Overview screen, make the following entries and press Enter:Sold To party: 33100001Ship To party: 33100001Cust. Reference: Reference number Enter a customer purchase order number as referenceReq. Deliv. Date: <Current date + 5 days> |  |  |
| 6 | Enter Characteristic Value | There are two optional ways to configure the characteristic value for the material. You can choose to execute either step 6.In the All Items section, enter the following value and choose Enter.Material Number:AVC_RBT_BUNDLEQuantity: for example, 1 PCNote If you want to create billing plan for this sales order, manually enter the following value as well. If not, press Enter.ItCa (Item category): CBTMOn the Variant Configuration screen, select value for characteristics below and choose Done.Robot Bundle Robot Appplication: <Sealing>Service Level agreement:<8h at five days a week>Robot Base UnitReach(Minimum)-Requested<10>.Reach(Maximum)-Requested<50> |  |  |
| 7 | Save Document | Choose Save Document. Make a note of the sales order number: __________. | The order is saved.Note If the sales order might require approval, please refer to scope item Sell from Stock (BD9), and complete the activities of Process Sales Order Approval. |  |

## Appendix

### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| J59 - Accounts Receivable | Complete the following activities:Posting a Customer Invoice in AccountingOverdue ReceivablesDisplay Customer BalancesManage Customer Line Items |
| BEI - Period-End Closing – Plant | Complete the following activities:Perform the period end financial accounting activities for the plant. These are executed collectively as a part of month-end closing, and can only be executed once a month. |

#### Manufacturing Steps Production Order Processing (Optional)

Purpose

This process step shows you how to create stock (Sales order stock) for material finished goods, the detail steps please find in test script BJE.

Procedure

To produce the material and get it into Sales Order stock, execute the following steps described in the Business Process Documentation Test Script of the scope item Make-to-Order Production - Finished Goods Sales and Final Assembly (BJE).

Use materials from this scope item for Make-to-Order production:

| Master Data | Sample Value |
| --- | --- |
| Material | AVC_RBT_CNTRL_UNIT, AVC_RBT_ROBOT |
| Plant | 3310 |
| Area of Responsibility Production Supervisor | Plant 1 AE 3310 MTO VC -Valuated (YB3) |

Before Execute scope item BJE, you need to manually create below manufacturing master data:

| Master Data | Reference Master Data Script | Reference Input Parameter Value |
| --- | --- | --- |
| Material-Working Schedule View | 2T7-Create Product Master of Type "Configurable Material" - MDS(Step: Create Product Master Data – Work Scheduling) | Material: AVC_RBT_CNTRL_UNIT, AVC_RBT_ROBOTProd. Sched. Profile: YB0003 |
| Routing | BNL-Create Routing - MDS | Material: AVC_RBT_CNTRL_UNITPlant: 3310Choose Copy From Routing: 41010031Overall Status: 4Note down the group number start with 5*Repeat the same for material AVC_RBT_ROBOT |
| Production Version | BLD-Create Production Version - MDS | Material: AVC_RBT_CNTRL_UNIT, AVC_RBT_ROBOTVersion: 0001Minimum Lot Size: 1Maximum Lot Size: 99,999,999Task List Type: RoutingGroup: <Group number noted down for each material in previous step>Group Counter: 1Alternative BOM: 1BOM Usage: 3 |

Follow below steps in scope item BJE to complete make-to-order production:

| Test Procedure No. of BJE | Test Procedure |
| --- | --- |
| 4.4.1 | Material Requirements Planning for Sales Order |
| 4.6.1 | Create Production Order (CO01) |
| 4.6.2 | Release Production Orders (CO05N) |
| 4.6.3 | Pick Components (Picking List) |
| 4.6.4 | Confirm Assembly Activities |
| 4.6.5 | Posting Goods Receipt for Production Order |

#### Delivery and Billing Processing (Optional)

Purpose

This process step shows you how to deliver material to the customer and handle the billing, the detail steps please find in test script BD9.

Procedure

Please execute the following steps using the master data from this document (see also the following table).

| Master Data | Sample Value |
| --- | --- |
| Material | AVC_RBT_BUNDLE |
| Plant | 3310 |

| Test Procedure No. of BD9 | Test Procedure |
| --- | --- |
| 4.9 | Create Delivery |
| 4.12 | Execute Picking |
| 4.17 | Post Goods Issue |
| 4.22 | Create Billing Document |

### Relevant Processes

If the following processes are enabled in your system, you can also test these business processes for the configurable material described in this test script.

| Process |
| --- |
| BD9 - Sell from Stock |
| BDD - Lean Customer Returns |
| BDG - Sales Quotation |
| BDH - Sales Order Entry with One-Time Customer |
| BDQ - Invoice Correction Process with Debit Memo |
| BDW - Returnables Processing |
| BKL - Invoice Correction Process with Credit Memo |
| BKZ - Sales Order Processing with Invoice List and Collective Billing |
| BKX - Sales Order Processing – SEPA Direct Debit Handling |
| BKP - Customer Returns |
| 1F1 - Debit Memo Processing |
| 1EZ - Credit Memo Processing |
| 1B6 - Sales Rebate Processing |
| 1MC - Omnichannel Convergent Billing |
| 1Z1 - Digital Payments – Sales |

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
- related-to :: [[08-sales-order-management/customer-returns-for-sales-kits-5cx-ae-test-script-sap-s-4hana-cloud-p]]
- related-to :: [[08-sales-order-management/test-script-sales-order-processing-for-sales-kits-31q-ae-896]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4OC_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 21,664 chars in the whole document
