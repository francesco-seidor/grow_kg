---
id: 04-tax-and-statutory-reporting/test-script-enablement-of-sap-excise-tax-management-4lo-1033
title: "Test Script: Enablement of SAP Excise Tax Management (4LO) (4LO_S4CLD2608_BPD_EN_XX)"
description: "Test script for scope item 4LO: testing S/4HANA Cloud APIs integrating with SAP Excise Tax Management (BTP): org data, master data, material documents."
cluster: 04-tax-and-statutory-reporting
tags: [kb/tax-and-statutory-reporting, topic/excise-tax-vistex]
aliases: [4LO_S4CLD2608_BPD_EN_XX]
keywords: [SAP Excise Tax Management by Vistex, excise tax management, excise tax integration, organizational data replication, master data replication, material document replication, warehouse assignments, business roles, odata api services, test scripts]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4LO_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1033
topic: 04-tax-and-statutory-reporting/excise-tax-vistex
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Enablement of SAP Excise Tax Management (4LO) (4LO_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4LO_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **SAP Excise Tax Management by Vistex** in Tax and Statutory Reporting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Enablement of SAP Excise Tax Management (4LO) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232836667)

[2 Prerequisites 3](#_Toc232836668)

[2.1 System Access 3](#_Toc232836669)

[2.2 Roles 3](#_Toc232836670)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232836671)

[2.4 Additional Manual Configuration 5](#_Toc232836672)

[2.5 Business Conditions 5](#_Toc232836673)

[2.6 Preliminary Steps 5](#_Toc232836674)

[2.6.1 Prerequisite 5](#_Toc232836675)

[3 Test Procedures 6](#_Toc232836676)

[3.1 Replication of Organizational Data 6](#_Toc232836677)

[3.2 Replication of Master Data 7](#_Toc232836678)

[3.3 Replication of Material Documents 9](#_Toc232836679)

## Purpose

Overview

The integration scenario described here deals with available APIs from SAP S/4HANA Cloud Public Edition for integration with the SAP Excise Tax Management. The APIs are in the areas of Master Data (business partners, materials, organizational data), Materials Management (Material Documents), Logistics Execution (Delivery for Excise Movement and Control System (EMCS)), Sales (pricing in Sales Order and Billing), and Financials (posting of excise taxes to Accounting).

Country- and customer-specific details aren't covered and must be implemented on an individual basis to meet both legal and customer requirements.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

|  |  |
| --- | --- |
|  | Details |
| SAP Business Technology Platform | Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

Customer has to create a role for the 4LO integration or enhance an already existing role by the content described below:

| Object Type | TADIR Service |
| --- | --- |
| IWSG SAP Gateway: Service Group Metadata | ZAPI_BUSINESS_PARTNER_0001 |
| ZAPI_STORAGELOCATION_SRV_0001 |  |
| ZAPI_PRODUCT_SRV_0001 |  |
| ZAPI_EXCISETAXPLANT_SRV_0001 |  |
| ZAPI_EXCISETAXMATDOCITM_SRV_0001 |  |
| ZAPI_COMPANYCODE_SRV_0001 |  |
| ZAPI_EXCISETAXACCDOCPOST_SRV_0001 |  |
| ZAPI_GLACCOUNTINCHARTOFACCOUNTS_SRV |  |
| ZAPI_ET_UNITOFMEASURE_SRV_0001 |  |
| IWSV SAP Gateway Business Suite Enablement | API_BUSINESS_PARTNER 0001 |
| API_STORAGELOCATION_SRV 0001 |  |
| API_PRODUCT_SRV 0001 |  |
| API_EXCISETAXPLANT_SRV 0001 |  |
| API_EXCISETAXMATDOCITM_SRV 0001 |  |
| API_COMPANYCODE_SRV 0001 |  |
| API_EXCISETAXACCDOCPOST_SRV 0001 |  |
| API_GLACCOUNTINCHARTOFACCOUNTS_SRV |  |
| API_ET_UNITOFMEASURE_SRV 0001 |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | all available company codes |  |  |
| Storage Location | all available storage location |  |  |
| Material Master | all available |  |  |
| Business Partner | all available |  |  |
| Material Document | All available |  |  |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/75c791f92ce74fad7ef0174c9b962bd2)

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| J45 - Procurement of Direct Materials | There must be material master records available meeting the excise tax condition (e.g. alcohol, tobacco). The relevance for the excise tax will be defined in the SAP Business Technology Platform Excise Tax app.Material documents for the related material master records (e.g. purchase order, sales order). |

### Preliminary Steps

#### Prerequisite

Use

Create material master record.

Procedure

Copy an existing material master record in the SAP S/4HANA Cloud Public Edition system to a new material master record (all views etc.) and rename it to, for example, Alcohol, unit of measure: Liter.

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Replication of Organizational Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The configuration of the Excise Tax solution on SAP Business Technology Platform requires access to a minimal set of organizational data. On SAP Business Technology Platform-Excise Tax side, the integration is realized via value helps synchronously integrated to the connected SAP S/4HANA Cloud Public Edition tenant. By value picking, in some use cases, organizational data are directly transferred from the value help result list into SAP Business Technology Platform-Excise Tax instances. The SAP S/4HANA Cloud Public Edition Excise Tax Integration Layer, delivered with the integration scenario for Excise Tax Integration (SAP_COM_0568) provides the means to synchronously access Company Codes, Plants and Storage Locations.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 2 | Log On | Log on to the SAP Business Technology Platform Excise Tax tenant. You need to have the role of Configuration Expert or Tax Responsible assigned to your user . . | The Fiori launch pad should be loaded and various apps should be seen. |  |
| 3 | Check Company Codes | Use the Synchronize Data and View Changes. Choose the value helps for Company Code and Plant in the filter area and choose Go on the subsequent dialog boxes. | A list of the company codes and plants available in the SAP S/4HANA Cloud Public Edition system is displayed:Company Code: e.g. 1010, 1710 etc.Plant: e.g. 1010, 1710 etc. |  |
| 4 | Check Storage Locations | For the test of the Storage Location integration, use the Warehouse Assignments app. Choose the value help for Storage Location in the filter area and choose Go on the subsequent dialog boxes. | As a result, you see all storage locations with its description and with its assignment to a plant, which are maintained in the connected SAP S/4HANA Cloud Public Edition client.Storage Location: <any> |  |
| 5 | Create New Warehouse Assignment | To create a new warehouse assignment (in your test system), use the Warehouse Assignments app. Choose Create and select individual values from the Plant and Storage Location value helps. In addition, select a Tax Type and a corresponding Warehouse ID and enter a Plant Warehouse Number. Save the new warehouse assignment. | Check the created Warehouse.Verify its existence and correct assignment to the plant and storage location via the search functionality on the initial screen of the Warehouse Assignment app. |  |

### Replication of Master Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Running the SAP Business Technology Platform Excise Tax solution in terms of configuration, evaluations and data processing requires the synchronization of some master data with the connected SAP S/4HANA Cloud Public Edition client. In particular, the replication of business partners (in their roles as vendors and customers/ship-to parties) and materials, which are excise tax relevant, are of importance.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 2 | Log On | Log on to the SAP Business Technology Platform Excise Tax tenant. You need to have the role of Tax Responsible assigned to your user. . | The Fiori launchpad should be loaded and various apps should be seen. |  |
| 3 | Replication of Master Data | Open the Synchronize Data and View Changes app and choose Synchronize Master Data’ on the Master Data Synchronization tab. | This triggers the master data replication from the SAP S/4HANA Cloud Public Edition client to the SAP Business Technology Platform Excise Tax tenant. In order to see the result of the replication, choose Go on the same screen in the filter area and check the status for the replication of the different master data objects. To further check the integration, change a field in a master data instance and the trigger the replication. The result of the master data replication can be seen, for example, in apps such as Material Master or Business Partner Master Data.This triggers the master data replication from the SAP S/4HANA Cloud Private Edition client to the SAP Business Techhnology Platform Excise Tax tenant.. The following objects are replicated with the attributes as mentioned.* Vendor Data – BP Number, Name, City, Street* Customer Data - – BP Number, Name, City, Street* Company Code - Description* Storage Location - Description* Plant - Description* Unit of Measure for Material – Additional Unit ofMeasures for Material Master* Material Description – Description* PRODCOM – Prodcom NumberIf there are changed which are replicated, you can navigate in the logs to check them. |  |
| 4 | Replication of Material Documents | Start the document selection in the Execute Document Selection app.Caution Pay special attention to the number of documents that are due for selection in the header of this app. After fetching the documents from the SAP S/4HANA Cloud Public Edition client, the documents are valuated asynchronously. | As a result, in the processing overview, the number of documents is monitored that are fetched from the SAP S/4HANA Cloud Public Edition client in a certain time frame, as well as their classification is taken over to stock ledger, rejected, disregarded, or still in process. In the Display Stock Ledger app, you can view all material documents that are considered to be excise tax relevant. |  |

### Replication of Material Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The material documents are the basis for the excise tax calculation. Therefore, its replication from the SAP S/4HANA Cloud Public Edition client to the SAP Business Technology Platform Excise Tax solution plays a central role in the integration between both systems. In the course of the material document replication, all sorts of material movements are replicated to SAP Business Technology Platform Excise Tax. Depending on its movement type, the documents are sorted in SAP Business Technology Platform Excise Tax and evaluated regarding its relevance for excise tax, depending on the SAP Business Technology Platform Excise Tax configuration. The central process step is the calculation of the excise tax amount for each movement, which in turn is the basis for the excise tax declaration to the legal authorities.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 2 | Log On | Log on to the SAP Business Technology Platform Excise Tax tenant as an Administrator. |  |  |
| 3 | Replication of Material Documents | Start the document selection in the Execute Document Selection app.Caution Pay special attention to the number of documents that are due for selection in the header of this app. After fetching the documents from the SAP S/4HANA Cloud Public Edition client, the documents are valuated asynchronously. | As a result, in the processing overview, the number of documents is monitored that are fetched from the SAP S/4HANA Cloud Public Edition client in a certain time frame, as well as their classification is taken over to stock ledger, rejected, disregarded, or still in process. In the Display Stock Ledger app, you can view all material documents that are considered to be excise tax relevant. |  |

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
- related-to :: [[04-tax-and-statutory-reporting/test-script-enablement-of-sap-excise-tax-management-by-vistex-7z8-ae-s]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4LO_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 17,104 chars in the whole document
