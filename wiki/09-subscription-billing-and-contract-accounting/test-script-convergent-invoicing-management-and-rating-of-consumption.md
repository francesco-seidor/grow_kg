---
id: 09-subscription-billing-and-contract-accounting/test-script-convergent-invoicing-management-and-rating-of-consumption
title: Test Script - Convergent Invoicing – Management and Rating of Consumption Items (3DX_AE) (3DX_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition test script for scope item 3DX: uploading, displaying and rating consumption items to create billable items in Convergent Invoicing."
cluster: 09-subscription-billing-and-contract-accounting
tags: [kb/subscription-billing-and-contract-accounting, topic/consumption-items-and-rating]
aliases: [3DX_S4CLD2608_BPD_EN_AE]
keywords: [Consumption Items and Service-Type-Based Rating, consumption items, rating, billable items, convergent invoicing, mass run rating, business roles, business conditions, process integration, demo data]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3DX_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-929
topic: 09-subscription-billing-and-contract-accounting/consumption-items-and-rating
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script - Convergent Invoicing – Management and Rating of Consumption Items (3DX_AE) (3DX_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3DX_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Consumption Items and Service-Type-Based Rating** in Subscription Billing and Contract Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Convergent Invoicing – Management and Rating of Consumption Items (3DX_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232852298)

[2 Prerequisites 3](#_Toc232852299)

[2.1 System Access 3](#_Toc232852300)

[2.2 Roles 3](#_Toc232852301)

[2.3 Master Data, Organizational Data, and Other Data 3](#_Toc232852302)

[2.4 Business Conditions 4](#_Toc232852303)

[3 Overview Table 6](#_Toc232852304)

[4 Test Procedures 7](#_Toc232852305)

[4.1 Upload Consumption Items 7](#_Toc232852306)

[4.2 Display Consumption Items (Optional) 9](#_Toc232852307)

[4.3 Perform Rating 9](#_Toc232852308)

[4.3.1 Option 1: Perform Rating (Individual Run) 10](#_Toc232852309)

[4.3.2 Option 2: Perform Rating (Mass Run) 11](#_Toc232852310)

[4.4 Display Billable Item (Optional) 12](#_Toc232852311)

[5 Appendix 14](#_Toc232852312)

[5.1 Process Integration 14](#_Toc232852313)

[5.1.1 Preceding Processes 14](#_Toc232852314)

[5.1.2 Succeeding Processes 14](#_Toc232852315)

## Purpose

Overview

This process lets you create, rate, and manage consumption items in a usage-based process. The rating process for consumption items creates priced billable items.

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
| Company Code | 3310 |  |  |
| Sales Organization | 10 |  |  |
| Distribution Channel | 10 |  |  |
| Pricing Condition | PST0 |  |  |
| Pricing Condition | PST1 |  |  |
| Pricing Condition | PST2 |  |  |

You can find general information on how to create master data objects in the following Master Data Scripts (MDS):

Table 1: Master Data Script Reference

| Master Data Script ID | Description |
| --- | --- |
| 3GD | Create Service Type Based Pricing Condition - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met:

| Scope Item | Business Condition |
| --- | --- |
| 2AR- Contract Accounting – Master Data and Basic Functions | Must be run before the test script. Business Partner, Contract Account and Provider Contract must be created. |
| 2BG - Convergent Invoicing – Invoice Creation for Usage and Service | Must be deployed before running this test script. |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/ Transaction | Expected Results |
| --- | --- | --- | --- |
| [Upload Consumption Items](#unique_8) [page ] 7 | Invoicing Specialist (Convergent Invoicing) | Upload Consumption Items (F5081) | Consumption Item is created |
| [Display Consumption Items (Optional)](#unique_9) [page ] 9 | Invoicing Specialist (Convergent Invoicing) | Manage Consumption Items (F3410) | Consumption Items is displayed |
| [Option 1: Perform Rating (Individual Run)](#unique_10) [page ] 10 | Invoicing Specialist (Convergent Invoicing) | Perform Rating - Business Partner (FKKBIX_RATE_S) | Consumption Items is rated and the corresponding billable item is created. |
| [Option 2: Perform Rating (Mass Run)](#unique_11) [page ] 11 | Administrator (Convergent Invoicing) | Execute Rating - Mass Run (F3773) | Consumption Items is rated and the corresponding billable item is created |
| [Display Billable Item (Optional)](#unique_12) [page ] 12 | Invoicing Specialist (Convergent Invoicing) | Manage Consumption Items (F3410) | The corresponding billable item is displayed. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Upload Consumption Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you upload csv file based on the selected main items to generate the consumption item.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as Invoicing Specialist (Convergent Invoicing). | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the App | Choose the Upload Consumption Items (F5081) tile. | The Upload Consumption Items page is displayed. |  |
| 3 | Create Template | In the Upload Consumption Items screen, make the following entries as below and choose Create Template:Upload Schema: CSV File for Consumption Items |  |  |
| 4 | Choose Consumption Item Class | In the Create Template screen, make the entries as below:Choose Consumption Item Class: 0SAP |  |  |
| 5 | Choose Fields for Main Items | In the Create Template screen, make the following entries as below and choose Download Template:BusinessPartner: Business PartnerContractAccount: Contract AccountCAContract: ContractCAProviderContractItemNumber: Contract ItemCACnsmpnItmID: Consumption Item IDCACnsmpnItmConsumptionDateTime: Consumpt. DateCACnsmpnItmQty: Quantity ConsumedCACnsmpnItmQuantityUnit: Unit of MeasureCACnsmpnItmIDType: Type of Cons.Item ID | The items were chosen and download to local successfully. |  |
| 6 | Edit the local CSV file | Open and edit the copy at your native file system and add value to it accordingly.BusinessPartner: <Business Partner>ContractAccount: <Contract Account>CAContract: <Provider Contract>CACnsmpnItmID: <Consumption Item ID>CAProviderContractItemNumber: <Contract Item>CACnsmpnItmConsumptionDateTime: <the current date YYYYMMDDHHMMSS>CACnsmpnItmQty: <Quantity Consumed >CACnsmpnItmQuantityUnit: PCCACnsmpnItmIDType: <Type of Cons.Item ID> eg: 01 | Note Contract Account has to be maintained explicitly if the given business partner has multiple contract accounts.CACnsmpnItmID will be assigned internally if it hasn't been filled at CSV file.CAProviderContractItemNumber will be filled with 1 as default if it hasn't been filled at CSV file. |  |
| 7 | Import CSV File | In the Upload Consumption Items screen, make the entries as below:File Source: choose Browse…Choose the file and choose Open. | The file you edited at step 6 is uploaded to SAP system. |  |
| 8 | Read CSV File | Choose Read. | Log is provided to identify the csv file read error. |  |
| 9 | Load CSV File | Choose the entries you want to upload then choose Upload. | Before load data, you can make the modification to the individual field based on your request. |  |
| 10 | Display Log | Choose Show Application Log to display log. | From the log, you will see the item is created or not. |  |

### Display Consumption Items (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you display the created consumption items.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as Invoicing Specialist (Convergent Invoicing). | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the SAP Fiori App | Choose the Manage Consumption Items (F3410) tile. |  |  |
| 3 | Maintain Parameters | In the Manage Consumption Items screen, make the following entries as below:Consumption Item ID: <the consumption item id you want to display> |  |  |
| 4 | Execute | Choose Go. |  |  |
| 5 | Display Consumption item | Choose the search out item. | The consumption item is displayed. |  |

### Perform Rating

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you will rate the consumption item. The corresponding billable item will be generated. You can process with mass run or individual rating.

#### Option 1: Perform Rating (Individual Run)

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
| 2 | Access the App | Choose the Perform Rating - Business Partner (FKKBIX_RATE_S) tile. |  |  |
| 3 | Maintain Parameters | In the Perform Rating for Consumption Items (Individual Processing), make the entries as below:Rating Group: <rating group>Rating Date: <the current date>Business Partner: <business partner>Contract Account: <contract account>Simulation run: <don’t check> | Make sure Rating Date is after the Rate From Date of the consumption item to be rated. |  |
| 4 | Execute | Choose Execute. |  |  |
| 5 | Choose Consumption Item for Rating Package | In the Selection of Consumption Items for Rating Package dialog, choose the consumption items you want to rate and choose Save. |  |  |
| 6 | Create rating unit | In the Creation of Rating Units, choose Save |  |  |
| 7 | Check rating result | Choose Continue(Enter) to leave the dialog. |  |  |

#### Option 2: Perform Rating (Mass Run)

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
| 2 | Access the App | Choose the Execute Rating - Mass Run (F3773) tile. | The Execute Rating - Mass Runpage is displayed. |  |
| 3 | Create Application Job | Choose Create to create a new application job. | The New Job: Rating page is displayed. |  |
| 4 | Select Template | Make the following entries as below:Job Template: RatingJob Name: <job name>Choose Step 2. |  |  |
| 5 | Maintain Schedule Options | Make the following entries as below:Start Immediately: chooseRecurrence Pattern: Single RunChoose Step 3. |  |  |
| 6 | Maintain Parameters | Make the following entries as below:Prefix of Run ID: <Prefix of Run ID>Rating Group: S0001Business Partner: <Business Partner>Contract Account: <Contract Account>Simulation run: <don’t choose>Problem Class: <problem class>Rating Date: <the current date>, use a date after the rate from date in the consumption item to be rated. |  |  |
| 7 | Execute | Choose Schedule. | The job is running immediately. |  |
| 8 | Locate the job from application job list | In the Execute Rating - Mass Run screen, make the following entries as below:Date From-To:: <Today -1/+1 day> | The application job you want to find was located in the application jobs list. |  |
| 9 | Check Log | Choose Image of Log to access located the application job log. | The log of application job is displayed. From the log, you can see the result of application job. |  |

### Display Billable Item (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After rating, the system will create the billable item based on the rated consumption item. In this step, you can display the corresponding billable item from consumption item.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as Invoicing Specialist (Convergent Invoicing). | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the SAP Fiori App | Choose the Manage Consumption Items (F3410) tile. |  |  |
| 3 | Maintain Parameters | In the Manage Consumption Items screen, make the following entries as below:Consumption Item ID: <the consumption item id you rated> |  |  |
| 4 | Execute | Choose Go. |  |  |
| 5 | Display Consumption item | Choose the search out item. | The consumption item is displayed. |  |
| 6 | Choose Billable Item | Choose Billable Items | The corresponding billable item is displayed. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

The following processes and conditions can proceed this process.

| Process | Business Condition |
| --- | --- |
| 2AR- Contract Accounting – Master Data and Basic Functions | Must be run before the test script. Business Partner and Contract Account must be created. |

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| 2BG: Convergent Invoicing – Invoice Creation for Usage and Service | The created billable item as part of process 3DX: Convergent Invoicing – Management and Rating of Consumption Items can be used for further Billing and Invoicing in 2BG: Convergent Invoicing – Invoice Creation for Usage and Service of Perform Billing Process, Display Billing Document and Perform Invoicing Process. |

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
- related-to :: [[09-subscription-billing-and-contract-accounting/criar-condicao-de-determinacao-de-precos-baseada-em-tipo-de-servico-md]]
- related-to :: [[09-subscription-billing-and-contract-accounting/master-data-script-create-service-type-based-pricing-condition-mds-3gd]]
- related-to :: [[09-subscription-billing-and-contract-accounting/mds-3gd-319]]
- related-to :: [[09-subscription-billing-and-contract-accounting/mds-3gd-321]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3DX_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 21,249 chars in the whole document
