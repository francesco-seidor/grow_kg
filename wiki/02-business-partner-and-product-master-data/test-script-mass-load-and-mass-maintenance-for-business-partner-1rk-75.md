---
id: 02-business-partner-and-product-master-data/test-script-mass-load-and-mass-maintenance-for-business-partner-1rk-75
title: "Test Script: Mass Load and Mass Maintenance for Business Partner (1RK) (1RK_S4CLD2608_BPD_EN_XX)"
description: "SAP S/4HANA Cloud 1RK test script: Fiori test steps for business partner mass load, BP relationship load, mass maintenance, export and remediation."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/business-partner-mass-load-and-maintenance]
aliases: [1RK_S4CLD2608_BPD_EN_XX]
keywords: [Mass Load and Mass Maintenance for Business Partners, business partner mass load, business partner relationships, business partner mass maintenance, business partner remediation, consolidation process, test scripts, master data export, mass change tracking, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1RK_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-756
topic: 02-business-partner-and-product-master-data/business-partner-mass-load-and-maintenance
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Mass Load and Mass Maintenance for Business Partner (1RK) (1RK_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1RK_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Mass Load and Mass Maintenance for Business Partners** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Mass Load and Mass Maintenance for Business Partner (1RK) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232886272)

[2 Prerequisites 4](#_Toc232886273)

[2.1 System Access 4](#_Toc232886274)

[2.2 Roles 4](#_Toc232886275)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232886276)

[2.3.1 Download template file 5](#_Toc232886277)

[3 Overview Table 6](#_Toc232886278)

[4 Test Procedures 8](#_Toc232886279)

[4.1 Mass Load 8](#_Toc232886280)

[4.1.1 Import Source Data and Create Consolidation Process – Mass Load 8](#_Toc232886281)

[4.1.2 Validation 9](#_Toc232886282)

[4.1.3 Activation 10](#_Toc232886283)

[4.1.4 Manage Consolidation Process – Mass Load 11](#_Toc232886284)

[4.2 Mass Load – Business Partner Relationships 12](#_Toc232886285)

[4.2.1 Import Source Data and Create Consolidation Process – Mass Load Business Partner Relationships 12](#_Toc232886286)

[4.2.2 Validation 13](#_Toc232886287)

[4.2.3 Activation 14](#_Toc232886288)

[4.2.4 Manage Consolidation Process – Mass Load BP Relationships 15](#_Toc232886289)

[4.3 Mass Maintenance 16](#_Toc232886290)

[4.3.1 Scope Definition 16](#_Toc232886291)

[4.3.2 Record Selection 17](#_Toc232886292)

[4.3.3 Editing 18](#_Toc232886293)

[4.3.4 Validation 19](#_Toc232886294)

[4.3.5 Activation 19](#_Toc232886295)

[4.3.6 Track Mass Changes 20](#_Toc232886296)

[4.3.7 Export Active Data (Optional) 21](#_Toc232886297)

[4.4 Remediation 23](#_Toc232886298)

[4.4.1 Start Remediation Process 23](#_Toc232886299)

[4.4.2 Selection 24](#_Toc232886300)

[4.4.3 Validation 24](#_Toc232886301)

[4.4.4 Activation 25](#_Toc232886302)

## Purpose

Overview

Mass load and mass maintenance of business partner data provides capabilities to load and update multiple business partner master data records.

To load records, you import data from file. The system starts the checking, cleansing, validation, and activation processes. To update records, you select the fields and records you want to change. Once you enter your changes, the system provides statistics on the changed fields and validates the data. You check the validated data and activate it for use in business transactions.

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
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure. It is necessary to load a file into the system. Check whether such a file can be provided. It is also possible to start the app Import Data for Consolidation and choose Download File Template to use the file created by you.

#### Download template file

This step is necessary to get a template file for procedure "Import Source Data". These template files contain template data and can be replaced by own data.

Procedure

Run step 1 + 2 from procedure [Import Source Data and Create Consolidation Process – Mass Load](#unique_7) [page ] 8 and choose the link Download File Templates. Select Example Files to download a compressed file with example files to be used for uploading source data. Use one of these files (for example, BPARTNER.xlsx) for uploading or use them as a template for your own data. Ensure that for all rows the field Source_ID is filled with data.

Result

A new file for uploading source data is created.

## Overview Table

This scope item consists of several process steps provided in the following table:

Mass Load

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Import Source Data and Create Consolidation Process – Mass Load](#unique_7) [page ] 8 | Master Data Specialist - Business Partner Data | SAP Fiori: Import Data for Consolidation (Business Partners) | Source Data loaded into source table |
| [Validation](#unique_9) [page ] 9 | Master Data Specialist - Business Partner Data | SAP Fiori: Import Data for Consolidation (Business Partners) | Check the result, if records can be activated in the system (based on system customizing) |
| [Activation](#unique_10) [page ] 10 | Master Data Specialist - Business Partner Data | SAP Fiori: Import Data for Consolidation (Business Partners) | Master data has been updated |
| [Manage Consolidation Process – Mass Load](#unique_11) [page ] 11 | Master Data Specialist - Business Partner Data | SAP Fiori: Manage Consolidation Processes - Business Partners (F6556A) | Created process status can be seen or the process can be deleted. |

Mass Load – BP Relationships

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Import Source Data and Create Consolidation Process – Mass Load Business Partner Relationships](#unique_12) [page ] 12 | Master Data Specialist - Business Partner Data | SAP Fiori: Import Data for Consolidation (BP Relationship) | Source Data loaded into source table |
| [Validation](#unique_13) [page ] 13 | Master Data Specialist - Business Partner Data | SAP Fiori: Import Data for Consolidation (BP Relationship) | Check result, if records can be activated in the system (based on system customizing) |
| [Activation](#unique_14) [page ] 14 | Master Data Specialist - Business Partner Data | SAP Fiori: Import Data for Consolidation (BP Relationship) | Master data has been updated |
| [Manage Consolidation Process – Mass Load BP Relationships](#unique_15) [page ] 15 | Master Data Specialist - Business Partner Data | SAP Fiori: Manage Consolidation Process – Mass Load BP Relationships | Created process status can be seen or the process can be deleted. |

Mass Maintenance

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Scope Definition](#unique_16) [page ] 16 | Master Data Specialist - Business Partner Data | SAP Fiori: Start Mass Maintenance (Business Partners) | The scope with all fields which should be changed has been defined. |
| [Record Selection](#unique_17) [page ] 17 | Master Data Specialist - Business Partner Data | SAP Fiori: Start Mass Maintenance (Business Partners) | Records which can be changed are available |
| [Editing](#unique_18) [page ] 18 | Master Data Specialist - Business Partner Data | SAP Fiori: Start Mass Maintenance (Business Partners) | Changed have been applied and are ready for validation |
| [Validation](#unique_19) [page ] 19 | Master Data Specialist - Business Partner Data | SAP Fiori: Start Mass Maintenance (Business Partners) | Check the result, if records can be activated in the system (based on system customizing) |
| [Activation](#unique_20) [page ] 19 | Master Data Specialist - Business Partner Data | SAP Fiori: Start Mass Maintenance (Business Partners) | Master data has been updated |
| [Export Active Data (Optional)](#unique_21) [page ] 21 | Master Data Specialist - Business Partner Data | SAP Fiori: Export Master Data (Business Partners) | Active data is downloaded into an Excel file. |
| [Track Mass Changes](#unique_22) [page ] 20 | Master Data Specialist - Business Partner Data | SAP Fiori: Track Mass Changes (Business Partners) | Track your changes made during the Mass Maintenance process. |

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

Import Source Data is required to uploaded data into the source tables before you start a consolidation process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori Launchpad displays. |  |
| 2 | Access App | Open Import Data for Consolidation - Business Partner Master under the tile group Mass Load for Business Partner Master | The Import Data for Consolidation – Business Partners screen displays. |  |
| 3 | Select File | Choose browse to select a file for upload. You can use the example file from [Download template file](#unique_6) [page ] 5.Make sure you maintain at least two Business Partners (One as organization and other as Person). | System transfers the file to the system and shows some progress information. |  |
| 4. | Create Data Import | Source System: Input any source system name. For example: SOURCE01Data Package: Default is the file name. Enter the required data package name.Import settings: Choose Skip and continue.choose Import.Optional: You can import without Source system to prevent Key Mapping generation. Preferred for Mass Creation use case. | Data is imported and the status of the imported data can be seen.If you get an error, please change the value in the field Source System. This means someone else has already imported the same data using the same source system. |  |
| 5 | Create Consolidation Process | Choose Consolidate in the top right corner after importing the source data. | Create Consolidation BP Mass Load Page appears. |  |
| 6 | Enter Description | Check the description and adapt it to your needs, if necessary. Check the process template. Use SAP: Load Business Partner Data.Choose Save. | Consolidation process page appears. |  |

#### Validation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

Validation provides an information, if the data can be activated data. The checks are done based on the system settings. Erroneous data cannot be activated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Start Validation | Choose Start and start validation. | The system starts the validation and shows a result screen when finished. |  |
| 2 | Check Errors and Warnings | Choose Errors and Warnings to show details. | Message texts are shown. |  |
| 3 | Show Records | Choose Show Result to navigate through the list of records. | The system shows a list with records. |  |
| 4 | Check the result | Navigate through all the related tables of a record using the tab bar.After finishing the review, choose Back. | Lists of all relevant tables will be shown. |  |

#### Activation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

Activation step will trigger the activation of the data into the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Start Activation | Choose Continue (at the bottom of the screen) to start the activation. | The system starts the activation and shows a result screen when finished. |  |
| 2 | Check Errors and Warnings | Choose Errors and Warnings to show details. | Message texts are shown. |  |

#### Manage Consolidation Process – Mass Load

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
| 1 | Log On | Log on to the SAP Fiori Launchpad as Master Data Specialist - Business Partner Data. | The SAP Fiori Launchpad displays. |  |
| 2 | Access App | Open Manage Consolidation Processes - Business Partners (F6556A)app under the tile group Mass Load for Business Partner Master. | The Manage Consolidation Process – Mass Load Business Partners screen displays. |  |
| 3 | Processes | Check for the status of all the consolidation process you created. Check parameters like Data source user creation date number of records , and so on. | Status can be seen. |  |

### Mass Load – Business Partner Relationships

Preparation Step: Create Active Business Partners.

In order to load a Business Partner relationship file you need to have active Business Partner in the system. So as a preparation, first you will need to create active Business Partners in the system.

1. Start the app ‘Maintain Business Partner’ under ‘Business Partner’ tile group.
2. Create multiple business partner organizations and persons. In the execution part of the test case you will create relationships between these partners. Maintain general and address data.
3. Save business partners and note down the BP ID’s

Preparation Step: Adapt your BP relationship file.

From section 2.3.1 you can download the file template for BP Relationships. For the mass creation use case you can use the example file BPREL_Mass_Create.xlsx. Adapt your file by replacing the Key values from your Active Business Partners. By doing this you have a file which defines the relationship data for your active Business Partners.

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
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Business Partner Data for Business Partner Data. | The SAP Fiori Launchpad displays. |  |
| 2 | Access App | Open Import Data for Consolidation - BP Relationships under the tile group Mass Load for Business Partner Master | The Import Data for Consolidation-Business Partner Relationships screen displays. |  |
| 3 | Select File | Choose browse to select a file for upload. You can use the example file from Download template file [page ] 4.Make sure you maintain at least two Business Partners (One as organization and other as Person). | System transfers the file to the system and shows some progress information. |  |
| 4. | Create Data Import | Source System: Input any source system name. For example: SOURCE01Data Package: Default is the file name. Enter the required data package name.Import settings: Choose Skip and continue.choose Import.Optional: You can import without Source system to prevent Key Mapping generation. You have to select this option, if you want to create relationships to already existing business partners. | Data is imported and the status of the imported data can be seen.If you get an error, please change the value in the field Source System. This means someone else has already imported the same data using the same source system. |  |
| 5 | Create Consolidation Process | Choose Consolidate on top right corner after importing the source data. | Create Consolidation BP Relationships Mass Load Page appears. |  |
| 6 | Enter Description | Check the description and adapt it to your needs, if necessary. Check the process template. Use SAP: Load BP relationships.Choose Save. | Consolidation process page appears. |  |

#### Validation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

Validation provides an information, if the data can be activated data. The checks are done based on the system settings. Erroneous data cannot be activated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Start Validation | Choose Start and start validation. | The system starts the validation and shows a result screen when finished. |  |
| 2 | Check Errors and Warnings | Choose Errors and Warnings to show details. | Message texts are shown. |  |
| 3 | Show Records | Choose Show Result to navigate through the list of records. | The system shows a list with records. |  |
| 4 | Check the result | Navigate through all the related tables of a record using the tab bar.After finishing the review, choose Back. | Lists of all relevant tables will be shown. |  |

#### Activation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

Activation step will trigger the activation of the data into the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Start Activation | Choose Continue (at the bottom of the screen) to start the activation. | The system starts the activation and shows a result screen when finished. |  |
| 2 | Check Errors and Warnings | Choose Errors and Warnings to show details. | Message texts are shown. |  |

#### Manage Consolidation Process – Mass Load BP Relationships

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
| 1 | Log On | Log on to the SAP Fiori Launchpad as Master Data Specialist - Business Partner Data for Business Partner Data. | The SAP Fiori Launchpad displays. |  |
| 2 | Access App | Open Manage Consolidation Process - Mass Load BP Relationships app under the tile group Mass Load for Business Partner Master. | The Manage Consolidation Process - Mass Load BP Relationships screen displays. |  |
| 3 | Processes | Check for the status of all the consolidation process you created. Check parameters like Data source user creation date number of records , and so on. | Status can be seen. |  |

### Mass Maintenance

#### Scope Definition

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
| 1 | Log On | Log on to the SAP Fiori Launchpad as Master Data Specialist - Business Partner Data, . | The SAP Fiori Launchpad displays. |  |
| 2 | Access App | Open Start Mass Maintenance (Business Partners) | The Start Mass Maintenance (Business Partners) screen displays. |  |
| 3 | Enter Description | Check the description and adapt it to your needs, if necessary. Choose save and start the process.Import file is optional and you can use the file which you Export using [Export Active Data (Optional)](#unique_21) [page ] 21 app. |  |  |
| 4 | Add fields to be changed (scope fields) | Use F4-help to search for fields by field description and add one or more fields to the scope list. | List of scope fields are defined. |  |

#### Record Selection

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In Record Selection, all records that can be changed can be selected by different select criteria.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Start Selection | Choose Continue (on the bottom of the screen) to start the check. | Selection screen appears. |  |
| 2 | Define Includes and Excludes | Define select types and field values to find the range of records to be changed. You must use only criteria, which finds the existing Business Partner numbers in the system. | List of criteria |  |

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
| 1 | Start Edit step | Choose Start to start the Edit step. Choose Edit Records to start with editing. | The system shows the number of entries for the relevant tables. |  |
| 2 | Select table for the changes | Select the relevant table from the tab bar. | The system shows the current values of the record in this table. |  |
| 3 | Select records for mass change | Select some or all of the records to change the same field values by selecting the checklist on the left side of the table. | Records are selected. The buttons for Replace Values and Clear Fields are activated. |  |
| 4 | Mass Change of values | Choose Replace Values and input the target value in all the fields that must be changed.Choose Replace to apply these changes. | Applied field values appears in the table. |  |
| 5 | Single changes of values | Directly enter the new field values for each field. | Field values applied immediately. |  |
| 6 | Check number of changes | Choose Back.The system checks the number of changed rows. | Bar Chart with changes appears.. |  |

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
| 1 | Start Validation | Choose Continue (at the bottom of the screen) to start the validation. | The system starts the validation and shows a result screen when finished. |  |
| 2 | Check Errors and Warnings | Choose the numbers Errors and Warnings to show details. | Message texts are shown. |  |
| 3 | Show Records | Choose Show Result to navigate to the list of the records. | The system shows a list with records. |  |
| 4 | Check the result | Navigate through all related tables of a record using the tab bar.After finishing the review, choose Back. | Lists of all relevant tables are shown. |  |

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
| 1 | Start Activation | Choose Continue (at the bottom of the screen) to start the activation. | The system starts the activation and shows a result screen when finished. |  |
| 2 | Check Errors and Warnings | Choose Errors and Warnings to show details. | Message texts are shown. |  |

#### Track Mass Changes

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
| 1 | Access App | Go back to the home page of Fiori Launchpad. Open Track Mass Changes (Business Partners). | The Track Mass Changes (Business Partners) screen displays. |  |
| 2 | Filter Inputs | Enter the process ID that you noted down in [Activation](#unique_20) [page ] 19 Procedure step 1. Choose Go | You must be able to see the list of changes made by you during the Consolidation Process. If no changes are available, then you made no changes during the Mass Maintenance process. |  |

#### Export Active Data (Optional)

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
| 1 | Log On | Log on to the SAP Fiori Launchpad as Master Data Specialist - Business Partner Data for Business Partner Data. | The SAP Fiori Launchpad displays. |  |
| 2 | Access App | Open Export Master Data (Business Partners) | The Export Master Data (Business Partners) screen displays. |  |
| 3 | Define Scope | Select one or more fields from different tables by using F4 help or ‘Type Ahead’ functionality and then choose Ok. Or do the following step by Marking the radio button to choose all the fields from all tables. | The selected attributes appear under Fields.Use X for removal of the fields if needed. |  |
| 4 | Select Attributes | Mark the checkbox Select all fields from all tables. |  |  |
| 5 | Select Business Partners | Select the Business partners that you created. Try with different attributes using Include or Exclude functionality. |  |  |
| 6 | Use selection filter | Optional Step - Select the checkbox, Use selection criteria as filter to export the records which are defined in the selection criteria. For example, when your BP has several addresses, and you want to export the BP of a specific address then use this checkbox. Provided you have defined the address as your selection criteria. This checkbox works for all the attributes specific to Business partners. |  |  |
| 7 | Choose Export | Export can be made as either Office Open XML (*.xlsx) or a Com-pressed CSV (*.zip).After all the selections are made, choose Export on bottom right. | Confirmation pop-up appears saying how many business partners will be exported. | Preferred to export it as Zip when huge data is involved. |
| 8 | Save File | Choose Export on the Confirmation Dialog Box. | Information popup should appear saying File is being Generated. choose ok and save the file to your local. |  |
| 9 | Verify and Make changes in the file | Open file and verify the data and make changes.Change some attributes in the excel file.Save your changes. | Selected business partners with the tables and attributes defined in scope are exported.Necessary key fields are available. |  |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as Master Data Specialist for Business Partner Data . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open the app Manage Remediation Processes for Business Partners. | The Manage Remediation Processes app opens. |  |
| 3 | Create Process | Select Create Process. | The page to start the remediation process for Business Partners is displayed. |  |
| 4 | Select Process Template | Enter a description for the process.Select the process template SAP: Validate and Remediate BP | The process template SAP: Validate and Remediate BP is offered and selected for the process. |  |
| 5 | Save | Choose Save at the bottom of the screen to save the new process. | The new process is confirmed with the message "A new process is being created", and the Data Quality Remediation page is displayed. |  |

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
| 1 | Define Selection Criteria | Select the Business Partners to be validated by entering include or exclude criteria. |  |  |

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
| 1 | Validation | Choose Start at the bottom of the screen to start the validation. | The validation of the selected business partners is started. |  |
| 2 | Check Validation Result | When the process has stopped for the review of the validation, the number of errors and warnings is displayed. In addition, there is a graphical representation of the validation status.To check the validation results in detail, choose Show Result in the graphical view. | Navigate to the Validation: Result page. |  |
| 3 | Change Business Partners | To change data, select the table for which you want to change data, for example, Basic Data. Select the records and choose Replace Values.In the pop-up window, enter the new values for the selected records. Choose Replace.Note: In the Overview, data cannot be changed. | In the Changes column, the number of changes is displayed. Clicking the number displays the changed fields with the new and the old values. |  |
| 4 | Navigate Back | Choose the back arrow to navigate back to the remediation process page. |  |  |

#### Activation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The activation step triggers the activation of the data in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Activation | Choose Continue at the bottom of the screen. In the pop-up warning message, choose Continue.Note: If no record was changed, there will be no pop-up window. | The system starts the activation and shows the activation result when finished. |  |

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
- related-to :: [[02-business-partner-and-product-master-data/mass-load-and-mass-maintenance-for-business-partners-7mi-test-script-1]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1RK_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 39,908 chars in the whole document
