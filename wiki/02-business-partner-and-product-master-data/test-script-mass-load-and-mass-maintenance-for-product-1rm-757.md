---
id: 02-business-partner-and-product-master-data/test-script-mass-load-and-mass-maintenance-for-product-1rm-757
title: "Test Script: Mass Load and Mass Maintenance for Product (1RM) (1RM_S4CLD2608_BPD_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 1RM: mass load, mass maintenance, export and remediation of Product master data via Fiori apps."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/product-mass-load-and-maintenance]
aliases: [1RM_S4CLD2608_BPD_EN_XX]
keywords: [Mass Load and Mass Maintenance for Products, product mass load, product mass maintenance, product data remediation, product data export, consolidation process, validation and activation, track changes, business roles, feature activation]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1RM_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-757
topic: 02-business-partner-and-product-master-data/product-mass-load-and-maintenance
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Mass Load and Mass Maintenance for Product (1RM) (1RM_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1RM_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Mass Load and Mass Maintenance for Products** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Mass Load and Mass Maintenance for Product (1RM) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232883964)

[2 Prerequisites 4](#_Toc232883965)

[2.1 System Access 4](#_Toc232883966)

[2.2 Roles 4](#_Toc232883967)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232883968)

[2.3.1 Download template file 5](#_Toc232883969)

[2.4 Business Conditions 5](#_Toc232883970)

[3 Overview Table 6](#_Toc232883971)

[4 Test Procedures 8](#_Toc232883972)

[4.1 Mass Load 8](#_Toc232883973)

[4.1.1 Import Source Data and Create Consolidation Process – Mass Load 8](#_Toc232883974)

[4.1.2 Validation 9](#_Toc232883975)

[4.1.3 Activation 10](#_Toc232883976)

[4.1.4 Manage Consolidation Process – Mass Load 11](#_Toc232883977)

[4.2 Mass Maintenance 11](#_Toc232883978)

[4.2.1 Create Process 11](#_Toc232883979)

[4.2.2 Record Selection 12](#_Toc232883980)

[4.2.3 Editing 13](#_Toc232883981)

[4.2.4 Remove Unchanged Data 14](#_Toc232883982)

[4.2.5 Validation 15](#_Toc232883983)

[4.2.6 Activation 15](#_Toc232883984)

[4.2.7 Track Changes 16](#_Toc232883985)

[4.2.8 Export Active Data (Optional) 17](#_Toc232883986)

[4.3 Remediation 19](#_Toc232883987)

[4.3.1 Start Remediation Process 19](#_Toc232883988)

[4.3.2 Selection 20](#_Toc232883989)

[4.3.3 Validation 20](#_Toc232883990)

[4.3.4 Activation 21](#_Toc232883991)

## Purpose

Overview

This scope item provides capabilities to load, update, validate, remediate, and export multiple Product Master data records simultaneously within the SAP S/4HANA Cloud Public Edition system.

The scope item supports both the classic applications and the new cloud-ready applications with the same business processes and capabilities. Users can perform mass load, mass maintenance, export, and remediation activities using either application framework.

To load records, users import product data from files. The system validates and activates the data before it becomes available for business processes.

To update records, users define the fields and records to be changed. The system validates the changes, provides statistics for the updated data, and activates the records for productive use.

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
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Products / Product Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

Use your own master data to go through the test procedure. It is necessary to load a file into the system. Check whether such a file can be provided. It is also possible to start the app Import Master Data and choose Download File Template to use the template to create your own file.

#### Download template file

This step is necessary to get a template file for procedure "Import Source Data". These template files contain template data and can be replaced by your own data.

Procedure

Run step 1 + 2 from procedure [Import Source Data and Create Consolidation Process – Mass Load](#unique_7) [page ] 8 and choose the link Download File Templates. Select Example Files to download a compressed file with example files to be used for uploading source data. Use one of these files (for example, MATERIAL.xlsx) for uploading or use them as a template for your own data. Ensure that for all rows the field Source_ID is filled with data.

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

This scope item consists of several process steps provided in the following table:

Mass Load

| Process Step | Business Role | Transaction / App | Expected Results |
| --- | --- | --- | --- |
| [Import Source Data and Create Consolidation Process – Mass Load](#unique_7) [page ] 8 | Master Data Specialist - Product Data | SAP Fiori: Import Master Data - Products (F8545) | Source Data loaded into source table. The app opens and asks for Process details. |
| [Validation](#unique_10) [page ] 9 | Master Data Specialist - Product Data | SAP Fiori: Import Master Data - Products (F8545) | Check the result to determine whether records can be activated in the system (based on system customizing) |
| [Activation](#unique_11) [page ] 10 | Master Data Specialist - Product Data | SAP Fiori: Import Master Data - Products (F8545) | Master data has been updated |
| [Manage Consolidation Process – Mass Load](#unique_12) [page ] 11 | Master Data Specialist - Product Data | SAP Fiori: Manage Consolidation Processes - Products (F8544) | Created process status can be seen or the process can be deleted. |

Mass Maintenance

| Process Step | Business Role | Transaction / App | Expected Results |
| --- | --- | --- | --- |
| [Create Process](#unique_13) [page ] 11 | Master Data Specialist - Product Data | SAP Fiori: Manage Mass Maintenance - Products (F9335) | Scope with all fields is defined that is changed. |
| [Record Selection](#unique_14) [page ] 12 | Master Data Specialist - Product Data | SAP Fiori: Manage Mass Maintenance - Products (F9335) | Records that can be changed are available |
| [Editing](#unique_15) [page ] 13 | Master Data Specialist - Product Data | SAP Fiori: Manage Mass Maintenance - Products (F9335) | Changes have been applied and are ready for validation |
| [Validation](#unique_10) [page ] 9 | Master Data Specialist - Product Data | SAP Fiori: Manage Mass Maintenance - Products (F9335) | Check the result to determine whether records can be activated in the system (based on system customizing) |
| [Activation](#unique_11) [page ] 10 | Master Data Specialist - Product Data | SAP Fiori: Manage Mass Maintenance - Products (F9335) | Master data has been updated |
| [Export Active Data (Optional)](#unique_16) [page ] 17 | Master Data Specialist - Product Data | SAP Fiori: Export Master Data - Products (F8465) | Active Data gets downloaded into Excel file. |
| [Track Changes](#unique_17) [page ] 16 | Master Data Specialist - Product Data | SAP Fiori: Track Changes - Products (F8469) | Track your changes made during the Mass Maintenance process. |

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

Import Source Data is required to upload data into the source tables before you can start a consolidation process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Master Data Specialist - Product Data. | The SAP Fiori Launchpad displays. |  |
| 2 | Access App | Open app Import Master Data - Products (F8545) | The Import Master Data - Products screen displays. |  |
| 3 | Create Data Import | Choose Create to create a new import.Source System: Input any source system name. For example: SOURCE01Data Package: Enter the required data package name.Choose ‘Upload’ to select a file for upload. You can use the example file from [Download template file](#unique_6) [page ] 5.Choose Create.Optional: You can import without source system to prevent key mapping generation. Preferred for mass creation use case. | Data is imported and the status of the imported data can be seen.If you get an error, change the value in the Source System field. This error means that someone else has already imported the same data using the same source system. |  |
| 4 | Create Consolidation Process | Choose Create Process on top right corner after importing the source data. | Create Process dialog appears. |  |
| 5 | Enter Description | Enter process description if necessary. Check the process template. Use SAP: Mass Creation Product Data.Choose Create. | Consolidation process page appears. |  |

#### Validation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

Validation provides information on whether the data can be activated. The checks are done based on the system settings. Erroneous data cannot be activated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Start Validation | Choose Start to start the validation. | The system starts the validation and shows a result screen when finished. |  |
| 2 | Check Errors and Warnings | Choose Errors and Warnings under Step Messages to show details. | Message texts are shown. |  |
| 3 | Show Records | Choose Show Results to navigate through the list of records. | The system shows a list with records. |  |
| 4 | Check the result | Navigate through all related tables of a record using the tab bar.After finishing the review, choose Back. | List of all relevant tables appears. |  |

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
| 2 | Check Errors and Warnings (optional) | Choose Errors and Warnings under Step Messages to show details. | Message texts are shown. |  |

#### Manage Consolidation Process – Mass Load

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

You can list all processes in one overview.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Product Data. | The SAP Fiori Launchpad displays. |  |
| 2 | Access App | Open app Manage Consolidation Processes - Products (F8544). | The Manage Consolidation Process - Products screen displays. |  |
| 3 | Processes | Check for the status of all the consolidation process you created. Check parameters like Data Source, Created By, Created On, Records , and so on. | Status can be seen. |  |

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

Scope definition is the first step in mass maintenance to define the fields that to be changed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Master Data Specialist - Product Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Mass Maintenance - Products (F9335). | The Manage Mass Maintenance - Products screen displays. |  |
| 3 | Create Process | Choose Create to create a new mass maintenance process. Enter a description if necessary.Import of records is optional and you can use the file which you exported using the [Export Active Data (Optional)](#unique_16) [page ] 17 app. |  |  |

#### Record Selection

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In Record Selection, the records that is required to be changed can be selected by different select criteria.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Define Selection Criteria | Define select types and field values to find the range of records to be changed. You must use only criteria, which finds the existing products in the system.Choose Start to create the process | List of criteria |  |

#### Editing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

This process step will provide the list of potential records to be changed and the user can define the new field values.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Navigate to Mass Edit UI | Choose Edit Records to start with editing. | The system shows the number of entries in the relevant tables. |  |
| 2 | Select table for the changes | Select the relevant table from the tab bar. | The system shows the current values of the record in this table. |  |
| 3 | Select records for mass change | Select some or of the records to change the same field values by selecting the checklist on the left side of the table and choose Mass Edit - Selected Items. If you want to edit all the records in respective table, choose Mass Edit - All Items | Records are selected. Mass Edit dialog opens. |  |
| 4 | Mass Change of values | For the fields you want to change, choose one of the options from dropdown menu <Keep Values>, <Enter New Value> or <Clear Values>. In case of ‘New Value’, enter the target value. Choose Save to apply the changes. | Applied field values appear in the table. |  |
| 5 | Single changes of values | Choose Edit and directly enter the new field values for each field. Choose Save to apply the changes. | Field values applied immediately. |  |
| 6 | Check number of changes | Choose Back.The system checks the number of changed rows. | Bar Chart with changes appears. |  |

#### Remove Unchanged Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In the process step ‘Remove Unchanged Data’ the records which have not been changed in the previous step will be removed from the process to improve performance during subsequent validation and activation steps. This process step will be executed automatically and does not require any user interaction.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Start Remove Unchanged Data | Choose Continue (on the bottom of the screen) to start remove unchanged data validation. | System executes the process step and continues automatically with validation. |  |

#### Validation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

Validation provides information on whether the data can be activated. The checks are done based on the system settings. Erroneous data cannot be activated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| # | Start Validation | Choose Start to start the validation. | The system starts the validation and shows a result screen when finished. |  |
| # | Check Errors and Warnings | Choose Errors and Warnings under Step Messages to show details. | Message texts are shown. |  |
| # | Show Records | Choose Show Results to navigate through the list of records. | The system shows a list with records. |  |
| # | Check the result | Navigate through all related tables of a record using the tab bar.After finishing the review, choose Back. | List of all relevant tables appears. |  |

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
| # | Start Activation | Choose Continue (at the bottom of the screen) to start the activation. | The system starts the activation and shows a result screen when finished. |  |
| # | Check Errors and Warnings (optional) | Choose Errors and Warnings under Step Messages to show details. | Message texts are shown. |  |

#### Track Changes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

Track your changes made during the Mass Maintenance process. You can view the list of changes only if you have made the changes during the Mass Maintenance process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access App | Go back to the home page of Fiori Launchpad. Open Track Changes - Products (F8469). | The Track Mass Changes - Products screen displays. |  |
| 2 | Filter Inputs | Enter your process Id and choose Go | You must be able to see the list of changes made during the mass maintenance process |  |

#### Export Active Data (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

Active data can be downloaded into a spreadsheet file before importing it. Exported file can be used in Mass Maintenance.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Master Data Specialist - Product Data. | The SAP Fiori Launchpad displays. |  |
| 2 | Access App | Open Export Master Data - Products (F8465). | The Export Master Data - Products screen displays. |  |
| 3 | Define Scope | Select one or more fields from different tables by using F4 help or Type Ahead functionality and then choose Ok. Or do the following step by marking the Radio button to choose all the fields from all tables. | The selected attributes appears under Fields.Use X for removal of the fields if needed. |  |
| 4 | Select Attributes | Mark the checkbox Select all fields from all tables. |  |  |
| 5 | Select Products | Select the Products that you created. Try with different attributes using Include or Exclude functionality. |  |  |
| 6 | Use selection filter | Optional Step - Select the checkbox, Use selection criteria as filter to export the records which are defined in the selection criteria. For example, when your Product has several Plant data, and you want to export the Product of a specific Plant then use this checkbox. Provided you have defined the Plant as your selection criteria. This checkbox works for all the attributes specific to Products. |  |  |
| 7 | Choose Export | Export can be made as either Office Open XML (*.xlsx) or a compressed CSV (*.zip).After all the selections are made, choose Export on bottom right. | Confirmation popup appears saying how many products will be exported | Preferred to exporting it as Zip when huge data is involved |
| 8 | Save File | Choose Export on the Confirmation Dialog Box. | Information popup should appear saying File is being Generated. Choose Ok and save the file to your local. |  |
| 9 | Verify and Make changes in the file. | Open the file and verify the data and make some changes.Change some attributes in the Excel file.Save your changes. | Selected products with the tables and attributes defined in scope are exported.Necessary key fields are available. |  |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as Master Data Specialist - Product Data. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open the app Manage Remediation Processes (F8327). | The Manage Remediation Processes (F8327) app opens. |  |
| 3 | Create Process | Choose Create to create a new process. Enter a description if necessary. |  |  |
| 4 | Select Process Template | Enter a description for the process.Select the process template SAP: Validate and Remediate Product | The process template SAP: Validate and Remediate Product is offered and selected for the process. |  |

#### Selection

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Start the remediation process with the selection of your products.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Define Selection Criteria | Select the Products to be validated by entering selection criteria.Define select types and field values to find the range of records to be changed. You must use only criteria that find the existing products in the system. |  |  |
| 2 | Start | Choose Start to create the process. | Data Quality Remediation page is displayed. |  |

#### Validation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

Validation provides information on whether the data can be activated. The checks are done based on the system settings. Erroneous data cannot be activated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| # | Start Validation | Choose Start to start the validation. | The system starts the validation and shows a result screen when finished. |  |
| # | Check Errors and Warnings | Choose Errors and Warnings under Step Messages to show details. | Message texts are shown. |  |
| # | Show Records | Choose Show Results to navigate through the list of records. | The system shows a list with records. |  |
| # | Check the result | Navigate through all related tables of a record using the tab bar.After finishing the review, choose Back. | List of all relevant tables appears. |  |

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
| # | Start Activation | Choose Continue (at the bottom of the screen) to start the activation. | The system starts the activation and shows a result screen when finished. |  |
| # | Check Errors and Warnings (optional) | Choose Errors and Warnings under Step Messages to show details. | Message texts are shown. |  |

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
- see-also :: [[02-business-partner-and-product-master-data/test-script-master-data-consolidation-for-product-1n1-742]]
- see-also :: [[01-solution-foundation-and-platform/test-script-data-migration-to-sap-s-4hana-from-sap-bh3-1268]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1RM_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 32,754 chars in the whole document
