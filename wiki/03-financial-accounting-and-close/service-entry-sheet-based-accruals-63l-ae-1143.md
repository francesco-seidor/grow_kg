---
id: 03-financial-accounting-and-close/service-entry-sheet-based-accruals-63l-ae-1143
title: Service Entry Sheet Based Accruals (63L_AE) (63L_S4CLD2608_BPD_EN_AE)
description: "Test script for scope item 63L_AE: configuring, proposing, posting and simulating accruals from service entry sheets in SAP S/4HANA Cloud Public Edition 2608."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/service-entry-sheet-accruals]
aliases: [63L_S4CLD2608_BPD_EN_AE]
keywords: [Service Entry Sheet Based Accruals, service entry sheet accruals, periodic accruals, accrual simulation, accrual engine, accrual configuration, service purchase orders, accrual review, business roles, master data]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/63L_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1143
topic: 03-financial-accounting-and-close/service-entry-sheet-accruals
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Service Entry Sheet Based Accruals (63L_AE) (63L_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/63L_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Service Entry Sheet Based Accruals** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Service Entry Sheet Based Accruals (63L_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232858006)

[2 Prerequisites 4](#_Toc232858007)

[2.1 System Access 4](#_Toc232858008)

[2.2 Roles 4](#_Toc232858009)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232858010)

[2.4 Business Conditions 5](#_Toc232858011)

[2.5 Preliminary Steps 6](#_Toc232858012)

[2.5.1 Adjust Transfer Priorities for Accruals 6](#_Toc232858013)

[2.5.2 Define Accrual Item Types and Methods for Purchase Orders of Service 7](#_Toc232858014)

[3 Overview Table 10](#_Toc232858015)

[4 Test Procedures 11](#_Toc232858016)

[4.1 Service Entry Sheet Accruals 11](#_Toc232858017)

[4.1.1 Transfer Purchase Orders (Optional) 11](#_Toc232858018)

[4.1.2 Propose Periodic Accruals (Optional) 12](#_Toc232858019)

[4.1.3 Review Service Entry Sheet Accruals for Cost Accountant (Optional) 13](#_Toc232858020)

[4.1.4 Post Periodic Accruals 14](#_Toc232858021)

[4.1.5 Display Service Entry Sheet Accruals 15](#_Toc232858022)

[4.2 Simulate Service Entry Sheet Accruals 16](#_Toc232858023)

[4.2.1 Simulate Posting Run 16](#_Toc232858024)

[4.2.2 Display Simulated Accrual Postings 17](#_Toc232858025)

[4.2.3 Compare Simulated and Actual Accrual Postings 18](#_Toc232858026)

## Purpose

Overview

This scope item lets you calculate and post accruals based on service entry sheets submitted against lean service purchase orders. You can replicate the lean service purchase orders as accrual objects based on service entry sheets submitted, but not yet approved, to propose the accrual amount. You can then review the accrual amount and generate periodic accrual journal postings and reverse the documents in the next period.

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
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT |  |
| Cost Accountant - Overhead | SAP_BR_OVERHEAD_ACCOUNTANT | Overhead Accounting | SAP_BR_OVERHEAD_ACCOUNTANT |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 |  |  |
| Chart of Accounts | YCOA |  |  |
| Controlling Area | A000 |  |  |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

| MDS | Description |
| --- | --- |
| BNM | Create Cost Center and Cost Center Group |
| BNG | Create G/L Account and Cost Element |
| BNH | Create Profit Center |

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 22Z - Procurement of Services or22K - External Workforce Procurement via SAP Fieldglass | Create a purchase order with an unapproved service entry sheet. |

### Preliminary Steps

#### Adjust Transfer Priorities for Accruals

Purpose

In this activity, you assign transfer priorities to accrual engine components.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). |  |  |
| 3 | Access Configuration | Open Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Access Configuration | Make the following entries:Application Area: FinanceSub Application Area: General Ledger |  |  |
| 5 | Open | Open Service Entry Sheet Accruals. |  |  |
| 6 | Select Configuration Step | For the Adjust Transfer Priorities for Accruals step, choose Configure. | The Change View "Variants for purchase order data transfer": Overview screen displays. |  |
| 7 | Assign Priority To Component | Make the following entries and choose Save:Comp onent: SSACTransfer Priority Order: 1 1st Priority | The priority is assigned to component SSAC. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access Configuration | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Adjust Transfer Priorities for Accruals.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Adjust Transfer Priorities for Accruals screen is displayed. |  |
| 3 | Assign Priority To Component | Make the following entries and choose Save:Comp onent: SSACTransfer Priority Order: 1 1st Priority | The priority is assigned to component SSAC. |  |

#### Define Accrual Item Types and Methods for Purchase Orders of Service

Purpose

In this activity, you assign company codes to purchase order transfer variants.

|  |
| --- |
| Note You can make a transfer variant the standard variant for all company codes by setting the Default Variant for Transfer indicator in the Variants for PO related Data Transfer view. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). |  |  |
| 3 | Access Configuration | Open Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Access Configuration | Make the following entries:Application Area: FinanceSub Application Area: General Ledger |  |  |
| 5 | Open | Open Service Entry Sheet Accruals |  |  |
| 6 | Select Configuration Step | For the Define Accrual Item Types and Methods for Purchase Orders of Service step, choose Configure. | The Change View "Variants for PO related Data Transfer": Overview screen displays. |  |
| 7 | Access Configuration | Double-click Assign company code to transfer variant to access the view. | The Change View "Assign company code to transfer variant": Overview screen displays. |  |
| 8 | Assign Company Code To Transfer Variant | Choose New Entries.Make the following entries and choose Save:Company Code: 3310Transfer Variant: SSES | The company code is assigned to transfer variant SSES. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access Configuration | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Accrual Item Types and Methods for Purchase Orders of Service.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Accrual Item Types and Methods for Purchase Orders of Service screen is displayed. |  |
| 3 | Access Configuration | Double-click Assign company code to transfer variant. | The Change View "Assign company code to transfer variant": Overview screen displays. |  |
| 4 | Assign Company Code To Transfer Variant | Choose New Entries.Make the following entries and choose Save:Company Code: 3310Transfer Variant: SSES | The company code is assigned to transfer variant SSES. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Table 1: Service Entry Sheet Accruals

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Transfer Purchase Orders (Optional)](#unique_11) [page ] 11 | General Ledger Accountant | Schedule Accruals Jobs (F3778) | The job is executed and the purchase orders are transferred to the accrual engine. |
| [Propose Periodic Accruals (Optional)](#unique_12) [page ] 12 | General Ledger Accountant | Schedule Accruals Jobs (F3778) | The job is executed and the purchase order accruals are scheduled. |
| [Review Service Entry Sheet Accruals for Cost Accountant (Optional)](#unique_13) [page ] 13 | Cost Accountant - Overhead | Review Service Entry Sheet Accruals - For Cost Accountant (F6108) | The proposed accrual amounts are displayed. |
| [Post Periodic Accruals](#unique_14) [page ] 14 | General Ledger Accountant | Schedule Accruals Jobs (F3778) | The job is executed and the accrued purchase orders are posted. |
| [Display Service Entry Sheet Accruals](#unique_15) [page ] 15 | General Ledger Accountant | Display Service Entry Sheet Accruals (F6107) | The service entry sheet for an accrual object is displayed. |

Table 2: Simulate Service Entry Sheet Accruals

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Simulate Posting Run](#unique_16) [page ] 16 | General Ledger Accountant | Schedule Accruals Jobs (F3778) | The job is executed and the postings are simulated. |
| [Display Simulated Accrual Postings](#unique_17) [page ] 17 | General Ledger Accountant | Accrual Postings - With Simulation (W0183) | The simulated postings of purchase order accrual objects are displayed. |
| [Compare Simulated and Actual Accrual Postings](#unique_18) [page ] 18 | General Ledger Accountant | Accrual Postings - Simulated / Posted (W0184) | A comparison of simulated and actual postings of purchase order accrual objects is displayed. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Service Entry Sheet Accruals

#### Transfer Purchase Orders (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

In this activity, you manually transfer purchase orders to the accrual engine.

|  |
| --- |
| Note This step is not mandatory. Purchase orders are automatically transferred by default. However, if you uncheck Online Integ. Active within the SSCUI Define Accrual Item Types and Methods for Purchase Orders of Service, you will have to perform this step manually. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access App | Open Schedule Accruals Jobs (F3778). | The Application Jobs screen displays. |  |
| 3 | Create Job | Choose Create. | The New Job screen displays. |  |
| 4 | Enter Data | Make the following entries and choose Schedule:Template Selection section:Job Template: Service Entry Sheet Accruals – Transfer Purchase Orders to Accrual EngineJob Name: Service Entry Sheet Accruals – Transfer Purchase Orders to Accrual EngineChoose Step 2.Scheduling Options:Start Immediately: SelectedChoose Step 3.Parameters:Company Code: 3310Purchasing Document: <Purchasing Document>Item: <Optional>Document Date: <Optional> | The job is created and started immediately. |  |

#### Propose Periodic Accruals (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

In this activity, you schedule service entry sheet accruals.

|  |
| --- |
| Note This step is optional if you don’t use the Review Service Entry Sheet Accruals - For Cost Accountant (F6108) app to review the proposed accruals. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access App | Open Schedule Accruals Jobs (F3778). | The Application Jobs screen displays. |  |
| 3 | Make Selection | Choose Create. | The New Job screen displays. |  |
| 4 | View Details | Make the following entries and choose Schedule:Template Selection section:Job Template: Service Entry Sheet Accruals – Propose Periodic AccrualsJob Name: Service Entry Sheet Accruals – Propose Periodic AccrualsChoose Step 2.Scheduling Options:Start Immediately: SelectedChoose Step 3.Parameters:Last Day of Period: <Date>Company Code: 3310Ledger Group: <Optional>Accrual Object: <Purchase Order>Accrual Subobject: <Optional>Accrual Item Type: <Optional> | The job is created and started immediately. |  |

#### Review Service Entry Sheet Accruals for Cost Accountant (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To follow a four-eyes principle, managers in accounting need an overview of all critical tasks and milestones during financial close. These should allow for steps to be taken to ensure quality and timeliness, and to be reviewed and approved. Each task and milestone subject to approval must be shown with all result objects and all relevant attributes. This ensures that overall period closing or year-end closing is done in time, ready for legal reporting, and with completeness and correctness of books.

|  |
| --- |
| Note This app currently only displays data.If you proposed accrual amounts, you can view the proposed amounts with this app. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. |  |  |
| 2 | Access App | Open Review Service Entry Sheet Accruals - For Cost Accountant (F6108). |  |  |
| 3 | Display Serivce Entry Sheet Accruals | Make the following entries and choose Go:Last Day of Period: for example, <Last Day of Current Month>Company Code: 3310Purchase Order: <Purchase Order> | The proposed accrual amounts are displayed. |  |

#### Post Periodic Accruals

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

In this activity, you post the accrued purchase orders.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access App | Open Schedule Accruals Jobs (F3778). | The Application Jobs screen displays. |  |
| 3 | Create Job | Choose Create. | The New Job screen displays. |  |
| 4 | Enter Data | Make the following entries and choose Schedule:Template Selection section:Job Template: Service Entry Sheet Accruals – Post Periodic AccrualsJob Name: Service Entry Sheet Accruals – Post Periodic AccrualsChoose Step 2.Scheduling Options:Start Immediately: SelectedChoose Step 3.Parameters:Last Day of Period: <Date>Company Code: 3310Ledger Group: <Optional>Accrual Object: <Optional>Accrual Subobject: <Optional>Accrual Item Type: <Optional>Note You can select Rev. on First Day of Next Perd if you want the reversal of periodic accrual posting to take place on the first day of the next period. If you leave this check box empty, the system posts the accrual reversal on the last day of the next period. | The job is created and started immediately. |  |

#### Display Service Entry Sheet Accruals

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

In this activity, you view service entry sheet accruals.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access App | Open Display Service Entry Sheet Accruals (F6107). | The Display Service Entry Sheet Accruals screen displays. |  |
| 3 | Make Selection | Make the following entries and choose Go:Company Code: 3310Purchase Order: <Purchase Order> | The service entry sheet accrual objects display. |  |
| 4 | View Details | Choose a service entry sheet accrual object (>). | The details of the selected accrual object are displayed. |  |

### Simulate Service Entry Sheet Accruals

#### Simulate Posting Run

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you simulate the posting of purchase order accrual objects.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Accruals Jobs (F3778). | The Application Jobs screen displays. |  |
| 3 | Create a New Job | Choose Create. | The New Job screen displays. |  |
| 4 | Enter Data | Make the following entries and choose Schedule:Template Selection section:Job Template: Service Entry Sheet Accruals - Simulate Accrual PostingsJob Name: Service Entry Sheet Accruals - Simulate Accrual PostingsChoose Step 2.Scheduling Options section:Start Immediately: SelectedChoose Step 3.Parameters:Company Code: 3310Accrual Object: <accrual object> | The job is created and started immediately. |  |

#### Display Simulated Accrual Postings

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you view simulated postings of purchase order accrual objects.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Accrual Postings - With Simulation (W0183). | The Accrual Postings With Simulation - Query screen displays. |  |
| 3 | Enter Data | Make the following entries and choose Go:Valid to Date: for example, <last day of lifecycle>Company Code: 3310Fiscal Year: for example, <current year>Fiscal Period: for example, <current period>Component: for example, SSACAccrual Object: <accrual object> | The reports displays the data specified by your query.Note Once accruals are posted for an accrual object, only the actual posted accrual amount will be displayed. |  |

#### Compare Simulated and Actual Accrual Postings

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you view and compare simulated postings with actual postings of purchase order accrual objects.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Accrual Postings - Simulated / Posted (W0184). | The Simulated Posted Compare - Query screen displays. |  |
| 3 | Enter Data | Make the following entries and choose Go:Valid to Date: for example, <last day of lifecycle>Company Code: 3310Fiscal Year: for example, <current year>Fiscal Period: for example, <current period>Component: for example, SSACAccrual Object: <accrual object> | The reports displays the data specified by your query for comparison. |  |

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
- related-to :: [[03-financial-accounting-and-close/test-script-purchase-order-accruals-2vb-ae-sap-s-4hana-cloud-public-ed]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/63L_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 28,649 chars in the whole document
