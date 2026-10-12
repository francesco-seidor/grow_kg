---
id: 02-business-partner-and-product-master-data/test-script-master-data-consolidation-for-product-1n1-742
title: "Test Script: Master Data Consolidation for Product (1N1) (1N1_S4CLD2608_BPD_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 1N1: import, match, consolidate, validate and activate product master data."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/master-data-consolidation]
aliases: [1N1_S4CLD2608_BPD_EN_XX]
keywords: [Master Data Consolidation for Products and Business Partners, product master data consolidation, import source data, duplicate matching, best record calculation, validation and activation, track mass changes, consolidation automation, business roles, feature activation]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1N1_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-742
topic: 02-business-partner-and-product-master-data/master-data-consolidation
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Master Data Consolidation for Product (1N1) (1N1_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1N1_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Master Data Consolidation for Products and Business Partners** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Master Data Consolidation for Product (1N1) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232848911)

[2 Prerequisites 3](#_Toc232848912)

[2.1 System Access 3](#_Toc232848913)

[2.2 Roles 3](#_Toc232848914)

[2.3 Master Data, Organizational Data, and Other Data 3](#_Toc232848915)

[2.3.1 Download template file 3](#_Toc232848916)

[2.4 Business Conditions 4](#_Toc232848917)

[3 Overview Table 5](#_Toc232848918)

[4 Test Procedures 6](#_Toc232848919)

[4.1 Import Source Data 6](#_Toc232848920)

[4.2 Initial Check 7](#_Toc232848921)

[4.3 Matching 8](#_Toc232848922)

[4.4 Best Record Calculation 9](#_Toc232848923)

[4.5 Validation 9](#_Toc232848924)

[4.6 Activation 10](#_Toc232848925)

[4.7 Track Mass Changes 11](#_Toc232848926)

[4.8 Automation 12](#_Toc232848927)

## Purpose

Overview

This scope item enables organizations to load, validate, consolidate, and activate product master data from various source systems. The scope item supports duplicate detection and consolidation processes to improve product master data quality and consistency across the enterprise.

The scope item supports both the classic applications and the new cloud-ready applications with the same business processes and capabilities.

During the consolidation process, the system identifies duplicate product records and groups them into match groups. Based on survivorship rules defined for product master attributes, the system calculates the best record for each duplicate group. These best records can then be used in analytical and operational business scenarios.

Optionally, users can import source files without assigning a source system to prevent key mapping generation. This option is preferred for product mass creation scenarios.

The scope item also provides process templates that support automation, including derivation steps in which derivation scenarios are executed automatically.

To use the cloud-ready applications, you must activate the MDC_PRODUCT_GOVERNANCE feature toggle.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

This section describes test procedures for each process step that belongs to this scope item.

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

For more information, refer to How to Create a Business Role from a Template in the product assistance for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

Use your own master data to go through the test procedure. It is necessary to load a file into the system. Check whether such a file can be provided. It is also possible to start the app Import Master Data and choose Download File Template to use the file created by you.

#### Download template file

This step is necessary to get a template file for the procedure "Import Source Data". These template files contain template data and can be replaced by your own data.

Procedure

Run step 1 + 2 from procedure [Import Source Data](#unique_7) [page ] 6 and choose the link Download File Templates. Select Example Files to download a compressed file with example files to be used for uploading source data. Use one of these files (for example- MATERIAL.xlsx) for uploading or use them as a template for your own data. Ensure that for all rows the field Source_ID will be filled with data.

Result

A new file for uploading source data is created.

### Business Conditions

Activate Features

In a software update, SAP delivers certain features that could have an impact on your implemented solution initially in an inactive state. You can choose to already activate these features before they become available by default in a later release.

The test procedures in this document describe the software behavior when all features have been activated. It is a prerequisite for testing that you have activated all of the following features in each of your systems using the configuration activity Activate Features. For more information about this activity, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/3e94fcc37b42433b97d6aef0c830dc52.html) for SAP S/4HANA Cloud Public Edition.

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

- Configure Your Solution:

Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).

Navigate to Manage your Solution > Configure Your Solution. Search for Activate Features. In the search result, select the configuration activity and go to the next screen. Select the configuration step and choose Configure.

- SAP Central Business Configuration:

Log on to the project experience in SAP Central Business Configuration.

Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Activate Features. Choose the link to navigate directly to the target system of SAP S/4HANA Cloud Public Edition. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).

| Feature ID | Feature Title |
| --- | --- |
| MDC_PRODUCT_GOVERNANCE | Successor MDG Apps for Product - Cloud-Ready Mode in MDG |

## Overview Table

The scope item Master Data Consolidation for Product (1N1) consists of several process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the home page contains only the apps necessary for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the home page using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the home page and include the hidden apps, navigate to your user profile and choose App Finder. |

|  |  |  |  |
| --- | --- | --- | --- |
| Choose the appropriate entity: Process Step, Report, or Item | Business Role | App/Transaction | Expected Results |
| [Import Source Data](#unique_7) [page ] 6 | Master Data Specialist - Product Data (MDG) | SAP Fiori: Import Master Data - Products (F8545) | Source Data loaded into source table. |
| [Initial Check](#unique_10) [page ] 7 | Master Data Specialist - Product Data (MDG) | SAP Fiori: Manage Consolidation Processes - Products (F8544) | The system provides the result of a check (based on system customizing). |
| [Matching](#unique_11) [page ] 8 | Master Data Specialist - Product Data (MDG) | SAP Fiori: Manage Consolidation Processes - Products (F8544) | Match groups with potential duplicates. |
| [Best Record Calculation](#unique_12) [page ] 9 | Master Data Specialist - Product Data (MDG) | SAP Fiori: Manage Consolidation Processes - Products (F8544) | Best records based on approved match groups. |
| [Validation](#unique_13) [page ] 9 | Master Data Specialist - Product Data (MDG) | SAP Fiori: Manage Consolidation Processes - Products (F8544) | Check the result to determine whether records can be activated in the system (based on system customizing). |
| [Activation](#unique_14) [page ] 10 | Master Data Specialist - Product Data (MDG) | SAP Fiori: Manage Consolidation Processes - Products (F8544) | New master data has been created or existing master data has been updated. |
| [Track Mass Changes](#unique_15) [page ] 11 | Master Data Specialist - Product Data (MDG) | SAP Fiori: Track Changes - Products (F8469) | Track your changes made during the Consolidation Process. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Import Source Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Import Source Data must upload data into the source tables before you start a consolidation process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data (MDG). | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open the Import Master Data - Products (F8545) app. | The Import Master Data - Products (F8545) screen displays. |  |
| 3 | Create New Import | Choose Create to create a new import. | The New: Import screen displays. |  |
| 4 | Describe Data Source | Enter the following data:Source System: Enter a source system name, for example, CRM_US.Data Package: Enter a data package (System shows default Package name after the file is uploaded. See next step.).Optional: You can import without Source System to prevent Key Mapping generation. Preferred for Mass Creation use case. | The system accepts the data and the footer toolbar should show the Create button. |  |
| 5 | Select File | Press Upload to select a file for upload. You can use the example file from chapter [Download template file](#unique_6) [page ] 3. | The system transfers the file to the system and shows some progress information. |  |
| 6 | Import | Check the settings and press Create (at the bottom of the screen) to continue. | The system provides some information about the import steps in the import log. |  |
| 7 | Create Consolidation Process | Choose on Consolidate and enter the following data and choose Save to continue.Description: Enter a description for the consolidation process, for example, Consolidate Product for CRM_US.Process Template: Select an available process template, for example, SAP: Consolidate Product Data. | The system creates a new consolidation process and shows the process UI. |  |

### Initial Check

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Initial check provides a first impression of the quality of the loaded data. The checks are done based on the system settings.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Start Initial Check | Choose Start (at the bottom of the screen) to start the check. | The system starts the check and shows the result screen when finished. |  |
| 2 | Check Errors and Warnings | Click on the numbers Errors and Warnings to show details. | Message texts are shown. |  |
| 3 | Show Records | Choose Show Result to navigate through the list of records. | The system shows a list with records. |  |
| 4 | Check the Result | Navigate through all related tables of a record using the tab bar.After finishing the review, choose the Back icon. | A list of all the relevant tables is shown. |  |

### Matching

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step identifies duplicates and shows a list of match groups (groups of potential duplicates). The user has to review all open groups and has to approve or reject them.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Start Matching Step | Choose Continue (at the bottom of the screen) to start the matching step. | The system starts the matching and shows the result screen when finished. The result shows bars with approved, or open match groups, or both. |  |
| 2 | Select Open Match Groups | On the bar chart, choose the bar Open match groups (if existing) and select Show Details to navigate through the open match groups. | The system shows a list with open match groups. |  |
| 3 | Approve or Reject Match Groups | Go to each open match group and approve or reject it:Choose the Approve button at the top of the group to approve.Choose the Reject button at the top of the group to reject.After finishing the review, select the Back icon. | All the match groups that are approved or rejected disappear from the list of open match groups. |  |

### Best Record Calculation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

This process step merges the records for approved match groups into one record. This merging is based on a specified rule.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Start Best Record Calculation step | Choose Continue (at the bottom of the screen) to start the Best Record Calculation step. | The system starts the step and shows the result screen when finished. The result shows a pie with a different group of target records. |  |
| 2 | Show Best Records | Select Show Result to navigate to the list of best records. | The system shows a list with the best records. |  |
| 3 | Check the Result | Navigate through all related tables of a record using the tab bar.After finishing the review, select the Back icon. | A list of all the relevant tables is shown. |  |

### Validation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Validation provides information showing whether the data can be activated. The checks are done based on the system settings. Erroneous data cannot be activated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Start in Validation | Choose Continue (at the bottom of the screen) to start the validation. | The system starts the validation and shows the result screen when finished. |  |
| 2 | Check Errors and Warnings | Click on the numbers Errors and Warnings to show details. | Message texts are shown. |  |
| 3 | Show Records | Choose Show Results to navigate through the list of records. | The system shows a list with records. |  |
| 4 | Check the Result | Navigate through all related tables of a record using the tab bar.After finishing the review, choose the Back icon. | A list of all relevant tables is shown. |  |

### Activation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The activation step triggers the activation of the data into the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Start Activation | In case no errors were detected during the Validation step, the system continues with the Activation step automatically.Otherwise, choose Continue (at the bottom of the screen) to start the activation. | The system starts the activation and shows a result screen when finished. Note down the process Id. |  |
| 2 | Check Errors and Warnings (optional) | When warnings or errors occurred, the system provides this information. Click on the numbers Errors and Warnings to show details. | Message texts are shown. |  |

### Track Mass Changes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Track your changes made during the Consolidation process. You can view the list of changes only if you have made the changes during the consolidation process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access App | Go back to the SAP Fiori launchpad. Open Track Changes - Products (F8469). | The Track Changes - Products screen displays. |  |
| 2 | Filter Inputs | Enter the process ID that you noted down in [Activation](#unique_14) [page ] 10 step 1. Choose Go. | You must be able to see the list of changes that you made during the consolidation process. If there are no changes available, then you made no changes during the consolidation process. |  |

### Automation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Verify the process template for consolidation automation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data (MDG). | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open the Import Master Data - Products (F8545) app. | The Import Master Data - Products (F8545) screen displays. |  |
| 3 | Select File | Press Browse to select a file for upload. You can use the example file from chapter [Download template file](#unique_6) [page ] 3. | The system transfers the file to the system and shows some progress information. |  |
| 4 | Describe Data Source | Enter the following data:Source System: Enter a source system name, for example, CRM_US.Data Package: System shows default package name.Optional: You can import without source system to prevent Key Mapping generation. This approach is preferred for the Mass Creation use case. | The system accepts the data, and the footer toolbar should show the Import button. |  |
| 5 | Import | Check the settings and choose Import (at the bottom of the screen) to continue. | The system goes to the Import Details screen. The system provides some information about the import steps. |  |
| 6 | Create Consolidation Process | Choose Consolidate, enter the following data, and choose Save to continue.Description: Enter a description for the consolidation process.Process Template: Select an available process template for automation, for example, SAP: Consolidate Product Automated. | The system creates a new consolidation process and shows the process UI. |  |
| 7 | Check | In the process UI, the following steps should be displayed:Initial CheckMatchingBest Record CalculationDerivationValidationActivation | The Derivation step is included in the process UI. |  |

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
- related-to :: [[02-business-partner-and-product-master-data/test-script-master-data-consolidation-for-business-partner-1n3-743]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1N1_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 24,204 chars in the whole document
