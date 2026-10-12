---
id: 03-financial-accounting-and-close/test-script-monitoring-of-goods-and-invoice-receipts-2v7-ae-876
title: "Test Script: Monitoring of Goods and Invoice Receipts (2V7_AE) (2V7_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 2V7: reconciling, monitoring and analyzing GR/IR accounts, with optional notification setup via situation handling."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/gr-ir-monitoring]
aliases: [2V7_S4CLD2608_BPD_EN_AE]
keywords: [GR/IR Account Monitoring and Reconciliation, gr/ir reconciliation, gr/ir monitoring, situation handling, gr/ir process insights, test scripts, business roles, sample master data, business conditions, machine learning prediction]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2V7_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-876
topic: 03-financial-accounting-and-close/gr-ir-monitoring
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Monitoring of Goods and Invoice Receipts (2V7_AE) (2V7_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2V7_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **GR/IR Account Monitoring and Reconciliation** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Monitoring of Goods and Invoice Receipts (2V7_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232850769)

[2 Prerequisites 3](#_Toc232850770)

[2.1 System Access 3](#_Toc232850771)

[2.2 Roles 3](#_Toc232850772)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232850773)

[2.4 Business Conditions 5](#_Toc232850774)

[3 Overview Table 6](#_Toc232850775)

[4 Test Procedures 7](#_Toc232850776)

[4.1 Reconcile GR/IR Accounts 7](#_Toc232850777)

[4.2 Monitor GR/IR Account Reconciliation 8](#_Toc232850778)

[4.3 Monitor Notifications (Optional) 10](#_Toc232850779)

[4.4 Analyze GR/IR Process 13](#_Toc232850780)

## Purpose

Overview

The GR/IR monitor is an application in SAP S/4HANA Cloud Public Edition that helps the accountants to process the cases where the goods receipts and the invoices receipts are not exactly matched and written off automatically. The processors set the statuses to purchase orders to indicate the next actions that must be taken in the context of certain purchase order. A machine learning feature of the GR/IR application makes a prediction of the next status based on the history of processing. The predictions are provided by a Machine Learning (ML) service that runs on the Cloud Foundry. This communication scenario is related to the connection of the SAP S/4HANA Cloud Public Edition system and the ML service.

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
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Management / Business Process Management | SAP_BR_BUSINESS_PROCESS_SPEC / SAP_CA_SPT_BPS_PC |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Master Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 |  |  |
| Chart of Accounts | YCOA |  |  |
| Controlling Area | A000 |  |  |
| Cost Center | 33101001 |  |  |

You can find general information on how to create master data objects in the following Master Data Scripts (MDS):

| MDS | Description |
| --- | --- |
| BND | Create Customer Master - MDS |
| BNM | Create Cost Center and Cost Center Group - MDS |
| BNG | Create G/L Account and Cost Element - MDS |
| BNH | Create Profit Center - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| J60 - Accounts Payable | Execute all steps in this test script. |
| 31N - Situation Handling | Must be in scope to use situation handling. |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Reconcile GR/IR Accounts](#unique_8) [page ] 7 | General Ledger Accountant | Reconcile GR/IR Accounts (F3302) | You reconciled the accounts. |
| [Monitor GR/IR Account Reconciliation](#unique_9) [page ] 8 | General Ledger Accountant | Monitor GR/IR Account Reconciliation - Overview (F3303) | You monitored the reconciliation. |
| [Monitor Notifications (Optional)](#unique_10) [page ] 10 | General Ledger Accountant |  | You monitored notifications. |
| [Analyze GR/IR Process](#unique_11) [page ] 13 | General Ledger Accountant | GR/IR Process Insights (F5796) | You viewed a graphical overivew of the GR/IR process. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Reconcile GR/IR Accounts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you clarify the unreconciled GR/IR accounts.

Using this app, you can get a detailed analysis of the purchasing document in a tabular format. The displayed details are:

- An overview tab that shows the quantity of good received and the invoiced quantity as well as the cash equivalents
- A financial accounting open item tab that shows the GR and invoice documents
- A purchase order history tab
- A contacts tab that shows detailed information about the buying agent and supplier
- A notes tab that shows document details

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access App | Open Reconcile GR/IR Accounts (F3302). | The Intelligent Goods and Invoice Receipt Account Reconciliation view is displayed. |  |
| 3 | Maintain Selection | Make the following entries and press Enter:Company Code: 3310 | The invoice and GR open items for the company code are displayed. |  |
| 4 | Select Purchasing Document for Analysis | Select the purchasing document to analyze and choose the Details button. | The details of the purchasing document display. |  |
| 5 | Request Change in Purchasing Document | After you analyze the purchasing document's data, you can request a change.Choose Process Item. |  |  |
| 6 | Request Change in Purchasing Document | Make the following entries and choose Save:Processing Step (Status): for example, Request Completion of DeliveryPriority: for example, HighProcessing Department: for example, Team 01Processor: <choose a processor from the list> (the list shows up when you start typing in the field)Root Cause: for example, Incomplete goods receiptNote: <message to the processor> | The purchasing document is sent for further analysis or change. |  |

### Monitor GR/IR Account Reconciliation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The app provides an analytical overview of goods and invoice receipt reconciliation on the company code level.

The analysis is based on two types of KPIs:

- Open FI items
- Purchase order items

The KPIs contained in the open FI items are:

- Open FI items by company code
- Open FI items by posting date
- Open FI items by Supplier
- Open FI items by dimension

The KPIs contained in the purchase order items are:

- Purchase order items GR surplus
- Purchase order items IR surplus
- Purchase order items GR equals IR
- Purchase order items Process information

Both open FI items and purchase order items KPIs can be displayed by one of the following:

- Controlling area
- Company code
- Profit Center
- Supplier
- Plant
- Purchasing Organization
- Material Group

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access App | Open Monitor GR/IR Account Reconciliation - Overview (F3303). | The Goods and Invoice Receipt Reconciliation Overview view is displayed. |  |
| 3 | Maintain Selection | In the Filter bar, make the following entries and press Enter:Company Code: 3310 | The KPIs for the open FI items and purchase order items are displayed. |  |

### Monitor Notifications (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

|  |
| --- |
| Note Situation Handling must be in scope to perform this step. |

Prerequisite - Manage Teams and Responsibilities

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on on to the SAP Fiori launchpad as Configuration Expert - Business Process Configuration |  |  |
| 2 | Access App | Open Manage Teams and Responsibilities (F2412) . |  |  |
| 3 | Create Team | Choose Create. | The New Team screen displays. |  |
| 4 | Maintain General Information | On the Team Information tab, make the following entries:General InformationName: ZGRIR_TEAMStatus: EnabledType: FIGRIR |  |  |
| 5 | Define Responsibility | On the Responsibility Definitions tab, make the following entries:Company Code: 3310 |  |  |
| 6 | Add Team Members | On the Team Members tab, choose Create.Make the following entries and choose OK:User ID: for example, General Ledger Accountant |  |  |
| 7 | Create | Choose Create. | The team is saved. |  |

Prerequisite - Manage Situation Types

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on on to the SAP Fiori launchpad as Business Process Specialist |  |  |
| 2 | Access App | Open Manage Situation Types (F2947) . | The Manage Situation Types screen displays. |  |
| 3 | Select the Template | Choose Go.Select Template FIN_GRIRPROCESSORCHANGED and choose Copy. | The Situation Type screen displays. |  |
| 4 | Maintain the Situation | Make the following entries:Admin Information section:ID: ZGRIR_TESTName: for example, GR/IR Clearing Processor Is Changed |  |  |
| 5 | Add Responsibility Rule | On the Recipients tab, choose Add Rule for Responsibility Rules .Select Get GR/IR Clearing Processor and choose OK. |  |  |
| 6 | Save Situation Type | Choose Save. | The Enable Situation Type dialog box is displays. |  |
| 7 | Enable Situation Type | Choose Yes. | The situation type is enabled. |  |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on on to the SAP Fiori launchpad as Business Process Specialist |  |  |
| 2 | Access App | Open Manage Situation Types (F2947) . | The Manage Situation Types screen displays. |  |
| 3 | Select the Template | Choose Go.Select Template FIN_GRIRDEVIATIONEXCEEDSTRHSHLD and choose Copy. | The Situation Type screen displays. |  |
| 4 | Maintain the Situation | Make the following entries:Admin Information section:ID: ZGRIR_THRESHOLDName: for example, GR/IR Deviation Exceeds Threshold |  |  |
| 5 | Add Conditions | On the Conditions tab, make the following entries:Send Notification: selectedCompany Code: 3310Balance Amount: for example, <=1000000 |  |  |
| 6 | Schedule Batch Job | On the Batch Job Scheduling tab, make the following entries:Time Zone: for example, UTCStart Batch Job At: for example, 20:00 |  |  |
| 7 | Manage Notifications | On the Situation Display tab, make the following entries:NotificationAggregate Notifications: selectedResend Notifications: deselected |  |  |
| 8 | Manage Notification Recipients | On the Recipients tab, make the following entries:Responsibility by TeamsTeam Category: GR/IR Account ReconciliationMember Function: GR/IR Account Reconciliation |  |  |
| 9 | Save Situation Type | Choose Save. | The Enable Situation Type dialog box is displays. |  |
| 10 | Enable Situation Type | Choose Yes. | The situation type is enabled. |  |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Select Notification | On the top-right of the Home screen, choose Notifications.Choose a notification that says you have been assigned as Processor for a GR/IR Account Reconciliation purchasing document item. | The Intelligent Goods and Invoice Receipt Account Reconciliation screen displays. |  |
| 3 | Select Notification | On the top-right of the Home screen, choose Notifications.Choose a notification that says there is a deviation on a GR/IR account for a purchasing document item which exceeds the threshold. | The Intelligent Goods and Invoice Receipt Account Reconciliation screen displays. |  |

### Analyze GR/IR Process

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can gain insights into the GR/IR (goods receipt/invoice receipt) account reconciliation process. You can:

- Analyze the completed GR/IR account reconciliation processing in detail
- Filter data by organizational units such as company code, supplier, plant, material group, purchasing organization and more
- View process transitions
- View process insights for a processing step (status), processing department, processor, priority and root cause

Prerequisite

You reconciled your GR/IR (Goods Receipt/Invoice Receipt) accounts.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access App | Open GR/IR Process Insights (F5796). | The GR/IR Process Insights view is displayed. |  |
| 3 | Maintain Selection | In the Filter bar, make the following entries and choose Go:Company Code: 3310Supplier: <supplier>Note If the Supplier field is not visible, choose Adapt Filters to display it. If you want to view insights on a different field, choose that field instead. | The process insights for the selected company code and supplier are displayed. |  |
| 4 | Change Insights | In the area below the filter bar, you can change the value in the Process Insights for dropdown to view different insights. You can also use the buttons to the right of the view to change between chart and table views. |  |  |

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
- related-to :: [[03-financial-accounting-and-close/test-script-machine-learning-for-monitoring-of-goods-and-invoice-recei]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2V7_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 21,190 chars in the whole document
