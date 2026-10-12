---
id: 09-subscription-billing-and-contract-accounting/convergent-invoicing-cost-handling-for-subscriptions-and-usage-6wd-ae
title: Convergent Invoicing – Cost Handling for Subscriptions and Usage (6WD_AE) Test Script (6WD_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition test script for scope item 6WD: posting cost of sales via billable items, billing and invoicing in Convergent Invoicing."
cluster: 09-subscription-billing-and-contract-accounting
tags: [kb/subscription-billing-and-contract-accounting, topic/cost-handling-for-subscriptions]
aliases: [6WD_S4CLD2608_BPD_EN_AE]
keywords: [Cost Handling for Subscriptions and Usage, convergent invoicing, cost posting, billable items, billing process, invoicing process, amount calculation key, test scripts, business roles, csv upload template]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6WD_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1198
topic: 09-subscription-billing-and-contract-accounting/cost-handling-for-subscriptions
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Convergent Invoicing – Cost Handling for Subscriptions and Usage (6WD_AE) Test Script (6WD_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6WD_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Cost Handling for Subscriptions and Usage** in Subscription Billing and Contract Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Convergent Invoicing – Cost Handling for Subscriptions and Usage (6WD_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232859705)

[2 Prerequisites 4](#_Toc232859706)

[2.1 System Access 4](#_Toc232859707)

[2.2 Roles 4](#_Toc232859708)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232859709)

[2.4 Business Conditions 5](#_Toc232859710)

[2.5 Preliminary Steps 6](#_Toc232859711)

[2.5.1 Maintain Amount Calculation Key 6](#_Toc232859712)

[3 Overview Table 9](#_Toc232859713)

[4 Test Procedures 10](#_Toc232859714)

[4.1 Create Billable Items 10](#_Toc232859715)

[4.1.1 Option 1: Upload Billable Items 10](#_Toc232859716)

[4.1.2 Option 2: Invoke Create Billable Items SOAP API 12](#_Toc232859717)

[4.2 Perform Billing Process 12](#_Toc232859718)

[4.2.1 Option 1: Perform Billing Process (Mass Run) 12](#_Toc232859719)

[4.2.2 Option 2: Perform Billing Process (Individual Run) 14](#_Toc232859720)

[4.3 Perform Invoicing Process 15](#_Toc232859721)

[4.3.1 Option 1: Perform Invoicing Process (Mass Run) 15](#_Toc232859722)

[4.3.2 Option 2: Perform Invoicing Process (Individual Run) 16](#_Toc232859723)

[5 Appendix 18](#_Toc232859724)

[5.1 Process Integration 18](#_Toc232859725)

[5.1.1 Preceding Processes 18](#_Toc232859726)

[5.2 CSV Template Creation 18](#_Toc232859727)

[5.2.1 Sample Data for Cost 18](#_Toc232859728)

## Purpose

Overview

This process allows the posting of costs as well as cost recognition for fulfillment costs.

In invoicing, the cost of sales can be posted as an expense to financial accounting, and G/L items are automatically created in FI-CA. This posting to expense accounts can be done synchronously with sales revenue posting during bill creation. Depending on the type of costs, composite cost amounts can be determined and posted to different expense accounts.

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

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log on |
| --- | --- | --- | --- | --- |
| Invoicing Specialist (Convergent Invoicing) | SAP_BR_INVOICING_SPEC_CINV | Convergent Invoicing / Subscription Billing | SAP_BR_INVOICING_SPECIALIST_CINV / SAP_CEC_SPT_SUBSCR_BILLG_SPCLST_PC |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Administrator (Convergent Invoicing) | SAP_BR_INVOICING_ADMIN_CINV | Administration - Convergent Invoicing | SAP_BR_INVOICING_ADMIN_CINV |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company code | 3310 | Company Code 3310 |  |

### Business Conditions

Before this scope item can be tested, the following business condition must be met:

| Scope Item | Business Condition |
| --- | --- |
| 2AR - Contract Accounting – Master Data and Basic Functions | Must be run before this test script. Business Partner and Contract Account must be created. |
| 2BG - Convergent Invoicing – Invoice Creation for Usage and Service | Must be deployed before running this test script. |

### Preliminary Steps

#### Maintain Amount Calculation Key

Use

In this step, you enhance the amount calculation key of SCST.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration.. | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution .Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Configure Your Solution screen is displayed. |  |
| 4 | Open Maintain Calculation Key | On the Configure Your Solution: Realize Phase screen, search Maintain Amount Calculation Key then choose Enter.Select the line of the item of Cost Posting and go to the next screen.On the Configuration Your Solution - Cost Posting screen, choose Configure on the line of configuration step with name Maintain Amount Calculation Key. |  |  |
| 5 | Make Parameters to maintain calculation key | On the Maintain Amount Calculation Key - Change screen, choose the line with the calculation key SCST, and then choose Validity.Choose New Entries and make the entries as below:Crcy: <your currency>Valid From: <today's date>Choose Save to save the validity.Choose the newly added validity and choose Calculation Rules.Confirm the information dialog with message Entries are not added individually to the change request.Choose New Entries, on the New Entries: Details of Added Entries screen, make the entries as below:Base Amt Limit: <Lower Limit for Base Amount>, for example, 0.Debit/Credit: <Debit or Credit> for example, Debit.Percentage: <your percentage>, for example, 5.Choose Save. | The calculation key SCST has been enhanced.Note The amount of cost will be determined as: Based on the given example, the amount of cost = Customer Amount * Percentage |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Maintain Amount Calculation Key | Go to the Business Processes Configuration app. You can search for a configuration activity and navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).Search for Maintain Amount Calculation Key. |  |  |
| 3 | Make Parameters to maintain calculation key | On the Maintain Amount Calculation Key - Change screen, choose the line with the calculation key SCST, and then choose Validity.Choose New Entries and make the entries as below:Crcy: <your currency>Valid From: <today's date>Choose Save to save the validity.Choose the newly added validity and choose Calculation Rules.Confirm the information dialog with message Entries are not added individually to the change request.Choose New Entries, on the New Entries: Details of Added Entries screen, make the entries as below:Base Amt Limit: <Lower Limit for Base Amount>, for example, 0.Debit/Credit: <Debit or Credit> for example, Debit.Percentage: <your percentage>, for example, 5.Choose Save. | The calculation key SCST has been enhanced.Note The amount of cost will be determined as: Based on the given example, the amount of cost = Customer Amount * Percentage |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Create Billable Items |  |  |  |
| [Option 1: Upload Billable Items](#unique_9) [page ] 10 | Invoicing Specialist (Convergent Invoicing) | Upload Billable Items (F4664) | Billable Item is created. |
| [Option 2: Invoke Create Billable Items SOAP API](#unique_10) [page ] 12 | N/A | N/A | Billable Item is created by invoking create billable items SOAP API |
| Perform Billable Process |  |  |  |
| [Option 1: Perform Billing Process (Mass Run)](#unique_11) [page ] 12 | Administrator (Convergent Invoicing) | Execute Billing - Mass Run (F3525) | Billing Document is created |
| [Option 2: Perform Billing Process (Individual Run)](#unique_12) [page ] 14 | Invoicing Specialist (Convergent Invoicing) | Execute Billing - Business Partner (FKKBIX_S) | Billing Document is created |
| Perform Invoicing Process |  |  |  |
| [Option 1: Perform Invoicing Process (Mass Run)](#unique_13) [page ] 15 | Administrator (Convergent Invoicing) | Execute Invoicing - Mass Run (F3524) | Invoicing Document is created |
| [Option 2: Perform Invoicing Process (Individual Run)](#unique_14) [page ] 16 | Invoicing Specialist (Convergent Invoicing) | Execute Invoicing - Business Partner (FKKINV_S) | Invoicing Document is created |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Billable Items

#### Option 1: Upload Billable Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you upload csv file based on the selected items to generate the billable item.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad as Invoicing Specialist (Convergent Invoicing). | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the App | Choose Upload Billable Items (F4664) tile. | The Upload of Billable Item page is displayed. |  |
| 3 | Create Template | In the Upload of Billable Items screen, make the following entries as below and choose Create Template.Upload Schema: CSV File for Billable Items |  |  |
| 4 | Choose Billable Item Class | In the Create Template screen, make the entries as below:Choose Billable Item Class: 0SAP |  |  |
| 5 | Choose Record Type | Choose Main Items. |  |  |
| 6 | Choose Fields for Record Types | Please refer to Data Item Selection in the Appendix to choose fields of record type based on Sample Data for Cost.Choose Download Template. | The items were chosen and saved successfully. |  |
| 7 | Edit the local CSV file | Open and edit the copy at your native file system and add value to it accordingly. | Based on the given sequence of main item, the values were filled into csv file.Add value for CostNote Please follow the sample data mentioned in Appendix to create the CSV file for Cost. |  |
| 8 | Import CSV File | In the Upload of Billable Items screen, make the entries as below:File Source: Choose Browse and find the file you edited.Choose OK to close the popup dialog of File Upload and upload the file you edited at step7 from native file system to SAP file system. | The file you edited at step7 was uploaded to SAP system. |  |
| 9 | Read CSV File | Choose Read. | Log is provided to identify the csv file read error.If there is no error, the field and filed value of CSV file can be displayed at Preview section. You also can choose Edit to modify the value as your demands. |  |
| 10 | Load CSV File | Choose the entries you want to upload then choose Upload. | Before load data, you can make the modification to the individual field based on your request. |  |
| 11 | Display Log | Choose Show Application Log to display log. | From the log, you will see the billable item is created or not. |  |
| 12 | Display Billable Items | Choose Close on the Application Log screen then choose Show Billable Items on the Upload Messages screen. | Two Billable Items with the same Same Source Transaction ID are generated. One Billable Item is for Service Consumption and the other is for the Cost of Subriscaption.Please record the Source Transaction Id. |  |

#### Option 2: Invoke Create Billable Items SOAP API

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create the billable items by invoking the SOAP API of convergent invoicing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Navigate to SAP API Business HUB | Open web browser and navigate to [https://api.sap.com](https://api.sap.com) | The SAP API Business HUB home page is displayed. |  |
| 2 | Locate SAP S/4HANA Cloud Public Edition API package | Choose SAP S/4HANA Cloud Public Edition and choose APIs tab. | The SAP S/4HANA Cloud Public Edition API package is located. |  |
| 3 | Search out create billable items SOAP API | Choose SOAP and search for Convergent Invoicing Billable Items - Create. | The create billable items SOAP API is displayed. |  |

### Perform Billing Process

#### Option 1: Perform Billing Process (Mass Run)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as Administrator (Convergent Invoicing). | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the App | Choose Execute Billing - Mass Run (F3525) tile. | The Execute Billing - Mass Run page is displayed |  |
| 3 | Create Application Job | Choose Create button to create a new application job. | The New Job: Billing (Mass Creation) page is displayed |  |
| 4 | Select Template | Make the following entries as below:Job Template; Billing (Mass Creation)Job Name; <job name>Choose Step2. |  |  |
| 5 | Maintain Schedule Options | Make the following entries as below:Start Immediately: chooseRecurrence Pattern: Single RunChoose Step3. |  |  |
| 6 | Maintain Parameters | Make the following entries as below:Prefix of Run ID: <Prefix of Run ID>Billing Process: Y001Contract Account: <the required contract account>Simulation Run: <don’t choose>Billing Date: <the current date>Problem Class: <problem class> |  |  |
| 7 | Execute | Choose Schedule. | The job is running immediately. |  |
| 8 | Locate the job from application job list | In the Execute Billing - Mass Run screen, make the following entries as below:Date From-To: Today -1/+1 dayChoose Go button. | The application job you want to find was located in the application jobs list. |  |
| 9 | Check Log | Choose Image of Log to access the located application job log. | The log of application job is displayed. From the log, you can see the result of application job. |  |

#### Option 2: Perform Billing Process (Individual Run)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as Invoicing Specialist (Convergent Invoicing). | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the App | Choose Execute Billing - Business Partner (FKKBIX_S) tile. | The Billing (Individual Creation) page is displayed. |  |
| 3 | Maintain Parameters | In the Billing (Individual Creation), make the following entries as below:Billing Process: Y001Billing Date: <the current date>Contract Account: <the required contract account> |  |  |
| 4 | Execute | Choose Execute. |  |  |
| 5 | Choose Billable Item and Create Billing Units | In the Choose Billable Items dialog, choose the two Billable Items whose Source Transaction ID is the same as the one you have recorded in the previous step then choose Save. In the Creation of Billing Units dialog, choose Save, until you see the dialog Billing Ended. | A dialog Billing Ended is displayed.Please record the Billing Document Number. |  |
| 6 | Check Billing Document | Choose Continue (Enter) to leave the dialog. |  |  |

### Perform Invoicing Process

#### Option 1: Perform Invoicing Process (Mass Run)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as Administrator (Convergent Invoicing). | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the App | Choose Execute Invoicing - Mass Run (F3524). | The Execute Invoicing - Mass Run page is displayed. |  |
| 3 | Create Application Job | Choose Create button to create a new application job. | The New Job: Invoicing (Mass Creation) page is displayed. |  |
| 4 | Select Template | Make the following entries as below:Job Template; Invoicing (Mass Creation)Job Name; <job name>Choose Step2. |  |  |
| 5 | Maintain Schedule Options | Make the following entries as below:Start Immediately: chooseRecurrence Pattern: Single RunChoose Step3. |  |  |
| 6 | Maintain Parameters | Make the following entries as below:Prefix of Run ID: <Prefix of Run ID>Invoicing Process: Y1Business Partner: <the required business partner>Contract Account: <the required contract account>Simulation Run: <don’t choose>Document Date: <the current date>Posting Date: <the current date>Problem Class: <problem class> |  |  |
| 7 | Execute | Choose Schedule. | The job is running immediately. |  |
| 8 | Locate the job from application job list | In the Execute Invoicing - Mass Run screen, make the following entries as below:Date From-To: Today -1/+1 dayChoose Go button. |  |  |
| 9 | Check Log | Choose Image of Log to located the application job log. | The log of application job is displayed. From the log, you can see the result of application job. |  |

#### Option 2: Perform Invoicing Process (Individual Run)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as Invoicing Specialist (Convergent Invoicing). | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the App | Choose Execute Invoicing - Business Partner (FKKINV_S) tile. | The Invoicing (Individual Creation) page is displayed. |  |
| 3 | Maintain Parameters | In the Invoicing (Individual Creation), make the following entries as below:Invoicing Process: Y1Document Date: <the current date>Posting Date: <the current date>Business Partner: <the required business partner>Contract Account: <the required contract account> |  |  |
| 4 | Execute | Choose Execute. | A dialog Selection of Source Documents is displayed. |  |
| 5 | Select Source Documents | On the Selection of Source Documents dialog, choose the one which Source Document No. is the same as your recorded Billing Doucment No. , then choose Save. | A dialog Creation of Invoicing Units is displayed if there are more than one source documents to be invoiced. You can choose All Together or All Individually, then choose Save to continue. |  |
| 6 | Post Invoicing Document | In the Save invoicing document dialog, choose Yes, until you see the dialog Invoicing Ended. If you choose Document, you can check thedocuments before posting. | A dialog Invoicing Ended is displayed.Invoicing document is posted. |  |
| 7 | Check Invoicing Document | Choose Continue (Enter) to leave the dialog. |  |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

You may first have completed the following processes and conditions before you start with the test steps:

Table 1:

| Process | Business Condition |
| --- | --- |
| Contract Accounting – Master Data and Basic Functions(2AR) | Must be run before the test script. Business Partner and Contract Account must be created. |

### CSV Template Creation

#### Sample Data for Cost

| Item of Main Items | Global Field Name | Cost | Comments |
| --- | --- | --- | --- |
| BIT_AMOUNT | CABllbleItmAmount | Positive Value | Billable Item Amt |
| GPART | BusinessPartner | The business partner | Business Partner |
| SRCTAID | CABllbleItmSourceTransId | Any Number | Source Trans.ID |
| SUBPROCESS | CABillgSubprocess | Y001 | Subprocess of Billing |
| BITTYPE | CABllbleItmType | Y001 | Type of Billable Item |
| VKONT | ContractAccount | The contract account | Contract Account |
| BIT_CURR | CABllbleItmCurrency | The currency | Currency |
| CO_TYPE | CABllbleItmCostType | SCST | Billable Item Cost Type |

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
- see-also :: [[09-subscription-billing-and-contract-accounting/convergent-invoicing-invoice-correction-processing-2be-ae-test-script]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6WD_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 28,482 chars in the whole document
