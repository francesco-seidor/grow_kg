---
id: 09-subscription-billing-and-contract-accounting/convergent-invoicing-recurring-and-one-off-items-2t3-ae-test-script-86
title: Convergent Invoicing – Recurring and One-Off Items (2T3_AE) Test Script (2T3_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition test script (2T3_AE) for Convergent Invoicing: billing plans, billable items, billing and invoicing runs."
cluster: 09-subscription-billing-and-contract-accounting
tags: [kb/subscription-billing-and-contract-accounting, topic/recurring-and-one-off-billing]
aliases: [2T3_S4CLD2608_BPD_EN_AE]
keywords: ["Convergent Invoicing: Recurring, One-Off and Usage…", convergent invoicing, billing plans, billing plan items, billing process, invoicing process, test scripts, business roles, prerequisites, billing documents]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2T3_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-861
topic: 09-subscription-billing-and-contract-accounting/recurring-and-one-off-billing
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Convergent Invoicing – Recurring and One-Off Items (2T3_AE) Test Script (2T3_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2T3_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Convergent Invoicing: Recurring, One-Off and Usage Billing, Invoice Correction** in Subscription Billing and Contract Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Convergent Invoicing – Recurring and One-Off Items (2T3_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232850307)

[2 Prerequisites 4](#_Toc232850308)

[2.1 System Access 4](#_Toc232850309)

[2.2 Roles 4](#_Toc232850310)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232850311)

[2.4 Business Conditions 5](#_Toc232850312)

[3 Overview Table 6](#_Toc232850313)

[4 Test Procedures 7](#_Toc232850314)

[4.1 Create Billing Plan 7](#_Toc232850315)

[4.2 Request Billing Plan Items 8](#_Toc232850316)

[4.2.1 Option 1: Request Billing Plan Items (Mass Run) 9](#_Toc232850317)

[4.2.2 Option 2: Request Billing Plan Items (Individual Run) 10](#_Toc232850318)

[4.3 Perform Billing Process 11](#_Toc232850319)

[4.3.1 Option 1: Perform Billing Process (Mass Run) 11](#_Toc232850320)

[4.3.2 Option 2: Perform Billing Process (Individual Run) 12](#_Toc232850321)

[4.4 Display Billing Document (Optional) 13](#_Toc232850322)

[4.5 Perform Invoicing Process 14](#_Toc232850323)

[4.5.1 Option 1: Perform Invoicing Process (Mass Run) 15](#_Toc232850324)

[4.5.2 Option 2: Perform Invoicing Process (Individual Run) 16](#_Toc232850325)

[4.6 Display Invoicing Document (Optional) 17](#_Toc232850326)

[5 Appendix 18](#_Toc232850327)

[5.1 Process Integration 18](#_Toc232850328)

[5.1.1 Preceding Processes 18](#_Toc232850329)

[5.1.2 Succeeding Processes 18](#_Toc232850330)

## Purpose

Overview

This process allows the creation of billing plans in convergent invoicing. Billing plans can be used to define recurring and one-time charges for a contract or contract account.

- Recurring charges as a monthly contract fee
- One time charge like a contract activation fee
- Monthly credit
- Down payment requests to build up an advance payment plan

For this reason, the billing plan is divided into 3 tabs: “plan items”, “billable items” (that have already been generated), and “reference items”.

The plan items contain the rules and information for creating billable items, for example:

- Amount payable
- Billing cycle
- Validity of payment
    - Start and end date
    - Unlimited validity

A periodic request run uses these rules and this information to generate billable items. These billable items can then be invoiced.

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
| Invoicing Specialist (Convergent Invoicing) | SAP_BR_INVOICING_SPEC_CINV | Convergent Invoicing / Subscription Billing | SAP_BR_INVOICING_SPECIALIST_CINV / SAP_CEC_SPT_SUBSCR_BILLG_SPCLST_PC |  |
| Administrator (Convergent Invoicing) | SAP_BR_INVOICING_ADMIN_CINV | Administration - Convergent Invoicing | SAP_BR_INVOICING_ADMIN_CINV |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 | Company Code 3310 |  |

You can find general information on how to create master data objects in the following Master Data Scripts (MDS):

Table 1: Master Data Script Reference

| Master Data Script ID | Description |
| --- | --- |
| 3GD | Create Service Type Based Pricing Condition - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| 2AR- Contract Accounting – Master Data and Basic Functions | Must be run before this test script. Business Partner and Contract Account must be created. |
| 2BG - Convergent Invoicing – Invoice Creation for Usage and Service | Must be deployed before running this test script. |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Billing Plan](#unique_8) [page ] 7 | Invoicing Specialist (Convergent Invoicing) | Manage Billing Plans (F2824) | Billing Plan is created |
| [Request Billing Plan Items](#unique_9) [page ] 8 |  |  |  |
| [Option 1: Request Billing Plan Items (Mass Run)](#unique_10) [page ] 9 | Administrator (Convergent Invoicing) | Request Billing Plan Items - Mass Run (F3530) | Billable item is created |
| [Option 2: Request Billing Plan Items (Individual Run)](#unique_11) [page ] 10 | Invoicing Specialist (Convergent Invoicing) | Request Billing Plan Items - Business Partner (FKKBIXBIP_S) | Billable item is created |
| [Perform Billing Process](#unique_12) [page ] 11 |  |  |  |
| [Option 1: Perform Billing Process (Mass Run)](#unique_13) [page ] 11 | Administrator (Convergent Invoicing) | Execute Billing - Mass Run (F3525) | Billing Document is created |
| [Option 2: Perform Billing Process (Individual Run)](#unique_14) [page ] 12 | Invoicing Specialist (Convergent Invoicing) | Execute Billing - Business Partner (FKKBIX_S) | Billing Document is created |
| [Display Billing Document (Optional)](#unique_15) [page ] 13 | Invoicing Specialist (Convergent Invoicing) | Manage Billing Documents (F2250) | Billing Document is displayed |
| [Perform Invoicing Process](#unique_16) [page ] 14 |  |  |  |
| [Option 1: Perform Invoicing Process (Mass Run)](#unique_17) [page ] 15 | Administrator (Convergent Invoicing) | Execute Invoicing - Mass Run (F3524) | Invoicing Document is created. |
| [Option 2: Perform Invoicing Process (Individual Run)](#unique_18) [page ] 16 | Invoicing Specialist (Convergent Invoicing) | Execute Invoicing - Business Partner (FKKINV_S) | Invoicing Document is created |
| [Display Invoicing Document (Optional)](#unique_19) [page ] 17 | Invoicing Specialist (Convergent Invoicing) | Manage Invoicing Documents (F2048) | Invoicing Document is displayed |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Billing Plan

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you will create Billing Plan. If you created Contract Provider with Billing Plan at 2AR Contract Accounting – Master Data and Basic Functions, you can skip this step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad as Invoicing Specialist (Convergent Invoicing). | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the App | Choose the Manage Billing Plans (F2824) tile. | The Manage Billing Plans page is displayed. |  |
| 3 | Create Billing Plan | In Manage Billing Plans screen, choose Create button. |  |  |
| 4 | Maintain Parameters | In Create Billing Plan screen, make the following entries as below:Billing Plan Type: <General Billing Plan>External Reference: <External Reference>Choose Next to close Create Billing Plan screen.Business Partner: : <business partner>Contract Account: <contract account> | The Billing Plan page is displayed.Note External Reference is optional. |  |
| 5 | Create Billing Plan Item | Choose Plan Items in the Billing Plan screen. You can create one off billing plan item or recurring billing plan item.To create a one-off billing plan item, choose Create and make the following entries below:Billing Plan Item Type: <billing plan item Type of one off>Amount: <amount>Currency: <currency>Valid From: <valid from>Valid To: <valid to>To create a recurring billing plan item, choose Create and make the following entries below:Billing Plan Item Type: <billing plan item Type of recurring>Amount: <amount>Currency: <currency>Valid From: <valid from>Valid To: <valid to>Billing Cycle: <billing cycle> | One billing plan item is created. Based on the demand, you can create more billing plan item. |  |
| 6 | Save Billing Plan | Choose Create. |  |  |
| 7 | Release Billing Plan | Choose Release | The billing plan is released. |  |

### Request Billing Plan Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you request billing plan items to create billable items. You can process it with mass run or individual run.

#### Option 1: Request Billing Plan Items (Mass Run)

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad as Administrator (Convergent Invoicing). | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the App | Choose the Request Billing Plan Items - Mass Run (F3530) tile. | The Application Jobs page is displayed. |  |
| 3 | Create Application Job | Choose Create to create a new application job. | The New Job page is displayed. |  |
| 4 | Select Template | Make the following entries as below:Job Template: Request Billing Plan ItemJob Name: <job name>Choose Step2. |  |  |
| 5 | Maintain Schedule Options | Make the following entries as below:Start Immediately: chooseRecurrence Pattern: Single RunChoose Step3. |  |  |
| 6 | Maintain Parameters | Make the following entries as below:Prefix of Run ID: <Prefix of Run ID>Business Partner: <The Business Partner>Contract Account: <The Required Contract Account>Simulation Run: <Don’t Choose>Request date: <The Request Date>Problem Class: <problem class> eg: Additional Information |  |  |
| 7 | Execute | Choose Schedule. | The job is running immediately. |  |
| 8 | Locate the job from application job list | In the Application Jobs screen, make the following entries as below:Date From-To:: <Today -1/+1 day>Choose Go. | The application job you want to find was located in the application jobs list. |  |
| 9 | Check Log | Choose Image of Log to access located the application job log. | The log of application job is displayed. From the log, you can see the result of application job. |  |

#### Option 2: Request Billing Plan Items (Individual Run)

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad as Invoicing Specialist (Convergent Invoicing). | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the App | Choose the Request Billing Plan Items - Business Partner (FKKBIXBIP_S) tile. | The Request Billing Plan Items (Individual Processing) page is displayed |  |
| 3 | Maintain Parameters | In the Request Billing Plan Items (Individual Processing), make the following entries as below:Request Data: <The Request Date>Business Partner: <The Business Partner>Contract Account: <The Contract Account> |  |  |
| 4 | Execute | Choose Execute.Choose Continue to close Request Run Ended screen. |  |  |

### Perform Billing Process

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you start up the billing process to create the billing document. You can process with mass run or individual creation.

|  |
| --- |
| Note If you enabled Clarification at 2BG-Convergent Invoicing: Invoicing creation for Usage and Service, please follow the Perform Billing Process of 2BG-Convergent Invoicing: Invoicing creation for Usage and Service to perform Billing.If the clarification case is created when perform billing, please follow the Clarify Clarification Case Relevant to Billing Document (Optional) of 2BG-Convergent Invoicing: Invoicing creation for Usage and Service to perform Billing |

#### Option 1: Perform Billing Process (Mass Run)

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad as Administrator (Convergent Invoicing). | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the App | Choose the Execute Billing - Mass Run (F3525) tile. | The Execute Billing - Mass Run page is displayed |  |
| 3 | Create Application Job | Choose Create button to create a new application job. | The New Job: Billing (Mass Creation) page is displayed. |  |
| 4 | Select Template | Make the following entries as below:Job Template; Billing (Mass Creation)Job Name; <job name>Choose Step2. |  |  |
| 5 | Maintain Schedule Options | Make the following entries as below:Start Immediately: chooseRecurrence Pattern: Single RunChoose Step 3. |  |  |
| 6 | Maintain Parameters | Make the following entries as below:Prefix of Run ID: <Prefix of Run ID>Billing Process: <Y001>Contract Account: <The Required Contract Account>Simulation Run: <Don’t Choose>Billing Date: <The Current Date>Problem Class: <problem class> |  |  |
| 7 | Execute | Choose Schedule. | The job is running immediately. |  |
| 8 | Locate the job from application job list | In the Execute Billing - Mass Run screen, make the following entries as below:Date From-To:: <Today -1/+1 day>Choose Go. | The application job you want to find was located in the application jobs list. |  |
| 9 | Check Log | Choose Image of Log to access located the application job log. | The log of application job is displayed. From the log, you can see the result of application job. |  |

#### Option 2: Perform Billing Process (Individual Run)

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad as Invoicing Specialist (Convergent Invoicing) | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the App | Choose Execute Billing - Business Partner (FKKBIX_S) tile. | The Billing (Individual Creation) page is displayed. |  |
| 3 | Maintain Parameters | In the Billing (Individual Creation), make the following entries as below:Billing Process: <Y001>Billing Date: <The Current Date>Contract Account: <The Required Contract Account> |  |  |
| 4 | Execute | Choose Execute. |  |  |
| 5 | Choose Billable Item and Create Billing Units | In the Choose Billable Items and Creation of Billing Units dialog, choose Save, until you see the dialog Billing Ended. | A dialog Billing Ended is displayed. |  |
| 6 | Check Billing Document | Choose Continue (Enter) to leave the dialog. |  |  |

### Display Billing Document (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can display the billing document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad as Invoicing Specialist (Convergent Invoicing). | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the App | Choose the Manage Billing Documents (F2250) tile. | The Manage Billing Documents page is displayed |  |
| 3 | Maintain Parameters | In the Manage Billing Documents screen, make the following entries as below:Billing Document: <The Billing Document You Want to Display> |  |  |
| 4 | Execute | Choose Go. |  |  |
| 5 | Display Billing Document | Choose the item searched out. | The billing document is displayed. |  |

### Perform Invoicing Process

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create invoice document based on the billing document you created at previous step. You can proceed with mass run or individual creation.

|  |
| --- |
| Note If you enabled Clarification at 2BG-Convergent Invoicing: Invoicing creation for Usage and Service, please follow the Perform Invoicing Process of 2BG-Convergent Invoicing: Invoicing creation for Usage and Service to perform Billing.If the clarification case is created when perform invoicing, please follow the Clarify Clarification Case Relevant to Invoicing Document (Optional) of 2BG-Convergent Invoicing: Invoicing creation for Usage and Service to perform Billing |

#### Option 1: Perform Invoicing Process (Mass Run)

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad as Administrator (Convergent Invoicing). | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the App | Choose Execute Invoicing - Mass Run (F3524) | The Execute Invoicing - Mass Run page is displayed |  |
| 3 | Create Application Job | Choose Create to create a new application job. | The New Job: Invoicing (Mass Creation) page is displayed |  |
| 4 | Select Template | Make the following entries as below:Job Template: Invoicing (Mass Creation)Job Name: <job name>Choose Step2. |  |  |
| 5 | Maintain Schedule Options | Make the following entries as below:Start Immediately: chooseRecurrence Pattern: Single RunChoose Step3. |  |  |
| 6 | Maintain Parameters | Make the following entries as below:Prefix of Run ID: <Prefix of Run ID>Invoicing Process: Y1Business Partner: <The Required Business Partner>Contract Account:<The Required Contract Account>Simulation Run: <Don’t Choose>Document Date: <The Current Date>Posting Date:<The Current Date>Problem Class: <problem class> |  |  |
| 7 | Execute | Choose Schedule. | The job is running immediately. |  |
| 8 | Locate the job from application job list | In the Execute Invoicing - Mass Run screen, make the following entries as below:Date From-To:: <Today -1/+1 day>Choose Go. |  |  |
| 9 | Check Log | Choose Image of Log to locate the application job log. | The log of application job is displayed. From the log, you can see the result of application job. |  |

#### Option 2: Perform Invoicing Process (Individual Run)

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad as Invoicing Specialist (Convergent Invoicing). | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the App | Choose Execute Invoicing - Business Partner (FKKINV_S) tile. | The Invoicing (Individual Creation) page is displayed. |  |
| 3 | Maintain Parameters | In the Invoicing (Individual Creation), make the following entries as below:Invoicing Process: Y1Document Date: <The Current Date>Posting Date: <The Current Date>Business Partner: <The Required Business Partner>Contract Account: <The Required Contract Account> |  |  |
| 4 | Execute | Choose Execute. | A dialog Selection of Source Documents is displayed. |  |
| 5 | Select Source Documents | On the Selection of Source Documents dialog choose Save. | A dialog Creation of Invoicing Units is displayed if there are more than one source documents to be invoiced. You can choose All Together or All Individually, then choose Save to continue. |  |
| 6 | Post Invoicing Document | In the Save invoicing document? dialog, chooseYes, until you see the dialog Invoicing Ended. If you choose Document, you can check the documents before posting. | A dialog Invoicing Ended is displayed.The invoicing document is posted. |  |
| 7 | Check Invoicing Document | Choose Continue (Enter) to leave the dialog. |  |  |

### Display Invoicing Document (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you display the created invoicing document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad as Invoicing Specialist (Convergent Invoicing). | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the App | In the Invoicing group, choose the Manage Invoicing Documents (F2048) tile. | The Manage Invoicing Documents page is displayed. |  |
| 3 | Maintain Parameters | In the Manage Invoicing Documents screen, make the following entries as below:Invoicing Document: <The Invoicing Document you want to Display> |  |  |
| 4 | Execute | Choose Go. |  |  |
| 5 | Display Invoicing Document | Choose Details. | The invoicing document is displayed. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

You may first have completed the following processes and conditions before you start with the test steps:

| Process | Business Condition |
| --- | --- |
| 2AR- Contract Accounting – Master Data and Basic Functions | Must be run before the test script. Business Partner and Contract Account must be created. |

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| 2BE: Convergent Invoicing – Invoice Correction Processing | The invoicing document created as part of process 2BG: Convergent Invoicing: Invoice Creation for Usage and Service can be used for further processing in 2BE: Convergent Invoicing: Invoice Correction Processing |

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
- related-to :: [[09-subscription-billing-and-contract-accounting/convergent-invoicing-invoice-correction-processing-2be-ae-test-script]]
- related-to :: [[09-subscription-billing-and-contract-accounting/test-script-convergent-invoicing-invoice-creation-for-usage-and-servic]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2T3_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 29,105 chars in the whole document
