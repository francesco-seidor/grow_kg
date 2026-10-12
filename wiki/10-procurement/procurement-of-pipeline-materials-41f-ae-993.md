---
id: 10-procurement/procurement-of-pipeline-materials-41f-ae-993
title: Procurement of Pipeline Materials (41F_AE) (41F_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud 2608 test script for scope item 41F_AE: pipeline info record, consumption posting and pipeline settlement or scheduled supplier invoice jobs."
cluster: 10-procurement
tags: [kb/procurement, topic/pipeline-procurement]
aliases: [41F_S4CLD2608_BPD_EN_AE]
keywords: [Procurement of Pipeline Materials, pipeline materials, purchasing info records, record consumption, pipeline settlement, supplier invoice jobs, goods issue, business roles, demo data update behavior, 41F]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/41F_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-993
topic: 10-procurement/pipeline-procurement
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Procurement of Pipeline Materials (41F_AE) (41F_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/41F_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Procurement of Pipeline Materials** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Procurement of Pipeline Materials (41F_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232854218)

[2 Prerequisites 3](#_Toc232854219)

[2.1 System Access 3](#_Toc232854220)

[2.2 Roles 3](#_Toc232854221)

[2.3 Master Data, Organizational Data, and Other Data 3](#_Toc232854222)

[3 Overview Table 5](#_Toc232854223)

[4 Test Procedures 6](#_Toc232854224)

[4.1 Create Purchasing Info Record 6](#_Toc232854225)

[4.2 Record Consumption 7](#_Toc232854226)

[4.3 Invoice Receipt from Pipeline Withdrawal 9](#_Toc232854227)

[4.3.1 Option 1: Create Pipeline Settlement 9](#_Toc232854228)

[4.3.2 Option 2: Schedule Supplier Invoice Jobs 10](#_Toc232854229)

## Purpose

Overview

The pipeline process begins with the creation of a pipeline info record and is followed by the posting goods issue from the pipeline. The process is closed with the settling of pipeline liabilities.

A pipeline material is a material that flows directly into the production process from a pipeline (for example, oil), from a pipe (for example, tap water), or from another similar source (for example, electricity).

A material from the pipeline is always available; that is, it can be withdrawn from the pipeline at any time and in any quantity.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all prerequisites to conducting the test in terms of systems, users, master data, organizational data, and other test data and business conditions.

### System Access

| System | Details |
| --- | --- |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log on |
| --- | --- | --- | --- | --- |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANTSAP_BR_AP_ACCOUNTANT_PROCUREMT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure:

| Master data | Value | Master. data details | Comments |
| --- | --- | --- | --- |
| Material | PIP01 | Pipeline Material 01 |  |
| Supplier | 33300003 | INLANDSLIEFERANT DE 3 |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Standard storage 1 |  |
| Company Code | 3310 | Company Code 3310 |  |
| Purchase Organization | 3310 | Purch. Org. 3310 |  |
| Purchasing group | 001 | Group 001 |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Purchasing Info Record](#unique_7) [page ] 6 | Purchaser | Create Purchasing Info Record (ME11) | Purchase Info Record is created successfully. |
| [Record Consumption](#unique_8) [page ] 7 | Warehouse Clerk | Post Goods Movement (MIGO) | Goods Movement is posted successfully. |
| Invoice Receipt from Pipeline Withdrawal |  |  |  |
| [Option 1: Create Pipeline Settlement](#unique_9) [page ] 9 | Accounts Payable Accountant | Create Logistics Consignment and Pipeline Settlement (MRKON) | Pipeline Settlement is created successfully. |
| [Option 2: Schedule Supplier Invoice Jobs](#unique_10) [page ] 10 | Accounts Payable Accountant | Schedule Supplier Invoice Jobs - Advanced (F1683) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Purchasing Info Record

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To run through this test script, the info records for the necessary materials must be available as master data. If the Info Record has not been maintained in the system yet, create the required master data.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Purchaser . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Purchasing Info Records (F1982). | The Manage Purchasing Info Records screen is displayed. |  |
| 3 | Open New Purchasing Info Record | Choose Create. | The Purchasing Info Record Screen is displayed. |  |
| 4 | Enter Header Data | Make the following entries:Purchasing Info Record Category: PipelinePurchasing Organization: 3310Supplier: 33300003Material: PIP01Plant: 3310Purchasing Group: 001 | Header data is added. |  |
| 5 | Enter General Information | Make the following entries:Available From: TodayAvailable To: 12/31/9999 | General Information is added. |  |
| 6 | Enter Delivery and Quantity Data | Make the following entries:Delivery Time in Days: 2Tax Code: <Input Tax Code>Order Unit: LStandard Order Quantity: 1 | Delivery and Quantity Data is added. |  |
| 7 | Enter Condition Data | In the Condition section, choose Create.In the General Information area, make the following entries:Valid From: TodayValid To: 12/31/9999Amount: <Net Price>Pricing Unit: 1Currency: AEDChoose Apply. | Condition Data is added |  |
| 8 | Enter Reference Data (optional) | You can enter reference data. | Reference data is added. |  |
| 9 | Save your data | Choose Create. | The purchasing info record is saved. |  |

### Record Consumption

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step you create an opportunity without a preceding document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO).It only displays this way if it was your last transaction. So, the action for the user should be: selectReference Document for MIGO Goods Issue > Other. |  |  |
| 3 | Enter Movement Type | Make the following entry and choose Enter.Executable Action in Transaction MIGO: Goods IssueReference Document for MIGO Transaction: Other | The Goods Issue Other screen displays. |  |
| 4 | Edit Material | On the Goods Issue Other Screen: Material tab, make the following entry, and choose Enter:Material: PIP01 |  |  |
| 5 | Enter Quantity Data | On the Goods Issue Other Screen: Quantity tab, make the following entry, and choose Enter:Qty in Unit of Entry: 100Unit of Entry: L |  |  |
| 6 | Enter data on the Goods Issue Other Screen: Where Tab | On the Goods Issue Other Screen: Where tab. Use the helper to make the following entries:Movement Type: 201P (Consumption for cost center from pipeline)Make the following entries and choose Enter:Plant: 3310If the vendor is not changed to 33300003, please go to Goods Issue Other Screen: Partner and fill in 33300003 manually. |  |  |
| 7 | Enter Account Assignment Data | Click on Account Assignment. On the Goods Issue Other Screen: Account Assignment tab. Make the following entries:G/L account: 51100000Cost Center: 33101301 |  |  |
| 8 | Save Your Entries | Choose Post. | Material document posted with document number. Make a note of the Material Document number. |  |

### Invoice Receipt from Pipeline Withdrawal

#### Option 1: Create Pipeline Settlement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step you settle the pipeline withdrawal with invoice receipt.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Choose Create Logistics Consignment and Pipeline Settlement (MRKON) . | The Logistics Consignment and Pipeline Settlement screen is displayed. |  |
| 3 | Enter Data | Make the following entries and choose Execute:Company Code: 3310Supplier: 33300003Plant: 3310Material: PIP01Material Document: <Enter the Material Document number generated in previous step>Pipeline: SelectedSettle: Selected |  |  |
| 4 | Create Settlement | Choose Run. | The record of material document displays with Information Text: Settled and the Document Number. |  |
| 5 | View settlement Document | On the Logistic Consignment and Pipeline Settlement screen, you can see the invoice document number under column Doc. No.. |  |  |

#### Option 2: Schedule Supplier Invoice Jobs

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Scheduling supplier invoice jobs is especially effective if you create settlement documents periodically.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Schedule Supplier Invoice Jobs - Advanced (F1683). | The Application Jobs screen is displayed. |  |
| 3 | Create Application Job | Choose Create. | The New Job screen is displayed. |  |
| 4 | Execute Consignment settlement | Make the following entries:In the Template Selection section, from the drop-down box of Job Template, choose Logistic Consignment and Pipeline Settlement, then choose Step 2In the Scheduling Options section, make sure that Start Immediately checkbox is checked. Or you can also set the start date and start time, then choose Step 3In the Parameter Section section, make the following entries:Company Code: for example, 3310Supplier: 33300003Plant: 3310Material: PIP01Material Document: Enter the material document number created from the last step.Consignment: DeselectedPipeline: SelectedDisplay: SelectedTax Date: <Today>Note The Tax Date is the key date for calculating tax, please maintain it carefully according to your financial business requirements. Withdrawals Not Settled: SelectedChoose Check. | The system message displays: You can go ahead and schedule the job. |  |
| 5 | Schedule the job without Test Run | Select Settle and then choose Schedule. |  |  |
| 6 | Check the result | In the Application Jobs screen, find the job you created. You may need to wait several minutes and refresh to see the results after the job status becomes finished.Choose Results. | The detailed log is displayed in the Document (ID, XXXXX) screen. You can find the corresponding Document number and FI Document number created. |  |

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
> Flagged while digesting this document, not verified: Record Consumption purpose text says 'create an opportunity without a preceding document', which does not match the goods issue steps.

## Connections
- part-of :: [[_cluster]]
- see-also :: [[10-procurement/einkaufsinfosatz-anlegen-sds-bhd-stammdatenskript-562]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/41F_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 17,762 chars in the whole document
