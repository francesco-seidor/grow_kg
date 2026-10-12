---
id: 02-business-partner-and-product-master-data/test-script-central-governance-for-product-1n5-sap-s-4hana-cloud-publi
title: "Test Script: Central Governance for Product (1N5) - SAP S/4HANA Cloud Public Edition (1N5_S4CLD2608_BPD_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 1N5: product master data mass processing and central governance create/change/approve flows."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/central-governance-products-business-partners]
aliases: [1N5_S4CLD2608_BPD_EN_XX]
keywords: [Central Governance for Products and Business Partners, product governance, product master data, mass processing, governance process approval, create product, change product, test scripts, business roles, feature activation]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1N5_S4CLD2608_BPD_EN_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-744
topic: 02-business-partner-and-product-master-data/central-governance-products-business-partners
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Central Governance for Product (1N5) - SAP S/4HANA Cloud Public Edition (1N5_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1N5_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Central Governance for Products and Business Partners** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Central Governance for Product (1N5) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232846689)

[2 Prerequisites 4](#_Toc232846690)

[2.1 System Access 4](#_Toc232846691)

[2.2 Roles 4](#_Toc232846692)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232846693)

[2.4 Business Conditions 5](#_Toc232846694)

[3 Overview Table 6](#_Toc232846695)

[4 Test Procedures 8](#_Toc232846696)

[4.1 Manage Governance Processes Products 8](#_Toc232846697)

[4.1.1 Create Process 8](#_Toc232846698)

[4.1.2 Editing 9](#_Toc232846699)

[4.1.3 Remove Unchanged Data 10](#_Toc232846700)

[4.1.4 Validation 10](#_Toc232846701)

[4.1.5 Activation 11](#_Toc232846702)

[4.1.6 Track Mass Changes 12](#_Toc232846703)

[4.2 Manage Governance Processes with Automation 13](#_Toc232846704)

[4.2.1 Check Derivation Step in Process UI 13](#_Toc232846705)

[4.3 Manage Products Central Governance 14](#_Toc232846706)

[4.3.1 Create New Product Using Governance Process 14](#_Toc232846707)

[4.3.2 Submit Governance Process 16](#_Toc232846708)

[4.3.3 [Optional] Validate and Approve Governance Process 17](#_Toc232846709)

[4.3.4 [Optional] Reject Governance Process 18](#_Toc232846710)

[4.3.5 [Optional] Send Governance Process for Revision 19](#_Toc232846711)

[4.4 Manage Products Central Governance 20](#_Toc232846712)

[4.4.1 Change Active Product Using Governance Process 20](#_Toc232846713)

[4.4.2 Submit Governance Process 22](#_Toc232846714)

[4.4.3 [Optional] Validate and Approve Governance Process 22](#_Toc232846715)

## Purpose

Overview

This scope item provides comprehensive capabilities for managing product master data within the SAP S/4HANA Cloud Public Edition system. It supports both the classic mass processing approach and the new cloud-ready governance process for products.

In classic mode, users can perform mass processing of product master data, enabling efficient updates across multiple product records simultaneously. To update records, select the fields and records to change. Once you enter your changes, the system provides statistics on the changed fields and validates the data. You check the validated data and activate it for use in business transactions. Classification is supported. You can also download active data for mass processing.

In cloud-ready mode, dedicated governance applications support streamlined single requests, mass requests, and inbound processing scenarios for product master data. Users can create, change, validate, and activate product records using simplified cloud-ready governance flows.

To use the cloud-ready Product Governance applications, you must activate the MDC_PRODUCT_GOVERNANCE feature toggle.

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

Use your own master data to go through the test procedure.

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

The scope item consists of several process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the home page only contains the apps necessary for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the home page using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the home page and include the hidden apps, navigate to your user profile and choose App Finder. |

Table 1: Manage Governance Processes Products

|  |  |  |  |
| --- | --- | --- | --- |
| Choose the appropriate entity: Process Step, Report, or Item | Business Role | App/Transaction | Expected Results |
| [Create Process](#unique_8) [page ] 8 | Master Data Specialist - Product Data | Manage Mass Processes - Products (F8321) | Process can be created with records that can be changed. |
| [Editing](#unique_9) [page ] 9 | Master Data Specialist - Product Data | Manage Mass Processes - Products (F8321) | Changes have been applied and are ready for validation. |
| [Remove Unchanged Data](#unique_10) [page ] 10 | Master Data Specialist - Product Data | Manage Mass Processes - Products (F8321) | Unchanged records are removed from the process. |
| [Validation](#unique_11) [page ] 10 | Master Data Specialist - Product Data | Manage Mass Processes - Products (F8321) | Check the result to determine whether records can be activated in the system (based on system customizing) |
| [Activation](#unique_12) [page ] 11 | Master Data Specialist - Product Data | Manage Mass Processes - Products (F8321) | Success message tells that Master data has been updated |
| [Track Mass Changes](#unique_13) [page ] 12 | Master Data Specialist - Product Data | Manage Mass Processes - Products (F8321) | Track your changes made during the Mass Processing Process. |

Table 2: Manage Governance Processes with Automation Products

|  |  |  |  |
| --- | --- | --- | --- |
| Choose the appropriate entity: Process Step, Report, or Item | Business Role | App/Transaction | Expected Results |
| [Check Derivation Step in Process UI](#unique_14) [page ] 13 | Master Data Specialist - Product Data | Manage Mass Processes - Products (F8321) | Process with the Derivation step is executed automatically when the related data is processed. |

Table 3: Manage Products Central Governance – Create Product

|  |  |  |  |
| --- | --- | --- | --- |
| Choose the appropriate entity: Process Step, Report, or Item | Business Role | App/Transaction | Expected Results |
| [Create New Product Using Governance Process](#unique_15) [page ] 14 | Master Data Specialist - Product Data | Manage Governance Processes - Products (F8466) | Process can be created and product data can be entered. |
| [Submit Governance Process](#unique_16) [page ] 16 | Master Data Specialist - Product Data | Manage Governance Processes - Products (F8466) | Process can be submitted for Approval. |
| [[Optional] Validate and Approve Governance Process](#unique_17) [page ] 17 | Master Data Specialist - Product Data | Manage Governance Processes - Products (F8466) | Process can be validated and approved. |

Table 4: Manage Products Central Governance – Change Product

|  |  |  |  |
| --- | --- | --- | --- |
| Choose the appropriate entity: Process Step, Report, or Item | Business Role | App/Transaction | Expected Results |
| [Change Active Product Using Governance Process](#unique_18) [page ] 20 | Master Data Specialist - Product Data | Manage Governance Processes - Products (F8466) | Process can be created and product data can be entered. |
| [Submit Governance Process](#unique_19) [page ] 22 | Master Data Specialist - Product Data | Manage Governance Processes - Products (F8466) | Process can be submitted for Approval. |
| [[Optional] Validate and Approve Governance Process](#unique_20) [page ] 22 | Master Data Specialist - Product Data | Manage Governance Processes - Products (F8466) | Process can be validated and approved. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Manage Governance Processes Products

#### Create Process

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Scope definition is the first step in mass processing to select the Products to be changed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data . | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Manage Governance Processes - Products (F8466). | The Manage Governance Processes - Products (F8466) app opens. |  |
| 3 | Create Process | Choose Create and enter a description. Choose your process template or use the default template SAP: Mass Processing Product.Choose start process with Selection.Under Selection, enter the product number.Choose Check Selection and verify the number of records selected for mass processing.Choose Start. | System saves the data and creates a mass process.The Edit step is highlighted in green. The KPI is identified as unchanged records for all the tables |  |

#### Editing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step will provide the list of potential records to be changed and the user can define the new field values.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Select table for the changes | Select the relevant table in the tab bar. | The current values of the record in this table are shown. |  |
| 2 | Select records for mass change | Select the records that you want to edit.Choose Mass Edit, then choose Selected Items. | Records are selected and the Mass Edit dialog box opens. |  |
| 3 | Mass Change of values | For each field, you can choose to enter a new value, keep the same value or clear the values.Use Enter New Value and enter new values.Choose Save. | The new field values are applied. The Details column shows the number of completed changes as a link.Opening the link displays the old and new value for the field. |  |
| 4 | Single changes of values | To edit a single record, choose Edit the header and type in directly the new field values individually for each field.Choose Save. | The new field values are applied immediately.The Details column shows the number of completed changes as a link.Opening the link displays the old and new value for the field. |  |
| 5 | Check number of changes | Choose Back, the system verifies the number of changed rows. | The bar chart in the results section shows the number of changed rows. |  |

#### Remove Unchanged Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step will remove unchanged records from the process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Start Remove Unchanged Data | Press Continue (on the bottom of the screen) to start the step Remove Unchanged Data. | Unchanged records will be removed from the process. Only the changed records will be processed further. |  |

#### Validation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Validation provides information, if the data can be activated data. The checks are done based on the system settings. Erroneous data cannot be activated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Start Validation | Validation step will be executed since there is no check point between Remove Unchanged Data and Validation step. | System starts the validation. |  |
| 2 | Check Errors and Warnings | The Validation step will fail in case of any errors.Click on the numbers Errors and Warnings to show details. | Message texts are shown. |  |
| 3 | Show Records | Click on Show Result to navigate to the list of the records. | System shows a list with records. |  |
| 4 | Check the result | Navigate through all related tables of a record using the tab bar. Correct the errors using single record level edit or Mass Edit.After finishing the review click on Back icon.Note down the process ID. | Lists of all relevant tables will be shown. |  |

#### Activation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Activation step will trigger the activation of the data into the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Start Activation | Press Continue (on the bottom of the screen) to start the activation. | System starts the activation and shows a result screen when finished. |  |
| 2 | Check Errors and Warnings (optional) | When warnings or errors occurred, the system provides this information. Click the numbers Errors and Warnings to show details. | Message texts are shown. |  |

#### Track Mass Changes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Track your changes made during the Mass Processing process. You can view the list of changes, only if, you have made any changes during the Mass Processing process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access App | Go back to the Homepage of Fiori Launchpad. Open Track Changes - Products (F8469) | The Track Changes (Products) screen displays. |  |
| 2 | Filter Inputs | Enter the process ID you noted down in Section [Activation](#unique_12) [page ] 11 Procedure step 4. Choose Go. | You should be able to see the list of changes made by you during the Mass Processing Process. If there are no changes available then probably you made no changes during the Mass Processing process. |  |

### Manage Governance Processes with Automation

#### Check Derivation Step in Process UI

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Verify the process template for mass processing automation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad opens. |  |
| 2 | Access App | Open Manage Governance Processes - Products (F8466) | The Manage Mass Processes - Products screen displays. |  |
| 3 | Create Process | Create a new process, enter the description, and select an available process template for automation, for example, SAP: Mass Processing Product Automated.Choose start process with Selection.Under Selection, enter the product number.Choose Check Selection and verify the number of records selected for mass processing.Choose Start. | The system saves the data and creates a mass process. |  |
| 4 | Check | In the process UI, there should be below steps displayed:EditDerivationRemove Unchanged DataValidationActivation | The Derivation step is included in the process UI. |  |

### Manage Products Central Governance

#### Create New Product Using Governance Process

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

As a requester you can create a new governance process to create a new product.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data for Product Data. | The SAP Fiori launchpad opens. |  |
| 2 | Access App | Open Manage Products - Central Governance (F8467) | The Manage Products - Central Governance (F8467) app opens. |  |
| 3 | Create Single Processing for Product | Choose Create, then fill out at least the mandatory fields (Product Description, Product Type & Industry Sector).Choose Create. | The Quick Create dialog box appears.The process template SAP: Single Processing Product is filled in. The data that you entered in the Quick Create dialog box is visible in the overview page. |  |
| 4 | Enter Process Information | Choose Create New Process.Enter a description for the process.Choose the Due Date. | The process information is filled in. |  |
| 5 | Enter General Information – Basic Data | Click the drop-down button next to General Information and choose “Basic Data”. Enter some data for example External Product Group, Old Product Number and Authorization Group. Choose Show More to display additional fields. | The basic data is filled in. |  |
| 6 | Enter General Information – Product Description | Click the drop-down button next to General Information and choose Product Description.Click Create in the Product Descriptions table and use the value help to add additional languages. The Description column can be maintained manually. | The product description is filled in. |  |
| 7 | Enter General Information – Base Unit of Measure | Click the drop-down button next to General Information and choose Base Unit of Measure.Enter the Base Unit of Measure and optionally maintain the Net Weight. | Base Unit of Measure is filled in.Net Weight can be entered. |  |
| 8 | Enter General Information – Units of Measure | Click the drop-down button next to General Information and choose Units of Measure.Click on the Base Unit of Measure entry, you will be automatically navigated to the Subobject page.Enter some data on the Subobject Page.For example, you can also maintain new GTINs using the Create button next to the GTIN table.When the GTIN is entered manually, the GTIN Category is automatically derivedfrom the entered GTIN.Choose Apply.Use the Create button to create an Alternative Unit of Measure. You will be automatically navigated to the Subobject page. Enter at least the mandatory data (Unit of Measure).Choose Apply. | Base Unit of Measure cannot be changed.The Subobject Pages opens and data from the Unit of Measure table matches the data on the Subobject Page.Alternative Unit of Measure can be created. |  |
| 9 | Enter Product Compliance Data | In the Product Compliance table use the drop-down button for Product Compliance to select a value. | Product Compliance can be created. |  |
| 10 | Enter Configuration Data | In the Configuration table maintain the fields. Use the value help and select or deselect the checkbox as needed. | Configuration data can be created. |  |
| 11 | Enter Purchasing Data | In the Purchasing table maintain the fields, use the value helps. | Purchasing data can be created. |  |
| 12 | Enter Sales Data | In the Sales table maintain the fields, use the value helps. | Sales data can be created. |  |
| 13 | Enter Storage Data | In the Storage table maintain the fields, use the value helps. | Storage data can be created. |  |
| 14 | Enter Warehouse Management Data | In the Warehouse Management table maintain the fields. . Use the value help and select or deselect the checkboxes as needed. | Warehouse Management data can be created. |  |
| 15 | Save Your Process | Choose Save.In the Changes table check your performed changes. | A confirmation message stating Object Created is displayed.The Process ID is displayed as a link under the Process Information section.In case of a validation error, the error will be displayed in a popup window.Page is switched to display mode and new tab Changes will be available. |  |

#### Submit Governance Process

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Submit the governance process for approval.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Submit Single Request | Choose Submit. | A confirmation message with the text Process XYZ started displays. Where XYZ is the ID of your governance process. | If a workflow is configured in the Configure Process Template app, the workflow for this governance process will be triggered automatically after it is submitted. |
| 2 | Check Process KPI | On the Process Information tab, choose the highlighted Process ID. | The Single Processing view for this process opens.The process status is Stopped for Review (Edit).The product data is displayed as bars and categorized as Inserted Rows.The Delete and Continue buttons are not visible. | The process cannot be continued or deleted using the process UI because it is controlled by a workflow. |

#### [Optional] Validate and Approve Governance Process

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The approver validates the product data and approves the request.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Check Workflow Inbox | Navigate to the home page of the SAP Fiori launchpad and choose My Inbox. | A task named Approve Master Data Request XYZ is displayed in the All Tasks list. XYZ stands for the ID of your governance process. |  |
| 2 | Check Product Data | Choose the task and verify the product data.Navigate between the different tabs to view the data entered in each table, for example address or bank accounts. | The data entered during the [Create New Product Using Governance Process](#unique_15) [page ] 14 step is displayed.If no data was entered for certain tables, they are not displayed.The data is not editable. |  |
| 3 | Approve Request | Choose Approve. | A confirmation message stating Task processed successfully is displayed. The task is removed from the task list. |  |
| 4 | Check Governance Process | Navigate to the Manage Governance Processes - Products (F8466) app and check your Single Processing. Verify the KPI chart of the [Activation](#unique_12) [page ] 11 step. | The process status is set to Completed.One new single record is activated successfully.The KPI chart color is set to green. |  |
| 5 | Check Activated Product Data | Navigate to the Manage Products - Central Governance (F8467) app and search for your product using the search criteria in the filter bar.Open the product details and check the data. | The product record is displayed.The data entered during the [Create New Product Using Governance Process](#unique_15) [page ] 14 step is displayed. | The single request process is completed and the product data is activated. |

#### [Optional] Reject Governance Process

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The approver validates the product data and rejects the request.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Check Workflow Inbox | Navigate back to the Product Governance launchpad and choose My Inbox. | A task named Approve Master Data Request XYZ is displayed in the All Tasks list. XYZ stands for the ID of your governance process. |  |
| 2 | Reject Request | Choose Reject. | A confirmation message with the text Task processed successfully is displayed. The task is removed from the task list. |  |
| 3 | Check Governance Process | Navigate to the Manage Governance Processes - Products (F8466) app and check your Single Processing. | The process status is set to Deleted.The process has stopped at the Edit step. A confirmation message with the text The process was deleted is displayed. |  |

#### [Optional] Send Governance Process for Revision

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The approver validates the product data and sends the request for revision.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Check Workflow Inbox | Navigate back to the Product Governance launchpad and choose My Inbox. | A task named Approve Master Data Request XYZ is displayed in the All Tasks list. XYZ stands for the ID of your governance process. |  |
| 2 | Send Request for Revision | Choose Send for Revision.You may need to enter a reason in the Quick Warning dialog box. | A confirmation message with the text Task processed successfully is displayed. The task is removed from the task list. |  |
| 3 | Check Workflow Inbox | Choose Refresh in the workflow task list and scroll up. | A new task named Rework Master Data Request XYZ is displayed in the All Tasks list. XYZ stands for the ID of your governance process. |  |
| 4 | Revise Request | Choose the task from the task list, then choose Edit and change some of the product data.Change the Product Description. Save your changes.Choose Send for Approval and repeat the steps from [[Optional] Validate and Approve Governance Process](#unique_17) [page ] 17 | The request opens in read-only mode.The Edit, Send for Approval, and Withdraw Request buttons are visible.The UI changes to edit mode from the workflow inbox. All available data tabs are enabled for editing. Adding or removing attachments is also enabled. |  |

### Manage Products Central Governance

#### Change Active Product Using Governance Process

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

As a requester you can create a new governance process to change a new product.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad opens. |  |
| 2 | Access App | Open Manage Products - Central Governance (F8467) | The Manage Products - Central Governance (F8467) app opens. |  |
| 3 | Search for Product | Search for your active product using the filters. | The search results are displayed. |  |
| 4 | Navigate to Product Details | Choose an entry from the search result list to open the product details. | The product record opens. |  |
| 5 | Create New Governance Process | Choose Edit and provide the process information details | The UI changes to edit mode and process information can be entered.The Process Information tab displays.The process template SAP: Single Processing Product is selected by default. |  |
| 6 | Change Product Data | Change values for some of the fields and delete values from other fields. For example, delete and replace some of the values in the General Information table.Change the Product Compliance data.Delete some of the Standard Communication details and replace them with new details.Delete or change existing characteristic values in the Classification data.Change or Delete existing Configuration data.Change or Delete existing Purchasing data.Change or Delete existing Storage data.Change or Delete existing Warehouse Management data. |  |  |
| 7 | Save Your Process | Choose Save.Note down the process ID. | A confirmation message with the text Request Created is displayed.The Process ID is displayed as a link under the Process Information section.All changes are displayed under the Changes tab. |  |

#### Submit Governance Process

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Submit the governance process for approval.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Submit Single Request | Choose Submit. | A confirmation message with the text Process XYZ started displays. Where XYZ is the ID of your governance process. | If a workflow is configured in the Configure Process Template app, the workflow for this governance process will be triggered automatically after it is submitted. |
| 2 | Check Single Request Process | In the Process Information tab, choose the highlighted Process ID.Check the KPI chart for the Edit step. | The Single Processing view for this process opens.The process status is Stopped for Review (Edit).The product data is displayed as bars and categorized as Changed Rows for the data that you changed.Deleted entries of dependent data such as role or address are categorized as Deleted Rows and added entries are categorized as Inserted Rows. | The process cannot be continued or deleted using the process UI because it is controlled by a workflow. |

#### [Optional] Validate and Approve Governance Process

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The approver validates the product data and approves the request.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Check Workflow Inbox | Navigate back to the Product Governance launchpad and choose My Inbox. | A task named Approve Master Data Request XYZ is displayed in the All Tasks list. XYZ stands for the ID of your governance process. |  |
| 2 | Check Product Data | Choose the task, then choose the Changes tab. Verify all changes.Choose Check. | The data entered during the [Create New Product Using Governance Process](#unique_15) [page ] 14 step is displayed.Changes made during the [Change Active Product Using Governance Process](#unique_18) [page ] 20 step is displayed in the Changes table.If no data was entered for certain tables, they are not displayed.The data is not editable. |  |
| 3 | Approve Request | Choose Approve. | A confirmation message with the text Task processed successfully is displayed. The task is removed from the task list. |  |
| 4 | Check Governance Process | Navigate to the Manage Governance Processes - Products (F8466) app and check your Single Processing. Verify the KPI chart of [Activation](#unique_12) [page ] 11 step.. | The process status is set to Completed.One new single record is activated successfully.The KPI chart color is set to green. |  |
| 5 | Check Activated Product Data | Navigate to the Manage Products - Central Governance (F8467) app and search for your product using the search criteria in the filter bar.Open the product details and check the data. | The product record is displayed.The data changed during the [Change Active Product Using Governance Process](#unique_18) [page ] 20 step is displayed. |  |

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

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: App naming differs inside the document: the Overview Table lists Manage Mass Processes - Products (F8321) for the mass-processing steps, but the Create Process and Derivation procedures instruct opening Manage Governance Processes - Products (F8466).

## Connections
- part-of :: [[_cluster]]
- related-to :: [[02-business-partner-and-product-master-data/test-script-central-governance-for-business-partner-1n7-sap-s-4hana-cl]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1N5_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 39,891 chars in the whole document
