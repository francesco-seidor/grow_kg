---
id: 02-business-partner-and-product-master-data/test-script-master-data-consolidation-for-business-partner-1n3-743
title: "Test Script: Master Data Consolidation for Business Partner (1N3) (1N3_S4CLD2608_BPD_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 1N3: importing, matching, best-record calculation, validation, activation and automation of business partner consolidation."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/master-data-consolidation]
aliases: [1N3_S4CLD2608_BPD_EN_XX]
keywords: [Master Data Consolidation for Products and Business Partners, master data consolidation, business partner data, import source data, duplicate matching, best record calculation, validation, activation, mass change tracking, consolidation automation]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1N3_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-743
topic: 02-business-partner-and-product-master-data/master-data-consolidation
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Master Data Consolidation for Business Partner (1N3) (1N3_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1N3_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Master Data Consolidation for Products and Business Partners** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Master Data Consolidation for Business Partner (1N3) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232847164)

[2 Prerequisites 3](#_Toc232847165)

[2.1 System Access 3](#_Toc232847166)

[2.2 Roles 3](#_Toc232847167)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232847168)

[2.3.1 Download template file 4](#_Toc232847169)

[3 Overview Table 5](#_Toc232847170)

[4 Test Procedures 6](#_Toc232847171)

[4.1 Import Source Data 6](#_Toc232847172)

[4.2 Initial Check 7](#_Toc232847173)

[4.3 Matching 8](#_Toc232847174)

[4.4 Best Record Calculation 9](#_Toc232847175)

[4.5 Validation 9](#_Toc232847176)

[4.6 Activation 10](#_Toc232847177)

[4.7 Track Mass Changes 11](#_Toc232847178)

[4.8 Automation 12](#_Toc232847179)

## Purpose

Overview

The Master Data Consolidation for Business Partner scope item provides capabilities to load master data from various sources and to detect duplicates during the load process as well as during regular housekeeping activities.

For each of the resulting match groups, the system calculates a best record out of the duplicates in that group using survivorship rules on the master data attributes. These best records can then be used in dedicated analytical or business scenarios.

Optionally, you can import the source file without source system to prevent key mapping generation. This is preferred for the mass creation use case.

We also provide a process template that supports automation. This process contains a derivation step in which derivation scenarios are executed.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

|  |
| --- |
| Caution Testing in a 3-System LandscapeIn a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version (see the following [link](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/TestScripts/1N3_S4CLD2602_BPD_EN_XX.docx)). |

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
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure. It is necessary to load a file into the system. Check, if such a file can be provided. It is also possible to start the app Import Master Data, create a new import, and choose Download File Template to use this for an own created file.

#### Download template file

This step is necessary to get a template file for procedure 4.1 (Import Source Data). These template files contain template data and can be replaced by own data.

Procedure

Run step 1 + 2 from procedure [Import Source Data](#unique_7) [page ] 6 and choose the link Download File Templates. Select Example Files to download a compressed file with example files to be used for uploading source data. Use one of these files (for example, BPARTNER.xlsx) for uploading or use them as a template for your own data. Ensure that for all rows the field Source_ID will be filled with data.

Result

A new file for uploading source data has been created.

## Overview Table

The scope item Master Data Consolidation for Business Partner (1N3) consists of several process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Choose the appropriate entity: Process Step, Report or Item | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Import Source Data](#unique_7) [page ] 6 | Master Data Specialist - Business Partner Data | SAP Fiori: Import Master Data (F6553A) | Source Data loaded into source table. |
| [Initial Check](#unique_9) [page ] 7 | Master Data Specialist - Business Partner Data | SAP Fiori: Manage Consolidation Processes (F6556A) | The system provides the result of a check (based on system customizing). |
| [Matching](#unique_10) [page ] 8 | Master Data Specialist - Business Partner Data | SAP Fiori: Manage Consolidation Processes (F6556A) | Match groups with potential duplicates. |
| [Best Record Calculation](#unique_11) [page ] 9 | Master Data Specialist - Business Partner Data | SAP Fiori: Manage Consolidation Processes (F6556A) | Best records based on approved match groups. |
| [Validation](#unique_12) [page ] 9 | Master Data Specialist - Business Partner Data | SAP Fiori: Manage Consolidation Processes (F6556A) | Check the result to determine whether records can be activated in the system (based on system customizing). |
| [Activation](#unique_13) [page ] 10 | Master Data Specialist - Business Partner Data | SAP Fiori: Manage Consolidation Processes (F6556A) | New master data has been created or existing master data has been updated. |
| [Track Mass Changes](#unique_14) [page ] 11 | Master Data Specialist - Business Partner Data | SAP Fiori: Track Changes (F6569A) | Track your changes made during the Consolidation Process. |

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

Import Source Data is needed to upload data into the source tables before you can start a consolidation process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open the Import Master Data (F6553A) app. | The Import Master Data (F6553A) screen displays. |  |
| 3 | Create New Import | Choose Create to create a new import. | The New: Import screen displays. |  |
| 4 | Describe Data Source | Enter the following data:Source System: Enter a source system name, for example, CRM_US.Data Package: Enter a data package (System shows default package name after the file is uploaded. See next step.).Optional: You can import without Source System to prevent Key Mapping generation. Preferred for Mass Creation use case. | System accepts the data and the footer toolbar should show the button Create. |  |
| 5 | Select File | Press Upload to select a file for upload. You can use the example file from chapter [Download template file](#unique_6) [page ] 4. | System transfers the file to the system and shows some progress information. |  |
| 6 | Import | Check the settings and press Create (at the bottom of the screen) to continue. | The system provides some information about the import steps in the import log. |  |
| 7 | Create Consolidation Process | Choose Create Process and enter the following data and choose Create to continue.Description: Enter a description for the consolidation process, for example, Consolidate BP for CRM_US.Process Template: Select an available process template, for example, SAP: Consolidate Business Partner Data. | The system creates a new consolidation process and shows the process UI. |  |

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
| 1 | Start initial check | Choose Start (at the bottom of the screen) to start the check. | The system starts the check and shows a result screen when finished. |  |
| 2 | Check Errors and Warnings | Click the numbers Errors and Warnings to show details. | Message texts are shown. |  |
| 3 | Show Records | Choose Show Results to navigate through the list of the records. | The system shows a list with records. |  |
| 4 | Check the result | Navigate through all related tables of a record using the tab bar.After finishing the review, choose the Back icon. | Lists of all relevant tables are shown. |  |

### Matching

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step will identify duplicates and shows a list of match groups (group of potential duplicates). The user has to review all open groups and has to approve or reject them.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Start matching step | Choose Continue (at the bottom of the screen) to start matching step. | The system starts the matching and shows a result screen when finished. The result shows bars with approved and(or) open match groups. |  |
| 2 | Select open match groups | On the bar chart, choose the bar Open match groups (if existing) and choose Show Details to navigate through the open match groups. | The system shows a list with open match groups. |  |
| 3 | Approve or reject match groups | Go to each open match group and approve or reject it:Choose Approve button at the top of the group to approve.Choose Reject button at the top of the group to reject.After finishing the review, choose on Back icon. | All the match groups that are approved or rejected will disappear from the list of open match groups. |  |

### Best Record Calculation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step merges records for all the approved match groups into one record. This merging is based on a specified rule.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Start Best Record Calculation step | Choose Continue (at the bottom of the screen) to Start Best Record Calculation step. | The system starts the step and shows a result screen when finished. The result shows a pie with different groups of the target records. |  |
| 2 | Show Best Records | Choose Show Results to navigate through the list of best records. | The system shows a list with the best records. |  |
| 3 | Check the result | Navigate through all related tables of a record using the tab bar.After finishing the review, choose the Back icon. | Lists of all relevant tables are shown. |  |

### Validation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Validation provides information about whether the data can be activated. The checks are done based on the system settings. Erroneous data cannot be activated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Start in Validation | Choose Continue (at the bottom of the screen) to start the validation. | The system starts the validation and shows a result screen when finished. |  |
| 2 | Check Errors and Warnings | Click the numbers Errors and Warnings to show details. | Message texts are shown. |  |
| 3 | Show Records | Choose the Show Results to navigate through the list of the records. | The system shows a list with records. |  |
| 4 | Check the result | Navigate through all related tables of a record using the tab bar.After finishing the review, choose the Back icon. | Lists of all relevant tables are shown. |  |

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
| 1 | Start Activation | If no errors were detected during the Validation step, the system continues with the Activation step automatically.Otherwise, choose Continue (at the bottom of the screen) to start the activation. | The system starts the activation and shows a result screen when finished. Note down the process Id. |  |
| 2 | Check Errors and Warnings (optional) | When warnings or errors occurred, the system provides this information. Click the numbers Errors and Warnings to show details. | Message texts are shown. |  |

### Track Mass Changes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Track your changes made during the Consolidation process. You can view the list of changes only when you have made any changes during the consolidation process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access App | Go back to the SAP Fiori launchpad. Open Track Changes - Business Partners (F6569A). | The Track Changes (Business Partners) screen displays. |  |
| 2 | Filter Inputs | Enter the process ID you noted down in Section [Activation](#unique_13) [page ] 10 → Procedure step 1. Click Go. | You should be able to see the list of changes made by you during the Consolidation Process. If there are no changes available then probably you made no changes during the consolidation process. |  |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Import Data for Consolidation (Business Partners). | The Import Data for Consolidation (Business Partners) screen displays. |  |
| 3 | Select File | Press Browse to select a file for upload. You can use the example file from chapter [Download template file](#unique_6) [page ] 4. | The system transfers the file to the system and shows some progress information. |  |
| 4 | Describe Data Source | Enter the following data:Source System: Enter a source system name, for example, CRM_US.Data Package: System shows default Package name.Optional: You can import without Source System to prevent Key Mapping generation. Preferred for Mass Creation use case. | The system accepts the data and the footer toolbar should show the Import button. |  |
| 5 | Import | Check the settings and choose Import (at the bottom of the screen) to continue. | The system goes to the Import Details screen. The system provides some information about the import steps. |  |
| 6 | Create Consolidation Process | Choose on Consolidate and enter the following data and choose Save to continue.Description: Enter a description for the consolidation process.Process Template: Select an available process template for automation, for example, SAP: Consolidate BP Automated. | The system creates a new consolidation process and shows the process UI. |  |
| 7 | Check | On the process UI, the following steps should be displayed:Initial CheckMatchingBest Record CalculationDerivationValidationActivation | The Derivation step is included on the process UI. |  |

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
- related-to :: [[02-business-partner-and-product-master-data/test-script-master-data-consolidation-for-product-1n1-742]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1N3_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 24,513 chars in the whole document
