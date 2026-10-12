---
id: 08-sales-order-management/external-billing-1z6-ae-test-script-792
title: External Billing (1Z6_AE) Test Script (1Z6_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 1Z6_AE: checking billing documents created via the external billing interface (AE)."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/external-billing]
aliases: [1Z6_S4CLD2608_BPD_EN_AE]
keywords: [External Billing Interface, external billing, billing documents, invoice cancellation, message monitoring, automatic account determination, electronic payments, condition records, business roles, test scripts]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1Z6_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-792
topic: 08-sales-order-management/external-billing
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# External Billing (1Z6_AE) Test Script (1Z6_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1Z6_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **External Billing Interface** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | External Billing (1Z6_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232848586)

[2 Prerequisites 3](#_Toc232848587)

[2.1 System Access 3](#_Toc232848588)

[2.2 Roles 3](#_Toc232848589)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232848590)

[2.4 Preliminary Steps 5](#_Toc232848591)

[2.4.1 Display the Billing Documents 5](#_Toc232848592)

[2.4.2 Assign G/L Account for Electronic Payment Service Provider Direct Capture Process (Optional) 6](#_Toc232848593)

[2.4.3 Create Condition Records (Optional) 8](#_Toc232848594)

[3 Overview Table 10](#_Toc232848595)

[4 Test Procedures 11](#_Toc232848596)

[4.1 Check Invoice Ext. Transaction Billing Document Created in the SAP System 11](#_Toc232848597)

[4.2 Check Invoice Cancellation Billing Document Created in the SAP System 13](#_Toc232848598)

[4.3 Monitor External Billing Document Created in the SAP System (Optional) 14](#_Toc232848599)

[5 Appendix 16](#_Toc232848600)

[5.1 Process Integration 16](#_Toc232848601)

[5.2 Succeeding Processes 16](#_Toc232848602)

## Purpose

Overview

This scope item enables the use of the external billing interface to create billing documents, without predecessor documents in SD calling from an external system (SAP or non-SAP).

The scope item encompasses the necessary customizing to run business application programming interfaces (BAPIs) for exchanging billing data between your SAP or non-SAP on-premise system and your SAP S/4HANA Cloud Public Edition system.

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
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Configuration Expert - Business Network Integration | SAP_BR_CONF_EXPERT_BUS_NET_INT | Business Network Integration / Business Network Integration - Concur Integration / Business Network Integration - Output Control / Business Network Integration - Data Replication / Configuration Expert - Business Network Integration Cross Applications | SAP_CORE_SPT_INT_PC / SAP_CON_SPT_CONCUR_INT_PC / SAP_OC_SPT_INT_PC / SAP_CA_SPT_DATA_REP_PC / SAP_CA_SPT_BUS_NETWORK_INT_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Customer | 33100001 |  |  |
| Material | TG10 | Material generalNo serial number, no batch. | See sections Preliminary Steps. |
| Material | TG0011 | Material generalNo serial number, no batch. | See sections Preliminary Steps. |
| Material | TG11 | Material generalNo serial number, no batch. | See sections Preliminary Steps. |
| Plant | 3310 |  |  |
| Storage Location | 331A |  |  |
| Sales organization | 3310 |  |  |
| Distribution channel | 10 |  |  |
| Division | 00 |  |  |

For more information on creating these master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) Scripts (MDS):

Table 1: Master Data Script Reference

| Master Data Script ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BND | Create Customer Master - MDS |

### Preliminary Steps

#### Display the Billing Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The default setting for an employee should be maintained by the Administrator mandatorily. Plant and Company code needs to be presented a primary information in the user defaults screen.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Billing Documents (F0797).Enter search term(s) in the filter bar. |  |  |
| 3 | Display billing document | Choose and display the billing document. |  |  |

#### Assign G/L Account for Electronic Payment Service Provider Direct Capture Process (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The process step shows you how to assign G/L account as below before process execution if you need to process direct capture.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note To create country-/region-dependent settings for the intended local version, , choose Set Local Version. | The Configure Your Solution screen displays. |  |
| 4 | Open Another App | Choose Automatic Account Determination in the following area: Finance > General Ledger > Charts of Accounts. | The Configure Your Solution - Chart of Accounts screen displays. |  |
| 5 | Go to Configuration Details | Choose Configure on the right to Automatic Account Determination configuration step. | The Automatic Account Determination 1 Area screen displays. |  |
| 6 | Fill in Basic Information | Make the following entries:Area: <Sales>Subarea: <Sales Billing>Process: <Assign G/L Accounts>Choose Step 2. | The Automatic Account Determination 2 Parameters screen displays. |  |
| 7 | Fill in Relevant Information | Make the following entries:Chart of Accounts: <YCOA>Application: <VD>Condition Table: <006>Sales Org. Table: 3310Choose Step 3. | The Automatic Account Determination 3 Account Assignments screen displays. |  |
| 8 | Maintain G/L Account Assignment | Choose Add and scroll down to the bottom.Make the following entries:Condtion Type：<A001 (Standard)>Company Code: 3310Card Type: <DP1P>G/L Account: 12530100Accruals Acc.: <Keep it Blank>Choose Review. | The Automatic Account Determination screen displays with relevant information. |  |
| 9 | Review in the Information and Save | Choose Save, and then choose Save again for confirmation. | The G/L account assignment is saved. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Automatic Account Determination | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Automatic Account Determination.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Automatic Account Determination 1 Area screen displays. |  |
| 3 | Fill in Basic Information | Make the following entries:Area: <Sales>Subarea: <Sales Billing>Process: <Assign G/L Accounts>Choose Step 2. | The Automatic Account Determination 2 Parameters screen displays. |  |
| 4 | Fill in Relevant Information | Make the following entries:Chart of Accounts: <YCOA>Application: <VD>Condition Table: <006>Sales Org. Table: 3310Choose Step 3. | The Automatic Account Determination 3 Account Assignments screen displays. |  |
| 5 | Maintain G/L Account Assignment | Choose Add and scroll down to the bottom.Make the following entries:Condtion Type：<A001 (Standard)>Company Code: 3310Card Type: <DP1P>G/L Account: 12530100Accruals Acc.: <Keep it Blank>Choose Review. | The Automatic Account Determination screen displays with relevant information. |  |
| 6 | Review in the Information and Save | Choose Save, and then choose Save again for confirmation. | The G/L account assignment is saved. |  |

#### Create Condition Records (Optional)

Purpose

In case you have finetuned the access sequence of SAP pre-shipped condition types, the relative condition records should be created accordingly.

You can find general information on how to create your own master data in the following: [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 2: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BEW | Create Free Goods Condition - MDS |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Check Invoice Ext. Transaction Billing Document Created in the SAP System](#unique_10) [page ] 11 | Billing Clerk | Manage Billing Documents (F0797) | The billing document shows. |
| [Check Invoice Cancellation Billing Document Created in the SAP System](#unique_11) [page ] 13 | Billing Clerk | Manage Billing Documents (F0797) | The billing document shows. |
| [Monitor External Billing Document Created in the SAP System (Optional)](#unique_12) [page ] 14 | Configuration Expert - Business Network Integration | Assign Recipients to Users (F2949) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Check Invoice Ext. Transaction Billing Document Created in the SAP System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check the billing document created from the external system.

Prerequisite

You may need to contact your system administrator to check whether the billing document is created correctly in the SAP system via the interface.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Billing Documents (F0797).Enter search term(s) in the filter bar.For example, choose Billing Type: Invoice Ext. Transaction (CIX1) or Pro Forma for Ext. Transaction (CIX5). | The screen shows the related billing documents. |  |
| 3 | Navigate to the Billing Document | Tap on billing document number, then choose Display Billing Documents. | The Display Billing Document XXX: Overview screen displays. |  |
| 4 | Check the Payment Card. (Optional) | Note This step is required if the SAP S/4HANA has been integrated with SAP digit payment system.On the Display Billing Document xxx: Overview screen, choose More > Goto > Header > Electronic Payments. | The Payment Card information displays.Credit Card details are stored:Card typeCard token (not be displayed)Mask numberCard holderValid-to |  |
| 5 | Check Authorization (Optional) | Note This step is required if the SAP S/4HANA has been integrated with SAP digit payment system and the payment method with card type "DP2P" has been used.On the Display Billing Document xxx:Overview screen, choose More > Goto > Header > Electronic Payment.Double-click the authorized line for more detail. | Below details are stored:● Card type: "DP2P"● Auth. Number● Auth. Date● Authorized Amt● Payment Serv. Provid● Transaction ID |  |
| 6 | Check Direct Capture (Optional) | Note This step is required if the SAP S/4HANA has been integrated with SAP digit payment system and the payment method with card type "DP1P" has been used.On the Display Billing Document xxx: Overview screen, choose More > Goto > Header > Electronic Payment.Double-click the authorized line for more detail. | Below details are stored:● Card type: "DP1P"● Authorized Amt● Payment Serv. Provid● Payment ID |  |
| 7 | Check Output Condition | On the Invoice XXX Display: Overview of Billing Items screen, choose More > Goto > Header > Output. | The Invoice XXX Display: Output screen displays. |  |
| 8 | Display Print Preview | On the Invoice XXX Display: Output screen, select the line already created for the print output.Choose Display PDF Document. | Print preview displays. |  |
| 9 | Navigate to the Billing Document | Close the preview and choose Back. | The Display Billing Document XXX: Overview screen displays. |  |
| 10 | Check Accounting Document | Choose Accounting.Double-click the accounting document. | The screen shows the accounting document. |  |

### Check Invoice Cancellation Billing Document Created in the SAP System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check the Cancel billing document created from the external system.

Prerequisite

You may need to contact your system administrator to check whether the billing document is created correctly in the SAP system via the interface.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Billing Documents (F0797).Enter search term(s) in the filter bar.For example, choose Billing Type: Invoice Cancellation (CICX). | The screen shows the related billing documents. |  |
| 3 | Navigate to the Billing Document | Input billing document number XXX which is created by external transaction through the interface in external system.Choose Display Billing Document. | The Invoice XXX Display: Overview screen displays. |  |
| 4 | Check the Payment Card (Optional) | This step is required if SAP S/4HANA has been integrated with SAP digit payment system.On the Display Billing Document xxx: Overview screen, choose More > Goto > Header > Electronic Payment. | The Payment Card information displays.Credit Card details are stored:Card typeCard token (not be displayed)Mask numberCard holderValid-to |  |
| 5 | Check Output Condition | On the Invoice XXX Display: Overview of Billing Items screen, choose More > Goto > Header > Output. | The Invoice XXX Display: Output screen displays. |  |
| 6 | Display Print Preview | On the Invoice XXX Display: Output screen, select the line already created for the print output.Choose Display Document. | Print preview displays. |  |
| 7 | Navigate to the Billing Document | Close the preview and choose Back button. | The Display Billing Document XXX: Overview screen displays. |  |
| 8 | Check Accounting Document | Choose Accounting.Double-click the accounting document. | The screen shows the accounting document. |  |

### Monitor External Billing Document Created in the SAP System (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to monitor status for the external billing document created from the external system.

Prerequisite

You may need to contact your system administrator to check whether the billing document is created correctly in the SAP system via the interface.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Network Integration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Choose Assign Recipients to Users (F2949).Enter CONF_EXPERT_BUS_NET_INT in the filter bar, then choose it from list. | Recipients for User displays |  |
| 3 | Assign Recipient | Choose Assign.Namespace: /SDBILRecipient Name: SDBIL_BD_R_IN_RECIPENTChoose Assign. | The Invoice XXX Display: Overview screen displays. |  |
| 4 | Check document status | Navigate to home page, then choose Message Monitoring Overview.External Billing document creation status can be seen under sector /SDBIL/BD_R_IN. | External Billing document creation status displays |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

Attachments of external billing documents can be mass maintained with service API API_CV_ATTACHMENT.

### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| Accounts Receivable (J59) | Posting a Customer Invoice in Accounting, etc.Using the master data from this document, complete the following activities described in the test script:Posting a Customer Invoice in AccountingOverdue Receivables, Display Customer BalancesManage Customer Line Items |
| Sales Order Fulfillment Monitoring and Operations (BKK) (optional) | This test script describes the collection of periodic activities, such as day’s ending activities.Using the master data from this document, complete all the activities described in the Business Process Documentation of the scope item:Sales Order Fulfillment Monitoring and Operations (BKK) (sections Review Sales Documents Blocked for Billing, Review Billing Due List, Review Log of Collective Invoice Creation and Review List of Blocked (for accounting) Billing Documents) |

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
- related-to :: [[08-sales-order-management/test-script-omnichannel-convergent-billing-1mc-ae-sap-s-4hana-cloud-pu]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1Z6_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 25,500 chars in the whole document
