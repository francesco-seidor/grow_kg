---
id: 02-business-partner-and-product-master-data/mass-load-and-mass-maintenance-for-business-partners-7mi-test-script-1
title: Mass Load and Mass Maintenance for Business Partners (7MI) - Test Script (7MI_S4CLD2608_BPD_EN_XX)
description: "SAP S/4HANA Cloud Public Edition test script, scope item 7MI: business partner mass load, relationship load, mass maintenance, export, tracking, remediation."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/business-partner-mass-load-and-maintenance]
aliases: [7MI_S4CLD2608_BPD_EN_XX]
keywords: [Mass Load and Mass Maintenance for Business Partners, business partner mass load, business partner relationships, mass maintenance, data remediation, scope item testing, validation and activation, master data export, change tracking, consolidation processes]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7MI_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1220
topic: 02-business-partner-and-product-master-data/business-partner-mass-load-and-maintenance
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Mass Load and Mass Maintenance for Business Partners (7MI) - Test Script (7MI_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7MI_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Mass Load and Mass Maintenance for Business Partners** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Mass Load and Mass Maintenance for Business Partners (7MI)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Mass Load and Mass Maintenance for Business Partners (7MI) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232828369)

[2 Prerequisites 4](#_Toc232828370)

[2.1 System Access 4](#_Toc232828371)

[2.2 Roles 4](#_Toc232828372)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232828373)

[2.3.1 Download template file 5](#_Toc232828374)

[3 Overview Table 6](#_Toc232828375)

[4 Test Procedures 8](#_Toc232828376)

[4.1 Mass Load 8](#_Toc232828377)

[4.1.1 Import Source Data and Create Consolidation Process – Mass Load 8](#_Toc232828378)

[4.1.2 Validation 9](#_Toc232828379)

[4.1.3 Activation 10](#_Toc232828380)

[4.1.4 Manage Consolidation Processes – Mass Load 10](#_Toc232828381)

[4.2 Mass Load – Business Partner Relationships 11](#_Toc232828382)

[4.2.1 Import Source Data and Create Consolidation Process – Mass Load Business Partner Relationships 12](#_Toc232828383)

[4.2.2 Validation 13](#_Toc232828384)

[4.2.3 Activation 14](#_Toc232828385)

[4.2.4 Manage Mass Creation Processes – BP Relationships 14](#_Toc232828386)

[4.3 Mass Maintenance 15](#_Toc232828387)

[4.3.1 Create Process 15](#_Toc232828388)

[4.3.2 Record Selection 16](#_Toc232828389)

[4.3.3 Editing 17](#_Toc232828390)

[4.3.4 Remove Unchanged Data 18](#_Toc232828391)

[4.3.5 Validation 18](#_Toc232828392)

[4.3.6 Activation 19](#_Toc232828393)

[4.3.7 Track Changes 20](#_Toc232828394)

[4.3.8 Export Master Data (Optional) 21](#_Toc232828395)

[4.4 Remediation 22](#_Toc232828396)

[4.4.1 Start Remediation Process 22](#_Toc232828397)

[4.4.2 Selection 23](#_Toc232828398)

[4.4.3 Validation 24](#_Toc232828399)

[4.4.4 Activation 25](#_Toc232828400)

## Purpose

Overview

Mass Load and Mass Maintenance of business partner data provides capabilities to load and update multiple business partner master data records simultaneously.

To load records, you import data from a file. The system starts the checking, cleansing, validation, and activation processes.

To update records, you select the fields and records you want to change. Once you enter your changes, the system provides statistics on the changed fields and validates the data. You check the validated data and activate it for use in business transactions.

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

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Business Partner Governance | SAP_CA_SPT_MDG_BP_GOV_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure. It is necessary to load a file into the system. Check whether such a file can be provided. It is also possible to start the app Import Master Data - BP Hierarchies (F7487A) and choose Download File Templates to use this to create your own file.

#### Download template file

This step is necessary to get a template file for the procedure "Import Source Data". These template files contain template data and can be replaced by your own data.

Procedure

Run step 1 + 2 from procedure [Import Source Data and Create Consolidation Process – Mass Load](#unique_7) [page ] 8 and choose the link Download File Templates. Select Example Files to download a compressed file with example files to be used for uploading source data. Use one of these files (for example - BP_Org_Simple.xlsx) for uploading or use them as a template for your own data. Ensure that for all rows the field Source_ID is filled with data.

Result

A new file for uploading source data is created.

## Overview Table

This scope item consists of several process steps provided in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Mass Load

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Import Source Data and Create Consolidation Process – Mass Load](#unique_7) [page ] 8 | Master Data Specialist - Business Partner Data | SAP Fiori: Import Master Data (Business Partners) | Source Data loaded into source table |
| [Validation](#unique_9) [page ] 9 | Master Data Specialist - Business Partner Data | SAP Fiori: Import Master Data (Business Partners) | Check the result to determine whether records can be activated in the system (based on system customizing) |
| [Activation](#unique_10) [page ] 10 | Master Data Specialist - Business Partner Data | SAP Fiori: Import Master Data (Business Partners) | Master data has been updated |
| [Manage Consolidation Processes – Mass Load](#unique_11) [page ] 10 | Master Data Specialist - Business Partner Data | SAP Fiori: Manage Consolidation Processes (Business Partners) | Created process status can be seen or the process can be deleted. |

Mass Load – BP Relationships

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Import Source Data and Create Consolidation Process – Mass Load Business Partner Relationships](#unique_12) [page ] 12 | Master Data Specialist - Business Partner Data | SAP Fiori: Import Master Data (BP Relationships) | Source Data loaded into source table |
| [Validation](#unique_9) [page ] 9 | Master Data Specialist - Business Partner Data | SAP Fiori: Import Master Data (BP Relationships) | Check the result to determine whether records can be activated in the system (based on system customizing) |
| [Activation](#unique_10) [page ] 10 | Master Data Specialist - Business Partner Data | SAP Fiori: Import Master Data (BP Relationships) | Master data has been updated |
| [Manage Mass Creation Processes – BP Relationships](#unique_13) [page ] 14 | Master Data Specialist - Business Partner Data | SAP Fiori: Manage Mass Creation Processes (BP Relationships) | Created process status can be seen or the process can be deleted. |

Mass Maintenance

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Process](#unique_14) [page ] 15 | Master Data Specialist - Business Partner Data | SAP Fiori: Manage Mass Maintenance Processes (Business Partners) | The creation of a new mass maintenance process is initiated. |
| [Record Selection](#unique_15) [page ] 16 | Master Data Specialist - Business Partner Data | SAP Fiori: Manage Mass Maintenance Processes (Business Partners) | Records which can be changed are available |
| [Editing](#unique_16) [page ] 17 | Master Data Specialist - Business Partner Data | SAP Fiori: Manage Mass Maintenance Processes (Business Partners) | Changes have been applied and are ready for validation |
| [Validation](#unique_17) [page ] 18 | Master Data Specialist - Business Partner Data | SAP Fiori: Manage Mass Maintenance Processes (Business Partners) | Check the result to determine whether records can be activated in the system (based on system customizing) |
| [Activation](#unique_10) [page ] 10 | Master Data Specialist - Business Partner Data | SAP Fiori: Manage Mass Maintenance Processes (Business Partners) | Master data has been updated |
| [Export Master Data (Optional)](#unique_18) [page ] 21 | Master Data Specialist - Business Partner Data | SAP Fiori: Export Master Data (Business Partners) | Active data is downloaded into an Excel file. |
| [Track Changes](#unique_19) [page ] 20 | Master Data Specialist - Business Partner Data | SAP Fiori: Track Changes (Business Partners) | Track your changes made during the Mass Maintenance Process. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Mass Load

#### Import Source Data and Create Consolidation Process – Mass Load

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Import Source Data is required to upload data into the source tables before you start a consolidation process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
|  | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist for Business Partner Data. | The SAP Fiori Launchpad displays. |  |
|  | Access App | Open Import Master Data - Business Partners (F6553A) under the tile group Mass Load for Business Partner Master | The Import Master Data–Business Partners screen displays. |  |
|  | Create Data Import | Choose Create to create a new import.Source System: Input any source system name. For example: SOURCE01Data Package: Enter the required data package name.Choose ‘Upload’ to select a file for upload. You can use the example file from [Download template file](#unique_6) [page ] 5.Make sure you maintain at least two business partners (one as organization and other as person).Choose Create.Optional: You can import without source system to prevent key mapping generation. Preferred for mass creation use case. | Data is imported and the status of the imported data can be seen.If you get an error, change the value in the field Source System. This error means that someone else has already imported the same data using the same source system. |  |
|  | Create Consolidation Process | Choose Create Process in the top-right corner after importing the source data. | Create Process dialog appears. |  |
|  | Enter Description | Enter process description if necessary. Check the process template. Use SAP: Mass Creation BP.Choose Create. | Consolidation process page appears. |  |

#### Validation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

Validation provides information about whether the data can be activated. The checks are done based on the system settings. Erroneous data cannot be activated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
|  | Start Initial Check | Choose Start and start the initial check. | The system starts the initial check and shows a result screen when finished. |  |
|  | Check Errors and Warnings | Choose Errors and Warnings under Step Messages to show details. | Message texts are shown. |  |
|  | Show Records | Choose Show Result to navigate through the list of records. | The system shows a list with records. |  |
|  | Check the result | Navigate through all the related tables of a record using the tab bar.After finishing the review, choose Back. | Lists of all relevant tables are shown. |  |

#### Activation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

The activation step triggers the activation of the data into the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
|  | Start Activation | Choose Continue (at the bottom of the screen) to start the activation. | The system starts the activation and shows a result screen when finished. |  |
|  | Check Errors and Warnings | Choose Errors and Warnings to under Step Messages show details. | Message texts are shown. |  |

#### Manage Consolidation Processes – Mass Load

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

You can list all processes.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
|  | Log On | Log on to the SAP Fiori Launchpad as Master Data Specialist - Business Partner Data | The SAP Fiori Launchpad displays. |  |
|  | Access App | Open Manage Consolidation Processes (Business Partners) app under the tile group Mass Load for Business Partner Master. | The Manage Consolidation Processes (Business Partners) screen displays. |  |
|  | Processes | Check for the status of all the consolidation process you created. Check parameters like Data Source, Created By, Created On, Number of Records , and so on. | The status can be seen. |  |

### Mass Load – Business Partner Relationships

Preparation Step: Create Active Business Partners.

To load a Business Partner relationship file, you need to have an active Business Partner in the system. As preparation, you therefore first need to create active Business Partners in the system.

1. Start the app ‘Maintain Business Partner’ under ‘Business Partner’ tile group.
2. Create multiple business partner organizations and persons. In the execution part of the test case, you create relationships between these partners. Maintain general and address data.
3. Save business partners and note down the BP ID’s

Preparation Step: Adapt your BP relationship file.

From section 2.3.1, you can download the file template for BP Relationships. For the mass creation use case, you can use the example file BPREL_Mass_Create.xlsx. Adapt your file by replacing the Key values from your Active Business Partners. Doing so gives you a file that defines the relationship data for your active Business Partners.

#### Import Source Data and Create Consolidation Process – Mass Load Business Partner Relationships

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Import Source Data is required to upload data into the source tables before you start a load process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comments |
| --- | --- | --- | --- | --- |
|  | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Business Partner Data for Business Partner Data. | The SAP Fiori Launchpad displays. |  |
|  | Access App | Open Import Master Data - BP Relationships (F6552A) under the tile group Mass Load for Business Partner Master | The Import Master Data-Business Partner Relationships screen displays. |  |
|  | Create Data Import | Choose Create to create a new import.Source System: Input any source system name. For example: SOURCE01Data Package: Enter the required data package name.Choose ‘Upload’ to select a file for upload. You can use the example file from [Download template file](#unique_6) [page ] 5.Make sure you maintain at least two business partners (one as organization and other as person).Choose Create.Optional: You can import without source system to prevent key mapping generation. You have to select this option if you want to create relationships to already existing business partners | Data is imported and the status of the imported data can be seen.If you get an error, change the value in the field Source System. This means someone else has already imported the same data using the same source system. |  |
|  | Create Mass Creation Process | Choose Create Process in the top-right corner after importing the source data. | Create Process dialog appears. |  |
|  | Enter Description | Enter a process description if necessary. Check the process template. Use SAP: Mass Creation Business Partner Data.Choose Create. | Consolidation process page appears. |  |

#### Validation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

Validation provides information about whether the data can be activated. The checks are done based on the system settings. Erroneous data cannot be activated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
|  | Start Initial Check | Choose Start and start the initial check. | The system starts the initial check and shows a result screen when finished. |  |
|  | Check Errors and Warnings | Choose Errors and Warnings under Step Messages to show details. | Message texts are shown. |  |
|  | Show Records | Choose Show Result to navigate through the list of records. | The system shows a list with records. |  |
|  | Check the result | Navigate through all the related tables of a record using the tab bar.After finishing the review, choose Back. | Lists of all relevant tables are shown. |  |

#### Activation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

The activation step triggers the activation of the data into the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
|  | Start Activation | Choose Continue (at the bottom of the screen) to start the activation. | The system starts the activation and shows a result screen when finished. |  |
|  | Check Errors and Warnings | Choose Errors and Warnings to under Step Messages show details. | Message texts are shown. |  |

#### Manage Mass Creation Processes – BP Relationships

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

You can list all processes.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
|  | Log On | Log on to the SAP Fiori Launchpad as Master Data Specialist - Business Partner Data for Business Partner Data. | The SAP Fiori Launchpad displays. |  |
|  | Access App | Open Manage Mass Creation Processes BP Relationships app under the tile group Mass Load for Business Partner Master. | The Manage Mass Creation Processes - BP Relationships screen displays. |  |
|  | Processes | Check for the status of all the consolidation process you created. Check parameters like the following: Data Source, Created By, Created On, Number of Records, and so on. | The status can be seen. |  |

### Mass Maintenance

#### Create Process

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

Scope definition is the first step in mass maintenance to define the fields to be changed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
|  | Log On | Log on to the SAP Fiori Launchpad as Master Data Specialist - Business Partner Data for Business Partner Data. | The SAP Fiori Launchpad displays. |  |
|  | Access App | Open the Manage Mass Maintenance - Business Partners (F7974) app | The Manage Mass Maintenance (Business Partners) screen displays. |  |
|  | Create Process | Choose Create to create a new mass maintenance process. Enter a description if necessary.Import of records is optional and you can use the file which you exported using the [Export Master Data (Optional)](#unique_18) [page ] 21 app. |  |  |

#### Record Selection

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In Selection, all records that can be changed can be selected by different select criteria.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Define Selection Criteria | Define select types and field values to find the range of records to be changed. You must use only criteria that find the existing business partners in the system.Choose Start to create the process | List of criteria |  |

#### Editing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

This process step provides the list of potential records to be changed and the user can define the new field values.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
|  | Navigate to Mass Edit UI | Choose Edit Records to start with editing. | The system shows the number of entries in the relevant tables. |  |
|  | Select table for the changes | Select the relevant table from the tab bar. | The system shows the current values of the record in this table. |  |
|  | Select records for mass change | Select some or of the records to change the same field values by selecting the checklist on the left side of the table and choose Mass Edit - Selected Records. If you want to edit all the records in the respective table, choose Mass Edit - All Records | Records are selected. Mass Edit dialog opens. |  |
|  | Mass Change of values | For the fields you want to change, choose one of the options from the dropdown menu: <Keep Values>, <Enter New Value>, or <Clear Values>. For ‘New Value’, enter the target value. Choose Save to apply the changes. | Applied field values appear in the table. |  |
|  | Single changes of values | Choose Edit and directly enter the new field values for each field. Choose Save to apply the changes. | Field values applied immediately. |  |
|  | Check number of changes | Choose Back.The system checks the number of changed rows. | A Bar Chart with changes appears. |  |

#### Remove Unchanged Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In the process step ‘Remove Unchanged Data’ the records which have not been changed in the previous step are removed from the process to improve performance during subsequent validation and activation steps. This process step is executed automatically and does not require any user interaction.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Start Remove Unchanged Data | Choose Continue (on the bottom of the screen) to start removing unchanged data validation. | The system executes the process step and continues automatically with validation. |  |

#### Validation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The validation step provides checks to verify whether the data can be activated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
|  | Validation | Choose Start at the bottom of the screen to start the validation. | The validation of the selected business partners is started. |  |
|  | Check Validation Result | When the process has stopped for the review of the validation, the number of errors and warnings is displayed. In addition, there is a graphical representation of the validation status.To check the validation results in detail, choose Show Results in the graphical view. | Navigate to the Validation: Result page. |  |
|  | Mass Change of values | For the fields you want to change, choose one of the options from the dropdown menu: <Keep Values>, <Enter New Value> or <Clear Values>. For ‘New Value’, enter the target value. Choose Save to apply the changes. | Applied field values appear in the table. | 4 |
|  | Single changes of values | Choose Edit and directly enter the new field values for each field. Choose Save to apply the changes. | Field values applied immediately. | 5 |
|  | Navigate Back | Choose the back arrow to navigate back to the remediation process page. |  |  |

#### Activation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

The activation step triggers the activation of the data into the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
|  | Start Activation | Choose Continue (at the bottom of the screen) to start the activation. | The system starts the activation and shows a result screen when finished. |  |
|  | Check Errors and Warnings | Choose Errors and Warnings to under Step Messages show details. | Message texts are shown. |  |

#### Track Changes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Track your changes made during the Mass Maintenance process. You can view the list of changes only if you have made the changes during the Mass Maintenance process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
|  | Access App | Go back to the home page of the SAP Fiori launchpad. Open Track Changes (Business Partners). | The Track Changes (Business Partners) screen displays. |  |
|  | Filter Inputs | Enter your process Id and choose Go | You must be able to see the list of changes made during the mass maintenance process |  |

#### Export Master Data (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

Active data can be downloaded into a spreadsheet file before importing it. Exported file can be used in Mass Maintenance

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
|  | Log On | Log on to the SAP Fiori Launchpad as Master Data Specialist - Business Partner Data for Business Partner Data. | The SAP Fiori Launchpad displays. |  |
|  | Access App | Open Export Master Data (Business Partners) | The Export Master Data (Business Partners) screen displays. |  |
|  | Define Scope | Select one or more fields from different tables by using F4 help or ‘Type Ahead’ functionality and then choose Ok. Or do the following step by Marking the radio button to choose all the fields from all tables. | The selected attributes appear under Fields.Use X for removal of the fields if needed. |  |
|  | Select Attributes | Mark the checkbox Select all fields from all tables. |  |  |
|  | Select Business Partners | Select the Business partners that you created. Try with different attributes using the Include or Exclude functionality. |  |  |
|  | Use selection filter | Optional Step - Select the checkbox, Use selection criteria as filter to export the records which are defined in the selection criteria. For example, when your BP has several addresses, and you want to export the BP of a specific address then use this checkbox. Provided you have defined the address as your selection criteria. This checkbox works for all the attributes specific to Business partners. |  |  |
|  | Choose Export | Export can be made as either Office Open XML (*.xlsx) or a compressed CSV (*.zip).After all the selections are made, choose Export on bottom right. | A confirmation popup appears showing how many business partners are exported. | Preferred to export it as Zip when huge data is involved. |
|  | Save File | Choose Export on the Confirmation Dialog Box. | An information popup should appear indicating that the file is being generated. Choose ok and save the file to your local. |  |
|  | Verify and Make changes in the file | Open the file and verify the data and make changes.Change some attributes in the excel file.Save your changes. | Selected business partners with the tables and attributes defined in scope are exported.Necessary key fields are available. |  |

### Remediation

#### Start Remediation Process

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Create the remediation process by assigning a process name and a corresponding process template.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
|  | Log On | Log on to the SAP Fiori launchpad as Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad is displayed. |  |
|  | Access the SAP Fiori App | Open the app Manage Remediation Processes (F8327). | The Manage Remediation Processes (F8327) app opens. |  |
|  | Create Process | Choose Create to create a new process. Enter a description if necessary. |  |  |
|  | Select Process Template | Select the process template SAP: Validate and Remediate BP | The process template SAP: Validate and Remediate BP is offered and selected for the process. |  |

#### Selection

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Start the remediation process with the selection of your Business Partners.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Define Selection Criteria | Select the Business Partners to be validated by entering selection criteria.Define select types and field values to find the range of records to be changed. You must use only criteria that find the existing business partners in the system. |  |  |
| 2. | Start | Choose Start to create the process. | The Data Quality Remediation page is displayed. |  |

#### Validation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The validation step provides checks to verify whether the data can be activated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
|  | Validation | Choose Start at the bottom of the screen to start the validation. | The validation of the selected business partners is started. |  |
|  | Check Validation Result | When the process has stopped for the review of the validation, the number of errors and warnings is displayed. In addition, there is a graphical representation of the validation status.To check the validation results in detail, choose Show Results in the graphical view. | Navigate to the Validation: Result page. |  |
|  | Mass Change of values | For the fields you want to change, choose one of the options from the dropdown menu: <Keep Values>, <Enter New Value> or <Clear Values>. For ‘New Value’, enter the target value. Choose Save to apply the changes. | Applied field values appear in the table. | 4 |
|  | Single changes of values | Choose Edit and directly enter the new field values for each field. Choose Save to apply the changes. | Field values applied immediately. | 5 |
|  | Navigate Back | Choose the back arrow to navigate back to the remediation process page. |  |  |

#### Activation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

The activation step triggers the activation of the data into the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
|  | Start Activation | Choose Continue (at the bottom of the screen) to start the activation. | The system starts the activation and shows a result screen when finished. |  |
|  | Check Errors and Warnings | Choose Errors and Warnings to under Step Messages show details. | Message texts are shown. |  |

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
- related-to :: [[02-business-partner-and-product-master-data/test-script-mass-load-and-mass-maintenance-for-business-partner-1rk-75]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7MI_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 41,167 chars in the whole document
