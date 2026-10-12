---
id: 12-production-and-manufacturing/test-script-third-party-shop-floor-execution-process-industry-3w3-979
title: Test Script - Third-Party Shop Floor Execution – Process Industry (3W3) (3W3_S4CLD2608_BPD_EN_XX)
description: "SAP S/4HANA Cloud Public Edition test script for scope item 3W3: integrating a third-party MES with process orders, from order creation to goods receipt and scrap review."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/mes-and-shop-floor-integration]
aliases: [3W3_S4CLD2608_BPD_EN_XX]
keywords: [Manufacturing Execution System and Third-Party Shop Floor…, mes integration, process orders, goods issue, production confirmation, goods receipt, order progress monitoring, scrap reporting, business roles, business conditions]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3W3_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-979
topic: 12-production-and-manufacturing/mes-and-shop-floor-integration
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script - Third-Party Shop Floor Execution – Process Industry (3W3) (3W3_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3W3_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Manufacturing Execution System and Third-Party Shop Floor Integration** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Third-Party Shop Floor Execution – Process Industry (3W3) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232844421)

[2 Prerequisites 3](#_Toc232844422)

[2.1 System Access 3](#_Toc232844423)

[2.2 Roles 3](#_Toc232844424)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232844425)

[2.4 Additional Manual Configuration 4](#_Toc232844426)

[2.5 Business Conditions 4](#_Toc232844427)

[3 Overview Table 6](#_Toc232844428)

[4 Test Procedures 7](#_Toc232844429)

[4.1 Process Order Processing 7](#_Toc232844430)

[4.1.1 Create Process Order 7](#_Toc232844431)

[4.1.2 Manual Goods Issue of Batch-Managed Components 8](#_Toc232844432)

[4.1.3 Monitor Order Progress 9](#_Toc232844433)

[4.1.4 Confirm Production in a Third-Party System 10](#_Toc232844434)

[4.1.5 Post Goods Receipt for Finished Good 11](#_Toc232844435)

[4.1.6 Review Process Order Confirmation 12](#_Toc232844436)

[4.1.7 Review Scrap Report 13](#_Toc232844437)

[5 Appendix 14](#_Toc232844438)

[5.1 Succeeding Processes 14](#_Toc232844439)

## Purpose

Overview

This scope item covers the setup of the integration from SAP S/4HANA Cloud Public Edition to Manufacturing Execution Systems (MES).

An MES integrates business and manufacturing processes that help to run efficient, high-quality production on the shop floor.

This scope item provides an example of integrating a local customer shop floor system directly into SAP S/4HANA Cloud Public Edition, giving manufacturing staff a clear overview of production operations and improving analytical capability for the management team. SAP S/4HANA Cloud Public Edition is the system of record for all master data. An MES or a shop floor system is the system of record for all work-in-progress data.

This communication scenario provides end points (inbound and outbound) that can be used to integrate an on-premise third-party MES to production operation for process orders through OData calls and SOAP messages.

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
| Production Planner | SAP_BR_PRODN_PLNR | Production Planning | SAP_BR_PRODN_PLNR |  |
| Production Supervisor - Process Manufacturing | SAP_BR_PRODN_SUPERVISOR_PROC | Production Management - Process Manufacturing | SAP_BR_PRODN_SUPERVISOR_PROC |  |
| Production Operator - Process Manufacturing | SAP_BR_PRODN_OPTR_PROC | Production Execution - Process Manufacturing | SAP_BR_PRODN_OPTR_PROC |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Production Engineer - Process Manufacturing | SAP_BR_PRODN_ENG_PROC | Production Engineering - Process Manufacturing | SAP_BR_PRODN_ENG_PROC |  |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

Use your own master data or the following sample data to go through the test procedure.

The sample master data are reused from Make-to-Stock – Process Manufacturing Based on Process Order (BJ8) scope item from US version (plant 1710) as an example. Please adopt according to your plant.

For more information about creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNR | Create Product Master of type "Raw Material" - MDS |
| BNS | Create Product Master of type "Semi-Finished Good" - MDS |
| BNT | Create Product Master of type "Finished Good" - MDS |
| BNJ | Create Production Work Center - MDS |
| BNK | Create Material BOM for Production and Sales - MDS |
| BNL | Create Routing - MDS |
| BLD | Create Production Version - MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/a486faf5536fbca73ea9678c15ca0bf9)

### Business Conditions

As this scope item is an API whitelisting scope item, master data and organizational data that are named in this test script are only examples (in this case from scope item BJ8).

To run this test, you have to activate at least one scope item, where process orders are used.

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| BEG - Standard Cost Calculation | Must be run before this test script. |
| BNZ - Create New Open MM Posting Period - MDS | Must be run before this test script. Posting Period is up to date. |
| BJ8 - Make-to-Stock – Process Manufacturing Based on Process Order | If you have activated scope item BJ8, demo data can be reused for this test script. |
| 3UK - Inbound Storage Tank Management – Process Manufacturing | If you have activated scope item 3UK, adopt master data accordingly for this test script. |
| 42N - Tank Trailer Filling with Residuals | If you have activated scope item 42N, adopt master data accordingly for this test script. |
| 3OK - Make-to-Order Production – Process Manufacturing | If you have activated scope item 3OK, adopt master data accordingly for this test script. |
| 3L7 - Make-to-Stock with Co- and By-Products – Process Manufacturing | If you have activated scope item 3L7, adopt master data accordingly for this test script. |
| 3UL - Make-to-Stock with Silo Material – Process Manufacturing | If you have activated scope item 3UL, adopt master data accordingly for this test script. |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Process Order](#unique_9) [page ] 7 | Production Supervisor - Process Manufacturing | Create Process Order (COR1) |  |
| [Manual Goods Issue of Batch-Managed Components](#unique_10) [page ] 8 | Warehouse Clerk | Post Goods Movement (MIGO) |  |
| [Monitor Order Progress](#unique_11) [page ] 9 | Production Supervisor - Process Manufacturing | Monitor Order Progress (CO46) |  |
| [Confirm Production in a Third-Party System](#unique_12) [page ] 10 |  |  |  |
| [Post Goods Receipt for Finished Good](#unique_13) [page ] 11 | Warehouse Clerk | Post Goods Movement (MIGO) |  |
| [Review Process Order Confirmation](#unique_14) [page ] 12 | Production Supervisor - Process Manufacturing | Display Process Order Confirmation (CORT) |  |
| [Review Scrap Report](#unique_15) [page ] 13 | Production Supervisor - Process Manufacturing | Material Scrap - Maximum Deviation (F2035) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Process Order Processing

|  |
| --- |
| Note In this test script, the production process has to be executed at first for the semifinished material (SG24) and afterwards for the finished product (FG29). |

#### Create Process Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create process orders. Because the order release is executed automatically, production can start immediately.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Process Order (COR1). | The Create Process Order: Initial Screen displays. |  |
| 3 | Enter Restriction | Make the following entries and choose Continue:Material Number: SG24 and FG29Production Plant: for example, 1710Process Order Type: YBM2 | The system displays the Create Process Order: Header - General Data screen where you enter your data for creation of process order.Note Create first process orders for the semi-finished material (SG24) and proceed the entire Succeeding Processes section. Then repeat these steps for the finished good (FG29). |  |
| 4 | Create Process Order | Make the following entries and choose Save:Total Qty: <your amount of products to produce>Start: <your start date>Choose Operation:Control Key: YPI1 | Process orders are created and automatically released for semi-finished material (SG24) or finished product (FG29).The control key in every operation is changed to anonther milestone control key (e.g. YPI1) to enable distribution of the order.Note the process order numbers. |  |

#### Manual Goods Issue of Batch-Managed Components

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The withdrawal of the raw materials is used for the process order. This withdrawal can be done by using the picking list or doing a manual goods issue. This process step shows you how to perform a goods issue.

|  |
| --- |
| Note If the material is set for backflush (in material master or resource), the withdrawing is done automatically after you confirm the operation or the whole order. Backflushing should not be used for batch-managed components (to ensure that the physically picked and consumed batch is the same as the recorded batch). |

Prerequisites

Ensure that sufficient material is available on stock. You can check the stock levels using the Monitor Stock/Requirements List app that is available for the Production Planner role.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Initial screen displays. |  |
| 3 | Enter Process Order Number | Make the following entries and press Enter:Trans./Event: Goods IssueReference Document: OrderOrder Number: <XXXX> (from previous steps)Movement Type: 261 | The screen name adapts after entries are made. |  |
| 4 | Check each Item | Select Item OK for each item. | Ensure that the detail screen displays. |  |
| 5 | Perform Batch Determination | Choose Stock Determ. for All. | The Batch Determination MM: Select Batches screen displays. |  |
| 6 | Copy Batch Determination Result | Check the required batch and choose Copy.Repeat this step for all the materials selected. | The Goods Issue Order XXXX screen displays.In addition, the batch numbers are determined. |  |
| 7 | Post Goods Movements | Choose Post. | The goods movements are posted. |  |

#### Monitor Order Progress

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to see progress for process orders, components and operations, starting with the Stock/Requirements List.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Order Progress (CO46). | The Order Progress Report: Selection screen displays. |  |
| 3 | Enter Overall Profile | Make the following entry and choose the Production/Process Order tab:Overall Profile: SAP000000002 |  |  |
| 4 | Enter Process Order Number | Make the following entry and choose Execute:Production/Process Order: <XXXX> (from previous steps)Note You can review the order with its operations and components by double clicking on the order number and choose Display Element. In the Display Process Order: Header - General Data screen, choose Operations or Material List to see the related data. | Th Stock/Requirements List as of XX hrs screen displays. |  |

#### Confirm Production in a Third-Party System

Purpose

The confirmation documents in SAP S/4HANA Cloud Public Edition include the processing status of order, operations, phases and individual capacities. It is an instrument to monitor the order. The time ticket confirmation allows recording of either the default times for machine and labour usage, or actual times for major deviations. Backflushed materials will be posted automatically when confirming the respective phase when backflush for components are set.

This process step shows you how to confirm production. You may post scrap quantities optionally. If there are not any major deviations occurred, then only the last phase must be confirmed.

The confirmations have to be done in the respective Manufacturing Execution System (MES) and are distributed to SAP S/4HANA Cloud Public Edition.

Procedure

Confirm the operations in the connected MES and make sure to distribute them to SAP S/4HANA Cloud Public Edition.

#### Post Goods Receipt for Finished Good

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to post the goods receipt for the process order. You may post goods receipt for the total quantity, but usually already partial quantities of the products are required for further processing, such as consumption for further production or subsequent deliveries for sales orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Initial screen displays. |  |
| 3 | Enter Process Order Number | Make the following entries and press Enter:Trans./Event: Goods ReceiptReference Document: OrderOrder Number: <XXXX> (From previous steps)Movement Type: <101> | Screen name adapts after entries are made. |  |
| 4 | Enter Date of Manufacture | Choose Batch tab and make the following entry:Date of Manufacture: <Current Date>Note This step is only available for SAP-delivered standard content as some customizing changes in SSCUI could make things different. |  |  |
| 5 | Check Item | Select item OK. | Ensure that the detail screen displays. |  |
| 6 | Post Goods Movement | Choose Post. | The goods movements are posted.The batch number is created automatically while posting.Production date and shelf life expiration date are recorded within the batch master of the finished goods. |  |

#### Review Process Order Confirmation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step describes how to review confirmations for process orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Process Order Confirmation (CORT). | The Display Process Order Confirmation: Initial screen displays. |  |
| 3 | Enter Process Order Number | Make the following entry and choose Enter:Process Order: <process order number from previous steps>Double click on a quantity to see details of this confirmation. | The Display Process Order Confirmation: Operation/Phase Overview screen displays.Confirmations are reviewed and checked within your responsibility area. |  |

#### Review Scrap Report

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to review the scrap report.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Material Scrap - Maximum Deviation (F2035). |  |  |
| 3 | Investigate Scrap | Materials Scrap may be displayed by various filters.You could choose the corresponding material in Chart to display the details. |  |  |

## Appendix

### Succeeding Processes

After completing the activities in this test script, you may continue testing the following business process:

| Scope Item | Business Condition |
| --- | --- |
| BEI - Period-End Closing – Plant | These are executed collectively as a part of month-end closing. For more information on the month-end closing procedure, see BEI test script.Note that month-end closing can only be executed once a month. |

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
- related-to :: [[12-production-and-manufacturing/test-script-production-operations-with-manufacturing-execution-system]]
- related-to :: [[12-production-and-manufacturing/test-script-third-party-shop-floor-execution-discrete-industry-3w4-980]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3W3_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 23,483 chars in the whole document
